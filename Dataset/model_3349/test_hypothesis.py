import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SJExpression,
    smallJava::SJNull,
    smallJava::SJIntConstant,
    smallJava::SJStringConstant,
    smallJava::SJSuper,
    smallJava::SJMemberSelection,
    smallJava::SJSymbolRef,
    smallJava::SJBoolConstant,
    smallJava::SJNew,
    smallJava::SJThis,
    smallJava::SJAssignment,
    smallJava::SJSymbol,
    smallJava::SJBlock,
    smallJava::SJProgram,
    SJStatement,
    smallJava::SJExpression,
    smallJava::SJIfStatement,
    smallJava::SJReturn,
    smallJava::SJStatement,
    SJBlock,
    smallJava::SJIfBlock,
    SJSymbol,
    smallJava::SJVariableDeclaration,
    smallJava::SJMethodBody,
    smallJava::SJParameter,
    SJMember,
    smallJava::SJMethod,
    smallJava::SJField,
    smallJava::SJMember,
    smallJava::SJClass,
    smallJava::SJImport,
    SJAccessLevel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sjexpression_is_not_abstract():
    assert not inspect.isabstract(SJExpression)


def test_sjexpression_constructor_exists():
    assert callable(SJExpression.__init__)


def test_sjexpression_constructor_args():
    sig = inspect.signature(SJExpression.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjnull_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJNull)


def test_smalljava::sjnull_constructor_exists():
    assert callable(smallJava::SJNull.__init__)


def test_smalljava::sjnull_constructor_args():
    sig = inspect.signature(smallJava::SJNull.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjintconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJIntConstant)


def test_smalljava::sjintconstant_constructor_exists():
    assert callable(smallJava::SJIntConstant.__init__)


def test_smalljava::sjintconstant_constructor_args():
    sig = inspect.signature(smallJava::SJIntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava::sjintconstant_has_value():
    assert hasattr(smallJava::SJIntConstant, "value")
    descriptor = None
    for klass in smallJava::SJIntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjstringconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJStringConstant)


def test_smalljava::sjstringconstant_constructor_exists():
    assert callable(smallJava::SJStringConstant.__init__)


def test_smalljava::sjstringconstant_constructor_args():
    sig = inspect.signature(smallJava::SJStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava::sjstringconstant_has_value():
    assert hasattr(smallJava::SJStringConstant, "value")
    descriptor = None
    for klass in smallJava::SJStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjsuper_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJSuper)


def test_smalljava::sjsuper_constructor_exists():
    assert callable(smallJava::SJSuper.__init__)


def test_smalljava::sjsuper_constructor_args():
    sig = inspect.signature(smallJava::SJSuper.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjmemberselection_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJMemberSelection)


def test_smalljava::sjmemberselection_constructor_exists():
    assert callable(smallJava::SJMemberSelection.__init__)


def test_smalljava::sjmemberselection_constructor_args():
    sig = inspect.signature(smallJava::SJMemberSelection.__init__)
    params = list(sig.parameters.keys())
    assert "methodinvocation" in params, "Missing parameter 'methodinvocation'"

def test_smalljava::sjmemberselection_has_methodinvocation():
    assert hasattr(smallJava::SJMemberSelection, "methodinvocation")
    descriptor = None
    for klass in smallJava::SJMemberSelection.__mro__:
        if "methodinvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodinvocation"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjsymbolref_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJSymbolRef)


def test_smalljava::sjsymbolref_constructor_exists():
    assert callable(smallJava::SJSymbolRef.__init__)


def test_smalljava::sjsymbolref_constructor_args():
    sig = inspect.signature(smallJava::SJSymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjboolconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJBoolConstant)


def test_smalljava::sjboolconstant_constructor_exists():
    assert callable(smallJava::SJBoolConstant.__init__)


def test_smalljava::sjboolconstant_constructor_args():
    sig = inspect.signature(smallJava::SJBoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava::sjboolconstant_has_value():
    assert hasattr(smallJava::SJBoolConstant, "value")
    descriptor = None
    for klass in smallJava::SJBoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjnew_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJNew)


def test_smalljava::sjnew_constructor_exists():
    assert callable(smallJava::SJNew.__init__)


def test_smalljava::sjnew_constructor_args():
    sig = inspect.signature(smallJava::SJNew.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjthis_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJThis)


def test_smalljava::sjthis_constructor_exists():
    assert callable(smallJava::SJThis.__init__)


def test_smalljava::sjthis_constructor_args():
    sig = inspect.signature(smallJava::SJThis.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjassignment_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJAssignment)


def test_smalljava::sjassignment_constructor_exists():
    assert callable(smallJava::SJAssignment.__init__)


def test_smalljava::sjassignment_constructor_args():
    sig = inspect.signature(smallJava::SJAssignment.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjsymbol_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJSymbol)


def test_smalljava::sjsymbol_constructor_exists():
    assert callable(smallJava::SJSymbol.__init__)


def test_smalljava::sjsymbol_constructor_args():
    sig = inspect.signature(smallJava::SJSymbol.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalljava::sjsymbol_has_name():
    assert hasattr(smallJava::SJSymbol, "name")
    descriptor = None
    for klass in smallJava::SJSymbol.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjblock_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJBlock)


def test_smalljava::sjblock_constructor_exists():
    assert callable(smallJava::SJBlock.__init__)


def test_smalljava::sjblock_constructor_args():
    sig = inspect.signature(smallJava::SJBlock.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjprogram_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJProgram)


def test_smalljava::sjprogram_constructor_exists():
    assert callable(smallJava::SJProgram.__init__)


def test_smalljava::sjprogram_constructor_args():
    sig = inspect.signature(smallJava::SJProgram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalljava::sjprogram_has_name():
    assert hasattr(smallJava::SJProgram, "name")
    descriptor = None
    for klass in smallJava::SJProgram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sjstatement_is_not_abstract():
    assert not inspect.isabstract(SJStatement)


def test_sjstatement_constructor_exists():
    assert callable(SJStatement.__init__)


def test_sjstatement_constructor_args():
    sig = inspect.signature(SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjexpression_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJExpression)


def test_smalljava::sjexpression_constructor_exists():
    assert callable(smallJava::SJExpression.__init__)


def test_smalljava::sjexpression_constructor_args():
    sig = inspect.signature(smallJava::SJExpression.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjifstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJIfStatement)


def test_smalljava::sjifstatement_constructor_exists():
    assert callable(smallJava::SJIfStatement.__init__)


def test_smalljava::sjifstatement_constructor_args():
    sig = inspect.signature(smallJava::SJIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjreturn_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJReturn)


def test_smalljava::sjreturn_constructor_exists():
    assert callable(smallJava::SJReturn.__init__)


def test_smalljava::sjreturn_constructor_args():
    sig = inspect.signature(smallJava::SJReturn.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJStatement)


def test_smalljava::sjstatement_constructor_exists():
    assert callable(smallJava::SJStatement.__init__)


def test_smalljava::sjstatement_constructor_args():
    sig = inspect.signature(smallJava::SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_sjblock_is_not_abstract():
    assert not inspect.isabstract(SJBlock)


def test_sjblock_constructor_exists():
    assert callable(SJBlock.__init__)


def test_sjblock_constructor_args():
    sig = inspect.signature(SJBlock.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjifblock_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJIfBlock)


def test_smalljava::sjifblock_constructor_exists():
    assert callable(smallJava::SJIfBlock.__init__)


def test_smalljava::sjifblock_constructor_args():
    sig = inspect.signature(smallJava::SJIfBlock.__init__)
    params = list(sig.parameters.keys())



def test_sjsymbol_is_not_abstract():
    assert not inspect.isabstract(SJSymbol)


def test_sjsymbol_constructor_exists():
    assert callable(SJSymbol.__init__)


def test_sjsymbol_constructor_args():
    sig = inspect.signature(SJSymbol.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJVariableDeclaration)


def test_smalljava::sjvariabledeclaration_constructor_exists():
    assert callable(smallJava::SJVariableDeclaration.__init__)


def test_smalljava::sjvariabledeclaration_constructor_args():
    sig = inspect.signature(smallJava::SJVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjmethodbody_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJMethodBody)


def test_smalljava::sjmethodbody_constructor_exists():
    assert callable(smallJava::SJMethodBody.__init__)


def test_smalljava::sjmethodbody_constructor_args():
    sig = inspect.signature(smallJava::SJMethodBody.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjparameter_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJParameter)


def test_smalljava::sjparameter_constructor_exists():
    assert callable(smallJava::SJParameter.__init__)


def test_smalljava::sjparameter_constructor_args():
    sig = inspect.signature(smallJava::SJParameter.__init__)
    params = list(sig.parameters.keys())



def test_sjmember_is_not_abstract():
    assert not inspect.isabstract(SJMember)


def test_sjmember_constructor_exists():
    assert callable(SJMember.__init__)


def test_sjmember_constructor_args():
    sig = inspect.signature(SJMember.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjmethod_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJMethod)


def test_smalljava::sjmethod_constructor_exists():
    assert callable(smallJava::SJMethod.__init__)


def test_smalljava::sjmethod_constructor_args():
    sig = inspect.signature(smallJava::SJMethod.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjfield_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJField)


def test_smalljava::sjfield_constructor_exists():
    assert callable(smallJava::SJField.__init__)


def test_smalljava::sjfield_constructor_args():
    sig = inspect.signature(smallJava::SJField.__init__)
    params = list(sig.parameters.keys())



def test_smalljava::sjmember_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJMember)


def test_smalljava::sjmember_constructor_exists():
    assert callable(smallJava::SJMember.__init__)


def test_smalljava::sjmember_constructor_args():
    sig = inspect.signature(smallJava::SJMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "access" in params, "Missing parameter 'access'"

def test_smalljava::sjmember_has_name():
    assert hasattr(smallJava::SJMember, "name")
    descriptor = None
    for klass in smallJava::SJMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_smalljava::sjmember_has_access():
    assert hasattr(smallJava::SJMember, "access")
    descriptor = None
    for klass in smallJava::SJMember.__mro__:
        if "access" in klass.__dict__:
            descriptor = klass.__dict__["access"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjclass_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJClass)


def test_smalljava::sjclass_constructor_exists():
    assert callable(smallJava::SJClass.__init__)


def test_smalljava::sjclass_constructor_args():
    sig = inspect.signature(smallJava::SJClass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalljava::sjclass_has_name():
    assert hasattr(smallJava::SJClass, "name")
    descriptor = None
    for klass in smallJava::SJClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalljava::sjimport_is_not_abstract():
    assert not inspect.isabstract(smallJava::SJImport)


def test_smalljava::sjimport_constructor_exists():
    assert callable(smallJava::SJImport.__init__)


def test_smalljava::sjimport_constructor_args():
    sig = inspect.signature(smallJava::SJImport.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_smalljava::sjimport_has_importedNamespace():
    assert hasattr(smallJava::SJImport, "importedNamespace")
    descriptor = None
    for klass in smallJava::SJImport.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)

def test_sjaccesslevel_exists():
    # Check that the Enumeration exists
    assert SJAccessLevel is not None

def test_sjaccesslevel_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SJAccessLevel]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SJAccessLevel"


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
SJExpression_strategy = st.builds(
    SJExpression,
)
smallJava::SJNull_strategy = st.builds(
    smallJava::SJNull,
)
smallJava::SJIntConstant_strategy = st.builds(
    smallJava::SJIntConstant,
    value=
        st.integers()
)
smallJava::SJStringConstant_strategy = st.builds(
    smallJava::SJStringConstant,
    value=
        safe_text
)
smallJava::SJSuper_strategy = st.builds(
    smallJava::SJSuper,
)
smallJava::SJMemberSelection_strategy = st.builds(
    smallJava::SJMemberSelection,
    methodinvocation=
        st.booleans()
)
smallJava::SJSymbolRef_strategy = st.builds(
    smallJava::SJSymbolRef,
)
smallJava::SJBoolConstant_strategy = st.builds(
    smallJava::SJBoolConstant,
    value=
        safe_text
)
smallJava::SJNew_strategy = st.builds(
    smallJava::SJNew,
)
smallJava::SJThis_strategy = st.builds(
    smallJava::SJThis,
)
smallJava::SJAssignment_strategy = st.builds(
    smallJava::SJAssignment,
)
smallJava::SJSymbol_strategy = st.builds(
    smallJava::SJSymbol,
    name=
        safe_text
)
smallJava::SJBlock_strategy = st.builds(
    smallJava::SJBlock,
)
smallJava::SJProgram_strategy = st.builds(
    smallJava::SJProgram,
    name=
        safe_text
)
SJStatement_strategy = st.builds(
    SJStatement,
)
smallJava::SJExpression_strategy = st.builds(
    smallJava::SJExpression,
)
smallJava::SJIfStatement_strategy = st.builds(
    smallJava::SJIfStatement,
)
smallJava::SJReturn_strategy = st.builds(
    smallJava::SJReturn,
)
smallJava::SJStatement_strategy = st.builds(
    smallJava::SJStatement,
)
SJBlock_strategy = st.builds(
    SJBlock,
)
smallJava::SJIfBlock_strategy = st.builds(
    smallJava::SJIfBlock,
)
SJSymbol_strategy = st.builds(
    SJSymbol,
)
smallJava::SJVariableDeclaration_strategy = st.builds(
    smallJava::SJVariableDeclaration,
)
smallJava::SJMethodBody_strategy = st.builds(
    smallJava::SJMethodBody,
)
smallJava::SJParameter_strategy = st.builds(
    smallJava::SJParameter,
)
SJMember_strategy = st.builds(
    SJMember,
)
smallJava::SJMethod_strategy = st.builds(
    smallJava::SJMethod,
)
smallJava::SJField_strategy = st.builds(
    smallJava::SJField,
)
smallJava::SJMember_strategy = st.builds(
    smallJava::SJMember,
    name=
        safe_text,
    access=
        safe_text
)
smallJava::SJClass_strategy = st.builds(
    smallJava::SJClass,
    name=
        safe_text
)
smallJava::SJImport_strategy = st.builds(
    smallJava::SJImport,
    importedNamespace=
        safe_text
)

@given(instance=SJExpression_strategy)
@settings(max_examples=50)
def test_sjexpression_instantiation(instance):
    assert isinstance(instance, SJExpression)

@given(instance=smallJava::SJNull_strategy)
@settings(max_examples=50)
def test_smalljava::sjnull_instantiation(instance):
    assert isinstance(instance, smallJava::SJNull)

@given(instance=smallJava::SJIntConstant_strategy)
@settings(max_examples=50)
def test_smalljava::sjintconstant_instantiation(instance):
    assert isinstance(instance, smallJava::SJIntConstant)

@given(instance=smallJava::SJIntConstant_strategy)
def test_smalljava::sjintconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=smallJava::SJIntConstant_strategy)
def test_smalljava::sjintconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava::SJStringConstant_strategy)
@settings(max_examples=50)
def test_smalljava::sjstringconstant_instantiation(instance):
    assert isinstance(instance, smallJava::SJStringConstant)

@given(instance=smallJava::SJStringConstant_strategy)
def test_smalljava::sjstringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smallJava::SJStringConstant_strategy)
def test_smalljava::sjstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava::SJSuper_strategy)
@settings(max_examples=50)
def test_smalljava::sjsuper_instantiation(instance):
    assert isinstance(instance, smallJava::SJSuper)

@given(instance=smallJava::SJMemberSelection_strategy)
@settings(max_examples=50)
def test_smalljava::sjmemberselection_instantiation(instance):
    assert isinstance(instance, smallJava::SJMemberSelection)

@given(instance=smallJava::SJMemberSelection_strategy)
def test_smalljava::sjmemberselection_methodinvocation_type(instance):
    assert isinstance(instance.methodinvocation, bool)


@given(instance=smallJava::SJMemberSelection_strategy)
def test_smalljava::sjmemberselection_methodinvocation_setter(instance):
    original = instance.methodinvocation
    instance.methodinvocation = original
    assert instance.methodinvocation == original

@given(instance=smallJava::SJSymbolRef_strategy)
@settings(max_examples=50)
def test_smalljava::sjsymbolref_instantiation(instance):
    assert isinstance(instance, smallJava::SJSymbolRef)

@given(instance=smallJava::SJBoolConstant_strategy)
@settings(max_examples=50)
def test_smalljava::sjboolconstant_instantiation(instance):
    assert isinstance(instance, smallJava::SJBoolConstant)

@given(instance=smallJava::SJBoolConstant_strategy)
def test_smalljava::sjboolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=smallJava::SJBoolConstant_strategy)
def test_smalljava::sjboolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava::SJNew_strategy)
@settings(max_examples=50)
def test_smalljava::sjnew_instantiation(instance):
    assert isinstance(instance, smallJava::SJNew)

@given(instance=smallJava::SJThis_strategy)
@settings(max_examples=50)
def test_smalljava::sjthis_instantiation(instance):
    assert isinstance(instance, smallJava::SJThis)

@given(instance=smallJava::SJAssignment_strategy)
@settings(max_examples=50)
def test_smalljava::sjassignment_instantiation(instance):
    assert isinstance(instance, smallJava::SJAssignment)

@given(instance=smallJava::SJSymbol_strategy)
@settings(max_examples=50)
def test_smalljava::sjsymbol_instantiation(instance):
    assert isinstance(instance, smallJava::SJSymbol)

@given(instance=smallJava::SJSymbol_strategy)
def test_smalljava::sjsymbol_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smallJava::SJSymbol_strategy)
def test_smalljava::sjsymbol_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smallJava::SJBlock_strategy)
@settings(max_examples=50)
def test_smalljava::sjblock_instantiation(instance):
    assert isinstance(instance, smallJava::SJBlock)

@given(instance=smallJava::SJProgram_strategy)
@settings(max_examples=50)
def test_smalljava::sjprogram_instantiation(instance):
    assert isinstance(instance, smallJava::SJProgram)

@given(instance=smallJava::SJProgram_strategy)
def test_smalljava::sjprogram_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smallJava::SJProgram_strategy)
def test_smalljava::sjprogram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SJStatement_strategy)
@settings(max_examples=50)
def test_sjstatement_instantiation(instance):
    assert isinstance(instance, SJStatement)

@given(instance=smallJava::SJExpression_strategy)
@settings(max_examples=50)
def test_smalljava::sjexpression_instantiation(instance):
    assert isinstance(instance, smallJava::SJExpression)

@given(instance=smallJava::SJIfStatement_strategy)
@settings(max_examples=50)
def test_smalljava::sjifstatement_instantiation(instance):
    assert isinstance(instance, smallJava::SJIfStatement)

@given(instance=smallJava::SJReturn_strategy)
@settings(max_examples=50)
def test_smalljava::sjreturn_instantiation(instance):
    assert isinstance(instance, smallJava::SJReturn)

@given(instance=smallJava::SJStatement_strategy)
@settings(max_examples=50)
def test_smalljava::sjstatement_instantiation(instance):
    assert isinstance(instance, smallJava::SJStatement)

@given(instance=SJBlock_strategy)
@settings(max_examples=50)
def test_sjblock_instantiation(instance):
    assert isinstance(instance, SJBlock)

@given(instance=smallJava::SJIfBlock_strategy)
@settings(max_examples=50)
def test_smalljava::sjifblock_instantiation(instance):
    assert isinstance(instance, smallJava::SJIfBlock)

@given(instance=SJSymbol_strategy)
@settings(max_examples=50)
def test_sjsymbol_instantiation(instance):
    assert isinstance(instance, SJSymbol)

@given(instance=smallJava::SJVariableDeclaration_strategy)
@settings(max_examples=50)
def test_smalljava::sjvariabledeclaration_instantiation(instance):
    assert isinstance(instance, smallJava::SJVariableDeclaration)

@given(instance=smallJava::SJMethodBody_strategy)
@settings(max_examples=50)
def test_smalljava::sjmethodbody_instantiation(instance):
    assert isinstance(instance, smallJava::SJMethodBody)

@given(instance=smallJava::SJParameter_strategy)
@settings(max_examples=50)
def test_smalljava::sjparameter_instantiation(instance):
    assert isinstance(instance, smallJava::SJParameter)

@given(instance=SJMember_strategy)
@settings(max_examples=50)
def test_sjmember_instantiation(instance):
    assert isinstance(instance, SJMember)

@given(instance=smallJava::SJMethod_strategy)
@settings(max_examples=50)
def test_smalljava::sjmethod_instantiation(instance):
    assert isinstance(instance, smallJava::SJMethod)

@given(instance=smallJava::SJField_strategy)
@settings(max_examples=50)
def test_smalljava::sjfield_instantiation(instance):
    assert isinstance(instance, smallJava::SJField)

@given(instance=smallJava::SJMember_strategy)
@settings(max_examples=50)
def test_smalljava::sjmember_instantiation(instance):
    assert isinstance(instance, smallJava::SJMember)

@given(instance=smallJava::SJMember_strategy)
def test_smalljava::sjmember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smallJava::SJMember_strategy)
def test_smalljava::sjmember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smallJava::SJMember_strategy)
def test_smalljava::sjmember_access_type(instance):
    assert isinstance(instance.access, str)


@given(instance=smallJava::SJMember_strategy)
def test_smalljava::sjmember_access_setter(instance):
    original = instance.access
    instance.access = original
    assert instance.access == original

@given(instance=smallJava::SJClass_strategy)
@settings(max_examples=50)
def test_smalljava::sjclass_instantiation(instance):
    assert isinstance(instance, smallJava::SJClass)

@given(instance=smallJava::SJClass_strategy)
def test_smalljava::sjclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smallJava::SJClass_strategy)
def test_smalljava::sjclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smallJava::SJImport_strategy)
@settings(max_examples=50)
def test_smalljava::sjimport_instantiation(instance):
    assert isinstance(instance, smallJava::SJImport)

@given(instance=smallJava::SJImport_strategy)
def test_smalljava::sjimport_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=smallJava::SJImport_strategy)
def test_smalljava::sjimport_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original
