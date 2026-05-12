import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ArgumentExpression,
    expressions_FeatureCall,
    expressions_Type,
    expressions_ElementReferenceExpression,
    expressions_EObject,
    UnaryExpression,
    expressions_NumericalUnaryExpression,
    expressions_LogicalNotExpression,
    BinaryExpression,
    expressions_BitwiseXorExpression,
    expressions_NumericalMultiplyDivideExpression,
    expressions_BitwiseOrExpression,
    expressions_LogicalRelationExpression,
    expressions_BitwiseAndExpression,
    expressions_LogicalAndExpression,
    expressions_NumericalAddSubtractExpression,
    expressions_ShiftExpression,
    expressions_LogicalOrExpression,
    Literal,
    expressions_NullLiteral,
    expressions_IntLiteral,
    expressions_FloatLiteral,
    expressions_DoubleLiteral,
    expressions_StringLiteral,
    expressions_HexLiteral,
    expressions_BoolLiteral,
    expressions_Literal,
    Expression,
    expressions_TypeCastExpression,
    expressions_PrimitiveValueExpression,
    expressions_AssignmentExpression,
    expressions_ConditionalExpression,
    expressions_ArgumentExpression,
    expressions_ParenthesizedExpression,
    expressions_UnaryExpression,
    expressions_BinaryExpression,
    expressions_Expression,
    MultiplicativeOperator,
    RelationalOperator,
    AssignmentOperator,
    UnaryOperator,
    BitwiseOperator,
    AdditiveOperator,
    LogicalOperator,
    ShiftOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_argumentexpression_is_not_abstract():
    assert not inspect.isabstract(ArgumentExpression)


def test_argumentexpression_constructor_exists():
    assert callable(ArgumentExpression.__init__)


def test_argumentexpression_constructor_args():
    sig = inspect.signature(ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_featurecall_is_not_abstract():
    assert not inspect.isabstract(expressions_FeatureCall)


def test_expressions_featurecall_constructor_exists():
    assert callable(expressions_FeatureCall.__init__)


def test_expressions_featurecall_constructor_args():
    sig = inspect.signature(expressions_FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "arrayAccess" in params, "Missing parameter 'arrayAccess'"
    assert "operationCall" in params, "Missing parameter 'operationCall'"

def test_expressions_featurecall_has_arrayAccess():
    assert hasattr(expressions_FeatureCall, "arrayAccess")
    descriptor = None
    for klass in expressions_FeatureCall.__mro__:
        if "arrayAccess" in klass.__dict__:
            descriptor = klass.__dict__["arrayAccess"]
            break
    assert isinstance(descriptor, property)

def test_expressions_featurecall_has_operationCall():
    assert hasattr(expressions_FeatureCall, "operationCall")
    descriptor = None
    for klass in expressions_FeatureCall.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)



def test_expressions_type_is_not_abstract():
    assert not inspect.isabstract(expressions_Type)


def test_expressions_type_constructor_exists():
    assert callable(expressions_Type.__init__)


def test_expressions_type_constructor_args():
    sig = inspect.signature(expressions_Type.__init__)
    params = list(sig.parameters.keys())



def test_expressions_elementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ElementReferenceExpression)


def test_expressions_elementreferenceexpression_constructor_exists():
    assert callable(expressions_ElementReferenceExpression.__init__)


def test_expressions_elementreferenceexpression_constructor_args():
    sig = inspect.signature(expressions_ElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationCall" in params, "Missing parameter 'operationCall'"
    assert "arrayAccess" in params, "Missing parameter 'arrayAccess'"

def test_expressions_elementreferenceexpression_has_operationCall():
    assert hasattr(expressions_ElementReferenceExpression, "operationCall")
    descriptor = None
    for klass in expressions_ElementReferenceExpression.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)

def test_expressions_elementreferenceexpression_has_arrayAccess():
    assert hasattr(expressions_ElementReferenceExpression, "arrayAccess")
    descriptor = None
    for klass in expressions_ElementReferenceExpression.__mro__:
        if "arrayAccess" in klass.__dict__:
            descriptor = klass.__dict__["arrayAccess"]
            break
    assert isinstance(descriptor, property)



def test_expressions_eobject_is_not_abstract():
    assert not inspect.isabstract(expressions_EObject)


def test_expressions_eobject_constructor_exists():
    assert callable(expressions_EObject.__init__)


def test_expressions_eobject_constructor_args():
    sig = inspect.signature(expressions_EObject.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_numericalunaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_NumericalUnaryExpression)


def test_expressions_numericalunaryexpression_constructor_exists():
    assert callable(expressions_NumericalUnaryExpression.__init__)


def test_expressions_numericalunaryexpression_constructor_args():
    sig = inspect.signature(expressions_NumericalUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_numericalunaryexpression_has_operator():
    assert hasattr(expressions_NumericalUnaryExpression, "operator")
    descriptor = None
    for klass in expressions_NumericalUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_LogicalNotExpression)


def test_expressions_logicalnotexpression_constructor_exists():
    assert callable(expressions_LogicalNotExpression.__init__)


def test_expressions_logicalnotexpression_constructor_args():
    sig = inspect.signature(expressions_LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_BitwiseXorExpression)


def test_expressions_bitwisexorexpression_constructor_exists():
    assert callable(expressions_BitwiseXorExpression.__init__)


def test_expressions_bitwisexorexpression_constructor_args():
    sig = inspect.signature(expressions_BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_numericalmultiplydivideexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_NumericalMultiplyDivideExpression)


def test_expressions_numericalmultiplydivideexpression_constructor_exists():
    assert callable(expressions_NumericalMultiplyDivideExpression.__init__)


def test_expressions_numericalmultiplydivideexpression_constructor_args():
    sig = inspect.signature(expressions_NumericalMultiplyDivideExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_numericalmultiplydivideexpression_has_operator():
    assert hasattr(expressions_NumericalMultiplyDivideExpression, "operator")
    descriptor = None
    for klass in expressions_NumericalMultiplyDivideExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_BitwiseOrExpression)


def test_expressions_bitwiseorexpression_constructor_exists():
    assert callable(expressions_BitwiseOrExpression.__init__)


def test_expressions_bitwiseorexpression_constructor_args():
    sig = inspect.signature(expressions_BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_logicalrelationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_LogicalRelationExpression)


def test_expressions_logicalrelationexpression_constructor_exists():
    assert callable(expressions_LogicalRelationExpression.__init__)


def test_expressions_logicalrelationexpression_constructor_args():
    sig = inspect.signature(expressions_LogicalRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_logicalrelationexpression_has_operator():
    assert hasattr(expressions_LogicalRelationExpression, "operator")
    descriptor = None
    for klass in expressions_LogicalRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_BitwiseAndExpression)


def test_expressions_bitwiseandexpression_constructor_exists():
    assert callable(expressions_BitwiseAndExpression.__init__)


def test_expressions_bitwiseandexpression_constructor_args():
    sig = inspect.signature(expressions_BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_LogicalAndExpression)


def test_expressions_logicalandexpression_constructor_exists():
    assert callable(expressions_LogicalAndExpression.__init__)


def test_expressions_logicalandexpression_constructor_args():
    sig = inspect.signature(expressions_LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_numericaladdsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_NumericalAddSubtractExpression)


def test_expressions_numericaladdsubtractexpression_constructor_exists():
    assert callable(expressions_NumericalAddSubtractExpression.__init__)


def test_expressions_numericaladdsubtractexpression_constructor_args():
    sig = inspect.signature(expressions_NumericalAddSubtractExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_numericaladdsubtractexpression_has_operator():
    assert hasattr(expressions_NumericalAddSubtractExpression, "operator")
    descriptor = None
    for klass in expressions_NumericalAddSubtractExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_shiftexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ShiftExpression)


def test_expressions_shiftexpression_constructor_exists():
    assert callable(expressions_ShiftExpression.__init__)


def test_expressions_shiftexpression_constructor_args():
    sig = inspect.signature(expressions_ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_shiftexpression_has_operator():
    assert hasattr(expressions_ShiftExpression, "operator")
    descriptor = None
    for klass in expressions_ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_LogicalOrExpression)


def test_expressions_logicalorexpression_constructor_exists():
    assert callable(expressions_LogicalOrExpression.__init__)


def test_expressions_logicalorexpression_constructor_args():
    sig = inspect.signature(expressions_LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_expressions_nullliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_NullLiteral)


def test_expressions_nullliteral_constructor_exists():
    assert callable(expressions_NullLiteral.__init__)


def test_expressions_nullliteral_constructor_args():
    sig = inspect.signature(expressions_NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expressions_intliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_IntLiteral)


def test_expressions_intliteral_constructor_exists():
    assert callable(expressions_IntLiteral.__init__)


def test_expressions_intliteral_constructor_args():
    sig = inspect.signature(expressions_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_intliteral_has_value():
    assert hasattr(expressions_IntLiteral, "value")
    descriptor = None
    for klass in expressions_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_floatliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_FloatLiteral)


def test_expressions_floatliteral_constructor_exists():
    assert callable(expressions_FloatLiteral.__init__)


def test_expressions_floatliteral_constructor_args():
    sig = inspect.signature(expressions_FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_floatliteral_has_value():
    assert hasattr(expressions_FloatLiteral, "value")
    descriptor = None
    for klass in expressions_FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_doubleliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_DoubleLiteral)


def test_expressions_doubleliteral_constructor_exists():
    assert callable(expressions_DoubleLiteral.__init__)


def test_expressions_doubleliteral_constructor_args():
    sig = inspect.signature(expressions_DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_doubleliteral_has_value():
    assert hasattr(expressions_DoubleLiteral, "value")
    descriptor = None
    for klass in expressions_DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_stringliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_StringLiteral)


def test_expressions_stringliteral_constructor_exists():
    assert callable(expressions_StringLiteral.__init__)


def test_expressions_stringliteral_constructor_args():
    sig = inspect.signature(expressions_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_stringliteral_has_value():
    assert hasattr(expressions_StringLiteral, "value")
    descriptor = None
    for klass in expressions_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_hexliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_HexLiteral)


def test_expressions_hexliteral_constructor_exists():
    assert callable(expressions_HexLiteral.__init__)


def test_expressions_hexliteral_constructor_args():
    sig = inspect.signature(expressions_HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_hexliteral_has_value():
    assert hasattr(expressions_HexLiteral, "value")
    descriptor = None
    for klass in expressions_HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_boolliteral_is_not_abstract():
    assert not inspect.isabstract(expressions_BoolLiteral)


def test_expressions_boolliteral_constructor_exists():
    assert callable(expressions_BoolLiteral.__init__)


def test_expressions_boolliteral_constructor_args():
    sig = inspect.signature(expressions_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions_boolliteral_has_value():
    assert hasattr(expressions_BoolLiteral, "value")
    descriptor = None
    for klass in expressions_BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions_literal_is_not_abstract():
    assert not inspect.isabstract(expressions_Literal)


def test_expressions_literal_constructor_exists():
    assert callable(expressions_Literal.__init__)


def test_expressions_literal_constructor_args():
    sig = inspect.signature(expressions_Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_typecastexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_TypeCastExpression)


def test_expressions_typecastexpression_constructor_exists():
    assert callable(expressions_TypeCastExpression.__init__)


def test_expressions_typecastexpression_constructor_args():
    sig = inspect.signature(expressions_TypeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_PrimitiveValueExpression)


def test_expressions_primitivevalueexpression_constructor_exists():
    assert callable(expressions_PrimitiveValueExpression.__init__)


def test_expressions_primitivevalueexpression_constructor_args():
    sig = inspect.signature(expressions_PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_AssignmentExpression)


def test_expressions_assignmentexpression_constructor_exists():
    assert callable(expressions_AssignmentExpression.__init__)


def test_expressions_assignmentexpression_constructor_args():
    sig = inspect.signature(expressions_AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions_assignmentexpression_has_operator():
    assert hasattr(expressions_AssignmentExpression, "operator")
    descriptor = None
    for klass in expressions_AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions_conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ConditionalExpression)


def test_expressions_conditionalexpression_constructor_exists():
    assert callable(expressions_ConditionalExpression.__init__)


def test_expressions_conditionalexpression_constructor_args():
    sig = inspect.signature(expressions_ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_argumentexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ArgumentExpression)


def test_expressions_argumentexpression_constructor_exists():
    assert callable(expressions_ArgumentExpression.__init__)


def test_expressions_argumentexpression_constructor_args():
    sig = inspect.signature(expressions_ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_ParenthesizedExpression)


def test_expressions_parenthesizedexpression_constructor_exists():
    assert callable(expressions_ParenthesizedExpression.__init__)


def test_expressions_parenthesizedexpression_constructor_args():
    sig = inspect.signature(expressions_ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_UnaryExpression)


def test_expressions_unaryexpression_constructor_exists():
    assert callable(expressions_UnaryExpression.__init__)


def test_expressions_unaryexpression_constructor_args():
    sig = inspect.signature(expressions_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions_BinaryExpression)


def test_expressions_binaryexpression_constructor_exists():
    assert callable(expressions_BinaryExpression.__init__)


def test_expressions_binaryexpression_constructor_args():
    sig = inspect.signature(expressions_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions_expression_is_not_abstract():
    assert not inspect.isabstract(expressions_Expression)


def test_expressions_expression_constructor_exists():
    assert callable(expressions_Expression.__init__)


def test_expressions_expression_constructor_args():
    sig = inspect.signature(expressions_Expression.__init__)
    params = list(sig.parameters.keys())

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mod",
        "mul",
        "div",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "smallerEqual",
        "greaterEqual",
        "notEquals",
        "equals",
        "smaller",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "assign",
        "leftShiftAssign",
        "modAssign",
        "xorAssign",
        "divAssign",
        "rightShiftAssign",
        "addAssign",
        "andAssign",
        "multAssign",
        "orAssign",
        "subAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

def test_unaryoperator_exists():
    # Check that the Enumeration exists
    assert UnaryOperator is not None

def test_unaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UnaryOperator]
    expected_literals = [
        "complement",
        "positive",
        "negative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UnaryOperator"

def test_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "xor",
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"

def test_additiveoperator_exists():
    # Check that the Enumeration exists
    assert AdditiveOperator is not None

def test_additiveoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdditiveOperator]
    expected_literals = [
        "minus",
        "plus",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdditiveOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "and_",
        "or_",
        "not_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "left",
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"


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
ArgumentExpression_strategy = st.builds(
    ArgumentExpression,
)
expressions_FeatureCall_strategy = st.builds(
    expressions_FeatureCall,
    arrayAccess=
        st.booleans(),
    operationCall=
        st.booleans()
)
expressions_Type_strategy = st.builds(
    expressions_Type,
)
expressions_ElementReferenceExpression_strategy = st.builds(
    expressions_ElementReferenceExpression,
    operationCall=
        st.booleans(),
    arrayAccess=
        st.booleans()
)
expressions_EObject_strategy = st.builds(
    expressions_EObject,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
expressions_NumericalUnaryExpression_strategy = st.builds(
    expressions_NumericalUnaryExpression,
    operator=
        safe_text
)
expressions_LogicalNotExpression_strategy = st.builds(
    expressions_LogicalNotExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
expressions_BitwiseXorExpression_strategy = st.builds(
    expressions_BitwiseXorExpression,
)
expressions_NumericalMultiplyDivideExpression_strategy = st.builds(
    expressions_NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
expressions_BitwiseOrExpression_strategy = st.builds(
    expressions_BitwiseOrExpression,
)
expressions_LogicalRelationExpression_strategy = st.builds(
    expressions_LogicalRelationExpression,
    operator=
        safe_text
)
expressions_BitwiseAndExpression_strategy = st.builds(
    expressions_BitwiseAndExpression,
)
expressions_LogicalAndExpression_strategy = st.builds(
    expressions_LogicalAndExpression,
)
expressions_NumericalAddSubtractExpression_strategy = st.builds(
    expressions_NumericalAddSubtractExpression,
    operator=
        safe_text
)
expressions_ShiftExpression_strategy = st.builds(
    expressions_ShiftExpression,
    operator=
        safe_text
)
expressions_LogicalOrExpression_strategy = st.builds(
    expressions_LogicalOrExpression,
)
Literal_strategy = st.builds(
    Literal,
)
expressions_NullLiteral_strategy = st.builds(
    expressions_NullLiteral,
)
expressions_IntLiteral_strategy = st.builds(
    expressions_IntLiteral,
    value=
        st.integers()
)
expressions_FloatLiteral_strategy = st.builds(
    expressions_FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expressions_DoubleLiteral_strategy = st.builds(
    expressions_DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expressions_StringLiteral_strategy = st.builds(
    expressions_StringLiteral,
    value=
        safe_text
)
expressions_HexLiteral_strategy = st.builds(
    expressions_HexLiteral,
    value=
        st.integers()
)
expressions_BoolLiteral_strategy = st.builds(
    expressions_BoolLiteral,
    value=
        st.booleans()
)
expressions_Literal_strategy = st.builds(
    expressions_Literal,
)
Expression_strategy = st.builds(
    Expression,
)
expressions_TypeCastExpression_strategy = st.builds(
    expressions_TypeCastExpression,
)
expressions_PrimitiveValueExpression_strategy = st.builds(
    expressions_PrimitiveValueExpression,
)
expressions_AssignmentExpression_strategy = st.builds(
    expressions_AssignmentExpression,
    operator=
        safe_text
)
expressions_ConditionalExpression_strategy = st.builds(
    expressions_ConditionalExpression,
)
expressions_ArgumentExpression_strategy = st.builds(
    expressions_ArgumentExpression,
)
expressions_ParenthesizedExpression_strategy = st.builds(
    expressions_ParenthesizedExpression,
)
expressions_UnaryExpression_strategy = st.builds(
    expressions_UnaryExpression,
)
expressions_BinaryExpression_strategy = st.builds(
    expressions_BinaryExpression,
)
expressions_Expression_strategy = st.builds(
    expressions_Expression,
)

@given(instance=ArgumentExpression_strategy)
@settings(max_examples=50)
def test_argumentexpression_instantiation(instance):
    assert isinstance(instance, ArgumentExpression)

@given(instance=expressions_FeatureCall_strategy)
@settings(max_examples=50)
def test_expressions_featurecall_instantiation(instance):
    assert isinstance(instance, expressions_FeatureCall)



@given(instance=expressions_FeatureCall_strategy)
def test_expressions_featurecall_arrayAccess_setter(instance):
    original = instance.arrayAccess
    instance.arrayAccess = original
    assert instance.arrayAccess == original



@given(instance=expressions_FeatureCall_strategy)
def test_expressions_featurecall_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original

@given(instance=expressions_Type_strategy)
@settings(max_examples=50)
def test_expressions_type_instantiation(instance):
    assert isinstance(instance, expressions_Type)

@given(instance=expressions_ElementReferenceExpression_strategy)
@settings(max_examples=50)
def test_expressions_elementreferenceexpression_instantiation(instance):
    assert isinstance(instance, expressions_ElementReferenceExpression)



@given(instance=expressions_ElementReferenceExpression_strategy)
def test_expressions_elementreferenceexpression_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original



@given(instance=expressions_ElementReferenceExpression_strategy)
def test_expressions_elementreferenceexpression_arrayAccess_setter(instance):
    original = instance.arrayAccess
    instance.arrayAccess = original
    assert instance.arrayAccess == original

@given(instance=expressions_EObject_strategy)
@settings(max_examples=50)
def test_expressions_eobject_instantiation(instance):
    assert isinstance(instance, expressions_EObject)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=expressions_NumericalUnaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_numericalunaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalUnaryExpression)



@given(instance=expressions_NumericalUnaryExpression_strategy)
def test_expressions_numericalunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_LogicalNotExpression_strategy)
@settings(max_examples=50)
def test_expressions_logicalnotexpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalNotExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=expressions_BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_expressions_bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseXorExpression)

@given(instance=expressions_NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=50)
def test_expressions_numericalmultiplydivideexpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalMultiplyDivideExpression)



@given(instance=expressions_NumericalMultiplyDivideExpression_strategy)
def test_expressions_numericalmultiplydivideexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_expressions_bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseOrExpression)

@given(instance=expressions_LogicalRelationExpression_strategy)
@settings(max_examples=50)
def test_expressions_logicalrelationexpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalRelationExpression)



@given(instance=expressions_LogicalRelationExpression_strategy)
def test_expressions_logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_expressions_bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, expressions_BitwiseAndExpression)

@given(instance=expressions_LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_expressions_logicalandexpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalAndExpression)

@given(instance=expressions_NumericalAddSubtractExpression_strategy)
@settings(max_examples=50)
def test_expressions_numericaladdsubtractexpression_instantiation(instance):
    assert isinstance(instance, expressions_NumericalAddSubtractExpression)



@given(instance=expressions_NumericalAddSubtractExpression_strategy)
def test_expressions_numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_ShiftExpression_strategy)
@settings(max_examples=50)
def test_expressions_shiftexpression_instantiation(instance):
    assert isinstance(instance, expressions_ShiftExpression)



@given(instance=expressions_ShiftExpression_strategy)
def test_expressions_shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_expressions_logicalorexpression_instantiation(instance):
    assert isinstance(instance, expressions_LogicalOrExpression)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=expressions_NullLiteral_strategy)
@settings(max_examples=50)
def test_expressions_nullliteral_instantiation(instance):
    assert isinstance(instance, expressions_NullLiteral)

@given(instance=expressions_IntLiteral_strategy)
@settings(max_examples=50)
def test_expressions_intliteral_instantiation(instance):
    assert isinstance(instance, expressions_IntLiteral)



@given(instance=expressions_IntLiteral_strategy)
def test_expressions_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_FloatLiteral_strategy)
@settings(max_examples=50)
def test_expressions_floatliteral_instantiation(instance):
    assert isinstance(instance, expressions_FloatLiteral)



@given(instance=expressions_FloatLiteral_strategy)
def test_expressions_floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_DoubleLiteral_strategy)
@settings(max_examples=50)
def test_expressions_doubleliteral_instantiation(instance):
    assert isinstance(instance, expressions_DoubleLiteral)



@given(instance=expressions_DoubleLiteral_strategy)
def test_expressions_doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_StringLiteral_strategy)
@settings(max_examples=50)
def test_expressions_stringliteral_instantiation(instance):
    assert isinstance(instance, expressions_StringLiteral)



@given(instance=expressions_StringLiteral_strategy)
def test_expressions_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_HexLiteral_strategy)
@settings(max_examples=50)
def test_expressions_hexliteral_instantiation(instance):
    assert isinstance(instance, expressions_HexLiteral)



@given(instance=expressions_HexLiteral_strategy)
def test_expressions_hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_BoolLiteral_strategy)
@settings(max_examples=50)
def test_expressions_boolliteral_instantiation(instance):
    assert isinstance(instance, expressions_BoolLiteral)



@given(instance=expressions_BoolLiteral_strategy)
def test_expressions_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions_Literal_strategy)
@settings(max_examples=50)
def test_expressions_literal_instantiation(instance):
    assert isinstance(instance, expressions_Literal)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressions_TypeCastExpression_strategy)
@settings(max_examples=50)
def test_expressions_typecastexpression_instantiation(instance):
    assert isinstance(instance, expressions_TypeCastExpression)

@given(instance=expressions_PrimitiveValueExpression_strategy)
@settings(max_examples=50)
def test_expressions_primitivevalueexpression_instantiation(instance):
    assert isinstance(instance, expressions_PrimitiveValueExpression)

@given(instance=expressions_AssignmentExpression_strategy)
@settings(max_examples=50)
def test_expressions_assignmentexpression_instantiation(instance):
    assert isinstance(instance, expressions_AssignmentExpression)



@given(instance=expressions_AssignmentExpression_strategy)
def test_expressions_assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions_ConditionalExpression_strategy)
@settings(max_examples=50)
def test_expressions_conditionalexpression_instantiation(instance):
    assert isinstance(instance, expressions_ConditionalExpression)

@given(instance=expressions_ArgumentExpression_strategy)
@settings(max_examples=50)
def test_expressions_argumentexpression_instantiation(instance):
    assert isinstance(instance, expressions_ArgumentExpression)

@given(instance=expressions_ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_expressions_parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, expressions_ParenthesizedExpression)

@given(instance=expressions_UnaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_unaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_UnaryExpression)

@given(instance=expressions_BinaryExpression_strategy)
@settings(max_examples=50)
def test_expressions_binaryexpression_instantiation(instance):
    assert isinstance(instance, expressions_BinaryExpression)

@given(instance=expressions_Expression_strategy)
@settings(max_examples=50)
def test_expressions_expression_instantiation(instance):
    assert isinstance(instance, expressions_Expression)
