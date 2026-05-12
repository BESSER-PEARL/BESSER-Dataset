import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    modulespecification_Module,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modulespecification_module_is_not_abstract():
    assert not inspect.isabstract(modulespecification_Module)


def test_modulespecification_module_constructor_exists():
    assert callable(modulespecification_Module.__init__)


def test_modulespecification_module_constructor_args():
    sig = inspect.signature(modulespecification_Module.__init__)
    params = list(sig.parameters.keys())
    assert "uie3Suffix" in params, "Missing parameter 'uie3Suffix'"
    assert "generateUiFragment" in params, "Missing parameter 'generateUiFragment'"
    assert "mavenVersionSuffix" in params, "Missing parameter 'mavenVersionSuffix'"
    assert "updateSiteId" in params, "Missing parameter 'updateSiteId'"
    assert "generateTests" in params, "Missing parameter 'generateTests'"
    assert "generateUpdatesite" in params, "Missing parameter 'generateUpdatesite'"
    assert "generateParent" in params, "Missing parameter 'generateParent'"
    assert "uie3Id" in params, "Missing parameter 'uie3Id'"
    assert "baseLocation" in params, "Missing parameter 'baseLocation'"
    assert "license" in params, "Missing parameter 'license'"
    assert "version" in params, "Missing parameter 'version'"
    assert "osgiVersion" in params, "Missing parameter 'osgiVersion'"
    assert "mavenVersion" in params, "Missing parameter 'mavenVersion'"
    assert "featureId" in params, "Missing parameter 'featureId'"
    assert "moduleName" in params, "Missing parameter 'moduleName'"
    assert "isLicenseUrlEmpty" in params, "Missing parameter 'isLicenseUrlEmpty'"
    assert "uiSuffix" in params, "Missing parameter 'uiSuffix'"
    assert "copyRightYear" in params, "Missing parameter 'copyRightYear'"
    assert "tychoParentName" in params, "Missing parameter 'tychoParentName'"
    assert "coreId" in params, "Missing parameter 'coreId'"
    assert "isUpdateSiteUrlEmpty" in params, "Missing parameter 'isUpdateSiteUrlEmpty'"
    assert "tychoVersion" in params, "Missing parameter 'tychoVersion'"
    assert "coreModuleName" in params, "Missing parameter 'coreModuleName'"
    assert "isAuthorEmailEmpty" in params, "Missing parameter 'isAuthorEmailEmpty'"
    assert "coreSuffix" in params, "Missing parameter 'coreSuffix'"
    assert "copyRightAuthorName" in params, "Missing parameter 'copyRightAuthorName'"
    assert "licenseUrl" in params, "Missing parameter 'licenseUrl'"
    assert "providerName" in params, "Missing parameter 'providerName'"
    assert "uiId" in params, "Missing parameter 'uiId'"
    assert "uiModuleName" in params, "Missing parameter 'uiModuleName'"
    assert "mavenGroupId" in params, "Missing parameter 'mavenGroupId'"
    assert "targetId" in params, "Missing parameter 'targetId'"
    assert "generateTarget" in params, "Missing parameter 'generateTarget'"
    assert "generateFeature" in params, "Missing parameter 'generateFeature'"
    assert "targetSuffix" in params, "Missing parameter 'targetSuffix'"
    assert "copyRightUrl" in params, "Missing parameter 'copyRightUrl'"
    assert "updateSiteUrl" in params, "Missing parameter 'updateSiteUrl'"
    assert "osgiVersionQualifier" in params, "Missing parameter 'osgiVersionQualifier'"
    assert "testsSuffix" in params, "Missing parameter 'testsSuffix'"
    assert "baseId" in params, "Missing parameter 'baseId'"
    assert "authorEmail" in params, "Missing parameter 'authorEmail'"
    assert "isLicenseEmpty" in params, "Missing parameter 'isLicenseEmpty'"
    assert "testsId" in params, "Missing parameter 'testsId'"
    assert "categoryName" in params, "Missing parameter 'categoryName'"
    assert "updateSiteSuffix" in params, "Missing parameter 'updateSiteSuffix'"
    assert "javaVersion" in params, "Missing parameter 'javaVersion'"
    assert "featureSuffix" in params, "Missing parameter 'featureSuffix'"

def test_modulespecification_module_has_uie3Suffix():
    assert hasattr(modulespecification_Module, "uie3Suffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "uie3Suffix" in klass.__dict__:
            descriptor = klass.__dict__["uie3Suffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateUiFragment():
    assert hasattr(modulespecification_Module, "generateUiFragment")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateUiFragment" in klass.__dict__:
            descriptor = klass.__dict__["generateUiFragment"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_mavenVersionSuffix():
    assert hasattr(modulespecification_Module, "mavenVersionSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "mavenVersionSuffix" in klass.__dict__:
            descriptor = klass.__dict__["mavenVersionSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_updateSiteId():
    assert hasattr(modulespecification_Module, "updateSiteId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "updateSiteId" in klass.__dict__:
            descriptor = klass.__dict__["updateSiteId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateTests():
    assert hasattr(modulespecification_Module, "generateTests")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateTests" in klass.__dict__:
            descriptor = klass.__dict__["generateTests"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateUpdatesite():
    assert hasattr(modulespecification_Module, "generateUpdatesite")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateUpdatesite" in klass.__dict__:
            descriptor = klass.__dict__["generateUpdatesite"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateParent():
    assert hasattr(modulespecification_Module, "generateParent")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateParent" in klass.__dict__:
            descriptor = klass.__dict__["generateParent"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_uie3Id():
    assert hasattr(modulespecification_Module, "uie3Id")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "uie3Id" in klass.__dict__:
            descriptor = klass.__dict__["uie3Id"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_baseLocation():
    assert hasattr(modulespecification_Module, "baseLocation")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "baseLocation" in klass.__dict__:
            descriptor = klass.__dict__["baseLocation"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_license():
    assert hasattr(modulespecification_Module, "license")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "license" in klass.__dict__:
            descriptor = klass.__dict__["license"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_version():
    assert hasattr(modulespecification_Module, "version")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_osgiVersion():
    assert hasattr(modulespecification_Module, "osgiVersion")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "osgiVersion" in klass.__dict__:
            descriptor = klass.__dict__["osgiVersion"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_mavenVersion():
    assert hasattr(modulespecification_Module, "mavenVersion")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "mavenVersion" in klass.__dict__:
            descriptor = klass.__dict__["mavenVersion"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_featureId():
    assert hasattr(modulespecification_Module, "featureId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "featureId" in klass.__dict__:
            descriptor = klass.__dict__["featureId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_moduleName():
    assert hasattr(modulespecification_Module, "moduleName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "moduleName" in klass.__dict__:
            descriptor = klass.__dict__["moduleName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_isLicenseUrlEmpty():
    assert hasattr(modulespecification_Module, "isLicenseUrlEmpty")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "isLicenseUrlEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isLicenseUrlEmpty"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_uiSuffix():
    assert hasattr(modulespecification_Module, "uiSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "uiSuffix" in klass.__dict__:
            descriptor = klass.__dict__["uiSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_copyRightYear():
    assert hasattr(modulespecification_Module, "copyRightYear")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "copyRightYear" in klass.__dict__:
            descriptor = klass.__dict__["copyRightYear"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_tychoParentName():
    assert hasattr(modulespecification_Module, "tychoParentName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "tychoParentName" in klass.__dict__:
            descriptor = klass.__dict__["tychoParentName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_coreId():
    assert hasattr(modulespecification_Module, "coreId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "coreId" in klass.__dict__:
            descriptor = klass.__dict__["coreId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_isUpdateSiteUrlEmpty():
    assert hasattr(modulespecification_Module, "isUpdateSiteUrlEmpty")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "isUpdateSiteUrlEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isUpdateSiteUrlEmpty"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_tychoVersion():
    assert hasattr(modulespecification_Module, "tychoVersion")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "tychoVersion" in klass.__dict__:
            descriptor = klass.__dict__["tychoVersion"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_coreModuleName():
    assert hasattr(modulespecification_Module, "coreModuleName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "coreModuleName" in klass.__dict__:
            descriptor = klass.__dict__["coreModuleName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_isAuthorEmailEmpty():
    assert hasattr(modulespecification_Module, "isAuthorEmailEmpty")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "isAuthorEmailEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isAuthorEmailEmpty"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_coreSuffix():
    assert hasattr(modulespecification_Module, "coreSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "coreSuffix" in klass.__dict__:
            descriptor = klass.__dict__["coreSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_copyRightAuthorName():
    assert hasattr(modulespecification_Module, "copyRightAuthorName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "copyRightAuthorName" in klass.__dict__:
            descriptor = klass.__dict__["copyRightAuthorName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_licenseUrl():
    assert hasattr(modulespecification_Module, "licenseUrl")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "licenseUrl" in klass.__dict__:
            descriptor = klass.__dict__["licenseUrl"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_providerName():
    assert hasattr(modulespecification_Module, "providerName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "providerName" in klass.__dict__:
            descriptor = klass.__dict__["providerName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_uiId():
    assert hasattr(modulespecification_Module, "uiId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "uiId" in klass.__dict__:
            descriptor = klass.__dict__["uiId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_uiModuleName():
    assert hasattr(modulespecification_Module, "uiModuleName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "uiModuleName" in klass.__dict__:
            descriptor = klass.__dict__["uiModuleName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_mavenGroupId():
    assert hasattr(modulespecification_Module, "mavenGroupId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "mavenGroupId" in klass.__dict__:
            descriptor = klass.__dict__["mavenGroupId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_targetId():
    assert hasattr(modulespecification_Module, "targetId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "targetId" in klass.__dict__:
            descriptor = klass.__dict__["targetId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateTarget():
    assert hasattr(modulespecification_Module, "generateTarget")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateTarget" in klass.__dict__:
            descriptor = klass.__dict__["generateTarget"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_generateFeature():
    assert hasattr(modulespecification_Module, "generateFeature")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "generateFeature" in klass.__dict__:
            descriptor = klass.__dict__["generateFeature"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_targetSuffix():
    assert hasattr(modulespecification_Module, "targetSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "targetSuffix" in klass.__dict__:
            descriptor = klass.__dict__["targetSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_copyRightUrl():
    assert hasattr(modulespecification_Module, "copyRightUrl")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "copyRightUrl" in klass.__dict__:
            descriptor = klass.__dict__["copyRightUrl"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_updateSiteUrl():
    assert hasattr(modulespecification_Module, "updateSiteUrl")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "updateSiteUrl" in klass.__dict__:
            descriptor = klass.__dict__["updateSiteUrl"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_osgiVersionQualifier():
    assert hasattr(modulespecification_Module, "osgiVersionQualifier")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "osgiVersionQualifier" in klass.__dict__:
            descriptor = klass.__dict__["osgiVersionQualifier"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_testsSuffix():
    assert hasattr(modulespecification_Module, "testsSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "testsSuffix" in klass.__dict__:
            descriptor = klass.__dict__["testsSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_baseId():
    assert hasattr(modulespecification_Module, "baseId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "baseId" in klass.__dict__:
            descriptor = klass.__dict__["baseId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_authorEmail():
    assert hasattr(modulespecification_Module, "authorEmail")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "authorEmail" in klass.__dict__:
            descriptor = klass.__dict__["authorEmail"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_isLicenseEmpty():
    assert hasattr(modulespecification_Module, "isLicenseEmpty")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "isLicenseEmpty" in klass.__dict__:
            descriptor = klass.__dict__["isLicenseEmpty"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_testsId():
    assert hasattr(modulespecification_Module, "testsId")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "testsId" in klass.__dict__:
            descriptor = klass.__dict__["testsId"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_categoryName():
    assert hasattr(modulespecification_Module, "categoryName")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "categoryName" in klass.__dict__:
            descriptor = klass.__dict__["categoryName"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_updateSiteSuffix():
    assert hasattr(modulespecification_Module, "updateSiteSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "updateSiteSuffix" in klass.__dict__:
            descriptor = klass.__dict__["updateSiteSuffix"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_javaVersion():
    assert hasattr(modulespecification_Module, "javaVersion")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "javaVersion" in klass.__dict__:
            descriptor = klass.__dict__["javaVersion"]
            break
    assert isinstance(descriptor, property)

def test_modulespecification_module_has_featureSuffix():
    assert hasattr(modulespecification_Module, "featureSuffix")
    descriptor = None
    for klass in modulespecification_Module.__mro__:
        if "featureSuffix" in klass.__dict__:
            descriptor = klass.__dict__["featureSuffix"]
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
modulespecification_Module_strategy = st.builds(
    modulespecification_Module,
    uie3Suffix=
        safe_text,
    generateUiFragment=
        st.booleans(),
    mavenVersionSuffix=
        safe_text,
    updateSiteId=
        safe_text,
    generateTests=
        st.booleans(),
    generateUpdatesite=
        st.booleans(),
    generateParent=
        st.booleans(),
    uie3Id=
        safe_text,
    baseLocation=
        safe_text,
    license=
        safe_text,
    version=
        safe_text,
    osgiVersion=
        safe_text,
    mavenVersion=
        safe_text,
    featureId=
        safe_text,
    moduleName=
        safe_text,
    isLicenseUrlEmpty=
        st.booleans(),
    uiSuffix=
        safe_text,
    copyRightYear=
        safe_text,
    tychoParentName=
        safe_text,
    coreId=
        safe_text,
    isUpdateSiteUrlEmpty=
        st.booleans(),
    tychoVersion=
        safe_text,
    coreModuleName=
        safe_text,
    isAuthorEmailEmpty=
        st.booleans(),
    coreSuffix=
        safe_text,
    copyRightAuthorName=
        safe_text,
    licenseUrl=
        safe_text,
    providerName=
        safe_text,
    uiId=
        safe_text,
    uiModuleName=
        safe_text,
    mavenGroupId=
        safe_text,
    targetId=
        safe_text,
    generateTarget=
        st.booleans(),
    generateFeature=
        st.booleans(),
    targetSuffix=
        safe_text,
    copyRightUrl=
        safe_text,
    updateSiteUrl=
        safe_text,
    osgiVersionQualifier=
        safe_text,
    testsSuffix=
        safe_text,
    baseId=
        safe_text,
    authorEmail=
        safe_text,
    isLicenseEmpty=
        st.booleans(),
    testsId=
        safe_text,
    categoryName=
        safe_text,
    updateSiteSuffix=
        safe_text,
    javaVersion=
        safe_text,
    featureSuffix=
        safe_text
)

@given(instance=modulespecification_Module_strategy)
@settings(max_examples=50)
def test_modulespecification_module_instantiation(instance):
    assert isinstance(instance, modulespecification_Module)



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_uie3Suffix_setter(instance):
    original = instance.uie3Suffix
    instance.uie3Suffix = original
    assert instance.uie3Suffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateUiFragment_setter(instance):
    original = instance.generateUiFragment
    instance.generateUiFragment = original
    assert instance.generateUiFragment == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_mavenVersionSuffix_setter(instance):
    original = instance.mavenVersionSuffix
    instance.mavenVersionSuffix = original
    assert instance.mavenVersionSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_updateSiteId_setter(instance):
    original = instance.updateSiteId
    instance.updateSiteId = original
    assert instance.updateSiteId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateTests_setter(instance):
    original = instance.generateTests
    instance.generateTests = original
    assert instance.generateTests == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateUpdatesite_setter(instance):
    original = instance.generateUpdatesite
    instance.generateUpdatesite = original
    assert instance.generateUpdatesite == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateParent_setter(instance):
    original = instance.generateParent
    instance.generateParent = original
    assert instance.generateParent == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_uie3Id_setter(instance):
    original = instance.uie3Id
    instance.uie3Id = original
    assert instance.uie3Id == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_baseLocation_setter(instance):
    original = instance.baseLocation
    instance.baseLocation = original
    assert instance.baseLocation == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_license_setter(instance):
    original = instance.license
    instance.license = original
    assert instance.license == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_osgiVersion_setter(instance):
    original = instance.osgiVersion
    instance.osgiVersion = original
    assert instance.osgiVersion == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_mavenVersion_setter(instance):
    original = instance.mavenVersion
    instance.mavenVersion = original
    assert instance.mavenVersion == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_featureId_setter(instance):
    original = instance.featureId
    instance.featureId = original
    assert instance.featureId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_moduleName_setter(instance):
    original = instance.moduleName
    instance.moduleName = original
    assert instance.moduleName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_isLicenseUrlEmpty_setter(instance):
    original = instance.isLicenseUrlEmpty
    instance.isLicenseUrlEmpty = original
    assert instance.isLicenseUrlEmpty == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_uiSuffix_setter(instance):
    original = instance.uiSuffix
    instance.uiSuffix = original
    assert instance.uiSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_copyRightYear_setter(instance):
    original = instance.copyRightYear
    instance.copyRightYear = original
    assert instance.copyRightYear == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_tychoParentName_setter(instance):
    original = instance.tychoParentName
    instance.tychoParentName = original
    assert instance.tychoParentName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_coreId_setter(instance):
    original = instance.coreId
    instance.coreId = original
    assert instance.coreId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_isUpdateSiteUrlEmpty_setter(instance):
    original = instance.isUpdateSiteUrlEmpty
    instance.isUpdateSiteUrlEmpty = original
    assert instance.isUpdateSiteUrlEmpty == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_tychoVersion_setter(instance):
    original = instance.tychoVersion
    instance.tychoVersion = original
    assert instance.tychoVersion == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_coreModuleName_setter(instance):
    original = instance.coreModuleName
    instance.coreModuleName = original
    assert instance.coreModuleName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_isAuthorEmailEmpty_setter(instance):
    original = instance.isAuthorEmailEmpty
    instance.isAuthorEmailEmpty = original
    assert instance.isAuthorEmailEmpty == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_coreSuffix_setter(instance):
    original = instance.coreSuffix
    instance.coreSuffix = original
    assert instance.coreSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_copyRightAuthorName_setter(instance):
    original = instance.copyRightAuthorName
    instance.copyRightAuthorName = original
    assert instance.copyRightAuthorName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_licenseUrl_setter(instance):
    original = instance.licenseUrl
    instance.licenseUrl = original
    assert instance.licenseUrl == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_providerName_setter(instance):
    original = instance.providerName
    instance.providerName = original
    assert instance.providerName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_uiId_setter(instance):
    original = instance.uiId
    instance.uiId = original
    assert instance.uiId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_uiModuleName_setter(instance):
    original = instance.uiModuleName
    instance.uiModuleName = original
    assert instance.uiModuleName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_mavenGroupId_setter(instance):
    original = instance.mavenGroupId
    instance.mavenGroupId = original
    assert instance.mavenGroupId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_targetId_setter(instance):
    original = instance.targetId
    instance.targetId = original
    assert instance.targetId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateTarget_setter(instance):
    original = instance.generateTarget
    instance.generateTarget = original
    assert instance.generateTarget == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_generateFeature_setter(instance):
    original = instance.generateFeature
    instance.generateFeature = original
    assert instance.generateFeature == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_targetSuffix_setter(instance):
    original = instance.targetSuffix
    instance.targetSuffix = original
    assert instance.targetSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_copyRightUrl_setter(instance):
    original = instance.copyRightUrl
    instance.copyRightUrl = original
    assert instance.copyRightUrl == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_updateSiteUrl_setter(instance):
    original = instance.updateSiteUrl
    instance.updateSiteUrl = original
    assert instance.updateSiteUrl == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_osgiVersionQualifier_setter(instance):
    original = instance.osgiVersionQualifier
    instance.osgiVersionQualifier = original
    assert instance.osgiVersionQualifier == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_testsSuffix_setter(instance):
    original = instance.testsSuffix
    instance.testsSuffix = original
    assert instance.testsSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_baseId_setter(instance):
    original = instance.baseId
    instance.baseId = original
    assert instance.baseId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_authorEmail_setter(instance):
    original = instance.authorEmail
    instance.authorEmail = original
    assert instance.authorEmail == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_isLicenseEmpty_setter(instance):
    original = instance.isLicenseEmpty
    instance.isLicenseEmpty = original
    assert instance.isLicenseEmpty == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_testsId_setter(instance):
    original = instance.testsId
    instance.testsId = original
    assert instance.testsId == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_categoryName_setter(instance):
    original = instance.categoryName
    instance.categoryName = original
    assert instance.categoryName == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_updateSiteSuffix_setter(instance):
    original = instance.updateSiteSuffix
    instance.updateSiteSuffix = original
    assert instance.updateSiteSuffix == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_javaVersion_setter(instance):
    original = instance.javaVersion
    instance.javaVersion = original
    assert instance.javaVersion == original



@given(instance=modulespecification_Module_strategy)
def test_modulespecification_module_featureSuffix_setter(instance):
    original = instance.featureSuffix
    instance.featureSuffix = original
    assert instance.featureSuffix == original
