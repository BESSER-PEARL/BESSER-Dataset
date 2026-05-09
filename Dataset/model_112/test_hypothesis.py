import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    javasimplified::BooleanLiteral,
    javasimplified::ArrayCreation,
    javasimplified::StringLiteral,
    javasimplified::NullLiteral,
    javasimplified::ThisExpression,
    javasimplified::VariableAccess,
    javasimplified::InstanceOfExpression,
    javasimplified::ClassInstanceCreation,
    javasimplified::NumberLiteral,
    javasimplified::ArrayAccess,
    javasimplified::CastExpression,
    javasimplified::Assignment,
    javasimplified::Expression,
    javasimplified::NamedElement,
    javasimplified::ImportDeclaration,
    Type,
    javasimplified::Interface,
    javasimplified::PrimitiveType,
    javasimplified::Comment,
    Statement,
    javasimplified::TryStatement,
    javasimplified::ThrowStatement,
    javasimplified::CatchStatment,
    javasimplified::IfStatement,
    javasimplified::ForStatement,
    javasimplified::Block,
    javasimplified::ReturnStatement,
    javasimplified::WhileStatement,
    javasimplified::ExpressionStatement,
    javasimplified::Variable,
    javasimplified::Statement,
    javasimplified::Modifier,
    javasimplified::Class,
    NamedElement,
    javasimplified::Parameter,
    javasimplified::Package,
    javasimplified::Model,
    javasimplified::Type,
    javasimplified::Method,
    VisibilityKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(javasimplified::BooleanLiteral)


def test_javasimplified::booleanliteral_constructor_exists():
    assert callable(javasimplified::BooleanLiteral.__init__)


def test_javasimplified::booleanliteral_constructor_args():
    sig = inspect.signature(javasimplified::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_javasimplified::booleanliteral_has_value():
    assert hasattr(javasimplified::BooleanLiteral, "value")
    descriptor = None
    for klass in javasimplified::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::arraycreation_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ArrayCreation)


def test_javasimplified::arraycreation_constructor_exists():
    assert callable(javasimplified::ArrayCreation.__init__)


def test_javasimplified::arraycreation_constructor_args():
    sig = inspect.signature(javasimplified::ArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::stringliteral_is_not_abstract():
    assert not inspect.isabstract(javasimplified::StringLiteral)


def test_javasimplified::stringliteral_constructor_exists():
    assert callable(javasimplified::StringLiteral.__init__)


def test_javasimplified::stringliteral_constructor_args():
    sig = inspect.signature(javasimplified::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_javasimplified::stringliteral_has_value():
    assert hasattr(javasimplified::StringLiteral, "value")
    descriptor = None
    for klass in javasimplified::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::nullliteral_is_not_abstract():
    assert not inspect.isabstract(javasimplified::NullLiteral)


def test_javasimplified::nullliteral_constructor_exists():
    assert callable(javasimplified::NullLiteral.__init__)


def test_javasimplified::nullliteral_constructor_args():
    sig = inspect.signature(javasimplified::NullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::thisexpression_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ThisExpression)


def test_javasimplified::thisexpression_constructor_exists():
    assert callable(javasimplified::ThisExpression.__init__)


def test_javasimplified::thisexpression_constructor_args():
    sig = inspect.signature(javasimplified::ThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::variableaccess_is_not_abstract():
    assert not inspect.isabstract(javasimplified::VariableAccess)


def test_javasimplified::variableaccess_constructor_exists():
    assert callable(javasimplified::VariableAccess.__init__)


def test_javasimplified::variableaccess_constructor_args():
    sig = inspect.signature(javasimplified::VariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::instanceofexpression_is_not_abstract():
    assert not inspect.isabstract(javasimplified::InstanceOfExpression)


def test_javasimplified::instanceofexpression_constructor_exists():
    assert callable(javasimplified::InstanceOfExpression.__init__)


def test_javasimplified::instanceofexpression_constructor_args():
    sig = inspect.signature(javasimplified::InstanceOfExpression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::classinstancecreation_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ClassInstanceCreation)


def test_javasimplified::classinstancecreation_constructor_exists():
    assert callable(javasimplified::ClassInstanceCreation.__init__)


def test_javasimplified::classinstancecreation_constructor_args():
    sig = inspect.signature(javasimplified::ClassInstanceCreation.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::numberliteral_is_not_abstract():
    assert not inspect.isabstract(javasimplified::NumberLiteral)


def test_javasimplified::numberliteral_constructor_exists():
    assert callable(javasimplified::NumberLiteral.__init__)


def test_javasimplified::numberliteral_constructor_args():
    sig = inspect.signature(javasimplified::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_javasimplified::numberliteral_has_value():
    assert hasattr(javasimplified::NumberLiteral, "value")
    descriptor = None
    for klass in javasimplified::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::arrayaccess_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ArrayAccess)


def test_javasimplified::arrayaccess_constructor_exists():
    assert callable(javasimplified::ArrayAccess.__init__)


def test_javasimplified::arrayaccess_constructor_args():
    sig = inspect.signature(javasimplified::ArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::castexpression_is_not_abstract():
    assert not inspect.isabstract(javasimplified::CastExpression)


def test_javasimplified::castexpression_constructor_exists():
    assert callable(javasimplified::CastExpression.__init__)


def test_javasimplified::castexpression_constructor_args():
    sig = inspect.signature(javasimplified::CastExpression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::assignment_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Assignment)


def test_javasimplified::assignment_constructor_exists():
    assert callable(javasimplified::Assignment.__init__)


def test_javasimplified::assignment_constructor_args():
    sig = inspect.signature(javasimplified::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::expression_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Expression)


def test_javasimplified::expression_constructor_exists():
    assert callable(javasimplified::Expression.__init__)


def test_javasimplified::expression_constructor_args():
    sig = inspect.signature(javasimplified::Expression.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::namedelement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::NamedElement)


def test_javasimplified::namedelement_constructor_exists():
    assert callable(javasimplified::NamedElement.__init__)


def test_javasimplified::namedelement_constructor_args():
    sig = inspect.signature(javasimplified::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javasimplified::namedelement_has_name():
    assert hasattr(javasimplified::NamedElement, "name")
    descriptor = None
    for klass in javasimplified::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::importdeclaration_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ImportDeclaration)


def test_javasimplified::importdeclaration_constructor_exists():
    assert callable(javasimplified::ImportDeclaration.__init__)


def test_javasimplified::importdeclaration_constructor_args():
    sig = inspect.signature(javasimplified::ImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::interface_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Interface)


def test_javasimplified::interface_constructor_exists():
    assert callable(javasimplified::Interface.__init__)


def test_javasimplified::interface_constructor_args():
    sig = inspect.signature(javasimplified::Interface.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::primitivetype_is_not_abstract():
    assert not inspect.isabstract(javasimplified::PrimitiveType)


def test_javasimplified::primitivetype_constructor_exists():
    assert callable(javasimplified::PrimitiveType.__init__)


def test_javasimplified::primitivetype_constructor_args():
    sig = inspect.signature(javasimplified::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::comment_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Comment)


def test_javasimplified::comment_constructor_exists():
    assert callable(javasimplified::Comment.__init__)


def test_javasimplified::comment_constructor_args():
    sig = inspect.signature(javasimplified::Comment.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::trystatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::TryStatement)


def test_javasimplified::trystatement_constructor_exists():
    assert callable(javasimplified::TryStatement.__init__)


def test_javasimplified::trystatement_constructor_args():
    sig = inspect.signature(javasimplified::TryStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::throwstatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ThrowStatement)


def test_javasimplified::throwstatement_constructor_exists():
    assert callable(javasimplified::ThrowStatement.__init__)


def test_javasimplified::throwstatement_constructor_args():
    sig = inspect.signature(javasimplified::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::catchstatment_is_not_abstract():
    assert not inspect.isabstract(javasimplified::CatchStatment)


def test_javasimplified::catchstatment_constructor_exists():
    assert callable(javasimplified::CatchStatment.__init__)


def test_javasimplified::catchstatment_constructor_args():
    sig = inspect.signature(javasimplified::CatchStatment.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::ifstatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::IfStatement)


def test_javasimplified::ifstatement_constructor_exists():
    assert callable(javasimplified::IfStatement.__init__)


def test_javasimplified::ifstatement_constructor_args():
    sig = inspect.signature(javasimplified::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::forstatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ForStatement)


def test_javasimplified::forstatement_constructor_exists():
    assert callable(javasimplified::ForStatement.__init__)


def test_javasimplified::forstatement_constructor_args():
    sig = inspect.signature(javasimplified::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::block_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Block)


def test_javasimplified::block_constructor_exists():
    assert callable(javasimplified::Block.__init__)


def test_javasimplified::block_constructor_args():
    sig = inspect.signature(javasimplified::Block.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::returnstatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ReturnStatement)


def test_javasimplified::returnstatement_constructor_exists():
    assert callable(javasimplified::ReturnStatement.__init__)


def test_javasimplified::returnstatement_constructor_args():
    sig = inspect.signature(javasimplified::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::whilestatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::WhileStatement)


def test_javasimplified::whilestatement_constructor_exists():
    assert callable(javasimplified::WhileStatement.__init__)


def test_javasimplified::whilestatement_constructor_args():
    sig = inspect.signature(javasimplified::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::ExpressionStatement)


def test_javasimplified::expressionstatement_constructor_exists():
    assert callable(javasimplified::ExpressionStatement.__init__)


def test_javasimplified::expressionstatement_constructor_args():
    sig = inspect.signature(javasimplified::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::variable_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Variable)


def test_javasimplified::variable_constructor_exists():
    assert callable(javasimplified::Variable.__init__)


def test_javasimplified::variable_constructor_args():
    sig = inspect.signature(javasimplified::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_javasimplified::variable_has_name():
    assert hasattr(javasimplified::Variable, "name")
    descriptor = None
    for klass in javasimplified::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::statement_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Statement)


def test_javasimplified::statement_constructor_exists():
    assert callable(javasimplified::Statement.__init__)


def test_javasimplified::statement_constructor_args():
    sig = inspect.signature(javasimplified::Statement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::modifier_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Modifier)


def test_javasimplified::modifier_constructor_exists():
    assert callable(javasimplified::Modifier.__init__)


def test_javasimplified::modifier_constructor_args():
    sig = inspect.signature(javasimplified::Modifier.__init__)
    params = list(sig.parameters.keys())
    assert "isVolatile" in params, "Missing parameter 'isVolatile'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"
    assert "isSynchronized" in params, "Missing parameter 'isSynchronized'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_javasimplified::modifier_has_isVolatile():
    assert hasattr(javasimplified::Modifier, "isVolatile")
    descriptor = None
    for klass in javasimplified::Modifier.__mro__:
        if "isVolatile" in klass.__dict__:
            descriptor = klass.__dict__["isVolatile"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified::modifier_has_visibility():
    assert hasattr(javasimplified::Modifier, "visibility")
    descriptor = None
    for klass in javasimplified::Modifier.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified::modifier_has_isStatic():
    assert hasattr(javasimplified::Modifier, "isStatic")
    descriptor = None
    for klass in javasimplified::Modifier.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified::modifier_has_isSynchronized():
    assert hasattr(javasimplified::Modifier, "isSynchronized")
    descriptor = None
    for klass in javasimplified::Modifier.__mro__:
        if "isSynchronized" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronized"]
            break
    assert isinstance(descriptor, property)

def test_javasimplified::modifier_has_isFinal():
    assert hasattr(javasimplified::Modifier, "isFinal")
    descriptor = None
    for klass in javasimplified::Modifier.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_javasimplified::class_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Class)


def test_javasimplified::class_constructor_exists():
    assert callable(javasimplified::Class.__init__)


def test_javasimplified::class_constructor_args():
    sig = inspect.signature(javasimplified::Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_javasimplified::class_has_isAbstract():
    assert hasattr(javasimplified::Class, "isAbstract")
    descriptor = None
    for klass in javasimplified::Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::parameter_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Parameter)


def test_javasimplified::parameter_constructor_exists():
    assert callable(javasimplified::Parameter.__init__)


def test_javasimplified::parameter_constructor_args():
    sig = inspect.signature(javasimplified::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::package_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Package)


def test_javasimplified::package_constructor_exists():
    assert callable(javasimplified::Package.__init__)


def test_javasimplified::package_constructor_args():
    sig = inspect.signature(javasimplified::Package.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::model_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Model)


def test_javasimplified::model_constructor_exists():
    assert callable(javasimplified::Model.__init__)


def test_javasimplified::model_constructor_args():
    sig = inspect.signature(javasimplified::Model.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::type_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Type)


def test_javasimplified::type_constructor_exists():
    assert callable(javasimplified::Type.__init__)


def test_javasimplified::type_constructor_args():
    sig = inspect.signature(javasimplified::Type.__init__)
    params = list(sig.parameters.keys())



def test_javasimplified::method_is_not_abstract():
    assert not inspect.isabstract(javasimplified::Method)


def test_javasimplified::method_constructor_exists():
    assert callable(javasimplified::Method.__init__)


def test_javasimplified::method_constructor_args():
    sig = inspect.signature(javasimplified::Method.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_javasimplified::method_has_visibility():
    assert hasattr(javasimplified::Method, "visibility")
    descriptor = None
    for klass in javasimplified::Method.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "none",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"


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
Expression_strategy = st.builds(
    Expression,
)
javasimplified::BooleanLiteral_strategy = st.builds(
    javasimplified::BooleanLiteral,
    value=
        st.booleans()
)
javasimplified::ArrayCreation_strategy = st.builds(
    javasimplified::ArrayCreation,
)
javasimplified::StringLiteral_strategy = st.builds(
    javasimplified::StringLiteral,
    value=
        safe_text
)
javasimplified::NullLiteral_strategy = st.builds(
    javasimplified::NullLiteral,
)
javasimplified::ThisExpression_strategy = st.builds(
    javasimplified::ThisExpression,
)
javasimplified::VariableAccess_strategy = st.builds(
    javasimplified::VariableAccess,
)
javasimplified::InstanceOfExpression_strategy = st.builds(
    javasimplified::InstanceOfExpression,
)
javasimplified::ClassInstanceCreation_strategy = st.builds(
    javasimplified::ClassInstanceCreation,
)
javasimplified::NumberLiteral_strategy = st.builds(
    javasimplified::NumberLiteral,
    value=
        safe_text
)
javasimplified::ArrayAccess_strategy = st.builds(
    javasimplified::ArrayAccess,
)
javasimplified::CastExpression_strategy = st.builds(
    javasimplified::CastExpression,
)
javasimplified::Assignment_strategy = st.builds(
    javasimplified::Assignment,
)
javasimplified::Expression_strategy = st.builds(
    javasimplified::Expression,
)
javasimplified::NamedElement_strategy = st.builds(
    javasimplified::NamedElement,
    name=
        safe_text
)
javasimplified::ImportDeclaration_strategy = st.builds(
    javasimplified::ImportDeclaration,
)
Type_strategy = st.builds(
    Type,
)
javasimplified::Interface_strategy = st.builds(
    javasimplified::Interface,
)
javasimplified::PrimitiveType_strategy = st.builds(
    javasimplified::PrimitiveType,
)
javasimplified::Comment_strategy = st.builds(
    javasimplified::Comment,
)
Statement_strategy = st.builds(
    Statement,
)
javasimplified::TryStatement_strategy = st.builds(
    javasimplified::TryStatement,
)
javasimplified::ThrowStatement_strategy = st.builds(
    javasimplified::ThrowStatement,
)
javasimplified::CatchStatment_strategy = st.builds(
    javasimplified::CatchStatment,
)
javasimplified::IfStatement_strategy = st.builds(
    javasimplified::IfStatement,
)
javasimplified::ForStatement_strategy = st.builds(
    javasimplified::ForStatement,
)
javasimplified::Block_strategy = st.builds(
    javasimplified::Block,
)
javasimplified::ReturnStatement_strategy = st.builds(
    javasimplified::ReturnStatement,
)
javasimplified::WhileStatement_strategy = st.builds(
    javasimplified::WhileStatement,
)
javasimplified::ExpressionStatement_strategy = st.builds(
    javasimplified::ExpressionStatement,
)
javasimplified::Variable_strategy = st.builds(
    javasimplified::Variable,
    name=
        safe_text
)
javasimplified::Statement_strategy = st.builds(
    javasimplified::Statement,
)
javasimplified::Modifier_strategy = st.builds(
    javasimplified::Modifier,
    isVolatile=
        st.booleans(),
    visibility=
        safe_text,
    isStatic=
        st.booleans(),
    isSynchronized=
        st.booleans(),
    isFinal=
        st.booleans()
)
javasimplified::Class_strategy = st.builds(
    javasimplified::Class,
    isAbstract=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
javasimplified::Parameter_strategy = st.builds(
    javasimplified::Parameter,
)
javasimplified::Package_strategy = st.builds(
    javasimplified::Package,
)
javasimplified::Model_strategy = st.builds(
    javasimplified::Model,
)
javasimplified::Type_strategy = st.builds(
    javasimplified::Type,
)
javasimplified::Method_strategy = st.builds(
    javasimplified::Method,
    visibility=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=javasimplified::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_javasimplified::booleanliteral_instantiation(instance):
    assert isinstance(instance, javasimplified::BooleanLiteral)

@given(instance=javasimplified::BooleanLiteral_strategy)
def test_javasimplified::booleanliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=javasimplified::BooleanLiteral_strategy)
def test_javasimplified::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=javasimplified::ArrayCreation_strategy)
@settings(max_examples=50)
def test_javasimplified::arraycreation_instantiation(instance):
    assert isinstance(instance, javasimplified::ArrayCreation)

@given(instance=javasimplified::StringLiteral_strategy)
@settings(max_examples=50)
def test_javasimplified::stringliteral_instantiation(instance):
    assert isinstance(instance, javasimplified::StringLiteral)

@given(instance=javasimplified::StringLiteral_strategy)
def test_javasimplified::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=javasimplified::StringLiteral_strategy)
def test_javasimplified::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=javasimplified::NullLiteral_strategy)
@settings(max_examples=50)
def test_javasimplified::nullliteral_instantiation(instance):
    assert isinstance(instance, javasimplified::NullLiteral)

@given(instance=javasimplified::ThisExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::thisexpression_instantiation(instance):
    assert isinstance(instance, javasimplified::ThisExpression)

@given(instance=javasimplified::VariableAccess_strategy)
@settings(max_examples=50)
def test_javasimplified::variableaccess_instantiation(instance):
    assert isinstance(instance, javasimplified::VariableAccess)

@given(instance=javasimplified::InstanceOfExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::instanceofexpression_instantiation(instance):
    assert isinstance(instance, javasimplified::InstanceOfExpression)

@given(instance=javasimplified::ClassInstanceCreation_strategy)
@settings(max_examples=50)
def test_javasimplified::classinstancecreation_instantiation(instance):
    assert isinstance(instance, javasimplified::ClassInstanceCreation)

@given(instance=javasimplified::NumberLiteral_strategy)
@settings(max_examples=50)
def test_javasimplified::numberliteral_instantiation(instance):
    assert isinstance(instance, javasimplified::NumberLiteral)

@given(instance=javasimplified::NumberLiteral_strategy)
def test_javasimplified::numberliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=javasimplified::NumberLiteral_strategy)
def test_javasimplified::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=javasimplified::ArrayAccess_strategy)
@settings(max_examples=50)
def test_javasimplified::arrayaccess_instantiation(instance):
    assert isinstance(instance, javasimplified::ArrayAccess)

@given(instance=javasimplified::CastExpression_strategy)
@settings(max_examples=50)
def test_javasimplified::castexpression_instantiation(instance):
    assert isinstance(instance, javasimplified::CastExpression)

@given(instance=javasimplified::Assignment_strategy)
@settings(max_examples=50)
def test_javasimplified::assignment_instantiation(instance):
    assert isinstance(instance, javasimplified::Assignment)

@given(instance=javasimplified::Expression_strategy)
@settings(max_examples=50)
def test_javasimplified::expression_instantiation(instance):
    assert isinstance(instance, javasimplified::Expression)

@given(instance=javasimplified::NamedElement_strategy)
@settings(max_examples=50)
def test_javasimplified::namedelement_instantiation(instance):
    assert isinstance(instance, javasimplified::NamedElement)

@given(instance=javasimplified::NamedElement_strategy)
def test_javasimplified::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javasimplified::NamedElement_strategy)
def test_javasimplified::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javasimplified::ImportDeclaration_strategy)
@settings(max_examples=50)
def test_javasimplified::importdeclaration_instantiation(instance):
    assert isinstance(instance, javasimplified::ImportDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=javasimplified::Interface_strategy)
@settings(max_examples=50)
def test_javasimplified::interface_instantiation(instance):
    assert isinstance(instance, javasimplified::Interface)

@given(instance=javasimplified::PrimitiveType_strategy)
@settings(max_examples=50)
def test_javasimplified::primitivetype_instantiation(instance):
    assert isinstance(instance, javasimplified::PrimitiveType)

@given(instance=javasimplified::Comment_strategy)
@settings(max_examples=50)
def test_javasimplified::comment_instantiation(instance):
    assert isinstance(instance, javasimplified::Comment)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=javasimplified::TryStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::trystatement_instantiation(instance):
    assert isinstance(instance, javasimplified::TryStatement)

@given(instance=javasimplified::ThrowStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::throwstatement_instantiation(instance):
    assert isinstance(instance, javasimplified::ThrowStatement)

@given(instance=javasimplified::CatchStatment_strategy)
@settings(max_examples=50)
def test_javasimplified::catchstatment_instantiation(instance):
    assert isinstance(instance, javasimplified::CatchStatment)

@given(instance=javasimplified::IfStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::ifstatement_instantiation(instance):
    assert isinstance(instance, javasimplified::IfStatement)

@given(instance=javasimplified::ForStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::forstatement_instantiation(instance):
    assert isinstance(instance, javasimplified::ForStatement)

@given(instance=javasimplified::Block_strategy)
@settings(max_examples=50)
def test_javasimplified::block_instantiation(instance):
    assert isinstance(instance, javasimplified::Block)

@given(instance=javasimplified::ReturnStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::returnstatement_instantiation(instance):
    assert isinstance(instance, javasimplified::ReturnStatement)

@given(instance=javasimplified::WhileStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::whilestatement_instantiation(instance):
    assert isinstance(instance, javasimplified::WhileStatement)

@given(instance=javasimplified::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_javasimplified::expressionstatement_instantiation(instance):
    assert isinstance(instance, javasimplified::ExpressionStatement)

@given(instance=javasimplified::Variable_strategy)
@settings(max_examples=50)
def test_javasimplified::variable_instantiation(instance):
    assert isinstance(instance, javasimplified::Variable)

@given(instance=javasimplified::Variable_strategy)
def test_javasimplified::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=javasimplified::Variable_strategy)
def test_javasimplified::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=javasimplified::Statement_strategy)
@settings(max_examples=50)
def test_javasimplified::statement_instantiation(instance):
    assert isinstance(instance, javasimplified::Statement)

@given(instance=javasimplified::Modifier_strategy)
@settings(max_examples=50)
def test_javasimplified::modifier_instantiation(instance):
    assert isinstance(instance, javasimplified::Modifier)

@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isVolatile_type(instance):
    assert isinstance(instance.isVolatile, bool)


@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isVolatile_setter(instance):
    original = instance.isVolatile
    instance.isVolatile = original
    assert instance.isVolatile == original

@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isStatic_type(instance):
    assert isinstance(instance.isStatic, bool)


@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isSynchronized_type(instance):
    assert isinstance(instance.isSynchronized, bool)


@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isSynchronized_setter(instance):
    original = instance.isSynchronized
    instance.isSynchronized = original
    assert instance.isSynchronized == original

@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=javasimplified::Modifier_strategy)
def test_javasimplified::modifier_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=javasimplified::Class_strategy)
@settings(max_examples=50)
def test_javasimplified::class_instantiation(instance):
    assert isinstance(instance, javasimplified::Class)

@given(instance=javasimplified::Class_strategy)
def test_javasimplified::class_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=javasimplified::Class_strategy)
def test_javasimplified::class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=javasimplified::Parameter_strategy)
@settings(max_examples=50)
def test_javasimplified::parameter_instantiation(instance):
    assert isinstance(instance, javasimplified::Parameter)

@given(instance=javasimplified::Package_strategy)
@settings(max_examples=50)
def test_javasimplified::package_instantiation(instance):
    assert isinstance(instance, javasimplified::Package)

@given(instance=javasimplified::Model_strategy)
@settings(max_examples=50)
def test_javasimplified::model_instantiation(instance):
    assert isinstance(instance, javasimplified::Model)

@given(instance=javasimplified::Type_strategy)
@settings(max_examples=50)
def test_javasimplified::type_instantiation(instance):
    assert isinstance(instance, javasimplified::Type)

@given(instance=javasimplified::Method_strategy)
@settings(max_examples=50)
def test_javasimplified::method_instantiation(instance):
    assert isinstance(instance, javasimplified::Method)

@given(instance=javasimplified::Method_strategy)
def test_javasimplified::method_visibility_type(instance):
    assert isinstance(instance.visibility, str)


@given(instance=javasimplified::Method_strategy)
def test_javasimplified::method_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original
