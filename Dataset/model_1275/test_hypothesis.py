import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocl::uml::TemplateParameterType,
    ocl::uml::VariableExp,
    ocl::uml::Variable,
    ocl::uml::LetExp,
    ocl::uml::IteratorExp,
    ocl::uml::LoopExp,
    ocl::uml::IterateExp,
    ocl::uml::InvalidLiteralExp,
    ocl::uml::UnspecifiedValueExp,
    ocl::uml::TypeExp,
    ocl::uml::TupleLiteralPart,
    ocl::uml::TupleLiteralExp,
    ocl::uml::StringLiteralExp,
    ocl::uml::StateExp,
    ocl::uml::RealLiteralExp,
    ocl::uml::PropertyCallExp,
    ocl::uml::OperationCallExp,
    ocl::uml::NullLiteralExp,
    ocl::uml::MessageExp,
    ocl::uml::OCLExpression,
    ocl::uml::CallExp,
    ocl::uml::FeatureCallExp,
    ocl::uml::NavigationCallExp,
    ocl::uml::AssociationClassCallExp,
    ocl::uml::UnlimitedNaturalLiteralExp,
    ocl::uml::NumericLiteralExp,
    ocl::uml::IntegerLiteralExp,
    ocl::uml::IfExp,
    ocl::uml::EnumLiteralExp,
    ocl::uml::CollectionRange,
    ocl::uml::CollectionLiteralExp,
    ocl::uml::CollectionLiteralPart,
    ocl::uml::CollectionItem,
    ocl::uml::LiteralExp,
    ocl::uml::PrimitiveLiteralExp,
    ocl::uml::BooleanLiteralExp,
    ocl::uml::TypeType,
    types::ElementType,
    Classifier,
    ocl::uml::ElementType,
    ocl::uml::ExpressionInOCL,
    ocl::uml::SequenceType,
    ocl::uml::OrderedSetType,
    ocl::uml::SetType,
    ocl::uml::BagType,
    ocl::uml::TupleType,
    ocl::uml::CollectionType,
    ocl::uml::PrimitiveType,
    uml::ocl::Property,
    ocl::uml::MessageType,
    ocl::uml::InvalidType,
    ocl::uml::VoidType,
    uml::ocl::Operation,
    ocl::uml::AnyType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl::uml::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TemplateParameterType)


def test_ocl::uml::templateparametertype_constructor_exists():
    assert callable(ocl::uml::TemplateParameterType.__init__)


def test_ocl::uml::templateparametertype_constructor_args():
    sig = inspect.signature(ocl::uml::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::VariableExp)


def test_ocl::uml::variableexp_constructor_exists():
    assert callable(ocl::uml::VariableExp.__init__)


def test_ocl::uml::variableexp_constructor_args():
    sig = inspect.signature(ocl::uml::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::variable_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::Variable)


def test_ocl::uml::variable_constructor_exists():
    assert callable(ocl::uml::Variable.__init__)


def test_ocl::uml::variable_constructor_args():
    sig = inspect.signature(ocl::uml::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::letexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::LetExp)


def test_ocl::uml::letexp_constructor_exists():
    assert callable(ocl::uml::LetExp.__init__)


def test_ocl::uml::letexp_constructor_args():
    sig = inspect.signature(ocl::uml::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::IteratorExp)


def test_ocl::uml::iteratorexp_constructor_exists():
    assert callable(ocl::uml::IteratorExp.__init__)


def test_ocl::uml::iteratorexp_constructor_args():
    sig = inspect.signature(ocl::uml::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::LoopExp)


def test_ocl::uml::loopexp_constructor_exists():
    assert callable(ocl::uml::LoopExp.__init__)


def test_ocl::uml::loopexp_constructor_args():
    sig = inspect.signature(ocl::uml::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::IterateExp)


def test_ocl::uml::iterateexp_constructor_exists():
    assert callable(ocl::uml::IterateExp.__init__)


def test_ocl::uml::iterateexp_constructor_args():
    sig = inspect.signature(ocl::uml::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::InvalidLiteralExp)


def test_ocl::uml::invalidliteralexp_constructor_exists():
    assert callable(ocl::uml::InvalidLiteralExp.__init__)


def test_ocl::uml::invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::UnspecifiedValueExp)


def test_ocl::uml::unspecifiedvalueexp_constructor_exists():
    assert callable(ocl::uml::UnspecifiedValueExp.__init__)


def test_ocl::uml::unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl::uml::UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TypeExp)


def test_ocl::uml::typeexp_constructor_exists():
    assert callable(ocl::uml::TypeExp.__init__)


def test_ocl::uml::typeexp_constructor_args():
    sig = inspect.signature(ocl::uml::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TupleLiteralPart)


def test_ocl::uml::tupleliteralpart_constructor_exists():
    assert callable(ocl::uml::TupleLiteralPart.__init__)


def test_ocl::uml::tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl::uml::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TupleLiteralExp)


def test_ocl::uml::tupleliteralexp_constructor_exists():
    assert callable(ocl::uml::TupleLiteralExp.__init__)


def test_ocl::uml::tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::StringLiteralExp)


def test_ocl::uml::stringliteralexp_constructor_exists():
    assert callable(ocl::uml::StringLiteralExp.__init__)


def test_ocl::uml::stringliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::StateExp)


def test_ocl::uml::stateexp_constructor_exists():
    assert callable(ocl::uml::StateExp.__init__)


def test_ocl::uml::stateexp_constructor_args():
    sig = inspect.signature(ocl::uml::StateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::RealLiteralExp)


def test_ocl::uml::realliteralexp_constructor_exists():
    assert callable(ocl::uml::RealLiteralExp.__init__)


def test_ocl::uml::realliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::PropertyCallExp)


def test_ocl::uml::propertycallexp_constructor_exists():
    assert callable(ocl::uml::PropertyCallExp.__init__)


def test_ocl::uml::propertycallexp_constructor_args():
    sig = inspect.signature(ocl::uml::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::OperationCallExp)


def test_ocl::uml::operationcallexp_constructor_exists():
    assert callable(ocl::uml::OperationCallExp.__init__)


def test_ocl::uml::operationcallexp_constructor_args():
    sig = inspect.signature(ocl::uml::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::NullLiteralExp)


def test_ocl::uml::nullliteralexp_constructor_exists():
    assert callable(ocl::uml::NullLiteralExp.__init__)


def test_ocl::uml::nullliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::MessageExp)


def test_ocl::uml::messageexp_constructor_exists():
    assert callable(ocl::uml::MessageExp.__init__)


def test_ocl::uml::messageexp_constructor_args():
    sig = inspect.signature(ocl::uml::MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::OCLExpression)


def test_ocl::uml::oclexpression_constructor_exists():
    assert callable(ocl::uml::OCLExpression.__init__)


def test_ocl::uml::oclexpression_constructor_args():
    sig = inspect.signature(ocl::uml::OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::callexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CallExp)


def test_ocl::uml::callexp_constructor_exists():
    assert callable(ocl::uml::CallExp.__init__)


def test_ocl::uml::callexp_constructor_args():
    sig = inspect.signature(ocl::uml::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::FeatureCallExp)


def test_ocl::uml::featurecallexp_constructor_exists():
    assert callable(ocl::uml::FeatureCallExp.__init__)


def test_ocl::uml::featurecallexp_constructor_args():
    sig = inspect.signature(ocl::uml::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::NavigationCallExp)


def test_ocl::uml::navigationcallexp_constructor_exists():
    assert callable(ocl::uml::NavigationCallExp.__init__)


def test_ocl::uml::navigationcallexp_constructor_args():
    sig = inspect.signature(ocl::uml::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::AssociationClassCallExp)


def test_ocl::uml::associationclasscallexp_constructor_exists():
    assert callable(ocl::uml::AssociationClassCallExp.__init__)


def test_ocl::uml::associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl::uml::AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::UnlimitedNaturalLiteralExp)


def test_ocl::uml::unlimitednaturalliteralexp_constructor_exists():
    assert callable(ocl::uml::UnlimitedNaturalLiteralExp.__init__)


def test_ocl::uml::unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::NumericLiteralExp)


def test_ocl::uml::numericliteralexp_constructor_exists():
    assert callable(ocl::uml::NumericLiteralExp.__init__)


def test_ocl::uml::numericliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::IntegerLiteralExp)


def test_ocl::uml::integerliteralexp_constructor_exists():
    assert callable(ocl::uml::IntegerLiteralExp.__init__)


def test_ocl::uml::integerliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::IfExp)


def test_ocl::uml::ifexp_constructor_exists():
    assert callable(ocl::uml::IfExp.__init__)


def test_ocl::uml::ifexp_constructor_args():
    sig = inspect.signature(ocl::uml::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::EnumLiteralExp)


def test_ocl::uml::enumliteralexp_constructor_exists():
    assert callable(ocl::uml::EnumLiteralExp.__init__)


def test_ocl::uml::enumliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CollectionRange)


def test_ocl::uml::collectionrange_constructor_exists():
    assert callable(ocl::uml::CollectionRange.__init__)


def test_ocl::uml::collectionrange_constructor_args():
    sig = inspect.signature(ocl::uml::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CollectionLiteralExp)


def test_ocl::uml::collectionliteralexp_constructor_exists():
    assert callable(ocl::uml::CollectionLiteralExp.__init__)


def test_ocl::uml::collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CollectionLiteralPart)


def test_ocl::uml::collectionliteralpart_constructor_exists():
    assert callable(ocl::uml::CollectionLiteralPart.__init__)


def test_ocl::uml::collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl::uml::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CollectionItem)


def test_ocl::uml::collectionitem_constructor_exists():
    assert callable(ocl::uml::CollectionItem.__init__)


def test_ocl::uml::collectionitem_constructor_args():
    sig = inspect.signature(ocl::uml::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::LiteralExp)


def test_ocl::uml::literalexp_constructor_exists():
    assert callable(ocl::uml::LiteralExp.__init__)


def test_ocl::uml::literalexp_constructor_args():
    sig = inspect.signature(ocl::uml::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::PrimitiveLiteralExp)


def test_ocl::uml::primitiveliteralexp_constructor_exists():
    assert callable(ocl::uml::PrimitiveLiteralExp.__init__)


def test_ocl::uml::primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::BooleanLiteralExp)


def test_ocl::uml::booleanliteralexp_constructor_exists():
    assert callable(ocl::uml::BooleanLiteralExp.__init__)


def test_ocl::uml::booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl::uml::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::typetype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TypeType)


def test_ocl::uml::typetype_constructor_exists():
    assert callable(ocl::uml::TypeType.__init__)


def test_ocl::uml::typetype_constructor_args():
    sig = inspect.signature(ocl::uml::TypeType.__init__)
    params = list(sig.parameters.keys())



def test_types::elementtype_is_not_abstract():
    assert not inspect.isabstract(types::ElementType)


def test_types::elementtype_constructor_exists():
    assert callable(types::ElementType.__init__)


def test_types::elementtype_constructor_args():
    sig = inspect.signature(types::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::ElementType)


def test_ocl::uml::elementtype_constructor_exists():
    assert callable(ocl::uml::ElementType.__init__)


def test_ocl::uml::elementtype_constructor_args():
    sig = inspect.signature(ocl::uml::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::ExpressionInOCL)


def test_ocl::uml::expressioninocl_constructor_exists():
    assert callable(ocl::uml::ExpressionInOCL.__init__)


def test_ocl::uml::expressioninocl_constructor_args():
    sig = inspect.signature(ocl::uml::ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::SequenceType)


def test_ocl::uml::sequencetype_constructor_exists():
    assert callable(ocl::uml::SequenceType.__init__)


def test_ocl::uml::sequencetype_constructor_args():
    sig = inspect.signature(ocl::uml::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::OrderedSetType)


def test_ocl::uml::orderedsettype_constructor_exists():
    assert callable(ocl::uml::OrderedSetType.__init__)


def test_ocl::uml::orderedsettype_constructor_args():
    sig = inspect.signature(ocl::uml::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::settype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::SetType)


def test_ocl::uml::settype_constructor_exists():
    assert callable(ocl::uml::SetType.__init__)


def test_ocl::uml::settype_constructor_args():
    sig = inspect.signature(ocl::uml::SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::BagType)


def test_ocl::uml::bagtype_constructor_exists():
    assert callable(ocl::uml::BagType.__init__)


def test_ocl::uml::bagtype_constructor_args():
    sig = inspect.signature(ocl::uml::BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TupleType)


def test_ocl::uml::tupletype_constructor_exists():
    assert callable(ocl::uml::TupleType.__init__)


def test_ocl::uml::tupletype_constructor_args():
    sig = inspect.signature(ocl::uml::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CollectionType)


def test_ocl::uml::collectiontype_constructor_exists():
    assert callable(ocl::uml::CollectionType.__init__)


def test_ocl::uml::collectiontype_constructor_args():
    sig = inspect.signature(ocl::uml::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::PrimitiveType)


def test_ocl::uml::primitivetype_constructor_exists():
    assert callable(ocl::uml::PrimitiveType.__init__)


def test_ocl::uml::primitivetype_constructor_args():
    sig = inspect.signature(ocl::uml::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml::ocl::property_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::Property)


def test_uml::ocl::property_constructor_exists():
    assert callable(uml::ocl::Property.__init__)


def test_uml::ocl::property_constructor_args():
    sig = inspect.signature(uml::ocl::Property.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::MessageType)


def test_ocl::uml::messagetype_constructor_exists():
    assert callable(ocl::uml::MessageType.__init__)


def test_ocl::uml::messagetype_constructor_args():
    sig = inspect.signature(ocl::uml::MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::InvalidType)


def test_ocl::uml::invalidtype_constructor_exists():
    assert callable(ocl::uml::InvalidType.__init__)


def test_ocl::uml::invalidtype_constructor_args():
    sig = inspect.signature(ocl::uml::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::VoidType)


def test_ocl::uml::voidtype_constructor_exists():
    assert callable(ocl::uml::VoidType.__init__)


def test_ocl::uml::voidtype_constructor_args():
    sig = inspect.signature(ocl::uml::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_uml::ocl::operation_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::Operation)


def test_uml::ocl::operation_constructor_exists():
    assert callable(uml::ocl::Operation.__init__)


def test_uml::ocl::operation_constructor_args():
    sig = inspect.signature(uml::ocl::Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::anytype_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::AnyType)


def test_ocl::uml::anytype_constructor_exists():
    assert callable(ocl::uml::AnyType.__init__)


def test_ocl::uml::anytype_constructor_args():
    sig = inspect.signature(ocl::uml::AnyType.__init__)
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
ocl::uml::TemplateParameterType_strategy = st.builds(
    ocl::uml::TemplateParameterType,
)
ocl::uml::VariableExp_strategy = st.builds(
    ocl::uml::VariableExp,
)
ocl::uml::Variable_strategy = st.builds(
    ocl::uml::Variable,
)
ocl::uml::LetExp_strategy = st.builds(
    ocl::uml::LetExp,
)
ocl::uml::IteratorExp_strategy = st.builds(
    ocl::uml::IteratorExp,
)
ocl::uml::LoopExp_strategy = st.builds(
    ocl::uml::LoopExp,
)
ocl::uml::IterateExp_strategy = st.builds(
    ocl::uml::IterateExp,
)
ocl::uml::InvalidLiteralExp_strategy = st.builds(
    ocl::uml::InvalidLiteralExp,
)
ocl::uml::UnspecifiedValueExp_strategy = st.builds(
    ocl::uml::UnspecifiedValueExp,
)
ocl::uml::TypeExp_strategy = st.builds(
    ocl::uml::TypeExp,
)
ocl::uml::TupleLiteralPart_strategy = st.builds(
    ocl::uml::TupleLiteralPart,
)
ocl::uml::TupleLiteralExp_strategy = st.builds(
    ocl::uml::TupleLiteralExp,
)
ocl::uml::StringLiteralExp_strategy = st.builds(
    ocl::uml::StringLiteralExp,
)
ocl::uml::StateExp_strategy = st.builds(
    ocl::uml::StateExp,
)
ocl::uml::RealLiteralExp_strategy = st.builds(
    ocl::uml::RealLiteralExp,
)
ocl::uml::PropertyCallExp_strategy = st.builds(
    ocl::uml::PropertyCallExp,
)
ocl::uml::OperationCallExp_strategy = st.builds(
    ocl::uml::OperationCallExp,
)
ocl::uml::NullLiteralExp_strategy = st.builds(
    ocl::uml::NullLiteralExp,
)
ocl::uml::MessageExp_strategy = st.builds(
    ocl::uml::MessageExp,
)
ocl::uml::OCLExpression_strategy = st.builds(
    ocl::uml::OCLExpression,
)
ocl::uml::CallExp_strategy = st.builds(
    ocl::uml::CallExp,
)
ocl::uml::FeatureCallExp_strategy = st.builds(
    ocl::uml::FeatureCallExp,
)
ocl::uml::NavigationCallExp_strategy = st.builds(
    ocl::uml::NavigationCallExp,
)
ocl::uml::AssociationClassCallExp_strategy = st.builds(
    ocl::uml::AssociationClassCallExp,
)
ocl::uml::UnlimitedNaturalLiteralExp_strategy = st.builds(
    ocl::uml::UnlimitedNaturalLiteralExp,
)
ocl::uml::NumericLiteralExp_strategy = st.builds(
    ocl::uml::NumericLiteralExp,
)
ocl::uml::IntegerLiteralExp_strategy = st.builds(
    ocl::uml::IntegerLiteralExp,
)
ocl::uml::IfExp_strategy = st.builds(
    ocl::uml::IfExp,
)
ocl::uml::EnumLiteralExp_strategy = st.builds(
    ocl::uml::EnumLiteralExp,
)
ocl::uml::CollectionRange_strategy = st.builds(
    ocl::uml::CollectionRange,
)
ocl::uml::CollectionLiteralExp_strategy = st.builds(
    ocl::uml::CollectionLiteralExp,
)
ocl::uml::CollectionLiteralPart_strategy = st.builds(
    ocl::uml::CollectionLiteralPart,
)
ocl::uml::CollectionItem_strategy = st.builds(
    ocl::uml::CollectionItem,
)
ocl::uml::LiteralExp_strategy = st.builds(
    ocl::uml::LiteralExp,
)
ocl::uml::PrimitiveLiteralExp_strategy = st.builds(
    ocl::uml::PrimitiveLiteralExp,
)
ocl::uml::BooleanLiteralExp_strategy = st.builds(
    ocl::uml::BooleanLiteralExp,
)
ocl::uml::TypeType_strategy = st.builds(
    ocl::uml::TypeType,
)
types::ElementType_strategy = st.builds(
    types::ElementType,
)
Classifier_strategy = st.builds(
    Classifier,
)
ocl::uml::ElementType_strategy = st.builds(
    ocl::uml::ElementType,
)
ocl::uml::ExpressionInOCL_strategy = st.builds(
    ocl::uml::ExpressionInOCL,
)
ocl::uml::SequenceType_strategy = st.builds(
    ocl::uml::SequenceType,
)
ocl::uml::OrderedSetType_strategy = st.builds(
    ocl::uml::OrderedSetType,
)
ocl::uml::SetType_strategy = st.builds(
    ocl::uml::SetType,
)
ocl::uml::BagType_strategy = st.builds(
    ocl::uml::BagType,
)
ocl::uml::TupleType_strategy = st.builds(
    ocl::uml::TupleType,
)
ocl::uml::CollectionType_strategy = st.builds(
    ocl::uml::CollectionType,
)
ocl::uml::PrimitiveType_strategy = st.builds(
    ocl::uml::PrimitiveType,
)
uml::ocl::Property_strategy = st.builds(
    uml::ocl::Property,
)
ocl::uml::MessageType_strategy = st.builds(
    ocl::uml::MessageType,
)
ocl::uml::InvalidType_strategy = st.builds(
    ocl::uml::InvalidType,
)
ocl::uml::VoidType_strategy = st.builds(
    ocl::uml::VoidType,
)
uml::ocl::Operation_strategy = st.builds(
    uml::ocl::Operation,
)
ocl::uml::AnyType_strategy = st.builds(
    ocl::uml::AnyType,
)

@given(instance=ocl::uml::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_ocl::uml::templateparametertype_instantiation(instance):
    assert isinstance(instance, ocl::uml::TemplateParameterType)

@given(instance=ocl::uml::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::variableexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::VariableExp)

@given(instance=ocl::uml::Variable_strategy)
@settings(max_examples=50)
def test_ocl::uml::variable_instantiation(instance):
    assert isinstance(instance, ocl::uml::Variable)

@given(instance=ocl::uml::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::letexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::LetExp)

@given(instance=ocl::uml::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::IteratorExp)

@given(instance=ocl::uml::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::loopexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::LoopExp)

@given(instance=ocl::uml::IterateExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::iterateexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::IterateExp)

@given(instance=ocl::uml::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::InvalidLiteralExp)

@given(instance=ocl::uml::UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::UnspecifiedValueExp)

@given(instance=ocl::uml::TypeExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::typeexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::TypeExp)

@given(instance=ocl::uml::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::uml::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::uml::TupleLiteralPart)

@given(instance=ocl::uml::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::TupleLiteralExp)

@given(instance=ocl::uml::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::StringLiteralExp)

@given(instance=ocl::uml::StateExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::stateexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::StateExp)

@given(instance=ocl::uml::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::RealLiteralExp)

@given(instance=ocl::uml::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::PropertyCallExp)

@given(instance=ocl::uml::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::OperationCallExp)

@given(instance=ocl::uml::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::NullLiteralExp)

@given(instance=ocl::uml::MessageExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::messageexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::MessageExp)

@given(instance=ocl::uml::OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl::uml::oclexpression_instantiation(instance):
    assert isinstance(instance, ocl::uml::OCLExpression)

@given(instance=ocl::uml::CallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::callexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::CallExp)

@given(instance=ocl::uml::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::FeatureCallExp)

@given(instance=ocl::uml::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::NavigationCallExp)

@given(instance=ocl::uml::AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::AssociationClassCallExp)

@given(instance=ocl::uml::UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::UnlimitedNaturalLiteralExp)

@given(instance=ocl::uml::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::NumericLiteralExp)

@given(instance=ocl::uml::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::IntegerLiteralExp)

@given(instance=ocl::uml::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::ifexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::IfExp)

@given(instance=ocl::uml::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::EnumLiteralExp)

@given(instance=ocl::uml::CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl::uml::collectionrange_instantiation(instance):
    assert isinstance(instance, ocl::uml::CollectionRange)

@given(instance=ocl::uml::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::CollectionLiteralExp)

@given(instance=ocl::uml::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::uml::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::uml::CollectionLiteralPart)

@given(instance=ocl::uml::CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl::uml::collectionitem_instantiation(instance):
    assert isinstance(instance, ocl::uml::CollectionItem)

@given(instance=ocl::uml::LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::literalexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::LiteralExp)

@given(instance=ocl::uml::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::PrimitiveLiteralExp)

@given(instance=ocl::uml::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::uml::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::uml::BooleanLiteralExp)

@given(instance=ocl::uml::TypeType_strategy)
@settings(max_examples=50)
def test_ocl::uml::typetype_instantiation(instance):
    assert isinstance(instance, ocl::uml::TypeType)

@given(instance=types::ElementType_strategy)
@settings(max_examples=50)
def test_types::elementtype_instantiation(instance):
    assert isinstance(instance, types::ElementType)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=ocl::uml::ElementType_strategy)
@settings(max_examples=50)
def test_ocl::uml::elementtype_instantiation(instance):
    assert isinstance(instance, ocl::uml::ElementType)

@given(instance=ocl::uml::ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_ocl::uml::expressioninocl_instantiation(instance):
    assert isinstance(instance, ocl::uml::ExpressionInOCL)

@given(instance=ocl::uml::SequenceType_strategy)
@settings(max_examples=50)
def test_ocl::uml::sequencetype_instantiation(instance):
    assert isinstance(instance, ocl::uml::SequenceType)

@given(instance=ocl::uml::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::uml::orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl::uml::OrderedSetType)

@given(instance=ocl::uml::SetType_strategy)
@settings(max_examples=50)
def test_ocl::uml::settype_instantiation(instance):
    assert isinstance(instance, ocl::uml::SetType)

@given(instance=ocl::uml::BagType_strategy)
@settings(max_examples=50)
def test_ocl::uml::bagtype_instantiation(instance):
    assert isinstance(instance, ocl::uml::BagType)

@given(instance=ocl::uml::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::uml::tupletype_instantiation(instance):
    assert isinstance(instance, ocl::uml::TupleType)

@given(instance=ocl::uml::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::uml::collectiontype_instantiation(instance):
    assert isinstance(instance, ocl::uml::CollectionType)

@given(instance=ocl::uml::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::uml::primitivetype_instantiation(instance):
    assert isinstance(instance, ocl::uml::PrimitiveType)

@given(instance=uml::ocl::Property_strategy)
@settings(max_examples=50)
def test_uml::ocl::property_instantiation(instance):
    assert isinstance(instance, uml::ocl::Property)

@given(instance=ocl::uml::MessageType_strategy)
@settings(max_examples=50)
def test_ocl::uml::messagetype_instantiation(instance):
    assert isinstance(instance, ocl::uml::MessageType)

@given(instance=ocl::uml::InvalidType_strategy)
@settings(max_examples=50)
def test_ocl::uml::invalidtype_instantiation(instance):
    assert isinstance(instance, ocl::uml::InvalidType)

@given(instance=ocl::uml::VoidType_strategy)
@settings(max_examples=50)
def test_ocl::uml::voidtype_instantiation(instance):
    assert isinstance(instance, ocl::uml::VoidType)

@given(instance=uml::ocl::Operation_strategy)
@settings(max_examples=50)
def test_uml::ocl::operation_instantiation(instance):
    assert isinstance(instance, uml::ocl::Operation)

@given(instance=ocl::uml::AnyType_strategy)
@settings(max_examples=50)
def test_ocl::uml::anytype_instantiation(instance):
    assert isinstance(instance, ocl::uml::AnyType)
