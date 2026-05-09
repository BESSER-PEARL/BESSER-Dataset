import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minioclcs::EObject,
    minioclcs::CSTrace,
    LiteralExpCS,
    minioclcs::IntLiteralExpCS,
    BooleanLiteralExpCS,
    minioclcs::BooleanExpCS,
    minioclcs::EClass,
    minioclcs::CollectionLiteralExpCS,
    minioclcs::NullLiteralExpCS,
    minioclcs::BooleanLiteralExpCS,
    LoopExpCS,
    minioclcs::IterateExpCS,
    minioclcs::CollectExpCS,
    NavigationExpCS,
    minioclcs::LoopExpCS,
    PrimaryExpCS,
    minioclcs::NameExpCS,
    minioclcs::LiteralExpCS,
    minioclcs::LetExpCS,
    minioclcs::SelfExpCS,
    CallExpCS,
    minioclcs::PrimaryExpCS,
    EqualityExpCS,
    minioclcs::CallExpCS,
    ExpCS,
    minioclcs::EqualityExpCS,
    CSTrace,
    minioclcs::PackageCS,
    minioclcs::ExpCS,
    minioclcs::ConstraintsDefCS,
    minioclcs::MultiplicityCS,
    minioclcs::PropertyCS,
    minioclcs::AccVarCS,
    minioclcs::ClassCS,
    minioclcs::PathElementCS,
    minioclcs::CollectionLiteralPartCS,
    minioclcs::ImportCS,
    minioclcs::OperationCS,
    minioclcs::ParameterCS,
    minioclcs::InvariantCS,
    minioclcs::PathNameCS,
    minioclcs::RoundedBracketClauseCS,
    minioclcs::IteratorVarCS,
    minioclcs::LetVarCS,
    minioclcs::NavigationExpCS,
    minioclcs::RootCS,
    CollectionKindCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minioclcs::eobject_is_not_abstract():
    assert not inspect.isabstract(minioclcs::EObject)


def test_minioclcs::eobject_constructor_exists():
    assert callable(minioclcs::EObject.__init__)


def test_minioclcs::eobject_constructor_args():
    sig = inspect.signature(minioclcs::EObject.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::cstrace_is_not_abstract():
    assert not inspect.isabstract(minioclcs::CSTrace)


def test_minioclcs::cstrace_constructor_exists():
    assert callable(minioclcs::CSTrace.__init__)


def test_minioclcs::cstrace_constructor_args():
    sig = inspect.signature(minioclcs::CSTrace.__init__)
    params = list(sig.parameters.keys())



def test_literalexpcs_is_not_abstract():
    assert not inspect.isabstract(LiteralExpCS)


def test_literalexpcs_constructor_exists():
    assert callable(LiteralExpCS.__init__)


def test_literalexpcs_constructor_args():
    sig = inspect.signature(LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::intliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::IntLiteralExpCS)


def test_minioclcs::intliteralexpcs_constructor_exists():
    assert callable(minioclcs::IntLiteralExpCS.__init__)


def test_minioclcs::intliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs::IntLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "intSymbol" in params, "Missing parameter 'intSymbol'"

def test_minioclcs::intliteralexpcs_has_intSymbol():
    assert hasattr(minioclcs::IntLiteralExpCS, "intSymbol")
    descriptor = None
    for klass in minioclcs::IntLiteralExpCS.__mro__:
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



def test_minioclcs::booleanexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::BooleanExpCS)


def test_minioclcs::booleanexpcs_constructor_exists():
    assert callable(minioclcs::BooleanExpCS.__init__)


def test_minioclcs::booleanexpcs_constructor_args():
    sig = inspect.signature(minioclcs::BooleanExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "boolSymbol" in params, "Missing parameter 'boolSymbol'"

def test_minioclcs::booleanexpcs_has_boolSymbol():
    assert hasattr(minioclcs::BooleanExpCS, "boolSymbol")
    descriptor = None
    for klass in minioclcs::BooleanExpCS.__mro__:
        if "boolSymbol" in klass.__dict__:
            descriptor = klass.__dict__["boolSymbol"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::eclass_is_not_abstract():
    assert not inspect.isabstract(minioclcs::EClass)


def test_minioclcs::eclass_constructor_exists():
    assert callable(minioclcs::EClass.__init__)


def test_minioclcs::eclass_constructor_args():
    sig = inspect.signature(minioclcs::EClass.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::collectionliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::CollectionLiteralExpCS)


def test_minioclcs::collectionliteralexpcs_constructor_exists():
    assert callable(minioclcs::CollectionLiteralExpCS.__init__)


def test_minioclcs::collectionliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs::CollectionLiteralExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_minioclcs::collectionliteralexpcs_has_kind():
    assert hasattr(minioclcs::CollectionLiteralExpCS, "kind")
    descriptor = None
    for klass in minioclcs::CollectionLiteralExpCS.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::nullliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::NullLiteralExpCS)


def test_minioclcs::nullliteralexpcs_constructor_exists():
    assert callable(minioclcs::NullLiteralExpCS.__init__)


def test_minioclcs::nullliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs::NullLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::booleanliteralexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::BooleanLiteralExpCS)


def test_minioclcs::booleanliteralexpcs_constructor_exists():
    assert callable(minioclcs::BooleanLiteralExpCS.__init__)


def test_minioclcs::booleanliteralexpcs_constructor_args():
    sig = inspect.signature(minioclcs::BooleanLiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_loopexpcs_is_not_abstract():
    assert not inspect.isabstract(LoopExpCS)


def test_loopexpcs_constructor_exists():
    assert callable(LoopExpCS.__init__)


def test_loopexpcs_constructor_args():
    sig = inspect.signature(LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::iterateexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::IterateExpCS)


def test_minioclcs::iterateexpcs_constructor_exists():
    assert callable(minioclcs::IterateExpCS.__init__)


def test_minioclcs::iterateexpcs_constructor_args():
    sig = inspect.signature(minioclcs::IterateExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::collectexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::CollectExpCS)


def test_minioclcs::collectexpcs_constructor_exists():
    assert callable(minioclcs::CollectExpCS.__init__)


def test_minioclcs::collectexpcs_constructor_args():
    sig = inspect.signature(minioclcs::CollectExpCS.__init__)
    params = list(sig.parameters.keys())



def test_navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(NavigationExpCS)


def test_navigationexpcs_constructor_exists():
    assert callable(NavigationExpCS.__init__)


def test_navigationexpcs_constructor_args():
    sig = inspect.signature(NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::loopexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::LoopExpCS)


def test_minioclcs::loopexpcs_constructor_exists():
    assert callable(minioclcs::LoopExpCS.__init__)


def test_minioclcs::loopexpcs_constructor_args():
    sig = inspect.signature(minioclcs::LoopExpCS.__init__)
    params = list(sig.parameters.keys())



def test_primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpCS)


def test_primaryexpcs_constructor_exists():
    assert callable(PrimaryExpCS.__init__)


def test_primaryexpcs_constructor_args():
    sig = inspect.signature(PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::nameexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::NameExpCS)


def test_minioclcs::nameexpcs_constructor_exists():
    assert callable(minioclcs::NameExpCS.__init__)


def test_minioclcs::nameexpcs_constructor_args():
    sig = inspect.signature(minioclcs::NameExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::literalexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::LiteralExpCS)


def test_minioclcs::literalexpcs_constructor_exists():
    assert callable(minioclcs::LiteralExpCS.__init__)


def test_minioclcs::literalexpcs_constructor_args():
    sig = inspect.signature(minioclcs::LiteralExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::letexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::LetExpCS)


def test_minioclcs::letexpcs_constructor_exists():
    assert callable(minioclcs::LetExpCS.__init__)


def test_minioclcs::letexpcs_constructor_args():
    sig = inspect.signature(minioclcs::LetExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::selfexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::SelfExpCS)


def test_minioclcs::selfexpcs_constructor_exists():
    assert callable(minioclcs::SelfExpCS.__init__)


def test_minioclcs::selfexpcs_constructor_args():
    sig = inspect.signature(minioclcs::SelfExpCS.__init__)
    params = list(sig.parameters.keys())



def test_callexpcs_is_not_abstract():
    assert not inspect.isabstract(CallExpCS)


def test_callexpcs_constructor_exists():
    assert callable(CallExpCS.__init__)


def test_callexpcs_constructor_args():
    sig = inspect.signature(CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::primaryexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::PrimaryExpCS)


def test_minioclcs::primaryexpcs_constructor_exists():
    assert callable(minioclcs::PrimaryExpCS.__init__)


def test_minioclcs::primaryexpcs_constructor_args():
    sig = inspect.signature(minioclcs::PrimaryExpCS.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpcs_is_not_abstract():
    assert not inspect.isabstract(EqualityExpCS)


def test_equalityexpcs_constructor_exists():
    assert callable(EqualityExpCS.__init__)


def test_equalityexpcs_constructor_args():
    sig = inspect.signature(EqualityExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::callexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::CallExpCS)


def test_minioclcs::callexpcs_constructor_exists():
    assert callable(minioclcs::CallExpCS.__init__)


def test_minioclcs::callexpcs_constructor_args():
    sig = inspect.signature(minioclcs::CallExpCS.__init__)
    params = list(sig.parameters.keys())



def test_expcs_is_not_abstract():
    assert not inspect.isabstract(ExpCS)


def test_expcs_constructor_exists():
    assert callable(ExpCS.__init__)


def test_expcs_constructor_args():
    sig = inspect.signature(ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::equalityexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::EqualityExpCS)


def test_minioclcs::equalityexpcs_constructor_exists():
    assert callable(minioclcs::EqualityExpCS.__init__)


def test_minioclcs::equalityexpcs_constructor_args():
    sig = inspect.signature(minioclcs::EqualityExpCS.__init__)
    params = list(sig.parameters.keys())
    assert "opName" in params, "Missing parameter 'opName'"

def test_minioclcs::equalityexpcs_has_opName():
    assert hasattr(minioclcs::EqualityExpCS, "opName")
    descriptor = None
    for klass in minioclcs::EqualityExpCS.__mro__:
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



def test_minioclcs::packagecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::PackageCS)


def test_minioclcs::packagecs_constructor_exists():
    assert callable(minioclcs::PackageCS.__init__)


def test_minioclcs::packagecs_constructor_args():
    sig = inspect.signature(minioclcs::PackageCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::packagecs_has_name():
    assert hasattr(minioclcs::PackageCS, "name")
    descriptor = None
    for klass in minioclcs::PackageCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::expcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::ExpCS)


def test_minioclcs::expcs_constructor_exists():
    assert callable(minioclcs::ExpCS.__init__)


def test_minioclcs::expcs_constructor_args():
    sig = inspect.signature(minioclcs::ExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::constraintsdefcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::ConstraintsDefCS)


def test_minioclcs::constraintsdefcs_constructor_exists():
    assert callable(minioclcs::ConstraintsDefCS.__init__)


def test_minioclcs::constraintsdefcs_constructor_args():
    sig = inspect.signature(minioclcs::ConstraintsDefCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::multiplicitycs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::MultiplicityCS)


def test_minioclcs::multiplicitycs_constructor_exists():
    assert callable(minioclcs::MultiplicityCS.__init__)


def test_minioclcs::multiplicitycs_constructor_args():
    sig = inspect.signature(minioclcs::MultiplicityCS.__init__)
    params = list(sig.parameters.keys())
    assert "opt" in params, "Missing parameter 'opt'"
    assert "mandatory" in params, "Missing parameter 'mandatory'"
    assert "mult" in params, "Missing parameter 'mult'"
    assert "upperInt" in params, "Missing parameter 'upperInt'"
    assert "lowerInt" in params, "Missing parameter 'lowerInt'"
    assert "upperMult" in params, "Missing parameter 'upperMult'"

def test_minioclcs::multiplicitycs_has_opt():
    assert hasattr(minioclcs::MultiplicityCS, "opt")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "opt" in klass.__dict__:
            descriptor = klass.__dict__["opt"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::multiplicitycs_has_mandatory():
    assert hasattr(minioclcs::MultiplicityCS, "mandatory")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "mandatory" in klass.__dict__:
            descriptor = klass.__dict__["mandatory"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::multiplicitycs_has_mult():
    assert hasattr(minioclcs::MultiplicityCS, "mult")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "mult" in klass.__dict__:
            descriptor = klass.__dict__["mult"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::multiplicitycs_has_upperInt():
    assert hasattr(minioclcs::MultiplicityCS, "upperInt")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "upperInt" in klass.__dict__:
            descriptor = klass.__dict__["upperInt"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::multiplicitycs_has_lowerInt():
    assert hasattr(minioclcs::MultiplicityCS, "lowerInt")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "lowerInt" in klass.__dict__:
            descriptor = klass.__dict__["lowerInt"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::multiplicitycs_has_upperMult():
    assert hasattr(minioclcs::MultiplicityCS, "upperMult")
    descriptor = None
    for klass in minioclcs::MultiplicityCS.__mro__:
        if "upperMult" in klass.__dict__:
            descriptor = klass.__dict__["upperMult"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::propertycs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::PropertyCS)


def test_minioclcs::propertycs_constructor_exists():
    assert callable(minioclcs::PropertyCS.__init__)


def test_minioclcs::propertycs_constructor_args():
    sig = inspect.signature(minioclcs::PropertyCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::propertycs_has_name():
    assert hasattr(minioclcs::PropertyCS, "name")
    descriptor = None
    for klass in minioclcs::PropertyCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::accvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::AccVarCS)


def test_minioclcs::accvarcs_constructor_exists():
    assert callable(minioclcs::AccVarCS.__init__)


def test_minioclcs::accvarcs_constructor_args():
    sig = inspect.signature(minioclcs::AccVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "accName" in params, "Missing parameter 'accName'"

def test_minioclcs::accvarcs_has_accName():
    assert hasattr(minioclcs::AccVarCS, "accName")
    descriptor = None
    for klass in minioclcs::AccVarCS.__mro__:
        if "accName" in klass.__dict__:
            descriptor = klass.__dict__["accName"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::classcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::ClassCS)


def test_minioclcs::classcs_constructor_exists():
    assert callable(minioclcs::ClassCS.__init__)


def test_minioclcs::classcs_constructor_args():
    sig = inspect.signature(minioclcs::ClassCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::classcs_has_name():
    assert hasattr(minioclcs::ClassCS, "name")
    descriptor = None
    for klass in minioclcs::ClassCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::PathElementCS)


def test_minioclcs::pathelementcs_constructor_exists():
    assert callable(minioclcs::PathElementCS.__init__)


def test_minioclcs::pathelementcs_constructor_args():
    sig = inspect.signature(minioclcs::PathElementCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::collectionliteralpartcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::CollectionLiteralPartCS)


def test_minioclcs::collectionliteralpartcs_constructor_exists():
    assert callable(minioclcs::CollectionLiteralPartCS.__init__)


def test_minioclcs::collectionliteralpartcs_constructor_args():
    sig = inspect.signature(minioclcs::CollectionLiteralPartCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::importcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::ImportCS)


def test_minioclcs::importcs_constructor_exists():
    assert callable(minioclcs::ImportCS.__init__)


def test_minioclcs::importcs_constructor_args():
    sig = inspect.signature(minioclcs::ImportCS.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "uri" in params, "Missing parameter 'uri'"

def test_minioclcs::importcs_has_alias():
    assert hasattr(minioclcs::ImportCS, "alias")
    descriptor = None
    for klass in minioclcs::ImportCS.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_minioclcs::importcs_has_uri():
    assert hasattr(minioclcs::ImportCS, "uri")
    descriptor = None
    for klass in minioclcs::ImportCS.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::operationcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::OperationCS)


def test_minioclcs::operationcs_constructor_exists():
    assert callable(minioclcs::OperationCS.__init__)


def test_minioclcs::operationcs_constructor_args():
    sig = inspect.signature(minioclcs::OperationCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::operationcs_has_name():
    assert hasattr(minioclcs::OperationCS, "name")
    descriptor = None
    for klass in minioclcs::OperationCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::parametercs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::ParameterCS)


def test_minioclcs::parametercs_constructor_exists():
    assert callable(minioclcs::ParameterCS.__init__)


def test_minioclcs::parametercs_constructor_args():
    sig = inspect.signature(minioclcs::ParameterCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::parametercs_has_name():
    assert hasattr(minioclcs::ParameterCS, "name")
    descriptor = None
    for klass in minioclcs::ParameterCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::invariantcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::InvariantCS)


def test_minioclcs::invariantcs_constructor_exists():
    assert callable(minioclcs::InvariantCS.__init__)


def test_minioclcs::invariantcs_constructor_args():
    sig = inspect.signature(minioclcs::InvariantCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::PathNameCS)


def test_minioclcs::pathnamecs_constructor_exists():
    assert callable(minioclcs::PathNameCS.__init__)


def test_minioclcs::pathnamecs_constructor_args():
    sig = inspect.signature(minioclcs::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::roundedbracketclausecs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::RoundedBracketClauseCS)


def test_minioclcs::roundedbracketclausecs_constructor_exists():
    assert callable(minioclcs::RoundedBracketClauseCS.__init__)


def test_minioclcs::roundedbracketclausecs_constructor_args():
    sig = inspect.signature(minioclcs::RoundedBracketClauseCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::iteratorvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::IteratorVarCS)


def test_minioclcs::iteratorvarcs_constructor_exists():
    assert callable(minioclcs::IteratorVarCS.__init__)


def test_minioclcs::iteratorvarcs_constructor_args():
    sig = inspect.signature(minioclcs::IteratorVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "itName" in params, "Missing parameter 'itName'"

def test_minioclcs::iteratorvarcs_has_itName():
    assert hasattr(minioclcs::IteratorVarCS, "itName")
    descriptor = None
    for klass in minioclcs::IteratorVarCS.__mro__:
        if "itName" in klass.__dict__:
            descriptor = klass.__dict__["itName"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::letvarcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::LetVarCS)


def test_minioclcs::letvarcs_constructor_exists():
    assert callable(minioclcs::LetVarCS.__init__)


def test_minioclcs::letvarcs_constructor_args():
    sig = inspect.signature(minioclcs::LetVarCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minioclcs::letvarcs_has_name():
    assert hasattr(minioclcs::LetVarCS, "name")
    descriptor = None
    for klass in minioclcs::LetVarCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minioclcs::navigationexpcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::NavigationExpCS)


def test_minioclcs::navigationexpcs_constructor_exists():
    assert callable(minioclcs::NavigationExpCS.__init__)


def test_minioclcs::navigationexpcs_constructor_args():
    sig = inspect.signature(minioclcs::NavigationExpCS.__init__)
    params = list(sig.parameters.keys())



def test_minioclcs::rootcs_is_not_abstract():
    assert not inspect.isabstract(minioclcs::RootCS)


def test_minioclcs::rootcs_constructor_exists():
    assert callable(minioclcs::RootCS.__init__)


def test_minioclcs::rootcs_constructor_args():
    sig = inspect.signature(minioclcs::RootCS.__init__)
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
minioclcs::EObject_strategy = st.builds(
    minioclcs::EObject,
)
minioclcs::CSTrace_strategy = st.builds(
    minioclcs::CSTrace,
)
LiteralExpCS_strategy = st.builds(
    LiteralExpCS,
)
minioclcs::IntLiteralExpCS_strategy = st.builds(
    minioclcs::IntLiteralExpCS,
    intSymbol=
        st.integers()
)
BooleanLiteralExpCS_strategy = st.builds(
    BooleanLiteralExpCS,
)
minioclcs::BooleanExpCS_strategy = st.builds(
    minioclcs::BooleanExpCS,
    boolSymbol=
        st.booleans()
)
minioclcs::EClass_strategy = st.builds(
    minioclcs::EClass,
)
minioclcs::CollectionLiteralExpCS_strategy = st.builds(
    minioclcs::CollectionLiteralExpCS,
    kind=
        safe_text
)
minioclcs::NullLiteralExpCS_strategy = st.builds(
    minioclcs::NullLiteralExpCS,
)
minioclcs::BooleanLiteralExpCS_strategy = st.builds(
    minioclcs::BooleanLiteralExpCS,
)
LoopExpCS_strategy = st.builds(
    LoopExpCS,
)
minioclcs::IterateExpCS_strategy = st.builds(
    minioclcs::IterateExpCS,
)
minioclcs::CollectExpCS_strategy = st.builds(
    minioclcs::CollectExpCS,
)
NavigationExpCS_strategy = st.builds(
    NavigationExpCS,
)
minioclcs::LoopExpCS_strategy = st.builds(
    minioclcs::LoopExpCS,
)
PrimaryExpCS_strategy = st.builds(
    PrimaryExpCS,
)
minioclcs::NameExpCS_strategy = st.builds(
    minioclcs::NameExpCS,
)
minioclcs::LiteralExpCS_strategy = st.builds(
    minioclcs::LiteralExpCS,
)
minioclcs::LetExpCS_strategy = st.builds(
    minioclcs::LetExpCS,
)
minioclcs::SelfExpCS_strategy = st.builds(
    minioclcs::SelfExpCS,
)
CallExpCS_strategy = st.builds(
    CallExpCS,
)
minioclcs::PrimaryExpCS_strategy = st.builds(
    minioclcs::PrimaryExpCS,
)
EqualityExpCS_strategy = st.builds(
    EqualityExpCS,
)
minioclcs::CallExpCS_strategy = st.builds(
    minioclcs::CallExpCS,
)
ExpCS_strategy = st.builds(
    ExpCS,
)
minioclcs::EqualityExpCS_strategy = st.builds(
    minioclcs::EqualityExpCS,
    opName=
        safe_text
)
CSTrace_strategy = st.builds(
    CSTrace,
)
minioclcs::PackageCS_strategy = st.builds(
    minioclcs::PackageCS,
    name=
        safe_text
)
minioclcs::ExpCS_strategy = st.builds(
    minioclcs::ExpCS,
)
minioclcs::ConstraintsDefCS_strategy = st.builds(
    minioclcs::ConstraintsDefCS,
)
minioclcs::MultiplicityCS_strategy = st.builds(
    minioclcs::MultiplicityCS,
    opt=
        st.booleans(),
    mandatory=
        st.integers(),
    mult=
        st.booleans(),
    upperInt=
        st.integers(),
    lowerInt=
        st.integers(),
    upperMult=
        st.booleans()
)
minioclcs::PropertyCS_strategy = st.builds(
    minioclcs::PropertyCS,
    name=
        safe_text
)
minioclcs::AccVarCS_strategy = st.builds(
    minioclcs::AccVarCS,
    accName=
        safe_text
)
minioclcs::ClassCS_strategy = st.builds(
    minioclcs::ClassCS,
    name=
        safe_text
)
minioclcs::PathElementCS_strategy = st.builds(
    minioclcs::PathElementCS,
)
minioclcs::CollectionLiteralPartCS_strategy = st.builds(
    minioclcs::CollectionLiteralPartCS,
)
minioclcs::ImportCS_strategy = st.builds(
    minioclcs::ImportCS,
    alias=
        safe_text,
    uri=
        safe_text
)
minioclcs::OperationCS_strategy = st.builds(
    minioclcs::OperationCS,
    name=
        safe_text
)
minioclcs::ParameterCS_strategy = st.builds(
    minioclcs::ParameterCS,
    name=
        safe_text
)
minioclcs::InvariantCS_strategy = st.builds(
    minioclcs::InvariantCS,
)
minioclcs::PathNameCS_strategy = st.builds(
    minioclcs::PathNameCS,
)
minioclcs::RoundedBracketClauseCS_strategy = st.builds(
    minioclcs::RoundedBracketClauseCS,
)
minioclcs::IteratorVarCS_strategy = st.builds(
    minioclcs::IteratorVarCS,
    itName=
        safe_text
)
minioclcs::LetVarCS_strategy = st.builds(
    minioclcs::LetVarCS,
    name=
        safe_text
)
minioclcs::NavigationExpCS_strategy = st.builds(
    minioclcs::NavigationExpCS,
)
minioclcs::RootCS_strategy = st.builds(
    minioclcs::RootCS,
)

@given(instance=minioclcs::EObject_strategy)
@settings(max_examples=50)
def test_minioclcs::eobject_instantiation(instance):
    assert isinstance(instance, minioclcs::EObject)

@given(instance=minioclcs::CSTrace_strategy)
@settings(max_examples=50)
def test_minioclcs::cstrace_instantiation(instance):
    assert isinstance(instance, minioclcs::CSTrace)

@given(instance=LiteralExpCS_strategy)
@settings(max_examples=50)
def test_literalexpcs_instantiation(instance):
    assert isinstance(instance, LiteralExpCS)

@given(instance=minioclcs::IntLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::intliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::IntLiteralExpCS)

@given(instance=minioclcs::IntLiteralExpCS_strategy)
def test_minioclcs::intliteralexpcs_intSymbol_type(instance):
    assert isinstance(instance.intSymbol, int)


@given(instance=minioclcs::IntLiteralExpCS_strategy)
def test_minioclcs::intliteralexpcs_intSymbol_setter(instance):
    original = instance.intSymbol
    instance.intSymbol = original
    assert instance.intSymbol == original

@given(instance=BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, BooleanLiteralExpCS)

@given(instance=minioclcs::BooleanExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::booleanexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::BooleanExpCS)

@given(instance=minioclcs::BooleanExpCS_strategy)
def test_minioclcs::booleanexpcs_boolSymbol_type(instance):
    assert isinstance(instance.boolSymbol, bool)


@given(instance=minioclcs::BooleanExpCS_strategy)
def test_minioclcs::booleanexpcs_boolSymbol_setter(instance):
    original = instance.boolSymbol
    instance.boolSymbol = original
    assert instance.boolSymbol == original

@given(instance=minioclcs::EClass_strategy)
@settings(max_examples=50)
def test_minioclcs::eclass_instantiation(instance):
    assert isinstance(instance, minioclcs::EClass)

@given(instance=minioclcs::CollectionLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::collectionliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::CollectionLiteralExpCS)

@given(instance=minioclcs::CollectionLiteralExpCS_strategy)
def test_minioclcs::collectionliteralexpcs_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=minioclcs::CollectionLiteralExpCS_strategy)
def test_minioclcs::collectionliteralexpcs_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=minioclcs::NullLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::nullliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::NullLiteralExpCS)

@given(instance=minioclcs::BooleanLiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::booleanliteralexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::BooleanLiteralExpCS)

@given(instance=LoopExpCS_strategy)
@settings(max_examples=50)
def test_loopexpcs_instantiation(instance):
    assert isinstance(instance, LoopExpCS)

@given(instance=minioclcs::IterateExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::iterateexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::IterateExpCS)

@given(instance=minioclcs::CollectExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::collectexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::CollectExpCS)

@given(instance=NavigationExpCS_strategy)
@settings(max_examples=50)
def test_navigationexpcs_instantiation(instance):
    assert isinstance(instance, NavigationExpCS)

@given(instance=minioclcs::LoopExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::loopexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::LoopExpCS)

@given(instance=PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_primaryexpcs_instantiation(instance):
    assert isinstance(instance, PrimaryExpCS)

@given(instance=minioclcs::NameExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::nameexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::NameExpCS)

@given(instance=minioclcs::LiteralExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::literalexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::LiteralExpCS)

@given(instance=minioclcs::LetExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::letexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::LetExpCS)

@given(instance=minioclcs::SelfExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::selfexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::SelfExpCS)

@given(instance=CallExpCS_strategy)
@settings(max_examples=50)
def test_callexpcs_instantiation(instance):
    assert isinstance(instance, CallExpCS)

@given(instance=minioclcs::PrimaryExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::primaryexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::PrimaryExpCS)

@given(instance=EqualityExpCS_strategy)
@settings(max_examples=50)
def test_equalityexpcs_instantiation(instance):
    assert isinstance(instance, EqualityExpCS)

@given(instance=minioclcs::CallExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::callexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::CallExpCS)

@given(instance=ExpCS_strategy)
@settings(max_examples=50)
def test_expcs_instantiation(instance):
    assert isinstance(instance, ExpCS)

@given(instance=minioclcs::EqualityExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::equalityexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::EqualityExpCS)

@given(instance=minioclcs::EqualityExpCS_strategy)
def test_minioclcs::equalityexpcs_opName_type(instance):
    assert isinstance(instance.opName, str)


@given(instance=minioclcs::EqualityExpCS_strategy)
def test_minioclcs::equalityexpcs_opName_setter(instance):
    original = instance.opName
    instance.opName = original
    assert instance.opName == original

@given(instance=CSTrace_strategy)
@settings(max_examples=50)
def test_cstrace_instantiation(instance):
    assert isinstance(instance, CSTrace)

@given(instance=minioclcs::PackageCS_strategy)
@settings(max_examples=50)
def test_minioclcs::packagecs_instantiation(instance):
    assert isinstance(instance, minioclcs::PackageCS)

@given(instance=minioclcs::PackageCS_strategy)
def test_minioclcs::packagecs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::PackageCS_strategy)
def test_minioclcs::packagecs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::ExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::expcs_instantiation(instance):
    assert isinstance(instance, minioclcs::ExpCS)

@given(instance=minioclcs::ConstraintsDefCS_strategy)
@settings(max_examples=50)
def test_minioclcs::constraintsdefcs_instantiation(instance):
    assert isinstance(instance, minioclcs::ConstraintsDefCS)

@given(instance=minioclcs::MultiplicityCS_strategy)
@settings(max_examples=50)
def test_minioclcs::multiplicitycs_instantiation(instance):
    assert isinstance(instance, minioclcs::MultiplicityCS)

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_opt_type(instance):
    assert isinstance(instance.opt, bool)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_opt_setter(instance):
    original = instance.opt
    instance.opt = original
    assert instance.opt == original

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_mandatory_type(instance):
    assert isinstance(instance.mandatory, int)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_mandatory_setter(instance):
    original = instance.mandatory
    instance.mandatory = original
    assert instance.mandatory == original

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_mult_type(instance):
    assert isinstance(instance.mult, bool)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_mult_setter(instance):
    original = instance.mult
    instance.mult = original
    assert instance.mult == original

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_upperInt_type(instance):
    assert isinstance(instance.upperInt, int)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_upperInt_setter(instance):
    original = instance.upperInt
    instance.upperInt = original
    assert instance.upperInt == original

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_lowerInt_type(instance):
    assert isinstance(instance.lowerInt, int)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_lowerInt_setter(instance):
    original = instance.lowerInt
    instance.lowerInt = original
    assert instance.lowerInt == original

@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_upperMult_type(instance):
    assert isinstance(instance.upperMult, bool)


@given(instance=minioclcs::MultiplicityCS_strategy)
def test_minioclcs::multiplicitycs_upperMult_setter(instance):
    original = instance.upperMult
    instance.upperMult = original
    assert instance.upperMult == original

@given(instance=minioclcs::PropertyCS_strategy)
@settings(max_examples=50)
def test_minioclcs::propertycs_instantiation(instance):
    assert isinstance(instance, minioclcs::PropertyCS)

@given(instance=minioclcs::PropertyCS_strategy)
def test_minioclcs::propertycs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::PropertyCS_strategy)
def test_minioclcs::propertycs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::AccVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs::accvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs::AccVarCS)

@given(instance=minioclcs::AccVarCS_strategy)
def test_minioclcs::accvarcs_accName_type(instance):
    assert isinstance(instance.accName, str)


@given(instance=minioclcs::AccVarCS_strategy)
def test_minioclcs::accvarcs_accName_setter(instance):
    original = instance.accName
    instance.accName = original
    assert instance.accName == original

@given(instance=minioclcs::ClassCS_strategy)
@settings(max_examples=50)
def test_minioclcs::classcs_instantiation(instance):
    assert isinstance(instance, minioclcs::ClassCS)

@given(instance=minioclcs::ClassCS_strategy)
def test_minioclcs::classcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::ClassCS_strategy)
def test_minioclcs::classcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::PathElementCS_strategy)
@settings(max_examples=50)
def test_minioclcs::pathelementcs_instantiation(instance):
    assert isinstance(instance, minioclcs::PathElementCS)

@given(instance=minioclcs::CollectionLiteralPartCS_strategy)
@settings(max_examples=50)
def test_minioclcs::collectionliteralpartcs_instantiation(instance):
    assert isinstance(instance, minioclcs::CollectionLiteralPartCS)

@given(instance=minioclcs::ImportCS_strategy)
@settings(max_examples=50)
def test_minioclcs::importcs_instantiation(instance):
    assert isinstance(instance, minioclcs::ImportCS)

@given(instance=minioclcs::ImportCS_strategy)
def test_minioclcs::importcs_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=minioclcs::ImportCS_strategy)
def test_minioclcs::importcs_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=minioclcs::ImportCS_strategy)
def test_minioclcs::importcs_uri_type(instance):
    assert isinstance(instance.uri, str)


@given(instance=minioclcs::ImportCS_strategy)
def test_minioclcs::importcs_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=minioclcs::OperationCS_strategy)
@settings(max_examples=50)
def test_minioclcs::operationcs_instantiation(instance):
    assert isinstance(instance, minioclcs::OperationCS)

@given(instance=minioclcs::OperationCS_strategy)
def test_minioclcs::operationcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::OperationCS_strategy)
def test_minioclcs::operationcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::ParameterCS_strategy)
@settings(max_examples=50)
def test_minioclcs::parametercs_instantiation(instance):
    assert isinstance(instance, minioclcs::ParameterCS)

@given(instance=minioclcs::ParameterCS_strategy)
def test_minioclcs::parametercs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::ParameterCS_strategy)
def test_minioclcs::parametercs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::InvariantCS_strategy)
@settings(max_examples=50)
def test_minioclcs::invariantcs_instantiation(instance):
    assert isinstance(instance, minioclcs::InvariantCS)

@given(instance=minioclcs::PathNameCS_strategy)
@settings(max_examples=50)
def test_minioclcs::pathnamecs_instantiation(instance):
    assert isinstance(instance, minioclcs::PathNameCS)

@given(instance=minioclcs::RoundedBracketClauseCS_strategy)
@settings(max_examples=50)
def test_minioclcs::roundedbracketclausecs_instantiation(instance):
    assert isinstance(instance, minioclcs::RoundedBracketClauseCS)

@given(instance=minioclcs::IteratorVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs::iteratorvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs::IteratorVarCS)

@given(instance=minioclcs::IteratorVarCS_strategy)
def test_minioclcs::iteratorvarcs_itName_type(instance):
    assert isinstance(instance.itName, str)


@given(instance=minioclcs::IteratorVarCS_strategy)
def test_minioclcs::iteratorvarcs_itName_setter(instance):
    original = instance.itName
    instance.itName = original
    assert instance.itName == original

@given(instance=minioclcs::LetVarCS_strategy)
@settings(max_examples=50)
def test_minioclcs::letvarcs_instantiation(instance):
    assert isinstance(instance, minioclcs::LetVarCS)

@given(instance=minioclcs::LetVarCS_strategy)
def test_minioclcs::letvarcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=minioclcs::LetVarCS_strategy)
def test_minioclcs::letvarcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=minioclcs::NavigationExpCS_strategy)
@settings(max_examples=50)
def test_minioclcs::navigationexpcs_instantiation(instance):
    assert isinstance(instance, minioclcs::NavigationExpCS)

@given(instance=minioclcs::RootCS_strategy)
@settings(max_examples=50)
def test_minioclcs::rootcs_instantiation(instance):
    assert isinstance(instance, minioclcs::RootCS)
