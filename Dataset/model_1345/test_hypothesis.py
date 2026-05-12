import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    qvtimperativecs_QueryCS,
    qvtimperativecs_TransformationCS,
    RootPackageCS,
    qvtimperativecs_TopLevelCS,
    ModelElementCS,
    qvtimperativecs_MappingStatementCS,
    qvtimperativecs_VariableCS,
    AbstractMappingCS,
    qvtimperativecs_MappingCS,
    PredicateOrAssignmentCS,
    qvtimperativecs_ImperativePredicateOrAssignmentCS,
    qvtimperativecs_PathNameCS,
    DomainCS,
    qvtimperativecs_ImperativeDomainCS,
    qvtimperativecs_Mapping,
    MappingStatementCS,
    qvtimperativecs_MappingSequenceCS,
    qvtimperativecs_MappingLoopCS,
    qvtimperativecs_Variable,
    qvtimperativecs_MappingCallCS,
    qvtimperativecs_ExpCS,
    ExpCS,
    qvtimperativecs_MappingCallBindingCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_qvtimperativecs_querycs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_QueryCS)


def test_qvtimperativecs_querycs_constructor_exists():
    assert callable(qvtimperativecs_QueryCS.__init__)


def test_qvtimperativecs_querycs_constructor_args():
    sig = inspect.signature(qvtimperativecs_QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_TransformationCS)


def test_qvtimperativecs_transformationcs_constructor_exists():
    assert callable(qvtimperativecs_TransformationCS.__init__)


def test_qvtimperativecs_transformationcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_rootpackagecs_is_not_abstract():
    assert not inspect.isabstract(RootPackageCS)


def test_rootpackagecs_constructor_exists():
    assert callable(RootPackageCS.__init__)


def test_rootpackagecs_constructor_args():
    sig = inspect.signature(RootPackageCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_TopLevelCS)


def test_qvtimperativecs_toplevelcs_constructor_exists():
    assert callable(qvtimperativecs_TopLevelCS.__init__)


def test_qvtimperativecs_toplevelcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_modelelementcs_is_not_abstract():
    assert not inspect.isabstract(ModelElementCS)


def test_modelelementcs_constructor_exists():
    assert callable(ModelElementCS.__init__)


def test_modelelementcs_constructor_args():
    sig = inspect.signature(ModelElementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingstatementcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingStatementCS)


def test_qvtimperativecs_mappingstatementcs_constructor_exists():
    assert callable(qvtimperativecs_MappingStatementCS.__init__)


def test_qvtimperativecs_mappingstatementcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_variablecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_VariableCS)


def test_qvtimperativecs_variablecs_constructor_exists():
    assert callable(qvtimperativecs_VariableCS.__init__)


def test_qvtimperativecs_variablecs_constructor_args():
    sig = inspect.signature(qvtimperativecs_VariableCS.__init__)
    params = list(sig.parameters.keys())



def test_abstractmappingcs_is_not_abstract():
    assert not inspect.isabstract(AbstractMappingCS)


def test_abstractmappingcs_constructor_exists():
    assert callable(AbstractMappingCS.__init__)


def test_abstractmappingcs_constructor_args():
    sig = inspect.signature(AbstractMappingCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingCS)


def test_qvtimperativecs_mappingcs_constructor_exists():
    assert callable(qvtimperativecs_MappingCS.__init__)


def test_qvtimperativecs_mappingcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingCS.__init__)
    params = list(sig.parameters.keys())



def test_predicateorassignmentcs_is_not_abstract():
    assert not inspect.isabstract(PredicateOrAssignmentCS)


def test_predicateorassignmentcs_constructor_exists():
    assert callable(PredicateOrAssignmentCS.__init__)


def test_predicateorassignmentcs_constructor_args():
    sig = inspect.signature(PredicateOrAssignmentCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_imperativepredicateorassignmentcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_ImperativePredicateOrAssignmentCS)


def test_qvtimperativecs_imperativepredicateorassignmentcs_constructor_exists():
    assert callable(qvtimperativecs_ImperativePredicateOrAssignmentCS.__init__)


def test_qvtimperativecs_imperativepredicateorassignmentcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_ImperativePredicateOrAssignmentCS.__init__)
    params = list(sig.parameters.keys())
    assert "isAccumulate" in params, "Missing parameter 'isAccumulate'"

def test_qvtimperativecs_imperativepredicateorassignmentcs_has_isAccumulate():
    assert hasattr(qvtimperativecs_ImperativePredicateOrAssignmentCS, "isAccumulate")
    descriptor = None
    for klass in qvtimperativecs_ImperativePredicateOrAssignmentCS.__mro__:
        if "isAccumulate" in klass.__dict__:
            descriptor = klass.__dict__["isAccumulate"]
            break
    assert isinstance(descriptor, property)



def test_qvtimperativecs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_PathNameCS)


def test_qvtimperativecs_pathnamecs_constructor_exists():
    assert callable(qvtimperativecs_PathNameCS.__init__)


def test_qvtimperativecs_pathnamecs_constructor_args():
    sig = inspect.signature(qvtimperativecs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_domaincs_is_not_abstract():
    assert not inspect.isabstract(DomainCS)


def test_domaincs_constructor_exists():
    assert callable(DomainCS.__init__)


def test_domaincs_constructor_args():
    sig = inspect.signature(DomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_imperativedomaincs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_ImperativeDomainCS)


def test_qvtimperativecs_imperativedomaincs_constructor_exists():
    assert callable(qvtimperativecs_ImperativeDomainCS.__init__)


def test_qvtimperativecs_imperativedomaincs_constructor_args():
    sig = inspect.signature(qvtimperativecs_ImperativeDomainCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mapping_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_Mapping)


def test_qvtimperativecs_mapping_constructor_exists():
    assert callable(qvtimperativecs_Mapping.__init__)


def test_qvtimperativecs_mapping_constructor_args():
    sig = inspect.signature(qvtimperativecs_Mapping.__init__)
    params = list(sig.parameters.keys())



def test_mappingstatementcs_is_not_abstract():
    assert not inspect.isabstract(MappingStatementCS)


def test_mappingstatementcs_constructor_exists():
    assert callable(MappingStatementCS.__init__)


def test_mappingstatementcs_constructor_args():
    sig = inspect.signature(MappingStatementCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingsequencecs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingSequenceCS)


def test_qvtimperativecs_mappingsequencecs_constructor_exists():
    assert callable(qvtimperativecs_MappingSequenceCS.__init__)


def test_qvtimperativecs_mappingsequencecs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingSequenceCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingloopcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingLoopCS)


def test_qvtimperativecs_mappingloopcs_constructor_exists():
    assert callable(qvtimperativecs_MappingLoopCS.__init__)


def test_qvtimperativecs_mappingloopcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingLoopCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_variable_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_Variable)


def test_qvtimperativecs_variable_constructor_exists():
    assert callable(qvtimperativecs_Variable.__init__)


def test_qvtimperativecs_variable_constructor_args():
    sig = inspect.signature(qvtimperativecs_Variable.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingcallcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingCallCS)


def test_qvtimperativecs_mappingcallcs_constructor_exists():
    assert callable(qvtimperativecs_MappingCallCS.__init__)


def test_qvtimperativecs_mappingcallcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingCallCS.__init__)
    params = list(sig.parameters.keys())
    assert "isInfinite" in params, "Missing parameter 'isInfinite'"

def test_qvtimperativecs_mappingcallcs_has_isInfinite():
    assert hasattr(qvtimperativecs_MappingCallCS, "isInfinite")
    descriptor = None
    for klass in qvtimperativecs_MappingCallCS.__mro__:
        if "isInfinite" in klass.__dict__:
            descriptor = klass.__dict__["isInfinite"]
            break
    assert isinstance(descriptor, property)



def test_qvtimperativecs_expcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_ExpCS)


def test_qvtimperativecs_expcs_constructor_exists():
    assert callable(qvtimperativecs_ExpCS.__init__)


def test_qvtimperativecs_expcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtimperativecs_mappingcallbindingcs_is_not_abstract():
    assert not inspect.isabstract(qvtimperativecs_MappingCallBindingCS)


def test_qvtimperativecs_mappingcallbindingcs_constructor_exists():
    assert callable(qvtimperativecs_MappingCallBindingCS.__init__)


def test_qvtimperativecs_mappingcallbindingcs_constructor_args():
    sig = inspect.signature(qvtimperativecs_MappingCallBindingCS.__init__)
    params = list(sig.parameters.keys())
    assert "isPolled" in params, "Missing parameter 'isPolled'"

def test_qvtimperativecs_mappingcallbindingcs_has_isPolled():
    assert hasattr(qvtimperativecs_MappingCallBindingCS, "isPolled")
    descriptor = None
    for klass in qvtimperativecs_MappingCallBindingCS.__mro__:
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
qvtimperativecs_QueryCS_strategy = st.builds(
    qvtimperativecs_QueryCS,
)
qvtimperativecs_TransformationCS_strategy = st.builds(
    qvtimperativecs_TransformationCS,
)
RootPackageCS_strategy = st.builds(
    RootPackageCS,
)
qvtimperativecs_TopLevelCS_strategy = st.builds(
    qvtimperativecs_TopLevelCS,
)
ModelElementCS_strategy = st.builds(
    ModelElementCS,
)
qvtimperativecs_MappingStatementCS_strategy = st.builds(
    qvtimperativecs_MappingStatementCS,
)
qvtimperativecs_VariableCS_strategy = st.builds(
    qvtimperativecs_VariableCS,
)
AbstractMappingCS_strategy = st.builds(
    AbstractMappingCS,
)
qvtimperativecs_MappingCS_strategy = st.builds(
    qvtimperativecs_MappingCS,
)
PredicateOrAssignmentCS_strategy = st.builds(
    PredicateOrAssignmentCS,
)
qvtimperativecs_ImperativePredicateOrAssignmentCS_strategy = st.builds(
    qvtimperativecs_ImperativePredicateOrAssignmentCS,
    isAccumulate=
        st.booleans()
)
qvtimperativecs_PathNameCS_strategy = st.builds(
    qvtimperativecs_PathNameCS,
)
DomainCS_strategy = st.builds(
    DomainCS,
)
qvtimperativecs_ImperativeDomainCS_strategy = st.builds(
    qvtimperativecs_ImperativeDomainCS,
)
qvtimperativecs_Mapping_strategy = st.builds(
    qvtimperativecs_Mapping,
)
MappingStatementCS_strategy = st.builds(
    MappingStatementCS,
)
qvtimperativecs_MappingSequenceCS_strategy = st.builds(
    qvtimperativecs_MappingSequenceCS,
)
qvtimperativecs_MappingLoopCS_strategy = st.builds(
    qvtimperativecs_MappingLoopCS,
)
qvtimperativecs_Variable_strategy = st.builds(
    qvtimperativecs_Variable,
)
qvtimperativecs_MappingCallCS_strategy = st.builds(
    qvtimperativecs_MappingCallCS,
    isInfinite=
        st.booleans()
)
qvtimperativecs_ExpCS_strategy = st.builds(
    qvtimperativecs_ExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
qvtimperativecs_MappingCallBindingCS_strategy = st.builds(
    qvtimperativecs_MappingCallBindingCS,
    isPolled=
        st.booleans()
)

@given(instance=qvtimperativecs_QueryCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_querycs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_QueryCS)

@given(instance=qvtimperativecs_TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_transformationcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_TransformationCS)

@given(instance=RootPackageCS_strategy)
@settings(max_examples=50)
def test_rootpackagecs_instantiation(instance):
    assert isinstance(instance, RootPackageCS)

@given(instance=qvtimperativecs_TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_TopLevelCS)

@given(instance=ModelElementCS_strategy)
@settings(max_examples=50)
def test_modelelementcs_instantiation(instance):
    assert isinstance(instance, ModelElementCS)

@given(instance=qvtimperativecs_MappingStatementCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingstatementcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingStatementCS)

@given(instance=qvtimperativecs_VariableCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_variablecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_VariableCS)

@given(instance=AbstractMappingCS_strategy)
@settings(max_examples=50)
def test_abstractmappingcs_instantiation(instance):
    assert isinstance(instance, AbstractMappingCS)

@given(instance=qvtimperativecs_MappingCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCS)

@given(instance=PredicateOrAssignmentCS_strategy)
@settings(max_examples=50)
def test_predicateorassignmentcs_instantiation(instance):
    assert isinstance(instance, PredicateOrAssignmentCS)

@given(instance=qvtimperativecs_ImperativePredicateOrAssignmentCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_imperativepredicateorassignmentcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ImperativePredicateOrAssignmentCS)



@given(instance=qvtimperativecs_ImperativePredicateOrAssignmentCS_strategy)
def test_qvtimperativecs_imperativepredicateorassignmentcs_isAccumulate_setter(instance):
    original = instance.isAccumulate
    instance.isAccumulate = original
    assert instance.isAccumulate == original

@given(instance=qvtimperativecs_PathNameCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_pathnamecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_PathNameCS)

@given(instance=DomainCS_strategy)
@settings(max_examples=50)
def test_domaincs_instantiation(instance):
    assert isinstance(instance, DomainCS)

@given(instance=qvtimperativecs_ImperativeDomainCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_imperativedomaincs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ImperativeDomainCS)

@given(instance=qvtimperativecs_Mapping_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mapping_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_Mapping)

@given(instance=MappingStatementCS_strategy)
@settings(max_examples=50)
def test_mappingstatementcs_instantiation(instance):
    assert isinstance(instance, MappingStatementCS)

@given(instance=qvtimperativecs_MappingSequenceCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingsequencecs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingSequenceCS)

@given(instance=qvtimperativecs_MappingLoopCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingloopcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingLoopCS)

@given(instance=qvtimperativecs_Variable_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_variable_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_Variable)

@given(instance=qvtimperativecs_MappingCallCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingcallcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCallCS)



@given(instance=qvtimperativecs_MappingCallCS_strategy)
def test_qvtimperativecs_mappingcallcs_isInfinite_setter(instance):
    original = instance.isInfinite
    instance.isInfinite = original
    assert instance.isInfinite == original

@given(instance=qvtimperativecs_ExpCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_expcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_ExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=qvtimperativecs_MappingCallBindingCS_strategy)
@settings(max_examples=50)
def test_qvtimperativecs_mappingcallbindingcs_instantiation(instance):
    assert isinstance(instance, qvtimperativecs_MappingCallBindingCS)



@given(instance=qvtimperativecs_MappingCallBindingCS_strategy)
def test_qvtimperativecs_mappingcallbindingcs_isPolled_setter(instance):
    original = instance.isPolled
    instance.isPolled = original
    assert instance.isPolled == original
