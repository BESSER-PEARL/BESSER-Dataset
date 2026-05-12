import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Exception,
    ClassV,
    ClassU,
    ClassT,
    ClassS,
    ClassR,
    ClassQ,
    InterfaceO_Interface,
    ClassP,
    ClassN,
    ClassM,
    ClassG,
    ClassF,
    ClassE,
    ClassD,
    ErrorCode,
    ErrorCodeException,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exception_is_not_abstract():
    assert not inspect.isabstract(Exception)


def test_exception_constructor_exists():
    assert callable(Exception.__init__)


def test_exception_constructor_args():
    sig = inspect.signature(Exception.__init__)
    params = list(sig.parameters.keys())



def test_classv_is_not_abstract():
    assert not inspect.isabstract(ClassV)


def test_classv_constructor_exists():
    assert callable(ClassV.__init__)


def test_classv_constructor_args():
    sig = inspect.signature(ClassV.__init__)
    params = list(sig.parameters.keys())



def test_classu_is_not_abstract():
    assert not inspect.isabstract(ClassU)


def test_classu_constructor_exists():
    assert callable(ClassU.__init__)


def test_classu_constructor_args():
    sig = inspect.signature(ClassU.__init__)
    params = list(sig.parameters.keys())



def test_classt_is_not_abstract():
    assert not inspect.isabstract(ClassT)


def test_classt_constructor_exists():
    assert callable(ClassT.__init__)


def test_classt_constructor_args():
    sig = inspect.signature(ClassT.__init__)
    params = list(sig.parameters.keys())



def test_classs_is_not_abstract():
    assert not inspect.isabstract(ClassS)


def test_classs_constructor_exists():
    assert callable(ClassS.__init__)


def test_classs_constructor_args():
    sig = inspect.signature(ClassS.__init__)
    params = list(sig.parameters.keys())



def test_classr_is_not_abstract():
    assert not inspect.isabstract(ClassR)


def test_classr_constructor_exists():
    assert callable(ClassR.__init__)


def test_classr_constructor_args():
    sig = inspect.signature(ClassR.__init__)
    params = list(sig.parameters.keys())



def test_classq_is_not_abstract():
    assert not inspect.isabstract(ClassQ)


def test_classq_constructor_exists():
    assert callable(ClassQ.__init__)


def test_classq_constructor_args():
    sig = inspect.signature(ClassQ.__init__)
    params = list(sig.parameters.keys())



def test_interfaceo_interface_is_not_abstract():
    assert not inspect.isabstract(InterfaceO_Interface)


def test_interfaceo_interface_constructor_exists():
    assert callable(InterfaceO_Interface.__init__)


def test_interfaceo_interface_constructor_args():
    sig = inspect.signature(InterfaceO_Interface.__init__)
    params = list(sig.parameters.keys())



def test_classp_is_not_abstract():
    assert not inspect.isabstract(ClassP)


def test_classp_constructor_exists():
    assert callable(ClassP.__init__)


def test_classp_constructor_args():
    sig = inspect.signature(ClassP.__init__)
    params = list(sig.parameters.keys())



def test_classn_is_not_abstract():
    assert not inspect.isabstract(ClassN)


def test_classn_constructor_exists():
    assert callable(ClassN.__init__)


def test_classn_constructor_args():
    sig = inspect.signature(ClassN.__init__)
    params = list(sig.parameters.keys())



def test_classm_is_not_abstract():
    assert not inspect.isabstract(ClassM)


def test_classm_constructor_exists():
    assert callable(ClassM.__init__)


def test_classm_constructor_args():
    sig = inspect.signature(ClassM.__init__)
    params = list(sig.parameters.keys())



def test_classg_is_not_abstract():
    assert not inspect.isabstract(ClassG)


def test_classg_constructor_exists():
    assert callable(ClassG.__init__)


def test_classg_constructor_args():
    sig = inspect.signature(ClassG.__init__)
    params = list(sig.parameters.keys())



def test_classf_is_not_abstract():
    assert not inspect.isabstract(ClassF)


def test_classf_constructor_exists():
    assert callable(ClassF.__init__)


def test_classf_constructor_args():
    sig = inspect.signature(ClassF.__init__)
    params = list(sig.parameters.keys())



def test_classe_is_not_abstract():
    assert not inspect.isabstract(ClassE)


def test_classe_constructor_exists():
    assert callable(ClassE.__init__)


def test_classe_constructor_args():
    sig = inspect.signature(ClassE.__init__)
    params = list(sig.parameters.keys())



def test_classd_is_not_abstract():
    assert not inspect.isabstract(ClassD)


def test_classd_constructor_exists():
    assert callable(ClassD.__init__)


def test_classd_constructor_args():
    sig = inspect.signature(ClassD.__init__)
    params = list(sig.parameters.keys())



def test_errorcode_is_not_abstract():
    assert not inspect.isabstract(ErrorCode)


def test_errorcode_constructor_exists():
    assert callable(ErrorCode.__init__)


def test_errorcode_constructor_args():
    sig = inspect.signature(ErrorCode.__init__)
    params = list(sig.parameters.keys())
    assert "domain" in params, "Missing parameter 'domain'"
    assert "subdomain" in params, "Missing parameter 'subdomain'"
    assert "tier" in params, "Missing parameter 'tier'"
    assert "reason" in params, "Missing parameter 'reason'"

def test_errorcode_has_domain():
    assert hasattr(ErrorCode, "domain")
    descriptor = None
    for klass in ErrorCode.__mro__:
        if "domain" in klass.__dict__:
            descriptor = klass.__dict__["domain"]
            break
    assert isinstance(descriptor, property)

def test_errorcode_has_subdomain():
    assert hasattr(ErrorCode, "subdomain")
    descriptor = None
    for klass in ErrorCode.__mro__:
        if "subdomain" in klass.__dict__:
            descriptor = klass.__dict__["subdomain"]
            break
    assert isinstance(descriptor, property)

def test_errorcode_has_tier():
    assert hasattr(ErrorCode, "tier")
    descriptor = None
    for klass in ErrorCode.__mro__:
        if "tier" in klass.__dict__:
            descriptor = klass.__dict__["tier"]
            break
    assert isinstance(descriptor, property)

def test_errorcode_has_reason():
    assert hasattr(ErrorCode, "reason")
    descriptor = None
    for klass in ErrorCode.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)



def test_errorcodeexception_is_not_abstract():
    assert not inspect.isabstract(ErrorCodeException)


def test_errorcodeexception_constructor_exists():
    assert callable(ErrorCodeException.__init__)


def test_errorcodeexception_constructor_args():
    sig = inspect.signature(ErrorCodeException.__init__)
    params = list(sig.parameters.keys())
    assert "errorCode" in params, "Missing parameter 'errorCode'"
    assert "throwable" in params, "Missing parameter 'throwable'"
    assert "errorCodeMessage" in params, "Missing parameter 'errorCodeMessage'"

def test_errorcodeexception_has_errorCode():
    assert hasattr(ErrorCodeException, "errorCode")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)

def test_errorcodeexception_has_throwable():
    assert hasattr(ErrorCodeException, "throwable")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "throwable" in klass.__dict__:
            descriptor = klass.__dict__["throwable"]
            break
    assert isinstance(descriptor, property)

def test_errorcodeexception_has_errorCodeMessage():
    assert hasattr(ErrorCodeException, "errorCodeMessage")
    descriptor = None
    for klass in ErrorCodeException.__mro__:
        if "errorCodeMessage" in klass.__dict__:
            descriptor = klass.__dict__["errorCodeMessage"]
            break
    assert isinstance(descriptor, property)



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "ownerName" in params, "Missing parameter 'ownerName'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_bankaccount_has_ownerName():
    assert hasattr(BankAccount, "ownerName")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "ownerName" in klass.__dict__:
            descriptor = klass.__dict__["ownerName"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_balance():
    assert hasattr(BankAccount, "balance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
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
Exception_strategy = st.builds(
    Exception,
)
ClassV_strategy = st.builds(
    ClassV,
)
ClassU_strategy = st.builds(
    ClassU,
)
ClassT_strategy = st.builds(
    ClassT,
)
ClassS_strategy = st.builds(
    ClassS,
)
ClassR_strategy = st.builds(
    ClassR,
)
ClassQ_strategy = st.builds(
    ClassQ,
)
InterfaceO_Interface_strategy = st.builds(
    InterfaceO_Interface,
)
ClassP_strategy = st.builds(
    ClassP,
)
ClassN_strategy = st.builds(
    ClassN,
)
ClassM_strategy = st.builds(
    ClassM,
)
ClassG_strategy = st.builds(
    ClassG,
)
ClassF_strategy = st.builds(
    ClassF,
)
ClassE_strategy = st.builds(
    ClassE,
)
ClassD_strategy = st.builds(
    ClassD,
)
ErrorCode_strategy = st.builds(
    ErrorCode,
    domain=
        st.integers(),
    subdomain=
        st.integers(),
    tier=
        st.integers(),
    reason=
        st.integers()
)
ErrorCodeException_strategy = st.builds(
    ErrorCodeException,
    errorCode=
        st.none(),
    throwable=
        safe_text,
    errorCodeMessage=
        safe_text
)
BankAccount_strategy = st.builds(
    BankAccount,
    ownerName=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=Exception_strategy)
@settings(max_examples=50)
def test_exception_instantiation(instance):
    assert isinstance(instance, Exception)

@given(instance=ClassV_strategy)
@settings(max_examples=50)
def test_classv_instantiation(instance):
    assert isinstance(instance, ClassV)

@given(instance=ClassU_strategy)
@settings(max_examples=50)
def test_classu_instantiation(instance):
    assert isinstance(instance, ClassU)

@given(instance=ClassT_strategy)
@settings(max_examples=50)
def test_classt_instantiation(instance):
    assert isinstance(instance, ClassT)

@given(instance=ClassS_strategy)
@settings(max_examples=50)
def test_classs_instantiation(instance):
    assert isinstance(instance, ClassS)

@given(instance=ClassR_strategy)
@settings(max_examples=50)
def test_classr_instantiation(instance):
    assert isinstance(instance, ClassR)

@given(instance=ClassQ_strategy)
@settings(max_examples=50)
def test_classq_instantiation(instance):
    assert isinstance(instance, ClassQ)

@given(instance=InterfaceO_Interface_strategy)
@settings(max_examples=50)
def test_interfaceo_interface_instantiation(instance):
    assert isinstance(instance, InterfaceO_Interface)

@given(instance=ClassP_strategy)
@settings(max_examples=50)
def test_classp_instantiation(instance):
    assert isinstance(instance, ClassP)

@given(instance=ClassN_strategy)
@settings(max_examples=50)
def test_classn_instantiation(instance):
    assert isinstance(instance, ClassN)

@given(instance=ClassM_strategy)
@settings(max_examples=50)
def test_classm_instantiation(instance):
    assert isinstance(instance, ClassM)

@given(instance=ClassG_strategy)
@settings(max_examples=50)
def test_classg_instantiation(instance):
    assert isinstance(instance, ClassG)

@given(instance=ClassF_strategy)
@settings(max_examples=50)
def test_classf_instantiation(instance):
    assert isinstance(instance, ClassF)

@given(instance=ClassE_strategy)
@settings(max_examples=50)
def test_classe_instantiation(instance):
    assert isinstance(instance, ClassE)

@given(instance=ClassD_strategy)
@settings(max_examples=50)
def test_classd_instantiation(instance):
    assert isinstance(instance, ClassD)

@given(instance=ErrorCode_strategy)
@settings(max_examples=50)
def test_errorcode_instantiation(instance):
    assert isinstance(instance, ErrorCode)



@given(instance=ErrorCode_strategy)
def test_errorcode_domain_setter(instance):
    original = instance.domain
    instance.domain = original
    assert instance.domain == original



@given(instance=ErrorCode_strategy)
def test_errorcode_subdomain_setter(instance):
    original = instance.subdomain
    instance.subdomain = original
    assert instance.subdomain == original



@given(instance=ErrorCode_strategy)
def test_errorcode_tier_setter(instance):
    original = instance.tier
    instance.tier = original
    assert instance.tier == original



@given(instance=ErrorCode_strategy)
def test_errorcode_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=ErrorCodeException_strategy)
@settings(max_examples=50)
def test_errorcodeexception_instantiation(instance):
    assert isinstance(instance, ErrorCodeException)



@given(instance=ErrorCodeException_strategy)
def test_errorcodeexception_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original



@given(instance=ErrorCodeException_strategy)
def test_errorcodeexception_throwable_setter(instance):
    original = instance.throwable
    instance.throwable = original
    assert instance.throwable == original



@given(instance=ErrorCodeException_strategy)
def test_errorcodeexception_errorCodeMessage_setter(instance):
    original = instance.errorCodeMessage
    instance.errorCodeMessage = original
    assert instance.errorCodeMessage == original

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_ownerName_setter(instance):
    original = instance.ownerName
    instance.ownerName = original
    assert instance.ownerName == original



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original
