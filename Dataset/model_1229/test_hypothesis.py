import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    QueryCS,
    TransformationCS,
    RealizeableVariableCS,
    qvtcore_cst_RealizedVariableCS,
    ParamDeclarationCS,
    cst_IHasName,
    cst_CSTNode,
    qvtcore_cst_QueryCS,
    UnrealizedVariableCS,
    DomainCS,
    MappingCS,
    OperationCallExpCS,
    CSTNode,
    qvtcore_cst_ParamDeclarationCS,
    qvtcore_cst_TopLevelCS,
    qvtcore_cst_EnforcementOperationCS,
    AreaCS,
    qvtcore_cst_DomainCS,
    IdentifierCS,
    PathNameCS,
    RealizedVariableCS,
    EnforcementOperationCS,
    PatternCS,
    qvtcore_cst_GuardPatternCS,
    qvtcore_cst_BottomPatternCS,
    OCLExpressionCS,
    qvtcore_cst_AssignmentCS,
    BottomPatternCS,
    GuardPatternCS,
    IdentifiedCS,
    qvtcore_cst_DirectionCS,
    qvtcore_cst_MappingCS,
    qvtcore_cst_RealizeableVariableCS,
    qvtcore_cst_PatternCS,
    TypeCS,
    qvtcore_cst_AreaCS,
    qvtcore_cst_UnrealizedVariableCS,
    DirectionCS,
    qvtcore_cst_TransformationCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_querycs_is_not_abstract():
    assert not inspect.isabstract(QueryCS)


def test_querycs_constructor_exists():
    assert callable(QueryCS.__init__)


def test_querycs_constructor_args():
    sig = inspect.signature(QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_transformationcs_is_not_abstract():
    assert not inspect.isabstract(TransformationCS)


def test_transformationcs_constructor_exists():
    assert callable(TransformationCS.__init__)


def test_transformationcs_constructor_args():
    sig = inspect.signature(TransformationCS.__init__)
    params = list(sig.parameters.keys())



def test_realizeablevariablecs_is_not_abstract():
    assert not inspect.isabstract(RealizeableVariableCS)


def test_realizeablevariablecs_constructor_exists():
    assert callable(RealizeableVariableCS.__init__)


def test_realizeablevariablecs_constructor_args():
    sig = inspect.signature(RealizeableVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_realizedvariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_RealizedVariableCS)


def test_qvtcore_cst_realizedvariablecs_constructor_exists():
    assert callable(qvtcore_cst_RealizedVariableCS.__init__)


def test_qvtcore_cst_realizedvariablecs_constructor_args():
    sig = inspect.signature(qvtcore_cst_RealizedVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(ParamDeclarationCS)


def test_paramdeclarationcs_constructor_exists():
    assert callable(ParamDeclarationCS.__init__)


def test_paramdeclarationcs_constructor_args():
    sig = inspect.signature(ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_cst_ihasname_is_not_abstract():
    assert not inspect.isabstract(cst_IHasName)


def test_cst_ihasname_constructor_exists():
    assert callable(cst_IHasName.__init__)


def test_cst_ihasname_constructor_args():
    sig = inspect.signature(cst_IHasName.__init__)
    params = list(sig.parameters.keys())



def test_cst_cstnode_is_not_abstract():
    assert not inspect.isabstract(cst_CSTNode)


def test_cst_cstnode_constructor_exists():
    assert callable(cst_CSTNode.__init__)


def test_cst_cstnode_constructor_args():
    sig = inspect.signature(cst_CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_querycs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_QueryCS)


def test_qvtcore_cst_querycs_constructor_exists():
    assert callable(qvtcore_cst_QueryCS.__init__)


def test_qvtcore_cst_querycs_constructor_args():
    sig = inspect.signature(qvtcore_cst_QueryCS.__init__)
    params = list(sig.parameters.keys())



def test_unrealizedvariablecs_is_not_abstract():
    assert not inspect.isabstract(UnrealizedVariableCS)


def test_unrealizedvariablecs_constructor_exists():
    assert callable(UnrealizedVariableCS.__init__)


def test_unrealizedvariablecs_constructor_args():
    sig = inspect.signature(UnrealizedVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_domaincs_is_not_abstract():
    assert not inspect.isabstract(DomainCS)


def test_domaincs_constructor_exists():
    assert callable(DomainCS.__init__)


def test_domaincs_constructor_args():
    sig = inspect.signature(DomainCS.__init__)
    params = list(sig.parameters.keys())



def test_mappingcs_is_not_abstract():
    assert not inspect.isabstract(MappingCS)


def test_mappingcs_constructor_exists():
    assert callable(MappingCS.__init__)


def test_mappingcs_constructor_args():
    sig = inspect.signature(MappingCS.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexpcs_is_not_abstract():
    assert not inspect.isabstract(OperationCallExpCS)


def test_operationcallexpcs_constructor_exists():
    assert callable(OperationCallExpCS.__init__)


def test_operationcallexpcs_constructor_args():
    sig = inspect.signature(OperationCallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_cstnode_is_not_abstract():
    assert not inspect.isabstract(CSTNode)


def test_cstnode_constructor_exists():
    assert callable(CSTNode.__init__)


def test_cstnode_constructor_args():
    sig = inspect.signature(CSTNode.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_paramdeclarationcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_ParamDeclarationCS)


def test_qvtcore_cst_paramdeclarationcs_constructor_exists():
    assert callable(qvtcore_cst_ParamDeclarationCS.__init__)


def test_qvtcore_cst_paramdeclarationcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_ParamDeclarationCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_toplevelcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_TopLevelCS)


def test_qvtcore_cst_toplevelcs_constructor_exists():
    assert callable(qvtcore_cst_TopLevelCS.__init__)


def test_qvtcore_cst_toplevelcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_TopLevelCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_enforcementoperationcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_EnforcementOperationCS)


def test_qvtcore_cst_enforcementoperationcs_constructor_exists():
    assert callable(qvtcore_cst_EnforcementOperationCS.__init__)


def test_qvtcore_cst_enforcementoperationcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_EnforcementOperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "deletion" in params, "Missing parameter 'deletion'"

def test_qvtcore_cst_enforcementoperationcs_has_deletion():
    assert hasattr(qvtcore_cst_EnforcementOperationCS, "deletion")
    descriptor = None
    for klass in qvtcore_cst_EnforcementOperationCS.__mro__:
        if "deletion" in klass.__dict__:
            descriptor = klass.__dict__["deletion"]
            break
    assert isinstance(descriptor, property)



def test_areacs_is_not_abstract():
    assert not inspect.isabstract(AreaCS)


def test_areacs_constructor_exists():
    assert callable(AreaCS.__init__)


def test_areacs_constructor_args():
    sig = inspect.signature(AreaCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_domaincs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_DomainCS)


def test_qvtcore_cst_domaincs_constructor_exists():
    assert callable(qvtcore_cst_DomainCS.__init__)


def test_qvtcore_cst_domaincs_constructor_args():
    sig = inspect.signature(qvtcore_cst_DomainCS.__init__)
    params = list(sig.parameters.keys())
    assert "check" in params, "Missing parameter 'check'"
    assert "enforce" in params, "Missing parameter 'enforce'"

def test_qvtcore_cst_domaincs_has_check():
    assert hasattr(qvtcore_cst_DomainCS, "check")
    descriptor = None
    for klass in qvtcore_cst_DomainCS.__mro__:
        if "check" in klass.__dict__:
            descriptor = klass.__dict__["check"]
            break
    assert isinstance(descriptor, property)

def test_qvtcore_cst_domaincs_has_enforce():
    assert hasattr(qvtcore_cst_DomainCS, "enforce")
    descriptor = None
    for klass in qvtcore_cst_DomainCS.__mro__:
        if "enforce" in klass.__dict__:
            descriptor = klass.__dict__["enforce"]
            break
    assert isinstance(descriptor, property)



def test_identifiercs_is_not_abstract():
    assert not inspect.isabstract(IdentifierCS)


def test_identifiercs_constructor_exists():
    assert callable(IdentifierCS.__init__)


def test_identifiercs_constructor_args():
    sig = inspect.signature(IdentifierCS.__init__)
    params = list(sig.parameters.keys())



def test_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(PathNameCS)


def test_pathnamecs_constructor_exists():
    assert callable(PathNameCS.__init__)


def test_pathnamecs_constructor_args():
    sig = inspect.signature(PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_realizedvariablecs_is_not_abstract():
    assert not inspect.isabstract(RealizedVariableCS)


def test_realizedvariablecs_constructor_exists():
    assert callable(RealizedVariableCS.__init__)


def test_realizedvariablecs_constructor_args():
    sig = inspect.signature(RealizedVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_enforcementoperationcs_is_not_abstract():
    assert not inspect.isabstract(EnforcementOperationCS)


def test_enforcementoperationcs_constructor_exists():
    assert callable(EnforcementOperationCS.__init__)


def test_enforcementoperationcs_constructor_args():
    sig = inspect.signature(EnforcementOperationCS.__init__)
    params = list(sig.parameters.keys())



def test_patterncs_is_not_abstract():
    assert not inspect.isabstract(PatternCS)


def test_patterncs_constructor_exists():
    assert callable(PatternCS.__init__)


def test_patterncs_constructor_args():
    sig = inspect.signature(PatternCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_guardpatterncs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_GuardPatternCS)


def test_qvtcore_cst_guardpatterncs_constructor_exists():
    assert callable(qvtcore_cst_GuardPatternCS.__init__)


def test_qvtcore_cst_guardpatterncs_constructor_args():
    sig = inspect.signature(qvtcore_cst_GuardPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_bottompatterncs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_BottomPatternCS)


def test_qvtcore_cst_bottompatterncs_constructor_exists():
    assert callable(qvtcore_cst_BottomPatternCS.__init__)


def test_qvtcore_cst_bottompatterncs_constructor_args():
    sig = inspect.signature(qvtcore_cst_BottomPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_oclexpressioncs_is_not_abstract():
    assert not inspect.isabstract(OCLExpressionCS)


def test_oclexpressioncs_constructor_exists():
    assert callable(OCLExpressionCS.__init__)


def test_oclexpressioncs_constructor_args():
    sig = inspect.signature(OCLExpressionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_assignmentcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_AssignmentCS)


def test_qvtcore_cst_assignmentcs_constructor_exists():
    assert callable(qvtcore_cst_AssignmentCS.__init__)


def test_qvtcore_cst_assignmentcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_AssignmentCS.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_qvtcore_cst_assignmentcs_has_default():
    assert hasattr(qvtcore_cst_AssignmentCS, "default")
    descriptor = None
    for klass in qvtcore_cst_AssignmentCS.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_bottompatterncs_is_not_abstract():
    assert not inspect.isabstract(BottomPatternCS)


def test_bottompatterncs_constructor_exists():
    assert callable(BottomPatternCS.__init__)


def test_bottompatterncs_constructor_args():
    sig = inspect.signature(BottomPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_guardpatterncs_is_not_abstract():
    assert not inspect.isabstract(GuardPatternCS)


def test_guardpatterncs_constructor_exists():
    assert callable(GuardPatternCS.__init__)


def test_guardpatterncs_constructor_args():
    sig = inspect.signature(GuardPatternCS.__init__)
    params = list(sig.parameters.keys())



def test_identifiedcs_is_not_abstract():
    assert not inspect.isabstract(IdentifiedCS)


def test_identifiedcs_constructor_exists():
    assert callable(IdentifiedCS.__init__)


def test_identifiedcs_constructor_args():
    sig = inspect.signature(IdentifiedCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_directioncs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_DirectionCS)


def test_qvtcore_cst_directioncs_constructor_exists():
    assert callable(qvtcore_cst_DirectionCS.__init__)


def test_qvtcore_cst_directioncs_constructor_args():
    sig = inspect.signature(qvtcore_cst_DirectionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_mappingcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_MappingCS)


def test_qvtcore_cst_mappingcs_constructor_exists():
    assert callable(qvtcore_cst_MappingCS.__init__)


def test_qvtcore_cst_mappingcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_MappingCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_realizeablevariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_RealizeableVariableCS)


def test_qvtcore_cst_realizeablevariablecs_constructor_exists():
    assert callable(qvtcore_cst_RealizeableVariableCS.__init__)


def test_qvtcore_cst_realizeablevariablecs_constructor_args():
    sig = inspect.signature(qvtcore_cst_RealizeableVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_patterncs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_PatternCS)


def test_qvtcore_cst_patterncs_constructor_exists():
    assert callable(qvtcore_cst_PatternCS.__init__)


def test_qvtcore_cst_patterncs_constructor_args():
    sig = inspect.signature(qvtcore_cst_PatternCS.__init__)
    params = list(sig.parameters.keys())



def test_typecs_is_not_abstract():
    assert not inspect.isabstract(TypeCS)


def test_typecs_constructor_exists():
    assert callable(TypeCS.__init__)


def test_typecs_constructor_args():
    sig = inspect.signature(TypeCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_areacs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_AreaCS)


def test_qvtcore_cst_areacs_constructor_exists():
    assert callable(qvtcore_cst_AreaCS.__init__)


def test_qvtcore_cst_areacs_constructor_args():
    sig = inspect.signature(qvtcore_cst_AreaCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_unrealizedvariablecs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_UnrealizedVariableCS)


def test_qvtcore_cst_unrealizedvariablecs_constructor_exists():
    assert callable(qvtcore_cst_UnrealizedVariableCS.__init__)


def test_qvtcore_cst_unrealizedvariablecs_constructor_args():
    sig = inspect.signature(qvtcore_cst_UnrealizedVariableCS.__init__)
    params = list(sig.parameters.keys())



def test_directioncs_is_not_abstract():
    assert not inspect.isabstract(DirectionCS)


def test_directioncs_constructor_exists():
    assert callable(DirectionCS.__init__)


def test_directioncs_constructor_args():
    sig = inspect.signature(DirectionCS.__init__)
    params = list(sig.parameters.keys())



def test_qvtcore_cst_transformationcs_is_not_abstract():
    assert not inspect.isabstract(qvtcore_cst_TransformationCS)


def test_qvtcore_cst_transformationcs_constructor_exists():
    assert callable(qvtcore_cst_TransformationCS.__init__)


def test_qvtcore_cst_transformationcs_constructor_args():
    sig = inspect.signature(qvtcore_cst_TransformationCS.__init__)
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
QueryCS_strategy = st.builds(
    QueryCS,
)
TransformationCS_strategy = st.builds(
    TransformationCS,
)
RealizeableVariableCS_strategy = st.builds(
    RealizeableVariableCS,
)
qvtcore_cst_RealizedVariableCS_strategy = st.builds(
    qvtcore_cst_RealizedVariableCS,
)
ParamDeclarationCS_strategy = st.builds(
    ParamDeclarationCS,
)
cst_IHasName_strategy = st.builds(
    cst_IHasName,
)
cst_CSTNode_strategy = st.builds(
    cst_CSTNode,
)
qvtcore_cst_QueryCS_strategy = st.builds(
    qvtcore_cst_QueryCS,
)
UnrealizedVariableCS_strategy = st.builds(
    UnrealizedVariableCS,
)
DomainCS_strategy = st.builds(
    DomainCS,
)
MappingCS_strategy = st.builds(
    MappingCS,
)
OperationCallExpCS_strategy = st.builds(
    OperationCallExpCS,
)
CSTNode_strategy = st.builds(
    CSTNode,
)
qvtcore_cst_ParamDeclarationCS_strategy = st.builds(
    qvtcore_cst_ParamDeclarationCS,
)
qvtcore_cst_TopLevelCS_strategy = st.builds(
    qvtcore_cst_TopLevelCS,
)
qvtcore_cst_EnforcementOperationCS_strategy = st.builds(
    qvtcore_cst_EnforcementOperationCS,
    deletion=
        st.booleans()
)
AreaCS_strategy = st.builds(
    AreaCS,
)
qvtcore_cst_DomainCS_strategy = st.builds(
    qvtcore_cst_DomainCS,
    check=
        st.booleans(),
    enforce=
        st.booleans()
)
IdentifierCS_strategy = st.builds(
    IdentifierCS,
)
PathNameCS_strategy = st.builds(
    PathNameCS,
)
RealizedVariableCS_strategy = st.builds(
    RealizedVariableCS,
)
EnforcementOperationCS_strategy = st.builds(
    EnforcementOperationCS,
)
PatternCS_strategy = st.builds(
    PatternCS,
)
qvtcore_cst_GuardPatternCS_strategy = st.builds(
    qvtcore_cst_GuardPatternCS,
)
qvtcore_cst_BottomPatternCS_strategy = st.builds(
    qvtcore_cst_BottomPatternCS,
)
OCLExpressionCS_strategy = st.builds(
    OCLExpressionCS,
)
qvtcore_cst_AssignmentCS_strategy = st.builds(
    qvtcore_cst_AssignmentCS,
    default=
        st.booleans()
)
BottomPatternCS_strategy = st.builds(
    BottomPatternCS,
)
GuardPatternCS_strategy = st.builds(
    GuardPatternCS,
)
IdentifiedCS_strategy = st.builds(
    IdentifiedCS,
)
qvtcore_cst_DirectionCS_strategy = st.builds(
    qvtcore_cst_DirectionCS,
)
qvtcore_cst_MappingCS_strategy = st.builds(
    qvtcore_cst_MappingCS,
)
qvtcore_cst_RealizeableVariableCS_strategy = st.builds(
    qvtcore_cst_RealizeableVariableCS,
)
qvtcore_cst_PatternCS_strategy = st.builds(
    qvtcore_cst_PatternCS,
)
TypeCS_strategy = st.builds(
    TypeCS,
)
qvtcore_cst_AreaCS_strategy = st.builds(
    qvtcore_cst_AreaCS,
)
qvtcore_cst_UnrealizedVariableCS_strategy = st.builds(
    qvtcore_cst_UnrealizedVariableCS,
)
DirectionCS_strategy = st.builds(
    DirectionCS,
)
qvtcore_cst_TransformationCS_strategy = st.builds(
    qvtcore_cst_TransformationCS,
)

@given(instance=QueryCS_strategy)
@settings(max_examples=50)
def test_querycs_instantiation(instance):
    assert isinstance(instance, QueryCS)

@given(instance=TransformationCS_strategy)
@settings(max_examples=50)
def test_transformationcs_instantiation(instance):
    assert isinstance(instance, TransformationCS)

@given(instance=RealizeableVariableCS_strategy)
@settings(max_examples=50)
def test_realizeablevariablecs_instantiation(instance):
    assert isinstance(instance, RealizeableVariableCS)

@given(instance=qvtcore_cst_RealizedVariableCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_realizedvariablecs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_RealizedVariableCS)

@given(instance=ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, ParamDeclarationCS)

@given(instance=cst_IHasName_strategy)
@settings(max_examples=50)
def test_cst_ihasname_instantiation(instance):
    assert isinstance(instance, cst_IHasName)

@given(instance=cst_CSTNode_strategy)
@settings(max_examples=50)
def test_cst_cstnode_instantiation(instance):
    assert isinstance(instance, cst_CSTNode)

@given(instance=qvtcore_cst_QueryCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_querycs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_QueryCS)

@given(instance=UnrealizedVariableCS_strategy)
@settings(max_examples=50)
def test_unrealizedvariablecs_instantiation(instance):
    assert isinstance(instance, UnrealizedVariableCS)

@given(instance=DomainCS_strategy)
@settings(max_examples=50)
def test_domaincs_instantiation(instance):
    assert isinstance(instance, DomainCS)

@given(instance=MappingCS_strategy)
@settings(max_examples=50)
def test_mappingcs_instantiation(instance):
    assert isinstance(instance, MappingCS)

@given(instance=OperationCallExpCS_strategy)
@settings(max_examples=50)
def test_operationcallexpcs_instantiation(instance):
    assert isinstance(instance, OperationCallExpCS)

@given(instance=CSTNode_strategy)
@settings(max_examples=50)
def test_cstnode_instantiation(instance):
    assert isinstance(instance, CSTNode)

@given(instance=qvtcore_cst_ParamDeclarationCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_paramdeclarationcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_ParamDeclarationCS)

@given(instance=qvtcore_cst_TopLevelCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_toplevelcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_TopLevelCS)

@given(instance=qvtcore_cst_EnforcementOperationCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_enforcementoperationcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_EnforcementOperationCS)



@given(instance=qvtcore_cst_EnforcementOperationCS_strategy)
def test_qvtcore_cst_enforcementoperationcs_deletion_setter(instance):
    original = instance.deletion
    instance.deletion = original
    assert instance.deletion == original

@given(instance=AreaCS_strategy)
@settings(max_examples=50)
def test_areacs_instantiation(instance):
    assert isinstance(instance, AreaCS)

@given(instance=qvtcore_cst_DomainCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_domaincs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_DomainCS)



@given(instance=qvtcore_cst_DomainCS_strategy)
def test_qvtcore_cst_domaincs_check_setter(instance):
    original = instance.check
    instance.check = original
    assert instance.check == original



@given(instance=qvtcore_cst_DomainCS_strategy)
def test_qvtcore_cst_domaincs_enforce_setter(instance):
    original = instance.enforce
    instance.enforce = original
    assert instance.enforce == original

@given(instance=IdentifierCS_strategy)
@settings(max_examples=50)
def test_identifiercs_instantiation(instance):
    assert isinstance(instance, IdentifierCS)

@given(instance=PathNameCS_strategy)
@settings(max_examples=50)
def test_pathnamecs_instantiation(instance):
    assert isinstance(instance, PathNameCS)

@given(instance=RealizedVariableCS_strategy)
@settings(max_examples=50)
def test_realizedvariablecs_instantiation(instance):
    assert isinstance(instance, RealizedVariableCS)

@given(instance=EnforcementOperationCS_strategy)
@settings(max_examples=50)
def test_enforcementoperationcs_instantiation(instance):
    assert isinstance(instance, EnforcementOperationCS)

@given(instance=PatternCS_strategy)
@settings(max_examples=50)
def test_patterncs_instantiation(instance):
    assert isinstance(instance, PatternCS)

@given(instance=qvtcore_cst_GuardPatternCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_guardpatterncs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_GuardPatternCS)

@given(instance=qvtcore_cst_BottomPatternCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_bottompatterncs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_BottomPatternCS)

@given(instance=OCLExpressionCS_strategy)
@settings(max_examples=50)
def test_oclexpressioncs_instantiation(instance):
    assert isinstance(instance, OCLExpressionCS)

@given(instance=qvtcore_cst_AssignmentCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_assignmentcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_AssignmentCS)



@given(instance=qvtcore_cst_AssignmentCS_strategy)
def test_qvtcore_cst_assignmentcs_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=BottomPatternCS_strategy)
@settings(max_examples=50)
def test_bottompatterncs_instantiation(instance):
    assert isinstance(instance, BottomPatternCS)

@given(instance=GuardPatternCS_strategy)
@settings(max_examples=50)
def test_guardpatterncs_instantiation(instance):
    assert isinstance(instance, GuardPatternCS)

@given(instance=IdentifiedCS_strategy)
@settings(max_examples=50)
def test_identifiedcs_instantiation(instance):
    assert isinstance(instance, IdentifiedCS)

@given(instance=qvtcore_cst_DirectionCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_directioncs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_DirectionCS)

@given(instance=qvtcore_cst_MappingCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_mappingcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_MappingCS)

@given(instance=qvtcore_cst_RealizeableVariableCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_realizeablevariablecs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_RealizeableVariableCS)

@given(instance=qvtcore_cst_PatternCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_patterncs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_PatternCS)

@given(instance=TypeCS_strategy)
@settings(max_examples=50)
def test_typecs_instantiation(instance):
    assert isinstance(instance, TypeCS)

@given(instance=qvtcore_cst_AreaCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_areacs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_AreaCS)

@given(instance=qvtcore_cst_UnrealizedVariableCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_unrealizedvariablecs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_UnrealizedVariableCS)

@given(instance=DirectionCS_strategy)
@settings(max_examples=50)
def test_directioncs_instantiation(instance):
    assert isinstance(instance, DirectionCS)

@given(instance=qvtcore_cst_TransformationCS_strategy)
@settings(max_examples=50)
def test_qvtcore_cst_transformationcs_instantiation(instance):
    assert isinstance(instance, qvtcore_cst_TransformationCS)
