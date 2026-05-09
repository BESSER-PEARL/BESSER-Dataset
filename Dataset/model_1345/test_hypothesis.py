import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    qvtimperativecs::QueryCS,
    qvtimperativecs::TransformationCS,
    RootPackageCS,
    qvtimperativecs::TopLevelCS,
    ModelElementCS,
    qvtimperativecs::MappingStatementCS,
    qvtimperativecs::VariableCS,
    AbstractMappingCS,
    qvtimperativecs::MappingCS,
    PredicateOrAssignmentCS,
    qvtimperativecs::ImperativePredicateOrAssignmentCS,
    qvtimperativecs::PathNameCS,
    DomainCS,
    qvtimperativecs::ImperativeDomainCS,
    qvtimperativecs::Mapping,
    MappingStatementCS,
    qvtimperativecs::MappingLoopCS,
    qvtimperativecs::MappingSequenceCS,
    qvtimperativecs::Variable,
    qvtimperativecs::MappingCallCS,
    qvtimperativecs::ExpCS,
    ExpCS,
    qvtimperativecs::MappingCallBindingCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvtimperativecs::querycs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::QueryCS)


def test_qvtimperativecs::querycs_constructor_exists():
    assert callable(qvtimperativecs::QueryCS.__init__)


def test_qvtimperativecs::querycs_constructor_args():
    sig = inspect.signature(qvtimperativecs::QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::TransformationCS)


def test_qvtimperativecs::transformationcs_constructor_exists():
    assert callable(qvtimperativecs::TransformationCS.__init__)


def test_qvtimperativecs::transformationcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(RootPackageCS)


def test_rootpackagecs_constructor_exists():
    assert callable(RootPackageCS.__init__)


def test_rootpackagecs_constructor_args():
    sig = inspect.signature(RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::TopLevelCS)


def test_qvtimperativecs::toplevelcs_constructor_exists():
    assert callable(qvtimperativecs::TopLevelCS.__init__)


def test_qvtimperativecs::toplevelcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingStatementCS)


def test_qvtimperativecs::mappingstatementcs_constructor_exists():
    assert callable(qvtimperativecs::MappingStatementCS.__init__)


def test_qvtimperativecs::mappingstatementcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::variablecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::VariableCS)


def test_qvtimperativecs::variablecs_constructor_exists():
    assert callable(qvtimperativecs::VariableCS.__init__)


def test_qvtimperativecs::variablecs_constructor_args():
    sig = inspect.signature(qvtimperativecs::VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractmappingcs_is_not_abstract():
    assert not inspect.isabstract(AbstractMappingCS)


def test_abstractmappingcs_constructor_exists():
    assert callable(AbstractMappingCS.__init__)


def test_abstractmappingcs_constructor_args():
    sig = inspect.signature(AbstractMappingCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingCS)


def test_qvtimperativecs::mappingcs_constructor_exists():
    assert callable(qvtimperativecs::MappingCS.__init__)


def test_qvtimperativecs::mappingcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingCS.__init__)
    params = list(sig.parameters.keys())



def test_predicateorassignmentcs_is_not_abstract():
    assert not inspect.isabstract(PredicateOrAssignmentCS)


def test_predicateorassignmentcs_constructor_exists():
    assert callable(PredicateOrAssignmentCS.__init__)


def test_predicateorassignmentcs_constructor_args():
    sig = inspect.signature(PredicateOrAssignmentCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::imperativepredicateorassignmentcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::ImperativePredicateOrAssignmentCS)


def test_qvtimperativecs::imperativepredicateorassignmentcs_constructor_exists():
    assert callable(qvtimperativecs::ImperativePredicateOrAssignmentCS.__init__)


def test_qvtimperativecs::imperativepredicateorassignmentcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::ImperativePredicateOrAssignmentCS.__init__)
    params = list(sig.parameters.keys())
    assert "isAccumulate" in params, "Missing parameter 'isAccumulate'"

def test_qvtimperativecs::imperativepredicateorassignmentcs_has_isAccumulate():
    assert hasattr(qvtimperativecs::ImperativePredicateOrAssignmentCS, "isAccumulate")
    descriptor = None
    for klass in qvtimperativecs::ImperativePredicateOrAssignmentCS.__mro__:
        if "isAccumulate" in klass.__dict__:
            descriptor = klass.__dict__["isAccumulate"]
            break
    assert isinstance(descriptor, property)



def test_qvtimperativecs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::PathNameCS)


def test_qvtimperativecs::pathnamecs_constructor_exists():
    assert callable(qvtimperativecs::PathNameCS.__init__)


def test_qvtimperativecs::pathnamecs_constructor_args():
    sig = inspect.signature(qvtimperativecs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_domaincs_is_not_abstract():
    assert not inspect.isabstract(DomainCS)


def test_domaincs_constructor_exists():
    assert callable(DomainCS.__init__)


def test_domaincs_constructor_args():
    sig = inspect.signature(DomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::imperativedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::ImperativeDomainCS)


def test_qvtimperativecs::imperativedomaincs_constructor_exists():
    assert callable(qvtimperativecs::ImperativeDomainCS.__init__)


def test_qvtimperativecs::imperativedomaincs_constructor_args():
    sig = inspect.signature(qvtimperativecs::ImperativeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mapping_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::Mapping)


def test_qvtimperativecs::mapping_constructor_exists():
    assert callable(qvtimperativecs::Mapping.__init__)


def test_qvtimperativecs::mapping_constructor_args():
    sig = inspect.signature(qvtimperativecs::Mapping.__init__)
    params = list(sig.parameters.keys())



def test_mappingstatementcs_is_not_abstract():
    assert not inspect.isabstract(MappingStatementCS)


def test_mappingstatementcs_constructor_exists():
    assert callable(MappingStatementCS.__init__)


def test_mappingstatementcs_constructor_args():
    sig = inspect.signature(MappingStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingloopcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingLoopCS)


def test_qvtimperativecs::mappingloopcs_constructor_exists():
    assert callable(qvtimperativecs::MappingLoopCS.__init__)


def test_qvtimperativecs::mappingloopcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingLoopCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingsequencecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingSequenceCS)


def test_qvtimperativecs::mappingsequencecs_constructor_exists():
    assert callable(qvtimperativecs::MappingSequenceCS.__init__)


def test_qvtimperativecs::mappingsequencecs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingSequenceCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::variable_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::Variable)


def test_qvtimperativecs::variable_constructor_exists():
    assert callable(qvtimperativecs::Variable.__init__)


def test_qvtimperativecs::variable_constructor_args():
    sig = inspect.signature(qvtimperativecs::Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingcallcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingCallCS)


def test_qvtimperativecs::mappingcallcs_constructor_exists():
    assert callable(qvtimperativecs::MappingCallCS.__init__)


def test_qvtimperativecs::mappingcallcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingCallCS.__init__)
    params = list(sig.parameters.keys())
    assert "isInfinite" in params, "Missing parameter 'isInfinite'"

def test_qvtimperativecs::mappingcallcs_has_isInfinite():
    assert hasattr(qvtimperativecs::MappingCallCS, "isInfinite")
    descriptor = None
    for klass in qvtimperativecs::MappingCallCS.__mro__:
        if "isInfinite" in klass.__dict__:
            descriptor = klass.__dict__["isInfinite"]
            break
    assert isinstance(descriptor, property)



def test_qvtimperativecs::expcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::ExpCS)


def test_qvtimperativecs::expcs_constructor_exists():
    assert callable(qvtimperativecs::ExpCS.__init__)


def test_qvtimperativecs::expcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs::mappingcallbindingcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs::MappingCallBindingCS)


def test_qvtimperativecs::mappingcallbindingcs_constructor_exists():
    assert callable(qvtimperativecs::MappingCallBindingCS.__init__)


def test_qvtimperativecs::mappingcallbindingcs_constructor_args():
    sig = inspect.signature(qvtimperativecs::MappingCallBindingCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPolled" in params, "Missing parameter 'isPolled'"

def test_qvtimperativecs::mappingcallbindingcs_has_isPolled():
    assert hasattr(qvtimperativecs::MappingCallBindingCS, "isPolled")
    descriptor = None
    for klass in qvtimperativecs::MappingCallBindingCS.__mro__:
        if "isPolled" in klass.__dict__:
            descriptor = klass.__dict__["isPolled"]
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
qvtimperativecs::QueryCS_strategy = st.builds(
    qvtimperativecs::QueryCS,
)
qvtimperativecs::TransformationCS_strategy = st.builds(
    qvtimperativecs::TransformationCS,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
qvtimperativecs::TopLevelCS_strategy = st.builds(
    qvtimperativecs::TopLevelCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
qvtimperativecs::MappingStatementCS_strategy = st.builds(
    qvtimperativecs::MappingStatementCS,
)
qvtimperativecs::VariableCS_strategy = st.builds(
    qvtimperativecs::VariableCS,
)
AbstractMappingCS_strategy = st.builds(
    AbstractMappingCS,
)
qvtimperativecs::MappingCS_strategy = st.builds(
    qvtimperativecs::MappingCS,
)
PredicateOrAssignmentCS_strategy = st.builds(
    PredicateOrAssignmentCS,
)
qvtimperativecs::ImperativePredicateOrAssignmentCS_strategy = st.builds(
    qvtimperativecs::ImperativePredicateOrAssignmentCS,
    isAccumulate=
        st.booleans()
)
qvtimperativecs::PathNameCS_strategy = st.builds(
    qvtimperativecs::PathNameCS,
)
DomainCS_strategy = st.builds(
    DomainCS,
)
qvtimperativecs::ImperativeDomainCS_strategy = st.builds(
    qvtimperativecs::ImperativeDomainCS,
)
qvtimperativecs::Mapping_strategy = st.builds(
    qvtimperativecs::Mapping,
)
MappingStatementCS_strategy = st.builds(
    MappingStatementCS,
)
qvtimperativecs::MappingLoopCS_strategy = st.builds(
    qvtimperativecs::MappingLoopCS,
)
qvtimperativecs::MappingSequenceCS_strategy = st.builds(
    qvtimperativecs::MappingSequenceCS,
)
qvtimperativecs::Variable_strategy = st.builds(
    qvtimperativecs::Variable,
)
qvtimperativecs::MappingCallCS_strategy = st.builds(
    qvtimperativecs::MappingCallCS,
    isInfinite=
        st.booleans()
)
qvtimperativecs::ExpCS_strategy = st.builds(
    qvtimperativecs::ExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
qvtimperativecs::MappingCallBindingCS_strategy = st.builds(
    qvtimperativecs::MappingCallBindingCS,
    isPolled=
        st.booleans()
)

@given(instance=qvtimperativecs::QueryCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::querycs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::QueryCS)

@given(instance=qvtimperativecs::TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::transformationcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::TransformationCS)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=qvtimperativecs::TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::TopLevelCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=qvtimperativecs::MappingStatementCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingstatementcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingStatementCS)

@given(instance=qvtimperativecs::VariableCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::variablecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::VariableCS)

@given(instance=AbstractMappingCS_strategy)
@settings(max_examples=50)
def test_abstractmappingcs_instantiation(instance):
    assert isinstance(instance, AbstractMappingCS)

@given(instance=qvtimperativecs::MappingCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingCS)

@given(instance=PredicateOrAssignmentCS_strategy)
@settings(max_examples=50)
def test_predicateorassignmentcs_instantiation(instance):
    assert isinstance(instance, PredicateOrAssignmentCS)

@given(instance=qvtimperativecs::ImperativePredicateOrAssignmentCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::imperativepredicateorassignmentcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::ImperativePredicateOrAssignmentCS)

@given(instance=qvtimperativecs::ImperativePredicateOrAssignmentCS_strategy)
def test_qvtimperativecs::imperativepredicateorassignmentcs_isAccumulate_type(instance):
    assert isinstance(instance.isAccumulate, bool)


@given(instance=qvtimperativecs::ImperativePredicateOrAssignmentCS_strategy)
def test_qvtimperativecs::imperativepredicateorassignmentcs_isAccumulate_setter(instance):
    original = instance.isAccumulate
    instance.isAccumulate = original
    assert instance.isAccumulate == original

@given(instance=qvtimperativecs::PathNameCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::pathnamecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::PathNameCS)

@given(instance=DomainCS_strategy)
@settings(max_examples=50)
def test_domaincs_instantiation(instance):
    assert isinstance(instance, DomainCS)

@given(instance=qvtimperativecs::ImperativeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::imperativedomaincs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::ImperativeDomainCS)

@given(instance=qvtimperativecs::Mapping_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mapping_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::Mapping)

@given(instance=MappingStatementCS_strategy)
@settings(max_examples=50)
def test_mappingstatementcs_instantiation(instance):
    assert isinstance(instance, MappingStatementCS)

@given(instance=qvtimperativecs::MappingLoopCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingloopcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingLoopCS)

@given(instance=qvtimperativecs::MappingSequenceCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingsequencecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingSequenceCS)

@given(instance=qvtimperativecs::Variable_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::variable_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::Variable)

@given(instance=qvtimperativecs::MappingCallCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingcallcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingCallCS)

@given(instance=qvtimperativecs::MappingCallCS_strategy)
def test_qvtimperativecs::mappingcallcs_isInfinite_type(instance):
    assert isinstance(instance.isInfinite, bool)


@given(instance=qvtimperativecs::MappingCallCS_strategy)
def test_qvtimperativecs::mappingcallcs_isInfinite_setter(instance):
    original = instance.isInfinite
    instance.isInfinite = original
    assert instance.isInfinite == original

@given(instance=qvtimperativecs::ExpCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::expcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::ExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=qvtimperativecs::MappingCallBindingCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs::mappingcallbindingcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs::MappingCallBindingCS)

@given(instance=qvtimperativecs::MappingCallBindingCS_strategy)
def test_qvtimperativecs::mappingcallbindingcs_isPolled_type(instance):
    assert isinstance(instance.isPolled, bool)


@given(instance=qvtimperativecs::MappingCallBindingCS_strategy)
def test_qvtimperativecs::mappingcallbindingcs_isPolled_setter(instance):
    original = instance.isPolled
    instance.isPolled = original
    assert instance.isPolled == original
