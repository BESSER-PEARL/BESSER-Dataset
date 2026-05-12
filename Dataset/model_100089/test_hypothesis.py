import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MavenMaven_ContentsGoal,
    MavenMaven_AbstractGoal,
    Goal,
    Xmlns,
    MavenMaven_Project,
    AntPropertyName,
    MavenMaven_AntPropertyValue,
    ContentsGoal,
    MavenMaven_AttainGoal,
    MavenMaven_AntProperty,
    MavenMaven_Xmlns,
    PrePostGoal,
    AntTaskDef,
    AntProperty,
    MavenMaven_AntPropertyName,
    Path,
    FileTask,
    MavenMaven_Copy,
    MavenMaven_Mkdir,
    MavenMaven_Delete,
    Mapper,
    FilterSet,
    DocumentationTask,
    MavenMaven_Javadoc,
    ArchiveTask,
    MavenMaven_Jar,
    MavenMaven_FormatTstamp,
    CompileTask,
    MavenMaven_Javac,
    ExecutionTask,
    MavenMaven_Java,
    MavenMaven_Exec,
    FormatTstamp,
    MiscellaneousTask,
    MavenMaven_Tstamp,
    MavenMaven_Echo,
    ClassPath,
    MavenMaven_AntTaskDef,
    MavenMaven_Task,
    PreDefinedTask,
    MavenMaven_MiscellaneousTask,
    MavenMaven_DocumentationTask,
    MavenMaven_FileTask,
    MavenMaven_CompileTask,
    MavenMaven_ArchiveTask,
    MavenMaven_ExecutionTask,
    MavenMaven_Attribut,
    Attribut,
    Task,
    MavenMaven_PreDefinedTask,
    MavenMaven_NewTask,
    FiltersFile,
    Filter,
    FileSet,
    PathElement,
    Set,
    MavenMaven_ClassPath,
    MavenMaven_Path,
    MavenMaven_PatternSet,
    MavenMaven_FilterSet,
    Excludes,
    Includes,
    PatternSet,
    MavenMaven_FileSet,
    MavenMaven_Pattern,
    PostGoal,
    PreGoal,
    MavenMaven_PostGoal,
    InExcludes,
    MavenMaven_ExcludesFile,
    MavenMaven_IncludesFile,
    MavenMaven_Excludes,
    MavenMaven_Includes,
    Basic,
    MavenMaven_Filter,
    MavenMaven_InExcludes,
    MavenMaven_FileList,
    MavenMaven_PathElement,
    MavenMaven_FiltersFile,
    MavenMaven_Mapper,
    Pattern,
    MavenMaven_Set,
    MavenMaven_Basic,
    JellyCommand,
    MavenMaven_JellyForEach,
    MavenMaven_JellySet,
    MavenMaven_JellyCommand,
    MavenMaven_AntPropertyEnv,
    MavenMaven_AntPropertyFile,
    MavenMaven_AntPropertyLocation,
    MavenMaven_PreGoal,
    AbstractGoal,
    MavenMaven_Goal,
    MavenMaven_PrePostGoal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mavenmaven_contentsgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_ContentsGoal)


def test_mavenmaven_contentsgoal_constructor_exists():
    assert callable(MavenMaven_ContentsGoal.__init__)


def test_mavenmaven_contentsgoal_constructor_args():
    sig = inspect.signature(MavenMaven_ContentsGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_abstractgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AbstractGoal)


def test_mavenmaven_abstractgoal_constructor_exists():
    assert callable(MavenMaven_AbstractGoal.__init__)


def test_mavenmaven_abstractgoal_constructor_args():
    sig = inspect.signature(MavenMaven_AbstractGoal.__init__)
    params = list(sig.parameters.keys())



def test_goal_is_not_abstract():
    assert not inspect.isabstract(Goal)


def test_goal_constructor_exists():
    assert callable(Goal.__init__)


def test_goal_constructor_args():
    sig = inspect.signature(Goal.__init__)
    params = list(sig.parameters.keys())



def test_xmlns_is_not_abstract():
    assert not inspect.isabstract(Xmlns)


def test_xmlns_constructor_exists():
    assert callable(Xmlns.__init__)


def test_xmlns_constructor_args():
    sig = inspect.signature(Xmlns.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_project_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Project)


def test_mavenmaven_project_constructor_exists():
    assert callable(MavenMaven_Project.__init__)


def test_mavenmaven_project_constructor_args():
    sig = inspect.signature(MavenMaven_Project.__init__)
    params = list(sig.parameters.keys())



def test_antpropertyname_is_not_abstract():
    assert not inspect.isabstract(AntPropertyName)


def test_antpropertyname_constructor_exists():
    assert callable(AntPropertyName.__init__)


def test_antpropertyname_constructor_args():
    sig = inspect.signature(AntPropertyName.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_antpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntPropertyValue)


def test_mavenmaven_antpropertyvalue_constructor_exists():
    assert callable(MavenMaven_AntPropertyValue.__init__)


def test_mavenmaven_antpropertyvalue_constructor_args():
    sig = inspect.signature(MavenMaven_AntPropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven_antpropertyvalue_has_value():
    assert hasattr(MavenMaven_AntPropertyValue, "value")
    descriptor = None
    for klass in MavenMaven_AntPropertyValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_contentsgoal_is_not_abstract():
    assert not inspect.isabstract(ContentsGoal)


def test_contentsgoal_constructor_exists():
    assert callable(ContentsGoal.__init__)


def test_contentsgoal_constructor_args():
    sig = inspect.signature(ContentsGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_attaingoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AttainGoal)


def test_mavenmaven_attaingoal_constructor_exists():
    assert callable(MavenMaven_AttainGoal.__init__)


def test_mavenmaven_attaingoal_constructor_args():
    sig = inspect.signature(MavenMaven_AttainGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_antproperty_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntProperty)


def test_mavenmaven_antproperty_constructor_exists():
    assert callable(MavenMaven_AntProperty.__init__)


def test_mavenmaven_antproperty_constructor_args():
    sig = inspect.signature(MavenMaven_AntProperty.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_xmlns_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Xmlns)


def test_mavenmaven_xmlns_constructor_exists():
    assert callable(MavenMaven_Xmlns.__init__)


def test_mavenmaven_xmlns_constructor_args():
    sig = inspect.signature(MavenMaven_Xmlns.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven_xmlns_has_name():
    assert hasattr(MavenMaven_Xmlns, "name")
    descriptor = None
    for klass in MavenMaven_Xmlns.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_xmlns_has_value():
    assert hasattr(MavenMaven_Xmlns, "value")
    descriptor = None
    for klass in MavenMaven_Xmlns.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_prepostgoal_is_not_abstract():
    assert not inspect.isabstract(PrePostGoal)


def test_prepostgoal_constructor_exists():
    assert callable(PrePostGoal.__init__)


def test_prepostgoal_constructor_args():
    sig = inspect.signature(PrePostGoal.__init__)
    params = list(sig.parameters.keys())



def test_anttaskdef_is_not_abstract():
    assert not inspect.isabstract(AntTaskDef)


def test_anttaskdef_constructor_exists():
    assert callable(AntTaskDef.__init__)


def test_anttaskdef_constructor_args():
    sig = inspect.signature(AntTaskDef.__init__)
    params = list(sig.parameters.keys())



def test_antproperty_is_not_abstract():
    assert not inspect.isabstract(AntProperty)


def test_antproperty_constructor_exists():
    assert callable(AntProperty.__init__)


def test_antproperty_constructor_args():
    sig = inspect.signature(AntProperty.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_antpropertyname_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntPropertyName)


def test_mavenmaven_antpropertyname_constructor_exists():
    assert callable(MavenMaven_AntPropertyName.__init__)


def test_mavenmaven_antpropertyname_constructor_args():
    sig = inspect.signature(MavenMaven_AntPropertyName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven_antpropertyname_has_name():
    assert hasattr(MavenMaven_AntPropertyName, "name")
    descriptor = None
    for klass in MavenMaven_AntPropertyName.__mro__:
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



def test_filetask_is_not_abstract():
    assert not inspect.isabstract(FileTask)


def test_filetask_constructor_exists():
    assert callable(FileTask.__init__)


def test_filetask_constructor_args():
    sig = inspect.signature(FileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_copy_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Copy)


def test_mavenmaven_copy_constructor_exists():
    assert callable(MavenMaven_Copy.__init__)


def test_mavenmaven_copy_constructor_args():
    sig = inspect.signature(MavenMaven_Copy.__init__)
    params = list(sig.parameters.keys())
    assert "flatten" in params, "Missing parameter 'flatten'"
    assert "overwrite" in params, "Missing parameter 'overwrite'"
    assert "todir" in params, "Missing parameter 'todir'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "tofile" in params, "Missing parameter 'tofile'"
    assert "presservelastmodified" in params, "Missing parameter 'presservelastmodified'"
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven_copy_has_flatten():
    assert hasattr(MavenMaven_Copy, "flatten")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "flatten" in klass.__dict__:
            descriptor = klass.__dict__["flatten"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_overwrite():
    assert hasattr(MavenMaven_Copy, "overwrite")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "overwrite" in klass.__dict__:
            descriptor = klass.__dict__["overwrite"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_todir():
    assert hasattr(MavenMaven_Copy, "todir")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "todir" in klass.__dict__:
            descriptor = klass.__dict__["todir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_includeEmptyDirs():
    assert hasattr(MavenMaven_Copy, "includeEmptyDirs")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_filtering():
    assert hasattr(MavenMaven_Copy, "filtering")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_tofile():
    assert hasattr(MavenMaven_Copy, "tofile")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "tofile" in klass.__dict__:
            descriptor = klass.__dict__["tofile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_presservelastmodified():
    assert hasattr(MavenMaven_Copy, "presservelastmodified")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "presservelastmodified" in klass.__dict__:
            descriptor = klass.__dict__["presservelastmodified"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_copy_has_file():
    assert hasattr(MavenMaven_Copy, "file")
    descriptor = None
    for klass in MavenMaven_Copy.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_mkdir_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Mkdir)


def test_mavenmaven_mkdir_constructor_exists():
    assert callable(MavenMaven_Mkdir.__init__)


def test_mavenmaven_mkdir_constructor_args():
    sig = inspect.signature(MavenMaven_Mkdir.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven_mkdir_has_dir():
    assert hasattr(MavenMaven_Mkdir, "dir")
    descriptor = None
    for klass in MavenMaven_Mkdir.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_delete_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Delete)


def test_mavenmaven_delete_constructor_exists():
    assert callable(MavenMaven_Delete.__init__)


def test_mavenmaven_delete_constructor_args():
    sig = inspect.signature(MavenMaven_Delete.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "quiet" in params, "Missing parameter 'quiet'"
    assert "excludes" in params, "Missing parameter 'excludes'"
    assert "verbose" in params, "Missing parameter 'verbose'"
    assert "excludesfile" in params, "Missing parameter 'excludesfile'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "failonerror" in params, "Missing parameter 'failonerror'"
    assert "includesfile" in params, "Missing parameter 'includesfile'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven_delete_has_file():
    assert hasattr(MavenMaven_Delete, "file")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_quiet():
    assert hasattr(MavenMaven_Delete, "quiet")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "quiet" in klass.__dict__:
            descriptor = klass.__dict__["quiet"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_excludes():
    assert hasattr(MavenMaven_Delete, "excludes")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_verbose():
    assert hasattr(MavenMaven_Delete, "verbose")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_excludesfile():
    assert hasattr(MavenMaven_Delete, "excludesfile")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "excludesfile" in klass.__dict__:
            descriptor = klass.__dict__["excludesfile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_defaultexcludes():
    assert hasattr(MavenMaven_Delete, "defaultexcludes")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_failonerror():
    assert hasattr(MavenMaven_Delete, "failonerror")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "failonerror" in klass.__dict__:
            descriptor = klass.__dict__["failonerror"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_includesfile():
    assert hasattr(MavenMaven_Delete, "includesfile")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "includesfile" in klass.__dict__:
            descriptor = klass.__dict__["includesfile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_includeEmptyDirs():
    assert hasattr(MavenMaven_Delete, "includeEmptyDirs")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_includes():
    assert hasattr(MavenMaven_Delete, "includes")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_delete_has_dir():
    assert hasattr(MavenMaven_Delete, "dir")
    descriptor = None
    for klass in MavenMaven_Delete.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



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



def test_documentationtask_is_not_abstract():
    assert not inspect.isabstract(DocumentationTask)


def test_documentationtask_constructor_exists():
    assert callable(DocumentationTask.__init__)


def test_documentationtask_constructor_args():
    sig = inspect.signature(DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_javadoc_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Javadoc)


def test_mavenmaven_javadoc_constructor_exists():
    assert callable(MavenMaven_Javadoc.__init__)


def test_mavenmaven_javadoc_constructor_args():
    sig = inspect.signature(MavenMaven_Javadoc.__init__)
    params = list(sig.parameters.keys())
    assert "packagenames" in params, "Missing parameter 'packagenames'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "use" in params, "Missing parameter 'use'"
    assert "windowtitle" in params, "Missing parameter 'windowtitle'"
    assert "author" in params, "Missing parameter 'author'"
    assert "version" in params, "Missing parameter 'version'"
    assert "sourcepath" in params, "Missing parameter 'sourcepath'"
    assert "destdir" in params, "Missing parameter 'destdir'"

def test_mavenmaven_javadoc_has_packagenames():
    assert hasattr(MavenMaven_Javadoc, "packagenames")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "packagenames" in klass.__dict__:
            descriptor = klass.__dict__["packagenames"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_defaultexcludes():
    assert hasattr(MavenMaven_Javadoc, "defaultexcludes")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_use():
    assert hasattr(MavenMaven_Javadoc, "use")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_windowtitle():
    assert hasattr(MavenMaven_Javadoc, "windowtitle")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "windowtitle" in klass.__dict__:
            descriptor = klass.__dict__["windowtitle"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_author():
    assert hasattr(MavenMaven_Javadoc, "author")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_version():
    assert hasattr(MavenMaven_Javadoc, "version")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_sourcepath():
    assert hasattr(MavenMaven_Javadoc, "sourcepath")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "sourcepath" in klass.__dict__:
            descriptor = klass.__dict__["sourcepath"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javadoc_has_destdir():
    assert hasattr(MavenMaven_Javadoc, "destdir")
    descriptor = None
    for klass in MavenMaven_Javadoc.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)



def test_archivetask_is_not_abstract():
    assert not inspect.isabstract(ArchiveTask)


def test_archivetask_constructor_exists():
    assert callable(ArchiveTask.__init__)


def test_archivetask_constructor_args():
    sig = inspect.signature(ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_jar_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Jar)


def test_mavenmaven_jar_constructor_exists():
    assert callable(MavenMaven_Jar.__init__)


def test_mavenmaven_jar_constructor_args():
    sig = inspect.signature(MavenMaven_Jar.__init__)
    params = list(sig.parameters.keys())
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "jarfile" in params, "Missing parameter 'jarfile'"
    assert "manifest" in params, "Missing parameter 'manifest'"
    assert "basedir" in params, "Missing parameter 'basedir'"
    assert "compress" in params, "Missing parameter 'compress'"

def test_mavenmaven_jar_has_encoding():
    assert hasattr(MavenMaven_Jar, "encoding")
    descriptor = None
    for klass in MavenMaven_Jar.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jar_has_jarfile():
    assert hasattr(MavenMaven_Jar, "jarfile")
    descriptor = None
    for klass in MavenMaven_Jar.__mro__:
        if "jarfile" in klass.__dict__:
            descriptor = klass.__dict__["jarfile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jar_has_manifest():
    assert hasattr(MavenMaven_Jar, "manifest")
    descriptor = None
    for klass in MavenMaven_Jar.__mro__:
        if "manifest" in klass.__dict__:
            descriptor = klass.__dict__["manifest"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jar_has_basedir():
    assert hasattr(MavenMaven_Jar, "basedir")
    descriptor = None
    for klass in MavenMaven_Jar.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jar_has_compress():
    assert hasattr(MavenMaven_Jar, "compress")
    descriptor = None
    for klass in MavenMaven_Jar.__mro__:
        if "compress" in klass.__dict__:
            descriptor = klass.__dict__["compress"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_formattstamp_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FormatTstamp)


def test_mavenmaven_formattstamp_constructor_exists():
    assert callable(MavenMaven_FormatTstamp.__init__)


def test_mavenmaven_formattstamp_constructor_args():
    sig = inspect.signature(MavenMaven_FormatTstamp.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "property" in params, "Missing parameter 'property'"

def test_mavenmaven_formattstamp_has_offset():
    assert hasattr(MavenMaven_FormatTstamp, "offset")
    descriptor = None
    for klass in MavenMaven_FormatTstamp.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_formattstamp_has_unit():
    assert hasattr(MavenMaven_FormatTstamp, "unit")
    descriptor = None
    for klass in MavenMaven_FormatTstamp.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_formattstamp_has_pattern():
    assert hasattr(MavenMaven_FormatTstamp, "pattern")
    descriptor = None
    for klass in MavenMaven_FormatTstamp.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_formattstamp_has_locale():
    assert hasattr(MavenMaven_FormatTstamp, "locale")
    descriptor = None
    for klass in MavenMaven_FormatTstamp.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_formattstamp_has_property():
    assert hasattr(MavenMaven_FormatTstamp, "property")
    descriptor = None
    for klass in MavenMaven_FormatTstamp.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)



def test_compiletask_is_not_abstract():
    assert not inspect.isabstract(CompileTask)


def test_compiletask_constructor_exists():
    assert callable(CompileTask.__init__)


def test_compiletask_constructor_args():
    sig = inspect.signature(CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_javac_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Javac)


def test_mavenmaven_javac_constructor_exists():
    assert callable(MavenMaven_Javac.__init__)


def test_mavenmaven_javac_constructor_args():
    sig = inspect.signature(MavenMaven_Javac.__init__)
    params = list(sig.parameters.keys())
    assert "deprecation" in params, "Missing parameter 'deprecation'"
    assert "srcdir" in params, "Missing parameter 'srcdir'"
    assert "debug" in params, "Missing parameter 'debug'"
    assert "optimize" in params, "Missing parameter 'optimize'"
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "fork" in params, "Missing parameter 'fork'"

def test_mavenmaven_javac_has_deprecation():
    assert hasattr(MavenMaven_Javac, "deprecation")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "deprecation" in klass.__dict__:
            descriptor = klass.__dict__["deprecation"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javac_has_srcdir():
    assert hasattr(MavenMaven_Javac, "srcdir")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "srcdir" in klass.__dict__:
            descriptor = klass.__dict__["srcdir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javac_has_debug():
    assert hasattr(MavenMaven_Javac, "debug")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javac_has_optimize():
    assert hasattr(MavenMaven_Javac, "optimize")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "optimize" in klass.__dict__:
            descriptor = klass.__dict__["optimize"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javac_has_destdir():
    assert hasattr(MavenMaven_Javac, "destdir")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_javac_has_fork():
    assert hasattr(MavenMaven_Javac, "fork")
    descriptor = None
    for klass in MavenMaven_Javac.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)



def test_executiontask_is_not_abstract():
    assert not inspect.isabstract(ExecutionTask)


def test_executiontask_constructor_exists():
    assert callable(ExecutionTask.__init__)


def test_executiontask_constructor_args():
    sig = inspect.signature(ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_java_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Java)


def test_mavenmaven_java_constructor_exists():
    assert callable(MavenMaven_Java.__init__)


def test_mavenmaven_java_constructor_args():
    sig = inspect.signature(MavenMaven_Java.__init__)
    params = list(sig.parameters.keys())
    assert "classname" in params, "Missing parameter 'classname'"
    assert "jar" in params, "Missing parameter 'jar'"
    assert "fork" in params, "Missing parameter 'fork'"

def test_mavenmaven_java_has_classname():
    assert hasattr(MavenMaven_Java, "classname")
    descriptor = None
    for klass in MavenMaven_Java.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_java_has_jar():
    assert hasattr(MavenMaven_Java, "jar")
    descriptor = None
    for klass in MavenMaven_Java.__mro__:
        if "jar" in klass.__dict__:
            descriptor = klass.__dict__["jar"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_java_has_fork():
    assert hasattr(MavenMaven_Java, "fork")
    descriptor = None
    for klass in MavenMaven_Java.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_exec_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Exec)


def test_mavenmaven_exec_constructor_exists():
    assert callable(MavenMaven_Exec.__init__)


def test_mavenmaven_exec_constructor_args():
    sig = inspect.signature(MavenMaven_Exec.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "executable" in params, "Missing parameter 'executable'"

def test_mavenmaven_exec_has_dir():
    assert hasattr(MavenMaven_Exec, "dir")
    descriptor = None
    for klass in MavenMaven_Exec.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_exec_has_executable():
    assert hasattr(MavenMaven_Exec, "executable")
    descriptor = None
    for klass in MavenMaven_Exec.__mro__:
        if "executable" in klass.__dict__:
            descriptor = klass.__dict__["executable"]
            break
    assert isinstance(descriptor, property)



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



def test_mavenmaven_tstamp_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Tstamp)


def test_mavenmaven_tstamp_constructor_exists():
    assert callable(MavenMaven_Tstamp.__init__)


def test_mavenmaven_tstamp_constructor_args():
    sig = inspect.signature(MavenMaven_Tstamp.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_echo_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Echo)


def test_mavenmaven_echo_constructor_exists():
    assert callable(MavenMaven_Echo.__init__)


def test_mavenmaven_echo_constructor_args():
    sig = inspect.signature(MavenMaven_Echo.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "file" in params, "Missing parameter 'file'"
    assert "append" in params, "Missing parameter 'append'"

def test_mavenmaven_echo_has_message():
    assert hasattr(MavenMaven_Echo, "message")
    descriptor = None
    for klass in MavenMaven_Echo.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_echo_has_file():
    assert hasattr(MavenMaven_Echo, "file")
    descriptor = None
    for klass in MavenMaven_Echo.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_echo_has_append():
    assert hasattr(MavenMaven_Echo, "append")
    descriptor = None
    for klass in MavenMaven_Echo.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)



def test_classpath_is_not_abstract():
    assert not inspect.isabstract(ClassPath)


def test_classpath_constructor_exists():
    assert callable(ClassPath.__init__)


def test_classpath_constructor_args():
    sig = inspect.signature(ClassPath.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_anttaskdef_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntTaskDef)


def test_mavenmaven_anttaskdef_constructor_exists():
    assert callable(MavenMaven_AntTaskDef.__init__)


def test_mavenmaven_anttaskdef_constructor_args():
    sig = inspect.signature(MavenMaven_AntTaskDef.__init__)
    params = list(sig.parameters.keys())
    assert "classname" in params, "Missing parameter 'classname'"
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven_anttaskdef_has_classname():
    assert hasattr(MavenMaven_AntTaskDef, "classname")
    descriptor = None
    for klass in MavenMaven_AntTaskDef.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_anttaskdef_has_name():
    assert hasattr(MavenMaven_AntTaskDef, "name")
    descriptor = None
    for klass in MavenMaven_AntTaskDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_task_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Task)


def test_mavenmaven_task_constructor_exists():
    assert callable(MavenMaven_Task.__init__)


def test_mavenmaven_task_constructor_args():
    sig = inspect.signature(MavenMaven_Task.__init__)
    params = list(sig.parameters.keys())



def test_predefinedtask_is_not_abstract():
    assert not inspect.isabstract(PreDefinedTask)


def test_predefinedtask_constructor_exists():
    assert callable(PreDefinedTask.__init__)


def test_predefinedtask_constructor_args():
    sig = inspect.signature(PreDefinedTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_MiscellaneousTask)


def test_mavenmaven_miscellaneoustask_constructor_exists():
    assert callable(MavenMaven_MiscellaneousTask.__init__)


def test_mavenmaven_miscellaneoustask_constructor_args():
    sig = inspect.signature(MavenMaven_MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_documentationtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_DocumentationTask)


def test_mavenmaven_documentationtask_constructor_exists():
    assert callable(MavenMaven_DocumentationTask.__init__)


def test_mavenmaven_documentationtask_constructor_args():
    sig = inspect.signature(MavenMaven_DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_filetask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FileTask)


def test_mavenmaven_filetask_constructor_exists():
    assert callable(MavenMaven_FileTask.__init__)


def test_mavenmaven_filetask_constructor_args():
    sig = inspect.signature(MavenMaven_FileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_compiletask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_CompileTask)


def test_mavenmaven_compiletask_constructor_exists():
    assert callable(MavenMaven_CompileTask.__init__)


def test_mavenmaven_compiletask_constructor_args():
    sig = inspect.signature(MavenMaven_CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_archivetask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_ArchiveTask)


def test_mavenmaven_archivetask_constructor_exists():
    assert callable(MavenMaven_ArchiveTask.__init__)


def test_mavenmaven_archivetask_constructor_args():
    sig = inspect.signature(MavenMaven_ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_executiontask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_ExecutionTask)


def test_mavenmaven_executiontask_constructor_exists():
    assert callable(MavenMaven_ExecutionTask.__init__)


def test_mavenmaven_executiontask_constructor_args():
    sig = inspect.signature(MavenMaven_ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_attribut_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Attribut)


def test_mavenmaven_attribut_constructor_exists():
    assert callable(MavenMaven_Attribut.__init__)


def test_mavenmaven_attribut_constructor_args():
    sig = inspect.signature(MavenMaven_Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven_attribut_has_value():
    assert hasattr(MavenMaven_Attribut, "value")
    descriptor = None
    for klass in MavenMaven_Attribut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_attribut_has_name():
    assert hasattr(MavenMaven_Attribut, "name")
    descriptor = None
    for klass in MavenMaven_Attribut.__mro__:
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



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_predefinedtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PreDefinedTask)


def test_mavenmaven_predefinedtask_constructor_exists():
    assert callable(MavenMaven_PreDefinedTask.__init__)


def test_mavenmaven_predefinedtask_constructor_args():
    sig = inspect.signature(MavenMaven_PreDefinedTask.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "taskname" in params, "Missing parameter 'taskname'"
    assert "id" in params, "Missing parameter 'id'"

def test_mavenmaven_predefinedtask_has_description():
    assert hasattr(MavenMaven_PreDefinedTask, "description")
    descriptor = None
    for klass in MavenMaven_PreDefinedTask.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_predefinedtask_has_taskname():
    assert hasattr(MavenMaven_PreDefinedTask, "taskname")
    descriptor = None
    for klass in MavenMaven_PreDefinedTask.__mro__:
        if "taskname" in klass.__dict__:
            descriptor = klass.__dict__["taskname"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_predefinedtask_has_id():
    assert hasattr(MavenMaven_PreDefinedTask, "id")
    descriptor = None
    for klass in MavenMaven_PreDefinedTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_newtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_NewTask)


def test_mavenmaven_newtask_constructor_exists():
    assert callable(MavenMaven_NewTask.__init__)


def test_mavenmaven_newtask_constructor_args():
    sig = inspect.signature(MavenMaven_NewTask.__init__)
    params = list(sig.parameters.keys())



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



def test_set_is_not_abstract():
    assert not inspect.isabstract(Set)


def test_set_constructor_exists():
    assert callable(Set.__init__)


def test_set_constructor_args():
    sig = inspect.signature(Set.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_classpath_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_ClassPath)


def test_mavenmaven_classpath_constructor_exists():
    assert callable(MavenMaven_ClassPath.__init__)


def test_mavenmaven_classpath_constructor_args():
    sig = inspect.signature(MavenMaven_ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"

def test_mavenmaven_classpath_has_refid():
    assert hasattr(MavenMaven_ClassPath, "refid")
    descriptor = None
    for klass in MavenMaven_ClassPath.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_path_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Path)


def test_mavenmaven_path_constructor_exists():
    assert callable(MavenMaven_Path.__init__)


def test_mavenmaven_path_constructor_args():
    sig = inspect.signature(MavenMaven_Path.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"
    assert "id" in params, "Missing parameter 'id'"

def test_mavenmaven_path_has_refid():
    assert hasattr(MavenMaven_Path, "refid")
    descriptor = None
    for klass in MavenMaven_Path.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_path_has_id():
    assert hasattr(MavenMaven_Path, "id")
    descriptor = None
    for klass in MavenMaven_Path.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_patternset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PatternSet)


def test_mavenmaven_patternset_constructor_exists():
    assert callable(MavenMaven_PatternSet.__init__)


def test_mavenmaven_patternset_constructor_args():
    sig = inspect.signature(MavenMaven_PatternSet.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_filterset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FilterSet)


def test_mavenmaven_filterset_constructor_exists():
    assert callable(MavenMaven_FilterSet.__init__)


def test_mavenmaven_filterset_constructor_args():
    sig = inspect.signature(MavenMaven_FilterSet.__init__)
    params = list(sig.parameters.keys())
    assert "endtoken" in params, "Missing parameter 'endtoken'"
    assert "starttoken" in params, "Missing parameter 'starttoken'"

def test_mavenmaven_filterset_has_endtoken():
    assert hasattr(MavenMaven_FilterSet, "endtoken")
    descriptor = None
    for klass in MavenMaven_FilterSet.__mro__:
        if "endtoken" in klass.__dict__:
            descriptor = klass.__dict__["endtoken"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_filterset_has_starttoken():
    assert hasattr(MavenMaven_FilterSet, "starttoken")
    descriptor = None
    for klass in MavenMaven_FilterSet.__mro__:
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



def test_mavenmaven_fileset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FileSet)


def test_mavenmaven_fileset_constructor_exists():
    assert callable(MavenMaven_FileSet.__init__)


def test_mavenmaven_fileset_constructor_args():
    sig = inspect.signature(MavenMaven_FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven_fileset_has_dir():
    assert hasattr(MavenMaven_FileSet, "dir")
    descriptor = None
    for klass in MavenMaven_FileSet.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_pattern_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Pattern)


def test_mavenmaven_pattern_constructor_exists():
    assert callable(MavenMaven_Pattern.__init__)


def test_mavenmaven_pattern_constructor_args():
    sig = inspect.signature(MavenMaven_Pattern.__init__)
    params = list(sig.parameters.keys())



def test_postgoal_is_not_abstract():
    assert not inspect.isabstract(PostGoal)


def test_postgoal_constructor_exists():
    assert callable(PostGoal.__init__)


def test_postgoal_constructor_args():
    sig = inspect.signature(PostGoal.__init__)
    params = list(sig.parameters.keys())



def test_pregoal_is_not_abstract():
    assert not inspect.isabstract(PreGoal)


def test_pregoal_constructor_exists():
    assert callable(PreGoal.__init__)


def test_pregoal_constructor_args():
    sig = inspect.signature(PreGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_postgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PostGoal)


def test_mavenmaven_postgoal_constructor_exists():
    assert callable(MavenMaven_PostGoal.__init__)


def test_mavenmaven_postgoal_constructor_args():
    sig = inspect.signature(MavenMaven_PostGoal.__init__)
    params = list(sig.parameters.keys())



def test_inexcludes_is_not_abstract():
    assert not inspect.isabstract(InExcludes)


def test_inexcludes_constructor_exists():
    assert callable(InExcludes.__init__)


def test_inexcludes_constructor_args():
    sig = inspect.signature(InExcludes.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_excludesfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_ExcludesFile)


def test_mavenmaven_excludesfile_constructor_exists():
    assert callable(MavenMaven_ExcludesFile.__init__)


def test_mavenmaven_excludesfile_constructor_args():
    sig = inspect.signature(MavenMaven_ExcludesFile.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_includesfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_IncludesFile)


def test_mavenmaven_includesfile_constructor_exists():
    assert callable(MavenMaven_IncludesFile.__init__)


def test_mavenmaven_includesfile_constructor_args():
    sig = inspect.signature(MavenMaven_IncludesFile.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_excludes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Excludes)


def test_mavenmaven_excludes_constructor_exists():
    assert callable(MavenMaven_Excludes.__init__)


def test_mavenmaven_excludes_constructor_args():
    sig = inspect.signature(MavenMaven_Excludes.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_includes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Includes)


def test_mavenmaven_includes_constructor_exists():
    assert callable(MavenMaven_Includes.__init__)


def test_mavenmaven_includes_constructor_args():
    sig = inspect.signature(MavenMaven_Includes.__init__)
    params = list(sig.parameters.keys())



def test_basic_is_not_abstract():
    assert not inspect.isabstract(Basic)


def test_basic_constructor_exists():
    assert callable(Basic.__init__)


def test_basic_constructor_args():
    sig = inspect.signature(Basic.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_filter_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Filter)


def test_mavenmaven_filter_constructor_exists():
    assert callable(MavenMaven_Filter.__init__)


def test_mavenmaven_filter_constructor_args():
    sig = inspect.signature(MavenMaven_Filter.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven_filter_has_token():
    assert hasattr(MavenMaven_Filter, "token")
    descriptor = None
    for klass in MavenMaven_Filter.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_filter_has_value():
    assert hasattr(MavenMaven_Filter, "value")
    descriptor = None
    for klass in MavenMaven_Filter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_inexcludes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_InExcludes)


def test_mavenmaven_inexcludes_constructor_exists():
    assert callable(MavenMaven_InExcludes.__init__)


def test_mavenmaven_inexcludes_constructor_args():
    sig = inspect.signature(MavenMaven_InExcludes.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "unless" in params, "Missing parameter 'unless'"
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"

def test_mavenmaven_inexcludes_has_name():
    assert hasattr(MavenMaven_InExcludes, "name")
    descriptor = None
    for klass in MavenMaven_InExcludes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_inexcludes_has_unless():
    assert hasattr(MavenMaven_InExcludes, "unless")
    descriptor = None
    for klass in MavenMaven_InExcludes.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_inexcludes_has_ifCondition():
    assert hasattr(MavenMaven_InExcludes, "ifCondition")
    descriptor = None
    for klass in MavenMaven_InExcludes.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_filelist_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FileList)


def test_mavenmaven_filelist_constructor_exists():
    assert callable(MavenMaven_FileList.__init__)


def test_mavenmaven_filelist_constructor_args():
    sig = inspect.signature(MavenMaven_FileList.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "files" in params, "Missing parameter 'files'"

def test_mavenmaven_filelist_has_dir():
    assert hasattr(MavenMaven_FileList, "dir")
    descriptor = None
    for klass in MavenMaven_FileList.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_filelist_has_files():
    assert hasattr(MavenMaven_FileList, "files")
    descriptor = None
    for klass in MavenMaven_FileList.__mro__:
        if "files" in klass.__dict__:
            descriptor = klass.__dict__["files"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_pathelement_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PathElement)


def test_mavenmaven_pathelement_constructor_exists():
    assert callable(MavenMaven_PathElement.__init__)


def test_mavenmaven_pathelement_constructor_args():
    sig = inspect.signature(MavenMaven_PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "path" in params, "Missing parameter 'path'"

def test_mavenmaven_pathelement_has_location():
    assert hasattr(MavenMaven_PathElement, "location")
    descriptor = None
    for klass in MavenMaven_PathElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_pathelement_has_path():
    assert hasattr(MavenMaven_PathElement, "path")
    descriptor = None
    for klass in MavenMaven_PathElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_filtersfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_FiltersFile)


def test_mavenmaven_filtersfile_constructor_exists():
    assert callable(MavenMaven_FiltersFile.__init__)


def test_mavenmaven_filtersfile_constructor_args():
    sig = inspect.signature(MavenMaven_FiltersFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven_filtersfile_has_file():
    assert hasattr(MavenMaven_FiltersFile, "file")
    descriptor = None
    for klass in MavenMaven_FiltersFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_mapper_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Mapper)


def test_mavenmaven_mapper_constructor_exists():
    assert callable(MavenMaven_Mapper.__init__)


def test_mavenmaven_mapper_constructor_args():
    sig = inspect.signature(MavenMaven_Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "classname" in params, "Missing parameter 'classname'"
    assert "to" in params, "Missing parameter 'to'"
    assert "classpath" in params, "Missing parameter 'classpath'"
    assert "classpathref" in params, "Missing parameter 'classpathref'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "type" in params, "Missing parameter 'type'"

def test_mavenmaven_mapper_has_classname():
    assert hasattr(MavenMaven_Mapper, "classname")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_mapper_has_to():
    assert hasattr(MavenMaven_Mapper, "to")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_mapper_has_classpath():
    assert hasattr(MavenMaven_Mapper, "classpath")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "classpath" in klass.__dict__:
            descriptor = klass.__dict__["classpath"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_mapper_has_classpathref():
    assert hasattr(MavenMaven_Mapper, "classpathref")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "classpathref" in klass.__dict__:
            descriptor = klass.__dict__["classpathref"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_mapper_has_from_():
    assert hasattr(MavenMaven_Mapper, "from_")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_mapper_has_type():
    assert hasattr(MavenMaven_Mapper, "type")
    descriptor = None
    for klass in MavenMaven_Mapper.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_set_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Set)


def test_mavenmaven_set_constructor_exists():
    assert callable(MavenMaven_Set.__init__)


def test_mavenmaven_set_constructor_args():
    sig = inspect.signature(MavenMaven_Set.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_basic_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Basic)


def test_mavenmaven_basic_constructor_exists():
    assert callable(MavenMaven_Basic.__init__)


def test_mavenmaven_basic_constructor_args():
    sig = inspect.signature(MavenMaven_Basic.__init__)
    params = list(sig.parameters.keys())



def test_jellycommand_is_not_abstract():
    assert not inspect.isabstract(JellyCommand)


def test_jellycommand_constructor_exists():
    assert callable(JellyCommand.__init__)


def test_jellycommand_constructor_args():
    sig = inspect.signature(JellyCommand.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_jellyforeach_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_JellyForEach)


def test_mavenmaven_jellyforeach_constructor_exists():
    assert callable(MavenMaven_JellyForEach.__init__)


def test_mavenmaven_jellyforeach_constructor_args():
    sig = inspect.signature(MavenMaven_JellyForEach.__init__)
    params = list(sig.parameters.keys())
    assert "indexVar" in params, "Missing parameter 'indexVar'"
    assert "items" in params, "Missing parameter 'items'"
    assert "var" in params, "Missing parameter 'var'"

def test_mavenmaven_jellyforeach_has_indexVar():
    assert hasattr(MavenMaven_JellyForEach, "indexVar")
    descriptor = None
    for klass in MavenMaven_JellyForEach.__mro__:
        if "indexVar" in klass.__dict__:
            descriptor = klass.__dict__["indexVar"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jellyforeach_has_items():
    assert hasattr(MavenMaven_JellyForEach, "items")
    descriptor = None
    for klass in MavenMaven_JellyForEach.__mro__:
        if "items" in klass.__dict__:
            descriptor = klass.__dict__["items"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jellyforeach_has_var():
    assert hasattr(MavenMaven_JellyForEach, "var")
    descriptor = None
    for klass in MavenMaven_JellyForEach.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_jellyset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_JellySet)


def test_mavenmaven_jellyset_constructor_exists():
    assert callable(MavenMaven_JellySet.__init__)


def test_mavenmaven_jellyset_constructor_args():
    sig = inspect.signature(MavenMaven_JellySet.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "var" in params, "Missing parameter 'var'"

def test_mavenmaven_jellyset_has_value():
    assert hasattr(MavenMaven_JellySet, "value")
    descriptor = None
    for klass in MavenMaven_JellySet.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven_jellyset_has_var():
    assert hasattr(MavenMaven_JellySet, "var")
    descriptor = None
    for klass in MavenMaven_JellySet.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_jellycommand_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_JellyCommand)


def test_mavenmaven_jellycommand_constructor_exists():
    assert callable(MavenMaven_JellyCommand.__init__)


def test_mavenmaven_jellycommand_constructor_args():
    sig = inspect.signature(MavenMaven_JellyCommand.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_antpropertyenv_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntPropertyEnv)


def test_mavenmaven_antpropertyenv_constructor_exists():
    assert callable(MavenMaven_AntPropertyEnv.__init__)


def test_mavenmaven_antpropertyenv_constructor_args():
    sig = inspect.signature(MavenMaven_AntPropertyEnv.__init__)
    params = list(sig.parameters.keys())
    assert "environment" in params, "Missing parameter 'environment'"

def test_mavenmaven_antpropertyenv_has_environment():
    assert hasattr(MavenMaven_AntPropertyEnv, "environment")
    descriptor = None
    for klass in MavenMaven_AntPropertyEnv.__mro__:
        if "environment" in klass.__dict__:
            descriptor = klass.__dict__["environment"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_antpropertyfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntPropertyFile)


def test_mavenmaven_antpropertyfile_constructor_exists():
    assert callable(MavenMaven_AntPropertyFile.__init__)


def test_mavenmaven_antpropertyfile_constructor_args():
    sig = inspect.signature(MavenMaven_AntPropertyFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven_antpropertyfile_has_file():
    assert hasattr(MavenMaven_AntPropertyFile, "file")
    descriptor = None
    for klass in MavenMaven_AntPropertyFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_antpropertylocation_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_AntPropertyLocation)


def test_mavenmaven_antpropertylocation_constructor_exists():
    assert callable(MavenMaven_AntPropertyLocation.__init__)


def test_mavenmaven_antpropertylocation_constructor_args():
    sig = inspect.signature(MavenMaven_AntPropertyLocation.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_mavenmaven_antpropertylocation_has_location():
    assert hasattr(MavenMaven_AntPropertyLocation, "location")
    descriptor = None
    for klass in MavenMaven_AntPropertyLocation.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_pregoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PreGoal)


def test_mavenmaven_pregoal_constructor_exists():
    assert callable(MavenMaven_PreGoal.__init__)


def test_mavenmaven_pregoal_constructor_args():
    sig = inspect.signature(MavenMaven_PreGoal.__init__)
    params = list(sig.parameters.keys())



def test_abstractgoal_is_not_abstract():
    assert not inspect.isabstract(AbstractGoal)


def test_abstractgoal_constructor_exists():
    assert callable(AbstractGoal.__init__)


def test_abstractgoal_constructor_args():
    sig = inspect.signature(AbstractGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven_goal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_Goal)


def test_mavenmaven_goal_constructor_exists():
    assert callable(MavenMaven_Goal.__init__)


def test_mavenmaven_goal_constructor_args():
    sig = inspect.signature(MavenMaven_Goal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven_goal_has_name():
    assert hasattr(MavenMaven_Goal, "name")
    descriptor = None
    for klass in MavenMaven_Goal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven_prepostgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven_PrePostGoal)


def test_mavenmaven_prepostgoal_constructor_exists():
    assert callable(MavenMaven_PrePostGoal.__init__)


def test_mavenmaven_prepostgoal_constructor_args():
    sig = inspect.signature(MavenMaven_PrePostGoal.__init__)
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
MavenMaven_ContentsGoal_strategy = st.builds(
    MavenMaven_ContentsGoal,
)
MavenMaven_AbstractGoal_strategy = st.builds(
    MavenMaven_AbstractGoal,
)
Goal_strategy = st.builds(
    Goal,
)
Xmlns_strategy = st.builds(
    Xmlns,
)
MavenMaven_Project_strategy = st.builds(
    MavenMaven_Project,
)
AntPropertyName_strategy = st.builds(
    AntPropertyName,
)
MavenMaven_AntPropertyValue_strategy = st.builds(
    MavenMaven_AntPropertyValue,
    value=
        safe_text
)
ContentsGoal_strategy = st.builds(
    ContentsGoal,
)
MavenMaven_AttainGoal_strategy = st.builds(
    MavenMaven_AttainGoal,
)
MavenMaven_AntProperty_strategy = st.builds(
    MavenMaven_AntProperty,
)
MavenMaven_Xmlns_strategy = st.builds(
    MavenMaven_Xmlns,
    name=
        safe_text,
    value=
        safe_text
)
PrePostGoal_strategy = st.builds(
    PrePostGoal,
)
AntTaskDef_strategy = st.builds(
    AntTaskDef,
)
AntProperty_strategy = st.builds(
    AntProperty,
)
MavenMaven_AntPropertyName_strategy = st.builds(
    MavenMaven_AntPropertyName,
    name=
        safe_text
)
Path_strategy = st.builds(
    Path,
)
FileTask_strategy = st.builds(
    FileTask,
)
MavenMaven_Copy_strategy = st.builds(
    MavenMaven_Copy,
    flatten=
        safe_text,
    overwrite=
        safe_text,
    todir=
        safe_text,
    includeEmptyDirs=
        safe_text,
    filtering=
        safe_text,
    tofile=
        safe_text,
    presservelastmodified=
        safe_text,
    file=
        safe_text
)
MavenMaven_Mkdir_strategy = st.builds(
    MavenMaven_Mkdir,
    dir=
        safe_text
)
MavenMaven_Delete_strategy = st.builds(
    MavenMaven_Delete,
    file=
        safe_text,
    quiet=
        safe_text,
    excludes=
        safe_text,
    verbose=
        safe_text,
    excludesfile=
        safe_text,
    defaultexcludes=
        safe_text,
    failonerror=
        safe_text,
    includesfile=
        safe_text,
    includeEmptyDirs=
        safe_text,
    includes=
        safe_text,
    dir=
        safe_text
)
Mapper_strategy = st.builds(
    Mapper,
)
FilterSet_strategy = st.builds(
    FilterSet,
)
DocumentationTask_strategy = st.builds(
    DocumentationTask,
)
MavenMaven_Javadoc_strategy = st.builds(
    MavenMaven_Javadoc,
    packagenames=
        safe_text,
    defaultexcludes=
        safe_text,
    use=
        safe_text,
    windowtitle=
        safe_text,
    author=
        safe_text,
    version=
        safe_text,
    sourcepath=
        safe_text,
    destdir=
        safe_text
)
ArchiveTask_strategy = st.builds(
    ArchiveTask,
)
MavenMaven_Jar_strategy = st.builds(
    MavenMaven_Jar,
    encoding=
        safe_text,
    jarfile=
        safe_text,
    manifest=
        safe_text,
    basedir=
        safe_text,
    compress=
        safe_text
)
MavenMaven_FormatTstamp_strategy = st.builds(
    MavenMaven_FormatTstamp,
    offset=
        safe_text,
    unit=
        safe_text,
    pattern=
        safe_text,
    locale=
        safe_text,
    property=
        safe_text
)
CompileTask_strategy = st.builds(
    CompileTask,
)
MavenMaven_Javac_strategy = st.builds(
    MavenMaven_Javac,
    deprecation=
        safe_text,
    srcdir=
        safe_text,
    debug=
        safe_text,
    optimize=
        safe_text,
    destdir=
        safe_text,
    fork=
        safe_text
)
ExecutionTask_strategy = st.builds(
    ExecutionTask,
)
MavenMaven_Java_strategy = st.builds(
    MavenMaven_Java,
    classname=
        safe_text,
    jar=
        safe_text,
    fork=
        safe_text
)
MavenMaven_Exec_strategy = st.builds(
    MavenMaven_Exec,
    dir=
        safe_text,
    executable=
        safe_text
)
FormatTstamp_strategy = st.builds(
    FormatTstamp,
)
MiscellaneousTask_strategy = st.builds(
    MiscellaneousTask,
)
MavenMaven_Tstamp_strategy = st.builds(
    MavenMaven_Tstamp,
)
MavenMaven_Echo_strategy = st.builds(
    MavenMaven_Echo,
    message=
        safe_text,
    file=
        safe_text,
    append=
        safe_text
)
ClassPath_strategy = st.builds(
    ClassPath,
)
MavenMaven_AntTaskDef_strategy = st.builds(
    MavenMaven_AntTaskDef,
    classname=
        safe_text,
    name=
        safe_text
)
MavenMaven_Task_strategy = st.builds(
    MavenMaven_Task,
)
PreDefinedTask_strategy = st.builds(
    PreDefinedTask,
)
MavenMaven_MiscellaneousTask_strategy = st.builds(
    MavenMaven_MiscellaneousTask,
)
MavenMaven_DocumentationTask_strategy = st.builds(
    MavenMaven_DocumentationTask,
)
MavenMaven_FileTask_strategy = st.builds(
    MavenMaven_FileTask,
)
MavenMaven_CompileTask_strategy = st.builds(
    MavenMaven_CompileTask,
)
MavenMaven_ArchiveTask_strategy = st.builds(
    MavenMaven_ArchiveTask,
)
MavenMaven_ExecutionTask_strategy = st.builds(
    MavenMaven_ExecutionTask,
)
MavenMaven_Attribut_strategy = st.builds(
    MavenMaven_Attribut,
    value=
        safe_text,
    name=
        safe_text
)
Attribut_strategy = st.builds(
    Attribut,
)
Task_strategy = st.builds(
    Task,
)
MavenMaven_PreDefinedTask_strategy = st.builds(
    MavenMaven_PreDefinedTask,
    description=
        safe_text,
    taskname=
        safe_text,
    id=
        safe_text
)
MavenMaven_NewTask_strategy = st.builds(
    MavenMaven_NewTask,
)
FiltersFile_strategy = st.builds(
    FiltersFile,
)
Filter_strategy = st.builds(
    Filter,
)
FileSet_strategy = st.builds(
    FileSet,
)
PathElement_strategy = st.builds(
    PathElement,
)
Set_strategy = st.builds(
    Set,
)
MavenMaven_ClassPath_strategy = st.builds(
    MavenMaven_ClassPath,
    refid=
        safe_text
)
MavenMaven_Path_strategy = st.builds(
    MavenMaven_Path,
    refid=
        safe_text,
    id=
        safe_text
)
MavenMaven_PatternSet_strategy = st.builds(
    MavenMaven_PatternSet,
)
MavenMaven_FilterSet_strategy = st.builds(
    MavenMaven_FilterSet,
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
MavenMaven_FileSet_strategy = st.builds(
    MavenMaven_FileSet,
    dir=
        safe_text
)
MavenMaven_Pattern_strategy = st.builds(
    MavenMaven_Pattern,
)
PostGoal_strategy = st.builds(
    PostGoal,
)
PreGoal_strategy = st.builds(
    PreGoal,
)
MavenMaven_PostGoal_strategy = st.builds(
    MavenMaven_PostGoal,
)
InExcludes_strategy = st.builds(
    InExcludes,
)
MavenMaven_ExcludesFile_strategy = st.builds(
    MavenMaven_ExcludesFile,
)
MavenMaven_IncludesFile_strategy = st.builds(
    MavenMaven_IncludesFile,
)
MavenMaven_Excludes_strategy = st.builds(
    MavenMaven_Excludes,
)
MavenMaven_Includes_strategy = st.builds(
    MavenMaven_Includes,
)
Basic_strategy = st.builds(
    Basic,
)
MavenMaven_Filter_strategy = st.builds(
    MavenMaven_Filter,
    token=
        safe_text,
    value=
        safe_text
)
MavenMaven_InExcludes_strategy = st.builds(
    MavenMaven_InExcludes,
    name=
        safe_text,
    unless=
        safe_text,
    ifCondition=
        safe_text
)
MavenMaven_FileList_strategy = st.builds(
    MavenMaven_FileList,
    dir=
        safe_text,
    files=
        safe_text
)
MavenMaven_PathElement_strategy = st.builds(
    MavenMaven_PathElement,
    location=
        safe_text,
    path=
        safe_text
)
MavenMaven_FiltersFile_strategy = st.builds(
    MavenMaven_FiltersFile,
    file=
        safe_text
)
MavenMaven_Mapper_strategy = st.builds(
    MavenMaven_Mapper,
    classname=
        safe_text,
    to=
        safe_text,
    classpath=
        safe_text,
    classpathref=
        safe_text,
    from_=
        safe_text,
    type=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
MavenMaven_Set_strategy = st.builds(
    MavenMaven_Set,
)
MavenMaven_Basic_strategy = st.builds(
    MavenMaven_Basic,
)
JellyCommand_strategy = st.builds(
    JellyCommand,
)
MavenMaven_JellyForEach_strategy = st.builds(
    MavenMaven_JellyForEach,
    indexVar=
        safe_text,
    items=
        safe_text,
    var=
        safe_text
)
MavenMaven_JellySet_strategy = st.builds(
    MavenMaven_JellySet,
    value=
        safe_text,
    var=
        safe_text
)
MavenMaven_JellyCommand_strategy = st.builds(
    MavenMaven_JellyCommand,
)
MavenMaven_AntPropertyEnv_strategy = st.builds(
    MavenMaven_AntPropertyEnv,
    environment=
        safe_text
)
MavenMaven_AntPropertyFile_strategy = st.builds(
    MavenMaven_AntPropertyFile,
    file=
        safe_text
)
MavenMaven_AntPropertyLocation_strategy = st.builds(
    MavenMaven_AntPropertyLocation,
    location=
        safe_text
)
MavenMaven_PreGoal_strategy = st.builds(
    MavenMaven_PreGoal,
)
AbstractGoal_strategy = st.builds(
    AbstractGoal,
)
MavenMaven_Goal_strategy = st.builds(
    MavenMaven_Goal,
    name=
        safe_text
)
MavenMaven_PrePostGoal_strategy = st.builds(
    MavenMaven_PrePostGoal,
)

@given(instance=MavenMaven_ContentsGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_contentsgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_ContentsGoal)

@given(instance=MavenMaven_AbstractGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_abstractgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_AbstractGoal)

@given(instance=Goal_strategy)
@settings(max_examples=50)
def test_goal_instantiation(instance):
    assert isinstance(instance, Goal)

@given(instance=Xmlns_strategy)
@settings(max_examples=50)
def test_xmlns_instantiation(instance):
    assert isinstance(instance, Xmlns)

@given(instance=MavenMaven_Project_strategy)
@settings(max_examples=50)
def test_mavenmaven_project_instantiation(instance):
    assert isinstance(instance, MavenMaven_Project)

@given(instance=AntPropertyName_strategy)
@settings(max_examples=50)
def test_antpropertyname_instantiation(instance):
    assert isinstance(instance, AntPropertyName)

@given(instance=MavenMaven_AntPropertyValue_strategy)
@settings(max_examples=50)
def test_mavenmaven_antpropertyvalue_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntPropertyValue)



@given(instance=MavenMaven_AntPropertyValue_strategy)
def test_mavenmaven_antpropertyvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ContentsGoal_strategy)
@settings(max_examples=50)
def test_contentsgoal_instantiation(instance):
    assert isinstance(instance, ContentsGoal)

@given(instance=MavenMaven_AttainGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_attaingoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_AttainGoal)

@given(instance=MavenMaven_AntProperty_strategy)
@settings(max_examples=50)
def test_mavenmaven_antproperty_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntProperty)

@given(instance=MavenMaven_Xmlns_strategy)
@settings(max_examples=50)
def test_mavenmaven_xmlns_instantiation(instance):
    assert isinstance(instance, MavenMaven_Xmlns)



@given(instance=MavenMaven_Xmlns_strategy)
def test_mavenmaven_xmlns_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MavenMaven_Xmlns_strategy)
def test_mavenmaven_xmlns_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PrePostGoal_strategy)
@settings(max_examples=50)
def test_prepostgoal_instantiation(instance):
    assert isinstance(instance, PrePostGoal)

@given(instance=AntTaskDef_strategy)
@settings(max_examples=50)
def test_anttaskdef_instantiation(instance):
    assert isinstance(instance, AntTaskDef)

@given(instance=AntProperty_strategy)
@settings(max_examples=50)
def test_antproperty_instantiation(instance):
    assert isinstance(instance, AntProperty)

@given(instance=MavenMaven_AntPropertyName_strategy)
@settings(max_examples=50)
def test_mavenmaven_antpropertyname_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntPropertyName)



@given(instance=MavenMaven_AntPropertyName_strategy)
def test_mavenmaven_antpropertyname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Path_strategy)
@settings(max_examples=50)
def test_path_instantiation(instance):
    assert isinstance(instance, Path)

@given(instance=FileTask_strategy)
@settings(max_examples=50)
def test_filetask_instantiation(instance):
    assert isinstance(instance, FileTask)

@given(instance=MavenMaven_Copy_strategy)
@settings(max_examples=50)
def test_mavenmaven_copy_instantiation(instance):
    assert isinstance(instance, MavenMaven_Copy)



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_flatten_setter(instance):
    original = instance.flatten
    instance.flatten = original
    assert instance.flatten == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_overwrite_setter(instance):
    original = instance.overwrite
    instance.overwrite = original
    assert instance.overwrite == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_todir_setter(instance):
    original = instance.todir
    instance.todir = original
    assert instance.todir == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_tofile_setter(instance):
    original = instance.tofile
    instance.tofile = original
    assert instance.tofile == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_presservelastmodified_setter(instance):
    original = instance.presservelastmodified
    instance.presservelastmodified = original
    assert instance.presservelastmodified == original



@given(instance=MavenMaven_Copy_strategy)
def test_mavenmaven_copy_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven_Mkdir_strategy)
@settings(max_examples=50)
def test_mavenmaven_mkdir_instantiation(instance):
    assert isinstance(instance, MavenMaven_Mkdir)



@given(instance=MavenMaven_Mkdir_strategy)
def test_mavenmaven_mkdir_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven_Delete_strategy)
@settings(max_examples=50)
def test_mavenmaven_delete_instantiation(instance):
    assert isinstance(instance, MavenMaven_Delete)



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_quiet_setter(instance):
    original = instance.quiet
    instance.quiet = original
    assert instance.quiet == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_excludesfile_setter(instance):
    original = instance.excludesfile
    instance.excludesfile = original
    assert instance.excludesfile == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_failonerror_setter(instance):
    original = instance.failonerror
    instance.failonerror = original
    assert instance.failonerror == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_includesfile_setter(instance):
    original = instance.includesfile
    instance.includesfile = original
    assert instance.includesfile == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original



@given(instance=MavenMaven_Delete_strategy)
def test_mavenmaven_delete_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Mapper_strategy)
@settings(max_examples=50)
def test_mapper_instantiation(instance):
    assert isinstance(instance, Mapper)

@given(instance=FilterSet_strategy)
@settings(max_examples=50)
def test_filterset_instantiation(instance):
    assert isinstance(instance, FilterSet)

@given(instance=DocumentationTask_strategy)
@settings(max_examples=50)
def test_documentationtask_instantiation(instance):
    assert isinstance(instance, DocumentationTask)

@given(instance=MavenMaven_Javadoc_strategy)
@settings(max_examples=50)
def test_mavenmaven_javadoc_instantiation(instance):
    assert isinstance(instance, MavenMaven_Javadoc)



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_packagenames_setter(instance):
    original = instance.packagenames
    instance.packagenames = original
    assert instance.packagenames == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_windowtitle_setter(instance):
    original = instance.windowtitle
    instance.windowtitle = original
    assert instance.windowtitle == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_sourcepath_setter(instance):
    original = instance.sourcepath
    instance.sourcepath = original
    assert instance.sourcepath == original



@given(instance=MavenMaven_Javadoc_strategy)
def test_mavenmaven_javadoc_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original

@given(instance=ArchiveTask_strategy)
@settings(max_examples=50)
def test_archivetask_instantiation(instance):
    assert isinstance(instance, ArchiveTask)

@given(instance=MavenMaven_Jar_strategy)
@settings(max_examples=50)
def test_mavenmaven_jar_instantiation(instance):
    assert isinstance(instance, MavenMaven_Jar)



@given(instance=MavenMaven_Jar_strategy)
def test_mavenmaven_jar_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original



@given(instance=MavenMaven_Jar_strategy)
def test_mavenmaven_jar_jarfile_setter(instance):
    original = instance.jarfile
    instance.jarfile = original
    assert instance.jarfile == original



@given(instance=MavenMaven_Jar_strategy)
def test_mavenmaven_jar_manifest_setter(instance):
    original = instance.manifest
    instance.manifest = original
    assert instance.manifest == original



@given(instance=MavenMaven_Jar_strategy)
def test_mavenmaven_jar_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original



@given(instance=MavenMaven_Jar_strategy)
def test_mavenmaven_jar_compress_setter(instance):
    original = instance.compress
    instance.compress = original
    assert instance.compress == original

@given(instance=MavenMaven_FormatTstamp_strategy)
@settings(max_examples=50)
def test_mavenmaven_formattstamp_instantiation(instance):
    assert isinstance(instance, MavenMaven_FormatTstamp)



@given(instance=MavenMaven_FormatTstamp_strategy)
def test_mavenmaven_formattstamp_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=MavenMaven_FormatTstamp_strategy)
def test_mavenmaven_formattstamp_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original



@given(instance=MavenMaven_FormatTstamp_strategy)
def test_mavenmaven_formattstamp_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=MavenMaven_FormatTstamp_strategy)
def test_mavenmaven_formattstamp_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original



@given(instance=MavenMaven_FormatTstamp_strategy)
def test_mavenmaven_formattstamp_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original

@given(instance=CompileTask_strategy)
@settings(max_examples=50)
def test_compiletask_instantiation(instance):
    assert isinstance(instance, CompileTask)

@given(instance=MavenMaven_Javac_strategy)
@settings(max_examples=50)
def test_mavenmaven_javac_instantiation(instance):
    assert isinstance(instance, MavenMaven_Javac)



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_deprecation_setter(instance):
    original = instance.deprecation
    instance.deprecation = original
    assert instance.deprecation == original



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_srcdir_setter(instance):
    original = instance.srcdir
    instance.srcdir = original
    assert instance.srcdir == original



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_optimize_setter(instance):
    original = instance.optimize
    instance.optimize = original
    assert instance.optimize == original



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original



@given(instance=MavenMaven_Javac_strategy)
def test_mavenmaven_javac_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=ExecutionTask_strategy)
@settings(max_examples=50)
def test_executiontask_instantiation(instance):
    assert isinstance(instance, ExecutionTask)

@given(instance=MavenMaven_Java_strategy)
@settings(max_examples=50)
def test_mavenmaven_java_instantiation(instance):
    assert isinstance(instance, MavenMaven_Java)



@given(instance=MavenMaven_Java_strategy)
def test_mavenmaven_java_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=MavenMaven_Java_strategy)
def test_mavenmaven_java_jar_setter(instance):
    original = instance.jar
    instance.jar = original
    assert instance.jar == original



@given(instance=MavenMaven_Java_strategy)
def test_mavenmaven_java_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=MavenMaven_Exec_strategy)
@settings(max_examples=50)
def test_mavenmaven_exec_instantiation(instance):
    assert isinstance(instance, MavenMaven_Exec)



@given(instance=MavenMaven_Exec_strategy)
def test_mavenmaven_exec_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original



@given(instance=MavenMaven_Exec_strategy)
def test_mavenmaven_exec_executable_setter(instance):
    original = instance.executable
    instance.executable = original
    assert instance.executable == original

@given(instance=FormatTstamp_strategy)
@settings(max_examples=50)
def test_formattstamp_instantiation(instance):
    assert isinstance(instance, FormatTstamp)

@given(instance=MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MiscellaneousTask)

@given(instance=MavenMaven_Tstamp_strategy)
@settings(max_examples=50)
def test_mavenmaven_tstamp_instantiation(instance):
    assert isinstance(instance, MavenMaven_Tstamp)

@given(instance=MavenMaven_Echo_strategy)
@settings(max_examples=50)
def test_mavenmaven_echo_instantiation(instance):
    assert isinstance(instance, MavenMaven_Echo)



@given(instance=MavenMaven_Echo_strategy)
def test_mavenmaven_echo_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=MavenMaven_Echo_strategy)
def test_mavenmaven_echo_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=MavenMaven_Echo_strategy)
def test_mavenmaven_echo_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

@given(instance=ClassPath_strategy)
@settings(max_examples=50)
def test_classpath_instantiation(instance):
    assert isinstance(instance, ClassPath)

@given(instance=MavenMaven_AntTaskDef_strategy)
@settings(max_examples=50)
def test_mavenmaven_anttaskdef_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntTaskDef)



@given(instance=MavenMaven_AntTaskDef_strategy)
def test_mavenmaven_anttaskdef_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=MavenMaven_AntTaskDef_strategy)
def test_mavenmaven_anttaskdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven_Task_strategy)
@settings(max_examples=50)
def test_mavenmaven_task_instantiation(instance):
    assert isinstance(instance, MavenMaven_Task)

@given(instance=PreDefinedTask_strategy)
@settings(max_examples=50)
def test_predefinedtask_instantiation(instance):
    assert isinstance(instance, PreDefinedTask)

@given(instance=MavenMaven_MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MavenMaven_MiscellaneousTask)

@given(instance=MavenMaven_DocumentationTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_documentationtask_instantiation(instance):
    assert isinstance(instance, MavenMaven_DocumentationTask)

@given(instance=MavenMaven_FileTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_filetask_instantiation(instance):
    assert isinstance(instance, MavenMaven_FileTask)

@given(instance=MavenMaven_CompileTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_compiletask_instantiation(instance):
    assert isinstance(instance, MavenMaven_CompileTask)

@given(instance=MavenMaven_ArchiveTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_archivetask_instantiation(instance):
    assert isinstance(instance, MavenMaven_ArchiveTask)

@given(instance=MavenMaven_ExecutionTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_executiontask_instantiation(instance):
    assert isinstance(instance, MavenMaven_ExecutionTask)

@given(instance=MavenMaven_Attribut_strategy)
@settings(max_examples=50)
def test_mavenmaven_attribut_instantiation(instance):
    assert isinstance(instance, MavenMaven_Attribut)



@given(instance=MavenMaven_Attribut_strategy)
def test_mavenmaven_attribut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=MavenMaven_Attribut_strategy)
def test_mavenmaven_attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Attribut_strategy)
@settings(max_examples=50)
def test_attribut_instantiation(instance):
    assert isinstance(instance, Attribut)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=MavenMaven_PreDefinedTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_predefinedtask_instantiation(instance):
    assert isinstance(instance, MavenMaven_PreDefinedTask)



@given(instance=MavenMaven_PreDefinedTask_strategy)
def test_mavenmaven_predefinedtask_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=MavenMaven_PreDefinedTask_strategy)
def test_mavenmaven_predefinedtask_taskname_setter(instance):
    original = instance.taskname
    instance.taskname = original
    assert instance.taskname == original



@given(instance=MavenMaven_PreDefinedTask_strategy)
def test_mavenmaven_predefinedtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenMaven_NewTask_strategy)
@settings(max_examples=50)
def test_mavenmaven_newtask_instantiation(instance):
    assert isinstance(instance, MavenMaven_NewTask)

@given(instance=FiltersFile_strategy)
@settings(max_examples=50)
def test_filtersfile_instantiation(instance):
    assert isinstance(instance, FiltersFile)

@given(instance=Filter_strategy)
@settings(max_examples=50)
def test_filter_instantiation(instance):
    assert isinstance(instance, Filter)

@given(instance=FileSet_strategy)
@settings(max_examples=50)
def test_fileset_instantiation(instance):
    assert isinstance(instance, FileSet)

@given(instance=PathElement_strategy)
@settings(max_examples=50)
def test_pathelement_instantiation(instance):
    assert isinstance(instance, PathElement)

@given(instance=Set_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, Set)

@given(instance=MavenMaven_ClassPath_strategy)
@settings(max_examples=50)
def test_mavenmaven_classpath_instantiation(instance):
    assert isinstance(instance, MavenMaven_ClassPath)



@given(instance=MavenMaven_ClassPath_strategy)
def test_mavenmaven_classpath_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=MavenMaven_Path_strategy)
@settings(max_examples=50)
def test_mavenmaven_path_instantiation(instance):
    assert isinstance(instance, MavenMaven_Path)



@given(instance=MavenMaven_Path_strategy)
def test_mavenmaven_path_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original



@given(instance=MavenMaven_Path_strategy)
def test_mavenmaven_path_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenMaven_PatternSet_strategy)
@settings(max_examples=50)
def test_mavenmaven_patternset_instantiation(instance):
    assert isinstance(instance, MavenMaven_PatternSet)

@given(instance=MavenMaven_FilterSet_strategy)
@settings(max_examples=50)
def test_mavenmaven_filterset_instantiation(instance):
    assert isinstance(instance, MavenMaven_FilterSet)



@given(instance=MavenMaven_FilterSet_strategy)
def test_mavenmaven_filterset_endtoken_setter(instance):
    original = instance.endtoken
    instance.endtoken = original
    assert instance.endtoken == original



@given(instance=MavenMaven_FilterSet_strategy)
def test_mavenmaven_filterset_starttoken_setter(instance):
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

@given(instance=MavenMaven_FileSet_strategy)
@settings(max_examples=50)
def test_mavenmaven_fileset_instantiation(instance):
    assert isinstance(instance, MavenMaven_FileSet)



@given(instance=MavenMaven_FileSet_strategy)
def test_mavenmaven_fileset_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven_Pattern_strategy)
@settings(max_examples=50)
def test_mavenmaven_pattern_instantiation(instance):
    assert isinstance(instance, MavenMaven_Pattern)

@given(instance=PostGoal_strategy)
@settings(max_examples=50)
def test_postgoal_instantiation(instance):
    assert isinstance(instance, PostGoal)

@given(instance=PreGoal_strategy)
@settings(max_examples=50)
def test_pregoal_instantiation(instance):
    assert isinstance(instance, PreGoal)

@given(instance=MavenMaven_PostGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_postgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_PostGoal)

@given(instance=InExcludes_strategy)
@settings(max_examples=50)
def test_inexcludes_instantiation(instance):
    assert isinstance(instance, InExcludes)

@given(instance=MavenMaven_ExcludesFile_strategy)
@settings(max_examples=50)
def test_mavenmaven_excludesfile_instantiation(instance):
    assert isinstance(instance, MavenMaven_ExcludesFile)

@given(instance=MavenMaven_IncludesFile_strategy)
@settings(max_examples=50)
def test_mavenmaven_includesfile_instantiation(instance):
    assert isinstance(instance, MavenMaven_IncludesFile)

@given(instance=MavenMaven_Excludes_strategy)
@settings(max_examples=50)
def test_mavenmaven_excludes_instantiation(instance):
    assert isinstance(instance, MavenMaven_Excludes)

@given(instance=MavenMaven_Includes_strategy)
@settings(max_examples=50)
def test_mavenmaven_includes_instantiation(instance):
    assert isinstance(instance, MavenMaven_Includes)

@given(instance=Basic_strategy)
@settings(max_examples=50)
def test_basic_instantiation(instance):
    assert isinstance(instance, Basic)

@given(instance=MavenMaven_Filter_strategy)
@settings(max_examples=50)
def test_mavenmaven_filter_instantiation(instance):
    assert isinstance(instance, MavenMaven_Filter)



@given(instance=MavenMaven_Filter_strategy)
def test_mavenmaven_filter_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original



@given(instance=MavenMaven_Filter_strategy)
def test_mavenmaven_filter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MavenMaven_InExcludes_strategy)
@settings(max_examples=50)
def test_mavenmaven_inexcludes_instantiation(instance):
    assert isinstance(instance, MavenMaven_InExcludes)



@given(instance=MavenMaven_InExcludes_strategy)
def test_mavenmaven_inexcludes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=MavenMaven_InExcludes_strategy)
def test_mavenmaven_inexcludes_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original



@given(instance=MavenMaven_InExcludes_strategy)
def test_mavenmaven_inexcludes_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original

@given(instance=MavenMaven_FileList_strategy)
@settings(max_examples=50)
def test_mavenmaven_filelist_instantiation(instance):
    assert isinstance(instance, MavenMaven_FileList)



@given(instance=MavenMaven_FileList_strategy)
def test_mavenmaven_filelist_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original



@given(instance=MavenMaven_FileList_strategy)
def test_mavenmaven_filelist_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=MavenMaven_PathElement_strategy)
@settings(max_examples=50)
def test_mavenmaven_pathelement_instantiation(instance):
    assert isinstance(instance, MavenMaven_PathElement)



@given(instance=MavenMaven_PathElement_strategy)
def test_mavenmaven_pathelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=MavenMaven_PathElement_strategy)
def test_mavenmaven_pathelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=MavenMaven_FiltersFile_strategy)
@settings(max_examples=50)
def test_mavenmaven_filtersfile_instantiation(instance):
    assert isinstance(instance, MavenMaven_FiltersFile)



@given(instance=MavenMaven_FiltersFile_strategy)
def test_mavenmaven_filtersfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven_Mapper_strategy)
@settings(max_examples=50)
def test_mavenmaven_mapper_instantiation(instance):
    assert isinstance(instance, MavenMaven_Mapper)



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_classpath_setter(instance):
    original = instance.classpath
    instance.classpath = original
    assert instance.classpath == original



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_classpathref_setter(instance):
    original = instance.classpathref
    instance.classpathref = original
    assert instance.classpathref == original



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original



@given(instance=MavenMaven_Mapper_strategy)
def test_mavenmaven_mapper_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=MavenMaven_Set_strategy)
@settings(max_examples=50)
def test_mavenmaven_set_instantiation(instance):
    assert isinstance(instance, MavenMaven_Set)

@given(instance=MavenMaven_Basic_strategy)
@settings(max_examples=50)
def test_mavenmaven_basic_instantiation(instance):
    assert isinstance(instance, MavenMaven_Basic)

@given(instance=JellyCommand_strategy)
@settings(max_examples=50)
def test_jellycommand_instantiation(instance):
    assert isinstance(instance, JellyCommand)

@given(instance=MavenMaven_JellyForEach_strategy)
@settings(max_examples=50)
def test_mavenmaven_jellyforeach_instantiation(instance):
    assert isinstance(instance, MavenMaven_JellyForEach)



@given(instance=MavenMaven_JellyForEach_strategy)
def test_mavenmaven_jellyforeach_indexVar_setter(instance):
    original = instance.indexVar
    instance.indexVar = original
    assert instance.indexVar == original



@given(instance=MavenMaven_JellyForEach_strategy)
def test_mavenmaven_jellyforeach_items_setter(instance):
    original = instance.items
    instance.items = original
    assert instance.items == original



@given(instance=MavenMaven_JellyForEach_strategy)
def test_mavenmaven_jellyforeach_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=MavenMaven_JellySet_strategy)
@settings(max_examples=50)
def test_mavenmaven_jellyset_instantiation(instance):
    assert isinstance(instance, MavenMaven_JellySet)



@given(instance=MavenMaven_JellySet_strategy)
def test_mavenmaven_jellyset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=MavenMaven_JellySet_strategy)
def test_mavenmaven_jellyset_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=MavenMaven_JellyCommand_strategy)
@settings(max_examples=50)
def test_mavenmaven_jellycommand_instantiation(instance):
    assert isinstance(instance, MavenMaven_JellyCommand)

@given(instance=MavenMaven_AntPropertyEnv_strategy)
@settings(max_examples=50)
def test_mavenmaven_antpropertyenv_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntPropertyEnv)



@given(instance=MavenMaven_AntPropertyEnv_strategy)
def test_mavenmaven_antpropertyenv_environment_setter(instance):
    original = instance.environment
    instance.environment = original
    assert instance.environment == original

@given(instance=MavenMaven_AntPropertyFile_strategy)
@settings(max_examples=50)
def test_mavenmaven_antpropertyfile_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntPropertyFile)



@given(instance=MavenMaven_AntPropertyFile_strategy)
def test_mavenmaven_antpropertyfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven_AntPropertyLocation_strategy)
@settings(max_examples=50)
def test_mavenmaven_antpropertylocation_instantiation(instance):
    assert isinstance(instance, MavenMaven_AntPropertyLocation)



@given(instance=MavenMaven_AntPropertyLocation_strategy)
def test_mavenmaven_antpropertylocation_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=MavenMaven_PreGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_pregoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_PreGoal)

@given(instance=AbstractGoal_strategy)
@settings(max_examples=50)
def test_abstractgoal_instantiation(instance):
    assert isinstance(instance, AbstractGoal)

@given(instance=MavenMaven_Goal_strategy)
@settings(max_examples=50)
def test_mavenmaven_goal_instantiation(instance):
    assert isinstance(instance, MavenMaven_Goal)



@given(instance=MavenMaven_Goal_strategy)
def test_mavenmaven_goal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven_PrePostGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven_prepostgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven_PrePostGoal)
