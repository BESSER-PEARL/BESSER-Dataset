import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    raas_small_test_#10382437,
    raas_small_test_#30911270,
    raas_small_test_FourthLevelClassK,
    raas_small_test_#11832905,
    raas_small_test_ThirdLevelClassJ,
    raas_small_test_UnderClassF,
    raas_small_test_UnderClassE,
    raas_small_test_DerivedUnderClassE2,
    raas_small_test_DerivedUnderClassE1,
    raas_small_test_MergingE1AndE2,
    raas_small_test_TopClassD,
    raas_small_test_TopClassC,
    raas_small_test_TopClassB,
    raas_small_test_#16551649,
    raas_small_test_#5656663,
    raas_small_test_TopClassA,
    raas_small_test_TopClassM,
    raas_small_test_#7345254,
    raas_small_test_#19723516,
    raas_small_test_#29373817,
    raas_small_test_ReposRoot,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_raas_small_test_#10382437_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#10382437)


def test_raas_small_test_#10382437_constructor_exists():
    assert callable(raas_small_test_#10382437.__init__)


def test_raas_small_test_#10382437_constructor_args():
    sig = inspect.signature(raas_small_test_#10382437.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_#30911270_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#30911270)


def test_raas_small_test_#30911270_constructor_exists():
    assert callable(raas_small_test_#30911270.__init__)


def test_raas_small_test_#30911270_constructor_args():
    sig = inspect.signature(raas_small_test_#30911270.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_fourthlevelclassk_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_FourthLevelClassK)


def test_raas_small_test_fourthlevelclassk_constructor_exists():
    assert callable(raas_small_test_FourthLevelClassK.__init__)


def test_raas_small_test_fourthlevelclassk_constructor_args():
    sig = inspect.signature(raas_small_test_FourthLevelClassK.__init__)
    params = list(sig.parameters.keys())
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_fourthlevelclassk_has_optionalAttrInt():
    assert hasattr(raas_small_test_FourthLevelClassK, "optionalAttrInt")
    descriptor = None
    for klass in raas_small_test_FourthLevelClassK.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_fourthlevelclassk_has_multi2lowerAttrInt():
    assert hasattr(raas_small_test_FourthLevelClassK, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas_small_test_FourthLevelClassK.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_fourthlevelclassk_has_singleAttrInt():
    assert hasattr(raas_small_test_FourthLevelClassK, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_FourthLevelClassK.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_fourthlevelclassk_has_raasRef():
    assert hasattr(raas_small_test_FourthLevelClassK, "raasRef")
    descriptor = None
    for klass in raas_small_test_FourthLevelClassK.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_#11832905_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#11832905)


def test_raas_small_test_#11832905_constructor_exists():
    assert callable(raas_small_test_#11832905.__init__)


def test_raas_small_test_#11832905_constructor_args():
    sig = inspect.signature(raas_small_test_#11832905.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_thirdlevelclassj_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_ThirdLevelClassJ)


def test_raas_small_test_thirdlevelclassj_constructor_exists():
    assert callable(raas_small_test_ThirdLevelClassJ.__init__)


def test_raas_small_test_thirdlevelclassj_constructor_args():
    sig = inspect.signature(raas_small_test_ThirdLevelClassJ.__init__)
    params = list(sig.parameters.keys())
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"

def test_raas_small_test_thirdlevelclassj_has_optionalAttrInt():
    assert hasattr(raas_small_test_ThirdLevelClassJ, "optionalAttrInt")
    descriptor = None
    for klass in raas_small_test_ThirdLevelClassJ.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_thirdlevelclassj_has_raasRef():
    assert hasattr(raas_small_test_ThirdLevelClassJ, "raasRef")
    descriptor = None
    for klass in raas_small_test_ThirdLevelClassJ.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_thirdlevelclassj_has_multi2lowerAttrInt():
    assert hasattr(raas_small_test_ThirdLevelClassJ, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas_small_test_ThirdLevelClassJ.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_thirdlevelclassj_has_singleAttrInt():
    assert hasattr(raas_small_test_ThirdLevelClassJ, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_ThirdLevelClassJ.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_underclassf_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_UnderClassF)


def test_raas_small_test_underclassf_constructor_exists():
    assert callable(raas_small_test_UnderClassF.__init__)


def test_raas_small_test_underclassf_constructor_args():
    sig = inspect.signature(raas_small_test_UnderClassF.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_underclassf_has_singleAttrInt():
    assert hasattr(raas_small_test_UnderClassF, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_UnderClassF.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_underclassf_has_raasRef():
    assert hasattr(raas_small_test_UnderClassF, "raasRef")
    descriptor = None
    for klass in raas_small_test_UnderClassF.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_underclasse_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_UnderClassE)


def test_raas_small_test_underclasse_constructor_exists():
    assert callable(raas_small_test_UnderClassE.__init__)


def test_raas_small_test_underclasse_constructor_args():
    sig = inspect.signature(raas_small_test_UnderClassE.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_underclasse_has_raasRef():
    assert hasattr(raas_small_test_UnderClassE, "raasRef")
    descriptor = None
    for klass in raas_small_test_UnderClassE.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_derivedunderclasse2_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_DerivedUnderClassE2)


def test_raas_small_test_derivedunderclasse2_constructor_exists():
    assert callable(raas_small_test_DerivedUnderClassE2.__init__)


def test_raas_small_test_derivedunderclasse2_constructor_args():
    sig = inspect.signature(raas_small_test_DerivedUnderClassE2.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_derivedunderclasse2_has_raasRef():
    assert hasattr(raas_small_test_DerivedUnderClassE2, "raasRef")
    descriptor = None
    for klass in raas_small_test_DerivedUnderClassE2.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_derivedunderclasse1_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_DerivedUnderClassE1)


def test_raas_small_test_derivedunderclasse1_constructor_exists():
    assert callable(raas_small_test_DerivedUnderClassE1.__init__)


def test_raas_small_test_derivedunderclasse1_constructor_args():
    sig = inspect.signature(raas_small_test_DerivedUnderClassE1.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_derivedunderclasse1_has_raasRef():
    assert hasattr(raas_small_test_DerivedUnderClassE1, "raasRef")
    descriptor = None
    for klass in raas_small_test_DerivedUnderClassE1.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_merginge1ande2_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_MergingE1AndE2)


def test_raas_small_test_merginge1ande2_constructor_exists():
    assert callable(raas_small_test_MergingE1AndE2.__init__)


def test_raas_small_test_merginge1ande2_constructor_args():
    sig = inspect.signature(raas_small_test_MergingE1AndE2.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalAttrString" in params, "Missing parameter 'optionalAttrString'"

def test_raas_small_test_merginge1ande2_has_raasRef():
    assert hasattr(raas_small_test_MergingE1AndE2, "raasRef")
    descriptor = None
    for klass in raas_small_test_MergingE1AndE2.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_merginge1ande2_has_optionalAttrString():
    assert hasattr(raas_small_test_MergingE1AndE2, "optionalAttrString")
    descriptor = None
    for klass in raas_small_test_MergingE1AndE2.__mro__:
        if "optionalAttrString" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrString"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_topclassd_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_TopClassD)


def test_raas_small_test_topclassd_constructor_exists():
    assert callable(raas_small_test_TopClassD.__init__)


def test_raas_small_test_topclassd_constructor_args():
    sig = inspect.signature(raas_small_test_TopClassD.__init__)
    params = list(sig.parameters.keys())
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "optionalTimeZone" in params, "Missing parameter 'optionalTimeZone'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"

def test_raas_small_test_topclassd_has_multi2lowerAttrInt():
    assert hasattr(raas_small_test_TopClassD, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassD.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassd_has_optionalAttrInt():
    assert hasattr(raas_small_test_TopClassD, "optionalAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassD.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassd_has_raasRef():
    assert hasattr(raas_small_test_TopClassD, "raasRef")
    descriptor = None
    for klass in raas_small_test_TopClassD.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassd_has_optionalTimeZone():
    assert hasattr(raas_small_test_TopClassD, "optionalTimeZone")
    descriptor = None
    for klass in raas_small_test_TopClassD.__mro__:
        if "optionalTimeZone" in klass.__dict__:
            descriptor = klass.__dict__["optionalTimeZone"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassd_has_singleAttrInt():
    assert hasattr(raas_small_test_TopClassD, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassD.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_topclassc_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_TopClassC)


def test_raas_small_test_topclassc_constructor_exists():
    assert callable(raas_small_test_TopClassC.__init__)


def test_raas_small_test_topclassc_constructor_args():
    sig = inspect.signature(raas_small_test_TopClassC.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"

def test_raas_small_test_topclassc_has_singleAttrInt():
    assert hasattr(raas_small_test_TopClassC, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassC.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassc_has_raasRef():
    assert hasattr(raas_small_test_TopClassC, "raasRef")
    descriptor = None
    for klass in raas_small_test_TopClassC.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassc_has_multi2lowerAttrInt():
    assert hasattr(raas_small_test_TopClassC, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassC.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassc_has_optionalAttrInt():
    assert hasattr(raas_small_test_TopClassC, "optionalAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassC.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_topclassb_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_TopClassB)


def test_raas_small_test_topclassb_constructor_exists():
    assert callable(raas_small_test_TopClassB.__init__)


def test_raas_small_test_topclassb_constructor_args():
    sig = inspect.signature(raas_small_test_TopClassB.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "multi2lowerAttrInt" in params, "Missing parameter 'multi2lowerAttrInt'"
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "optionalAttrInt" in params, "Missing parameter 'optionalAttrInt'"

def test_raas_small_test_topclassb_has_raasRef():
    assert hasattr(raas_small_test_TopClassB, "raasRef")
    descriptor = None
    for klass in raas_small_test_TopClassB.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassb_has_multi2lowerAttrInt():
    assert hasattr(raas_small_test_TopClassB, "multi2lowerAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassB.__mro__:
        if "multi2lowerAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["multi2lowerAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassb_has_singleAttrInt():
    assert hasattr(raas_small_test_TopClassB, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassB.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassb_has_optionalAttrInt():
    assert hasattr(raas_small_test_TopClassB, "optionalAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassB.__mro__:
        if "optionalAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["optionalAttrInt"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_#16551649_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#16551649)


def test_raas_small_test_#16551649_constructor_exists():
    assert callable(raas_small_test_#16551649.__init__)


def test_raas_small_test_#16551649_constructor_args():
    sig = inspect.signature(raas_small_test_#16551649.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_#5656663_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#5656663)


def test_raas_small_test_#5656663_constructor_exists():
    assert callable(raas_small_test_#5656663.__init__)


def test_raas_small_test_#5656663_constructor_args():
    sig = inspect.signature(raas_small_test_#5656663.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_topclassa_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_TopClassA)


def test_raas_small_test_topclassa_constructor_exists():
    assert callable(raas_small_test_TopClassA.__init__)


def test_raas_small_test_topclassa_constructor_args():
    sig = inspect.signature(raas_small_test_TopClassA.__init__)
    params = list(sig.parameters.keys())
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_topclassa_has_raasRef():
    assert hasattr(raas_small_test_TopClassA, "raasRef")
    descriptor = None
    for klass in raas_small_test_TopClassA.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_topclassm_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_TopClassM)


def test_raas_small_test_topclassm_constructor_exists():
    assert callable(raas_small_test_TopClassM.__init__)


def test_raas_small_test_topclassm_constructor_args():
    sig = inspect.signature(raas_small_test_TopClassM.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrInt" in params, "Missing parameter 'singleAttrInt'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"

def test_raas_small_test_topclassm_has_singleAttrInt():
    assert hasattr(raas_small_test_TopClassM, "singleAttrInt")
    descriptor = None
    for klass in raas_small_test_TopClassM.__mro__:
        if "singleAttrInt" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrInt"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_topclassm_has_raasRef():
    assert hasattr(raas_small_test_TopClassM, "raasRef")
    descriptor = None
    for klass in raas_small_test_TopClassM.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)



def test_raas_small_test_#7345254_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#7345254)


def test_raas_small_test_#7345254_constructor_exists():
    assert callable(raas_small_test_#7345254.__init__)


def test_raas_small_test_#7345254_constructor_args():
    sig = inspect.signature(raas_small_test_#7345254.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_#19723516_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#19723516)


def test_raas_small_test_#19723516_constructor_exists():
    assert callable(raas_small_test_#19723516.__init__)


def test_raas_small_test_#19723516_constructor_args():
    sig = inspect.signature(raas_small_test_#19723516.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_#29373817_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_#29373817)


def test_raas_small_test_#29373817_constructor_exists():
    assert callable(raas_small_test_#29373817.__init__)


def test_raas_small_test_#29373817_constructor_args():
    sig = inspect.signature(raas_small_test_#29373817.__init__)
    params = list(sig.parameters.keys())



def test_raas_small_test_reposroot_is_not_abstract():
    assert not inspect.isabstract(raas_small_test_ReposRoot)


def test_raas_small_test_reposroot_constructor_exists():
    assert callable(raas_small_test_ReposRoot.__init__)


def test_raas_small_test_reposroot_constructor_args():
    sig = inspect.signature(raas_small_test_ReposRoot.__init__)
    params = list(sig.parameters.keys())
    assert "singleAttrString" in params, "Missing parameter 'singleAttrString'"
    assert "raasRef" in params, "Missing parameter 'raasRef'"
    assert "multiAttrString" in params, "Missing parameter 'multiAttrString'"

def test_raas_small_test_reposroot_has_singleAttrString():
    assert hasattr(raas_small_test_ReposRoot, "singleAttrString")
    descriptor = None
    for klass in raas_small_test_ReposRoot.__mro__:
        if "singleAttrString" in klass.__dict__:
            descriptor = klass.__dict__["singleAttrString"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_reposroot_has_raasRef():
    assert hasattr(raas_small_test_ReposRoot, "raasRef")
    descriptor = None
    for klass in raas_small_test_ReposRoot.__mro__:
        if "raasRef" in klass.__dict__:
            descriptor = klass.__dict__["raasRef"]
            break
    assert isinstance(descriptor, property)

def test_raas_small_test_reposroot_has_multiAttrString():
    assert hasattr(raas_small_test_ReposRoot, "multiAttrString")
    descriptor = None
    for klass in raas_small_test_ReposRoot.__mro__:
        if "multiAttrString" in klass.__dict__:
            descriptor = klass.__dict__["multiAttrString"]
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
raas_small_test_#10382437_strategy = st.builds(
    raas_small_test_#10382437,
)
raas_small_test_#30911270_strategy = st.builds(
    raas_small_test_#30911270,
)
raas_small_test_FourthLevelClassK_strategy = st.builds(
    raas_small_test_FourthLevelClassK,
    optionalAttrInt=
        st.integers(),
    multi2lowerAttrInt=
        st.integers(),
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text
)
raas_small_test_#11832905_strategy = st.builds(
    raas_small_test_#11832905,
)
raas_small_test_ThirdLevelClassJ_strategy = st.builds(
    raas_small_test_ThirdLevelClassJ,
    optionalAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    multi2lowerAttrInt=
        st.integers(),
    singleAttrInt=
        st.integers()
)
raas_small_test_UnderClassF_strategy = st.builds(
    raas_small_test_UnderClassF,
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text
)
raas_small_test_UnderClassE_strategy = st.builds(
    raas_small_test_UnderClassE,
    raasRef=
        safe_text
)
raas_small_test_DerivedUnderClassE2_strategy = st.builds(
    raas_small_test_DerivedUnderClassE2,
    raasRef=
        safe_text
)
raas_small_test_DerivedUnderClassE1_strategy = st.builds(
    raas_small_test_DerivedUnderClassE1,
    raasRef=
        safe_text
)
raas_small_test_MergingE1AndE2_strategy = st.builds(
    raas_small_test_MergingE1AndE2,
    raasRef=
        safe_text,
    optionalAttrString=
        safe_text
)
raas_small_test_TopClassD_strategy = st.builds(
    raas_small_test_TopClassD,
    multi2lowerAttrInt=
        st.integers(),
    optionalAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    optionalTimeZone=
        safe_text,
    singleAttrInt=
        st.integers()
)
raas_small_test_TopClassC_strategy = st.builds(
    raas_small_test_TopClassC,
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text,
    multi2lowerAttrInt=
        st.integers(),
    optionalAttrInt=
        st.integers()
)
raas_small_test_TopClassB_strategy = st.builds(
    raas_small_test_TopClassB,
    raasRef=
        safe_text,
    multi2lowerAttrInt=
        st.integers(),
    singleAttrInt=
        st.integers(),
    optionalAttrInt=
        st.integers()
)
raas_small_test_#16551649_strategy = st.builds(
    raas_small_test_#16551649,
)
raas_small_test_#5656663_strategy = st.builds(
    raas_small_test_#5656663,
)
raas_small_test_TopClassA_strategy = st.builds(
    raas_small_test_TopClassA,
    raasRef=
        safe_text
)
raas_small_test_TopClassM_strategy = st.builds(
    raas_small_test_TopClassM,
    singleAttrInt=
        st.integers(),
    raasRef=
        safe_text
)
raas_small_test_#7345254_strategy = st.builds(
    raas_small_test_#7345254,
)
raas_small_test_#19723516_strategy = st.builds(
    raas_small_test_#19723516,
)
raas_small_test_#29373817_strategy = st.builds(
    raas_small_test_#29373817,
)
raas_small_test_ReposRoot_strategy = st.builds(
    raas_small_test_ReposRoot,
    singleAttrString=
        safe_text,
    raasRef=
        safe_text,
    multiAttrString=
        safe_text
)

@given(instance=raas_small_test_#10382437_strategy)
@settings(max_examples=50)
def test_raas_small_test_#10382437_instantiation(instance):
    assert isinstance(instance, raas_small_test_#10382437)

@given(instance=raas_small_test_#30911270_strategy)
@settings(max_examples=50)
def test_raas_small_test_#30911270_instantiation(instance):
    assert isinstance(instance, raas_small_test_#30911270)

@given(instance=raas_small_test_FourthLevelClassK_strategy)
@settings(max_examples=50)
def test_raas_small_test_fourthlevelclassk_instantiation(instance):
    assert isinstance(instance, raas_small_test_FourthLevelClassK)



@given(instance=raas_small_test_FourthLevelClassK_strategy)
def test_raas_small_test_fourthlevelclassk_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original



@given(instance=raas_small_test_FourthLevelClassK_strategy)
def test_raas_small_test_fourthlevelclassk_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original



@given(instance=raas_small_test_FourthLevelClassK_strategy)
def test_raas_small_test_fourthlevelclassk_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original



@given(instance=raas_small_test_FourthLevelClassK_strategy)
def test_raas_small_test_fourthlevelclassk_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_#11832905_strategy)
@settings(max_examples=50)
def test_raas_small_test_#11832905_instantiation(instance):
    assert isinstance(instance, raas_small_test_#11832905)

@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
@settings(max_examples=50)
def test_raas_small_test_thirdlevelclassj_instantiation(instance):
    assert isinstance(instance, raas_small_test_ThirdLevelClassJ)



@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
def test_raas_small_test_thirdlevelclassj_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original



@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
def test_raas_small_test_thirdlevelclassj_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
def test_raas_small_test_thirdlevelclassj_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original



@given(instance=raas_small_test_ThirdLevelClassJ_strategy)
def test_raas_small_test_thirdlevelclassj_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas_small_test_UnderClassF_strategy)
@settings(max_examples=50)
def test_raas_small_test_underclassf_instantiation(instance):
    assert isinstance(instance, raas_small_test_UnderClassF)



@given(instance=raas_small_test_UnderClassF_strategy)
def test_raas_small_test_underclassf_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original



@given(instance=raas_small_test_UnderClassF_strategy)
def test_raas_small_test_underclassf_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_UnderClassE_strategy)
@settings(max_examples=50)
def test_raas_small_test_underclasse_instantiation(instance):
    assert isinstance(instance, raas_small_test_UnderClassE)



@given(instance=raas_small_test_UnderClassE_strategy)
def test_raas_small_test_underclasse_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_DerivedUnderClassE2_strategy)
@settings(max_examples=50)
def test_raas_small_test_derivedunderclasse2_instantiation(instance):
    assert isinstance(instance, raas_small_test_DerivedUnderClassE2)



@given(instance=raas_small_test_DerivedUnderClassE2_strategy)
def test_raas_small_test_derivedunderclasse2_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_DerivedUnderClassE1_strategy)
@settings(max_examples=50)
def test_raas_small_test_derivedunderclasse1_instantiation(instance):
    assert isinstance(instance, raas_small_test_DerivedUnderClassE1)



@given(instance=raas_small_test_DerivedUnderClassE1_strategy)
def test_raas_small_test_derivedunderclasse1_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_MergingE1AndE2_strategy)
@settings(max_examples=50)
def test_raas_small_test_merginge1ande2_instantiation(instance):
    assert isinstance(instance, raas_small_test_MergingE1AndE2)



@given(instance=raas_small_test_MergingE1AndE2_strategy)
def test_raas_small_test_merginge1ande2_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_MergingE1AndE2_strategy)
def test_raas_small_test_merginge1ande2_optionalAttrString_setter(instance):
    original = instance.optionalAttrString
    instance.optionalAttrString = original
    assert instance.optionalAttrString == original

@given(instance=raas_small_test_TopClassD_strategy)
@settings(max_examples=50)
def test_raas_small_test_topclassd_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassD)



@given(instance=raas_small_test_TopClassD_strategy)
def test_raas_small_test_topclassd_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original



@given(instance=raas_small_test_TopClassD_strategy)
def test_raas_small_test_topclassd_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original



@given(instance=raas_small_test_TopClassD_strategy)
def test_raas_small_test_topclassd_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_TopClassD_strategy)
def test_raas_small_test_topclassd_optionalTimeZone_setter(instance):
    original = instance.optionalTimeZone
    instance.optionalTimeZone = original
    assert instance.optionalTimeZone == original



@given(instance=raas_small_test_TopClassD_strategy)
def test_raas_small_test_topclassd_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original

@given(instance=raas_small_test_TopClassC_strategy)
@settings(max_examples=50)
def test_raas_small_test_topclassc_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassC)



@given(instance=raas_small_test_TopClassC_strategy)
def test_raas_small_test_topclassc_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original



@given(instance=raas_small_test_TopClassC_strategy)
def test_raas_small_test_topclassc_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_TopClassC_strategy)
def test_raas_small_test_topclassc_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original



@given(instance=raas_small_test_TopClassC_strategy)
def test_raas_small_test_topclassc_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas_small_test_TopClassB_strategy)
@settings(max_examples=50)
def test_raas_small_test_topclassb_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassB)



@given(instance=raas_small_test_TopClassB_strategy)
def test_raas_small_test_topclassb_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_TopClassB_strategy)
def test_raas_small_test_topclassb_multi2lowerAttrInt_setter(instance):
    original = instance.multi2lowerAttrInt
    instance.multi2lowerAttrInt = original
    assert instance.multi2lowerAttrInt == original



@given(instance=raas_small_test_TopClassB_strategy)
def test_raas_small_test_topclassb_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original



@given(instance=raas_small_test_TopClassB_strategy)
def test_raas_small_test_topclassb_optionalAttrInt_setter(instance):
    original = instance.optionalAttrInt
    instance.optionalAttrInt = original
    assert instance.optionalAttrInt == original

@given(instance=raas_small_test_#16551649_strategy)
@settings(max_examples=50)
def test_raas_small_test_#16551649_instantiation(instance):
    assert isinstance(instance, raas_small_test_#16551649)

@given(instance=raas_small_test_#5656663_strategy)
@settings(max_examples=50)
def test_raas_small_test_#5656663_instantiation(instance):
    assert isinstance(instance, raas_small_test_#5656663)

@given(instance=raas_small_test_TopClassA_strategy)
@settings(max_examples=50)
def test_raas_small_test_topclassa_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassA)



@given(instance=raas_small_test_TopClassA_strategy)
def test_raas_small_test_topclassa_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_TopClassM_strategy)
@settings(max_examples=50)
def test_raas_small_test_topclassm_instantiation(instance):
    assert isinstance(instance, raas_small_test_TopClassM)



@given(instance=raas_small_test_TopClassM_strategy)
def test_raas_small_test_topclassm_singleAttrInt_setter(instance):
    original = instance.singleAttrInt
    instance.singleAttrInt = original
    assert instance.singleAttrInt == original



@given(instance=raas_small_test_TopClassM_strategy)
def test_raas_small_test_topclassm_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original

@given(instance=raas_small_test_#7345254_strategy)
@settings(max_examples=50)
def test_raas_small_test_#7345254_instantiation(instance):
    assert isinstance(instance, raas_small_test_#7345254)

@given(instance=raas_small_test_#19723516_strategy)
@settings(max_examples=50)
def test_raas_small_test_#19723516_instantiation(instance):
    assert isinstance(instance, raas_small_test_#19723516)

@given(instance=raas_small_test_#29373817_strategy)
@settings(max_examples=50)
def test_raas_small_test_#29373817_instantiation(instance):
    assert isinstance(instance, raas_small_test_#29373817)

@given(instance=raas_small_test_ReposRoot_strategy)
@settings(max_examples=50)
def test_raas_small_test_reposroot_instantiation(instance):
    assert isinstance(instance, raas_small_test_ReposRoot)



@given(instance=raas_small_test_ReposRoot_strategy)
def test_raas_small_test_reposroot_singleAttrString_setter(instance):
    original = instance.singleAttrString
    instance.singleAttrString = original
    assert instance.singleAttrString == original



@given(instance=raas_small_test_ReposRoot_strategy)
def test_raas_small_test_reposroot_raasRef_setter(instance):
    original = instance.raasRef
    instance.raasRef = original
    assert instance.raasRef == original



@given(instance=raas_small_test_ReposRoot_strategy)
def test_raas_small_test_reposroot_multiAttrString_setter(instance):
    original = instance.multiAttrString
    instance.multiAttrString = original
    assert instance.multiAttrString == original
