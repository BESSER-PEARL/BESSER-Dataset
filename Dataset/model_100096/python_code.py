from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class sourcecleaner_ExtensionReference:

    def __init__(self, name: str, java: str, package: str, project: str, ExtensionReference: "sourcecleaner_Schema" = None, references: "sourcecleaner_Schema" = None, sourcecleaner_ExtensionReference: "sourcecleaner_Java" = None):
        self.name = name
        self.java = java
        self.package = package
        self.project = project
        self.ExtensionReference = ExtensionReference
        self.references = references
        self.sourcecleaner_ExtensionReference = sourcecleaner_ExtensionReference
        
        pass
    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package


    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, project: str):
        self.__project = project


    @property
    def java(self):
        return self.__java

    @java.setter
    def java(self, java: str):
        self.__java = java


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def ExtensionReference(self):
        return self.__ExtensionReference

    @ExtensionReference.setter
    def ExtensionReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionReference__ExtensionReference", None)
        self.__ExtensionReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema"):
                opp_val = getattr(old_value, "schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema"):
                opp_val = getattr(value, "schema", None)
                if opp_val is None:
                    setattr(value, "schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def references(self):
        return self.__references

    @references.setter
    def references(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionReference__references", None)
        self.__references = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema38"):
                opp_val = getattr(old_value, "Schema38", None)
                if opp_val == self:
                    setattr(old_value, "Schema38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema38"):
                opp_val = getattr(value, "Schema38", None)
                setattr(value, "Schema38", self)

    @property
    def sourcecleaner_ExtensionReference(self):
        return self.__sourcecleaner_ExtensionReference

    @sourcecleaner_ExtensionReference.setter
    def sourcecleaner_ExtensionReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionReference__sourcecleaner_ExtensionReference", None)
        self.__sourcecleaner_ExtensionReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Java40"):
                opp_val = getattr(old_value, "sourcecleaner_Java40", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Java40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Java40"):
                opp_val = getattr(value, "sourcecleaner_Java40", None)
                setattr(value, "sourcecleaner_Java40", self)

class sourcecleaner_ExtensionAttribute:

    def __init__(self, name: str, value: str, sourcecleaner_ExtensionAttribute: "sourcecleaner_Extension" = None):
        self.name = name
        self.value = value
        self.sourcecleaner_ExtensionAttribute = sourcecleaner_ExtensionAttribute
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourcecleaner_ExtensionAttribute(self):
        return self.__sourcecleaner_ExtensionAttribute

    @sourcecleaner_ExtensionAttribute.setter
    def sourcecleaner_ExtensionAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionAttribute__sourcecleaner_ExtensionAttribute", None)
        self.__sourcecleaner_ExtensionAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Extension"):
                opp_val = getattr(old_value, "sourcecleaner_Extension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Extension"):
                opp_val = getattr(value, "sourcecleaner_Extension", None)
                if opp_val is None:
                    setattr(value, "sourcecleaner_Extension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourcecleaner_Dependency:

    def __init__(self, name: str, version: str, reexport: bool, diagraph: bool, Dependency: "sourcecleaner_Manifest" = None, sourcecleaner_Dependency: "sourcecleaner_Manifest" = None, dependencies: "sourcecleaner_Manifest" = None):
        self.name = name
        self.version = version
        self.reexport = reexport
        self.diagraph = diagraph
        self.Dependency = Dependency
        self.sourcecleaner_Dependency = sourcecleaner_Dependency
        self.dependencies = dependencies
        
        pass
    @property
    def reexport(self):
        return self.__reexport

    @reexport.setter
    def reexport(self, reexport: bool):
        self.__reexport = reexport


    @property
    def diagraph(self):
        return self.__diagraph

    @diagraph.setter
    def diagraph(self, diagraph: bool):
        self.__diagraph = diagraph


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourcecleaner_Dependency(self):
        return self.__sourcecleaner_Dependency

    @sourcecleaner_Dependency.setter
    def sourcecleaner_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Dependency__sourcecleaner_Dependency", None)
        self.__sourcecleaner_Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Manifest21"):
                opp_val = getattr(old_value, "sourcecleaner_Manifest21", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Manifest21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Manifest21"):
                opp_val = getattr(value, "sourcecleaner_Manifest21", None)
                setattr(value, "sourcecleaner_Manifest21", self)

    @property
    def Dependency(self):
        return self.__Dependency

    @Dependency.setter
    def Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Dependency__Dependency", None)
        self.__Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requerant"):
                opp_val = getattr(old_value, "requerant", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requerant"):
                opp_val = getattr(value, "requerant", None)
                if opp_val is None:
                    setattr(value, "requerant", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dependencies(self):
        return self.__dependencies

    @dependencies.setter
    def dependencies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Dependency__dependencies", None)
        self.__dependencies = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manifest"):
                opp_val = getattr(old_value, "Manifest", None)
                if opp_val == self:
                    setattr(old_value, "Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manifest"):
                opp_val = getattr(value, "Manifest", None)
                setattr(value, "Manifest", self)

class Source:

    pass
class sourcecleaner_LocatedElement(ABC):

    def __init__(self, absolutePath: str, name: str):
        self.absolutePath = absolutePath
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def absolutePath(self):
        return self.__absolutePath

    @absolutePath.setter
    def absolutePath(self, absolutePath: str):
        self.__absolutePath = absolutePath


class sourcecleaner_Schema(Source):

    def __init__(self, extensionName: str, extensionId: str, pluginName: str, Schema: "sourcecleaner_Project" = None, schema: set["sourcecleaner_ExtensionReference"] = None, schema35: "sourcecleaner_Project" = None, Schema38: "sourcecleaner_ExtensionReference" = None):
        self.extensionName = extensionName
        self.extensionId = extensionId
        self.pluginName = pluginName
        self.Schema = Schema
        self.schema = schema if schema is not None else set()
        self.schema35 = schema35
        self.Schema38 = Schema38
        
        pass
    @property
    def extensionName(self):
        return self.__extensionName

    @extensionName.setter
    def extensionName(self, extensionName: str):
        self.__extensionName = extensionName


    @property
    def extensionId(self):
        return self.__extensionId

    @extensionId.setter
    def extensionId(self, extensionId: str):
        self.__extensionId = extensionId


    @property
    def pluginName(self):
        return self.__pluginName

    @pluginName.setter
    def pluginName(self, pluginName: str):
        self.__pluginName = pluginName


    @property
    def Schema(self):
        return self.__Schema

    @Schema.setter
    def Schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Schema__Schema", None)
        self.__Schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project9"):
                opp_val = getattr(old_value, "project9", None)
                if opp_val == self:
                    setattr(old_value, "project9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project9"):
                opp_val = getattr(value, "project9", None)
                setattr(value, "project9", self)

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Schema__schema", None)
        self.__schema = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionReference"):
                    opp_val = getattr(item, "ExtensionReference", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionReference"):
                    opp_val = getattr(item, "ExtensionReference", None)
                    
                    setattr(item, "ExtensionReference", self)
                    

    @property
    def Schema38(self):
        return self.__Schema38

    @Schema38.setter
    def Schema38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Schema__Schema38", None)
        self.__Schema38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "references"):
                opp_val = getattr(old_value, "references", None)
                if opp_val == self:
                    setattr(old_value, "references", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "references"):
                opp_val = getattr(value, "references", None)
                setattr(value, "references", self)

    @property
    def schema35(self):
        return self.__schema35

    @schema35.setter
    def schema35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Schema__schema35", None)
        self.__schema35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project36"):
                opp_val = getattr(old_value, "Project36", None)
                if opp_val == self:
                    setattr(old_value, "Project36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project36"):
                opp_val = getattr(value, "Project36", None)
                setattr(value, "Project36", self)

class sourcecleaner_ExtensionPoint:

    def __init__(self, id: str, name: str, schema: str, diagraph: bool, ExtensionPoint: "sourcecleaner_Extension" = None, extensionPoint: set["sourcecleaner_Extension"] = None, extensionPoints: "sourcecleaner_Plugin" = None, ExtensionPoint29: "sourcecleaner_Plugin" = None):
        self.id = id
        self.name = name
        self.schema = schema
        self.diagraph = diagraph
        self.ExtensionPoint = ExtensionPoint
        self.extensionPoint = extensionPoint if extensionPoint is not None else set()
        self.extensionPoints = extensionPoints
        self.ExtensionPoint29 = ExtensionPoint29
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, schema: str):
        self.__schema = schema


    @property
    def diagraph(self):
        return self.__diagraph

    @diagraph.setter
    def diagraph(self, diagraph: bool):
        self.__diagraph = diagraph


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def extensionPoints(self):
        return self.__extensionPoints

    @extensionPoints.setter
    def extensionPoints(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionPoint__extensionPoints", None)
        self.__extensionPoints = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plugin25"):
                opp_val = getattr(old_value, "Plugin25", None)
                if opp_val == self:
                    setattr(old_value, "Plugin25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plugin25"):
                opp_val = getattr(value, "Plugin25", None)
                setattr(value, "Plugin25", self)

    @property
    def extensionPoint(self):
        return self.__extensionPoint

    @extensionPoint.setter
    def extensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionPoint__extensionPoint", None)
        self.__extensionPoint = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    if opp_val == self:
                        setattr(item, "Extension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Extension"):
                    opp_val = getattr(item, "Extension", None)
                    
                    setattr(item, "Extension", self)
                    

    @property
    def ExtensionPoint(self):
        return self.__ExtensionPoint

    @ExtensionPoint.setter
    def ExtensionPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionPoint__ExtensionPoint", None)
        self.__ExtensionPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensions"):
                opp_val = getattr(old_value, "extensions", None)
                if opp_val == self:
                    setattr(old_value, "extensions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensions"):
                opp_val = getattr(value, "extensions", None)
                setattr(value, "extensions", self)

    @property
    def ExtensionPoint29(self):
        return self.__ExtensionPoint29

    @ExtensionPoint29.setter
    def ExtensionPoint29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ExtensionPoint__ExtensionPoint29", None)
        self.__ExtensionPoint29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plugin"):
                opp_val = getattr(old_value, "plugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plugin"):
                opp_val = getattr(value, "plugin", None)
                if opp_val is None:
                    setattr(value, "plugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourcecleaner_Extension:

    def __init__(self, pointId: str, clazz: str, id: str, name: str, extra: str, diagraph: bool, extensions: "sourcecleaner_ExtensionPoint" = None, Extension: "sourcecleaner_ExtensionPoint" = None, sourcecleaner_Extension27: "sourcecleaner_Plugin" = None, sourcecleaner_Extension: set["sourcecleaner_ExtensionAttribute"] = None, sourcecleaner_Extension19: "sourcecleaner_Java" = None):
        self.pointId = pointId
        self.clazz = clazz
        self.id = id
        self.name = name
        self.extra = extra
        self.diagraph = diagraph
        self.extensions = extensions
        self.Extension = Extension
        self.sourcecleaner_Extension27 = sourcecleaner_Extension27
        self.sourcecleaner_Extension = sourcecleaner_Extension if sourcecleaner_Extension is not None else set()
        self.sourcecleaner_Extension19 = sourcecleaner_Extension19
        
        pass
    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, extra: str):
        self.__extra = extra


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def diagraph(self):
        return self.__diagraph

    @diagraph.setter
    def diagraph(self, diagraph: bool):
        self.__diagraph = diagraph


    @property
    def clazz(self):
        return self.__clazz

    @clazz.setter
    def clazz(self, clazz: str):
        self.__clazz = clazz


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pointId(self):
        return self.__pointId

    @pointId.setter
    def pointId(self, pointId: str):
        self.__pointId = pointId


    @property
    def extensions(self):
        return self.__extensions

    @extensions.setter
    def extensions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Extension__extensions", None)
        self.__extensions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExtensionPoint"):
                opp_val = getattr(old_value, "ExtensionPoint", None)
                if opp_val == self:
                    setattr(old_value, "ExtensionPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExtensionPoint"):
                opp_val = getattr(value, "ExtensionPoint", None)
                setattr(value, "ExtensionPoint", self)

    @property
    def sourcecleaner_Extension(self):
        return self.__sourcecleaner_Extension

    @sourcecleaner_Extension.setter
    def sourcecleaner_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Extension__sourcecleaner_Extension", None)
        self.__sourcecleaner_Extension = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sourcecleaner_ExtensionAttribute"):
                    opp_val = getattr(item, "sourcecleaner_ExtensionAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "sourcecleaner_ExtensionAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sourcecleaner_ExtensionAttribute"):
                    opp_val = getattr(item, "sourcecleaner_ExtensionAttribute", None)
                    
                    setattr(item, "sourcecleaner_ExtensionAttribute", self)
                    

    @property
    def Extension(self):
        return self.__Extension

    @Extension.setter
    def Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Extension__Extension", None)
        self.__Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionPoint"):
                opp_val = getattr(old_value, "extensionPoint", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionPoint"):
                opp_val = getattr(value, "extensionPoint", None)
                if opp_val is None:
                    setattr(value, "extensionPoint", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sourcecleaner_Extension19(self):
        return self.__sourcecleaner_Extension19

    @sourcecleaner_Extension19.setter
    def sourcecleaner_Extension19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Extension__sourcecleaner_Extension19", None)
        self.__sourcecleaner_Extension19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Java"):
                opp_val = getattr(old_value, "sourcecleaner_Java", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Java", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Java"):
                opp_val = getattr(value, "sourcecleaner_Java", None)
                setattr(value, "sourcecleaner_Java", self)

    @property
    def sourcecleaner_Extension27(self):
        return self.__sourcecleaner_Extension27

    @sourcecleaner_Extension27.setter
    def sourcecleaner_Extension27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Extension__sourcecleaner_Extension27", None)
        self.__sourcecleaner_Extension27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Plugin"):
                opp_val = getattr(old_value, "sourcecleaner_Plugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Plugin"):
                opp_val = getattr(value, "sourcecleaner_Plugin", None)
                if opp_val is None:
                    setattr(value, "sourcecleaner_Plugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourcecleaner_Export:

    def __init__(self, name: str, sourcecleaner_Export: "sourcecleaner_Manifest" = None):
        self.name = name
        self.sourcecleaner_Export = sourcecleaner_Export
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourcecleaner_Export(self):
        return self.__sourcecleaner_Export

    @sourcecleaner_Export.setter
    def sourcecleaner_Export(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Export__sourcecleaner_Export", None)
        self.__sourcecleaner_Export = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Manifest15"):
                opp_val = getattr(old_value, "sourcecleaner_Manifest15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Manifest15"):
                opp_val = getattr(value, "sourcecleaner_Manifest15", None)
                if opp_val is None:
                    setattr(value, "sourcecleaner_Manifest15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sourcecleaner_ClassPath:

    def __init__(self, name: str, sourcecleaner_ClassPath: "sourcecleaner_Manifest" = None):
        self.name = name
        self.sourcecleaner_ClassPath = sourcecleaner_ClassPath
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sourcecleaner_ClassPath(self):
        return self.__sourcecleaner_ClassPath

    @sourcecleaner_ClassPath.setter
    def sourcecleaner_ClassPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_ClassPath__sourcecleaner_ClassPath", None)
        self.__sourcecleaner_ClassPath = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Manifest13"):
                opp_val = getattr(old_value, "sourcecleaner_Manifest13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Manifest13"):
                opp_val = getattr(value, "sourcecleaner_Manifest13", None)
                if opp_val is None:
                    setattr(value, "sourcecleaner_Manifest13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LocatedElement:

    pass
class sourcecleaner_Source(LocatedElement):

    def __init__(self, comment: str, handled: bool, mark: bool, content: str):
        self.comment = comment
        self.handled = handled
        self.mark = mark
        self.content = content
        
        pass
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content


    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark: bool):
        self.__mark = mark


    @property
    def handled(self):
        return self.__handled

    @handled.setter
    def handled(self, handled: bool):
        self.__handled = handled


    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment


class sourcecleaner_Project(LocatedElement):

    def __init__(self, id: int, workspace: str, project: set["sourcecleaner_Java"] = None, sourcecleaner_Project3: "sourcecleaner_Manifest" = None, sourcecleaner_Project5: "sourcecleaner_Build" = None, project7: "sourcecleaner_Plugin" = None, sourcecleaner_Project: "sourcecleaner_Configuration" = None, project9: "sourcecleaner_Schema" = None, Project: "sourcecleaner_Java" = None, Project32: "sourcecleaner_Plugin" = None, Project36: "sourcecleaner_Schema" = None):
        self.id = id
        self.workspace = workspace
        self.project = project if project is not None else set()
        self.sourcecleaner_Project3 = sourcecleaner_Project3
        self.sourcecleaner_Project5 = sourcecleaner_Project5
        self.project7 = project7
        self.sourcecleaner_Project = sourcecleaner_Project
        self.project9 = project9
        self.Project = Project
        self.Project32 = Project32
        self.Project36 = Project36
        
        pass
    @property
    def workspace(self):
        return self.__workspace

    @workspace.setter
    def workspace(self, workspace: str):
        self.__workspace = workspace


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Java"):
                    opp_val = getattr(item, "Java", None)
                    
                    if opp_val == self:
                        setattr(item, "Java", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Java"):
                    opp_val = getattr(item, "Java", None)
                    
                    setattr(item, "Java", self)
                    

    @property
    def sourcecleaner_Project5(self):
        return self.__sourcecleaner_Project5

    @sourcecleaner_Project5.setter
    def sourcecleaner_Project5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__sourcecleaner_Project5", None)
        self.__sourcecleaner_Project5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Build"):
                opp_val = getattr(old_value, "sourcecleaner_Build", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Build", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Build"):
                opp_val = getattr(value, "sourcecleaner_Build", None)
                setattr(value, "sourcecleaner_Build", self)

    @property
    def Project32(self):
        return self.__Project32

    @Project32.setter
    def Project32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__Project32", None)
        self.__Project32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "plugin31"):
                opp_val = getattr(old_value, "plugin31", None)
                if opp_val == self:
                    setattr(old_value, "plugin31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "plugin31"):
                opp_val = getattr(value, "plugin31", None)
                setattr(value, "plugin31", self)

    @property
    def sourcecleaner_Project3(self):
        return self.__sourcecleaner_Project3

    @sourcecleaner_Project3.setter
    def sourcecleaner_Project3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__sourcecleaner_Project3", None)
        self.__sourcecleaner_Project3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Manifest"):
                opp_val = getattr(old_value, "sourcecleaner_Manifest", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Manifest", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Manifest"):
                opp_val = getattr(value, "sourcecleaner_Manifest", None)
                setattr(value, "sourcecleaner_Manifest", self)

    @property
    def project9(self):
        return self.__project9

    @project9.setter
    def project9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__project9", None)
        self.__project9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Schema"):
                opp_val = getattr(old_value, "Schema", None)
                if opp_val == self:
                    setattr(old_value, "Schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Schema"):
                opp_val = getattr(value, "Schema", None)
                setattr(value, "Schema", self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sources"):
                opp_val = getattr(old_value, "sources", None)
                if opp_val == self:
                    setattr(old_value, "sources", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sources"):
                opp_val = getattr(value, "sources", None)
                setattr(value, "sources", self)

    @property
    def sourcecleaner_Project(self):
        return self.__sourcecleaner_Project

    @sourcecleaner_Project.setter
    def sourcecleaner_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__sourcecleaner_Project", None)
        self.__sourcecleaner_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Configuration"):
                opp_val = getattr(old_value, "sourcecleaner_Configuration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Configuration"):
                opp_val = getattr(value, "sourcecleaner_Configuration", None)
                if opp_val is None:
                    setattr(value, "sourcecleaner_Configuration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project36(self):
        return self.__Project36

    @Project36.setter
    def Project36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__Project36", None)
        self.__Project36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schema35"):
                opp_val = getattr(old_value, "schema35", None)
                if opp_val == self:
                    setattr(old_value, "schema35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schema35"):
                opp_val = getattr(value, "schema35", None)
                setattr(value, "schema35", self)

    @property
    def project7(self):
        return self.__project7

    @project7.setter
    def project7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Project__project7", None)
        self.__project7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Plugin"):
                opp_val = getattr(old_value, "Plugin", None)
                if opp_val == self:
                    setattr(old_value, "Plugin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Plugin"):
                opp_val = getattr(value, "Plugin", None)
                setattr(value, "Plugin", self)

class sourcecleaner_Configuration:

    def __init__(self, location: str, temp: str, sourcecleaner_Configuration: set["sourcecleaner_Project"] = None):
        self.location = location
        self.temp = temp
        self.sourcecleaner_Configuration = sourcecleaner_Configuration if sourcecleaner_Configuration is not None else set()
        
        pass
    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, temp: str):
        self.__temp = temp


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def sourcecleaner_Configuration(self):
        return self.__sourcecleaner_Configuration

    @sourcecleaner_Configuration.setter
    def sourcecleaner_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Configuration__sourcecleaner_Configuration", None)
        self.__sourcecleaner_Configuration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sourcecleaner_Project"):
                    opp_val = getattr(item, "sourcecleaner_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "sourcecleaner_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sourcecleaner_Project"):
                    opp_val = getattr(item, "sourcecleaner_Project", None)
                    
                    setattr(item, "sourcecleaner_Project", self)
                    

class sourcecleaner_Plugin(Source):

    def __init__(self, extra: str, Plugin: "sourcecleaner_Project" = None, Plugin25: "sourcecleaner_ExtensionPoint" = None, sourcecleaner_Plugin: set["sourcecleaner_Extension"] = None, plugin: set["sourcecleaner_ExtensionPoint"] = None, plugin31: "sourcecleaner_Project" = None):
        self.extra = extra
        self.Plugin = Plugin
        self.Plugin25 = Plugin25
        self.sourcecleaner_Plugin = sourcecleaner_Plugin if sourcecleaner_Plugin is not None else set()
        self.plugin = plugin if plugin is not None else set()
        self.plugin31 = plugin31
        
        pass
    @property
    def extra(self):
        return self.__extra

    @extra.setter
    def extra(self, extra: str):
        self.__extra = extra


    @property
    def Plugin(self):
        return self.__Plugin

    @Plugin.setter
    def Plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Plugin__Plugin", None)
        self.__Plugin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project7"):
                opp_val = getattr(old_value, "project7", None)
                if opp_val == self:
                    setattr(old_value, "project7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project7"):
                opp_val = getattr(value, "project7", None)
                setattr(value, "project7", self)

    @property
    def plugin31(self):
        return self.__plugin31

    @plugin31.setter
    def plugin31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Plugin__plugin31", None)
        self.__plugin31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project32"):
                opp_val = getattr(old_value, "Project32", None)
                if opp_val == self:
                    setattr(old_value, "Project32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project32"):
                opp_val = getattr(value, "Project32", None)
                setattr(value, "Project32", self)

    @property
    def sourcecleaner_Plugin(self):
        return self.__sourcecleaner_Plugin

    @sourcecleaner_Plugin.setter
    def sourcecleaner_Plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Plugin__sourcecleaner_Plugin", None)
        self.__sourcecleaner_Plugin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sourcecleaner_Extension27"):
                    opp_val = getattr(item, "sourcecleaner_Extension27", None)
                    
                    if opp_val == self:
                        setattr(item, "sourcecleaner_Extension27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sourcecleaner_Extension27"):
                    opp_val = getattr(item, "sourcecleaner_Extension27", None)
                    
                    setattr(item, "sourcecleaner_Extension27", self)
                    

    @property
    def plugin(self):
        return self.__plugin

    @plugin.setter
    def plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Plugin__plugin", None)
        self.__plugin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExtensionPoint29"):
                    opp_val = getattr(item, "ExtensionPoint29", None)
                    
                    if opp_val == self:
                        setattr(item, "ExtensionPoint29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExtensionPoint29"):
                    opp_val = getattr(item, "ExtensionPoint29", None)
                    
                    setattr(item, "ExtensionPoint29", self)
                    

    @property
    def Plugin25(self):
        return self.__Plugin25

    @Plugin25.setter
    def Plugin25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Plugin__Plugin25", None)
        self.__Plugin25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extensionPoints"):
                opp_val = getattr(old_value, "extensionPoints", None)
                if opp_val == self:
                    setattr(old_value, "extensionPoints", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extensionPoints"):
                opp_val = getattr(value, "extensionPoints", None)
                setattr(value, "extensionPoints", self)

class sourcecleaner_Build(Source):

    pass
class sourcecleaner_Manifest(Source):

    def __init__(self, lazy: bool, executionEnvironment: str, diagraph: bool, symbolicName: str, singleton: bool, vendor: str, version: str, versionId: str, versionQualifier: str, sourcecleaner_Manifest: "sourcecleaner_Project" = None, requerant: set["sourcecleaner_Dependency"] = None, sourcecleaner_Manifest13: set["sourcecleaner_ClassPath"] = None, sourcecleaner_Manifest15: set["sourcecleaner_Export"] = None, sourcecleaner_Manifest21: "sourcecleaner_Dependency" = None, Manifest: "sourcecleaner_Dependency" = None):
        self.lazy = lazy
        self.executionEnvironment = executionEnvironment
        self.diagraph = diagraph
        self.symbolicName = symbolicName
        self.singleton = singleton
        self.vendor = vendor
        self.version = version
        self.versionId = versionId
        self.versionQualifier = versionQualifier
        self.sourcecleaner_Manifest = sourcecleaner_Manifest
        self.requerant = requerant if requerant is not None else set()
        self.sourcecleaner_Manifest13 = sourcecleaner_Manifest13 if sourcecleaner_Manifest13 is not None else set()
        self.sourcecleaner_Manifest15 = sourcecleaner_Manifest15 if sourcecleaner_Manifest15 is not None else set()
        self.sourcecleaner_Manifest21 = sourcecleaner_Manifest21
        self.Manifest = Manifest
        
        pass
    @property
    def symbolicName(self):
        return self.__symbolicName

    @symbolicName.setter
    def symbolicName(self, symbolicName: str):
        self.__symbolicName = symbolicName


    @property
    def executionEnvironment(self):
        return self.__executionEnvironment

    @executionEnvironment.setter
    def executionEnvironment(self, executionEnvironment: str):
        self.__executionEnvironment = executionEnvironment


    @property
    def singleton(self):
        return self.__singleton

    @singleton.setter
    def singleton(self, singleton: bool):
        self.__singleton = singleton


    @property
    def versionId(self):
        return self.__versionId

    @versionId.setter
    def versionId(self, versionId: str):
        self.__versionId = versionId


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def diagraph(self):
        return self.__diagraph

    @diagraph.setter
    def diagraph(self, diagraph: bool):
        self.__diagraph = diagraph


    @property
    def lazy(self):
        return self.__lazy

    @lazy.setter
    def lazy(self, lazy: bool):
        self.__lazy = lazy


    @property
    def versionQualifier(self):
        return self.__versionQualifier

    @versionQualifier.setter
    def versionQualifier(self, versionQualifier: str):
        self.__versionQualifier = versionQualifier


    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor: str):
        self.__vendor = vendor


    @property
    def sourcecleaner_Manifest21(self):
        return self.__sourcecleaner_Manifest21

    @sourcecleaner_Manifest21.setter
    def sourcecleaner_Manifest21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__sourcecleaner_Manifest21", None)
        self.__sourcecleaner_Manifest21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Dependency"):
                opp_val = getattr(old_value, "sourcecleaner_Dependency", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Dependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Dependency"):
                opp_val = getattr(value, "sourcecleaner_Dependency", None)
                setattr(value, "sourcecleaner_Dependency", self)

    @property
    def requerant(self):
        return self.__requerant

    @requerant.setter
    def requerant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__requerant", None)
        self.__requerant = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Dependency"):
                    opp_val = getattr(item, "Dependency", None)
                    
                    setattr(item, "Dependency", self)
                    

    @property
    def sourcecleaner_Manifest15(self):
        return self.__sourcecleaner_Manifest15

    @sourcecleaner_Manifest15.setter
    def sourcecleaner_Manifest15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__sourcecleaner_Manifest15", None)
        self.__sourcecleaner_Manifest15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sourcecleaner_Export"):
                    opp_val = getattr(item, "sourcecleaner_Export", None)
                    
                    if opp_val == self:
                        setattr(item, "sourcecleaner_Export", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sourcecleaner_Export"):
                    opp_val = getattr(item, "sourcecleaner_Export", None)
                    
                    setattr(item, "sourcecleaner_Export", self)
                    

    @property
    def Manifest(self):
        return self.__Manifest

    @Manifest.setter
    def Manifest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__Manifest", None)
        self.__Manifest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dependencies"):
                opp_val = getattr(old_value, "dependencies", None)
                if opp_val == self:
                    setattr(old_value, "dependencies", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dependencies"):
                opp_val = getattr(value, "dependencies", None)
                setattr(value, "dependencies", self)

    @property
    def sourcecleaner_Manifest13(self):
        return self.__sourcecleaner_Manifest13

    @sourcecleaner_Manifest13.setter
    def sourcecleaner_Manifest13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__sourcecleaner_Manifest13", None)
        self.__sourcecleaner_Manifest13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sourcecleaner_ClassPath"):
                    opp_val = getattr(item, "sourcecleaner_ClassPath", None)
                    
                    if opp_val == self:
                        setattr(item, "sourcecleaner_ClassPath", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sourcecleaner_ClassPath"):
                    opp_val = getattr(item, "sourcecleaner_ClassPath", None)
                    
                    setattr(item, "sourcecleaner_ClassPath", self)
                    

    @property
    def sourcecleaner_Manifest(self):
        return self.__sourcecleaner_Manifest

    @sourcecleaner_Manifest.setter
    def sourcecleaner_Manifest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Manifest__sourcecleaner_Manifest", None)
        self.__sourcecleaner_Manifest = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Project3"):
                opp_val = getattr(old_value, "sourcecleaner_Project3", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Project3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Project3"):
                opp_val = getattr(value, "sourcecleaner_Project3", None)
                setattr(value, "sourcecleaner_Project3", self)

class sourcecleaner_Java(Source):

    def __init__(self, package: str, Java: "sourcecleaner_Project" = None, sources: "sourcecleaner_Project" = None, sourcecleaner_Java: "sourcecleaner_Extension" = None, sourcecleaner_Java40: "sourcecleaner_ExtensionReference" = None):
        self.package = package
        self.Java = Java
        self.sources = sources
        self.sourcecleaner_Java = sourcecleaner_Java
        self.sourcecleaner_Java40 = sourcecleaner_Java40
        
        pass
    @property
    def package(self):
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package


    @property
    def Java(self):
        return self.__Java

    @Java.setter
    def Java(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Java__Java", None)
        self.__Java = value
        
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
    def sources(self):
        return self.__sources

    @sources.setter
    def sources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Java__sources", None)
        self.__sources = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project"):
                opp_val = getattr(old_value, "Project", None)
                if opp_val == self:
                    setattr(old_value, "Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project"):
                opp_val = getattr(value, "Project", None)
                setattr(value, "Project", self)

    @property
    def sourcecleaner_Java(self):
        return self.__sourcecleaner_Java

    @sourcecleaner_Java.setter
    def sourcecleaner_Java(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Java__sourcecleaner_Java", None)
        self.__sourcecleaner_Java = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_Extension19"):
                opp_val = getattr(old_value, "sourcecleaner_Extension19", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_Extension19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_Extension19"):
                opp_val = getattr(value, "sourcecleaner_Extension19", None)
                setattr(value, "sourcecleaner_Extension19", self)

    @property
    def sourcecleaner_Java40(self):
        return self.__sourcecleaner_Java40

    @sourcecleaner_Java40.setter
    def sourcecleaner_Java40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sourcecleaner_Java__sourcecleaner_Java40", None)
        self.__sourcecleaner_Java40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourcecleaner_ExtensionReference"):
                opp_val = getattr(old_value, "sourcecleaner_ExtensionReference", None)
                if opp_val == self:
                    setattr(old_value, "sourcecleaner_ExtensionReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourcecleaner_ExtensionReference"):
                opp_val = getattr(value, "sourcecleaner_ExtensionReference", None)
                setattr(value, "sourcecleaner_ExtensionReference", self)
