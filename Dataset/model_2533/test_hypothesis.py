import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    raas::small::test::#10382437,
    raas::small::test::#30911270,
    raas::small::test::FourthLevelClassK,
    raas::small::test::#11832905,
    raas::small::test::ThirdLevelClassJ,
    raas::small::test::UnderClassF,
    raas::small::test::UnderClassE,
    raas::small::test::DerivedUnderClassE1,
    raas::small::test::DerivedUnderClassE2,
    raas::small::test::MergingE1AndE2,
    raas::small::test::TopClassD,
    raas::small::test::TopClassC,
    raas::small::test::TopClassB,
    raas::small::test::#16551649,
    raas::small::test::#5656663,
    raas::small::test::TopClassA,
    raas::small::test::TopClassM,
    raas::small::test::#7345254,
    raas::small::test::#19723516,
    raas::small::test::#29373817,
    raas::small::test::ReposRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_raas::small::test::#10382437_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#10382437)


def test_raas::small::test::#10382437_constructor_exists():
    assert callable(raas::small::test::#10382437.__init__)


def test_raas::small::test::#10382437_constructor_args():
    sig = inspect.signature(raas::small::test::#10382437.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::#30911270_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#30911270)


def test_raas::small::test::#30911270_constructor_exists():
    assert callable(raas::small::test::#30911270.__init__)


def test_raas::small::test::#30911270_constructor_args():
    sig = inspect.signature(raas::small::test::#30911270.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::fourthlevelclassk_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::FourthLevelClassK)


def test_raas::small::test::fourthlevelclassk_constructor_exists():
    assert callable(raas::small::test::FourthLevelClassK.__init__)


def test_raas::small::test::fourthlevelclassk_constructor_args():
    sig = inspect.signature(raas::small::test::FourthLevelClassK.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"

def test_raas::small::test::fourthlevelclassk_has_raasRef():
    assert hasattr(raas::small::test::FourthLevelClassK, "raasRef")
    descriptor = None
    for klass in raas::small::test::FourthLevelClassK.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::fourthlevelclassk_has_optionalAttrInt():
    assert hasattr(raas::small::test::FourthLevelClassK, "optionalAttrInt")
    descriptor = None
    for klass in raas::small::test::FourthLevelClassK.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::fourthlevelclassk_has_singleAttrInt():
    assert hasattr(raas::small::test::FourthLevelClassK, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::FourthLevelClassK.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::fourthlevelclassk_has_multi2lowerAttrInt():
    assert hasattr(raas::small::test::FourthLevelClassK, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas::small::test::FourthLevelClassK.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::#11832905_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#11832905)


def test_raas::small::test::#11832905_constructor_exists():
    assert callable(raas::small::test::#11832905.__init__)


def test_raas::small::test::#11832905_constructor_args():
    sig = inspect.signature(raas::small::test::#11832905.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::thirdlevelclassj_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::ThirdLevelClassJ)


def test_raas::small::test::thirdlevelclassj_constructor_exists():
    assert callable(raas::small::test::ThirdLevelClassJ.__init__)


def test_raas::small::test::thirdlevelclassj_constructor_args():
    sig = inspect.signature(raas::small::test::ThirdLevelClassJ.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"

def test_raas::small::test::thirdlevelclassj_has_raasRef():
    assert hasattr(raas::small::test::ThirdLevelClassJ, "raasRef")
    descriptor = None
    for klass in raas::small::test::ThirdLevelClassJ.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::thirdlevelclassj_has_optionalAttrInt():
    assert hasattr(raas::small::test::ThirdLevelClassJ, "optionalAttrInt")
    descriptor = None
    for klass in raas::small::test::ThirdLevelClassJ.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::thirdlevelclassj_has_singleAttrInt():
    assert hasattr(raas::small::test::ThirdLevelClassJ, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::ThirdLevelClassJ.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::thirdlevelclassj_has_multi2lowerAttrInt():
    assert hasattr(raas::small::test::ThirdLevelClassJ, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas::small::test::ThirdLevelClassJ.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::underclassf_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::UnderClassF)


def test_raas::small::test::underclassf_constructor_exists():
    assert callable(raas::small::test::UnderClassF.__init__)


def test_raas::small::test::underclassf_constructor_args():
    sig = inspect.signature(raas::small::test::UnderClassF.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"

def test_raas::small::test::underclassf_has_raasRef():
    assert hasattr(raas::small::test::UnderClassF, "raasRef")
    descriptor = None
    for klass in raas::small::test::UnderClassF.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::underclassf_has_singleAttrInt():
    assert hasattr(raas::small::test::UnderClassF, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::UnderClassF.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::underclasse_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::UnderClassE)


def test_raas::small::test::underclasse_constructor_exists():
    assert callable(raas::small::test::UnderClassE.__init__)


def test_raas::small::test::underclasse_constructor_args():
    sig = inspect.signature(raas::small::test::UnderClassE.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::underclasse_has_raasRef():
    assert hasattr(raas::small::test::UnderClassE, "raasRef")
    descriptor = None
    for klass in raas::small::test::UnderClassE.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::derivedunderclasse1_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::DerivedUnderClassE1)


def test_raas::small::test::derivedunderclasse1_constructor_exists():
    assert callable(raas::small::test::DerivedUnderClassE1.__init__)


def test_raas::small::test::derivedunderclasse1_constructor_args():
    sig = inspect.signature(raas::small::test::DerivedUnderClassE1.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::derivedunderclasse1_has_raasRef():
    assert hasattr(raas::small::test::DerivedUnderClassE1, "raasRef")
    descriptor = None
    for klass in raas::small::test::DerivedUnderClassE1.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::derivedunderclasse2_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::DerivedUnderClassE2)


def test_raas::small::test::derivedunderclasse2_constructor_exists():
    assert callable(raas::small::test::DerivedUnderClassE2.__init__)


def test_raas::small::test::derivedunderclasse2_constructor_args():
    sig = inspect.signature(raas::small::test::DerivedUnderClassE2.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::derivedunderclasse2_has_raasRef():
    assert hasattr(raas::small::test::DerivedUnderClassE2, "raasRef")
    descriptor = None
    for klass in raas::small::test::DerivedUnderClassE2.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::merginge1ande2_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::MergingE1AndE2)


def test_raas::small::test::merginge1ande2_constructor_exists():
    assert callable(raas::small::test::MergingE1AndE2.__init__)


def test_raas::small::test::merginge1ande2_constructor_args():
    sig = inspect.signature(raas::small::test::MergingE1AndE2.__init__)
    params = list(sig.parameters.keys())
    assert "optionalAttrString" in params, "Missing parameter 'optionalAttrString'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::merginge1ande2_has_optionalAttrString():
    assert hasattr(raas::small::test::MergingE1AndE2, "optionalAttrString")
    descriptor = None
    for klass in raas::small::test::MergingE1AndE2.__mro__:
        if "optionalAttrString" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrString"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::merginge1ande2_has_raasRef():
    assert hasattr(raas::small::test::MergingE1AndE2, "raasRef")
    descriptor = None
    for klass in raas::small::test::MergingE1AndE2.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::topclassd_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::TopClassD)


def test_raas::small::test::topclassd_constructor_exists():
    assert callable(raas::small::test::TopClassD.__init__)


def test_raas::small::test::topclassd_constructor_args():
    sig = inspect.signature(raas::small::test::TopClassD.__init__)
    params = list(sig.parameters.keys())
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "optionalTimeZone" in params, "Missing parameter 'optionalTimeZone'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"

def test_raas::small::test::topclassd_has_multi2lowerAttrInt():
    assert hasattr(raas::small::test::TopClassD, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassD.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassd_has_optionalTimeZone():
    assert hasattr(raas::small::test::TopClassD, "optionalTimeZone")
    descriptor = None
    for klass in raas::small::test::TopClassD.__mro__:
        if "optionalTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["optionalTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassd_has_singleAttrInt():
    assert hasattr(raas::small::test::TopClassD, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassD.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassd_has_raasRef():
    assert hasattr(raas::small::test::TopClassD, "raasRef")
    descriptor = None
    for klass in raas::small::test::TopClassD.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassd_has_optionalAttrInt():
    assert hasattr(raas::small::test::TopClassD, "optionalAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassD.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::topclassc_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::TopClassC)


def test_raas::small::test::topclassc_constructor_exists():
    assert callable(raas::small::test::TopClassC.__init__)


def test_raas::small::test::topclassc_constructor_args():
    sig = inspect.signature(raas::small::test::TopClassC.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"

def test_raas::small::test::topclassc_has_singleAttrInt():
    assert hasattr(raas::small::test::TopClassC, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassC.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassc_has_multi2lowerAttrInt():
    assert hasattr(raas::small::test::TopClassC, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassC.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassc_has_raasRef():
    assert hasattr(raas::small::test::TopClassC, "raasRef")
    descriptor = None
    for klass in raas::small::test::TopClassC.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassc_has_optionalAttrInt():
    assert hasattr(raas::small::test::TopClassC, "optionalAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassC.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::topclassb_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::TopClassB)


def test_raas::small::test::topclassb_constructor_exists():
    assert callable(raas::small::test::TopClassB.__init__)


def test_raas::small::test::topclassb_constructor_args():
    sig = inspect.signature(raas::small::test::TopClassB.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"

def test_raas::small::test::topclassb_has_singleAttrInt():
    assert hasattr(raas::small::test::TopClassB, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassB.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassb_has_multi2lowerAttrInt():
    assert hasattr(raas::small::test::TopClassB, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassB.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassb_has_raasRef():
    assert hasattr(raas::small::test::TopClassB, "raasRef")
    descriptor = None
    for klass in raas::small::test::TopClassB.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassb_has_optionalAttrInt():
    assert hasattr(raas::small::test::TopClassB, "optionalAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassB.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::#16551649_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#16551649)


def test_raas::small::test::#16551649_constructor_exists():
    assert callable(raas::small::test::#16551649.__init__)


def test_raas::small::test::#16551649_constructor_args():
    sig = inspect.signature(raas::small::test::#16551649.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::#5656663_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#5656663)


def test_raas::small::test::#5656663_constructor_exists():
    assert callable(raas::small::test::#5656663.__init__)


def test_raas::small::test::#5656663_constructor_args():
    sig = inspect.signature(raas::small::test::#5656663.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::topclassa_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::TopClassA)


def test_raas::small::test::topclassa_constructor_exists():
    assert callable(raas::small::test::TopClassA.__init__)


def test_raas::small::test::topclassa_constructor_args():
    sig = inspect.signature(raas::small::test::TopClassA.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::topclassa_has_raasRef():
    assert hasattr(raas::small::test::TopClassA, "raasRef")
    descriptor = None
    for klass in raas::small::test::TopClassA.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::topclassm_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::TopClassM)


def test_raas::small::test::topclassm_constructor_exists():
    assert callable(raas::small::test::TopClassM.__init__)


def test_raas::small::test::topclassm_constructor_args():
    sig = inspect.signature(raas::small::test::TopClassM.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::topclassm_has_singleAttrInt():
    assert hasattr(raas::small::test::TopClassM, "singleAttrInt")
    descriptor = None
    for klass in raas::small::test::TopClassM.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::topclassm_has_raasRef():
    assert hasattr(raas::small::test::TopClassM, "raasRef")
    descriptor = None
    for klass in raas::small::test::TopClassM.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas::small::test::#7345254_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#7345254)


def test_raas::small::test::#7345254_constructor_exists():
    assert callable(raas::small::test::#7345254.__init__)


def test_raas::small::test::#7345254_constructor_args():
    sig = inspect.signature(raas::small::test::#7345254.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::#19723516_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#19723516)


def test_raas::small::test::#19723516_constructor_exists():
    assert callable(raas::small::test::#19723516.__init__)


def test_raas::small::test::#19723516_constructor_args():
    sig = inspect.signature(raas::small::test::#19723516.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::#29373817_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::#29373817)


def test_raas::small::test::#29373817_constructor_exists():
    assert callable(raas::small::test::#29373817.__init__)


def test_raas::small::test::#29373817_constructor_args():
    sig = inspect.signature(raas::small::test::#29373817.__init__)
    params = list(sig.parameters.keys())



def test_raas::small::test::reposroot_is_not_abstract():
    assert not inspect.isabstract(raas::small::test::ReposRoot)


def test_raas::small::test::reposroot_constructor_exists():
    assert callable(raas::small::test::ReposRoot.__init__)


def test_raas::small::test::reposroot_constructor_args():
    sig = inspect.signature(raas::small::test::ReposRoot.__init__)
    params = list(sig.parameters.keys())
    assert "multiAttrString" in params, "Missing parameter 'multiAttrString'"
    assert "singleAttrString" in params, "Missing parameter 'singleAttrString'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas::small::test::reposroot_has_multiAttrString():
    assert hasattr(raas::small::test::ReposRoot, "multiAttrString")
    descriptor = None
    for klass in raas::small::test::ReposRoot.__mro__:
        if "multiAttrString" in klass.__dict__:
            descriptor = klass.__dict__["multiAttrString"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::reposroot_has_singleAttrString():
    assert hasattr(raas::small::test::ReposRoot, "singleAttrString")
    descriptor = None
    for klass in raas::small::test::ReposRoot.__mro__:
        if "singleAttrString" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrString"]
            break
    assert isinstance(descriptor, property)

def test_raas::small::test::reposroot_has_raasRef():
    assert hasattr(raas::small::test::ReposRoot, "raasRef")
    descriptor = None
    for klass in raas::small::test::ReposRoot.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
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
raas::small::test::#10382437_strategy = st.builds(
    raas::small::test::#10382437,
)
raas::small::test::#30911270_strategy = st.builds(
    raas::small::test::#30911270,
)
raas::small::test::FourthLevelClassK_strategy = st.builds(
    raas::small::test::FourthLevelClassK,
    raasRef=
        safe_text,
    optionalAttrInt=
        st.integers(),
    singleAttrInt=
        st.integers(),
    multi2lowerAttrInt=
        st.integers()
)
raas::small::test::#11832905_strategy = st.builds(
    raas::small::test::#11832905,
)
raas::small::test::ThirdLevelClassJ_strategy = st.builds(
    raas::small::test::ThirdLevelClassJ,
    raasRef=
        safe_text,
    optionalAttrInt=
        st.integers(),
    singleAttrInt=
        st.integers(),
    multi2lowerAttrInt=
        st.integers()
)
raas::small::test::UnderClassF_strategy = st.builds(
    raas::small::test::UnderClassF,
    raasRef=
        safe_text,
    singleAttrInt=
        st.integers()
)
raas::small::test::UnderClassE_strategy = st.builds(
    raas::small::test::UnderClassE,
    raasRef=
        safe_text
)
raas::small::test::DerivedUnderClassE1_strategy = st.builds(
    raas::small::test::DerivedUnderClassE1,
    raasRef=
        safe_text
)
raas::small::test::DerivedUnderClassE2_strategy = st.builds(
    raas::small::test::DerivedUnderClassE2,
    raasRef=
        safe_text
)
raas::small::test::MergingE1AndE2_strategy = st.builds(
    raas::small::test::MergingE1AndE2,
    optionalAttrString=
        safe_text,
    raasRef=
        safe_text
)
raas::small::test::TopClassD_strategy = st.builds(
    raas::small::test::TopClassD,
    multi2lowerAttrInt=
        st.integers(),
    optionalTimeZone=
        safe_text,
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    optionalAttrInt=
        st.integers()
)
raas::small::test::TopClassC_strategy = st.builds(
    raas::small::test::TopClassC,
    singleAttrInt=
        st.integers(),
    multi2lowerAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    optionalAttrInt=
        st.integers()
)
raas::small::test::TopClassB_strategy = st.builds(
    raas::small::test::TopClassB,
    singleAttrInt=
        st.integers(),
    multi2lowerAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    optionalAttrInt=
        st.integers()
)
raas::small::test::#16551649_strategy = st.builds(
    raas::small::test::#16551649,
)
raas::small::test::#5656663_strategy = st.builds(
    raas::small::test::#5656663,
)
raas::small::test::TopClassA_strategy = st.builds(
    raas::small::test::TopClassA,
    raasRef=
        safe_text
)
raas::small::test::TopClassM_strategy = st.builds(
    raas::small::test::TopClassM,
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text
)
raas::small::test::#7345254_strategy = st.builds(
    raas::small::test::#7345254,
)
raas::small::test::#19723516_strategy = st.builds(
    raas::small::test::#19723516,
)
raas::small::test::#29373817_strategy = st.builds(
    raas::small::test::#29373817,
)
raas::small::test::ReposRoot_strategy = st.builds(
    raas::small::test::ReposRoot,
    multiAttrString=
        safe_text,
    singleAttrString=
        safe_text,
    raasRef=
        safe_text
)

@given(instance=raas::small::test::#10382437_strategy)
@settings(max_examples=50)
def test_raas::small::test::#10382437_instantiation(instance):
    assert isinstance(instance, raas::small::test::#10382437)

@given(instance=raas::small::test::#30911270_strategy)
@settings(max_examples=50)
def test_raas::small::test::#30911270_instantiation(instance):
    assert isinstance(instance, raas::small::test::#30911270)

@given(instance=raas::small::test::FourthLevelClassK_strategy)
@settings(max_examples=50)
def test_raas::small::test::fourthlevelclassk_instantiation(instance):
    assert isinstance(instance, raas::small::test::FourthLevelClassK)

@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_optionalAttrInt_type(instance):
    assert isinstance(instance.optionalAttrInt, int)


@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_multi2lowerAttrInt_type(instance):
    assert isinstance(instance.multi2lowerAttrInt, int)


@given(instance=raas::small::test::FourthLevelClassK_strategy)
def test_raas::small::test::fourthlevelclassk_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original

@given(instance=raas::small::test::#11832905_strategy)
@settings(max_examples=50)
def test_raas::small::test::#11832905_instantiation(instance):
    assert isinstance(instance, raas::small::test::#11832905)

@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
@settings(max_examples=50)
def test_raas::small::test::thirdlevelclassj_instantiation(instance):
    assert isinstance(instance, raas::small::test::ThirdLevelClassJ)

@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_optionalAttrInt_type(instance):
    assert isinstance(instance.optionalAttrInt, int)


@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_multi2lowerAttrInt_type(instance):
    assert isinstance(instance.multi2lowerAttrInt, int)


@given(instance=raas::small::test::ThirdLevelClassJ_strategy)
def test_raas::small::test::thirdlevelclassj_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original

@given(instance=raas::small::test::UnderClassF_strategy)
@settings(max_examples=50)
def test_raas::small::test::underclassf_instantiation(instance):
    assert isinstance(instance, raas::small::test::UnderClassF)

@given(instance=raas::small::test::UnderClassF_strategy)
def test_raas::small::test::underclassf_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::UnderClassF_strategy)
def test_raas::small::test::underclassf_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::UnderClassF_strategy)
def test_raas::small::test::underclassf_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::UnderClassF_strategy)
def test_raas::small::test::underclassf_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::UnderClassE_strategy)
@settings(max_examples=50)
def test_raas::small::test::underclasse_instantiation(instance):
    assert isinstance(instance, raas::small::test::UnderClassE)

@given(instance=raas::small::test::UnderClassE_strategy)
def test_raas::small::test::underclasse_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::UnderClassE_strategy)
def test_raas::small::test::underclasse_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::DerivedUnderClassE1_strategy)
@settings(max_examples=50)
def test_raas::small::test::derivedunderclasse1_instantiation(instance):
    assert isinstance(instance, raas::small::test::DerivedUnderClassE1)

@given(instance=raas::small::test::DerivedUnderClassE1_strategy)
def test_raas::small::test::derivedunderclasse1_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::DerivedUnderClassE1_strategy)
def test_raas::small::test::derivedunderclasse1_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::DerivedUnderClassE2_strategy)
@settings(max_examples=50)
def test_raas::small::test::derivedunderclasse2_instantiation(instance):
    assert isinstance(instance, raas::small::test::DerivedUnderClassE2)

@given(instance=raas::small::test::DerivedUnderClassE2_strategy)
def test_raas::small::test::derivedunderclasse2_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::DerivedUnderClassE2_strategy)
def test_raas::small::test::derivedunderclasse2_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::MergingE1AndE2_strategy)
@settings(max_examples=50)
def test_raas::small::test::merginge1ande2_instantiation(instance):
    assert isinstance(instance, raas::small::test::MergingE1AndE2)

@given(instance=raas::small::test::MergingE1AndE2_strategy)
def test_raas::small::test::merginge1ande2_optionalAttrString_type(instance):
    assert isinstance(instance.optionalAttrString, str)


@given(instance=raas::small::test::MergingE1AndE2_strategy)
def test_raas::small::test::merginge1ande2_optionalAttrString_setter(instance):
    original = instance.optionalAttrString
    instance.optionalAttrString = original
    assert instance.optionalAttrString == original

@given(instance=raas::small::test::MergingE1AndE2_strategy)
def test_raas::small::test::merginge1ande2_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::MergingE1AndE2_strategy)
def test_raas::small::test::merginge1ande2_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::TopClassD_strategy)
@settings(max_examples=50)
def test_raas::small::test::topclassd_instantiation(instance):
    assert isinstance(instance, raas::small::test::TopClassD)

@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_multi2lowerAttrInt_type(instance):
    assert isinstance(instance.multi2lowerAttrInt, int)


@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original

@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_optionalTimeZone_type(instance):
    assert isinstance(instance.optionalTimeZone, str)


@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_optionalTimeZone_setter(instance):
    original = instance.optionalTimeZone
    instance.optionalTimeZone = original
    assert instance.optionalTimeZone == original

@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_optionalAttrInt_type(instance):
    assert isinstance(instance.optionalAttrInt, int)


@given(instance=raas::small::test::TopClassD_strategy)
def test_raas::small::test::topclassd_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas::small::test::TopClassC_strategy)
@settings(max_examples=50)
def test_raas::small::test::topclassc_instantiation(instance):
    assert isinstance(instance, raas::small::test::TopClassC)

@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_multi2lowerAttrInt_type(instance):
    assert isinstance(instance.multi2lowerAttrInt, int)


@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original

@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_optionalAttrInt_type(instance):
    assert isinstance(instance.optionalAttrInt, int)


@given(instance=raas::small::test::TopClassC_strategy)
def test_raas::small::test::topclassc_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas::small::test::TopClassB_strategy)
@settings(max_examples=50)
def test_raas::small::test::topclassb_instantiation(instance):
    assert isinstance(instance, raas::small::test::TopClassB)

@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_multi2lowerAttrInt_type(instance):
    assert isinstance(instance.multi2lowerAttrInt, int)


@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original

@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_optionalAttrInt_type(instance):
    assert isinstance(instance.optionalAttrInt, int)


@given(instance=raas::small::test::TopClassB_strategy)
def test_raas::small::test::topclassb_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas::small::test::#16551649_strategy)
@settings(max_examples=50)
def test_raas::small::test::#16551649_instantiation(instance):
    assert isinstance(instance, raas::small::test::#16551649)

@given(instance=raas::small::test::#5656663_strategy)
@settings(max_examples=50)
def test_raas::small::test::#5656663_instantiation(instance):
    assert isinstance(instance, raas::small::test::#5656663)

@given(instance=raas::small::test::TopClassA_strategy)
@settings(max_examples=50)
def test_raas::small::test::topclassa_instantiation(instance):
    assert isinstance(instance, raas::small::test::TopClassA)

@given(instance=raas::small::test::TopClassA_strategy)
def test_raas::small::test::topclassa_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::TopClassA_strategy)
def test_raas::small::test::topclassa_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::TopClassM_strategy)
@settings(max_examples=50)
def test_raas::small::test::topclassm_instantiation(instance):
    assert isinstance(instance, raas::small::test::TopClassM)

@given(instance=raas::small::test::TopClassM_strategy)
def test_raas::small::test::topclassm_singleAttrInt_type(instance):
    assert isinstance(instance.singleAttrInt, int)


@given(instance=raas::small::test::TopClassM_strategy)
def test_raas::small::test::topclassm_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas::small::test::TopClassM_strategy)
def test_raas::small::test::topclassm_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::TopClassM_strategy)
def test_raas::small::test::topclassm_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas::small::test::#7345254_strategy)
@settings(max_examples=50)
def test_raas::small::test::#7345254_instantiation(instance):
    assert isinstance(instance, raas::small::test::#7345254)

@given(instance=raas::small::test::#19723516_strategy)
@settings(max_examples=50)
def test_raas::small::test::#19723516_instantiation(instance):
    assert isinstance(instance, raas::small::test::#19723516)

@given(instance=raas::small::test::#29373817_strategy)
@settings(max_examples=50)
def test_raas::small::test::#29373817_instantiation(instance):
    assert isinstance(instance, raas::small::test::#29373817)

@given(instance=raas::small::test::ReposRoot_strategy)
@settings(max_examples=50)
def test_raas::small::test::reposroot_instantiation(instance):
    assert isinstance(instance, raas::small::test::ReposRoot)

@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_multiAttrString_type(instance):
    assert isinstance(instance.multiAttrString, str)


@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_multiAttrString_setter(instance):
    original = instance.multiAttrString
    instance.multiAttrString = original
    assert instance.multiAttrString == original

@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_singleAttrString_type(instance):
    assert isinstance(instance.singleAttrString, str)


@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_singleAttrString_setter(instance):
    original = instance.singleAttrString
    instance.singleAttrString = original
    assert instance.singleAttrString == original

@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_raasRef_type(instance):
    assert isinstance(instance.raasRef, str)


@given(instance=raas::small::test::ReposRoot_strategy)
def test_raas::small::test::reposroot_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original
