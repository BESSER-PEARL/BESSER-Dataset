import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sourcecleaner::ExtensionReference,
    sourcecleaner::ExtensionAttribute,
    sourcecleaner::Dependency,
    Source,
    sourcecleaner::LocatedElement,
    sourcecleaner::Schema,
    sourcecleaner::ExtensionPoint,
    sourcecleaner::Extension,
    sourcecleaner::Export,
    sourcecleaner::ClassPath,
    LocatedElement,
    sourcecleaner::Source,
    sourcecleaner::Project,
    sourcecleaner::Configuration,
    sourcecleaner::Plugin,
    sourcecleaner::Build,
    sourcecleaner::Manifest,
    sourcecleaner::Java,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sourcecleaner::extensionreference_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::ExtensionReference)


def test_sourcecleaner::extensionreference_constructor_exists():
    assert callable(sourcecleaner::ExtensionReference.__init__)


def test_sourcecleaner::extensionreference_constructor_args():
    sig = inspect.signature(sourcecleaner::ExtensionReference.__init__)
    params = list(sig.parameters.keys())
    assert "java" in params, "Missing parameter 'java'"
    assert "name" in params, "Missing parameter 'name'"
    assert "project" in params, "Missing parameter 'project'"
    assert "package" in params, "Missing parameter 'package'"

def test_sourcecleaner::extensionreference_has_java():
    assert hasattr(sourcecleaner::ExtensionReference, "java")
    descriptor = None
    for klass in sourcecleaner::ExtensionReference.__mro__:
        if "java" in klass.__dict__:
            descriptor = klass.__dict__["java"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionreference_has_name():
    assert hasattr(sourcecleaner::ExtensionReference, "name")
    descriptor = None
    for klass in sourcecleaner::ExtensionReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionreference_has_project():
    assert hasattr(sourcecleaner::ExtensionReference, "project")
    descriptor = None
    for klass in sourcecleaner::ExtensionReference.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionreference_has_package():
    assert hasattr(sourcecleaner::ExtensionReference, "package")
    descriptor = None
    for klass in sourcecleaner::ExtensionReference.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::extensionattribute_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::ExtensionAttribute)


def test_sourcecleaner::extensionattribute_constructor_exists():
    assert callable(sourcecleaner::ExtensionAttribute.__init__)


def test_sourcecleaner::extensionattribute_constructor_args():
    sig = inspect.signature(sourcecleaner::ExtensionAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner::extensionattribute_has_value():
    assert hasattr(sourcecleaner::ExtensionAttribute, "value")
    descriptor = None
    for klass in sourcecleaner::ExtensionAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionattribute_has_name():
    assert hasattr(sourcecleaner::ExtensionAttribute, "name")
    descriptor = None
    for klass in sourcecleaner::ExtensionAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::dependency_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Dependency)


def test_sourcecleaner::dependency_constructor_exists():
    assert callable(sourcecleaner::Dependency.__init__)


def test_sourcecleaner::dependency_constructor_args():
    sig = inspect.signature(sourcecleaner::Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "reexport" in params, "Missing parameter 'reexport'"
    assert "version" in params, "Missing parameter 'version'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner::dependency_has_diagraph():
    assert hasattr(sourcecleaner::Dependency, "diagraph")
    descriptor = None
    for klass in sourcecleaner::Dependency.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::dependency_has_reexport():
    assert hasattr(sourcecleaner::Dependency, "reexport")
    descriptor = None
    for klass in sourcecleaner::Dependency.__mro__:
        if "reexport" in klass.__dict__:
            descriptor = klass.__dict__["reexport"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::dependency_has_version():
    assert hasattr(sourcecleaner::Dependency, "version")
    descriptor = None
    for klass in sourcecleaner::Dependency.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::dependency_has_name():
    assert hasattr(sourcecleaner::Dependency, "name")
    descriptor = None
    for klass in sourcecleaner::Dependency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_sourcecleaner::locatedelement_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::LocatedElement)


def test_sourcecleaner::locatedelement_constructor_exists():
    assert callable(sourcecleaner::LocatedElement.__init__)


def test_sourcecleaner::locatedelement_constructor_args():
    sig = inspect.signature(sourcecleaner::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "absolutePath" in params, "Missing parameter 'absolutePath'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner::locatedelement_has_absolutePath():
    assert hasattr(sourcecleaner::LocatedElement, "absolutePath")
    descriptor = None
    for klass in sourcecleaner::LocatedElement.__mro__:
        if "absolutePath" in klass.__dict__:
            descriptor = klass.__dict__["absolutePath"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::locatedelement_has_name():
    assert hasattr(sourcecleaner::LocatedElement, "name")
    descriptor = None
    for klass in sourcecleaner::LocatedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::schema_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Schema)


def test_sourcecleaner::schema_constructor_exists():
    assert callable(sourcecleaner::Schema.__init__)


def test_sourcecleaner::schema_constructor_args():
    sig = inspect.signature(sourcecleaner::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "pluginName" in params, "Missing parameter 'pluginName'"
    assert "extensionName" in params, "Missing parameter 'extensionName'"
    assert "extensionId" in params, "Missing parameter 'extensionId'"

def test_sourcecleaner::schema_has_pluginName():
    assert hasattr(sourcecleaner::Schema, "pluginName")
    descriptor = None
    for klass in sourcecleaner::Schema.__mro__:
        if "pluginName" in klass.__dict__:
            descriptor = klass.__dict__["pluginName"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::schema_has_extensionName():
    assert hasattr(sourcecleaner::Schema, "extensionName")
    descriptor = None
    for klass in sourcecleaner::Schema.__mro__:
        if "extensionName" in klass.__dict__:
            descriptor = klass.__dict__["extensionName"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::schema_has_extensionId():
    assert hasattr(sourcecleaner::Schema, "extensionId")
    descriptor = None
    for klass in sourcecleaner::Schema.__mro__:
        if "extensionId" in klass.__dict__:
            descriptor = klass.__dict__["extensionId"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::extensionpoint_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::ExtensionPoint)


def test_sourcecleaner::extensionpoint_constructor_exists():
    assert callable(sourcecleaner::ExtensionPoint.__init__)


def test_sourcecleaner::extensionpoint_constructor_args():
    sig = inspect.signature(sourcecleaner::ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "diagraph" in params, "Missing parameter 'diagraph'"

def test_sourcecleaner::extensionpoint_has_id():
    assert hasattr(sourcecleaner::ExtensionPoint, "id")
    descriptor = None
    for klass in sourcecleaner::ExtensionPoint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionpoint_has_name():
    assert hasattr(sourcecleaner::ExtensionPoint, "name")
    descriptor = None
    for klass in sourcecleaner::ExtensionPoint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionpoint_has_schema():
    assert hasattr(sourcecleaner::ExtensionPoint, "schema")
    descriptor = None
    for klass in sourcecleaner::ExtensionPoint.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extensionpoint_has_diagraph():
    assert hasattr(sourcecleaner::ExtensionPoint, "diagraph")
    descriptor = None
    for klass in sourcecleaner::ExtensionPoint.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::extension_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Extension)


def test_sourcecleaner::extension_constructor_exists():
    assert callable(sourcecleaner::Extension.__init__)


def test_sourcecleaner::extension_constructor_args():
    sig = inspect.signature(sourcecleaner::Extension.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "extra" in params, "Missing parameter 'extra'"
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "pointId" in params, "Missing parameter 'pointId'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "id" in params, "Missing parameter 'id'"

def test_sourcecleaner::extension_has_name():
    assert hasattr(sourcecleaner::Extension, "name")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extension_has_extra():
    assert hasattr(sourcecleaner::Extension, "extra")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extension_has_diagraph():
    assert hasattr(sourcecleaner::Extension, "diagraph")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extension_has_pointId():
    assert hasattr(sourcecleaner::Extension, "pointId")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "pointId" in klass.__dict__:
            descriptor = klass.__dict__["pointId"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extension_has_clazz():
    assert hasattr(sourcecleaner::Extension, "clazz")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::extension_has_id():
    assert hasattr(sourcecleaner::Extension, "id")
    descriptor = None
    for klass in sourcecleaner::Extension.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::export_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Export)


def test_sourcecleaner::export_constructor_exists():
    assert callable(sourcecleaner::Export.__init__)


def test_sourcecleaner::export_constructor_args():
    sig = inspect.signature(sourcecleaner::Export.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner::export_has_name():
    assert hasattr(sourcecleaner::Export, "name")
    descriptor = None
    for klass in sourcecleaner::Export.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::classpath_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::ClassPath)


def test_sourcecleaner::classpath_constructor_exists():
    assert callable(sourcecleaner::ClassPath.__init__)


def test_sourcecleaner::classpath_constructor_args():
    sig = inspect.signature(sourcecleaner::ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner::classpath_has_name():
    assert hasattr(sourcecleaner::ClassPath, "name")
    descriptor = None
    for klass in sourcecleaner::ClassPath.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_sourcecleaner::source_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Source)


def test_sourcecleaner::source_constructor_exists():
    assert callable(sourcecleaner::Source.__init__)


def test_sourcecleaner::source_constructor_args():
    sig = inspect.signature(sourcecleaner::Source.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "mark" in params, "Missing parameter 'mark'"
    assert "handled" in params, "Missing parameter 'handled'"
    assert "content" in params, "Missing parameter 'content'"

def test_sourcecleaner::source_has_comment():
    assert hasattr(sourcecleaner::Source, "comment")
    descriptor = None
    for klass in sourcecleaner::Source.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::source_has_mark():
    assert hasattr(sourcecleaner::Source, "mark")
    descriptor = None
    for klass in sourcecleaner::Source.__mro__:
        if "mark" in klass.__dict__:
            descriptor = klass.__dict__["mark"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::source_has_handled():
    assert hasattr(sourcecleaner::Source, "handled")
    descriptor = None
    for klass in sourcecleaner::Source.__mro__:
        if "handled" in klass.__dict__:
            descriptor = klass.__dict__["handled"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::source_has_content():
    assert hasattr(sourcecleaner::Source, "content")
    descriptor = None
    for klass in sourcecleaner::Source.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::project_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Project)


def test_sourcecleaner::project_constructor_exists():
    assert callable(sourcecleaner::Project.__init__)


def test_sourcecleaner::project_constructor_args():
    sig = inspect.signature(sourcecleaner::Project.__init__)
    params = list(sig.parameters.keys())
    assert "workspace" in params, "Missing parameter 'workspace'"
    assert "id" in params, "Missing parameter 'id'"

def test_sourcecleaner::project_has_workspace():
    assert hasattr(sourcecleaner::Project, "workspace")
    descriptor = None
    for klass in sourcecleaner::Project.__mro__:
        if "workspace" in klass.__dict__:
            descriptor = klass.__dict__["workspace"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::project_has_id():
    assert hasattr(sourcecleaner::Project, "id")
    descriptor = None
    for klass in sourcecleaner::Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::configuration_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Configuration)


def test_sourcecleaner::configuration_constructor_exists():
    assert callable(sourcecleaner::Configuration.__init__)


def test_sourcecleaner::configuration_constructor_args():
    sig = inspect.signature(sourcecleaner::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "temp" in params, "Missing parameter 'temp'"

def test_sourcecleaner::configuration_has_location():
    assert hasattr(sourcecleaner::Configuration, "location")
    descriptor = None
    for klass in sourcecleaner::Configuration.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::configuration_has_temp():
    assert hasattr(sourcecleaner::Configuration, "temp")
    descriptor = None
    for klass in sourcecleaner::Configuration.__mro__:
        if "temp" in klass.__dict__:
            descriptor = klass.__dict__["temp"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::plugin_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Plugin)


def test_sourcecleaner::plugin_constructor_exists():
    assert callable(sourcecleaner::Plugin.__init__)


def test_sourcecleaner::plugin_constructor_args():
    sig = inspect.signature(sourcecleaner::Plugin.__init__)
    params = list(sig.parameters.keys())
    assert "extra" in params, "Missing parameter 'extra'"

def test_sourcecleaner::plugin_has_extra():
    assert hasattr(sourcecleaner::Plugin, "extra")
    descriptor = None
    for klass in sourcecleaner::Plugin.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::build_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Build)


def test_sourcecleaner::build_constructor_exists():
    assert callable(sourcecleaner::Build.__init__)


def test_sourcecleaner::build_constructor_args():
    sig = inspect.signature(sourcecleaner::Build.__init__)
    params = list(sig.parameters.keys())



def test_sourcecleaner::manifest_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Manifest)


def test_sourcecleaner::manifest_constructor_exists():
    assert callable(sourcecleaner::Manifest.__init__)


def test_sourcecleaner::manifest_constructor_args():
    sig = inspect.signature(sourcecleaner::Manifest.__init__)
    params = list(sig.parameters.keys())
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "version" in params, "Missing parameter 'version'"
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"
    assert "versionQualifier" in params, "Missing parameter 'versionQualifier'"
    assert "singleton" in params, "Missing parameter 'singleton'"
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "versionId" in params, "Missing parameter 'versionId'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "executionEnvironment" in params, "Missing parameter 'executionEnvironment'"

def test_sourcecleaner::manifest_has_vendor():
    assert hasattr(sourcecleaner::Manifest, "vendor")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_version():
    assert hasattr(sourcecleaner::Manifest, "version")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_symbolicName():
    assert hasattr(sourcecleaner::Manifest, "symbolicName")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_versionQualifier():
    assert hasattr(sourcecleaner::Manifest, "versionQualifier")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "versionQualifier" in klass.__dict__:
            descriptor = klass.__dict__["versionQualifier"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_singleton():
    assert hasattr(sourcecleaner::Manifest, "singleton")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "singleton" in klass.__dict__:
            descriptor = klass.__dict__["singleton"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_diagraph():
    assert hasattr(sourcecleaner::Manifest, "diagraph")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_versionId():
    assert hasattr(sourcecleaner::Manifest, "versionId")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "versionId" in klass.__dict__:
            descriptor = klass.__dict__["versionId"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_lazy():
    assert hasattr(sourcecleaner::Manifest, "lazy")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner::manifest_has_executionEnvironment():
    assert hasattr(sourcecleaner::Manifest, "executionEnvironment")
    descriptor = None
    for klass in sourcecleaner::Manifest.__mro__:
        if "executionEnvironment" in klass.__dict__:
            descriptor = klass.__dict__["executionEnvironment"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner::java_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner::Java)


def test_sourcecleaner::java_constructor_exists():
    assert callable(sourcecleaner::Java.__init__)


def test_sourcecleaner::java_constructor_args():
    sig = inspect.signature(sourcecleaner::Java.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_sourcecleaner::java_has_package():
    assert hasattr(sourcecleaner::Java, "package")
    descriptor = None
    for klass in sourcecleaner::Java.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
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
sourcecleaner::ExtensionReference_strategy = st.builds(
    sourcecleaner::ExtensionReference,
    java=
        safe_text,
    name=
        safe_text,
    project=
        safe_text,
    package=
        safe_text
)
sourcecleaner::ExtensionAttribute_strategy = st.builds(
    sourcecleaner::ExtensionAttribute,
    value=
        safe_text,
    name=
        safe_text
)
sourcecleaner::Dependency_strategy = st.builds(
    sourcecleaner::Dependency,
    diagraph=
        st.booleans(),
    reexport=
        st.booleans(),
    version=
        safe_text,
    name=
        safe_text
)
Source_strategy = st.builds(
    Source,
)
sourcecleaner::LocatedElement_strategy = st.builds(
    sourcecleaner::LocatedElement,
    absolutePath=
        safe_text,
    name=
        safe_text
)
sourcecleaner::Schema_strategy = st.builds(
    sourcecleaner::Schema,
    pluginName=
        safe_text,
    extensionName=
        safe_text,
    extensionId=
        safe_text
)
sourcecleaner::ExtensionPoint_strategy = st.builds(
    sourcecleaner::ExtensionPoint,
    id=
        safe_text,
    name=
        safe_text,
    schema=
        safe_text,
    diagraph=
        st.booleans()
)
sourcecleaner::Extension_strategy = st.builds(
    sourcecleaner::Extension,
    name=
        safe_text,
    extra=
        safe_text,
    diagraph=
        st.booleans(),
    pointId=
        safe_text,
    clazz=
        safe_text,
    id=
        safe_text
)
sourcecleaner::Export_strategy = st.builds(
    sourcecleaner::Export,
    name=
        safe_text
)
sourcecleaner::ClassPath_strategy = st.builds(
    sourcecleaner::ClassPath,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
sourcecleaner::Source_strategy = st.builds(
    sourcecleaner::Source,
    comment=
        safe_text,
    mark=
        st.booleans(),
    handled=
        st.booleans(),
    content=
        safe_text
)
sourcecleaner::Project_strategy = st.builds(
    sourcecleaner::Project,
    workspace=
        safe_text,
    id=
        st.integers()
)
sourcecleaner::Configuration_strategy = st.builds(
    sourcecleaner::Configuration,
    location=
        safe_text,
    temp=
        safe_text
)
sourcecleaner::Plugin_strategy = st.builds(
    sourcecleaner::Plugin,
    extra=
        safe_text
)
sourcecleaner::Build_strategy = st.builds(
    sourcecleaner::Build,
)
sourcecleaner::Manifest_strategy = st.builds(
    sourcecleaner::Manifest,
    vendor=
        safe_text,
    version=
        safe_text,
    symbolicName=
        safe_text,
    versionQualifier=
        safe_text,
    singleton=
        st.booleans(),
    diagraph=
        st.booleans(),
    versionId=
        safe_text,
    lazy=
        st.booleans(),
    executionEnvironment=
        safe_text
)
sourcecleaner::Java_strategy = st.builds(
    sourcecleaner::Java,
    package=
        safe_text
)

@given(instance=sourcecleaner::ExtensionReference_strategy)
@settings(max_examples=50)
def test_sourcecleaner::extensionreference_instantiation(instance):
    assert isinstance(instance, sourcecleaner::ExtensionReference)

@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_java_type(instance):
    assert isinstance(instance.java, str)


@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_java_setter(instance):
    original = instance.java
    instance.java = original
    assert instance.java == original

@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_project_type(instance):
    assert isinstance(instance.project, str)


@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=sourcecleaner::ExtensionReference_strategy)
def test_sourcecleaner::extensionreference_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=sourcecleaner::ExtensionAttribute_strategy)
@settings(max_examples=50)
def test_sourcecleaner::extensionattribute_instantiation(instance):
    assert isinstance(instance, sourcecleaner::ExtensionAttribute)

@given(instance=sourcecleaner::ExtensionAttribute_strategy)
def test_sourcecleaner::extensionattribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=sourcecleaner::ExtensionAttribute_strategy)
def test_sourcecleaner::extensionattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sourcecleaner::ExtensionAttribute_strategy)
def test_sourcecleaner::extensionattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::ExtensionAttribute_strategy)
def test_sourcecleaner::extensionattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::Dependency_strategy)
@settings(max_examples=50)
def test_sourcecleaner::dependency_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Dependency)

@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_diagraph_type(instance):
    assert isinstance(instance.diagraph, bool)


@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original

@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_reexport_type(instance):
    assert isinstance(instance.reexport, bool)


@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_reexport_setter(instance):
    original = instance.reexport
    instance.reexport = original
    assert instance.reexport == original

@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::Dependency_strategy)
def test_sourcecleaner::dependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=sourcecleaner::LocatedElement_strategy)
@settings(max_examples=50)
def test_sourcecleaner::locatedelement_instantiation(instance):
    assert isinstance(instance, sourcecleaner::LocatedElement)

@given(instance=sourcecleaner::LocatedElement_strategy)
def test_sourcecleaner::locatedelement_absolutePath_type(instance):
    assert isinstance(instance.absolutePath, str)


@given(instance=sourcecleaner::LocatedElement_strategy)
def test_sourcecleaner::locatedelement_absolutePath_setter(instance):
    original = instance.absolutePath
    instance.absolutePath = original
    assert instance.absolutePath == original

@given(instance=sourcecleaner::LocatedElement_strategy)
def test_sourcecleaner::locatedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::LocatedElement_strategy)
def test_sourcecleaner::locatedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::Schema_strategy)
@settings(max_examples=50)
def test_sourcecleaner::schema_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Schema)

@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_pluginName_type(instance):
    assert isinstance(instance.pluginName, str)


@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_pluginName_setter(instance):
    original = instance.pluginName
    instance.pluginName = original
    assert instance.pluginName == original

@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_extensionName_type(instance):
    assert isinstance(instance.extensionName, str)


@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_extensionName_setter(instance):
    original = instance.extensionName
    instance.extensionName = original
    assert instance.extensionName == original

@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_extensionId_type(instance):
    assert isinstance(instance.extensionId, str)


@given(instance=sourcecleaner::Schema_strategy)
def test_sourcecleaner::schema_extensionId_setter(instance):
    original = instance.extensionId
    instance.extensionId = original
    assert instance.extensionId == original

@given(instance=sourcecleaner::ExtensionPoint_strategy)
@settings(max_examples=50)
def test_sourcecleaner::extensionpoint_instantiation(instance):
    assert isinstance(instance, sourcecleaner::ExtensionPoint)

@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_diagraph_type(instance):
    assert isinstance(instance.diagraph, bool)


@given(instance=sourcecleaner::ExtensionPoint_strategy)
def test_sourcecleaner::extensionpoint_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original

@given(instance=sourcecleaner::Extension_strategy)
@settings(max_examples=50)
def test_sourcecleaner::extension_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Extension)

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_extra_type(instance):
    assert isinstance(instance.extra, str)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_diagraph_type(instance):
    assert isinstance(instance.diagraph, bool)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_pointId_type(instance):
    assert isinstance(instance.pointId, str)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_pointId_setter(instance):
    original = instance.pointId
    instance.pointId = original
    assert instance.pointId == original

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_clazz_type(instance):
    assert isinstance(instance.clazz, str)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=sourcecleaner::Extension_strategy)
def test_sourcecleaner::extension_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sourcecleaner::Export_strategy)
@settings(max_examples=50)
def test_sourcecleaner::export_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Export)

@given(instance=sourcecleaner::Export_strategy)
def test_sourcecleaner::export_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::Export_strategy)
def test_sourcecleaner::export_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner::ClassPath_strategy)
@settings(max_examples=50)
def test_sourcecleaner::classpath_instantiation(instance):
    assert isinstance(instance, sourcecleaner::ClassPath)

@given(instance=sourcecleaner::ClassPath_strategy)
def test_sourcecleaner::classpath_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sourcecleaner::ClassPath_strategy)
def test_sourcecleaner::classpath_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=sourcecleaner::Source_strategy)
@settings(max_examples=50)
def test_sourcecleaner::source_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Source)

@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_mark_type(instance):
    assert isinstance(instance.mark, bool)


@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_mark_setter(instance):
    original = instance.mark
    instance.mark = original
    assert instance.mark == original

@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_handled_type(instance):
    assert isinstance(instance.handled, bool)


@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_handled_setter(instance):
    original = instance.handled
    instance.handled = original
    assert instance.handled == original

@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=sourcecleaner::Source_strategy)
def test_sourcecleaner::source_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=sourcecleaner::Project_strategy)
@settings(max_examples=50)
def test_sourcecleaner::project_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Project)

@given(instance=sourcecleaner::Project_strategy)
def test_sourcecleaner::project_workspace_type(instance):
    assert isinstance(instance.workspace, str)


@given(instance=sourcecleaner::Project_strategy)
def test_sourcecleaner::project_workspace_setter(instance):
    original = instance.workspace
    instance.workspace = original
    assert instance.workspace == original

@given(instance=sourcecleaner::Project_strategy)
def test_sourcecleaner::project_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=sourcecleaner::Project_strategy)
def test_sourcecleaner::project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=sourcecleaner::Configuration_strategy)
@settings(max_examples=50)
def test_sourcecleaner::configuration_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Configuration)

@given(instance=sourcecleaner::Configuration_strategy)
def test_sourcecleaner::configuration_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=sourcecleaner::Configuration_strategy)
def test_sourcecleaner::configuration_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=sourcecleaner::Configuration_strategy)
def test_sourcecleaner::configuration_temp_type(instance):
    assert isinstance(instance.temp, str)


@given(instance=sourcecleaner::Configuration_strategy)
def test_sourcecleaner::configuration_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original

@given(instance=sourcecleaner::Plugin_strategy)
@settings(max_examples=50)
def test_sourcecleaner::plugin_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Plugin)

@given(instance=sourcecleaner::Plugin_strategy)
def test_sourcecleaner::plugin_extra_type(instance):
    assert isinstance(instance.extra, str)


@given(instance=sourcecleaner::Plugin_strategy)
def test_sourcecleaner::plugin_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original

@given(instance=sourcecleaner::Build_strategy)
@settings(max_examples=50)
def test_sourcecleaner::build_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Build)

@given(instance=sourcecleaner::Manifest_strategy)
@settings(max_examples=50)
def test_sourcecleaner::manifest_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Manifest)

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_vendor_type(instance):
    assert isinstance(instance.vendor, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_symbolicName_type(instance):
    assert isinstance(instance.symbolicName, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_versionQualifier_type(instance):
    assert isinstance(instance.versionQualifier, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_versionQualifier_setter(instance):
    original = instance.versionQualifier
    instance.versionQualifier = original
    assert instance.versionQualifier == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_singleton_type(instance):
    assert isinstance(instance.singleton, bool)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_singleton_setter(instance):
    original = instance.singleton
    instance.singleton = original
    assert instance.singleton == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_diagraph_type(instance):
    assert isinstance(instance.diagraph, bool)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_versionId_type(instance):
    assert isinstance(instance.versionId, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_versionId_setter(instance):
    original = instance.versionId
    instance.versionId = original
    assert instance.versionId == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_lazy_type(instance):
    assert isinstance(instance.lazy, bool)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original

@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_executionEnvironment_type(instance):
    assert isinstance(instance.executionEnvironment, str)


@given(instance=sourcecleaner::Manifest_strategy)
def test_sourcecleaner::manifest_executionEnvironment_setter(instance):
    original = instance.executionEnvironment
    instance.executionEnvironment = original
    assert instance.executionEnvironment == original

@given(instance=sourcecleaner::Java_strategy)
@settings(max_examples=50)
def test_sourcecleaner::java_instantiation(instance):
    assert isinstance(instance, sourcecleaner::Java)

@given(instance=sourcecleaner::Java_strategy)
def test_sourcecleaner::java_package_type(instance):
    assert isinstance(instance.package, str)


@given(instance=sourcecleaner::Java_strategy)
def test_sourcecleaner::java_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original
