from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Ant_Java:

    def __init__(self, classname: str, jar: str, fork: str, Ant_Java: "ClassPath" = None):
        self.classname = classname
        self.jar = jar
        self.fork = fork
        self.Ant_Java = Ant_Java
        
        pass
    @property
    def jar(self):
        return self.__jar

    @jar.setter
    def jar(self, jar: str):
        self.__jar = jar


    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def Ant_Java(self):
        return self.__Ant_Java

    @Ant_Java.setter
    def Ant_Java(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Java__Ant_Java", None)
        self.__Ant_Java = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassPath"):
                opp_val = getattr(old_value, "ClassPath", None)
                if opp_val == self:
                    setattr(old_value, "ClassPath", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassPath"):
                opp_val = getattr(value, "ClassPath", None)
                setattr(value, "ClassPath", self)

class Ant_Exec:

    def __init__(self, executable: str, dir: str):
        self.executable = executable
        self.dir = dir
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def executable(self):
        return self.__executable

    @executable.setter
    def executable(self, executable: str):
        self.__executable = executable


class PreDefinedTask:

    pass
class Ant_ExecutionTask(PreDefinedTask):

    pass
class Ant_Attribut:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
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


class CompileTask:

    pass
class Ant_Javac(CompileTask):

    def __init__(self, srcdir: str, destdir: str, debug: str, fork: str, optimize: str, deprecation: str, Ant_Javac: set["InExcludes"] = None, Ant_Javac44: "ClassPath" = None):
        self.srcdir = srcdir
        self.destdir = destdir
        self.debug = debug
        self.fork = fork
        self.optimize = optimize
        self.deprecation = deprecation
        self.Ant_Javac = Ant_Javac if Ant_Javac is not None else set()
        self.Ant_Javac44 = Ant_Javac44
        
        pass
    @property
    def optimize(self):
        return self.__optimize

    @optimize.setter
    def optimize(self, optimize: str):
        self.__optimize = optimize


    @property
    def destdir(self):
        return self.__destdir

    @destdir.setter
    def destdir(self, destdir: str):
        self.__destdir = destdir


    @property
    def srcdir(self):
        return self.__srcdir

    @srcdir.setter
    def srcdir(self, srcdir: str):
        self.__srcdir = srcdir


    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug: str):
        self.__debug = debug


    @property
    def deprecation(self):
        return self.__deprecation

    @deprecation.setter
    def deprecation(self, deprecation: str):
        self.__deprecation = deprecation


    @property
    def Ant_Javac(self):
        return self.__Ant_Javac

    @Ant_Javac.setter
    def Ant_Javac(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Javac__Ant_Javac", None)
        self.__Ant_Javac = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InExcludes42"):
                    opp_val = getattr(item, "InExcludes42", None)
                    
                    if opp_val == self:
                        setattr(item, "InExcludes42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InExcludes42"):
                    opp_val = getattr(item, "InExcludes42", None)
                    
                    setattr(item, "InExcludes42", self)
                    

    @property
    def Ant_Javac44(self):
        return self.__Ant_Javac44

    @Ant_Javac44.setter
    def Ant_Javac44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Javac__Ant_Javac44", None)
        self.__Ant_Javac44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassPath45"):
                opp_val = getattr(old_value, "ClassPath45", None)
                if opp_val == self:
                    setattr(old_value, "ClassPath45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassPath45"):
                opp_val = getattr(value, "ClassPath45", None)
                setattr(value, "ClassPath45", self)

class Ant_TaskDef:

    def __init__(self, classname: str, name: str):
        self.classname = classname
        self.name = name
        
        pass
    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Ant_Task(ABC):

    pass
class FileSet:

    pass
class PathElement:

    pass
class FiltersFile:

    pass
class Filter:

    pass
class Excludes:

    pass
class Includes:

    pass
class Attribut:

    pass
class Set:

    pass
class Ant_Path(Set):

    def __init__(self, id: str, refid: str, Ant_Path: "Path" = None, Ant_Path25: set["PathElement"] = None, Ant_Path27: set["FileSet"] = None):
        self.id = id
        self.refid = refid
        self.Ant_Path = Ant_Path
        self.Ant_Path25 = Ant_Path25 if Ant_Path25 is not None else set()
        self.Ant_Path27 = Ant_Path27 if Ant_Path27 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def Ant_Path27(self):
        return self.__Ant_Path27

    @Ant_Path27.setter
    def Ant_Path27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path27", None)
        self.__Ant_Path27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileSet"):
                    opp_val = getattr(item, "FileSet", None)
                    
                    if opp_val == self:
                        setattr(item, "FileSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileSet"):
                    opp_val = getattr(item, "FileSet", None)
                    
                    setattr(item, "FileSet", self)
                    

    @property
    def Ant_Path25(self):
        return self.__Ant_Path25

    @Ant_Path25.setter
    def Ant_Path25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path25", None)
        self.__Ant_Path25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PathElement"):
                    opp_val = getattr(item, "PathElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PathElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PathElement"):
                    opp_val = getattr(item, "PathElement", None)
                    
                    setattr(item, "PathElement", self)
                    

    @property
    def Ant_Path(self):
        return self.__Ant_Path

    @Ant_Path.setter
    def Ant_Path(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path", None)
        self.__Ant_Path = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Path23"):
                opp_val = getattr(old_value, "Path23", None)
                if opp_val == self:
                    setattr(old_value, "Path23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Path23"):
                opp_val = getattr(value, "Path23", None)
                setattr(value, "Path23", self)

class Ant_ClassPath(Set):

    def __init__(self, refid: str, Ant_ClassPath: set["PathElement"] = None, Ant_ClassPath31: set["FileSet"] = None):
        self.refid = refid
        self.Ant_ClassPath = Ant_ClassPath if Ant_ClassPath is not None else set()
        self.Ant_ClassPath31 = Ant_ClassPath31 if Ant_ClassPath31 is not None else set()
        
        pass
    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def Ant_ClassPath31(self):
        return self.__Ant_ClassPath31

    @Ant_ClassPath31.setter
    def Ant_ClassPath31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_ClassPath__Ant_ClassPath31", None)
        self.__Ant_ClassPath31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileSet32"):
                    opp_val = getattr(item, "FileSet32", None)
                    
                    if opp_val == self:
                        setattr(item, "FileSet32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileSet32"):
                    opp_val = getattr(item, "FileSet32", None)
                    
                    setattr(item, "FileSet32", self)
                    

    @property
    def Ant_ClassPath(self):
        return self.__Ant_ClassPath

    @Ant_ClassPath.setter
    def Ant_ClassPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_ClassPath__Ant_ClassPath", None)
        self.__Ant_ClassPath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PathElement29"):
                    opp_val = getattr(item, "PathElement29", None)
                    
                    if opp_val == self:
                        setattr(item, "PathElement29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PathElement29"):
                    opp_val = getattr(item, "PathElement29", None)
                    
                    setattr(item, "PathElement29", self)
                    

class Ant_FilterSet(Set):

    def __init__(self, starttoken: str, endtoken: str, Ant_FilterSet: set["Filter"] = None, Ant_FilterSet21: set["FiltersFile"] = None):
        self.starttoken = starttoken
        self.endtoken = endtoken
        self.Ant_FilterSet = Ant_FilterSet if Ant_FilterSet is not None else set()
        self.Ant_FilterSet21 = Ant_FilterSet21 if Ant_FilterSet21 is not None else set()
        
        pass
    @property
    def endtoken(self):
        return self.__endtoken

    @endtoken.setter
    def endtoken(self, endtoken: str):
        self.__endtoken = endtoken


    @property
    def starttoken(self):
        return self.__starttoken

    @starttoken.setter
    def starttoken(self, starttoken: str):
        self.__starttoken = starttoken


    @property
    def Ant_FilterSet21(self):
        return self.__Ant_FilterSet21

    @Ant_FilterSet21.setter
    def Ant_FilterSet21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FilterSet__Ant_FilterSet21", None)
        self.__Ant_FilterSet21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FiltersFile"):
                    opp_val = getattr(item, "FiltersFile", None)
                    
                    if opp_val == self:
                        setattr(item, "FiltersFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FiltersFile"):
                    opp_val = getattr(item, "FiltersFile", None)
                    
                    setattr(item, "FiltersFile", self)
                    

    @property
    def Ant_FilterSet(self):
        return self.__Ant_FilterSet

    @Ant_FilterSet.setter
    def Ant_FilterSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FilterSet__Ant_FilterSet", None)
        self.__Ant_FilterSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Filter"):
                    opp_val = getattr(item, "Filter", None)
                    
                    if opp_val == self:
                        setattr(item, "Filter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Filter"):
                    opp_val = getattr(item, "Filter", None)
                    
                    setattr(item, "Filter", self)
                    

class Ant_PatternSet(Set):

    pass
class InExcludes:

    pass
class Ant_IncludesFile(InExcludes):

    pass
class Ant_Excludes(InExcludes):

    pass
class Ant_ExcludesFile(InExcludes):

    pass
class Ant_Includes(InExcludes):

    pass
class PatternSet:

    pass
class Ant_FileSet(Set):

    def __init__(self, dir: str, Ant_FileSet: set["PatternSet"] = None, Ant_FileSet16: set["Includes"] = None, Ant_FileSet18: set["Excludes"] = None):
        self.dir = dir
        self.Ant_FileSet = Ant_FileSet if Ant_FileSet is not None else set()
        self.Ant_FileSet16 = Ant_FileSet16 if Ant_FileSet16 is not None else set()
        self.Ant_FileSet18 = Ant_FileSet18 if Ant_FileSet18 is not None else set()
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def Ant_FileSet16(self):
        return self.__Ant_FileSet16

    @Ant_FileSet16.setter
    def Ant_FileSet16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet16", None)
        self.__Ant_FileSet16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Includes"):
                    opp_val = getattr(item, "Includes", None)
                    
                    if opp_val == self:
                        setattr(item, "Includes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Includes"):
                    opp_val = getattr(item, "Includes", None)
                    
                    setattr(item, "Includes", self)
                    

    @property
    def Ant_FileSet18(self):
        return self.__Ant_FileSet18

    @Ant_FileSet18.setter
    def Ant_FileSet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet18", None)
        self.__Ant_FileSet18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Excludes"):
                    opp_val = getattr(item, "Excludes", None)
                    
                    if opp_val == self:
                        setattr(item, "Excludes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Excludes"):
                    opp_val = getattr(item, "Excludes", None)
                    
                    setattr(item, "Excludes", self)
                    

    @property
    def Ant_FileSet(self):
        return self.__Ant_FileSet

    @Ant_FileSet.setter
    def Ant_FileSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet", None)
        self.__Ant_FileSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PatternSet"):
                    opp_val = getattr(item, "PatternSet", None)
                    
                    if opp_val == self:
                        setattr(item, "PatternSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PatternSet"):
                    opp_val = getattr(item, "PatternSet", None)
                    
                    setattr(item, "PatternSet", self)
                    

class Task:

    pass
class Ant_PreDefinedTask(Task):

    def __init__(self, id: str, taskname: str, description: str, Task: "Ant_Target" = None):
        self.id = id
        self.taskname = taskname
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def taskname(self):
        return self.__taskname

    @taskname.setter
    def taskname(self, taskname: str):
        self.__taskname = taskname


class Ant_NewTask(Task):

    pass
class Ant_Target:

    def __init__(self, name: str, description: str, unless: str, ifCondition: str, Ant_Target: set["Target"] = None, target: set["Task"] = None):
        self.name = name
        self.description = description
        self.unless = unless
        self.ifCondition = ifCondition
        self.Ant_Target = Ant_Target if Ant_Target is not None else set()
        self.target = target if target is not None else set()
        
        pass
    @property
    def ifCondition(self):
        return self.__ifCondition

    @ifCondition.setter
    def ifCondition(self, ifCondition: str):
        self.__ifCondition = ifCondition


    @property
    def unless(self):
        return self.__unless

    @unless.setter
    def unless(self, unless: str):
        self.__unless = unless


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    if opp_val == self:
                        setattr(item, "Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    setattr(item, "Task", self)
                    

    @property
    def Ant_Target(self):
        return self.__Ant_Target

    @Ant_Target.setter
    def Ant_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Ant_Target", None)
        self.__Ant_Target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Target11"):
                    opp_val = getattr(item, "Target11", None)
                    
                    if opp_val == self:
                        setattr(item, "Target11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Target11"):
                    opp_val = getattr(item, "Target11", None)
                    
                    setattr(item, "Target11", self)
                    

class PropertyName:

    pass
class Ant_PropertyLocation(PropertyName):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class Ant_PropertyValue(PropertyName):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Ant_Property(ABC):

    pass
class TaskDef:

    pass
class Property:

    pass
class Ant_PropertyName(Property):

    def __init__(self, name: str, Property: "Ant_Project" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Ant_PropertyEnv(Property):

    def __init__(self, environment: str, Property: "Ant_Project" = None):
        self.environment = environment
        
        pass
    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment


class Ant_PropertyFile(Property):

    def __init__(self, file: str, Property: "Ant_Project" = None):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class Basic:

    pass
class Ant_InExcludes(Basic):

    def __init__(self, name: str, ifCondition: str, unless: str):
        self.name = name
        self.ifCondition = ifCondition
        self.unless = unless
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def unless(self):
        return self.__unless

    @unless.setter
    def unless(self, unless: str):
        self.__unless = unless


    @property
    def ifCondition(self):
        return self.__ifCondition

    @ifCondition.setter
    def ifCondition(self, ifCondition: str):
        self.__ifCondition = ifCondition


class Ant_Filter(Basic):

    def __init__(self, token: str, value: str):
        self.token = token
        self.value = value
        
        pass
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Ant_PathElement(Basic):

    def __init__(self, path: str, location: str):
        self.path = path
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


class Ant_FiltersFile(Basic):

    def __init__(self, file: str):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class Ant_FileList(Basic):

    def __init__(self, dir: str, files: str):
        self.dir = dir
        self.files = files
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files: str):
        self.__files = files


class Ant_Mapper(Basic):

    def __init__(self, type: str, classname: str, classpath: str, classpathref: str, from_: str, to: str):
        self.type = type
        self.classname = classname
        self.classpath = classpath
        self.classpathref = classpathref
        self.from_ = from_
        self.to = to
        
        pass
    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def classpathref(self):
        return self.__classpathref

    @classpathref.setter
    def classpathref(self, classpathref: str):
        self.__classpathref = classpathref


    @property
    def classpath(self):
        return self.__classpath

    @classpath.setter
    def classpath(self, classpath: str):
        self.__classpath = classpath


class Pattern:

    pass
class Ant_Set(Pattern):

    pass
class Ant_Basic(Pattern):

    pass
class Ant_Pattern(ABC):

    pass
class Target:

    pass
class Ant_Project:

    def __init__(self, name: str, basedir: str, description: str, Ant_Project: "Target" = None, Ant_Project2: "Path" = None, Ant_Project4: set["Property"] = None, Ant_Project6: set["TaskDef"] = None, Ant_Project8: set["Target"] = None):
        self.name = name
        self.basedir = basedir
        self.description = description
        self.Ant_Project = Ant_Project
        self.Ant_Project2 = Ant_Project2
        self.Ant_Project4 = Ant_Project4 if Ant_Project4 is not None else set()
        self.Ant_Project6 = Ant_Project6 if Ant_Project6 is not None else set()
        self.Ant_Project8 = Ant_Project8 if Ant_Project8 is not None else set()
        
        pass
    @property
    def basedir(self):
        return self.__basedir

    @basedir.setter
    def basedir(self, basedir: str):
        self.__basedir = basedir


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def Ant_Project6(self):
        return self.__Ant_Project6

    @Ant_Project6.setter
    def Ant_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Project__Ant_Project6", None)
        self.__Ant_Project6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TaskDef"):
                    opp_val = getattr(item, "TaskDef", None)
                    
                    if opp_val == self:
                        setattr(item, "TaskDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TaskDef"):
                    opp_val = getattr(item, "TaskDef", None)
                    
                    setattr(item, "TaskDef", self)
                    

    @property
    def Ant_Project(self):
        return self.__Ant_Project

    @Ant_Project.setter
    def Ant_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Project__Ant_Project", None)
        self.__Ant_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Target"):
                opp_val = getattr(old_value, "Target", None)
                if opp_val == self:
                    setattr(old_value, "Target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Target"):
                opp_val = getattr(value, "Target", None)
                setattr(value, "Target", self)

    @property
    def Ant_Project2(self):
        return self.__Ant_Project2

    @Ant_Project2.setter
    def Ant_Project2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Project__Ant_Project2", None)
        self.__Ant_Project2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Path"):
                opp_val = getattr(old_value, "Path", None)
                if opp_val == self:
                    setattr(old_value, "Path", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Path"):
                opp_val = getattr(value, "Path", None)
                setattr(value, "Path", self)

    @property
    def Ant_Project4(self):
        return self.__Ant_Project4

    @Ant_Project4.setter
    def Ant_Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Project__Ant_Project4", None)
        self.__Ant_Project4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property"):
                    opp_val = getattr(item, "Property", None)
                    
                    setattr(item, "Property", self)
                    

    @property
    def Ant_Project8(self):
        return self.__Ant_Project8

    @Ant_Project8.setter
    def Ant_Project8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Project__Ant_Project8", None)
        self.__Ant_Project8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Target9"):
                    opp_val = getattr(item, "Target9", None)
                    
                    if opp_val == self:
                        setattr(item, "Target9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Target9"):
                    opp_val = getattr(item, "Target9", None)
                    
                    setattr(item, "Target9", self)
                    

class Path:

    pass
class Mapper:

    pass
class FilterSet:

    pass
class FileTask:

    pass
class Ant_Copy(FileTask):

    def __init__(self, presservelastmodified: str, tofile: str, todir: str, overwrite: str, filtering: str, file: str, flatten: str, includeEmptyDirs: str, Ant_Copy: "FileSet" = None, Ant_Copy49: "FilterSet" = None, Ant_Copy51: "Mapper" = None):
        self.presservelastmodified = presservelastmodified
        self.tofile = tofile
        self.todir = todir
        self.overwrite = overwrite
        self.filtering = filtering
        self.file = file
        self.flatten = flatten
        self.includeEmptyDirs = includeEmptyDirs
        self.Ant_Copy = Ant_Copy
        self.Ant_Copy49 = Ant_Copy49
        self.Ant_Copy51 = Ant_Copy51
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def includeEmptyDirs(self):
        return self.__includeEmptyDirs

    @includeEmptyDirs.setter
    def includeEmptyDirs(self, includeEmptyDirs: str):
        self.__includeEmptyDirs = includeEmptyDirs


    @property
    def tofile(self):
        return self.__tofile

    @tofile.setter
    def tofile(self, tofile: str):
        self.__tofile = tofile


    @property
    def overwrite(self):
        return self.__overwrite

    @overwrite.setter
    def overwrite(self, overwrite: str):
        self.__overwrite = overwrite


    @property
    def flatten(self):
        return self.__flatten

    @flatten.setter
    def flatten(self, flatten: str):
        self.__flatten = flatten


    @property
    def todir(self):
        return self.__todir

    @todir.setter
    def todir(self, todir: str):
        self.__todir = todir


    @property
    def presservelastmodified(self):
        return self.__presservelastmodified

    @presservelastmodified.setter
    def presservelastmodified(self, presservelastmodified: str):
        self.__presservelastmodified = presservelastmodified


    @property
    def filtering(self):
        return self.__filtering

    @filtering.setter
    def filtering(self, filtering: str):
        self.__filtering = filtering


    @property
    def Ant_Copy51(self):
        return self.__Ant_Copy51

    @Ant_Copy51.setter
    def Ant_Copy51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Copy__Ant_Copy51", None)
        self.__Ant_Copy51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Mapper"):
                opp_val = getattr(old_value, "Mapper", None)
                if opp_val == self:
                    setattr(old_value, "Mapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Mapper"):
                opp_val = getattr(value, "Mapper", None)
                setattr(value, "Mapper", self)

    @property
    def Ant_Copy(self):
        return self.__Ant_Copy

    @Ant_Copy.setter
    def Ant_Copy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Copy__Ant_Copy", None)
        self.__Ant_Copy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileSet47"):
                opp_val = getattr(old_value, "FileSet47", None)
                if opp_val == self:
                    setattr(old_value, "FileSet47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileSet47"):
                opp_val = getattr(value, "FileSet47", None)
                setattr(value, "FileSet47", self)

    @property
    def Ant_Copy49(self):
        return self.__Ant_Copy49

    @Ant_Copy49.setter
    def Ant_Copy49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Copy__Ant_Copy49", None)
        self.__Ant_Copy49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FilterSet"):
                opp_val = getattr(old_value, "FilterSet", None)
                if opp_val == self:
                    setattr(old_value, "FilterSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FilterSet"):
                opp_val = getattr(value, "FilterSet", None)
                setattr(value, "FilterSet", self)

class Ant_Delete(FileTask):

    def __init__(self, file: str, dir: str, verbose: str, quiet: str, failonerror: str, includeEmptyDirs: str, includes: str, includesfile: str, excludes: str, excludesfile: str, defaultexcludes: str):
        self.file = file
        self.dir = dir
        self.verbose = verbose
        self.quiet = quiet
        self.failonerror = failonerror
        self.includeEmptyDirs = includeEmptyDirs
        self.includes = includes
        self.includesfile = includesfile
        self.excludes = excludes
        self.excludesfile = excludesfile
        self.defaultexcludes = defaultexcludes
        
        pass
    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, includes: str):
        self.__includes = includes


    @property
    def excludesfile(self):
        return self.__excludesfile

    @excludesfile.setter
    def excludesfile(self, excludesfile: str):
        self.__excludesfile = excludesfile


    @property
    def includesfile(self):
        return self.__includesfile

    @includesfile.setter
    def includesfile(self, includesfile: str):
        self.__includesfile = includesfile


    @property
    def defaultexcludes(self):
        return self.__defaultexcludes

    @defaultexcludes.setter
    def defaultexcludes(self, defaultexcludes: str):
        self.__defaultexcludes = defaultexcludes


    @property
    def includeEmptyDirs(self):
        return self.__includeEmptyDirs

    @includeEmptyDirs.setter
    def includeEmptyDirs(self, includeEmptyDirs: str):
        self.__includeEmptyDirs = includeEmptyDirs


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: str):
        self.__verbose = verbose


    @property
    def quiet(self):
        return self.__quiet

    @quiet.setter
    def quiet(self, quiet: str):
        self.__quiet = quiet


    @property
    def failonerror(self):
        return self.__failonerror

    @failonerror.setter
    def failonerror(self, failonerror: str):
        self.__failonerror = failonerror


    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, excludes: str):
        self.__excludes = excludes


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class Ant_Mkdir(FileTask):

    def __init__(self, dir: str):
        self.dir = dir
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


class Ant_FileTask(PreDefinedTask):

    pass
class ArchiveTask:

    pass
class Ant_Jar(ArchiveTask):

    def __init__(self, jarfile: str, basedir: str, compress: str, encoding: str, manifest: str):
        self.jarfile = jarfile
        self.basedir = basedir
        self.compress = compress
        self.encoding = encoding
        self.manifest = manifest
        
        pass
    @property
    def basedir(self):
        return self.__basedir

    @basedir.setter
    def basedir(self, basedir: str):
        self.__basedir = basedir


    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding


    @property
    def manifest(self):
        return self.__manifest

    @manifest.setter
    def manifest(self, manifest: str):
        self.__manifest = manifest


    @property
    def compress(self):
        return self.__compress

    @compress.setter
    def compress(self, compress: str):
        self.__compress = compress


    @property
    def jarfile(self):
        return self.__jarfile

    @jarfile.setter
    def jarfile(self, jarfile: str):
        self.__jarfile = jarfile


class Ant_ArchiveTask(PreDefinedTask):

    pass
class DocumentationTask:

    pass
class Ant_Javadoc(DocumentationTask):

    def __init__(self, sourcepath: str, destdir: str, packagenames: str, defaultexcludes: str, author: str, version: str, use: str, windowtitle: str):
        self.sourcepath = sourcepath
        self.destdir = destdir
        self.packagenames = packagenames
        self.defaultexcludes = defaultexcludes
        self.author = author
        self.version = version
        self.use = use
        self.windowtitle = windowtitle
        
        pass
    @property
    def destdir(self):
        return self.__destdir

    @destdir.setter
    def destdir(self, destdir: str):
        self.__destdir = destdir


    @property
    def windowtitle(self):
        return self.__windowtitle

    @windowtitle.setter
    def windowtitle(self, windowtitle: str):
        self.__windowtitle = windowtitle


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def defaultexcludes(self):
        return self.__defaultexcludes

    @defaultexcludes.setter
    def defaultexcludes(self, defaultexcludes: str):
        self.__defaultexcludes = defaultexcludes


    @property
    def sourcepath(self):
        return self.__sourcepath

    @sourcepath.setter
    def sourcepath(self, sourcepath: str):
        self.__sourcepath = sourcepath


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


    @property
    def packagenames(self):
        return self.__packagenames

    @packagenames.setter
    def packagenames(self, packagenames: str):
        self.__packagenames = packagenames


class Ant_DocumentationTask(PreDefinedTask):

    pass
class Ant_CompileTask(PreDefinedTask):

    pass
class Ant_FormatTstamp:

    def __init__(self, property1: str, pattern: str, offset: str, unit: str, locale: str):
        self.property1 = property1
        self.pattern = pattern
        self.offset = offset
        self.unit = unit
        self.locale = locale
        
        pass
    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


    @property
    def property1(self):
        return self.__property1

    @property1.setter
    def property1(self, property1: str):
        self.__property1 = property1


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


    @property
    def locale(self):
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale


    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class FormatTstamp:

    pass
class MiscellaneousTask:

    pass
class Ant_Tstamp(MiscellaneousTask):

    pass
class Ant_Echo(MiscellaneousTask):

    def __init__(self, message: str, file: str, append: str):
        self.message = message
        self.file = file
        self.append = append
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def append(self):
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append


class Ant_MiscellaneousTask(PreDefinedTask):

    pass
class ClassPath:

    pass