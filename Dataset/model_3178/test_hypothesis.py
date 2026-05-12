import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tym_EObject,
    tym_Model,
    tym_FunctionBlock,
    tym_Function,
    tym_Block,
    Expression,
    tym_Plus,
    tym_IntConstant,
    tym_Comparison,
    tym_BoolConstant,
    tym_StringConstant,
    tym_Equality,
    tym_And,
    tym_Not,
    tym_VariableRef,
    tym_MulOrDiv,
    tym_Minus,
    tym_Or,
    tym_Expression,
    AbstractElement,
    tym_PrintStatement,
    tym_FunctionCall,
    tym_LoopStatement,
    tym_TestStatement,
    tym_Return,
    tym_Variable,
    tym_AbstractElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tym_eobject_is_not_abstract():
    assert not inspect.isabstract(tym_EObject)


def test_tym_eobject_constructor_exists():
    assert callable(tym_EObject.__init__)


def test_tym_eobject_constructor_args():
    sig = inspect.signature(tym_EObject.__init__)
    params = list(sig.parameters.keys())



def test_tym_model_is_not_abstract():
    assert not inspect.isabstract(tym_Model)


def test_tym_model_constructor_exists():
    assert callable(tym_Model.__init__)


def test_tym_model_constructor_args():
    sig = inspect.signature(tym_Model.__init__)
    params = list(sig.parameters.keys())



def test_tym_functionblock_is_not_abstract():
    assert not inspect.isabstract(tym_FunctionBlock)


def test_tym_functionblock_constructor_exists():
    assert callable(tym_FunctionBlock.__init__)


def test_tym_functionblock_constructor_args():
    sig = inspect.signature(tym_FunctionBlock.__init__)
    params = list(sig.parameters.keys())



def test_tym_function_is_not_abstract():
    assert not inspect.isabstract(tym_Function)


def test_tym_function_constructor_exists():
    assert callable(tym_Function.__init__)


def test_tym_function_constructor_args():
    sig = inspect.signature(tym_Function.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "name" in params, "Missing parameter 'name'"

def test_tym_function_has_return_():
    assert hasattr(tym_Function, "return_")
    descriptor = None
    for klass in tym_Function.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_tym_function_has_name():
    assert hasattr(tym_Function, "name")
    descriptor = None
    for klass in tym_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tym_block_is_not_abstract():
    assert not inspect.isabstract(tym_Block)


def test_tym_block_constructor_exists():
    assert callable(tym_Block.__init__)


def test_tym_block_constructor_args():
    sig = inspect.signature(tym_Block.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_tym_plus_is_not_abstract():
    assert not inspect.isabstract(tym_Plus)


def test_tym_plus_constructor_exists():
    assert callable(tym_Plus.__init__)


def test_tym_plus_constructor_args():
    sig = inspect.signature(tym_Plus.__init__)
    params = list(sig.parameters.keys())



def test_tym_intconstant_is_not_abstract():
    assert not inspect.isabstract(tym_IntConstant)


def test_tym_intconstant_constructor_exists():
    assert callable(tym_IntConstant.__init__)


def test_tym_intconstant_constructor_args():
    sig = inspect.signature(tym_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym_intconstant_has_value():
    assert hasattr(tym_IntConstant, "value")
    descriptor = None
    for klass in tym_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym_comparison_is_not_abstract():
    assert not inspect.isabstract(tym_Comparison)


def test_tym_comparison_constructor_exists():
    assert callable(tym_Comparison.__init__)


def test_tym_comparison_constructor_args():
    sig = inspect.signature(tym_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym_comparison_has_op():
    assert hasattr(tym_Comparison, "op")
    descriptor = None
    for klass in tym_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym_boolconstant_is_not_abstract():
    assert not inspect.isabstract(tym_BoolConstant)


def test_tym_boolconstant_constructor_exists():
    assert callable(tym_BoolConstant.__init__)


def test_tym_boolconstant_constructor_args():
    sig = inspect.signature(tym_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym_boolconstant_has_value():
    assert hasattr(tym_BoolConstant, "value")
    descriptor = None
    for klass in tym_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym_stringconstant_is_not_abstract():
    assert not inspect.isabstract(tym_StringConstant)


def test_tym_stringconstant_constructor_exists():
    assert callable(tym_StringConstant.__init__)


def test_tym_stringconstant_constructor_args():
    sig = inspect.signature(tym_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym_stringconstant_has_value():
    assert hasattr(tym_StringConstant, "value")
    descriptor = None
    for klass in tym_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym_equality_is_not_abstract():
    assert not inspect.isabstract(tym_Equality)


def test_tym_equality_constructor_exists():
    assert callable(tym_Equality.__init__)


def test_tym_equality_constructor_args():
    sig = inspect.signature(tym_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym_equality_has_op():
    assert hasattr(tym_Equality, "op")
    descriptor = None
    for klass in tym_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym_and_is_not_abstract():
    assert not inspect.isabstract(tym_And)


def test_tym_and_constructor_exists():
    assert callable(tym_And.__init__)


def test_tym_and_constructor_args():
    sig = inspect.signature(tym_And.__init__)
    params = list(sig.parameters.keys())



def test_tym_not_is_not_abstract():
    assert not inspect.isabstract(tym_Not)


def test_tym_not_constructor_exists():
    assert callable(tym_Not.__init__)


def test_tym_not_constructor_args():
    sig = inspect.signature(tym_Not.__init__)
    params = list(sig.parameters.keys())



def test_tym_variableref_is_not_abstract():
    assert not inspect.isabstract(tym_VariableRef)


def test_tym_variableref_constructor_exists():
    assert callable(tym_VariableRef.__init__)


def test_tym_variableref_constructor_args():
    sig = inspect.signature(tym_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_tym_mulordiv_is_not_abstract():
    assert not inspect.isabstract(tym_MulOrDiv)


def test_tym_mulordiv_constructor_exists():
    assert callable(tym_MulOrDiv.__init__)


def test_tym_mulordiv_constructor_args():
    sig = inspect.signature(tym_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym_mulordiv_has_op():
    assert hasattr(tym_MulOrDiv, "op")
    descriptor = None
    for klass in tym_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym_minus_is_not_abstract():
    assert not inspect.isabstract(tym_Minus)


def test_tym_minus_constructor_exists():
    assert callable(tym_Minus.__init__)


def test_tym_minus_constructor_args():
    sig = inspect.signature(tym_Minus.__init__)
    params = list(sig.parameters.keys())



def test_tym_or_is_not_abstract():
    assert not inspect.isabstract(tym_Or)


def test_tym_or_constructor_exists():
    assert callable(tym_Or.__init__)


def test_tym_or_constructor_args():
    sig = inspect.signature(tym_Or.__init__)
    params = list(sig.parameters.keys())



def test_tym_expression_is_not_abstract():
    assert not inspect.isabstract(tym_Expression)


def test_tym_expression_constructor_exists():
    assert callable(tym_Expression.__init__)


def test_tym_expression_constructor_args():
    sig = inspect.signature(tym_Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_tym_printstatement_is_not_abstract():
    assert not inspect.isabstract(tym_PrintStatement)


def test_tym_printstatement_constructor_exists():
    assert callable(tym_PrintStatement.__init__)


def test_tym_printstatement_constructor_args():
    sig = inspect.signature(tym_PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym_functioncall_is_not_abstract():
    assert not inspect.isabstract(tym_FunctionCall)


def test_tym_functioncall_constructor_exists():
    assert callable(tym_FunctionCall.__init__)


def test_tym_functioncall_constructor_args():
    sig = inspect.signature(tym_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_tym_loopstatement_is_not_abstract():
    assert not inspect.isabstract(tym_LoopStatement)


def test_tym_loopstatement_constructor_exists():
    assert callable(tym_LoopStatement.__init__)


def test_tym_loopstatement_constructor_args():
    sig = inspect.signature(tym_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym_teststatement_is_not_abstract():
    assert not inspect.isabstract(tym_TestStatement)


def test_tym_teststatement_constructor_exists():
    assert callable(tym_TestStatement.__init__)


def test_tym_teststatement_constructor_args():
    sig = inspect.signature(tym_TestStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym_return_is_not_abstract():
    assert not inspect.isabstract(tym_Return)


def test_tym_return_constructor_exists():
    assert callable(tym_Return.__init__)


def test_tym_return_constructor_args():
    sig = inspect.signature(tym_Return.__init__)
    params = list(sig.parameters.keys())



def test_tym_variable_is_not_abstract():
    assert not inspect.isabstract(tym_Variable)


def test_tym_variable_constructor_exists():
    assert callable(tym_Variable.__init__)


def test_tym_variable_constructor_args():
    sig = inspect.signature(tym_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "vartype" in params, "Missing parameter 'vartype'"

def test_tym_variable_has_name():
    assert hasattr(tym_Variable, "name")
    descriptor = None
    for klass in tym_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tym_variable_has_vartype():
    assert hasattr(tym_Variable, "vartype")
    descriptor = None
    for klass in tym_Variable.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)



def test_tym_abstractelement_is_not_abstract():
    assert not inspect.isabstract(tym_AbstractElement)


def test_tym_abstractelement_constructor_exists():
    assert callable(tym_AbstractElement.__init__)


def test_tym_abstractelement_constructor_args():
    sig = inspect.signature(tym_AbstractElement.__init__)
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
tym_EObject_strategy = st.builds(
    tym_EObject,
)
tym_Model_strategy = st.builds(
    tym_Model,
)
tym_FunctionBlock_strategy = st.builds(
    tym_FunctionBlock,
)
tym_Function_strategy = st.builds(
    tym_Function,
    return_=
        safe_text,
    name=
        safe_text
)
tym_Block_strategy = st.builds(
    tym_Block,
)
Expression_strategy = st.builds(
    Expression,
)
tym_Plus_strategy = st.builds(
    tym_Plus,
)
tym_IntConstant_strategy = st.builds(
    tym_IntConstant,
    value=
        st.integers()
)
tym_Comparison_strategy = st.builds(
    tym_Comparison,
    op=
        safe_text
)
tym_BoolConstant_strategy = st.builds(
    tym_BoolConstant,
    value=
        safe_text
)
tym_StringConstant_strategy = st.builds(
    tym_StringConstant,
    value=
        safe_text
)
tym_Equality_strategy = st.builds(
    tym_Equality,
    op=
        safe_text
)
tym_And_strategy = st.builds(
    tym_And,
)
tym_Not_strategy = st.builds(
    tym_Not,
)
tym_VariableRef_strategy = st.builds(
    tym_VariableRef,
)
tym_MulOrDiv_strategy = st.builds(
    tym_MulOrDiv,
    op=
        safe_text
)
tym_Minus_strategy = st.builds(
    tym_Minus,
)
tym_Or_strategy = st.builds(
    tym_Or,
)
tym_Expression_strategy = st.builds(
    tym_Expression,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
tym_PrintStatement_strategy = st.builds(
    tym_PrintStatement,
)
tym_FunctionCall_strategy = st.builds(
    tym_FunctionCall,
)
tym_LoopStatement_strategy = st.builds(
    tym_LoopStatement,
)
tym_TestStatement_strategy = st.builds(
    tym_TestStatement,
)
tym_Return_strategy = st.builds(
    tym_Return,
)
tym_Variable_strategy = st.builds(
    tym_Variable,
    name=
        safe_text,
    vartype=
        safe_text
)
tym_AbstractElement_strategy = st.builds(
    tym_AbstractElement,
)

@given(instance=tym_EObject_strategy)
@settings(max_examples=50)
def test_tym_eobject_instantiation(instance):
    assert isinstance(instance, tym_EObject)

@given(instance=tym_Model_strategy)
@settings(max_examples=50)
def test_tym_model_instantiation(instance):
    assert isinstance(instance, tym_Model)

@given(instance=tym_FunctionBlock_strategy)
@settings(max_examples=50)
def test_tym_functionblock_instantiation(instance):
    assert isinstance(instance, tym_FunctionBlock)

@given(instance=tym_Function_strategy)
@settings(max_examples=50)
def test_tym_function_instantiation(instance):
    assert isinstance(instance, tym_Function)



@given(instance=tym_Function_strategy)
def test_tym_function_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original



@given(instance=tym_Function_strategy)
def test_tym_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tym_Block_strategy)
@settings(max_examples=50)
def test_tym_block_instantiation(instance):
    assert isinstance(instance, tym_Block)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=tym_Plus_strategy)
@settings(max_examples=50)
def test_tym_plus_instantiation(instance):
    assert isinstance(instance, tym_Plus)

@given(instance=tym_IntConstant_strategy)
@settings(max_examples=50)
def test_tym_intconstant_instantiation(instance):
    assert isinstance(instance, tym_IntConstant)



@given(instance=tym_IntConstant_strategy)
def test_tym_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym_Comparison_strategy)
@settings(max_examples=50)
def test_tym_comparison_instantiation(instance):
    assert isinstance(instance, tym_Comparison)



@given(instance=tym_Comparison_strategy)
def test_tym_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym_BoolConstant_strategy)
@settings(max_examples=50)
def test_tym_boolconstant_instantiation(instance):
    assert isinstance(instance, tym_BoolConstant)



@given(instance=tym_BoolConstant_strategy)
def test_tym_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym_StringConstant_strategy)
@settings(max_examples=50)
def test_tym_stringconstant_instantiation(instance):
    assert isinstance(instance, tym_StringConstant)



@given(instance=tym_StringConstant_strategy)
def test_tym_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym_Equality_strategy)
@settings(max_examples=50)
def test_tym_equality_instantiation(instance):
    assert isinstance(instance, tym_Equality)



@given(instance=tym_Equality_strategy)
def test_tym_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym_And_strategy)
@settings(max_examples=50)
def test_tym_and_instantiation(instance):
    assert isinstance(instance, tym_And)

@given(instance=tym_Not_strategy)
@settings(max_examples=50)
def test_tym_not_instantiation(instance):
    assert isinstance(instance, tym_Not)

@given(instance=tym_VariableRef_strategy)
@settings(max_examples=50)
def test_tym_variableref_instantiation(instance):
    assert isinstance(instance, tym_VariableRef)

@given(instance=tym_MulOrDiv_strategy)
@settings(max_examples=50)
def test_tym_mulordiv_instantiation(instance):
    assert isinstance(instance, tym_MulOrDiv)



@given(instance=tym_MulOrDiv_strategy)
def test_tym_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym_Minus_strategy)
@settings(max_examples=50)
def test_tym_minus_instantiation(instance):
    assert isinstance(instance, tym_Minus)

@given(instance=tym_Or_strategy)
@settings(max_examples=50)
def test_tym_or_instantiation(instance):
    assert isinstance(instance, tym_Or)

@given(instance=tym_Expression_strategy)
@settings(max_examples=50)
def test_tym_expression_instantiation(instance):
    assert isinstance(instance, tym_Expression)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=tym_PrintStatement_strategy)
@settings(max_examples=50)
def test_tym_printstatement_instantiation(instance):
    assert isinstance(instance, tym_PrintStatement)

@given(instance=tym_FunctionCall_strategy)
@settings(max_examples=50)
def test_tym_functioncall_instantiation(instance):
    assert isinstance(instance, tym_FunctionCall)

@given(instance=tym_LoopStatement_strategy)
@settings(max_examples=50)
def test_tym_loopstatement_instantiation(instance):
    assert isinstance(instance, tym_LoopStatement)

@given(instance=tym_TestStatement_strategy)
@settings(max_examples=50)
def test_tym_teststatement_instantiation(instance):
    assert isinstance(instance, tym_TestStatement)

@given(instance=tym_Return_strategy)
@settings(max_examples=50)
def test_tym_return_instantiation(instance):
    assert isinstance(instance, tym_Return)

@given(instance=tym_Variable_strategy)
@settings(max_examples=50)
def test_tym_variable_instantiation(instance):
    assert isinstance(instance, tym_Variable)



@given(instance=tym_Variable_strategy)
def test_tym_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=tym_Variable_strategy)
def test_tym_variable_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original

@given(instance=tym_AbstractElement_strategy)
@settings(max_examples=50)
def test_tym_abstractelement_instantiation(instance):
    assert isinstance(instance, tym_AbstractElement)
