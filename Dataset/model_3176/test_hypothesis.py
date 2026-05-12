import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SJExpression,
    smallJava_SJStringConstant,
    smallJava_SJIntConstant,
    smallJava_SJNew,
    smallJava_SJBoolConstant,
    smallJava_SJNull,
    smallJava_SJMemberSelection,
    smallJava_SJSymbolRef,
    smallJava_SJThis,
    smallJava_SJAssignment,
    SJStatement,
    smallJava_SJIfStatement,
    smallJava_SJReturn,
    smallJava_SJExpression,
    smallJava_SJNamedElement,
    SJMember,
    smallJava_SJMethod,
    smallJava_SJField,
    SJNamedElement,
    smallJava_SJMember,
    smallJava_SJSymbol,
    smallJava_SJClass,
    smallJava_SJStatement,
    SJSymbol,
    smallJava_SJVariableDeclaration,
    smallJava_SJBlock,
    smallJava_SJParameter,
    smallJava_SJProgram,
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



def test_smalljava_sjstringconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJStringConstant)


def test_smalljava_sjstringconstant_constructor_exists():
    assert callable(smallJava_SJStringConstant.__init__)


def test_smalljava_sjstringconstant_constructor_args():
    sig = inspect.signature(smallJava_SJStringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava_sjstringconstant_has_value():
    assert hasattr(smallJava_SJStringConstant, "value")
    descriptor = None
    for klass in smallJava_SJStringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava_sjintconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJIntConstant)


def test_smalljava_sjintconstant_constructor_exists():
    assert callable(smallJava_SJIntConstant.__init__)


def test_smalljava_sjintconstant_constructor_args():
    sig = inspect.signature(smallJava_SJIntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava_sjintconstant_has_value():
    assert hasattr(smallJava_SJIntConstant, "value")
    descriptor = None
    for klass in smallJava_SJIntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava_sjnew_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNew)


def test_smalljava_sjnew_constructor_exists():
    assert callable(smallJava_SJNew.__init__)


def test_smalljava_sjnew_constructor_args():
    sig = inspect.signature(smallJava_SJNew.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjboolconstant_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJBoolConstant)


def test_smalljava_sjboolconstant_constructor_exists():
    assert callable(smallJava_SJBoolConstant.__init__)


def test_smalljava_sjboolconstant_constructor_args():
    sig = inspect.signature(smallJava_SJBoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_smalljava_sjboolconstant_has_value():
    assert hasattr(smallJava_SJBoolConstant, "value")
    descriptor = None
    for klass in smallJava_SJBoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_smalljava_sjnull_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNull)


def test_smalljava_sjnull_constructor_exists():
    assert callable(smallJava_SJNull.__init__)


def test_smalljava_sjnull_constructor_args():
    sig = inspect.signature(smallJava_SJNull.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjmemberselection_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMemberSelection)


def test_smalljava_sjmemberselection_constructor_exists():
    assert callable(smallJava_SJMemberSelection.__init__)


def test_smalljava_sjmemberselection_constructor_args():
    sig = inspect.signature(smallJava_SJMemberSelection.__init__)
    params = list(sig.parameters.keys())
    assert "methodinvocation" in params, "Missing parameter 'methodinvocation'"

def test_smalljava_sjmemberselection_has_methodinvocation():
    assert hasattr(smallJava_SJMemberSelection, "methodinvocation")
    descriptor = None
    for klass in smallJava_SJMemberSelection.__mro__:
        if "methodinvocation" in klass.__dict__:
            descriptor = klass.__dict__["methodinvocation"]
            break
    assert isinstance(descriptor, property)



def test_smalljava_sjsymbolref_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJSymbolRef)


def test_smalljava_sjsymbolref_constructor_exists():
    assert callable(smallJava_SJSymbolRef.__init__)


def test_smalljava_sjsymbolref_constructor_args():
    sig = inspect.signature(smallJava_SJSymbolRef.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjthis_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJThis)


def test_smalljava_sjthis_constructor_exists():
    assert callable(smallJava_SJThis.__init__)


def test_smalljava_sjthis_constructor_args():
    sig = inspect.signature(smallJava_SJThis.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjassignment_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJAssignment)


def test_smalljava_sjassignment_constructor_exists():
    assert callable(smallJava_SJAssignment.__init__)


def test_smalljava_sjassignment_constructor_args():
    sig = inspect.signature(smallJava_SJAssignment.__init__)
    params = list(sig.parameters.keys())



def test_sjstatement_is_not_abstract():
    assert not inspect.isabstract(SJStatement)


def test_sjstatement_constructor_exists():
    assert callable(SJStatement.__init__)


def test_sjstatement_constructor_args():
    sig = inspect.signature(SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjifstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJIfStatement)


def test_smalljava_sjifstatement_constructor_exists():
    assert callable(smallJava_SJIfStatement.__init__)


def test_smalljava_sjifstatement_constructor_args():
    sig = inspect.signature(smallJava_SJIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjreturn_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJReturn)


def test_smalljava_sjreturn_constructor_exists():
    assert callable(smallJava_SJReturn.__init__)


def test_smalljava_sjreturn_constructor_args():
    sig = inspect.signature(smallJava_SJReturn.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjexpression_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJExpression)


def test_smalljava_sjexpression_constructor_exists():
    assert callable(smallJava_SJExpression.__init__)


def test_smalljava_sjexpression_constructor_args():
    sig = inspect.signature(smallJava_SJExpression.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjnamedelement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJNamedElement)


def test_smalljava_sjnamedelement_constructor_exists():
    assert callable(smallJava_SJNamedElement.__init__)


def test_smalljava_sjnamedelement_constructor_args():
    sig = inspect.signature(smallJava_SJNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalljava_sjnamedelement_has_name():
    assert hasattr(smallJava_SJNamedElement, "name")
    descriptor = None
    for klass in smallJava_SJNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sjmember_is_not_abstract():
    assert not inspect.isabstract(SJMember)


def test_sjmember_constructor_exists():
    assert callable(SJMember.__init__)


def test_sjmember_constructor_args():
    sig = inspect.signature(SJMember.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjmethod_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMethod)


def test_smalljava_sjmethod_constructor_exists():
    assert callable(smallJava_SJMethod.__init__)


def test_smalljava_sjmethod_constructor_args():
    sig = inspect.signature(smallJava_SJMethod.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjfield_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJField)


def test_smalljava_sjfield_constructor_exists():
    assert callable(smallJava_SJField.__init__)


def test_smalljava_sjfield_constructor_args():
    sig = inspect.signature(smallJava_SJField.__init__)
    params = list(sig.parameters.keys())



def test_sjnamedelement_is_not_abstract():
    assert not inspect.isabstract(SJNamedElement)


def test_sjnamedelement_constructor_exists():
    assert callable(SJNamedElement.__init__)


def test_sjnamedelement_constructor_args():
    sig = inspect.signature(SJNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjmember_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJMember)


def test_smalljava_sjmember_constructor_exists():
    assert callable(smallJava_SJMember.__init__)


def test_smalljava_sjmember_constructor_args():
    sig = inspect.signature(smallJava_SJMember.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjsymbol_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJSymbol)


def test_smalljava_sjsymbol_constructor_exists():
    assert callable(smallJava_SJSymbol.__init__)


def test_smalljava_sjsymbol_constructor_args():
    sig = inspect.signature(smallJava_SJSymbol.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjclass_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJClass)


def test_smalljava_sjclass_constructor_exists():
    assert callable(smallJava_SJClass.__init__)


def test_smalljava_sjclass_constructor_args():
    sig = inspect.signature(smallJava_SJClass.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjstatement_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJStatement)


def test_smalljava_sjstatement_constructor_exists():
    assert callable(smallJava_SJStatement.__init__)


def test_smalljava_sjstatement_constructor_args():
    sig = inspect.signature(smallJava_SJStatement.__init__)
    params = list(sig.parameters.keys())



def test_sjsymbol_is_not_abstract():
    assert not inspect.isabstract(SJSymbol)


def test_sjsymbol_constructor_exists():
    assert callable(SJSymbol.__init__)


def test_sjsymbol_constructor_args():
    sig = inspect.signature(SJSymbol.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJVariableDeclaration)


def test_smalljava_sjvariabledeclaration_constructor_exists():
    assert callable(smallJava_SJVariableDeclaration.__init__)


def test_smalljava_sjvariabledeclaration_constructor_args():
    sig = inspect.signature(smallJava_SJVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjblock_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJBlock)


def test_smalljava_sjblock_constructor_exists():
    assert callable(smallJava_SJBlock.__init__)


def test_smalljava_sjblock_constructor_args():
    sig = inspect.signature(smallJava_SJBlock.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjparameter_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJParameter)


def test_smalljava_sjparameter_constructor_exists():
    assert callable(smallJava_SJParameter.__init__)


def test_smalljava_sjparameter_constructor_args():
    sig = inspect.signature(smallJava_SJParameter.__init__)
    params = list(sig.parameters.keys())



def test_smalljava_sjprogram_is_not_abstract():
    assert not inspect.isabstract(smallJava_SJProgram)


def test_smalljava_sjprogram_constructor_exists():
    assert callable(smallJava_SJProgram.__init__)


def test_smalljava_sjprogram_constructor_args():
    sig = inspect.signature(smallJava_SJProgram.__init__)
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
SJExpression_strategy = st.builds(
    SJExpression,
)
smallJava_SJStringConstant_strategy = st.builds(
    smallJava_SJStringConstant,
    value=
        safe_text
)
smallJava_SJIntConstant_strategy = st.builds(
    smallJava_SJIntConstant,
    value=
        st.integers()
)
smallJava_SJNew_strategy = st.builds(
    smallJava_SJNew,
)
smallJava_SJBoolConstant_strategy = st.builds(
    smallJava_SJBoolConstant,
    value=
        safe_text
)
smallJava_SJNull_strategy = st.builds(
    smallJava_SJNull,
)
smallJava_SJMemberSelection_strategy = st.builds(
    smallJava_SJMemberSelection,
    methodinvocation=
        st.booleans()
)
smallJava_SJSymbolRef_strategy = st.builds(
    smallJava_SJSymbolRef,
)
smallJava_SJThis_strategy = st.builds(
    smallJava_SJThis,
)
smallJava_SJAssignment_strategy = st.builds(
    smallJava_SJAssignment,
)
SJStatement_strategy = st.builds(
    SJStatement,
)
smallJava_SJIfStatement_strategy = st.builds(
    smallJava_SJIfStatement,
)
smallJava_SJReturn_strategy = st.builds(
    smallJava_SJReturn,
)
smallJava_SJExpression_strategy = st.builds(
    smallJava_SJExpression,
)
smallJava_SJNamedElement_strategy = st.builds(
    smallJava_SJNamedElement,
    name=
        safe_text
)
SJMember_strategy = st.builds(
    SJMember,
)
smallJava_SJMethod_strategy = st.builds(
    smallJava_SJMethod,
)
smallJava_SJField_strategy = st.builds(
    smallJava_SJField,
)
SJNamedElement_strategy = st.builds(
    SJNamedElement,
)
smallJava_SJMember_strategy = st.builds(
    smallJava_SJMember,
)
smallJava_SJSymbol_strategy = st.builds(
    smallJava_SJSymbol,
)
smallJava_SJClass_strategy = st.builds(
    smallJava_SJClass,
)
smallJava_SJStatement_strategy = st.builds(
    smallJava_SJStatement,
)
SJSymbol_strategy = st.builds(
    SJSymbol,
)
smallJava_SJVariableDeclaration_strategy = st.builds(
    smallJava_SJVariableDeclaration,
)
smallJava_SJBlock_strategy = st.builds(
    smallJava_SJBlock,
)
smallJava_SJParameter_strategy = st.builds(
    smallJava_SJParameter,
)
smallJava_SJProgram_strategy = st.builds(
    smallJava_SJProgram,
)

@given(instance=SJExpression_strategy)
@settings(max_examples=50)
def test_sjexpression_instantiation(instance):
    assert isinstance(instance, SJExpression)

@given(instance=smallJava_SJStringConstant_strategy)
@settings(max_examples=50)
def test_smalljava_sjstringconstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJStringConstant)



@given(instance=smallJava_SJStringConstant_strategy)
def test_smalljava_sjstringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava_SJIntConstant_strategy)
@settings(max_examples=50)
def test_smalljava_sjintconstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJIntConstant)



@given(instance=smallJava_SJIntConstant_strategy)
def test_smalljava_sjintconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava_SJNew_strategy)
@settings(max_examples=50)
def test_smalljava_sjnew_instantiation(instance):
    assert isinstance(instance, smallJava_SJNew)

@given(instance=smallJava_SJBoolConstant_strategy)
@settings(max_examples=50)
def test_smalljava_sjboolconstant_instantiation(instance):
    assert isinstance(instance, smallJava_SJBoolConstant)



@given(instance=smallJava_SJBoolConstant_strategy)
def test_smalljava_sjboolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=smallJava_SJNull_strategy)
@settings(max_examples=50)
def test_smalljava_sjnull_instantiation(instance):
    assert isinstance(instance, smallJava_SJNull)

@given(instance=smallJava_SJMemberSelection_strategy)
@settings(max_examples=50)
def test_smalljava_sjmemberselection_instantiation(instance):
    assert isinstance(instance, smallJava_SJMemberSelection)



@given(instance=smallJava_SJMemberSelection_strategy)
def test_smalljava_sjmemberselection_methodinvocation_setter(instance):
    original = instance.methodinvocation
    instance.methodinvocation = original
    assert instance.methodinvocation == original

@given(instance=smallJava_SJSymbolRef_strategy)
@settings(max_examples=50)
def test_smalljava_sjsymbolref_instantiation(instance):
    assert isinstance(instance, smallJava_SJSymbolRef)

@given(instance=smallJava_SJThis_strategy)
@settings(max_examples=50)
def test_smalljava_sjthis_instantiation(instance):
    assert isinstance(instance, smallJava_SJThis)

@given(instance=smallJava_SJAssignment_strategy)
@settings(max_examples=50)
def test_smalljava_sjassignment_instantiation(instance):
    assert isinstance(instance, smallJava_SJAssignment)

@given(instance=SJStatement_strategy)
@settings(max_examples=50)
def test_sjstatement_instantiation(instance):
    assert isinstance(instance, SJStatement)

@given(instance=smallJava_SJIfStatement_strategy)
@settings(max_examples=50)
def test_smalljava_sjifstatement_instantiation(instance):
    assert isinstance(instance, smallJava_SJIfStatement)

@given(instance=smallJava_SJReturn_strategy)
@settings(max_examples=50)
def test_smalljava_sjreturn_instantiation(instance):
    assert isinstance(instance, smallJava_SJReturn)

@given(instance=smallJava_SJExpression_strategy)
@settings(max_examples=50)
def test_smalljava_sjexpression_instantiation(instance):
    assert isinstance(instance, smallJava_SJExpression)

@given(instance=smallJava_SJNamedElement_strategy)
@settings(max_examples=50)
def test_smalljava_sjnamedelement_instantiation(instance):
    assert isinstance(instance, smallJava_SJNamedElement)



@given(instance=smallJava_SJNamedElement_strategy)
def test_smalljava_sjnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SJMember_strategy)
@settings(max_examples=50)
def test_sjmember_instantiation(instance):
    assert isinstance(instance, SJMember)

@given(instance=smallJava_SJMethod_strategy)
@settings(max_examples=50)
def test_smalljava_sjmethod_instantiation(instance):
    assert isinstance(instance, smallJava_SJMethod)

@given(instance=smallJava_SJField_strategy)
@settings(max_examples=50)
def test_smalljava_sjfield_instantiation(instance):
    assert isinstance(instance, smallJava_SJField)

@given(instance=SJNamedElement_strategy)
@settings(max_examples=50)
def test_sjnamedelement_instantiation(instance):
    assert isinstance(instance, SJNamedElement)

@given(instance=smallJava_SJMember_strategy)
@settings(max_examples=50)
def test_smalljava_sjmember_instantiation(instance):
    assert isinstance(instance, smallJava_SJMember)

@given(instance=smallJava_SJSymbol_strategy)
@settings(max_examples=50)
def test_smalljava_sjsymbol_instantiation(instance):
    assert isinstance(instance, smallJava_SJSymbol)

@given(instance=smallJava_SJClass_strategy)
@settings(max_examples=50)
def test_smalljava_sjclass_instantiation(instance):
    assert isinstance(instance, smallJava_SJClass)

@given(instance=smallJava_SJStatement_strategy)
@settings(max_examples=50)
def test_smalljava_sjstatement_instantiation(instance):
    assert isinstance(instance, smallJava_SJStatement)

@given(instance=SJSymbol_strategy)
@settings(max_examples=50)
def test_sjsymbol_instantiation(instance):
    assert isinstance(instance, SJSymbol)

@given(instance=smallJava_SJVariableDeclaration_strategy)
@settings(max_examples=50)
def test_smalljava_sjvariabledeclaration_instantiation(instance):
    assert isinstance(instance, smallJava_SJVariableDeclaration)

@given(instance=smallJava_SJBlock_strategy)
@settings(max_examples=50)
def test_smalljava_sjblock_instantiation(instance):
    assert isinstance(instance, smallJava_SJBlock)

@given(instance=smallJava_SJParameter_strategy)
@settings(max_examples=50)
def test_smalljava_sjparameter_instantiation(instance):
    assert isinstance(instance, smallJava_SJParameter)

@given(instance=smallJava_SJProgram_strategy)
@settings(max_examples=50)
def test_smalljava_sjprogram_instantiation(instance):
    assert isinstance(instance, smallJava_SJProgram)
