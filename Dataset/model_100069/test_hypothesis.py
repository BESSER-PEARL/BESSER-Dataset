import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Mapper,
    FilterSet,
    FileTask,
    Ant_Delete,
    Ant_Mkdir,
    ArchiveTask,
    Ant_Jar,
    DocumentationTask,
    Ant_Javadoc,
    CompileTask,
    Ant_Copy,
    Ant_Javac,
    Ant_TaskDef,
    Ant_FormatTstamp,
    Ant_Task,
    FormatTstamp,
    MiscellaneousTask,
    Ant_Tstamp,
    Ant_Echo,
    ClassPath,
    FileSet,
    PathElement,
    Ant_Java,
    Ant_Exec,
    PreDefinedTask,
    Ant_FileTask,
    Ant_CompileTask,
    Ant_MiscellaneousTask,
    Ant_DocumentationTask,
    Ant_ArchiveTask,
    Ant_ExecutionTask,
    Ant_Attribut,
    Attribut,
    Set,
    Ant_ClassPath,
    Ant_FileSet,
    Ant_PatternSet,
    Ant_Path,
    FiltersFile,
    Filter,
    Ant_FilterSet,
    Excludes,
    Includes,
    PatternSet,
    Task,
    Ant_PreDefinedTask,
    Ant_NewTask,
    Ant_Target,
    InExcludes,
    Ant_Excludes,
    Ant_IncludesFile,
    Ant_ExcludesFile,
    Ant_Includes,
    Basic,
    Ant_InExcludes,
    Ant_FiltersFile,
    Ant_PathElement,
    Ant_Filter,
    Ant_FileList,
    Ant_Mapper,
    Pattern,
    Ant_Set,
    Ant_Basic,
    Ant_Pattern,
    Ant_Project,
    PropertyName,
    Ant_PropertyLocation,
    Ant_PropertyValue,
    Ant_Property,
    TaskDef,
    Property,
    Ant_PropertyEnv,
    Ant_PropertyFile,
    Ant_PropertyName,
    Path,
    Target,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mapper_is_not_abstract():
    assert not inspect.isabstract(Mapper)


def test_mapper_constructor_exists():
    assert callable(Mapper.__init__)


def test_mapper_constructor_args():
    sig = inspect.signature(Mapper.__init__)
    params = list(sig.parameters.keys())



def test_filterset_is_not_abstract():
    assert not inspect.isabstract(FilterSet)


def test_filterset_constructor_exists():
    assert callable(FilterSet.__init__)


def test_filterset_constructor_args():
    sig = inspect.signature(FilterSet.__init__)
    params = list(sig.parameters.keys())



def test_filetask_is_not_abstract():
    assert not inspect.isabstract(FileTask)


def test_filetask_constructor_exists():
    assert callable(FileTask.__init__)


def test_filetask_constructor_args():
    sig = inspect.signature(FileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_delete_is_not_abstract():
    assert not inspect.isabstract(Ant_Delete)


def test_ant_delete_constructor_exists():
    assert callable(Ant_Delete.__init__)


def test_ant_delete_constructor_args():
    sig = inspect.signature(Ant_Delete.__init__)
    params = list(sig.parameters.keys())
    assert "verbose" in params, "Missing parameter 'verbose'"
    assert "dir" in params, "Missing parameter 'dir'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "file" in params, "Missing parameter 'file'"
    assert "excludes" in params, "Missing parameter 'excludes'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "includesfile" in params, "Missing parameter 'includesfile'"
    assert "excludesfile" in params, "Missing parameter 'excludesfile'"
    assert "failonerror" in params, "Missing parameter 'failonerror'"
    assert "quiet" in params, "Missing parameter 'quiet'"

def test_ant_delete_has_verbose():
    assert hasattr(Ant_Delete, "verbose")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_dir():
    assert hasattr(Ant_Delete, "dir")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_defaultexcludes():
    assert hasattr(Ant_Delete, "defaultexcludes")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_file():
    assert hasattr(Ant_Delete, "file")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_excludes():
    assert hasattr(Ant_Delete, "excludes")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_includeEmptyDirs():
    assert hasattr(Ant_Delete, "includeEmptyDirs")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_includes():
    assert hasattr(Ant_Delete, "includes")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_includesfile():
    assert hasattr(Ant_Delete, "includesfile")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "includesfile" in klass.__dict__:
            descriptor = klass.__dict__["includesfile"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_excludesfile():
    assert hasattr(Ant_Delete, "excludesfile")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "excludesfile" in klass.__dict__:
            descriptor = klass.__dict__["excludesfile"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_failonerror():
    assert hasattr(Ant_Delete, "failonerror")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "failonerror" in klass.__dict__:
            descriptor = klass.__dict__["failonerror"]
            break
    assert isinstance(descriptor, property)

def test_ant_delete_has_quiet():
    assert hasattr(Ant_Delete, "quiet")
    descriptor = None
    for klass in Ant_Delete.__mro__:
        if "quiet" in klass.__dict__:
            descriptor = klass.__dict__["quiet"]
            break
    assert isinstance(descriptor, property)



def test_ant_mkdir_is_not_abstract():
    assert not inspect.isabstract(Ant_Mkdir)


def test_ant_mkdir_constructor_exists():
    assert callable(Ant_Mkdir.__init__)


def test_ant_mkdir_constructor_args():
    sig = inspect.signature(Ant_Mkdir.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_ant_mkdir_has_dir():
    assert hasattr(Ant_Mkdir, "dir")
    descriptor = None
    for klass in Ant_Mkdir.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_archivetask_is_not_abstract():
    assert not inspect.isabstract(ArchiveTask)


def test_archivetask_constructor_exists():
    assert callable(ArchiveTask.__init__)


def test_archivetask_constructor_args():
    sig = inspect.signature(ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_jar_is_not_abstract():
    assert not inspect.isabstract(Ant_Jar)


def test_ant_jar_constructor_exists():
    assert callable(Ant_Jar.__init__)


def test_ant_jar_constructor_args():
    sig = inspect.signature(Ant_Jar.__init__)
    params = list(sig.parameters.keys())
    assert "manifest" in params, "Missing parameter 'manifest'"
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "jarfile" in params, "Missing parameter 'jarfile'"
    assert "compress" in params, "Missing parameter 'compress'"
    assert "basedir" in params, "Missing parameter 'basedir'"

def test_ant_jar_has_manifest():
    assert hasattr(Ant_Jar, "manifest")
    descriptor = None
    for klass in Ant_Jar.__mro__:
        if "manifest" in klass.__dict__:
            descriptor = klass.__dict__["manifest"]
            break
    assert isinstance(descriptor, property)

def test_ant_jar_has_encoding():
    assert hasattr(Ant_Jar, "encoding")
    descriptor = None
    for klass in Ant_Jar.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_ant_jar_has_jarfile():
    assert hasattr(Ant_Jar, "jarfile")
    descriptor = None
    for klass in Ant_Jar.__mro__:
        if "jarfile" in klass.__dict__:
            descriptor = klass.__dict__["jarfile"]
            break
    assert isinstance(descriptor, property)

def test_ant_jar_has_compress():
    assert hasattr(Ant_Jar, "compress")
    descriptor = None
    for klass in Ant_Jar.__mro__:
        if "compress" in klass.__dict__:
            descriptor = klass.__dict__["compress"]
            break
    assert isinstance(descriptor, property)

def test_ant_jar_has_basedir():
    assert hasattr(Ant_Jar, "basedir")
    descriptor = None
    for klass in Ant_Jar.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)



def test_documentationtask_is_not_abstract():
    assert not inspect.isabstract(DocumentationTask)


def test_documentationtask_constructor_exists():
    assert callable(DocumentationTask.__init__)


def test_documentationtask_constructor_args():
    sig = inspect.signature(DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_javadoc_is_not_abstract():
    assert not inspect.isabstract(Ant_Javadoc)


def test_ant_javadoc_constructor_exists():
    assert callable(Ant_Javadoc.__init__)


def test_ant_javadoc_constructor_args():
    sig = inspect.signature(Ant_Javadoc.__init__)
    params = list(sig.parameters.keys())
    assert "packagenames" in params, "Missing parameter 'packagenames'"
    assert "author" in params, "Missing parameter 'author'"
    assert "windowtitle" in params, "Missing parameter 'windowtitle'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "sourcepath" in params, "Missing parameter 'sourcepath'"
    assert "use" in params, "Missing parameter 'use'"
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "version" in params, "Missing parameter 'version'"

def test_ant_javadoc_has_packagenames():
    assert hasattr(Ant_Javadoc, "packagenames")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "packagenames" in klass.__dict__:
            descriptor = klass.__dict__["packagenames"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_author():
    assert hasattr(Ant_Javadoc, "author")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_windowtitle():
    assert hasattr(Ant_Javadoc, "windowtitle")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "windowtitle" in klass.__dict__:
            descriptor = klass.__dict__["windowtitle"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_defaultexcludes():
    assert hasattr(Ant_Javadoc, "defaultexcludes")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_sourcepath():
    assert hasattr(Ant_Javadoc, "sourcepath")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "sourcepath" in klass.__dict__:
            descriptor = klass.__dict__["sourcepath"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_use():
    assert hasattr(Ant_Javadoc, "use")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_destdir():
    assert hasattr(Ant_Javadoc, "destdir")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_ant_javadoc_has_version():
    assert hasattr(Ant_Javadoc, "version")
    descriptor = None
    for klass in Ant_Javadoc.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_compiletask_is_not_abstract():
    assert not inspect.isabstract(CompileTask)


def test_compiletask_constructor_exists():
    assert callable(CompileTask.__init__)


def test_compiletask_constructor_args():
    sig = inspect.signature(CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_copy_is_not_abstract():
    assert not inspect.isabstract(Ant_Copy)


def test_ant_copy_constructor_exists():
    assert callable(Ant_Copy.__init__)


def test_ant_copy_constructor_args():
    sig = inspect.signature(Ant_Copy.__init__)
    params = list(sig.parameters.keys())
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "overwrite" in params, "Missing parameter 'overwrite'"
    assert "file" in params, "Missing parameter 'file'"
    assert "todir" in params, "Missing parameter 'todir'"
    assert "flatten" in params, "Missing parameter 'flatten'"
    assert "tofile" in params, "Missing parameter 'tofile'"
    assert "presservelastmodified" in params, "Missing parameter 'presservelastmodified'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"

def test_ant_copy_has_filtering():
    assert hasattr(Ant_Copy, "filtering")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_overwrite():
    assert hasattr(Ant_Copy, "overwrite")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "overwrite" in klass.__dict__:
            descriptor = klass.__dict__["overwrite"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_file():
    assert hasattr(Ant_Copy, "file")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_todir():
    assert hasattr(Ant_Copy, "todir")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "todir" in klass.__dict__:
            descriptor = klass.__dict__["todir"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_flatten():
    assert hasattr(Ant_Copy, "flatten")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "flatten" in klass.__dict__:
            descriptor = klass.__dict__["flatten"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_tofile():
    assert hasattr(Ant_Copy, "tofile")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "tofile" in klass.__dict__:
            descriptor = klass.__dict__["tofile"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_presservelastmodified():
    assert hasattr(Ant_Copy, "presservelastmodified")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "presservelastmodified" in klass.__dict__:
            descriptor = klass.__dict__["presservelastmodified"]
            break
    assert isinstance(descriptor, property)

def test_ant_copy_has_includeEmptyDirs():
    assert hasattr(Ant_Copy, "includeEmptyDirs")
    descriptor = None
    for klass in Ant_Copy.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)



def test_ant_javac_is_not_abstract():
    assert not inspect.isabstract(Ant_Javac)


def test_ant_javac_constructor_exists():
    assert callable(Ant_Javac.__init__)


def test_ant_javac_constructor_args():
    sig = inspect.signature(Ant_Javac.__init__)
    params = list(sig.parameters.keys())
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "deprecation" in params, "Missing parameter 'deprecation'"
    assert "srcdir" in params, "Missing parameter 'srcdir'"
    assert "debug" in params, "Missing parameter 'debug'"
    assert "optimize" in params, "Missing parameter 'optimize'"
    assert "fork" in params, "Missing parameter 'fork'"

def test_ant_javac_has_destdir():
    assert hasattr(Ant_Javac, "destdir")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_ant_javac_has_deprecation():
    assert hasattr(Ant_Javac, "deprecation")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "deprecation" in klass.__dict__:
            descriptor = klass.__dict__["deprecation"]
            break
    assert isinstance(descriptor, property)

def test_ant_javac_has_srcdir():
    assert hasattr(Ant_Javac, "srcdir")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "srcdir" in klass.__dict__:
            descriptor = klass.__dict__["srcdir"]
            break
    assert isinstance(descriptor, property)

def test_ant_javac_has_debug():
    assert hasattr(Ant_Javac, "debug")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_ant_javac_has_optimize():
    assert hasattr(Ant_Javac, "optimize")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "optimize" in klass.__dict__:
            descriptor = klass.__dict__["optimize"]
            break
    assert isinstance(descriptor, property)

def test_ant_javac_has_fork():
    assert hasattr(Ant_Javac, "fork")
    descriptor = None
    for klass in Ant_Javac.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)



def test_ant_taskdef_is_not_abstract():
    assert not inspect.isabstract(Ant_TaskDef)


def test_ant_taskdef_constructor_exists():
    assert callable(Ant_TaskDef.__init__)


def test_ant_taskdef_constructor_args():
    sig = inspect.signature(Ant_TaskDef.__init__)
    params = list(sig.parameters.keys())
    assert "classname" in params, "Missing parameter 'classname'"
    assert "name" in params, "Missing parameter 'name'"

def test_ant_taskdef_has_classname():
    assert hasattr(Ant_TaskDef, "classname")
    descriptor = None
    for klass in Ant_TaskDef.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_ant_taskdef_has_name():
    assert hasattr(Ant_TaskDef, "name")
    descriptor = None
    for klass in Ant_TaskDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ant_formattstamp_is_not_abstract():
    assert not inspect.isabstract(Ant_FormatTstamp)


def test_ant_formattstamp_constructor_exists():
    assert callable(Ant_FormatTstamp.__init__)


def test_ant_formattstamp_constructor_args():
    sig = inspect.signature(Ant_FormatTstamp.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "property" in params, "Missing parameter 'property'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "offset" in params, "Missing parameter 'offset'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_ant_formattstamp_has_pattern():
    assert hasattr(Ant_FormatTstamp, "pattern")
    descriptor = None
    for klass in Ant_FormatTstamp.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_ant_formattstamp_has_property():
    assert hasattr(Ant_FormatTstamp, "property")
    descriptor = None
    for klass in Ant_FormatTstamp.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)

def test_ant_formattstamp_has_locale():
    assert hasattr(Ant_FormatTstamp, "locale")
    descriptor = None
    for klass in Ant_FormatTstamp.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_ant_formattstamp_has_offset():
    assert hasattr(Ant_FormatTstamp, "offset")
    descriptor = None
    for klass in Ant_FormatTstamp.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_ant_formattstamp_has_unit():
    assert hasattr(Ant_FormatTstamp, "unit")
    descriptor = None
    for klass in Ant_FormatTstamp.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_ant_task_is_not_abstract():
    assert not inspect.isabstract(Ant_Task)


def test_ant_task_constructor_exists():
    assert callable(Ant_Task.__init__)


def test_ant_task_constructor_args():
    sig = inspect.signature(Ant_Task.__init__)
    params = list(sig.parameters.keys())



def test_formattstamp_is_not_abstract():
    assert not inspect.isabstract(FormatTstamp)


def test_formattstamp_constructor_exists():
    assert callable(FormatTstamp.__init__)


def test_formattstamp_constructor_args():
    sig = inspect.signature(FormatTstamp.__init__)
    params = list(sig.parameters.keys())



def test_miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(MiscellaneousTask)


def test_miscellaneoustask_constructor_exists():
    assert callable(MiscellaneousTask.__init__)


def test_miscellaneoustask_constructor_args():
    sig = inspect.signature(MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_tstamp_is_not_abstract():
    assert not inspect.isabstract(Ant_Tstamp)


def test_ant_tstamp_constructor_exists():
    assert callable(Ant_Tstamp.__init__)


def test_ant_tstamp_constructor_args():
    sig = inspect.signature(Ant_Tstamp.__init__)
    params = list(sig.parameters.keys())



def test_ant_echo_is_not_abstract():
    assert not inspect.isabstract(Ant_Echo)


def test_ant_echo_constructor_exists():
    assert callable(Ant_Echo.__init__)


def test_ant_echo_constructor_args():
    sig = inspect.signature(Ant_Echo.__init__)
    params = list(sig.parameters.keys())
    assert "append" in params, "Missing parameter 'append'"
    assert "file" in params, "Missing parameter 'file'"
    assert "message" in params, "Missing parameter 'message'"

def test_ant_echo_has_append():
    assert hasattr(Ant_Echo, "append")
    descriptor = None
    for klass in Ant_Echo.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_ant_echo_has_file():
    assert hasattr(Ant_Echo, "file")
    descriptor = None
    for klass in Ant_Echo.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant_echo_has_message():
    assert hasattr(Ant_Echo, "message")
    descriptor = None
    for klass in Ant_Echo.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_classpath_is_not_abstract():
    assert not inspect.isabstract(ClassPath)


def test_classpath_constructor_exists():
    assert callable(ClassPath.__init__)


def test_classpath_constructor_args():
    sig = inspect.signature(ClassPath.__init__)
    params = list(sig.parameters.keys())



def test_fileset_is_not_abstract():
    assert not inspect.isabstract(FileSet)


def test_fileset_constructor_exists():
    assert callable(FileSet.__init__)


def test_fileset_constructor_args():
    sig = inspect.signature(FileSet.__init__)
    params = list(sig.parameters.keys())



def test_pathelement_is_not_abstract():
    assert not inspect.isabstract(PathElement)


def test_pathelement_constructor_exists():
    assert callable(PathElement.__init__)


def test_pathelement_constructor_args():
    sig = inspect.signature(PathElement.__init__)
    params = list(sig.parameters.keys())



def test_ant_java_is_not_abstract():
    assert not inspect.isabstract(Ant_Java)


def test_ant_java_constructor_exists():
    assert callable(Ant_Java.__init__)


def test_ant_java_constructor_args():
    sig = inspect.signature(Ant_Java.__init__)
    params = list(sig.parameters.keys())
    assert "classname" in params, "Missing parameter 'classname'"
    assert "fork" in params, "Missing parameter 'fork'"
    assert "jar" in params, "Missing parameter 'jar'"

def test_ant_java_has_classname():
    assert hasattr(Ant_Java, "classname")
    descriptor = None
    for klass in Ant_Java.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_ant_java_has_fork():
    assert hasattr(Ant_Java, "fork")
    descriptor = None
    for klass in Ant_Java.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)

def test_ant_java_has_jar():
    assert hasattr(Ant_Java, "jar")
    descriptor = None
    for klass in Ant_Java.__mro__:
        if "jar" in klass.__dict__:
            descriptor = klass.__dict__["jar"]
            break
    assert isinstance(descriptor, property)



def test_ant_exec_is_not_abstract():
    assert not inspect.isabstract(Ant_Exec)


def test_ant_exec_constructor_exists():
    assert callable(Ant_Exec.__init__)


def test_ant_exec_constructor_args():
    sig = inspect.signature(Ant_Exec.__init__)
    params = list(sig.parameters.keys())
    assert "executable" in params, "Missing parameter 'executable'"
    assert "dir" in params, "Missing parameter 'dir'"

def test_ant_exec_has_executable():
    assert hasattr(Ant_Exec, "executable")
    descriptor = None
    for klass in Ant_Exec.__mro__:
        if "executable" in klass.__dict__:
            descriptor = klass.__dict__["executable"]
            break
    assert isinstance(descriptor, property)

def test_ant_exec_has_dir():
    assert hasattr(Ant_Exec, "dir")
    descriptor = None
    for klass in Ant_Exec.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtask_is_not_abstract():
    assert not inspect.isabstract(PreDefinedTask)


def test_predefinedtask_constructor_exists():
    assert callable(PreDefinedTask.__init__)


def test_predefinedtask_constructor_args():
    sig = inspect.signature(PreDefinedTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_filetask_is_not_abstract():
    assert not inspect.isabstract(Ant_FileTask)


def test_ant_filetask_constructor_exists():
    assert callable(Ant_FileTask.__init__)


def test_ant_filetask_constructor_args():
    sig = inspect.signature(Ant_FileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_compiletask_is_not_abstract():
    assert not inspect.isabstract(Ant_CompileTask)


def test_ant_compiletask_constructor_exists():
    assert callable(Ant_CompileTask.__init__)


def test_ant_compiletask_constructor_args():
    sig = inspect.signature(Ant_CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(Ant_MiscellaneousTask)


def test_ant_miscellaneoustask_constructor_exists():
    assert callable(Ant_MiscellaneousTask.__init__)


def test_ant_miscellaneoustask_constructor_args():
    sig = inspect.signature(Ant_MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_documentationtask_is_not_abstract():
    assert not inspect.isabstract(Ant_DocumentationTask)


def test_ant_documentationtask_constructor_exists():
    assert callable(Ant_DocumentationTask.__init__)


def test_ant_documentationtask_constructor_args():
    sig = inspect.signature(Ant_DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_archivetask_is_not_abstract():
    assert not inspect.isabstract(Ant_ArchiveTask)


def test_ant_archivetask_constructor_exists():
    assert callable(Ant_ArchiveTask.__init__)


def test_ant_archivetask_constructor_args():
    sig = inspect.signature(Ant_ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_executiontask_is_not_abstract():
    assert not inspect.isabstract(Ant_ExecutionTask)


def test_ant_executiontask_constructor_exists():
    assert callable(Ant_ExecutionTask.__init__)


def test_ant_executiontask_constructor_args():
    sig = inspect.signature(Ant_ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_attribut_is_not_abstract():
    assert not inspect.isabstract(Ant_Attribut)


def test_ant_attribut_constructor_exists():
    assert callable(Ant_Attribut.__init__)


def test_ant_attribut_constructor_args():
    sig = inspect.signature(Ant_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_ant_attribut_has_value():
    assert hasattr(Ant_Attribut, "value")
    descriptor = None
    for klass in Ant_Attribut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ant_attribut_has_name():
    assert hasattr(Ant_Attribut, "name")
    descriptor = None
    for klass in Ant_Attribut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_attribut_is_not_abstract():
    assert not inspect.isabstract(Attribut)


def test_attribut_constructor_exists():
    assert callable(Attribut.__init__)


def test_attribut_constructor_args():
    sig = inspect.signature(Attribut.__init__)
    params = list(sig.parameters.keys())



def test_set_is_not_abstract():
    assert not inspect.isabstract(Set)


def test_set_constructor_exists():
    assert callable(Set.__init__)


def test_set_constructor_args():
    sig = inspect.signature(Set.__init__)
    params = list(sig.parameters.keys())



def test_ant_classpath_is_not_abstract():
    assert not inspect.isabstract(Ant_ClassPath)


def test_ant_classpath_constructor_exists():
    assert callable(Ant_ClassPath.__init__)


def test_ant_classpath_constructor_args():
    sig = inspect.signature(Ant_ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"

def test_ant_classpath_has_refid():
    assert hasattr(Ant_ClassPath, "refid")
    descriptor = None
    for klass in Ant_ClassPath.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)



def test_ant_fileset_is_not_abstract():
    assert not inspect.isabstract(Ant_FileSet)


def test_ant_fileset_constructor_exists():
    assert callable(Ant_FileSet.__init__)


def test_ant_fileset_constructor_args():
    sig = inspect.signature(Ant_FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_ant_fileset_has_dir():
    assert hasattr(Ant_FileSet, "dir")
    descriptor = None
    for klass in Ant_FileSet.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_ant_patternset_is_not_abstract():
    assert not inspect.isabstract(Ant_PatternSet)


def test_ant_patternset_constructor_exists():
    assert callable(Ant_PatternSet.__init__)


def test_ant_patternset_constructor_args():
    sig = inspect.signature(Ant_PatternSet.__init__)
    params = list(sig.parameters.keys())



def test_ant_path_is_not_abstract():
    assert not inspect.isabstract(Ant_Path)


def test_ant_path_constructor_exists():
    assert callable(Ant_Path.__init__)


def test_ant_path_constructor_args():
    sig = inspect.signature(Ant_Path.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"
    assert "id" in params, "Missing parameter 'id'"

def test_ant_path_has_refid():
    assert hasattr(Ant_Path, "refid")
    descriptor = None
    for klass in Ant_Path.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)

def test_ant_path_has_id():
    assert hasattr(Ant_Path, "id")
    descriptor = None
    for klass in Ant_Path.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_filtersfile_is_not_abstract():
    assert not inspect.isabstract(FiltersFile)


def test_filtersfile_constructor_exists():
    assert callable(FiltersFile.__init__)


def test_filtersfile_constructor_args():
    sig = inspect.signature(FiltersFile.__init__)
    params = list(sig.parameters.keys())



def test_filter_is_not_abstract():
    assert not inspect.isabstract(Filter)


def test_filter_constructor_exists():
    assert callable(Filter.__init__)


def test_filter_constructor_args():
    sig = inspect.signature(Filter.__init__)
    params = list(sig.parameters.keys())



def test_ant_filterset_is_not_abstract():
    assert not inspect.isabstract(Ant_FilterSet)


def test_ant_filterset_constructor_exists():
    assert callable(Ant_FilterSet.__init__)


def test_ant_filterset_constructor_args():
    sig = inspect.signature(Ant_FilterSet.__init__)
    params = list(sig.parameters.keys())
    assert "endtoken" in params, "Missing parameter 'endtoken'"
    assert "starttoken" in params, "Missing parameter 'starttoken'"

def test_ant_filterset_has_endtoken():
    assert hasattr(Ant_FilterSet, "endtoken")
    descriptor = None
    for klass in Ant_FilterSet.__mro__:
        if "endtoken" in klass.__dict__:
            descriptor = klass.__dict__["endtoken"]
            break
    assert isinstance(descriptor, property)

def test_ant_filterset_has_starttoken():
    assert hasattr(Ant_FilterSet, "starttoken")
    descriptor = None
    for klass in Ant_FilterSet.__mro__:
        if "starttoken" in klass.__dict__:
            descriptor = klass.__dict__["starttoken"]
            break
    assert isinstance(descriptor, property)



def test_excludes_is_not_abstract():
    assert not inspect.isabstract(Excludes)


def test_excludes_constructor_exists():
    assert callable(Excludes.__init__)


def test_excludes_constructor_args():
    sig = inspect.signature(Excludes.__init__)
    params = list(sig.parameters.keys())



def test_includes_is_not_abstract():
    assert not inspect.isabstract(Includes)


def test_includes_constructor_exists():
    assert callable(Includes.__init__)


def test_includes_constructor_args():
    sig = inspect.signature(Includes.__init__)
    params = list(sig.parameters.keys())



def test_patternset_is_not_abstract():
    assert not inspect.isabstract(PatternSet)


def test_patternset_constructor_exists():
    assert callable(PatternSet.__init__)


def test_patternset_constructor_args():
    sig = inspect.signature(PatternSet.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_ant_predefinedtask_is_not_abstract():
    assert not inspect.isabstract(Ant_PreDefinedTask)


def test_ant_predefinedtask_constructor_exists():
    assert callable(Ant_PreDefinedTask.__init__)


def test_ant_predefinedtask_constructor_args():
    sig = inspect.signature(Ant_PreDefinedTask.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "taskname" in params, "Missing parameter 'taskname'"
    assert "id" in params, "Missing parameter 'id'"

def test_ant_predefinedtask_has_description():
    assert hasattr(Ant_PreDefinedTask, "description")
    descriptor = None
    for klass in Ant_PreDefinedTask.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ant_predefinedtask_has_taskname():
    assert hasattr(Ant_PreDefinedTask, "taskname")
    descriptor = None
    for klass in Ant_PreDefinedTask.__mro__:
        if "taskname" in klass.__dict__:
            descriptor = klass.__dict__["taskname"]
            break
    assert isinstance(descriptor, property)

def test_ant_predefinedtask_has_id():
    assert hasattr(Ant_PreDefinedTask, "id")
    descriptor = None
    for klass in Ant_PreDefinedTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ant_newtask_is_not_abstract():
    assert not inspect.isabstract(Ant_NewTask)


def test_ant_newtask_constructor_exists():
    assert callable(Ant_NewTask.__init__)


def test_ant_newtask_constructor_args():
    sig = inspect.signature(Ant_NewTask.__init__)
    params = list(sig.parameters.keys())



def test_ant_target_is_not_abstract():
    assert not inspect.isabstract(Ant_Target)


def test_ant_target_constructor_exists():
    assert callable(Ant_Target.__init__)


def test_ant_target_constructor_args():
    sig = inspect.signature(Ant_Target.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unless" in params, "Missing parameter 'unless'"
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"
    assert "description" in params, "Missing parameter 'description'"

def test_ant_target_has_name():
    assert hasattr(Ant_Target, "name")
    descriptor = None
    for klass in Ant_Target.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant_target_has_unless():
    assert hasattr(Ant_Target, "unless")
    descriptor = None
    for klass in Ant_Target.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
            break
    assert isinstance(descriptor, property)

def test_ant_target_has_ifCondition():
    assert hasattr(Ant_Target, "ifCondition")
    descriptor = None
    for klass in Ant_Target.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)

def test_ant_target_has_description():
    assert hasattr(Ant_Target, "description")
    descriptor = None
    for klass in Ant_Target.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_inexcludes_is_not_abstract():
    assert not inspect.isabstract(InExcludes)


def test_inexcludes_constructor_exists():
    assert callable(InExcludes.__init__)


def test_inexcludes_constructor_args():
    sig = inspect.signature(InExcludes.__init__)
    params = list(sig.parameters.keys())



def test_ant_excludes_is_not_abstract():
    assert not inspect.isabstract(Ant_Excludes)


def test_ant_excludes_constructor_exists():
    assert callable(Ant_Excludes.__init__)


def test_ant_excludes_constructor_args():
    sig = inspect.signature(Ant_Excludes.__init__)
    params = list(sig.parameters.keys())



def test_ant_includesfile_is_not_abstract():
    assert not inspect.isabstract(Ant_IncludesFile)


def test_ant_includesfile_constructor_exists():
    assert callable(Ant_IncludesFile.__init__)


def test_ant_includesfile_constructor_args():
    sig = inspect.signature(Ant_IncludesFile.__init__)
    params = list(sig.parameters.keys())



def test_ant_excludesfile_is_not_abstract():
    assert not inspect.isabstract(Ant_ExcludesFile)


def test_ant_excludesfile_constructor_exists():
    assert callable(Ant_ExcludesFile.__init__)


def test_ant_excludesfile_constructor_args():
    sig = inspect.signature(Ant_ExcludesFile.__init__)
    params = list(sig.parameters.keys())



def test_ant_includes_is_not_abstract():
    assert not inspect.isabstract(Ant_Includes)


def test_ant_includes_constructor_exists():
    assert callable(Ant_Includes.__init__)


def test_ant_includes_constructor_args():
    sig = inspect.signature(Ant_Includes.__init__)
    params = list(sig.parameters.keys())



def test_basic_is_not_abstract():
    assert not inspect.isabstract(Basic)


def test_basic_constructor_exists():
    assert callable(Basic.__init__)


def test_basic_constructor_args():
    sig = inspect.signature(Basic.__init__)
    params = list(sig.parameters.keys())



def test_ant_inexcludes_is_not_abstract():
    assert not inspect.isabstract(Ant_InExcludes)


def test_ant_inexcludes_constructor_exists():
    assert callable(Ant_InExcludes.__init__)


def test_ant_inexcludes_constructor_args():
    sig = inspect.signature(Ant_InExcludes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unless" in params, "Missing parameter 'unless'"
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"

def test_ant_inexcludes_has_name():
    assert hasattr(Ant_InExcludes, "name")
    descriptor = None
    for klass in Ant_InExcludes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant_inexcludes_has_unless():
    assert hasattr(Ant_InExcludes, "unless")
    descriptor = None
    for klass in Ant_InExcludes.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
            break
    assert isinstance(descriptor, property)

def test_ant_inexcludes_has_ifCondition():
    assert hasattr(Ant_InExcludes, "ifCondition")
    descriptor = None
    for klass in Ant_InExcludes.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)



def test_ant_filtersfile_is_not_abstract():
    assert not inspect.isabstract(Ant_FiltersFile)


def test_ant_filtersfile_constructor_exists():
    assert callable(Ant_FiltersFile.__init__)


def test_ant_filtersfile_constructor_args():
    sig = inspect.signature(Ant_FiltersFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_ant_filtersfile_has_file():
    assert hasattr(Ant_FiltersFile, "file")
    descriptor = None
    for klass in Ant_FiltersFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_ant_pathelement_is_not_abstract():
    assert not inspect.isabstract(Ant_PathElement)


def test_ant_pathelement_constructor_exists():
    assert callable(Ant_PathElement.__init__)


def test_ant_pathelement_constructor_args():
    sig = inspect.signature(Ant_PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "path" in params, "Missing parameter 'path'"

def test_ant_pathelement_has_location():
    assert hasattr(Ant_PathElement, "location")
    descriptor = None
    for klass in Ant_PathElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ant_pathelement_has_path():
    assert hasattr(Ant_PathElement, "path")
    descriptor = None
    for klass in Ant_PathElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_ant_filter_is_not_abstract():
    assert not inspect.isabstract(Ant_Filter)


def test_ant_filter_constructor_exists():
    assert callable(Ant_Filter.__init__)


def test_ant_filter_constructor_args():
    sig = inspect.signature(Ant_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "value" in params, "Missing parameter 'value'"

def test_ant_filter_has_token():
    assert hasattr(Ant_Filter, "token")
    descriptor = None
    for klass in Ant_Filter.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_ant_filter_has_value():
    assert hasattr(Ant_Filter, "value")
    descriptor = None
    for klass in Ant_Filter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ant_filelist_is_not_abstract():
    assert not inspect.isabstract(Ant_FileList)


def test_ant_filelist_constructor_exists():
    assert callable(Ant_FileList.__init__)


def test_ant_filelist_constructor_args():
    sig = inspect.signature(Ant_FileList.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "files" in params, "Missing parameter 'files'"

def test_ant_filelist_has_dir():
    assert hasattr(Ant_FileList, "dir")
    descriptor = None
    for klass in Ant_FileList.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_ant_filelist_has_files():
    assert hasattr(Ant_FileList, "files")
    descriptor = None
    for klass in Ant_FileList.__mro__:
        if "files" in klass.__dict__:
            descriptor = klass.__dict__["files"]
            break
    assert isinstance(descriptor, property)



def test_ant_mapper_is_not_abstract():
    assert not inspect.isabstract(Ant_Mapper)


def test_ant_mapper_constructor_exists():
    assert callable(Ant_Mapper.__init__)


def test_ant_mapper_constructor_args():
    sig = inspect.signature(Ant_Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "classpathref" in params, "Missing parameter 'classpathref'"
    assert "classpath" in params, "Missing parameter 'classpath'"
    assert "type" in params, "Missing parameter 'type'"
    assert "to" in params, "Missing parameter 'to'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "from_" in params, "Missing parameter 'from_'"

def test_ant_mapper_has_classpathref():
    assert hasattr(Ant_Mapper, "classpathref")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "classpathref" in klass.__dict__:
            descriptor = klass.__dict__["classpathref"]
            break
    assert isinstance(descriptor, property)

def test_ant_mapper_has_classpath():
    assert hasattr(Ant_Mapper, "classpath")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "classpath" in klass.__dict__:
            descriptor = klass.__dict__["classpath"]
            break
    assert isinstance(descriptor, property)

def test_ant_mapper_has_type():
    assert hasattr(Ant_Mapper, "type")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_ant_mapper_has_to():
    assert hasattr(Ant_Mapper, "to")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_ant_mapper_has_classname():
    assert hasattr(Ant_Mapper, "classname")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_ant_mapper_has_from_():
    assert hasattr(Ant_Mapper, "from_")
    descriptor = None
    for klass in Ant_Mapper.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_ant_set_is_not_abstract():
    assert not inspect.isabstract(Ant_Set)


def test_ant_set_constructor_exists():
    assert callable(Ant_Set.__init__)


def test_ant_set_constructor_args():
    sig = inspect.signature(Ant_Set.__init__)
    params = list(sig.parameters.keys())



def test_ant_basic_is_not_abstract():
    assert not inspect.isabstract(Ant_Basic)


def test_ant_basic_constructor_exists():
    assert callable(Ant_Basic.__init__)


def test_ant_basic_constructor_args():
    sig = inspect.signature(Ant_Basic.__init__)
    params = list(sig.parameters.keys())



def test_ant_pattern_is_not_abstract():
    assert not inspect.isabstract(Ant_Pattern)


def test_ant_pattern_constructor_exists():
    assert callable(Ant_Pattern.__init__)


def test_ant_pattern_constructor_args():
    sig = inspect.signature(Ant_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_ant_project_is_not_abstract():
    assert not inspect.isabstract(Ant_Project)


def test_ant_project_constructor_exists():
    assert callable(Ant_Project.__init__)


def test_ant_project_constructor_args():
    sig = inspect.signature(Ant_Project.__init__)
    params = list(sig.parameters.keys())
    assert "basedir" in params, "Missing parameter 'basedir'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_ant_project_has_basedir():
    assert hasattr(Ant_Project, "basedir")
    descriptor = None
    for klass in Ant_Project.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)

def test_ant_project_has_name():
    assert hasattr(Ant_Project, "name")
    descriptor = None
    for klass in Ant_Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant_project_has_description():
    assert hasattr(Ant_Project, "description")
    descriptor = None
    for klass in Ant_Project.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_propertyname_is_not_abstract():
    assert not inspect.isabstract(PropertyName)


def test_propertyname_constructor_exists():
    assert callable(PropertyName.__init__)


def test_propertyname_constructor_args():
    sig = inspect.signature(PropertyName.__init__)
    params = list(sig.parameters.keys())



def test_ant_propertylocation_is_not_abstract():
    assert not inspect.isabstract(Ant_PropertyLocation)


def test_ant_propertylocation_constructor_exists():
    assert callable(Ant_PropertyLocation.__init__)


def test_ant_propertylocation_constructor_args():
    sig = inspect.signature(Ant_PropertyLocation.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_ant_propertylocation_has_location():
    assert hasattr(Ant_PropertyLocation, "location")
    descriptor = None
    for klass in Ant_PropertyLocation.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_ant_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(Ant_PropertyValue)


def test_ant_propertyvalue_constructor_exists():
    assert callable(Ant_PropertyValue.__init__)


def test_ant_propertyvalue_constructor_args():
    sig = inspect.signature(Ant_PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ant_propertyvalue_has_value():
    assert hasattr(Ant_PropertyValue, "value")
    descriptor = None
    for klass in Ant_PropertyValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ant_property_is_not_abstract():
    assert not inspect.isabstract(Ant_Property)


def test_ant_property_constructor_exists():
    assert callable(Ant_Property.__init__)


def test_ant_property_constructor_args():
    sig = inspect.signature(Ant_Property.__init__)
    params = list(sig.parameters.keys())



def test_taskdef_is_not_abstract():
    assert not inspect.isabstract(TaskDef)


def test_taskdef_constructor_exists():
    assert callable(TaskDef.__init__)


def test_taskdef_constructor_args():
    sig = inspect.signature(TaskDef.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_ant_propertyenv_is_not_abstract():
    assert not inspect.isabstract(Ant_PropertyEnv)


def test_ant_propertyenv_constructor_exists():
    assert callable(Ant_PropertyEnv.__init__)


def test_ant_propertyenv_constructor_args():
    sig = inspect.signature(Ant_PropertyEnv.__init__)
    params = list(sig.parameters.keys())
    assert "environment" in params, "Missing parameter 'environment'"

def test_ant_propertyenv_has_environment():
    assert hasattr(Ant_PropertyEnv, "environment")
    descriptor = None
    for klass in Ant_PropertyEnv.__mro__:
        if "environment" in klass.__dict__:
            descriptor = klass.__dict__["environment"]
            break
    assert isinstance(descriptor, property)



def test_ant_propertyfile_is_not_abstract():
    assert not inspect.isabstract(Ant_PropertyFile)


def test_ant_propertyfile_constructor_exists():
    assert callable(Ant_PropertyFile.__init__)


def test_ant_propertyfile_constructor_args():
    sig = inspect.signature(Ant_PropertyFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_ant_propertyfile_has_file():
    assert hasattr(Ant_PropertyFile, "file")
    descriptor = None
    for klass in Ant_PropertyFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_ant_propertyname_is_not_abstract():
    assert not inspect.isabstract(Ant_PropertyName)


def test_ant_propertyname_constructor_exists():
    assert callable(Ant_PropertyName.__init__)


def test_ant_propertyname_constructor_args():
    sig = inspect.signature(Ant_PropertyName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ant_propertyname_has_name():
    assert hasattr(Ant_PropertyName, "name")
    descriptor = None
    for klass in Ant_PropertyName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_path_is_not_abstract():
    assert not inspect.isabstract(Path)


def test_path_constructor_exists():
    assert callable(Path.__init__)


def test_path_constructor_args():
    sig = inspect.signature(Path.__init__)
    params = list(sig.parameters.keys())



def test_target_is_not_abstract():
    assert not inspect.isabstract(Target)


def test_target_constructor_exists():
    assert callable(Target.__init__)


def test_target_constructor_args():
    sig = inspect.signature(Target.__init__)
    params = list(sig.parameters.keys())


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Mapper_strategy = st.builds(
    Mapper,
)
FilterSet_strategy = st.builds(
    FilterSet,
)
FileTask_strategy = st.builds(
    FileTask,
)
Ant_Delete_strategy = st.builds(
    Ant_Delete,
    verbose=
        safe_text,
    dir=
        safe_text,
    defaultexcludes=
        safe_text,
    file=
        safe_text,
    excludes=
        safe_text,
    includeEmptyDirs=
        safe_text,
    includes=
        safe_text,
    includesfile=
        safe_text,
    excludesfile=
        safe_text,
    failonerror=
        safe_text,
    quiet=
        safe_text
)
Ant_Mkdir_strategy = st.builds(
    Ant_Mkdir,
    dir=
        safe_text
)
ArchiveTask_strategy = st.builds(
    ArchiveTask,
)
Ant_Jar_strategy = st.builds(
    Ant_Jar,
    manifest=
        safe_text,
    encoding=
        safe_text,
    jarfile=
        safe_text,
    compress=
        safe_text,
    basedir=
        safe_text
)
DocumentationTask_strategy = st.builds(
    DocumentationTask,
)
Ant_Javadoc_strategy = st.builds(
    Ant_Javadoc,
    packagenames=
        safe_text,
    author=
        safe_text,
    windowtitle=
        safe_text,
    defaultexcludes=
        safe_text,
    sourcepath=
        safe_text,
    use=
        safe_text,
    destdir=
        safe_text,
    version=
        safe_text
)
CompileTask_strategy = st.builds(
    CompileTask,
)
Ant_Copy_strategy = st.builds(
    Ant_Copy,
    filtering=
        safe_text,
    overwrite=
        safe_text,
    file=
        safe_text,
    todir=
        safe_text,
    flatten=
        safe_text,
    tofile=
        safe_text,
    presservelastmodified=
        safe_text,
    includeEmptyDirs=
        safe_text
)
Ant_Javac_strategy = st.builds(
    Ant_Javac,
    destdir=
        safe_text,
    deprecation=
        safe_text,
    srcdir=
        safe_text,
    debug=
        safe_text,
    optimize=
        safe_text,
    fork=
        safe_text
)
Ant_TaskDef_strategy = st.builds(
    Ant_TaskDef,
    classname=
        safe_text,
    name=
        safe_text
)
Ant_FormatTstamp_strategy = st.builds(
    Ant_FormatTstamp,
    pattern=
        safe_text,
    property=
        safe_text,
    locale=
        safe_text,
    offset=
        safe_text,
    unit=
        safe_text
)
Ant_Task_strategy = st.builds(
    Ant_Task,
)
FormatTstamp_strategy = st.builds(
    FormatTstamp,
)
MiscellaneousTask_strategy = st.builds(
    MiscellaneousTask,
)
Ant_Tstamp_strategy = st.builds(
    Ant_Tstamp,
)
Ant_Echo_strategy = st.builds(
    Ant_Echo,
    append=
        safe_text,
    file=
        safe_text,
    message=
        safe_text
)
ClassPath_strategy = st.builds(
    ClassPath,
)
FileSet_strategy = st.builds(
    FileSet,
)
PathElement_strategy = st.builds(
    PathElement,
)
Ant_Java_strategy = st.builds(
    Ant_Java,
    classname=
        safe_text,
    fork=
        safe_text,
    jar=
        safe_text
)
Ant_Exec_strategy = st.builds(
    Ant_Exec,
    executable=
        safe_text,
    dir=
        safe_text
)
PreDefinedTask_strategy = st.builds(
    PreDefinedTask,
)
Ant_FileTask_strategy = st.builds(
    Ant_FileTask,
)
Ant_CompileTask_strategy = st.builds(
    Ant_CompileTask,
)
Ant_MiscellaneousTask_strategy = st.builds(
    Ant_MiscellaneousTask,
)
Ant_DocumentationTask_strategy = st.builds(
    Ant_DocumentationTask,
)
Ant_ArchiveTask_strategy = st.builds(
    Ant_ArchiveTask,
)
Ant_ExecutionTask_strategy = st.builds(
    Ant_ExecutionTask,
)
Ant_Attribut_strategy = st.builds(
    Ant_Attribut,
    value=
        safe_text,
    name=
        safe_text
)
Attribut_strategy = st.builds(
    Attribut,
)
Set_strategy = st.builds(
    Set,
)
Ant_ClassPath_strategy = st.builds(
    Ant_ClassPath,
    refid=
        safe_text
)
Ant_FileSet_strategy = st.builds(
    Ant_FileSet,
    dir=
        safe_text
)
Ant_PatternSet_strategy = st.builds(
    Ant_PatternSet,
)
Ant_Path_strategy = st.builds(
    Ant_Path,
    refid=
        safe_text,
    id=
        safe_text
)
FiltersFile_strategy = st.builds(
    FiltersFile,
)
Filter_strategy = st.builds(
    Filter,
)
Ant_FilterSet_strategy = st.builds(
    Ant_FilterSet,
    endtoken=
        safe_text,
    starttoken=
        safe_text
)
Excludes_strategy = st.builds(
    Excludes,
)
Includes_strategy = st.builds(
    Includes,
)
PatternSet_strategy = st.builds(
    PatternSet,
)
Task_strategy = st.builds(
    Task,
)
Ant_PreDefinedTask_strategy = st.builds(
    Ant_PreDefinedTask,
    description=
        safe_text,
    taskname=
        safe_text,
    id=
        safe_text
)
Ant_NewTask_strategy = st.builds(
    Ant_NewTask,
)
Ant_Target_strategy = st.builds(
    Ant_Target,
    name=
        safe_text,
    unless=
        safe_text,
    ifCondition=
        safe_text,
    description=
        safe_text
)
InExcludes_strategy = st.builds(
    InExcludes,
)
Ant_Excludes_strategy = st.builds(
    Ant_Excludes,
)
Ant_IncludesFile_strategy = st.builds(
    Ant_IncludesFile,
)
Ant_ExcludesFile_strategy = st.builds(
    Ant_ExcludesFile,
)
Ant_Includes_strategy = st.builds(
    Ant_Includes,
)
Basic_strategy = st.builds(
    Basic,
)
Ant_InExcludes_strategy = st.builds(
    Ant_InExcludes,
    name=
        safe_text,
    unless=
        safe_text,
    ifCondition=
        safe_text
)
Ant_FiltersFile_strategy = st.builds(
    Ant_FiltersFile,
    file=
        safe_text
)
Ant_PathElement_strategy = st.builds(
    Ant_PathElement,
    location=
        safe_text,
    path=
        safe_text
)
Ant_Filter_strategy = st.builds(
    Ant_Filter,
    token=
        safe_text,
    value=
        safe_text
)
Ant_FileList_strategy = st.builds(
    Ant_FileList,
    dir=
        safe_text,
    files=
        safe_text
)
Ant_Mapper_strategy = st.builds(
    Ant_Mapper,
    classpathref=
        safe_text,
    classpath=
        safe_text,
    type=
        safe_text,
    to=
        safe_text,
    classname=
        safe_text,
    from_=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
Ant_Set_strategy = st.builds(
    Ant_Set,
)
Ant_Basic_strategy = st.builds(
    Ant_Basic,
)
Ant_Pattern_strategy = st.builds(
    Ant_Pattern,
)
Ant_Project_strategy = st.builds(
    Ant_Project,
    basedir=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
PropertyName_strategy = st.builds(
    PropertyName,
)
Ant_PropertyLocation_strategy = st.builds(
    Ant_PropertyLocation,
    location=
        safe_text
)
Ant_PropertyValue_strategy = st.builds(
    Ant_PropertyValue,
    value=
        safe_text
)
Ant_Property_strategy = st.builds(
    Ant_Property,
)
TaskDef_strategy = st.builds(
    TaskDef,
)
Property_strategy = st.builds(
    Property,
)
Ant_PropertyEnv_strategy = st.builds(
    Ant_PropertyEnv,
    environment=
        safe_text
)
Ant_PropertyFile_strategy = st.builds(
    Ant_PropertyFile,
    file=
        safe_text
)
Ant_PropertyName_strategy = st.builds(
    Ant_PropertyName,
    name=
        safe_text
)
Path_strategy = st.builds(
    Path,
)
Target_strategy = st.builds(
    Target,
)

@given(instance=Mapper_strategy)
@settings(max_examples=50)
def test_mapper_instantiation(instance):
    assert isinstance(instance, Mapper)

@given(instance=FilterSet_strategy)
@settings(max_examples=50)
def test_filterset_instantiation(instance):
    assert isinstance(instance, FilterSet)

@given(instance=FileTask_strategy)
@settings(max_examples=50)
def test_filetask_instantiation(instance):
    assert isinstance(instance, FileTask)

@given(instance=Ant_Delete_strategy)
@settings(max_examples=50)
def test_ant_delete_instantiation(instance):
    assert isinstance(instance, Ant_Delete)



@given(instance=Ant_Delete_strategy)
def test_ant_delete_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_includesfile_setter(instance):
    original = instance.includesfile
    instance.includesfile = original
    assert instance.includesfile == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_excludesfile_setter(instance):
    original = instance.excludesfile
    instance.excludesfile = original
    assert instance.excludesfile == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_failonerror_setter(instance):
    original = instance.failonerror
    instance.failonerror = original
    assert instance.failonerror == original



@given(instance=Ant_Delete_strategy)
def test_ant_delete_quiet_setter(instance):
    original = instance.quiet
    instance.quiet = original
    assert instance.quiet == original

@given(instance=Ant_Mkdir_strategy)
@settings(max_examples=50)
def test_ant_mkdir_instantiation(instance):
    assert isinstance(instance, Ant_Mkdir)



@given(instance=Ant_Mkdir_strategy)
def test_ant_mkdir_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=ArchiveTask_strategy)
@settings(max_examples=50)
def test_archivetask_instantiation(instance):
    assert isinstance(instance, ArchiveTask)

@given(instance=Ant_Jar_strategy)
@settings(max_examples=50)
def test_ant_jar_instantiation(instance):
    assert isinstance(instance, Ant_Jar)



@given(instance=Ant_Jar_strategy)
def test_ant_jar_manifest_setter(instance):
    original = instance.manifest
    instance.manifest = original
    assert instance.manifest == original



@given(instance=Ant_Jar_strategy)
def test_ant_jar_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original



@given(instance=Ant_Jar_strategy)
def test_ant_jar_jarfile_setter(instance):
    original = instance.jarfile
    instance.jarfile = original
    assert instance.jarfile == original



@given(instance=Ant_Jar_strategy)
def test_ant_jar_compress_setter(instance):
    original = instance.compress
    instance.compress = original
    assert instance.compress == original



@given(instance=Ant_Jar_strategy)
def test_ant_jar_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original

@given(instance=DocumentationTask_strategy)
@settings(max_examples=50)
def test_documentationtask_instantiation(instance):
    assert isinstance(instance, DocumentationTask)

@given(instance=Ant_Javadoc_strategy)
@settings(max_examples=50)
def test_ant_javadoc_instantiation(instance):
    assert isinstance(instance, Ant_Javadoc)



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_packagenames_setter(instance):
    original = instance.packagenames
    instance.packagenames = original
    assert instance.packagenames == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_windowtitle_setter(instance):
    original = instance.windowtitle
    instance.windowtitle = original
    assert instance.windowtitle == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_sourcepath_setter(instance):
    original = instance.sourcepath
    instance.sourcepath = original
    assert instance.sourcepath == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original



@given(instance=Ant_Javadoc_strategy)
def test_ant_javadoc_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=CompileTask_strategy)
@settings(max_examples=50)
def test_compiletask_instantiation(instance):
    assert isinstance(instance, CompileTask)

@given(instance=Ant_Copy_strategy)
@settings(max_examples=50)
def test_ant_copy_instantiation(instance):
    assert isinstance(instance, Ant_Copy)



@given(instance=Ant_Copy_strategy)
def test_ant_copy_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_overwrite_setter(instance):
    original = instance.overwrite
    instance.overwrite = original
    assert instance.overwrite == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_todir_setter(instance):
    original = instance.todir
    instance.todir = original
    assert instance.todir == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_flatten_setter(instance):
    original = instance.flatten
    instance.flatten = original
    assert instance.flatten == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_tofile_setter(instance):
    original = instance.tofile
    instance.tofile = original
    assert instance.tofile == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_presservelastmodified_setter(instance):
    original = instance.presservelastmodified
    instance.presservelastmodified = original
    assert instance.presservelastmodified == original



@given(instance=Ant_Copy_strategy)
def test_ant_copy_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original

@given(instance=Ant_Javac_strategy)
@settings(max_examples=50)
def test_ant_javac_instantiation(instance):
    assert isinstance(instance, Ant_Javac)



@given(instance=Ant_Javac_strategy)
def test_ant_javac_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original



@given(instance=Ant_Javac_strategy)
def test_ant_javac_deprecation_setter(instance):
    original = instance.deprecation
    instance.deprecation = original
    assert instance.deprecation == original



@given(instance=Ant_Javac_strategy)
def test_ant_javac_srcdir_setter(instance):
    original = instance.srcdir
    instance.srcdir = original
    assert instance.srcdir == original



@given(instance=Ant_Javac_strategy)
def test_ant_javac_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original



@given(instance=Ant_Javac_strategy)
def test_ant_javac_optimize_setter(instance):
    original = instance.optimize
    instance.optimize = original
    assert instance.optimize == original



@given(instance=Ant_Javac_strategy)
def test_ant_javac_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=Ant_TaskDef_strategy)
@settings(max_examples=50)
def test_ant_taskdef_instantiation(instance):
    assert isinstance(instance, Ant_TaskDef)



@given(instance=Ant_TaskDef_strategy)
def test_ant_taskdef_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=Ant_TaskDef_strategy)
def test_ant_taskdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant_FormatTstamp_strategy)
@settings(max_examples=50)
def test_ant_formattstamp_instantiation(instance):
    assert isinstance(instance, Ant_FormatTstamp)



@given(instance=Ant_FormatTstamp_strategy)
def test_ant_formattstamp_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=Ant_FormatTstamp_strategy)
def test_ant_formattstamp_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original



@given(instance=Ant_FormatTstamp_strategy)
def test_ant_formattstamp_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=Ant_FormatTstamp_strategy)
def test_ant_formattstamp_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=Ant_FormatTstamp_strategy)
def test_ant_formattstamp_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=Ant_Task_strategy)
@settings(max_examples=50)
def test_ant_task_instantiation(instance):
    assert isinstance(instance, Ant_Task)

@given(instance=FormatTstamp_strategy)
@settings(max_examples=50)
def test_formattstamp_instantiation(instance):
    assert isinstance(instance, FormatTstamp)

@given(instance=MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MiscellaneousTask)

@given(instance=Ant_Tstamp_strategy)
@settings(max_examples=50)
def test_ant_tstamp_instantiation(instance):
    assert isinstance(instance, Ant_Tstamp)

@given(instance=Ant_Echo_strategy)
@settings(max_examples=50)
def test_ant_echo_instantiation(instance):
    assert isinstance(instance, Ant_Echo)



@given(instance=Ant_Echo_strategy)
def test_ant_echo_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original



@given(instance=Ant_Echo_strategy)
def test_ant_echo_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=Ant_Echo_strategy)
def test_ant_echo_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=ClassPath_strategy)
@settings(max_examples=50)
def test_classpath_instantiation(instance):
    assert isinstance(instance, ClassPath)

@given(instance=FileSet_strategy)
@settings(max_examples=50)
def test_fileset_instantiation(instance):
    assert isinstance(instance, FileSet)

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=Ant_Java_strategy)
@settings(max_examples=50)
def test_ant_java_instantiation(instance):
    assert isinstance(instance, Ant_Java)



@given(instance=Ant_Java_strategy)
def test_ant_java_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=Ant_Java_strategy)
def test_ant_java_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original



@given(instance=Ant_Java_strategy)
def test_ant_java_jar_setter(instance):
    original = instance.jar
    instance.jar = original
    assert instance.jar == original

@given(instance=Ant_Exec_strategy)
@settings(max_examples=50)
def test_ant_exec_instantiation(instance):
    assert isinstance(instance, Ant_Exec)



@given(instance=Ant_Exec_strategy)
def test_ant_exec_executable_setter(instance):
    original = instance.executable
    instance.executable = original
    assert instance.executable == original



@given(instance=Ant_Exec_strategy)
def test_ant_exec_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=PreDefinedTask_strategy)
@settings(max_examples=50)
def test_predefinedtask_instantiation(instance):
    assert isinstance(instance, PreDefinedTask)

@given(instance=Ant_FileTask_strategy)
@settings(max_examples=50)
def test_ant_filetask_instantiation(instance):
    assert isinstance(instance, Ant_FileTask)

@given(instance=Ant_CompileTask_strategy)
@settings(max_examples=50)
def test_ant_compiletask_instantiation(instance):
    assert isinstance(instance, Ant_CompileTask)

@given(instance=Ant_MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_ant_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, Ant_MiscellaneousTask)

@given(instance=Ant_DocumentationTask_strategy)
@settings(max_examples=50)
def test_ant_documentationtask_instantiation(instance):
    assert isinstance(instance, Ant_DocumentationTask)

@given(instance=Ant_ArchiveTask_strategy)
@settings(max_examples=50)
def test_ant_archivetask_instantiation(instance):
    assert isinstance(instance, Ant_ArchiveTask)

@given(instance=Ant_ExecutionTask_strategy)
@settings(max_examples=50)
def test_ant_executiontask_instantiation(instance):
    assert isinstance(instance, Ant_ExecutionTask)

@given(instance=Ant_Attribut_strategy)
@settings(max_examples=50)
def test_ant_attribut_instantiation(instance):
    assert isinstance(instance, Ant_Attribut)



@given(instance=Ant_Attribut_strategy)
def test_ant_attribut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Ant_Attribut_strategy)
def test_ant_attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Attribut_strategy)
@settings(max_examples=50)
def test_attribut_instantiation(instance):
    assert isinstance(instance, Attribut)

@given(instance=Set_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, Set)

@given(instance=Ant_ClassPath_strategy)
@settings(max_examples=50)
def test_ant_classpath_instantiation(instance):
    assert isinstance(instance, Ant_ClassPath)



@given(instance=Ant_ClassPath_strategy)
def test_ant_classpath_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=Ant_FileSet_strategy)
@settings(max_examples=50)
def test_ant_fileset_instantiation(instance):
    assert isinstance(instance, Ant_FileSet)



@given(instance=Ant_FileSet_strategy)
def test_ant_fileset_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Ant_PatternSet_strategy)
@settings(max_examples=50)
def test_ant_patternset_instantiation(instance):
    assert isinstance(instance, Ant_PatternSet)

@given(instance=Ant_Path_strategy)
@settings(max_examples=50)
def test_ant_path_instantiation(instance):
    assert isinstance(instance, Ant_Path)



@given(instance=Ant_Path_strategy)
def test_ant_path_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original



@given(instance=Ant_Path_strategy)
def test_ant_path_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=FiltersFile_strategy)
@settings(max_examples=50)
def test_filtersfile_instantiation(instance):
    assert isinstance(instance, FiltersFile)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=Ant_FilterSet_strategy)
@settings(max_examples=50)
def test_ant_filterset_instantiation(instance):
    assert isinstance(instance, Ant_FilterSet)



@given(instance=Ant_FilterSet_strategy)
def test_ant_filterset_endtoken_setter(instance):
    original = instance.endtoken
    instance.endtoken = original
    assert instance.endtoken == original



@given(instance=Ant_FilterSet_strategy)
def test_ant_filterset_starttoken_setter(instance):
    original = instance.starttoken
    instance.starttoken = original
    assert instance.starttoken == original

@given(instance=Excludes_strategy)
@settings(max_examples=50)
def test_excludes_instantiation(instance):
    assert isinstance(instance, Excludes)

@given(instance=Includes_strategy)
@settings(max_examples=50)
def test_includes_instantiation(instance):
    assert isinstance(instance, Includes)

@given(instance=PatternSet_strategy)
@settings(max_examples=50)
def test_patternset_instantiation(instance):
    assert isinstance(instance, PatternSet)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=Ant_PreDefinedTask_strategy)
@settings(max_examples=50)
def test_ant_predefinedtask_instantiation(instance):
    assert isinstance(instance, Ant_PreDefinedTask)



@given(instance=Ant_PreDefinedTask_strategy)
def test_ant_predefinedtask_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Ant_PreDefinedTask_strategy)
def test_ant_predefinedtask_taskname_setter(instance):
    original = instance.taskname
    instance.taskname = original
    assert instance.taskname == original



@given(instance=Ant_PreDefinedTask_strategy)
def test_ant_predefinedtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Ant_NewTask_strategy)
@settings(max_examples=50)
def test_ant_newtask_instantiation(instance):
    assert isinstance(instance, Ant_NewTask)

@given(instance=Ant_Target_strategy)
@settings(max_examples=50)
def test_ant_target_instantiation(instance):
    assert isinstance(instance, Ant_Target)



@given(instance=Ant_Target_strategy)
def test_ant_target_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Ant_Target_strategy)
def test_ant_target_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original



@given(instance=Ant_Target_strategy)
def test_ant_target_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original



@given(instance=Ant_Target_strategy)
def test_ant_target_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=InExcludes_strategy)
@settings(max_examples=50)
def test_inexcludes_instantiation(instance):
    assert isinstance(instance, InExcludes)

@given(instance=Ant_Excludes_strategy)
@settings(max_examples=50)
def test_ant_excludes_instantiation(instance):
    assert isinstance(instance, Ant_Excludes)

@given(instance=Ant_IncludesFile_strategy)
@settings(max_examples=50)
def test_ant_includesfile_instantiation(instance):
    assert isinstance(instance, Ant_IncludesFile)

@given(instance=Ant_ExcludesFile_strategy)
@settings(max_examples=50)
def test_ant_excludesfile_instantiation(instance):
    assert isinstance(instance, Ant_ExcludesFile)

@given(instance=Ant_Includes_strategy)
@settings(max_examples=50)
def test_ant_includes_instantiation(instance):
    assert isinstance(instance, Ant_Includes)

@given(instance=Basic_strategy)
@settings(max_examples=50)
def test_basic_instantiation(instance):
    assert isinstance(instance, Basic)

@given(instance=Ant_InExcludes_strategy)
@settings(max_examples=50)
def test_ant_inexcludes_instantiation(instance):
    assert isinstance(instance, Ant_InExcludes)



@given(instance=Ant_InExcludes_strategy)
def test_ant_inexcludes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Ant_InExcludes_strategy)
def test_ant_inexcludes_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original



@given(instance=Ant_InExcludes_strategy)
def test_ant_inexcludes_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original

@given(instance=Ant_FiltersFile_strategy)
@settings(max_examples=50)
def test_ant_filtersfile_instantiation(instance):
    assert isinstance(instance, Ant_FiltersFile)



@given(instance=Ant_FiltersFile_strategy)
def test_ant_filtersfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant_PathElement_strategy)
@settings(max_examples=50)
def test_ant_pathelement_instantiation(instance):
    assert isinstance(instance, Ant_PathElement)



@given(instance=Ant_PathElement_strategy)
def test_ant_pathelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Ant_PathElement_strategy)
def test_ant_pathelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Ant_Filter_strategy)
@settings(max_examples=50)
def test_ant_filter_instantiation(instance):
    assert isinstance(instance, Ant_Filter)



@given(instance=Ant_Filter_strategy)
def test_ant_filter_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=Ant_Filter_strategy)
def test_ant_filter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Ant_FileList_strategy)
@settings(max_examples=50)
def test_ant_filelist_instantiation(instance):
    assert isinstance(instance, Ant_FileList)



@given(instance=Ant_FileList_strategy)
def test_ant_filelist_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original



@given(instance=Ant_FileList_strategy)
def test_ant_filelist_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=Ant_Mapper_strategy)
@settings(max_examples=50)
def test_ant_mapper_instantiation(instance):
    assert isinstance(instance, Ant_Mapper)



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_classpathref_setter(instance):
    original = instance.classpathref
    instance.classpathref = original
    assert instance.classpathref == original



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_classpath_setter(instance):
    original = instance.classpath
    instance.classpath = original
    assert instance.classpath == original



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=Ant_Mapper_strategy)
def test_ant_mapper_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=Ant_Set_strategy)
@settings(max_examples=50)
def test_ant_set_instantiation(instance):
    assert isinstance(instance, Ant_Set)

@given(instance=Ant_Basic_strategy)
@settings(max_examples=50)
def test_ant_basic_instantiation(instance):
    assert isinstance(instance, Ant_Basic)

@given(instance=Ant_Pattern_strategy)
@settings(max_examples=50)
def test_ant_pattern_instantiation(instance):
    assert isinstance(instance, Ant_Pattern)

@given(instance=Ant_Project_strategy)
@settings(max_examples=50)
def test_ant_project_instantiation(instance):
    assert isinstance(instance, Ant_Project)



@given(instance=Ant_Project_strategy)
def test_ant_project_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original



@given(instance=Ant_Project_strategy)
def test_ant_project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Ant_Project_strategy)
def test_ant_project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PropertyName_strategy)
@settings(max_examples=50)
def test_propertyname_instantiation(instance):
    assert isinstance(instance, PropertyName)

@given(instance=Ant_PropertyLocation_strategy)
@settings(max_examples=50)
def test_ant_propertylocation_instantiation(instance):
    assert isinstance(instance, Ant_PropertyLocation)



@given(instance=Ant_PropertyLocation_strategy)
def test_ant_propertylocation_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Ant_PropertyValue_strategy)
@settings(max_examples=50)
def test_ant_propertyvalue_instantiation(instance):
    assert isinstance(instance, Ant_PropertyValue)



@given(instance=Ant_PropertyValue_strategy)
def test_ant_propertyvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Ant_Property_strategy)
@settings(max_examples=50)
def test_ant_property_instantiation(instance):
    assert isinstance(instance, Ant_Property)

@given(instance=TaskDef_strategy)
@settings(max_examples=50)
def test_taskdef_instantiation(instance):
    assert isinstance(instance, TaskDef)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Ant_PropertyEnv_strategy)
@settings(max_examples=50)
def test_ant_propertyenv_instantiation(instance):
    assert isinstance(instance, Ant_PropertyEnv)



@given(instance=Ant_PropertyEnv_strategy)
def test_ant_propertyenv_environment_setter(instance):
    original = instance.environment
    instance.environment = original
    assert instance.environment == original

@given(instance=Ant_PropertyFile_strategy)
@settings(max_examples=50)
def test_ant_propertyfile_instantiation(instance):
    assert isinstance(instance, Ant_PropertyFile)



@given(instance=Ant_PropertyFile_strategy)
def test_ant_propertyfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant_PropertyName_strategy)
@settings(max_examples=50)
def test_ant_propertyname_instantiation(instance):
    assert isinstance(instance, Ant_PropertyName)



@given(instance=Ant_PropertyName_strategy)
def test_ant_propertyname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Path_strategy)
@settings(max_examples=50)
def test_path_instantiation(instance):
    assert isinstance(instance, Path)

@given(instance=Target_strategy)
@settings(max_examples=50)
def test_target_instantiation(instance):
    assert isinstance(instance, Target)
