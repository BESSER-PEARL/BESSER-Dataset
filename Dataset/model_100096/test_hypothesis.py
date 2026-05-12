import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sourcecleaner_ExtensionReference,
    sourcecleaner_ExtensionAttribute,
    sourcecleaner_Dependency,
    Source,
    sourcecleaner_LocatedElement,
    sourcecleaner_Schema,
    sourcecleaner_ExtensionPoint,
    sourcecleaner_Extension,
    sourcecleaner_Export,
    sourcecleaner_ClassPath,
    LocatedElement,
    sourcecleaner_Source,
    sourcecleaner_Project,
    sourcecleaner_Configuration,
    sourcecleaner_Plugin,
    sourcecleaner_Build,
    sourcecleaner_Manifest,
    sourcecleaner_Java,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sourcecleaner_extensionreference_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_ExtensionReference)


def test_sourcecleaner_extensionreference_constructor_exists():
    assert callable(sourcecleaner_ExtensionReference.__init__)


def test_sourcecleaner_extensionreference_constructor_args():
    sig = inspect.signature(sourcecleaner_ExtensionReference.__init__)
    params = list(sig.parameters.keys())
    assert "java" in params, "Missing parameter 'java'"
    assert "project" in params, "Missing parameter 'project'"
    assert "package" in params, "Missing parameter 'package'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner_extensionreference_has_java():
    assert hasattr(sourcecleaner_ExtensionReference, "java")
    descriptor = None
    for klass in sourcecleaner_ExtensionReference.__mro__:
        if "java" in klass.__dict__:
            descriptor = klass.__dict__["java"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionreference_has_project():
    assert hasattr(sourcecleaner_ExtensionReference, "project")
    descriptor = None
    for klass in sourcecleaner_ExtensionReference.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionreference_has_package():
    assert hasattr(sourcecleaner_ExtensionReference, "package")
    descriptor = None
    for klass in sourcecleaner_ExtensionReference.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionreference_has_name():
    assert hasattr(sourcecleaner_ExtensionReference, "name")
    descriptor = None
    for klass in sourcecleaner_ExtensionReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_extensionattribute_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_ExtensionAttribute)


def test_sourcecleaner_extensionattribute_constructor_exists():
    assert callable(sourcecleaner_ExtensionAttribute.__init__)


def test_sourcecleaner_extensionattribute_constructor_args():
    sig = inspect.signature(sourcecleaner_ExtensionAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_sourcecleaner_extensionattribute_has_name():
    assert hasattr(sourcecleaner_ExtensionAttribute, "name")
    descriptor = None
    for klass in sourcecleaner_ExtensionAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionattribute_has_value():
    assert hasattr(sourcecleaner_ExtensionAttribute, "value")
    descriptor = None
    for klass in sourcecleaner_ExtensionAttribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_dependency_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Dependency)


def test_sourcecleaner_dependency_constructor_exists():
    assert callable(sourcecleaner_Dependency.__init__)


def test_sourcecleaner_dependency_constructor_args():
    sig = inspect.signature(sourcecleaner_Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "reexport" in params, "Missing parameter 'reexport'"
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "name" in params, "Missing parameter 'name'"
    assert "version" in params, "Missing parameter 'version'"

def test_sourcecleaner_dependency_has_reexport():
    assert hasattr(sourcecleaner_Dependency, "reexport")
    descriptor = None
    for klass in sourcecleaner_Dependency.__mro__:
        if "reexport" in klass.__dict__:
            descriptor = klass.__dict__["reexport"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_dependency_has_diagraph():
    assert hasattr(sourcecleaner_Dependency, "diagraph")
    descriptor = None
    for klass in sourcecleaner_Dependency.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_dependency_has_name():
    assert hasattr(sourcecleaner_Dependency, "name")
    descriptor = None
    for klass in sourcecleaner_Dependency.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_dependency_has_version():
    assert hasattr(sourcecleaner_Dependency, "version")
    descriptor = None
    for klass in sourcecleaner_Dependency.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_source_is_not_abstract():
    assert not inspect.isabstract(Source)


def test_source_constructor_exists():
    assert callable(Source.__init__)


def test_source_constructor_args():
    sig = inspect.signature(Source.__init__)
    params = list(sig.parameters.keys())



def test_sourcecleaner_locatedelement_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_LocatedElement)


def test_sourcecleaner_locatedelement_constructor_exists():
    assert callable(sourcecleaner_LocatedElement.__init__)


def test_sourcecleaner_locatedelement_constructor_args():
    sig = inspect.signature(sourcecleaner_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "absolutePath" in params, "Missing parameter 'absolutePath'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner_locatedelement_has_absolutePath():
    assert hasattr(sourcecleaner_LocatedElement, "absolutePath")
    descriptor = None
    for klass in sourcecleaner_LocatedElement.__mro__:
        if "absolutePath" in klass.__dict__:
            descriptor = klass.__dict__["absolutePath"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_locatedelement_has_name():
    assert hasattr(sourcecleaner_LocatedElement, "name")
    descriptor = None
    for klass in sourcecleaner_LocatedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_schema_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Schema)


def test_sourcecleaner_schema_constructor_exists():
    assert callable(sourcecleaner_Schema.__init__)


def test_sourcecleaner_schema_constructor_args():
    sig = inspect.signature(sourcecleaner_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "pluginName" in params, "Missing parameter 'pluginName'"
    assert "extensionId" in params, "Missing parameter 'extensionId'"
    assert "extensionName" in params, "Missing parameter 'extensionName'"

def test_sourcecleaner_schema_has_pluginName():
    assert hasattr(sourcecleaner_Schema, "pluginName")
    descriptor = None
    for klass in sourcecleaner_Schema.__mro__:
        if "pluginName" in klass.__dict__:
            descriptor = klass.__dict__["pluginName"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_schema_has_extensionId():
    assert hasattr(sourcecleaner_Schema, "extensionId")
    descriptor = None
    for klass in sourcecleaner_Schema.__mro__:
        if "extensionId" in klass.__dict__:
            descriptor = klass.__dict__["extensionId"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_schema_has_extensionName():
    assert hasattr(sourcecleaner_Schema, "extensionName")
    descriptor = None
    for klass in sourcecleaner_Schema.__mro__:
        if "extensionName" in klass.__dict__:
            descriptor = klass.__dict__["extensionName"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_ExtensionPoint)


def test_sourcecleaner_extensionpoint_constructor_exists():
    assert callable(sourcecleaner_ExtensionPoint.__init__)


def test_sourcecleaner_extensionpoint_constructor_args():
    sig = inspect.signature(sourcecleaner_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "id" in params, "Missing parameter 'id'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner_extensionpoint_has_diagraph():
    assert hasattr(sourcecleaner_ExtensionPoint, "diagraph")
    descriptor = None
    for klass in sourcecleaner_ExtensionPoint.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionpoint_has_id():
    assert hasattr(sourcecleaner_ExtensionPoint, "id")
    descriptor = None
    for klass in sourcecleaner_ExtensionPoint.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionpoint_has_schema():
    assert hasattr(sourcecleaner_ExtensionPoint, "schema")
    descriptor = None
    for klass in sourcecleaner_ExtensionPoint.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extensionpoint_has_name():
    assert hasattr(sourcecleaner_ExtensionPoint, "name")
    descriptor = None
    for klass in sourcecleaner_ExtensionPoint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_extension_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Extension)


def test_sourcecleaner_extension_constructor_exists():
    assert callable(sourcecleaner_Extension.__init__)


def test_sourcecleaner_extension_constructor_args():
    sig = inspect.signature(sourcecleaner_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "name" in params, "Missing parameter 'name'"
    assert "extra" in params, "Missing parameter 'extra'"
    assert "pointId" in params, "Missing parameter 'pointId'"
    assert "id" in params, "Missing parameter 'id'"
    assert "clazz" in params, "Missing parameter 'clazz'"

def test_sourcecleaner_extension_has_diagraph():
    assert hasattr(sourcecleaner_Extension, "diagraph")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extension_has_name():
    assert hasattr(sourcecleaner_Extension, "name")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extension_has_extra():
    assert hasattr(sourcecleaner_Extension, "extra")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extension_has_pointId():
    assert hasattr(sourcecleaner_Extension, "pointId")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "pointId" in klass.__dict__:
            descriptor = klass.__dict__["pointId"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extension_has_id():
    assert hasattr(sourcecleaner_Extension, "id")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_extension_has_clazz():
    assert hasattr(sourcecleaner_Extension, "clazz")
    descriptor = None
    for klass in sourcecleaner_Extension.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_export_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Export)


def test_sourcecleaner_export_constructor_exists():
    assert callable(sourcecleaner_Export.__init__)


def test_sourcecleaner_export_constructor_args():
    sig = inspect.signature(sourcecleaner_Export.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner_export_has_name():
    assert hasattr(sourcecleaner_Export, "name")
    descriptor = None
    for klass in sourcecleaner_Export.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_classpath_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_ClassPath)


def test_sourcecleaner_classpath_constructor_exists():
    assert callable(sourcecleaner_ClassPath.__init__)


def test_sourcecleaner_classpath_constructor_args():
    sig = inspect.signature(sourcecleaner_ClassPath.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sourcecleaner_classpath_has_name():
    assert hasattr(sourcecleaner_ClassPath, "name")
    descriptor = None
    for klass in sourcecleaner_ClassPath.__mro__:
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



def test_sourcecleaner_source_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Source)


def test_sourcecleaner_source_constructor_exists():
    assert callable(sourcecleaner_Source.__init__)


def test_sourcecleaner_source_constructor_args():
    sig = inspect.signature(sourcecleaner_Source.__init__)
    params = list(sig.parameters.keys())
    assert "mark" in params, "Missing parameter 'mark'"
    assert "handled" in params, "Missing parameter 'handled'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "content" in params, "Missing parameter 'content'"

def test_sourcecleaner_source_has_mark():
    assert hasattr(sourcecleaner_Source, "mark")
    descriptor = None
    for klass in sourcecleaner_Source.__mro__:
        if "mark" in klass.__dict__:
            descriptor = klass.__dict__["mark"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_source_has_handled():
    assert hasattr(sourcecleaner_Source, "handled")
    descriptor = None
    for klass in sourcecleaner_Source.__mro__:
        if "handled" in klass.__dict__:
            descriptor = klass.__dict__["handled"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_source_has_comment():
    assert hasattr(sourcecleaner_Source, "comment")
    descriptor = None
    for klass in sourcecleaner_Source.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_source_has_content():
    assert hasattr(sourcecleaner_Source, "content")
    descriptor = None
    for klass in sourcecleaner_Source.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_project_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Project)


def test_sourcecleaner_project_constructor_exists():
    assert callable(sourcecleaner_Project.__init__)


def test_sourcecleaner_project_constructor_args():
    sig = inspect.signature(sourcecleaner_Project.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "workspace" in params, "Missing parameter 'workspace'"

def test_sourcecleaner_project_has_id():
    assert hasattr(sourcecleaner_Project, "id")
    descriptor = None
    for klass in sourcecleaner_Project.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_project_has_workspace():
    assert hasattr(sourcecleaner_Project, "workspace")
    descriptor = None
    for klass in sourcecleaner_Project.__mro__:
        if "workspace" in klass.__dict__:
            descriptor = klass.__dict__["workspace"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_configuration_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Configuration)


def test_sourcecleaner_configuration_constructor_exists():
    assert callable(sourcecleaner_Configuration.__init__)


def test_sourcecleaner_configuration_constructor_args():
    sig = inspect.signature(sourcecleaner_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "temp" in params, "Missing parameter 'temp'"
    assert "location" in params, "Missing parameter 'location'"

def test_sourcecleaner_configuration_has_temp():
    assert hasattr(sourcecleaner_Configuration, "temp")
    descriptor = None
    for klass in sourcecleaner_Configuration.__mro__:
        if "temp" in klass.__dict__:
            descriptor = klass.__dict__["temp"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_configuration_has_location():
    assert hasattr(sourcecleaner_Configuration, "location")
    descriptor = None
    for klass in sourcecleaner_Configuration.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_plugin_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Plugin)


def test_sourcecleaner_plugin_constructor_exists():
    assert callable(sourcecleaner_Plugin.__init__)


def test_sourcecleaner_plugin_constructor_args():
    sig = inspect.signature(sourcecleaner_Plugin.__init__)
    params = list(sig.parameters.keys())
    assert "extra" in params, "Missing parameter 'extra'"

def test_sourcecleaner_plugin_has_extra():
    assert hasattr(sourcecleaner_Plugin, "extra")
    descriptor = None
    for klass in sourcecleaner_Plugin.__mro__:
        if "extra" in klass.__dict__:
            descriptor = klass.__dict__["extra"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_build_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Build)


def test_sourcecleaner_build_constructor_exists():
    assert callable(sourcecleaner_Build.__init__)


def test_sourcecleaner_build_constructor_args():
    sig = inspect.signature(sourcecleaner_Build.__init__)
    params = list(sig.parameters.keys())



def test_sourcecleaner_manifest_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Manifest)


def test_sourcecleaner_manifest_constructor_exists():
    assert callable(sourcecleaner_Manifest.__init__)


def test_sourcecleaner_manifest_constructor_args():
    sig = inspect.signature(sourcecleaner_Manifest.__init__)
    params = list(sig.parameters.keys())
    assert "executionEnvironment" in params, "Missing parameter 'executionEnvironment'"
    assert "vendor" in params, "Missing parameter 'vendor'"
    assert "diagraph" in params, "Missing parameter 'diagraph'"
    assert "symbolicName" in params, "Missing parameter 'symbolicName'"
    assert "singleton" in params, "Missing parameter 'singleton'"
    assert "version" in params, "Missing parameter 'version'"
    assert "lazy" in params, "Missing parameter 'lazy'"
    assert "versionId" in params, "Missing parameter 'versionId'"
    assert "versionQualifier" in params, "Missing parameter 'versionQualifier'"

def test_sourcecleaner_manifest_has_executionEnvironment():
    assert hasattr(sourcecleaner_Manifest, "executionEnvironment")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "executionEnvironment" in klass.__dict__:
            descriptor = klass.__dict__["executionEnvironment"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_vendor():
    assert hasattr(sourcecleaner_Manifest, "vendor")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "vendor" in klass.__dict__:
            descriptor = klass.__dict__["vendor"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_diagraph():
    assert hasattr(sourcecleaner_Manifest, "diagraph")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "diagraph" in klass.__dict__:
            descriptor = klass.__dict__["diagraph"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_symbolicName():
    assert hasattr(sourcecleaner_Manifest, "symbolicName")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "symbolicName" in klass.__dict__:
            descriptor = klass.__dict__["symbolicName"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_singleton():
    assert hasattr(sourcecleaner_Manifest, "singleton")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "singleton" in klass.__dict__:
            descriptor = klass.__dict__["singleton"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_version():
    assert hasattr(sourcecleaner_Manifest, "version")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_lazy():
    assert hasattr(sourcecleaner_Manifest, "lazy")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "lazy" in klass.__dict__:
            descriptor = klass.__dict__["lazy"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_versionId():
    assert hasattr(sourcecleaner_Manifest, "versionId")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "versionId" in klass.__dict__:
            descriptor = klass.__dict__["versionId"]
            break
    assert isinstance(descriptor, property)

def test_sourcecleaner_manifest_has_versionQualifier():
    assert hasattr(sourcecleaner_Manifest, "versionQualifier")
    descriptor = None
    for klass in sourcecleaner_Manifest.__mro__:
        if "versionQualifier" in klass.__dict__:
            descriptor = klass.__dict__["versionQualifier"]
            break
    assert isinstance(descriptor, property)



def test_sourcecleaner_java_is_not_abstract():
    assert not inspect.isabstract(sourcecleaner_Java)


def test_sourcecleaner_java_constructor_exists():
    assert callable(sourcecleaner_Java.__init__)


def test_sourcecleaner_java_constructor_args():
    sig = inspect.signature(sourcecleaner_Java.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_sourcecleaner_java_has_package():
    assert hasattr(sourcecleaner_Java, "package")
    descriptor = None
    for klass in sourcecleaner_Java.__mro__:
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
sourcecleaner_ExtensionReference_strategy = st.builds(
    sourcecleaner_ExtensionReference,
    java=
        safe_text,
    project=
        safe_text,
    package=
        safe_text,
    name=
        safe_text
)
sourcecleaner_ExtensionAttribute_strategy = st.builds(
    sourcecleaner_ExtensionAttribute,
    name=
        safe_text,
    value=
        safe_text
)
sourcecleaner_Dependency_strategy = st.builds(
    sourcecleaner_Dependency,
    reexport=
        st.booleans(),
    diagraph=
        st.booleans(),
    name=
        safe_text,
    version=
        safe_text
)
Source_strategy = st.builds(
    Source,
)
sourcecleaner_LocatedElement_strategy = st.builds(
    sourcecleaner_LocatedElement,
    absolutePath=
        safe_text,
    name=
        safe_text
)
sourcecleaner_Schema_strategy = st.builds(
    sourcecleaner_Schema,
    pluginName=
        safe_text,
    extensionId=
        safe_text,
    extensionName=
        safe_text
)
sourcecleaner_ExtensionPoint_strategy = st.builds(
    sourcecleaner_ExtensionPoint,
    diagraph=
        st.booleans(),
    id=
        safe_text,
    schema=
        safe_text,
    name=
        safe_text
)
sourcecleaner_Extension_strategy = st.builds(
    sourcecleaner_Extension,
    diagraph=
        st.booleans(),
    name=
        safe_text,
    extra=
        safe_text,
    pointId=
        safe_text,
    id=
        safe_text,
    clazz=
        safe_text
)
sourcecleaner_Export_strategy = st.builds(
    sourcecleaner_Export,
    name=
        safe_text
)
sourcecleaner_ClassPath_strategy = st.builds(
    sourcecleaner_ClassPath,
    name=
        safe_text
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
sourcecleaner_Source_strategy = st.builds(
    sourcecleaner_Source,
    mark=
        st.booleans(),
    handled=
        st.booleans(),
    comment=
        safe_text,
    content=
        safe_text
)
sourcecleaner_Project_strategy = st.builds(
    sourcecleaner_Project,
    id=
        st.integers(),
    workspace=
        safe_text
)
sourcecleaner_Configuration_strategy = st.builds(
    sourcecleaner_Configuration,
    temp=
        safe_text,
    location=
        safe_text
)
sourcecleaner_Plugin_strategy = st.builds(
    sourcecleaner_Plugin,
    extra=
        safe_text
)
sourcecleaner_Build_strategy = st.builds(
    sourcecleaner_Build,
)
sourcecleaner_Manifest_strategy = st.builds(
    sourcecleaner_Manifest,
    executionEnvironment=
        safe_text,
    vendor=
        safe_text,
    diagraph=
        st.booleans(),
    symbolicName=
        safe_text,
    singleton=
        st.booleans(),
    version=
        safe_text,
    lazy=
        st.booleans(),
    versionId=
        safe_text,
    versionQualifier=
        safe_text
)
sourcecleaner_Java_strategy = st.builds(
    sourcecleaner_Java,
    package=
        safe_text
)

@given(instance=sourcecleaner_ExtensionReference_strategy)
@settings(max_examples=50)
def test_sourcecleaner_extensionreference_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionReference)



@given(instance=sourcecleaner_ExtensionReference_strategy)
def test_sourcecleaner_extensionreference_java_setter(instance):
    original = instance.java
    instance.java = original
    assert instance.java == original



@given(instance=sourcecleaner_ExtensionReference_strategy)
def test_sourcecleaner_extensionreference_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original



@given(instance=sourcecleaner_ExtensionReference_strategy)
def test_sourcecleaner_extensionreference_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original



@given(instance=sourcecleaner_ExtensionReference_strategy)
def test_sourcecleaner_extensionreference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner_ExtensionAttribute_strategy)
@settings(max_examples=50)
def test_sourcecleaner_extensionattribute_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionAttribute)



@given(instance=sourcecleaner_ExtensionAttribute_strategy)
def test_sourcecleaner_extensionattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sourcecleaner_ExtensionAttribute_strategy)
def test_sourcecleaner_extensionattribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=sourcecleaner_Dependency_strategy)
@settings(max_examples=50)
def test_sourcecleaner_dependency_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Dependency)



@given(instance=sourcecleaner_Dependency_strategy)
def test_sourcecleaner_dependency_reexport_setter(instance):
    original = instance.reexport
    instance.reexport = original
    assert instance.reexport == original



@given(instance=sourcecleaner_Dependency_strategy)
def test_sourcecleaner_dependency_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original



@given(instance=sourcecleaner_Dependency_strategy)
def test_sourcecleaner_dependency_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sourcecleaner_Dependency_strategy)
def test_sourcecleaner_dependency_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Source_strategy)
@settings(max_examples=50)
def test_source_instantiation(instance):
    assert isinstance(instance, Source)

@given(instance=sourcecleaner_LocatedElement_strategy)
@settings(max_examples=50)
def test_sourcecleaner_locatedelement_instantiation(instance):
    assert isinstance(instance, sourcecleaner_LocatedElement)



@given(instance=sourcecleaner_LocatedElement_strategy)
def test_sourcecleaner_locatedelement_absolutePath_setter(instance):
    original = instance.absolutePath
    instance.absolutePath = original
    assert instance.absolutePath == original



@given(instance=sourcecleaner_LocatedElement_strategy)
def test_sourcecleaner_locatedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner_Schema_strategy)
@settings(max_examples=50)
def test_sourcecleaner_schema_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Schema)



@given(instance=sourcecleaner_Schema_strategy)
def test_sourcecleaner_schema_pluginName_setter(instance):
    original = instance.pluginName
    instance.pluginName = original
    assert instance.pluginName == original



@given(instance=sourcecleaner_Schema_strategy)
def test_sourcecleaner_schema_extensionId_setter(instance):
    original = instance.extensionId
    instance.extensionId = original
    assert instance.extensionId == original



@given(instance=sourcecleaner_Schema_strategy)
def test_sourcecleaner_schema_extensionName_setter(instance):
    original = instance.extensionName
    instance.extensionName = original
    assert instance.extensionName == original

@given(instance=sourcecleaner_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_sourcecleaner_extensionpoint_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ExtensionPoint)



@given(instance=sourcecleaner_ExtensionPoint_strategy)
def test_sourcecleaner_extensionpoint_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original



@given(instance=sourcecleaner_ExtensionPoint_strategy)
def test_sourcecleaner_extensionpoint_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sourcecleaner_ExtensionPoint_strategy)
def test_sourcecleaner_extensionpoint_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=sourcecleaner_ExtensionPoint_strategy)
def test_sourcecleaner_extensionpoint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner_Extension_strategy)
@settings(max_examples=50)
def test_sourcecleaner_extension_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Extension)



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_pointId_setter(instance):
    original = instance.pointId
    instance.pointId = original
    assert instance.pointId == original



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sourcecleaner_Extension_strategy)
def test_sourcecleaner_extension_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=sourcecleaner_Export_strategy)
@settings(max_examples=50)
def test_sourcecleaner_export_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Export)



@given(instance=sourcecleaner_Export_strategy)
def test_sourcecleaner_export_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sourcecleaner_ClassPath_strategy)
@settings(max_examples=50)
def test_sourcecleaner_classpath_instantiation(instance):
    assert isinstance(instance, sourcecleaner_ClassPath)



@given(instance=sourcecleaner_ClassPath_strategy)
def test_sourcecleaner_classpath_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=sourcecleaner_Source_strategy)
@settings(max_examples=50)
def test_sourcecleaner_source_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Source)



@given(instance=sourcecleaner_Source_strategy)
def test_sourcecleaner_source_mark_setter(instance):
    original = instance.mark
    instance.mark = original
    assert instance.mark == original



@given(instance=sourcecleaner_Source_strategy)
def test_sourcecleaner_source_handled_setter(instance):
    original = instance.handled
    instance.handled = original
    assert instance.handled == original



@given(instance=sourcecleaner_Source_strategy)
def test_sourcecleaner_source_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=sourcecleaner_Source_strategy)
def test_sourcecleaner_source_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=sourcecleaner_Project_strategy)
@settings(max_examples=50)
def test_sourcecleaner_project_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Project)



@given(instance=sourcecleaner_Project_strategy)
def test_sourcecleaner_project_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=sourcecleaner_Project_strategy)
def test_sourcecleaner_project_workspace_setter(instance):
    original = instance.workspace
    instance.workspace = original
    assert instance.workspace == original

@given(instance=sourcecleaner_Configuration_strategy)
@settings(max_examples=50)
def test_sourcecleaner_configuration_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Configuration)



@given(instance=sourcecleaner_Configuration_strategy)
def test_sourcecleaner_configuration_temp_setter(instance):
    original = instance.temp
    instance.temp = original
    assert instance.temp == original



@given(instance=sourcecleaner_Configuration_strategy)
def test_sourcecleaner_configuration_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=sourcecleaner_Plugin_strategy)
@settings(max_examples=50)
def test_sourcecleaner_plugin_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Plugin)



@given(instance=sourcecleaner_Plugin_strategy)
def test_sourcecleaner_plugin_extra_setter(instance):
    original = instance.extra
    instance.extra = original
    assert instance.extra == original

@given(instance=sourcecleaner_Build_strategy)
@settings(max_examples=50)
def test_sourcecleaner_build_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Build)

@given(instance=sourcecleaner_Manifest_strategy)
@settings(max_examples=50)
def test_sourcecleaner_manifest_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Manifest)



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_executionEnvironment_setter(instance):
    original = instance.executionEnvironment
    instance.executionEnvironment = original
    assert instance.executionEnvironment == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_vendor_setter(instance):
    original = instance.vendor
    instance.vendor = original
    assert instance.vendor == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_diagraph_setter(instance):
    original = instance.diagraph
    instance.diagraph = original
    assert instance.diagraph == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_symbolicName_setter(instance):
    original = instance.symbolicName
    instance.symbolicName = original
    assert instance.symbolicName == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_singleton_setter(instance):
    original = instance.singleton
    instance.singleton = original
    assert instance.singleton == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_lazy_setter(instance):
    original = instance.lazy
    instance.lazy = original
    assert instance.lazy == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_versionId_setter(instance):
    original = instance.versionId
    instance.versionId = original
    assert instance.versionId == original



@given(instance=sourcecleaner_Manifest_strategy)
def test_sourcecleaner_manifest_versionQualifier_setter(instance):
    original = instance.versionQualifier
    instance.versionQualifier = original
    assert instance.versionQualifier == original

@given(instance=sourcecleaner_Java_strategy)
@settings(max_examples=50)
def test_sourcecleaner_java_instantiation(instance):
    assert isinstance(instance, sourcecleaner_Java)



@given(instance=sourcecleaner_Java_strategy)
def test_sourcecleaner_java_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original
