import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Literal,
    expression_RealLiteral,
    expression_NullLiteral,
    expression_StringLiteral,
    expression_IntegerLiteral,
    expression_BooleanLiteral,
    Expression,
    expression_CastedExpression,
    expression_SwitchExpression,
    expression_IfExpression,
    expression_FeatureCall,
    expression_ConstructorCallExpression,
    expression_ListLiteral,
    expression_Literal,
    expression_GlobalVarExpression,
    expression_ChainExpression,
    expression_BooleanOperation,
    expression_LetExpression,
    expression_SyntaxElement,
    SyntaxElement,
    expression_Identifier,
    expression_Case,
    expression_Expression,
    FeatureCall,
    expression_CollectionExpression,
    expression_TypeSelectExpression,
    expression_OperationCall,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression_realliteral_is_not_abstract():
    assert not inspect.isabstract(expression_RealLiteral)


def test_expression_realliteral_constructor_exists():
    assert callable(expression_RealLiteral.__init__)


def test_expression_realliteral_constructor_args():
    sig = inspect.signature(expression_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression_realliteral_has_val():
    assert hasattr(expression_RealLiteral, "val")
    descriptor = None
    for klass in expression_RealLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_nullliteral_is_not_abstract():
    assert not inspect.isabstract(expression_NullLiteral)


def test_expression_nullliteral_constructor_exists():
    assert callable(expression_NullLiteral.__init__)


def test_expression_nullliteral_constructor_args():
    sig = inspect.signature(expression_NullLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression_nullliteral_has_val():
    assert hasattr(expression_NullLiteral, "val")
    descriptor = None
    for klass in expression_NullLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_stringliteral_is_not_abstract():
    assert not inspect.isabstract(expression_StringLiteral)


def test_expression_stringliteral_constructor_exists():
    assert callable(expression_StringLiteral.__init__)


def test_expression_stringliteral_constructor_args():
    sig = inspect.signature(expression_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression_stringliteral_has_val():
    assert hasattr(expression_StringLiteral, "val")
    descriptor = None
    for klass in expression_StringLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_integerliteral_is_not_abstract():
    assert not inspect.isabstract(expression_IntegerLiteral)


def test_expression_integerliteral_constructor_exists():
    assert callable(expression_IntegerLiteral.__init__)


def test_expression_integerliteral_constructor_args():
    sig = inspect.signature(expression_IntegerLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression_integerliteral_has_val():
    assert hasattr(expression_IntegerLiteral, "val")
    descriptor = None
    for klass in expression_IntegerLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(expression_BooleanLiteral)


def test_expression_booleanliteral_constructor_exists():
    assert callable(expression_BooleanLiteral.__init__)


def test_expression_booleanliteral_constructor_args():
    sig = inspect.signature(expression_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_expression_booleanliteral_has_val():
    assert hasattr(expression_BooleanLiteral, "val")
    descriptor = None
    for klass in expression_BooleanLiteral.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expression_castedexpression_is_not_abstract():
    assert not inspect.isabstract(expression_CastedExpression)


def test_expression_castedexpression_constructor_exists():
    assert callable(expression_CastedExpression.__init__)


def test_expression_castedexpression_constructor_args():
    sig = inspect.signature(expression_CastedExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_switchexpression_is_not_abstract():
    assert not inspect.isabstract(expression_SwitchExpression)


def test_expression_switchexpression_constructor_exists():
    assert callable(expression_SwitchExpression.__init__)


def test_expression_switchexpression_constructor_args():
    sig = inspect.signature(expression_SwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_ifexpression_is_not_abstract():
    assert not inspect.isabstract(expression_IfExpression)


def test_expression_ifexpression_constructor_exists():
    assert callable(expression_IfExpression.__init__)


def test_expression_ifexpression_constructor_args():
    sig = inspect.signature(expression_IfExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_featurecall_is_not_abstract():
    assert not inspect.isabstract(expression_FeatureCall)


def test_expression_featurecall_constructor_exists():
    assert callable(expression_FeatureCall.__init__)


def test_expression_featurecall_constructor_args():
    sig = inspect.signature(expression_FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expression_featurecall_has_name():
    assert hasattr(expression_FeatureCall, "name")
    descriptor = None
    for klass in expression_FeatureCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_constructorcallexpression_is_not_abstract():
    assert not inspect.isabstract(expression_ConstructorCallExpression)


def test_expression_constructorcallexpression_constructor_exists():
    assert callable(expression_ConstructorCallExpression.__init__)


def test_expression_constructorcallexpression_constructor_args():
    sig = inspect.signature(expression_ConstructorCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_listliteral_is_not_abstract():
    assert not inspect.isabstract(expression_ListLiteral)


def test_expression_listliteral_constructor_exists():
    assert callable(expression_ListLiteral.__init__)


def test_expression_listliteral_constructor_args():
    sig = inspect.signature(expression_ListLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expression_literal_is_not_abstract():
    assert not inspect.isabstract(expression_Literal)


def test_expression_literal_constructor_exists():
    assert callable(expression_Literal.__init__)


def test_expression_literal_constructor_args():
    sig = inspect.signature(expression_Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression_globalvarexpression_is_not_abstract():
    assert not inspect.isabstract(expression_GlobalVarExpression)


def test_expression_globalvarexpression_constructor_exists():
    assert callable(expression_GlobalVarExpression.__init__)


def test_expression_globalvarexpression_constructor_args():
    sig = inspect.signature(expression_GlobalVarExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expression_globalvarexpression_has_name():
    assert hasattr(expression_GlobalVarExpression, "name")
    descriptor = None
    for klass in expression_GlobalVarExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_chainexpression_is_not_abstract():
    assert not inspect.isabstract(expression_ChainExpression)


def test_expression_chainexpression_constructor_exists():
    assert callable(expression_ChainExpression.__init__)


def test_expression_chainexpression_constructor_args():
    sig = inspect.signature(expression_ChainExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_booleanoperation_is_not_abstract():
    assert not inspect.isabstract(expression_BooleanOperation)


def test_expression_booleanoperation_constructor_exists():
    assert callable(expression_BooleanOperation.__init__)


def test_expression_booleanoperation_constructor_args():
    sig = inspect.signature(expression_BooleanOperation.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expression_booleanoperation_has_operator():
    assert hasattr(expression_BooleanOperation, "operator")
    descriptor = None
    for klass in expression_BooleanOperation.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expression_letexpression_is_not_abstract():
    assert not inspect.isabstract(expression_LetExpression)


def test_expression_letexpression_constructor_exists():
    assert callable(expression_LetExpression.__init__)


def test_expression_letexpression_constructor_args():
    sig = inspect.signature(expression_LetExpression.__init__)
    params = list(sig.parameters.keys())
    assert "identifier" in params, "Missing parameter 'identifier'"

def test_expression_letexpression_has_identifier():
    assert hasattr(expression_LetExpression, "identifier")
    descriptor = None
    for klass in expression_LetExpression.__mro__:
        if "identifier" in klass.__dict__:
            descriptor = klass.__dict__["identifier"]
            break
    assert isinstance(descriptor, property)



def test_expression_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(expression_SyntaxElement)


def test_expression_syntaxelement_constructor_exists():
    assert callable(expression_SyntaxElement.__init__)


def test_expression_syntaxelement_constructor_args():
    sig = inspect.signature(expression_SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_syntaxelement_is_not_abstract():
    assert not inspect.isabstract(SyntaxElement)


def test_syntaxelement_constructor_exists():
    assert callable(SyntaxElement.__init__)


def test_syntaxelement_constructor_args():
    sig = inspect.signature(SyntaxElement.__init__)
    params = list(sig.parameters.keys())



def test_expression_identifier_is_not_abstract():
    assert not inspect.isabstract(expression_Identifier)


def test_expression_identifier_constructor_exists():
    assert callable(expression_Identifier.__init__)


def test_expression_identifier_constructor_args():
    sig = inspect.signature(expression_Identifier.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "cl" in params, "Missing parameter 'cl'"

def test_expression_identifier_has_id():
    assert hasattr(expression_Identifier, "id")
    descriptor = None
    for klass in expression_Identifier.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_expression_identifier_has_cl():
    assert hasattr(expression_Identifier, "cl")
    descriptor = None
    for klass in expression_Identifier.__mro__:
        if "cl" in klass.__dict__:
            descriptor = klass.__dict__["cl"]
            break
    assert isinstance(descriptor, property)



def test_expression_case_is_not_abstract():
    assert not inspect.isabstract(expression_Case)


def test_expression_case_constructor_exists():
    assert callable(expression_Case.__init__)


def test_expression_case_constructor_args():
    sig = inspect.signature(expression_Case.__init__)
    params = list(sig.parameters.keys())



def test_expression_expression_is_not_abstract():
    assert not inspect.isabstract(expression_Expression)


def test_expression_expression_constructor_exists():
    assert callable(expression_Expression.__init__)


def test_expression_expression_constructor_args():
    sig = inspect.signature(expression_Expression.__init__)
    params = list(sig.parameters.keys())



def test_featurecall_is_not_abstract():
    assert not inspect.isabstract(FeatureCall)


def test_featurecall_constructor_exists():
    assert callable(FeatureCall.__init__)


def test_featurecall_constructor_args():
    sig = inspect.signature(FeatureCall.__init__)
    params = list(sig.parameters.keys())



def test_expression_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(expression_CollectionExpression)


def test_expression_collectionexpression_constructor_exists():
    assert callable(expression_CollectionExpression.__init__)


def test_expression_collectionexpression_constructor_args():
    sig = inspect.signature(expression_CollectionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_expression_collectionexpression_has_var():
    assert hasattr(expression_CollectionExpression, "var")
    descriptor = None
    for klass in expression_CollectionExpression.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_expression_typeselectexpression_is_not_abstract():
    assert not inspect.isabstract(expression_TypeSelectExpression)


def test_expression_typeselectexpression_constructor_exists():
    assert callable(expression_TypeSelectExpression.__init__)


def test_expression_typeselectexpression_constructor_args():
    sig = inspect.signature(expression_TypeSelectExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_operationcall_is_not_abstract():
    assert not inspect.isabstract(expression_OperationCall)


def test_expression_operationcall_constructor_exists():
    assert callable(expression_OperationCall.__init__)


def test_expression_operationcall_constructor_args():
    sig = inspect.signature(expression_OperationCall.__init__)
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
Literal_strategy = st.builds(
    Literal,
)
expression_RealLiteral_strategy = st.builds(
    expression_RealLiteral,
    val=
        safe_text
)
expression_NullLiteral_strategy = st.builds(
    expression_NullLiteral,
    val=
        safe_text
)
expression_StringLiteral_strategy = st.builds(
    expression_StringLiteral,
    val=
        safe_text
)
expression_IntegerLiteral_strategy = st.builds(
    expression_IntegerLiteral,
    val=
        st.integers()
)
expression_BooleanLiteral_strategy = st.builds(
    expression_BooleanLiteral,
    val=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
expression_CastedExpression_strategy = st.builds(
    expression_CastedExpression,
)
expression_SwitchExpression_strategy = st.builds(
    expression_SwitchExpression,
)
expression_IfExpression_strategy = st.builds(
    expression_IfExpression,
)
expression_FeatureCall_strategy = st.builds(
    expression_FeatureCall,
    name=
        safe_text
)
expression_ConstructorCallExpression_strategy = st.builds(
    expression_ConstructorCallExpression,
)
expression_ListLiteral_strategy = st.builds(
    expression_ListLiteral,
)
expression_Literal_strategy = st.builds(
    expression_Literal,
)
expression_GlobalVarExpression_strategy = st.builds(
    expression_GlobalVarExpression,
    name=
        safe_text
)
expression_ChainExpression_strategy = st.builds(
    expression_ChainExpression,
)
expression_BooleanOperation_strategy = st.builds(
    expression_BooleanOperation,
    operator=
        safe_text
)
expression_LetExpression_strategy = st.builds(
    expression_LetExpression,
    identifier=
        safe_text
)
expression_SyntaxElement_strategy = st.builds(
    expression_SyntaxElement,
)
SyntaxElement_strategy = st.builds(
    SyntaxElement,
)
expression_Identifier_strategy = st.builds(
    expression_Identifier,
    id=
        safe_text,
    cl=
        safe_text
)
expression_Case_strategy = st.builds(
    expression_Case,
)
expression_Expression_strategy = st.builds(
    expression_Expression,
)
FeatureCall_strategy = st.builds(
    FeatureCall,
)
expression_CollectionExpression_strategy = st.builds(
    expression_CollectionExpression,
    var=
        safe_text
)
expression_TypeSelectExpression_strategy = st.builds(
    expression_TypeSelectExpression,
)
expression_OperationCall_strategy = st.builds(
    expression_OperationCall,
)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=expression_RealLiteral_strategy)
@settings(max_examples=50)
def test_expression_realliteral_instantiation(instance):
    assert isinstance(instance, expression_RealLiteral)



@given(instance=expression_RealLiteral_strategy)
def test_expression_realliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression_NullLiteral_strategy)
@settings(max_examples=50)
def test_expression_nullliteral_instantiation(instance):
    assert isinstance(instance, expression_NullLiteral)



@given(instance=expression_NullLiteral_strategy)
def test_expression_nullliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression_StringLiteral_strategy)
@settings(max_examples=50)
def test_expression_stringliteral_instantiation(instance):
    assert isinstance(instance, expression_StringLiteral)



@given(instance=expression_StringLiteral_strategy)
def test_expression_stringliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression_IntegerLiteral_strategy)
@settings(max_examples=50)
def test_expression_integerliteral_instantiation(instance):
    assert isinstance(instance, expression_IntegerLiteral)



@given(instance=expression_IntegerLiteral_strategy)
def test_expression_integerliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=expression_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_expression_booleanliteral_instantiation(instance):
    assert isinstance(instance, expression_BooleanLiteral)



@given(instance=expression_BooleanLiteral_strategy)
def test_expression_booleanliteral_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expression_CastedExpression_strategy)
@settings(max_examples=50)
def test_expression_castedexpression_instantiation(instance):
    assert isinstance(instance, expression_CastedExpression)

@given(instance=expression_SwitchExpression_strategy)
@settings(max_examples=50)
def test_expression_switchexpression_instantiation(instance):
    assert isinstance(instance, expression_SwitchExpression)

@given(instance=expression_IfExpression_strategy)
@settings(max_examples=50)
def test_expression_ifexpression_instantiation(instance):
    assert isinstance(instance, expression_IfExpression)

@given(instance=expression_FeatureCall_strategy)
@settings(max_examples=50)
def test_expression_featurecall_instantiation(instance):
    assert isinstance(instance, expression_FeatureCall)



@given(instance=expression_FeatureCall_strategy)
def test_expression_featurecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expression_ConstructorCallExpression_strategy)
@settings(max_examples=50)
def test_expression_constructorcallexpression_instantiation(instance):
    assert isinstance(instance, expression_ConstructorCallExpression)

@given(instance=expression_ListLiteral_strategy)
@settings(max_examples=50)
def test_expression_listliteral_instantiation(instance):
    assert isinstance(instance, expression_ListLiteral)

@given(instance=expression_Literal_strategy)
@settings(max_examples=50)
def test_expression_literal_instantiation(instance):
    assert isinstance(instance, expression_Literal)

@given(instance=expression_GlobalVarExpression_strategy)
@settings(max_examples=50)
def test_expression_globalvarexpression_instantiation(instance):
    assert isinstance(instance, expression_GlobalVarExpression)



@given(instance=expression_GlobalVarExpression_strategy)
def test_expression_globalvarexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expression_ChainExpression_strategy)
@settings(max_examples=50)
def test_expression_chainexpression_instantiation(instance):
    assert isinstance(instance, expression_ChainExpression)

@given(instance=expression_BooleanOperation_strategy)
@settings(max_examples=50)
def test_expression_booleanoperation_instantiation(instance):
    assert isinstance(instance, expression_BooleanOperation)



@given(instance=expression_BooleanOperation_strategy)
def test_expression_booleanoperation_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expression_LetExpression_strategy)
@settings(max_examples=50)
def test_expression_letexpression_instantiation(instance):
    assert isinstance(instance, expression_LetExpression)



@given(instance=expression_LetExpression_strategy)
def test_expression_letexpression_identifier_setter(instance):
    original = instance.identifier
    instance.identifier = original
    assert instance.identifier == original

@given(instance=expression_SyntaxElement_strategy)
@settings(max_examples=50)
def test_expression_syntaxelement_instantiation(instance):
    assert isinstance(instance, expression_SyntaxElement)

@given(instance=SyntaxElement_strategy)
@settings(max_examples=50)
def test_syntaxelement_instantiation(instance):
    assert isinstance(instance, SyntaxElement)

@given(instance=expression_Identifier_strategy)
@settings(max_examples=50)
def test_expression_identifier_instantiation(instance):
    assert isinstance(instance, expression_Identifier)



@given(instance=expression_Identifier_strategy)
def test_expression_identifier_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=expression_Identifier_strategy)
def test_expression_identifier_cl_setter(instance):
    original = instance.cl
    instance.cl = original
    assert instance.cl == original

@given(instance=expression_Case_strategy)
@settings(max_examples=50)
def test_expression_case_instantiation(instance):
    assert isinstance(instance, expression_Case)

@given(instance=expression_Expression_strategy)
@settings(max_examples=50)
def test_expression_expression_instantiation(instance):
    assert isinstance(instance, expression_Expression)

@given(instance=FeatureCall_strategy)
@settings(max_examples=50)
def test_featurecall_instantiation(instance):
    assert isinstance(instance, FeatureCall)

@given(instance=expression_CollectionExpression_strategy)
@settings(max_examples=50)
def test_expression_collectionexpression_instantiation(instance):
    assert isinstance(instance, expression_CollectionExpression)



@given(instance=expression_CollectionExpression_strategy)
def test_expression_collectionexpression_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=expression_TypeSelectExpression_strategy)
@settings(max_examples=50)
def test_expression_typeselectexpression_instantiation(instance):
    assert isinstance(instance, expression_TypeSelectExpression)

@given(instance=expression_OperationCall_strategy)
@settings(max_examples=50)
def test_expression_operationcall_instantiation(instance):
    assert isinstance(instance, expression_OperationCall)
