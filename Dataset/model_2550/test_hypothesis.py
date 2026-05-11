import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dml::TE,
    dml::EObject,
    dml::TAN,
    dml::IS,
    dml::PE,
    dml::FC,
    dml::DI,
    dml::PARFORPARAMS,
    dml::FP,
    dml::BS,
    dml::E,
    dml::SPKV,
    dml::PL,
    dml::ID,
    dml::S,
    dml::F,
    dml::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dml::te_is_not_abstract():
    assert not inspect.isabstract(dml::TE)


def test_dml::te_constructor_exists():
    assert callable(dml::TE.__init__)


def test_dml::te_constructor_args():
    sig = inspect.signature(dml::TE.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "i" in params, "Missing parameter 'i'"
    assert "s" in params, "Missing parameter 's'"
    assert "d" in params, "Missing parameter 'd'"

def test_dml::te_has_b():
    assert hasattr(dml::TE, "b")
    descriptor = None
    for klass in dml::TE.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_dml::te_has_i():
    assert hasattr(dml::TE, "i")
    descriptor = None
    for klass in dml::TE.__mro__:
        if "i" in klass.__dict__:
            descriptor = klass.__dict__["i"]
            break
    assert isinstance(descriptor, property)

def test_dml::te_has_s():
    assert hasattr(dml::TE, "s")
    descriptor = None
    for klass in dml::TE.__mro__:
        if "s" in klass.__dict__:
            descriptor = klass.__dict__["s"]
            break
    assert isinstance(descriptor, property)

def test_dml::te_has_d():
    assert hasattr(dml::TE, "d")
    descriptor = None
    for klass in dml::TE.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_dml::eobject_is_not_abstract():
    assert not inspect.isabstract(dml::EObject)


def test_dml::eobject_constructor_exists():
    assert callable(dml::EObject.__init__)


def test_dml::eobject_constructor_args():
    sig = inspect.signature(dml::EObject.__init__)
    params = list(sig.parameters.keys())



def test_dml::tan_is_not_abstract():
    assert not inspect.isabstract(dml::TAN)


def test_dml::tan_constructor_exists():
    assert callable(dml::TAN.__init__)


def test_dml::tan_constructor_args():
    sig = inspect.signature(dml::TAN.__init__)
    params = list(sig.parameters.keys())
    assert "t" in params, "Missing parameter 't'"

def test_dml::tan_has_t():
    assert hasattr(dml::TAN, "t")
    descriptor = None
    for klass in dml::TAN.__mro__:
        if "t" in klass.__dict__:
            descriptor = klass.__dict__["t"]
            break
    assert isinstance(descriptor, property)



def test_dml::is_is_not_abstract():
    assert not inspect.isabstract(dml::IS)


def test_dml::is_constructor_exists():
    assert callable(dml::IS.__init__)


def test_dml::is_constructor_args():
    sig = inspect.signature(dml::IS.__init__)
    params = list(sig.parameters.keys())



def test_dml::pe_is_not_abstract():
    assert not inspect.isabstract(dml::PE)


def test_dml::pe_constructor_exists():
    assert callable(dml::PE.__init__)


def test_dml::pe_constructor_args():
    sig = inspect.signature(dml::PE.__init__)
    params = list(sig.parameters.keys())



def test_dml::fc_is_not_abstract():
    assert not inspect.isabstract(dml::FC)


def test_dml::fc_constructor_exists():
    assert callable(dml::FC.__init__)


def test_dml::fc_constructor_args():
    sig = inspect.signature(dml::FC.__init__)
    params = list(sig.parameters.keys())
    assert "bif" in params, "Missing parameter 'bif'"

def test_dml::fc_has_bif():
    assert hasattr(dml::FC, "bif")
    descriptor = None
    for klass in dml::FC.__mro__:
        if "bif" in klass.__dict__:
            descriptor = klass.__dict__["bif"]
            break
    assert isinstance(descriptor, property)



def test_dml::di_is_not_abstract():
    assert not inspect.isabstract(dml::DI)


def test_dml::di_constructor_exists():
    assert callable(dml::DI.__init__)


def test_dml::di_constructor_args():
    sig = inspect.signature(dml::DI.__init__)
    params = list(sig.parameters.keys())
    assert "cln" in params, "Missing parameter 'cln'"
    assert "clid" in params, "Missing parameter 'clid'"

def test_dml::di_has_cln():
    assert hasattr(dml::DI, "cln")
    descriptor = None
    for klass in dml::DI.__mro__:
        if "cln" in klass.__dict__:
            descriptor = klass.__dict__["cln"]
            break
    assert isinstance(descriptor, property)

def test_dml::di_has_clid():
    assert hasattr(dml::DI, "clid")
    descriptor = None
    for klass in dml::DI.__mro__:
        if "clid" in klass.__dict__:
            descriptor = klass.__dict__["clid"]
            break
    assert isinstance(descriptor, property)



def test_dml::parforparams_is_not_abstract():
    assert not inspect.isabstract(dml::PARFORPARAMS)


def test_dml::parforparams_constructor_exists():
    assert callable(dml::PARFORPARAMS.__init__)


def test_dml::parforparams_constructor_args():
    sig = inspect.signature(dml::PARFORPARAMS.__init__)
    params = list(sig.parameters.keys())
    assert "params" in params, "Missing parameter 'params'"

def test_dml::parforparams_has_params():
    assert hasattr(dml::PARFORPARAMS, "params")
    descriptor = None
    for klass in dml::PARFORPARAMS.__mro__:
        if "params" in klass.__dict__:
            descriptor = klass.__dict__["params"]
            break
    assert isinstance(descriptor, property)



def test_dml::fp_is_not_abstract():
    assert not inspect.isabstract(dml::FP)


def test_dml::fp_constructor_exists():
    assert callable(dml::FP.__init__)


def test_dml::fp_constructor_args():
    sig = inspect.signature(dml::FP.__init__)
    params = list(sig.parameters.keys())



def test_dml::bs_is_not_abstract():
    assert not inspect.isabstract(dml::BS)


def test_dml::bs_constructor_exists():
    assert callable(dml::BS.__init__)


def test_dml::bs_constructor_args():
    sig = inspect.signature(dml::BS.__init__)
    params = list(sig.parameters.keys())



def test_dml::e_is_not_abstract():
    assert not inspect.isabstract(dml::E)


def test_dml::e_constructor_exists():
    assert callable(dml::E.__init__)


def test_dml::e_constructor_args():
    sig = inspect.signature(dml::E.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_dml::e_has_op():
    assert hasattr(dml::E, "op")
    descriptor = None
    for klass in dml::E.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_dml::spkv_is_not_abstract():
    assert not inspect.isabstract(dml::SPKV)


def test_dml::spkv_constructor_exists():
    assert callable(dml::SPKV.__init__)


def test_dml::spkv_constructor_args():
    sig = inspect.signature(dml::SPKV.__init__)
    params = list(sig.parameters.keys())
    assert "v" in params, "Missing parameter 'v'"

def test_dml::spkv_has_v():
    assert hasattr(dml::SPKV, "v")
    descriptor = None
    for klass in dml::SPKV.__mro__:
        if "v" in klass.__dict__:
            descriptor = klass.__dict__["v"]
            break
    assert isinstance(descriptor, property)



def test_dml::pl_is_not_abstract():
    assert not inspect.isabstract(dml::PL)


def test_dml::pl_constructor_exists():
    assert callable(dml::PL.__init__)


def test_dml::pl_constructor_args():
    sig = inspect.signature(dml::PL.__init__)
    params = list(sig.parameters.keys())



def test_dml::id_is_not_abstract():
    assert not inspect.isabstract(dml::ID)


def test_dml::id_constructor_exists():
    assert callable(dml::ID.__init__)


def test_dml::id_constructor_args():
    sig = inspect.signature(dml::ID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dml::id_has_name():
    assert hasattr(dml::ID, "name")
    descriptor = None
    for klass in dml::ID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dml::s_is_not_abstract():
    assert not inspect.isabstract(dml::S)


def test_dml::s_constructor_exists():
    assert callable(dml::S.__init__)


def test_dml::s_constructor_args():
    sig = inspect.signature(dml::S.__init__)
    params = list(sig.parameters.keys())
    assert "cwd" in params, "Missing parameter 'cwd'"
    assert "src" in params, "Missing parameter 'src'"

def test_dml::s_has_cwd():
    assert hasattr(dml::S, "cwd")
    descriptor = None
    for klass in dml::S.__mro__:
        if "cwd" in klass.__dict__:
            descriptor = klass.__dict__["cwd"]
            break
    assert isinstance(descriptor, property)

def test_dml::s_has_src():
    assert hasattr(dml::S, "src")
    descriptor = None
    for klass in dml::S.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)



def test_dml::f_is_not_abstract():
    assert not inspect.isabstract(dml::F)


def test_dml::f_constructor_exists():
    assert callable(dml::F.__init__)


def test_dml::f_constructor_args():
    sig = inspect.signature(dml::F.__init__)
    params = list(sig.parameters.keys())



def test_dml::d_is_not_abstract():
    assert not inspect.isabstract(dml::D)


def test_dml::d_constructor_exists():
    assert callable(dml::D.__init__)


def test_dml::d_constructor_args():
    sig = inspect.signature(dml::D.__init__)
    params = list(sig.parameters.keys())


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
dml::TE_strategy = st.builds(
    dml::TE,
    b=
        safe_text,
    i=
        st.integers(),
    s=
        safe_text,
    d=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dml::EObject_strategy = st.builds(
    dml::EObject,
)
dml::TAN_strategy = st.builds(
    dml::TAN,
    t=
        safe_text
)
dml::IS_strategy = st.builds(
    dml::IS,
)
dml::PE_strategy = st.builds(
    dml::PE,
)
dml::FC_strategy = st.builds(
    dml::FC,
    bif=
        safe_text
)
dml::DI_strategy = st.builds(
    dml::DI,
    cln=
        safe_text,
    clid=
        safe_text
)
dml::PARFORPARAMS_strategy = st.builds(
    dml::PARFORPARAMS,
    params=
        safe_text
)
dml::FP_strategy = st.builds(
    dml::FP,
)
dml::BS_strategy = st.builds(
    dml::BS,
)
dml::E_strategy = st.builds(
    dml::E,
    op=
        safe_text
)
dml::SPKV_strategy = st.builds(
    dml::SPKV,
    v=
        safe_text
)
dml::PL_strategy = st.builds(
    dml::PL,
)
dml::ID_strategy = st.builds(
    dml::ID,
    name=
        safe_text
)
dml::S_strategy = st.builds(
    dml::S,
    cwd=
        safe_text,
    src=
        safe_text
)
dml::F_strategy = st.builds(
    dml::F,
)
dml::D_strategy = st.builds(
    dml::D,
)

@given(instance=dml::TE_strategy)
@settings(max_examples=50)
def test_dml::te_instantiation(instance):
    assert isinstance(instance, dml::TE)

@given(instance=dml::TE_strategy)
def test_dml::te_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=dml::TE_strategy)
def test_dml::te_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=dml::TE_strategy)
def test_dml::te_i_type(instance):
    assert isinstance(instance.i, int)


@given(instance=dml::TE_strategy)
def test_dml::te_i_setter(instance):
    original = instance.i
    instance.i = original
    assert instance.i == original

@given(instance=dml::TE_strategy)
def test_dml::te_s_type(instance):
    assert isinstance(instance.s, str)


@given(instance=dml::TE_strategy)
def test_dml::te_s_setter(instance):
    original = instance.s
    instance.s = original
    assert instance.s == original

@given(instance=dml::TE_strategy)
def test_dml::te_d_type(instance):
    assert isinstance(instance.d, float)


@given(instance=dml::TE_strategy)
def test_dml::te_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=dml::EObject_strategy)
@settings(max_examples=50)
def test_dml::eobject_instantiation(instance):
    assert isinstance(instance, dml::EObject)

@given(instance=dml::TAN_strategy)
@settings(max_examples=50)
def test_dml::tan_instantiation(instance):
    assert isinstance(instance, dml::TAN)

@given(instance=dml::TAN_strategy)
def test_dml::tan_t_type(instance):
    assert isinstance(instance.t, str)


@given(instance=dml::TAN_strategy)
def test_dml::tan_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original

@given(instance=dml::IS_strategy)
@settings(max_examples=50)
def test_dml::is_instantiation(instance):
    assert isinstance(instance, dml::IS)

@given(instance=dml::PE_strategy)
@settings(max_examples=50)
def test_dml::pe_instantiation(instance):
    assert isinstance(instance, dml::PE)

@given(instance=dml::FC_strategy)
@settings(max_examples=50)
def test_dml::fc_instantiation(instance):
    assert isinstance(instance, dml::FC)

@given(instance=dml::FC_strategy)
def test_dml::fc_bif_type(instance):
    assert isinstance(instance.bif, str)


@given(instance=dml::FC_strategy)
def test_dml::fc_bif_setter(instance):
    original = instance.bif
    instance.bif = original
    assert instance.bif == original

@given(instance=dml::DI_strategy)
@settings(max_examples=50)
def test_dml::di_instantiation(instance):
    assert isinstance(instance, dml::DI)

@given(instance=dml::DI_strategy)
def test_dml::di_cln_type(instance):
    assert isinstance(instance.cln, str)


@given(instance=dml::DI_strategy)
def test_dml::di_cln_setter(instance):
    original = instance.cln
    instance.cln = original
    assert instance.cln == original

@given(instance=dml::DI_strategy)
def test_dml::di_clid_type(instance):
    assert isinstance(instance.clid, str)


@given(instance=dml::DI_strategy)
def test_dml::di_clid_setter(instance):
    original = instance.clid
    instance.clid = original
    assert instance.clid == original

@given(instance=dml::PARFORPARAMS_strategy)
@settings(max_examples=50)
def test_dml::parforparams_instantiation(instance):
    assert isinstance(instance, dml::PARFORPARAMS)

@given(instance=dml::PARFORPARAMS_strategy)
def test_dml::parforparams_params_type(instance):
    assert isinstance(instance.params, str)


@given(instance=dml::PARFORPARAMS_strategy)
def test_dml::parforparams_params_setter(instance):
    original = instance.params
    instance.params = original
    assert instance.params == original

@given(instance=dml::FP_strategy)
@settings(max_examples=50)
def test_dml::fp_instantiation(instance):
    assert isinstance(instance, dml::FP)

@given(instance=dml::BS_strategy)
@settings(max_examples=50)
def test_dml::bs_instantiation(instance):
    assert isinstance(instance, dml::BS)

@given(instance=dml::E_strategy)
@settings(max_examples=50)
def test_dml::e_instantiation(instance):
    assert isinstance(instance, dml::E)

@given(instance=dml::E_strategy)
def test_dml::e_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=dml::E_strategy)
def test_dml::e_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=dml::SPKV_strategy)
@settings(max_examples=50)
def test_dml::spkv_instantiation(instance):
    assert isinstance(instance, dml::SPKV)

@given(instance=dml::SPKV_strategy)
def test_dml::spkv_v_type(instance):
    assert isinstance(instance.v, str)


@given(instance=dml::SPKV_strategy)
def test_dml::spkv_v_setter(instance):
    original = instance.v
    instance.v = original
    assert instance.v == original

@given(instance=dml::PL_strategy)
@settings(max_examples=50)
def test_dml::pl_instantiation(instance):
    assert isinstance(instance, dml::PL)

@given(instance=dml::ID_strategy)
@settings(max_examples=50)
def test_dml::id_instantiation(instance):
    assert isinstance(instance, dml::ID)

@given(instance=dml::ID_strategy)
def test_dml::id_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dml::ID_strategy)
def test_dml::id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dml::S_strategy)
@settings(max_examples=50)
def test_dml::s_instantiation(instance):
    assert isinstance(instance, dml::S)

@given(instance=dml::S_strategy)
def test_dml::s_cwd_type(instance):
    assert isinstance(instance.cwd, str)


@given(instance=dml::S_strategy)
def test_dml::s_cwd_setter(instance):
    original = instance.cwd
    instance.cwd = original
    assert instance.cwd == original

@given(instance=dml::S_strategy)
def test_dml::s_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=dml::S_strategy)
def test_dml::s_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=dml::F_strategy)
@settings(max_examples=50)
def test_dml::f_instantiation(instance):
    assert isinstance(instance, dml::F)

@given(instance=dml::D_strategy)
@settings(max_examples=50)
def test_dml::d_instantiation(instance):
    assert isinstance(instance, dml::D)
