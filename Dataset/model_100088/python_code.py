from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
    def use(self):
        return self.__use

    @use.setter
    def use(self, use: str):
        self.__use = use


    @property
    def windowtitle(self):
        return self.__windowtitle

    @windowtitle.setter
    def windowtitle(self, windowtitle: str):
        self.__windowtitle = windowtitle


    @property
    def defaultexcludes(self):
        return self.__defaultexcludes

    @defaultexcludes.setter
    def defaultexcludes(self, defaultexcludes: str):
        self.__defaultexcludes = defaultexcludes


    @property
    def destdir(self):
        return self.__destdir

    @destdir.setter
    def destdir(self, destdir: str):
        self.__destdir = destdir


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


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
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


class CompileTask:

    pass
class MavenMaven_Javac(CompileTask):

    def __init__(self, srcdir: str, destdir: str, debug: str, fork: str, optimize: str, deprecation: str, MavenMaven_Javac: set["MavenMaven_InExcludes"] = None, MavenMaven_Javac56: "MavenMaven_ClassPath" = None):
        self.srcdir = srcdir
        self.destdir = destdir
        self.debug = debug
        self.fork = fork
        self.optimize = optimize
        self.deprecation = deprecation
        self.MavenMaven_Javac = MavenMaven_Javac if MavenMaven_Javac is not None else set()
        self.MavenMaven_Javac56 = MavenMaven_Javac56
        
        pass
    @property
    def fork(self):
        return self.__fork

    @fork.setter
    def fork(self, fork: str):
        self.__fork = fork


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
    def MavenMaven_Javac56(self):
        return self.__MavenMaven_Javac56

    @MavenMaven_Javac56.setter
    def MavenMaven_Javac56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Javac__MavenMaven_Javac56", None)
        self.__MavenMaven_Javac56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_ClassPath57"):
                opp_val = getattr(old_value, "MavenMaven_ClassPath57", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_ClassPath57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_ClassPath57"):
                opp_val = getattr(value, "MavenMaven_ClassPath57", None)
                setattr(value, "MavenMaven_ClassPath57", self)

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
                if hasattr(item, "MavenMaven_InExcludes54"):
                    opp_val = getattr(item, "MavenMaven_InExcludes54", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_InExcludes54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_InExcludes54"):
                    opp_val = getattr(item, "MavenMaven_InExcludes54", None)
                    
                    setattr(item, "MavenMaven_InExcludes54", self)
                    

class FileTask:

    pass
class MavenMaven_Copy(FileTask):

    def __init__(self, file: str, presservelastmodified: str, tofile: str, todir: str, overwrite: str, filtering: str, flatten: str, includeEmptyDirs: str, MavenMaven_Copy: "MavenMaven_FileSet" = None, MavenMaven_Copy61: "MavenMaven_FilterSet" = None, MavenMaven_Copy64: "MavenMaven_Mapper" = None):
        self.file = file
        self.presservelastmodified = presservelastmodified
        self.tofile = tofile
        self.todir = todir
        self.overwrite = overwrite
        self.filtering = filtering
        self.flatten = flatten
        self.includeEmptyDirs = includeEmptyDirs
        self.MavenMaven_Copy = MavenMaven_Copy
        self.MavenMaven_Copy61 = MavenMaven_Copy61
        self.MavenMaven_Copy64 = MavenMaven_Copy64
        
        pass
    @property
    def tofile(self):
        return self.__tofile

    @tofile.setter
    def tofile(self, tofile: str):
        self.__tofile = tofile


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
    def presservelastmodified(self):
        return self.__presservelastmodified

    @presservelastmodified.setter
    def presservelastmodified(self, presservelastmodified: str):
        self.__presservelastmodified = presservelastmodified


    @property
    def todir(self):
        return self.__todir

    @todir.setter
    def todir(self, todir: str):
        self.__todir = todir


    @property
    def overwrite(self):
        return self.__overwrite

    @overwrite.setter
    def overwrite(self, overwrite: str):
        self.__overwrite = overwrite


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
            if hasattr(old_value, "MavenMaven_FileSet59"):
                opp_val = getattr(old_value, "MavenMaven_FileSet59", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_FileSet59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_FileSet59"):
                opp_val = getattr(value, "MavenMaven_FileSet59", None)
                setattr(value, "MavenMaven_FileSet59", self)

    @property
    def MavenMaven_Copy61(self):
        return self.__MavenMaven_Copy61

    @MavenMaven_Copy61.setter
    def MavenMaven_Copy61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Copy__MavenMaven_Copy61", None)
        self.__MavenMaven_Copy61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_FilterSet62"):
                opp_val = getattr(old_value, "MavenMaven_FilterSet62", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_FilterSet62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_FilterSet62"):
                opp_val = getattr(value, "MavenMaven_FilterSet62", None)
                setattr(value, "MavenMaven_FilterSet62", self)

    @property
    def MavenMaven_Copy64(self):
        return self.__MavenMaven_Copy64

    @MavenMaven_Copy64.setter
    def MavenMaven_Copy64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Copy__MavenMaven_Copy64", None)
        self.__MavenMaven_Copy64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Mapper"):
                opp_val = getattr(old_value, "MavenMaven_Mapper", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Mapper", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Mapper"):
                opp_val = getattr(value, "MavenMaven_Mapper", None)
                setattr(value, "MavenMaven_Mapper", self)

class MavenMaven_Delete(FileTask):

    def __init__(self, defaultexcludes: str, file: str, dir: str, verbose: str, quiet: str, failonerror: str, includeEmptyDirs: str, includes: str, includesfile: str, excludes: str, excludesfile: str):
        self.defaultexcludes = defaultexcludes
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
        
        pass
    @property
    def includesfile(self):
        return self.__includesfile

    @includesfile.setter
    def includesfile(self, includesfile: str):
        self.__includesfile = includesfile


    @property
    def includes(self):
        return self.__includes

    @includes.setter
    def includes(self, includes: str):
        self.__includes = includes


    @property
    def includeEmptyDirs(self):
        return self.__includeEmptyDirs

    @includeEmptyDirs.setter
    def includeEmptyDirs(self, includeEmptyDirs: str):
        self.__includeEmptyDirs = includeEmptyDirs


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
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def excludesfile(self):
        return self.__excludesfile

    @excludesfile.setter
    def excludesfile(self, excludesfile: str):
        self.__excludesfile = excludesfile


    @property
    def verbose(self):
        return self.__verbose

    @verbose.setter
    def verbose(self, verbose: str):
        self.__verbose = verbose


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
    def basedir(self):
        return self.__basedir

    @basedir.setter
    def basedir(self, basedir: str):
        self.__basedir = basedir


    @property
    def manifest(self):
        return self.__manifest

    @manifest.setter
    def manifest(self, manifest: str):
        self.__manifest = manifest


class ExecutionTask:

    pass
class MavenMaven_Java(ExecutionTask):

    def __init__(self, classname: str, jar: str, fork: str, MavenMaven_Java: "MavenMaven_ClassPath" = None):
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
            if hasattr(old_value, "MavenMaven_ClassPath51"):
                opp_val = getattr(old_value, "MavenMaven_ClassPath51", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_ClassPath51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_ClassPath51"):
                opp_val = getattr(value, "MavenMaven_ClassPath51", None)
                setattr(value, "MavenMaven_ClassPath51", self)

class MavenMaven_Exec(ExecutionTask):

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
class MavenMaven_ArchiveTask(PreDefinedTask):

    pass
class MavenMaven_FileTask(PreDefinedTask):

    pass
class MavenMaven_DocumentationTask(PreDefinedTask):

    pass
class MavenMaven_ExecutionTask(PreDefinedTask):

    pass
class MavenMaven_Attribut:

    def __init__(self, name: str, value: str, MavenMaven_Attribut: "MavenMaven_NewTask" = None):
        self.name = name
        self.value = value
        self.MavenMaven_Attribut = MavenMaven_Attribut
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def MavenMaven_Attribut(self):
        return self.__MavenMaven_Attribut

    @MavenMaven_Attribut.setter
    def MavenMaven_Attribut(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Attribut__MavenMaven_Attribut", None)
        self.__MavenMaven_Attribut = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_NewTask49"):
                opp_val = getattr(old_value, "MavenMaven_NewTask49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_NewTask49"):
                opp_val = getattr(value, "MavenMaven_NewTask49", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_NewTask49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MavenMaven_CompileTask(PreDefinedTask):

    pass
class MavenMaven_FormatTstamp:

    def __init__(self, property1: str, pattern: str, offset: str, unit: str, locale: str, MavenMaven_FormatTstamp: "MavenMaven_Tstamp" = None):
        self.property1 = property1
        self.pattern = pattern
        self.offset = offset
        self.unit = unit
        self.locale = locale
        self.MavenMaven_FormatTstamp = MavenMaven_FormatTstamp
        
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
    def MavenMaven_FormatTstamp(self):
        return self.__MavenMaven_FormatTstamp

    @MavenMaven_FormatTstamp.setter
    def MavenMaven_FormatTstamp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FormatTstamp__MavenMaven_FormatTstamp", None)
        self.__MavenMaven_FormatTstamp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Tstamp"):
                opp_val = getattr(old_value, "MavenMaven_Tstamp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Tstamp"):
                opp_val = getattr(value, "MavenMaven_Tstamp", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Tstamp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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


class MavenMaven_MiscellaneousTask(PreDefinedTask):

    pass
class Task:

    pass
class MavenMaven_PreDefinedTask(Task):

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
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class MavenMaven_NewTask(Task):

    pass
class InExcludes:

    pass
class MavenMaven_IncludesFile(InExcludes):

    pass
class MavenMaven_ExcludesFile(InExcludes):

    pass
class MavenMaven_Excludes(InExcludes):

    pass
class MavenMaven_Includes(InExcludes):

    pass
class Basic:

    pass
class MavenMaven_Filter(Basic):

    def __init__(self, token: str, value: str, MavenMaven_Filter: "MavenMaven_FilterSet" = None):
        self.token = token
        self.value = value
        self.MavenMaven_Filter = MavenMaven_Filter
        
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
    def MavenMaven_Filter(self):
        return self.__MavenMaven_Filter

    @MavenMaven_Filter.setter
    def MavenMaven_Filter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Filter__MavenMaven_Filter", None)
        self.__MavenMaven_Filter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_FilterSet"):
                opp_val = getattr(old_value, "MavenMaven_FilterSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_FilterSet"):
                opp_val = getattr(value, "MavenMaven_FilterSet", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_FilterSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MavenMaven_InExcludes(Basic):

    def __init__(self, name: str, ifCondition: str, unless: str, MavenMaven_InExcludes: "MavenMaven_PatternSet" = None, MavenMaven_InExcludes54: "MavenMaven_Javac" = None):
        self.name = name
        self.ifCondition = ifCondition
        self.unless = unless
        self.MavenMaven_InExcludes = MavenMaven_InExcludes
        self.MavenMaven_InExcludes54 = MavenMaven_InExcludes54
        
        pass
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
    def unless(self):
        return self.__unless

    @unless.setter
    def unless(self, unless: str):
        self.__unless = unless


    @property
    def MavenMaven_InExcludes54(self):
        return self.__MavenMaven_InExcludes54

    @MavenMaven_InExcludes54.setter
    def MavenMaven_InExcludes54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_InExcludes__MavenMaven_InExcludes54", None)
        self.__MavenMaven_InExcludes54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Javac"):
                opp_val = getattr(old_value, "MavenMaven_Javac", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Javac"):
                opp_val = getattr(value, "MavenMaven_Javac", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Javac", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MavenMaven_InExcludes(self):
        return self.__MavenMaven_InExcludes

    @MavenMaven_InExcludes.setter
    def MavenMaven_InExcludes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_InExcludes__MavenMaven_InExcludes", None)
        self.__MavenMaven_InExcludes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_PatternSet"):
                opp_val = getattr(old_value, "MavenMaven_PatternSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_PatternSet"):
                opp_val = getattr(value, "MavenMaven_PatternSet", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_PatternSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MavenMaven_FileList(Basic):

    def __init__(self, dir: str, files: str):
        self.dir = dir
        self.files = files
        
        pass
    @property
    def files(self):
        return self.__files

    @files.setter
    def files(self, files: str):
        self.__files = files


    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


class MavenMaven_Mapper(Basic):

    def __init__(self, type: str, classname: str, classpath: str, classpathref: str, from_: str, to: str, MavenMaven_Mapper: "MavenMaven_Copy" = None):
        self.type = type
        self.classname = classname
        self.classpath = classpath
        self.classpathref = classpathref
        self.from_ = from_
        self.to = to
        self.MavenMaven_Mapper = MavenMaven_Mapper
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def classpathref(self):
        return self.__classpathref

    @classpathref.setter
    def classpathref(self, classpathref: str):
        self.__classpathref = classpathref


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
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_


    @property
    def classpath(self):
        return self.__classpath

    @classpath.setter
    def classpath(self, classpath: str):
        self.__classpath = classpath


    @property
    def MavenMaven_Mapper(self):
        return self.__MavenMaven_Mapper

    @MavenMaven_Mapper.setter
    def MavenMaven_Mapper(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Mapper__MavenMaven_Mapper", None)
        self.__MavenMaven_Mapper = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Copy64"):
                opp_val = getattr(old_value, "MavenMaven_Copy64", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Copy64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Copy64"):
                opp_val = getattr(value, "MavenMaven_Copy64", None)
                setattr(value, "MavenMaven_Copy64", self)

class Pattern:

    pass
class MavenMaven_Basic(Pattern):

    pass
class Set:

    pass
class MavenMaven_FilterSet(Set):

    def __init__(self, starttoken: str, endtoken: str, MavenMaven_FilterSet: set["MavenMaven_Filter"] = None, MavenMaven_FilterSet32: set["MavenMaven_FiltersFile"] = None, MavenMaven_FilterSet62: "MavenMaven_Copy" = None):
        self.starttoken = starttoken
        self.endtoken = endtoken
        self.MavenMaven_FilterSet = MavenMaven_FilterSet if MavenMaven_FilterSet is not None else set()
        self.MavenMaven_FilterSet32 = MavenMaven_FilterSet32 if MavenMaven_FilterSet32 is not None else set()
        self.MavenMaven_FilterSet62 = MavenMaven_FilterSet62
        
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
    def MavenMaven_FilterSet32(self):
        return self.__MavenMaven_FilterSet32

    @MavenMaven_FilterSet32.setter
    def MavenMaven_FilterSet32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FilterSet__MavenMaven_FilterSet32", None)
        self.__MavenMaven_FilterSet32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MavenMaven_FiltersFile"):
                    opp_val = getattr(item, "MavenMaven_FiltersFile", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_FiltersFile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_FiltersFile"):
                    opp_val = getattr(item, "MavenMaven_FiltersFile", None)
                    
                    setattr(item, "MavenMaven_FiltersFile", self)
                    

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
                if hasattr(item, "MavenMaven_Filter"):
                    opp_val = getattr(item, "MavenMaven_Filter", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_Filter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_Filter"):
                    opp_val = getattr(item, "MavenMaven_Filter", None)
                    
                    setattr(item, "MavenMaven_Filter", self)
                    

    @property
    def MavenMaven_FilterSet62(self):
        return self.__MavenMaven_FilterSet62

    @MavenMaven_FilterSet62.setter
    def MavenMaven_FilterSet62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FilterSet__MavenMaven_FilterSet62", None)
        self.__MavenMaven_FilterSet62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Copy61"):
                opp_val = getattr(old_value, "MavenMaven_Copy61", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Copy61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Copy61"):
                opp_val = getattr(value, "MavenMaven_Copy61", None)
                setattr(value, "MavenMaven_Copy61", self)

class MavenMaven_FileSet(Set):

    def __init__(self, dir: str, MavenMaven_FileSet: set["MavenMaven_PatternSet"] = None, MavenMaven_FileSet27: set["MavenMaven_Includes"] = None, MavenMaven_FileSet29: set["MavenMaven_Excludes"] = None, MavenMaven_FileSet40: "MavenMaven_Path" = None, MavenMaven_FileSet45: "MavenMaven_ClassPath" = None, MavenMaven_FileSet59: "MavenMaven_Copy" = None):
        self.dir = dir
        self.MavenMaven_FileSet = MavenMaven_FileSet if MavenMaven_FileSet is not None else set()
        self.MavenMaven_FileSet27 = MavenMaven_FileSet27 if MavenMaven_FileSet27 is not None else set()
        self.MavenMaven_FileSet29 = MavenMaven_FileSet29 if MavenMaven_FileSet29 is not None else set()
        self.MavenMaven_FileSet40 = MavenMaven_FileSet40
        self.MavenMaven_FileSet45 = MavenMaven_FileSet45
        self.MavenMaven_FileSet59 = MavenMaven_FileSet59
        
        pass
    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, dir: str):
        self.__dir = dir


    @property
    def MavenMaven_FileSet45(self):
        return self.__MavenMaven_FileSet45

    @MavenMaven_FileSet45.setter
    def MavenMaven_FileSet45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet45", None)
        self.__MavenMaven_FileSet45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_ClassPath44"):
                opp_val = getattr(old_value, "MavenMaven_ClassPath44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_ClassPath44"):
                opp_val = getattr(value, "MavenMaven_ClassPath44", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_ClassPath44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MavenMaven_FileSet40(self):
        return self.__MavenMaven_FileSet40

    @MavenMaven_FileSet40.setter
    def MavenMaven_FileSet40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet40", None)
        self.__MavenMaven_FileSet40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Path39"):
                opp_val = getattr(old_value, "MavenMaven_Path39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Path39"):
                opp_val = getattr(value, "MavenMaven_Path39", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Path39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "MavenMaven_PatternSet25"):
                    opp_val = getattr(item, "MavenMaven_PatternSet25", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_PatternSet25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_PatternSet25"):
                    opp_val = getattr(item, "MavenMaven_PatternSet25", None)
                    
                    setattr(item, "MavenMaven_PatternSet25", self)
                    

    @property
    def MavenMaven_FileSet59(self):
        return self.__MavenMaven_FileSet59

    @MavenMaven_FileSet59.setter
    def MavenMaven_FileSet59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet59", None)
        self.__MavenMaven_FileSet59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Copy"):
                opp_val = getattr(old_value, "MavenMaven_Copy", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Copy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Copy"):
                opp_val = getattr(value, "MavenMaven_Copy", None)
                setattr(value, "MavenMaven_Copy", self)

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
                if hasattr(item, "MavenMaven_Excludes"):
                    opp_val = getattr(item, "MavenMaven_Excludes", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_Excludes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_Excludes"):
                    opp_val = getattr(item, "MavenMaven_Excludes", None)
                    
                    setattr(item, "MavenMaven_Excludes", self)
                    

    @property
    def MavenMaven_FileSet27(self):
        return self.__MavenMaven_FileSet27

    @MavenMaven_FileSet27.setter
    def MavenMaven_FileSet27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FileSet__MavenMaven_FileSet27", None)
        self.__MavenMaven_FileSet27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MavenMaven_Includes"):
                    opp_val = getattr(item, "MavenMaven_Includes", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_Includes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_Includes"):
                    opp_val = getattr(item, "MavenMaven_Includes", None)
                    
                    setattr(item, "MavenMaven_Includes", self)
                    

class MavenMaven_ClassPath(Set):

    def __init__(self, refid: str, MavenMaven_ClassPath: set["MavenMaven_PathElement"] = None, MavenMaven_ClassPath44: set["MavenMaven_FileSet"] = None, MavenMaven_ClassPath51: "MavenMaven_Java" = None, MavenMaven_ClassPath57: "MavenMaven_Javac" = None):
        self.refid = refid
        self.MavenMaven_ClassPath = MavenMaven_ClassPath if MavenMaven_ClassPath is not None else set()
        self.MavenMaven_ClassPath44 = MavenMaven_ClassPath44 if MavenMaven_ClassPath44 is not None else set()
        self.MavenMaven_ClassPath51 = MavenMaven_ClassPath51
        self.MavenMaven_ClassPath57 = MavenMaven_ClassPath57
        
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
                if hasattr(item, "MavenMaven_PathElement42"):
                    opp_val = getattr(item, "MavenMaven_PathElement42", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_PathElement42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_PathElement42"):
                    opp_val = getattr(item, "MavenMaven_PathElement42", None)
                    
                    setattr(item, "MavenMaven_PathElement42", self)
                    

    @property
    def MavenMaven_ClassPath51(self):
        return self.__MavenMaven_ClassPath51

    @MavenMaven_ClassPath51.setter
    def MavenMaven_ClassPath51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_ClassPath__MavenMaven_ClassPath51", None)
        self.__MavenMaven_ClassPath51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Java"):
                opp_val = getattr(old_value, "MavenMaven_Java", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Java", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Java"):
                opp_val = getattr(value, "MavenMaven_Java", None)
                setattr(value, "MavenMaven_Java", self)

    @property
    def MavenMaven_ClassPath57(self):
        return self.__MavenMaven_ClassPath57

    @MavenMaven_ClassPath57.setter
    def MavenMaven_ClassPath57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_ClassPath__MavenMaven_ClassPath57", None)
        self.__MavenMaven_ClassPath57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Javac56"):
                opp_val = getattr(old_value, "MavenMaven_Javac56", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Javac56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Javac56"):
                opp_val = getattr(value, "MavenMaven_Javac56", None)
                setattr(value, "MavenMaven_Javac56", self)

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
                if hasattr(item, "MavenMaven_FileSet45"):
                    opp_val = getattr(item, "MavenMaven_FileSet45", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_FileSet45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_FileSet45"):
                    opp_val = getattr(item, "MavenMaven_FileSet45", None)
                    
                    setattr(item, "MavenMaven_FileSet45", self)
                    

class MavenMaven_PatternSet(Set):

    pass
class MavenMaven_Set(Pattern):

    pass
class MavenMaven_PathElement(Basic):

    def __init__(self, path: str, location: str, MavenMaven_PathElement42: "MavenMaven_ClassPath" = None, MavenMaven_PathElement: "MavenMaven_Path" = None):
        self.path = path
        self.location = location
        self.MavenMaven_PathElement42 = MavenMaven_PathElement42
        self.MavenMaven_PathElement = MavenMaven_PathElement
        
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
    def MavenMaven_PathElement(self):
        return self.__MavenMaven_PathElement

    @MavenMaven_PathElement.setter
    def MavenMaven_PathElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_PathElement__MavenMaven_PathElement", None)
        self.__MavenMaven_PathElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Path37"):
                opp_val = getattr(old_value, "MavenMaven_Path37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Path37"):
                opp_val = getattr(value, "MavenMaven_Path37", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Path37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MavenMaven_PathElement42(self):
        return self.__MavenMaven_PathElement42

    @MavenMaven_PathElement42.setter
    def MavenMaven_PathElement42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_PathElement__MavenMaven_PathElement42", None)
        self.__MavenMaven_PathElement42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_ClassPath"):
                opp_val = getattr(old_value, "MavenMaven_ClassPath", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_ClassPath"):
                opp_val = getattr(value, "MavenMaven_ClassPath", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_ClassPath", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MavenMaven_FiltersFile(Basic):

    def __init__(self, file: str, MavenMaven_FiltersFile: "MavenMaven_FilterSet" = None):
        self.file = file
        self.MavenMaven_FiltersFile = MavenMaven_FiltersFile
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


    @property
    def MavenMaven_FiltersFile(self):
        return self.__MavenMaven_FiltersFile

    @MavenMaven_FiltersFile.setter
    def MavenMaven_FiltersFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_FiltersFile__MavenMaven_FiltersFile", None)
        self.__MavenMaven_FiltersFile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_FilterSet32"):
                opp_val = getattr(old_value, "MavenMaven_FilterSet32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_FilterSet32"):
                opp_val = getattr(value, "MavenMaven_FilterSet32", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_FilterSet32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MavenMaven_ContentsGoal(ABC):

    pass
class MavenMaven_AbstractGoal(ABC):

    pass
class JellyCommand:

    pass
class MavenMaven_JellySet(JellyCommand):

    def __init__(self, var: str, value: str):
        self.var = var
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def var(self):
        return self.__var

    @var.setter
    def var(self, var: str):
        self.__var = var


class MavenMaven_Pattern(ABC):

    pass
class PrePostGoal:

    pass
class MavenMaven_PostGoal(PrePostGoal):

    pass
class MavenMaven_PreGoal(PrePostGoal):

    pass
class AbstractGoal:

    pass
class MavenMaven_Path(Set):

    def __init__(self, id: str, refid: str, MavenMaven_Path39: set["MavenMaven_FileSet"] = None, MavenMaven_Path: "MavenMaven_Project" = None, MavenMaven_Path35: "MavenMaven_Path" = None, MavenMaven_Path33: "MavenMaven_Path" = None, MavenMaven_Path37: set["MavenMaven_PathElement"] = None):
        self.id = id
        self.refid = refid
        self.MavenMaven_Path39 = MavenMaven_Path39 if MavenMaven_Path39 is not None else set()
        self.MavenMaven_Path = MavenMaven_Path
        self.MavenMaven_Path35 = MavenMaven_Path35
        self.MavenMaven_Path33 = MavenMaven_Path33
        self.MavenMaven_Path37 = MavenMaven_Path37 if MavenMaven_Path37 is not None else set()
        
        pass
    @property
    def refid(self):
        return self.__refid

    @refid.setter
    def refid(self, refid: str):
        self.__refid = refid


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def MavenMaven_Path33(self):
        return self.__MavenMaven_Path33

    @MavenMaven_Path33.setter
    def MavenMaven_Path33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path33", None)
        self.__MavenMaven_Path33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Path35"):
                opp_val = getattr(old_value, "MavenMaven_Path35", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Path35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Path35"):
                opp_val = getattr(value, "MavenMaven_Path35", None)
                setattr(value, "MavenMaven_Path35", self)

    @property
    def MavenMaven_Path37(self):
        return self.__MavenMaven_Path37

    @MavenMaven_Path37.setter
    def MavenMaven_Path37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path37", None)
        self.__MavenMaven_Path37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MavenMaven_PathElement"):
                    opp_val = getattr(item, "MavenMaven_PathElement", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_PathElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_PathElement"):
                    opp_val = getattr(item, "MavenMaven_PathElement", None)
                    
                    setattr(item, "MavenMaven_PathElement", self)
                    

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
            if hasattr(old_value, "MavenMaven_Project4"):
                opp_val = getattr(old_value, "MavenMaven_Project4", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Project4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Project4"):
                opp_val = getattr(value, "MavenMaven_Project4", None)
                setattr(value, "MavenMaven_Project4", self)

    @property
    def MavenMaven_Path35(self):
        return self.__MavenMaven_Path35

    @MavenMaven_Path35.setter
    def MavenMaven_Path35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path35", None)
        self.__MavenMaven_Path35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Path33"):
                opp_val = getattr(old_value, "MavenMaven_Path33", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Path33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Path33"):
                opp_val = getattr(value, "MavenMaven_Path33", None)
                setattr(value, "MavenMaven_Path33", self)

    @property
    def MavenMaven_Path39(self):
        return self.__MavenMaven_Path39

    @MavenMaven_Path39.setter
    def MavenMaven_Path39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Path__MavenMaven_Path39", None)
        self.__MavenMaven_Path39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MavenMaven_FileSet40"):
                    opp_val = getattr(item, "MavenMaven_FileSet40", None)
                    
                    if opp_val == self:
                        setattr(item, "MavenMaven_FileSet40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MavenMaven_FileSet40"):
                    opp_val = getattr(item, "MavenMaven_FileSet40", None)
                    
                    setattr(item, "MavenMaven_FileSet40", self)
                    

class MavenMaven_Goal(AbstractGoal):

    def __init__(self, name: str, MavenMaven_Goal13: "MavenMaven_Project" = None, MavenMaven_Goal: "MavenMaven_Project" = None, Goal: "MavenMaven_PreGoal" = None, Goal19: "MavenMaven_PostGoal" = None, centralGoal: "MavenMaven_PreGoal" = None, centralGoal22: "MavenMaven_PostGoal" = None, MavenMaven_Goal16: "MavenMaven_AttainGoal" = None):
        self.name = name
        self.MavenMaven_Goal13 = MavenMaven_Goal13
        self.MavenMaven_Goal = MavenMaven_Goal
        self.Goal = Goal
        self.Goal19 = Goal19
        self.centralGoal = centralGoal
        self.centralGoal22 = centralGoal22
        self.MavenMaven_Goal16 = MavenMaven_Goal16
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Goal(self):
        return self.__Goal

    @Goal.setter
    def Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__Goal", None)
        self.__Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "preGoal"):
                opp_val = getattr(old_value, "preGoal", None)
                if opp_val == self:
                    setattr(old_value, "preGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "preGoal"):
                opp_val = getattr(value, "preGoal", None)
                setattr(value, "preGoal", self)

    @property
    def centralGoal22(self):
        return self.__centralGoal22

    @centralGoal22.setter
    def centralGoal22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__centralGoal22", None)
        self.__centralGoal22 = value
        
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

    @property
    def MavenMaven_Goal13(self):
        return self.__MavenMaven_Goal13

    @MavenMaven_Goal13.setter
    def MavenMaven_Goal13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__MavenMaven_Goal13", None)
        self.__MavenMaven_Goal13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Project12"):
                opp_val = getattr(old_value, "MavenMaven_Project12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Project12"):
                opp_val = getattr(value, "MavenMaven_Project12", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Project12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def Goal19(self):
        return self.__Goal19

    @Goal19.setter
    def Goal19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__Goal19", None)
        self.__Goal19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "postGoal"):
                opp_val = getattr(old_value, "postGoal", None)
                if opp_val == self:
                    setattr(old_value, "postGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "postGoal"):
                opp_val = getattr(value, "postGoal", None)
                setattr(value, "postGoal", self)

    @property
    def MavenMaven_Goal(self):
        return self.__MavenMaven_Goal

    @MavenMaven_Goal.setter
    def MavenMaven_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__MavenMaven_Goal", None)
        self.__MavenMaven_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Project2"):
                opp_val = getattr(old_value, "MavenMaven_Project2", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_Project2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Project2"):
                opp_val = getattr(value, "MavenMaven_Project2", None)
                setattr(value, "MavenMaven_Project2", self)

    @property
    def MavenMaven_Goal16(self):
        return self.__MavenMaven_Goal16

    @MavenMaven_Goal16.setter
    def MavenMaven_Goal16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Goal__MavenMaven_Goal16", None)
        self.__MavenMaven_Goal16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_AttainGoal"):
                opp_val = getattr(old_value, "MavenMaven_AttainGoal", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_AttainGoal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_AttainGoal"):
                opp_val = getattr(value, "MavenMaven_AttainGoal", None)
                setattr(value, "MavenMaven_AttainGoal", self)

class MavenMaven_Xmlns:

    def __init__(self, name: str, value: str, MavenMaven_Xmlns: "MavenMaven_Project" = None):
        self.name = name
        self.value = value
        self.MavenMaven_Xmlns = MavenMaven_Xmlns
        
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
    def MavenMaven_Xmlns(self):
        return self.__MavenMaven_Xmlns

    @MavenMaven_Xmlns.setter
    def MavenMaven_Xmlns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_Xmlns__MavenMaven_Xmlns", None)
        self.__MavenMaven_Xmlns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Project"):
                opp_val = getattr(old_value, "MavenMaven_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Project"):
                opp_val = getattr(value, "MavenMaven_Project", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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


class AntProperty:

    pass
class MavenMaven_AntPropertyEnv(AntProperty):

    def __init__(self, environment: str):
        self.environment = environment
        
        pass
    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, environment: str):
        self.__environment = environment


class MavenMaven_AntPropertyFile(AntProperty):

    def __init__(self, file: str):
        self.file = file
        
        pass
    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file: str):
        self.__file = file


class MavenMaven_AntPropertyName(AntProperty):

    def __init__(self, name: str):
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
class MavenMaven_AttainGoal(ContentsGoal):

    pass
class MavenMaven_Task(ContentsGoal):

    pass
class MavenMaven_AntProperty(ContentsGoal):

    pass
class MavenMaven_JellyCommand(ContentsGoal):

    pass
class MavenMaven_PrePostGoal(AbstractGoal):

    pass
class MavenMaven_AntTaskDef(ContentsGoal):

    def __init__(self, name: str, classname: str, MavenMaven_AntTaskDef: "MavenMaven_Project" = None, MavenMaven_AntTaskDef47: "MavenMaven_NewTask" = None):
        self.name = name
        self.classname = classname
        self.MavenMaven_AntTaskDef = MavenMaven_AntTaskDef
        self.MavenMaven_AntTaskDef47 = MavenMaven_AntTaskDef47
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def classname(self):
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname


    @property
    def MavenMaven_AntTaskDef(self):
        return self.__MavenMaven_AntTaskDef

    @MavenMaven_AntTaskDef.setter
    def MavenMaven_AntTaskDef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_AntTaskDef__MavenMaven_AntTaskDef", None)
        self.__MavenMaven_AntTaskDef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_Project8"):
                opp_val = getattr(old_value, "MavenMaven_Project8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_Project8"):
                opp_val = getattr(value, "MavenMaven_Project8", None)
                if opp_val is None:
                    setattr(value, "MavenMaven_Project8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MavenMaven_AntTaskDef47(self):
        return self.__MavenMaven_AntTaskDef47

    @MavenMaven_AntTaskDef47.setter
    def MavenMaven_AntTaskDef47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MavenMaven_AntTaskDef__MavenMaven_AntTaskDef47", None)
        self.__MavenMaven_AntTaskDef47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MavenMaven_NewTask"):
                opp_val = getattr(old_value, "MavenMaven_NewTask", None)
                if opp_val == self:
                    setattr(old_value, "MavenMaven_NewTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MavenMaven_NewTask"):
                opp_val = getattr(value, "MavenMaven_NewTask", None)
                setattr(value, "MavenMaven_NewTask", self)
