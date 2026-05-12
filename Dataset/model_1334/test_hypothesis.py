import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    minioclcs_EObject,
    minioclcs_CSTrace,
    LiteralExpCS,
    minioclcs_IntLiteralExpCS,
    BooleanLiteralExpCS,
    minioclcs_BooleanExpCS,
    minioclcs_EClass,
    minioclcs_CollectionLiteralExpCS,
    minioclcs_NullLiteralExpCS,
    minioclcs_BooleanLiteralExpCS,
    LoopExpCS,
    minioclcs_IterateExpCS,
    minioclcs_CollectExpCS,
    NavigationExpCS,
    minioclcs_LoopExpCS,
    PrimaryExpCS,
    minioclcs_LetExpCS,
    minioclcs_LiteralExpCS,
    minioclcs_NameExpCS,
    minioclcs_SelfExpCS,
    CallExpCS,
    minioclcs_PrimaryExpCS,
    EqualityExpCS,
    minioclcs_CallExpCS,
    ExpCS,
    minioclcs_EqualityExpCS,
    CSTrace,
    minioclcs_InvariantCS,
    minioclcs_RoundedBracketClauseCS,
    minioclcs_PropertyCS,
    minioclcs_ParameterCS,
    minioclcs_PathNameCS,
    minioclcs_LetVarCS,
    minioclcs_NavigationExpCS,
    minioclcs_MultiplicityCS,
    minioclcs_AccVarCS,
    minioclcs_ClassCS,
    minioclcs_PackageCS,
    minioclcs_ConstraintsDefCS,
    minioclcs_CollectionLiteralPartCS,
    minioclcs_OperationCS,
    minioclcs_PathElementCS,
    minioclcs_ImportCS,
    minioclcs_IteratorVarCS,
    minioclcs_ExpCS,
    minioclcs_RootCS,
    CollectionKindCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minioclcs_eobject_is_not_abstract():
    assert not inspect.isabstract(minioclcs_EObject)


def test_minioclcs_eobject_constructor_exists():
    assert callable(minioclcs_EObject.__init__)


def test_minioclcs_eobject_constructor_args():
    sig = inspect.signature(minioclcs_EObject.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_cstrace_is_not_abstract():
    assert not inspect.isabstract(minioclcs_CSTrace)


def test_minioclcs_cstrace_constructor_exists():
    assert callable(minioclcs_CSTrace.__init__)


def test_minioclcs_cstrace_constructor_args():
    sig = inspect.signature(minioclcs_CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_IntLiteralExpCS)


def test_minioclcs_intliteralexpcs_constructor_exists():
    assert callable(minioclcs_IntLiteralExpCS.__init__)


def test_minioclcs_intliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs_IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_minioclcs_intliteralexpcs_has_intSymbol():
    assert hasattr(minioclcs_IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in minioclcs_IntLiteralExpCS.__mro__:
        if "intSymbol" in klass.__dict__:
            descriptor = klass.__dict__["intSymbol"]
            break
    assert isinstance(descriptor, property)



def test_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(BooleanLiteralExpCS)


def test_booleanliteralexpcs_constructor_exists():
    assert callable(BooleanLiteralExpCS.__init__)


def test_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_BooleanExpCS)


def test_minioclcs_booleanexpcs_constructor_exists():
    assert callable(minioclcs_BooleanExpCS.__init__)


def test_minioclcs_booleanexpcs_constructor_args():
    sig = inspect.signature(minioclcs_BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_minioclcs_booleanexpcs_has_boolSymbol():
    assert hasattr(minioclcs_BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in minioclcs_BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_eclass_is_not_abstract():
    assert not inspect.isabstract(minioclcs_EClass)


def test_minioclcs_eclass_constructor_exists():
    assert callable(minioclcs_EClass.__init__)


def test_minioclcs_eclass_constructor_args():
    sig = inspect.signature(minioclcs_EClass.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_CollectionLiteralExpCS)


def test_minioclcs_collectionliteralexpcs_constructor_exists():
    assert callable(minioclcs_CollectionLiteralExpCS.__init__)


def test_minioclcs_collectionliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs_CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_minioclcs_collectionliteralexpcs_has_kind():
    assert hasattr(minioclcs_CollectionLiteralExpCS, "kind")
    descriptor = None
    for klass in minioclcs_CollectionLiteralExpCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_NullLiteralExpCS)


def test_minioclcs_nullliteralexpcs_constructor_exists():
    assert callable(minioclcs_NullLiteralExpCS.__init__)


def test_minioclcs_nullliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs_NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_BooleanLiteralExpCS)


def test_minioclcs_booleanliteralexpcs_constructor_exists():
    assert callable(minioclcs_BooleanLiteralExpCS.__init__)


def test_minioclcs_booleanliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs_BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_IterateExpCS)


def test_minioclcs_iterateexpcs_constructor_exists():
    assert callable(minioclcs_IterateExpCS.__init__)


def test_minioclcs_iterateexpcs_constructor_args():
    sig = inspect.signature(minioclcs_IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_collectexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_CollectExpCS)


def test_minioclcs_collectexpcs_constructor_exists():
    assert callable(minioclcs_CollectExpCS.__init__)


def test_minioclcs_collectexpcs_constructor_args():
    sig = inspect.signature(minioclcs_CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_LoopExpCS)


def test_minioclcs_loopexpcs_constructor_exists():
    assert callable(minioclcs_LoopExpCS.__init__)


def test_minioclcs_loopexpcs_constructor_args():
    sig = inspect.signature(minioclcs_LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_letexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_LetExpCS)


def test_minioclcs_letexpcs_constructor_exists():
    assert callable(minioclcs_LetExpCS.__init__)


def test_minioclcs_letexpcs_constructor_args():
    sig = inspect.signature(minioclcs_LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_LiteralExpCS)


def test_minioclcs_literalexpcs_constructor_exists():
    assert callable(minioclcs_LiteralExpCS.__init__)


def test_minioclcs_literalexpcs_constructor_args():
    sig = inspect.signature(minioclcs_LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_nameexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_NameExpCS)


def test_minioclcs_nameexpcs_constructor_exists():
    assert callable(minioclcs_NameExpCS.__init__)


def test_minioclcs_nameexpcs_constructor_args():
    sig = inspect.signature(minioclcs_NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_selfexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_SelfExpCS)


def test_minioclcs_selfexpcs_constructor_exists():
    assert callable(minioclcs_SelfExpCS.__init__)


def test_minioclcs_selfexpcs_constructor_args():
    sig = inspect.signature(minioclcs_SelfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_PrimaryExpCS)


def test_minioclcs_primaryexpcs_constructor_exists():
    assert callable(minioclcs_PrimaryExpCS.__init__)


def test_minioclcs_primaryexpcs_constructor_args():
    sig = inspect.signature(minioclcs_PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpcs_is_not_abstract():
    assert not inspect.isabstract(EqualityExpCS)


def test_equalityexpcs_constructor_exists():
    assert callable(EqualityExpCS.__init__)


def test_equalityexpcs_constructor_args():
    sig = inspect.signature(EqualityExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_callexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_CallExpCS)


def test_minioclcs_callexpcs_constructor_exists():
    assert callable(minioclcs_CallExpCS.__init__)


def test_minioclcs_callexpcs_constructor_args():
    sig = inspect.signature(minioclcs_CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_equalityexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_EqualityExpCS)


def test_minioclcs_equalityexpcs_constructor_exists():
    assert callable(minioclcs_EqualityExpCS.__init__)


def test_minioclcs_equalityexpcs_constructor_args():
    sig = inspect.signature(minioclcs_EqualityExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_minioclcs_equalityexpcs_has_opName():
    assert hasattr(minioclcs_EqualityExpCS, "opName")
    descriptor = None
    for klass in minioclcs_EqualityExpCS.__mro__:
        if "opName" in klass.__dict__:
            descriptor = klass.__dict__["opName"]
            break
    assert isinstance(descriptor, property)



def test_cstrace_is_not_abstract():
    assert not inspect.isabstract(CSTrace)


def test_cstrace_constructor_exists():
    assert callable(CSTrace.__init__)


def test_cstrace_constructor_args():
    sig = inspect.signature(CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_invariantcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_InvariantCS)


def test_minioclcs_invariantcs_constructor_exists():
    assert callable(minioclcs_InvariantCS.__init__)


def test_minioclcs_invariantcs_constructor_args():
    sig = inspect.signature(minioclcs_InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_RoundedBracketClauseCS)


def test_minioclcs_roundedbracketclausecs_constructor_exists():
    assert callable(minioclcs_RoundedBracketClauseCS.__init__)


def test_minioclcs_roundedbracketclausecs_constructor_args():
    sig = inspect.signature(minioclcs_RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_propertycs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_PropertyCS)


def test_minioclcs_propertycs_constructor_exists():
    assert callable(minioclcs_PropertyCS.__init__)


def test_minioclcs_propertycs_constructor_args():
    sig = inspect.signature(minioclcs_PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_propertycs_has_name():
    assert hasattr(minioclcs_PropertyCS, "name")
    descriptor = None
    for klass in minioclcs_PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_parametercs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_ParameterCS)


def test_minioclcs_parametercs_constructor_exists():
    assert callable(minioclcs_ParameterCS.__init__)


def test_minioclcs_parametercs_constructor_args():
    sig = inspect.signature(minioclcs_ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_parametercs_has_name():
    assert hasattr(minioclcs_ParameterCS, "name")
    descriptor = None
    for klass in minioclcs_ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_PathNameCS)


def test_minioclcs_pathnamecs_constructor_exists():
    assert callable(minioclcs_PathNameCS.__init__)


def test_minioclcs_pathnamecs_constructor_args():
    sig = inspect.signature(minioclcs_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_letvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_LetVarCS)


def test_minioclcs_letvarcs_constructor_exists():
    assert callable(minioclcs_LetVarCS.__init__)


def test_minioclcs_letvarcs_constructor_args():
    sig = inspect.signature(minioclcs_LetVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_letvarcs_has_name():
    assert hasattr(minioclcs_LetVarCS, "name")
    descriptor = None
    for klass in minioclcs_LetVarCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_NavigationExpCS)


def test_minioclcs_navigationexpcs_constructor_exists():
    assert callable(minioclcs_NavigationExpCS.__init__)


def test_minioclcs_navigationexpcs_constructor_args():
    sig = inspect.signature(minioclcs_NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_MultiplicityCS)


def test_minioclcs_multiplicitycs_constructor_exists():
    assert callable(minioclcs_MultiplicityCS.__init__)


def test_minioclcs_multiplicitycs_constructor_args():
    sig = inspect.signature(minioclcs_MultiplicityCS.__init__)
    params = list(sig.parameters.keys())
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "upperInt" in params, "Missing parameter 'upperInt'"
    assert "mult" in params, "Missing parameter 'mult'"
    assert "upperMult" in params, "Missing parameter 'upperMult'"
    assert "opt" in params, "Missing parameter 'opt'"
    assert "lowerInt" in params, "Missing parameter 'lowerInt'"

def test_minioclcs_multiplicitycs_has_mandatory():
    assert hasattr(minioclcs_MultiplicityCS, "mandatory")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_multiplicitycs_has_upperInt():
    assert hasattr(minioclcs_MultiplicityCS, "upperInt")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "upperInt" in klass.__dict__:
            descriptor = klass.__dict__["upperInt"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_multiplicitycs_has_mult():
    assert hasattr(minioclcs_MultiplicityCS, "mult")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "mult" in klass.__dict__:
            descriptor = klass.__dict__["mult"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_multiplicitycs_has_upperMult():
    assert hasattr(minioclcs_MultiplicityCS, "upperMult")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "upperMult" in klass.__dict__:
            descriptor = klass.__dict__["upperMult"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_multiplicitycs_has_opt():
    assert hasattr(minioclcs_MultiplicityCS, "opt")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "opt" in klass.__dict__:
            descriptor = klass.__dict__["opt"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_multiplicitycs_has_lowerInt():
    assert hasattr(minioclcs_MultiplicityCS, "lowerInt")
    descriptor = None
    for klass in minioclcs_MultiplicityCS.__mro__:
        if "lowerInt" in klass.__dict__:
            descriptor = klass.__dict__["lowerInt"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_accvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_AccVarCS)


def test_minioclcs_accvarcs_constructor_exists():
    assert callable(minioclcs_AccVarCS.__init__)


def test_minioclcs_accvarcs_constructor_args():
    sig = inspect.signature(minioclcs_AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accName" in params, "Missing parameter 'accName'"

def test_minioclcs_accvarcs_has_accName():
    assert hasattr(minioclcs_AccVarCS, "accName")
    descriptor = None
    for klass in minioclcs_AccVarCS.__mro__:
        if "accName" in klass.__dict__:
            descriptor = klass.__dict__["accName"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_classcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_ClassCS)


def test_minioclcs_classcs_constructor_exists():
    assert callable(minioclcs_ClassCS.__init__)


def test_minioclcs_classcs_constructor_args():
    sig = inspect.signature(minioclcs_ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_classcs_has_name():
    assert hasattr(minioclcs_ClassCS, "name")
    descriptor = None
    for klass in minioclcs_ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_packagecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_PackageCS)


def test_minioclcs_packagecs_constructor_exists():
    assert callable(minioclcs_PackageCS.__init__)


def test_minioclcs_packagecs_constructor_args():
    sig = inspect.signature(minioclcs_PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_packagecs_has_name():
    assert hasattr(minioclcs_PackageCS, "name")
    descriptor = None
    for klass in minioclcs_PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_constraintsdefcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_ConstraintsDefCS)


def test_minioclcs_constraintsdefcs_constructor_exists():
    assert callable(minioclcs_ConstraintsDefCS.__init__)


def test_minioclcs_constraintsdefcs_constructor_args():
    sig = inspect.signature(minioclcs_ConstraintsDefCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_CollectionLiteralPartCS)


def test_minioclcs_collectionliteralpartcs_constructor_exists():
    assert callable(minioclcs_CollectionLiteralPartCS.__init__)


def test_minioclcs_collectionliteralpartcs_constructor_args():
    sig = inspect.signature(minioclcs_CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_operationcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_OperationCS)


def test_minioclcs_operationcs_constructor_exists():
    assert callable(minioclcs_OperationCS.__init__)


def test_minioclcs_operationcs_constructor_args():
    sig = inspect.signature(minioclcs_OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs_operationcs_has_name():
    assert hasattr(minioclcs_OperationCS, "name")
    descriptor = None
    for klass in minioclcs_OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_PathElementCS)


def test_minioclcs_pathelementcs_constructor_exists():
    assert callable(minioclcs_PathElementCS.__init__)


def test_minioclcs_pathelementcs_constructor_args():
    sig = inspect.signature(minioclcs_PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_importcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_ImportCS)


def test_minioclcs_importcs_constructor_exists():
    assert callable(minioclcs_ImportCS.__init__)


def test_minioclcs_importcs_constructor_args():
    sig = inspect.signature(minioclcs_ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_minioclcs_importcs_has_alias():
    assert hasattr(minioclcs_ImportCS, "alias")
    descriptor = None
    for klass in minioclcs_ImportCS.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs_importcs_has_uri():
    assert hasattr(minioclcs_ImportCS, "uri")
    descriptor = None
    for klass in minioclcs_ImportCS.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_IteratorVarCS)


def test_minioclcs_iteratorvarcs_constructor_exists():
    assert callable(minioclcs_IteratorVarCS.__init__)


def test_minioclcs_iteratorvarcs_constructor_args():
    sig = inspect.signature(minioclcs_IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_minioclcs_iteratorvarcs_has_itName():
    assert hasattr(minioclcs_IteratorVarCS, "itName")
    descriptor = None
    for klass in minioclcs_IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs_expcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_ExpCS)


def test_minioclcs_expcs_constructor_exists():
    assert callable(minioclcs_ExpCS.__init__)


def test_minioclcs_expcs_constructor_args():
    sig = inspect.signature(minioclcs_ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs_rootcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs_RootCS)


def test_minioclcs_rootcs_constructor_exists():
    assert callable(minioclcs_RootCS.__init__)


def test_minioclcs_rootcs_constructor_args():
    sig = inspect.signature(minioclcs_RootCS.__init__)
    params = list(sig.parameters.keys())

def test_collectionkindcs_exists():
    # Check that the Enumeration exists
    assert CollectionKindCS is not None

def test_collectionkindcs_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKindCS]
    expected_literals = [
        "Collection",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKindCS"


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
minioclcs_EObject_strategy = st.builds(
    minioclcs_EObject,
)
minioclcs_CSTrace_strategy = st.builds(
    minioclcs_CSTrace,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
minioclcs_IntLiteralExpCS_strategy = st.builds(
    minioclcs_IntLiteralExpCS,
    intSymbol=
        st.integers()
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
minioclcs_BooleanExpCS_strategy = st.builds(
    minioclcs_BooleanExpCS,
    boolSymbol=
        st.booleans()
)
minioclcs_EClass_strategy = st.builds(
    minioclcs_EClass,
)
minioclcs_CollectionLiteralExpCS_strategy = st.builds(
    minioclcs_CollectionLiteralExpCS,
    kind=
        safe_text
)
minioclcs_NullLiteralExpCS_strategy = st.builds(
    minioclcs_NullLiteralExpCS,
)
minioclcs_BooleanLiteralExpCS_strategy = st.builds(
    minioclcs_BooleanLiteralExpCS,
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
minioclcs_IterateExpCS_strategy = st.builds(
    minioclcs_IterateExpCS,
)
minioclcs_CollectExpCS_strategy = st.builds(
    minioclcs_CollectExpCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
minioclcs_LoopExpCS_strategy = st.builds(
    minioclcs_LoopExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
minioclcs_LetExpCS_strategy = st.builds(
    minioclcs_LetExpCS,
)
minioclcs_LiteralExpCS_strategy = st.builds(
    minioclcs_LiteralExpCS,
)
minioclcs_NameExpCS_strategy = st.builds(
    minioclcs_NameExpCS,
)
minioclcs_SelfExpCS_strategy = st.builds(
    minioclcs_SelfExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
minioclcs_PrimaryExpCS_strategy = st.builds(
    minioclcs_PrimaryExpCS,
)
EqualityExpCS_strategy = st.builds(
    EqualityExpCS,
)
minioclcs_CallExpCS_strategy = st.builds(
    minioclcs_CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
minioclcs_EqualityExpCS_strategy = st.builds(
    minioclcs_EqualityExpCS,
    opName=
        safe_text
)
CSTrace_strategy = st.builds(
    CSTrace,
)
minioclcs_InvariantCS_strategy = st.builds(
    minioclcs_InvariantCS,
)
minioclcs_RoundedBracketClauseCS_strategy = st.builds(
    minioclcs_RoundedBracketClauseCS,
)
minioclcs_PropertyCS_strategy = st.builds(
    minioclcs_PropertyCS,
    name=
        safe_text
)
minioclcs_ParameterCS_strategy = st.builds(
    minioclcs_ParameterCS,
    name=
        safe_text
)
minioclcs_PathNameCS_strategy = st.builds(
    minioclcs_PathNameCS,
)
minioclcs_LetVarCS_strategy = st.builds(
    minioclcs_LetVarCS,
    name=
        safe_text
)
minioclcs_NavigationExpCS_strategy = st.builds(
    minioclcs_NavigationExpCS,
)
minioclcs_MultiplicityCS_strategy = st.builds(
    minioclcs_MultiplicityCS,
    mandatory=
        st.integers(),
    upperInt=
        st.integers(),
    mult=
        st.booleans(),
    upperMult=
        st.booleans(),
    opt=
        st.booleans(),
    lowerInt=
        st.integers()
)
minioclcs_AccVarCS_strategy = st.builds(
    minioclcs_AccVarCS,
    accName=
        safe_text
)
minioclcs_ClassCS_strategy = st.builds(
    minioclcs_ClassCS,
    name=
        safe_text
)
minioclcs_PackageCS_strategy = st.builds(
    minioclcs_PackageCS,
    name=
        safe_text
)
minioclcs_ConstraintsDefCS_strategy = st.builds(
    minioclcs_ConstraintsDefCS,
)
minioclcs_CollectionLiteralPartCS_strategy = st.builds(
    minioclcs_CollectionLiteralPartCS,
)
minioclcs_OperationCS_strategy = st.builds(
    minioclcs_OperationCS,
    name=
        safe_text
)
minioclcs_PathElementCS_strategy = st.builds(
    minioclcs_PathElementCS,
)
minioclcs_ImportCS_strategy = st.builds(
    minioclcs_ImportCS,
    alias=
        safe_text,
    uri=
        safe_text
)
minioclcs_IteratorVarCS_strategy = st.builds(
    minioclcs_IteratorVarCS,
    itName=
        safe_text
)
minioclcs_ExpCS_strategy = st.builds(
    minioclcs_ExpCS,
)
minioclcs_RootCS_strategy = st.builds(
    minioclcs_RootCS,
)

@given(instance=minioclcs_EObject_strategy)
@settings(max_examples=50)
def test_minioclcs_eobject_instantiation(instance):
    assert isinstance(instance, minioclcs_EObject)

@given(instance=minioclcs_CSTrace_strategy)
@settings(max_examples=50)
def test_minioclcs_cstrace_instantiation(instance):
    assert isinstance(instance, minioclcs_CSTrace)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=minioclcs_IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_intliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_IntLiteralExpCS)



@given(instance=minioclcs_IntLiteralExpCS_strategy)
def test_minioclcs_intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=minioclcs_BooleanExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_booleanexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_BooleanExpCS)



@given(instance=minioclcs_BooleanExpCS_strategy)
def test_minioclcs_booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=minioclcs_EClass_strategy)
@settings(max_examples=50)
def test_minioclcs_eclass_instantiation(instance):
    assert isinstance(instance, minioclcs_EClass)

@given(instance=minioclcs_CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectionLiteralExpCS)



@given(instance=minioclcs_CollectionLiteralExpCS_strategy)
def test_minioclcs_collectionliteralexpcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=minioclcs_NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_NullLiteralExpCS)

@given(instance=minioclcs_BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_BooleanLiteralExpCS)

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=minioclcs_IterateExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_iterateexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_IterateExpCS)

@given(instance=minioclcs_CollectExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_collectexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectExpCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=minioclcs_LoopExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_loopexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_LoopExpCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=minioclcs_LetExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_letexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_LetExpCS)

@given(instance=minioclcs_LiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_literalexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_LiteralExpCS)

@given(instance=minioclcs_NameExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_nameexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_NameExpCS)

@given(instance=minioclcs_SelfExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_selfexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_SelfExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=minioclcs_PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_primaryexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_PrimaryExpCS)

@given(instance=EqualityExpCS_strategy)
@settings(max_examples=50)
def test_equalityexpcs_instantiation(instance):
    assert isinstance(instance, EqualityExpCS)

@given(instance=minioclcs_CallExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_callexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=minioclcs_EqualityExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_equalityexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_EqualityExpCS)



@given(instance=minioclcs_EqualityExpCS_strategy)
def test_minioclcs_equalityexpcs_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=minioclcs_InvariantCS_strategy)
@settings(max_examples=50)
def test_minioclcs_invariantcs_instantiation(instance):
    assert isinstance(instance, minioclcs_InvariantCS)

@given(instance=minioclcs_RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_minioclcs_roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, minioclcs_RoundedBracketClauseCS)

@given(instance=minioclcs_PropertyCS_strategy)
@settings(max_examples=50)
def test_minioclcs_propertycs_instantiation(instance):
    assert isinstance(instance, minioclcs_PropertyCS)



@given(instance=minioclcs_PropertyCS_strategy)
def test_minioclcs_propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_ParameterCS_strategy)
@settings(max_examples=50)
def test_minioclcs_parametercs_instantiation(instance):
    assert isinstance(instance, minioclcs_ParameterCS)



@given(instance=minioclcs_ParameterCS_strategy)
def test_minioclcs_parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_PathNameCS_strategy)
@settings(max_examples=50)
def test_minioclcs_pathnamecs_instantiation(instance):
    assert isinstance(instance, minioclcs_PathNameCS)

@given(instance=minioclcs_LetVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs_letvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs_LetVarCS)



@given(instance=minioclcs_LetVarCS_strategy)
def test_minioclcs_letvarcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_NavigationExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_navigationexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs_NavigationExpCS)

@given(instance=minioclcs_MultiplicityCS_strategy)
@settings(max_examples=50)
def test_minioclcs_multiplicitycs_instantiation(instance):
    assert isinstance(instance, minioclcs_MultiplicityCS)



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_upperInt_setter(instance):
    original = instance.upperInt
    instance.upperInt = original
    assert instance.upperInt == original



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_mult_setter(instance):
    original = instance.mult
    instance.mult = original
    assert instance.mult == original



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_upperMult_setter(instance):
    original = instance.upperMult
    instance.upperMult = original
    assert instance.upperMult == original



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_opt_setter(instance):
    original = instance.opt
    instance.opt = original
    assert instance.opt == original



@given(instance=minioclcs_MultiplicityCS_strategy)
def test_minioclcs_multiplicitycs_lowerInt_setter(instance):
    original = instance.lowerInt
    instance.lowerInt = original
    assert instance.lowerInt == original

@given(instance=minioclcs_AccVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs_accvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs_AccVarCS)



@given(instance=minioclcs_AccVarCS_strategy)
def test_minioclcs_accvarcs_accName_setter(instance):
    original = instance.accName
    instance.accName = original
    assert instance.accName == original

@given(instance=minioclcs_ClassCS_strategy)
@settings(max_examples=50)
def test_minioclcs_classcs_instantiation(instance):
    assert isinstance(instance, minioclcs_ClassCS)



@given(instance=minioclcs_ClassCS_strategy)
def test_minioclcs_classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_PackageCS_strategy)
@settings(max_examples=50)
def test_minioclcs_packagecs_instantiation(instance):
    assert isinstance(instance, minioclcs_PackageCS)



@given(instance=minioclcs_PackageCS_strategy)
def test_minioclcs_packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_ConstraintsDefCS_strategy)
@settings(max_examples=50)
def test_minioclcs_constraintsdefcs_instantiation(instance):
    assert isinstance(instance, minioclcs_ConstraintsDefCS)

@given(instance=minioclcs_CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_minioclcs_collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, minioclcs_CollectionLiteralPartCS)

@given(instance=minioclcs_OperationCS_strategy)
@settings(max_examples=50)
def test_minioclcs_operationcs_instantiation(instance):
    assert isinstance(instance, minioclcs_OperationCS)



@given(instance=minioclcs_OperationCS_strategy)
def test_minioclcs_operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs_PathElementCS_strategy)
@settings(max_examples=50)
def test_minioclcs_pathelementcs_instantiation(instance):
    assert isinstance(instance, minioclcs_PathElementCS)

@given(instance=minioclcs_ImportCS_strategy)
@settings(max_examples=50)
def test_minioclcs_importcs_instantiation(instance):
    assert isinstance(instance, minioclcs_ImportCS)



@given(instance=minioclcs_ImportCS_strategy)
def test_minioclcs_importcs_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=minioclcs_ImportCS_strategy)
def test_minioclcs_importcs_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=minioclcs_IteratorVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs_iteratorvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs_IteratorVarCS)



@given(instance=minioclcs_IteratorVarCS_strategy)
def test_minioclcs_iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=minioclcs_ExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs_expcs_instantiation(instance):
    assert isinstance(instance, minioclcs_ExpCS)

@given(instance=minioclcs_RootCS_strategy)
@settings(max_examples=50)
def test_minioclcs_rootcs_instantiation(instance):
    assert isinstance(instance, minioclcs_RootCS)
