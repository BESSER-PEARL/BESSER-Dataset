import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PrimaryExpression,
    cool_IsvoidExpression,
    cool_NegationExpression,
    cool_AssignmentExpression,
    cool_ConditionalExpression,
    cool_CaseExpression,
    cool_LoopExpression,
    cool_IntegerCompositeExpression,
    cool_NewExpression,
    cool_DispatchExpression,
    cool_BlockExpression,
    cool_LetExpression,
    cool_SelfTypeLiteral,
    Expression,
    cool_Minus,
    cool_MultiplicationExpression,
    cool_AdditionExpression,
    cool_Div,
    cool_CompareExpression,
    cool_PrimaryExpression,
    cool_Expression,
    Feature_,
    cool_Method,
    cool_Attr,
    cool_Type,
    IdentifiableElement,
    cool_Case,
    cool_Feature_,
    cool_LetDeclaration,
    cool_Formal,
    Type,
    cool_ParenExpression,
    Literal,
    cool_StringLiteral,
    cool_BooleanLiteral,
    cool_NumberLiteral,
    cool_Literal,
    cool_IdentifiableElement,
    cool_IdentifierRefExpression,
    cool_Class_,
    cool_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(PrimaryExpression)


def test_primaryexpression_constructor_exists():
    assert callable(PrimaryExpression.__init__)


def test_primaryexpression_constructor_args():
    sig = inspect.signature(PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_isvoidexpression_is_not_abstract():
    assert not inspect.isabstract(cool_IsvoidExpression)


def test_cool_isvoidexpression_constructor_exists():
    assert callable(cool_IsvoidExpression.__init__)


def test_cool_isvoidexpression_constructor_args():
    sig = inspect.signature(cool_IsvoidExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_negationexpression_is_not_abstract():
    assert not inspect.isabstract(cool_NegationExpression)


def test_cool_negationexpression_constructor_exists():
    assert callable(cool_NegationExpression.__init__)


def test_cool_negationexpression_constructor_args():
    sig = inspect.signature(cool_NegationExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(cool_AssignmentExpression)


def test_cool_assignmentexpression_constructor_exists():
    assert callable(cool_AssignmentExpression.__init__)


def test_cool_assignmentexpression_constructor_args():
    sig = inspect.signature(cool_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cool_assignmentexpression_has_name():
    assert hasattr(cool_AssignmentExpression, "name")
    descriptor = None
    for klass in cool_AssignmentExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cool_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(cool_ConditionalExpression)


def test_cool_conditionalexpression_constructor_exists():
    assert callable(cool_ConditionalExpression.__init__)


def test_cool_conditionalexpression_constructor_args():
    sig = inspect.signature(cool_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_caseexpression_is_not_abstract():
    assert not inspect.isabstract(cool_CaseExpression)


def test_cool_caseexpression_constructor_exists():
    assert callable(cool_CaseExpression.__init__)


def test_cool_caseexpression_constructor_args():
    sig = inspect.signature(cool_CaseExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_loopexpression_is_not_abstract():
    assert not inspect.isabstract(cool_LoopExpression)


def test_cool_loopexpression_constructor_exists():
    assert callable(cool_LoopExpression.__init__)


def test_cool_loopexpression_constructor_args():
    sig = inspect.signature(cool_LoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_integercompositeexpression_is_not_abstract():
    assert not inspect.isabstract(cool_IntegerCompositeExpression)


def test_cool_integercompositeexpression_constructor_exists():
    assert callable(cool_IntegerCompositeExpression.__init__)


def test_cool_integercompositeexpression_constructor_args():
    sig = inspect.signature(cool_IntegerCompositeExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_newexpression_is_not_abstract():
    assert not inspect.isabstract(cool_NewExpression)


def test_cool_newexpression_constructor_exists():
    assert callable(cool_NewExpression.__init__)


def test_cool_newexpression_constructor_args():
    sig = inspect.signature(cool_NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_dispatchexpression_is_not_abstract():
    assert not inspect.isabstract(cool_DispatchExpression)


def test_cool_dispatchexpression_constructor_exists():
    assert callable(cool_DispatchExpression.__init__)


def test_cool_dispatchexpression_constructor_args():
    sig = inspect.signature(cool_DispatchExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_blockexpression_is_not_abstract():
    assert not inspect.isabstract(cool_BlockExpression)


def test_cool_blockexpression_constructor_exists():
    assert callable(cool_BlockExpression.__init__)


def test_cool_blockexpression_constructor_args():
    sig = inspect.signature(cool_BlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_letexpression_is_not_abstract():
    assert not inspect.isabstract(cool_LetExpression)


def test_cool_letexpression_constructor_exists():
    assert callable(cool_LetExpression.__init__)


def test_cool_letexpression_constructor_args():
    sig = inspect.signature(cool_LetExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_selftypeliteral_is_not_abstract():
    assert not inspect.isabstract(cool_SelfTypeLiteral)


def test_cool_selftypeliteral_constructor_exists():
    assert callable(cool_SelfTypeLiteral.__init__)


def test_cool_selftypeliteral_constructor_args():
    sig = inspect.signature(cool_SelfTypeLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_cool_minus_is_not_abstract():
    assert not inspect.isabstract(cool_Minus)


def test_cool_minus_constructor_exists():
    assert callable(cool_Minus.__init__)


def test_cool_minus_constructor_args():
    sig = inspect.signature(cool_Minus.__init__)
    params = list(sig.parameters.keys())



def test_cool_multiplicationexpression_is_not_abstract():
    assert not inspect.isabstract(cool_MultiplicationExpression)


def test_cool_multiplicationexpression_constructor_exists():
    assert callable(cool_MultiplicationExpression.__init__)


def test_cool_multiplicationexpression_constructor_args():
    sig = inspect.signature(cool_MultiplicationExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_additionexpression_is_not_abstract():
    assert not inspect.isabstract(cool_AdditionExpression)


def test_cool_additionexpression_constructor_exists():
    assert callable(cool_AdditionExpression.__init__)


def test_cool_additionexpression_constructor_args():
    sig = inspect.signature(cool_AdditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_div_is_not_abstract():
    assert not inspect.isabstract(cool_Div)


def test_cool_div_constructor_exists():
    assert callable(cool_Div.__init__)


def test_cool_div_constructor_args():
    sig = inspect.signature(cool_Div.__init__)
    params = list(sig.parameters.keys())



def test_cool_compareexpression_is_not_abstract():
    assert not inspect.isabstract(cool_CompareExpression)


def test_cool_compareexpression_constructor_exists():
    assert callable(cool_CompareExpression.__init__)


def test_cool_compareexpression_constructor_args():
    sig = inspect.signature(cool_CompareExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_cool_compareexpression_has_op():
    assert hasattr(cool_CompareExpression, "op")
    descriptor = None
    for klass in cool_CompareExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_cool_primaryexpression_is_not_abstract():
    assert not inspect.isabstract(cool_PrimaryExpression)


def test_cool_primaryexpression_constructor_exists():
    assert callable(cool_PrimaryExpression.__init__)


def test_cool_primaryexpression_constructor_args():
    sig = inspect.signature(cool_PrimaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_expression_is_not_abstract():
    assert not inspect.isabstract(cool_Expression)


def test_cool_expression_constructor_exists():
    assert callable(cool_Expression.__init__)


def test_cool_expression_constructor_args():
    sig = inspect.signature(cool_Expression.__init__)
    params = list(sig.parameters.keys())



def test_feature__is_not_abstract():
    assert not inspect.isabstract(Feature_)


def test_feature__constructor_exists():
    assert callable(Feature_.__init__)


def test_feature__constructor_args():
    sig = inspect.signature(Feature_.__init__)
    params = list(sig.parameters.keys())



def test_cool_method_is_not_abstract():
    assert not inspect.isabstract(cool_Method)


def test_cool_method_constructor_exists():
    assert callable(cool_Method.__init__)


def test_cool_method_constructor_args():
    sig = inspect.signature(cool_Method.__init__)
    params = list(sig.parameters.keys())



def test_cool_attr_is_not_abstract():
    assert not inspect.isabstract(cool_Attr)


def test_cool_attr_constructor_exists():
    assert callable(cool_Attr.__init__)


def test_cool_attr_constructor_args():
    sig = inspect.signature(cool_Attr.__init__)
    params = list(sig.parameters.keys())



def test_cool_type_is_not_abstract():
    assert not inspect.isabstract(cool_Type)


def test_cool_type_constructor_exists():
    assert callable(cool_Type.__init__)


def test_cool_type_constructor_args():
    sig = inspect.signature(cool_Type.__init__)
    params = list(sig.parameters.keys())



def test_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(IdentifiableElement)


def test_identifiableelement_constructor_exists():
    assert callable(IdentifiableElement.__init__)


def test_identifiableelement_constructor_args():
    sig = inspect.signature(IdentifiableElement.__init__)
    params = list(sig.parameters.keys())



def test_cool_case_is_not_abstract():
    assert not inspect.isabstract(cool_Case)


def test_cool_case_constructor_exists():
    assert callable(cool_Case.__init__)


def test_cool_case_constructor_args():
    sig = inspect.signature(cool_Case.__init__)
    params = list(sig.parameters.keys())



def test_cool_feature__is_not_abstract():
    assert not inspect.isabstract(cool_Feature_)


def test_cool_feature__constructor_exists():
    assert callable(cool_Feature_.__init__)


def test_cool_feature__constructor_args():
    sig = inspect.signature(cool_Feature_.__init__)
    params = list(sig.parameters.keys())



def test_cool_letdeclaration_is_not_abstract():
    assert not inspect.isabstract(cool_LetDeclaration)


def test_cool_letdeclaration_constructor_exists():
    assert callable(cool_LetDeclaration.__init__)


def test_cool_letdeclaration_constructor_args():
    sig = inspect.signature(cool_LetDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_cool_formal_is_not_abstract():
    assert not inspect.isabstract(cool_Formal)


def test_cool_formal_constructor_exists():
    assert callable(cool_Formal.__init__)


def test_cool_formal_constructor_args():
    sig = inspect.signature(cool_Formal.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_cool_parenexpression_is_not_abstract():
    assert not inspect.isabstract(cool_ParenExpression)


def test_cool_parenexpression_constructor_exists():
    assert callable(cool_ParenExpression.__init__)


def test_cool_parenexpression_constructor_args():
    sig = inspect.signature(cool_ParenExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_cool_stringliteral_is_not_abstract():
    assert not inspect.isabstract(cool_StringLiteral)


def test_cool_stringliteral_constructor_exists():
    assert callable(cool_StringLiteral.__init__)


def test_cool_stringliteral_constructor_args():
    sig = inspect.signature(cool_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool_stringliteral_has_value():
    assert hasattr(cool_StringLiteral, "value")
    descriptor = None
    for klass in cool_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(cool_BooleanLiteral)


def test_cool_booleanliteral_constructor_exists():
    assert callable(cool_BooleanLiteral.__init__)


def test_cool_booleanliteral_constructor_args():
    sig = inspect.signature(cool_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool_booleanliteral_has_value():
    assert hasattr(cool_BooleanLiteral, "value")
    descriptor = None
    for klass in cool_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool_numberliteral_is_not_abstract():
    assert not inspect.isabstract(cool_NumberLiteral)


def test_cool_numberliteral_constructor_exists():
    assert callable(cool_NumberLiteral.__init__)


def test_cool_numberliteral_constructor_args():
    sig = inspect.signature(cool_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cool_numberliteral_has_value():
    assert hasattr(cool_NumberLiteral, "value")
    descriptor = None
    for klass in cool_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cool_literal_is_not_abstract():
    assert not inspect.isabstract(cool_Literal)


def test_cool_literal_constructor_exists():
    assert callable(cool_Literal.__init__)


def test_cool_literal_constructor_args():
    sig = inspect.signature(cool_Literal.__init__)
    params = list(sig.parameters.keys())



def test_cool_identifiableelement_is_not_abstract():
    assert not inspect.isabstract(cool_IdentifiableElement)


def test_cool_identifiableelement_constructor_exists():
    assert callable(cool_IdentifiableElement.__init__)


def test_cool_identifiableelement_constructor_args():
    sig = inspect.signature(cool_IdentifiableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cool_identifiableelement_has_name():
    assert hasattr(cool_IdentifiableElement, "name")
    descriptor = None
    for klass in cool_IdentifiableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cool_identifierrefexpression_is_not_abstract():
    assert not inspect.isabstract(cool_IdentifierRefExpression)


def test_cool_identifierrefexpression_constructor_exists():
    assert callable(cool_IdentifierRefExpression.__init__)


def test_cool_identifierrefexpression_constructor_args():
    sig = inspect.signature(cool_IdentifierRefExpression.__init__)
    params = list(sig.parameters.keys())



def test_cool_class__is_not_abstract():
    assert not inspect.isabstract(cool_Class_)


def test_cool_class__constructor_exists():
    assert callable(cool_Class_.__init__)


def test_cool_class__constructor_args():
    sig = inspect.signature(cool_Class_.__init__)
    params = list(sig.parameters.keys())



def test_cool_program_is_not_abstract():
    assert not inspect.isabstract(cool_Program)


def test_cool_program_constructor_exists():
    assert callable(cool_Program.__init__)


def test_cool_program_constructor_args():
    sig = inspect.signature(cool_Program.__init__)
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
PrimaryExpression_strategy = st.builds(
    PrimaryExpression,
)
cool_IsvoidExpression_strategy = st.builds(
    cool_IsvoidExpression,
)
cool_NegationExpression_strategy = st.builds(
    cool_NegationExpression,
)
cool_AssignmentExpression_strategy = st.builds(
    cool_AssignmentExpression,
    name=
        safe_text
)
cool_ConditionalExpression_strategy = st.builds(
    cool_ConditionalExpression,
)
cool_CaseExpression_strategy = st.builds(
    cool_CaseExpression,
)
cool_LoopExpression_strategy = st.builds(
    cool_LoopExpression,
)
cool_IntegerCompositeExpression_strategy = st.builds(
    cool_IntegerCompositeExpression,
)
cool_NewExpression_strategy = st.builds(
    cool_NewExpression,
)
cool_DispatchExpression_strategy = st.builds(
    cool_DispatchExpression,
)
cool_BlockExpression_strategy = st.builds(
    cool_BlockExpression,
)
cool_LetExpression_strategy = st.builds(
    cool_LetExpression,
)
cool_SelfTypeLiteral_strategy = st.builds(
    cool_SelfTypeLiteral,
)
Expression_strategy = st.builds(
    Expression,
)
cool_Minus_strategy = st.builds(
    cool_Minus,
)
cool_MultiplicationExpression_strategy = st.builds(
    cool_MultiplicationExpression,
)
cool_AdditionExpression_strategy = st.builds(
    cool_AdditionExpression,
)
cool_Div_strategy = st.builds(
    cool_Div,
)
cool_CompareExpression_strategy = st.builds(
    cool_CompareExpression,
    op=
        safe_text
)
cool_PrimaryExpression_strategy = st.builds(
    cool_PrimaryExpression,
)
cool_Expression_strategy = st.builds(
    cool_Expression,
)
Feature__strategy = st.builds(
    Feature_,
)
cool_Method_strategy = st.builds(
    cool_Method,
)
cool_Attr_strategy = st.builds(
    cool_Attr,
)
cool_Type_strategy = st.builds(
    cool_Type,
)
IdentifiableElement_strategy = st.builds(
    IdentifiableElement,
)
cool_Case_strategy = st.builds(
    cool_Case,
)
cool_Feature__strategy = st.builds(
    cool_Feature_,
)
cool_LetDeclaration_strategy = st.builds(
    cool_LetDeclaration,
)
cool_Formal_strategy = st.builds(
    cool_Formal,
)
Type_strategy = st.builds(
    Type,
)
cool_ParenExpression_strategy = st.builds(
    cool_ParenExpression,
)
Literal_strategy = st.builds(
    Literal,
)
cool_StringLiteral_strategy = st.builds(
    cool_StringLiteral,
    value=
        safe_text
)
cool_BooleanLiteral_strategy = st.builds(
    cool_BooleanLiteral,
    value=
        safe_text
)
cool_NumberLiteral_strategy = st.builds(
    cool_NumberLiteral,
    value=
        st.integers()
)
cool_Literal_strategy = st.builds(
    cool_Literal,
)
cool_IdentifiableElement_strategy = st.builds(
    cool_IdentifiableElement,
    name=
        safe_text
)
cool_IdentifierRefExpression_strategy = st.builds(
    cool_IdentifierRefExpression,
)
cool_Class__strategy = st.builds(
    cool_Class_,
)
cool_Program_strategy = st.builds(
    cool_Program,
)

@given(instance=PrimaryExpression_strategy)
@settings(max_examples=50)
def test_primaryexpression_instantiation(instance):
    assert isinstance(instance, PrimaryExpression)

@given(instance=cool_IsvoidExpression_strategy)
@settings(max_examples=50)
def test_cool_isvoidexpression_instantiation(instance):
    assert isinstance(instance, cool_IsvoidExpression)

@given(instance=cool_NegationExpression_strategy)
@settings(max_examples=50)
def test_cool_negationexpression_instantiation(instance):
    assert isinstance(instance, cool_NegationExpression)

@given(instance=cool_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_cool_assignmentexpression_instantiation(instance):
    assert isinstance(instance, cool_AssignmentExpression)



@given(instance=cool_AssignmentExpression_strategy)
def test_cool_assignmentexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cool_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_cool_conditionalexpression_instantiation(instance):
    assert isinstance(instance, cool_ConditionalExpression)

@given(instance=cool_CaseExpression_strategy)
@settings(max_examples=50)
def test_cool_caseexpression_instantiation(instance):
    assert isinstance(instance, cool_CaseExpression)

@given(instance=cool_LoopExpression_strategy)
@settings(max_examples=50)
def test_cool_loopexpression_instantiation(instance):
    assert isinstance(instance, cool_LoopExpression)

@given(instance=cool_IntegerCompositeExpression_strategy)
@settings(max_examples=50)
def test_cool_integercompositeexpression_instantiation(instance):
    assert isinstance(instance, cool_IntegerCompositeExpression)

@given(instance=cool_NewExpression_strategy)
@settings(max_examples=50)
def test_cool_newexpression_instantiation(instance):
    assert isinstance(instance, cool_NewExpression)

@given(instance=cool_DispatchExpression_strategy)
@settings(max_examples=50)
def test_cool_dispatchexpression_instantiation(instance):
    assert isinstance(instance, cool_DispatchExpression)

@given(instance=cool_BlockExpression_strategy)
@settings(max_examples=50)
def test_cool_blockexpression_instantiation(instance):
    assert isinstance(instance, cool_BlockExpression)

@given(instance=cool_LetExpression_strategy)
@settings(max_examples=50)
def test_cool_letexpression_instantiation(instance):
    assert isinstance(instance, cool_LetExpression)

@given(instance=cool_SelfTypeLiteral_strategy)
@settings(max_examples=50)
def test_cool_selftypeliteral_instantiation(instance):
    assert isinstance(instance, cool_SelfTypeLiteral)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=cool_Minus_strategy)
@settings(max_examples=50)
def test_cool_minus_instantiation(instance):
    assert isinstance(instance, cool_Minus)

@given(instance=cool_MultiplicationExpression_strategy)
@settings(max_examples=50)
def test_cool_multiplicationexpression_instantiation(instance):
    assert isinstance(instance, cool_MultiplicationExpression)

@given(instance=cool_AdditionExpression_strategy)
@settings(max_examples=50)
def test_cool_additionexpression_instantiation(instance):
    assert isinstance(instance, cool_AdditionExpression)

@given(instance=cool_Div_strategy)
@settings(max_examples=50)
def test_cool_div_instantiation(instance):
    assert isinstance(instance, cool_Div)

@given(instance=cool_CompareExpression_strategy)
@settings(max_examples=50)
def test_cool_compareexpression_instantiation(instance):
    assert isinstance(instance, cool_CompareExpression)



@given(instance=cool_CompareExpression_strategy)
def test_cool_compareexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=cool_PrimaryExpression_strategy)
@settings(max_examples=50)
def test_cool_primaryexpression_instantiation(instance):
    assert isinstance(instance, cool_PrimaryExpression)

@given(instance=cool_Expression_strategy)
@settings(max_examples=50)
def test_cool_expression_instantiation(instance):
    assert isinstance(instance, cool_Expression)

@given(instance=Feature__strategy)
@settings(max_examples=50)
def test_feature__instantiation(instance):
    assert isinstance(instance, Feature_)

@given(instance=cool_Method_strategy)
@settings(max_examples=50)
def test_cool_method_instantiation(instance):
    assert isinstance(instance, cool_Method)

@given(instance=cool_Attr_strategy)
@settings(max_examples=50)
def test_cool_attr_instantiation(instance):
    assert isinstance(instance, cool_Attr)

@given(instance=cool_Type_strategy)
@settings(max_examples=50)
def test_cool_type_instantiation(instance):
    assert isinstance(instance, cool_Type)

@given(instance=IdentifiableElement_strategy)
@settings(max_examples=50)
def test_identifiableelement_instantiation(instance):
    assert isinstance(instance, IdentifiableElement)

@given(instance=cool_Case_strategy)
@settings(max_examples=50)
def test_cool_case_instantiation(instance):
    assert isinstance(instance, cool_Case)

@given(instance=cool_Feature__strategy)
@settings(max_examples=50)
def test_cool_feature__instantiation(instance):
    assert isinstance(instance, cool_Feature_)

@given(instance=cool_LetDeclaration_strategy)
@settings(max_examples=50)
def test_cool_letdeclaration_instantiation(instance):
    assert isinstance(instance, cool_LetDeclaration)

@given(instance=cool_Formal_strategy)
@settings(max_examples=50)
def test_cool_formal_instantiation(instance):
    assert isinstance(instance, cool_Formal)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=cool_ParenExpression_strategy)
@settings(max_examples=50)
def test_cool_parenexpression_instantiation(instance):
    assert isinstance(instance, cool_ParenExpression)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=cool_StringLiteral_strategy)
@settings(max_examples=50)
def test_cool_stringliteral_instantiation(instance):
    assert isinstance(instance, cool_StringLiteral)



@given(instance=cool_StringLiteral_strategy)
def test_cool_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_cool_booleanliteral_instantiation(instance):
    assert isinstance(instance, cool_BooleanLiteral)



@given(instance=cool_BooleanLiteral_strategy)
def test_cool_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool_NumberLiteral_strategy)
@settings(max_examples=50)
def test_cool_numberliteral_instantiation(instance):
    assert isinstance(instance, cool_NumberLiteral)



@given(instance=cool_NumberLiteral_strategy)
def test_cool_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cool_Literal_strategy)
@settings(max_examples=50)
def test_cool_literal_instantiation(instance):
    assert isinstance(instance, cool_Literal)

@given(instance=cool_IdentifiableElement_strategy)
@settings(max_examples=50)
def test_cool_identifiableelement_instantiation(instance):
    assert isinstance(instance, cool_IdentifiableElement)



@given(instance=cool_IdentifiableElement_strategy)
def test_cool_identifiableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cool_IdentifierRefExpression_strategy)
@settings(max_examples=50)
def test_cool_identifierrefexpression_instantiation(instance):
    assert isinstance(instance, cool_IdentifierRefExpression)

@given(instance=cool_Class__strategy)
@settings(max_examples=50)
def test_cool_class__instantiation(instance):
    assert isinstance(instance, cool_Class_)

@given(instance=cool_Program_strategy)
@settings(max_examples=50)
def test_cool_program_instantiation(instance):
    assert isinstance(instance, cool_Program)
