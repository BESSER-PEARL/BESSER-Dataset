from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DocumentationTask:

    pass
class Ant_Javadoc(DocumentationTask):

    def __init__(self, version: str, use: str, windowtitle: str, sourcepath: str, destdir: str, packagenames: str, defaultexcludes: str, author: str):
        self.version = version
        self.use = use
        self.windowtitle = windowtitle
        self.sourcepath = sourcepath
        self.destdir = destdir
        self.packagenames = packagenames
        self.defaultexcludes = defaultexcludes
        self.author = author
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def packagenames(self):
        return self.__packagenames

    @packagenames.setter
    def packagenames(self, packagenames: str):
        self.__packagenames = packagenames


    @property
    def sourcepath(self):
        return self.__sourcepath

    @sourcepath.setter
    def sourcepath(self, sourcepath: str):
        self.__sourcepath = sourcepath


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
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def defaultexcludes(self):
        return self.__defaultexcludes

    @defaultexcludes.setter
    def defaultexcludes(self, defaultexcludes: str):
        self.__defaultexcludes = defaultexcludes


    @property
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


class CompileTask:

    pass
class Ant_Javac(CompileTask):

    def __init__(self, srcdir: str, destdir: str, debug: str, fork: str, optimize: str, deprecation: str, Ant_Javac: set["Ant_InExcludes"] = None, Ant_Javac48: "Ant_ClassPath" = None):
        self.srcdir = srcdir
        self.destdir = destdir
        self.debug = debug
        self.fork = fork
        self.optimize = optimize
        self.deprecation = deprecation
        self.Ant_Javac = Ant_Javac if Ant_Javac is not None else set()
        self.Ant_Javac48 = Ant_Javac48
        
        pass
    @property
    def deprecation(self):
        return self.__deprecation

    @deprecation.setter
    def deprecation(self, deprecation: str):
        self.__deprecation = deprecation


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
                if hasattr(item, "Ant_InExcludes46"):
                    opp_val = getattr(item, "Ant_InExcludes46", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_InExcludes46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_InExcludes46"):
                    opp_val = getattr(item, "Ant_InExcludes46", None)
                    
                    setattr(item, "Ant_InExcludes46", self)
                    

    @property
    def Ant_Javac48(self):
        return self.__Ant_Javac48

    @Ant_Javac48.setter
    def Ant_Javac48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Javac__Ant_Javac48", None)
        self.__Ant_Javac48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_ClassPath49"):
                opp_val = getattr(old_value, "Ant_ClassPath49", None)
                if opp_val == self:
                    setattr(old_value, "Ant_ClassPath49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_ClassPath49"):
                opp_val = getattr(value, "Ant_ClassPath49", None)
                setattr(value, "Ant_ClassPath49", self)

class FileTask:

    pass
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
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: str):
        self.__verbose = verbose


    @property
    def excludesfile(self):
        return self.__excludesfile

    @excludesfile.setter
    def excludesfile(self, excludesfile: str):
        self.__excludesfile = excludesfile


    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, includes: str):
        self.__includes = includes


    @property
    def failonerror(self):
        return self.__failonerror

    @failonerror.setter
    def failonerror(self, failonerror: str):
        self.__failonerror = failonerror


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def includeEmptyDirs(self):
        return self.__includeEmptyDirs

    @includeEmptyDirs.setter
    def includeEmptyDirs(self, includeEmptyDirs: str):
        self.__includeEmptyDirs = includeEmptyDirs


    @property
    def includesfile(self):
        return self.__includesfile

    @includesfile.setter
    def includesfile(self, includesfile: str):
        self.__includesfile = includesfile


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


    @property
    def quiet(self):
        return self.__quiet

    @quiet.setter
    def quiet(self, quiet: str):
        self.__quiet = quiet


    @property
    def defaultexcludes(self):
        return self.__defaultexcludes

    @defaultexcludes.setter
    def defaultexcludes(self, defaultexcludes: str):
        self.__defaultexcludes = defaultexcludes


class Ant_Copy(FileTask):

    def __init__(self, file: str, presservelastmodified: str, tofile: str, todir: str, overwrite: str, filtering: str, flatten: str, includeEmptyDirs: str, Ant_Copy: "Ant_FileSet" = None, Ant_Copy53: "Ant_FilterSet" = None, Ant_Copy56: "Ant_Mapper" = None):
        self.file = file
        self.presservelastmodified = presservelastmodified
        self.tofile = tofile
        self.todir = todir
        self.overwrite = overwrite
        self.filtering = filtering
        self.flatten = flatten
        self.includeEmptyDirs = includeEmptyDirs
        self.Ant_Copy = Ant_Copy
        self.Ant_Copy53 = Ant_Copy53
        self.Ant_Copy56 = Ant_Copy56
        
        pass
    @property
    def presservelastmodified(self):
        return self.__presservelastmodified

    @presservelastmodified.setter
    def presservelastmodified(self, presservelastmodified: str):
        self.__presservelastmodified = presservelastmodified


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
    def filtering(self):
        return self.__filtering

    @filtering.setter
    def filtering(self, filtering: str):
        self.__filtering = filtering


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
    def tofile(self):
        return self.__tofile

    @tofile.setter
    def tofile(self, tofile: str):
        self.__tofile = tofile


    @property
    def todir(self):
        return self.__todir

    @todir.setter
    def todir(self, todir: str):
        self.__todir = todir


    @property
    def Ant_Copy53(self):
        return self.__Ant_Copy53

    @Ant_Copy53.setter
    def Ant_Copy53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Copy__Ant_Copy53", None)
        self.__Ant_Copy53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_FilterSet54"):
                opp_val = getattr(old_value, "Ant_FilterSet54", None)
                if opp_val == self:
                    setattr(old_value, "Ant_FilterSet54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_FilterSet54"):
                opp_val = getattr(value, "Ant_FilterSet54", None)
                setattr(value, "Ant_FilterSet54", self)

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
            if hasattr(old_value, "Ant_FileSet51"):
                opp_val = getattr(old_value, "Ant_FileSet51", None)
                if opp_val == self:
                    setattr(old_value, "Ant_FileSet51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_FileSet51"):
                opp_val = getattr(value, "Ant_FileSet51", None)
                setattr(value, "Ant_FileSet51", self)

    @property
    def Ant_Copy56(self):
        return self.__Ant_Copy56

    @Ant_Copy56.setter
    def Ant_Copy56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Copy__Ant_Copy56", None)
        self.__Ant_Copy56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Mapper"):
                opp_val = getattr(old_value, "Ant_Mapper", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Mapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Mapper"):
                opp_val = getattr(value, "Ant_Mapper", None)
                setattr(value, "Ant_Mapper", self)

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
    def jarfile(self):
        return self.__jarfile

    @jarfile.setter
    def jarfile(self, jarfile: str):
        self.__jarfile = jarfile


    @property
    def manifest(self):
        return self.__manifest

    @manifest.setter
    def manifest(self, manifest: str):
        self.__manifest = manifest


    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding


    @property
    def compress(self):
        return self.__compress

    @compress.setter
    def compress(self, compress: str):
        self.__compress = compress


class ExecutionTask:

    pass
class Ant_Exec(ExecutionTask):

    def __init__(self, executable: str, dir: str):
        self.executable = executable
        self.dir = dir
        
        pass
    @property
    def executable(self):
        return self.__executable

    @executable.setter
    def executable(self, executable: str):
        self.__executable = executable


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


class Ant_Java(ExecutionTask):

    def __init__(self, fork: str, classname: str, jar: str, Ant_Java: "Ant_ClassPath" = None):
        self.fork = fork
        self.classname = classname
        self.jar = jar
        self.Ant_Java = Ant_Java
        
        pass
    @property
    def jar(self):
        return self.__jar

    @jar.setter
    def jar(self, jar: str):
        self.__jar = jar


    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


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
            if hasattr(old_value, "Ant_ClassPath43"):
                opp_val = getattr(old_value, "Ant_ClassPath43", None)
                if opp_val == self:
                    setattr(old_value, "Ant_ClassPath43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_ClassPath43"):
                opp_val = getattr(value, "Ant_ClassPath43", None)
                setattr(value, "Ant_ClassPath43", self)

class Ant_Attribut:

    def __init__(self, name: str, value: str, Ant_Attribut: "Ant_NewTask" = None):
        self.name = name
        self.value = value
        self.Ant_Attribut = Ant_Attribut
        
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
    def Ant_Attribut(self):
        return self.__Ant_Attribut

    @Ant_Attribut.setter
    def Ant_Attribut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Attribut__Ant_Attribut", None)
        self.__Ant_Attribut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_NewTask41"):
                opp_val = getattr(old_value, "Ant_NewTask41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_NewTask41"):
                opp_val = getattr(value, "Ant_NewTask41", None)
                if opp_val is None:
                    setattr(value, "Ant_NewTask41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Task:

    pass
class Ant_PreDefinedTask(Task):

    def __init__(self, id: str, taskname: str, description: str):
        self.id = id
        self.taskname = taskname
        self.description = description
        
        pass
    @property
    def taskname(self):
        return self.__taskname

    @taskname.setter
    def taskname(self, taskname: str):
        self.__taskname = taskname


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


class Ant_NewTask(Task):

    pass
class Ant_FormatTstamp:

    def __init__(self, property1: str, pattern: str, offset: str, unit: str, locale: str, Ant_FormatTstamp: "Ant_Tstamp" = None):
        self.property1 = property1
        self.pattern = pattern
        self.offset = offset
        self.unit = unit
        self.locale = locale
        self.Ant_FormatTstamp = Ant_FormatTstamp
        
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
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


    @property
    def locale(self):
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


    @property
    def Ant_FormatTstamp(self):
        return self.__Ant_FormatTstamp

    @Ant_FormatTstamp.setter
    def Ant_FormatTstamp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FormatTstamp__Ant_FormatTstamp", None)
        self.__Ant_FormatTstamp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Tstamp"):
                opp_val = getattr(old_value, "Ant_Tstamp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Tstamp"):
                opp_val = getattr(value, "Ant_Tstamp", None)
                if opp_val is None:
                    setattr(value, "Ant_Tstamp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def append(self):
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append


class PreDefinedTask:

    pass
class Ant_ArchiveTask(PreDefinedTask):

    pass
class Ant_DocumentationTask(PreDefinedTask):

    pass
class Ant_FileTask(PreDefinedTask):

    pass
class Ant_CompileTask(PreDefinedTask):

    pass
class Ant_ExecutionTask(PreDefinedTask):

    pass
class Ant_MiscellaneousTask(PreDefinedTask):

    pass
class Set:

    pass
class Ant_FilterSet(Set):

    def __init__(self, starttoken: str, endtoken: str, Ant_FilterSet: set["Ant_Filter"] = None, Ant_FilterSet23: set["Ant_FiltersFile"] = None, Ant_FilterSet54: "Ant_Copy" = None):
        self.starttoken = starttoken
        self.endtoken = endtoken
        self.Ant_FilterSet = Ant_FilterSet if Ant_FilterSet is not None else set()
        self.Ant_FilterSet23 = Ant_FilterSet23 if Ant_FilterSet23 is not None else set()
        self.Ant_FilterSet54 = Ant_FilterSet54
        
        pass
    @property
    def starttoken(self):
        return self.__starttoken

    @starttoken.setter
    def starttoken(self, starttoken: str):
        self.__starttoken = starttoken


    @property
    def endtoken(self):
        return self.__endtoken

    @endtoken.setter
    def endtoken(self, endtoken: str):
        self.__endtoken = endtoken


    @property
    def Ant_FilterSet54(self):
        return self.__Ant_FilterSet54

    @Ant_FilterSet54.setter
    def Ant_FilterSet54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FilterSet__Ant_FilterSet54", None)
        self.__Ant_FilterSet54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Copy53"):
                opp_val = getattr(old_value, "Ant_Copy53", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Copy53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Copy53"):
                opp_val = getattr(value, "Ant_Copy53", None)
                setattr(value, "Ant_Copy53", self)

    @property
    def Ant_FilterSet23(self):
        return self.__Ant_FilterSet23

    @Ant_FilterSet23.setter
    def Ant_FilterSet23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FilterSet__Ant_FilterSet23", None)
        self.__Ant_FilterSet23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_FiltersFile"):
                    opp_val = getattr(item, "Ant_FiltersFile", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_FiltersFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_FiltersFile"):
                    opp_val = getattr(item, "Ant_FiltersFile", None)
                    
                    setattr(item, "Ant_FiltersFile", self)
                    

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
                if hasattr(item, "Ant_Filter"):
                    opp_val = getattr(item, "Ant_Filter", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Filter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Filter"):
                    opp_val = getattr(item, "Ant_Filter", None)
                    
                    setattr(item, "Ant_Filter", self)
                    

class Ant_FileSet(Set):

    def __init__(self, dir: str, Ant_FileSet31: "Ant_Path" = None, Ant_FileSet: set["Ant_PatternSet"] = None, Ant_FileSet18: set["Ant_Includes"] = None, Ant_FileSet20: set["Ant_Excludes"] = None, Ant_FileSet36: "Ant_ClassPath" = None, Ant_FileSet51: "Ant_Copy" = None):
        self.dir = dir
        self.Ant_FileSet31 = Ant_FileSet31
        self.Ant_FileSet = Ant_FileSet if Ant_FileSet is not None else set()
        self.Ant_FileSet18 = Ant_FileSet18 if Ant_FileSet18 is not None else set()
        self.Ant_FileSet20 = Ant_FileSet20 if Ant_FileSet20 is not None else set()
        self.Ant_FileSet36 = Ant_FileSet36
        self.Ant_FileSet51 = Ant_FileSet51
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def Ant_FileSet31(self):
        return self.__Ant_FileSet31

    @Ant_FileSet31.setter
    def Ant_FileSet31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet31", None)
        self.__Ant_FileSet31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Path30"):
                opp_val = getattr(old_value, "Ant_Path30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Path30"):
                opp_val = getattr(value, "Ant_Path30", None)
                if opp_val is None:
                    setattr(value, "Ant_Path30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Ant_Includes"):
                    opp_val = getattr(item, "Ant_Includes", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Includes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Includes"):
                    opp_val = getattr(item, "Ant_Includes", None)
                    
                    setattr(item, "Ant_Includes", self)
                    

    @property
    def Ant_FileSet51(self):
        return self.__Ant_FileSet51

    @Ant_FileSet51.setter
    def Ant_FileSet51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet51", None)
        self.__Ant_FileSet51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Copy"):
                opp_val = getattr(old_value, "Ant_Copy", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Copy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Copy"):
                opp_val = getattr(value, "Ant_Copy", None)
                setattr(value, "Ant_Copy", self)

    @property
    def Ant_FileSet36(self):
        return self.__Ant_FileSet36

    @Ant_FileSet36.setter
    def Ant_FileSet36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet36", None)
        self.__Ant_FileSet36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_ClassPath35"):
                opp_val = getattr(old_value, "Ant_ClassPath35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_ClassPath35"):
                opp_val = getattr(value, "Ant_ClassPath35", None)
                if opp_val is None:
                    setattr(value, "Ant_ClassPath35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "Ant_PatternSet16"):
                    opp_val = getattr(item, "Ant_PatternSet16", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_PatternSet16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_PatternSet16"):
                    opp_val = getattr(item, "Ant_PatternSet16", None)
                    
                    setattr(item, "Ant_PatternSet16", self)
                    

    @property
    def Ant_FileSet20(self):
        return self.__Ant_FileSet20

    @Ant_FileSet20.setter
    def Ant_FileSet20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FileSet__Ant_FileSet20", None)
        self.__Ant_FileSet20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_Excludes"):
                    opp_val = getattr(item, "Ant_Excludes", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Excludes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Excludes"):
                    opp_val = getattr(item, "Ant_Excludes", None)
                    
                    setattr(item, "Ant_Excludes", self)
                    

class Ant_PatternSet(Set):

    pass
class Ant_ClassPath(Set):

    def __init__(self, refid: str, Ant_ClassPath: set["Ant_PathElement"] = None, Ant_ClassPath43: "Ant_Java" = None, Ant_ClassPath35: set["Ant_FileSet"] = None, Ant_ClassPath49: "Ant_Javac" = None):
        self.refid = refid
        self.Ant_ClassPath = Ant_ClassPath if Ant_ClassPath is not None else set()
        self.Ant_ClassPath43 = Ant_ClassPath43
        self.Ant_ClassPath35 = Ant_ClassPath35 if Ant_ClassPath35 is not None else set()
        self.Ant_ClassPath49 = Ant_ClassPath49
        
        pass
    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def Ant_ClassPath43(self):
        return self.__Ant_ClassPath43

    @Ant_ClassPath43.setter
    def Ant_ClassPath43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_ClassPath__Ant_ClassPath43", None)
        self.__Ant_ClassPath43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Java"):
                opp_val = getattr(old_value, "Ant_Java", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Java", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Java"):
                opp_val = getattr(value, "Ant_Java", None)
                setattr(value, "Ant_Java", self)

    @property
    def Ant_ClassPath35(self):
        return self.__Ant_ClassPath35

    @Ant_ClassPath35.setter
    def Ant_ClassPath35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_ClassPath__Ant_ClassPath35", None)
        self.__Ant_ClassPath35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_FileSet36"):
                    opp_val = getattr(item, "Ant_FileSet36", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_FileSet36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_FileSet36"):
                    opp_val = getattr(item, "Ant_FileSet36", None)
                    
                    setattr(item, "Ant_FileSet36", self)
                    

    @property
    def Ant_ClassPath49(self):
        return self.__Ant_ClassPath49

    @Ant_ClassPath49.setter
    def Ant_ClassPath49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_ClassPath__Ant_ClassPath49", None)
        self.__Ant_ClassPath49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Javac48"):
                opp_val = getattr(old_value, "Ant_Javac48", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Javac48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Javac48"):
                opp_val = getattr(value, "Ant_Javac48", None)
                setattr(value, "Ant_Javac48", self)

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
                if hasattr(item, "Ant_PathElement33"):
                    opp_val = getattr(item, "Ant_PathElement33", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_PathElement33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_PathElement33"):
                    opp_val = getattr(item, "Ant_PathElement33", None)
                    
                    setattr(item, "Ant_PathElement33", self)
                    

class Basic:

    pass
class Ant_InExcludes(Basic):

    def __init__(self, name: str, ifCondition: str, unless: str, Ant_InExcludes: "Ant_PatternSet" = None, Ant_InExcludes46: "Ant_Javac" = None):
        self.name = name
        self.ifCondition = ifCondition
        self.unless = unless
        self.Ant_InExcludes = Ant_InExcludes
        self.Ant_InExcludes46 = Ant_InExcludes46
        
        pass
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


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Ant_InExcludes46(self):
        return self.__Ant_InExcludes46

    @Ant_InExcludes46.setter
    def Ant_InExcludes46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_InExcludes__Ant_InExcludes46", None)
        self.__Ant_InExcludes46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Javac"):
                opp_val = getattr(old_value, "Ant_Javac", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Javac"):
                opp_val = getattr(value, "Ant_Javac", None)
                if opp_val is None:
                    setattr(value, "Ant_Javac", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ant_InExcludes(self):
        return self.__Ant_InExcludes

    @Ant_InExcludes.setter
    def Ant_InExcludes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_InExcludes__Ant_InExcludes", None)
        self.__Ant_InExcludes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_PatternSet"):
                opp_val = getattr(old_value, "Ant_PatternSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_PatternSet"):
                opp_val = getattr(value, "Ant_PatternSet", None)
                if opp_val is None:
                    setattr(value, "Ant_PatternSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Ant_Mapper(Basic):

    def __init__(self, type: str, classname: str, classpath: str, classpathref: str, from_: str, to: str, Ant_Mapper: "Ant_Copy" = None):
        self.type = type
        self.classname = classname
        self.classpath = classpath
        self.classpathref = classpathref
        self.from_ = from_
        self.to = to
        self.Ant_Mapper = Ant_Mapper
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def classpath(self):
        return self.__classpath

    @classpath.setter
    def classpath(self, classpath: str):
        self.__classpath = classpath


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
    def classpathref(self):
        return self.__classpathref

    @classpathref.setter
    def classpathref(self, classpathref: str):
        self.__classpathref = classpathref


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def Ant_Mapper(self):
        return self.__Ant_Mapper

    @Ant_Mapper.setter
    def Ant_Mapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Mapper__Ant_Mapper", None)
        self.__Ant_Mapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Copy56"):
                opp_val = getattr(old_value, "Ant_Copy56", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Copy56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Copy56"):
                opp_val = getattr(value, "Ant_Copy56", None)
                setattr(value, "Ant_Copy56", self)

class Pattern:

    pass
class Ant_Set(Pattern):

    pass
class Ant_Basic(Pattern):

    pass
class Ant_Pattern(ABC):

    pass
class Ant_Task(ABC):

    pass
class Ant_PathElement(Basic):

    def __init__(self, path: str, location: str, Ant_PathElement: "Ant_Path" = None, Ant_PathElement33: "Ant_ClassPath" = None):
        self.path = path
        self.location = location
        self.Ant_PathElement = Ant_PathElement
        self.Ant_PathElement33 = Ant_PathElement33
        
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


    @property
    def Ant_PathElement(self):
        return self.__Ant_PathElement

    @Ant_PathElement.setter
    def Ant_PathElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_PathElement__Ant_PathElement", None)
        self.__Ant_PathElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Path28"):
                opp_val = getattr(old_value, "Ant_Path28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Path28"):
                opp_val = getattr(value, "Ant_Path28", None)
                if opp_val is None:
                    setattr(value, "Ant_Path28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ant_PathElement33(self):
        return self.__Ant_PathElement33

    @Ant_PathElement33.setter
    def Ant_PathElement33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_PathElement__Ant_PathElement33", None)
        self.__Ant_PathElement33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_ClassPath"):
                opp_val = getattr(old_value, "Ant_ClassPath", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_ClassPath"):
                opp_val = getattr(value, "Ant_ClassPath", None)
                if opp_val is None:
                    setattr(value, "Ant_ClassPath", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Ant_FiltersFile(Basic):

    def __init__(self, file: str, Ant_FiltersFile: "Ant_FilterSet" = None):
        self.file = file
        self.Ant_FiltersFile = Ant_FiltersFile
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def Ant_FiltersFile(self):
        return self.__Ant_FiltersFile

    @Ant_FiltersFile.setter
    def Ant_FiltersFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_FiltersFile__Ant_FiltersFile", None)
        self.__Ant_FiltersFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_FilterSet23"):
                opp_val = getattr(old_value, "Ant_FilterSet23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_FilterSet23"):
                opp_val = getattr(value, "Ant_FilterSet23", None)
                if opp_val is None:
                    setattr(value, "Ant_FilterSet23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Ant_Filter(Basic):

    def __init__(self, token: str, value: str, Ant_Filter: "Ant_FilterSet" = None):
        self.token = token
        self.value = value
        self.Ant_Filter = Ant_Filter
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token


    @property
    def Ant_Filter(self):
        return self.__Ant_Filter

    @Ant_Filter.setter
    def Ant_Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Filter__Ant_Filter", None)
        self.__Ant_Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_FilterSet"):
                opp_val = getattr(old_value, "Ant_FilterSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_FilterSet"):
                opp_val = getattr(value, "Ant_FilterSet", None)
                if opp_val is None:
                    setattr(value, "Ant_FilterSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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


class InExcludes:

    pass
class Ant_IncludesFile(InExcludes):

    pass
class Ant_Includes(InExcludes):

    pass
class Ant_Excludes(InExcludes):

    pass
class Ant_ExcludesFile(InExcludes):

    pass
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


class Property:

    pass
class Ant_PropertyFile(Property):

    def __init__(self, file: str):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class Ant_PropertyEnv(Property):

    def __init__(self, environment: str):
        self.environment = environment
        
        pass
    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment


class Ant_PropertyName(Property):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Ant_TaskDef:

    def __init__(self, name: str, classname: str, Ant_TaskDef: "Ant_Project" = None, Ant_TaskDef39: "Ant_NewTask" = None):
        self.name = name
        self.classname = classname
        self.Ant_TaskDef = Ant_TaskDef
        self.Ant_TaskDef39 = Ant_TaskDef39
        
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


    @property
    def Ant_TaskDef39(self):
        return self.__Ant_TaskDef39

    @Ant_TaskDef39.setter
    def Ant_TaskDef39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_TaskDef__Ant_TaskDef39", None)
        self.__Ant_TaskDef39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_NewTask"):
                opp_val = getattr(old_value, "Ant_NewTask", None)
                if opp_val == self:
                    setattr(old_value, "Ant_NewTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_NewTask"):
                opp_val = getattr(value, "Ant_NewTask", None)
                setattr(value, "Ant_NewTask", self)

    @property
    def Ant_TaskDef(self):
        return self.__Ant_TaskDef

    @Ant_TaskDef.setter
    def Ant_TaskDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_TaskDef__Ant_TaskDef", None)
        self.__Ant_TaskDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Project6"):
                opp_val = getattr(old_value, "Ant_Project6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Project6"):
                opp_val = getattr(value, "Ant_Project6", None)
                if opp_val is None:
                    setattr(value, "Ant_Project6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Ant_Property(ABC):

    pass
class Ant_Path(Set):

    def __init__(self, id: str, refid: str, Ant_Path: "Ant_Project" = None, Ant_Path26: "Ant_Path" = None, Ant_Path24: "Ant_Path" = None, Ant_Path28: set["Ant_PathElement"] = None, Ant_Path30: set["Ant_FileSet"] = None):
        self.id = id
        self.refid = refid
        self.Ant_Path = Ant_Path
        self.Ant_Path26 = Ant_Path26
        self.Ant_Path24 = Ant_Path24
        self.Ant_Path28 = Ant_Path28 if Ant_Path28 is not None else set()
        self.Ant_Path30 = Ant_Path30 if Ant_Path30 is not None else set()
        
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
    def Ant_Path30(self):
        return self.__Ant_Path30

    @Ant_Path30.setter
    def Ant_Path30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path30", None)
        self.__Ant_Path30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_FileSet31"):
                    opp_val = getattr(item, "Ant_FileSet31", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_FileSet31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_FileSet31"):
                    opp_val = getattr(item, "Ant_FileSet31", None)
                    
                    setattr(item, "Ant_FileSet31", self)
                    

    @property
    def Ant_Path28(self):
        return self.__Ant_Path28

    @Ant_Path28.setter
    def Ant_Path28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path28", None)
        self.__Ant_Path28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_PathElement"):
                    opp_val = getattr(item, "Ant_PathElement", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_PathElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_PathElement"):
                    opp_val = getattr(item, "Ant_PathElement", None)
                    
                    setattr(item, "Ant_PathElement", self)
                    

    @property
    def Ant_Path26(self):
        return self.__Ant_Path26

    @Ant_Path26.setter
    def Ant_Path26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path26", None)
        self.__Ant_Path26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Path24"):
                opp_val = getattr(old_value, "Ant_Path24", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Path24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Path24"):
                opp_val = getattr(value, "Ant_Path24", None)
                setattr(value, "Ant_Path24", self)

    @property
    def Ant_Path24(self):
        return self.__Ant_Path24

    @Ant_Path24.setter
    def Ant_Path24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Path__Ant_Path24", None)
        self.__Ant_Path24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Path26"):
                opp_val = getattr(old_value, "Ant_Path26", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Path26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Path26"):
                opp_val = getattr(value, "Ant_Path26", None)
                setattr(value, "Ant_Path26", self)

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
            if hasattr(old_value, "Ant_Project2"):
                opp_val = getattr(old_value, "Ant_Project2", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Project2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Project2"):
                opp_val = getattr(value, "Ant_Project2", None)
                setattr(value, "Ant_Project2", self)

class Ant_Target:

    def __init__(self, name: str, description: str, unless: str, ifCondition: str, Ant_Target9: "Ant_Project" = None, Ant_Target: "Ant_Project" = None, Ant_Target12: "Ant_Target" = None, Ant_Target10: set["Ant_Target"] = None, target: set["Ant_Task"] = None, Target: "Ant_Task" = None):
        self.name = name
        self.description = description
        self.unless = unless
        self.ifCondition = ifCondition
        self.Ant_Target9 = Ant_Target9
        self.Ant_Target = Ant_Target
        self.Ant_Target12 = Ant_Target12
        self.Ant_Target10 = Ant_Target10 if Ant_Target10 is not None else set()
        self.target = target if target is not None else set()
        self.Target = Target
        
        pass
    @property
    def ifCondition(self):
        return self.__ifCondition

    @ifCondition.setter
    def ifCondition(self, ifCondition: str):
        self.__ifCondition = ifCondition


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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
    def Target(self):
        return self.__Target

    @Target.setter
    def Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Target", None)
        self.__Target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks"):
                opp_val = getattr(old_value, "tasks", None)
                if opp_val == self:
                    setattr(old_value, "tasks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks"):
                opp_val = getattr(value, "tasks", None)
                setattr(value, "tasks", self)

    @property
    def Ant_Target9(self):
        return self.__Ant_Target9

    @Ant_Target9.setter
    def Ant_Target9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Ant_Target9", None)
        self.__Ant_Target9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Project8"):
                opp_val = getattr(old_value, "Ant_Project8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Project8"):
                opp_val = getattr(value, "Ant_Project8", None)
                if opp_val is None:
                    setattr(value, "Ant_Project8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ant_Target(self):
        return self.__Ant_Target

    @Ant_Target.setter
    def Ant_Target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Ant_Target", None)
        self.__Ant_Target = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Project"):
                opp_val = getattr(old_value, "Ant_Project", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Project"):
                opp_val = getattr(value, "Ant_Project", None)
                setattr(value, "Ant_Project", self)

    @property
    def Ant_Target12(self):
        return self.__Ant_Target12

    @Ant_Target12.setter
    def Ant_Target12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Ant_Target12", None)
        self.__Ant_Target12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ant_Target10"):
                opp_val = getattr(old_value, "Ant_Target10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Target10"):
                opp_val = getattr(value, "Ant_Target10", None)
                if opp_val is None:
                    setattr(value, "Ant_Target10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Ant_Target10(self):
        return self.__Ant_Target10

    @Ant_Target10.setter
    def Ant_Target10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ant_Target__Ant_Target10", None)
        self.__Ant_Target10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ant_Target12"):
                    opp_val = getattr(item, "Ant_Target12", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Target12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Target12"):
                    opp_val = getattr(item, "Ant_Target12", None)
                    
                    setattr(item, "Ant_Target12", self)
                    

class Ant_Project:

    def __init__(self, name: str, basedir: str, description: str, Ant_Project8: set["Ant_Target"] = None, Ant_Project: "Ant_Target" = None, Ant_Project2: "Ant_Path" = None, Ant_Project4: set["Ant_Property"] = None, Ant_Project6: set["Ant_TaskDef"] = None):
        self.name = name
        self.basedir = basedir
        self.description = description
        self.Ant_Project8 = Ant_Project8 if Ant_Project8 is not None else set()
        self.Ant_Project = Ant_Project
        self.Ant_Project2 = Ant_Project2
        self.Ant_Project4 = Ant_Project4 if Ant_Project4 is not None else set()
        self.Ant_Project6 = Ant_Project6 if Ant_Project6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def basedir(self):
        return self.__basedir

    @basedir.setter
    def basedir(self, basedir: str):
        self.__basedir = basedir


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


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
            if hasattr(old_value, "Ant_Path"):
                opp_val = getattr(old_value, "Ant_Path", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Path", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Path"):
                opp_val = getattr(value, "Ant_Path", None)
                setattr(value, "Ant_Path", self)

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
                if hasattr(item, "Ant_Property"):
                    opp_val = getattr(item, "Ant_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Property"):
                    opp_val = getattr(item, "Ant_Property", None)
                    
                    setattr(item, "Ant_Property", self)
                    

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
            if hasattr(old_value, "Ant_Target"):
                opp_val = getattr(old_value, "Ant_Target", None)
                if opp_val == self:
                    setattr(old_value, "Ant_Target", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ant_Target"):
                opp_val = getattr(value, "Ant_Target", None)
                setattr(value, "Ant_Target", self)

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
                if hasattr(item, "Ant_TaskDef"):
                    opp_val = getattr(item, "Ant_TaskDef", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_TaskDef", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_TaskDef"):
                    opp_val = getattr(item, "Ant_TaskDef", None)
                    
                    setattr(item, "Ant_TaskDef", self)
                    

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
                if hasattr(item, "Ant_Target9"):
                    opp_val = getattr(item, "Ant_Target9", None)
                    
                    if opp_val == self:
                        setattr(item, "Ant_Target9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ant_Target9"):
                    opp_val = getattr(item, "Ant_Target9", None)
                    
                    setattr(item, "Ant_Target9", self)
                    
