from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SetupTaskScope(Enum):
    None_ = "None_"
    Eclipse = "Eclipse"
    Project = "Project"
    Branch = "Branch"
    User = "User"
    Configuration = "Configuration"
class Trigger(Enum):
    BOOTSTRAP = "BOOTSTRAP"
    STARTUP = "STARTUP"
    MANUAL = "MANUAL"
class ComponentType(Enum):
    OSGI_BUNDLE = "OSGI_BUNDLE"
    BUCKMINSTER = "BUCKMINSTER"
    JAR = "JAR"
    BOM = "BOM"
    UNKNOWN = "UNKNOWN"
    ECLIPSE_FEATURE = "ECLIPSE_FEATURE"
class VariableType(Enum):
    STRING = "STRING"
    TEXT = "TEXT"
    PASSWORD = "PASSWORD"
    PATTERN = "PATTERN"
    URI = "URI"
    FILE = "FILE"
    FOLDER = "FOLDER"
    RESOURCE = "RESOURCE"
    CONTAINER = "CONTAINER"
    PROJECT = "PROJECT"
    BOOLEAN = "BOOLEAN"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"


############################################
# Definition of Classes
############################################

class setup_Query:

    def __init__(self, summary: str, uRL: str, queries: "setup_MylynQueriesTask" = None, setup_Query: set["setup_QueryAttribute"] = None, Query: "setup_MylynQueriesTask" = None):
        self.summary = summary
        self.uRL = uRL
        self.queries = queries
        self.setup_Query = setup_Query if setup_Query is not None else set()
        self.Query = Query
        
        pass
    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def queries(self):
        return self.__queries

    @queries.setter
    def queries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Query__queries", None)
        self.__queries = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MylynQueriesTask"):
                opp_val = getattr(old_value, "MylynQueriesTask", None)
                if opp_val == self:
                    setattr(old_value, "MylynQueriesTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MylynQueriesTask"):
                opp_val = getattr(value, "MylynQueriesTask", None)
                setattr(value, "MylynQueriesTask", self)

    @property
    def setup_Query(self):
        return self.__setup_Query

    @setup_Query.setter
    def setup_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Query__setup_Query", None)
        self.__setup_Query = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_QueryAttribute"):
                    opp_val = getattr(item, "setup_QueryAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_QueryAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_QueryAttribute"):
                    opp_val = getattr(item, "setup_QueryAttribute", None)
                    
                    setattr(item, "setup_QueryAttribute", self)
                    

    @property
    def Query(self):
        return self.__Query

    @Query.setter
    def Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Query__Query", None)
        self.__Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "task"):
                opp_val = getattr(old_value, "task", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "task"):
                opp_val = getattr(value, "task", None)
                if opp_val is None:
                    setattr(value, "task", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_BuildPlan:

    def __init__(self, name: str, setup_BuildPlan: "setup_MylynBuildsTask" = None):
        self.name = name
        self.setup_BuildPlan = setup_BuildPlan
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def setup_BuildPlan(self):
        return self.__setup_BuildPlan

    @setup_BuildPlan.setter
    def setup_BuildPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_BuildPlan__setup_BuildPlan", None)
        self.__setup_BuildPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_MylynBuildsTask"):
                opp_val = getattr(old_value, "setup_MylynBuildsTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_MylynBuildsTask"):
                opp_val = getattr(value, "setup_MylynBuildsTask", None)
                if opp_val is None:
                    setattr(value, "setup_MylynBuildsTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_QueryAttribute:

    def __init__(self, key: str, value: str, setup_QueryAttribute: "setup_Query" = None):
        self.key = key
        self.value = value
        self.setup_QueryAttribute = setup_QueryAttribute
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def setup_QueryAttribute(self):
        return self.__setup_QueryAttribute

    @setup_QueryAttribute.setter
    def setup_QueryAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_QueryAttribute__setup_QueryAttribute", None)
        self.__setup_QueryAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Query"):
                opp_val = getattr(old_value, "setup_Query", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Query"):
                opp_val = getattr(value, "setup_Query", None)
                if opp_val is None:
                    setattr(value, "setup_Query", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_TextModification:

    def __init__(self, pattern: str, substitutions: str, setup_TextModification: "setup_TextModifyTask" = None):
        self.pattern = pattern
        self.substitutions = substitutions
        self.setup_TextModification = setup_TextModification
        
        pass
    @property
    def substitutions(self):
        return self.__substitutions

    @substitutions.setter
    def substitutions(self, substitutions: str):
        self.__substitutions = substitutions


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def setup_TextModification(self):
        return self.__setup_TextModification

    @setup_TextModification.setter
    def setup_TextModification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TextModification__setup_TextModification", None)
        self.__setup_TextModification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_TextModifyTask"):
                opp_val = getattr(old_value, "setup_TextModifyTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_TextModifyTask"):
                opp_val = getattr(value, "setup_TextModifyTask", None)
                if opp_val is None:
                    setattr(value, "setup_TextModifyTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_CommandParameter:

    def __init__(self, iD: str, value: str, setup_CommandParameter: "setup_KeyBindingTask" = None):
        self.iD = iD
        self.value = value
        self.setup_CommandParameter = setup_CommandParameter
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def setup_CommandParameter(self):
        return self.__setup_CommandParameter

    @setup_CommandParameter.setter
    def setup_CommandParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_CommandParameter__setup_CommandParameter", None)
        self.__setup_CommandParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_KeyBindingTask63"):
                opp_val = getattr(old_value, "setup_KeyBindingTask63", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_KeyBindingTask63"):
                opp_val = getattr(value, "setup_KeyBindingTask63", None)
                if opp_val is None:
                    setattr(value, "setup_KeyBindingTask63", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_KeyBindingContext:

    def __init__(self, iD: str, setup_KeyBindingContext: "setup_KeyBindingTask" = None):
        self.iD = iD
        self.setup_KeyBindingContext = setup_KeyBindingContext
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


    @property
    def setup_KeyBindingContext(self):
        return self.__setup_KeyBindingContext

    @setup_KeyBindingContext.setter
    def setup_KeyBindingContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_KeyBindingContext__setup_KeyBindingContext", None)
        self.__setup_KeyBindingContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_KeyBindingTask"):
                opp_val = getattr(old_value, "setup_KeyBindingTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_KeyBindingTask"):
                opp_val = getattr(value, "setup_KeyBindingTask", None)
                if opp_val is None:
                    setattr(value, "setup_KeyBindingTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_FileEditor:

    def __init__(self, iD: str, setup_FileEditor: "setup_FileAssociationTask" = None, setup_FileEditor58: "setup_FileMapping" = None):
        self.iD = iD
        self.setup_FileEditor = setup_FileEditor
        self.setup_FileEditor58 = setup_FileEditor58
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


    @property
    def setup_FileEditor(self):
        return self.__setup_FileEditor

    @setup_FileEditor.setter
    def setup_FileEditor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_FileEditor__setup_FileEditor", None)
        self.__setup_FileEditor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_FileAssociationTask"):
                opp_val = getattr(old_value, "setup_FileAssociationTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_FileAssociationTask"):
                opp_val = getattr(value, "setup_FileAssociationTask", None)
                if opp_val is None:
                    setattr(value, "setup_FileAssociationTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_FileEditor58(self):
        return self.__setup_FileEditor58

    @setup_FileEditor58.setter
    def setup_FileEditor58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_FileEditor__setup_FileEditor58", None)
        self.__setup_FileEditor58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_FileMapping57"):
                opp_val = getattr(old_value, "setup_FileMapping57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_FileMapping57"):
                opp_val = getattr(value, "setup_FileMapping57", None)
                if opp_val is None:
                    setattr(value, "setup_FileMapping57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_WorkingSet:

    pass
class setup_FileMapping:

    def __init__(self, filePattern: str, defaultEditorID: str, setup_FileMapping: "setup_FileAssociationsTask" = None, setup_FileMapping57: set["setup_FileEditor"] = None):
        self.filePattern = filePattern
        self.defaultEditorID = defaultEditorID
        self.setup_FileMapping = setup_FileMapping
        self.setup_FileMapping57 = setup_FileMapping57 if setup_FileMapping57 is not None else set()
        
        pass
    @property
    def defaultEditorID(self):
        return self.__defaultEditorID

    @defaultEditorID.setter
    def defaultEditorID(self, defaultEditorID: str):
        self.__defaultEditorID = defaultEditorID


    @property
    def filePattern(self):
        return self.__filePattern

    @filePattern.setter
    def filePattern(self, filePattern: str):
        self.__filePattern = filePattern


    @property
    def setup_FileMapping57(self):
        return self.__setup_FileMapping57

    @setup_FileMapping57.setter
    def setup_FileMapping57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_FileMapping__setup_FileMapping57", None)
        self.__setup_FileMapping57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_FileEditor58"):
                    opp_val = getattr(item, "setup_FileEditor58", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_FileEditor58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_FileEditor58"):
                    opp_val = getattr(item, "setup_FileEditor58", None)
                    
                    setattr(item, "setup_FileEditor58", self)
                    

    @property
    def setup_FileMapping(self):
        return self.__setup_FileMapping

    @setup_FileMapping.setter
    def setup_FileMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_FileMapping__setup_FileMapping", None)
        self.__setup_FileMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_FileAssociationsTask"):
                opp_val = getattr(old_value, "setup_FileAssociationsTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_FileAssociationsTask"):
                opp_val = getattr(value, "setup_FileAssociationsTask", None)
                if opp_val is None:
                    setattr(value, "setup_FileAssociationsTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_TargletData(ABC):

    def __init__(self, activeRepositoryList: str, includeSources: bool, includeAllPlatforms: bool, name: str, setup_TargletData42: set["setup_AutomaticSourceLocator"] = None, setup_TargletData45: set["setup_RepositoryList"] = None, setup_TargletData47: set["setup_P2Repository"] = None, setup_TargletData: set["setup_InstallableUnit"] = None):
        self.activeRepositoryList = activeRepositoryList
        self.includeSources = includeSources
        self.includeAllPlatforms = includeAllPlatforms
        self.name = name
        self.setup_TargletData42 = setup_TargletData42 if setup_TargletData42 is not None else set()
        self.setup_TargletData45 = setup_TargletData45 if setup_TargletData45 is not None else set()
        self.setup_TargletData47 = setup_TargletData47 if setup_TargletData47 is not None else set()
        self.setup_TargletData = setup_TargletData if setup_TargletData is not None else set()
        
        pass
    @property
    def activeRepositoryList(self):
        return self.__activeRepositoryList

    @activeRepositoryList.setter
    def activeRepositoryList(self, activeRepositoryList: str):
        self.__activeRepositoryList = activeRepositoryList


    @property
    def includeAllPlatforms(self):
        return self.__includeAllPlatforms

    @includeAllPlatforms.setter
    def includeAllPlatforms(self, includeAllPlatforms: bool):
        self.__includeAllPlatforms = includeAllPlatforms


    @property
    def includeSources(self):
        return self.__includeSources

    @includeSources.setter
    def includeSources(self, includeSources: bool):
        self.__includeSources = includeSources


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def setup_TargletData42(self):
        return self.__setup_TargletData42

    @setup_TargletData42.setter
    def setup_TargletData42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TargletData__setup_TargletData42", None)
        self.__setup_TargletData42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_AutomaticSourceLocator43"):
                    opp_val = getattr(item, "setup_AutomaticSourceLocator43", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_AutomaticSourceLocator43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_AutomaticSourceLocator43"):
                    opp_val = getattr(item, "setup_AutomaticSourceLocator43", None)
                    
                    setattr(item, "setup_AutomaticSourceLocator43", self)
                    

    @property
    def setup_TargletData(self):
        return self.__setup_TargletData

    @setup_TargletData.setter
    def setup_TargletData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TargletData__setup_TargletData", None)
        self.__setup_TargletData = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_InstallableUnit40"):
                    opp_val = getattr(item, "setup_InstallableUnit40", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_InstallableUnit40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_InstallableUnit40"):
                    opp_val = getattr(item, "setup_InstallableUnit40", None)
                    
                    setattr(item, "setup_InstallableUnit40", self)
                    

    @property
    def setup_TargletData47(self):
        return self.__setup_TargletData47

    @setup_TargletData47.setter
    def setup_TargletData47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TargletData__setup_TargletData47", None)
        self.__setup_TargletData47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_P2Repository48"):
                    opp_val = getattr(item, "setup_P2Repository48", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_P2Repository48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_P2Repository48"):
                    opp_val = getattr(item, "setup_P2Repository48", None)
                    
                    setattr(item, "setup_P2Repository48", self)
                    

    @property
    def setup_TargletData45(self):
        return self.__setup_TargletData45

    @setup_TargletData45.setter
    def setup_TargletData45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TargletData__setup_TargletData45", None)
        self.__setup_TargletData45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_RepositoryList"):
                    opp_val = getattr(item, "setup_RepositoryList", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_RepositoryList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_RepositoryList"):
                    opp_val = getattr(item, "setup_RepositoryList", None)
                    
                    setattr(item, "setup_RepositoryList", self)
                    

class TargletData:

    pass
class setup_Targlet(TargletData):

    pass
class setup_RepositoryList:

    def __init__(self, name: str, setup_RepositoryList: "setup_TargletData" = None, setup_RepositoryList50: set["setup_P2Repository"] = None):
        self.name = name
        self.setup_RepositoryList = setup_RepositoryList
        self.setup_RepositoryList50 = setup_RepositoryList50 if setup_RepositoryList50 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def setup_RepositoryList(self):
        return self.__setup_RepositoryList

    @setup_RepositoryList.setter
    def setup_RepositoryList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_RepositoryList__setup_RepositoryList", None)
        self.__setup_RepositoryList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_TargletData45"):
                opp_val = getattr(old_value, "setup_TargletData45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_TargletData45"):
                opp_val = getattr(value, "setup_TargletData45", None)
                if opp_val is None:
                    setattr(value, "setup_TargletData45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_RepositoryList50(self):
        return self.__setup_RepositoryList50

    @setup_RepositoryList50.setter
    def setup_RepositoryList50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_RepositoryList__setup_RepositoryList50", None)
        self.__setup_RepositoryList50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_P2Repository51"):
                    opp_val = getattr(item, "setup_P2Repository51", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_P2Repository51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_P2Repository51"):
                    opp_val = getattr(item, "setup_P2Repository51", None)
                    
                    setattr(item, "setup_P2Repository51", self)
                    

class ComponentExtension:

    pass
class setup_ComponentDefinition(ComponentExtension):

    def __init__(self, version: str, iD: str):
        self.version = version
        self.iD = iD
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


class setup_Component:

    def __init__(self, name: str, type: str, versionRange: str, setup_Component: "setup_MaterializationTask" = None):
        self.name = name
        self.type = type
        self.versionRange = versionRange
        self.setup_Component = setup_Component
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def versionRange(self):
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def setup_Component(self):
        return self.__setup_Component

    @setup_Component.setter
    def setup_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Component__setup_Component", None)
        self.__setup_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_MaterializationTask"):
                opp_val = getattr(old_value, "setup_MaterializationTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_MaterializationTask"):
                opp_val = getattr(value, "setup_MaterializationTask", None)
                if opp_val is None:
                    setattr(value, "setup_MaterializationTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_ComponentExtension:

    pass
class setup_Predicate:

    pass
class SourceLocator:

    pass
class setup_AutomaticSourceLocator(SourceLocator):

    def __init__(self, rootFolder: str, locateNestedProjects: bool, setup_AutomaticSourceLocator: set["setup_Predicate"] = None, setup_AutomaticSourceLocator38: "setup_MavenImportTask" = None, setup_AutomaticSourceLocator43: "setup_TargletData" = None, setup_AutomaticSourceLocator53: "setup_ProjectsImportTask" = None):
        self.rootFolder = rootFolder
        self.locateNestedProjects = locateNestedProjects
        self.setup_AutomaticSourceLocator = setup_AutomaticSourceLocator if setup_AutomaticSourceLocator is not None else set()
        self.setup_AutomaticSourceLocator38 = setup_AutomaticSourceLocator38
        self.setup_AutomaticSourceLocator43 = setup_AutomaticSourceLocator43
        self.setup_AutomaticSourceLocator53 = setup_AutomaticSourceLocator53
        
        pass
    @property
    def rootFolder(self):
        return self.__rootFolder

    @rootFolder.setter
    def rootFolder(self, rootFolder: str):
        self.__rootFolder = rootFolder


    @property
    def locateNestedProjects(self):
        return self.__locateNestedProjects

    @locateNestedProjects.setter
    def locateNestedProjects(self, locateNestedProjects: bool):
        self.__locateNestedProjects = locateNestedProjects


    @property
    def setup_AutomaticSourceLocator38(self):
        return self.__setup_AutomaticSourceLocator38

    @setup_AutomaticSourceLocator38.setter
    def setup_AutomaticSourceLocator38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_AutomaticSourceLocator__setup_AutomaticSourceLocator38", None)
        self.__setup_AutomaticSourceLocator38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_MavenImportTask"):
                opp_val = getattr(old_value, "setup_MavenImportTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_MavenImportTask"):
                opp_val = getattr(value, "setup_MavenImportTask", None)
                if opp_val is None:
                    setattr(value, "setup_MavenImportTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_AutomaticSourceLocator53(self):
        return self.__setup_AutomaticSourceLocator53

    @setup_AutomaticSourceLocator53.setter
    def setup_AutomaticSourceLocator53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_AutomaticSourceLocator__setup_AutomaticSourceLocator53", None)
        self.__setup_AutomaticSourceLocator53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_ProjectsImportTask"):
                opp_val = getattr(old_value, "setup_ProjectsImportTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_ProjectsImportTask"):
                opp_val = getattr(value, "setup_ProjectsImportTask", None)
                if opp_val is None:
                    setattr(value, "setup_ProjectsImportTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_AutomaticSourceLocator43(self):
        return self.__setup_AutomaticSourceLocator43

    @setup_AutomaticSourceLocator43.setter
    def setup_AutomaticSourceLocator43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_AutomaticSourceLocator__setup_AutomaticSourceLocator43", None)
        self.__setup_AutomaticSourceLocator43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_TargletData42"):
                opp_val = getattr(old_value, "setup_TargletData42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_TargletData42"):
                opp_val = getattr(value, "setup_TargletData42", None)
                if opp_val is None:
                    setattr(value, "setup_TargletData42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_AutomaticSourceLocator(self):
        return self.__setup_AutomaticSourceLocator

    @setup_AutomaticSourceLocator.setter
    def setup_AutomaticSourceLocator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_AutomaticSourceLocator__setup_AutomaticSourceLocator", None)
        self.__setup_AutomaticSourceLocator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_Predicate"):
                    opp_val = getattr(item, "setup_Predicate", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_Predicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_Predicate"):
                    opp_val = getattr(item, "setup_Predicate", None)
                    
                    setattr(item, "setup_Predicate", self)
                    

class setup_ManualSourceLocator(SourceLocator):

    def __init__(self, location: str, componentNamePattern: str, componentTypes: str):
        self.location = location
        self.componentNamePattern = componentNamePattern
        self.componentTypes = componentTypes
        
        pass
    @property
    def componentTypes(self):
        return self.__componentTypes

    @componentTypes.setter
    def componentTypes(self, componentTypes: str):
        self.__componentTypes = componentTypes


    @property
    def componentNamePattern(self):
        return self.__componentNamePattern

    @componentNamePattern.setter
    def componentNamePattern(self, componentNamePattern: str):
        self.__componentNamePattern = componentNamePattern


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class setup_SourceLocator(ABC):

    pass
class setup_P2Repository:

    def __init__(self, uRL: str, setup_P2Repository: "setup_P2Task" = None, setup_P2Repository33: "setup_MaterializationTask" = None, setup_P2Repository48: "setup_TargletData" = None, setup_P2Repository51: "setup_RepositoryList" = None):
        self.uRL = uRL
        self.setup_P2Repository = setup_P2Repository
        self.setup_P2Repository33 = setup_P2Repository33
        self.setup_P2Repository48 = setup_P2Repository48
        self.setup_P2Repository51 = setup_P2Repository51
        
        pass
    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def setup_P2Repository48(self):
        return self.__setup_P2Repository48

    @setup_P2Repository48.setter
    def setup_P2Repository48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Repository__setup_P2Repository48", None)
        self.__setup_P2Repository48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_TargletData47"):
                opp_val = getattr(old_value, "setup_TargletData47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_TargletData47"):
                opp_val = getattr(value, "setup_TargletData47", None)
                if opp_val is None:
                    setattr(value, "setup_TargletData47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_P2Repository(self):
        return self.__setup_P2Repository

    @setup_P2Repository.setter
    def setup_P2Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Repository__setup_P2Repository", None)
        self.__setup_P2Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_P2Task27"):
                opp_val = getattr(old_value, "setup_P2Task27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_P2Task27"):
                opp_val = getattr(value, "setup_P2Task27", None)
                if opp_val is None:
                    setattr(value, "setup_P2Task27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_P2Repository51(self):
        return self.__setup_P2Repository51

    @setup_P2Repository51.setter
    def setup_P2Repository51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Repository__setup_P2Repository51", None)
        self.__setup_P2Repository51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_RepositoryList50"):
                opp_val = getattr(old_value, "setup_RepositoryList50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_RepositoryList50"):
                opp_val = getattr(value, "setup_RepositoryList50", None)
                if opp_val is None:
                    setattr(value, "setup_RepositoryList50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_P2Repository33(self):
        return self.__setup_P2Repository33

    @setup_P2Repository33.setter
    def setup_P2Repository33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Repository__setup_P2Repository33", None)
        self.__setup_P2Repository33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_MaterializationTask32"):
                opp_val = getattr(old_value, "setup_MaterializationTask32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_MaterializationTask32"):
                opp_val = getattr(value, "setup_MaterializationTask32", None)
                if opp_val is None:
                    setattr(value, "setup_MaterializationTask32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_InstallableUnit:

    def __init__(self, iD: str, versionRange: str, setup_InstallableUnit: "setup_P2Task" = None, setup_InstallableUnit36: "setup_ComponentExtension" = None, setup_InstallableUnit40: "setup_TargletData" = None):
        self.iD = iD
        self.versionRange = versionRange
        self.setup_InstallableUnit = setup_InstallableUnit
        self.setup_InstallableUnit36 = setup_InstallableUnit36
        self.setup_InstallableUnit40 = setup_InstallableUnit40
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


    @property
    def versionRange(self):
        return self.__versionRange

    @versionRange.setter
    def versionRange(self, versionRange: str):
        self.__versionRange = versionRange


    @property
    def setup_InstallableUnit36(self):
        return self.__setup_InstallableUnit36

    @setup_InstallableUnit36.setter
    def setup_InstallableUnit36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_InstallableUnit__setup_InstallableUnit36", None)
        self.__setup_InstallableUnit36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_ComponentExtension"):
                opp_val = getattr(old_value, "setup_ComponentExtension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_ComponentExtension"):
                opp_val = getattr(value, "setup_ComponentExtension", None)
                if opp_val is None:
                    setattr(value, "setup_ComponentExtension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_InstallableUnit(self):
        return self.__setup_InstallableUnit

    @setup_InstallableUnit.setter
    def setup_InstallableUnit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_InstallableUnit__setup_InstallableUnit", None)
        self.__setup_InstallableUnit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_P2Task"):
                opp_val = getattr(old_value, "setup_P2Task", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_P2Task"):
                opp_val = getattr(value, "setup_P2Task", None)
                if opp_val is None:
                    setattr(value, "setup_P2Task", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_InstallableUnit40(self):
        return self.__setup_InstallableUnit40

    @setup_InstallableUnit40.setter
    def setup_InstallableUnit40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_InstallableUnit__setup_InstallableUnit40", None)
        self.__setup_InstallableUnit40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_TargletData"):
                opp_val = getattr(old_value, "setup_TargletData", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_TargletData"):
                opp_val = getattr(value, "setup_TargletData", None)
                if opp_val is None:
                    setattr(value, "setup_TargletData", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BasicMaterializationTask:

    pass
class setup_MaterializationTask(BasicMaterializationTask):

    pass
class setup_BuckminsterImportTask(BasicMaterializationTask):

    def __init__(self, mspec: str):
        self.mspec = mspec
        
        pass
    @property
    def mspec(self):
        return self.__mspec

    @mspec.setter
    def mspec(self, mspec: str):
        self.__mspec = mspec


class SetupTask:

    pass
class setup_MylynQueryTask(SetupTask):

    def __init__(self, connectorKind: str, summary: str, repositoryURL: str, relativeURL: str):
        self.connectorKind = connectorKind
        self.summary = summary
        self.repositoryURL = repositoryURL
        self.relativeURL = relativeURL
        
        pass
    @property
    def connectorKind(self):
        return self.__connectorKind

    @connectorKind.setter
    def connectorKind(self, connectorKind: str):
        self.__connectorKind = connectorKind


    @property
    def repositoryURL(self):
        return self.__repositoryURL

    @repositoryURL.setter
    def repositoryURL(self, repositoryURL: str):
        self.__repositoryURL = repositoryURL


    @property
    def summary(self):
        return self.__summary

    @summary.setter
    def summary(self, summary: str):
        self.__summary = summary


    @property
    def relativeURL(self):
        return self.__relativeURL

    @relativeURL.setter
    def relativeURL(self, relativeURL: str):
        self.__relativeURL = relativeURL


class setup_KeyBindingTask(SetupTask):

    def __init__(self, platform: str, locale: str, keys: str, command: str, scheme: str, setup_KeyBindingTask: set["setup_KeyBindingContext"] = None, setup_KeyBindingTask63: set["setup_CommandParameter"] = None):
        self.platform = platform
        self.locale = locale
        self.keys = keys
        self.command = command
        self.scheme = scheme
        self.setup_KeyBindingTask = setup_KeyBindingTask if setup_KeyBindingTask is not None else set()
        self.setup_KeyBindingTask63 = setup_KeyBindingTask63 if setup_KeyBindingTask63 is not None else set()
        
        pass
    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, command: str):
        self.__command = command


    @property
    def scheme(self):
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme


    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, keys: str):
        self.__keys = keys


    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, platform: str):
        self.__platform = platform


    @property
    def locale(self):
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale


    @property
    def setup_KeyBindingTask63(self):
        return self.__setup_KeyBindingTask63

    @setup_KeyBindingTask63.setter
    def setup_KeyBindingTask63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_KeyBindingTask__setup_KeyBindingTask63", None)
        self.__setup_KeyBindingTask63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_CommandParameter"):
                    opp_val = getattr(item, "setup_CommandParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_CommandParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_CommandParameter"):
                    opp_val = getattr(item, "setup_CommandParameter", None)
                    
                    setattr(item, "setup_CommandParameter", self)
                    

    @property
    def setup_KeyBindingTask(self):
        return self.__setup_KeyBindingTask

    @setup_KeyBindingTask.setter
    def setup_KeyBindingTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_KeyBindingTask__setup_KeyBindingTask", None)
        self.__setup_KeyBindingTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_KeyBindingContext"):
                    opp_val = getattr(item, "setup_KeyBindingContext", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_KeyBindingContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_KeyBindingContext"):
                    opp_val = getattr(item, "setup_KeyBindingContext", None)
                    
                    setattr(item, "setup_KeyBindingContext", self)
                    

class setup_FileAssociationsTask(SetupTask):

    pass
class setup_TargletImportTask(SetupTask):

    def __init__(self, targletURI: str):
        self.targletURI = targletURI
        
        pass
    @property
    def targletURI(self):
        return self.__targletURI

    @targletURI.setter
    def targletURI(self, targletURI: str):
        self.__targletURI = targletURI


class setup_WorkingSetTask(SetupTask):

    pass
class setup_MylynBuildsTask(SetupTask):

    def __init__(self, connectorKind: str, serverURL: str, userID: str, password: str, setup_MylynBuildsTask: set["setup_BuildPlan"] = None):
        self.connectorKind = connectorKind
        self.serverURL = serverURL
        self.userID = userID
        self.password = password
        self.setup_MylynBuildsTask = setup_MylynBuildsTask if setup_MylynBuildsTask is not None else set()
        
        pass
    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID


    @property
    def serverURL(self):
        return self.__serverURL

    @serverURL.setter
    def serverURL(self, serverURL: str):
        self.__serverURL = serverURL


    @property
    def connectorKind(self):
        return self.__connectorKind

    @connectorKind.setter
    def connectorKind(self, connectorKind: str):
        self.__connectorKind = connectorKind


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def setup_MylynBuildsTask(self):
        return self.__setup_MylynBuildsTask

    @setup_MylynBuildsTask.setter
    def setup_MylynBuildsTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_MylynBuildsTask__setup_MylynBuildsTask", None)
        self.__setup_MylynBuildsTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_BuildPlan"):
                    opp_val = getattr(item, "setup_BuildPlan", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_BuildPlan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_BuildPlan"):
                    opp_val = getattr(item, "setup_BuildPlan", None)
                    
                    setattr(item, "setup_BuildPlan", self)
                    

class setup_TargetPlatformTask(SetupTask):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class setup_BasicMaterializationTask(SetupTask):

    def __init__(self, targetPlatform: str, bundlePool: str):
        self.targetPlatform = targetPlatform
        self.bundlePool = bundlePool
        
        pass
    @property
    def bundlePool(self):
        return self.__bundlePool

    @bundlePool.setter
    def bundlePool(self, bundlePool: str):
        self.__bundlePool = bundlePool


    @property
    def targetPlatform(self):
        return self.__targetPlatform

    @targetPlatform.setter
    def targetPlatform(self, targetPlatform: str):
        self.__targetPlatform = targetPlatform


class setup_MavenImportTask(SetupTask):

    pass
class setup_P2Task(SetupTask):

    def __init__(self, mergeDisabled: bool, licenseConfirmationDisabled: bool, setup_P2Task: set["setup_InstallableUnit"] = None, setup_P2Task27: set["setup_P2Repository"] = None):
        self.mergeDisabled = mergeDisabled
        self.licenseConfirmationDisabled = licenseConfirmationDisabled
        self.setup_P2Task = setup_P2Task if setup_P2Task is not None else set()
        self.setup_P2Task27 = setup_P2Task27 if setup_P2Task27 is not None else set()
        
        pass
    @property
    def mergeDisabled(self):
        return self.__mergeDisabled

    @mergeDisabled.setter
    def mergeDisabled(self, mergeDisabled: bool):
        self.__mergeDisabled = mergeDisabled


    @property
    def licenseConfirmationDisabled(self):
        return self.__licenseConfirmationDisabled

    @licenseConfirmationDisabled.setter
    def licenseConfirmationDisabled(self, licenseConfirmationDisabled: bool):
        self.__licenseConfirmationDisabled = licenseConfirmationDisabled


    @property
    def setup_P2Task(self):
        return self.__setup_P2Task

    @setup_P2Task.setter
    def setup_P2Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Task__setup_P2Task", None)
        self.__setup_P2Task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_InstallableUnit"):
                    opp_val = getattr(item, "setup_InstallableUnit", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_InstallableUnit", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_InstallableUnit"):
                    opp_val = getattr(item, "setup_InstallableUnit", None)
                    
                    setattr(item, "setup_InstallableUnit", self)
                    

    @property
    def setup_P2Task27(self):
        return self.__setup_P2Task27

    @setup_P2Task27.setter
    def setup_P2Task27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_P2Task__setup_P2Task27", None)
        self.__setup_P2Task27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_P2Repository"):
                    opp_val = getattr(item, "setup_P2Repository", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_P2Repository", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_P2Repository"):
                    opp_val = getattr(item, "setup_P2Repository", None)
                    
                    setattr(item, "setup_P2Repository", self)
                    

class setup_ProjectsImportTask(SetupTask):

    pass
class setup_EclipsePreferenceTask(SetupTask):

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class setup_TargletTask(TargletData, SetupTask):

    pass
class setup_TextModifyTask(SetupTask):

    def __init__(self, uRL: str, encoding: str, setup_TextModifyTask: set["setup_TextModification"] = None):
        self.uRL = uRL
        self.encoding = encoding
        self.setup_TextModifyTask = setup_TextModifyTask if setup_TextModifyTask is not None else set()
        
        pass
    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding


    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


    @property
    def setup_TextModifyTask(self):
        return self.__setup_TextModifyTask

    @setup_TextModifyTask.setter
    def setup_TextModifyTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_TextModifyTask__setup_TextModifyTask", None)
        self.__setup_TextModifyTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_TextModification"):
                    opp_val = getattr(item, "setup_TextModification", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_TextModification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_TextModification"):
                    opp_val = getattr(item, "setup_TextModification", None)
                    
                    setattr(item, "setup_TextModification", self)
                    

class setup_JRETask(SetupTask):

    def __init__(self, version: str, location: str):
        self.version = version
        self.location = location
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class setup_FileAssociationTask(SetupTask):

    def __init__(self, filePattern: str, defaultEditorID: str, setup_FileAssociationTask: set["setup_FileEditor"] = None):
        self.filePattern = filePattern
        self.defaultEditorID = defaultEditorID
        self.setup_FileAssociationTask = setup_FileAssociationTask if setup_FileAssociationTask is not None else set()
        
        pass
    @property
    def defaultEditorID(self):
        return self.__defaultEditorID

    @defaultEditorID.setter
    def defaultEditorID(self, defaultEditorID: str):
        self.__defaultEditorID = defaultEditorID


    @property
    def filePattern(self):
        return self.__filePattern

    @filePattern.setter
    def filePattern(self, filePattern: str):
        self.__filePattern = filePattern


    @property
    def setup_FileAssociationTask(self):
        return self.__setup_FileAssociationTask

    @setup_FileAssociationTask.setter
    def setup_FileAssociationTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_FileAssociationTask__setup_FileAssociationTask", None)
        self.__setup_FileAssociationTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_FileEditor"):
                    opp_val = getattr(item, "setup_FileEditor", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_FileEditor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_FileEditor"):
                    opp_val = getattr(item, "setup_FileEditor", None)
                    
                    setattr(item, "setup_FileEditor", self)
                    

class setup_GitCloneTask(SetupTask):

    def __init__(self, location: str, remoteName: str, remoteURI: str, pushURI: str, userID: str, checkoutBranch: str):
        self.location = location
        self.remoteName = remoteName
        self.remoteURI = remoteURI
        self.pushURI = pushURI
        self.userID = userID
        self.checkoutBranch = checkoutBranch
        
        pass
    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID


    @property
    def checkoutBranch(self):
        return self.__checkoutBranch

    @checkoutBranch.setter
    def checkoutBranch(self, checkoutBranch: str):
        self.__checkoutBranch = checkoutBranch


    @property
    def pushURI(self):
        return self.__pushURI

    @pushURI.setter
    def pushURI(self, pushURI: str):
        self.__pushURI = pushURI


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def remoteName(self):
        return self.__remoteName

    @remoteName.setter
    def remoteName(self, remoteName: str):
        self.__remoteName = remoteName


    @property
    def remoteURI(self):
        return self.__remoteURI

    @remoteURI.setter
    def remoteURI(self, remoteURI: str):
        self.__remoteURI = remoteURI


class setup_ResourceCreationTask(SetupTask):

    def __init__(self, content: str, targetURL: str, encoding: str):
        self.content = content
        self.targetURL = targetURL
        self.encoding = encoding
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def targetURL(self):
        return self.__targetURL

    @targetURL.setter
    def targetURL(self, targetURL: str):
        self.__targetURL = targetURL


    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding


class setup_ResourceCopyTask(SetupTask):

    def __init__(self, sourceURL: str, targetURL: str):
        self.sourceURL = sourceURL
        self.targetURL = targetURL
        
        pass
    @property
    def targetURL(self):
        return self.__targetURL

    @targetURL.setter
    def targetURL(self, targetURL: str):
        self.__targetURL = targetURL


    @property
    def sourceURL(self):
        return self.__sourceURL

    @sourceURL.setter
    def sourceURL(self, sourceURL: str):
        self.__sourceURL = sourceURL


class setup_MylynQueriesTask(SetupTask):

    def __init__(self, connectorKind: str, repositoryURL: str, userID: str, password: str, MylynQueriesTask: "setup_Query" = None, task: set["setup_Query"] = None):
        self.connectorKind = connectorKind
        self.repositoryURL = repositoryURL
        self.userID = userID
        self.password = password
        self.MylynQueriesTask = MylynQueriesTask
        self.task = task if task is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password


    @property
    def userID(self):
        return self.__userID

    @userID.setter
    def userID(self, userID: str):
        self.__userID = userID


    @property
    def repositoryURL(self):
        return self.__repositoryURL

    @repositoryURL.setter
    def repositoryURL(self, repositoryURL: str):
        self.__repositoryURL = repositoryURL


    @property
    def connectorKind(self):
        return self.__connectorKind

    @connectorKind.setter
    def connectorKind(self, connectorKind: str):
        self.__connectorKind = connectorKind


    @property
    def MylynQueriesTask(self):
        return self.__MylynQueriesTask

    @MylynQueriesTask.setter
    def MylynQueriesTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_MylynQueriesTask__MylynQueriesTask", None)
        self.__MylynQueriesTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queries"):
                opp_val = getattr(old_value, "queries", None)
                if opp_val == self:
                    setattr(old_value, "queries", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queries"):
                opp_val = getattr(value, "queries", None)
                setattr(value, "queries", self)

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_MylynQueriesTask__task", None)
        self.__task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    if opp_val == self:
                        setattr(item, "Query", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Query"):
                    opp_val = getattr(item, "Query", None)
                    
                    setattr(item, "Query", self)
                    

class setup_ProjectSetImportTask(SetupTask):

    def __init__(self, uRL: str):
        self.uRL = uRL
        
        pass
    @property
    def uRL(self):
        return self.__uRL

    @uRL.setter
    def uRL(self, uRL: str):
        self.__uRL = uRL


class setup_ApiBaselineTask(SetupTask):

    def __init__(self, version: str, containerFolder: str, zipLocation: str):
        self.version = version
        self.containerFolder = containerFolder
        self.zipLocation = zipLocation
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def zipLocation(self):
        return self.__zipLocation

    @zipLocation.setter
    def zipLocation(self, zipLocation: str):
        self.__zipLocation = zipLocation


    @property
    def containerFolder(self):
        return self.__containerFolder

    @containerFolder.setter
    def containerFolder(self, containerFolder: str):
        self.__containerFolder = containerFolder


class SetupTaskContainer:

    pass
class setup_CompoundSetupTask(SetupTask, SetupTaskContainer):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class setup_ScopeRoot(SetupTaskContainer):

    def __init__(self):
        
        pass
    def getScope(self) :
        # TODO: Implement getScope method
        pass

    def getParentScopeRoot(self) :
        # TODO: Implement getParentScopeRoot method
        pass

class setup_SetupTaskContainer(ABC):

    pass
class setup_LinkLocationTask(SetupTask):

    def __init__(self, path: str, name: str):
        self.path = path
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


class setup_EclipseIniTask(SetupTask):

    def __init__(self, option: str, value: str, vm: bool):
        self.option = option
        self.value = value
        self.vm = vm
        
        pass
    @property
    def vm(self):
        return self.__vm

    @vm.setter
    def vm(self, vm: bool):
        self.__vm = vm


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def option(self):
        return self.__option

    @option.setter
    def option(self, option: str):
        self.__option = option


class setup_RedirectionTask(SetupTask):

    def __init__(self, sourceURL: str, targetURL: str):
        self.sourceURL = sourceURL
        self.targetURL = targetURL
        
        pass
    @property
    def sourceURL(self):
        return self.__sourceURL

    @sourceURL.setter
    def sourceURL(self, sourceURL: str):
        self.__sourceURL = sourceURL


    @property
    def targetURL(self):
        return self.__targetURL

    @targetURL.setter
    def targetURL(self, targetURL: str):
        self.__targetURL = targetURL


class setup_VariableChoice:

    def __init__(self, value: str, label: str, setup_VariableChoice: "setup_ContextVariableTask" = None):
        self.value = value
        self.label = label
        self.setup_VariableChoice = setup_VariableChoice
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def setup_VariableChoice(self):
        return self.__setup_VariableChoice

    @setup_VariableChoice.setter
    def setup_VariableChoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_VariableChoice__setup_VariableChoice", None)
        self.__setup_VariableChoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_ContextVariableTask"):
                opp_val = getattr(old_value, "setup_ContextVariableTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_ContextVariableTask"):
                opp_val = getattr(value, "setup_ContextVariableTask", None)
                if opp_val is None:
                    setattr(value, "setup_ContextVariableTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_ContextVariableTask(SetupTask):

    def __init__(self, type: str, name: str, value: str, stringSubstitution: bool, label: str, setup_ContextVariableTask: set["setup_VariableChoice"] = None):
        self.type = type
        self.name = name
        self.value = value
        self.stringSubstitution = stringSubstitution
        self.label = label
        self.setup_ContextVariableTask = setup_ContextVariableTask if setup_ContextVariableTask is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def stringSubstitution(self):
        return self.__stringSubstitution

    @stringSubstitution.setter
    def stringSubstitution(self, stringSubstitution: bool):
        self.__stringSubstitution = stringSubstitution


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def setup_ContextVariableTask(self):
        return self.__setup_ContextVariableTask

    @setup_ContextVariableTask.setter
    def setup_ContextVariableTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_ContextVariableTask__setup_ContextVariableTask", None)
        self.__setup_ContextVariableTask = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_VariableChoice"):
                    opp_val = getattr(item, "setup_VariableChoice", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_VariableChoice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_VariableChoice"):
                    opp_val = getattr(item, "setup_VariableChoice", None)
                    
                    setattr(item, "setup_VariableChoice", self)
                    

class setup_SetupTask(ABC):

    def __init__(self, disabled: bool, scope: str, excludedTriggers: str, documentation: str, setup_SetupTask: "setup_SetupTask" = None, setup_SetupTask18: set["setup_SetupTask"] = None, setup_SetupTask21: set["setup_ConfigurableItem"] = None, setup_SetupTask23: "setup_SetupTaskContainer" = None):
        self.disabled = disabled
        self.scope = scope
        self.excludedTriggers = excludedTriggers
        self.documentation = documentation
        self.setup_SetupTask = setup_SetupTask
        self.setup_SetupTask18 = setup_SetupTask18 if setup_SetupTask18 is not None else set()
        self.setup_SetupTask21 = setup_SetupTask21 if setup_SetupTask21 is not None else set()
        self.setup_SetupTask23 = setup_SetupTask23
        
        pass
    @property
    def disabled(self):
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: bool):
        self.__disabled = disabled


    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def excludedTriggers(self):
        return self.__excludedTriggers

    @excludedTriggers.setter
    def excludedTriggers(self, excludedTriggers: str):
        self.__excludedTriggers = excludedTriggers


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def setup_SetupTask18(self):
        return self.__setup_SetupTask18

    @setup_SetupTask18.setter
    def setup_SetupTask18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_SetupTask__setup_SetupTask18", None)
        self.__setup_SetupTask18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_SetupTask"):
                    opp_val = getattr(item, "setup_SetupTask", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_SetupTask", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_SetupTask"):
                    opp_val = getattr(item, "setup_SetupTask", None)
                    
                    setattr(item, "setup_SetupTask", self)
                    

    @property
    def setup_SetupTask21(self):
        return self.__setup_SetupTask21

    @setup_SetupTask21.setter
    def setup_SetupTask21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_SetupTask__setup_SetupTask21", None)
        self.__setup_SetupTask21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_ConfigurableItem"):
                    opp_val = getattr(item, "setup_ConfigurableItem", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_ConfigurableItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_ConfigurableItem"):
                    opp_val = getattr(item, "setup_ConfigurableItem", None)
                    
                    setattr(item, "setup_ConfigurableItem", self)
                    

    @property
    def setup_SetupTask23(self):
        return self.__setup_SetupTask23

    @setup_SetupTask23.setter
    def setup_SetupTask23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_SetupTask__setup_SetupTask23", None)
        self.__setup_SetupTask23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_SetupTaskContainer"):
                opp_val = getattr(old_value, "setup_SetupTaskContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_SetupTaskContainer"):
                opp_val = getattr(value, "setup_SetupTaskContainer", None)
                if opp_val is None:
                    setattr(value, "setup_SetupTaskContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_SetupTask(self):
        return self.__setup_SetupTask

    @setup_SetupTask.setter
    def setup_SetupTask(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_SetupTask__setup_SetupTask", None)
        self.__setup_SetupTask = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_SetupTask18"):
                opp_val = getattr(old_value, "setup_SetupTask18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_SetupTask18"):
                opp_val = getattr(value, "setup_SetupTask18", None)
                if opp_val is None:
                    setattr(value, "setup_SetupTask18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getScopeRoot(self) :
        # TODO: Implement getScopeRoot method
        pass

    def requires(self, setup_setupTask) :
        # TODO: Implement requires method
        pass

    def getValidTriggers(self) :
        # TODO: Implement getValidTriggers method
        pass

    def getTriggers(self) :
        # TODO: Implement getTriggers method
        pass

class setup_Setup:

    def __init__(self, setup_Setup: "setup_Branch" = None, setup_Setup16: "setup_Eclipse" = None):
        self.setup_Setup = setup_Setup
        self.setup_Setup16 = setup_Setup16
        
        pass
    @property
    def setup_Setup16(self):
        return self.__setup_Setup16

    @setup_Setup16.setter
    def setup_Setup16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Setup__setup_Setup16", None)
        self.__setup_Setup16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Eclipse17"):
                opp_val = getattr(old_value, "setup_Eclipse17", None)
                if opp_val == self:
                    setattr(old_value, "setup_Eclipse17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Eclipse17"):
                opp_val = getattr(value, "setup_Eclipse17", None)
                setattr(value, "setup_Eclipse17", self)

    @property
    def setup_Setup(self):
        return self.__setup_Setup

    @setup_Setup.setter
    def setup_Setup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Setup__setup_Setup", None)
        self.__setup_Setup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Branch14"):
                opp_val = getattr(old_value, "setup_Branch14", None)
                if opp_val == self:
                    setattr(old_value, "setup_Branch14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Branch14"):
                opp_val = getattr(value, "setup_Branch14", None)
                setattr(value, "setup_Branch14", self)

    def getSetupTasks(self, setup_filterRestrictions, setup_preferences, setup_trigger) :
        # TODO: Implement getSetupTasks method
        pass

class ConfigurableItem:

    pass
class setup_Eclipse(ConfigurableItem):

    def __init__(self, version: str, eclipseVersions: "setup_Configuration" = None, setup_Eclipse17: "setup_Setup" = None, setup_Eclipse12: "setup_Branch" = None, Eclipse: "setup_Configuration" = None, setup_Eclipse: "setup_Project" = None):
        self.version = version
        self.eclipseVersions = eclipseVersions
        self.setup_Eclipse17 = setup_Eclipse17
        self.setup_Eclipse12 = setup_Eclipse12
        self.Eclipse = Eclipse
        self.setup_Eclipse = setup_Eclipse
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def Eclipse(self):
        return self.__Eclipse

    @Eclipse.setter
    def Eclipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Eclipse__Eclipse", None)
        self.__Eclipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configuration"):
                opp_val = getattr(old_value, "configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configuration"):
                opp_val = getattr(value, "configuration", None)
                if opp_val is None:
                    setattr(value, "configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eclipseVersions(self):
        return self.__eclipseVersions

    @eclipseVersions.setter
    def eclipseVersions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Eclipse__eclipseVersions", None)
        self.__eclipseVersions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration"):
                opp_val = getattr(old_value, "Configuration", None)
                if opp_val == self:
                    setattr(old_value, "Configuration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration"):
                opp_val = getattr(value, "Configuration", None)
                setattr(value, "Configuration", self)

    @property
    def setup_Eclipse(self):
        return self.__setup_Eclipse

    @setup_Eclipse.setter
    def setup_Eclipse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Eclipse__setup_Eclipse", None)
        self.__setup_Eclipse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Project"):
                opp_val = getattr(old_value, "setup_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Project"):
                opp_val = getattr(value, "setup_Project", None)
                if opp_val is None:
                    setattr(value, "setup_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_Eclipse12(self):
        return self.__setup_Eclipse12

    @setup_Eclipse12.setter
    def setup_Eclipse12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Eclipse__setup_Eclipse12", None)
        self.__setup_Eclipse12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Branch"):
                opp_val = getattr(old_value, "setup_Branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Branch"):
                opp_val = getattr(value, "setup_Branch", None)
                if opp_val is None:
                    setattr(value, "setup_Branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_Eclipse17(self):
        return self.__setup_Eclipse17

    @setup_Eclipse17.setter
    def setup_Eclipse17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Eclipse__setup_Eclipse17", None)
        self.__setup_Eclipse17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Setup16"):
                opp_val = getattr(old_value, "setup_Setup16", None)
                if opp_val == self:
                    setattr(old_value, "setup_Setup16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Setup16"):
                opp_val = getattr(value, "setup_Setup16", None)
                setattr(value, "setup_Setup16", self)

class setup_Branch(ConfigurableItem):

    def __init__(self, name: str, setup_Branch14: "setup_Setup" = None, branches: "setup_Project" = None, setup_Branch: set["setup_Eclipse"] = None, Branch: "setup_Project" = None):
        self.name = name
        self.setup_Branch14 = setup_Branch14
        self.branches = branches
        self.setup_Branch = setup_Branch if setup_Branch is not None else set()
        self.Branch = Branch
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def setup_Branch14(self):
        return self.__setup_Branch14

    @setup_Branch14.setter
    def setup_Branch14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Branch__setup_Branch14", None)
        self.__setup_Branch14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_Setup"):
                opp_val = getattr(old_value, "setup_Setup", None)
                if opp_val == self:
                    setattr(old_value, "setup_Setup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_Setup"):
                opp_val = getattr(value, "setup_Setup", None)
                setattr(value, "setup_Setup", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Branch__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project"):
                opp_val = getattr(old_value, "project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project"):
                opp_val = getattr(value, "project", None)
                if opp_val is None:
                    setattr(value, "project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_Branch(self):
        return self.__setup_Branch

    @setup_Branch.setter
    def setup_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Branch__setup_Branch", None)
        self.__setup_Branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_Eclipse12"):
                    opp_val = getattr(item, "setup_Eclipse12", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_Eclipse12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_Eclipse12"):
                    opp_val = getattr(item, "setup_Eclipse12", None)
                    
                    setattr(item, "setup_Eclipse12", self)
                    

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Branch__branches", None)
        self.__branches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project10"):
                opp_val = getattr(old_value, "Project10", None)
                if opp_val == self:
                    setattr(old_value, "Project10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project10"):
                opp_val = getattr(value, "Project10", None)
                setattr(value, "Project10", self)

class setup_Project(ConfigurableItem):

    def __init__(self, name: str, label: str, Project10: "setup_Branch" = None, Project: "setup_Configuration" = None, projects: "setup_Configuration" = None, project: set["setup_Branch"] = None, setup_Project: set["setup_Eclipse"] = None):
        self.name = name
        self.label = label
        self.Project10 = Project10
        self.Project = Project
        self.projects = projects
        self.project = project if project is not None else set()
        self.setup_Project = setup_Project if setup_Project is not None else set()
        
        pass
    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Branch"):
                    opp_val = getattr(item, "Branch", None)
                    
                    if opp_val == self:
                        setattr(item, "Branch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Branch"):
                    opp_val = getattr(item, "Branch", None)
                    
                    setattr(item, "Branch", self)
                    

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Project__projects", None)
        self.__projects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Configuration6"):
                opp_val = getattr(old_value, "Configuration6", None)
                if opp_val == self:
                    setattr(old_value, "Configuration6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Configuration6"):
                opp_val = getattr(value, "Configuration6", None)
                setattr(value, "Configuration6", self)

    @property
    def Project10(self):
        return self.__Project10

    @Project10.setter
    def Project10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Project__Project10", None)
        self.__Project10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branches"):
                opp_val = getattr(old_value, "branches", None)
                if opp_val == self:
                    setattr(old_value, "branches", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branches"):
                opp_val = getattr(value, "branches", None)
                setattr(value, "branches", self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "configuration4"):
                opp_val = getattr(old_value, "configuration4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "configuration4"):
                opp_val = getattr(value, "configuration4", None)
                if opp_val is None:
                    setattr(value, "configuration4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def setup_Project(self):
        return self.__setup_Project

    @setup_Project.setter
    def setup_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Project__setup_Project", None)
        self.__setup_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "setup_Eclipse"):
                    opp_val = getattr(item, "setup_Eclipse", None)
                    
                    if opp_val == self:
                        setattr(item, "setup_Eclipse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "setup_Eclipse"):
                    opp_val = getattr(item, "setup_Eclipse", None)
                    
                    setattr(item, "setup_Eclipse", self)
                    

class ScopeRoot:

    pass
class setup_Preferences(ScopeRoot):

    def __init__(self, installFolder: str, acceptedLicenses: str):
        self.installFolder = installFolder
        self.acceptedLicenses = acceptedLicenses
        
        pass
    @property
    def installFolder(self):
        return self.__installFolder

    @installFolder.setter
    def installFolder(self, installFolder: str):
        self.__installFolder = installFolder


    @property
    def acceptedLicenses(self):
        return self.__acceptedLicenses

    @acceptedLicenses.setter
    def acceptedLicenses(self, acceptedLicenses: str):
        self.__acceptedLicenses = acceptedLicenses


class setup_Configuration(ScopeRoot):

    pass
class setup_ConfigurableItem(ScopeRoot):

    pass
class setup_Index:

    def __init__(self, name: str, uRI: str, oldURIs: str, setup_Index: "setup_MetaIndex" = None):
        self.name = name
        self.uRI = uRI
        self.oldURIs = oldURIs
        self.setup_Index = setup_Index
        
        pass
    @property
    def uRI(self):
        return self.__uRI

    @uRI.setter
    def uRI(self, uRI: str):
        self.__uRI = uRI


    @property
    def oldURIs(self):
        return self.__oldURIs

    @oldURIs.setter
    def oldURIs(self, oldURIs: str):
        self.__oldURIs = oldURIs


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def setup_Index(self):
        return self.__setup_Index

    @setup_Index.setter
    def setup_Index(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_setup_Index__setup_Index", None)
        self.__setup_Index = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "setup_MetaIndex"):
                opp_val = getattr(old_value, "setup_MetaIndex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "setup_MetaIndex"):
                opp_val = getattr(value, "setup_MetaIndex", None)
                if opp_val is None:
                    setattr(value, "setup_MetaIndex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class setup_MetaIndex:

    pass