import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    build_Build,
    build_Contact,
    build_Promotion,
    build_Compiler,
    build_Contribution,
    build_Category,
    build_Map,
    build_Config,
    build_Platform,
    build_InstallationUnit,
    build_Repository,
    InstallationUnit,
    build_Feature,
    build_Product,
    build_Bundle,
    BuildType,
    OS,
    ArchiveFormat,
    WS,
    ARCH,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_build_build_is_not_abstract():
    assert not inspect.isabstract(build_Build)


def test_build_build_constructor_exists():
    assert callable(build_Build.__init__)


def test_build_build_constructor_args():
    sig = inspect.signature(build_Build.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "sendmail" in params, "Missing parameter 'sendmail'"
    assert "time" in params, "Missing parameter 'time'"
    assert "buildRoot" in params, "Missing parameter 'buildRoot'"
    assert "label" in params, "Missing parameter 'label'"
    assert "type" in params, "Missing parameter 'type'"
    assert "builderURL" in params, "Missing parameter 'builderURL'"
    assert "launchVM" in params, "Missing parameter 'launchVM'"
    assert "fetchTag" in params, "Missing parameter 'fetchTag'"

def test_build_build_has_date():
    assert hasattr(build_Build, "date")
    descriptor = None
    for klass in build_Build.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_sendmail():
    assert hasattr(build_Build, "sendmail")
    descriptor = None
    for klass in build_Build.__mro__:
        if "sendmail" in klass.__dict__:
            descriptor = klass.__dict__["sendmail"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_time():
    assert hasattr(build_Build, "time")
    descriptor = None
    for klass in build_Build.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_buildRoot():
    assert hasattr(build_Build, "buildRoot")
    descriptor = None
    for klass in build_Build.__mro__:
        if "buildRoot" in klass.__dict__:
            descriptor = klass.__dict__["buildRoot"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_label():
    assert hasattr(build_Build, "label")
    descriptor = None
    for klass in build_Build.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_type():
    assert hasattr(build_Build, "type")
    descriptor = None
    for klass in build_Build.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_builderURL():
    assert hasattr(build_Build, "builderURL")
    descriptor = None
    for klass in build_Build.__mro__:
        if "builderURL" in klass.__dict__:
            descriptor = klass.__dict__["builderURL"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_launchVM():
    assert hasattr(build_Build, "launchVM")
    descriptor = None
    for klass in build_Build.__mro__:
        if "launchVM" in klass.__dict__:
            descriptor = klass.__dict__["launchVM"]
            break
    assert isinstance(descriptor, property)

def test_build_build_has_fetchTag():
    assert hasattr(build_Build, "fetchTag")
    descriptor = None
    for klass in build_Build.__mro__:
        if "fetchTag" in klass.__dict__:
            descriptor = klass.__dict__["fetchTag"]
            break
    assert isinstance(descriptor, property)



def test_build_contact_is_not_abstract():
    assert not inspect.isabstract(build_Contact)


def test_build_contact_constructor_exists():
    assert callable(build_Contact.__init__)


def test_build_contact_constructor_args():
    sig = inspect.signature(build_Contact.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "name" in params, "Missing parameter 'name'"

def test_build_contact_has_email():
    assert hasattr(build_Contact, "email")
    descriptor = None
    for klass in build_Contact.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_build_contact_has_name():
    assert hasattr(build_Contact, "name")
    descriptor = None
    for klass in build_Contact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_build_promotion_is_not_abstract():
    assert not inspect.isabstract(build_Promotion)


def test_build_promotion_constructor_exists():
    assert callable(build_Promotion.__init__)


def test_build_promotion_constructor_args():
    sig = inspect.signature(build_Promotion.__init__)
    params = list(sig.parameters.keys())
    assert "incubating" in params, "Missing parameter 'incubating'"
    assert "uploadDirectory" in params, "Missing parameter 'uploadDirectory'"
    assert "buildAlias" in params, "Missing parameter 'buildAlias'"
    assert "baseURL" in params, "Missing parameter 'baseURL'"
    assert "downloadDirectory" in params, "Missing parameter 'downloadDirectory'"

def test_build_promotion_has_incubating():
    assert hasattr(build_Promotion, "incubating")
    descriptor = None
    for klass in build_Promotion.__mro__:
        if "incubating" in klass.__dict__:
            descriptor = klass.__dict__["incubating"]
            break
    assert isinstance(descriptor, property)

def test_build_promotion_has_uploadDirectory():
    assert hasattr(build_Promotion, "uploadDirectory")
    descriptor = None
    for klass in build_Promotion.__mro__:
        if "uploadDirectory" in klass.__dict__:
            descriptor = klass.__dict__["uploadDirectory"]
            break
    assert isinstance(descriptor, property)

def test_build_promotion_has_buildAlias():
    assert hasattr(build_Promotion, "buildAlias")
    descriptor = None
    for klass in build_Promotion.__mro__:
        if "buildAlias" in klass.__dict__:
            descriptor = klass.__dict__["buildAlias"]
            break
    assert isinstance(descriptor, property)

def test_build_promotion_has_baseURL():
    assert hasattr(build_Promotion, "baseURL")
    descriptor = None
    for klass in build_Promotion.__mro__:
        if "baseURL" in klass.__dict__:
            descriptor = klass.__dict__["baseURL"]
            break
    assert isinstance(descriptor, property)

def test_build_promotion_has_downloadDirectory():
    assert hasattr(build_Promotion, "downloadDirectory")
    descriptor = None
    for klass in build_Promotion.__mro__:
        if "downloadDirectory" in klass.__dict__:
            descriptor = klass.__dict__["downloadDirectory"]
            break
    assert isinstance(descriptor, property)



def test_build_compiler_is_not_abstract():
    assert not inspect.isabstract(build_Compiler)


def test_build_compiler_constructor_exists():
    assert callable(build_Compiler.__init__)


def test_build_compiler_constructor_args():
    sig = inspect.signature(build_Compiler.__init__)
    params = list(sig.parameters.keys())
    assert "verbose" in params, "Missing parameter 'verbose'"
    assert "args" in params, "Missing parameter 'args'"
    assert "targetVersion" in params, "Missing parameter 'targetVersion'"
    assert "sourceVersion" in params, "Missing parameter 'sourceVersion'"
    assert "debugInfo" in params, "Missing parameter 'debugInfo'"
    assert "failOnError" in params, "Missing parameter 'failOnError'"

def test_build_compiler_has_verbose():
    assert hasattr(build_Compiler, "verbose")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "verbose" in klass.__dict__:
            descriptor = klass.__dict__["verbose"]
            break
    assert isinstance(descriptor, property)

def test_build_compiler_has_args():
    assert hasattr(build_Compiler, "args")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "args" in klass.__dict__:
            descriptor = klass.__dict__["args"]
            break
    assert isinstance(descriptor, property)

def test_build_compiler_has_targetVersion():
    assert hasattr(build_Compiler, "targetVersion")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "targetVersion" in klass.__dict__:
            descriptor = klass.__dict__["targetVersion"]
            break
    assert isinstance(descriptor, property)

def test_build_compiler_has_sourceVersion():
    assert hasattr(build_Compiler, "sourceVersion")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "sourceVersion" in klass.__dict__:
            descriptor = klass.__dict__["sourceVersion"]
            break
    assert isinstance(descriptor, property)

def test_build_compiler_has_debugInfo():
    assert hasattr(build_Compiler, "debugInfo")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "debugInfo" in klass.__dict__:
            descriptor = klass.__dict__["debugInfo"]
            break
    assert isinstance(descriptor, property)

def test_build_compiler_has_failOnError():
    assert hasattr(build_Compiler, "failOnError")
    descriptor = None
    for klass in build_Compiler.__mro__:
        if "failOnError" in klass.__dict__:
            descriptor = klass.__dict__["failOnError"]
            break
    assert isinstance(descriptor, property)



def test_build_contribution_is_not_abstract():
    assert not inspect.isabstract(build_Contribution)


def test_build_contribution_constructor_exists():
    assert callable(build_Contribution.__init__)


def test_build_contribution_constructor_args():
    sig = inspect.signature(build_Contribution.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_build_contribution_has_label():
    assert hasattr(build_Contribution, "label")
    descriptor = None
    for klass in build_Contribution.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_build_category_is_not_abstract():
    assert not inspect.isabstract(build_Category)


def test_build_category_constructor_exists():
    assert callable(build_Category.__init__)


def test_build_category_constructor_args():
    sig = inspect.signature(build_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "label" in params, "Missing parameter 'label'"

def test_build_category_has_name():
    assert hasattr(build_Category, "name")
    descriptor = None
    for klass in build_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_build_category_has_description():
    assert hasattr(build_Category, "description")
    descriptor = None
    for klass in build_Category.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_build_category_has_label():
    assert hasattr(build_Category, "label")
    descriptor = None
    for klass in build_Category.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_build_map_is_not_abstract():
    assert not inspect.isabstract(build_Map)


def test_build_map_constructor_exists():
    assert callable(build_Map.__init__)


def test_build_map_constructor_args():
    sig = inspect.signature(build_Map.__init__)
    params = list(sig.parameters.keys())
    assert "root" in params, "Missing parameter 'root'"
    assert "tag" in params, "Missing parameter 'tag'"
    assert "repo" in params, "Missing parameter 'repo'"

def test_build_map_has_root():
    assert hasattr(build_Map, "root")
    descriptor = None
    for klass in build_Map.__mro__:
        if "root" in klass.__dict__:
            descriptor = klass.__dict__["root"]
            break
    assert isinstance(descriptor, property)

def test_build_map_has_tag():
    assert hasattr(build_Map, "tag")
    descriptor = None
    for klass in build_Map.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)

def test_build_map_has_repo():
    assert hasattr(build_Map, "repo")
    descriptor = None
    for klass in build_Map.__mro__:
        if "repo" in klass.__dict__:
            descriptor = klass.__dict__["repo"]
            break
    assert isinstance(descriptor, property)



def test_build_config_is_not_abstract():
    assert not inspect.isabstract(build_Config)


def test_build_config_constructor_exists():
    assert callable(build_Config.__init__)


def test_build_config_constructor_args():
    sig = inspect.signature(build_Config.__init__)
    params = list(sig.parameters.keys())
    assert "os" in params, "Missing parameter 'os'"
    assert "archiveFormat" in params, "Missing parameter 'archiveFormat'"
    assert "ws" in params, "Missing parameter 'ws'"
    assert "arch" in params, "Missing parameter 'arch'"

def test_build_config_has_os():
    assert hasattr(build_Config, "os")
    descriptor = None
    for klass in build_Config.__mro__:
        if "os" in klass.__dict__:
            descriptor = klass.__dict__["os"]
            break
    assert isinstance(descriptor, property)

def test_build_config_has_archiveFormat():
    assert hasattr(build_Config, "archiveFormat")
    descriptor = None
    for klass in build_Config.__mro__:
        if "archiveFormat" in klass.__dict__:
            descriptor = klass.__dict__["archiveFormat"]
            break
    assert isinstance(descriptor, property)

def test_build_config_has_ws():
    assert hasattr(build_Config, "ws")
    descriptor = None
    for klass in build_Config.__mro__:
        if "ws" in klass.__dict__:
            descriptor = klass.__dict__["ws"]
            break
    assert isinstance(descriptor, property)

def test_build_config_has_arch():
    assert hasattr(build_Config, "arch")
    descriptor = None
    for klass in build_Config.__mro__:
        if "arch" in klass.__dict__:
            descriptor = klass.__dict__["arch"]
            break
    assert isinstance(descriptor, property)



def test_build_platform_is_not_abstract():
    assert not inspect.isabstract(build_Platform)


def test_build_platform_constructor_exists():
    assert callable(build_Platform.__init__)


def test_build_platform_constructor_args():
    sig = inspect.signature(build_Platform.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "deltapack" in params, "Missing parameter 'deltapack'"
    assert "file" in params, "Missing parameter 'file'"

def test_build_platform_has_location():
    assert hasattr(build_Platform, "location")
    descriptor = None
    for klass in build_Platform.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_build_platform_has_deltapack():
    assert hasattr(build_Platform, "deltapack")
    descriptor = None
    for klass in build_Platform.__mro__:
        if "deltapack" in klass.__dict__:
            descriptor = klass.__dict__["deltapack"]
            break
    assert isinstance(descriptor, property)

def test_build_platform_has_file():
    assert hasattr(build_Platform, "file")
    descriptor = None
    for klass in build_Platform.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_build_installationunit_is_not_abstract():
    assert not inspect.isabstract(build_InstallationUnit)


def test_build_installationunit_constructor_exists():
    assert callable(build_InstallationUnit.__init__)


def test_build_installationunit_constructor_args():
    sig = inspect.signature(build_InstallationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "version" in params, "Missing parameter 'version'"

def test_build_installationunit_has_id():
    assert hasattr(build_InstallationUnit, "id")
    descriptor = None
    for klass in build_InstallationUnit.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_build_installationunit_has_version():
    assert hasattr(build_InstallationUnit, "version")
    descriptor = None
    for klass in build_InstallationUnit.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_build_repository_is_not_abstract():
    assert not inspect.isabstract(build_Repository)


def test_build_repository_constructor_exists():
    assert callable(build_Repository.__init__)


def test_build_repository_constructor_args():
    sig = inspect.signature(build_Repository.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "label" in params, "Missing parameter 'label'"

def test_build_repository_has_location():
    assert hasattr(build_Repository, "location")
    descriptor = None
    for klass in build_Repository.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_build_repository_has_label():
    assert hasattr(build_Repository, "label")
    descriptor = None
    for klass in build_Repository.__mro__:
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



def test_build_feature_is_not_abstract():
    assert not inspect.isabstract(build_Feature)


def test_build_feature_constructor_exists():
    assert callable(build_Feature.__init__)


def test_build_feature_constructor_args():
    sig = inspect.signature(build_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "inProduct" in params, "Missing parameter 'inProduct'"

def test_build_feature_has_inProduct():
    assert hasattr(build_Feature, "inProduct")
    descriptor = None
    for klass in build_Feature.__mro__:
        if "inProduct" in klass.__dict__:
            descriptor = klass.__dict__["inProduct"]
            break
    assert isinstance(descriptor, property)



def test_build_product_is_not_abstract():
    assert not inspect.isabstract(build_Product)


def test_build_product_constructor_exists():
    assert callable(build_Product.__init__)


def test_build_product_constructor_args():
    sig = inspect.signature(build_Product.__init__)
    params = list(sig.parameters.keys())



def test_build_bundle_is_not_abstract():
    assert not inspect.isabstract(build_Bundle)


def test_build_bundle_constructor_exists():
    assert callable(build_Bundle.__init__)


def test_build_bundle_constructor_args():
    sig = inspect.signature(build_Bundle.__init__)
    params = list(sig.parameters.keys())

def test_buildtype_exists():
    # Check that the Enumeration exists
    assert BuildType is not None

def test_buildtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BuildType]
    expected_literals = [
        "Continuous",
        "Integration",
        "Release",
        "Stable",
        "Nightly",
        "Maintenance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BuildType"

def test_os_exists():
    # Check that the Enumeration exists
    assert OS is not None

def test_os_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OS]
    expected_literals = [
        "linux",
        "macosx",
        "aix",
        "solaris",
        "hpux",
        "win32",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OS"

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

def test_ws_exists():
    # Check that the Enumeration exists
    assert WS is not None

def test_ws_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WS]
    expected_literals = [
        "motif",
        "win32",
        "carbon",
        "gtk",
        "cocoa",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WS"

def test_arch_exists():
    # Check that the Enumeration exists
    assert ARCH is not None

def test_arch_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ARCH]
    expected_literals = [
        "s390x",
        "x86_64",
        "sparc",
        "s390",
        "x86",
        "ppc64",
        "ppc",
        "ia64_32",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ARCH"


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
build_Build_strategy = st.builds(
    build_Build,
    date=
        safe_text,
    sendmail=
        st.booleans(),
    time=
        safe_text,
    buildRoot=
        safe_text,
    label=
        safe_text,
    type=
        safe_text,
    builderURL=
        safe_text,
    launchVM=
        safe_text,
    fetchTag=
        safe_text
)
build_Contact_strategy = st.builds(
    build_Contact,
    email=
        safe_text,
    name=
        safe_text
)
build_Promotion_strategy = st.builds(
    build_Promotion,
    incubating=
        st.booleans(),
    uploadDirectory=
        safe_text,
    buildAlias=
        safe_text,
    baseURL=
        safe_text,
    downloadDirectory=
        safe_text
)
build_Compiler_strategy = st.builds(
    build_Compiler,
    verbose=
        st.booleans(),
    args=
        safe_text,
    targetVersion=
        safe_text,
    sourceVersion=
        safe_text,
    debugInfo=
        st.booleans(),
    failOnError=
        st.booleans()
)
build_Contribution_strategy = st.builds(
    build_Contribution,
    label=
        safe_text
)
build_Category_strategy = st.builds(
    build_Category,
    name=
        safe_text,
    description=
        safe_text,
    label=
        safe_text
)
build_Map_strategy = st.builds(
    build_Map,
    root=
        safe_text,
    tag=
        safe_text,
    repo=
        safe_text
)
build_Config_strategy = st.builds(
    build_Config,
    os=
        safe_text,
    archiveFormat=
        safe_text,
    ws=
        safe_text,
    arch=
        safe_text
)
build_Platform_strategy = st.builds(
    build_Platform,
    location=
        safe_text,
    deltapack=
        safe_text,
    file=
        safe_text
)
build_InstallationUnit_strategy = st.builds(
    build_InstallationUnit,
    id=
        safe_text,
    version=
        safe_text
)
build_Repository_strategy = st.builds(
    build_Repository,
    location=
        safe_text,
    label=
        safe_text
)
InstallationUnit_strategy = st.builds(
    InstallationUnit,
)
build_Feature_strategy = st.builds(
    build_Feature,
    inProduct=
        st.booleans()
)
build_Product_strategy = st.builds(
    build_Product,
)
build_Bundle_strategy = st.builds(
    build_Bundle,
)

@given(instance=build_Build_strategy)
@settings(max_examples=50)
def test_build_build_instantiation(instance):
    assert isinstance(instance, build_Build)



@given(instance=build_Build_strategy)
def test_build_build_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=build_Build_strategy)
def test_build_build_sendmail_setter(instance):
    original = instance.sendmail
    instance.sendmail = original
    assert instance.sendmail == original



@given(instance=build_Build_strategy)
def test_build_build_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original



@given(instance=build_Build_strategy)
def test_build_build_buildRoot_setter(instance):
    original = instance.buildRoot
    instance.buildRoot = original
    assert instance.buildRoot == original



@given(instance=build_Build_strategy)
def test_build_build_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=build_Build_strategy)
def test_build_build_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=build_Build_strategy)
def test_build_build_builderURL_setter(instance):
    original = instance.builderURL
    instance.builderURL = original
    assert instance.builderURL == original



@given(instance=build_Build_strategy)
def test_build_build_launchVM_setter(instance):
    original = instance.launchVM
    instance.launchVM = original
    assert instance.launchVM == original



@given(instance=build_Build_strategy)
def test_build_build_fetchTag_setter(instance):
    original = instance.fetchTag
    instance.fetchTag = original
    assert instance.fetchTag == original

@given(instance=build_Contact_strategy)
@settings(max_examples=50)
def test_build_contact_instantiation(instance):
    assert isinstance(instance, build_Contact)



@given(instance=build_Contact_strategy)
def test_build_contact_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=build_Contact_strategy)
def test_build_contact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=build_Promotion_strategy)
@settings(max_examples=50)
def test_build_promotion_instantiation(instance):
    assert isinstance(instance, build_Promotion)



@given(instance=build_Promotion_strategy)
def test_build_promotion_incubating_setter(instance):
    original = instance.incubating
    instance.incubating = original
    assert instance.incubating == original



@given(instance=build_Promotion_strategy)
def test_build_promotion_uploadDirectory_setter(instance):
    original = instance.uploadDirectory
    instance.uploadDirectory = original
    assert instance.uploadDirectory == original



@given(instance=build_Promotion_strategy)
def test_build_promotion_buildAlias_setter(instance):
    original = instance.buildAlias
    instance.buildAlias = original
    assert instance.buildAlias == original



@given(instance=build_Promotion_strategy)
def test_build_promotion_baseURL_setter(instance):
    original = instance.baseURL
    instance.baseURL = original
    assert instance.baseURL == original



@given(instance=build_Promotion_strategy)
def test_build_promotion_downloadDirectory_setter(instance):
    original = instance.downloadDirectory
    instance.downloadDirectory = original
    assert instance.downloadDirectory == original

@given(instance=build_Compiler_strategy)
@settings(max_examples=50)
def test_build_compiler_instantiation(instance):
    assert isinstance(instance, build_Compiler)



@given(instance=build_Compiler_strategy)
def test_build_compiler_verbose_setter(instance):
    original = instance.verbose
    instance.verbose = original
    assert instance.verbose == original



@given(instance=build_Compiler_strategy)
def test_build_compiler_args_setter(instance):
    original = instance.args
    instance.args = original
    assert instance.args == original



@given(instance=build_Compiler_strategy)
def test_build_compiler_targetVersion_setter(instance):
    original = instance.targetVersion
    instance.targetVersion = original
    assert instance.targetVersion == original



@given(instance=build_Compiler_strategy)
def test_build_compiler_sourceVersion_setter(instance):
    original = instance.sourceVersion
    instance.sourceVersion = original
    assert instance.sourceVersion == original



@given(instance=build_Compiler_strategy)
def test_build_compiler_debugInfo_setter(instance):
    original = instance.debugInfo
    instance.debugInfo = original
    assert instance.debugInfo == original



@given(instance=build_Compiler_strategy)
def test_build_compiler_failOnError_setter(instance):
    original = instance.failOnError
    instance.failOnError = original
    assert instance.failOnError == original

@given(instance=build_Contribution_strategy)
@settings(max_examples=50)
def test_build_contribution_instantiation(instance):
    assert isinstance(instance, build_Contribution)



@given(instance=build_Contribution_strategy)
def test_build_contribution_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=build_Category_strategy)
@settings(max_examples=50)
def test_build_category_instantiation(instance):
    assert isinstance(instance, build_Category)



@given(instance=build_Category_strategy)
def test_build_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=build_Category_strategy)
def test_build_category_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=build_Category_strategy)
def test_build_category_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=build_Map_strategy)
@settings(max_examples=50)
def test_build_map_instantiation(instance):
    assert isinstance(instance, build_Map)



@given(instance=build_Map_strategy)
def test_build_map_root_setter(instance):
    original = instance.root
    instance.root = original
    assert instance.root == original



@given(instance=build_Map_strategy)
def test_build_map_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original



@given(instance=build_Map_strategy)
def test_build_map_repo_setter(instance):
    original = instance.repo
    instance.repo = original
    assert instance.repo == original

@given(instance=build_Config_strategy)
@settings(max_examples=50)
def test_build_config_instantiation(instance):
    assert isinstance(instance, build_Config)



@given(instance=build_Config_strategy)
def test_build_config_os_setter(instance):
    original = instance.os
    instance.os = original
    assert instance.os == original



@given(instance=build_Config_strategy)
def test_build_config_archiveFormat_setter(instance):
    original = instance.archiveFormat
    instance.archiveFormat = original
    assert instance.archiveFormat == original



@given(instance=build_Config_strategy)
def test_build_config_ws_setter(instance):
    original = instance.ws
    instance.ws = original
    assert instance.ws == original



@given(instance=build_Config_strategy)
def test_build_config_arch_setter(instance):
    original = instance.arch
    instance.arch = original
    assert instance.arch == original

@given(instance=build_Platform_strategy)
@settings(max_examples=50)
def test_build_platform_instantiation(instance):
    assert isinstance(instance, build_Platform)



@given(instance=build_Platform_strategy)
def test_build_platform_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=build_Platform_strategy)
def test_build_platform_deltapack_setter(instance):
    original = instance.deltapack
    instance.deltapack = original
    assert instance.deltapack == original



@given(instance=build_Platform_strategy)
def test_build_platform_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=build_InstallationUnit_strategy)
@settings(max_examples=50)
def test_build_installationunit_instantiation(instance):
    assert isinstance(instance, build_InstallationUnit)



@given(instance=build_InstallationUnit_strategy)
def test_build_installationunit_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=build_InstallationUnit_strategy)
def test_build_installationunit_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=build_Repository_strategy)
@settings(max_examples=50)
def test_build_repository_instantiation(instance):
    assert isinstance(instance, build_Repository)



@given(instance=build_Repository_strategy)
def test_build_repository_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=build_Repository_strategy)
def test_build_repository_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=InstallationUnit_strategy)
@settings(max_examples=50)
def test_installationunit_instantiation(instance):
    assert isinstance(instance, InstallationUnit)

@given(instance=build_Feature_strategy)
@settings(max_examples=50)
def test_build_feature_instantiation(instance):
    assert isinstance(instance, build_Feature)



@given(instance=build_Feature_strategy)
def test_build_feature_inProduct_setter(instance):
    original = instance.inProduct
    instance.inProduct = original
    assert instance.inProduct == original

@given(instance=build_Product_strategy)
@settings(max_examples=50)
def test_build_product_instantiation(instance):
    assert isinstance(instance, build_Product)

@given(instance=build_Bundle_strategy)
@settings(max_examples=50)
def test_build_bundle_instantiation(instance):
    assert isinstance(instance, build_Bundle)
