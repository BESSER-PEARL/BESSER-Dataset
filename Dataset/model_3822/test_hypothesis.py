import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArgumentExpression,
    expressions::FeatureCall,
    expressions::Type,
    expressions::ElementReferenceExpression,
    expressions::EObject,
    UnaryExpression,
    expressions::NumericalUnaryExpression,
    expressions::LogicalNotExpression,
    BinaryExpression,
    expressions::BitwiseOrExpression,
    expressions::LogicalRelationExpression,
    expressions::BitwiseXorExpression,
    expressions::LogicalAndExpression,
    expressions::NumericalAddSubtractExpression,
    expressions::BitwiseAndExpression,
    expressions::NumericalMultiplyDivideExpression,
    expressions::ShiftExpression,
    expressions::LogicalOrExpression,
    Literal,
    expressions::DoubleLiteral,
    expressions::HexLiteral,
    expressions::StringLiteral,
    expressions::IntLiteral,
    expressions::FloatLiteral,
    expressions::NullLiteral,
    expressions::BoolLiteral,
    expressions::Literal,
    Expression,
    expressions::ConditionalExpression,
    expressions::UnaryExpression,
    expressions::ArgumentExpression,
    expressions::TypeCastExpression,
    expressions::ParenthesizedExpression,
    expressions::AssignmentExpression,
    expressions::PrimitiveValueExpression,
    expressions::BinaryExpression,
    expressions::Expression,
    UnaryOperator,
    AssignmentOperator,
    AdditiveOperator,
    ShiftOperator,
    RelationalOperator,
    BitwiseOperator,
    MultiplicativeOperator,
    LogicalOperator,
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



def test_expressions::featurecall_is_not_abstract():
    assert not inspect.isabstract(expressions::FeatureCall)


def test_expressions::featurecall_constructor_exists():
    assert callable(expressions::FeatureCall.__init__)


def test_expressions::featurecall_constructor_args():
    sig = inspect.signature(expressions::FeatureCall.__init__)
    params = list(sig.parameters.keys())
    assert "arrayAccess" in params, "Missing parameter 'arrayAccess'"
    assert "operationCall" in params, "Missing parameter 'operationCall'"

def test_expressions::featurecall_has_arrayAccess():
    assert hasattr(expressions::FeatureCall, "arrayAccess")
    descriptor = None
    for klass in expressions::FeatureCall.__mro__:
        if "arrayAccess" in klass.__dict__:
            descriptor = klass.__dict__["arrayAccess"]
            break
    assert isinstance(descriptor, property)

def test_expressions::featurecall_has_operationCall():
    assert hasattr(expressions::FeatureCall, "operationCall")
    descriptor = None
    for klass in expressions::FeatureCall.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)



def test_expressions::type_is_not_abstract():
    assert not inspect.isabstract(expressions::Type)


def test_expressions::type_constructor_exists():
    assert callable(expressions::Type.__init__)


def test_expressions::type_constructor_args():
    sig = inspect.signature(expressions::Type.__init__)
    params = list(sig.parameters.keys())



def test_expressions::elementreferenceexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ElementReferenceExpression)


def test_expressions::elementreferenceexpression_constructor_exists():
    assert callable(expressions::ElementReferenceExpression.__init__)


def test_expressions::elementreferenceexpression_constructor_args():
    sig = inspect.signature(expressions::ElementReferenceExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operationCall" in params, "Missing parameter 'operationCall'"
    assert "arrayAccess" in params, "Missing parameter 'arrayAccess'"

def test_expressions::elementreferenceexpression_has_operationCall():
    assert hasattr(expressions::ElementReferenceExpression, "operationCall")
    descriptor = None
    for klass in expressions::ElementReferenceExpression.__mro__:
        if "operationCall" in klass.__dict__:
            descriptor = klass.__dict__["operationCall"]
            break
    assert isinstance(descriptor, property)

def test_expressions::elementreferenceexpression_has_arrayAccess():
    assert hasattr(expressions::ElementReferenceExpression, "arrayAccess")
    descriptor = None
    for klass in expressions::ElementReferenceExpression.__mro__:
        if "arrayAccess" in klass.__dict__:
            descriptor = klass.__dict__["arrayAccess"]
            break
    assert isinstance(descriptor, property)



def test_expressions::eobject_is_not_abstract():
    assert not inspect.isabstract(expressions::EObject)


def test_expressions::eobject_constructor_exists():
    assert callable(expressions::EObject.__init__)


def test_expressions::eobject_constructor_args():
    sig = inspect.signature(expressions::EObject.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::numericalunaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::NumericalUnaryExpression)


def test_expressions::numericalunaryexpression_constructor_exists():
    assert callable(expressions::NumericalUnaryExpression.__init__)


def test_expressions::numericalunaryexpression_constructor_args():
    sig = inspect.signature(expressions::NumericalUnaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::numericalunaryexpression_has_operator():
    assert hasattr(expressions::NumericalUnaryExpression, "operator")
    descriptor = None
    for klass in expressions::NumericalUnaryExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::logicalnotexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::LogicalNotExpression)


def test_expressions::logicalnotexpression_constructor_exists():
    assert callable(expressions::LogicalNotExpression.__init__)


def test_expressions::logicalnotexpression_constructor_args():
    sig = inspect.signature(expressions::LogicalNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::bitwiseorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::BitwiseOrExpression)


def test_expressions::bitwiseorexpression_constructor_exists():
    assert callable(expressions::BitwiseOrExpression.__init__)


def test_expressions::bitwiseorexpression_constructor_args():
    sig = inspect.signature(expressions::BitwiseOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::logicalrelationexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::LogicalRelationExpression)


def test_expressions::logicalrelationexpression_constructor_exists():
    assert callable(expressions::LogicalRelationExpression.__init__)


def test_expressions::logicalrelationexpression_constructor_args():
    sig = inspect.signature(expressions::LogicalRelationExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::logicalrelationexpression_has_operator():
    assert hasattr(expressions::LogicalRelationExpression, "operator")
    descriptor = None
    for klass in expressions::LogicalRelationExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::bitwisexorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::BitwiseXorExpression)


def test_expressions::bitwisexorexpression_constructor_exists():
    assert callable(expressions::BitwiseXorExpression.__init__)


def test_expressions::bitwisexorexpression_constructor_args():
    sig = inspect.signature(expressions::BitwiseXorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::logicalandexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::LogicalAndExpression)


def test_expressions::logicalandexpression_constructor_exists():
    assert callable(expressions::LogicalAndExpression.__init__)


def test_expressions::logicalandexpression_constructor_args():
    sig = inspect.signature(expressions::LogicalAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::numericaladdsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::NumericalAddSubtractExpression)


def test_expressions::numericaladdsubtractexpression_constructor_exists():
    assert callable(expressions::NumericalAddSubtractExpression.__init__)


def test_expressions::numericaladdsubtractexpression_constructor_args():
    sig = inspect.signature(expressions::NumericalAddSubtractExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::numericaladdsubtractexpression_has_operator():
    assert hasattr(expressions::NumericalAddSubtractExpression, "operator")
    descriptor = None
    for klass in expressions::NumericalAddSubtractExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::bitwiseandexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::BitwiseAndExpression)


def test_expressions::bitwiseandexpression_constructor_exists():
    assert callable(expressions::BitwiseAndExpression.__init__)


def test_expressions::bitwiseandexpression_constructor_args():
    sig = inspect.signature(expressions::BitwiseAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::numericalmultiplydivideexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::NumericalMultiplyDivideExpression)


def test_expressions::numericalmultiplydivideexpression_constructor_exists():
    assert callable(expressions::NumericalMultiplyDivideExpression.__init__)


def test_expressions::numericalmultiplydivideexpression_constructor_args():
    sig = inspect.signature(expressions::NumericalMultiplyDivideExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::numericalmultiplydivideexpression_has_operator():
    assert hasattr(expressions::NumericalMultiplyDivideExpression, "operator")
    descriptor = None
    for klass in expressions::NumericalMultiplyDivideExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ShiftExpression)


def test_expressions::shiftexpression_constructor_exists():
    assert callable(expressions::ShiftExpression.__init__)


def test_expressions::shiftexpression_constructor_args():
    sig = inspect.signature(expressions::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::shiftexpression_has_operator():
    assert hasattr(expressions::ShiftExpression, "operator")
    descriptor = None
    for klass in expressions::ShiftExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::logicalorexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::LogicalOrExpression)


def test_expressions::logicalorexpression_constructor_exists():
    assert callable(expressions::LogicalOrExpression.__init__)


def test_expressions::logicalorexpression_constructor_args():
    sig = inspect.signature(expressions::LogicalOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_literal_is_not_abstract():
    assert not inspect.isabstract(Literal)


def test_literal_constructor_exists():
    assert callable(Literal.__init__)


def test_literal_constructor_args():
    sig = inspect.signature(Literal.__init__)
    params = list(sig.parameters.keys())



def test_expressions::doubleliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::DoubleLiteral)


def test_expressions::doubleliteral_constructor_exists():
    assert callable(expressions::DoubleLiteral.__init__)


def test_expressions::doubleliteral_constructor_args():
    sig = inspect.signature(expressions::DoubleLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::doubleliteral_has_value():
    assert hasattr(expressions::DoubleLiteral, "value")
    descriptor = None
    for klass in expressions::DoubleLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::hexliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::HexLiteral)


def test_expressions::hexliteral_constructor_exists():
    assert callable(expressions::HexLiteral.__init__)


def test_expressions::hexliteral_constructor_args():
    sig = inspect.signature(expressions::HexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::hexliteral_has_value():
    assert hasattr(expressions::HexLiteral, "value")
    descriptor = None
    for klass in expressions::HexLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::stringliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::StringLiteral)


def test_expressions::stringliteral_constructor_exists():
    assert callable(expressions::StringLiteral.__init__)


def test_expressions::stringliteral_constructor_args():
    sig = inspect.signature(expressions::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::stringliteral_has_value():
    assert hasattr(expressions::StringLiteral, "value")
    descriptor = None
    for klass in expressions::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::intliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::IntLiteral)


def test_expressions::intliteral_constructor_exists():
    assert callable(expressions::IntLiteral.__init__)


def test_expressions::intliteral_constructor_args():
    sig = inspect.signature(expressions::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::intliteral_has_value():
    assert hasattr(expressions::IntLiteral, "value")
    descriptor = None
    for klass in expressions::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::floatliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::FloatLiteral)


def test_expressions::floatliteral_constructor_exists():
    assert callable(expressions::FloatLiteral.__init__)


def test_expressions::floatliteral_constructor_args():
    sig = inspect.signature(expressions::FloatLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::floatliteral_has_value():
    assert hasattr(expressions::FloatLiteral, "value")
    descriptor = None
    for klass in expressions::FloatLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::nullliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::NullLiteral)


def test_expressions::nullliteral_constructor_exists():
    assert callable(expressions::NullLiteral.__init__)


def test_expressions::nullliteral_constructor_args():
    sig = inspect.signature(expressions::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_expressions::boolliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::BoolLiteral)


def test_expressions::boolliteral_constructor_exists():
    assert callable(expressions::BoolLiteral.__init__)


def test_expressions::boolliteral_constructor_args():
    sig = inspect.signature(expressions::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressions::boolliteral_has_value():
    assert hasattr(expressions::BoolLiteral, "value")
    descriptor = None
    for klass in expressions::BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressions::literal_is_not_abstract():
    assert not inspect.isabstract(expressions::Literal)


def test_expressions::literal_constructor_exists():
    assert callable(expressions::Literal.__init__)


def test_expressions::literal_constructor_args():
    sig = inspect.signature(expressions::Literal.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::conditionalexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ConditionalExpression)


def test_expressions::conditionalexpression_constructor_exists():
    assert callable(expressions::ConditionalExpression.__init__)


def test_expressions::conditionalexpression_constructor_args():
    sig = inspect.signature(expressions::ConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::UnaryExpression)


def test_expressions::unaryexpression_constructor_exists():
    assert callable(expressions::UnaryExpression.__init__)


def test_expressions::unaryexpression_constructor_args():
    sig = inspect.signature(expressions::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::argumentexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ArgumentExpression)


def test_expressions::argumentexpression_constructor_exists():
    assert callable(expressions::ArgumentExpression.__init__)


def test_expressions::argumentexpression_constructor_args():
    sig = inspect.signature(expressions::ArgumentExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::typecastexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::TypeCastExpression)


def test_expressions::typecastexpression_constructor_exists():
    assert callable(expressions::TypeCastExpression.__init__)


def test_expressions::typecastexpression_constructor_args():
    sig = inspect.signature(expressions::TypeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::parenthesizedexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::ParenthesizedExpression)


def test_expressions::parenthesizedexpression_constructor_exists():
    assert callable(expressions::ParenthesizedExpression.__init__)


def test_expressions::parenthesizedexpression_constructor_args():
    sig = inspect.signature(expressions::ParenthesizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::AssignmentExpression)


def test_expressions::assignmentexpression_constructor_exists():
    assert callable(expressions::AssignmentExpression.__init__)


def test_expressions::assignmentexpression_constructor_args():
    sig = inspect.signature(expressions::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_expressions::assignmentexpression_has_operator():
    assert hasattr(expressions::AssignmentExpression, "operator")
    descriptor = None
    for klass in expressions::AssignmentExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_expressions::primitivevalueexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::PrimitiveValueExpression)


def test_expressions::primitivevalueexpression_constructor_exists():
    assert callable(expressions::PrimitiveValueExpression.__init__)


def test_expressions::primitivevalueexpression_constructor_args():
    sig = inspect.signature(expressions::PrimitiveValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::BinaryExpression)


def test_expressions::binaryexpression_constructor_exists():
    assert callable(expressions::BinaryExpression.__init__)


def test_expressions::binaryexpression_constructor_args():
    sig = inspect.signature(expressions::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_expressions::expression_is_not_abstract():
    assert not inspect.isabstract(expressions::Expression)


def test_expressions::expression_constructor_exists():
    assert callable(expressions::Expression.__init__)


def test_expressions::expression_constructor_args():
    sig = inspect.signature(expressions::Expression.__init__)
    params = list(sig.parameters.keys())

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

def test_assignmentoperator_exists():
    # Check that the Enumeration exists
    assert AssignmentOperator is not None

def test_assignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentOperator]
    expected_literals = [
        "subAssign",
        "addAssign",
        "andAssign",
        "multAssign",
        "rightShiftAssign",
        "divAssign",
        "xorAssign",
        "orAssign",
        "assign",
        "leftShiftAssign",
        "modAssign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentOperator"

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

def test_shiftoperator_exists():
    # Check that the Enumeration exists
    assert ShiftOperator is not None

def test_shiftoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShiftOperator]
    expected_literals = [
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShiftOperator"

def test_relationaloperator_exists():
    # Check that the Enumeration exists
    assert RelationalOperator is not None

def test_relationaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationalOperator]
    expected_literals = [
        "greaterEqual",
        "notEquals",
        "smaller",
        "equals",
        "smallerEqual",
        "greater",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationalOperator"

def test_bitwiseoperator_exists():
    # Check that the Enumeration exists
    assert BitwiseOperator is not None

def test_bitwiseoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BitwiseOperator]
    expected_literals = [
        "or_",
        "and_",
        "xor",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BitwiseOperator"

def test_multiplicativeoperator_exists():
    # Check that the Enumeration exists
    assert MultiplicativeOperator is not None

def test_multiplicativeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiplicativeOperator]
    expected_literals = [
        "mod",
        "div",
        "mul",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiplicativeOperator"

def test_logicaloperator_exists():
    # Check that the Enumeration exists
    assert LogicalOperator is not None

def test_logicaloperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalOperator]
    expected_literals = [
        "not_",
        "and_",
        "or_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalOperator"


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
expressions::FeatureCall_strategy = st.builds(
    expressions::FeatureCall,
    arrayAccess=
        st.booleans(),
    operationCall=
        st.booleans()
)
expressions::Type_strategy = st.builds(
    expressions::Type,
)
expressions::ElementReferenceExpression_strategy = st.builds(
    expressions::ElementReferenceExpression,
    operationCall=
        st.booleans(),
    arrayAccess=
        st.booleans()
)
expressions::EObject_strategy = st.builds(
    expressions::EObject,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
expressions::NumericalUnaryExpression_strategy = st.builds(
    expressions::NumericalUnaryExpression,
    operator=
        safe_text
)
expressions::LogicalNotExpression_strategy = st.builds(
    expressions::LogicalNotExpression,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
expressions::BitwiseOrExpression_strategy = st.builds(
    expressions::BitwiseOrExpression,
)
expressions::LogicalRelationExpression_strategy = st.builds(
    expressions::LogicalRelationExpression,
    operator=
        safe_text
)
expressions::BitwiseXorExpression_strategy = st.builds(
    expressions::BitwiseXorExpression,
)
expressions::LogicalAndExpression_strategy = st.builds(
    expressions::LogicalAndExpression,
)
expressions::NumericalAddSubtractExpression_strategy = st.builds(
    expressions::NumericalAddSubtractExpression,
    operator=
        safe_text
)
expressions::BitwiseAndExpression_strategy = st.builds(
    expressions::BitwiseAndExpression,
)
expressions::NumericalMultiplyDivideExpression_strategy = st.builds(
    expressions::NumericalMultiplyDivideExpression,
    operator=
        safe_text
)
expressions::ShiftExpression_strategy = st.builds(
    expressions::ShiftExpression,
    operator=
        safe_text
)
expressions::LogicalOrExpression_strategy = st.builds(
    expressions::LogicalOrExpression,
)
Literal_strategy = st.builds(
    Literal,
)
expressions::DoubleLiteral_strategy = st.builds(
    expressions::DoubleLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expressions::HexLiteral_strategy = st.builds(
    expressions::HexLiteral,
    value=
        st.integers()
)
expressions::StringLiteral_strategy = st.builds(
    expressions::StringLiteral,
    value=
        safe_text
)
expressions::IntLiteral_strategy = st.builds(
    expressions::IntLiteral,
    value=
        st.integers()
)
expressions::FloatLiteral_strategy = st.builds(
    expressions::FloatLiteral,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
expressions::NullLiteral_strategy = st.builds(
    expressions::NullLiteral,
)
expressions::BoolLiteral_strategy = st.builds(
    expressions::BoolLiteral,
    value=
        st.booleans()
)
expressions::Literal_strategy = st.builds(
    expressions::Literal,
)
Expression_strategy = st.builds(
    Expression,
)
expressions::ConditionalExpression_strategy = st.builds(
    expressions::ConditionalExpression,
)
expressions::UnaryExpression_strategy = st.builds(
    expressions::UnaryExpression,
)
expressions::ArgumentExpression_strategy = st.builds(
    expressions::ArgumentExpression,
)
expressions::TypeCastExpression_strategy = st.builds(
    expressions::TypeCastExpression,
)
expressions::ParenthesizedExpression_strategy = st.builds(
    expressions::ParenthesizedExpression,
)
expressions::AssignmentExpression_strategy = st.builds(
    expressions::AssignmentExpression,
    operator=
        safe_text
)
expressions::PrimitiveValueExpression_strategy = st.builds(
    expressions::PrimitiveValueExpression,
)
expressions::BinaryExpression_strategy = st.builds(
    expressions::BinaryExpression,
)
expressions::Expression_strategy = st.builds(
    expressions::Expression,
)

@given(instance=ArgumentExpression_strategy)
@settings(max_examples=50)
def test_argumentexpression_instantiation(instance):
    assert isinstance(instance, ArgumentExpression)

@given(instance=expressions::FeatureCall_strategy)
@settings(max_examples=50)
def test_expressions::featurecall_instantiation(instance):
    assert isinstance(instance, expressions::FeatureCall)

@given(instance=expressions::FeatureCall_strategy)
def test_expressions::featurecall_arrayAccess_type(instance):
    assert isinstance(instance.arrayAccess, bool)


@given(instance=expressions::FeatureCall_strategy)
def test_expressions::featurecall_arrayAccess_setter(instance):
    original = instance.arrayAccess
    instance.arrayAccess = original
    assert instance.arrayAccess == original

@given(instance=expressions::FeatureCall_strategy)
def test_expressions::featurecall_operationCall_type(instance):
    assert isinstance(instance.operationCall, bool)


@given(instance=expressions::FeatureCall_strategy)
def test_expressions::featurecall_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original

@given(instance=expressions::Type_strategy)
@settings(max_examples=50)
def test_expressions::type_instantiation(instance):
    assert isinstance(instance, expressions::Type)

@given(instance=expressions::ElementReferenceExpression_strategy)
@settings(max_examples=50)
def test_expressions::elementreferenceexpression_instantiation(instance):
    assert isinstance(instance, expressions::ElementReferenceExpression)

@given(instance=expressions::ElementReferenceExpression_strategy)
def test_expressions::elementreferenceexpression_operationCall_type(instance):
    assert isinstance(instance.operationCall, bool)


@given(instance=expressions::ElementReferenceExpression_strategy)
def test_expressions::elementreferenceexpression_operationCall_setter(instance):
    original = instance.operationCall
    instance.operationCall = original
    assert instance.operationCall == original

@given(instance=expressions::ElementReferenceExpression_strategy)
def test_expressions::elementreferenceexpression_arrayAccess_type(instance):
    assert isinstance(instance.arrayAccess, bool)


@given(instance=expressions::ElementReferenceExpression_strategy)
def test_expressions::elementreferenceexpression_arrayAccess_setter(instance):
    original = instance.arrayAccess
    instance.arrayAccess = original
    assert instance.arrayAccess == original

@given(instance=expressions::EObject_strategy)
@settings(max_examples=50)
def test_expressions::eobject_instantiation(instance):
    assert isinstance(instance, expressions::EObject)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=expressions::NumericalUnaryExpression_strategy)
@settings(max_examples=50)
def test_expressions::numericalunaryexpression_instantiation(instance):
    assert isinstance(instance, expressions::NumericalUnaryExpression)

@given(instance=expressions::NumericalUnaryExpression_strategy)
def test_expressions::numericalunaryexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::NumericalUnaryExpression_strategy)
def test_expressions::numericalunaryexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::LogicalNotExpression_strategy)
@settings(max_examples=50)
def test_expressions::logicalnotexpression_instantiation(instance):
    assert isinstance(instance, expressions::LogicalNotExpression)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=expressions::BitwiseOrExpression_strategy)
@settings(max_examples=50)
def test_expressions::bitwiseorexpression_instantiation(instance):
    assert isinstance(instance, expressions::BitwiseOrExpression)

@given(instance=expressions::LogicalRelationExpression_strategy)
@settings(max_examples=50)
def test_expressions::logicalrelationexpression_instantiation(instance):
    assert isinstance(instance, expressions::LogicalRelationExpression)

@given(instance=expressions::LogicalRelationExpression_strategy)
def test_expressions::logicalrelationexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::LogicalRelationExpression_strategy)
def test_expressions::logicalrelationexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::BitwiseXorExpression_strategy)
@settings(max_examples=50)
def test_expressions::bitwisexorexpression_instantiation(instance):
    assert isinstance(instance, expressions::BitwiseXorExpression)

@given(instance=expressions::LogicalAndExpression_strategy)
@settings(max_examples=50)
def test_expressions::logicalandexpression_instantiation(instance):
    assert isinstance(instance, expressions::LogicalAndExpression)

@given(instance=expressions::NumericalAddSubtractExpression_strategy)
@settings(max_examples=50)
def test_expressions::numericaladdsubtractexpression_instantiation(instance):
    assert isinstance(instance, expressions::NumericalAddSubtractExpression)

@given(instance=expressions::NumericalAddSubtractExpression_strategy)
def test_expressions::numericaladdsubtractexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::NumericalAddSubtractExpression_strategy)
def test_expressions::numericaladdsubtractexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::BitwiseAndExpression_strategy)
@settings(max_examples=50)
def test_expressions::bitwiseandexpression_instantiation(instance):
    assert isinstance(instance, expressions::BitwiseAndExpression)

@given(instance=expressions::NumericalMultiplyDivideExpression_strategy)
@settings(max_examples=50)
def test_expressions::numericalmultiplydivideexpression_instantiation(instance):
    assert isinstance(instance, expressions::NumericalMultiplyDivideExpression)

@given(instance=expressions::NumericalMultiplyDivideExpression_strategy)
def test_expressions::numericalmultiplydivideexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::NumericalMultiplyDivideExpression_strategy)
def test_expressions::numericalmultiplydivideexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::ShiftExpression_strategy)
@settings(max_examples=50)
def test_expressions::shiftexpression_instantiation(instance):
    assert isinstance(instance, expressions::ShiftExpression)

@given(instance=expressions::ShiftExpression_strategy)
def test_expressions::shiftexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::ShiftExpression_strategy)
def test_expressions::shiftexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::LogicalOrExpression_strategy)
@settings(max_examples=50)
def test_expressions::logicalorexpression_instantiation(instance):
    assert isinstance(instance, expressions::LogicalOrExpression)

@given(instance=Literal_strategy)
@settings(max_examples=50)
def test_literal_instantiation(instance):
    assert isinstance(instance, Literal)

@given(instance=expressions::DoubleLiteral_strategy)
@settings(max_examples=50)
def test_expressions::doubleliteral_instantiation(instance):
    assert isinstance(instance, expressions::DoubleLiteral)

@given(instance=expressions::DoubleLiteral_strategy)
def test_expressions::doubleliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=expressions::DoubleLiteral_strategy)
def test_expressions::doubleliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::HexLiteral_strategy)
@settings(max_examples=50)
def test_expressions::hexliteral_instantiation(instance):
    assert isinstance(instance, expressions::HexLiteral)

@given(instance=expressions::HexLiteral_strategy)
def test_expressions::hexliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expressions::HexLiteral_strategy)
def test_expressions::hexliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::StringLiteral_strategy)
@settings(max_examples=50)
def test_expressions::stringliteral_instantiation(instance):
    assert isinstance(instance, expressions::StringLiteral)

@given(instance=expressions::StringLiteral_strategy)
def test_expressions::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expressions::StringLiteral_strategy)
def test_expressions::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::IntLiteral_strategy)
@settings(max_examples=50)
def test_expressions::intliteral_instantiation(instance):
    assert isinstance(instance, expressions::IntLiteral)

@given(instance=expressions::IntLiteral_strategy)
def test_expressions::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expressions::IntLiteral_strategy)
def test_expressions::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::FloatLiteral_strategy)
@settings(max_examples=50)
def test_expressions::floatliteral_instantiation(instance):
    assert isinstance(instance, expressions::FloatLiteral)

@given(instance=expressions::FloatLiteral_strategy)
def test_expressions::floatliteral_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=expressions::FloatLiteral_strategy)
def test_expressions::floatliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::NullLiteral_strategy)
@settings(max_examples=50)
def test_expressions::nullliteral_instantiation(instance):
    assert isinstance(instance, expressions::NullLiteral)

@given(instance=expressions::BoolLiteral_strategy)
@settings(max_examples=50)
def test_expressions::boolliteral_instantiation(instance):
    assert isinstance(instance, expressions::BoolLiteral)

@given(instance=expressions::BoolLiteral_strategy)
def test_expressions::boolliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=expressions::BoolLiteral_strategy)
def test_expressions::boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressions::Literal_strategy)
@settings(max_examples=50)
def test_expressions::literal_instantiation(instance):
    assert isinstance(instance, expressions::Literal)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressions::ConditionalExpression_strategy)
@settings(max_examples=50)
def test_expressions::conditionalexpression_instantiation(instance):
    assert isinstance(instance, expressions::ConditionalExpression)

@given(instance=expressions::UnaryExpression_strategy)
@settings(max_examples=50)
def test_expressions::unaryexpression_instantiation(instance):
    assert isinstance(instance, expressions::UnaryExpression)

@given(instance=expressions::ArgumentExpression_strategy)
@settings(max_examples=50)
def test_expressions::argumentexpression_instantiation(instance):
    assert isinstance(instance, expressions::ArgumentExpression)

@given(instance=expressions::TypeCastExpression_strategy)
@settings(max_examples=50)
def test_expressions::typecastexpression_instantiation(instance):
    assert isinstance(instance, expressions::TypeCastExpression)

@given(instance=expressions::ParenthesizedExpression_strategy)
@settings(max_examples=50)
def test_expressions::parenthesizedexpression_instantiation(instance):
    assert isinstance(instance, expressions::ParenthesizedExpression)

@given(instance=expressions::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_expressions::assignmentexpression_instantiation(instance):
    assert isinstance(instance, expressions::AssignmentExpression)

@given(instance=expressions::AssignmentExpression_strategy)
def test_expressions::assignmentexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=expressions::AssignmentExpression_strategy)
def test_expressions::assignmentexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=expressions::PrimitiveValueExpression_strategy)
@settings(max_examples=50)
def test_expressions::primitivevalueexpression_instantiation(instance):
    assert isinstance(instance, expressions::PrimitiveValueExpression)

@given(instance=expressions::BinaryExpression_strategy)
@settings(max_examples=50)
def test_expressions::binaryexpression_instantiation(instance):
    assert isinstance(instance, expressions::BinaryExpression)

@given(instance=expressions::Expression_strategy)
@settings(max_examples=50)
def test_expressions::expression_instantiation(instance):
    assert isinstance(instance, expressions::Expression)
