import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    InExcludes,
    Ant::ExcludesFile,
    Ant::Excludes,
    Ant::IncludesFile,
    Ant::Includes,
    Basic,
    Ant::InExcludes,
    Ant::FileList,
    Ant::Mapper,
    Pattern,
    Ant::Basic,
    Ant::Pattern,
    Ant::Project,
    PropertyName,
    Ant::PropertyLocation,
    Ant::PropertyValue,
    Ant::Property,
    TaskDef,
    Property,
    Ant::PropertyEnv,
    Ant::PropertyFile,
    Ant::PropertyName,
    Path,
    Target,
    Mapper,
    FilterSet,
    FileTask,
    Ant::Delete,
    Ant::Mkdir,
    ArchiveTask,
    Ant::Jar,
    DocumentationTask,
    Ant::Javadoc,
    CompileTask,
    Ant::Copy,
    Ant::Javac,
    Ant::TaskDef,
    Ant::FormatTstamp,
    Ant::Task,
    FormatTstamp,
    MiscellaneousTask,
    Ant::Tstamp,
    Ant::Echo,
    ClassPath,
    FileSet,
    PathElement,
    Ant::Java,
    Ant::Exec,
    PreDefinedTask,
    Ant::FileTask,
    Ant::CompileTask,
    Ant::DocumentationTask,
    Ant::MiscellaneousTask,
    Ant::ArchiveTask,
    Ant::ExecutionTask,
    Ant::Attribut,
    Attribut,
    Set,
    Ant::ClassPath,
    Ant::FileSet,
    Ant::PatternSet,
    Ant::Set,
    Ant::PathElement,
    Ant::FiltersFile,
    Ant::Filter,
    Ant::Path,
    FiltersFile,
    Filter,
    Ant::FilterSet,
    Excludes,
    Includes,
    PatternSet,
    Task,
    Ant::PreDefinedTask,
    Ant::NewTask,
    Ant::Target,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_inexcludes_is_not_abstract():
    assert not inspect.isabstract(InExcludes)


def test_inexcludes_constructor_exists():
    assert callable(InExcludes.__init__)


def test_inexcludes_constructor_args():
    sig = inspect.signature(InExcludes.__init__)
    params = list(sig.parameters.keys())



def test_ant::excludesfile_is_not_abstract():
    assert not inspect.isabstract(Ant::ExcludesFile)


def test_ant::excludesfile_constructor_exists():
    assert callable(Ant::ExcludesFile.__init__)


def test_ant::excludesfile_constructor_args():
    sig = inspect.signature(Ant::ExcludesFile.__init__)
    params = list(sig.parameters.keys())



def test_ant::excludes_is_not_abstract():
    assert not inspect.isabstract(Ant::Excludes)


def test_ant::excludes_constructor_exists():
    assert callable(Ant::Excludes.__init__)


def test_ant::excludes_constructor_args():
    sig = inspect.signature(Ant::Excludes.__init__)
    params = list(sig.parameters.keys())



def test_ant::includesfile_is_not_abstract():
    assert not inspect.isabstract(Ant::IncludesFile)


def test_ant::includesfile_constructor_exists():
    assert callable(Ant::IncludesFile.__init__)


def test_ant::includesfile_constructor_args():
    sig = inspect.signature(Ant::IncludesFile.__init__)
    params = list(sig.parameters.keys())



def test_ant::includes_is_not_abstract():
    assert not inspect.isabstract(Ant::Includes)


def test_ant::includes_constructor_exists():
    assert callable(Ant::Includes.__init__)


def test_ant::includes_constructor_args():
    sig = inspect.signature(Ant::Includes.__init__)
    params = list(sig.parameters.keys())



def test_basic_is_not_abstract():
    assert not inspect.isabstract(Basic)


def test_basic_constructor_exists():
    assert callable(Basic.__init__)


def test_basic_constructor_args():
    sig = inspect.signature(Basic.__init__)
    params = list(sig.parameters.keys())



def test_ant::inexcludes_is_not_abstract():
    assert not inspect.isabstract(Ant::InExcludes)


def test_ant::inexcludes_constructor_exists():
    assert callable(Ant::InExcludes.__init__)


def test_ant::inexcludes_constructor_args():
    sig = inspect.signature(Ant::InExcludes.__init__)
    params = list(sig.parameters.keys())
    assert "unless" in params, "Missing parameter 'unless'"
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"
    assert "name" in params, "Missing parameter 'name'"

def test_ant::inexcludes_has_unless():
    assert hasattr(Ant::InExcludes, "unless")
    descriptor = None
    for klass in Ant::InExcludes.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
            break
    assert isinstance(descriptor, property)

def test_ant::inexcludes_has_ifCondition():
    assert hasattr(Ant::InExcludes, "ifCondition")
    descriptor = None
    for klass in Ant::InExcludes.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)

def test_ant::inexcludes_has_name():
    assert hasattr(Ant::InExcludes, "name")
    descriptor = None
    for klass in Ant::InExcludes.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ant::filelist_is_not_abstract():
    assert not inspect.isabstract(Ant::FileList)


def test_ant::filelist_constructor_exists():
    assert callable(Ant::FileList.__init__)


def test_ant::filelist_constructor_args():
    sig = inspect.signature(Ant::FileList.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "files" in params, "Missing parameter 'files'"

def test_ant::filelist_has_dir():
    assert hasattr(Ant::FileList, "dir")
    descriptor = None
    for klass in Ant::FileList.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_ant::filelist_has_files():
    assert hasattr(Ant::FileList, "files")
    descriptor = None
    for klass in Ant::FileList.__mro__:
        if "files" in klass.__dict__:
            descriptor = klass.__dict__["files"]
            break
    assert isinstance(descriptor, property)



def test_ant::mapper_is_not_abstract():
    assert not inspect.isabstract(Ant::Mapper)


def test_ant::mapper_constructor_exists():
    assert callable(Ant::Mapper.__init__)


def test_ant::mapper_constructor_args():
    sig = inspect.signature(Ant::Mapper.__init__)
    params = list(sig.parameters.keys())
    assert "to" in params, "Missing parameter 'to'"
    assert "classname" in params, "Missing parameter 'classname'"
    assert "from_" in params, "Missing parameter 'from_'"
    assert "classpathref" in params, "Missing parameter 'classpathref'"
    assert "classpath" in params, "Missing parameter 'classpath'"
    assert "type" in params, "Missing parameter 'type'"

def test_ant::mapper_has_to():
    assert hasattr(Ant::Mapper, "to")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
        if "to" in klass.__dict__:
            descriptor = klass.__dict__["to"]
            break
    assert isinstance(descriptor, property)

def test_ant::mapper_has_classname():
    assert hasattr(Ant::Mapper, "classname")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)

def test_ant::mapper_has_from_():
    assert hasattr(Ant::Mapper, "from_")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)

def test_ant::mapper_has_classpathref():
    assert hasattr(Ant::Mapper, "classpathref")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
        if "classpathref" in klass.__dict__:
            descriptor = klass.__dict__["classpathref"]
            break
    assert isinstance(descriptor, property)

def test_ant::mapper_has_classpath():
    assert hasattr(Ant::Mapper, "classpath")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
        if "classpath" in klass.__dict__:
            descriptor = klass.__dict__["classpath"]
            break
    assert isinstance(descriptor, property)

def test_ant::mapper_has_type():
    assert hasattr(Ant::Mapper, "type")
    descriptor = None
    for klass in Ant::Mapper.__mro__:
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



def test_ant::basic_is_not_abstract():
    assert not inspect.isabstract(Ant::Basic)


def test_ant::basic_constructor_exists():
    assert callable(Ant::Basic.__init__)


def test_ant::basic_constructor_args():
    sig = inspect.signature(Ant::Basic.__init__)
    params = list(sig.parameters.keys())



def test_ant::pattern_is_not_abstract():
    assert not inspect.isabstract(Ant::Pattern)


def test_ant::pattern_constructor_exists():
    assert callable(Ant::Pattern.__init__)


def test_ant::pattern_constructor_args():
    sig = inspect.signature(Ant::Pattern.__init__)
    params = list(sig.parameters.keys())



def test_ant::project_is_not_abstract():
    assert not inspect.isabstract(Ant::Project)


def test_ant::project_constructor_exists():
    assert callable(Ant::Project.__init__)


def test_ant::project_constructor_args():
    sig = inspect.signature(Ant::Project.__init__)
    params = list(sig.parameters.keys())
    assert "basedir" in params, "Missing parameter 'basedir'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_ant::project_has_basedir():
    assert hasattr(Ant::Project, "basedir")
    descriptor = None
    for klass in Ant::Project.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)

def test_ant::project_has_name():
    assert hasattr(Ant::Project, "name")
    descriptor = None
    for klass in Ant::Project.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant::project_has_description():
    assert hasattr(Ant::Project, "description")
    descriptor = None
    for klass in Ant::Project.__mro__:
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



def test_ant::propertylocation_is_not_abstract():
    assert not inspect.isabstract(Ant::PropertyLocation)


def test_ant::propertylocation_constructor_exists():
    assert callable(Ant::PropertyLocation.__init__)


def test_ant::propertylocation_constructor_args():
    sig = inspect.signature(Ant::PropertyLocation.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_ant::propertylocation_has_location():
    assert hasattr(Ant::PropertyLocation, "location")
    descriptor = None
    for klass in Ant::PropertyLocation.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_ant::propertyvalue_is_not_abstract():
    assert not inspect.isabstract(Ant::PropertyValue)


def test_ant::propertyvalue_constructor_exists():
    assert callable(Ant::PropertyValue.__init__)


def test_ant::propertyvalue_constructor_args():
    sig = inspect.signature(Ant::PropertyValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ant::propertyvalue_has_value():
    assert hasattr(Ant::PropertyValue, "value")
    descriptor = None
    for klass in Ant::PropertyValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ant::property_is_not_abstract():
    assert not inspect.isabstract(Ant::Property)


def test_ant::property_constructor_exists():
    assert callable(Ant::Property.__init__)


def test_ant::property_constructor_args():
    sig = inspect.signature(Ant::Property.__init__)
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



def test_ant::propertyenv_is_not_abstract():
    assert not inspect.isabstract(Ant::PropertyEnv)


def test_ant::propertyenv_constructor_exists():
    assert callable(Ant::PropertyEnv.__init__)


def test_ant::propertyenv_constructor_args():
    sig = inspect.signature(Ant::PropertyEnv.__init__)
    params = list(sig.parameters.keys())
    assert "environment" in params, "Missing parameter 'environment'"

def test_ant::propertyenv_has_environment():
    assert hasattr(Ant::PropertyEnv, "environment")
    descriptor = None
    for klass in Ant::PropertyEnv.__mro__:
        if "environment" in klass.__dict__:
            descriptor = klass.__dict__["environment"]
            break
    assert isinstance(descriptor, property)



def test_ant::propertyfile_is_not_abstract():
    assert not inspect.isabstract(Ant::PropertyFile)


def test_ant::propertyfile_constructor_exists():
    assert callable(Ant::PropertyFile.__init__)


def test_ant::propertyfile_constructor_args():
    sig = inspect.signature(Ant::PropertyFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_ant::propertyfile_has_file():
    assert hasattr(Ant::PropertyFile, "file")
    descriptor = None
    for klass in Ant::PropertyFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_ant::propertyname_is_not_abstract():
    assert not inspect.isabstract(Ant::PropertyName)


def test_ant::propertyname_constructor_exists():
    assert callable(Ant::PropertyName.__init__)


def test_ant::propertyname_constructor_args():
    sig = inspect.signature(Ant::PropertyName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ant::propertyname_has_name():
    assert hasattr(Ant::PropertyName, "name")
    descriptor = None
    for klass in Ant::PropertyName.__mro__:
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



def test_ant::delete_is_not_abstract():
    assert not inspect.isabstract(Ant::Delete)


def test_ant::delete_constructor_exists():
    assert callable(Ant::Delete.__init__)


def test_ant::delete_constructor_args():
    sig = inspect.signature(Ant::Delete.__init__)
    params = list(sig.parameters.keys())
    assert "verbose" in params, "Missing parameter 'verbose'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "includes" in params, "Missing parameter 'includes'"
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "includesfile" in params, "Missing parameter 'includesfile'"
    assert "failonerror" in params, "Missing parameter 'failonerror'"
    assert "excludesfile" in params, "Missing parameter 'excludesfile'"
    assert "file" in params, "Missing parameter 'file'"
    assert "dir" in params, "Missing parameter 'dir'"
    assert "excludes" in params, "Missing parameter 'excludes'"
    assert "quiet" in params, "Missing parameter 'quiet'"

def test_ant::delete_has_verbose():
    assert hasattr(Ant::Delete, "verbose")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_includeEmptyDirs():
    assert hasattr(Ant::Delete, "includeEmptyDirs")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_includes():
    assert hasattr(Ant::Delete, "includes")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "includes" in klass.__dict__:
            descriptor = klass.__dict__["includes"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_defaultexcludes():
    assert hasattr(Ant::Delete, "defaultexcludes")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_includesfile():
    assert hasattr(Ant::Delete, "includesfile")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "includesfile" in klass.__dict__:
            descriptor = klass.__dict__["includesfile"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_failonerror():
    assert hasattr(Ant::Delete, "failonerror")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "failonerror" in klass.__dict__:
            descriptor = klass.__dict__["failonerror"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_excludesfile():
    assert hasattr(Ant::Delete, "excludesfile")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "excludesfile" in klass.__dict__:
            descriptor = klass.__dict__["excludesfile"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_file():
    assert hasattr(Ant::Delete, "file")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_dir():
    assert hasattr(Ant::Delete, "dir")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_excludes():
    assert hasattr(Ant::Delete, "excludes")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "excludes" in klass.__dict__:
            descriptor = klass.__dict__["excludes"]
            break
    assert isinstance(descriptor, property)

def test_ant::delete_has_quiet():
    assert hasattr(Ant::Delete, "quiet")
    descriptor = None
    for klass in Ant::Delete.__mro__:
        if "quiet" in klass.__dict__:
            descriptor = klass.__dict__["quiet"]
            break
    assert isinstance(descriptor, property)



def test_ant::mkdir_is_not_abstract():
    assert not inspect.isabstract(Ant::Mkdir)


def test_ant::mkdir_constructor_exists():
    assert callable(Ant::Mkdir.__init__)


def test_ant::mkdir_constructor_args():
    sig = inspect.signature(Ant::Mkdir.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_ant::mkdir_has_dir():
    assert hasattr(Ant::Mkdir, "dir")
    descriptor = None
    for klass in Ant::Mkdir.__mro__:
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



def test_ant::jar_is_not_abstract():
    assert not inspect.isabstract(Ant::Jar)


def test_ant::jar_constructor_exists():
    assert callable(Ant::Jar.__init__)


def test_ant::jar_constructor_args():
    sig = inspect.signature(Ant::Jar.__init__)
    params = list(sig.parameters.keys())
    assert "jarfile" in params, "Missing parameter 'jarfile'"
    assert "encoding" in params, "Missing parameter 'encoding'"
    assert "manifest" in params, "Missing parameter 'manifest'"
    assert "basedir" in params, "Missing parameter 'basedir'"
    assert "compress" in params, "Missing parameter 'compress'"

def test_ant::jar_has_jarfile():
    assert hasattr(Ant::Jar, "jarfile")
    descriptor = None
    for klass in Ant::Jar.__mro__:
        if "jarfile" in klass.__dict__:
            descriptor = klass.__dict__["jarfile"]
            break
    assert isinstance(descriptor, property)

def test_ant::jar_has_encoding():
    assert hasattr(Ant::Jar, "encoding")
    descriptor = None
    for klass in Ant::Jar.__mro__:
        if "encoding" in klass.__dict__:
            descriptor = klass.__dict__["encoding"]
            break
    assert isinstance(descriptor, property)

def test_ant::jar_has_manifest():
    assert hasattr(Ant::Jar, "manifest")
    descriptor = None
    for klass in Ant::Jar.__mro__:
        if "manifest" in klass.__dict__:
            descriptor = klass.__dict__["manifest"]
            break
    assert isinstance(descriptor, property)

def test_ant::jar_has_basedir():
    assert hasattr(Ant::Jar, "basedir")
    descriptor = None
    for klass in Ant::Jar.__mro__:
        if "basedir" in klass.__dict__:
            descriptor = klass.__dict__["basedir"]
            break
    assert isinstance(descriptor, property)

def test_ant::jar_has_compress():
    assert hasattr(Ant::Jar, "compress")
    descriptor = None
    for klass in Ant::Jar.__mro__:
        if "compress" in klass.__dict__:
            descriptor = klass.__dict__["compress"]
            break
    assert isinstance(descriptor, property)



def test_documentationtask_is_not_abstract():
    assert not inspect.isabstract(DocumentationTask)


def test_documentationtask_constructor_exists():
    assert callable(DocumentationTask.__init__)


def test_documentationtask_constructor_args():
    sig = inspect.signature(DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::javadoc_is_not_abstract():
    assert not inspect.isabstract(Ant::Javadoc)


def test_ant::javadoc_constructor_exists():
    assert callable(Ant::Javadoc.__init__)


def test_ant::javadoc_constructor_args():
    sig = inspect.signature(Ant::Javadoc.__init__)
    params = list(sig.parameters.keys())
    assert "defaultexcludes" in params, "Missing parameter 'defaultexcludes'"
    assert "version" in params, "Missing parameter 'version'"
    assert "use" in params, "Missing parameter 'use'"
    assert "windowtitle" in params, "Missing parameter 'windowtitle'"
    assert "sourcepath" in params, "Missing parameter 'sourcepath'"
    assert "packagenames" in params, "Missing parameter 'packagenames'"
    assert "author" in params, "Missing parameter 'author'"
    assert "destdir" in params, "Missing parameter 'destdir'"

def test_ant::javadoc_has_defaultexcludes():
    assert hasattr(Ant::Javadoc, "defaultexcludes")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "defaultexcludes" in klass.__dict__:
            descriptor = klass.__dict__["defaultexcludes"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_version():
    assert hasattr(Ant::Javadoc, "version")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_use():
    assert hasattr(Ant::Javadoc, "use")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "use" in klass.__dict__:
            descriptor = klass.__dict__["use"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_windowtitle():
    assert hasattr(Ant::Javadoc, "windowtitle")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "windowtitle" in klass.__dict__:
            descriptor = klass.__dict__["windowtitle"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_sourcepath():
    assert hasattr(Ant::Javadoc, "sourcepath")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "sourcepath" in klass.__dict__:
            descriptor = klass.__dict__["sourcepath"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_packagenames():
    assert hasattr(Ant::Javadoc, "packagenames")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "packagenames" in klass.__dict__:
            descriptor = klass.__dict__["packagenames"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_author():
    assert hasattr(Ant::Javadoc, "author")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_ant::javadoc_has_destdir():
    assert hasattr(Ant::Javadoc, "destdir")
    descriptor = None
    for klass in Ant::Javadoc.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)



def test_compiletask_is_not_abstract():
    assert not inspect.isabstract(CompileTask)


def test_compiletask_constructor_exists():
    assert callable(CompileTask.__init__)


def test_compiletask_constructor_args():
    sig = inspect.signature(CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::copy_is_not_abstract():
    assert not inspect.isabstract(Ant::Copy)


def test_ant::copy_constructor_exists():
    assert callable(Ant::Copy.__init__)


def test_ant::copy_constructor_args():
    sig = inspect.signature(Ant::Copy.__init__)
    params = list(sig.parameters.keys())
    assert "tofile" in params, "Missing parameter 'tofile'"
    assert "file" in params, "Missing parameter 'file'"
    assert "todir" in params, "Missing parameter 'todir'"
    assert "filtering" in params, "Missing parameter 'filtering'"
    assert "includeEmptyDirs" in params, "Missing parameter 'includeEmptyDirs'"
    assert "overwrite" in params, "Missing parameter 'overwrite'"
    assert "flatten" in params, "Missing parameter 'flatten'"
    assert "presservelastmodified" in params, "Missing parameter 'presservelastmodified'"

def test_ant::copy_has_tofile():
    assert hasattr(Ant::Copy, "tofile")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "tofile" in klass.__dict__:
            descriptor = klass.__dict__["tofile"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_file():
    assert hasattr(Ant::Copy, "file")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_todir():
    assert hasattr(Ant::Copy, "todir")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "todir" in klass.__dict__:
            descriptor = klass.__dict__["todir"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_filtering():
    assert hasattr(Ant::Copy, "filtering")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "filtering" in klass.__dict__:
            descriptor = klass.__dict__["filtering"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_includeEmptyDirs():
    assert hasattr(Ant::Copy, "includeEmptyDirs")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "includeEmptyDirs" in klass.__dict__:
            descriptor = klass.__dict__["includeEmptyDirs"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_overwrite():
    assert hasattr(Ant::Copy, "overwrite")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "overwrite" in klass.__dict__:
            descriptor = klass.__dict__["overwrite"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_flatten():
    assert hasattr(Ant::Copy, "flatten")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "flatten" in klass.__dict__:
            descriptor = klass.__dict__["flatten"]
            break
    assert isinstance(descriptor, property)

def test_ant::copy_has_presservelastmodified():
    assert hasattr(Ant::Copy, "presservelastmodified")
    descriptor = None
    for klass in Ant::Copy.__mro__:
        if "presservelastmodified" in klass.__dict__:
            descriptor = klass.__dict__["presservelastmodified"]
            break
    assert isinstance(descriptor, property)



def test_ant::javac_is_not_abstract():
    assert not inspect.isabstract(Ant::Javac)


def test_ant::javac_constructor_exists():
    assert callable(Ant::Javac.__init__)


def test_ant::javac_constructor_args():
    sig = inspect.signature(Ant::Javac.__init__)
    params = list(sig.parameters.keys())
    assert "optimize" in params, "Missing parameter 'optimize'"
    assert "deprecation" in params, "Missing parameter 'deprecation'"
    assert "fork" in params, "Missing parameter 'fork'"
    assert "destdir" in params, "Missing parameter 'destdir'"
    assert "srcdir" in params, "Missing parameter 'srcdir'"
    assert "debug" in params, "Missing parameter 'debug'"

def test_ant::javac_has_optimize():
    assert hasattr(Ant::Javac, "optimize")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "optimize" in klass.__dict__:
            descriptor = klass.__dict__["optimize"]
            break
    assert isinstance(descriptor, property)

def test_ant::javac_has_deprecation():
    assert hasattr(Ant::Javac, "deprecation")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "deprecation" in klass.__dict__:
            descriptor = klass.__dict__["deprecation"]
            break
    assert isinstance(descriptor, property)

def test_ant::javac_has_fork():
    assert hasattr(Ant::Javac, "fork")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)

def test_ant::javac_has_destdir():
    assert hasattr(Ant::Javac, "destdir")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "destdir" in klass.__dict__:
            descriptor = klass.__dict__["destdir"]
            break
    assert isinstance(descriptor, property)

def test_ant::javac_has_srcdir():
    assert hasattr(Ant::Javac, "srcdir")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "srcdir" in klass.__dict__:
            descriptor = klass.__dict__["srcdir"]
            break
    assert isinstance(descriptor, property)

def test_ant::javac_has_debug():
    assert hasattr(Ant::Javac, "debug")
    descriptor = None
    for klass in Ant::Javac.__mro__:
        if "debug" in klass.__dict__:
            descriptor = klass.__dict__["debug"]
            break
    assert isinstance(descriptor, property)



def test_ant::taskdef_is_not_abstract():
    assert not inspect.isabstract(Ant::TaskDef)


def test_ant::taskdef_constructor_exists():
    assert callable(Ant::TaskDef.__init__)


def test_ant::taskdef_constructor_args():
    sig = inspect.signature(Ant::TaskDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_ant::taskdef_has_name():
    assert hasattr(Ant::TaskDef, "name")
    descriptor = None
    for klass in Ant::TaskDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant::taskdef_has_classname():
    assert hasattr(Ant::TaskDef, "classname")
    descriptor = None
    for klass in Ant::TaskDef.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_ant::formattstamp_is_not_abstract():
    assert not inspect.isabstract(Ant::FormatTstamp)


def test_ant::formattstamp_constructor_exists():
    assert callable(Ant::FormatTstamp.__init__)


def test_ant::formattstamp_constructor_args():
    sig = inspect.signature(Ant::FormatTstamp.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "property" in params, "Missing parameter 'property'"
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "locale" in params, "Missing parameter 'locale'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_ant::formattstamp_has_offset():
    assert hasattr(Ant::FormatTstamp, "offset")
    descriptor = None
    for klass in Ant::FormatTstamp.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_ant::formattstamp_has_property():
    assert hasattr(Ant::FormatTstamp, "property")
    descriptor = None
    for klass in Ant::FormatTstamp.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)

def test_ant::formattstamp_has_pattern():
    assert hasattr(Ant::FormatTstamp, "pattern")
    descriptor = None
    for klass in Ant::FormatTstamp.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_ant::formattstamp_has_locale():
    assert hasattr(Ant::FormatTstamp, "locale")
    descriptor = None
    for klass in Ant::FormatTstamp.__mro__:
        if "locale" in klass.__dict__:
            descriptor = klass.__dict__["locale"]
            break
    assert isinstance(descriptor, property)

def test_ant::formattstamp_has_unit():
    assert hasattr(Ant::FormatTstamp, "unit")
    descriptor = None
    for klass in Ant::FormatTstamp.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_ant::task_is_not_abstract():
    assert not inspect.isabstract(Ant::Task)


def test_ant::task_constructor_exists():
    assert callable(Ant::Task.__init__)


def test_ant::task_constructor_args():
    sig = inspect.signature(Ant::Task.__init__)
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



def test_ant::tstamp_is_not_abstract():
    assert not inspect.isabstract(Ant::Tstamp)


def test_ant::tstamp_constructor_exists():
    assert callable(Ant::Tstamp.__init__)


def test_ant::tstamp_constructor_args():
    sig = inspect.signature(Ant::Tstamp.__init__)
    params = list(sig.parameters.keys())



def test_ant::echo_is_not_abstract():
    assert not inspect.isabstract(Ant::Echo)


def test_ant::echo_constructor_exists():
    assert callable(Ant::Echo.__init__)


def test_ant::echo_constructor_args():
    sig = inspect.signature(Ant::Echo.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"
    assert "message" in params, "Missing parameter 'message'"
    assert "append" in params, "Missing parameter 'append'"

def test_ant::echo_has_file():
    assert hasattr(Ant::Echo, "file")
    descriptor = None
    for klass in Ant::Echo.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_ant::echo_has_message():
    assert hasattr(Ant::Echo, "message")
    descriptor = None
    for klass in Ant::Echo.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_ant::echo_has_append():
    assert hasattr(Ant::Echo, "append")
    descriptor = None
    for klass in Ant::Echo.__mro__:
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



def test_ant::java_is_not_abstract():
    assert not inspect.isabstract(Ant::Java)


def test_ant::java_constructor_exists():
    assert callable(Ant::Java.__init__)


def test_ant::java_constructor_args():
    sig = inspect.signature(Ant::Java.__init__)
    params = list(sig.parameters.keys())
    assert "fork" in params, "Missing parameter 'fork'"
    assert "jar" in params, "Missing parameter 'jar'"
    assert "classname" in params, "Missing parameter 'classname'"

def test_ant::java_has_fork():
    assert hasattr(Ant::Java, "fork")
    descriptor = None
    for klass in Ant::Java.__mro__:
        if "fork" in klass.__dict__:
            descriptor = klass.__dict__["fork"]
            break
    assert isinstance(descriptor, property)

def test_ant::java_has_jar():
    assert hasattr(Ant::Java, "jar")
    descriptor = None
    for klass in Ant::Java.__mro__:
        if "jar" in klass.__dict__:
            descriptor = klass.__dict__["jar"]
            break
    assert isinstance(descriptor, property)

def test_ant::java_has_classname():
    assert hasattr(Ant::Java, "classname")
    descriptor = None
    for klass in Ant::Java.__mro__:
        if "classname" in klass.__dict__:
            descriptor = klass.__dict__["classname"]
            break
    assert isinstance(descriptor, property)



def test_ant::exec_is_not_abstract():
    assert not inspect.isabstract(Ant::Exec)


def test_ant::exec_constructor_exists():
    assert callable(Ant::Exec.__init__)


def test_ant::exec_constructor_args():
    sig = inspect.signature(Ant::Exec.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"
    assert "executable" in params, "Missing parameter 'executable'"

def test_ant::exec_has_dir():
    assert hasattr(Ant::Exec, "dir")
    descriptor = None
    for klass in Ant::Exec.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)

def test_ant::exec_has_executable():
    assert hasattr(Ant::Exec, "executable")
    descriptor = None
    for klass in Ant::Exec.__mro__:
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



def test_ant::filetask_is_not_abstract():
    assert not inspect.isabstract(Ant::FileTask)


def test_ant::filetask_constructor_exists():
    assert callable(Ant::FileTask.__init__)


def test_ant::filetask_constructor_args():
    sig = inspect.signature(Ant::FileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::compiletask_is_not_abstract():
    assert not inspect.isabstract(Ant::CompileTask)


def test_ant::compiletask_constructor_exists():
    assert callable(Ant::CompileTask.__init__)


def test_ant::compiletask_constructor_args():
    sig = inspect.signature(Ant::CompileTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::documentationtask_is_not_abstract():
    assert not inspect.isabstract(Ant::DocumentationTask)


def test_ant::documentationtask_constructor_exists():
    assert callable(Ant::DocumentationTask.__init__)


def test_ant::documentationtask_constructor_args():
    sig = inspect.signature(Ant::DocumentationTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::miscellaneoustask_is_not_abstract():
    assert not inspect.isabstract(Ant::MiscellaneousTask)


def test_ant::miscellaneoustask_constructor_exists():
    assert callable(Ant::MiscellaneousTask.__init__)


def test_ant::miscellaneoustask_constructor_args():
    sig = inspect.signature(Ant::MiscellaneousTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::archivetask_is_not_abstract():
    assert not inspect.isabstract(Ant::ArchiveTask)


def test_ant::archivetask_constructor_exists():
    assert callable(Ant::ArchiveTask.__init__)


def test_ant::archivetask_constructor_args():
    sig = inspect.signature(Ant::ArchiveTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::executiontask_is_not_abstract():
    assert not inspect.isabstract(Ant::ExecutionTask)


def test_ant::executiontask_constructor_exists():
    assert callable(Ant::ExecutionTask.__init__)


def test_ant::executiontask_constructor_args():
    sig = inspect.signature(Ant::ExecutionTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::attribut_is_not_abstract():
    assert not inspect.isabstract(Ant::Attribut)


def test_ant::attribut_constructor_exists():
    assert callable(Ant::Attribut.__init__)


def test_ant::attribut_constructor_args():
    sig = inspect.signature(Ant::Attribut.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_ant::attribut_has_name():
    assert hasattr(Ant::Attribut, "name")
    descriptor = None
    for klass in Ant::Attribut.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant::attribut_has_value():
    assert hasattr(Ant::Attribut, "value")
    descriptor = None
    for klass in Ant::Attribut.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
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



def test_ant::classpath_is_not_abstract():
    assert not inspect.isabstract(Ant::ClassPath)


def test_ant::classpath_constructor_exists():
    assert callable(Ant::ClassPath.__init__)


def test_ant::classpath_constructor_args():
    sig = inspect.signature(Ant::ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"

def test_ant::classpath_has_refid():
    assert hasattr(Ant::ClassPath, "refid")
    descriptor = None
    for klass in Ant::ClassPath.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)



def test_ant::fileset_is_not_abstract():
    assert not inspect.isabstract(Ant::FileSet)


def test_ant::fileset_constructor_exists():
    assert callable(Ant::FileSet.__init__)


def test_ant::fileset_constructor_args():
    sig = inspect.signature(Ant::FileSet.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_ant::fileset_has_dir():
    assert hasattr(Ant::FileSet, "dir")
    descriptor = None
    for klass in Ant::FileSet.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_ant::patternset_is_not_abstract():
    assert not inspect.isabstract(Ant::PatternSet)


def test_ant::patternset_constructor_exists():
    assert callable(Ant::PatternSet.__init__)


def test_ant::patternset_constructor_args():
    sig = inspect.signature(Ant::PatternSet.__init__)
    params = list(sig.parameters.keys())



def test_ant::set_is_not_abstract():
    assert not inspect.isabstract(Ant::Set)


def test_ant::set_constructor_exists():
    assert callable(Ant::Set.__init__)


def test_ant::set_constructor_args():
    sig = inspect.signature(Ant::Set.__init__)
    params = list(sig.parameters.keys())



def test_ant::pathelement_is_not_abstract():
    assert not inspect.isabstract(Ant::PathElement)


def test_ant::pathelement_constructor_exists():
    assert callable(Ant::PathElement.__init__)


def test_ant::pathelement_constructor_args():
    sig = inspect.signature(Ant::PathElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "path" in params, "Missing parameter 'path'"

def test_ant::pathelement_has_location():
    assert hasattr(Ant::PathElement, "location")
    descriptor = None
    for klass in Ant::PathElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ant::pathelement_has_path():
    assert hasattr(Ant::PathElement, "path")
    descriptor = None
    for klass in Ant::PathElement.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)



def test_ant::filtersfile_is_not_abstract():
    assert not inspect.isabstract(Ant::FiltersFile)


def test_ant::filtersfile_constructor_exists():
    assert callable(Ant::FiltersFile.__init__)


def test_ant::filtersfile_constructor_args():
    sig = inspect.signature(Ant::FiltersFile.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_ant::filtersfile_has_file():
    assert hasattr(Ant::FiltersFile, "file")
    descriptor = None
    for klass in Ant::FiltersFile.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_ant::filter_is_not_abstract():
    assert not inspect.isabstract(Ant::Filter)


def test_ant::filter_constructor_exists():
    assert callable(Ant::Filter.__init__)


def test_ant::filter_constructor_args():
    sig = inspect.signature(Ant::Filter.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "token" in params, "Missing parameter 'token'"

def test_ant::filter_has_value():
    assert hasattr(Ant::Filter, "value")
    descriptor = None
    for klass in Ant::Filter.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_ant::filter_has_token():
    assert hasattr(Ant::Filter, "token")
    descriptor = None
    for klass in Ant::Filter.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_ant::path_is_not_abstract():
    assert not inspect.isabstract(Ant::Path)


def test_ant::path_constructor_exists():
    assert callable(Ant::Path.__init__)


def test_ant::path_constructor_args():
    sig = inspect.signature(Ant::Path.__init__)
    params = list(sig.parameters.keys())
    assert "refid" in params, "Missing parameter 'refid'"
    assert "id" in params, "Missing parameter 'id'"

def test_ant::path_has_refid():
    assert hasattr(Ant::Path, "refid")
    descriptor = None
    for klass in Ant::Path.__mro__:
        if "refid" in klass.__dict__:
            descriptor = klass.__dict__["refid"]
            break
    assert isinstance(descriptor, property)

def test_ant::path_has_id():
    assert hasattr(Ant::Path, "id")
    descriptor = None
    for klass in Ant::Path.__mro__:
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



def test_ant::filterset_is_not_abstract():
    assert not inspect.isabstract(Ant::FilterSet)


def test_ant::filterset_constructor_exists():
    assert callable(Ant::FilterSet.__init__)


def test_ant::filterset_constructor_args():
    sig = inspect.signature(Ant::FilterSet.__init__)
    params = list(sig.parameters.keys())
    assert "starttoken" in params, "Missing parameter 'starttoken'"
    assert "endtoken" in params, "Missing parameter 'endtoken'"

def test_ant::filterset_has_starttoken():
    assert hasattr(Ant::FilterSet, "starttoken")
    descriptor = None
    for klass in Ant::FilterSet.__mro__:
        if "starttoken" in klass.__dict__:
            descriptor = klass.__dict__["starttoken"]
            break
    assert isinstance(descriptor, property)

def test_ant::filterset_has_endtoken():
    assert hasattr(Ant::FilterSet, "endtoken")
    descriptor = None
    for klass in Ant::FilterSet.__mro__:
        if "endtoken" in klass.__dict__:
            descriptor = klass.__dict__["endtoken"]
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



def test_ant::predefinedtask_is_not_abstract():
    assert not inspect.isabstract(Ant::PreDefinedTask)


def test_ant::predefinedtask_constructor_exists():
    assert callable(Ant::PreDefinedTask.__init__)


def test_ant::predefinedtask_constructor_args():
    sig = inspect.signature(Ant::PreDefinedTask.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "taskname" in params, "Missing parameter 'taskname'"
    assert "id" in params, "Missing parameter 'id'"

def test_ant::predefinedtask_has_description():
    assert hasattr(Ant::PreDefinedTask, "description")
    descriptor = None
    for klass in Ant::PreDefinedTask.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ant::predefinedtask_has_taskname():
    assert hasattr(Ant::PreDefinedTask, "taskname")
    descriptor = None
    for klass in Ant::PreDefinedTask.__mro__:
        if "taskname" in klass.__dict__:
            descriptor = klass.__dict__["taskname"]
            break
    assert isinstance(descriptor, property)

def test_ant::predefinedtask_has_id():
    assert hasattr(Ant::PreDefinedTask, "id")
    descriptor = None
    for klass in Ant::PreDefinedTask.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ant::newtask_is_not_abstract():
    assert not inspect.isabstract(Ant::NewTask)


def test_ant::newtask_constructor_exists():
    assert callable(Ant::NewTask.__init__)


def test_ant::newtask_constructor_args():
    sig = inspect.signature(Ant::NewTask.__init__)
    params = list(sig.parameters.keys())



def test_ant::target_is_not_abstract():
    assert not inspect.isabstract(Ant::Target)


def test_ant::target_constructor_exists():
    assert callable(Ant::Target.__init__)


def test_ant::target_constructor_args():
    sig = inspect.signature(Ant::Target.__init__)
    params = list(sig.parameters.keys())
    assert "ifCondition" in params, "Missing parameter 'ifCondition'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "unless" in params, "Missing parameter 'unless'"

def test_ant::target_has_ifCondition():
    assert hasattr(Ant::Target, "ifCondition")
    descriptor = None
    for klass in Ant::Target.__mro__:
        if "ifCondition" in klass.__dict__:
            descriptor = klass.__dict__["ifCondition"]
            break
    assert isinstance(descriptor, property)

def test_ant::target_has_description():
    assert hasattr(Ant::Target, "description")
    descriptor = None
    for klass in Ant::Target.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ant::target_has_name():
    assert hasattr(Ant::Target, "name")
    descriptor = None
    for klass in Ant::Target.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ant::target_has_unless():
    assert hasattr(Ant::Target, "unless")
    descriptor = None
    for klass in Ant::Target.__mro__:
        if "unless" in klass.__dict__:
            descriptor = klass.__dict__["unless"]
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
InExcludes_strategy = st.builds(
    InExcludes,
)
Ant::ExcludesFile_strategy = st.builds(
    Ant::ExcludesFile,
)
Ant::Excludes_strategy = st.builds(
    Ant::Excludes,
)
Ant::IncludesFile_strategy = st.builds(
    Ant::IncludesFile,
)
Ant::Includes_strategy = st.builds(
    Ant::Includes,
)
Basic_strategy = st.builds(
    Basic,
)
Ant::InExcludes_strategy = st.builds(
    Ant::InExcludes,
    unless=
        safe_text,
    ifCondition=
        safe_text,
    name=
        safe_text
)
Ant::FileList_strategy = st.builds(
    Ant::FileList,
    dir=
        safe_text,
    files=
        safe_text
)
Ant::Mapper_strategy = st.builds(
    Ant::Mapper,
    to=
        safe_text,
    classname=
        safe_text,
    from_=
        safe_text,
    classpathref=
        safe_text,
    classpath=
        safe_text,
    type=
        safe_text
)
Pattern_strategy = st.builds(
    Pattern,
)
Ant::Basic_strategy = st.builds(
    Ant::Basic,
)
Ant::Pattern_strategy = st.builds(
    Ant::Pattern,
)
Ant::Project_strategy = st.builds(
    Ant::Project,
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
Ant::PropertyLocation_strategy = st.builds(
    Ant::PropertyLocation,
    location=
        safe_text
)
Ant::PropertyValue_strategy = st.builds(
    Ant::PropertyValue,
    value=
        safe_text
)
Ant::Property_strategy = st.builds(
    Ant::Property,
)
TaskDef_strategy = st.builds(
    TaskDef,
)
Property_strategy = st.builds(
    Property,
)
Ant::PropertyEnv_strategy = st.builds(
    Ant::PropertyEnv,
    environment=
        safe_text
)
Ant::PropertyFile_strategy = st.builds(
    Ant::PropertyFile,
    file=
        safe_text
)
Ant::PropertyName_strategy = st.builds(
    Ant::PropertyName,
    name=
        safe_text
)
Path_strategy = st.builds(
    Path,
)
Target_strategy = st.builds(
    Target,
)
Mapper_strategy = st.builds(
    Mapper,
)
FilterSet_strategy = st.builds(
    FilterSet,
)
FileTask_strategy = st.builds(
    FileTask,
)
Ant::Delete_strategy = st.builds(
    Ant::Delete,
    verbose=
        safe_text,
    includeEmptyDirs=
        safe_text,
    includes=
        safe_text,
    defaultexcludes=
        safe_text,
    includesfile=
        safe_text,
    failonerror=
        safe_text,
    excludesfile=
        safe_text,
    file=
        safe_text,
    dir=
        safe_text,
    excludes=
        safe_text,
    quiet=
        safe_text
)
Ant::Mkdir_strategy = st.builds(
    Ant::Mkdir,
    dir=
        safe_text
)
ArchiveTask_strategy = st.builds(
    ArchiveTask,
)
Ant::Jar_strategy = st.builds(
    Ant::Jar,
    jarfile=
        safe_text,
    encoding=
        safe_text,
    manifest=
        safe_text,
    basedir=
        safe_text,
    compress=
        safe_text
)
DocumentationTask_strategy = st.builds(
    DocumentationTask,
)
Ant::Javadoc_strategy = st.builds(
    Ant::Javadoc,
    defaultexcludes=
        safe_text,
    version=
        safe_text,
    use=
        safe_text,
    windowtitle=
        safe_text,
    sourcepath=
        safe_text,
    packagenames=
        safe_text,
    author=
        safe_text,
    destdir=
        safe_text
)
CompileTask_strategy = st.builds(
    CompileTask,
)
Ant::Copy_strategy = st.builds(
    Ant::Copy,
    tofile=
        safe_text,
    file=
        safe_text,
    todir=
        safe_text,
    filtering=
        safe_text,
    includeEmptyDirs=
        safe_text,
    overwrite=
        safe_text,
    flatten=
        safe_text,
    presservelastmodified=
        safe_text
)
Ant::Javac_strategy = st.builds(
    Ant::Javac,
    optimize=
        safe_text,
    deprecation=
        safe_text,
    fork=
        safe_text,
    destdir=
        safe_text,
    srcdir=
        safe_text,
    debug=
        safe_text
)
Ant::TaskDef_strategy = st.builds(
    Ant::TaskDef,
    name=
        safe_text,
    classname=
        safe_text
)
Ant::FormatTstamp_strategy = st.builds(
    Ant::FormatTstamp,
    offset=
        safe_text,
    property=
        safe_text,
    pattern=
        safe_text,
    locale=
        safe_text,
    unit=
        safe_text
)
Ant::Task_strategy = st.builds(
    Ant::Task,
)
FormatTstamp_strategy = st.builds(
    FormatTstamp,
)
MiscellaneousTask_strategy = st.builds(
    MiscellaneousTask,
)
Ant::Tstamp_strategy = st.builds(
    Ant::Tstamp,
)
Ant::Echo_strategy = st.builds(
    Ant::Echo,
    file=
        safe_text,
    message=
        safe_text,
    append=
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
Ant::Java_strategy = st.builds(
    Ant::Java,
    fork=
        safe_text,
    jar=
        safe_text,
    classname=
        safe_text
)
Ant::Exec_strategy = st.builds(
    Ant::Exec,
    dir=
        safe_text,
    executable=
        safe_text
)
PreDefinedTask_strategy = st.builds(
    PreDefinedTask,
)
Ant::FileTask_strategy = st.builds(
    Ant::FileTask,
)
Ant::CompileTask_strategy = st.builds(
    Ant::CompileTask,
)
Ant::DocumentationTask_strategy = st.builds(
    Ant::DocumentationTask,
)
Ant::MiscellaneousTask_strategy = st.builds(
    Ant::MiscellaneousTask,
)
Ant::ArchiveTask_strategy = st.builds(
    Ant::ArchiveTask,
)
Ant::ExecutionTask_strategy = st.builds(
    Ant::ExecutionTask,
)
Ant::Attribut_strategy = st.builds(
    Ant::Attribut,
    name=
        safe_text,
    value=
        safe_text
)
Attribut_strategy = st.builds(
    Attribut,
)
Set_strategy = st.builds(
    Set,
)
Ant::ClassPath_strategy = st.builds(
    Ant::ClassPath,
    refid=
        safe_text
)
Ant::FileSet_strategy = st.builds(
    Ant::FileSet,
    dir=
        safe_text
)
Ant::PatternSet_strategy = st.builds(
    Ant::PatternSet,
)
Ant::Set_strategy = st.builds(
    Ant::Set,
)
Ant::PathElement_strategy = st.builds(
    Ant::PathElement,
    location=
        safe_text,
    path=
        safe_text
)
Ant::FiltersFile_strategy = st.builds(
    Ant::FiltersFile,
    file=
        safe_text
)
Ant::Filter_strategy = st.builds(
    Ant::Filter,
    value=
        safe_text,
    token=
        safe_text
)
Ant::Path_strategy = st.builds(
    Ant::Path,
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
Ant::FilterSet_strategy = st.builds(
    Ant::FilterSet,
    starttoken=
        safe_text,
    endtoken=
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
Ant::PreDefinedTask_strategy = st.builds(
    Ant::PreDefinedTask,
    description=
        safe_text,
    taskname=
        safe_text,
    id=
        safe_text
)
Ant::NewTask_strategy = st.builds(
    Ant::NewTask,
)
Ant::Target_strategy = st.builds(
    Ant::Target,
    ifCondition=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    unless=
        safe_text
)

@given(instance=InExcludes_strategy)
@settings(max_examples=50)
def test_inexcludes_instantiation(instance):
    assert isinstance(instance, InExcludes)

@given(instance=Ant::ExcludesFile_strategy)
@settings(max_examples=50)
def test_ant::excludesfile_instantiation(instance):
    assert isinstance(instance, Ant::ExcludesFile)

@given(instance=Ant::Excludes_strategy)
@settings(max_examples=50)
def test_ant::excludes_instantiation(instance):
    assert isinstance(instance, Ant::Excludes)

@given(instance=Ant::IncludesFile_strategy)
@settings(max_examples=50)
def test_ant::includesfile_instantiation(instance):
    assert isinstance(instance, Ant::IncludesFile)

@given(instance=Ant::Includes_strategy)
@settings(max_examples=50)
def test_ant::includes_instantiation(instance):
    assert isinstance(instance, Ant::Includes)

@given(instance=Basic_strategy)
@settings(max_examples=50)
def test_basic_instantiation(instance):
    assert isinstance(instance, Basic)

@given(instance=Ant::InExcludes_strategy)
@settings(max_examples=50)
def test_ant::inexcludes_instantiation(instance):
    assert isinstance(instance, Ant::InExcludes)

@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_unless_type(instance):
    assert isinstance(instance.unless, str)


@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original

@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_ifCondition_type(instance):
    assert isinstance(instance.ifCondition, str)


@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original

@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::InExcludes_strategy)
def test_ant::inexcludes_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant::FileList_strategy)
@settings(max_examples=50)
def test_ant::filelist_instantiation(instance):
    assert isinstance(instance, Ant::FileList)

@given(instance=Ant::FileList_strategy)
def test_ant::filelist_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=Ant::FileList_strategy)
def test_ant::filelist_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Ant::FileList_strategy)
def test_ant::filelist_files_type(instance):
    assert isinstance(instance.files, str)


@given(instance=Ant::FileList_strategy)
def test_ant::filelist_files_setter(instance):
    original = instance.files
    instance.files = original
    assert instance.files == original

@given(instance=Ant::Mapper_strategy)
@settings(max_examples=50)
def test_ant::mapper_instantiation(instance):
    assert isinstance(instance, Ant::Mapper)

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_to_type(instance):
    assert isinstance(instance.to, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_to_setter(instance):
    original = instance.to
    instance.to = original
    assert instance.to == original

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classpathref_type(instance):
    assert isinstance(instance.classpathref, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classpathref_setter(instance):
    original = instance.classpathref
    instance.classpathref = original
    assert instance.classpathref == original

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classpath_type(instance):
    assert isinstance(instance.classpath, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_classpath_setter(instance):
    original = instance.classpath
    instance.classpath = original
    assert instance.classpath == original

@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Ant::Mapper_strategy)
def test_ant::mapper_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Pattern_strategy)
@settings(max_examples=50)
def test_pattern_instantiation(instance):
    assert isinstance(instance, Pattern)

@given(instance=Ant::Basic_strategy)
@settings(max_examples=50)
def test_ant::basic_instantiation(instance):
    assert isinstance(instance, Ant::Basic)

@given(instance=Ant::Pattern_strategy)
@settings(max_examples=50)
def test_ant::pattern_instantiation(instance):
    assert isinstance(instance, Ant::Pattern)

@given(instance=Ant::Project_strategy)
@settings(max_examples=50)
def test_ant::project_instantiation(instance):
    assert isinstance(instance, Ant::Project)

@given(instance=Ant::Project_strategy)
def test_ant::project_basedir_type(instance):
    assert isinstance(instance.basedir, str)


@given(instance=Ant::Project_strategy)
def test_ant::project_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original

@given(instance=Ant::Project_strategy)
def test_ant::project_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::Project_strategy)
def test_ant::project_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant::Project_strategy)
def test_ant::project_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Ant::Project_strategy)
def test_ant::project_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PropertyName_strategy)
@settings(max_examples=50)
def test_propertyname_instantiation(instance):
    assert isinstance(instance, PropertyName)

@given(instance=Ant::PropertyLocation_strategy)
@settings(max_examples=50)
def test_ant::propertylocation_instantiation(instance):
    assert isinstance(instance, Ant::PropertyLocation)

@given(instance=Ant::PropertyLocation_strategy)
def test_ant::propertylocation_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=Ant::PropertyLocation_strategy)
def test_ant::propertylocation_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Ant::PropertyValue_strategy)
@settings(max_examples=50)
def test_ant::propertyvalue_instantiation(instance):
    assert isinstance(instance, Ant::PropertyValue)

@given(instance=Ant::PropertyValue_strategy)
def test_ant::propertyvalue_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Ant::PropertyValue_strategy)
def test_ant::propertyvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Ant::Property_strategy)
@settings(max_examples=50)
def test_ant::property_instantiation(instance):
    assert isinstance(instance, Ant::Property)

@given(instance=TaskDef_strategy)
@settings(max_examples=50)
def test_taskdef_instantiation(instance):
    assert isinstance(instance, TaskDef)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=Ant::PropertyEnv_strategy)
@settings(max_examples=50)
def test_ant::propertyenv_instantiation(instance):
    assert isinstance(instance, Ant::PropertyEnv)

@given(instance=Ant::PropertyEnv_strategy)
def test_ant::propertyenv_environment_type(instance):
    assert isinstance(instance.environment, str)


@given(instance=Ant::PropertyEnv_strategy)
def test_ant::propertyenv_environment_setter(instance):
    original = instance.environment
    instance.environment = original
    assert instance.environment == original

@given(instance=Ant::PropertyFile_strategy)
@settings(max_examples=50)
def test_ant::propertyfile_instantiation(instance):
    assert isinstance(instance, Ant::PropertyFile)

@given(instance=Ant::PropertyFile_strategy)
def test_ant::propertyfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=Ant::PropertyFile_strategy)
def test_ant::propertyfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant::PropertyName_strategy)
@settings(max_examples=50)
def test_ant::propertyname_instantiation(instance):
    assert isinstance(instance, Ant::PropertyName)

@given(instance=Ant::PropertyName_strategy)
def test_ant::propertyname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::PropertyName_strategy)
def test_ant::propertyname_name_setter(instance):
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

@given(instance=Ant::Delete_strategy)
@settings(max_examples=50)
def test_ant::delete_instantiation(instance):
    assert isinstance(instance, Ant::Delete)

@given(instance=Ant::Delete_strategy)
def test_ant::delete_verbose_type(instance):
    assert isinstance(instance.verbose, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_includeEmptyDirs_type(instance):
    assert isinstance(instance.includeEmptyDirs, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_includes_type(instance):
    assert isinstance(instance.includes, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_includes_setter(instance):
    original = instance.includes
    instance.includes = original
    assert instance.includes == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_defaultexcludes_type(instance):
    assert isinstance(instance.defaultexcludes, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_includesfile_type(instance):
    assert isinstance(instance.includesfile, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_includesfile_setter(instance):
    original = instance.includesfile
    instance.includesfile = original
    assert instance.includesfile == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_failonerror_type(instance):
    assert isinstance(instance.failonerror, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_failonerror_setter(instance):
    original = instance.failonerror
    instance.failonerror = original
    assert instance.failonerror == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_excludesfile_type(instance):
    assert isinstance(instance.excludesfile, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_excludesfile_setter(instance):
    original = instance.excludesfile
    instance.excludesfile = original
    assert instance.excludesfile == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_excludes_type(instance):
    assert isinstance(instance.excludes, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_excludes_setter(instance):
    original = instance.excludes
    instance.excludes = original
    assert instance.excludes == original

@given(instance=Ant::Delete_strategy)
def test_ant::delete_quiet_type(instance):
    assert isinstance(instance.quiet, str)


@given(instance=Ant::Delete_strategy)
def test_ant::delete_quiet_setter(instance):
    original = instance.quiet
    instance.quiet = original
    assert instance.quiet == original

@given(instance=Ant::Mkdir_strategy)
@settings(max_examples=50)
def test_ant::mkdir_instantiation(instance):
    assert isinstance(instance, Ant::Mkdir)

@given(instance=Ant::Mkdir_strategy)
def test_ant::mkdir_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=Ant::Mkdir_strategy)
def test_ant::mkdir_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=ArchiveTask_strategy)
@settings(max_examples=50)
def test_archivetask_instantiation(instance):
    assert isinstance(instance, ArchiveTask)

@given(instance=Ant::Jar_strategy)
@settings(max_examples=50)
def test_ant::jar_instantiation(instance):
    assert isinstance(instance, Ant::Jar)

@given(instance=Ant::Jar_strategy)
def test_ant::jar_jarfile_type(instance):
    assert isinstance(instance.jarfile, str)


@given(instance=Ant::Jar_strategy)
def test_ant::jar_jarfile_setter(instance):
    original = instance.jarfile
    instance.jarfile = original
    assert instance.jarfile == original

@given(instance=Ant::Jar_strategy)
def test_ant::jar_encoding_type(instance):
    assert isinstance(instance.encoding, str)


@given(instance=Ant::Jar_strategy)
def test_ant::jar_encoding_setter(instance):
    original = instance.encoding
    instance.encoding = original
    assert instance.encoding == original

@given(instance=Ant::Jar_strategy)
def test_ant::jar_manifest_type(instance):
    assert isinstance(instance.manifest, str)


@given(instance=Ant::Jar_strategy)
def test_ant::jar_manifest_setter(instance):
    original = instance.manifest
    instance.manifest = original
    assert instance.manifest == original

@given(instance=Ant::Jar_strategy)
def test_ant::jar_basedir_type(instance):
    assert isinstance(instance.basedir, str)


@given(instance=Ant::Jar_strategy)
def test_ant::jar_basedir_setter(instance):
    original = instance.basedir
    instance.basedir = original
    assert instance.basedir == original

@given(instance=Ant::Jar_strategy)
def test_ant::jar_compress_type(instance):
    assert isinstance(instance.compress, str)


@given(instance=Ant::Jar_strategy)
def test_ant::jar_compress_setter(instance):
    original = instance.compress
    instance.compress = original
    assert instance.compress == original

@given(instance=DocumentationTask_strategy)
@settings(max_examples=50)
def test_documentationtask_instantiation(instance):
    assert isinstance(instance, DocumentationTask)

@given(instance=Ant::Javadoc_strategy)
@settings(max_examples=50)
def test_ant::javadoc_instantiation(instance):
    assert isinstance(instance, Ant::Javadoc)

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_defaultexcludes_type(instance):
    assert isinstance(instance.defaultexcludes, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_defaultexcludes_setter(instance):
    original = instance.defaultexcludes
    instance.defaultexcludes = original
    assert instance.defaultexcludes == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_use_type(instance):
    assert isinstance(instance.use, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_use_setter(instance):
    original = instance.use
    instance.use = original
    assert instance.use == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_windowtitle_type(instance):
    assert isinstance(instance.windowtitle, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_windowtitle_setter(instance):
    original = instance.windowtitle
    instance.windowtitle = original
    assert instance.windowtitle == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_sourcepath_type(instance):
    assert isinstance(instance.sourcepath, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_sourcepath_setter(instance):
    original = instance.sourcepath
    instance.sourcepath = original
    assert instance.sourcepath == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_packagenames_type(instance):
    assert isinstance(instance.packagenames, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_packagenames_setter(instance):
    original = instance.packagenames
    instance.packagenames = original
    assert instance.packagenames == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_destdir_type(instance):
    assert isinstance(instance.destdir, str)


@given(instance=Ant::Javadoc_strategy)
def test_ant::javadoc_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original

@given(instance=CompileTask_strategy)
@settings(max_examples=50)
def test_compiletask_instantiation(instance):
    assert isinstance(instance, CompileTask)

@given(instance=Ant::Copy_strategy)
@settings(max_examples=50)
def test_ant::copy_instantiation(instance):
    assert isinstance(instance, Ant::Copy)

@given(instance=Ant::Copy_strategy)
def test_ant::copy_tofile_type(instance):
    assert isinstance(instance.tofile, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_tofile_setter(instance):
    original = instance.tofile
    instance.tofile = original
    assert instance.tofile == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_todir_type(instance):
    assert isinstance(instance.todir, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_todir_setter(instance):
    original = instance.todir
    instance.todir = original
    assert instance.todir == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_filtering_type(instance):
    assert isinstance(instance.filtering, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_filtering_setter(instance):
    original = instance.filtering
    instance.filtering = original
    assert instance.filtering == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_includeEmptyDirs_type(instance):
    assert isinstance(instance.includeEmptyDirs, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_includeEmptyDirs_setter(instance):
    original = instance.includeEmptyDirs
    instance.includeEmptyDirs = original
    assert instance.includeEmptyDirs == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_overwrite_type(instance):
    assert isinstance(instance.overwrite, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_overwrite_setter(instance):
    original = instance.overwrite
    instance.overwrite = original
    assert instance.overwrite == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_flatten_type(instance):
    assert isinstance(instance.flatten, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_flatten_setter(instance):
    original = instance.flatten
    instance.flatten = original
    assert instance.flatten == original

@given(instance=Ant::Copy_strategy)
def test_ant::copy_presservelastmodified_type(instance):
    assert isinstance(instance.presservelastmodified, str)


@given(instance=Ant::Copy_strategy)
def test_ant::copy_presservelastmodified_setter(instance):
    original = instance.presservelastmodified
    instance.presservelastmodified = original
    assert instance.presservelastmodified == original

@given(instance=Ant::Javac_strategy)
@settings(max_examples=50)
def test_ant::javac_instantiation(instance):
    assert isinstance(instance, Ant::Javac)

@given(instance=Ant::Javac_strategy)
def test_ant::javac_optimize_type(instance):
    assert isinstance(instance.optimize, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_optimize_setter(instance):
    original = instance.optimize
    instance.optimize = original
    assert instance.optimize == original

@given(instance=Ant::Javac_strategy)
def test_ant::javac_deprecation_type(instance):
    assert isinstance(instance.deprecation, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_deprecation_setter(instance):
    original = instance.deprecation
    instance.deprecation = original
    assert instance.deprecation == original

@given(instance=Ant::Javac_strategy)
def test_ant::javac_fork_type(instance):
    assert isinstance(instance.fork, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=Ant::Javac_strategy)
def test_ant::javac_destdir_type(instance):
    assert isinstance(instance.destdir, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_destdir_setter(instance):
    original = instance.destdir
    instance.destdir = original
    assert instance.destdir == original

@given(instance=Ant::Javac_strategy)
def test_ant::javac_srcdir_type(instance):
    assert isinstance(instance.srcdir, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_srcdir_setter(instance):
    original = instance.srcdir
    instance.srcdir = original
    assert instance.srcdir == original

@given(instance=Ant::Javac_strategy)
def test_ant::javac_debug_type(instance):
    assert isinstance(instance.debug, str)


@given(instance=Ant::Javac_strategy)
def test_ant::javac_debug_setter(instance):
    original = instance.debug
    instance.debug = original
    assert instance.debug == original

@given(instance=Ant::TaskDef_strategy)
@settings(max_examples=50)
def test_ant::taskdef_instantiation(instance):
    assert isinstance(instance, Ant::TaskDef)

@given(instance=Ant::TaskDef_strategy)
def test_ant::taskdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::TaskDef_strategy)
def test_ant::taskdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant::TaskDef_strategy)
def test_ant::taskdef_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=Ant::TaskDef_strategy)
def test_ant::taskdef_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=Ant::FormatTstamp_strategy)
@settings(max_examples=50)
def test_ant::formattstamp_instantiation(instance):
    assert isinstance(instance, Ant::FormatTstamp)

@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_offset_type(instance):
    assert isinstance(instance.offset, str)


@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_property_type(instance):
    assert isinstance(instance.property, str)


@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original

@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_locale_type(instance):
    assert isinstance(instance.locale, str)


@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_locale_setter(instance):
    original = instance.locale
    instance.locale = original
    assert instance.locale == original

@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=Ant::FormatTstamp_strategy)
def test_ant::formattstamp_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=Ant::Task_strategy)
@settings(max_examples=50)
def test_ant::task_instantiation(instance):
    assert isinstance(instance, Ant::Task)

@given(instance=FormatTstamp_strategy)
@settings(max_examples=50)
def test_formattstamp_instantiation(instance):
    assert isinstance(instance, FormatTstamp)

@given(instance=MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_miscellaneoustask_instantiation(instance):
    assert isinstance(instance, MiscellaneousTask)

@given(instance=Ant::Tstamp_strategy)
@settings(max_examples=50)
def test_ant::tstamp_instantiation(instance):
    assert isinstance(instance, Ant::Tstamp)

@given(instance=Ant::Echo_strategy)
@settings(max_examples=50)
def test_ant::echo_instantiation(instance):
    assert isinstance(instance, Ant::Echo)

@given(instance=Ant::Echo_strategy)
def test_ant::echo_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=Ant::Echo_strategy)
def test_ant::echo_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant::Echo_strategy)
def test_ant::echo_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=Ant::Echo_strategy)
def test_ant::echo_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=Ant::Echo_strategy)
def test_ant::echo_append_type(instance):
    assert isinstance(instance.append, str)


@given(instance=Ant::Echo_strategy)
def test_ant::echo_append_setter(instance):
    original = instance.append
    instance.append = original
    assert instance.append == original

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

@given(instance=Ant::Java_strategy)
@settings(max_examples=50)
def test_ant::java_instantiation(instance):
    assert isinstance(instance, Ant::Java)

@given(instance=Ant::Java_strategy)
def test_ant::java_fork_type(instance):
    assert isinstance(instance.fork, str)


@given(instance=Ant::Java_strategy)
def test_ant::java_fork_setter(instance):
    original = instance.fork
    instance.fork = original
    assert instance.fork == original

@given(instance=Ant::Java_strategy)
def test_ant::java_jar_type(instance):
    assert isinstance(instance.jar, str)


@given(instance=Ant::Java_strategy)
def test_ant::java_jar_setter(instance):
    original = instance.jar
    instance.jar = original
    assert instance.jar == original

@given(instance=Ant::Java_strategy)
def test_ant::java_classname_type(instance):
    assert isinstance(instance.classname, str)


@given(instance=Ant::Java_strategy)
def test_ant::java_classname_setter(instance):
    original = instance.classname
    instance.classname = original
    assert instance.classname == original

@given(instance=Ant::Exec_strategy)
@settings(max_examples=50)
def test_ant::exec_instantiation(instance):
    assert isinstance(instance, Ant::Exec)

@given(instance=Ant::Exec_strategy)
def test_ant::exec_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=Ant::Exec_strategy)
def test_ant::exec_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Ant::Exec_strategy)
def test_ant::exec_executable_type(instance):
    assert isinstance(instance.executable, str)


@given(instance=Ant::Exec_strategy)
def test_ant::exec_executable_setter(instance):
    original = instance.executable
    instance.executable = original
    assert instance.executable == original

@given(instance=PreDefinedTask_strategy)
@settings(max_examples=50)
def test_predefinedtask_instantiation(instance):
    assert isinstance(instance, PreDefinedTask)

@given(instance=Ant::FileTask_strategy)
@settings(max_examples=50)
def test_ant::filetask_instantiation(instance):
    assert isinstance(instance, Ant::FileTask)

@given(instance=Ant::CompileTask_strategy)
@settings(max_examples=50)
def test_ant::compiletask_instantiation(instance):
    assert isinstance(instance, Ant::CompileTask)

@given(instance=Ant::DocumentationTask_strategy)
@settings(max_examples=50)
def test_ant::documentationtask_instantiation(instance):
    assert isinstance(instance, Ant::DocumentationTask)

@given(instance=Ant::MiscellaneousTask_strategy)
@settings(max_examples=50)
def test_ant::miscellaneoustask_instantiation(instance):
    assert isinstance(instance, Ant::MiscellaneousTask)

@given(instance=Ant::ArchiveTask_strategy)
@settings(max_examples=50)
def test_ant::archivetask_instantiation(instance):
    assert isinstance(instance, Ant::ArchiveTask)

@given(instance=Ant::ExecutionTask_strategy)
@settings(max_examples=50)
def test_ant::executiontask_instantiation(instance):
    assert isinstance(instance, Ant::ExecutionTask)

@given(instance=Ant::Attribut_strategy)
@settings(max_examples=50)
def test_ant::attribut_instantiation(instance):
    assert isinstance(instance, Ant::Attribut)

@given(instance=Ant::Attribut_strategy)
def test_ant::attribut_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::Attribut_strategy)
def test_ant::attribut_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant::Attribut_strategy)
def test_ant::attribut_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Ant::Attribut_strategy)
def test_ant::attribut_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Attribut_strategy)
@settings(max_examples=50)
def test_attribut_instantiation(instance):
    assert isinstance(instance, Attribut)

@given(instance=Set_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, Set)

@given(instance=Ant::ClassPath_strategy)
@settings(max_examples=50)
def test_ant::classpath_instantiation(instance):
    assert isinstance(instance, Ant::ClassPath)

@given(instance=Ant::ClassPath_strategy)
def test_ant::classpath_refid_type(instance):
    assert isinstance(instance.refid, str)


@given(instance=Ant::ClassPath_strategy)
def test_ant::classpath_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=Ant::FileSet_strategy)
@settings(max_examples=50)
def test_ant::fileset_instantiation(instance):
    assert isinstance(instance, Ant::FileSet)

@given(instance=Ant::FileSet_strategy)
def test_ant::fileset_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=Ant::FileSet_strategy)
def test_ant::fileset_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Ant::PatternSet_strategy)
@settings(max_examples=50)
def test_ant::patternset_instantiation(instance):
    assert isinstance(instance, Ant::PatternSet)

@given(instance=Ant::Set_strategy)
@settings(max_examples=50)
def test_ant::set_instantiation(instance):
    assert isinstance(instance, Ant::Set)

@given(instance=Ant::PathElement_strategy)
@settings(max_examples=50)
def test_ant::pathelement_instantiation(instance):
    assert isinstance(instance, Ant::PathElement)

@given(instance=Ant::PathElement_strategy)
def test_ant::pathelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=Ant::PathElement_strategy)
def test_ant::pathelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Ant::PathElement_strategy)
def test_ant::pathelement_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=Ant::PathElement_strategy)
def test_ant::pathelement_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=Ant::FiltersFile_strategy)
@settings(max_examples=50)
def test_ant::filtersfile_instantiation(instance):
    assert isinstance(instance, Ant::FiltersFile)

@given(instance=Ant::FiltersFile_strategy)
def test_ant::filtersfile_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=Ant::FiltersFile_strategy)
def test_ant::filtersfile_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=Ant::Filter_strategy)
@settings(max_examples=50)
def test_ant::filter_instantiation(instance):
    assert isinstance(instance, Ant::Filter)

@given(instance=Ant::Filter_strategy)
def test_ant::filter_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Ant::Filter_strategy)
def test_ant::filter_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Ant::Filter_strategy)
def test_ant::filter_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=Ant::Filter_strategy)
def test_ant::filter_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=Ant::Path_strategy)
@settings(max_examples=50)
def test_ant::path_instantiation(instance):
    assert isinstance(instance, Ant::Path)

@given(instance=Ant::Path_strategy)
def test_ant::path_refid_type(instance):
    assert isinstance(instance.refid, str)


@given(instance=Ant::Path_strategy)
def test_ant::path_refid_setter(instance):
    original = instance.refid
    instance.refid = original
    assert instance.refid == original

@given(instance=Ant::Path_strategy)
def test_ant::path_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Ant::Path_strategy)
def test_ant::path_id_setter(instance):
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

@given(instance=Ant::FilterSet_strategy)
@settings(max_examples=50)
def test_ant::filterset_instantiation(instance):
    assert isinstance(instance, Ant::FilterSet)

@given(instance=Ant::FilterSet_strategy)
def test_ant::filterset_starttoken_type(instance):
    assert isinstance(instance.starttoken, str)


@given(instance=Ant::FilterSet_strategy)
def test_ant::filterset_starttoken_setter(instance):
    original = instance.starttoken
    instance.starttoken = original
    assert instance.starttoken == original

@given(instance=Ant::FilterSet_strategy)
def test_ant::filterset_endtoken_type(instance):
    assert isinstance(instance.endtoken, str)


@given(instance=Ant::FilterSet_strategy)
def test_ant::filterset_endtoken_setter(instance):
    original = instance.endtoken
    instance.endtoken = original
    assert instance.endtoken == original

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

@given(instance=Ant::PreDefinedTask_strategy)
@settings(max_examples=50)
def test_ant::predefinedtask_instantiation(instance):
    assert isinstance(instance, Ant::PreDefinedTask)

@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_taskname_type(instance):
    assert isinstance(instance.taskname, str)


@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_taskname_setter(instance):
    original = instance.taskname
    instance.taskname = original
    assert instance.taskname == original

@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Ant::PreDefinedTask_strategy)
def test_ant::predefinedtask_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Ant::NewTask_strategy)
@settings(max_examples=50)
def test_ant::newtask_instantiation(instance):
    assert isinstance(instance, Ant::NewTask)

@given(instance=Ant::Target_strategy)
@settings(max_examples=50)
def test_ant::target_instantiation(instance):
    assert isinstance(instance, Ant::Target)

@given(instance=Ant::Target_strategy)
def test_ant::target_ifCondition_type(instance):
    assert isinstance(instance.ifCondition, str)


@given(instance=Ant::Target_strategy)
def test_ant::target_ifCondition_setter(instance):
    original = instance.ifCondition
    instance.ifCondition = original
    assert instance.ifCondition == original

@given(instance=Ant::Target_strategy)
def test_ant::target_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Ant::Target_strategy)
def test_ant::target_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Ant::Target_strategy)
def test_ant::target_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Ant::Target_strategy)
def test_ant::target_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Ant::Target_strategy)
def test_ant::target_unless_type(instance):
    assert isinstance(instance.unless, str)


@given(instance=Ant::Target_strategy)
def test_ant::target_unless_setter(instance):
    original = instance.unless
    instance.unless = original
    assert instance.unless == original
