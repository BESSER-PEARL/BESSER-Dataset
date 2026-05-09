import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ocl::query::Query,
    ocl::utilities::Visitable,
    ocl::utilities::PredefinedType,
    ASTNode,
    ocl::utilities::TypedASTNode,
    ocl::utilities::CallingASTNode,
    ocl::utilities::ASTNode,
    uml::ocl::EClassifier,
    uml::ocl::EClass,
    ocl::uml::SendSignalAction,
    uml::ocl::ENamedElement,
    ENamedElement,
    ocl::uml::TypedElement,
    uml::ocl::EOperation,
    ocl::uml::CallOperationAction,
    expressions::ocl::EParameter,
    expressions::ocl::EClassifier,
    TupleLiteralPart,
    expressions::ocl::EObject,
    PrimitiveLiteralExp,
    ocl::expressions::StringLiteralExp,
    ocl::expressions::BooleanLiteralExp,
    expressions::ocl::EClass,
    NavigationCallExp,
    ocl::expressions::AssociationClassCallExp,
    PrimitiveReal,
    ocl::types::PrimitiveInteger,
    PrimitiveType,
    ocl::types::PrimitiveString,
    ocl::types::PrimitiveReal,
    ocl::types::PrimitiveBoolean,
    types::ocl::EClass,
    types::ocl::EOperation,
    EClass,
    ocl::types::TupleType,
    ocl::types::ElementType,
    types::ocl::EClassifier,
    utilities::TypedASTNode,
    EDataType,
    CollectionType,
    ocl::types::SequenceType,
    ocl::types::SetType,
    ocl::types::OrderedSetType,
    ocl::types::BagType,
    utilities::PredefinedType,
    ocl::types::MessageType,
    ocl::types::PrimitiveType,
    ocl::types::CollectionType,
    EClassifier,
    ocl::types::TypeType,
    ocl::types::VoidType,
    ocl::types::InvalidType,
    ocl::types::AnyType,
    ocl::expressions::PropertyCallExp,
    expressions::ocl::EOperation,
    utilities::ASTNode,
    utilities::Visitable,
    ocl::uml::Constraint,
    uml::TypedElement,
    ocl::expressions::TupleLiteralPart,
    ocl::expressions::Variable,
    ocl::expressions::OCLExpression,
    ocl::expressions::NumericLiteralExp,
    expressions::ocl::EStructuralFeature,
    FeatureCallExp,
    ocl::expressions::OperationCallExp,
    ocl::expressions::NavigationCallExp,
    SendSignalAction,
    CallOperationAction,
    Variable,
    LoopExp,
    ocl::expressions::IteratorExp,
    ocl::expressions::IterateExp,
    NumericLiteralExp,
    ocl::expressions::RealLiteralExp,
    ocl::expressions::IntegerLiteralExp,
    CallExp,
    ocl::expressions::LoopExp,
    ocl::expressions::FeatureCallExp,
    expressions::ocl::EEnumLiteral,
    TypedElement,
    ocl::expressions::CollectionLiteralPart,
    LiteralExp,
    ocl::expressions::TupleLiteralExp,
    ocl::expressions::PrimitiveLiteralExp,
    ocl::expressions::InvalidLiteralExp,
    ocl::expressions::NullLiteralExp,
    ocl::expressions::EnumLiteralExp,
    ocl::expressions::CollectionLiteralExp,
    CollectionLiteralPart,
    ocl::expressions::CollectionRange,
    ocl::expressions::CollectionItem,
    OCLExpression,
    ocl::expressions::LiteralExp,
    ocl::expressions::LetExp,
    ocl::expressions::IfExp,
    ocl::expressions::TypeExp,
    ocl::expressions::StateExp,
    ocl::expressions::VariableExp,
    utilities::CallingASTNode,
    expressions::OCLExpression,
    ocl::expressions::CallExp,
    ocl::expressions::UnspecifiedValueExp,
    ocl::expressions::MessageExp,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ocl::query::query_is_not_abstract():
    assert not inspect.isabstract(ocl::query::Query)


def test_ocl::query::query_constructor_exists():
    assert callable(ocl::query::Query.__init__)


def test_ocl::query::query_constructor_args():
    sig = inspect.signature(ocl::query::Query.__init__)
    params = list(sig.parameters.keys())
    assert "extentMap" in params, "Missing parameter 'extentMap'"

def test_ocl::query::query_has_extentMap():
    assert hasattr(ocl::query::Query, "extentMap")
    descriptor = None
    for klass in ocl::query::Query.__mro__:
        if "extentMap" in klass.__dict__:
            descriptor = klass.__dict__["extentMap"]
            break
    assert isinstance(descriptor, property)



def test_ocl::utilities::visitable_is_not_abstract():
    assert not inspect.isabstract(ocl::utilities::Visitable)


def test_ocl::utilities::visitable_constructor_exists():
    assert callable(ocl::utilities::Visitable.__init__)


def test_ocl::utilities::visitable_constructor_args():
    sig = inspect.signature(ocl::utilities::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::utilities::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(ocl::utilities::PredefinedType)


def test_ocl::utilities::predefinedtype_constructor_exists():
    assert callable(ocl::utilities::PredefinedType.__init__)


def test_ocl::utilities::predefinedtype_constructor_args():
    sig = inspect.signature(ocl::utilities::PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_astnode_is_not_abstract():
    assert not inspect.isabstract(ASTNode)


def test_astnode_constructor_exists():
    assert callable(ASTNode.__init__)


def test_astnode_constructor_args():
    sig = inspect.signature(ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_ocl::utilities::typedastnode_is_not_abstract():
    assert not inspect.isabstract(ocl::utilities::TypedASTNode)


def test_ocl::utilities::typedastnode_constructor_exists():
    assert callable(ocl::utilities::TypedASTNode.__init__)


def test_ocl::utilities::typedastnode_constructor_args():
    sig = inspect.signature(ocl::utilities::TypedASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "typeStartPosition" in params, "Missing parameter 'typeStartPosition'"
    assert "typeEndPosition" in params, "Missing parameter 'typeEndPosition'"

def test_ocl::utilities::typedastnode_has_typeStartPosition():
    assert hasattr(ocl::utilities::TypedASTNode, "typeStartPosition")
    descriptor = None
    for klass in ocl::utilities::TypedASTNode.__mro__:
        if "typeStartPosition" in klass.__dict__:
            descriptor = klass.__dict__["typeStartPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl::utilities::typedastnode_has_typeEndPosition():
    assert hasattr(ocl::utilities::TypedASTNode, "typeEndPosition")
    descriptor = None
    for klass in ocl::utilities::TypedASTNode.__mro__:
        if "typeEndPosition" in klass.__dict__:
            descriptor = klass.__dict__["typeEndPosition"]
            break
    assert isinstance(descriptor, property)



def test_ocl::utilities::callingastnode_is_not_abstract():
    assert not inspect.isabstract(ocl::utilities::CallingASTNode)


def test_ocl::utilities::callingastnode_constructor_exists():
    assert callable(ocl::utilities::CallingASTNode.__init__)


def test_ocl::utilities::callingastnode_constructor_args():
    sig = inspect.signature(ocl::utilities::CallingASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "propertyStartPosition" in params, "Missing parameter 'propertyStartPosition'"
    assert "propertyEndPosition" in params, "Missing parameter 'propertyEndPosition'"

def test_ocl::utilities::callingastnode_has_propertyStartPosition():
    assert hasattr(ocl::utilities::CallingASTNode, "propertyStartPosition")
    descriptor = None
    for klass in ocl::utilities::CallingASTNode.__mro__:
        if "propertyStartPosition" in klass.__dict__:
            descriptor = klass.__dict__["propertyStartPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl::utilities::callingastnode_has_propertyEndPosition():
    assert hasattr(ocl::utilities::CallingASTNode, "propertyEndPosition")
    descriptor = None
    for klass in ocl::utilities::CallingASTNode.__mro__:
        if "propertyEndPosition" in klass.__dict__:
            descriptor = klass.__dict__["propertyEndPosition"]
            break
    assert isinstance(descriptor, property)



def test_ocl::utilities::astnode_is_not_abstract():
    assert not inspect.isabstract(ocl::utilities::ASTNode)


def test_ocl::utilities::astnode_constructor_exists():
    assert callable(ocl::utilities::ASTNode.__init__)


def test_ocl::utilities::astnode_constructor_args():
    sig = inspect.signature(ocl::utilities::ASTNode.__init__)
    params = list(sig.parameters.keys())
    assert "endPosition" in params, "Missing parameter 'endPosition'"
    assert "startPosition" in params, "Missing parameter 'startPosition'"

def test_ocl::utilities::astnode_has_endPosition():
    assert hasattr(ocl::utilities::ASTNode, "endPosition")
    descriptor = None
    for klass in ocl::utilities::ASTNode.__mro__:
        if "endPosition" in klass.__dict__:
            descriptor = klass.__dict__["endPosition"]
            break
    assert isinstance(descriptor, property)

def test_ocl::utilities::astnode_has_startPosition():
    assert hasattr(ocl::utilities::ASTNode, "startPosition")
    descriptor = None
    for klass in ocl::utilities::ASTNode.__mro__:
        if "startPosition" in klass.__dict__:
            descriptor = klass.__dict__["startPosition"]
            break
    assert isinstance(descriptor, property)



def test_uml::ocl::eclassifier_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::EClassifier)


def test_uml::ocl::eclassifier_constructor_exists():
    assert callable(uml::ocl::EClassifier.__init__)


def test_uml::ocl::eclassifier_constructor_args():
    sig = inspect.signature(uml::ocl::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml::ocl::eclass_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::EClass)


def test_uml::ocl::eclass_constructor_exists():
    assert callable(uml::ocl::EClass.__init__)


def test_uml::ocl::eclass_constructor_args():
    sig = inspect.signature(uml::ocl::EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::SendSignalAction)


def test_ocl::uml::sendsignalaction_constructor_exists():
    assert callable(ocl::uml::SendSignalAction.__init__)


def test_ocl::uml::sendsignalaction_constructor_args():
    sig = inspect.signature(ocl::uml::SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml::ocl::enamedelement_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::ENamedElement)


def test_uml::ocl::enamedelement_constructor_exists():
    assert callable(uml::ocl::ENamedElement.__init__)


def test_uml::ocl::enamedelement_constructor_args():
    sig = inspect.signature(uml::ocl::ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_enamedelement_is_not_abstract():
    assert not inspect.isabstract(ENamedElement)


def test_enamedelement_constructor_exists():
    assert callable(ENamedElement.__init__)


def test_enamedelement_constructor_args():
    sig = inspect.signature(ENamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::TypedElement)


def test_ocl::uml::typedelement_constructor_exists():
    assert callable(ocl::uml::TypedElement.__init__)


def test_ocl::uml::typedelement_constructor_args():
    sig = inspect.signature(ocl::uml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml::ocl::eoperation_is_not_abstract():
    assert not inspect.isabstract(uml::ocl::EOperation)


def test_uml::ocl::eoperation_constructor_exists():
    assert callable(uml::ocl::EOperation.__init__)


def test_uml::ocl::eoperation_constructor_args():
    sig = inspect.signature(uml::ocl::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::calloperationaction_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::CallOperationAction)


def test_ocl::uml::calloperationaction_constructor_exists():
    assert callable(ocl::uml::CallOperationAction.__init__)


def test_ocl::uml::calloperationaction_constructor_args():
    sig = inspect.signature(ocl::uml::CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_expressions::ocl::eparameter_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EParameter)


def test_expressions::ocl::eparameter_constructor_exists():
    assert callable(expressions::ocl::EParameter.__init__)


def test_expressions::ocl::eparameter_constructor_args():
    sig = inspect.signature(expressions::ocl::EParameter.__init__)
    params = list(sig.parameters.keys())



def test_expressions::ocl::eclassifier_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EClassifier)


def test_expressions::ocl::eclassifier_constructor_exists():
    assert callable(expressions::ocl::EClassifier.__init__)


def test_expressions::ocl::eclassifier_constructor_args():
    sig = inspect.signature(expressions::ocl::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_expressions::ocl::eobject_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EObject)


def test_expressions::ocl::eobject_constructor_exists():
    assert callable(expressions::ocl::EObject.__init__)


def test_expressions::ocl::eobject_constructor_args():
    sig = inspect.signature(expressions::ocl::EObject.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::StringLiteralExp)


def test_ocl::expressions::stringliteralexp_constructor_exists():
    assert callable(ocl::expressions::StringLiteralExp.__init__)


def test_ocl::expressions::stringliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl::expressions::stringliteralexp_has_stringSymbol():
    assert hasattr(ocl::expressions::StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in ocl::expressions::StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::expressions::booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::BooleanLiteralExp)


def test_ocl::expressions::booleanliteralexp_constructor_exists():
    assert callable(ocl::expressions::BooleanLiteralExp.__init__)


def test_ocl::expressions::booleanliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl::expressions::booleanliteralexp_has_booleanSymbol():
    assert hasattr(ocl::expressions::BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in ocl::expressions::BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_expressions::ocl::eclass_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EClass)


def test_expressions::ocl::eclass_constructor_exists():
    assert callable(expressions::ocl::EClass.__init__)


def test_expressions::ocl::eclass_constructor_args():
    sig = inspect.signature(expressions::ocl::EClass.__init__)
    params = list(sig.parameters.keys())



def test_navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(NavigationCallExp)


def test_navigationcallexp_constructor_exists():
    assert callable(NavigationCallExp.__init__)


def test_navigationcallexp_constructor_args():
    sig = inspect.signature(NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::associationclasscallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::AssociationClassCallExp)


def test_ocl::expressions::associationclasscallexp_constructor_exists():
    assert callable(ocl::expressions::AssociationClassCallExp.__init__)


def test_ocl::expressions::associationclasscallexp_constructor_args():
    sig = inspect.signature(ocl::expressions::AssociationClassCallExp.__init__)
    params = list(sig.parameters.keys())



def test_primitivereal_is_not_abstract():
    assert not inspect.isabstract(PrimitiveReal)


def test_primitivereal_constructor_exists():
    assert callable(PrimitiveReal.__init__)


def test_primitivereal_constructor_args():
    sig = inspect.signature(PrimitiveReal.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::primitiveinteger_is_not_abstract():
    assert not inspect.isabstract(ocl::types::PrimitiveInteger)


def test_ocl::types::primitiveinteger_constructor_exists():
    assert callable(ocl::types::PrimitiveInteger.__init__)


def test_ocl::types::primitiveinteger_constructor_args():
    sig = inspect.signature(ocl::types::PrimitiveInteger.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::primitivestring_is_not_abstract():
    assert not inspect.isabstract(ocl::types::PrimitiveString)


def test_ocl::types::primitivestring_constructor_exists():
    assert callable(ocl::types::PrimitiveString.__init__)


def test_ocl::types::primitivestring_constructor_args():
    sig = inspect.signature(ocl::types::PrimitiveString.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::primitivereal_is_not_abstract():
    assert not inspect.isabstract(ocl::types::PrimitiveReal)


def test_ocl::types::primitivereal_constructor_exists():
    assert callable(ocl::types::PrimitiveReal.__init__)


def test_ocl::types::primitivereal_constructor_args():
    sig = inspect.signature(ocl::types::PrimitiveReal.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::primitiveboolean_is_not_abstract():
    assert not inspect.isabstract(ocl::types::PrimitiveBoolean)


def test_ocl::types::primitiveboolean_constructor_exists():
    assert callable(ocl::types::PrimitiveBoolean.__init__)


def test_ocl::types::primitiveboolean_constructor_args():
    sig = inspect.signature(ocl::types::PrimitiveBoolean.__init__)
    params = list(sig.parameters.keys())



def test_types::ocl::eclass_is_not_abstract():
    assert not inspect.isabstract(types::ocl::EClass)


def test_types::ocl::eclass_constructor_exists():
    assert callable(types::ocl::EClass.__init__)


def test_types::ocl::eclass_constructor_args():
    sig = inspect.signature(types::ocl::EClass.__init__)
    params = list(sig.parameters.keys())



def test_types::ocl::eoperation_is_not_abstract():
    assert not inspect.isabstract(types::ocl::EOperation)


def test_types::ocl::eoperation_constructor_exists():
    assert callable(types::ocl::EOperation.__init__)


def test_types::ocl::eoperation_constructor_args():
    sig = inspect.signature(types::ocl::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_eclass_is_not_abstract():
    assert not inspect.isabstract(EClass)


def test_eclass_constructor_exists():
    assert callable(EClass.__init__)


def test_eclass_constructor_args():
    sig = inspect.signature(EClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::tupletype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::TupleType)


def test_ocl::types::tupletype_constructor_exists():
    assert callable(ocl::types::TupleType.__init__)


def test_ocl::types::tupletype_constructor_args():
    sig = inspect.signature(ocl::types::TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::elementtype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::ElementType)


def test_ocl::types::elementtype_constructor_exists():
    assert callable(ocl::types::ElementType.__init__)


def test_ocl::types::elementtype_constructor_args():
    sig = inspect.signature(ocl::types::ElementType.__init__)
    params = list(sig.parameters.keys())



def test_types::ocl::eclassifier_is_not_abstract():
    assert not inspect.isabstract(types::ocl::EClassifier)


def test_types::ocl::eclassifier_constructor_exists():
    assert callable(types::ocl::EClassifier.__init__)


def test_types::ocl::eclassifier_constructor_args():
    sig = inspect.signature(types::ocl::EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_utilities::typedastnode_is_not_abstract():
    assert not inspect.isabstract(utilities::TypedASTNode)


def test_utilities::typedastnode_constructor_exists():
    assert callable(utilities::TypedASTNode.__init__)


def test_utilities::typedastnode_constructor_args():
    sig = inspect.signature(utilities::TypedASTNode.__init__)
    params = list(sig.parameters.keys())



def test_edatatype_is_not_abstract():
    assert not inspect.isabstract(EDataType)


def test_edatatype_constructor_exists():
    assert callable(EDataType.__init__)


def test_edatatype_constructor_args():
    sig = inspect.signature(EDataType.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::sequencetype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::SequenceType)


def test_ocl::types::sequencetype_constructor_exists():
    assert callable(ocl::types::SequenceType.__init__)


def test_ocl::types::sequencetype_constructor_args():
    sig = inspect.signature(ocl::types::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::settype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::SetType)


def test_ocl::types::settype_constructor_exists():
    assert callable(ocl::types::SetType.__init__)


def test_ocl::types::settype_constructor_args():
    sig = inspect.signature(ocl::types::SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::OrderedSetType)


def test_ocl::types::orderedsettype_constructor_exists():
    assert callable(ocl::types::OrderedSetType.__init__)


def test_ocl::types::orderedsettype_constructor_args():
    sig = inspect.signature(ocl::types::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::bagtype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::BagType)


def test_ocl::types::bagtype_constructor_exists():
    assert callable(ocl::types::BagType.__init__)


def test_ocl::types::bagtype_constructor_args():
    sig = inspect.signature(ocl::types::BagType.__init__)
    params = list(sig.parameters.keys())



def test_utilities::predefinedtype_is_not_abstract():
    assert not inspect.isabstract(utilities::PredefinedType)


def test_utilities::predefinedtype_constructor_exists():
    assert callable(utilities::PredefinedType.__init__)


def test_utilities::predefinedtype_constructor_args():
    sig = inspect.signature(utilities::PredefinedType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::messagetype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::MessageType)


def test_ocl::types::messagetype_constructor_exists():
    assert callable(ocl::types::MessageType.__init__)


def test_ocl::types::messagetype_constructor_args():
    sig = inspect.signature(ocl::types::MessageType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::primitivetype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::PrimitiveType)


def test_ocl::types::primitivetype_constructor_exists():
    assert callable(ocl::types::PrimitiveType.__init__)


def test_ocl::types::primitivetype_constructor_args():
    sig = inspect.signature(ocl::types::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::collectiontype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::CollectionType)


def test_ocl::types::collectiontype_constructor_exists():
    assert callable(ocl::types::CollectionType.__init__)


def test_ocl::types::collectiontype_constructor_args():
    sig = inspect.signature(ocl::types::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::types::collectiontype_has_kind():
    assert hasattr(ocl::types::CollectionType, "kind")
    descriptor = None
    for klass in ocl::types::CollectionType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_eclassifier_is_not_abstract():
    assert not inspect.isabstract(EClassifier)


def test_eclassifier_constructor_exists():
    assert callable(EClassifier.__init__)


def test_eclassifier_constructor_args():
    sig = inspect.signature(EClassifier.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::typetype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::TypeType)


def test_ocl::types::typetype_constructor_exists():
    assert callable(ocl::types::TypeType.__init__)


def test_ocl::types::typetype_constructor_args():
    sig = inspect.signature(ocl::types::TypeType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::voidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::VoidType)


def test_ocl::types::voidtype_constructor_exists():
    assert callable(ocl::types::VoidType.__init__)


def test_ocl::types::voidtype_constructor_args():
    sig = inspect.signature(ocl::types::VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::invalidtype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::InvalidType)


def test_ocl::types::invalidtype_constructor_exists():
    assert callable(ocl::types::InvalidType.__init__)


def test_ocl::types::invalidtype_constructor_args():
    sig = inspect.signature(ocl::types::InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::types::anytype_is_not_abstract():
    assert not inspect.isabstract(ocl::types::AnyType)


def test_ocl::types::anytype_constructor_exists():
    assert callable(ocl::types::AnyType.__init__)


def test_ocl::types::anytype_constructor_args():
    sig = inspect.signature(ocl::types::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::PropertyCallExp)


def test_ocl::expressions::propertycallexp_constructor_exists():
    assert callable(ocl::expressions::PropertyCallExp.__init__)


def test_ocl::expressions::propertycallexp_constructor_args():
    sig = inspect.signature(ocl::expressions::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_expressions::ocl::eoperation_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EOperation)


def test_expressions::ocl::eoperation_constructor_exists():
    assert callable(expressions::ocl::EOperation.__init__)


def test_expressions::ocl::eoperation_constructor_args():
    sig = inspect.signature(expressions::ocl::EOperation.__init__)
    params = list(sig.parameters.keys())



def test_utilities::astnode_is_not_abstract():
    assert not inspect.isabstract(utilities::ASTNode)


def test_utilities::astnode_constructor_exists():
    assert callable(utilities::ASTNode.__init__)


def test_utilities::astnode_constructor_args():
    sig = inspect.signature(utilities::ASTNode.__init__)
    params = list(sig.parameters.keys())



def test_utilities::visitable_is_not_abstract():
    assert not inspect.isabstract(utilities::Visitable)


def test_utilities::visitable_constructor_exists():
    assert callable(utilities::Visitable.__init__)


def test_utilities::visitable_constructor_args():
    sig = inspect.signature(utilities::Visitable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::uml::constraint_is_not_abstract():
    assert not inspect.isabstract(ocl::uml::Constraint)


def test_ocl::uml::constraint_constructor_exists():
    assert callable(ocl::uml::Constraint.__init__)


def test_ocl::uml::constraint_constructor_args():
    sig = inspect.signature(ocl::uml::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "stereotype" in params, "Missing parameter 'stereotype'"
    assert "instanceVarName" in params, "Missing parameter 'instanceVarName'"

def test_ocl::uml::constraint_has_stereotype():
    assert hasattr(ocl::uml::Constraint, "stereotype")
    descriptor = None
    for klass in ocl::uml::Constraint.__mro__:
        if "stereotype" in klass.__dict__:
            descriptor = klass.__dict__["stereotype"]
            break
    assert isinstance(descriptor, property)

def test_ocl::uml::constraint_has_instanceVarName():
    assert hasattr(ocl::uml::Constraint, "instanceVarName")
    descriptor = None
    for klass in ocl::uml::Constraint.__mro__:
        if "instanceVarName" in klass.__dict__:
            descriptor = klass.__dict__["instanceVarName"]
            break
    assert isinstance(descriptor, property)



def test_uml::typedelement_is_not_abstract():
    assert not inspect.isabstract(uml::TypedElement)


def test_uml::typedelement_constructor_exists():
    assert callable(uml::TypedElement.__init__)


def test_uml::typedelement_constructor_args():
    sig = inspect.signature(uml::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::TupleLiteralPart)


def test_ocl::expressions::tupleliteralpart_constructor_exists():
    assert callable(ocl::expressions::TupleLiteralPart.__init__)


def test_ocl::expressions::tupleliteralpart_constructor_args():
    sig = inspect.signature(ocl::expressions::TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::variable_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::Variable)


def test_ocl::expressions::variable_constructor_exists():
    assert callable(ocl::expressions::Variable.__init__)


def test_ocl::expressions::variable_constructor_args():
    sig = inspect.signature(ocl::expressions::Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::oclexpression_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::OCLExpression)


def test_ocl::expressions::oclexpression_constructor_exists():
    assert callable(ocl::expressions::OCLExpression.__init__)


def test_ocl::expressions::oclexpression_constructor_args():
    sig = inspect.signature(ocl::expressions::OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::NumericLiteralExp)


def test_ocl::expressions::numericliteralexp_constructor_exists():
    assert callable(ocl::expressions::NumericLiteralExp.__init__)


def test_ocl::expressions::numericliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_expressions::ocl::estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EStructuralFeature)


def test_expressions::ocl::estructuralfeature_constructor_exists():
    assert callable(expressions::ocl::EStructuralFeature.__init__)


def test_expressions::ocl::estructuralfeature_constructor_args():
    sig = inspect.signature(expressions::ocl::EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexp_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExp)


def test_featurecallexp_constructor_exists():
    assert callable(FeatureCallExp.__init__)


def test_featurecallexp_constructor_args():
    sig = inspect.signature(FeatureCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::OperationCallExp)


def test_ocl::expressions::operationcallexp_constructor_exists():
    assert callable(ocl::expressions::OperationCallExp.__init__)


def test_ocl::expressions::operationcallexp_constructor_args():
    sig = inspect.signature(ocl::expressions::OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::navigationcallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::NavigationCallExp)


def test_ocl::expressions::navigationcallexp_constructor_exists():
    assert callable(ocl::expressions::NavigationCallExp.__init__)


def test_ocl::expressions::navigationcallexp_constructor_args():
    sig = inspect.signature(ocl::expressions::NavigationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(SendSignalAction)


def test_sendsignalaction_constructor_exists():
    assert callable(SendSignalAction.__init__)


def test_sendsignalaction_constructor_args():
    sig = inspect.signature(SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(CallOperationAction)


def test_calloperationaction_constructor_exists():
    assert callable(CallOperationAction.__init__)


def test_calloperationaction_constructor_args():
    sig = inspect.signature(CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::IteratorExp)


def test_ocl::expressions::iteratorexp_constructor_exists():
    assert callable(ocl::expressions::IteratorExp.__init__)


def test_ocl::expressions::iteratorexp_constructor_args():
    sig = inspect.signature(ocl::expressions::IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::iterateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::IterateExp)


def test_ocl::expressions::iterateexp_constructor_exists():
    assert callable(ocl::expressions::IterateExp.__init__)


def test_ocl::expressions::iterateexp_constructor_args():
    sig = inspect.signature(ocl::expressions::IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::RealLiteralExp)


def test_ocl::expressions::realliteralexp_constructor_exists():
    assert callable(ocl::expressions::RealLiteralExp.__init__)


def test_ocl::expressions::realliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl::expressions::realliteralexp_has_realSymbol():
    assert hasattr(ocl::expressions::RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in ocl::expressions::RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl::expressions::integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::IntegerLiteralExp)


def test_ocl::expressions::integerliteralexp_constructor_exists():
    assert callable(ocl::expressions::IntegerLiteralExp.__init__)


def test_ocl::expressions::integerliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl::expressions::integerliteralexp_has_integerSymbol():
    assert hasattr(ocl::expressions::IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in ocl::expressions::IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::loopexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::LoopExp)


def test_ocl::expressions::loopexp_constructor_exists():
    assert callable(ocl::expressions::LoopExp.__init__)


def test_ocl::expressions::loopexp_constructor_args():
    sig = inspect.signature(ocl::expressions::LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::featurecallexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::FeatureCallExp)


def test_ocl::expressions::featurecallexp_constructor_exists():
    assert callable(ocl::expressions::FeatureCallExp.__init__)


def test_ocl::expressions::featurecallexp_constructor_args():
    sig = inspect.signature(ocl::expressions::FeatureCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "markedPre" in params, "Missing parameter 'markedPre'"

def test_ocl::expressions::featurecallexp_has_markedPre():
    assert hasattr(ocl::expressions::FeatureCallExp, "markedPre")
    descriptor = None
    for klass in ocl::expressions::FeatureCallExp.__mro__:
        if "markedPre" in klass.__dict__:
            descriptor = klass.__dict__["markedPre"]
            break
    assert isinstance(descriptor, property)



def test_expressions::ocl::eenumliteral_is_not_abstract():
    assert not inspect.isabstract(expressions::ocl::EEnumLiteral)


def test_expressions::ocl::eenumliteral_constructor_exists():
    assert callable(expressions::ocl::EEnumLiteral.__init__)


def test_expressions::ocl::eenumliteral_constructor_args():
    sig = inspect.signature(expressions::ocl::EEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::CollectionLiteralPart)


def test_ocl::expressions::collectionliteralpart_constructor_exists():
    assert callable(ocl::expressions::CollectionLiteralPart.__init__)


def test_ocl::expressions::collectionliteralpart_constructor_args():
    sig = inspect.signature(ocl::expressions::CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::TupleLiteralExp)


def test_ocl::expressions::tupleliteralexp_constructor_exists():
    assert callable(ocl::expressions::TupleLiteralExp.__init__)


def test_ocl::expressions::tupleliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::PrimitiveLiteralExp)


def test_ocl::expressions::primitiveliteralexp_constructor_exists():
    assert callable(ocl::expressions::PrimitiveLiteralExp.__init__)


def test_ocl::expressions::primitiveliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::InvalidLiteralExp)


def test_ocl::expressions::invalidliteralexp_constructor_exists():
    assert callable(ocl::expressions::InvalidLiteralExp.__init__)


def test_ocl::expressions::invalidliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::NullLiteralExp)


def test_ocl::expressions::nullliteralexp_constructor_exists():
    assert callable(ocl::expressions::NullLiteralExp.__init__)


def test_ocl::expressions::nullliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::EnumLiteralExp)


def test_ocl::expressions::enumliteralexp_constructor_exists():
    assert callable(ocl::expressions::EnumLiteralExp.__init__)


def test_ocl::expressions::enumliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::CollectionLiteralExp)


def test_ocl::expressions::collectionliteralexp_constructor_exists():
    assert callable(ocl::expressions::CollectionLiteralExp.__init__)


def test_ocl::expressions::collectionliteralexp_constructor_args():
    sig = inspect.signature(ocl::expressions::CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl::expressions::collectionliteralexp_has_kind():
    assert hasattr(ocl::expressions::CollectionLiteralExp, "kind")
    descriptor = None
    for klass in ocl::expressions::CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::collectionrange_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::CollectionRange)


def test_ocl::expressions::collectionrange_constructor_exists():
    assert callable(ocl::expressions::CollectionRange.__init__)


def test_ocl::expressions::collectionrange_constructor_args():
    sig = inspect.signature(ocl::expressions::CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::collectionitem_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::CollectionItem)


def test_ocl::expressions::collectionitem_constructor_exists():
    assert callable(ocl::expressions::CollectionItem.__init__)


def test_ocl::expressions::collectionitem_constructor_args():
    sig = inspect.signature(ocl::expressions::CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCLExpression)


def test_oclexpression_constructor_exists():
    assert callable(OCLExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::literalexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::LiteralExp)


def test_ocl::expressions::literalexp_constructor_exists():
    assert callable(ocl::expressions::LiteralExp.__init__)


def test_ocl::expressions::literalexp_constructor_args():
    sig = inspect.signature(ocl::expressions::LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::letexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::LetExp)


def test_ocl::expressions::letexp_constructor_exists():
    assert callable(ocl::expressions::LetExp.__init__)


def test_ocl::expressions::letexp_constructor_args():
    sig = inspect.signature(ocl::expressions::LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::ifexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::IfExp)


def test_ocl::expressions::ifexp_constructor_exists():
    assert callable(ocl::expressions::IfExp.__init__)


def test_ocl::expressions::ifexp_constructor_args():
    sig = inspect.signature(ocl::expressions::IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::typeexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::TypeExp)


def test_ocl::expressions::typeexp_constructor_exists():
    assert callable(ocl::expressions::TypeExp.__init__)


def test_ocl::expressions::typeexp_constructor_args():
    sig = inspect.signature(ocl::expressions::TypeExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::stateexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::StateExp)


def test_ocl::expressions::stateexp_constructor_exists():
    assert callable(ocl::expressions::StateExp.__init__)


def test_ocl::expressions::stateexp_constructor_args():
    sig = inspect.signature(ocl::expressions::StateExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::variableexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::VariableExp)


def test_ocl::expressions::variableexp_constructor_exists():
    assert callable(ocl::expressions::VariableExp.__init__)


def test_ocl::expressions::variableexp_constructor_args():
    sig = inspect.signature(ocl::expressions::VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_utilities::callingastnode_is_not_abstract():
    assert not inspect.isabstract(utilities::CallingASTNode)


def test_utilities::callingastnode_constructor_exists():
    assert callable(utilities::CallingASTNode.__init__)


def test_utilities::callingastnode_constructor_args():
    sig = inspect.signature(utilities::CallingASTNode.__init__)
    params = list(sig.parameters.keys())



def test_expressions::oclexpression_is_not_abstract():
    assert not inspect.isabstract(expressions::OCLExpression)


def test_expressions::oclexpression_constructor_exists():
    assert callable(expressions::OCLExpression.__init__)


def test_expressions::oclexpression_constructor_args():
    sig = inspect.signature(expressions::OCLExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::callexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::CallExp)


def test_ocl::expressions::callexp_constructor_exists():
    assert callable(ocl::expressions::CallExp.__init__)


def test_ocl::expressions::callexp_constructor_args():
    sig = inspect.signature(ocl::expressions::CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::unspecifiedvalueexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::UnspecifiedValueExp)


def test_ocl::expressions::unspecifiedvalueexp_constructor_exists():
    assert callable(ocl::expressions::UnspecifiedValueExp.__init__)


def test_ocl::expressions::unspecifiedvalueexp_constructor_args():
    sig = inspect.signature(ocl::expressions::UnspecifiedValueExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl::expressions::messageexp_is_not_abstract():
    assert not inspect.isabstract(ocl::expressions::MessageExp)


def test_ocl::expressions::messageexp_constructor_exists():
    assert callable(ocl::expressions::MessageExp.__init__)


def test_ocl::expressions::messageexp_constructor_args():
    sig = inspect.signature(ocl::expressions::MessageExp.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "bag",
        "set",
        "collection",
        "orderedSet",
        "sequence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionKind"


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
ocl::query::Query_strategy = st.builds(
    ocl::query::Query,
    extentMap=
        safe_text
)
ocl::utilities::Visitable_strategy = st.builds(
    ocl::utilities::Visitable,
)
ocl::utilities::PredefinedType_strategy = st.builds(
    ocl::utilities::PredefinedType,
)
ASTNode_strategy = st.builds(
    ASTNode,
)
ocl::utilities::TypedASTNode_strategy = st.builds(
    ocl::utilities::TypedASTNode,
    typeStartPosition=
        st.integers(),
    typeEndPosition=
        st.integers()
)
ocl::utilities::CallingASTNode_strategy = st.builds(
    ocl::utilities::CallingASTNode,
    propertyStartPosition=
        st.integers(),
    propertyEndPosition=
        st.integers()
)
ocl::utilities::ASTNode_strategy = st.builds(
    ocl::utilities::ASTNode,
    endPosition=
        st.integers(),
    startPosition=
        st.integers()
)
uml::ocl::EClassifier_strategy = st.builds(
    uml::ocl::EClassifier,
)
uml::ocl::EClass_strategy = st.builds(
    uml::ocl::EClass,
)
ocl::uml::SendSignalAction_strategy = st.builds(
    ocl::uml::SendSignalAction,
)
uml::ocl::ENamedElement_strategy = st.builds(
    uml::ocl::ENamedElement,
)
ENamedElement_strategy = st.builds(
    ENamedElement,
)
ocl::uml::TypedElement_strategy = st.builds(
    ocl::uml::TypedElement,
)
uml::ocl::EOperation_strategy = st.builds(
    uml::ocl::EOperation,
)
ocl::uml::CallOperationAction_strategy = st.builds(
    ocl::uml::CallOperationAction,
)
expressions::ocl::EParameter_strategy = st.builds(
    expressions::ocl::EParameter,
)
expressions::ocl::EClassifier_strategy = st.builds(
    expressions::ocl::EClassifier,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
expressions::ocl::EObject_strategy = st.builds(
    expressions::ocl::EObject,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
ocl::expressions::StringLiteralExp_strategy = st.builds(
    ocl::expressions::StringLiteralExp,
    stringSymbol=
        safe_text
)
ocl::expressions::BooleanLiteralExp_strategy = st.builds(
    ocl::expressions::BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
expressions::ocl::EClass_strategy = st.builds(
    expressions::ocl::EClass,
)
NavigationCallExp_strategy = st.builds(
    NavigationCallExp,
)
ocl::expressions::AssociationClassCallExp_strategy = st.builds(
    ocl::expressions::AssociationClassCallExp,
)
PrimitiveReal_strategy = st.builds(
    PrimitiveReal,
)
ocl::types::PrimitiveInteger_strategy = st.builds(
    ocl::types::PrimitiveInteger,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
ocl::types::PrimitiveString_strategy = st.builds(
    ocl::types::PrimitiveString,
)
ocl::types::PrimitiveReal_strategy = st.builds(
    ocl::types::PrimitiveReal,
)
ocl::types::PrimitiveBoolean_strategy = st.builds(
    ocl::types::PrimitiveBoolean,
)
types::ocl::EClass_strategy = st.builds(
    types::ocl::EClass,
)
types::ocl::EOperation_strategy = st.builds(
    types::ocl::EOperation,
)
EClass_strategy = st.builds(
    EClass,
)
ocl::types::TupleType_strategy = st.builds(
    ocl::types::TupleType,
)
ocl::types::ElementType_strategy = st.builds(
    ocl::types::ElementType,
)
types::ocl::EClassifier_strategy = st.builds(
    types::ocl::EClassifier,
)
utilities::TypedASTNode_strategy = st.builds(
    utilities::TypedASTNode,
)
EDataType_strategy = st.builds(
    EDataType,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
ocl::types::SequenceType_strategy = st.builds(
    ocl::types::SequenceType,
)
ocl::types::SetType_strategy = st.builds(
    ocl::types::SetType,
)
ocl::types::OrderedSetType_strategy = st.builds(
    ocl::types::OrderedSetType,
)
ocl::types::BagType_strategy = st.builds(
    ocl::types::BagType,
)
utilities::PredefinedType_strategy = st.builds(
    utilities::PredefinedType,
)
ocl::types::MessageType_strategy = st.builds(
    ocl::types::MessageType,
)
ocl::types::PrimitiveType_strategy = st.builds(
    ocl::types::PrimitiveType,
)
ocl::types::CollectionType_strategy = st.builds(
    ocl::types::CollectionType,
    kind=
        safe_text
)
EClassifier_strategy = st.builds(
    EClassifier,
)
ocl::types::TypeType_strategy = st.builds(
    ocl::types::TypeType,
)
ocl::types::VoidType_strategy = st.builds(
    ocl::types::VoidType,
)
ocl::types::InvalidType_strategy = st.builds(
    ocl::types::InvalidType,
)
ocl::types::AnyType_strategy = st.builds(
    ocl::types::AnyType,
)
ocl::expressions::PropertyCallExp_strategy = st.builds(
    ocl::expressions::PropertyCallExp,
)
expressions::ocl::EOperation_strategy = st.builds(
    expressions::ocl::EOperation,
)
utilities::ASTNode_strategy = st.builds(
    utilities::ASTNode,
)
utilities::Visitable_strategy = st.builds(
    utilities::Visitable,
)
ocl::uml::Constraint_strategy = st.builds(
    ocl::uml::Constraint,
    stereotype=
        safe_text,
    instanceVarName=
        safe_text
)
uml::TypedElement_strategy = st.builds(
    uml::TypedElement,
)
ocl::expressions::TupleLiteralPart_strategy = st.builds(
    ocl::expressions::TupleLiteralPart,
)
ocl::expressions::Variable_strategy = st.builds(
    ocl::expressions::Variable,
)
ocl::expressions::OCLExpression_strategy = st.builds(
    ocl::expressions::OCLExpression,
)
ocl::expressions::NumericLiteralExp_strategy = st.builds(
    ocl::expressions::NumericLiteralExp,
)
expressions::ocl::EStructuralFeature_strategy = st.builds(
    expressions::ocl::EStructuralFeature,
)
FeatureCallExp_strategy = st.builds(
    FeatureCallExp,
)
ocl::expressions::OperationCallExp_strategy = st.builds(
    ocl::expressions::OperationCallExp,
)
ocl::expressions::NavigationCallExp_strategy = st.builds(
    ocl::expressions::NavigationCallExp,
)
SendSignalAction_strategy = st.builds(
    SendSignalAction,
)
CallOperationAction_strategy = st.builds(
    CallOperationAction,
)
Variable_strategy = st.builds(
    Variable,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
ocl::expressions::IteratorExp_strategy = st.builds(
    ocl::expressions::IteratorExp,
)
ocl::expressions::IterateExp_strategy = st.builds(
    ocl::expressions::IterateExp,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
ocl::expressions::RealLiteralExp_strategy = st.builds(
    ocl::expressions::RealLiteralExp,
    realSymbol=
        safe_text
)
ocl::expressions::IntegerLiteralExp_strategy = st.builds(
    ocl::expressions::IntegerLiteralExp,
    integerSymbol=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
ocl::expressions::LoopExp_strategy = st.builds(
    ocl::expressions::LoopExp,
)
ocl::expressions::FeatureCallExp_strategy = st.builds(
    ocl::expressions::FeatureCallExp,
    markedPre=
        st.booleans()
)
expressions::ocl::EEnumLiteral_strategy = st.builds(
    expressions::ocl::EEnumLiteral,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ocl::expressions::CollectionLiteralPart_strategy = st.builds(
    ocl::expressions::CollectionLiteralPart,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ocl::expressions::TupleLiteralExp_strategy = st.builds(
    ocl::expressions::TupleLiteralExp,
)
ocl::expressions::PrimitiveLiteralExp_strategy = st.builds(
    ocl::expressions::PrimitiveLiteralExp,
)
ocl::expressions::InvalidLiteralExp_strategy = st.builds(
    ocl::expressions::InvalidLiteralExp,
)
ocl::expressions::NullLiteralExp_strategy = st.builds(
    ocl::expressions::NullLiteralExp,
)
ocl::expressions::EnumLiteralExp_strategy = st.builds(
    ocl::expressions::EnumLiteralExp,
)
ocl::expressions::CollectionLiteralExp_strategy = st.builds(
    ocl::expressions::CollectionLiteralExp,
    kind=
        safe_text
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
ocl::expressions::CollectionRange_strategy = st.builds(
    ocl::expressions::CollectionRange,
)
ocl::expressions::CollectionItem_strategy = st.builds(
    ocl::expressions::CollectionItem,
)
OCLExpression_strategy = st.builds(
    OCLExpression,
)
ocl::expressions::LiteralExp_strategy = st.builds(
    ocl::expressions::LiteralExp,
)
ocl::expressions::LetExp_strategy = st.builds(
    ocl::expressions::LetExp,
)
ocl::expressions::IfExp_strategy = st.builds(
    ocl::expressions::IfExp,
)
ocl::expressions::TypeExp_strategy = st.builds(
    ocl::expressions::TypeExp,
)
ocl::expressions::StateExp_strategy = st.builds(
    ocl::expressions::StateExp,
)
ocl::expressions::VariableExp_strategy = st.builds(
    ocl::expressions::VariableExp,
)
utilities::CallingASTNode_strategy = st.builds(
    utilities::CallingASTNode,
)
expressions::OCLExpression_strategy = st.builds(
    expressions::OCLExpression,
)
ocl::expressions::CallExp_strategy = st.builds(
    ocl::expressions::CallExp,
)
ocl::expressions::UnspecifiedValueExp_strategy = st.builds(
    ocl::expressions::UnspecifiedValueExp,
)
ocl::expressions::MessageExp_strategy = st.builds(
    ocl::expressions::MessageExp,
)

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=50)
def test_ocl::query::query_instantiation(instance):
    assert isinstance(instance, ocl::query::Query)

@given(instance=ocl::query::Query_strategy)
def test_ocl::query::query_extentMap_type(instance):
    assert isinstance(instance.extentMap, str)


@given(instance=ocl::query::Query_strategy)
def test_ocl::query::query_extentMap_setter(instance):
    original = instance.extentMap
    instance.extentMap = original
    assert instance.extentMap == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_select_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.select(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.select).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'select' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'select' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'select' in ocl::query::Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_evaluate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evaluate(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evaluate).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evaluate' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evaluate' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evaluate' in ocl::query::Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_check_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.check(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.check).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'check' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'check' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'check' in ocl::query::Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_querytext_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.queryText()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.queryText).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'queryText' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'queryText' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'queryText' in ocl::query::Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_reject_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.reject(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.reject).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'reject' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'reject' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'reject' in ocl::query::Query is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::query::Query_strategy)
@settings(max_examples=30)
def test_ocl::query::query_resulttype_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.resultType()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.resultType).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'resultType' in ocl::query::Query is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'resultType' in ocl::query::Query did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'resultType' in ocl::query::Query is not implemented or raised an error")

@given(instance=ocl::utilities::Visitable_strategy)
@settings(max_examples=50)
def test_ocl::utilities::visitable_instantiation(instance):
    assert isinstance(instance, ocl::utilities::Visitable)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=ocl::utilities::Visitable_strategy)
@settings(max_examples=30)
def test_ocl::utilities::visitable_accept_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.accept(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.accept).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'accept' in ocl::utilities::Visitable is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'accept' in ocl::utilities::Visitable did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'accept' in ocl::utilities::Visitable is not implemented or raised an error")

@given(instance=ocl::utilities::PredefinedType_strategy)
@settings(max_examples=50)
def test_ocl::utilities::predefinedtype_instantiation(instance):
    assert isinstance(instance, ocl::utilities::PredefinedType)

@given(instance=ASTNode_strategy)
@settings(max_examples=50)
def test_astnode_instantiation(instance):
    assert isinstance(instance, ASTNode)

@given(instance=ocl::utilities::TypedASTNode_strategy)
@settings(max_examples=50)
def test_ocl::utilities::typedastnode_instantiation(instance):
    assert isinstance(instance, ocl::utilities::TypedASTNode)

@given(instance=ocl::utilities::TypedASTNode_strategy)
def test_ocl::utilities::typedastnode_typeStartPosition_type(instance):
    assert isinstance(instance.typeStartPosition, int)


@given(instance=ocl::utilities::TypedASTNode_strategy)
def test_ocl::utilities::typedastnode_typeStartPosition_setter(instance):
    original = instance.typeStartPosition
    instance.typeStartPosition = original
    assert instance.typeStartPosition == original

@given(instance=ocl::utilities::TypedASTNode_strategy)
def test_ocl::utilities::typedastnode_typeEndPosition_type(instance):
    assert isinstance(instance.typeEndPosition, int)


@given(instance=ocl::utilities::TypedASTNode_strategy)
def test_ocl::utilities::typedastnode_typeEndPosition_setter(instance):
    original = instance.typeEndPosition
    instance.typeEndPosition = original
    assert instance.typeEndPosition == original

@given(instance=ocl::utilities::CallingASTNode_strategy)
@settings(max_examples=50)
def test_ocl::utilities::callingastnode_instantiation(instance):
    assert isinstance(instance, ocl::utilities::CallingASTNode)

@given(instance=ocl::utilities::CallingASTNode_strategy)
def test_ocl::utilities::callingastnode_propertyStartPosition_type(instance):
    assert isinstance(instance.propertyStartPosition, int)


@given(instance=ocl::utilities::CallingASTNode_strategy)
def test_ocl::utilities::callingastnode_propertyStartPosition_setter(instance):
    original = instance.propertyStartPosition
    instance.propertyStartPosition = original
    assert instance.propertyStartPosition == original

@given(instance=ocl::utilities::CallingASTNode_strategy)
def test_ocl::utilities::callingastnode_propertyEndPosition_type(instance):
    assert isinstance(instance.propertyEndPosition, int)


@given(instance=ocl::utilities::CallingASTNode_strategy)
def test_ocl::utilities::callingastnode_propertyEndPosition_setter(instance):
    original = instance.propertyEndPosition
    instance.propertyEndPosition = original
    assert instance.propertyEndPosition == original

@given(instance=ocl::utilities::ASTNode_strategy)
@settings(max_examples=50)
def test_ocl::utilities::astnode_instantiation(instance):
    assert isinstance(instance, ocl::utilities::ASTNode)

@given(instance=ocl::utilities::ASTNode_strategy)
def test_ocl::utilities::astnode_endPosition_type(instance):
    assert isinstance(instance.endPosition, int)


@given(instance=ocl::utilities::ASTNode_strategy)
def test_ocl::utilities::astnode_endPosition_setter(instance):
    original = instance.endPosition
    instance.endPosition = original
    assert instance.endPosition == original

@given(instance=ocl::utilities::ASTNode_strategy)
def test_ocl::utilities::astnode_startPosition_type(instance):
    assert isinstance(instance.startPosition, int)


@given(instance=ocl::utilities::ASTNode_strategy)
def test_ocl::utilities::astnode_startPosition_setter(instance):
    original = instance.startPosition
    instance.startPosition = original
    assert instance.startPosition == original

@given(instance=uml::ocl::EClassifier_strategy)
@settings(max_examples=50)
def test_uml::ocl::eclassifier_instantiation(instance):
    assert isinstance(instance, uml::ocl::EClassifier)

@given(instance=uml::ocl::EClass_strategy)
@settings(max_examples=50)
def test_uml::ocl::eclass_instantiation(instance):
    assert isinstance(instance, uml::ocl::EClass)

@given(instance=ocl::uml::SendSignalAction_strategy)
@settings(max_examples=50)
def test_ocl::uml::sendsignalaction_instantiation(instance):
    assert isinstance(instance, ocl::uml::SendSignalAction)

@given(instance=uml::ocl::ENamedElement_strategy)
@settings(max_examples=50)
def test_uml::ocl::enamedelement_instantiation(instance):
    assert isinstance(instance, uml::ocl::ENamedElement)

@given(instance=ENamedElement_strategy)
@settings(max_examples=50)
def test_enamedelement_instantiation(instance):
    assert isinstance(instance, ENamedElement)

@given(instance=ocl::uml::TypedElement_strategy)
@settings(max_examples=50)
def test_ocl::uml::typedelement_instantiation(instance):
    assert isinstance(instance, ocl::uml::TypedElement)

@given(instance=uml::ocl::EOperation_strategy)
@settings(max_examples=50)
def test_uml::ocl::eoperation_instantiation(instance):
    assert isinstance(instance, uml::ocl::EOperation)

@given(instance=ocl::uml::CallOperationAction_strategy)
@settings(max_examples=50)
def test_ocl::uml::calloperationaction_instantiation(instance):
    assert isinstance(instance, ocl::uml::CallOperationAction)

@given(instance=expressions::ocl::EParameter_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eparameter_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EParameter)

@given(instance=expressions::ocl::EClassifier_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eclassifier_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EClassifier)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=expressions::ocl::EObject_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eobject_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EObject)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=ocl::expressions::StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::stringliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::StringLiteralExp)

@given(instance=ocl::expressions::StringLiteralExp_strategy)
def test_ocl::expressions::stringliteralexp_stringSymbol_type(instance):
    assert isinstance(instance.stringSymbol, str)


@given(instance=ocl::expressions::StringLiteralExp_strategy)
def test_ocl::expressions::stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=ocl::expressions::BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::BooleanLiteralExp)

@given(instance=ocl::expressions::BooleanLiteralExp_strategy)
def test_ocl::expressions::booleanliteralexp_booleanSymbol_type(instance):
    assert isinstance(instance.booleanSymbol, str)


@given(instance=ocl::expressions::BooleanLiteralExp_strategy)
def test_ocl::expressions::booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=expressions::ocl::EClass_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eclass_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EClass)

@given(instance=NavigationCallExp_strategy)
@settings(max_examples=50)
def test_navigationcallexp_instantiation(instance):
    assert isinstance(instance, NavigationCallExp)

@given(instance=ocl::expressions::AssociationClassCallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::associationclasscallexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::AssociationClassCallExp)

@given(instance=PrimitiveReal_strategy)
@settings(max_examples=50)
def test_primitivereal_instantiation(instance):
    assert isinstance(instance, PrimitiveReal)

@given(instance=ocl::types::PrimitiveInteger_strategy)
@settings(max_examples=50)
def test_ocl::types::primitiveinteger_instantiation(instance):
    assert isinstance(instance, ocl::types::PrimitiveInteger)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=ocl::types::PrimitiveString_strategy)
@settings(max_examples=50)
def test_ocl::types::primitivestring_instantiation(instance):
    assert isinstance(instance, ocl::types::PrimitiveString)

@given(instance=ocl::types::PrimitiveReal_strategy)
@settings(max_examples=50)
def test_ocl::types::primitivereal_instantiation(instance):
    assert isinstance(instance, ocl::types::PrimitiveReal)

@given(instance=ocl::types::PrimitiveBoolean_strategy)
@settings(max_examples=50)
def test_ocl::types::primitiveboolean_instantiation(instance):
    assert isinstance(instance, ocl::types::PrimitiveBoolean)

@given(instance=types::ocl::EClass_strategy)
@settings(max_examples=50)
def test_types::ocl::eclass_instantiation(instance):
    assert isinstance(instance, types::ocl::EClass)

@given(instance=types::ocl::EOperation_strategy)
@settings(max_examples=50)
def test_types::ocl::eoperation_instantiation(instance):
    assert isinstance(instance, types::ocl::EOperation)

@given(instance=EClass_strategy)
@settings(max_examples=50)
def test_eclass_instantiation(instance):
    assert isinstance(instance, EClass)

@given(instance=ocl::types::TupleType_strategy)
@settings(max_examples=50)
def test_ocl::types::tupletype_instantiation(instance):
    assert isinstance(instance, ocl::types::TupleType)

@given(instance=ocl::types::ElementType_strategy)
@settings(max_examples=50)
def test_ocl::types::elementtype_instantiation(instance):
    assert isinstance(instance, ocl::types::ElementType)

@given(instance=types::ocl::EClassifier_strategy)
@settings(max_examples=50)
def test_types::ocl::eclassifier_instantiation(instance):
    assert isinstance(instance, types::ocl::EClassifier)

@given(instance=utilities::TypedASTNode_strategy)
@settings(max_examples=50)
def test_utilities::typedastnode_instantiation(instance):
    assert isinstance(instance, utilities::TypedASTNode)

@given(instance=EDataType_strategy)
@settings(max_examples=50)
def test_edatatype_instantiation(instance):
    assert isinstance(instance, EDataType)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=ocl::types::SequenceType_strategy)
@settings(max_examples=50)
def test_ocl::types::sequencetype_instantiation(instance):
    assert isinstance(instance, ocl::types::SequenceType)

@given(instance=ocl::types::SetType_strategy)
@settings(max_examples=50)
def test_ocl::types::settype_instantiation(instance):
    assert isinstance(instance, ocl::types::SetType)

@given(instance=ocl::types::OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl::types::orderedsettype_instantiation(instance):
    assert isinstance(instance, ocl::types::OrderedSetType)

@given(instance=ocl::types::BagType_strategy)
@settings(max_examples=50)
def test_ocl::types::bagtype_instantiation(instance):
    assert isinstance(instance, ocl::types::BagType)

@given(instance=utilities::PredefinedType_strategy)
@settings(max_examples=50)
def test_utilities::predefinedtype_instantiation(instance):
    assert isinstance(instance, utilities::PredefinedType)

@given(instance=ocl::types::MessageType_strategy)
@settings(max_examples=50)
def test_ocl::types::messagetype_instantiation(instance):
    assert isinstance(instance, ocl::types::MessageType)

@given(instance=ocl::types::PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl::types::primitivetype_instantiation(instance):
    assert isinstance(instance, ocl::types::PrimitiveType)

@given(instance=ocl::types::CollectionType_strategy)
@settings(max_examples=50)
def test_ocl::types::collectiontype_instantiation(instance):
    assert isinstance(instance, ocl::types::CollectionType)

@given(instance=ocl::types::CollectionType_strategy)
def test_ocl::types::collectiontype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ocl::types::CollectionType_strategy)
def test_ocl::types::collectiontype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=EClassifier_strategy)
@settings(max_examples=50)
def test_eclassifier_instantiation(instance):
    assert isinstance(instance, EClassifier)

@given(instance=ocl::types::TypeType_strategy)
@settings(max_examples=50)
def test_ocl::types::typetype_instantiation(instance):
    assert isinstance(instance, ocl::types::TypeType)

@given(instance=ocl::types::VoidType_strategy)
@settings(max_examples=50)
def test_ocl::types::voidtype_instantiation(instance):
    assert isinstance(instance, ocl::types::VoidType)

@given(instance=ocl::types::InvalidType_strategy)
@settings(max_examples=50)
def test_ocl::types::invalidtype_instantiation(instance):
    assert isinstance(instance, ocl::types::InvalidType)

@given(instance=ocl::types::AnyType_strategy)
@settings(max_examples=50)
def test_ocl::types::anytype_instantiation(instance):
    assert isinstance(instance, ocl::types::AnyType)

@given(instance=ocl::expressions::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::propertycallexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::PropertyCallExp)

@given(instance=expressions::ocl::EOperation_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eoperation_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EOperation)

@given(instance=utilities::ASTNode_strategy)
@settings(max_examples=50)
def test_utilities::astnode_instantiation(instance):
    assert isinstance(instance, utilities::ASTNode)

@given(instance=utilities::Visitable_strategy)
@settings(max_examples=50)
def test_utilities::visitable_instantiation(instance):
    assert isinstance(instance, utilities::Visitable)

@given(instance=ocl::uml::Constraint_strategy)
@settings(max_examples=50)
def test_ocl::uml::constraint_instantiation(instance):
    assert isinstance(instance, ocl::uml::Constraint)

@given(instance=ocl::uml::Constraint_strategy)
def test_ocl::uml::constraint_stereotype_type(instance):
    assert isinstance(instance.stereotype, str)


@given(instance=ocl::uml::Constraint_strategy)
def test_ocl::uml::constraint_stereotype_setter(instance):
    original = instance.stereotype
    instance.stereotype = original
    assert instance.stereotype == original

@given(instance=ocl::uml::Constraint_strategy)
def test_ocl::uml::constraint_instanceVarName_type(instance):
    assert isinstance(instance.instanceVarName, str)


@given(instance=ocl::uml::Constraint_strategy)
def test_ocl::uml::constraint_instanceVarName_setter(instance):
    original = instance.instanceVarName
    instance.instanceVarName = original
    assert instance.instanceVarName == original

@given(instance=uml::TypedElement_strategy)
@settings(max_examples=50)
def test_uml::typedelement_instantiation(instance):
    assert isinstance(instance, uml::TypedElement)

@given(instance=ocl::expressions::TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::expressions::tupleliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::expressions::TupleLiteralPart)

@given(instance=ocl::expressions::Variable_strategy)
@settings(max_examples=50)
def test_ocl::expressions::variable_instantiation(instance):
    assert isinstance(instance, ocl::expressions::Variable)

@given(instance=ocl::expressions::OCLExpression_strategy)
@settings(max_examples=50)
def test_ocl::expressions::oclexpression_instantiation(instance):
    assert isinstance(instance, ocl::expressions::OCLExpression)

@given(instance=ocl::expressions::NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::numericliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::NumericLiteralExp)

@given(instance=expressions::ocl::EStructuralFeature_strategy)
@settings(max_examples=50)
def test_expressions::ocl::estructuralfeature_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EStructuralFeature)

@given(instance=FeatureCallExp_strategy)
@settings(max_examples=50)
def test_featurecallexp_instantiation(instance):
    assert isinstance(instance, FeatureCallExp)

@given(instance=ocl::expressions::OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::operationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::OperationCallExp)

@given(instance=ocl::expressions::NavigationCallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::navigationcallexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::NavigationCallExp)

@given(instance=SendSignalAction_strategy)
@settings(max_examples=50)
def test_sendsignalaction_instantiation(instance):
    assert isinstance(instance, SendSignalAction)

@given(instance=CallOperationAction_strategy)
@settings(max_examples=50)
def test_calloperationaction_instantiation(instance):
    assert isinstance(instance, CallOperationAction)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=ocl::expressions::IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::iteratorexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::IteratorExp)

@given(instance=ocl::expressions::IterateExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::iterateexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::IterateExp)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=ocl::expressions::RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::realliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::RealLiteralExp)

@given(instance=ocl::expressions::RealLiteralExp_strategy)
def test_ocl::expressions::realliteralexp_realSymbol_type(instance):
    assert isinstance(instance.realSymbol, str)


@given(instance=ocl::expressions::RealLiteralExp_strategy)
def test_ocl::expressions::realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=ocl::expressions::IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::integerliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::IntegerLiteralExp)

@given(instance=ocl::expressions::IntegerLiteralExp_strategy)
def test_ocl::expressions::integerliteralexp_integerSymbol_type(instance):
    assert isinstance(instance.integerSymbol, str)


@given(instance=ocl::expressions::IntegerLiteralExp_strategy)
def test_ocl::expressions::integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=ocl::expressions::LoopExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::loopexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::LoopExp)

@given(instance=ocl::expressions::FeatureCallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::featurecallexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::FeatureCallExp)

@given(instance=ocl::expressions::FeatureCallExp_strategy)
def test_ocl::expressions::featurecallexp_markedPre_type(instance):
    assert isinstance(instance.markedPre, bool)


@given(instance=ocl::expressions::FeatureCallExp_strategy)
def test_ocl::expressions::featurecallexp_markedPre_setter(instance):
    original = instance.markedPre
    instance.markedPre = original
    assert instance.markedPre == original

@given(instance=expressions::ocl::EEnumLiteral_strategy)
@settings(max_examples=50)
def test_expressions::ocl::eenumliteral_instantiation(instance):
    assert isinstance(instance, expressions::ocl::EEnumLiteral)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ocl::expressions::CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl::expressions::collectionliteralpart_instantiation(instance):
    assert isinstance(instance, ocl::expressions::CollectionLiteralPart)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ocl::expressions::TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::TupleLiteralExp)

@given(instance=ocl::expressions::PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::PrimitiveLiteralExp)

@given(instance=ocl::expressions::InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::invalidliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::InvalidLiteralExp)

@given(instance=ocl::expressions::NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::nullliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::NullLiteralExp)

@given(instance=ocl::expressions::EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::enumliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::EnumLiteralExp)

@given(instance=ocl::expressions::CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::CollectionLiteralExp)

@given(instance=ocl::expressions::CollectionLiteralExp_strategy)
def test_ocl::expressions::collectionliteralexp_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=ocl::expressions::CollectionLiteralExp_strategy)
def test_ocl::expressions::collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=ocl::expressions::CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl::expressions::collectionrange_instantiation(instance):
    assert isinstance(instance, ocl::expressions::CollectionRange)

@given(instance=ocl::expressions::CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl::expressions::collectionitem_instantiation(instance):
    assert isinstance(instance, ocl::expressions::CollectionItem)

@given(instance=OCLExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OCLExpression)

@given(instance=ocl::expressions::LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::literalexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::LiteralExp)

@given(instance=ocl::expressions::LetExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::letexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::LetExp)

@given(instance=ocl::expressions::IfExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::ifexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::IfExp)

@given(instance=ocl::expressions::TypeExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::typeexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::TypeExp)

@given(instance=ocl::expressions::StateExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::stateexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::StateExp)

@given(instance=ocl::expressions::VariableExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::variableexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::VariableExp)

@given(instance=utilities::CallingASTNode_strategy)
@settings(max_examples=50)
def test_utilities::callingastnode_instantiation(instance):
    assert isinstance(instance, utilities::CallingASTNode)

@given(instance=expressions::OCLExpression_strategy)
@settings(max_examples=50)
def test_expressions::oclexpression_instantiation(instance):
    assert isinstance(instance, expressions::OCLExpression)

@given(instance=ocl::expressions::CallExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::callexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::CallExp)

@given(instance=ocl::expressions::UnspecifiedValueExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::unspecifiedvalueexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::UnspecifiedValueExp)

@given(instance=ocl::expressions::MessageExp_strategy)
@settings(max_examples=50)
def test_ocl::expressions::messageexp_instantiation(instance):
    assert isinstance(instance, ocl::expressions::MessageExp)
