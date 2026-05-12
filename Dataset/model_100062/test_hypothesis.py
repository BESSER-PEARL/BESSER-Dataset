import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    build::InstallationUnit,
    build::Repository,
    InstallationUnit,
    build::Bundle,
    build::Feature,
    build::Build,
    build::Contact,
    build::Promotion,
    build::Compiler,
    build::Product,
    build::Contribution,
    build::Category,
    build::Map,
    build::Config,
    build::Platform,
    WS,
    ArchiveFormat,
    OS,
    ARCH,
    BuildType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_build::installationunit_is_not_abstract():
    assert not inspect.isabstract(build::InstallationUnit)


def test_build::installationunit_constructor_exists():
    assert callable(build::InstallationUnit.__init__)


def test_build::installationunit_constructor_args():
    sig = inspect.signature(build::InstallationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_build::installationunit_has_id():
    assert hasattr(build::InstallationUnit, "id")
    descriptor = None
    for klass in build::InstallationUnit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_build::installationunit_has_version():
    assert hasattr(build::InstallationUnit, "version")
    descriptor = None
    for klass in build::InstallationUnit.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_build::repository_is_not_abstract():
    assert not inspect.isabstract(build::Repository)


def test_build::repository_constructor_exists():
    assert callable(build::Repository.__init__)


def test_build::repository_constructor_args():
    sig = inspect.signature(build::Repository.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "label" in params, "Missing parameter 'label'"

def test_build::repository_has_location():
    assert hasattr(build::Repository, "location")
    descriptor = None
    for klass in build::Repository.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_build::repository_has_label():
    assert hasattr(build::Repository, "label")
    descriptor = None
    for klass in build::Repository.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_installationunit_is_not_abstract():
    assert not inspect.isabstract(InstallationUnit)


def test_installationunit_constructor_exists():
    assert callable(InstallationUnit.__init__)


def test_installationunit_constructor_args():
    sig = inspect.signature(InstallationUnit.__init__)
    params = list(sig.parameters.keys())



def test_build::bundle_is_not_abstract():
    assert not inspect.isabstract(build::Bundle)


def test_build::bundle_constructor_exists():
    assert callable(build::Bundle.__init__)


def test_build::bundle_constructor_args():
    sig = inspect.signature(build::Bundle.__init__)
    params = list(sig.parameters.keys())



def test_build::feature_is_not_abstract():
    assert not inspect.isabstract(build::Feature)


def test_build::feature_constructor_exists():
    assert callable(build::Feature.__init__)


def test_build::feature_constructor_args():
    sig = inspect.signature(build::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "inProduct" in params, "Missing parameter 'inProduct'"

def test_build::feature_has_inProduct():
    assert hasattr(build::Feature, "inProduct")
    descriptor = None
    for klass in build::Feature.__mro__:
        if "inProduct" in klass.__dict__:
            descriptor = klass.__dict__["inProduct"]
            break
    assert isinstance(descriptor, property)



def test_build::build_is_not_abstract():
    assert not inspect.isabstract(build::Build)


def test_build::build_constructor_exists():
    assert callable(build::Build.__init__)


def test_build::build_constructor_args():
    sig = inspect.signature(build::Build.__init__)
    params = list(sig.parameters.keys())
    assert "buildRoot" in params, "Missing parameter 'buildRoot'"
    assert "date" in params, "Missing parameter 'date'"
    assert "time" in params, "Missing parameter 'time'"
    assert "sendmail" in params, "Missing parameter 'sendmail'"
    assert "launchVM" in params, "Missing parameter 'launchVM'"
    assert "type" in params, "Missing parameter 'type'"
    assert "builderURL" in params, "Missing parameter 'builderURL'"
    assert "fetchTag" in params, "Missing parameter 'fetchTag'"
    assert "label" in params, "Missing parameter 'label'"

def test_build::build_has_buildRoot():
    assert hasattr(build::Build, "buildRoot")
    descriptor = None
    for klass in build::Build.__mro__:
        if "buildRoot" in klass.__dict__:
            descriptor = klass.__dict__["buildRoot"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_date():
    assert hasattr(build::Build, "date")
    descriptor = None
    for klass in build::Build.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_time():
    assert hasattr(build::Build, "time")
    descriptor = None
    for klass in build::Build.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_sendmail():
    assert hasattr(build::Build, "sendmail")
    descriptor = None
    for klass in build::Build.__mro__:
        if "sendmail" in klass.__dict__:
            descriptor = klass.__dict__["sendmail"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_launchVM():
    assert hasattr(build::Build, "launchVM")
    descriptor = None
    for klass in build::Build.__mro__:
        if "launchVM" in klass.__dict__:
            descriptor = klass.__dict__["launchVM"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_type():
    assert hasattr(build::Build, "type")
    descriptor = None
    for klass in build::Build.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_builderURL():
    assert hasattr(build::Build, "builderURL")
    descriptor = None
    for klass in build::Build.__mro__:
        if "builderURL" in klass.__dict__:
            descriptor = klass.__dict__["builderURL"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_fetchTag():
    assert hasattr(build::Build, "fetchTag")
    descriptor = None
    for klass in build::Build.__mro__:
        if "fetchTag" in klass.__dict__:
            descriptor = klass.__dict__["fetchTag"]
            break
    assert isinstance(descriptor, property)

def test_build::build_has_label():
    assert hasattr(build::Build, "label")
    descriptor = None
    for klass in build::Build.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_build::contact_is_not_abstract():
    assert not inspect.isabstract(build::Contact)


def test_build::contact_constructor_exists():
    assert callable(build::Contact.__init__)


def test_build::contact_constructor_args():
    sig = inspect.signature(build::Contact.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_build::contact_has_email():
    assert hasattr(build::Contact, "email")
    descriptor = None
    for klass in build::Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_build::contact_has_name():
    assert hasattr(build::Contact, "name")
    descriptor = None
    for klass in build::Contact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_build::promotion_is_not_abstract():
    assert not inspect.isabstract(build::Promotion)


def test_build::promotion_constructor_exists():
    assert callable(build::Promotion.__init__)


def test_build::promotion_constructor_args():
    sig = inspect.signature(build::Promotion.__init__)
    params = list(sig.parameters.keys())
    assert "baseURL" in params, "Missing parameter 'baseURL'"
    assert "uploadDirectory" in params, "Missing parameter 'uploadDirectory'"
    assert "incubating" in params, "Missing parameter 'incubating'"
    assert "buildAlias" in params, "Missing parameter 'buildAlias'"
    assert "downloadDirectory" in params, "Missing parameter 'downloadDirectory'"

def test_build::promotion_has_baseURL():
    assert hasattr(build::Promotion, "baseURL")
    descriptor = None
    for klass in build::Promotion.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)

def test_build::promotion_has_uploadDirectory():
    assert hasattr(build::Promotion, "uploadDirectory")
    descriptor = None
    for klass in build::Promotion.__mro__:
        if "uploadDirectory" in klass.__dict__:
            descriptor = klass.__dict__["uploadDirectory"]
            break
    assert isinstance(descriptor, property)

def test_build::promotion_has_incubating():
    assert hasattr(build::Promotion, "incubating")
    descriptor = None
    for klass in build::Promotion.__mro__:
        if "incubating" in klass.__dict__:
            descriptor = klass.__dict__["incubating"]
            break
    assert isinstance(descriptor, property)

def test_build::promotion_has_buildAlias():
    assert hasattr(build::Promotion, "buildAlias")
    descriptor = None
    for klass in build::Promotion.__mro__:
        if "buildAlias" in klass.__dict__:
            descriptor = klass.__dict__["buildAlias"]
            break
    assert isinstance(descriptor, property)

def test_build::promotion_has_downloadDirectory():
    assert hasattr(build::Promotion, "downloadDirectory")
    descriptor = None
    for klass in build::Promotion.__mro__:
        if "downloadDirectory" in klass.__dict__:
            descriptor = klass.__dict__["downloadDirectory"]
            break
    assert isinstance(descriptor, property)



def test_build::compiler_is_not_abstract():
    assert not inspect.isabstract(build::Compiler)


def test_build::compiler_constructor_exists():
    assert callable(build::Compiler.__init__)


def test_build::compiler_constructor_args():
    sig = inspect.signature(build::Compiler.__init__)
    params = list(sig.parameters.keys())
    assert "args" in params, "Missing parameter 'args'"
    assert "targetVersion" in params, "Missing parameter 'targetVersion'"
    assert "sourceVersion" in params, "Missing parameter 'sourceVersion'"
    assert "verbose" in params, "Missing parameter 'verbose'"
    assert "debugInfo" in params, "Missing parameter 'debugInfo'"
    assert "failOnError" in params, "Missing parameter 'failOnError'"

def test_build::compiler_has_args():
    assert hasattr(build::Compiler, "args")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_build::compiler_has_targetVersion():
    assert hasattr(build::Compiler, "targetVersion")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "targetVersion" in klass.__dict__:
            descriptor = klass.__dict__["targetVersion"]
            break
    assert isinstance(descriptor, property)

def test_build::compiler_has_sourceVersion():
    assert hasattr(build::Compiler, "sourceVersion")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "sourceVersion" in klass.__dict__:
            descriptor = klass.__dict__["sourceVersion"]
            break
    assert isinstance(descriptor, property)

def test_build::compiler_has_verbose():
    assert hasattr(build::Compiler, "verbose")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)

def test_build::compiler_has_debugInfo():
    assert hasattr(build::Compiler, "debugInfo")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "debugInfo" in klass.__dict__:
            descriptor = klass.__dict__["debugInfo"]
            break
    assert isinstance(descriptor, property)

def test_build::compiler_has_failOnError():
    assert hasattr(build::Compiler, "failOnError")
    descriptor = None
    for klass in build::Compiler.__mro__:
        if "failOnError" in klass.__dict__:
            descriptor = klass.__dict__["failOnError"]
            break
    assert isinstance(descriptor, property)



def test_build::product_is_not_abstract():
    assert not inspect.isabstract(build::Product)


def test_build::product_constructor_exists():
    assert callable(build::Product.__init__)


def test_build::product_constructor_args():
    sig = inspect.signature(build::Product.__init__)
    params = list(sig.parameters.keys())



def test_build::contribution_is_not_abstract():
    assert not inspect.isabstract(build::Contribution)


def test_build::contribution_constructor_exists():
    assert callable(build::Contribution.__init__)


def test_build::contribution_constructor_args():
    sig = inspect.signature(build::Contribution.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_build::contribution_has_label():
    assert hasattr(build::Contribution, "label")
    descriptor = None
    for klass in build::Contribution.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_build::category_is_not_abstract():
    assert not inspect.isabstract(build::Category)


def test_build::category_constructor_exists():
    assert callable(build::Category.__init__)


def test_build::category_constructor_args():
    sig = inspect.signature(build::Category.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"
    assert "name" in params, "Missing parameter 'name'"

def test_build::category_has_description():
    assert hasattr(build::Category, "description")
    descriptor = None
    for klass in build::Category.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_build::category_has_label():
    assert hasattr(build::Category, "label")
    descriptor = None
    for klass in build::Category.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_build::category_has_name():
    assert hasattr(build::Category, "name")
    descriptor = None
    for klass in build::Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_build::map_is_not_abstract():
    assert not inspect.isabstract(build::Map)


def test_build::map_constructor_exists():
    assert callable(build::Map.__init__)


def test_build::map_constructor_args():
    sig = inspect.signature(build::Map.__init__)
    params = list(sig.parameters.keys())
    assert "repo" in params, "Missing parameter 'repo'"
    assert "root" in params, "Missing parameter 'root'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_build::map_has_repo():
    assert hasattr(build::Map, "repo")
    descriptor = None
    for klass in build::Map.__mro__:
        if "repo" in klass.__dict__:
            descriptor = klass.__dict__["repo"]
            break
    assert isinstance(descriptor, property)

def test_build::map_has_root():
    assert hasattr(build::Map, "root")
    descriptor = None
    for klass in build::Map.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_build::map_has_tag():
    assert hasattr(build::Map, "tag")
    descriptor = None
    for klass in build::Map.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_build::config_is_not_abstract():
    assert not inspect.isabstract(build::Config)


def test_build::config_constructor_exists():
    assert callable(build::Config.__init__)


def test_build::config_constructor_args():
    sig = inspect.signature(build::Config.__init__)
    params = list(sig.parameters.keys())
    assert "os" in params, "Missing parameter 'os'"
    assert "arch" in params, "Missing parameter 'arch'"
    assert "ws" in params, "Missing parameter 'ws'"
    assert "archiveFormat" in params, "Missing parameter 'archiveFormat'"

def test_build::config_has_os():
    assert hasattr(build::Config, "os")
    descriptor = None
    for klass in build::Config.__mro__:
        if "os" in klass.__dict__:
            descriptor = klass.__dict__["os"]
            break
    assert isinstance(descriptor, property)

def test_build::config_has_arch():
    assert hasattr(build::Config, "arch")
    descriptor = None
    for klass in build::Config.__mro__:
        if "arch" in klass.__dict__:
            descriptor = klass.__dict__["arch"]
            break
    assert isinstance(descriptor, property)

def test_build::config_has_ws():
    assert hasattr(build::Config, "ws")
    descriptor = None
    for klass in build::Config.__mro__:
        if "ws" in klass.__dict__:
            descriptor = klass.__dict__["ws"]
            break
    assert isinstance(descriptor, property)

def test_build::config_has_archiveFormat():
    assert hasattr(build::Config, "archiveFormat")
    descriptor = None
    for klass in build::Config.__mro__:
        if "archiveFormat" in klass.__dict__:
            descriptor = klass.__dict__["archiveFormat"]
            break
    assert isinstance(descriptor, property)



def test_build::platform_is_not_abstract():
    assert not inspect.isabstract(build::Platform)


def test_build::platform_constructor_exists():
    assert callable(build::Platform.__init__)


def test_build::platform_constructor_args():
    sig = inspect.signature(build::Platform.__init__)
    params = list(sig.parameters.keys())
    assert "deltapack" in params, "Missing parameter 'deltapack'"
    assert "file" in params, "Missing parameter 'file'"
    assert "location" in params, "Missing parameter 'location'"

def test_build::platform_has_deltapack():
    assert hasattr(build::Platform, "deltapack")
    descriptor = None
    for klass in build::Platform.__mro__:
        if "deltapack" in klass.__dict__:
            descriptor = klass.__dict__["deltapack"]
            break
    assert isinstance(descriptor, property)

def test_build::platform_has_file():
    assert hasattr(build::Platform, "file")
    descriptor = None
    for klass in build::Platform.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_build::platform_has_location():
    assert hasattr(build::Platform, "location")
    descriptor = None
    for klass in build::Platform.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ws_exists():
    # Check that the Enumeration exists
    assert WS is not None

def test_ws_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WS]
    expected_literals = [
        "gtk",
        "carbon",
        "win32",
        "cocoa",
        "motif",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WS"

def test_archiveformat_exists():
    # Check that the Enumeration exists
    assert ArchiveFormat is not None

def test_archiveformat_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ArchiveFormat]
    expected_literals = [
        "tar",
        "zip",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ArchiveFormat"

def test_os_exists():
    # Check that the Enumeration exists
    assert OS is not None

def test_os_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OS]
    expected_literals = [
        "macosx",
        "hpux",
        "aix",
        "linux",
        "solaris",
        "win32",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OS"

def test_arch_exists():
    # Check that the Enumeration exists
    assert ARCH is not None

def test_arch_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ARCH]
    expected_literals = [
        "s390x",
        "sparc",
        "x86",
        "x86_64",
        "s390",
        "ia64_32",
        "ppc",
        "ppc64",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ARCH"

def test_buildtype_exists():
    # Check that the Enumeration exists
    assert BuildType is not None

def test_buildtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuildType]
    expected_literals = [
        "Release",
        "Continuous",
        "Nightly",
        "Integration",
        "Stable",
        "Maintenance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuildType"


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
build::InstallationUnit_strategy = st.builds(
    build::InstallationUnit,
    id=
        safe_text,
    version=
        safe_text
)
build::Repository_strategy = st.builds(
    build::Repository,
    location=
        safe_text,
    label=
        safe_text
)
InstallationUnit_strategy = st.builds(
    InstallationUnit,
)
build::Bundle_strategy = st.builds(
    build::Bundle,
)
build::Feature_strategy = st.builds(
    build::Feature,
    inProduct=
        st.booleans()
)
build::Build_strategy = st.builds(
    build::Build,
    buildRoot=
        safe_text,
    date=
        safe_text,
    time=
        safe_text,
    sendmail=
        st.booleans(),
    launchVM=
        safe_text,
    type=
        safe_text,
    builderURL=
        safe_text,
    fetchTag=
        safe_text,
    label=
        safe_text
)
build::Contact_strategy = st.builds(
    build::Contact,
    email=
        safe_text,
    name=
        safe_text
)
build::Promotion_strategy = st.builds(
    build::Promotion,
    baseURL=
        safe_text,
    uploadDirectory=
        safe_text,
    incubating=
        st.booleans(),
    buildAlias=
        safe_text,
    downloadDirectory=
        safe_text
)
build::Compiler_strategy = st.builds(
    build::Compiler,
    args=
        safe_text,
    targetVersion=
        safe_text,
    sourceVersion=
        safe_text,
    verbose=
        st.booleans(),
    debugInfo=
        st.booleans(),
    failOnError=
        st.booleans()
)
build::Product_strategy = st.builds(
    build::Product,
)
build::Contribution_strategy = st.builds(
    build::Contribution,
    label=
        safe_text
)
build::Category_strategy = st.builds(
    build::Category,
    description=
        safe_text,
    label=
        safe_text,
    name=
        safe_text
)
build::Map_strategy = st.builds(
    build::Map,
    repo=
        safe_text,
    root=
        safe_text,
    tag=
        safe_text
)
build::Config_strategy = st.builds(
    build::Config,
    os=
        safe_text,
    arch=
        safe_text,
    ws=
        safe_text,
    archiveFormat=
        safe_text
)
build::Platform_strategy = st.builds(
    build::Platform,
    deltapack=
        safe_text,
    file=
        safe_text,
    location=
        safe_text
)

@given(instance=build::InstallationUnit_strategy)
@settings(max_examples=50)
def test_build::installationunit_instantiation(instance):
    assert isinstance(instance, build::InstallationUnit)

@given(instance=build::InstallationUnit_strategy)
def test_build::installationunit_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=build::InstallationUnit_strategy)
def test_build::installationunit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=build::InstallationUnit_strategy)
def test_build::installationunit_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=build::InstallationUnit_strategy)
def test_build::installationunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=build::Repository_strategy)
@settings(max_examples=50)
def test_build::repository_instantiation(instance):
    assert isinstance(instance, build::Repository)

@given(instance=build::Repository_strategy)
def test_build::repository_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=build::Repository_strategy)
def test_build::repository_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=build::Repository_strategy)
def test_build::repository_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=build::Repository_strategy)
def test_build::repository_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=InstallationUnit_strategy)
@settings(max_examples=50)
def test_installationunit_instantiation(instance):
    assert isinstance(instance, InstallationUnit)

@given(instance=build::Bundle_strategy)
@settings(max_examples=50)
def test_build::bundle_instantiation(instance):
    assert isinstance(instance, build::Bundle)

@given(instance=build::Feature_strategy)
@settings(max_examples=50)
def test_build::feature_instantiation(instance):
    assert isinstance(instance, build::Feature)

@given(instance=build::Feature_strategy)
def test_build::feature_inProduct_type(instance):
    assert isinstance(instance.inProduct, bool)


@given(instance=build::Feature_strategy)
def test_build::feature_inProduct_setter(instance):
    original = instance.inProduct
    instance.inProduct = original
    assert instance.inProduct == original

@given(instance=build::Build_strategy)
@settings(max_examples=50)
def test_build::build_instantiation(instance):
    assert isinstance(instance, build::Build)

@given(instance=build::Build_strategy)
def test_build::build_buildRoot_type(instance):
    assert isinstance(instance.buildRoot, str)


@given(instance=build::Build_strategy)
def test_build::build_buildRoot_setter(instance):
    original = instance.buildRoot
    instance.buildRoot = original
    assert instance.buildRoot == original

@given(instance=build::Build_strategy)
def test_build::build_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=build::Build_strategy)
def test_build::build_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=build::Build_strategy)
def test_build::build_time_type(instance):
    assert isinstance(instance.time, str)


@given(instance=build::Build_strategy)
def test_build::build_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=build::Build_strategy)
def test_build::build_sendmail_type(instance):
    assert isinstance(instance.sendmail, bool)


@given(instance=build::Build_strategy)
def test_build::build_sendmail_setter(instance):
    original = instance.sendmail
    instance.sendmail = original
    assert instance.sendmail == original

@given(instance=build::Build_strategy)
def test_build::build_launchVM_type(instance):
    assert isinstance(instance.launchVM, str)


@given(instance=build::Build_strategy)
def test_build::build_launchVM_setter(instance):
    original = instance.launchVM
    instance.launchVM = original
    assert instance.launchVM == original

@given(instance=build::Build_strategy)
def test_build::build_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=build::Build_strategy)
def test_build::build_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=build::Build_strategy)
def test_build::build_builderURL_type(instance):
    assert isinstance(instance.builderURL, str)


@given(instance=build::Build_strategy)
def test_build::build_builderURL_setter(instance):
    original = instance.builderURL
    instance.builderURL = original
    assert instance.builderURL == original

@given(instance=build::Build_strategy)
def test_build::build_fetchTag_type(instance):
    assert isinstance(instance.fetchTag, str)


@given(instance=build::Build_strategy)
def test_build::build_fetchTag_setter(instance):
    original = instance.fetchTag
    instance.fetchTag = original
    assert instance.fetchTag == original

@given(instance=build::Build_strategy)
def test_build::build_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=build::Build_strategy)
def test_build::build_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=build::Contact_strategy)
@settings(max_examples=50)
def test_build::contact_instantiation(instance):
    assert isinstance(instance, build::Contact)

@given(instance=build::Contact_strategy)
def test_build::contact_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=build::Contact_strategy)
def test_build::contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=build::Contact_strategy)
def test_build::contact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=build::Contact_strategy)
def test_build::contact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=build::Promotion_strategy)
@settings(max_examples=50)
def test_build::promotion_instantiation(instance):
    assert isinstance(instance, build::Promotion)

@given(instance=build::Promotion_strategy)
def test_build::promotion_baseURL_type(instance):
    assert isinstance(instance.baseURL, str)


@given(instance=build::Promotion_strategy)
def test_build::promotion_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original

@given(instance=build::Promotion_strategy)
def test_build::promotion_uploadDirectory_type(instance):
    assert isinstance(instance.uploadDirectory, str)


@given(instance=build::Promotion_strategy)
def test_build::promotion_uploadDirectory_setter(instance):
    original = instance.uploadDirectory
    instance.uploadDirectory = original
    assert instance.uploadDirectory == original

@given(instance=build::Promotion_strategy)
def test_build::promotion_incubating_type(instance):
    assert isinstance(instance.incubating, bool)


@given(instance=build::Promotion_strategy)
def test_build::promotion_incubating_setter(instance):
    original = instance.incubating
    instance.incubating = original
    assert instance.incubating == original

@given(instance=build::Promotion_strategy)
def test_build::promotion_buildAlias_type(instance):
    assert isinstance(instance.buildAlias, str)


@given(instance=build::Promotion_strategy)
def test_build::promotion_buildAlias_setter(instance):
    original = instance.buildAlias
    instance.buildAlias = original
    assert instance.buildAlias == original

@given(instance=build::Promotion_strategy)
def test_build::promotion_downloadDirectory_type(instance):
    assert isinstance(instance.downloadDirectory, str)


@given(instance=build::Promotion_strategy)
def test_build::promotion_downloadDirectory_setter(instance):
    original = instance.downloadDirectory
    instance.downloadDirectory = original
    assert instance.downloadDirectory == original

@given(instance=build::Compiler_strategy)
@settings(max_examples=50)
def test_build::compiler_instantiation(instance):
    assert isinstance(instance, build::Compiler)

@given(instance=build::Compiler_strategy)
def test_build::compiler_args_type(instance):
    assert isinstance(instance.args, str)


@given(instance=build::Compiler_strategy)
def test_build::compiler_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original

@given(instance=build::Compiler_strategy)
def test_build::compiler_targetVersion_type(instance):
    assert isinstance(instance.targetVersion, str)


@given(instance=build::Compiler_strategy)
def test_build::compiler_targetVersion_setter(instance):
    original = instance.targetVersion
    instance.targetVersion = original
    assert instance.targetVersion == original

@given(instance=build::Compiler_strategy)
def test_build::compiler_sourceVersion_type(instance):
    assert isinstance(instance.sourceVersion, str)


@given(instance=build::Compiler_strategy)
def test_build::compiler_sourceVersion_setter(instance):
    original = instance.sourceVersion
    instance.sourceVersion = original
    assert instance.sourceVersion == original

@given(instance=build::Compiler_strategy)
def test_build::compiler_verbose_type(instance):
    assert isinstance(instance.verbose, bool)


@given(instance=build::Compiler_strategy)
def test_build::compiler_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original

@given(instance=build::Compiler_strategy)
def test_build::compiler_debugInfo_type(instance):
    assert isinstance(instance.debugInfo, bool)


@given(instance=build::Compiler_strategy)
def test_build::compiler_debugInfo_setter(instance):
    original = instance.debugInfo
    instance.debugInfo = original
    assert instance.debugInfo == original

@given(instance=build::Compiler_strategy)
def test_build::compiler_failOnError_type(instance):
    assert isinstance(instance.failOnError, bool)


@given(instance=build::Compiler_strategy)
def test_build::compiler_failOnError_setter(instance):
    original = instance.failOnError
    instance.failOnError = original
    assert instance.failOnError == original

@given(instance=build::Product_strategy)
@settings(max_examples=50)
def test_build::product_instantiation(instance):
    assert isinstance(instance, build::Product)

@given(instance=build::Contribution_strategy)
@settings(max_examples=50)
def test_build::contribution_instantiation(instance):
    assert isinstance(instance, build::Contribution)

@given(instance=build::Contribution_strategy)
def test_build::contribution_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=build::Contribution_strategy)
def test_build::contribution_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=build::Category_strategy)
@settings(max_examples=50)
def test_build::category_instantiation(instance):
    assert isinstance(instance, build::Category)

@given(instance=build::Category_strategy)
def test_build::category_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=build::Category_strategy)
def test_build::category_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=build::Category_strategy)
def test_build::category_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=build::Category_strategy)
def test_build::category_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=build::Category_strategy)
def test_build::category_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=build::Category_strategy)
def test_build::category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=build::Map_strategy)
@settings(max_examples=50)
def test_build::map_instantiation(instance):
    assert isinstance(instance, build::Map)

@given(instance=build::Map_strategy)
def test_build::map_repo_type(instance):
    assert isinstance(instance.repo, str)


@given(instance=build::Map_strategy)
def test_build::map_repo_setter(instance):
    original = instance.repo
    instance.repo = original
    assert instance.repo == original

@given(instance=build::Map_strategy)
def test_build::map_root_type(instance):
    assert isinstance(instance.root, str)


@given(instance=build::Map_strategy)
def test_build::map_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original

@given(instance=build::Map_strategy)
def test_build::map_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=build::Map_strategy)
def test_build::map_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=build::Config_strategy)
@settings(max_examples=50)
def test_build::config_instantiation(instance):
    assert isinstance(instance, build::Config)

@given(instance=build::Config_strategy)
def test_build::config_os_type(instance):
    assert isinstance(instance.os, str)


@given(instance=build::Config_strategy)
def test_build::config_os_setter(instance):
    original = instance.os
    instance.os = original
    assert instance.os == original

@given(instance=build::Config_strategy)
def test_build::config_arch_type(instance):
    assert isinstance(instance.arch, str)


@given(instance=build::Config_strategy)
def test_build::config_arch_setter(instance):
    original = instance.arch
    instance.arch = original
    assert instance.arch == original

@given(instance=build::Config_strategy)
def test_build::config_ws_type(instance):
    assert isinstance(instance.ws, str)


@given(instance=build::Config_strategy)
def test_build::config_ws_setter(instance):
    original = instance.ws
    instance.ws = original
    assert instance.ws == original

@given(instance=build::Config_strategy)
def test_build::config_archiveFormat_type(instance):
    assert isinstance(instance.archiveFormat, str)


@given(instance=build::Config_strategy)
def test_build::config_archiveFormat_setter(instance):
    original = instance.archiveFormat
    instance.archiveFormat = original
    assert instance.archiveFormat == original

@given(instance=build::Platform_strategy)
@settings(max_examples=50)
def test_build::platform_instantiation(instance):
    assert isinstance(instance, build::Platform)

@given(instance=build::Platform_strategy)
def test_build::platform_deltapack_type(instance):
    assert isinstance(instance.deltapack, str)


@given(instance=build::Platform_strategy)
def test_build::platform_deltapack_setter(instance):
    original = instance.deltapack
    instance.deltapack = original
    assert instance.deltapack == original

@given(instance=build::Platform_strategy)
def test_build::platform_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=build::Platform_strategy)
def test_build::platform_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=build::Platform_strategy)
def test_build::platform_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=build::Platform_strategy)
def test_build::platform_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
