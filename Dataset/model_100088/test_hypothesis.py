import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DocumentationTask,
    MavenMaven::Javadoc,
    CompileTask,
    MavenMaven::Javac,
    FileTask,
    MavenMaven::Delete,
    MavenMaven::Copy,
    MavenMaven::Mkdir,
    ArchiveTask,
    MavenMaven::Jar,
    ExecutionTask,
    MavenMaven::Java,
    MavenMaven::Exec,
    PreDefinedTask,
    MavenMaven::FileTask,
    MavenMaven::ArchiveTask,
    MavenMaven::DocumentationTask,
    MavenMaven::ExecutionTask,
    MavenMaven::Attribut,
    MavenMaven::CompileTask,
    MavenMaven::FormatTstamp,
    MiscellaneousTask,
    MavenMaven::Tstamp,
    MavenMaven::Echo,
    MavenMaven::MiscellaneousTask,
    Task,
    MavenMaven::PreDefinedTask,
    MavenMaven::NewTask,
    InExcludes,
    MavenMaven::IncludesFile,
    MavenMaven::Excludes,
    MavenMaven::ExcludesFile,
    MavenMaven::Includes,
    Basic,
    MavenMaven::Filter,
    MavenMaven::FileList,
    MavenMaven::InExcludes,
    MavenMaven::Mapper,
    Pattern,
    MavenMaven::Basic,
    Set,
    MavenMaven::FilterSet,
    MavenMaven::FileSet,
    MavenMaven::ClassPath,
    MavenMaven::PatternSet,
    MavenMaven::Set,
    MavenMaven::PathElement,
    MavenMaven::FiltersFile,
    MavenMaven::ContentsGoal,
    MavenMaven::AbstractGoal,
    JellyCommand,
    MavenMaven::JellySet,
    MavenMaven::Pattern,
    PrePostGoal,
    MavenMaven::PostGoal,
    MavenMaven::PreGoal,
    AbstractGoal,
    MavenMaven::Path,
    MavenMaven::Goal,
    MavenMaven::Xmlns,
    MavenMaven::Project,
    AntPropertyName,
    MavenMaven::AntPropertyLocation,
    MavenMaven::AntPropertyValue,
    AntProperty,
    MavenMaven::AntPropertyEnv,
    MavenMaven::AntPropertyFile,
    MavenMaven::AntPropertyName,
    ContentsGoal,
    MavenMaven::JellyCommand,
    MavenMaven::AntProperty,
    MavenMaven::AttainGoal,
    MavenMaven::Task,
    MavenMaven::PrePostGoal,
    MavenMaven::AntTaskDef,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_documentationtask_is_not_abstract():
    assert not inspect.isabstract(DocumentationTask)


def test_documentationtask_constructor_exists():
    assert callable(DocumentationTask.__init__)


def test_documentationtask_constructor_args():
    sig = inspect.signature(DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::javadoc_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Javadoc)


def test_mavenmaven::javadoc_constructor_exists():
    assert callable(MavenMaven::Javadoc.__init__)


def test_mavenmaven::javadoc_constructor_args():
    sig = inspect.signature(MavenMaven::Javadoc.__init__)
    params = list(sig.parameters.keys())
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "use" in params, "Missing parameter 'use'"
    assert "author" in params, "Missing parameter 'author'"
    assert "version" in params, "Missing parameter 'version'"
    assert "windowtitle" in params, "Missing parameter 'windowtitle'"
    assert "sourcepath" in params, "Missing parameter 'sourcepath'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "packagenames" in params, "Missing parameter 'packagenames'"

def test_mavenmaven::javadoc_has_destdir():
    assert hasattr(MavenMaven::Javadoc, "destdir")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_use():
    assert hasattr(MavenMaven::Javadoc, "use")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_author():
    assert hasattr(MavenMaven::Javadoc, "author")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_version():
    assert hasattr(MavenMaven::Javadoc, "version")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_windowtitle():
    assert hasattr(MavenMaven::Javadoc, "windowtitle")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "windowtitle" in klass.__dict__:
            descriptor = klass.__dict__["windowtitle"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_sourcepath():
    assert hasattr(MavenMaven::Javadoc, "sourcepath")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "sourcepath" in klass.__dict__:
            descriptor = klass.__dict__["sourcepath"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_defaultexcludes():
    assert hasattr(MavenMaven::Javadoc, "defaultexcludes")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javadoc_has_packagenames():
    assert hasattr(MavenMaven::Javadoc, "packagenames")
    descriptor = None
    for klass in MavenMaven::Javadoc.__mro__:
        if "packagenames" in klass.__dict__:
            descriptor = klass.__dict__["packagenames"]
            break
    assert isinstance(descriptor, property)



def test_compiletask_is_not_abstract():
    assert not inspect.isabstract(CompileTask)


def test_compiletask_constructor_exists():
    assert callable(CompileTask.__init__)


def test_compiletask_constructor_args():
    sig = inspect.signature(CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::javac_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Javac)


def test_mavenmaven::javac_constructor_exists():
    assert callable(MavenMaven::Javac.__init__)


def test_mavenmaven::javac_constructor_args():
    sig = inspect.signature(MavenMaven::Javac.__init__)
    params = list(sig.parameters.keys())
    assert "optimize" in params, "Missing parameter 'optimize'"
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "deprecation" in params, "Missing parameter 'deprecation'"
    assert "srcdir" in params, "Missing parameter 'srcdir'"
    assert "fork" in params, "Missing parameter 'fork'"
    assert "debug" in params, "Missing parameter 'debug'"

def test_mavenmaven::javac_has_optimize():
    assert hasattr(MavenMaven::Javac, "optimize")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "optimize" in klass.__dict__:
            descriptor = klass.__dict__["optimize"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javac_has_destdir():
    assert hasattr(MavenMaven::Javac, "destdir")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javac_has_deprecation():
    assert hasattr(MavenMaven::Javac, "deprecation")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "deprecation" in klass.__dict__:
            descriptor = klass.__dict__["deprecation"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javac_has_srcdir():
    assert hasattr(MavenMaven::Javac, "srcdir")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "srcdir" in klass.__dict__:
            descriptor = klass.__dict__["srcdir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javac_has_fork():
    assert hasattr(MavenMaven::Javac, "fork")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::javac_has_debug():
    assert hasattr(MavenMaven::Javac, "debug")
    descriptor = None
    for klass in MavenMaven::Javac.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_filetask_is_not_abstract():
    assert not inspect.isabstract(FileTask)


def test_filetask_constructor_exists():
    assert callable(FileTask.__init__)


def test_filetask_constructor_args():
    sig = inspect.signature(FileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::delete_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Delete)


def test_mavenmaven::delete_constructor_exists():
    assert callable(MavenMaven::Delete.__init__)


def test_mavenmaven::delete_constructor_args():
    sig = inspect.signature(MavenMaven::Delete.__init__)
    params = list(sig.parameters.keys())
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "failonerror" in params, "Missing parameter 'failonerror'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "dir" in params, "Missing parameter 'dir'"
    assert "file" in params, "Missing parameter 'file'"
    assert "excludesfile" in params, "Missing parameter 'excludesfile'"
    assert "quiet" in params, "Missing parameter 'quiet'"
    assert "excludes" in params, "Missing parameter 'excludes'"
    assert "includesfile" in params, "Missing parameter 'includesfile'"
    assert "verbose" in params, "Missing parameter 'verbose'"

def test_mavenmaven::delete_has_includeEmptyDirs():
    assert hasattr(MavenMaven::Delete, "includeEmptyDirs")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_includes():
    assert hasattr(MavenMaven::Delete, "includes")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_failonerror():
    assert hasattr(MavenMaven::Delete, "failonerror")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "failonerror" in klass.__dict__:
            descriptor = klass.__dict__["failonerror"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_defaultexcludes():
    assert hasattr(MavenMaven::Delete, "defaultexcludes")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_dir():
    assert hasattr(MavenMaven::Delete, "dir")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_file():
    assert hasattr(MavenMaven::Delete, "file")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_excludesfile():
    assert hasattr(MavenMaven::Delete, "excludesfile")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "excludesfile" in klass.__dict__:
            descriptor = klass.__dict__["excludesfile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_quiet():
    assert hasattr(MavenMaven::Delete, "quiet")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "quiet" in klass.__dict__:
            descriptor = klass.__dict__["quiet"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_excludes():
    assert hasattr(MavenMaven::Delete, "excludes")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_includesfile():
    assert hasattr(MavenMaven::Delete, "includesfile")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "includesfile" in klass.__dict__:
            descriptor = klass.__dict__["includesfile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::delete_has_verbose():
    assert hasattr(MavenMaven::Delete, "verbose")
    descriptor = None
    for klass in MavenMaven::Delete.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::copy_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Copy)


def test_mavenmaven::copy_constructor_exists():
    assert callable(MavenMaven::Copy.__init__)


def test_mavenmaven::copy_constructor_args():
    sig = inspect.signature(MavenMaven::Copy.__init__)
    params = list(sig.parameters.keys())
    assert "flatten" in params, "Missing parameter 'flatten'"
    assert "overwrite" in params, "Missing parameter 'overwrite'"
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "todir" in params, "Missing parameter 'todir'"
    assert "presservelastmodified" in params, "Missing parameter 'presservelastmodified'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "tofile" in params, "Missing parameter 'tofile'"
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven::copy_has_flatten():
    assert hasattr(MavenMaven::Copy, "flatten")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "flatten" in klass.__dict__:
            descriptor = klass.__dict__["flatten"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_overwrite():
    assert hasattr(MavenMaven::Copy, "overwrite")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "overwrite" in klass.__dict__:
            descriptor = klass.__dict__["overwrite"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_filtering():
    assert hasattr(MavenMaven::Copy, "filtering")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_todir():
    assert hasattr(MavenMaven::Copy, "todir")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "todir" in klass.__dict__:
            descriptor = klass.__dict__["todir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_presservelastmodified():
    assert hasattr(MavenMaven::Copy, "presservelastmodified")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "presservelastmodified" in klass.__dict__:
            descriptor = klass.__dict__["presservelastmodified"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_includeEmptyDirs():
    assert hasattr(MavenMaven::Copy, "includeEmptyDirs")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_tofile():
    assert hasattr(MavenMaven::Copy, "tofile")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "tofile" in klass.__dict__:
            descriptor = klass.__dict__["tofile"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::copy_has_file():
    assert hasattr(MavenMaven::Copy, "file")
    descriptor = None
    for klass in MavenMaven::Copy.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::mkdir_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Mkdir)


def test_mavenmaven::mkdir_constructor_exists():
    assert callable(MavenMaven::Mkdir.__init__)


def test_mavenmaven::mkdir_constructor_args():
    sig = inspect.signature(MavenMaven::Mkdir.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven::mkdir_has_dir():
    assert hasattr(MavenMaven::Mkdir, "dir")
    descriptor = None
    for klass in MavenMaven::Mkdir.__mro__:
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



def test_mavenmaven::jar_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Jar)


def test_mavenmaven::jar_constructor_exists():
    assert callable(MavenMaven::Jar.__init__)


def test_mavenmaven::jar_constructor_args():
    sig = inspect.signature(MavenMaven::Jar.__init__)
    params = list(sig.parameters.keys())
    assert "manifest" in params, "Missing parameter 'manifest'"
    assert "basedir" in params, "Missing parameter 'basedir'"
    assert "compress" in params, "Missing parameter 'compress'"
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "jarfile" in params, "Missing parameter 'jarfile'"

def test_mavenmaven::jar_has_manifest():
    assert hasattr(MavenMaven::Jar, "manifest")
    descriptor = None
    for klass in MavenMaven::Jar.__mro__:
        if "manifest" in klass.__dict__:
            descriptor = klass.__dict__["manifest"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::jar_has_basedir():
    assert hasattr(MavenMaven::Jar, "basedir")
    descriptor = None
    for klass in MavenMaven::Jar.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::jar_has_compress():
    assert hasattr(MavenMaven::Jar, "compress")
    descriptor = None
    for klass in MavenMaven::Jar.__mro__:
        if "compress" in klass.__dict__:
            descriptor = klass.__dict__["compress"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::jar_has_encoding():
    assert hasattr(MavenMaven::Jar, "encoding")
    descriptor = None
    for klass in MavenMaven::Jar.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::jar_has_jarfile():
    assert hasattr(MavenMaven::Jar, "jarfile")
    descriptor = None
    for klass in MavenMaven::Jar.__mro__:
        if "jarfile" in klass.__dict__:
            descriptor = klass.__dict__["jarfile"]
            break
    assert isinstance(descriptor, property)



def test_executiontask_is_not_abstract():
    assert not inspect.isabstract(ExecutionTask)


def test_executiontask_constructor_exists():
    assert callable(ExecutionTask.__init__)


def test_executiontask_constructor_args():
    sig = inspect.signature(ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::java_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Java)


def test_mavenmaven::java_constructor_exists():
    assert callable(MavenMaven::Java.__init__)


def test_mavenmaven::java_constructor_args():
    sig = inspect.signature(MavenMaven::Java.__init__)
    params = list(sig.parameters.keys())
    assert "jar" in params, "Missing parameter 'jar'"
    assert "fork" in params, "Missing parameter 'fork'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_mavenmaven::java_has_jar():
    assert hasattr(MavenMaven::Java, "jar")
    descriptor = None
    for klass in MavenMaven::Java.__mro__:
        if "jar" in klass.__dict__:
            descriptor = klass.__dict__["jar"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::java_has_fork():
    assert hasattr(MavenMaven::Java, "fork")
    descriptor = None
    for klass in MavenMaven::Java.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::java_has_classname():
    assert hasattr(MavenMaven::Java, "classname")
    descriptor = None
    for klass in MavenMaven::Java.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::exec_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Exec)


def test_mavenmaven::exec_constructor_exists():
    assert callable(MavenMaven::Exec.__init__)


def test_mavenmaven::exec_constructor_args():
    sig = inspect.signature(MavenMaven::Exec.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "executable" in params, "Missing parameter 'executable'"

def test_mavenmaven::exec_has_dir():
    assert hasattr(MavenMaven::Exec, "dir")
    descriptor = None
    for klass in MavenMaven::Exec.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::exec_has_executable():
    assert hasattr(MavenMaven::Exec, "executable")
    descriptor = None
    for klass in MavenMaven::Exec.__mro__:
        if "executable" in klass.__dict__:
            descriptor = klass.__dict__["executable"]
            break
    assert isinstance(descriptor, property)



def test_predefinedtask_is_not_abstract():
    assert not inspect.isabstract(PreDefinedTask)


def test_predefinedtask_constructor_exists():
    assert callable(PreDefinedTask.__init__)


def test_predefinedtask_constructor_args():
    sig = inspect.signature(PreDefinedTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::filetask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FileTask)


def test_mavenmaven::filetask_constructor_exists():
    assert callable(MavenMaven::FileTask.__init__)


def test_mavenmaven::filetask_constructor_args():
    sig = inspect.signature(MavenMaven::FileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::archivetask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::ArchiveTask)


def test_mavenmaven::archivetask_constructor_exists():
    assert callable(MavenMaven::ArchiveTask.__init__)


def test_mavenmaven::archivetask_constructor_args():
    sig = inspect.signature(MavenMaven::ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::documentationtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::DocumentationTask)


def test_mavenmaven::documentationtask_constructor_exists():
    assert callable(MavenMaven::DocumentationTask.__init__)


def test_mavenmaven::documentationtask_constructor_args():
    sig = inspect.signature(MavenMaven::DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::executiontask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::ExecutionTask)


def test_mavenmaven::executiontask_constructor_exists():
    assert callable(MavenMaven::ExecutionTask.__init__)


def test_mavenmaven::executiontask_constructor_args():
    sig = inspect.signature(MavenMaven::ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::attribut_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Attribut)


def test_mavenmaven::attribut_constructor_exists():
    assert callable(MavenMaven::Attribut.__init__)


def test_mavenmaven::attribut_constructor_args():
    sig = inspect.signature(MavenMaven::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven::attribut_has_value():
    assert hasattr(MavenMaven::Attribut, "value")
    descriptor = None
    for klass in MavenMaven::Attribut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::attribut_has_name():
    assert hasattr(MavenMaven::Attribut, "name")
    descriptor = None
    for klass in MavenMaven::Attribut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::compiletask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::CompileTask)


def test_mavenmaven::compiletask_constructor_exists():
    assert callable(MavenMaven::CompileTask.__init__)


def test_mavenmaven::compiletask_constructor_args():
    sig = inspect.signature(MavenMaven::CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::formattstamp_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FormatTstamp)


def test_mavenmaven::formattstamp_constructor_exists():
    assert callable(MavenMaven::FormatTstamp.__init__)


def test_mavenmaven::formattstamp_constructor_args():
    sig = inspect.signature(MavenMaven::FormatTstamp.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "offset" in params, "Missing parameter 'offset'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "property" in params, "Missing parameter 'property'"

def test_mavenmaven::formattstamp_has_unit():
    assert hasattr(MavenMaven::FormatTstamp, "unit")
    descriptor = None
    for klass in MavenMaven::FormatTstamp.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::formattstamp_has_pattern():
    assert hasattr(MavenMaven::FormatTstamp, "pattern")
    descriptor = None
    for klass in MavenMaven::FormatTstamp.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::formattstamp_has_offset():
    assert hasattr(MavenMaven::FormatTstamp, "offset")
    descriptor = None
    for klass in MavenMaven::FormatTstamp.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::formattstamp_has_locale():
    assert hasattr(MavenMaven::FormatTstamp, "locale")
    descriptor = None
    for klass in MavenMaven::FormatTstamp.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::formattstamp_has_property():
    assert hasattr(MavenMaven::FormatTstamp, "property")
    descriptor = None
    for klass in MavenMaven::FormatTstamp.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)



def test_miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(MiscellaneousTask)


def test_miscellaneoustask_constructor_exists():
    assert callable(MiscellaneousTask.__init__)


def test_miscellaneoustask_constructor_args():
    sig = inspect.signature(MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::tstamp_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Tstamp)


def test_mavenmaven::tstamp_constructor_exists():
    assert callable(MavenMaven::Tstamp.__init__)


def test_mavenmaven::tstamp_constructor_args():
    sig = inspect.signature(MavenMaven::Tstamp.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::echo_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Echo)


def test_mavenmaven::echo_constructor_exists():
    assert callable(MavenMaven::Echo.__init__)


def test_mavenmaven::echo_constructor_args():
    sig = inspect.signature(MavenMaven::Echo.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "append" in params, "Missing parameter 'append'"
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven::echo_has_message():
    assert hasattr(MavenMaven::Echo, "message")
    descriptor = None
    for klass in MavenMaven::Echo.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::echo_has_append():
    assert hasattr(MavenMaven::Echo, "append")
    descriptor = None
    for klass in MavenMaven::Echo.__mro__:
        if "append" in klass.__dict__:
            descriptor = klass.__dict__["append"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::echo_has_file():
    assert hasattr(MavenMaven::Echo, "file")
    descriptor = None
    for klass in MavenMaven::Echo.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::MiscellaneousTask)


def test_mavenmaven::miscellaneoustask_constructor_exists():
    assert callable(MavenMaven::MiscellaneousTask.__init__)


def test_mavenmaven::miscellaneoustask_constructor_args():
    sig = inspect.signature(MavenMaven::MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::predefinedtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PreDefinedTask)


def test_mavenmaven::predefinedtask_constructor_exists():
    assert callable(MavenMaven::PreDefinedTask.__init__)


def test_mavenmaven::predefinedtask_constructor_args():
    sig = inspect.signature(MavenMaven::PreDefinedTask.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "taskname" in params, "Missing parameter 'taskname'"
    assert "id" in params, "Missing parameter 'id'"

def test_mavenmaven::predefinedtask_has_description():
    assert hasattr(MavenMaven::PreDefinedTask, "description")
    descriptor = None
    for klass in MavenMaven::PreDefinedTask.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::predefinedtask_has_taskname():
    assert hasattr(MavenMaven::PreDefinedTask, "taskname")
    descriptor = None
    for klass in MavenMaven::PreDefinedTask.__mro__:
        if "taskname" in klass.__dict__:
            descriptor = klass.__dict__["taskname"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::predefinedtask_has_id():
    assert hasattr(MavenMaven::PreDefinedTask, "id")
    descriptor = None
    for klass in MavenMaven::PreDefinedTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::newtask_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::NewTask)


def test_mavenmaven::newtask_constructor_exists():
    assert callable(MavenMaven::NewTask.__init__)


def test_mavenmaven::newtask_constructor_args():
    sig = inspect.signature(MavenMaven::NewTask.__init__)
    params = list(sig.parameters.keys())



def test_inexcludes_is_not_abstract():
    assert not inspect.isabstract(InExcludes)


def test_inexcludes_constructor_exists():
    assert callable(InExcludes.__init__)


def test_inexcludes_constructor_args():
    sig = inspect.signature(InExcludes.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::includesfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::IncludesFile)


def test_mavenmaven::includesfile_constructor_exists():
    assert callable(MavenMaven::IncludesFile.__init__)


def test_mavenmaven::includesfile_constructor_args():
    sig = inspect.signature(MavenMaven::IncludesFile.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::excludes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Excludes)


def test_mavenmaven::excludes_constructor_exists():
    assert callable(MavenMaven::Excludes.__init__)


def test_mavenmaven::excludes_constructor_args():
    sig = inspect.signature(MavenMaven::Excludes.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::excludesfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::ExcludesFile)


def test_mavenmaven::excludesfile_constructor_exists():
    assert callable(MavenMaven::ExcludesFile.__init__)


def test_mavenmaven::excludesfile_constructor_args():
    sig = inspect.signature(MavenMaven::ExcludesFile.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::includes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Includes)


def test_mavenmaven::includes_constructor_exists():
    assert callable(MavenMaven::Includes.__init__)


def test_mavenmaven::includes_constructor_args():
    sig = inspect.signature(MavenMaven::Includes.__init__)
    params = list(sig.parameters.keys())



def test_basic_is_not_abstract():
    assert not inspect.isabstract(Basic)


def test_basic_constructor_exists():
    assert callable(Basic.__init__)


def test_basic_constructor_args():
    sig = inspect.signature(Basic.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::filter_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Filter)


def test_mavenmaven::filter_constructor_exists():
    assert callable(MavenMaven::Filter.__init__)


def test_mavenmaven::filter_constructor_args():
    sig = inspect.signature(MavenMaven::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven::filter_has_token():
    assert hasattr(MavenMaven::Filter, "token")
    descriptor = None
    for klass in MavenMaven::Filter.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::filter_has_value():
    assert hasattr(MavenMaven::Filter, "value")
    descriptor = None
    for klass in MavenMaven::Filter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::filelist_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FileList)


def test_mavenmaven::filelist_constructor_exists():
    assert callable(MavenMaven::FileList.__init__)


def test_mavenmaven::filelist_constructor_args():
    sig = inspect.signature(MavenMaven::FileList.__init__)
    params = list(sig.parameters.keys())
    assert "files" in params, "Missing parameter 'files'"
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven::filelist_has_files():
    assert hasattr(MavenMaven::FileList, "files")
    descriptor = None
    for klass in MavenMaven::FileList.__mro__:
        if "files" in klass.__dict__:
            descriptor = klass.__dict__["files"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::filelist_has_dir():
    assert hasattr(MavenMaven::FileList, "dir")
    descriptor = None
    for klass in MavenMaven::FileList.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::inexcludes_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::InExcludes)


def test_mavenmaven::inexcludes_constructor_exists():
    assert callable(MavenMaven::InExcludes.__init__)


def test_mavenmaven::inexcludes_constructor_args():
    sig = inspect.signature(MavenMaven::InExcludes.__init__)
    params = list(sig.parameters.keys())
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"
    assert "unless" in params, "Missing parameter 'unless'"
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven::inexcludes_has_ifCondition():
    assert hasattr(MavenMaven::InExcludes, "ifCondition")
    descriptor = None
    for klass in MavenMaven::InExcludes.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::inexcludes_has_unless():
    assert hasattr(MavenMaven::InExcludes, "unless")
    descriptor = None
    for klass in MavenMaven::InExcludes.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::inexcludes_has_name():
    assert hasattr(MavenMaven::InExcludes, "name")
    descriptor = None
    for klass in MavenMaven::InExcludes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::mapper_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Mapper)


def test_mavenmaven::mapper_constructor_exists():
    assert callable(MavenMaven::Mapper.__init__)


def test_mavenmaven::mapper_constructor_args():
    sig = inspect.signature(MavenMaven::Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "classpathref" in params, "Missing parameter 'classpathref'"
    assert "classpath" in params, "Missing parameter 'classpath'"
    assert "type" in params, "Missing parameter 'type'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_mavenmaven::mapper_has_to():
    assert hasattr(MavenMaven::Mapper, "to")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::mapper_has_classpathref():
    assert hasattr(MavenMaven::Mapper, "classpathref")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "classpathref" in klass.__dict__:
            descriptor = klass.__dict__["classpathref"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::mapper_has_classpath():
    assert hasattr(MavenMaven::Mapper, "classpath")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "classpath" in klass.__dict__:
            descriptor = klass.__dict__["classpath"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::mapper_has_type():
    assert hasattr(MavenMaven::Mapper, "type")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::mapper_has_from_():
    assert hasattr(MavenMaven::Mapper, "from_")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::mapper_has_classname():
    assert hasattr(MavenMaven::Mapper, "classname")
    descriptor = None
    for klass in MavenMaven::Mapper.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_pattern_is_not_abstract():
    assert not inspect.isabstract(Pattern)


def test_pattern_constructor_exists():
    assert callable(Pattern.__init__)


def test_pattern_constructor_args():
    sig = inspect.signature(Pattern.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::basic_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Basic)


def test_mavenmaven::basic_constructor_exists():
    assert callable(MavenMaven::Basic.__init__)


def test_mavenmaven::basic_constructor_args():
    sig = inspect.signature(MavenMaven::Basic.__init__)
    params = list(sig.parameters.keys())



def test_set_is_not_abstract():
    assert not inspect.isabstract(Set)


def test_set_constructor_exists():
    assert callable(Set.__init__)


def test_set_constructor_args():
    sig = inspect.signature(Set.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::filterset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FilterSet)


def test_mavenmaven::filterset_constructor_exists():
    assert callable(MavenMaven::FilterSet.__init__)


def test_mavenmaven::filterset_constructor_args():
    sig = inspect.signature(MavenMaven::FilterSet.__init__)
    params = list(sig.parameters.keys())
    assert "endtoken" in params, "Missing parameter 'endtoken'"
    assert "starttoken" in params, "Missing parameter 'starttoken'"

def test_mavenmaven::filterset_has_endtoken():
    assert hasattr(MavenMaven::FilterSet, "endtoken")
    descriptor = None
    for klass in MavenMaven::FilterSet.__mro__:
        if "endtoken" in klass.__dict__:
            descriptor = klass.__dict__["endtoken"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::filterset_has_starttoken():
    assert hasattr(MavenMaven::FilterSet, "starttoken")
    descriptor = None
    for klass in MavenMaven::FilterSet.__mro__:
        if "starttoken" in klass.__dict__:
            descriptor = klass.__dict__["starttoken"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::fileset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FileSet)


def test_mavenmaven::fileset_constructor_exists():
    assert callable(MavenMaven::FileSet.__init__)


def test_mavenmaven::fileset_constructor_args():
    sig = inspect.signature(MavenMaven::FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_mavenmaven::fileset_has_dir():
    assert hasattr(MavenMaven::FileSet, "dir")
    descriptor = None
    for klass in MavenMaven::FileSet.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::classpath_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::ClassPath)


def test_mavenmaven::classpath_constructor_exists():
    assert callable(MavenMaven::ClassPath.__init__)


def test_mavenmaven::classpath_constructor_args():
    sig = inspect.signature(MavenMaven::ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"

def test_mavenmaven::classpath_has_refid():
    assert hasattr(MavenMaven::ClassPath, "refid")
    descriptor = None
    for klass in MavenMaven::ClassPath.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::patternset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PatternSet)


def test_mavenmaven::patternset_constructor_exists():
    assert callable(MavenMaven::PatternSet.__init__)


def test_mavenmaven::patternset_constructor_args():
    sig = inspect.signature(MavenMaven::PatternSet.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::set_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Set)


def test_mavenmaven::set_constructor_exists():
    assert callable(MavenMaven::Set.__init__)


def test_mavenmaven::set_constructor_args():
    sig = inspect.signature(MavenMaven::Set.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::pathelement_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PathElement)


def test_mavenmaven::pathelement_constructor_exists():
    assert callable(MavenMaven::PathElement.__init__)


def test_mavenmaven::pathelement_constructor_args():
    sig = inspect.signature(MavenMaven::PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "path" in params, "Missing parameter 'path'"

def test_mavenmaven::pathelement_has_location():
    assert hasattr(MavenMaven::PathElement, "location")
    descriptor = None
    for klass in MavenMaven::PathElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::pathelement_has_path():
    assert hasattr(MavenMaven::PathElement, "path")
    descriptor = None
    for klass in MavenMaven::PathElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::filtersfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::FiltersFile)


def test_mavenmaven::filtersfile_constructor_exists():
    assert callable(MavenMaven::FiltersFile.__init__)


def test_mavenmaven::filtersfile_constructor_args():
    sig = inspect.signature(MavenMaven::FiltersFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven::filtersfile_has_file():
    assert hasattr(MavenMaven::FiltersFile, "file")
    descriptor = None
    for klass in MavenMaven::FiltersFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::contentsgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::ContentsGoal)


def test_mavenmaven::contentsgoal_constructor_exists():
    assert callable(MavenMaven::ContentsGoal.__init__)


def test_mavenmaven::contentsgoal_constructor_args():
    sig = inspect.signature(MavenMaven::ContentsGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::abstractgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AbstractGoal)


def test_mavenmaven::abstractgoal_constructor_exists():
    assert callable(MavenMaven::AbstractGoal.__init__)


def test_mavenmaven::abstractgoal_constructor_args():
    sig = inspect.signature(MavenMaven::AbstractGoal.__init__)
    params = list(sig.parameters.keys())



def test_jellycommand_is_not_abstract():
    assert not inspect.isabstract(JellyCommand)


def test_jellycommand_constructor_exists():
    assert callable(JellyCommand.__init__)


def test_jellycommand_constructor_args():
    sig = inspect.signature(JellyCommand.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::jellyset_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::JellySet)


def test_mavenmaven::jellyset_constructor_exists():
    assert callable(MavenMaven::JellySet.__init__)


def test_mavenmaven::jellyset_constructor_args():
    sig = inspect.signature(MavenMaven::JellySet.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven::jellyset_has_var():
    assert hasattr(MavenMaven::JellySet, "var")
    descriptor = None
    for klass in MavenMaven::JellySet.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::jellyset_has_value():
    assert hasattr(MavenMaven::JellySet, "value")
    descriptor = None
    for klass in MavenMaven::JellySet.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::pattern_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Pattern)


def test_mavenmaven::pattern_constructor_exists():
    assert callable(MavenMaven::Pattern.__init__)


def test_mavenmaven::pattern_constructor_args():
    sig = inspect.signature(MavenMaven::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_prepostgoal_is_not_abstract():
    assert not inspect.isabstract(PrePostGoal)


def test_prepostgoal_constructor_exists():
    assert callable(PrePostGoal.__init__)


def test_prepostgoal_constructor_args():
    sig = inspect.signature(PrePostGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::postgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PostGoal)


def test_mavenmaven::postgoal_constructor_exists():
    assert callable(MavenMaven::PostGoal.__init__)


def test_mavenmaven::postgoal_constructor_args():
    sig = inspect.signature(MavenMaven::PostGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::pregoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PreGoal)


def test_mavenmaven::pregoal_constructor_exists():
    assert callable(MavenMaven::PreGoal.__init__)


def test_mavenmaven::pregoal_constructor_args():
    sig = inspect.signature(MavenMaven::PreGoal.__init__)
    params = list(sig.parameters.keys())



def test_abstractgoal_is_not_abstract():
    assert not inspect.isabstract(AbstractGoal)


def test_abstractgoal_constructor_exists():
    assert callable(AbstractGoal.__init__)


def test_abstractgoal_constructor_args():
    sig = inspect.signature(AbstractGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::path_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Path)


def test_mavenmaven::path_constructor_exists():
    assert callable(MavenMaven::Path.__init__)


def test_mavenmaven::path_constructor_args():
    sig = inspect.signature(MavenMaven::Path.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "refid" in params, "Missing parameter 'refid'"

def test_mavenmaven::path_has_id():
    assert hasattr(MavenMaven::Path, "id")
    descriptor = None
    for klass in MavenMaven::Path.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::path_has_refid():
    assert hasattr(MavenMaven::Path, "refid")
    descriptor = None
    for klass in MavenMaven::Path.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::goal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Goal)


def test_mavenmaven::goal_constructor_exists():
    assert callable(MavenMaven::Goal.__init__)


def test_mavenmaven::goal_constructor_args():
    sig = inspect.signature(MavenMaven::Goal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven::goal_has_name():
    assert hasattr(MavenMaven::Goal, "name")
    descriptor = None
    for klass in MavenMaven::Goal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::xmlns_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Xmlns)


def test_mavenmaven::xmlns_constructor_exists():
    assert callable(MavenMaven::Xmlns.__init__)


def test_mavenmaven::xmlns_constructor_args():
    sig = inspect.signature(MavenMaven::Xmlns.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven::xmlns_has_name():
    assert hasattr(MavenMaven::Xmlns, "name")
    descriptor = None
    for klass in MavenMaven::Xmlns.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::xmlns_has_value():
    assert hasattr(MavenMaven::Xmlns, "value")
    descriptor = None
    for klass in MavenMaven::Xmlns.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::project_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Project)


def test_mavenmaven::project_constructor_exists():
    assert callable(MavenMaven::Project.__init__)


def test_mavenmaven::project_constructor_args():
    sig = inspect.signature(MavenMaven::Project.__init__)
    params = list(sig.parameters.keys())



def test_antpropertyname_is_not_abstract():
    assert not inspect.isabstract(AntPropertyName)


def test_antpropertyname_constructor_exists():
    assert callable(AntPropertyName.__init__)


def test_antpropertyname_constructor_args():
    sig = inspect.signature(AntPropertyName.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::antpropertylocation_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntPropertyLocation)


def test_mavenmaven::antpropertylocation_constructor_exists():
    assert callable(MavenMaven::AntPropertyLocation.__init__)


def test_mavenmaven::antpropertylocation_constructor_args():
    sig = inspect.signature(MavenMaven::AntPropertyLocation.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_mavenmaven::antpropertylocation_has_location():
    assert hasattr(MavenMaven::AntPropertyLocation, "location")
    descriptor = None
    for klass in MavenMaven::AntPropertyLocation.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::antpropertyvalue_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntPropertyValue)


def test_mavenmaven::antpropertyvalue_constructor_exists():
    assert callable(MavenMaven::AntPropertyValue.__init__)


def test_mavenmaven::antpropertyvalue_constructor_args():
    sig = inspect.signature(MavenMaven::AntPropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mavenmaven::antpropertyvalue_has_value():
    assert hasattr(MavenMaven::AntPropertyValue, "value")
    descriptor = None
    for klass in MavenMaven::AntPropertyValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_antproperty_is_not_abstract():
    assert not inspect.isabstract(AntProperty)


def test_antproperty_constructor_exists():
    assert callable(AntProperty.__init__)


def test_antproperty_constructor_args():
    sig = inspect.signature(AntProperty.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::antpropertyenv_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntPropertyEnv)


def test_mavenmaven::antpropertyenv_constructor_exists():
    assert callable(MavenMaven::AntPropertyEnv.__init__)


def test_mavenmaven::antpropertyenv_constructor_args():
    sig = inspect.signature(MavenMaven::AntPropertyEnv.__init__)
    params = list(sig.parameters.keys())
    assert "environment" in params, "Missing parameter 'environment'"

def test_mavenmaven::antpropertyenv_has_environment():
    assert hasattr(MavenMaven::AntPropertyEnv, "environment")
    descriptor = None
    for klass in MavenMaven::AntPropertyEnv.__mro__:
        if "environment" in klass.__dict__:
            descriptor = klass.__dict__["environment"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::antpropertyfile_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntPropertyFile)


def test_mavenmaven::antpropertyfile_constructor_exists():
    assert callable(MavenMaven::AntPropertyFile.__init__)


def test_mavenmaven::antpropertyfile_constructor_args():
    sig = inspect.signature(MavenMaven::AntPropertyFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_mavenmaven::antpropertyfile_has_file():
    assert hasattr(MavenMaven::AntPropertyFile, "file")
    descriptor = None
    for klass in MavenMaven::AntPropertyFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_mavenmaven::antpropertyname_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntPropertyName)


def test_mavenmaven::antpropertyname_constructor_exists():
    assert callable(MavenMaven::AntPropertyName.__init__)


def test_mavenmaven::antpropertyname_constructor_args():
    sig = inspect.signature(MavenMaven::AntPropertyName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mavenmaven::antpropertyname_has_name():
    assert hasattr(MavenMaven::AntPropertyName, "name")
    descriptor = None
    for klass in MavenMaven::AntPropertyName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_contentsgoal_is_not_abstract():
    assert not inspect.isabstract(ContentsGoal)


def test_contentsgoal_constructor_exists():
    assert callable(ContentsGoal.__init__)


def test_contentsgoal_constructor_args():
    sig = inspect.signature(ContentsGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::jellycommand_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::JellyCommand)


def test_mavenmaven::jellycommand_constructor_exists():
    assert callable(MavenMaven::JellyCommand.__init__)


def test_mavenmaven::jellycommand_constructor_args():
    sig = inspect.signature(MavenMaven::JellyCommand.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::antproperty_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntProperty)


def test_mavenmaven::antproperty_constructor_exists():
    assert callable(MavenMaven::AntProperty.__init__)


def test_mavenmaven::antproperty_constructor_args():
    sig = inspect.signature(MavenMaven::AntProperty.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::attaingoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AttainGoal)


def test_mavenmaven::attaingoal_constructor_exists():
    assert callable(MavenMaven::AttainGoal.__init__)


def test_mavenmaven::attaingoal_constructor_args():
    sig = inspect.signature(MavenMaven::AttainGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::task_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::Task)


def test_mavenmaven::task_constructor_exists():
    assert callable(MavenMaven::Task.__init__)


def test_mavenmaven::task_constructor_args():
    sig = inspect.signature(MavenMaven::Task.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::prepostgoal_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::PrePostGoal)


def test_mavenmaven::prepostgoal_constructor_exists():
    assert callable(MavenMaven::PrePostGoal.__init__)


def test_mavenmaven::prepostgoal_constructor_args():
    sig = inspect.signature(MavenMaven::PrePostGoal.__init__)
    params = list(sig.parameters.keys())



def test_mavenmaven::anttaskdef_is_not_abstract():
    assert not inspect.isabstract(MavenMaven::AntTaskDef)


def test_mavenmaven::anttaskdef_constructor_exists():
    assert callable(MavenMaven::AntTaskDef.__init__)


def test_mavenmaven::anttaskdef_constructor_args():
    sig = inspect.signature(MavenMaven::AntTaskDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_mavenmaven::anttaskdef_has_name():
    assert hasattr(MavenMaven::AntTaskDef, "name")
    descriptor = None
    for klass in MavenMaven::AntTaskDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_mavenmaven::anttaskdef_has_classname():
    assert hasattr(MavenMaven::AntTaskDef, "classname")
    descriptor = None
    for klass in MavenMaven::AntTaskDef.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)


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
DocumentationTask_strategy = st.builds(
    DocumentationTask,
)
MavenMaven::Javadoc_strategy = st.builds(
    MavenMaven::Javadoc,
    destdir=
        safe_text,
    use=
        safe_text,
    author=
        safe_text,
    version=
        safe_text,
    windowtitle=
        safe_text,
    sourcepath=
        safe_text,
    defaultexcludes=
        safe_text,
    packagenames=
        safe_text
)
CompileTask_strategy = st.builds(
    CompileTask,
)
MavenMaven::Javac_strategy = st.builds(
    MavenMaven::Javac,
    optimize=
        safe_text,
    destdir=
        safe_text,
    deprecation=
        safe_text,
    srcdir=
        safe_text,
    fork=
        safe_text,
    debug=
        safe_text
)
FileTask_strategy = st.builds(
    FileTask,
)
MavenMaven::Delete_strategy = st.builds(
    MavenMaven::Delete,
    includeEmptyDirs=
        safe_text,
    includes=
        safe_text,
    failonerror=
        safe_text,
    defaultexcludes=
        safe_text,
    dir=
        safe_text,
    file=
        safe_text,
    excludesfile=
        safe_text,
    quiet=
        safe_text,
    excludes=
        safe_text,
    includesfile=
        safe_text,
    verbose=
        safe_text
)
MavenMaven::Copy_strategy = st.builds(
    MavenMaven::Copy,
    flatten=
        safe_text,
    overwrite=
        safe_text,
    filtering=
        safe_text,
    todir=
        safe_text,
    presservelastmodified=
        safe_text,
    includeEmptyDirs=
        safe_text,
    tofile=
        safe_text,
    file=
        safe_text
)
MavenMaven::Mkdir_strategy = st.builds(
    MavenMaven::Mkdir,
    dir=
        safe_text
)
ArchiveTask_strategy = st.builds(
    ArchiveTask,
)
MavenMaven::Jar_strategy = st.builds(
    MavenMaven::Jar,
    manifest=
        safe_text,
    basedir=
        safe_text,
    compress=
        safe_text,
    encoding=
        safe_text,
    jarfile=
        safe_text
)
ExecutionTask_strategy = st.builds(
    ExecutionTask,
)
MavenMaven::Java_strategy = st.builds(
    MavenMaven::Java,
    jar=
        safe_text,
    fork=
        safe_text,
    classname=
        safe_text
)
MavenMaven::Exec_strategy = st.builds(
    MavenMaven::Exec,
    dir=
        safe_text,
    executable=
        safe_text
)
PreDefinedTask_strategy = st.builds(
    PreDefinedTask,
)
MavenMaven::FileTask_strategy = st.builds(
    MavenMaven::FileTask,
)
MavenMaven::ArchiveTask_strategy = st.builds(
    MavenMaven::ArchiveTask,
)
MavenMaven::DocumentationTask_strategy = st.builds(
    MavenMaven::DocumentationTask,
)
MavenMaven::ExecutionTask_strategy = st.builds(
    MavenMaven::ExecutionTask,
)
MavenMaven::Attribut_strategy = st.builds(
    MavenMaven::Attribut,
    value=
        safe_text,
    name=
        safe_text
)
MavenMaven::CompileTask_strategy = st.builds(
    MavenMaven::CompileTask,
)
MavenMaven::FormatTstamp_strategy = st.builds(
    MavenMaven::FormatTstamp,
    unit=
        safe_text,
    pattern=
        safe_text,
    offset=
        safe_text,
    locale=
        safe_text,
    property=
        safe_text
)
MiscellaneousTask_strategy = st.builds(
    MiscellaneousTask,
)
MavenMaven::Tstamp_strategy = st.builds(
    MavenMaven::Tstamp,
)
MavenMaven::Echo_strategy = st.builds(
    MavenMaven::Echo,
    message=
        safe_text,
    append=
        safe_text,
    file=
        safe_text
)
MavenMaven::MiscellaneousTask_strategy = st.builds(
    MavenMaven::MiscellaneousTask,
)
Task_strategy = st.builds(
    Task,
)
MavenMaven::PreDefinedTask_strategy = st.builds(
    MavenMaven::PreDefinedTask,
    description=
        safe_text,
    taskname=
        safe_text,
    id=
        safe_text
)
MavenMaven::NewTask_strategy = st.builds(
    MavenMaven::NewTask,
)
InExcludes_strategy = st.builds(
    InExcludes,
)
MavenMaven::IncludesFile_strategy = st.builds(
    MavenMaven::IncludesFile,
)
MavenMaven::Excludes_strategy = st.builds(
    MavenMaven::Excludes,
)
MavenMaven::ExcludesFile_strategy = st.builds(
    MavenMaven::ExcludesFile,
)
MavenMaven::Includes_strategy = st.builds(
    MavenMaven::Includes,
)
Basic_strategy = st.builds(
    Basic,
)
MavenMaven::Filter_strategy = st.builds(
    MavenMaven::Filter,
    token=
        safe_text,
    value=
        safe_text
)
MavenMaven::FileList_strategy = st.builds(
    MavenMaven::FileList,
    files=
        safe_text,
    dir=
        safe_text
)
MavenMaven::InExcludes_strategy = st.builds(
    MavenMaven::InExcludes,
    ifCondition=
        safe_text,
    unless=
        safe_text,
    name=
        safe_text
)
MavenMaven::Mapper_strategy = st.builds(
    MavenMaven::Mapper,
    to=
        safe_text,
    classpathref=
        safe_text,
    classpath=
        safe_text,
    type=
        safe_text,
    from_=
        safe_text,
    classname=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
MavenMaven::Basic_strategy = st.builds(
    MavenMaven::Basic,
)
Set_strategy = st.builds(
    Set,
)
MavenMaven::FilterSet_strategy = st.builds(
    MavenMaven::FilterSet,
    endtoken=
        safe_text,
    starttoken=
        safe_text
)
MavenMaven::FileSet_strategy = st.builds(
    MavenMaven::FileSet,
    dir=
        safe_text
)
MavenMaven::ClassPath_strategy = st.builds(
    MavenMaven::ClassPath,
    refid=
        safe_text
)
MavenMaven::PatternSet_strategy = st.builds(
    MavenMaven::PatternSet,
)
MavenMaven::Set_strategy = st.builds(
    MavenMaven::Set,
)
MavenMaven::PathElement_strategy = st.builds(
    MavenMaven::PathElement,
    location=
        safe_text,
    path=
        safe_text
)
MavenMaven::FiltersFile_strategy = st.builds(
    MavenMaven::FiltersFile,
    file=
        safe_text
)
MavenMaven::ContentsGoal_strategy = st.builds(
    MavenMaven::ContentsGoal,
)
MavenMaven::AbstractGoal_strategy = st.builds(
    MavenMaven::AbstractGoal,
)
JellyCommand_strategy = st.builds(
    JellyCommand,
)
MavenMaven::JellySet_strategy = st.builds(
    MavenMaven::JellySet,
    var=
        safe_text,
    value=
        safe_text
)
MavenMaven::Pattern_strategy = st.builds(
    MavenMaven::Pattern,
)
PrePostGoal_strategy = st.builds(
    PrePostGoal,
)
MavenMaven::PostGoal_strategy = st.builds(
    MavenMaven::PostGoal,
)
MavenMaven::PreGoal_strategy = st.builds(
    MavenMaven::PreGoal,
)
AbstractGoal_strategy = st.builds(
    AbstractGoal,
)
MavenMaven::Path_strategy = st.builds(
    MavenMaven::Path,
    id=
        safe_text,
    refid=
        safe_text
)
MavenMaven::Goal_strategy = st.builds(
    MavenMaven::Goal,
    name=
        safe_text
)
MavenMaven::Xmlns_strategy = st.builds(
    MavenMaven::Xmlns,
    name=
        safe_text,
    value=
        safe_text
)
MavenMaven::Project_strategy = st.builds(
    MavenMaven::Project,
)
AntPropertyName_strategy = st.builds(
    AntPropertyName,
)
MavenMaven::AntPropertyLocation_strategy = st.builds(
    MavenMaven::AntPropertyLocation,
    location=
        safe_text
)
MavenMaven::AntPropertyValue_strategy = st.builds(
    MavenMaven::AntPropertyValue,
    value=
        safe_text
)
AntProperty_strategy = st.builds(
    AntProperty,
)
MavenMaven::AntPropertyEnv_strategy = st.builds(
    MavenMaven::AntPropertyEnv,
    environment=
        safe_text
)
MavenMaven::AntPropertyFile_strategy = st.builds(
    MavenMaven::AntPropertyFile,
    file=
        safe_text
)
MavenMaven::AntPropertyName_strategy = st.builds(
    MavenMaven::AntPropertyName,
    name=
        safe_text
)
ContentsGoal_strategy = st.builds(
    ContentsGoal,
)
MavenMaven::JellyCommand_strategy = st.builds(
    MavenMaven::JellyCommand,
)
MavenMaven::AntProperty_strategy = st.builds(
    MavenMaven::AntProperty,
)
MavenMaven::AttainGoal_strategy = st.builds(
    MavenMaven::AttainGoal,
)
MavenMaven::Task_strategy = st.builds(
    MavenMaven::Task,
)
MavenMaven::PrePostGoal_strategy = st.builds(
    MavenMaven::PrePostGoal,
)
MavenMaven::AntTaskDef_strategy = st.builds(
    MavenMaven::AntTaskDef,
    name=
        safe_text,
    classname=
        safe_text
)

@given(instance=DocumentationTask_strategy)
@settings(max_examples=50)
def test_documentationtask_instantiation(instance):
    assert isinstance(instance, DocumentationTask)

@given(instance=MavenMaven::Javadoc_strategy)
@settings(max_examples=50)
def test_mavenmaven::javadoc_instantiation(instance):
    assert isinstance(instance, MavenMaven::Javadoc)

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_destdir_type(instance):
    assert isinstance(instance.destdir, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_use_type(instance):
    assert isinstance(instance.use, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_windowtitle_type(instance):
    assert isinstance(instance.windowtitle, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_windowtitle_setter(instance):
    original = instance.windowtitle
    instance.windowtitle = original
    assert instance.windowtitle == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_sourcepath_type(instance):
    assert isinstance(instance.sourcepath, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_sourcepath_setter(instance):
    original = instance.sourcepath
    instance.sourcepath = original
    assert instance.sourcepath == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_defaultexcludes_type(instance):
    assert isinstance(instance.defaultexcludes, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original

@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_packagenames_type(instance):
    assert isinstance(instance.packagenames, str)


@given(instance=MavenMaven::Javadoc_strategy)
def test_mavenmaven::javadoc_packagenames_setter(instance):
    original = instance.packagenames
    instance.packagenames = original
    assert instance.packagenames == original

@given(instance=CompileTask_strategy)
@settings(max_examples=50)
def test_compiletask_instantiation(instance):
    assert isinstance(instance, CompileTask)

@given(instance=MavenMaven::Javac_strategy)
@settings(max_examples=50)
def test_mavenmaven::javac_instantiation(instance):
    assert isinstance(instance, MavenMaven::Javac)

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_optimize_type(instance):
    assert isinstance(instance.optimize, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_optimize_setter(instance):
    original = instance.optimize
    instance.optimize = original
    assert instance.optimize == original

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_destdir_type(instance):
    assert isinstance(instance.destdir, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_deprecation_type(instance):
    assert isinstance(instance.deprecation, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_deprecation_setter(instance):
    original = instance.deprecation
    instance.deprecation = original
    assert instance.deprecation == original

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_srcdir_type(instance):
    assert isinstance(instance.srcdir, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_srcdir_setter(instance):
    original = instance.srcdir
    instance.srcdir = original
    assert instance.srcdir == original

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_fork_type(instance):
    assert isinstance(instance.fork, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_debug_type(instance):
    assert isinstance(instance.debug, str)


@given(instance=MavenMaven::Javac_strategy)
def test_mavenmaven::javac_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=FileTask_strategy)
@settings(max_examples=50)
def test_filetask_instantiation(instance):
    assert isinstance(instance, FileTask)

@given(instance=MavenMaven::Delete_strategy)
@settings(max_examples=50)
def test_mavenmaven::delete_instantiation(instance):
    assert isinstance(instance, MavenMaven::Delete)

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includeEmptyDirs_type(instance):
    assert isinstance(instance.includeEmptyDirs, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includes_type(instance):
    assert isinstance(instance.includes, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_failonerror_type(instance):
    assert isinstance(instance.failonerror, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_failonerror_setter(instance):
    original = instance.failonerror
    instance.failonerror = original
    assert instance.failonerror == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_defaultexcludes_type(instance):
    assert isinstance(instance.defaultexcludes, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_excludesfile_type(instance):
    assert isinstance(instance.excludesfile, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_excludesfile_setter(instance):
    original = instance.excludesfile
    instance.excludesfile = original
    assert instance.excludesfile == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_quiet_type(instance):
    assert isinstance(instance.quiet, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_quiet_setter(instance):
    original = instance.quiet
    instance.quiet = original
    assert instance.quiet == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_excludes_type(instance):
    assert isinstance(instance.excludes, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includesfile_type(instance):
    assert isinstance(instance.includesfile, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_includesfile_setter(instance):
    original = instance.includesfile
    instance.includesfile = original
    assert instance.includesfile == original

@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_verbose_type(instance):
    assert isinstance(instance.verbose, str)


@given(instance=MavenMaven::Delete_strategy)
def test_mavenmaven::delete_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original

@given(instance=MavenMaven::Copy_strategy)
@settings(max_examples=50)
def test_mavenmaven::copy_instantiation(instance):
    assert isinstance(instance, MavenMaven::Copy)

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_flatten_type(instance):
    assert isinstance(instance.flatten, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_flatten_setter(instance):
    original = instance.flatten
    instance.flatten = original
    assert instance.flatten == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_overwrite_type(instance):
    assert isinstance(instance.overwrite, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_overwrite_setter(instance):
    original = instance.overwrite
    instance.overwrite = original
    assert instance.overwrite == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_filtering_type(instance):
    assert isinstance(instance.filtering, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_todir_type(instance):
    assert isinstance(instance.todir, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_todir_setter(instance):
    original = instance.todir
    instance.todir = original
    assert instance.todir == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_presservelastmodified_type(instance):
    assert isinstance(instance.presservelastmodified, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_presservelastmodified_setter(instance):
    original = instance.presservelastmodified
    instance.presservelastmodified = original
    assert instance.presservelastmodified == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_includeEmptyDirs_type(instance):
    assert isinstance(instance.includeEmptyDirs, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_tofile_type(instance):
    assert isinstance(instance.tofile, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_tofile_setter(instance):
    original = instance.tofile
    instance.tofile = original
    assert instance.tofile == original

@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=MavenMaven::Copy_strategy)
def test_mavenmaven::copy_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven::Mkdir_strategy)
@settings(max_examples=50)
def test_mavenmaven::mkdir_instantiation(instance):
    assert isinstance(instance, MavenMaven::Mkdir)

@given(instance=MavenMaven::Mkdir_strategy)
def test_mavenmaven::mkdir_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MavenMaven::Mkdir_strategy)
def test_mavenmaven::mkdir_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=ArchiveTask_strategy)
@settings(max_examples=50)
def test_archivetask_instantiation(instance):
    assert isinstance(instance, ArchiveTask)

@given(instance=MavenMaven::Jar_strategy)
@settings(max_examples=50)
def test_mavenmaven::jar_instantiation(instance):
    assert isinstance(instance, MavenMaven::Jar)

@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_manifest_type(instance):
    assert isinstance(instance.manifest, str)


@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_manifest_setter(instance):
    original = instance.manifest
    instance.manifest = original
    assert instance.manifest == original

@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_basedir_type(instance):
    assert isinstance(instance.basedir, str)


@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original

@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_compress_type(instance):
    assert isinstance(instance.compress, str)


@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_compress_setter(instance):
    original = instance.compress
    instance.compress = original
    assert instance.compress == original

@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_jarfile_type(instance):
    assert isinstance(instance.jarfile, str)


@given(instance=MavenMaven::Jar_strategy)
def test_mavenmaven::jar_jarfile_setter(instance):
    original = instance.jarfile
    instance.jarfile = original
    assert instance.jarfile == original

@given(instance=ExecutionTask_strategy)
@settings(max_examples=50)
def test_executiontask_instantiation(instance):
    assert isinstance(instance, ExecutionTask)

@given(instance=MavenMaven::Java_strategy)
@settings(max_examples=50)
def test_mavenmaven::java_instantiation(instance):
    assert isinstance(instance, MavenMaven::Java)

@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_jar_type(instance):
    assert isinstance(instance.jar, str)


@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_jar_setter(instance):
    original = instance.jar
    instance.jar = original
    assert instance.jar == original

@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_fork_type(instance):
    assert isinstance(instance.fork, str)


@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=MavenMaven::Java_strategy)
def test_mavenmaven::java_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=MavenMaven::Exec_strategy)
@settings(max_examples=50)
def test_mavenmaven::exec_instantiation(instance):
    assert isinstance(instance, MavenMaven::Exec)

@given(instance=MavenMaven::Exec_strategy)
def test_mavenmaven::exec_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MavenMaven::Exec_strategy)
def test_mavenmaven::exec_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven::Exec_strategy)
def test_mavenmaven::exec_executable_type(instance):
    assert isinstance(instance.executable, str)


@given(instance=MavenMaven::Exec_strategy)
def test_mavenmaven::exec_executable_setter(instance):
    original = instance.executable
    instance.executable = original
    assert instance.executable == original

@given(instance=PreDefinedTask_strategy)
@settings(max_examples=50)
def test_predefinedtask_instantiation(instance):
    assert isinstance(instance, PreDefinedTask)

@given(instance=MavenMaven::FileTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::filetask_instantiation(instance):
    assert isinstance(instance, MavenMaven::FileTask)

@given(instance=MavenMaven::ArchiveTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::archivetask_instantiation(instance):
    assert isinstance(instance, MavenMaven::ArchiveTask)

@given(instance=MavenMaven::DocumentationTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::documentationtask_instantiation(instance):
    assert isinstance(instance, MavenMaven::DocumentationTask)

@given(instance=MavenMaven::ExecutionTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::executiontask_instantiation(instance):
    assert isinstance(instance, MavenMaven::ExecutionTask)

@given(instance=MavenMaven::Attribut_strategy)
@settings(max_examples=50)
def test_mavenmaven::attribut_instantiation(instance):
    assert isinstance(instance, MavenMaven::Attribut)

@given(instance=MavenMaven::Attribut_strategy)
def test_mavenmaven::attribut_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MavenMaven::Attribut_strategy)
def test_mavenmaven::attribut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MavenMaven::Attribut_strategy)
def test_mavenmaven::attribut_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::Attribut_strategy)
def test_mavenmaven::attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven::CompileTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::compiletask_instantiation(instance):
    assert isinstance(instance, MavenMaven::CompileTask)

@given(instance=MavenMaven::FormatTstamp_strategy)
@settings(max_examples=50)
def test_mavenmaven::formattstamp_instantiation(instance):
    assert isinstance(instance, MavenMaven::FormatTstamp)

@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_locale_type(instance):
    assert isinstance(instance.locale, str)


@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original

@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_property_type(instance):
    assert isinstance(instance.property, str)


@given(instance=MavenMaven::FormatTstamp_strategy)
def test_mavenmaven::formattstamp_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original

@given(instance=MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MiscellaneousTask)

@given(instance=MavenMaven::Tstamp_strategy)
@settings(max_examples=50)
def test_mavenmaven::tstamp_instantiation(instance):
    assert isinstance(instance, MavenMaven::Tstamp)

@given(instance=MavenMaven::Echo_strategy)
@settings(max_examples=50)
def test_mavenmaven::echo_instantiation(instance):
    assert isinstance(instance, MavenMaven::Echo)

@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_append_type(instance):
    assert isinstance(instance.append, str)


@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=MavenMaven::Echo_strategy)
def test_mavenmaven::echo_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven::MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MavenMaven::MiscellaneousTask)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=MavenMaven::PreDefinedTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::predefinedtask_instantiation(instance):
    assert isinstance(instance, MavenMaven::PreDefinedTask)

@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_taskname_type(instance):
    assert isinstance(instance.taskname, str)


@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_taskname_setter(instance):
    original = instance.taskname
    instance.taskname = original
    assert instance.taskname == original

@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MavenMaven::PreDefinedTask_strategy)
def test_mavenmaven::predefinedtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenMaven::NewTask_strategy)
@settings(max_examples=50)
def test_mavenmaven::newtask_instantiation(instance):
    assert isinstance(instance, MavenMaven::NewTask)

@given(instance=InExcludes_strategy)
@settings(max_examples=50)
def test_inexcludes_instantiation(instance):
    assert isinstance(instance, InExcludes)

@given(instance=MavenMaven::IncludesFile_strategy)
@settings(max_examples=50)
def test_mavenmaven::includesfile_instantiation(instance):
    assert isinstance(instance, MavenMaven::IncludesFile)

@given(instance=MavenMaven::Excludes_strategy)
@settings(max_examples=50)
def test_mavenmaven::excludes_instantiation(instance):
    assert isinstance(instance, MavenMaven::Excludes)

@given(instance=MavenMaven::ExcludesFile_strategy)
@settings(max_examples=50)
def test_mavenmaven::excludesfile_instantiation(instance):
    assert isinstance(instance, MavenMaven::ExcludesFile)

@given(instance=MavenMaven::Includes_strategy)
@settings(max_examples=50)
def test_mavenmaven::includes_instantiation(instance):
    assert isinstance(instance, MavenMaven::Includes)

@given(instance=Basic_strategy)
@settings(max_examples=50)
def test_basic_instantiation(instance):
    assert isinstance(instance, Basic)

@given(instance=MavenMaven::Filter_strategy)
@settings(max_examples=50)
def test_mavenmaven::filter_instantiation(instance):
    assert isinstance(instance, MavenMaven::Filter)

@given(instance=MavenMaven::Filter_strategy)
def test_mavenmaven::filter_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=MavenMaven::Filter_strategy)
def test_mavenmaven::filter_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=MavenMaven::Filter_strategy)
def test_mavenmaven::filter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MavenMaven::Filter_strategy)
def test_mavenmaven::filter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MavenMaven::FileList_strategy)
@settings(max_examples=50)
def test_mavenmaven::filelist_instantiation(instance):
    assert isinstance(instance, MavenMaven::FileList)

@given(instance=MavenMaven::FileList_strategy)
def test_mavenmaven::filelist_files_type(instance):
    assert isinstance(instance.files, str)


@given(instance=MavenMaven::FileList_strategy)
def test_mavenmaven::filelist_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=MavenMaven::FileList_strategy)
def test_mavenmaven::filelist_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MavenMaven::FileList_strategy)
def test_mavenmaven::filelist_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven::InExcludes_strategy)
@settings(max_examples=50)
def test_mavenmaven::inexcludes_instantiation(instance):
    assert isinstance(instance, MavenMaven::InExcludes)

@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_ifCondition_type(instance):
    assert isinstance(instance.ifCondition, str)


@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original

@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_unless_type(instance):
    assert isinstance(instance.unless, str)


@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original

@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::InExcludes_strategy)
def test_mavenmaven::inexcludes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven::Mapper_strategy)
@settings(max_examples=50)
def test_mavenmaven::mapper_instantiation(instance):
    assert isinstance(instance, MavenMaven::Mapper)

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classpathref_type(instance):
    assert isinstance(instance.classpathref, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classpathref_setter(instance):
    original = instance.classpathref
    instance.classpathref = original
    assert instance.classpathref == original

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classpath_type(instance):
    assert isinstance(instance.classpath, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classpath_setter(instance):
    original = instance.classpath
    instance.classpath = original
    assert instance.classpath == original

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=MavenMaven::Mapper_strategy)
def test_mavenmaven::mapper_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=MavenMaven::Basic_strategy)
@settings(max_examples=50)
def test_mavenmaven::basic_instantiation(instance):
    assert isinstance(instance, MavenMaven::Basic)

@given(instance=Set_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, Set)

@given(instance=MavenMaven::FilterSet_strategy)
@settings(max_examples=50)
def test_mavenmaven::filterset_instantiation(instance):
    assert isinstance(instance, MavenMaven::FilterSet)

@given(instance=MavenMaven::FilterSet_strategy)
def test_mavenmaven::filterset_endtoken_type(instance):
    assert isinstance(instance.endtoken, str)


@given(instance=MavenMaven::FilterSet_strategy)
def test_mavenmaven::filterset_endtoken_setter(instance):
    original = instance.endtoken
    instance.endtoken = original
    assert instance.endtoken == original

@given(instance=MavenMaven::FilterSet_strategy)
def test_mavenmaven::filterset_starttoken_type(instance):
    assert isinstance(instance.starttoken, str)


@given(instance=MavenMaven::FilterSet_strategy)
def test_mavenmaven::filterset_starttoken_setter(instance):
    original = instance.starttoken
    instance.starttoken = original
    assert instance.starttoken == original

@given(instance=MavenMaven::FileSet_strategy)
@settings(max_examples=50)
def test_mavenmaven::fileset_instantiation(instance):
    assert isinstance(instance, MavenMaven::FileSet)

@given(instance=MavenMaven::FileSet_strategy)
def test_mavenmaven::fileset_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MavenMaven::FileSet_strategy)
def test_mavenmaven::fileset_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=MavenMaven::ClassPath_strategy)
@settings(max_examples=50)
def test_mavenmaven::classpath_instantiation(instance):
    assert isinstance(instance, MavenMaven::ClassPath)

@given(instance=MavenMaven::ClassPath_strategy)
def test_mavenmaven::classpath_refid_type(instance):
    assert isinstance(instance.refid, str)


@given(instance=MavenMaven::ClassPath_strategy)
def test_mavenmaven::classpath_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=MavenMaven::PatternSet_strategy)
@settings(max_examples=50)
def test_mavenmaven::patternset_instantiation(instance):
    assert isinstance(instance, MavenMaven::PatternSet)

@given(instance=MavenMaven::Set_strategy)
@settings(max_examples=50)
def test_mavenmaven::set_instantiation(instance):
    assert isinstance(instance, MavenMaven::Set)

@given(instance=MavenMaven::PathElement_strategy)
@settings(max_examples=50)
def test_mavenmaven::pathelement_instantiation(instance):
    assert isinstance(instance, MavenMaven::PathElement)

@given(instance=MavenMaven::PathElement_strategy)
def test_mavenmaven::pathelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=MavenMaven::PathElement_strategy)
def test_mavenmaven::pathelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=MavenMaven::PathElement_strategy)
def test_mavenmaven::pathelement_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=MavenMaven::PathElement_strategy)
def test_mavenmaven::pathelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=MavenMaven::FiltersFile_strategy)
@settings(max_examples=50)
def test_mavenmaven::filtersfile_instantiation(instance):
    assert isinstance(instance, MavenMaven::FiltersFile)

@given(instance=MavenMaven::FiltersFile_strategy)
def test_mavenmaven::filtersfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=MavenMaven::FiltersFile_strategy)
def test_mavenmaven::filtersfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven::ContentsGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::contentsgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::ContentsGoal)

@given(instance=MavenMaven::AbstractGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::abstractgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::AbstractGoal)

@given(instance=JellyCommand_strategy)
@settings(max_examples=50)
def test_jellycommand_instantiation(instance):
    assert isinstance(instance, JellyCommand)

@given(instance=MavenMaven::JellySet_strategy)
@settings(max_examples=50)
def test_mavenmaven::jellyset_instantiation(instance):
    assert isinstance(instance, MavenMaven::JellySet)

@given(instance=MavenMaven::JellySet_strategy)
def test_mavenmaven::jellyset_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=MavenMaven::JellySet_strategy)
def test_mavenmaven::jellyset_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=MavenMaven::JellySet_strategy)
def test_mavenmaven::jellyset_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MavenMaven::JellySet_strategy)
def test_mavenmaven::jellyset_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MavenMaven::Pattern_strategy)
@settings(max_examples=50)
def test_mavenmaven::pattern_instantiation(instance):
    assert isinstance(instance, MavenMaven::Pattern)

@given(instance=PrePostGoal_strategy)
@settings(max_examples=50)
def test_prepostgoal_instantiation(instance):
    assert isinstance(instance, PrePostGoal)

@given(instance=MavenMaven::PostGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::postgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::PostGoal)

@given(instance=MavenMaven::PreGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::pregoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::PreGoal)

@given(instance=AbstractGoal_strategy)
@settings(max_examples=50)
def test_abstractgoal_instantiation(instance):
    assert isinstance(instance, AbstractGoal)

@given(instance=MavenMaven::Path_strategy)
@settings(max_examples=50)
def test_mavenmaven::path_instantiation(instance):
    assert isinstance(instance, MavenMaven::Path)

@given(instance=MavenMaven::Path_strategy)
def test_mavenmaven::path_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=MavenMaven::Path_strategy)
def test_mavenmaven::path_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=MavenMaven::Path_strategy)
def test_mavenmaven::path_refid_type(instance):
    assert isinstance(instance.refid, str)


@given(instance=MavenMaven::Path_strategy)
def test_mavenmaven::path_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=MavenMaven::Goal_strategy)
@settings(max_examples=50)
def test_mavenmaven::goal_instantiation(instance):
    assert isinstance(instance, MavenMaven::Goal)

@given(instance=MavenMaven::Goal_strategy)
def test_mavenmaven::goal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::Goal_strategy)
def test_mavenmaven::goal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven::Xmlns_strategy)
@settings(max_examples=50)
def test_mavenmaven::xmlns_instantiation(instance):
    assert isinstance(instance, MavenMaven::Xmlns)

@given(instance=MavenMaven::Xmlns_strategy)
def test_mavenmaven::xmlns_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::Xmlns_strategy)
def test_mavenmaven::xmlns_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven::Xmlns_strategy)
def test_mavenmaven::xmlns_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MavenMaven::Xmlns_strategy)
def test_mavenmaven::xmlns_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MavenMaven::Project_strategy)
@settings(max_examples=50)
def test_mavenmaven::project_instantiation(instance):
    assert isinstance(instance, MavenMaven::Project)

@given(instance=AntPropertyName_strategy)
@settings(max_examples=50)
def test_antpropertyname_instantiation(instance):
    assert isinstance(instance, AntPropertyName)

@given(instance=MavenMaven::AntPropertyLocation_strategy)
@settings(max_examples=50)
def test_mavenmaven::antpropertylocation_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntPropertyLocation)

@given(instance=MavenMaven::AntPropertyLocation_strategy)
def test_mavenmaven::antpropertylocation_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=MavenMaven::AntPropertyLocation_strategy)
def test_mavenmaven::antpropertylocation_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=MavenMaven::AntPropertyValue_strategy)
@settings(max_examples=50)
def test_mavenmaven::antpropertyvalue_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntPropertyValue)

@given(instance=MavenMaven::AntPropertyValue_strategy)
def test_mavenmaven::antpropertyvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MavenMaven::AntPropertyValue_strategy)
def test_mavenmaven::antpropertyvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AntProperty_strategy)
@settings(max_examples=50)
def test_antproperty_instantiation(instance):
    assert isinstance(instance, AntProperty)

@given(instance=MavenMaven::AntPropertyEnv_strategy)
@settings(max_examples=50)
def test_mavenmaven::antpropertyenv_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntPropertyEnv)

@given(instance=MavenMaven::AntPropertyEnv_strategy)
def test_mavenmaven::antpropertyenv_environment_type(instance):
    assert isinstance(instance.environment, str)


@given(instance=MavenMaven::AntPropertyEnv_strategy)
def test_mavenmaven::antpropertyenv_environment_setter(instance):
    original = instance.environment
    instance.environment = original
    assert instance.environment == original

@given(instance=MavenMaven::AntPropertyFile_strategy)
@settings(max_examples=50)
def test_mavenmaven::antpropertyfile_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntPropertyFile)

@given(instance=MavenMaven::AntPropertyFile_strategy)
def test_mavenmaven::antpropertyfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=MavenMaven::AntPropertyFile_strategy)
def test_mavenmaven::antpropertyfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=MavenMaven::AntPropertyName_strategy)
@settings(max_examples=50)
def test_mavenmaven::antpropertyname_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntPropertyName)

@given(instance=MavenMaven::AntPropertyName_strategy)
def test_mavenmaven::antpropertyname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::AntPropertyName_strategy)
def test_mavenmaven::antpropertyname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ContentsGoal_strategy)
@settings(max_examples=50)
def test_contentsgoal_instantiation(instance):
    assert isinstance(instance, ContentsGoal)

@given(instance=MavenMaven::JellyCommand_strategy)
@settings(max_examples=50)
def test_mavenmaven::jellycommand_instantiation(instance):
    assert isinstance(instance, MavenMaven::JellyCommand)

@given(instance=MavenMaven::AntProperty_strategy)
@settings(max_examples=50)
def test_mavenmaven::antproperty_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntProperty)

@given(instance=MavenMaven::AttainGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::attaingoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::AttainGoal)

@given(instance=MavenMaven::Task_strategy)
@settings(max_examples=50)
def test_mavenmaven::task_instantiation(instance):
    assert isinstance(instance, MavenMaven::Task)

@given(instance=MavenMaven::PrePostGoal_strategy)
@settings(max_examples=50)
def test_mavenmaven::prepostgoal_instantiation(instance):
    assert isinstance(instance, MavenMaven::PrePostGoal)

@given(instance=MavenMaven::AntTaskDef_strategy)
@settings(max_examples=50)
def test_mavenmaven::anttaskdef_instantiation(instance):
    assert isinstance(instance, MavenMaven::AntTaskDef)

@given(instance=MavenMaven::AntTaskDef_strategy)
def test_mavenmaven::anttaskdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MavenMaven::AntTaskDef_strategy)
def test_mavenmaven::anttaskdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MavenMaven::AntTaskDef_strategy)
def test_mavenmaven::anttaskdef_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=MavenMaven::AntTaskDef_strategy)
def test_mavenmaven::anttaskdef_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original
