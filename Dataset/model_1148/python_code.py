from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class HistoryTypeDatatype(Enum):
    shallow = "shallow"
    deep = "deep"
class AssignTypeDatatype(Enum):
    lastchild = "lastchild"
    previoussibling = "previoussibling"
    nextsibling = "nextsibling"
    replace = "replace"
    delete = "delete"
    addattribute = "addattribute"
    replacechildren = "replacechildren"
    firstchild = "firstchild"
class TransitionTypeDatatype(Enum):
    internal = "internal"
    external = "external"
class BooleanDatatype(Enum):
    true = "true"
    false = "false"
class ExmodeDatatype(Enum):
    lax = "lax"
    strict = "strict"
class BindingDatatype(Enum):
    early = "early"
    late = "late"


############################################
# Definition of Classes
############################################

class scxml_ScxmlScxmlType:

    def __init__(self, scxmlScxmlMix: str, any: str, binding: str, datamodel1: str, exmode: str, initial: str, name: str, version: str, anyAttribute: str, scxml_ScxmlScxmlType: "scxml_DocumentRoot" = None, scxml_ScxmlScxmlType288: set["scxml_ScxmlStateType"] = None, scxml_ScxmlScxmlType291: set["scxml_ScxmlParallelType"] = None, scxml_ScxmlScxmlType294: set["scxml_ScxmlFinalType"] = None, scxml_ScxmlScxmlType297: set["scxml_ScxmlDatamodelType"] = None, scxml_ScxmlScxmlType300: set["scxml_ScxmlScriptType"] = None):
        self.scxmlScxmlMix = scxmlScxmlMix
        self.any = any
        self.binding = binding
        self.datamodel1 = datamodel1
        self.exmode = exmode
        self.initial = initial
        self.name = name
        self.version = version
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlScxmlType = scxml_ScxmlScxmlType
        self.scxml_ScxmlScxmlType288 = scxml_ScxmlScxmlType288 if scxml_ScxmlScxmlType288 is not None else set()
        self.scxml_ScxmlScxmlType291 = scxml_ScxmlScxmlType291 if scxml_ScxmlScxmlType291 is not None else set()
        self.scxml_ScxmlScxmlType294 = scxml_ScxmlScxmlType294 if scxml_ScxmlScxmlType294 is not None else set()
        self.scxml_ScxmlScxmlType297 = scxml_ScxmlScxmlType297 if scxml_ScxmlScxmlType297 is not None else set()
        self.scxml_ScxmlScxmlType300 = scxml_ScxmlScxmlType300 if scxml_ScxmlScxmlType300 is not None else set()
        
    @property
    def scxmlScxmlMix(self) -> str:
        return self.__scxmlScxmlMix

    @scxmlScxmlMix.setter
    def scxmlScxmlMix(self, scxmlScxmlMix: str):
        self.__scxmlScxmlMix = scxmlScxmlMix

    @property
    def datamodel1(self) -> str:
        return self.__datamodel1

    @datamodel1.setter
    def datamodel1(self, datamodel1: str):
        self.__datamodel1 = datamodel1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def binding(self) -> str:
        return self.__binding

    @binding.setter
    def binding(self, binding: str):
        self.__binding = binding

    @property
    def exmode(self) -> str:
        return self.__exmode

    @exmode.setter
    def exmode(self, exmode: str):
        self.__exmode = exmode

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlScxmlType294(self):
        return self.__scxml_ScxmlScxmlType294

    @scxml_ScxmlScxmlType294.setter
    def scxml_ScxmlScxmlType294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType294", None)
        self.__scxml_ScxmlScxmlType294 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlFinalType295"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType295", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlFinalType295", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlFinalType295"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType295", None)
                    
                    setattr(item, "scxml_ScxmlFinalType295", self)
                    

    @property
    def scxml_ScxmlScxmlType297(self):
        return self.__scxml_ScxmlScxmlType297

    @scxml_ScxmlScxmlType297.setter
    def scxml_ScxmlScxmlType297(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType297", None)
        self.__scxml_ScxmlScxmlType297 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDatamodelType298"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType298", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDatamodelType298", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDatamodelType298"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType298", None)
                    
                    setattr(item, "scxml_ScxmlDatamodelType298", self)
                    

    @property
    def scxml_ScxmlScxmlType(self):
        return self.__scxml_ScxmlScxmlType

    @scxml_ScxmlScxmlType.setter
    def scxml_ScxmlScxmlType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType", None)
        self.__scxml_ScxmlScxmlType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot49"):
                opp_val = getattr(old_value, "scxml_DocumentRoot49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot49"):
                opp_val = getattr(value, "scxml_DocumentRoot49", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScxmlType288(self):
        return self.__scxml_ScxmlScxmlType288

    @scxml_ScxmlScxmlType288.setter
    def scxml_ScxmlScxmlType288(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType288", None)
        self.__scxml_ScxmlScxmlType288 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlStateType289"):
                    opp_val = getattr(item, "scxml_ScxmlStateType289", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlStateType289", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlStateType289"):
                    opp_val = getattr(item, "scxml_ScxmlStateType289", None)
                    
                    setattr(item, "scxml_ScxmlStateType289", self)
                    

    @property
    def scxml_ScxmlScxmlType291(self):
        return self.__scxml_ScxmlScxmlType291

    @scxml_ScxmlScxmlType291.setter
    def scxml_ScxmlScxmlType291(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType291", None)
        self.__scxml_ScxmlScxmlType291 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParallelType292"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType292", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParallelType292", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParallelType292"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType292", None)
                    
                    setattr(item, "scxml_ScxmlParallelType292", self)
                    

    @property
    def scxml_ScxmlScxmlType300(self):
        return self.__scxml_ScxmlScxmlType300

    @scxml_ScxmlScxmlType300.setter
    def scxml_ScxmlScxmlType300(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScxmlType__scxml_ScxmlScxmlType300", None)
        self.__scxml_ScxmlScxmlType300 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType301"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType301", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType301", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType301"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType301", None)
                    
                    setattr(item, "scxml_ScxmlScriptType301", self)
                    

class scxml_ScxmlScriptType:

    def __init__(self, mixed: str, scxmlExtraContent: str, any: str, src: str, anyAttribute: str, scxml_ScxmlScriptType: "scxml_DocumentRoot" = None, scxml_ScxmlScriptType79: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlScriptType112: "scxml_ScxmlForeachType" = None, scxml_ScxmlScriptType139: "scxml_ScxmlIfType" = None, scxml_ScxmlScriptType166: "scxml_ScxmlIfType" = None, scxml_ScxmlScriptType193: "scxml_ScxmlIfType" = None, scxml_ScxmlScriptType229: "scxml_ScxmlOnentryType" = None, scxml_ScxmlScriptType253: "scxml_ScxmlOnexitType" = None, scxml_ScxmlScriptType301: "scxml_ScxmlScxmlType" = None, scxml_ScxmlScriptType352: "scxml_ScxmlTransitionType" = None):
        self.mixed = mixed
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.src = src
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlScriptType = scxml_ScxmlScriptType
        self.scxml_ScxmlScriptType79 = scxml_ScxmlScriptType79
        self.scxml_ScxmlScriptType112 = scxml_ScxmlScriptType112
        self.scxml_ScxmlScriptType139 = scxml_ScxmlScriptType139
        self.scxml_ScxmlScriptType166 = scxml_ScxmlScriptType166
        self.scxml_ScxmlScriptType193 = scxml_ScxmlScriptType193
        self.scxml_ScxmlScriptType229 = scxml_ScxmlScriptType229
        self.scxml_ScxmlScriptType253 = scxml_ScxmlScriptType253
        self.scxml_ScxmlScriptType301 = scxml_ScxmlScriptType301
        self.scxml_ScxmlScriptType352 = scxml_ScxmlScriptType352
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def scxml_ScxmlScriptType79(self):
        return self.__scxml_ScxmlScriptType79

    @scxml_ScxmlScriptType79.setter
    def scxml_ScxmlScriptType79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType79", None)
        self.__scxml_ScxmlScriptType79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType78"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType78"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType78", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType166(self):
        return self.__scxml_ScxmlScriptType166

    @scxml_ScxmlScriptType166.setter
    def scxml_ScxmlScriptType166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType166", None)
        self.__scxml_ScxmlScriptType166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType165"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType165"):
                opp_val = getattr(value, "scxml_ScxmlIfType165", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType139(self):
        return self.__scxml_ScxmlScriptType139

    @scxml_ScxmlScriptType139.setter
    def scxml_ScxmlScriptType139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType139", None)
        self.__scxml_ScxmlScriptType139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType138"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType138"):
                opp_val = getattr(value, "scxml_ScxmlIfType138", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType253(self):
        return self.__scxml_ScxmlScriptType253

    @scxml_ScxmlScriptType253.setter
    def scxml_ScxmlScriptType253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType253", None)
        self.__scxml_ScxmlScriptType253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType252"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType252"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType252", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType229(self):
        return self.__scxml_ScxmlScriptType229

    @scxml_ScxmlScriptType229.setter
    def scxml_ScxmlScriptType229(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType229", None)
        self.__scxml_ScxmlScriptType229 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType228"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType228", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType228"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType228", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType228", set([self]))
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
            if hasattr(old_value, "scxml_DocumentRoot47"):
                opp_val = getattr(old_value, "scxml_DocumentRoot47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot47"):
                opp_val = getattr(value, "scxml_DocumentRoot47", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType352(self):
        return self.__scxml_ScxmlScriptType352

    @scxml_ScxmlScriptType352.setter
    def scxml_ScxmlScriptType352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType352", None)
        self.__scxml_ScxmlScriptType352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType351"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType351", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType351"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType351", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType351", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType193(self):
        return self.__scxml_ScxmlScriptType193

    @scxml_ScxmlScriptType193.setter
    def scxml_ScxmlScriptType193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType193", None)
        self.__scxml_ScxmlScriptType193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType192"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType192", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType192"):
                opp_val = getattr(value, "scxml_ScxmlIfType192", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType192", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType112(self):
        return self.__scxml_ScxmlScriptType112

    @scxml_ScxmlScriptType112.setter
    def scxml_ScxmlScriptType112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType112", None)
        self.__scxml_ScxmlScriptType112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType111"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType111"):
                opp_val = getattr(value, "scxml_ScxmlForeachType111", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlScriptType301(self):
        return self.__scxml_ScxmlScriptType301

    @scxml_ScxmlScriptType301.setter
    def scxml_ScxmlScriptType301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlScriptType__scxml_ScxmlScriptType301", None)
        self.__scxml_ScxmlScriptType301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType300"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType300", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType300"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType300", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType300", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlTransitionType:

    def __init__(self, scxmlCoreExecutablecontent: str, any: str, cond: str, type: str, anyAttribute: str, event: str, target: str, scxml_ScxmlTransitionType: "scxml_DocumentRoot" = None, scxml_ScxmlTransitionType124: "scxml_ScxmlHistoryType" = None, scxml_ScxmlTransitionType205: "scxml_ScxmlInitialType" = None, scxml_ScxmlTransitionType271: "scxml_ScxmlParallelType" = None, scxml_ScxmlTransitionType316: "scxml_ScxmlStateType" = None, scxml_ScxmlTransitionType339: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlTransitionType345: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlTransitionType348: set["scxml_ScxmlSendType"] = None, scxml_ScxmlTransitionType351: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlTransitionType354: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlTransitionType342: set["scxml_ScxmlIfType"] = None, scxml_ScxmlTransitionType360: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlTransitionType357: set["scxml_ScxmlLogType"] = None):
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.any = any
        self.cond = cond
        self.type = type
        self.anyAttribute = anyAttribute
        self.event = event
        self.target = target
        self.scxml_ScxmlTransitionType = scxml_ScxmlTransitionType
        self.scxml_ScxmlTransitionType124 = scxml_ScxmlTransitionType124
        self.scxml_ScxmlTransitionType205 = scxml_ScxmlTransitionType205
        self.scxml_ScxmlTransitionType271 = scxml_ScxmlTransitionType271
        self.scxml_ScxmlTransitionType316 = scxml_ScxmlTransitionType316
        self.scxml_ScxmlTransitionType339 = scxml_ScxmlTransitionType339 if scxml_ScxmlTransitionType339 is not None else set()
        self.scxml_ScxmlTransitionType345 = scxml_ScxmlTransitionType345 if scxml_ScxmlTransitionType345 is not None else set()
        self.scxml_ScxmlTransitionType348 = scxml_ScxmlTransitionType348 if scxml_ScxmlTransitionType348 is not None else set()
        self.scxml_ScxmlTransitionType351 = scxml_ScxmlTransitionType351 if scxml_ScxmlTransitionType351 is not None else set()
        self.scxml_ScxmlTransitionType354 = scxml_ScxmlTransitionType354 if scxml_ScxmlTransitionType354 is not None else set()
        self.scxml_ScxmlTransitionType342 = scxml_ScxmlTransitionType342 if scxml_ScxmlTransitionType342 is not None else set()
        self.scxml_ScxmlTransitionType360 = scxml_ScxmlTransitionType360 if scxml_ScxmlTransitionType360 is not None else set()
        self.scxml_ScxmlTransitionType357 = scxml_ScxmlTransitionType357 if scxml_ScxmlTransitionType357 is not None else set()
        
    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

    @property
    def scxml_ScxmlTransitionType205(self):
        return self.__scxml_ScxmlTransitionType205

    @scxml_ScxmlTransitionType205.setter
    def scxml_ScxmlTransitionType205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType205", None)
        self.__scxml_ScxmlTransitionType205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlInitialType204"):
                opp_val = getattr(old_value, "scxml_ScxmlInitialType204", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlInitialType204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlInitialType204"):
                opp_val = getattr(value, "scxml_ScxmlInitialType204", None)
                setattr(value, "scxml_ScxmlInitialType204", self)

    @property
    def scxml_ScxmlTransitionType342(self):
        return self.__scxml_ScxmlTransitionType342

    @scxml_ScxmlTransitionType342.setter
    def scxml_ScxmlTransitionType342(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType342", None)
        self.__scxml_ScxmlTransitionType342 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType343"):
                    opp_val = getattr(item, "scxml_ScxmlIfType343", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType343", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType343"):
                    opp_val = getattr(item, "scxml_ScxmlIfType343", None)
                    
                    setattr(item, "scxml_ScxmlIfType343", self)
                    

    @property
    def scxml_ScxmlTransitionType357(self):
        return self.__scxml_ScxmlTransitionType357

    @scxml_ScxmlTransitionType357.setter
    def scxml_ScxmlTransitionType357(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType357", None)
        self.__scxml_ScxmlTransitionType357 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType358"):
                    opp_val = getattr(item, "scxml_ScxmlLogType358", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType358", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType358"):
                    opp_val = getattr(item, "scxml_ScxmlLogType358", None)
                    
                    setattr(item, "scxml_ScxmlLogType358", self)
                    

    @property
    def scxml_ScxmlTransitionType124(self):
        return self.__scxml_ScxmlTransitionType124

    @scxml_ScxmlTransitionType124.setter
    def scxml_ScxmlTransitionType124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType124", None)
        self.__scxml_ScxmlTransitionType124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlHistoryType123"):
                opp_val = getattr(old_value, "scxml_ScxmlHistoryType123", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlHistoryType123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlHistoryType123"):
                opp_val = getattr(value, "scxml_ScxmlHistoryType123", None)
                setattr(value, "scxml_ScxmlHistoryType123", self)

    @property
    def scxml_ScxmlTransitionType351(self):
        return self.__scxml_ScxmlTransitionType351

    @scxml_ScxmlTransitionType351.setter
    def scxml_ScxmlTransitionType351(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType351", None)
        self.__scxml_ScxmlTransitionType351 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType352"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType352", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType352", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType352"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType352", None)
                    
                    setattr(item, "scxml_ScxmlScriptType352", self)
                    

    @property
    def scxml_ScxmlTransitionType348(self):
        return self.__scxml_ScxmlTransitionType348

    @scxml_ScxmlTransitionType348.setter
    def scxml_ScxmlTransitionType348(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType348", None)
        self.__scxml_ScxmlTransitionType348 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType349"):
                    opp_val = getattr(item, "scxml_ScxmlSendType349", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType349", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType349"):
                    opp_val = getattr(item, "scxml_ScxmlSendType349", None)
                    
                    setattr(item, "scxml_ScxmlSendType349", self)
                    

    @property
    def scxml_ScxmlTransitionType354(self):
        return self.__scxml_ScxmlTransitionType354

    @scxml_ScxmlTransitionType354.setter
    def scxml_ScxmlTransitionType354(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType354", None)
        self.__scxml_ScxmlTransitionType354 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType355"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType355", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType355", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType355"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType355", None)
                    
                    setattr(item, "scxml_ScxmlAssignType355", self)
                    

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
            if hasattr(old_value, "scxml_DocumentRoot55"):
                opp_val = getattr(old_value, "scxml_DocumentRoot55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot55"):
                opp_val = getattr(value, "scxml_DocumentRoot55", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlTransitionType345(self):
        return self.__scxml_ScxmlTransitionType345

    @scxml_ScxmlTransitionType345.setter
    def scxml_ScxmlTransitionType345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType345", None)
        self.__scxml_ScxmlTransitionType345 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType346"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType346", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType346", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType346"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType346", None)
                    
                    setattr(item, "scxml_ScxmlForeachType346", self)
                    

    @property
    def scxml_ScxmlTransitionType316(self):
        return self.__scxml_ScxmlTransitionType316

    @scxml_ScxmlTransitionType316.setter
    def scxml_ScxmlTransitionType316(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType316", None)
        self.__scxml_ScxmlTransitionType316 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType315"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType315", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType315"):
                opp_val = getattr(value, "scxml_ScxmlStateType315", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType315", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlTransitionType271(self):
        return self.__scxml_ScxmlTransitionType271

    @scxml_ScxmlTransitionType271.setter
    def scxml_ScxmlTransitionType271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType271", None)
        self.__scxml_ScxmlTransitionType271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType270"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType270", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType270"):
                opp_val = getattr(value, "scxml_ScxmlParallelType270", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType270", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlTransitionType360(self):
        return self.__scxml_ScxmlTransitionType360

    @scxml_ScxmlTransitionType360.setter
    def scxml_ScxmlTransitionType360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType360", None)
        self.__scxml_ScxmlTransitionType360 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType361"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType361", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType361", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType361"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType361", None)
                    
                    setattr(item, "scxml_ScxmlCancelType361", self)
                    

    @property
    def scxml_ScxmlTransitionType339(self):
        return self.__scxml_ScxmlTransitionType339

    @scxml_ScxmlTransitionType339.setter
    def scxml_ScxmlTransitionType339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlTransitionType__scxml_ScxmlTransitionType339", None)
        self.__scxml_ScxmlTransitionType339 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType340"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType340", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType340", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType340"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType340", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType340", self)
                    

class scxml_ScxmlStateType:

    def __init__(self, scxmlStateMix: str, anyAttribute: str, any: str, id: str, initial1: str, scxml_ScxmlStateType: "scxml_DocumentRoot" = None, scxml_ScxmlStateType274: "scxml_ScxmlParallelType" = None, scxml_ScxmlStateType289: "scxml_ScxmlScxmlType" = None, scxml_ScxmlStateType312: set["scxml_ScxmlOnexitType"] = None, scxml_ScxmlStateType315: set["scxml_ScxmlTransitionType"] = None, scxml_ScxmlStateType318: set["scxml_ScxmlInitialType"] = None, scxml_ScxmlStateType322: "scxml_ScxmlStateType" = None, scxml_ScxmlStateType320: set["scxml_ScxmlStateType"] = None, scxml_ScxmlStateType309: set["scxml_ScxmlOnentryType"] = None, scxml_ScxmlStateType327: set["scxml_ScxmlFinalType"] = None, scxml_ScxmlStateType330: set["scxml_ScxmlHistoryType"] = None, scxml_ScxmlStateType333: set["scxml_ScxmlDatamodelType"] = None, scxml_ScxmlStateType336: set["scxml_ScxmlInvokeType"] = None, scxml_ScxmlStateType324: set["scxml_ScxmlParallelType"] = None):
        self.scxmlStateMix = scxmlStateMix
        self.anyAttribute = anyAttribute
        self.any = any
        self.id = id
        self.initial1 = initial1
        self.scxml_ScxmlStateType = scxml_ScxmlStateType
        self.scxml_ScxmlStateType274 = scxml_ScxmlStateType274
        self.scxml_ScxmlStateType289 = scxml_ScxmlStateType289
        self.scxml_ScxmlStateType312 = scxml_ScxmlStateType312 if scxml_ScxmlStateType312 is not None else set()
        self.scxml_ScxmlStateType315 = scxml_ScxmlStateType315 if scxml_ScxmlStateType315 is not None else set()
        self.scxml_ScxmlStateType318 = scxml_ScxmlStateType318 if scxml_ScxmlStateType318 is not None else set()
        self.scxml_ScxmlStateType322 = scxml_ScxmlStateType322
        self.scxml_ScxmlStateType320 = scxml_ScxmlStateType320 if scxml_ScxmlStateType320 is not None else set()
        self.scxml_ScxmlStateType309 = scxml_ScxmlStateType309 if scxml_ScxmlStateType309 is not None else set()
        self.scxml_ScxmlStateType327 = scxml_ScxmlStateType327 if scxml_ScxmlStateType327 is not None else set()
        self.scxml_ScxmlStateType330 = scxml_ScxmlStateType330 if scxml_ScxmlStateType330 is not None else set()
        self.scxml_ScxmlStateType333 = scxml_ScxmlStateType333 if scxml_ScxmlStateType333 is not None else set()
        self.scxml_ScxmlStateType336 = scxml_ScxmlStateType336 if scxml_ScxmlStateType336 is not None else set()
        self.scxml_ScxmlStateType324 = scxml_ScxmlStateType324 if scxml_ScxmlStateType324 is not None else set()
        
    @property
    def scxmlStateMix(self) -> str:
        return self.__scxmlStateMix

    @scxmlStateMix.setter
    def scxmlStateMix(self, scxmlStateMix: str):
        self.__scxmlStateMix = scxmlStateMix

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def initial1(self) -> str:
        return self.__initial1

    @initial1.setter
    def initial1(self, initial1: str):
        self.__initial1 = initial1

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxml_ScxmlStateType312(self):
        return self.__scxml_ScxmlStateType312

    @scxml_ScxmlStateType312.setter
    def scxml_ScxmlStateType312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType312", None)
        self.__scxml_ScxmlStateType312 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexitType313"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType313", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexitType313", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexitType313"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType313", None)
                    
                    setattr(item, "scxml_ScxmlOnexitType313", self)
                    

    @property
    def scxml_ScxmlStateType333(self):
        return self.__scxml_ScxmlStateType333

    @scxml_ScxmlStateType333.setter
    def scxml_ScxmlStateType333(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType333", None)
        self.__scxml_ScxmlStateType333 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDatamodelType334"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType334", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDatamodelType334", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDatamodelType334"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType334", None)
                    
                    setattr(item, "scxml_ScxmlDatamodelType334", self)
                    

    @property
    def scxml_ScxmlStateType324(self):
        return self.__scxml_ScxmlStateType324

    @scxml_ScxmlStateType324.setter
    def scxml_ScxmlStateType324(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType324", None)
        self.__scxml_ScxmlStateType324 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParallelType325"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType325", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParallelType325", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParallelType325"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType325", None)
                    
                    setattr(item, "scxml_ScxmlParallelType325", self)
                    

    @property
    def scxml_ScxmlStateType318(self):
        return self.__scxml_ScxmlStateType318

    @scxml_ScxmlStateType318.setter
    def scxml_ScxmlStateType318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType318", None)
        self.__scxml_ScxmlStateType318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlInitialType319"):
                    opp_val = getattr(item, "scxml_ScxmlInitialType319", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlInitialType319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlInitialType319"):
                    opp_val = getattr(item, "scxml_ScxmlInitialType319", None)
                    
                    setattr(item, "scxml_ScxmlInitialType319", self)
                    

    @property
    def scxml_ScxmlStateType309(self):
        return self.__scxml_ScxmlStateType309

    @scxml_ScxmlStateType309.setter
    def scxml_ScxmlStateType309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType309", None)
        self.__scxml_ScxmlStateType309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnentryType310"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType310", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnentryType310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnentryType310"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType310", None)
                    
                    setattr(item, "scxml_ScxmlOnentryType310", self)
                    

    @property
    def scxml_ScxmlStateType315(self):
        return self.__scxml_ScxmlStateType315

    @scxml_ScxmlStateType315.setter
    def scxml_ScxmlStateType315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType315", None)
        self.__scxml_ScxmlStateType315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlTransitionType316"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType316", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlTransitionType316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlTransitionType316"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType316", None)
                    
                    setattr(item, "scxml_ScxmlTransitionType316", self)
                    

    @property
    def scxml_ScxmlStateType320(self):
        return self.__scxml_ScxmlStateType320

    @scxml_ScxmlStateType320.setter
    def scxml_ScxmlStateType320(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType320", None)
        self.__scxml_ScxmlStateType320 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlStateType322"):
                    opp_val = getattr(item, "scxml_ScxmlStateType322", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlStateType322", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlStateType322"):
                    opp_val = getattr(item, "scxml_ScxmlStateType322", None)
                    
                    setattr(item, "scxml_ScxmlStateType322", self)
                    

    @property
    def scxml_ScxmlStateType330(self):
        return self.__scxml_ScxmlStateType330

    @scxml_ScxmlStateType330.setter
    def scxml_ScxmlStateType330(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType330", None)
        self.__scxml_ScxmlStateType330 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlHistoryType331"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType331", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlHistoryType331", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlHistoryType331"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType331", None)
                    
                    setattr(item, "scxml_ScxmlHistoryType331", self)
                    

    @property
    def scxml_ScxmlStateType327(self):
        return self.__scxml_ScxmlStateType327

    @scxml_ScxmlStateType327.setter
    def scxml_ScxmlStateType327(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType327", None)
        self.__scxml_ScxmlStateType327 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlFinalType328"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType328", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlFinalType328", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlFinalType328"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType328", None)
                    
                    setattr(item, "scxml_ScxmlFinalType328", self)
                    

    @property
    def scxml_ScxmlStateType322(self):
        return self.__scxml_ScxmlStateType322

    @scxml_ScxmlStateType322.setter
    def scxml_ScxmlStateType322(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType322", None)
        self.__scxml_ScxmlStateType322 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType320"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType320", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType320"):
                opp_val = getattr(value, "scxml_ScxmlStateType320", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType320", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "scxml_DocumentRoot53"):
                opp_val = getattr(old_value, "scxml_DocumentRoot53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot53"):
                opp_val = getattr(value, "scxml_DocumentRoot53", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlStateType274(self):
        return self.__scxml_ScxmlStateType274

    @scxml_ScxmlStateType274.setter
    def scxml_ScxmlStateType274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType274", None)
        self.__scxml_ScxmlStateType274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType273"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType273", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType273"):
                opp_val = getattr(value, "scxml_ScxmlParallelType273", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType273", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlStateType289(self):
        return self.__scxml_ScxmlStateType289

    @scxml_ScxmlStateType289.setter
    def scxml_ScxmlStateType289(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType289", None)
        self.__scxml_ScxmlStateType289 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType288"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType288", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType288"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType288", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType288", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlStateType336(self):
        return self.__scxml_ScxmlStateType336

    @scxml_ScxmlStateType336.setter
    def scxml_ScxmlStateType336(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlStateType__scxml_ScxmlStateType336", None)
        self.__scxml_ScxmlStateType336 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlInvokeType337"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType337", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlInvokeType337", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlInvokeType337"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType337", None)
                    
                    setattr(item, "scxml_ScxmlInvokeType337", self)
                    

class scxml_ScxmlSendType:

    def __init__(self, scxmlSendMix: str, any: str, delay: str, idlocation: str, namelist: str, target: str, targetexpr: str, type: str, typeexpr: str, anyAttribute: str, delayexpr: str, event: str, eventexpr: str, id: str, scxml_ScxmlSendType: "scxml_DocumentRoot" = None, scxml_ScxmlSendType76: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlSendType109: "scxml_ScxmlForeachType" = None, scxml_ScxmlSendType136: "scxml_ScxmlIfType" = None, scxml_ScxmlSendType163: "scxml_ScxmlIfType" = None, scxml_ScxmlSendType190: "scxml_ScxmlIfType" = None, scxml_ScxmlSendType226: "scxml_ScxmlOnentryType" = None, scxml_ScxmlSendType250: "scxml_ScxmlOnexitType" = None, scxml_ScxmlSendType303: set["scxml_ScxmlContentType"] = None, scxml_ScxmlSendType306: set["scxml_ScxmlParamType"] = None, scxml_ScxmlSendType349: "scxml_ScxmlTransitionType" = None):
        self.scxmlSendMix = scxmlSendMix
        self.any = any
        self.delay = delay
        self.idlocation = idlocation
        self.namelist = namelist
        self.target = target
        self.targetexpr = targetexpr
        self.type = type
        self.typeexpr = typeexpr
        self.anyAttribute = anyAttribute
        self.delayexpr = delayexpr
        self.event = event
        self.eventexpr = eventexpr
        self.id = id
        self.scxml_ScxmlSendType = scxml_ScxmlSendType
        self.scxml_ScxmlSendType76 = scxml_ScxmlSendType76
        self.scxml_ScxmlSendType109 = scxml_ScxmlSendType109
        self.scxml_ScxmlSendType136 = scxml_ScxmlSendType136
        self.scxml_ScxmlSendType163 = scxml_ScxmlSendType163
        self.scxml_ScxmlSendType190 = scxml_ScxmlSendType190
        self.scxml_ScxmlSendType226 = scxml_ScxmlSendType226
        self.scxml_ScxmlSendType250 = scxml_ScxmlSendType250
        self.scxml_ScxmlSendType303 = scxml_ScxmlSendType303 if scxml_ScxmlSendType303 is not None else set()
        self.scxml_ScxmlSendType306 = scxml_ScxmlSendType306 if scxml_ScxmlSendType306 is not None else set()
        self.scxml_ScxmlSendType349 = scxml_ScxmlSendType349
        
    @property
    def typeexpr(self) -> str:
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr

    @property
    def targetexpr(self) -> str:
        return self.__targetexpr

    @targetexpr.setter
    def targetexpr(self, targetexpr: str):
        self.__targetexpr = targetexpr

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
    def idlocation(self) -> str:
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation

    @property
    def namelist(self) -> str:
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def delayexpr(self) -> str:
        return self.__delayexpr

    @delayexpr.setter
    def delayexpr(self, delayexpr: str):
        self.__delayexpr = delayexpr

    @property
    def delay(self) -> str:
        return self.__delay

    @delay.setter
    def delay(self, delay: str):
        self.__delay = delay

    @property
    def scxmlSendMix(self) -> str:
        return self.__scxmlSendMix

    @scxmlSendMix.setter
    def scxmlSendMix(self, scxmlSendMix: str):
        self.__scxmlSendMix = scxmlSendMix

    @property
    def eventexpr(self) -> str:
        return self.__eventexpr

    @eventexpr.setter
    def eventexpr(self, eventexpr: str):
        self.__eventexpr = eventexpr

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlSendType190(self):
        return self.__scxml_ScxmlSendType190

    @scxml_ScxmlSendType190.setter
    def scxml_ScxmlSendType190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType190", None)
        self.__scxml_ScxmlSendType190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType189"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType189", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType189"):
                opp_val = getattr(value, "scxml_ScxmlIfType189", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType189", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType306(self):
        return self.__scxml_ScxmlSendType306

    @scxml_ScxmlSendType306.setter
    def scxml_ScxmlSendType306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType306", None)
        self.__scxml_ScxmlSendType306 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParamType307"):
                    opp_val = getattr(item, "scxml_ScxmlParamType307", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParamType307", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParamType307"):
                    opp_val = getattr(item, "scxml_ScxmlParamType307", None)
                    
                    setattr(item, "scxml_ScxmlParamType307", self)
                    

    @property
    def scxml_ScxmlSendType250(self):
        return self.__scxml_ScxmlSendType250

    @scxml_ScxmlSendType250.setter
    def scxml_ScxmlSendType250(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType250", None)
        self.__scxml_ScxmlSendType250 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType249"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType249", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType249"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType249", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType249", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType226(self):
        return self.__scxml_ScxmlSendType226

    @scxml_ScxmlSendType226.setter
    def scxml_ScxmlSendType226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType226", None)
        self.__scxml_ScxmlSendType226 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType225"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType225", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType225"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType225", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType225", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType76(self):
        return self.__scxml_ScxmlSendType76

    @scxml_ScxmlSendType76.setter
    def scxml_ScxmlSendType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType76", None)
        self.__scxml_ScxmlSendType76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType75"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType75"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType75", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType349(self):
        return self.__scxml_ScxmlSendType349

    @scxml_ScxmlSendType349.setter
    def scxml_ScxmlSendType349(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType349", None)
        self.__scxml_ScxmlSendType349 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType348"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType348", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType348"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType348", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType348", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType163(self):
        return self.__scxml_ScxmlSendType163

    @scxml_ScxmlSendType163.setter
    def scxml_ScxmlSendType163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType163", None)
        self.__scxml_ScxmlSendType163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType162"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType162"):
                opp_val = getattr(value, "scxml_ScxmlIfType162", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "scxml_DocumentRoot51"):
                opp_val = getattr(old_value, "scxml_DocumentRoot51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot51"):
                opp_val = getattr(value, "scxml_DocumentRoot51", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType109(self):
        return self.__scxml_ScxmlSendType109

    @scxml_ScxmlSendType109.setter
    def scxml_ScxmlSendType109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType109", None)
        self.__scxml_ScxmlSendType109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType108"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType108"):
                opp_val = getattr(value, "scxml_ScxmlForeachType108", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType136(self):
        return self.__scxml_ScxmlSendType136

    @scxml_ScxmlSendType136.setter
    def scxml_ScxmlSendType136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType136", None)
        self.__scxml_ScxmlSendType136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType135"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType135", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType135"):
                opp_val = getattr(value, "scxml_ScxmlIfType135", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType135", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlSendType303(self):
        return self.__scxml_ScxmlSendType303

    @scxml_ScxmlSendType303.setter
    def scxml_ScxmlSendType303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlSendType__scxml_ScxmlSendType303", None)
        self.__scxml_ScxmlSendType303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlContentType304"):
                    opp_val = getattr(item, "scxml_ScxmlContentType304", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlContentType304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlContentType304"):
                    opp_val = getattr(item, "scxml_ScxmlContentType304", None)
                    
                    setattr(item, "scxml_ScxmlContentType304", self)
                    

class scxml_ScxmlOnexitType:

    def __init__(self, scxmlCoreExecutablecontent: str, any: str, anyAttribute: str, scxml_ScxmlOnexitType: "scxml_DocumentRoot" = None, scxml_ScxmlOnexitType94: "scxml_ScxmlFinalType" = None, scxml_ScxmlOnexitType240: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlOnexitType243: set["scxml_ScxmlIfType"] = None, scxml_ScxmlOnexitType246: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlOnexitType252: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlOnexitType255: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlOnexitType258: set["scxml_ScxmlLogType"] = None, scxml_ScxmlOnexitType249: set["scxml_ScxmlSendType"] = None, scxml_ScxmlOnexitType268: "scxml_ScxmlParallelType" = None, scxml_ScxmlOnexitType261: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlOnexitType313: "scxml_ScxmlStateType" = None):
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.any = any
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlOnexitType = scxml_ScxmlOnexitType
        self.scxml_ScxmlOnexitType94 = scxml_ScxmlOnexitType94
        self.scxml_ScxmlOnexitType240 = scxml_ScxmlOnexitType240 if scxml_ScxmlOnexitType240 is not None else set()
        self.scxml_ScxmlOnexitType243 = scxml_ScxmlOnexitType243 if scxml_ScxmlOnexitType243 is not None else set()
        self.scxml_ScxmlOnexitType246 = scxml_ScxmlOnexitType246 if scxml_ScxmlOnexitType246 is not None else set()
        self.scxml_ScxmlOnexitType252 = scxml_ScxmlOnexitType252 if scxml_ScxmlOnexitType252 is not None else set()
        self.scxml_ScxmlOnexitType255 = scxml_ScxmlOnexitType255 if scxml_ScxmlOnexitType255 is not None else set()
        self.scxml_ScxmlOnexitType258 = scxml_ScxmlOnexitType258 if scxml_ScxmlOnexitType258 is not None else set()
        self.scxml_ScxmlOnexitType249 = scxml_ScxmlOnexitType249 if scxml_ScxmlOnexitType249 is not None else set()
        self.scxml_ScxmlOnexitType268 = scxml_ScxmlOnexitType268
        self.scxml_ScxmlOnexitType261 = scxml_ScxmlOnexitType261 if scxml_ScxmlOnexitType261 is not None else set()
        self.scxml_ScxmlOnexitType313 = scxml_ScxmlOnexitType313
        
    @property
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

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
    def scxml_ScxmlOnexitType(self):
        return self.__scxml_ScxmlOnexitType

    @scxml_ScxmlOnexitType.setter
    def scxml_ScxmlOnexitType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType", None)
        self.__scxml_ScxmlOnexitType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot39"):
                opp_val = getattr(old_value, "scxml_DocumentRoot39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot39"):
                opp_val = getattr(value, "scxml_DocumentRoot39", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnexitType94(self):
        return self.__scxml_ScxmlOnexitType94

    @scxml_ScxmlOnexitType94.setter
    def scxml_ScxmlOnexitType94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType94", None)
        self.__scxml_ScxmlOnexitType94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalType93"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalType93", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalType93"):
                opp_val = getattr(value, "scxml_ScxmlFinalType93", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalType93", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnexitType252(self):
        return self.__scxml_ScxmlOnexitType252

    @scxml_ScxmlOnexitType252.setter
    def scxml_ScxmlOnexitType252(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType252", None)
        self.__scxml_ScxmlOnexitType252 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType253"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType253", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType253", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType253"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType253", None)
                    
                    setattr(item, "scxml_ScxmlScriptType253", self)
                    

    @property
    def scxml_ScxmlOnexitType261(self):
        return self.__scxml_ScxmlOnexitType261

    @scxml_ScxmlOnexitType261.setter
    def scxml_ScxmlOnexitType261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType261", None)
        self.__scxml_ScxmlOnexitType261 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType262"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType262", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType262", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType262"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType262", None)
                    
                    setattr(item, "scxml_ScxmlCancelType262", self)
                    

    @property
    def scxml_ScxmlOnexitType268(self):
        return self.__scxml_ScxmlOnexitType268

    @scxml_ScxmlOnexitType268.setter
    def scxml_ScxmlOnexitType268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType268", None)
        self.__scxml_ScxmlOnexitType268 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType267"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType267", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType267"):
                opp_val = getattr(value, "scxml_ScxmlParallelType267", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType267", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnexitType240(self):
        return self.__scxml_ScxmlOnexitType240

    @scxml_ScxmlOnexitType240.setter
    def scxml_ScxmlOnexitType240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType240", None)
        self.__scxml_ScxmlOnexitType240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType241"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType241", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType241", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType241"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType241", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType241", self)
                    

    @property
    def scxml_ScxmlOnexitType313(self):
        return self.__scxml_ScxmlOnexitType313

    @scxml_ScxmlOnexitType313.setter
    def scxml_ScxmlOnexitType313(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType313", None)
        self.__scxml_ScxmlOnexitType313 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType312"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType312", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType312"):
                opp_val = getattr(value, "scxml_ScxmlStateType312", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType312", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnexitType246(self):
        return self.__scxml_ScxmlOnexitType246

    @scxml_ScxmlOnexitType246.setter
    def scxml_ScxmlOnexitType246(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType246", None)
        self.__scxml_ScxmlOnexitType246 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType247"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType247", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType247", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType247"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType247", None)
                    
                    setattr(item, "scxml_ScxmlForeachType247", self)
                    

    @property
    def scxml_ScxmlOnexitType255(self):
        return self.__scxml_ScxmlOnexitType255

    @scxml_ScxmlOnexitType255.setter
    def scxml_ScxmlOnexitType255(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType255", None)
        self.__scxml_ScxmlOnexitType255 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType256"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType256", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType256", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType256"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType256", None)
                    
                    setattr(item, "scxml_ScxmlAssignType256", self)
                    

    @property
    def scxml_ScxmlOnexitType249(self):
        return self.__scxml_ScxmlOnexitType249

    @scxml_ScxmlOnexitType249.setter
    def scxml_ScxmlOnexitType249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType249", None)
        self.__scxml_ScxmlOnexitType249 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType250"):
                    opp_val = getattr(item, "scxml_ScxmlSendType250", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType250", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType250"):
                    opp_val = getattr(item, "scxml_ScxmlSendType250", None)
                    
                    setattr(item, "scxml_ScxmlSendType250", self)
                    

    @property
    def scxml_ScxmlOnexitType258(self):
        return self.__scxml_ScxmlOnexitType258

    @scxml_ScxmlOnexitType258.setter
    def scxml_ScxmlOnexitType258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType258", None)
        self.__scxml_ScxmlOnexitType258 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType259"):
                    opp_val = getattr(item, "scxml_ScxmlLogType259", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType259", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType259"):
                    opp_val = getattr(item, "scxml_ScxmlLogType259", None)
                    
                    setattr(item, "scxml_ScxmlLogType259", self)
                    

    @property
    def scxml_ScxmlOnexitType243(self):
        return self.__scxml_ScxmlOnexitType243

    @scxml_ScxmlOnexitType243.setter
    def scxml_ScxmlOnexitType243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnexitType__scxml_ScxmlOnexitType243", None)
        self.__scxml_ScxmlOnexitType243 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType244"):
                    opp_val = getattr(item, "scxml_ScxmlIfType244", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType244", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType244"):
                    opp_val = getattr(item, "scxml_ScxmlIfType244", None)
                    
                    setattr(item, "scxml_ScxmlIfType244", self)
                    

class scxml_ScxmlOnentryType:

    def __init__(self, any: str, scxmlCoreExecutablecontent: str, anyAttribute: str, scxml_ScxmlOnentryType: "scxml_DocumentRoot" = None, scxml_ScxmlOnentryType91: "scxml_ScxmlFinalType" = None, scxml_ScxmlOnentryType216: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlOnentryType219: set["scxml_ScxmlIfType"] = None, scxml_ScxmlOnentryType225: set["scxml_ScxmlSendType"] = None, scxml_ScxmlOnentryType228: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlOnentryType222: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlOnentryType234: set["scxml_ScxmlLogType"] = None, scxml_ScxmlOnentryType237: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlOnentryType231: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlOnentryType265: "scxml_ScxmlParallelType" = None, scxml_ScxmlOnentryType310: "scxml_ScxmlStateType" = None):
        self.any = any
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlOnentryType = scxml_ScxmlOnentryType
        self.scxml_ScxmlOnentryType91 = scxml_ScxmlOnentryType91
        self.scxml_ScxmlOnentryType216 = scxml_ScxmlOnentryType216 if scxml_ScxmlOnentryType216 is not None else set()
        self.scxml_ScxmlOnentryType219 = scxml_ScxmlOnentryType219 if scxml_ScxmlOnentryType219 is not None else set()
        self.scxml_ScxmlOnentryType225 = scxml_ScxmlOnentryType225 if scxml_ScxmlOnentryType225 is not None else set()
        self.scxml_ScxmlOnentryType228 = scxml_ScxmlOnentryType228 if scxml_ScxmlOnentryType228 is not None else set()
        self.scxml_ScxmlOnentryType222 = scxml_ScxmlOnentryType222 if scxml_ScxmlOnentryType222 is not None else set()
        self.scxml_ScxmlOnentryType234 = scxml_ScxmlOnentryType234 if scxml_ScxmlOnentryType234 is not None else set()
        self.scxml_ScxmlOnentryType237 = scxml_ScxmlOnentryType237 if scxml_ScxmlOnentryType237 is not None else set()
        self.scxml_ScxmlOnentryType231 = scxml_ScxmlOnentryType231 if scxml_ScxmlOnentryType231 is not None else set()
        self.scxml_ScxmlOnentryType265 = scxml_ScxmlOnentryType265
        self.scxml_ScxmlOnentryType310 = scxml_ScxmlOnentryType310
        
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
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

    @property
    def scxml_ScxmlOnentryType222(self):
        return self.__scxml_ScxmlOnentryType222

    @scxml_ScxmlOnentryType222.setter
    def scxml_ScxmlOnentryType222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType222", None)
        self.__scxml_ScxmlOnentryType222 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType223"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType223", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType223", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType223"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType223", None)
                    
                    setattr(item, "scxml_ScxmlForeachType223", self)
                    

    @property
    def scxml_ScxmlOnentryType237(self):
        return self.__scxml_ScxmlOnentryType237

    @scxml_ScxmlOnentryType237.setter
    def scxml_ScxmlOnentryType237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType237", None)
        self.__scxml_ScxmlOnentryType237 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType238"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType238", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType238", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType238"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType238", None)
                    
                    setattr(item, "scxml_ScxmlCancelType238", self)
                    

    @property
    def scxml_ScxmlOnentryType225(self):
        return self.__scxml_ScxmlOnentryType225

    @scxml_ScxmlOnentryType225.setter
    def scxml_ScxmlOnentryType225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType225", None)
        self.__scxml_ScxmlOnentryType225 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType226"):
                    opp_val = getattr(item, "scxml_ScxmlSendType226", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType226", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType226"):
                    opp_val = getattr(item, "scxml_ScxmlSendType226", None)
                    
                    setattr(item, "scxml_ScxmlSendType226", self)
                    

    @property
    def scxml_ScxmlOnentryType231(self):
        return self.__scxml_ScxmlOnentryType231

    @scxml_ScxmlOnentryType231.setter
    def scxml_ScxmlOnentryType231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType231", None)
        self.__scxml_ScxmlOnentryType231 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType232"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType232", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType232", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType232"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType232", None)
                    
                    setattr(item, "scxml_ScxmlAssignType232", self)
                    

    @property
    def scxml_ScxmlOnentryType216(self):
        return self.__scxml_ScxmlOnentryType216

    @scxml_ScxmlOnentryType216.setter
    def scxml_ScxmlOnentryType216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType216", None)
        self.__scxml_ScxmlOnentryType216 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType217"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType217", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType217", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType217"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType217", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType217", self)
                    

    @property
    def scxml_ScxmlOnentryType219(self):
        return self.__scxml_ScxmlOnentryType219

    @scxml_ScxmlOnentryType219.setter
    def scxml_ScxmlOnentryType219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType219", None)
        self.__scxml_ScxmlOnentryType219 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType220"):
                    opp_val = getattr(item, "scxml_ScxmlIfType220", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType220", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType220"):
                    opp_val = getattr(item, "scxml_ScxmlIfType220", None)
                    
                    setattr(item, "scxml_ScxmlIfType220", self)
                    

    @property
    def scxml_ScxmlOnentryType228(self):
        return self.__scxml_ScxmlOnentryType228

    @scxml_ScxmlOnentryType228.setter
    def scxml_ScxmlOnentryType228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType228", None)
        self.__scxml_ScxmlOnentryType228 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType229"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType229", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType229", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType229"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType229", None)
                    
                    setattr(item, "scxml_ScxmlScriptType229", self)
                    

    @property
    def scxml_ScxmlOnentryType91(self):
        return self.__scxml_ScxmlOnentryType91

    @scxml_ScxmlOnentryType91.setter
    def scxml_ScxmlOnentryType91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType91", None)
        self.__scxml_ScxmlOnentryType91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalType90"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalType90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalType90"):
                opp_val = getattr(value, "scxml_ScxmlFinalType90", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalType90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnentryType234(self):
        return self.__scxml_ScxmlOnentryType234

    @scxml_ScxmlOnentryType234.setter
    def scxml_ScxmlOnentryType234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType234", None)
        self.__scxml_ScxmlOnentryType234 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType235"):
                    opp_val = getattr(item, "scxml_ScxmlLogType235", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType235"):
                    opp_val = getattr(item, "scxml_ScxmlLogType235", None)
                    
                    setattr(item, "scxml_ScxmlLogType235", self)
                    

    @property
    def scxml_ScxmlOnentryType265(self):
        return self.__scxml_ScxmlOnentryType265

    @scxml_ScxmlOnentryType265.setter
    def scxml_ScxmlOnentryType265(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType265", None)
        self.__scxml_ScxmlOnentryType265 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType264"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType264", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType264"):
                opp_val = getattr(value, "scxml_ScxmlParallelType264", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType264", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnentryType(self):
        return self.__scxml_ScxmlOnentryType

    @scxml_ScxmlOnentryType.setter
    def scxml_ScxmlOnentryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType", None)
        self.__scxml_ScxmlOnentryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot37"):
                opp_val = getattr(old_value, "scxml_DocumentRoot37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot37"):
                opp_val = getattr(value, "scxml_DocumentRoot37", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlOnentryType310(self):
        return self.__scxml_ScxmlOnentryType310

    @scxml_ScxmlOnentryType310.setter
    def scxml_ScxmlOnentryType310(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlOnentryType__scxml_ScxmlOnentryType310", None)
        self.__scxml_ScxmlOnentryType310 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType309"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType309", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType309"):
                opp_val = getattr(value, "scxml_ScxmlStateType309", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType309", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlRaiseType:

    def __init__(self, event: str, anyAttribute: str, scxml_ScxmlRaiseType: "scxml_DocumentRoot" = None, scxml_ScxmlRaiseType67: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlRaiseType100: "scxml_ScxmlForeachType" = None, scxml_ScxmlRaiseType127: "scxml_ScxmlIfType" = None, scxml_ScxmlRaiseType154: "scxml_ScxmlIfType" = None, scxml_ScxmlRaiseType181: "scxml_ScxmlIfType" = None, scxml_ScxmlRaiseType217: "scxml_ScxmlOnentryType" = None, scxml_ScxmlRaiseType241: "scxml_ScxmlOnexitType" = None, scxml_ScxmlRaiseType340: "scxml_ScxmlTransitionType" = None):
        self.event = event
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlRaiseType = scxml_ScxmlRaiseType
        self.scxml_ScxmlRaiseType67 = scxml_ScxmlRaiseType67
        self.scxml_ScxmlRaiseType100 = scxml_ScxmlRaiseType100
        self.scxml_ScxmlRaiseType127 = scxml_ScxmlRaiseType127
        self.scxml_ScxmlRaiseType154 = scxml_ScxmlRaiseType154
        self.scxml_ScxmlRaiseType181 = scxml_ScxmlRaiseType181
        self.scxml_ScxmlRaiseType217 = scxml_ScxmlRaiseType217
        self.scxml_ScxmlRaiseType241 = scxml_ScxmlRaiseType241
        self.scxml_ScxmlRaiseType340 = scxml_ScxmlRaiseType340
        
    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlRaiseType217(self):
        return self.__scxml_ScxmlRaiseType217

    @scxml_ScxmlRaiseType217.setter
    def scxml_ScxmlRaiseType217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType217", None)
        self.__scxml_ScxmlRaiseType217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType216"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType216", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType216"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType216", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType216", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType127(self):
        return self.__scxml_ScxmlRaiseType127

    @scxml_ScxmlRaiseType127.setter
    def scxml_ScxmlRaiseType127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType127", None)
        self.__scxml_ScxmlRaiseType127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType126"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType126"):
                opp_val = getattr(value, "scxml_ScxmlIfType126", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType181(self):
        return self.__scxml_ScxmlRaiseType181

    @scxml_ScxmlRaiseType181.setter
    def scxml_ScxmlRaiseType181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType181", None)
        self.__scxml_ScxmlRaiseType181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType180"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType180", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType180"):
                opp_val = getattr(value, "scxml_ScxmlIfType180", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType180", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType(self):
        return self.__scxml_ScxmlRaiseType

    @scxml_ScxmlRaiseType.setter
    def scxml_ScxmlRaiseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType", None)
        self.__scxml_ScxmlRaiseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot45"):
                opp_val = getattr(old_value, "scxml_DocumentRoot45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot45"):
                opp_val = getattr(value, "scxml_DocumentRoot45", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType154(self):
        return self.__scxml_ScxmlRaiseType154

    @scxml_ScxmlRaiseType154.setter
    def scxml_ScxmlRaiseType154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType154", None)
        self.__scxml_ScxmlRaiseType154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType153"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType153"):
                opp_val = getattr(value, "scxml_ScxmlIfType153", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType67(self):
        return self.__scxml_ScxmlRaiseType67

    @scxml_ScxmlRaiseType67.setter
    def scxml_ScxmlRaiseType67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType67", None)
        self.__scxml_ScxmlRaiseType67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType66"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType66"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType66", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType100(self):
        return self.__scxml_ScxmlRaiseType100

    @scxml_ScxmlRaiseType100.setter
    def scxml_ScxmlRaiseType100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType100", None)
        self.__scxml_ScxmlRaiseType100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType99"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType99", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType99"):
                opp_val = getattr(value, "scxml_ScxmlForeachType99", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType99", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType340(self):
        return self.__scxml_ScxmlRaiseType340

    @scxml_ScxmlRaiseType340.setter
    def scxml_ScxmlRaiseType340(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType340", None)
        self.__scxml_ScxmlRaiseType340 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType339"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType339", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType339"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType339", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType339", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlRaiseType241(self):
        return self.__scxml_ScxmlRaiseType241

    @scxml_ScxmlRaiseType241.setter
    def scxml_ScxmlRaiseType241(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlRaiseType__scxml_ScxmlRaiseType241", None)
        self.__scxml_ScxmlRaiseType241 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType240"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType240"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType240", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlParamType:

    def __init__(self, scxmlExtraContent: str, any: str, expr: str, location: str, name: str, anyAttribute: str, scxml_ScxmlParamType: "scxml_DocumentRoot" = None, scxml_ScxmlParamType64: "scxml_ScxmlDonedataType" = None, scxml_ScxmlParamType211: "scxml_ScxmlInvokeType" = None, scxml_ScxmlParamType307: "scxml_ScxmlSendType" = None):
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.expr = expr
        self.location = location
        self.name = name
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlParamType = scxml_ScxmlParamType
        self.scxml_ScxmlParamType64 = scxml_ScxmlParamType64
        self.scxml_ScxmlParamType211 = scxml_ScxmlParamType211
        self.scxml_ScxmlParamType307 = scxml_ScxmlParamType307
        
    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

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
            if hasattr(old_value, "scxml_DocumentRoot43"):
                opp_val = getattr(old_value, "scxml_DocumentRoot43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot43"):
                opp_val = getattr(value, "scxml_DocumentRoot43", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParamType307(self):
        return self.__scxml_ScxmlParamType307

    @scxml_ScxmlParamType307.setter
    def scxml_ScxmlParamType307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParamType__scxml_ScxmlParamType307", None)
        self.__scxml_ScxmlParamType307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlSendType306"):
                opp_val = getattr(old_value, "scxml_ScxmlSendType306", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlSendType306"):
                opp_val = getattr(value, "scxml_ScxmlSendType306", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlSendType306", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParamType64(self):
        return self.__scxml_ScxmlParamType64

    @scxml_ScxmlParamType64.setter
    def scxml_ScxmlParamType64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParamType__scxml_ScxmlParamType64", None)
        self.__scxml_ScxmlParamType64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlDonedataType63"):
                opp_val = getattr(old_value, "scxml_ScxmlDonedataType63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlDonedataType63"):
                opp_val = getattr(value, "scxml_ScxmlDonedataType63", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlDonedataType63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParamType211(self):
        return self.__scxml_ScxmlParamType211

    @scxml_ScxmlParamType211.setter
    def scxml_ScxmlParamType211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParamType__scxml_ScxmlParamType211", None)
        self.__scxml_ScxmlParamType211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlInvokeType210"):
                opp_val = getattr(old_value, "scxml_ScxmlInvokeType210", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlInvokeType210"):
                opp_val = getattr(value, "scxml_ScxmlInvokeType210", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlInvokeType210", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlParallelType:

    def __init__(self, scxmlParallelMix: str, id: str, anyAttribute: str, any: str, scxml_ScxmlParallelType: "scxml_DocumentRoot" = None, scxml_ScxmlParallelType264: set["scxml_ScxmlOnentryType"] = None, scxml_ScxmlParallelType267: set["scxml_ScxmlOnexitType"] = None, scxml_ScxmlParallelType277: "scxml_ScxmlParallelType" = None, scxml_ScxmlParallelType275: set["scxml_ScxmlParallelType"] = None, scxml_ScxmlParallelType279: set["scxml_ScxmlHistoryType"] = None, scxml_ScxmlParallelType282: set["scxml_ScxmlDatamodelType"] = None, scxml_ScxmlParallelType270: set["scxml_ScxmlTransitionType"] = None, scxml_ScxmlParallelType273: set["scxml_ScxmlStateType"] = None, scxml_ScxmlParallelType285: set["scxml_ScxmlInvokeType"] = None, scxml_ScxmlParallelType292: "scxml_ScxmlScxmlType" = None, scxml_ScxmlParallelType325: "scxml_ScxmlStateType" = None):
        self.scxmlParallelMix = scxmlParallelMix
        self.id = id
        self.anyAttribute = anyAttribute
        self.any = any
        self.scxml_ScxmlParallelType = scxml_ScxmlParallelType
        self.scxml_ScxmlParallelType264 = scxml_ScxmlParallelType264 if scxml_ScxmlParallelType264 is not None else set()
        self.scxml_ScxmlParallelType267 = scxml_ScxmlParallelType267 if scxml_ScxmlParallelType267 is not None else set()
        self.scxml_ScxmlParallelType277 = scxml_ScxmlParallelType277
        self.scxml_ScxmlParallelType275 = scxml_ScxmlParallelType275 if scxml_ScxmlParallelType275 is not None else set()
        self.scxml_ScxmlParallelType279 = scxml_ScxmlParallelType279 if scxml_ScxmlParallelType279 is not None else set()
        self.scxml_ScxmlParallelType282 = scxml_ScxmlParallelType282 if scxml_ScxmlParallelType282 is not None else set()
        self.scxml_ScxmlParallelType270 = scxml_ScxmlParallelType270 if scxml_ScxmlParallelType270 is not None else set()
        self.scxml_ScxmlParallelType273 = scxml_ScxmlParallelType273 if scxml_ScxmlParallelType273 is not None else set()
        self.scxml_ScxmlParallelType285 = scxml_ScxmlParallelType285 if scxml_ScxmlParallelType285 is not None else set()
        self.scxml_ScxmlParallelType292 = scxml_ScxmlParallelType292
        self.scxml_ScxmlParallelType325 = scxml_ScxmlParallelType325
        
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
    def scxmlParallelMix(self) -> str:
        return self.__scxmlParallelMix

    @scxmlParallelMix.setter
    def scxmlParallelMix(self, scxmlParallelMix: str):
        self.__scxmlParallelMix = scxmlParallelMix

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxml_ScxmlParallelType292(self):
        return self.__scxml_ScxmlParallelType292

    @scxml_ScxmlParallelType292.setter
    def scxml_ScxmlParallelType292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType292", None)
        self.__scxml_ScxmlParallelType292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType291"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType291", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType291"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType291", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType291", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParallelType279(self):
        return self.__scxml_ScxmlParallelType279

    @scxml_ScxmlParallelType279.setter
    def scxml_ScxmlParallelType279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType279", None)
        self.__scxml_ScxmlParallelType279 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlHistoryType280"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType280", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlHistoryType280", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlHistoryType280"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType280", None)
                    
                    setattr(item, "scxml_ScxmlHistoryType280", self)
                    

    @property
    def scxml_ScxmlParallelType(self):
        return self.__scxml_ScxmlParallelType

    @scxml_ScxmlParallelType.setter
    def scxml_ScxmlParallelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType", None)
        self.__scxml_ScxmlParallelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot41"):
                opp_val = getattr(old_value, "scxml_DocumentRoot41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot41"):
                opp_val = getattr(value, "scxml_DocumentRoot41", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParallelType270(self):
        return self.__scxml_ScxmlParallelType270

    @scxml_ScxmlParallelType270.setter
    def scxml_ScxmlParallelType270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType270", None)
        self.__scxml_ScxmlParallelType270 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlTransitionType271"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType271", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlTransitionType271", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlTransitionType271"):
                    opp_val = getattr(item, "scxml_ScxmlTransitionType271", None)
                    
                    setattr(item, "scxml_ScxmlTransitionType271", self)
                    

    @property
    def scxml_ScxmlParallelType264(self):
        return self.__scxml_ScxmlParallelType264

    @scxml_ScxmlParallelType264.setter
    def scxml_ScxmlParallelType264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType264", None)
        self.__scxml_ScxmlParallelType264 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnentryType265"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType265", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnentryType265", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnentryType265"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType265", None)
                    
                    setattr(item, "scxml_ScxmlOnentryType265", self)
                    

    @property
    def scxml_ScxmlParallelType267(self):
        return self.__scxml_ScxmlParallelType267

    @scxml_ScxmlParallelType267.setter
    def scxml_ScxmlParallelType267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType267", None)
        self.__scxml_ScxmlParallelType267 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexitType268"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType268", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexitType268", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexitType268"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType268", None)
                    
                    setattr(item, "scxml_ScxmlOnexitType268", self)
                    

    @property
    def scxml_ScxmlParallelType277(self):
        return self.__scxml_ScxmlParallelType277

    @scxml_ScxmlParallelType277.setter
    def scxml_ScxmlParallelType277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType277", None)
        self.__scxml_ScxmlParallelType277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType275"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType275", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType275"):
                opp_val = getattr(value, "scxml_ScxmlParallelType275", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType275", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParallelType325(self):
        return self.__scxml_ScxmlParallelType325

    @scxml_ScxmlParallelType325.setter
    def scxml_ScxmlParallelType325(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType325", None)
        self.__scxml_ScxmlParallelType325 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType324"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType324", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType324"):
                opp_val = getattr(value, "scxml_ScxmlStateType324", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType324", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlParallelType275(self):
        return self.__scxml_ScxmlParallelType275

    @scxml_ScxmlParallelType275.setter
    def scxml_ScxmlParallelType275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType275", None)
        self.__scxml_ScxmlParallelType275 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParallelType277"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType277", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParallelType277", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParallelType277"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType277", None)
                    
                    setattr(item, "scxml_ScxmlParallelType277", self)
                    

    @property
    def scxml_ScxmlParallelType282(self):
        return self.__scxml_ScxmlParallelType282

    @scxml_ScxmlParallelType282.setter
    def scxml_ScxmlParallelType282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType282", None)
        self.__scxml_ScxmlParallelType282 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDatamodelType283"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType283", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDatamodelType283", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDatamodelType283"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType283", None)
                    
                    setattr(item, "scxml_ScxmlDatamodelType283", self)
                    

    @property
    def scxml_ScxmlParallelType285(self):
        return self.__scxml_ScxmlParallelType285

    @scxml_ScxmlParallelType285.setter
    def scxml_ScxmlParallelType285(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType285", None)
        self.__scxml_ScxmlParallelType285 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlInvokeType286"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType286", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlInvokeType286", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlInvokeType286"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType286", None)
                    
                    setattr(item, "scxml_ScxmlInvokeType286", self)
                    

    @property
    def scxml_ScxmlParallelType273(self):
        return self.__scxml_ScxmlParallelType273

    @scxml_ScxmlParallelType273.setter
    def scxml_ScxmlParallelType273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlParallelType__scxml_ScxmlParallelType273", None)
        self.__scxml_ScxmlParallelType273 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlStateType274"):
                    opp_val = getattr(item, "scxml_ScxmlStateType274", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlStateType274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlStateType274"):
                    opp_val = getattr(item, "scxml_ScxmlStateType274", None)
                    
                    setattr(item, "scxml_ScxmlStateType274", self)
                    

class scxml_ScxmlInitialType:

    def __init__(self, scxmlExtraContent: str, scxmlExtraContent1: str, any1: str, anyAttribute: str, any: str, scxml_ScxmlInitialType: "scxml_DocumentRoot" = None, scxml_ScxmlInitialType204: "scxml_ScxmlTransitionType" = None, scxml_ScxmlInitialType319: "scxml_ScxmlStateType" = None):
        self.scxmlExtraContent = scxmlExtraContent
        self.scxmlExtraContent1 = scxmlExtraContent1
        self.any1 = any1
        self.anyAttribute = anyAttribute
        self.any = any
        self.scxml_ScxmlInitialType = scxml_ScxmlInitialType
        self.scxml_ScxmlInitialType204 = scxml_ScxmlInitialType204
        self.scxml_ScxmlInitialType319 = scxml_ScxmlInitialType319
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any1(self) -> str:
        return self.__any1

    @any1.setter
    def any1(self, any1: str):
        self.__any1 = any1

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def scxmlExtraContent1(self) -> str:
        return self.__scxmlExtraContent1

    @scxmlExtraContent1.setter
    def scxmlExtraContent1(self, scxmlExtraContent1: str):
        self.__scxmlExtraContent1 = scxmlExtraContent1

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlInitialType(self):
        return self.__scxml_ScxmlInitialType

    @scxml_ScxmlInitialType.setter
    def scxml_ScxmlInitialType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInitialType__scxml_ScxmlInitialType", None)
        self.__scxml_ScxmlInitialType = value
        
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

    @property
    def scxml_ScxmlInitialType319(self):
        return self.__scxml_ScxmlInitialType319

    @scxml_ScxmlInitialType319.setter
    def scxml_ScxmlInitialType319(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInitialType__scxml_ScxmlInitialType319", None)
        self.__scxml_ScxmlInitialType319 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType318"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType318", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType318"):
                opp_val = getattr(value, "scxml_ScxmlStateType318", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType318", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlInitialType204(self):
        return self.__scxml_ScxmlInitialType204

    @scxml_ScxmlInitialType204.setter
    def scxml_ScxmlInitialType204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInitialType__scxml_ScxmlInitialType204", None)
        self.__scxml_ScxmlInitialType204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType205"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType205", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlTransitionType205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType205"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType205", None)
                setattr(value, "scxml_ScxmlTransitionType205", self)

class scxml_ScxmlLogType:

    def __init__(self, scxmlExtraContent: str, any: str, expr: str, label: str, anyAttribute: str, scxml_ScxmlLogType: "scxml_DocumentRoot" = None, scxml_ScxmlLogType85: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlLogType118: "scxml_ScxmlForeachType" = None, scxml_ScxmlLogType145: "scxml_ScxmlIfType" = None, scxml_ScxmlLogType172: "scxml_ScxmlIfType" = None, scxml_ScxmlLogType199: "scxml_ScxmlIfType" = None, scxml_ScxmlLogType235: "scxml_ScxmlOnentryType" = None, scxml_ScxmlLogType259: "scxml_ScxmlOnexitType" = None, scxml_ScxmlLogType358: "scxml_ScxmlTransitionType" = None):
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.expr = expr
        self.label = label
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlLogType = scxml_ScxmlLogType
        self.scxml_ScxmlLogType85 = scxml_ScxmlLogType85
        self.scxml_ScxmlLogType118 = scxml_ScxmlLogType118
        self.scxml_ScxmlLogType145 = scxml_ScxmlLogType145
        self.scxml_ScxmlLogType172 = scxml_ScxmlLogType172
        self.scxml_ScxmlLogType199 = scxml_ScxmlLogType199
        self.scxml_ScxmlLogType235 = scxml_ScxmlLogType235
        self.scxml_ScxmlLogType259 = scxml_ScxmlLogType259
        self.scxml_ScxmlLogType358 = scxml_ScxmlLogType358
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

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
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def scxml_ScxmlLogType199(self):
        return self.__scxml_ScxmlLogType199

    @scxml_ScxmlLogType199.setter
    def scxml_ScxmlLogType199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType199", None)
        self.__scxml_ScxmlLogType199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType198"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType198", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType198"):
                opp_val = getattr(value, "scxml_ScxmlIfType198", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType198", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType(self):
        return self.__scxml_ScxmlLogType

    @scxml_ScxmlLogType.setter
    def scxml_ScxmlLogType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType", None)
        self.__scxml_ScxmlLogType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot35"):
                opp_val = getattr(old_value, "scxml_DocumentRoot35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot35"):
                opp_val = getattr(value, "scxml_DocumentRoot35", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType85(self):
        return self.__scxml_ScxmlLogType85

    @scxml_ScxmlLogType85.setter
    def scxml_ScxmlLogType85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType85", None)
        self.__scxml_ScxmlLogType85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType84"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType84", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType84"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType84", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType84", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType235(self):
        return self.__scxml_ScxmlLogType235

    @scxml_ScxmlLogType235.setter
    def scxml_ScxmlLogType235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType235", None)
        self.__scxml_ScxmlLogType235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType234"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType234", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType234"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType234", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType234", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType145(self):
        return self.__scxml_ScxmlLogType145

    @scxml_ScxmlLogType145.setter
    def scxml_ScxmlLogType145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType145", None)
        self.__scxml_ScxmlLogType145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType144"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType144"):
                opp_val = getattr(value, "scxml_ScxmlIfType144", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType259(self):
        return self.__scxml_ScxmlLogType259

    @scxml_ScxmlLogType259.setter
    def scxml_ScxmlLogType259(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType259", None)
        self.__scxml_ScxmlLogType259 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType258"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType258", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType258"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType258", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType258", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType358(self):
        return self.__scxml_ScxmlLogType358

    @scxml_ScxmlLogType358.setter
    def scxml_ScxmlLogType358(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType358", None)
        self.__scxml_ScxmlLogType358 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType357"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType357", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType357"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType357", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType357", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType118(self):
        return self.__scxml_ScxmlLogType118

    @scxml_ScxmlLogType118.setter
    def scxml_ScxmlLogType118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType118", None)
        self.__scxml_ScxmlLogType118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType117"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType117"):
                opp_val = getattr(value, "scxml_ScxmlForeachType117", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlLogType172(self):
        return self.__scxml_ScxmlLogType172

    @scxml_ScxmlLogType172.setter
    def scxml_ScxmlLogType172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlLogType__scxml_ScxmlLogType172", None)
        self.__scxml_ScxmlLogType172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType171"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType171"):
                opp_val = getattr(value, "scxml_ScxmlIfType171", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlInvokeType:

    def __init__(self, scxmlInvokeMix: str, any: str, autoforward: str, id: str, idlocation: str, namelist: str, anyAttribute: str, src: str, srcexpr: str, type: str, typeexpr: str, scxml_ScxmlInvokeType: "scxml_DocumentRoot" = None, scxml_ScxmlInvokeType207: set["scxml_ScxmlContentType"] = None, scxml_ScxmlInvokeType213: set["scxml_ScxmlFinalizeType"] = None, scxml_ScxmlInvokeType210: set["scxml_ScxmlParamType"] = None, scxml_ScxmlInvokeType286: "scxml_ScxmlParallelType" = None, scxml_ScxmlInvokeType337: "scxml_ScxmlStateType" = None):
        self.scxmlInvokeMix = scxmlInvokeMix
        self.any = any
        self.autoforward = autoforward
        self.id = id
        self.idlocation = idlocation
        self.namelist = namelist
        self.anyAttribute = anyAttribute
        self.src = src
        self.srcexpr = srcexpr
        self.type = type
        self.typeexpr = typeexpr
        self.scxml_ScxmlInvokeType = scxml_ScxmlInvokeType
        self.scxml_ScxmlInvokeType207 = scxml_ScxmlInvokeType207 if scxml_ScxmlInvokeType207 is not None else set()
        self.scxml_ScxmlInvokeType213 = scxml_ScxmlInvokeType213 if scxml_ScxmlInvokeType213 is not None else set()
        self.scxml_ScxmlInvokeType210 = scxml_ScxmlInvokeType210 if scxml_ScxmlInvokeType210 is not None else set()
        self.scxml_ScxmlInvokeType286 = scxml_ScxmlInvokeType286
        self.scxml_ScxmlInvokeType337 = scxml_ScxmlInvokeType337
        
    @property
    def namelist(self) -> str:
        return self.__namelist

    @namelist.setter
    def namelist(self, namelist: str):
        self.__namelist = namelist

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def srcexpr(self) -> str:
        return self.__srcexpr

    @srcexpr.setter
    def srcexpr(self, srcexpr: str):
        self.__srcexpr = srcexpr

    @property
    def typeexpr(self) -> str:
        return self.__typeexpr

    @typeexpr.setter
    def typeexpr(self, typeexpr: str):
        self.__typeexpr = typeexpr

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def idlocation(self) -> str:
        return self.__idlocation

    @idlocation.setter
    def idlocation(self, idlocation: str):
        self.__idlocation = idlocation

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def autoforward(self) -> str:
        return self.__autoforward

    @autoforward.setter
    def autoforward(self, autoforward: str):
        self.__autoforward = autoforward

    @property
    def scxmlInvokeMix(self) -> str:
        return self.__scxmlInvokeMix

    @scxmlInvokeMix.setter
    def scxmlInvokeMix(self, scxmlInvokeMix: str):
        self.__scxmlInvokeMix = scxmlInvokeMix

    @property
    def scxml_ScxmlInvokeType337(self):
        return self.__scxml_ScxmlInvokeType337

    @scxml_ScxmlInvokeType337.setter
    def scxml_ScxmlInvokeType337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType337", None)
        self.__scxml_ScxmlInvokeType337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType336"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType336", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType336"):
                opp_val = getattr(value, "scxml_ScxmlStateType336", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType336", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlInvokeType286(self):
        return self.__scxml_ScxmlInvokeType286

    @scxml_ScxmlInvokeType286.setter
    def scxml_ScxmlInvokeType286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType286", None)
        self.__scxml_ScxmlInvokeType286 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType285"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType285", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType285"):
                opp_val = getattr(value, "scxml_ScxmlParallelType285", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType285", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlInvokeType(self):
        return self.__scxml_ScxmlInvokeType

    @scxml_ScxmlInvokeType.setter
    def scxml_ScxmlInvokeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType", None)
        self.__scxml_ScxmlInvokeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot33"):
                opp_val = getattr(old_value, "scxml_DocumentRoot33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot33"):
                opp_val = getattr(value, "scxml_DocumentRoot33", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlInvokeType207(self):
        return self.__scxml_ScxmlInvokeType207

    @scxml_ScxmlInvokeType207.setter
    def scxml_ScxmlInvokeType207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType207", None)
        self.__scxml_ScxmlInvokeType207 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlContentType208"):
                    opp_val = getattr(item, "scxml_ScxmlContentType208", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlContentType208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlContentType208"):
                    opp_val = getattr(item, "scxml_ScxmlContentType208", None)
                    
                    setattr(item, "scxml_ScxmlContentType208", self)
                    

    @property
    def scxml_ScxmlInvokeType213(self):
        return self.__scxml_ScxmlInvokeType213

    @scxml_ScxmlInvokeType213.setter
    def scxml_ScxmlInvokeType213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType213", None)
        self.__scxml_ScxmlInvokeType213 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlFinalizeType214"):
                    opp_val = getattr(item, "scxml_ScxmlFinalizeType214", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlFinalizeType214", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlFinalizeType214"):
                    opp_val = getattr(item, "scxml_ScxmlFinalizeType214", None)
                    
                    setattr(item, "scxml_ScxmlFinalizeType214", self)
                    

    @property
    def scxml_ScxmlInvokeType210(self):
        return self.__scxml_ScxmlInvokeType210

    @scxml_ScxmlInvokeType210.setter
    def scxml_ScxmlInvokeType210(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlInvokeType__scxml_ScxmlInvokeType210", None)
        self.__scxml_ScxmlInvokeType210 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParamType211"):
                    opp_val = getattr(item, "scxml_ScxmlParamType211", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParamType211", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParamType211"):
                    opp_val = getattr(item, "scxml_ScxmlParamType211", None)
                    
                    setattr(item, "scxml_ScxmlParamType211", self)
                    

class scxml_ScxmlForeachType:

    def __init__(self, scxmlCoreExecutablecontent: str, any: str, item: str, anyAttribute: str, array: str, index: str, scxml_ScxmlForeachType: "scxml_DocumentRoot" = None, scxml_ScxmlForeachType73: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlForeachType99: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlForeachType102: set["scxml_ScxmlIfType"] = None, scxml_ScxmlForeachType106: "scxml_ScxmlForeachType" = None, scxml_ScxmlForeachType104: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlForeachType108: set["scxml_ScxmlSendType"] = None, scxml_ScxmlForeachType111: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlForeachType114: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlForeachType117: set["scxml_ScxmlLogType"] = None, scxml_ScxmlForeachType120: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlForeachType133: "scxml_ScxmlIfType" = None, scxml_ScxmlForeachType160: "scxml_ScxmlIfType" = None, scxml_ScxmlForeachType187: "scxml_ScxmlIfType" = None, scxml_ScxmlForeachType223: "scxml_ScxmlOnentryType" = None, scxml_ScxmlForeachType247: "scxml_ScxmlOnexitType" = None, scxml_ScxmlForeachType346: "scxml_ScxmlTransitionType" = None):
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.any = any
        self.item = item
        self.anyAttribute = anyAttribute
        self.array = array
        self.index = index
        self.scxml_ScxmlForeachType = scxml_ScxmlForeachType
        self.scxml_ScxmlForeachType73 = scxml_ScxmlForeachType73
        self.scxml_ScxmlForeachType99 = scxml_ScxmlForeachType99 if scxml_ScxmlForeachType99 is not None else set()
        self.scxml_ScxmlForeachType102 = scxml_ScxmlForeachType102 if scxml_ScxmlForeachType102 is not None else set()
        self.scxml_ScxmlForeachType106 = scxml_ScxmlForeachType106
        self.scxml_ScxmlForeachType104 = scxml_ScxmlForeachType104 if scxml_ScxmlForeachType104 is not None else set()
        self.scxml_ScxmlForeachType108 = scxml_ScxmlForeachType108 if scxml_ScxmlForeachType108 is not None else set()
        self.scxml_ScxmlForeachType111 = scxml_ScxmlForeachType111 if scxml_ScxmlForeachType111 is not None else set()
        self.scxml_ScxmlForeachType114 = scxml_ScxmlForeachType114 if scxml_ScxmlForeachType114 is not None else set()
        self.scxml_ScxmlForeachType117 = scxml_ScxmlForeachType117 if scxml_ScxmlForeachType117 is not None else set()
        self.scxml_ScxmlForeachType120 = scxml_ScxmlForeachType120 if scxml_ScxmlForeachType120 is not None else set()
        self.scxml_ScxmlForeachType133 = scxml_ScxmlForeachType133
        self.scxml_ScxmlForeachType160 = scxml_ScxmlForeachType160
        self.scxml_ScxmlForeachType187 = scxml_ScxmlForeachType187
        self.scxml_ScxmlForeachType223 = scxml_ScxmlForeachType223
        self.scxml_ScxmlForeachType247 = scxml_ScxmlForeachType247
        self.scxml_ScxmlForeachType346 = scxml_ScxmlForeachType346
        
    @property
    def array(self) -> str:
        return self.__array

    @array.setter
    def array(self, array: str):
        self.__array = array

    @property
    def item(self) -> str:
        return self.__item

    @item.setter
    def item(self, item: str):
        self.__item = item

    @property
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def index(self) -> str:
        return self.__index

    @index.setter
    def index(self, index: str):
        self.__index = index

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlForeachType117(self):
        return self.__scxml_ScxmlForeachType117

    @scxml_ScxmlForeachType117.setter
    def scxml_ScxmlForeachType117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType117", None)
        self.__scxml_ScxmlForeachType117 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType118"):
                    opp_val = getattr(item, "scxml_ScxmlLogType118", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType118", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType118"):
                    opp_val = getattr(item, "scxml_ScxmlLogType118", None)
                    
                    setattr(item, "scxml_ScxmlLogType118", self)
                    

    @property
    def scxml_ScxmlForeachType99(self):
        return self.__scxml_ScxmlForeachType99

    @scxml_ScxmlForeachType99.setter
    def scxml_ScxmlForeachType99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType99", None)
        self.__scxml_ScxmlForeachType99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType100"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType100", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType100"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType100", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType100", self)
                    

    @property
    def scxml_ScxmlForeachType111(self):
        return self.__scxml_ScxmlForeachType111

    @scxml_ScxmlForeachType111.setter
    def scxml_ScxmlForeachType111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType111", None)
        self.__scxml_ScxmlForeachType111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType112"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType112", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType112", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType112"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType112", None)
                    
                    setattr(item, "scxml_ScxmlScriptType112", self)
                    

    @property
    def scxml_ScxmlForeachType104(self):
        return self.__scxml_ScxmlForeachType104

    @scxml_ScxmlForeachType104.setter
    def scxml_ScxmlForeachType104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType104", None)
        self.__scxml_ScxmlForeachType104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType106"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType106", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType106"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType106", None)
                    
                    setattr(item, "scxml_ScxmlForeachType106", self)
                    

    @property
    def scxml_ScxmlForeachType114(self):
        return self.__scxml_ScxmlForeachType114

    @scxml_ScxmlForeachType114.setter
    def scxml_ScxmlForeachType114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType114", None)
        self.__scxml_ScxmlForeachType114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType115"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType115", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType115"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType115", None)
                    
                    setattr(item, "scxml_ScxmlAssignType115", self)
                    

    @property
    def scxml_ScxmlForeachType346(self):
        return self.__scxml_ScxmlForeachType346

    @scxml_ScxmlForeachType346.setter
    def scxml_ScxmlForeachType346(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType346", None)
        self.__scxml_ScxmlForeachType346 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType345"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType345", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType345"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType345", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType345", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType247(self):
        return self.__scxml_ScxmlForeachType247

    @scxml_ScxmlForeachType247.setter
    def scxml_ScxmlForeachType247(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType247", None)
        self.__scxml_ScxmlForeachType247 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType246"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType246", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType246"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType246", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType246", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType187(self):
        return self.__scxml_ScxmlForeachType187

    @scxml_ScxmlForeachType187.setter
    def scxml_ScxmlForeachType187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType187", None)
        self.__scxml_ScxmlForeachType187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType186"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType186", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType186"):
                opp_val = getattr(value, "scxml_ScxmlIfType186", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType186", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType106(self):
        return self.__scxml_ScxmlForeachType106

    @scxml_ScxmlForeachType106.setter
    def scxml_ScxmlForeachType106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType106", None)
        self.__scxml_ScxmlForeachType106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType104"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType104"):
                opp_val = getattr(value, "scxml_ScxmlForeachType104", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType108(self):
        return self.__scxml_ScxmlForeachType108

    @scxml_ScxmlForeachType108.setter
    def scxml_ScxmlForeachType108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType108", None)
        self.__scxml_ScxmlForeachType108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType109"):
                    opp_val = getattr(item, "scxml_ScxmlSendType109", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType109"):
                    opp_val = getattr(item, "scxml_ScxmlSendType109", None)
                    
                    setattr(item, "scxml_ScxmlSendType109", self)
                    

    @property
    def scxml_ScxmlForeachType73(self):
        return self.__scxml_ScxmlForeachType73

    @scxml_ScxmlForeachType73.setter
    def scxml_ScxmlForeachType73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType73", None)
        self.__scxml_ScxmlForeachType73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType72"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType72"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType72", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType102(self):
        return self.__scxml_ScxmlForeachType102

    @scxml_ScxmlForeachType102.setter
    def scxml_ScxmlForeachType102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType102", None)
        self.__scxml_ScxmlForeachType102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType103"):
                    opp_val = getattr(item, "scxml_ScxmlIfType103", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType103"):
                    opp_val = getattr(item, "scxml_ScxmlIfType103", None)
                    
                    setattr(item, "scxml_ScxmlIfType103", self)
                    

    @property
    def scxml_ScxmlForeachType223(self):
        return self.__scxml_ScxmlForeachType223

    @scxml_ScxmlForeachType223.setter
    def scxml_ScxmlForeachType223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType223", None)
        self.__scxml_ScxmlForeachType223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType222"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType222", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType222"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType222", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType222", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType160(self):
        return self.__scxml_ScxmlForeachType160

    @scxml_ScxmlForeachType160.setter
    def scxml_ScxmlForeachType160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType160", None)
        self.__scxml_ScxmlForeachType160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType159"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType159"):
                opp_val = getattr(value, "scxml_ScxmlIfType159", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType133(self):
        return self.__scxml_ScxmlForeachType133

    @scxml_ScxmlForeachType133.setter
    def scxml_ScxmlForeachType133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType133", None)
        self.__scxml_ScxmlForeachType133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType132"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType132"):
                opp_val = getattr(value, "scxml_ScxmlIfType132", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType(self):
        return self.__scxml_ScxmlForeachType

    @scxml_ScxmlForeachType.setter
    def scxml_ScxmlForeachType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType", None)
        self.__scxml_ScxmlForeachType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot25"):
                opp_val = getattr(old_value, "scxml_DocumentRoot25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot25"):
                opp_val = getattr(value, "scxml_DocumentRoot25", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlForeachType120(self):
        return self.__scxml_ScxmlForeachType120

    @scxml_ScxmlForeachType120.setter
    def scxml_ScxmlForeachType120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlForeachType__scxml_ScxmlForeachType120", None)
        self.__scxml_ScxmlForeachType120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType121"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType121", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType121"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType121", None)
                    
                    setattr(item, "scxml_ScxmlCancelType121", self)
                    

class scxml_ScxmlIfType:

    def __init__(self, scxmlCoreExecutablecontent: str, any: str, scxmlCoreExecutablecontent1: str, any1: str, scxmlCoreExecutablecontent2: str, any2: str, cond: str, anyAttribute: str, scxml_ScxmlIfType: "scxml_DocumentRoot" = None, scxml_ScxmlIfType70: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlIfType103: "scxml_ScxmlForeachType" = None, scxml_ScxmlIfType126: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlIfType130: "scxml_ScxmlIfType" = None, scxml_ScxmlIfType128: set["scxml_ScxmlIfType"] = None, scxml_ScxmlIfType135: set["scxml_ScxmlSendType"] = None, scxml_ScxmlIfType138: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlIfType141: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlIfType132: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlIfType150: "scxml_ScxmlElseifType" = None, scxml_ScxmlIfType153: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlIfType144: set["scxml_ScxmlLogType"] = None, scxml_ScxmlIfType147: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlIfType159: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlIfType162: set["scxml_ScxmlSendType"] = None, scxml_ScxmlIfType165: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlIfType157: "scxml_ScxmlIfType" = None, scxml_ScxmlIfType155: set["scxml_ScxmlIfType"] = None, scxml_ScxmlIfType174: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlIfType177: "scxml_ScxmlElseType" = None, scxml_ScxmlIfType168: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlIfType171: set["scxml_ScxmlLogType"] = None, scxml_ScxmlIfType186: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlIfType189: set["scxml_ScxmlSendType"] = None, scxml_ScxmlIfType192: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlIfType180: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlIfType184: "scxml_ScxmlIfType" = None, scxml_ScxmlIfType182: set["scxml_ScxmlIfType"] = None, scxml_ScxmlIfType201: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlIfType195: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlIfType198: set["scxml_ScxmlLogType"] = None, scxml_ScxmlIfType220: "scxml_ScxmlOnentryType" = None, scxml_ScxmlIfType244: "scxml_ScxmlOnexitType" = None, scxml_ScxmlIfType343: "scxml_ScxmlTransitionType" = None):
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.any = any
        self.scxmlCoreExecutablecontent1 = scxmlCoreExecutablecontent1
        self.any1 = any1
        self.scxmlCoreExecutablecontent2 = scxmlCoreExecutablecontent2
        self.any2 = any2
        self.cond = cond
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlIfType = scxml_ScxmlIfType
        self.scxml_ScxmlIfType70 = scxml_ScxmlIfType70
        self.scxml_ScxmlIfType103 = scxml_ScxmlIfType103
        self.scxml_ScxmlIfType126 = scxml_ScxmlIfType126 if scxml_ScxmlIfType126 is not None else set()
        self.scxml_ScxmlIfType130 = scxml_ScxmlIfType130
        self.scxml_ScxmlIfType128 = scxml_ScxmlIfType128 if scxml_ScxmlIfType128 is not None else set()
        self.scxml_ScxmlIfType135 = scxml_ScxmlIfType135 if scxml_ScxmlIfType135 is not None else set()
        self.scxml_ScxmlIfType138 = scxml_ScxmlIfType138 if scxml_ScxmlIfType138 is not None else set()
        self.scxml_ScxmlIfType141 = scxml_ScxmlIfType141 if scxml_ScxmlIfType141 is not None else set()
        self.scxml_ScxmlIfType132 = scxml_ScxmlIfType132 if scxml_ScxmlIfType132 is not None else set()
        self.scxml_ScxmlIfType150 = scxml_ScxmlIfType150
        self.scxml_ScxmlIfType153 = scxml_ScxmlIfType153 if scxml_ScxmlIfType153 is not None else set()
        self.scxml_ScxmlIfType144 = scxml_ScxmlIfType144 if scxml_ScxmlIfType144 is not None else set()
        self.scxml_ScxmlIfType147 = scxml_ScxmlIfType147 if scxml_ScxmlIfType147 is not None else set()
        self.scxml_ScxmlIfType159 = scxml_ScxmlIfType159 if scxml_ScxmlIfType159 is not None else set()
        self.scxml_ScxmlIfType162 = scxml_ScxmlIfType162 if scxml_ScxmlIfType162 is not None else set()
        self.scxml_ScxmlIfType165 = scxml_ScxmlIfType165 if scxml_ScxmlIfType165 is not None else set()
        self.scxml_ScxmlIfType157 = scxml_ScxmlIfType157
        self.scxml_ScxmlIfType155 = scxml_ScxmlIfType155 if scxml_ScxmlIfType155 is not None else set()
        self.scxml_ScxmlIfType174 = scxml_ScxmlIfType174 if scxml_ScxmlIfType174 is not None else set()
        self.scxml_ScxmlIfType177 = scxml_ScxmlIfType177
        self.scxml_ScxmlIfType168 = scxml_ScxmlIfType168 if scxml_ScxmlIfType168 is not None else set()
        self.scxml_ScxmlIfType171 = scxml_ScxmlIfType171 if scxml_ScxmlIfType171 is not None else set()
        self.scxml_ScxmlIfType186 = scxml_ScxmlIfType186 if scxml_ScxmlIfType186 is not None else set()
        self.scxml_ScxmlIfType189 = scxml_ScxmlIfType189 if scxml_ScxmlIfType189 is not None else set()
        self.scxml_ScxmlIfType192 = scxml_ScxmlIfType192 if scxml_ScxmlIfType192 is not None else set()
        self.scxml_ScxmlIfType180 = scxml_ScxmlIfType180 if scxml_ScxmlIfType180 is not None else set()
        self.scxml_ScxmlIfType184 = scxml_ScxmlIfType184
        self.scxml_ScxmlIfType182 = scxml_ScxmlIfType182 if scxml_ScxmlIfType182 is not None else set()
        self.scxml_ScxmlIfType201 = scxml_ScxmlIfType201 if scxml_ScxmlIfType201 is not None else set()
        self.scxml_ScxmlIfType195 = scxml_ScxmlIfType195 if scxml_ScxmlIfType195 is not None else set()
        self.scxml_ScxmlIfType198 = scxml_ScxmlIfType198 if scxml_ScxmlIfType198 is not None else set()
        self.scxml_ScxmlIfType220 = scxml_ScxmlIfType220
        self.scxml_ScxmlIfType244 = scxml_ScxmlIfType244
        self.scxml_ScxmlIfType343 = scxml_ScxmlIfType343
        
    @property
    def scxmlCoreExecutablecontent1(self) -> str:
        return self.__scxmlCoreExecutablecontent1

    @scxmlCoreExecutablecontent1.setter
    def scxmlCoreExecutablecontent1(self, scxmlCoreExecutablecontent1: str):
        self.__scxmlCoreExecutablecontent1 = scxmlCoreExecutablecontent1

    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

    @property
    def any1(self) -> str:
        return self.__any1

    @any1.setter
    def any1(self, any1: str):
        self.__any1 = any1

    @property
    def scxmlCoreExecutablecontent2(self) -> str:
        return self.__scxmlCoreExecutablecontent2

    @scxmlCoreExecutablecontent2.setter
    def scxmlCoreExecutablecontent2(self, scxmlCoreExecutablecontent2: str):
        self.__scxmlCoreExecutablecontent2 = scxmlCoreExecutablecontent2

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
    def any2(self) -> str:
        return self.__any2

    @any2.setter
    def any2(self, any2: str):
        self.__any2 = any2

    @property
    def scxml_ScxmlIfType174(self):
        return self.__scxml_ScxmlIfType174

    @scxml_ScxmlIfType174.setter
    def scxml_ScxmlIfType174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType174", None)
        self.__scxml_ScxmlIfType174 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType175"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType175", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType175", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType175"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType175", None)
                    
                    setattr(item, "scxml_ScxmlCancelType175", self)
                    

    @property
    def scxml_ScxmlIfType70(self):
        return self.__scxml_ScxmlIfType70

    @scxml_ScxmlIfType70.setter
    def scxml_ScxmlIfType70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType70", None)
        self.__scxml_ScxmlIfType70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType69"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType69"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType69", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType130(self):
        return self.__scxml_ScxmlIfType130

    @scxml_ScxmlIfType130.setter
    def scxml_ScxmlIfType130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType130", None)
        self.__scxml_ScxmlIfType130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType128"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType128"):
                opp_val = getattr(value, "scxml_ScxmlIfType128", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType168(self):
        return self.__scxml_ScxmlIfType168

    @scxml_ScxmlIfType168.setter
    def scxml_ScxmlIfType168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType168", None)
        self.__scxml_ScxmlIfType168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType169"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType169", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType169", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType169"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType169", None)
                    
                    setattr(item, "scxml_ScxmlAssignType169", self)
                    

    @property
    def scxml_ScxmlIfType153(self):
        return self.__scxml_ScxmlIfType153

    @scxml_ScxmlIfType153.setter
    def scxml_ScxmlIfType153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType153", None)
        self.__scxml_ScxmlIfType153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType154"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType154", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType154", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType154"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType154", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType154", self)
                    

    @property
    def scxml_ScxmlIfType147(self):
        return self.__scxml_ScxmlIfType147

    @scxml_ScxmlIfType147.setter
    def scxml_ScxmlIfType147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType147", None)
        self.__scxml_ScxmlIfType147 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType148"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType148", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType148", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType148"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType148", None)
                    
                    setattr(item, "scxml_ScxmlCancelType148", self)
                    

    @property
    def scxml_ScxmlIfType195(self):
        return self.__scxml_ScxmlIfType195

    @scxml_ScxmlIfType195.setter
    def scxml_ScxmlIfType195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType195", None)
        self.__scxml_ScxmlIfType195 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType196"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType196", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType196", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType196"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType196", None)
                    
                    setattr(item, "scxml_ScxmlAssignType196", self)
                    

    @property
    def scxml_ScxmlIfType343(self):
        return self.__scxml_ScxmlIfType343

    @scxml_ScxmlIfType343.setter
    def scxml_ScxmlIfType343(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType343", None)
        self.__scxml_ScxmlIfType343 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType342"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType342", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType342"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType342", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType342", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType132(self):
        return self.__scxml_ScxmlIfType132

    @scxml_ScxmlIfType132.setter
    def scxml_ScxmlIfType132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType132", None)
        self.__scxml_ScxmlIfType132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType133"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType133", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType133"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType133", None)
                    
                    setattr(item, "scxml_ScxmlForeachType133", self)
                    

    @property
    def scxml_ScxmlIfType198(self):
        return self.__scxml_ScxmlIfType198

    @scxml_ScxmlIfType198.setter
    def scxml_ScxmlIfType198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType198", None)
        self.__scxml_ScxmlIfType198 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType199"):
                    opp_val = getattr(item, "scxml_ScxmlLogType199", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType199", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType199"):
                    opp_val = getattr(item, "scxml_ScxmlLogType199", None)
                    
                    setattr(item, "scxml_ScxmlLogType199", self)
                    

    @property
    def scxml_ScxmlIfType186(self):
        return self.__scxml_ScxmlIfType186

    @scxml_ScxmlIfType186.setter
    def scxml_ScxmlIfType186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType186", None)
        self.__scxml_ScxmlIfType186 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType187"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType187", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType187", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType187"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType187", None)
                    
                    setattr(item, "scxml_ScxmlForeachType187", self)
                    

    @property
    def scxml_ScxmlIfType141(self):
        return self.__scxml_ScxmlIfType141

    @scxml_ScxmlIfType141.setter
    def scxml_ScxmlIfType141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType141", None)
        self.__scxml_ScxmlIfType141 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType142"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType142", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType142", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType142"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType142", None)
                    
                    setattr(item, "scxml_ScxmlAssignType142", self)
                    

    @property
    def scxml_ScxmlIfType189(self):
        return self.__scxml_ScxmlIfType189

    @scxml_ScxmlIfType189.setter
    def scxml_ScxmlIfType189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType189", None)
        self.__scxml_ScxmlIfType189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType190"):
                    opp_val = getattr(item, "scxml_ScxmlSendType190", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType190", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType190"):
                    opp_val = getattr(item, "scxml_ScxmlSendType190", None)
                    
                    setattr(item, "scxml_ScxmlSendType190", self)
                    

    @property
    def scxml_ScxmlIfType135(self):
        return self.__scxml_ScxmlIfType135

    @scxml_ScxmlIfType135.setter
    def scxml_ScxmlIfType135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType135", None)
        self.__scxml_ScxmlIfType135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType136"):
                    opp_val = getattr(item, "scxml_ScxmlSendType136", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType136"):
                    opp_val = getattr(item, "scxml_ScxmlSendType136", None)
                    
                    setattr(item, "scxml_ScxmlSendType136", self)
                    

    @property
    def scxml_ScxmlIfType162(self):
        return self.__scxml_ScxmlIfType162

    @scxml_ScxmlIfType162.setter
    def scxml_ScxmlIfType162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType162", None)
        self.__scxml_ScxmlIfType162 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType163"):
                    opp_val = getattr(item, "scxml_ScxmlSendType163", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType163", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType163"):
                    opp_val = getattr(item, "scxml_ScxmlSendType163", None)
                    
                    setattr(item, "scxml_ScxmlSendType163", self)
                    

    @property
    def scxml_ScxmlIfType159(self):
        return self.__scxml_ScxmlIfType159

    @scxml_ScxmlIfType159.setter
    def scxml_ScxmlIfType159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType159", None)
        self.__scxml_ScxmlIfType159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType160"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType160", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType160", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType160"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType160", None)
                    
                    setattr(item, "scxml_ScxmlForeachType160", self)
                    

    @property
    def scxml_ScxmlIfType184(self):
        return self.__scxml_ScxmlIfType184

    @scxml_ScxmlIfType184.setter
    def scxml_ScxmlIfType184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType184", None)
        self.__scxml_ScxmlIfType184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType182"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType182"):
                opp_val = getattr(value, "scxml_ScxmlIfType182", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType180(self):
        return self.__scxml_ScxmlIfType180

    @scxml_ScxmlIfType180.setter
    def scxml_ScxmlIfType180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType180", None)
        self.__scxml_ScxmlIfType180 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType181"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType181", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType181", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType181"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType181", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType181", self)
                    

    @property
    def scxml_ScxmlIfType155(self):
        return self.__scxml_ScxmlIfType155

    @scxml_ScxmlIfType155.setter
    def scxml_ScxmlIfType155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType155", None)
        self.__scxml_ScxmlIfType155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType157"):
                    opp_val = getattr(item, "scxml_ScxmlIfType157", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType157", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType157"):
                    opp_val = getattr(item, "scxml_ScxmlIfType157", None)
                    
                    setattr(item, "scxml_ScxmlIfType157", self)
                    

    @property
    def scxml_ScxmlIfType171(self):
        return self.__scxml_ScxmlIfType171

    @scxml_ScxmlIfType171.setter
    def scxml_ScxmlIfType171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType171", None)
        self.__scxml_ScxmlIfType171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType172"):
                    opp_val = getattr(item, "scxml_ScxmlLogType172", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType172", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType172"):
                    opp_val = getattr(item, "scxml_ScxmlLogType172", None)
                    
                    setattr(item, "scxml_ScxmlLogType172", self)
                    

    @property
    def scxml_ScxmlIfType182(self):
        return self.__scxml_ScxmlIfType182

    @scxml_ScxmlIfType182.setter
    def scxml_ScxmlIfType182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType182", None)
        self.__scxml_ScxmlIfType182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType184"):
                    opp_val = getattr(item, "scxml_ScxmlIfType184", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType184", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType184"):
                    opp_val = getattr(item, "scxml_ScxmlIfType184", None)
                    
                    setattr(item, "scxml_ScxmlIfType184", self)
                    

    @property
    def scxml_ScxmlIfType150(self):
        return self.__scxml_ScxmlIfType150

    @scxml_ScxmlIfType150.setter
    def scxml_ScxmlIfType150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType150", None)
        self.__scxml_ScxmlIfType150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlElseifType151"):
                opp_val = getattr(old_value, "scxml_ScxmlElseifType151", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlElseifType151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlElseifType151"):
                opp_val = getattr(value, "scxml_ScxmlElseifType151", None)
                setattr(value, "scxml_ScxmlElseifType151", self)

    @property
    def scxml_ScxmlIfType244(self):
        return self.__scxml_ScxmlIfType244

    @scxml_ScxmlIfType244.setter
    def scxml_ScxmlIfType244(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType244", None)
        self.__scxml_ScxmlIfType244 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType243"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType243", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType243"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType243", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType243", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType128(self):
        return self.__scxml_ScxmlIfType128

    @scxml_ScxmlIfType128.setter
    def scxml_ScxmlIfType128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType128", None)
        self.__scxml_ScxmlIfType128 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType130"):
                    opp_val = getattr(item, "scxml_ScxmlIfType130", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType130"):
                    opp_val = getattr(item, "scxml_ScxmlIfType130", None)
                    
                    setattr(item, "scxml_ScxmlIfType130", self)
                    

    @property
    def scxml_ScxmlIfType165(self):
        return self.__scxml_ScxmlIfType165

    @scxml_ScxmlIfType165.setter
    def scxml_ScxmlIfType165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType165", None)
        self.__scxml_ScxmlIfType165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType166"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType166", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType166"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType166", None)
                    
                    setattr(item, "scxml_ScxmlScriptType166", self)
                    

    @property
    def scxml_ScxmlIfType157(self):
        return self.__scxml_ScxmlIfType157

    @scxml_ScxmlIfType157.setter
    def scxml_ScxmlIfType157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType157", None)
        self.__scxml_ScxmlIfType157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType155"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType155"):
                opp_val = getattr(value, "scxml_ScxmlIfType155", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType138(self):
        return self.__scxml_ScxmlIfType138

    @scxml_ScxmlIfType138.setter
    def scxml_ScxmlIfType138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType138", None)
        self.__scxml_ScxmlIfType138 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType139"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType139", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType139", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType139"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType139", None)
                    
                    setattr(item, "scxml_ScxmlScriptType139", self)
                    

    @property
    def scxml_ScxmlIfType126(self):
        return self.__scxml_ScxmlIfType126

    @scxml_ScxmlIfType126.setter
    def scxml_ScxmlIfType126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType126", None)
        self.__scxml_ScxmlIfType126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType127"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType127", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType127"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType127", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType127", self)
                    

    @property
    def scxml_ScxmlIfType177(self):
        return self.__scxml_ScxmlIfType177

    @scxml_ScxmlIfType177.setter
    def scxml_ScxmlIfType177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType177", None)
        self.__scxml_ScxmlIfType177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlElseType178"):
                opp_val = getattr(old_value, "scxml_ScxmlElseType178", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlElseType178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlElseType178"):
                opp_val = getattr(value, "scxml_ScxmlElseType178", None)
                setattr(value, "scxml_ScxmlElseType178", self)

    @property
    def scxml_ScxmlIfType192(self):
        return self.__scxml_ScxmlIfType192

    @scxml_ScxmlIfType192.setter
    def scxml_ScxmlIfType192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType192", None)
        self.__scxml_ScxmlIfType192 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType193"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType193", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType193", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType193"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType193", None)
                    
                    setattr(item, "scxml_ScxmlScriptType193", self)
                    

    @property
    def scxml_ScxmlIfType(self):
        return self.__scxml_ScxmlIfType

    @scxml_ScxmlIfType.setter
    def scxml_ScxmlIfType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType", None)
        self.__scxml_ScxmlIfType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot29"):
                opp_val = getattr(old_value, "scxml_DocumentRoot29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot29"):
                opp_val = getattr(value, "scxml_DocumentRoot29", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType201(self):
        return self.__scxml_ScxmlIfType201

    @scxml_ScxmlIfType201.setter
    def scxml_ScxmlIfType201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType201", None)
        self.__scxml_ScxmlIfType201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType202"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType202", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType202", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType202"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType202", None)
                    
                    setattr(item, "scxml_ScxmlCancelType202", self)
                    

    @property
    def scxml_ScxmlIfType144(self):
        return self.__scxml_ScxmlIfType144

    @scxml_ScxmlIfType144.setter
    def scxml_ScxmlIfType144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType144", None)
        self.__scxml_ScxmlIfType144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType145"):
                    opp_val = getattr(item, "scxml_ScxmlLogType145", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType145"):
                    opp_val = getattr(item, "scxml_ScxmlLogType145", None)
                    
                    setattr(item, "scxml_ScxmlLogType145", self)
                    

    @property
    def scxml_ScxmlIfType220(self):
        return self.__scxml_ScxmlIfType220

    @scxml_ScxmlIfType220.setter
    def scxml_ScxmlIfType220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType220", None)
        self.__scxml_ScxmlIfType220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType219"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType219", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType219"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType219", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType219", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlIfType103(self):
        return self.__scxml_ScxmlIfType103

    @scxml_ScxmlIfType103.setter
    def scxml_ScxmlIfType103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlIfType__scxml_ScxmlIfType103", None)
        self.__scxml_ScxmlIfType103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType102"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType102"):
                opp_val = getattr(value, "scxml_ScxmlForeachType102", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlHistoryType:

    def __init__(self, scxmlExtraContent1: str, scxmlExtraContent: str, any: str, anyAttribute: str, any1: str, id: str, type: str, scxml_ScxmlHistoryType: "scxml_DocumentRoot" = None, scxml_ScxmlHistoryType123: "scxml_ScxmlTransitionType" = None, scxml_ScxmlHistoryType280: "scxml_ScxmlParallelType" = None, scxml_ScxmlHistoryType331: "scxml_ScxmlStateType" = None):
        self.scxmlExtraContent1 = scxmlExtraContent1
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.anyAttribute = anyAttribute
        self.any1 = any1
        self.id = id
        self.type = type
        self.scxml_ScxmlHistoryType = scxml_ScxmlHistoryType
        self.scxml_ScxmlHistoryType123 = scxml_ScxmlHistoryType123
        self.scxml_ScxmlHistoryType280 = scxml_ScxmlHistoryType280
        self.scxml_ScxmlHistoryType331 = scxml_ScxmlHistoryType331
        
    @property
    def any1(self) -> str:
        return self.__any1

    @any1.setter
    def any1(self, any1: str):
        self.__any1 = any1

    @property
    def scxmlExtraContent1(self) -> str:
        return self.__scxmlExtraContent1

    @scxmlExtraContent1.setter
    def scxmlExtraContent1(self, scxmlExtraContent1: str):
        self.__scxmlExtraContent1 = scxmlExtraContent1

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlHistoryType123(self):
        return self.__scxml_ScxmlHistoryType123

    @scxml_ScxmlHistoryType123.setter
    def scxml_ScxmlHistoryType123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlHistoryType__scxml_ScxmlHistoryType123", None)
        self.__scxml_ScxmlHistoryType123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType124"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType124", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlTransitionType124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType124"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType124", None)
                setattr(value, "scxml_ScxmlTransitionType124", self)

    @property
    def scxml_ScxmlHistoryType280(self):
        return self.__scxml_ScxmlHistoryType280

    @scxml_ScxmlHistoryType280.setter
    def scxml_ScxmlHistoryType280(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlHistoryType__scxml_ScxmlHistoryType280", None)
        self.__scxml_ScxmlHistoryType280 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType279"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType279", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType279"):
                opp_val = getattr(value, "scxml_ScxmlParallelType279", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType279", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlHistoryType(self):
        return self.__scxml_ScxmlHistoryType

    @scxml_ScxmlHistoryType.setter
    def scxml_ScxmlHistoryType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlHistoryType__scxml_ScxmlHistoryType", None)
        self.__scxml_ScxmlHistoryType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot27"):
                opp_val = getattr(old_value, "scxml_DocumentRoot27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot27"):
                opp_val = getattr(value, "scxml_DocumentRoot27", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlHistoryType331(self):
        return self.__scxml_ScxmlHistoryType331

    @scxml_ScxmlHistoryType331.setter
    def scxml_ScxmlHistoryType331(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlHistoryType__scxml_ScxmlHistoryType331", None)
        self.__scxml_ScxmlHistoryType331 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType330"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType330", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType330"):
                opp_val = getattr(value, "scxml_ScxmlStateType330", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType330", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlElseType:

    def __init__(self, anyAttribute: str, scxml_ScxmlElseType: "scxml_DocumentRoot" = None, scxml_ScxmlElseType178: "scxml_ScxmlIfType" = None):
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlElseType = scxml_ScxmlElseType
        self.scxml_ScxmlElseType178 = scxml_ScxmlElseType178
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlElseType(self):
        return self.__scxml_ScxmlElseType

    @scxml_ScxmlElseType.setter
    def scxml_ScxmlElseType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlElseType__scxml_ScxmlElseType", None)
        self.__scxml_ScxmlElseType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot17"):
                opp_val = getattr(old_value, "scxml_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot17"):
                opp_val = getattr(value, "scxml_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlElseType178(self):
        return self.__scxml_ScxmlElseType178

    @scxml_ScxmlElseType178.setter
    def scxml_ScxmlElseType178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlElseType__scxml_ScxmlElseType178", None)
        self.__scxml_ScxmlElseType178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType177"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType177", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlIfType177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType177"):
                opp_val = getattr(value, "scxml_ScxmlIfType177", None)
                setattr(value, "scxml_ScxmlIfType177", self)

class scxml_ScxmlDonedataType:

    def __init__(self, anyAttribute: str, scxml_ScxmlDonedataType: "scxml_DocumentRoot" = None, scxml_ScxmlDonedataType60: "scxml_ScxmlContentType" = None, scxml_ScxmlDonedataType63: set["scxml_ScxmlParamType"] = None, scxml_ScxmlDonedataType97: "scxml_ScxmlFinalType" = None):
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlDonedataType = scxml_ScxmlDonedataType
        self.scxml_ScxmlDonedataType60 = scxml_ScxmlDonedataType60
        self.scxml_ScxmlDonedataType63 = scxml_ScxmlDonedataType63 if scxml_ScxmlDonedataType63 is not None else set()
        self.scxml_ScxmlDonedataType97 = scxml_ScxmlDonedataType97
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlDonedataType97(self):
        return self.__scxml_ScxmlDonedataType97

    @scxml_ScxmlDonedataType97.setter
    def scxml_ScxmlDonedataType97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDonedataType__scxml_ScxmlDonedataType97", None)
        self.__scxml_ScxmlDonedataType97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalType96"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalType96", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalType96"):
                opp_val = getattr(value, "scxml_ScxmlFinalType96", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalType96", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDonedataType60(self):
        return self.__scxml_ScxmlDonedataType60

    @scxml_ScxmlDonedataType60.setter
    def scxml_ScxmlDonedataType60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDonedataType__scxml_ScxmlDonedataType60", None)
        self.__scxml_ScxmlDonedataType60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlContentType61"):
                opp_val = getattr(old_value, "scxml_ScxmlContentType61", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlContentType61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlContentType61"):
                opp_val = getattr(value, "scxml_ScxmlContentType61", None)
                setattr(value, "scxml_ScxmlContentType61", self)

    @property
    def scxml_ScxmlDonedataType(self):
        return self.__scxml_ScxmlDonedataType

    @scxml_ScxmlDonedataType.setter
    def scxml_ScxmlDonedataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDonedataType__scxml_ScxmlDonedataType", None)
        self.__scxml_ScxmlDonedataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot15"):
                opp_val = getattr(old_value, "scxml_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot15"):
                opp_val = getattr(value, "scxml_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDonedataType63(self):
        return self.__scxml_ScxmlDonedataType63

    @scxml_ScxmlDonedataType63.setter
    def scxml_ScxmlDonedataType63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDonedataType__scxml_ScxmlDonedataType63", None)
        self.__scxml_ScxmlDonedataType63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParamType64"):
                    opp_val = getattr(item, "scxml_ScxmlParamType64", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParamType64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParamType64"):
                    opp_val = getattr(item, "scxml_ScxmlParamType64", None)
                    
                    setattr(item, "scxml_ScxmlParamType64", self)
                    

class scxml_ScxmlFinalizeType:

    def __init__(self, scxmlCoreExecutablecontent: str, any: str, anyAttribute: str, scxml_ScxmlFinalizeType: "scxml_DocumentRoot" = None, scxml_ScxmlFinalizeType66: set["scxml_ScxmlRaiseType"] = None, scxml_ScxmlFinalizeType69: set["scxml_ScxmlIfType"] = None, scxml_ScxmlFinalizeType72: set["scxml_ScxmlForeachType"] = None, scxml_ScxmlFinalizeType75: set["scxml_ScxmlSendType"] = None, scxml_ScxmlFinalizeType78: set["scxml_ScxmlScriptType"] = None, scxml_ScxmlFinalizeType81: set["scxml_ScxmlAssignType"] = None, scxml_ScxmlFinalizeType84: set["scxml_ScxmlLogType"] = None, scxml_ScxmlFinalizeType87: set["scxml_ScxmlCancelType"] = None, scxml_ScxmlFinalizeType214: "scxml_ScxmlInvokeType" = None):
        self.scxmlCoreExecutablecontent = scxmlCoreExecutablecontent
        self.any = any
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlFinalizeType = scxml_ScxmlFinalizeType
        self.scxml_ScxmlFinalizeType66 = scxml_ScxmlFinalizeType66 if scxml_ScxmlFinalizeType66 is not None else set()
        self.scxml_ScxmlFinalizeType69 = scxml_ScxmlFinalizeType69 if scxml_ScxmlFinalizeType69 is not None else set()
        self.scxml_ScxmlFinalizeType72 = scxml_ScxmlFinalizeType72 if scxml_ScxmlFinalizeType72 is not None else set()
        self.scxml_ScxmlFinalizeType75 = scxml_ScxmlFinalizeType75 if scxml_ScxmlFinalizeType75 is not None else set()
        self.scxml_ScxmlFinalizeType78 = scxml_ScxmlFinalizeType78 if scxml_ScxmlFinalizeType78 is not None else set()
        self.scxml_ScxmlFinalizeType81 = scxml_ScxmlFinalizeType81 if scxml_ScxmlFinalizeType81 is not None else set()
        self.scxml_ScxmlFinalizeType84 = scxml_ScxmlFinalizeType84 if scxml_ScxmlFinalizeType84 is not None else set()
        self.scxml_ScxmlFinalizeType87 = scxml_ScxmlFinalizeType87 if scxml_ScxmlFinalizeType87 is not None else set()
        self.scxml_ScxmlFinalizeType214 = scxml_ScxmlFinalizeType214
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxmlCoreExecutablecontent(self) -> str:
        return self.__scxmlCoreExecutablecontent

    @scxmlCoreExecutablecontent.setter
    def scxmlCoreExecutablecontent(self, scxmlCoreExecutablecontent: str):
        self.__scxmlCoreExecutablecontent = scxmlCoreExecutablecontent

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlFinalizeType81(self):
        return self.__scxml_ScxmlFinalizeType81

    @scxml_ScxmlFinalizeType81.setter
    def scxml_ScxmlFinalizeType81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType81", None)
        self.__scxml_ScxmlFinalizeType81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType82"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType82", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType82"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType82", None)
                    
                    setattr(item, "scxml_ScxmlAssignType82", self)
                    

    @property
    def scxml_ScxmlFinalizeType66(self):
        return self.__scxml_ScxmlFinalizeType66

    @scxml_ScxmlFinalizeType66.setter
    def scxml_ScxmlFinalizeType66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType66", None)
        self.__scxml_ScxmlFinalizeType66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType67"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType67", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType67", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType67"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType67", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType67", self)
                    

    @property
    def scxml_ScxmlFinalizeType72(self):
        return self.__scxml_ScxmlFinalizeType72

    @scxml_ScxmlFinalizeType72.setter
    def scxml_ScxmlFinalizeType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType72", None)
        self.__scxml_ScxmlFinalizeType72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType73"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType73", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType73"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType73", None)
                    
                    setattr(item, "scxml_ScxmlForeachType73", self)
                    

    @property
    def scxml_ScxmlFinalizeType84(self):
        return self.__scxml_ScxmlFinalizeType84

    @scxml_ScxmlFinalizeType84.setter
    def scxml_ScxmlFinalizeType84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType84", None)
        self.__scxml_ScxmlFinalizeType84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType85"):
                    opp_val = getattr(item, "scxml_ScxmlLogType85", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType85"):
                    opp_val = getattr(item, "scxml_ScxmlLogType85", None)
                    
                    setattr(item, "scxml_ScxmlLogType85", self)
                    

    @property
    def scxml_ScxmlFinalizeType78(self):
        return self.__scxml_ScxmlFinalizeType78

    @scxml_ScxmlFinalizeType78.setter
    def scxml_ScxmlFinalizeType78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType78", None)
        self.__scxml_ScxmlFinalizeType78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScriptType79"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType79", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScriptType79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScriptType79"):
                    opp_val = getattr(item, "scxml_ScxmlScriptType79", None)
                    
                    setattr(item, "scxml_ScxmlScriptType79", self)
                    

    @property
    def scxml_ScxmlFinalizeType75(self):
        return self.__scxml_ScxmlFinalizeType75

    @scxml_ScxmlFinalizeType75.setter
    def scxml_ScxmlFinalizeType75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType75", None)
        self.__scxml_ScxmlFinalizeType75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlSendType76"):
                    opp_val = getattr(item, "scxml_ScxmlSendType76", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlSendType76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlSendType76"):
                    opp_val = getattr(item, "scxml_ScxmlSendType76", None)
                    
                    setattr(item, "scxml_ScxmlSendType76", self)
                    

    @property
    def scxml_ScxmlFinalizeType(self):
        return self.__scxml_ScxmlFinalizeType

    @scxml_ScxmlFinalizeType.setter
    def scxml_ScxmlFinalizeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType", None)
        self.__scxml_ScxmlFinalizeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot23"):
                opp_val = getattr(old_value, "scxml_DocumentRoot23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot23"):
                opp_val = getattr(value, "scxml_DocumentRoot23", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlFinalizeType87(self):
        return self.__scxml_ScxmlFinalizeType87

    @scxml_ScxmlFinalizeType87.setter
    def scxml_ScxmlFinalizeType87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType87", None)
        self.__scxml_ScxmlFinalizeType87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType88"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType88", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType88"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType88", None)
                    
                    setattr(item, "scxml_ScxmlCancelType88", self)
                    

    @property
    def scxml_ScxmlFinalizeType214(self):
        return self.__scxml_ScxmlFinalizeType214

    @scxml_ScxmlFinalizeType214.setter
    def scxml_ScxmlFinalizeType214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType214", None)
        self.__scxml_ScxmlFinalizeType214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlInvokeType213"):
                opp_val = getattr(old_value, "scxml_ScxmlInvokeType213", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlInvokeType213"):
                opp_val = getattr(value, "scxml_ScxmlInvokeType213", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlInvokeType213", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlFinalizeType69(self):
        return self.__scxml_ScxmlFinalizeType69

    @scxml_ScxmlFinalizeType69.setter
    def scxml_ScxmlFinalizeType69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalizeType__scxml_ScxmlFinalizeType69", None)
        self.__scxml_ScxmlFinalizeType69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType70"):
                    opp_val = getattr(item, "scxml_ScxmlIfType70", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType70"):
                    opp_val = getattr(item, "scxml_ScxmlIfType70", None)
                    
                    setattr(item, "scxml_ScxmlIfType70", self)
                    

class scxml_ScxmlFinalType:

    def __init__(self, scxmlFinalMix: str, any: str, id: str, anyAttribute: str, scxml_ScxmlFinalType: "scxml_DocumentRoot" = None, scxml_ScxmlFinalType90: set["scxml_ScxmlOnentryType"] = None, scxml_ScxmlFinalType93: set["scxml_ScxmlOnexitType"] = None, scxml_ScxmlFinalType96: set["scxml_ScxmlDonedataType"] = None, scxml_ScxmlFinalType295: "scxml_ScxmlScxmlType" = None, scxml_ScxmlFinalType328: "scxml_ScxmlStateType" = None):
        self.scxmlFinalMix = scxmlFinalMix
        self.any = any
        self.id = id
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlFinalType = scxml_ScxmlFinalType
        self.scxml_ScxmlFinalType90 = scxml_ScxmlFinalType90 if scxml_ScxmlFinalType90 is not None else set()
        self.scxml_ScxmlFinalType93 = scxml_ScxmlFinalType93 if scxml_ScxmlFinalType93 is not None else set()
        self.scxml_ScxmlFinalType96 = scxml_ScxmlFinalType96 if scxml_ScxmlFinalType96 is not None else set()
        self.scxml_ScxmlFinalType295 = scxml_ScxmlFinalType295
        self.scxml_ScxmlFinalType328 = scxml_ScxmlFinalType328
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def scxmlFinalMix(self) -> str:
        return self.__scxmlFinalMix

    @scxmlFinalMix.setter
    def scxmlFinalMix(self, scxmlFinalMix: str):
        self.__scxmlFinalMix = scxmlFinalMix

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlFinalType328(self):
        return self.__scxml_ScxmlFinalType328

    @scxml_ScxmlFinalType328.setter
    def scxml_ScxmlFinalType328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType328", None)
        self.__scxml_ScxmlFinalType328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType327"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType327", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType327"):
                opp_val = getattr(value, "scxml_ScxmlStateType327", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType327", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlFinalType96(self):
        return self.__scxml_ScxmlFinalType96

    @scxml_ScxmlFinalType96.setter
    def scxml_ScxmlFinalType96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType96", None)
        self.__scxml_ScxmlFinalType96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDonedataType97"):
                    opp_val = getattr(item, "scxml_ScxmlDonedataType97", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDonedataType97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDonedataType97"):
                    opp_val = getattr(item, "scxml_ScxmlDonedataType97", None)
                    
                    setattr(item, "scxml_ScxmlDonedataType97", self)
                    

    @property
    def scxml_ScxmlFinalType295(self):
        return self.__scxml_ScxmlFinalType295

    @scxml_ScxmlFinalType295.setter
    def scxml_ScxmlFinalType295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType295", None)
        self.__scxml_ScxmlFinalType295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType294"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType294"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType294", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType294", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlFinalType93(self):
        return self.__scxml_ScxmlFinalType93

    @scxml_ScxmlFinalType93.setter
    def scxml_ScxmlFinalType93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType93", None)
        self.__scxml_ScxmlFinalType93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexitType94"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType94", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexitType94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexitType94"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType94", None)
                    
                    setattr(item, "scxml_ScxmlOnexitType94", self)
                    

    @property
    def scxml_ScxmlFinalType(self):
        return self.__scxml_ScxmlFinalType

    @scxml_ScxmlFinalType.setter
    def scxml_ScxmlFinalType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType", None)
        self.__scxml_ScxmlFinalType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot21"):
                opp_val = getattr(old_value, "scxml_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot21"):
                opp_val = getattr(value, "scxml_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlFinalType90(self):
        return self.__scxml_ScxmlFinalType90

    @scxml_ScxmlFinalType90.setter
    def scxml_ScxmlFinalType90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlFinalType__scxml_ScxmlFinalType90", None)
        self.__scxml_ScxmlFinalType90 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnentryType91"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType91", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnentryType91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnentryType91"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType91", None)
                    
                    setattr(item, "scxml_ScxmlOnentryType91", self)
                    

class scxml_ScxmlElseifType:

    def __init__(self, cond: str, anyAttribute: str, scxml_ScxmlElseifType: "scxml_DocumentRoot" = None, scxml_ScxmlElseifType151: "scxml_ScxmlIfType" = None):
        self.cond = cond
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlElseifType = scxml_ScxmlElseifType
        self.scxml_ScxmlElseifType151 = scxml_ScxmlElseifType151
        
    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def cond(self) -> str:
        return self.__cond

    @cond.setter
    def cond(self, cond: str):
        self.__cond = cond

    @property
    def scxml_ScxmlElseifType(self):
        return self.__scxml_ScxmlElseifType

    @scxml_ScxmlElseifType.setter
    def scxml_ScxmlElseifType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlElseifType__scxml_ScxmlElseifType", None)
        self.__scxml_ScxmlElseifType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot19"):
                opp_val = getattr(old_value, "scxml_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot19"):
                opp_val = getattr(value, "scxml_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlElseifType151(self):
        return self.__scxml_ScxmlElseifType151

    @scxml_ScxmlElseifType151.setter
    def scxml_ScxmlElseifType151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlElseifType__scxml_ScxmlElseifType151", None)
        self.__scxml_ScxmlElseifType151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType150"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType150", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlIfType150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType150"):
                opp_val = getattr(value, "scxml_ScxmlIfType150", None)
                setattr(value, "scxml_ScxmlIfType150", self)

class scxml_ScxmlCancelType:

    def __init__(self, anyAttribute: str, scxmlExtraContent: str, any: str, sendid: str, sendidexpr: str, scxml_ScxmlCancelType: "scxml_DocumentRoot" = None, scxml_ScxmlCancelType88: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlCancelType121: "scxml_ScxmlForeachType" = None, scxml_ScxmlCancelType148: "scxml_ScxmlIfType" = None, scxml_ScxmlCancelType175: "scxml_ScxmlIfType" = None, scxml_ScxmlCancelType202: "scxml_ScxmlIfType" = None, scxml_ScxmlCancelType238: "scxml_ScxmlOnentryType" = None, scxml_ScxmlCancelType262: "scxml_ScxmlOnexitType" = None, scxml_ScxmlCancelType361: "scxml_ScxmlTransitionType" = None):
        self.anyAttribute = anyAttribute
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.sendid = sendid
        self.sendidexpr = sendidexpr
        self.scxml_ScxmlCancelType = scxml_ScxmlCancelType
        self.scxml_ScxmlCancelType88 = scxml_ScxmlCancelType88
        self.scxml_ScxmlCancelType121 = scxml_ScxmlCancelType121
        self.scxml_ScxmlCancelType148 = scxml_ScxmlCancelType148
        self.scxml_ScxmlCancelType175 = scxml_ScxmlCancelType175
        self.scxml_ScxmlCancelType202 = scxml_ScxmlCancelType202
        self.scxml_ScxmlCancelType238 = scxml_ScxmlCancelType238
        self.scxml_ScxmlCancelType262 = scxml_ScxmlCancelType262
        self.scxml_ScxmlCancelType361 = scxml_ScxmlCancelType361
        
    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def sendidexpr(self) -> str:
        return self.__sendidexpr

    @sendidexpr.setter
    def sendidexpr(self, sendidexpr: str):
        self.__sendidexpr = sendidexpr

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def sendid(self) -> str:
        return self.__sendid

    @sendid.setter
    def sendid(self, sendid: str):
        self.__sendid = sendid

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlCancelType238(self):
        return self.__scxml_ScxmlCancelType238

    @scxml_ScxmlCancelType238.setter
    def scxml_ScxmlCancelType238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType238", None)
        self.__scxml_ScxmlCancelType238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType237"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType237"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType237", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType202(self):
        return self.__scxml_ScxmlCancelType202

    @scxml_ScxmlCancelType202.setter
    def scxml_ScxmlCancelType202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType202", None)
        self.__scxml_ScxmlCancelType202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType201"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType201", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType201"):
                opp_val = getattr(value, "scxml_ScxmlIfType201", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType201", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType148(self):
        return self.__scxml_ScxmlCancelType148

    @scxml_ScxmlCancelType148.setter
    def scxml_ScxmlCancelType148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType148", None)
        self.__scxml_ScxmlCancelType148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType147"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType147"):
                opp_val = getattr(value, "scxml_ScxmlIfType147", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType(self):
        return self.__scxml_ScxmlCancelType

    @scxml_ScxmlCancelType.setter
    def scxml_ScxmlCancelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType", None)
        self.__scxml_ScxmlCancelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot7"):
                opp_val = getattr(old_value, "scxml_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot7"):
                opp_val = getattr(value, "scxml_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType121(self):
        return self.__scxml_ScxmlCancelType121

    @scxml_ScxmlCancelType121.setter
    def scxml_ScxmlCancelType121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType121", None)
        self.__scxml_ScxmlCancelType121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType120"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType120", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType120"):
                opp_val = getattr(value, "scxml_ScxmlForeachType120", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType120", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType88(self):
        return self.__scxml_ScxmlCancelType88

    @scxml_ScxmlCancelType88.setter
    def scxml_ScxmlCancelType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType88", None)
        self.__scxml_ScxmlCancelType88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType87"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType87", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType87"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType87", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType87", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType175(self):
        return self.__scxml_ScxmlCancelType175

    @scxml_ScxmlCancelType175.setter
    def scxml_ScxmlCancelType175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType175", None)
        self.__scxml_ScxmlCancelType175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType174"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType174", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType174"):
                opp_val = getattr(value, "scxml_ScxmlIfType174", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType174", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType361(self):
        return self.__scxml_ScxmlCancelType361

    @scxml_ScxmlCancelType361.setter
    def scxml_ScxmlCancelType361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType361", None)
        self.__scxml_ScxmlCancelType361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType360"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType360", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType360"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType360", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType360", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlCancelType262(self):
        return self.__scxml_ScxmlCancelType262

    @scxml_ScxmlCancelType262.setter
    def scxml_ScxmlCancelType262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlCancelType__scxml_ScxmlCancelType262", None)
        self.__scxml_ScxmlCancelType262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType261"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType261", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType261"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType261", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType261", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlAssignType:

    def __init__(self, expr: str, location: str, type: str, anyAttribute: str, mixed: str, any: str, attr: str, scxml_ScxmlAssignType: "scxml_DocumentRoot" = None, scxml_ScxmlAssignType82: "scxml_ScxmlFinalizeType" = None, scxml_ScxmlAssignType115: "scxml_ScxmlForeachType" = None, scxml_ScxmlAssignType142: "scxml_ScxmlIfType" = None, scxml_ScxmlAssignType169: "scxml_ScxmlIfType" = None, scxml_ScxmlAssignType196: "scxml_ScxmlIfType" = None, scxml_ScxmlAssignType232: "scxml_ScxmlOnentryType" = None, scxml_ScxmlAssignType256: "scxml_ScxmlOnexitType" = None, scxml_ScxmlAssignType355: "scxml_ScxmlTransitionType" = None):
        self.expr = expr
        self.location = location
        self.type = type
        self.anyAttribute = anyAttribute
        self.mixed = mixed
        self.any = any
        self.attr = attr
        self.scxml_ScxmlAssignType = scxml_ScxmlAssignType
        self.scxml_ScxmlAssignType82 = scxml_ScxmlAssignType82
        self.scxml_ScxmlAssignType115 = scxml_ScxmlAssignType115
        self.scxml_ScxmlAssignType142 = scxml_ScxmlAssignType142
        self.scxml_ScxmlAssignType169 = scxml_ScxmlAssignType169
        self.scxml_ScxmlAssignType196 = scxml_ScxmlAssignType196
        self.scxml_ScxmlAssignType232 = scxml_ScxmlAssignType232
        self.scxml_ScxmlAssignType256 = scxml_ScxmlAssignType256
        self.scxml_ScxmlAssignType355 = scxml_ScxmlAssignType355
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def attr(self) -> str:
        return self.__attr

    @attr.setter
    def attr(self, attr: str):
        self.__attr = attr

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def scxml_ScxmlAssignType355(self):
        return self.__scxml_ScxmlAssignType355

    @scxml_ScxmlAssignType355.setter
    def scxml_ScxmlAssignType355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType355", None)
        self.__scxml_ScxmlAssignType355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlTransitionType354"):
                opp_val = getattr(old_value, "scxml_ScxmlTransitionType354", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlTransitionType354"):
                opp_val = getattr(value, "scxml_ScxmlTransitionType354", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlTransitionType354", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType256(self):
        return self.__scxml_ScxmlAssignType256

    @scxml_ScxmlAssignType256.setter
    def scxml_ScxmlAssignType256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType256", None)
        self.__scxml_ScxmlAssignType256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnexitType255"):
                opp_val = getattr(old_value, "scxml_ScxmlOnexitType255", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnexitType255"):
                opp_val = getattr(value, "scxml_ScxmlOnexitType255", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnexitType255", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType232(self):
        return self.__scxml_ScxmlAssignType232

    @scxml_ScxmlAssignType232.setter
    def scxml_ScxmlAssignType232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType232", None)
        self.__scxml_ScxmlAssignType232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlOnentryType231"):
                opp_val = getattr(old_value, "scxml_ScxmlOnentryType231", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlOnentryType231"):
                opp_val = getattr(value, "scxml_ScxmlOnentryType231", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlOnentryType231", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType(self):
        return self.__scxml_ScxmlAssignType

    @scxml_ScxmlAssignType.setter
    def scxml_ScxmlAssignType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType", None)
        self.__scxml_ScxmlAssignType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot5"):
                opp_val = getattr(old_value, "scxml_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot5"):
                opp_val = getattr(value, "scxml_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType169(self):
        return self.__scxml_ScxmlAssignType169

    @scxml_ScxmlAssignType169.setter
    def scxml_ScxmlAssignType169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType169", None)
        self.__scxml_ScxmlAssignType169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType168"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType168"):
                opp_val = getattr(value, "scxml_ScxmlIfType168", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType196(self):
        return self.__scxml_ScxmlAssignType196

    @scxml_ScxmlAssignType196.setter
    def scxml_ScxmlAssignType196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType196", None)
        self.__scxml_ScxmlAssignType196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType195"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType195", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType195"):
                opp_val = getattr(value, "scxml_ScxmlIfType195", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType195", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType82(self):
        return self.__scxml_ScxmlAssignType82

    @scxml_ScxmlAssignType82.setter
    def scxml_ScxmlAssignType82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType82", None)
        self.__scxml_ScxmlAssignType82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlFinalizeType81"):
                opp_val = getattr(old_value, "scxml_ScxmlFinalizeType81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlFinalizeType81"):
                opp_val = getattr(value, "scxml_ScxmlFinalizeType81", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlFinalizeType81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType142(self):
        return self.__scxml_ScxmlAssignType142

    @scxml_ScxmlAssignType142.setter
    def scxml_ScxmlAssignType142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType142", None)
        self.__scxml_ScxmlAssignType142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlIfType141"):
                opp_val = getattr(old_value, "scxml_ScxmlIfType141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlIfType141"):
                opp_val = getattr(value, "scxml_ScxmlIfType141", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlIfType141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlAssignType115(self):
        return self.__scxml_ScxmlAssignType115

    @scxml_ScxmlAssignType115.setter
    def scxml_ScxmlAssignType115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlAssignType__scxml_ScxmlAssignType115", None)
        self.__scxml_ScxmlAssignType115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlForeachType114"):
                opp_val = getattr(old_value, "scxml_ScxmlForeachType114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlForeachType114"):
                opp_val = getattr(value, "scxml_ScxmlForeachType114", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlForeachType114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlDatamodelType:

    def __init__(self, scxmlExtraContent: str, any: str, anyAttribute: str, scxml_ScxmlDatamodelType: "scxml_DocumentRoot" = None, scxml_ScxmlDatamodelType57: set["scxml_ScxmlDataType"] = None, scxml_ScxmlDatamodelType283: "scxml_ScxmlParallelType" = None, scxml_ScxmlDatamodelType298: "scxml_ScxmlScxmlType" = None, scxml_ScxmlDatamodelType334: "scxml_ScxmlStateType" = None):
        self.scxmlExtraContent = scxmlExtraContent
        self.any = any
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlDatamodelType = scxml_ScxmlDatamodelType
        self.scxml_ScxmlDatamodelType57 = scxml_ScxmlDatamodelType57 if scxml_ScxmlDatamodelType57 is not None else set()
        self.scxml_ScxmlDatamodelType283 = scxml_ScxmlDatamodelType283
        self.scxml_ScxmlDatamodelType298 = scxml_ScxmlDatamodelType298
        self.scxml_ScxmlDatamodelType334 = scxml_ScxmlDatamodelType334
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxmlExtraContent(self) -> str:
        return self.__scxmlExtraContent

    @scxmlExtraContent.setter
    def scxmlExtraContent(self, scxmlExtraContent: str):
        self.__scxmlExtraContent = scxmlExtraContent

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def scxml_ScxmlDatamodelType334(self):
        return self.__scxml_ScxmlDatamodelType334

    @scxml_ScxmlDatamodelType334.setter
    def scxml_ScxmlDatamodelType334(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDatamodelType__scxml_ScxmlDatamodelType334", None)
        self.__scxml_ScxmlDatamodelType334 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlStateType333"):
                opp_val = getattr(old_value, "scxml_ScxmlStateType333", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlStateType333"):
                opp_val = getattr(value, "scxml_ScxmlStateType333", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlStateType333", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDatamodelType57(self):
        return self.__scxml_ScxmlDatamodelType57

    @scxml_ScxmlDatamodelType57.setter
    def scxml_ScxmlDatamodelType57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDatamodelType__scxml_ScxmlDatamodelType57", None)
        self.__scxml_ScxmlDatamodelType57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDataType58"):
                    opp_val = getattr(item, "scxml_ScxmlDataType58", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDataType58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDataType58"):
                    opp_val = getattr(item, "scxml_ScxmlDataType58", None)
                    
                    setattr(item, "scxml_ScxmlDataType58", self)
                    

    @property
    def scxml_ScxmlDatamodelType298(self):
        return self.__scxml_ScxmlDatamodelType298

    @scxml_ScxmlDatamodelType298.setter
    def scxml_ScxmlDatamodelType298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDatamodelType__scxml_ScxmlDatamodelType298", None)
        self.__scxml_ScxmlDatamodelType298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlScxmlType297"):
                opp_val = getattr(old_value, "scxml_ScxmlScxmlType297", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlScxmlType297"):
                opp_val = getattr(value, "scxml_ScxmlScxmlType297", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlScxmlType297", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDatamodelType(self):
        return self.__scxml_ScxmlDatamodelType

    @scxml_ScxmlDatamodelType.setter
    def scxml_ScxmlDatamodelType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDatamodelType__scxml_ScxmlDatamodelType", None)
        self.__scxml_ScxmlDatamodelType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot13"):
                opp_val = getattr(old_value, "scxml_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot13"):
                opp_val = getattr(value, "scxml_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDatamodelType283(self):
        return self.__scxml_ScxmlDatamodelType283

    @scxml_ScxmlDatamodelType283.setter
    def scxml_ScxmlDatamodelType283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDatamodelType__scxml_ScxmlDatamodelType283", None)
        self.__scxml_ScxmlDatamodelType283 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlParallelType282"):
                opp_val = getattr(old_value, "scxml_ScxmlParallelType282", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlParallelType282"):
                opp_val = getattr(value, "scxml_ScxmlParallelType282", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlParallelType282", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlDataType:

    def __init__(self, expr: str, mixed: str, any: str, id: str, src: str, anyAttribute: str, scxml_ScxmlDataType: "scxml_DocumentRoot" = None, scxml_ScxmlDataType58: "scxml_ScxmlDatamodelType" = None):
        self.expr = expr
        self.mixed = mixed
        self.any = any
        self.id = id
        self.src = src
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlDataType = scxml_ScxmlDataType
        self.scxml_ScxmlDataType58 = scxml_ScxmlDataType58
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def scxml_ScxmlDataType58(self):
        return self.__scxml_ScxmlDataType58

    @scxml_ScxmlDataType58.setter
    def scxml_ScxmlDataType58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDataType__scxml_ScxmlDataType58", None)
        self.__scxml_ScxmlDataType58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlDatamodelType57"):
                opp_val = getattr(old_value, "scxml_ScxmlDatamodelType57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlDatamodelType57"):
                opp_val = getattr(value, "scxml_ScxmlDatamodelType57", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlDatamodelType57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlDataType(self):
        return self.__scxml_ScxmlDataType

    @scxml_ScxmlDataType.setter
    def scxml_ScxmlDataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlDataType__scxml_ScxmlDataType", None)
        self.__scxml_ScxmlDataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot11"):
                opp_val = getattr(old_value, "scxml_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot11"):
                opp_val = getattr(value, "scxml_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_ScxmlContentType:

    def __init__(self, mixed: str, any: str, expr: str, anyAttribute: str, scxml_ScxmlContentType: "scxml_DocumentRoot" = None, scxml_ScxmlContentType61: "scxml_ScxmlDonedataType" = None, scxml_ScxmlContentType208: "scxml_ScxmlInvokeType" = None, scxml_ScxmlContentType304: "scxml_ScxmlSendType" = None):
        self.mixed = mixed
        self.any = any
        self.expr = expr
        self.anyAttribute = anyAttribute
        self.scxml_ScxmlContentType = scxml_ScxmlContentType
        self.scxml_ScxmlContentType61 = scxml_ScxmlContentType61
        self.scxml_ScxmlContentType208 = scxml_ScxmlContentType208
        self.scxml_ScxmlContentType304 = scxml_ScxmlContentType304
        
    @property
    def any(self) -> str:
        return self.__any

    @any.setter
    def any(self, any: str):
        self.__any = any

    @property
    def expr(self) -> str:
        return self.__expr

    @expr.setter
    def expr(self, expr: str):
        self.__expr = expr

    @property
    def anyAttribute(self) -> str:
        return self.__anyAttribute

    @anyAttribute.setter
    def anyAttribute(self, anyAttribute: str):
        self.__anyAttribute = anyAttribute

    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def scxml_ScxmlContentType61(self):
        return self.__scxml_ScxmlContentType61

    @scxml_ScxmlContentType61.setter
    def scxml_ScxmlContentType61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlContentType__scxml_ScxmlContentType61", None)
        self.__scxml_ScxmlContentType61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlDonedataType60"):
                opp_val = getattr(old_value, "scxml_ScxmlDonedataType60", None)
                if opp_val == self:
                    setattr(old_value, "scxml_ScxmlDonedataType60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlDonedataType60"):
                opp_val = getattr(value, "scxml_ScxmlDonedataType60", None)
                setattr(value, "scxml_ScxmlDonedataType60", self)

    @property
    def scxml_ScxmlContentType304(self):
        return self.__scxml_ScxmlContentType304

    @scxml_ScxmlContentType304.setter
    def scxml_ScxmlContentType304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlContentType__scxml_ScxmlContentType304", None)
        self.__scxml_ScxmlContentType304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlSendType303"):
                opp_val = getattr(old_value, "scxml_ScxmlSendType303", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlSendType303"):
                opp_val = getattr(value, "scxml_ScxmlSendType303", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlSendType303", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlContentType(self):
        return self.__scxml_ScxmlContentType

    @scxml_ScxmlContentType.setter
    def scxml_ScxmlContentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlContentType__scxml_ScxmlContentType", None)
        self.__scxml_ScxmlContentType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_DocumentRoot9"):
                opp_val = getattr(old_value, "scxml_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_DocumentRoot9"):
                opp_val = getattr(value, "scxml_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "scxml_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scxml_ScxmlContentType208(self):
        return self.__scxml_ScxmlContentType208

    @scxml_ScxmlContentType208.setter
    def scxml_ScxmlContentType208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_ScxmlContentType__scxml_ScxmlContentType208", None)
        self.__scxml_ScxmlContentType208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scxml_ScxmlInvokeType207"):
                opp_val = getattr(old_value, "scxml_ScxmlInvokeType207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scxml_ScxmlInvokeType207"):
                opp_val = getattr(value, "scxml_ScxmlInvokeType207", None)
                if opp_val is None:
                    setattr(value, "scxml_ScxmlInvokeType207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scxml_EStringToStringMapEntry:

    pass
class scxml_DocumentRoot:

    def __init__(self, mixed: str, scxml_DocumentRoot: set["scxml_EStringToStringMapEntry"] = None, scxml_DocumentRoot7: set["scxml_ScxmlCancelType"] = None, scxml_DocumentRoot9: set["scxml_ScxmlContentType"] = None, scxml_DocumentRoot11: set["scxml_ScxmlDataType"] = None, scxml_DocumentRoot13: set["scxml_ScxmlDatamodelType"] = None, scxml_DocumentRoot2: set["scxml_EStringToStringMapEntry"] = None, scxml_DocumentRoot5: set["scxml_ScxmlAssignType"] = None, scxml_DocumentRoot19: set["scxml_ScxmlElseifType"] = None, scxml_DocumentRoot21: set["scxml_ScxmlFinalType"] = None, scxml_DocumentRoot23: set["scxml_ScxmlFinalizeType"] = None, scxml_DocumentRoot15: set["scxml_ScxmlDonedataType"] = None, scxml_DocumentRoot17: set["scxml_ScxmlElseType"] = None, scxml_DocumentRoot27: set["scxml_ScxmlHistoryType"] = None, scxml_DocumentRoot29: set["scxml_ScxmlIfType"] = None, scxml_DocumentRoot25: set["scxml_ScxmlForeachType"] = None, scxml_DocumentRoot33: set["scxml_ScxmlInvokeType"] = None, scxml_DocumentRoot35: set["scxml_ScxmlLogType"] = None, scxml_DocumentRoot31: set["scxml_ScxmlInitialType"] = None, scxml_DocumentRoot41: set["scxml_ScxmlParallelType"] = None, scxml_DocumentRoot43: set["scxml_ScxmlParamType"] = None, scxml_DocumentRoot45: set["scxml_ScxmlRaiseType"] = None, scxml_DocumentRoot37: set["scxml_ScxmlOnentryType"] = None, scxml_DocumentRoot39: set["scxml_ScxmlOnexitType"] = None, scxml_DocumentRoot51: set["scxml_ScxmlSendType"] = None, scxml_DocumentRoot53: set["scxml_ScxmlStateType"] = None, scxml_DocumentRoot55: set["scxml_ScxmlTransitionType"] = None, scxml_DocumentRoot47: set["scxml_ScxmlScriptType"] = None, scxml_DocumentRoot49: set["scxml_ScxmlScxmlType"] = None):
        self.mixed = mixed
        self.scxml_DocumentRoot = scxml_DocumentRoot if scxml_DocumentRoot is not None else set()
        self.scxml_DocumentRoot7 = scxml_DocumentRoot7 if scxml_DocumentRoot7 is not None else set()
        self.scxml_DocumentRoot9 = scxml_DocumentRoot9 if scxml_DocumentRoot9 is not None else set()
        self.scxml_DocumentRoot11 = scxml_DocumentRoot11 if scxml_DocumentRoot11 is not None else set()
        self.scxml_DocumentRoot13 = scxml_DocumentRoot13 if scxml_DocumentRoot13 is not None else set()
        self.scxml_DocumentRoot2 = scxml_DocumentRoot2 if scxml_DocumentRoot2 is not None else set()
        self.scxml_DocumentRoot5 = scxml_DocumentRoot5 if scxml_DocumentRoot5 is not None else set()
        self.scxml_DocumentRoot19 = scxml_DocumentRoot19 if scxml_DocumentRoot19 is not None else set()
        self.scxml_DocumentRoot21 = scxml_DocumentRoot21 if scxml_DocumentRoot21 is not None else set()
        self.scxml_DocumentRoot23 = scxml_DocumentRoot23 if scxml_DocumentRoot23 is not None else set()
        self.scxml_DocumentRoot15 = scxml_DocumentRoot15 if scxml_DocumentRoot15 is not None else set()
        self.scxml_DocumentRoot17 = scxml_DocumentRoot17 if scxml_DocumentRoot17 is not None else set()
        self.scxml_DocumentRoot27 = scxml_DocumentRoot27 if scxml_DocumentRoot27 is not None else set()
        self.scxml_DocumentRoot29 = scxml_DocumentRoot29 if scxml_DocumentRoot29 is not None else set()
        self.scxml_DocumentRoot25 = scxml_DocumentRoot25 if scxml_DocumentRoot25 is not None else set()
        self.scxml_DocumentRoot33 = scxml_DocumentRoot33 if scxml_DocumentRoot33 is not None else set()
        self.scxml_DocumentRoot35 = scxml_DocumentRoot35 if scxml_DocumentRoot35 is not None else set()
        self.scxml_DocumentRoot31 = scxml_DocumentRoot31 if scxml_DocumentRoot31 is not None else set()
        self.scxml_DocumentRoot41 = scxml_DocumentRoot41 if scxml_DocumentRoot41 is not None else set()
        self.scxml_DocumentRoot43 = scxml_DocumentRoot43 if scxml_DocumentRoot43 is not None else set()
        self.scxml_DocumentRoot45 = scxml_DocumentRoot45 if scxml_DocumentRoot45 is not None else set()
        self.scxml_DocumentRoot37 = scxml_DocumentRoot37 if scxml_DocumentRoot37 is not None else set()
        self.scxml_DocumentRoot39 = scxml_DocumentRoot39 if scxml_DocumentRoot39 is not None else set()
        self.scxml_DocumentRoot51 = scxml_DocumentRoot51 if scxml_DocumentRoot51 is not None else set()
        self.scxml_DocumentRoot53 = scxml_DocumentRoot53 if scxml_DocumentRoot53 is not None else set()
        self.scxml_DocumentRoot55 = scxml_DocumentRoot55 if scxml_DocumentRoot55 is not None else set()
        self.scxml_DocumentRoot47 = scxml_DocumentRoot47 if scxml_DocumentRoot47 is not None else set()
        self.scxml_DocumentRoot49 = scxml_DocumentRoot49 if scxml_DocumentRoot49 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

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
                if hasattr(item, "scxml_ScxmlInitialType"):
                    opp_val = getattr(item, "scxml_ScxmlInitialType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlInitialType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlInitialType"):
                    opp_val = getattr(item, "scxml_ScxmlInitialType", None)
                    
                    setattr(item, "scxml_ScxmlInitialType", self)
                    

    @property
    def scxml_DocumentRoot17(self):
        return self.__scxml_DocumentRoot17

    @scxml_DocumentRoot17.setter
    def scxml_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot17", None)
        self.__scxml_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlElseType"):
                    opp_val = getattr(item, "scxml_ScxmlElseType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlElseType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlElseType"):
                    opp_val = getattr(item, "scxml_ScxmlElseType", None)
                    
                    setattr(item, "scxml_ScxmlElseType", self)
                    

    @property
    def scxml_DocumentRoot25(self):
        return self.__scxml_DocumentRoot25

    @scxml_DocumentRoot25.setter
    def scxml_DocumentRoot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot25", None)
        self.__scxml_DocumentRoot25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlForeachType"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlForeachType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlForeachType"):
                    opp_val = getattr(item, "scxml_ScxmlForeachType", None)
                    
                    setattr(item, "scxml_ScxmlForeachType", self)
                    

    @property
    def scxml_DocumentRoot15(self):
        return self.__scxml_DocumentRoot15

    @scxml_DocumentRoot15.setter
    def scxml_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot15", None)
        self.__scxml_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDonedataType"):
                    opp_val = getattr(item, "scxml_ScxmlDonedataType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDonedataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDonedataType"):
                    opp_val = getattr(item, "scxml_ScxmlDonedataType", None)
                    
                    setattr(item, "scxml_ScxmlDonedataType", self)
                    

    @property
    def scxml_DocumentRoot33(self):
        return self.__scxml_DocumentRoot33

    @scxml_DocumentRoot33.setter
    def scxml_DocumentRoot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot33", None)
        self.__scxml_DocumentRoot33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlInvokeType"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlInvokeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlInvokeType"):
                    opp_val = getattr(item, "scxml_ScxmlInvokeType", None)
                    
                    setattr(item, "scxml_ScxmlInvokeType", self)
                    

    @property
    def scxml_DocumentRoot35(self):
        return self.__scxml_DocumentRoot35

    @scxml_DocumentRoot35.setter
    def scxml_DocumentRoot35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot35", None)
        self.__scxml_DocumentRoot35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlLogType"):
                    opp_val = getattr(item, "scxml_ScxmlLogType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlLogType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlLogType"):
                    opp_val = getattr(item, "scxml_ScxmlLogType", None)
                    
                    setattr(item, "scxml_ScxmlLogType", self)
                    

    @property
    def scxml_DocumentRoot39(self):
        return self.__scxml_DocumentRoot39

    @scxml_DocumentRoot39.setter
    def scxml_DocumentRoot39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot39", None)
        self.__scxml_DocumentRoot39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnexitType"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnexitType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnexitType"):
                    opp_val = getattr(item, "scxml_ScxmlOnexitType", None)
                    
                    setattr(item, "scxml_ScxmlOnexitType", self)
                    

    @property
    def scxml_DocumentRoot49(self):
        return self.__scxml_DocumentRoot49

    @scxml_DocumentRoot49.setter
    def scxml_DocumentRoot49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot49", None)
        self.__scxml_DocumentRoot49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlScxmlType"):
                    opp_val = getattr(item, "scxml_ScxmlScxmlType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlScxmlType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlScxmlType"):
                    opp_val = getattr(item, "scxml_ScxmlScxmlType", None)
                    
                    setattr(item, "scxml_ScxmlScxmlType", self)
                    

    @property
    def scxml_DocumentRoot51(self):
        return self.__scxml_DocumentRoot51

    @scxml_DocumentRoot51.setter
    def scxml_DocumentRoot51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot51", None)
        self.__scxml_DocumentRoot51 = value if value is not None else set()
        
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
                    

    @property
    def scxml_DocumentRoot7(self):
        return self.__scxml_DocumentRoot7

    @scxml_DocumentRoot7.setter
    def scxml_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot7", None)
        self.__scxml_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlCancelType"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlCancelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlCancelType"):
                    opp_val = getattr(item, "scxml_ScxmlCancelType", None)
                    
                    setattr(item, "scxml_ScxmlCancelType", self)
                    

    @property
    def scxml_DocumentRoot13(self):
        return self.__scxml_DocumentRoot13

    @scxml_DocumentRoot13.setter
    def scxml_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot13", None)
        self.__scxml_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDatamodelType"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDatamodelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDatamodelType"):
                    opp_val = getattr(item, "scxml_ScxmlDatamodelType", None)
                    
                    setattr(item, "scxml_ScxmlDatamodelType", self)
                    

    @property
    def scxml_DocumentRoot37(self):
        return self.__scxml_DocumentRoot37

    @scxml_DocumentRoot37.setter
    def scxml_DocumentRoot37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot37", None)
        self.__scxml_DocumentRoot37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlOnentryType"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlOnentryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlOnentryType"):
                    opp_val = getattr(item, "scxml_ScxmlOnentryType", None)
                    
                    setattr(item, "scxml_ScxmlOnentryType", self)
                    

    @property
    def scxml_DocumentRoot9(self):
        return self.__scxml_DocumentRoot9

    @scxml_DocumentRoot9.setter
    def scxml_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot9", None)
        self.__scxml_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlContentType"):
                    opp_val = getattr(item, "scxml_ScxmlContentType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlContentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlContentType"):
                    opp_val = getattr(item, "scxml_ScxmlContentType", None)
                    
                    setattr(item, "scxml_ScxmlContentType", self)
                    

    @property
    def scxml_DocumentRoot11(self):
        return self.__scxml_DocumentRoot11

    @scxml_DocumentRoot11.setter
    def scxml_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot11", None)
        self.__scxml_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlDataType"):
                    opp_val = getattr(item, "scxml_ScxmlDataType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlDataType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlDataType"):
                    opp_val = getattr(item, "scxml_ScxmlDataType", None)
                    
                    setattr(item, "scxml_ScxmlDataType", self)
                    

    @property
    def scxml_DocumentRoot41(self):
        return self.__scxml_DocumentRoot41

    @scxml_DocumentRoot41.setter
    def scxml_DocumentRoot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot41", None)
        self.__scxml_DocumentRoot41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlParallelType"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlParallelType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlParallelType"):
                    opp_val = getattr(item, "scxml_ScxmlParallelType", None)
                    
                    setattr(item, "scxml_ScxmlParallelType", self)
                    

    @property
    def scxml_DocumentRoot2(self):
        return self.__scxml_DocumentRoot2

    @scxml_DocumentRoot2.setter
    def scxml_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot2", None)
        self.__scxml_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "scxml_EStringToStringMapEntry3", None)
                    
                    setattr(item, "scxml_EStringToStringMapEntry3", self)
                    

    @property
    def scxml_DocumentRoot5(self):
        return self.__scxml_DocumentRoot5

    @scxml_DocumentRoot5.setter
    def scxml_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot5", None)
        self.__scxml_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlAssignType"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlAssignType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlAssignType"):
                    opp_val = getattr(item, "scxml_ScxmlAssignType", None)
                    
                    setattr(item, "scxml_ScxmlAssignType", self)
                    

    @property
    def scxml_DocumentRoot21(self):
        return self.__scxml_DocumentRoot21

    @scxml_DocumentRoot21.setter
    def scxml_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot21", None)
        self.__scxml_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlFinalType"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlFinalType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlFinalType"):
                    opp_val = getattr(item, "scxml_ScxmlFinalType", None)
                    
                    setattr(item, "scxml_ScxmlFinalType", self)
                    

    @property
    def scxml_DocumentRoot23(self):
        return self.__scxml_DocumentRoot23

    @scxml_DocumentRoot23.setter
    def scxml_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot23", None)
        self.__scxml_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlFinalizeType"):
                    opp_val = getattr(item, "scxml_ScxmlFinalizeType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlFinalizeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlFinalizeType"):
                    opp_val = getattr(item, "scxml_ScxmlFinalizeType", None)
                    
                    setattr(item, "scxml_ScxmlFinalizeType", self)
                    

    @property
    def scxml_DocumentRoot55(self):
        return self.__scxml_DocumentRoot55

    @scxml_DocumentRoot55.setter
    def scxml_DocumentRoot55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot55", None)
        self.__scxml_DocumentRoot55 = value if value is not None else set()
        
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
    def scxml_DocumentRoot47(self):
        return self.__scxml_DocumentRoot47

    @scxml_DocumentRoot47.setter
    def scxml_DocumentRoot47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot47", None)
        self.__scxml_DocumentRoot47 = value if value is not None else set()
        
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
    def scxml_DocumentRoot45(self):
        return self.__scxml_DocumentRoot45

    @scxml_DocumentRoot45.setter
    def scxml_DocumentRoot45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot45", None)
        self.__scxml_DocumentRoot45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlRaiseType"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlRaiseType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlRaiseType"):
                    opp_val = getattr(item, "scxml_ScxmlRaiseType", None)
                    
                    setattr(item, "scxml_ScxmlRaiseType", self)
                    

    @property
    def scxml_DocumentRoot29(self):
        return self.__scxml_DocumentRoot29

    @scxml_DocumentRoot29.setter
    def scxml_DocumentRoot29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot29", None)
        self.__scxml_DocumentRoot29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlIfType"):
                    opp_val = getattr(item, "scxml_ScxmlIfType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlIfType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlIfType"):
                    opp_val = getattr(item, "scxml_ScxmlIfType", None)
                    
                    setattr(item, "scxml_ScxmlIfType", self)
                    

    @property
    def scxml_DocumentRoot43(self):
        return self.__scxml_DocumentRoot43

    @scxml_DocumentRoot43.setter
    def scxml_DocumentRoot43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot43", None)
        self.__scxml_DocumentRoot43 = value if value is not None else set()
        
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
    def scxml_DocumentRoot53(self):
        return self.__scxml_DocumentRoot53

    @scxml_DocumentRoot53.setter
    def scxml_DocumentRoot53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot53", None)
        self.__scxml_DocumentRoot53 = value if value is not None else set()
        
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
    def scxml_DocumentRoot27(self):
        return self.__scxml_DocumentRoot27

    @scxml_DocumentRoot27.setter
    def scxml_DocumentRoot27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot27", None)
        self.__scxml_DocumentRoot27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlHistoryType"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlHistoryType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlHistoryType"):
                    opp_val = getattr(item, "scxml_ScxmlHistoryType", None)
                    
                    setattr(item, "scxml_ScxmlHistoryType", self)
                    

    @property
    def scxml_DocumentRoot19(self):
        return self.__scxml_DocumentRoot19

    @scxml_DocumentRoot19.setter
    def scxml_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scxml_DocumentRoot__scxml_DocumentRoot19", None)
        self.__scxml_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scxml_ScxmlElseifType"):
                    opp_val = getattr(item, "scxml_ScxmlElseifType", None)
                    
                    if opp_val == self:
                        setattr(item, "scxml_ScxmlElseifType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scxml_ScxmlElseifType"):
                    opp_val = getattr(item, "scxml_ScxmlElseifType", None)
                    
                    setattr(item, "scxml_ScxmlElseifType", self)
                    
