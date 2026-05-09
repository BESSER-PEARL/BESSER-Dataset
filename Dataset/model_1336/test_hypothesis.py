import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BooleanLiteralExpCS,
    miniOCL::BooleanExpCS,
    miniOCL::RoundedBracketClauseCS,
    miniOCL::PathElementCS,
    LiteralExpCS,
    miniOCL::BooleanLiteralExpCS,
    miniOCL::StringLiteralExpCS,
    miniOCL::IntLiteralExpCS,
    miniOCL::OperationCS,
    miniOCL::PropertyCS,
    miniOCL::PathNameCS,
    PrimaryExpCS,
    miniOCL::LiteralExpCS,
    CallExpCS,
    miniOCL::PrimaryExpCS,
    miniOCL::NameExpCS,
    LogicExpCS,
    miniOCL::CallExpCS,
    ExpCS,
    miniOCL::LogicExpCS,
    miniOCL::InvariantCS,
    miniOCL::ExpCS,
    miniOCL::ParameterCS,
    miniOCL::ClassCS,
    miniOCL::ConstraintCS,
    miniOCL::PackageCS,
    miniOCL::RootCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::BooleanExpCS)


def test_miniocl::booleanexpcs_constructor_exists():
    assert callable(miniOCL::BooleanExpCS.__init__)


def test_miniocl::booleanexpcs_constructor_args():
    sig = inspect.signature(miniOCL::BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_miniocl::booleanexpcs_has_boolSymbol():
    assert hasattr(miniOCL::BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in miniOCL::BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::RoundedBracketClauseCS)


def test_miniocl::roundedbracketclausecs_constructor_exists():
    assert callable(miniOCL::RoundedBracketClauseCS.__init__)


def test_miniocl::roundedbracketclausecs_constructor_args():
    sig = inspect.signature(miniOCL::RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::PathElementCS)


def test_miniocl::pathelementcs_constructor_exists():
    assert callable(miniOCL::PathElementCS.__init__)


def test_miniocl::pathelementcs_constructor_args():
    sig = inspect.signature(miniOCL::PathElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "pathName" in params, "Missing parameter 'pathName'"

def test_miniocl::pathelementcs_has_pathName():
    assert hasattr(miniOCL::PathElementCS, "pathName")
    descriptor = None
    for klass in miniOCL::PathElementCS.__mro__:
        if "pathName" in klass.__dict__:
            descriptor = klass.__dict__["pathName"]
            break
    assert isinstance(descriptor, property)



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::BooleanLiteralExpCS)


def test_miniocl::booleanliteralexpcs_constructor_exists():
    assert callable(miniOCL::BooleanLiteralExpCS.__init__)


def test_miniocl::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::StringLiteralExpCS)


def test_miniocl::stringliteralexpcs_constructor_exists():
    assert callable(miniOCL::StringLiteralExpCS.__init__)


def test_miniocl::stringliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL::StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_miniocl::stringliteralexpcs_has_stringSymbol():
    assert hasattr(miniOCL::StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in miniOCL::StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::IntLiteralExpCS)


def test_miniocl::intliteralexpcs_constructor_exists():
    assert callable(miniOCL::IntLiteralExpCS.__init__)


def test_miniocl::intliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL::IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_miniocl::intliteralexpcs_has_intSymbol():
    assert hasattr(miniOCL::IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in miniOCL::IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::operationcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::OperationCS)


def test_miniocl::operationcs_constructor_exists():
    assert callable(miniOCL::OperationCS.__init__)


def test_miniocl::operationcs_constructor_args():
    sig = inspect.signature(miniOCL::OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl::operationcs_has_name():
    assert hasattr(miniOCL::OperationCS, "name")
    descriptor = None
    for klass in miniOCL::OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::propertycs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::PropertyCS)


def test_miniocl::propertycs_constructor_exists():
    assert callable(miniOCL::PropertyCS.__init__)


def test_miniocl::propertycs_constructor_args():
    sig = inspect.signature(miniOCL::PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl::propertycs_has_name():
    assert hasattr(miniOCL::PropertyCS, "name")
    descriptor = None
    for klass in miniOCL::PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::PathNameCS)


def test_miniocl::pathnamecs_constructor_exists():
    assert callable(miniOCL::PathNameCS.__init__)


def test_miniocl::pathnamecs_constructor_args():
    sig = inspect.signature(miniOCL::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::LiteralExpCS)


def test_miniocl::literalexpcs_constructor_exists():
    assert callable(miniOCL::LiteralExpCS.__init__)


def test_miniocl::literalexpcs_constructor_args():
    sig = inspect.signature(miniOCL::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::PrimaryExpCS)


def test_miniocl::primaryexpcs_constructor_exists():
    assert callable(miniOCL::PrimaryExpCS.__init__)


def test_miniocl::primaryexpcs_constructor_args():
    sig = inspect.signature(miniOCL::PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::NameExpCS)


def test_miniocl::nameexpcs_constructor_exists():
    assert callable(miniOCL::NameExpCS.__init__)


def test_miniocl::nameexpcs_constructor_args():
    sig = inspect.signature(miniOCL::NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::callexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::CallExpCS)


def test_miniocl::callexpcs_constructor_exists():
    assert callable(miniOCL::CallExpCS.__init__)


def test_miniocl::callexpcs_constructor_args():
    sig = inspect.signature(miniOCL::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::logicexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::LogicExpCS)


def test_miniocl::logicexpcs_constructor_exists():
    assert callable(miniOCL::LogicExpCS.__init__)


def test_miniocl::logicexpcs_constructor_args():
    sig = inspect.signature(miniOCL::LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_miniocl::logicexpcs_has_op():
    assert hasattr(miniOCL::LogicExpCS, "op")
    descriptor = None
    for klass in miniOCL::LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::invariantcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::InvariantCS)


def test_miniocl::invariantcs_constructor_exists():
    assert callable(miniOCL::InvariantCS.__init__)


def test_miniocl::invariantcs_constructor_args():
    sig = inspect.signature(miniOCL::InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::expcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::ExpCS)


def test_miniocl::expcs_constructor_exists():
    assert callable(miniOCL::ExpCS.__init__)


def test_miniocl::expcs_constructor_args():
    sig = inspect.signature(miniOCL::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::parametercs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::ParameterCS)


def test_miniocl::parametercs_constructor_exists():
    assert callable(miniOCL::ParameterCS.__init__)


def test_miniocl::parametercs_constructor_args():
    sig = inspect.signature(miniOCL::ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl::parametercs_has_name():
    assert hasattr(miniOCL::ParameterCS, "name")
    descriptor = None
    for klass in miniOCL::ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::classcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::ClassCS)


def test_miniocl::classcs_constructor_exists():
    assert callable(miniOCL::ClassCS.__init__)


def test_miniocl::classcs_constructor_args():
    sig = inspect.signature(miniOCL::ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl::classcs_has_name():
    assert hasattr(miniOCL::ClassCS, "name")
    descriptor = None
    for klass in miniOCL::ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::constraintcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::ConstraintCS)


def test_miniocl::constraintcs_constructor_exists():
    assert callable(miniOCL::ConstraintCS.__init__)


def test_miniocl::constraintcs_constructor_args():
    sig = inspect.signature(miniOCL::ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl::packagecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::PackageCS)


def test_miniocl::packagecs_constructor_exists():
    assert callable(miniOCL::PackageCS.__init__)


def test_miniocl::packagecs_constructor_args():
    sig = inspect.signature(miniOCL::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl::packagecs_has_name():
    assert hasattr(miniOCL::PackageCS, "name")
    descriptor = None
    for klass in miniOCL::PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl::rootcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL::RootCS)


def test_miniocl::rootcs_constructor_exists():
    assert callable(miniOCL::RootCS.__init__)


def test_miniocl::rootcs_constructor_args():
    sig = inspect.signature(miniOCL::RootCS.__init__)
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
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
miniOCL::BooleanExpCS_strategy = st.builds(
    miniOCL::BooleanExpCS,
    boolSymbol=
        st.booleans()
)
miniOCL::RoundedBracketClauseCS_strategy = st.builds(
    miniOCL::RoundedBracketClauseCS,
)
miniOCL::PathElementCS_strategy = st.builds(
    miniOCL::PathElementCS,
    pathName=
        safe_text
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
miniOCL::BooleanLiteralExpCS_strategy = st.builds(
    miniOCL::BooleanLiteralExpCS,
)
miniOCL::StringLiteralExpCS_strategy = st.builds(
    miniOCL::StringLiteralExpCS,
    stringSymbol=
        safe_text
)
miniOCL::IntLiteralExpCS_strategy = st.builds(
    miniOCL::IntLiteralExpCS,
    intSymbol=
        st.integers()
)
miniOCL::OperationCS_strategy = st.builds(
    miniOCL::OperationCS,
    name=
        safe_text
)
miniOCL::PropertyCS_strategy = st.builds(
    miniOCL::PropertyCS,
    name=
        safe_text
)
miniOCL::PathNameCS_strategy = st.builds(
    miniOCL::PathNameCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
miniOCL::LiteralExpCS_strategy = st.builds(
    miniOCL::LiteralExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
miniOCL::PrimaryExpCS_strategy = st.builds(
    miniOCL::PrimaryExpCS,
)
miniOCL::NameExpCS_strategy = st.builds(
    miniOCL::NameExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
miniOCL::CallExpCS_strategy = st.builds(
    miniOCL::CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
miniOCL::LogicExpCS_strategy = st.builds(
    miniOCL::LogicExpCS,
    op=
        safe_text
)
miniOCL::InvariantCS_strategy = st.builds(
    miniOCL::InvariantCS,
)
miniOCL::ExpCS_strategy = st.builds(
    miniOCL::ExpCS,
)
miniOCL::ParameterCS_strategy = st.builds(
    miniOCL::ParameterCS,
    name=
        safe_text
)
miniOCL::ClassCS_strategy = st.builds(
    miniOCL::ClassCS,
    name=
        safe_text
)
miniOCL::ConstraintCS_strategy = st.builds(
    miniOCL::ConstraintCS,
)
miniOCL::PackageCS_strategy = st.builds(
    miniOCL::PackageCS,
    name=
        safe_text
)
miniOCL::RootCS_strategy = st.builds(
    miniOCL::RootCS,
)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=miniOCL::BooleanExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::booleanexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::BooleanExpCS)

@given(instance=miniOCL::BooleanExpCS_strategy)
def test_miniocl::booleanexpcs_boolSymbol_type(instance):
    assert isinstance(instance.boolSymbol, bool)


@given(instance=miniOCL::BooleanExpCS_strategy)
def test_miniocl::booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=miniOCL::RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_miniocl::roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, miniOCL::RoundedBracketClauseCS)

@given(instance=miniOCL::PathElementCS_strategy)
@settings(max_examples=50)
def test_miniocl::pathelementcs_instantiation(instance):
    assert isinstance(instance, miniOCL::PathElementCS)

@given(instance=miniOCL::PathElementCS_strategy)
def test_miniocl::pathelementcs_pathName_type(instance):
    assert isinstance(instance.pathName, str)


@given(instance=miniOCL::PathElementCS_strategy)
def test_miniocl::pathelementcs_pathName_setter(instance):
    original = instance.pathName
    instance.pathName = original
    assert instance.pathName == original

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=miniOCL::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::BooleanLiteralExpCS)

@given(instance=miniOCL::StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::StringLiteralExpCS)

@given(instance=miniOCL::StringLiteralExpCS_strategy)
def test_miniocl::stringliteralexpcs_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=miniOCL::StringLiteralExpCS_strategy)
def test_miniocl::stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=miniOCL::IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::intliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::IntLiteralExpCS)

@given(instance=miniOCL::IntLiteralExpCS_strategy)
def test_miniocl::intliteralexpcs_intSymbol_type(instance):
    assert isinstance(instance.intSymbol, int)


@given(instance=miniOCL::IntLiteralExpCS_strategy)
def test_miniocl::intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=miniOCL::OperationCS_strategy)
@settings(max_examples=50)
def test_miniocl::operationcs_instantiation(instance):
    assert isinstance(instance, miniOCL::OperationCS)

@given(instance=miniOCL::OperationCS_strategy)
def test_miniocl::operationcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniOCL::OperationCS_strategy)
def test_miniocl::operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL::PropertyCS_strategy)
@settings(max_examples=50)
def test_miniocl::propertycs_instantiation(instance):
    assert isinstance(instance, miniOCL::PropertyCS)

@given(instance=miniOCL::PropertyCS_strategy)
def test_miniocl::propertycs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniOCL::PropertyCS_strategy)
def test_miniocl::propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL::PathNameCS_strategy)
@settings(max_examples=50)
def test_miniocl::pathnamecs_instantiation(instance):
    assert isinstance(instance, miniOCL::PathNameCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=miniOCL::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::literalexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::LiteralExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=miniOCL::PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::primaryexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::PrimaryExpCS)

@given(instance=miniOCL::NameExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::nameexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::NameExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=miniOCL::CallExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::callexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=miniOCL::LogicExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::logicexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL::LogicExpCS)

@given(instance=miniOCL::LogicExpCS_strategy)
def test_miniocl::logicexpcs_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=miniOCL::LogicExpCS_strategy)
def test_miniocl::logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=miniOCL::InvariantCS_strategy)
@settings(max_examples=50)
def test_miniocl::invariantcs_instantiation(instance):
    assert isinstance(instance, miniOCL::InvariantCS)

@given(instance=miniOCL::ExpCS_strategy)
@settings(max_examples=50)
def test_miniocl::expcs_instantiation(instance):
    assert isinstance(instance, miniOCL::ExpCS)

@given(instance=miniOCL::ParameterCS_strategy)
@settings(max_examples=50)
def test_miniocl::parametercs_instantiation(instance):
    assert isinstance(instance, miniOCL::ParameterCS)

@given(instance=miniOCL::ParameterCS_strategy)
def test_miniocl::parametercs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniOCL::ParameterCS_strategy)
def test_miniocl::parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL::ClassCS_strategy)
@settings(max_examples=50)
def test_miniocl::classcs_instantiation(instance):
    assert isinstance(instance, miniOCL::ClassCS)

@given(instance=miniOCL::ClassCS_strategy)
def test_miniocl::classcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniOCL::ClassCS_strategy)
def test_miniocl::classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL::ConstraintCS_strategy)
@settings(max_examples=50)
def test_miniocl::constraintcs_instantiation(instance):
    assert isinstance(instance, miniOCL::ConstraintCS)

@given(instance=miniOCL::PackageCS_strategy)
@settings(max_examples=50)
def test_miniocl::packagecs_instantiation(instance):
    assert isinstance(instance, miniOCL::PackageCS)

@given(instance=miniOCL::PackageCS_strategy)
def test_miniocl::packagecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniOCL::PackageCS_strategy)
def test_miniocl::packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL::RootCS_strategy)
@settings(max_examples=50)
def test_miniocl::rootcs_instantiation(instance):
    assert isinstance(instance, miniOCL::RootCS)
