import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NavigationPathCS,
    miniOCL_NavigationPathElementCS,
    miniOCL_NavigationPathVariableCS,
    miniOCL_NavigationPathCS,
    miniOCL_NavigationPathNameCS,
    BooleanLiteralExpCS,
    miniOCL_BooleanExpCS,
    miniOCL_EStructuralFeature,
    PathCS,
    miniOCL_PathElementCS,
    miniOCL_PathVariableCS,
    miniOCL_PathCS,
    LiteralExpCS,
    miniOCL_StringLiteralExpCS,
    miniOCL_BooleanLiteralExpCS,
    miniOCL_IntLiteralExpCS,
    miniOCL_AccVarCS,
    LoopExpCS,
    miniOCL_ExistsExpCS,
    miniOCL_ForAllExpCS,
    miniOCL_IterateExpCS,
    miniOCL_CollectExpCS,
    miniOCL_IteratorVarCS,
    miniOCL_RoundedBracketClauseCS,
    NavigationExpCS,
    miniOCL_LoopExpCS,
    miniOCL_NavigationNameExpCS,
    miniOCL_NameExpCS,
    PrimaryExpCS,
    miniOCL_LiteralExpCS,
    CallExpCS,
    miniOCL_PrimaryExpCS,
    miniOCL_NavigationExpCS,
    LogicExpCS,
    miniOCL_CallExpCS,
    ExpCS,
    miniOCL_LogicExpCS,
    miniOCL_InvariantCS,
    miniOCL_ExpCS,
    miniOCL_ParameterCS,
    miniOCL_OperationCS,
    miniOCL_PropertyCS,
    miniOCL_PathNameCS,
    miniOCL_ClassCS,
    miniOCL_ConstraintCS,
    miniOCL_PackageCS,
    miniOCL_RootCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(NavigationPathCS)


def test_navigationpathcs_constructor_exists():
    assert callable(NavigationPathCS.__init__)


def test_navigationpathcs_constructor_args():
    sig = inspect.signature(NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_navigationpathelementcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationPathElementCS)


def test_miniocl_navigationpathelementcs_constructor_exists():
    assert callable(miniOCL_NavigationPathElementCS.__init__)


def test_miniocl_navigationpathelementcs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationPathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_navigationpathvariablecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationPathVariableCS)


def test_miniocl_navigationpathvariablecs_constructor_exists():
    assert callable(miniOCL_NavigationPathVariableCS.__init__)


def test_miniocl_navigationpathvariablecs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationPathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_miniocl_navigationpathvariablecs_has_varName():
    assert hasattr(miniOCL_NavigationPathVariableCS, "varName")
    descriptor = None
    for klass in miniOCL_NavigationPathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_navigationpathcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationPathCS)


def test_miniocl_navigationpathcs_constructor_exists():
    assert callable(miniOCL_NavigationPathCS.__init__)


def test_miniocl_navigationpathcs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationPathCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_navigationpathnamecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationPathNameCS)


def test_miniocl_navigationpathnamecs_constructor_exists():
    assert callable(miniOCL_NavigationPathNameCS.__init__)


def test_miniocl_navigationpathnamecs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationPathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_BooleanExpCS)


def test_miniocl_booleanexpcs_constructor_exists():
    assert callable(miniOCL_BooleanExpCS.__init__)


def test_miniocl_booleanexpcs_constructor_args():
    sig = inspect.signature(miniOCL_BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_miniocl_booleanexpcs_has_boolSymbol():
    assert hasattr(miniOCL_BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in miniOCL_BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(miniOCL_EStructuralFeature)


def test_miniocl_estructuralfeature_constructor_exists():
    assert callable(miniOCL_EStructuralFeature.__init__)


def test_miniocl_estructuralfeature_constructor_args():
    sig = inspect.signature(miniOCL_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_pathcs_is_not_abstract():
    assert not inspect.isabstract(PathCS)


def test_pathcs_constructor_exists():
    assert callable(PathCS.__init__)


def test_pathcs_constructor_args():
    sig = inspect.signature(PathCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PathElementCS)


def test_miniocl_pathelementcs_constructor_exists():
    assert callable(miniOCL_PathElementCS.__init__)


def test_miniocl_pathelementcs_constructor_args():
    sig = inspect.signature(miniOCL_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_pathvariablecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PathVariableCS)


def test_miniocl_pathvariablecs_constructor_exists():
    assert callable(miniOCL_PathVariableCS.__init__)


def test_miniocl_pathvariablecs_constructor_args():
    sig = inspect.signature(miniOCL_PathVariableCS.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_miniocl_pathvariablecs_has_varName():
    assert hasattr(miniOCL_PathVariableCS, "varName")
    descriptor = None
    for klass in miniOCL_PathVariableCS.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_pathcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PathCS)


def test_miniocl_pathcs_constructor_exists():
    assert callable(miniOCL_PathCS.__init__)


def test_miniocl_pathcs_constructor_args():
    sig = inspect.signature(miniOCL_PathCS.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_stringliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_StringLiteralExpCS)


def test_miniocl_stringliteralexpcs_constructor_exists():
    assert callable(miniOCL_StringLiteralExpCS.__init__)


def test_miniocl_stringliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL_StringLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_miniocl_stringliteralexpcs_has_stringSymbol():
    assert hasattr(miniOCL_StringLiteralExpCS, "stringSymbol")
    descriptor = None
    for klass in miniOCL_StringLiteralExpCS.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_BooleanLiteralExpCS)


def test_miniocl_booleanliteralexpcs_constructor_exists():
    assert callable(miniOCL_BooleanLiteralExpCS.__init__)


def test_miniocl_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_IntLiteralExpCS)


def test_miniocl_intliteralexpcs_constructor_exists():
    assert callable(miniOCL_IntLiteralExpCS.__init__)


def test_miniocl_intliteralexpcs_constructor_args():
    sig = inspect.signature(miniOCL_IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_miniocl_intliteralexpcs_has_intSymbol():
    assert hasattr(miniOCL_IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in miniOCL_IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_accvarcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_AccVarCS)


def test_miniocl_accvarcs_constructor_exists():
    assert callable(miniOCL_AccVarCS.__init__)


def test_miniocl_accvarcs_constructor_args():
    sig = inspect.signature(miniOCL_AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accVarName" in params, "Missing parameter 'accVarName'"

def test_miniocl_accvarcs_has_accVarName():
    assert hasattr(miniOCL_AccVarCS, "accVarName")
    descriptor = None
    for klass in miniOCL_AccVarCS.__mro__:
        if "accVarName" in klass.__dict__:
            descriptor = klass.__dict__["accVarName"]
            break
    assert isinstance(descriptor, property)



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_existsexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ExistsExpCS)


def test_miniocl_existsexpcs_constructor_exists():
    assert callable(miniOCL_ExistsExpCS.__init__)


def test_miniocl_existsexpcs_constructor_args():
    sig = inspect.signature(miniOCL_ExistsExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_forallexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ForAllExpCS)


def test_miniocl_forallexpcs_constructor_exists():
    assert callable(miniOCL_ForAllExpCS.__init__)


def test_miniocl_forallexpcs_constructor_args():
    sig = inspect.signature(miniOCL_ForAllExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_IterateExpCS)


def test_miniocl_iterateexpcs_constructor_exists():
    assert callable(miniOCL_IterateExpCS.__init__)


def test_miniocl_iterateexpcs_constructor_args():
    sig = inspect.signature(miniOCL_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_collectexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_CollectExpCS)


def test_miniocl_collectexpcs_constructor_exists():
    assert callable(miniOCL_CollectExpCS.__init__)


def test_miniocl_collectexpcs_constructor_args():
    sig = inspect.signature(miniOCL_CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_IteratorVarCS)


def test_miniocl_iteratorvarcs_constructor_exists():
    assert callable(miniOCL_IteratorVarCS.__init__)


def test_miniocl_iteratorvarcs_constructor_args():
    sig = inspect.signature(miniOCL_IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_miniocl_iteratorvarcs_has_itName():
    assert hasattr(miniOCL_IteratorVarCS, "itName")
    descriptor = None
    for klass in miniOCL_IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_RoundedBracketClauseCS)


def test_miniocl_roundedbracketclausecs_constructor_exists():
    assert callable(miniOCL_RoundedBracketClauseCS.__init__)


def test_miniocl_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(miniOCL_RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_LoopExpCS)


def test_miniocl_loopexpcs_constructor_exists():
    assert callable(miniOCL_LoopExpCS.__init__)


def test_miniocl_loopexpcs_constructor_args():
    sig = inspect.signature(miniOCL_LoopExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "logicOp" in params, "Missing parameter 'logicOp'"

def test_miniocl_loopexpcs_has_logicOp():
    assert hasattr(miniOCL_LoopExpCS, "logicOp")
    descriptor = None
    for klass in miniOCL_LoopExpCS.__mro__:
        if "logicOp" in klass.__dict__:
            descriptor = klass.__dict__["logicOp"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_navigationnameexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationNameExpCS)


def test_miniocl_navigationnameexpcs_constructor_exists():
    assert callable(miniOCL_NavigationNameExpCS.__init__)


def test_miniocl_navigationnameexpcs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationNameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NameExpCS)


def test_miniocl_nameexpcs_constructor_exists():
    assert callable(miniOCL_NameExpCS.__init__)


def test_miniocl_nameexpcs_constructor_args():
    sig = inspect.signature(miniOCL_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_LiteralExpCS)


def test_miniocl_literalexpcs_constructor_exists():
    assert callable(miniOCL_LiteralExpCS.__init__)


def test_miniocl_literalexpcs_constructor_args():
    sig = inspect.signature(miniOCL_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PrimaryExpCS)


def test_miniocl_primaryexpcs_constructor_exists():
    assert callable(miniOCL_PrimaryExpCS.__init__)


def test_miniocl_primaryexpcs_constructor_args():
    sig = inspect.signature(miniOCL_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_NavigationExpCS)


def test_miniocl_navigationexpcs_constructor_exists():
    assert callable(miniOCL_NavigationExpCS.__init__)


def test_miniocl_navigationexpcs_constructor_args():
    sig = inspect.signature(miniOCL_NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(LogicExpCS)


def test_logicexpcs_constructor_exists():
    assert callable(LogicExpCS.__init__)


def test_logicexpcs_constructor_args():
    sig = inspect.signature(LogicExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_callexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_CallExpCS)


def test_miniocl_callexpcs_constructor_exists():
    assert callable(miniOCL_CallExpCS.__init__)


def test_miniocl_callexpcs_constructor_args():
    sig = inspect.signature(miniOCL_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_logicexpcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_LogicExpCS)


def test_miniocl_logicexpcs_constructor_exists():
    assert callable(miniOCL_LogicExpCS.__init__)


def test_miniocl_logicexpcs_constructor_args():
    sig = inspect.signature(miniOCL_LogicExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_miniocl_logicexpcs_has_op():
    assert hasattr(miniOCL_LogicExpCS, "op")
    descriptor = None
    for klass in miniOCL_LogicExpCS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_invariantcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_InvariantCS)


def test_miniocl_invariantcs_constructor_exists():
    assert callable(miniOCL_InvariantCS.__init__)


def test_miniocl_invariantcs_constructor_args():
    sig = inspect.signature(miniOCL_InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_expcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ExpCS)


def test_miniocl_expcs_constructor_exists():
    assert callable(miniOCL_ExpCS.__init__)


def test_miniocl_expcs_constructor_args():
    sig = inspect.signature(miniOCL_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_parametercs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ParameterCS)


def test_miniocl_parametercs_constructor_exists():
    assert callable(miniOCL_ParameterCS.__init__)


def test_miniocl_parametercs_constructor_args():
    sig = inspect.signature(miniOCL_ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl_parametercs_has_name():
    assert hasattr(miniOCL_ParameterCS, "name")
    descriptor = None
    for klass in miniOCL_ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_operationcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_OperationCS)


def test_miniocl_operationcs_constructor_exists():
    assert callable(miniOCL_OperationCS.__init__)


def test_miniocl_operationcs_constructor_args():
    sig = inspect.signature(miniOCL_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl_operationcs_has_name():
    assert hasattr(miniOCL_OperationCS, "name")
    descriptor = None
    for klass in miniOCL_OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_propertycs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PropertyCS)


def test_miniocl_propertycs_constructor_exists():
    assert callable(miniOCL_PropertyCS.__init__)


def test_miniocl_propertycs_constructor_args():
    sig = inspect.signature(miniOCL_PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl_propertycs_has_name():
    assert hasattr(miniOCL_PropertyCS, "name")
    descriptor = None
    for klass in miniOCL_PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PathNameCS)


def test_miniocl_pathnamecs_constructor_exists():
    assert callable(miniOCL_PathNameCS.__init__)


def test_miniocl_pathnamecs_constructor_args():
    sig = inspect.signature(miniOCL_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_classcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ClassCS)


def test_miniocl_classcs_constructor_exists():
    assert callable(miniOCL_ClassCS.__init__)


def test_miniocl_classcs_constructor_args():
    sig = inspect.signature(miniOCL_ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl_classcs_has_name():
    assert hasattr(miniOCL_ClassCS, "name")
    descriptor = None
    for klass in miniOCL_ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_constraintcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_ConstraintCS)


def test_miniocl_constraintcs_constructor_exists():
    assert callable(miniOCL_ConstraintCS.__init__)


def test_miniocl_constraintcs_constructor_args():
    sig = inspect.signature(miniOCL_ConstraintCS.__init__)
    params = list(sig.parameters.keys())



def test_miniocl_packagecs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_PackageCS)


def test_miniocl_packagecs_constructor_exists():
    assert callable(miniOCL_PackageCS.__init__)


def test_miniocl_packagecs_constructor_args():
    sig = inspect.signature(miniOCL_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_miniocl_packagecs_has_name():
    assert hasattr(miniOCL_PackageCS, "name")
    descriptor = None
    for klass in miniOCL_PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_miniocl_rootcs_is_not_abstract():
    assert not inspect.isabstract(miniOCL_RootCS)


def test_miniocl_rootcs_constructor_exists():
    assert callable(miniOCL_RootCS.__init__)


def test_miniocl_rootcs_constructor_args():
    sig = inspect.signature(miniOCL_RootCS.__init__)
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
NavigationPathCS_strategy = st.builds(
    NavigationPathCS,
)
miniOCL_NavigationPathElementCS_strategy = st.builds(
    miniOCL_NavigationPathElementCS,
)
miniOCL_NavigationPathVariableCS_strategy = st.builds(
    miniOCL_NavigationPathVariableCS,
    varName=
        safe_text
)
miniOCL_NavigationPathCS_strategy = st.builds(
    miniOCL_NavigationPathCS,
)
miniOCL_NavigationPathNameCS_strategy = st.builds(
    miniOCL_NavigationPathNameCS,
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
miniOCL_BooleanExpCS_strategy = st.builds(
    miniOCL_BooleanExpCS,
    boolSymbol=
        st.booleans()
)
miniOCL_EStructuralFeature_strategy = st.builds(
    miniOCL_EStructuralFeature,
)
PathCS_strategy = st.builds(
    PathCS,
)
miniOCL_PathElementCS_strategy = st.builds(
    miniOCL_PathElementCS,
)
miniOCL_PathVariableCS_strategy = st.builds(
    miniOCL_PathVariableCS,
    varName=
        safe_text
)
miniOCL_PathCS_strategy = st.builds(
    miniOCL_PathCS,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
miniOCL_StringLiteralExpCS_strategy = st.builds(
    miniOCL_StringLiteralExpCS,
    stringSymbol=
        safe_text
)
miniOCL_BooleanLiteralExpCS_strategy = st.builds(
    miniOCL_BooleanLiteralExpCS,
)
miniOCL_IntLiteralExpCS_strategy = st.builds(
    miniOCL_IntLiteralExpCS,
    intSymbol=
        st.integers()
)
miniOCL_AccVarCS_strategy = st.builds(
    miniOCL_AccVarCS,
    accVarName=
        safe_text
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
miniOCL_ExistsExpCS_strategy = st.builds(
    miniOCL_ExistsExpCS,
)
miniOCL_ForAllExpCS_strategy = st.builds(
    miniOCL_ForAllExpCS,
)
miniOCL_IterateExpCS_strategy = st.builds(
    miniOCL_IterateExpCS,
)
miniOCL_CollectExpCS_strategy = st.builds(
    miniOCL_CollectExpCS,
)
miniOCL_IteratorVarCS_strategy = st.builds(
    miniOCL_IteratorVarCS,
    itName=
        safe_text
)
miniOCL_RoundedBracketClauseCS_strategy = st.builds(
    miniOCL_RoundedBracketClauseCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
miniOCL_LoopExpCS_strategy = st.builds(
    miniOCL_LoopExpCS,
    logicOp=
        safe_text
)
miniOCL_NavigationNameExpCS_strategy = st.builds(
    miniOCL_NavigationNameExpCS,
)
miniOCL_NameExpCS_strategy = st.builds(
    miniOCL_NameExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
miniOCL_LiteralExpCS_strategy = st.builds(
    miniOCL_LiteralExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
miniOCL_PrimaryExpCS_strategy = st.builds(
    miniOCL_PrimaryExpCS,
)
miniOCL_NavigationExpCS_strategy = st.builds(
    miniOCL_NavigationExpCS,
)
LogicExpCS_strategy = st.builds(
    LogicExpCS,
)
miniOCL_CallExpCS_strategy = st.builds(
    miniOCL_CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
miniOCL_LogicExpCS_strategy = st.builds(
    miniOCL_LogicExpCS,
    op=
        safe_text
)
miniOCL_InvariantCS_strategy = st.builds(
    miniOCL_InvariantCS,
)
miniOCL_ExpCS_strategy = st.builds(
    miniOCL_ExpCS,
)
miniOCL_ParameterCS_strategy = st.builds(
    miniOCL_ParameterCS,
    name=
        safe_text
)
miniOCL_OperationCS_strategy = st.builds(
    miniOCL_OperationCS,
    name=
        safe_text
)
miniOCL_PropertyCS_strategy = st.builds(
    miniOCL_PropertyCS,
    name=
        safe_text
)
miniOCL_PathNameCS_strategy = st.builds(
    miniOCL_PathNameCS,
)
miniOCL_ClassCS_strategy = st.builds(
    miniOCL_ClassCS,
    name=
        safe_text
)
miniOCL_ConstraintCS_strategy = st.builds(
    miniOCL_ConstraintCS,
)
miniOCL_PackageCS_strategy = st.builds(
    miniOCL_PackageCS,
    name=
        safe_text
)
miniOCL_RootCS_strategy = st.builds(
    miniOCL_RootCS,
)

@given(instance=NavigationPathCS_strategy)
@settings(max_examples=50)
def test_navigationpathcs_instantiation(instance):
    assert isinstance(instance, NavigationPathCS)

@given(instance=miniOCL_NavigationPathElementCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationpathelementcs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationPathElementCS)

@given(instance=miniOCL_NavigationPathVariableCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationpathvariablecs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationPathVariableCS)



@given(instance=miniOCL_NavigationPathVariableCS_strategy)
def test_miniocl_navigationpathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=miniOCL_NavigationPathCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationpathcs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationPathCS)

@given(instance=miniOCL_NavigationPathNameCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationpathnamecs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationPathNameCS)

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=miniOCL_BooleanExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_booleanexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_BooleanExpCS)



@given(instance=miniOCL_BooleanExpCS_strategy)
def test_miniocl_booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=miniOCL_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_miniocl_estructuralfeature_instantiation(instance):
    assert isinstance(instance, miniOCL_EStructuralFeature)

@given(instance=PathCS_strategy)
@settings(max_examples=50)
def test_pathcs_instantiation(instance):
    assert isinstance(instance, PathCS)

@given(instance=miniOCL_PathElementCS_strategy)
@settings(max_examples=50)
def test_miniocl_pathelementcs_instantiation(instance):
    assert isinstance(instance, miniOCL_PathElementCS)

@given(instance=miniOCL_PathVariableCS_strategy)
@settings(max_examples=50)
def test_miniocl_pathvariablecs_instantiation(instance):
    assert isinstance(instance, miniOCL_PathVariableCS)



@given(instance=miniOCL_PathVariableCS_strategy)
def test_miniocl_pathvariablecs_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=miniOCL_PathCS_strategy)
@settings(max_examples=50)
def test_miniocl_pathcs_instantiation(instance):
    assert isinstance(instance, miniOCL_PathCS)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=miniOCL_StringLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_stringliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_StringLiteralExpCS)



@given(instance=miniOCL_StringLiteralExpCS_strategy)
def test_miniocl_stringliteralexpcs_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=miniOCL_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_BooleanLiteralExpCS)

@given(instance=miniOCL_IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_intliteralexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_IntLiteralExpCS)



@given(instance=miniOCL_IntLiteralExpCS_strategy)
def test_miniocl_intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=miniOCL_AccVarCS_strategy)
@settings(max_examples=50)
def test_miniocl_accvarcs_instantiation(instance):
    assert isinstance(instance, miniOCL_AccVarCS)



@given(instance=miniOCL_AccVarCS_strategy)
def test_miniocl_accvarcs_accVarName_setter(instance):
    original = instance.accVarName
    instance.accVarName = original
    assert instance.accVarName == original

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=miniOCL_ExistsExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_existsexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_ExistsExpCS)

@given(instance=miniOCL_ForAllExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_forallexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_ForAllExpCS)

@given(instance=miniOCL_IterateExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_iterateexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_IterateExpCS)

@given(instance=miniOCL_CollectExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_collectexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_CollectExpCS)

@given(instance=miniOCL_IteratorVarCS_strategy)
@settings(max_examples=50)
def test_miniocl_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, miniOCL_IteratorVarCS)



@given(instance=miniOCL_IteratorVarCS_strategy)
def test_miniocl_iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=miniOCL_RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_miniocl_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, miniOCL_RoundedBracketClauseCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=miniOCL_LoopExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_loopexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_LoopExpCS)



@given(instance=miniOCL_LoopExpCS_strategy)
def test_miniocl_loopexpcs_logicOp_setter(instance):
    original = instance.logicOp
    instance.logicOp = original
    assert instance.logicOp == original

@given(instance=miniOCL_NavigationNameExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationnameexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationNameExpCS)

@given(instance=miniOCL_NameExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_nameexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_NameExpCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=miniOCL_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_literalexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_LiteralExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=miniOCL_PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_primaryexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_PrimaryExpCS)

@given(instance=miniOCL_NavigationExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_navigationexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_NavigationExpCS)

@given(instance=LogicExpCS_strategy)
@settings(max_examples=50)
def test_logicexpcs_instantiation(instance):
    assert isinstance(instance, LogicExpCS)

@given(instance=miniOCL_CallExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_callexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=miniOCL_LogicExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_logicexpcs_instantiation(instance):
    assert isinstance(instance, miniOCL_LogicExpCS)



@given(instance=miniOCL_LogicExpCS_strategy)
def test_miniocl_logicexpcs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=miniOCL_InvariantCS_strategy)
@settings(max_examples=50)
def test_miniocl_invariantcs_instantiation(instance):
    assert isinstance(instance, miniOCL_InvariantCS)

@given(instance=miniOCL_ExpCS_strategy)
@settings(max_examples=50)
def test_miniocl_expcs_instantiation(instance):
    assert isinstance(instance, miniOCL_ExpCS)

@given(instance=miniOCL_ParameterCS_strategy)
@settings(max_examples=50)
def test_miniocl_parametercs_instantiation(instance):
    assert isinstance(instance, miniOCL_ParameterCS)



@given(instance=miniOCL_ParameterCS_strategy)
def test_miniocl_parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL_OperationCS_strategy)
@settings(max_examples=50)
def test_miniocl_operationcs_instantiation(instance):
    assert isinstance(instance, miniOCL_OperationCS)



@given(instance=miniOCL_OperationCS_strategy)
def test_miniocl_operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL_PropertyCS_strategy)
@settings(max_examples=50)
def test_miniocl_propertycs_instantiation(instance):
    assert isinstance(instance, miniOCL_PropertyCS)



@given(instance=miniOCL_PropertyCS_strategy)
def test_miniocl_propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL_PathNameCS_strategy)
@settings(max_examples=50)
def test_miniocl_pathnamecs_instantiation(instance):
    assert isinstance(instance, miniOCL_PathNameCS)

@given(instance=miniOCL_ClassCS_strategy)
@settings(max_examples=50)
def test_miniocl_classcs_instantiation(instance):
    assert isinstance(instance, miniOCL_ClassCS)



@given(instance=miniOCL_ClassCS_strategy)
def test_miniocl_classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL_ConstraintCS_strategy)
@settings(max_examples=50)
def test_miniocl_constraintcs_instantiation(instance):
    assert isinstance(instance, miniOCL_ConstraintCS)

@given(instance=miniOCL_PackageCS_strategy)
@settings(max_examples=50)
def test_miniocl_packagecs_instantiation(instance):
    assert isinstance(instance, miniOCL_PackageCS)



@given(instance=miniOCL_PackageCS_strategy)
def test_miniocl_packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniOCL_RootCS_strategy)
@settings(max_examples=50)
def test_miniocl_rootcs_instantiation(instance):
    assert isinstance(instance, miniOCL_RootCS)
