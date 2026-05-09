import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocl::ecore::VariableExp,
    ocl::ecore::Variable,
    ocl::ecore::UnspecifiedValueExp,
    ocl::ecore::TypeExp,
    ocl::ecore::TupleLiteralPart,
    ocl::ecore::TupleLiteralExp,
    ocl::ecore::StringLiteralExp,
    ocl::ecore::StateExp,
    ocl::ecore::RealLiteralExp,
    ocl::ecore::PropertyCallExp,
    ocl::ecore::LoopExp,
    ocl::ecore::LiteralExp,
    ocl::ecore::LetExp,
    ocl::ecore::IteratorExp,
    ocl::ecore::IterateExp,
    ocl::ecore::InvalidLiteralExp,
    ocl::ecore::UnlimitedNaturalLiteralExp,
    ocl::ecore::IntegerLiteralExp,
    ocl::ecore::IfExp,
    ocl::ecore::FeatureCallExp,
    ocl::ecore::EnumLiteralExp,
    ocl::ecore::PrimitiveLiteralExp,
    ocl::ecore::OperationCallExp,
    ocl::ecore::OCLExpression,
    ocl::ecore::NumericLiteralExp,
    ocl::ecore::NullLiteralExp,
    ocl::ecore::NavigationCallExp,
    ocl::ecore::MessageExp,
    ecore::ocl::EClass,
    ocl::ecore::SendSignalAction,
    ecore::ocl::EModelElement,
    ENamedElement,
    ocl::ecore::Constraint,
    ecore::ocl::EOperation,
    ocl::ecore::CallOperationAction,
    ocl::ecore::VoidType,
    ocl::ecore::TypeType,
    ocl::ecore::CollectionRange,
    ocl::ecore::CollectionLiteralPart,
    ocl::ecore::CollectionLiteralExp,
    ocl::ecore::CollectionItem,
    ocl::ecore::CallExp,
    ocl::ecore::BooleanLiteralExp,
    ocl::ecore::AssociationClassCallExp,
    ocl::ecore::ExpressionInOCL,
    ocl::ecore::MessageType,
    ocl::ecore::InvalidType,
    types::ElementType,
    EClass,
    ocl::ecore::ElementType,
    ocl::ecore::CollectionType,
    ocl::ecore::BagType,
    ocl::ecore::AnyType,
    ocl::ecore::TupleType,
    ocl::ecore::TemplateParameterType,
    ocl::ecore::SetType,
    ocl::ecore::SequenceType,
    ocl::ecore::PrimitiveType,
    ocl::ecore::OrderedSetType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl::ecore::variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::VariableExp)


def test_ocl::ecore::variableexp_constructor_exists():
    assert callable(ocl::ecore::VariableExp.__init__)


def test_ocl::ecore::variableexp_constructor_args():
    sig = inspect.signature(ocl::ecore::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::variable_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::Variable)


def test_ocl::ecore::variable_constructor_exists():
    assert callable(ocl::ecore::Variable.__init__)


def test_ocl::ecore::variable_constructor_args():
    sig = inspect.signature(ocl::ecore::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::UnspecifiedValueExp)


def test_ocl::ecore::unspecifiedvalueexp_constructor_exists():
    assert callable(ocl::ecore::UnspecifiedValueExp.__init__)


def test_ocl::ecore::unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl::ecore::UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TypeExp)


def test_ocl::ecore::typeexp_constructor_exists():
    assert callable(ocl::ecore::TypeExp.__init__)


def test_ocl::ecore::typeexp_constructor_args():
    sig = inspect.signature(ocl::ecore::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TupleLiteralPart)


def test_ocl::ecore::tupleliteralpart_constructor_exists():
    assert callable(ocl::ecore::TupleLiteralPart.__init__)


def test_ocl::ecore::tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl::ecore::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TupleLiteralExp)


def test_ocl::ecore::tupleliteralexp_constructor_exists():
    assert callable(ocl::ecore::TupleLiteralExp.__init__)


def test_ocl::ecore::tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::StringLiteralExp)


def test_ocl::ecore::stringliteralexp_constructor_exists():
    assert callable(ocl::ecore::StringLiteralExp.__init__)


def test_ocl::ecore::stringliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::StateExp)


def test_ocl::ecore::stateexp_constructor_exists():
    assert callable(ocl::ecore::StateExp.__init__)


def test_ocl::ecore::stateexp_constructor_args():
    sig = inspect.signature(ocl::ecore::StateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::RealLiteralExp)


def test_ocl::ecore::realliteralexp_constructor_exists():
    assert callable(ocl::ecore::RealLiteralExp.__init__)


def test_ocl::ecore::realliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::PropertyCallExp)


def test_ocl::ecore::propertycallexp_constructor_exists():
    assert callable(ocl::ecore::PropertyCallExp.__init__)


def test_ocl::ecore::propertycallexp_constructor_args():
    sig = inspect.signature(ocl::ecore::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::LoopExp)


def test_ocl::ecore::loopexp_constructor_exists():
    assert callable(ocl::ecore::LoopExp.__init__)


def test_ocl::ecore::loopexp_constructor_args():
    sig = inspect.signature(ocl::ecore::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::LiteralExp)


def test_ocl::ecore::literalexp_constructor_exists():
    assert callable(ocl::ecore::LiteralExp.__init__)


def test_ocl::ecore::literalexp_constructor_args():
    sig = inspect.signature(ocl::ecore::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::letexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::LetExp)


def test_ocl::ecore::letexp_constructor_exists():
    assert callable(ocl::ecore::LetExp.__init__)


def test_ocl::ecore::letexp_constructor_args():
    sig = inspect.signature(ocl::ecore::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::IteratorExp)


def test_ocl::ecore::iteratorexp_constructor_exists():
    assert callable(ocl::ecore::IteratorExp.__init__)


def test_ocl::ecore::iteratorexp_constructor_args():
    sig = inspect.signature(ocl::ecore::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::IterateExp)


def test_ocl::ecore::iterateexp_constructor_exists():
    assert callable(ocl::ecore::IterateExp.__init__)


def test_ocl::ecore::iterateexp_constructor_args():
    sig = inspect.signature(ocl::ecore::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::InvalidLiteralExp)


def test_ocl::ecore::invalidliteralexp_constructor_exists():
    assert callable(ocl::ecore::InvalidLiteralExp.__init__)


def test_ocl::ecore::invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::unlimitednaturalliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::UnlimitedNaturalLiteralExp)


def test_ocl::ecore::unlimitednaturalliteralexp_constructor_exists():
    assert callable(ocl::ecore::UnlimitedNaturalLiteralExp.__init__)


def test_ocl::ecore::unlimitednaturalliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::UnlimitedNaturalLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::IntegerLiteralExp)


def test_ocl::ecore::integerliteralexp_constructor_exists():
    assert callable(ocl::ecore::IntegerLiteralExp.__init__)


def test_ocl::ecore::integerliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::IfExp)


def test_ocl::ecore::ifexp_constructor_exists():
    assert callable(ocl::ecore::IfExp.__init__)


def test_ocl::ecore::ifexp_constructor_args():
    sig = inspect.signature(ocl::ecore::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::FeatureCallExp)


def test_ocl::ecore::featurecallexp_constructor_exists():
    assert callable(ocl::ecore::FeatureCallExp.__init__)


def test_ocl::ecore::featurecallexp_constructor_args():
    sig = inspect.signature(ocl::ecore::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::EnumLiteralExp)


def test_ocl::ecore::enumliteralexp_constructor_exists():
    assert callable(ocl::ecore::EnumLiteralExp.__init__)


def test_ocl::ecore::enumliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::PrimitiveLiteralExp)


def test_ocl::ecore::primitiveliteralexp_constructor_exists():
    assert callable(ocl::ecore::PrimitiveLiteralExp.__init__)


def test_ocl::ecore::primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::OperationCallExp)


def test_ocl::ecore::operationcallexp_constructor_exists():
    assert callable(ocl::ecore::OperationCallExp.__init__)


def test_ocl::ecore::operationcallexp_constructor_args():
    sig = inspect.signature(ocl::ecore::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::OCLExpression)


def test_ocl::ecore::oclexpression_constructor_exists():
    assert callable(ocl::ecore::OCLExpression.__init__)


def test_ocl::ecore::oclexpression_constructor_args():
    sig = inspect.signature(ocl::ecore::OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::NumericLiteralExp)


def test_ocl::ecore::numericliteralexp_constructor_exists():
    assert callable(ocl::ecore::NumericLiteralExp.__init__)


def test_ocl::ecore::numericliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::NullLiteralExp)


def test_ocl::ecore::nullliteralexp_constructor_exists():
    assert callable(ocl::ecore::NullLiteralExp.__init__)


def test_ocl::ecore::nullliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::NavigationCallExp)


def test_ocl::ecore::navigationcallexp_constructor_exists():
    assert callable(ocl::ecore::NavigationCallExp.__init__)


def test_ocl::ecore::navigationcallexp_constructor_args():
    sig = inspect.signature(ocl::ecore::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::MessageExp)


def test_ocl::ecore::messageexp_constructor_exists():
    assert callable(ocl::ecore::MessageExp.__init__)


def test_ocl::ecore::messageexp_constructor_args():
    sig = inspect.signature(ocl::ecore::MessageExp.__init__)
    params = list(sig.parameters.keys())



def test_ecore::ocl::eclass_is_not_abstract():
    assert not inspect.isabstract(ecore::ocl::EClass)


def test_ecore::ocl::eclass_constructor_exists():
    assert callable(ecore::ocl::EClass.__init__)


def test_ecore::ocl::eclass_constructor_args():
    sig = inspect.signature(ecore::ocl::EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::SendSignalAction)


def test_ocl::ecore::sendsignalaction_constructor_exists():
    assert callable(ocl::ecore::SendSignalAction.__init__)


def test_ocl::ecore::sendsignalaction_constructor_args():
    sig = inspect.signature(ocl::ecore::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_ecore::ocl::emodelelement_is_not_abstract():
    assert not inspect.isabstract(ecore::ocl::EModelElement)


def test_ecore::ocl::emodelelement_constructor_exists():
    assert callable(ecore::ocl::EModelElement.__init__)


def test_ecore::ocl::emodelelement_constructor_args():
    sig = inspect.signature(ecore::ocl::EModelElement.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::constraint_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::Constraint)


def test_ocl::ecore::constraint_constructor_exists():
    assert callable(ocl::ecore::Constraint.__init__)


def test_ocl::ecore::constraint_constructor_args():
    sig = inspect.signature(ocl::ecore::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"

def test_ocl::ecore::constraint_has_stereotype():
    assert hasattr(ocl::ecore::Constraint, "stereotype")
    descriptor = None
    for klass in ocl::ecore::Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)



def test_ecore::ocl::eoperation_is_not_abstract():
    assert not inspect.isabstract(ecore::ocl::EOperation)


def test_ecore::ocl::eoperation_constructor_exists():
    assert callable(ecore::ocl::EOperation.__init__)


def test_ecore::ocl::eoperation_constructor_args():
    sig = inspect.signature(ecore::ocl::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CallOperationAction)


def test_ocl::ecore::calloperationaction_constructor_exists():
    assert callable(ocl::ecore::CallOperationAction.__init__)


def test_ocl::ecore::calloperationaction_constructor_args():
    sig = inspect.signature(ocl::ecore::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::VoidType)


def test_ocl::ecore::voidtype_constructor_exists():
    assert callable(ocl::ecore::VoidType.__init__)


def test_ocl::ecore::voidtype_constructor_args():
    sig = inspect.signature(ocl::ecore::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::typetype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TypeType)


def test_ocl::ecore::typetype_constructor_exists():
    assert callable(ocl::ecore::TypeType.__init__)


def test_ocl::ecore::typetype_constructor_args():
    sig = inspect.signature(ocl::ecore::TypeType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CollectionRange)


def test_ocl::ecore::collectionrange_constructor_exists():
    assert callable(ocl::ecore::CollectionRange.__init__)


def test_ocl::ecore::collectionrange_constructor_args():
    sig = inspect.signature(ocl::ecore::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CollectionLiteralPart)


def test_ocl::ecore::collectionliteralpart_constructor_exists():
    assert callable(ocl::ecore::CollectionLiteralPart.__init__)


def test_ocl::ecore::collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl::ecore::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CollectionLiteralExp)


def test_ocl::ecore::collectionliteralexp_constructor_exists():
    assert callable(ocl::ecore::CollectionLiteralExp.__init__)


def test_ocl::ecore::collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CollectionItem)


def test_ocl::ecore::collectionitem_constructor_exists():
    assert callable(ocl::ecore::CollectionItem.__init__)


def test_ocl::ecore::collectionitem_constructor_args():
    sig = inspect.signature(ocl::ecore::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::callexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CallExp)


def test_ocl::ecore::callexp_constructor_exists():
    assert callable(ocl::ecore::CallExp.__init__)


def test_ocl::ecore::callexp_constructor_args():
    sig = inspect.signature(ocl::ecore::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::BooleanLiteralExp)


def test_ocl::ecore::booleanliteralexp_constructor_exists():
    assert callable(ocl::ecore::BooleanLiteralExp.__init__)


def test_ocl::ecore::booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl::ecore::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::AssociationClassCallExp)


def test_ocl::ecore::associationclasscallexp_constructor_exists():
    assert callable(ocl::ecore::AssociationClassCallExp.__init__)


def test_ocl::ecore::associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl::ecore::AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::expressioninocl_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::ExpressionInOCL)


def test_ocl::ecore::expressioninocl_constructor_exists():
    assert callable(ocl::ecore::ExpressionInOCL.__init__)


def test_ocl::ecore::expressioninocl_constructor_args():
    sig = inspect.signature(ocl::ecore::ExpressionInOCL.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::MessageType)


def test_ocl::ecore::messagetype_constructor_exists():
    assert callable(ocl::ecore::MessageType.__init__)


def test_ocl::ecore::messagetype_constructor_args():
    sig = inspect.signature(ocl::ecore::MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::InvalidType)


def test_ocl::ecore::invalidtype_constructor_exists():
    assert callable(ocl::ecore::InvalidType.__init__)


def test_ocl::ecore::invalidtype_constructor_args():
    sig = inspect.signature(ocl::ecore::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_types::elementtype_is_not_abstract():
    assert not inspect.isabstract(types::ElementType)


def test_types::elementtype_constructor_exists():
    assert callable(types::ElementType.__init__)


def test_types::elementtype_constructor_args():
    sig = inspect.signature(types::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::ElementType)


def test_ocl::ecore::elementtype_constructor_exists():
    assert callable(ocl::ecore::ElementType.__init__)


def test_ocl::ecore::elementtype_constructor_args():
    sig = inspect.signature(ocl::ecore::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::CollectionType)


def test_ocl::ecore::collectiontype_constructor_exists():
    assert callable(ocl::ecore::CollectionType.__init__)


def test_ocl::ecore::collectiontype_constructor_args():
    sig = inspect.signature(ocl::ecore::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::BagType)


def test_ocl::ecore::bagtype_constructor_exists():
    assert callable(ocl::ecore::BagType.__init__)


def test_ocl::ecore::bagtype_constructor_args():
    sig = inspect.signature(ocl::ecore::BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::anytype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::AnyType)


def test_ocl::ecore::anytype_constructor_exists():
    assert callable(ocl::ecore::AnyType.__init__)


def test_ocl::ecore::anytype_constructor_args():
    sig = inspect.signature(ocl::ecore::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TupleType)


def test_ocl::ecore::tupletype_constructor_exists():
    assert callable(ocl::ecore::TupleType.__init__)


def test_ocl::ecore::tupletype_constructor_args():
    sig = inspect.signature(ocl::ecore::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::templateparametertype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::TemplateParameterType)


def test_ocl::ecore::templateparametertype_constructor_exists():
    assert callable(ocl::ecore::TemplateParameterType.__init__)


def test_ocl::ecore::templateparametertype_constructor_args():
    sig = inspect.signature(ocl::ecore::TemplateParameterType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::settype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::SetType)


def test_ocl::ecore::settype_constructor_exists():
    assert callable(ocl::ecore::SetType.__init__)


def test_ocl::ecore::settype_constructor_args():
    sig = inspect.signature(ocl::ecore::SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::SequenceType)


def test_ocl::ecore::sequencetype_constructor_exists():
    assert callable(ocl::ecore::SequenceType.__init__)


def test_ocl::ecore::sequencetype_constructor_args():
    sig = inspect.signature(ocl::ecore::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::PrimitiveType)


def test_ocl::ecore::primitivetype_constructor_exists():
    assert callable(ocl::ecore::PrimitiveType.__init__)


def test_ocl::ecore::primitivetype_constructor_args():
    sig = inspect.signature(ocl::ecore::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::ecore::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl::ecore::OrderedSetType)


def test_ocl::ecore::orderedsettype_constructor_exists():
    assert callable(ocl::ecore::OrderedSetType.__init__)


def test_ocl::ecore::orderedsettype_constructor_args():
    sig = inspect.signature(ocl::ecore::OrderedSetType.__init__)
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
ocl::ecore::VariableExp_strategy = st.builds(
    ocl::ecore::VariableExp,
)
ocl::ecore::Variable_strategy = st.builds(
    ocl::ecore::Variable,
)
ocl::ecore::UnspecifiedValueExp_strategy = st.builds(
    ocl::ecore::UnspecifiedValueExp,
)
ocl::ecore::TypeExp_strategy = st.builds(
    ocl::ecore::TypeExp,
)
ocl::ecore::TupleLiteralPart_strategy = st.builds(
    ocl::ecore::TupleLiteralPart,
)
ocl::ecore::TupleLiteralExp_strategy = st.builds(
    ocl::ecore::TupleLiteralExp,
)
ocl::ecore::StringLiteralExp_strategy = st.builds(
    ocl::ecore::StringLiteralExp,
)
ocl::ecore::StateExp_strategy = st.builds(
    ocl::ecore::StateExp,
)
ocl::ecore::RealLiteralExp_strategy = st.builds(
    ocl::ecore::RealLiteralExp,
)
ocl::ecore::PropertyCallExp_strategy = st.builds(
    ocl::ecore::PropertyCallExp,
)
ocl::ecore::LoopExp_strategy = st.builds(
    ocl::ecore::LoopExp,
)
ocl::ecore::LiteralExp_strategy = st.builds(
    ocl::ecore::LiteralExp,
)
ocl::ecore::LetExp_strategy = st.builds(
    ocl::ecore::LetExp,
)
ocl::ecore::IteratorExp_strategy = st.builds(
    ocl::ecore::IteratorExp,
)
ocl::ecore::IterateExp_strategy = st.builds(
    ocl::ecore::IterateExp,
)
ocl::ecore::InvalidLiteralExp_strategy = st.builds(
    ocl::ecore::InvalidLiteralExp,
)
ocl::ecore::UnlimitedNaturalLiteralExp_strategy = st.builds(
    ocl::ecore::UnlimitedNaturalLiteralExp,
)
ocl::ecore::IntegerLiteralExp_strategy = st.builds(
    ocl::ecore::IntegerLiteralExp,
)
ocl::ecore::IfExp_strategy = st.builds(
    ocl::ecore::IfExp,
)
ocl::ecore::FeatureCallExp_strategy = st.builds(
    ocl::ecore::FeatureCallExp,
)
ocl::ecore::EnumLiteralExp_strategy = st.builds(
    ocl::ecore::EnumLiteralExp,
)
ocl::ecore::PrimitiveLiteralExp_strategy = st.builds(
    ocl::ecore::PrimitiveLiteralExp,
)
ocl::ecore::OperationCallExp_strategy = st.builds(
    ocl::ecore::OperationCallExp,
)
ocl::ecore::OCLExpression_strategy = st.builds(
    ocl::ecore::OCLExpression,
)
ocl::ecore::NumericLiteralExp_strategy = st.builds(
    ocl::ecore::NumericLiteralExp,
)
ocl::ecore::NullLiteralExp_strategy = st.builds(
    ocl::ecore::NullLiteralExp,
)
ocl::ecore::NavigationCallExp_strategy = st.builds(
    ocl::ecore::NavigationCallExp,
)
ocl::ecore::MessageExp_strategy = st.builds(
    ocl::ecore::MessageExp,
)
ecore::ocl::EClass_strategy = st.builds(
    ecore::ocl::EClass,
)
ocl::ecore::SendSignalAction_strategy = st.builds(
    ocl::ecore::SendSignalAction,
)
ecore::ocl::EModelElement_strategy = st.builds(
    ecore::ocl::EModelElement,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ocl::ecore::Constraint_strategy = st.builds(
    ocl::ecore::Constraint,
    stereotype=
        safe_text
)
ecore::ocl::EOperation_strategy = st.builds(
    ecore::ocl::EOperation,
)
ocl::ecore::CallOperationAction_strategy = st.builds(
    ocl::ecore::CallOperationAction,
)
ocl::ecore::VoidType_strategy = st.builds(
    ocl::ecore::VoidType,
)
ocl::ecore::TypeType_strategy = st.builds(
    ocl::ecore::TypeType,
)
ocl::ecore::CollectionRange_strategy = st.builds(
    ocl::ecore::CollectionRange,
)
ocl::ecore::CollectionLiteralPart_strategy = st.builds(
    ocl::ecore::CollectionLiteralPart,
)
ocl::ecore::CollectionLiteralExp_strategy = st.builds(
    ocl::ecore::CollectionLiteralExp,
)
ocl::ecore::CollectionItem_strategy = st.builds(
    ocl::ecore::CollectionItem,
)
ocl::ecore::CallExp_strategy = st.builds(
    ocl::ecore::CallExp,
)
ocl::ecore::BooleanLiteralExp_strategy = st.builds(
    ocl::ecore::BooleanLiteralExp,
)
ocl::ecore::AssociationClassCallExp_strategy = st.builds(
    ocl::ecore::AssociationClassCallExp,
)
ocl::ecore::ExpressionInOCL_strategy = st.builds(
    ocl::ecore::ExpressionInOCL,
)
ocl::ecore::MessageType_strategy = st.builds(
    ocl::ecore::MessageType,
)
ocl::ecore::InvalidType_strategy = st.builds(
    ocl::ecore::InvalidType,
)
types::ElementType_strategy = st.builds(
    types::ElementType,
)
EClass_strategy = st.builds(
    EClass,
)
ocl::ecore::ElementType_strategy = st.builds(
    ocl::ecore::ElementType,
)
ocl::ecore::CollectionType_strategy = st.builds(
    ocl::ecore::CollectionType,
)
ocl::ecore::BagType_strategy = st.builds(
    ocl::ecore::BagType,
)
ocl::ecore::AnyType_strategy = st.builds(
    ocl::ecore::AnyType,
)
ocl::ecore::TupleType_strategy = st.builds(
    ocl::ecore::TupleType,
)
ocl::ecore::TemplateParameterType_strategy = st.builds(
    ocl::ecore::TemplateParameterType,
)
ocl::ecore::SetType_strategy = st.builds(
    ocl::ecore::SetType,
)
ocl::ecore::SequenceType_strategy = st.builds(
    ocl::ecore::SequenceType,
)
ocl::ecore::PrimitiveType_strategy = st.builds(
    ocl::ecore::PrimitiveType,
)
ocl::ecore::OrderedSetType_strategy = st.builds(
    ocl::ecore::OrderedSetType,
)

@given(instance=ocl::ecore::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::variableexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::VariableExp)

@given(instance=ocl::ecore::Variable_strategy)
@settings(max_examples=50)
def test_ocl::ecore::variable_instantiation(instance):
    assert isinstance(instance, ocl::ecore::Variable)

@given(instance=ocl::ecore::UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::UnspecifiedValueExp)

@given(instance=ocl::ecore::TypeExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::typeexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TypeExp)

@given(instance=ocl::ecore::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::ecore::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TupleLiteralPart)

@given(instance=ocl::ecore::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TupleLiteralExp)

@given(instance=ocl::ecore::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::StringLiteralExp)

@given(instance=ocl::ecore::StateExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::stateexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::StateExp)

@given(instance=ocl::ecore::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::RealLiteralExp)

@given(instance=ocl::ecore::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::PropertyCallExp)

@given(instance=ocl::ecore::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::loopexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::LoopExp)

@given(instance=ocl::ecore::LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::literalexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::LiteralExp)

@given(instance=ocl::ecore::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::letexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::LetExp)

@given(instance=ocl::ecore::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::IteratorExp)

@given(instance=ocl::ecore::IterateExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::iterateexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::IterateExp)

@given(instance=ocl::ecore::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::InvalidLiteralExp)

@given(instance=ocl::ecore::UnlimitedNaturalLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::unlimitednaturalliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::UnlimitedNaturalLiteralExp)

@given(instance=ocl::ecore::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::IntegerLiteralExp)

@given(instance=ocl::ecore::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::ifexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::IfExp)

@given(instance=ocl::ecore::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::FeatureCallExp)

@given(instance=ocl::ecore::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::EnumLiteralExp)

@given(instance=ocl::ecore::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::PrimitiveLiteralExp)

@given(instance=ocl::ecore::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::OperationCallExp)

@given(instance=ocl::ecore::OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl::ecore::oclexpression_instantiation(instance):
    assert isinstance(instance, ocl::ecore::OCLExpression)

@given(instance=ocl::ecore::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::NumericLiteralExp)

@given(instance=ocl::ecore::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::NullLiteralExp)

@given(instance=ocl::ecore::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::NavigationCallExp)

@given(instance=ocl::ecore::MessageExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::messageexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::MessageExp)

@given(instance=ecore::ocl::EClass_strategy)
@settings(max_examples=50)
def test_ecore::ocl::eclass_instantiation(instance):
    assert isinstance(instance, ecore::ocl::EClass)

@given(instance=ocl::ecore::SendSignalAction_strategy)
@settings(max_examples=50)
def test_ocl::ecore::sendsignalaction_instantiation(instance):
    assert isinstance(instance, ocl::ecore::SendSignalAction)

@given(instance=ecore::ocl::EModelElement_strategy)
@settings(max_examples=50)
def test_ecore::ocl::emodelelement_instantiation(instance):
    assert isinstance(instance, ecore::ocl::EModelElement)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ocl::ecore::Constraint_strategy)
@settings(max_examples=50)
def test_ocl::ecore::constraint_instantiation(instance):
    assert isinstance(instance, ocl::ecore::Constraint)

@given(instance=ocl::ecore::Constraint_strategy)
def test_ocl::ecore::constraint_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=ocl::ecore::Constraint_strategy)
def test_ocl::ecore::constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=ecore::ocl::EOperation_strategy)
@settings(max_examples=50)
def test_ecore::ocl::eoperation_instantiation(instance):
    assert isinstance(instance, ecore::ocl::EOperation)

@given(instance=ocl::ecore::CallOperationAction_strategy)
@settings(max_examples=50)
def test_ocl::ecore::calloperationaction_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CallOperationAction)

@given(instance=ocl::ecore::VoidType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::voidtype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::VoidType)

@given(instance=ocl::ecore::TypeType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::typetype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TypeType)

@given(instance=ocl::ecore::CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl::ecore::collectionrange_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CollectionRange)

@given(instance=ocl::ecore::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::ecore::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CollectionLiteralPart)

@given(instance=ocl::ecore::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CollectionLiteralExp)

@given(instance=ocl::ecore::CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl::ecore::collectionitem_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CollectionItem)

@given(instance=ocl::ecore::CallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::callexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CallExp)

@given(instance=ocl::ecore::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::BooleanLiteralExp)

@given(instance=ocl::ecore::AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl::ecore::associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl::ecore::AssociationClassCallExp)

@given(instance=ocl::ecore::ExpressionInOCL_strategy)
@settings(max_examples=50)
def test_ocl::ecore::expressioninocl_instantiation(instance):
    assert isinstance(instance, ocl::ecore::ExpressionInOCL)

@given(instance=ocl::ecore::MessageType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::messagetype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::MessageType)

@given(instance=ocl::ecore::InvalidType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::invalidtype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::InvalidType)

@given(instance=types::ElementType_strategy)
@settings(max_examples=50)
def test_types::elementtype_instantiation(instance):
    assert isinstance(instance, types::ElementType)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ocl::ecore::ElementType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::elementtype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::ElementType)

@given(instance=ocl::ecore::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::collectiontype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::CollectionType)

@given(instance=ocl::ecore::BagType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::bagtype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::BagType)

@given(instance=ocl::ecore::AnyType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::anytype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::AnyType)

@given(instance=ocl::ecore::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::tupletype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TupleType)

@given(instance=ocl::ecore::TemplateParameterType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::templateparametertype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::TemplateParameterType)

@given(instance=ocl::ecore::SetType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::settype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::SetType)

@given(instance=ocl::ecore::SequenceType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::sequencetype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::SequenceType)

@given(instance=ocl::ecore::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::primitivetype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::PrimitiveType)

@given(instance=ocl::ecore::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::ecore::orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl::ecore::OrderedSetType)
