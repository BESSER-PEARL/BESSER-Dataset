from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FileTask:

    pass
class MavenMaven_Copy(FileTask):

    def __init__(self, overwrite: str, filtering: str, flatten: str, includeEmptyDirs: str, file: str, presservelastmodified: str, tofile: str, todir: str, MavenMaven_Copy: "FileSet" = None, MavenMaven_Copy60: "FilterSet" = None, MavenMaven_Copy62: "Mapper" = None):
        self.overwrite = overwrite
        self.filtering = filtering
        self.flatten = flatten
        self.includeEmptyDirs = includeEmptyDirs
        self.file = file
        self.presservelastmodified = presservelastmodified
        self.tofile = tofile
        self.todir = todir
        self.MavenMaven_Copy = MavenMaven_Copy
        self.MavenMaven_Copy60 = MavenMaven_Copy60
        self.MavenMaven_Copy62 = MavenMaven_Copy62
        
        pass
    @property
    def tofile(self):
        return self.__tofile

    @tofile.setter
    def tofile(self, tofile: str):
        self.__tofile = tofile


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


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
    def filtering(self):
        return self.__filtering

    @filtering.setter
    def filtering(self, filtering: str):
        self.__filtering = filtering


    @property
    def includeEmptyDirs(self):
        return self.__includeEmptyDirs

    @includeEmptyDirs.setter
    def includeEmptyDirs(self, includeEmptyDirs: str):
        self.__includeEmptyDirs = includeEmptyDirs


    @property
    def MavenMaven_Copy62(self):
        return self.__MavenMaven_Copy62

    @MavenMaven_Copy62.setter
    def MavenMaven_Copy62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Copy__MavenMaven_Copy62", None)
        self.__MavenMaven_Copy62 = value
        
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
    def MavenMaven_Copy(self):
        return self.__MavenMaven_Copy

    @MavenMaven_Copy.setter
    def MavenMaven_Copy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Copy__MavenMaven_Copy", None)
        self.__MavenMaven_Copy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FileSet58"):
                opp_val = getattr(old_value, "FileSet58", None)
                if opp_val == self:
                    setattr(old_value, "FileSet58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FileSet58"):
                opp_val = getattr(value, "FileSet58", None)
                setattr(value, "FileSet58", self)

    @property
    def MavenMaven_Copy60(self):
        return self.__MavenMaven_Copy60

    @MavenMaven_Copy60.setter
    def MavenMaven_Copy60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Copy__MavenMaven_Copy60", None)
        self.__MavenMaven_Copy60 = value
        
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

class MavenMaven_Mkdir(FileTask):

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
class MavenMaven_Jar(ArchiveTask):

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


class MavenMaven_Delete(FileTask):

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
    def failonerror(self):
        return self.__failonerror

    @failonerror.setter
    def failonerror(self, failonerror: str):
        self.__failonerror = failonerror


    @property
    def includesfile(self):
        return self.__includesfile

    @includesfile.setter
    def includesfile(self, includesfile: str):
        self.__includesfile = includesfile


    @property
    def quiet(self):
        return self.__quiet

    @quiet.setter
    def quiet(self, quiet: str):
        self.__quiet = quiet


    @property
    def excludes(self):
        return self.__excludes

    @excludes.setter
    def excludes(self, excludes: str):
        self.__excludes = excludes


    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: str):
        self.__verbose = verbose


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


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


class Mapper:

    pass
class FilterSet:

    pass
class CompileTask:

    pass
class MavenMaven_Javac(CompileTask):

    def __init__(self, optimize: str, deprecation: str, srcdir: str, destdir: str, debug: str, fork: str, MavenMaven_Javac: set["InExcludes"] = None, MavenMaven_Javac55: "ClassPath" = None):
        self.optimize = optimize
        self.deprecation = deprecation
        self.srcdir = srcdir
        self.destdir = destdir
        self.debug = debug
        self.fork = fork
        self.MavenMaven_Javac = MavenMaven_Javac if MavenMaven_Javac is not None else set()
        self.MavenMaven_Javac55 = MavenMaven_Javac55
        
        pass
    @property
    def destdir(self):
        return self.__destdir

    @destdir.setter
    def destdir(self, destdir: str):
        self.__destdir = destdir


    @property
    def deprecation(self):
        return self.__deprecation

    @deprecation.setter
    def deprecation(self, deprecation: str):
        self.__deprecation = deprecation


    @property
    def optimize(self):
        return self.__optimize

    @optimize.setter
    def optimize(self, optimize: str):
        self.__optimize = optimize


    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


    @property
    def srcdir(self):
        return self.__srcdir

    @srcdir.setter
    def srcdir(self, srcdir: str):
        self.__srcdir = srcdir


    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, debug: str):
        self.__debug = debug


    @property
    def MavenMaven_Javac(self):
        return self.__MavenMaven_Javac

    @MavenMaven_Javac.setter
    def MavenMaven_Javac(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Javac__MavenMaven_Javac", None)
        self.__MavenMaven_Javac = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "InExcludes53"):
                    opp_val = getattr(item, "InExcludes53", None)
                    
                    if opp_val == self:
                        setattr(item, "InExcludes53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "InExcludes53"):
                    opp_val = getattr(item, "InExcludes53", None)
                    
                    setattr(item, "InExcludes53", self)
                    

    @property
    def MavenMaven_Javac55(self):
        return self.__MavenMaven_Javac55

    @MavenMaven_Javac55.setter
    def MavenMaven_Javac55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Javac__MavenMaven_Javac55", None)
        self.__MavenMaven_Javac55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ClassPath56"):
                opp_val = getattr(old_value, "ClassPath56", None)
                if opp_val == self:
                    setattr(old_value, "ClassPath56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ClassPath56"):
                opp_val = getattr(value, "ClassPath56", None)
                setattr(value, "ClassPath56", self)

class MavenMaven_FormatTstamp:

    def __init__(self, property: str, pattern: str, offset: str, unit: str, locale: str):
        self.property1 = property1
        self.pattern = pattern
        self.offset = offset
        self.unit = unit
        self.locale = locale
        
        pass
    @property
    def property1(self):
        return self.__property1

    @property1.setter
    def property1(self, property1: str):
        self.__property1 = property1


    @property
    def pattern(self):
        return self.__pattern

    @pattern.setter
    def pattern(self, pattern: str):
        self.__pattern = pattern


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
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit


class FormatTstamp:

    pass
class MiscellaneousTask:

    pass
class MavenMaven_Tstamp(MiscellaneousTask):

    pass
class MavenMaven_Echo(MiscellaneousTask):

    def __init__(self, message: str, file: str, append: str):
        self.message = message
        self.file = file
        self.append = append
        
        pass
    @property
    def append(self):
        return self.__append

    @append.setter
    def append(self, append: str):
        self.__append = append


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


class DocumentationTask:

    pass
class MavenMaven_Javadoc(DocumentationTask):

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


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


class MavenMaven_Attribut:

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


class Attribut:

    pass
class Task:

    pass
class MavenMaven_PreDefinedTask(Task):

    def __init__(self, description: str, id: str, taskname: str):
        self.description = description
        self.id = id
        self.taskname = taskname
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def taskname(self):
        return self.__taskname

    @taskname.setter
    def taskname(self, taskname: str):
        self.__taskname = taskname


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class MavenMaven_NewTask(Task):

    pass
class ClassPath:

    pass
class ExecutionTask:

    pass
class MavenMaven_Java(ExecutionTask):

    def __init__(self, classname: str, jar: str, fork: str, MavenMaven_Java: "ClassPath" = None):
        self.classname = classname
        self.jar = jar
        self.fork = fork
        self.MavenMaven_Java = MavenMaven_Java
        
        pass
    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


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
    def MavenMaven_Java(self):
        return self.__MavenMaven_Java

    @MavenMaven_Java.setter
    def MavenMaven_Java(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Java__MavenMaven_Java", None)
        self.__MavenMaven_Java = value
        
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

class MavenMaven_Exec(ExecutionTask):

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


class PreDefinedTask:

    pass
class MavenMaven_ArchiveTask(PreDefinedTask):

    pass
class MavenMaven_FileTask(PreDefinedTask):

    pass
class MavenMaven_MiscellaneousTask(PreDefinedTask):

    pass
class MavenMaven_DocumentationTask(PreDefinedTask):

    pass
class MavenMaven_CompileTask(PreDefinedTask):

    pass
class MavenMaven_ExecutionTask(PreDefinedTask):

    pass
class FiltersFile:

    pass
class Filter:

    pass
class Excludes:

    pass
class Includes:

    pass
class PatternSet:

    pass
class Set:

    pass
class MavenMaven_ClassPath(Set):

    def __init__(self, refid: str, MavenMaven_ClassPath: set["PathElement"] = None, MavenMaven_ClassPath44: set["FileSet"] = None):
        self.refid = refid
        self.MavenMaven_ClassPath = MavenMaven_ClassPath if MavenMaven_ClassPath is not None else set()
        self.MavenMaven_ClassPath44 = MavenMaven_ClassPath44 if MavenMaven_ClassPath44 is not None else set()
        
        pass
    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def MavenMaven_ClassPath(self):
        return self.__MavenMaven_ClassPath

    @MavenMaven_ClassPath.setter
    def MavenMaven_ClassPath(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_ClassPath__MavenMaven_ClassPath", None)
        self.__MavenMaven_ClassPath = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PathElement42"):
                    opp_val = getattr(item, "PathElement42", None)
                    
                    if opp_val == self:
                        setattr(item, "PathElement42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PathElement42"):
                    opp_val = getattr(item, "PathElement42", None)
                    
                    setattr(item, "PathElement42", self)
                    

    @property
    def MavenMaven_ClassPath44(self):
        return self.__MavenMaven_ClassPath44

    @MavenMaven_ClassPath44.setter
    def MavenMaven_ClassPath44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_ClassPath__MavenMaven_ClassPath44", None)
        self.__MavenMaven_ClassPath44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FileSet45"):
                    opp_val = getattr(item, "FileSet45", None)
                    
                    if opp_val == self:
                        setattr(item, "FileSet45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FileSet45"):
                    opp_val = getattr(item, "FileSet45", None)
                    
                    setattr(item, "FileSet45", self)
                    

class MavenMaven_FilterSet(Set):

    def __init__(self, starttoken: str, endtoken: str, MavenMaven_FilterSet34: set["FiltersFile"] = None, MavenMaven_FilterSet: set["Filter"] = None):
        self.starttoken = starttoken
        self.endtoken = endtoken
        self.MavenMaven_FilterSet34 = MavenMaven_FilterSet34 if MavenMaven_FilterSet34 is not None else set()
        self.MavenMaven_FilterSet = MavenMaven_FilterSet if MavenMaven_FilterSet is not None else set()
        
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
    def MavenMaven_FilterSet(self):
        return self.__MavenMaven_FilterSet

    @MavenMaven_FilterSet.setter
    def MavenMaven_FilterSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FilterSet__MavenMaven_FilterSet", None)
        self.__MavenMaven_FilterSet = value if value is not None else set()
        
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
                    

    @property
    def MavenMaven_FilterSet34(self):
        return self.__MavenMaven_FilterSet34

    @MavenMaven_FilterSet34.setter
    def MavenMaven_FilterSet34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FilterSet__MavenMaven_FilterSet34", None)
        self.__MavenMaven_FilterSet34 = value if value is not None else set()
        
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
                    

class MavenMaven_FileSet(Set):

    def __init__(self, dir: str, MavenMaven_FileSet: set["PatternSet"] = None, MavenMaven_FileSet29: set["Includes"] = None, MavenMaven_FileSet31: set["Excludes"] = None):
        self.dir = dir
        self.MavenMaven_FileSet = MavenMaven_FileSet if MavenMaven_FileSet is not None else set()
        self.MavenMaven_FileSet29 = MavenMaven_FileSet29 if MavenMaven_FileSet29 is not None else set()
        self.MavenMaven_FileSet31 = MavenMaven_FileSet31 if MavenMaven_FileSet31 is not None else set()
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def MavenMaven_FileSet29(self):
        return self.__MavenMaven_FileSet29

    @MavenMaven_FileSet29.setter
    def MavenMaven_FileSet29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet29", None)
        self.__MavenMaven_FileSet29 = value if value is not None else set()
        
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
    def MavenMaven_FileSet31(self):
        return self.__MavenMaven_FileSet31

    @MavenMaven_FileSet31.setter
    def MavenMaven_FileSet31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet31", None)
        self.__MavenMaven_FileSet31 = value if value is not None else set()
        
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
    def MavenMaven_FileSet(self):
        return self.__MavenMaven_FileSet

    @MavenMaven_FileSet.setter
    def MavenMaven_FileSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet", None)
        self.__MavenMaven_FileSet = value if value is not None else set()
        
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
                    

class MavenMaven_PatternSet(Set):

    pass
class FileSet:

    pass
class PathElement:

    pass
class MavenMaven_Path(Set):

    def __init__(self, id: str, refid: str, MavenMaven_Path: "Path" = None, MavenMaven_Path38: set["PathElement"] = None, MavenMaven_Path40: set["FileSet"] = None):
        self.id = id
        self.refid = refid
        self.MavenMaven_Path = MavenMaven_Path
        self.MavenMaven_Path38 = MavenMaven_Path38 if MavenMaven_Path38 is not None else set()
        self.MavenMaven_Path40 = MavenMaven_Path40 if MavenMaven_Path40 is not None else set()
        
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
    def MavenMaven_Path38(self):
        return self.__MavenMaven_Path38

    @MavenMaven_Path38.setter
    def MavenMaven_Path38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path38", None)
        self.__MavenMaven_Path38 = value if value is not None else set()
        
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
    def MavenMaven_Path(self):
        return self.__MavenMaven_Path

    @MavenMaven_Path.setter
    def MavenMaven_Path(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path", None)
        self.__MavenMaven_Path = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Path36"):
                opp_val = getattr(old_value, "Path36", None)
                if opp_val == self:
                    setattr(old_value, "Path36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Path36"):
                opp_val = getattr(value, "Path36", None)
                setattr(value, "Path36", self)

    @property
    def MavenMaven_Path40(self):
        return self.__MavenMaven_Path40

    @MavenMaven_Path40.setter
    def MavenMaven_Path40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path40", None)
        self.__MavenMaven_Path40 = value if value is not None else set()
        
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
                    

class InExcludes:

    pass
class MavenMaven_IncludesFile(InExcludes):

    pass
class MavenMaven_Excludes(InExcludes):

    pass
class MavenMaven_Includes(InExcludes):

    pass
class Basic:

    pass
class MavenMaven_InExcludes(Basic):

    def __init__(self, name: str, ifCondition: str, unless: str):
        self.name = name
        self.ifCondition = ifCondition
        self.unless = unless
        
        pass
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
    def ifCondition(self):
        return self.__ifCondition

    @ifCondition.setter
    def ifCondition(self, ifCondition: str):
        self.__ifCondition = ifCondition


class MavenMaven_PathElement(Basic):

    def __init__(self, path: str, location: str):
        self.path = path
        self.location = location
        
        pass
    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class MavenMaven_Mapper(Basic):

    def __init__(self, type: str, classname: str, classpath: str, classpathref: str, from_: str, to: str):
        self.type = type
        self.classname = classname
        self.classpath = classpath
        self.classpathref = classpathref
        self.from_ = from_
        self.to = to
        
        pass
    @property
    def classpathref(self):
        return self.__classpathref

    @classpathref.setter
    def classpathref(self, classpathref: str):
        self.__classpathref = classpathref


    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, to: str):
        self.__to = to


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def classpath(self):
        return self.__classpath

    @classpath.setter
    def classpath(self, classpath: str):
        self.__classpath = classpath


class Pattern:

    pass
class MavenMaven_Set(Pattern):

    pass
class MavenMaven_Basic(Pattern):

    pass
class MavenMaven_Pattern(ABC):

    pass
class PostGoal:

    pass
class PreGoal:

    pass
class MavenMaven_FiltersFile(Basic):

    def __init__(self, file: str):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class MavenMaven_Filter(Basic):

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


class MavenMaven_FileList(Basic):

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


class MavenMaven_ExcludesFile(InExcludes):

    pass
class MavenMaven_ContentsGoal(ABC):

    pass
class MavenMaven_AbstractGoal(ABC):

    pass
class JellyCommand:

    pass
class MavenMaven_JellyForEach(JellyCommand):

    def __init__(self, items: str, var: str, indexVar: str, MavenMaven_JellyForEach: "ContentsGoal" = None):
        self.items = items
        self.var = var
        self.indexVar = indexVar
        self.MavenMaven_JellyForEach = MavenMaven_JellyForEach
        
        pass
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var


    @property
    def indexVar(self):
        return self.__indexVar

    @indexVar.setter
    def indexVar(self, indexVar: str):
        self.__indexVar = indexVar


    @property
    def MavenMaven_JellyForEach(self):
        return self.__MavenMaven_JellyForEach

    @MavenMaven_JellyForEach.setter
    def MavenMaven_JellyForEach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_JellyForEach__MavenMaven_JellyForEach", None)
        self.__MavenMaven_JellyForEach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ContentsGoal"):
                opp_val = getattr(old_value, "ContentsGoal", None)
                if opp_val == self:
                    setattr(old_value, "ContentsGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ContentsGoal"):
                opp_val = getattr(value, "ContentsGoal", None)
                setattr(value, "ContentsGoal", self)

class MavenMaven_JellySet(JellyCommand):

    def __init__(self, var: str, value: str):
        self.var = var
        self.value = value
        
        pass
    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class AbstractGoal:

    pass
class MavenMaven_Goal(AbstractGoal):

    def __init__(self, name: str, centralGoal: "PreGoal" = None, centralGoal25: "PostGoal" = None):
        self.name = name
        self.centralGoal = centralGoal
        self.centralGoal25 = centralGoal25
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def centralGoal(self):
        return self.__centralGoal

    @centralGoal.setter
    def centralGoal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__centralGoal", None)
        self.__centralGoal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PreGoal"):
                opp_val = getattr(old_value, "PreGoal", None)
                if opp_val == self:
                    setattr(old_value, "PreGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PreGoal"):
                opp_val = getattr(value, "PreGoal", None)
                setattr(value, "PreGoal", self)

    @property
    def centralGoal25(self):
        return self.__centralGoal25

    @centralGoal25.setter
    def centralGoal25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__centralGoal25", None)
        self.__centralGoal25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PostGoal"):
                opp_val = getattr(old_value, "PostGoal", None)
                if opp_val == self:
                    setattr(old_value, "PostGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PostGoal"):
                opp_val = getattr(value, "PostGoal", None)
                setattr(value, "PostGoal", self)

class MavenMaven_PrePostGoal(AbstractGoal):

    pass
class MavenMaven_Xmlns:

    def __init__(self, value: str, name: str):
        self.value = value
        self.name = name
        
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


class PrePostGoal:

    pass
class MavenMaven_PreGoal(PrePostGoal):

    pass
class MavenMaven_PostGoal(PrePostGoal):

    pass
class AntTaskDef:

    pass
class AntProperty:

    pass
class MavenMaven_AntPropertyFile(AntProperty):

    def __init__(self, file: str, AntProperty: "MavenMaven_Project" = None):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class MavenMaven_AntPropertyEnv(AntProperty):

    def __init__(self, environment: str, AntProperty: "MavenMaven_Project" = None):
        self.environment = environment
        
        pass
    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment


class Path:

    pass
class Goal:

    pass
class Xmlns:

    pass
class MavenMaven_Project:

    pass
class AntPropertyName:

    pass
class MavenMaven_AntPropertyLocation(AntPropertyName):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class MavenMaven_AntPropertyValue(AntPropertyName):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class MavenMaven_AntPropertyName(AntProperty):

    def __init__(self, name: str, AntProperty: "MavenMaven_Project" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class ContentsGoal:

    pass
class MavenMaven_Task(ContentsGoal):

    pass
class MavenMaven_JellyCommand(ContentsGoal):

    pass
class MavenMaven_AttainGoal(ContentsGoal):

    pass
class MavenMaven_AntTaskDef(ContentsGoal):

    def __init__(self, name: str, classname: str, ContentsGoal: "MavenMaven_JellyForEach" = None, ContentsGoal16: "MavenMaven_AbstractGoal" = None):
        self.name = name
        self.classname = classname
        
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


class MavenMaven_AntProperty(ContentsGoal):

    pass