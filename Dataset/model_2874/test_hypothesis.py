import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CollectionInitValue,
    dom::ExpRange,
    dom::ExprList,
    AssignmentStatement,
    dom::SpecialAssignmentStatement,
    NameExpression,
    dom::SpecialNameExpression,
    Annotation,
    dom::SimpleAnnotation,
    dom::ModelExpression,
    dom::ShortModelDeclarationExpression,
    SwitchCaseStatement,
    dom::ExecutableAnnotation,
    CollectionType,
    dom::BagType,
    dom::SequenceType,
    dom::OrderedSetType,
    dom::SetType,
    PrimitiveType,
    dom::RealType,
    dom::IntegerType,
    dom::StringType,
    dom::BooleanType,
    Type,
    dom::ModelElementType,
    dom::CollectionType,
    dom::NativeType,
    dom::PrimitiveType,
    dom::MapType,
    dom::AnyType,
    CollectionExpression,
    dom::SequenceExpression,
    dom::OrderedSetExpression,
    dom::BagExpression,
    dom::SetExpression,
    LiteralExpression,
    dom::CollectionExpression,
    dom::MapExpression,
    dom::PrimitiveExpression,
    dom::SwitchCaseDefaultStatement,
    dom::SwitchCaseExpressionStatement,
    UnaryOperatorExpression,
    dom::NotOperatorExpression,
    dom::NegativeOperatorExpression,
    Statement,
    dom::TransactionStatement,
    dom::ReturnStatement,
    dom::ForStatement,
    dom::ContinueStatement,
    dom::SwitchCaseStatement,
    dom::BreakAllStatement,
    dom::ThrowStatement,
    dom::ExpressionStatement,
    dom::IfStatement,
    dom::BreakStatement,
    dom::AbortStatement,
    dom::WhileStatement,
    dom::SwitchStatement,
    dom::DeleteStatement,
    dom::AssignmentStatement,
    PrimitiveExpression,
    dom::RealExpression,
    dom::BooleanExpression,
    BinaryOperatorExpression,
    dom::XorOperatorExpression,
    dom::DivideOperatorExpression,
    dom::OrOperatorExpression,
    dom::PlusOperatorExpression,
    dom::NotEqualsOperatorExpression,
    dom::AndOperatorExpression,
    OperatorExpression,
    dom::UnaryOperatorExpression,
    dom::BinaryOperatorExpression,
    Expression,
    dom::VariableDeclarationExpression,
    dom::EnumerationLiteralExpression,
    dom::NewExpression,
    dom::ModelElementTypeExpression,
    dom::LiteralExpression,
    dom::FormalParameterExpression,
    dom::OperatorExpression,
    dom::MultiplyOperatorExpression,
    dom::MinusOperatorExpression,
    FeatureCallExpression,
    dom::PropertyCallExpression,
    dom::FOLMethodCallExpression,
    dom::MethodCallExpression,
    dom::LessThanOrEqualToOperatorExpression,
    dom::LessThanOperatorExpression,
    dom::IntegerExpression,
    dom::ImpliesOperatorExpression,
    dom::GreaterThanOrEqualToOperatorExpression,
    dom::GreaterThanOperatorExpression,
    dom::FeatureCallExpression,
    dom::EqualsOperatorExpression,
    dom::DomElement,
    dom::StringExpression,
    dom::ModelDeclarationStatement,
    dom::NameExpression,
    DomElement,
    dom::Block,
    dom::Type,
    dom::OperationDefinition,
    dom::Import,
    dom::CollectionInitValue,
    dom::Statement,
    dom::Expression,
    dom::KeyValue,
    dom::ModelDeclarationParameter,
    dom::Annotation,
    dom::AnnotationBlock,
    dom::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(CollectionInitValue)


def test_collectioninitvalue_constructor_exists():
    assert callable(CollectionInitValue.__init__)


def test_collectioninitvalue_constructor_args():
    sig = inspect.signature(CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::exprange_is_not_abstract():
    assert not inspect.isabstract(dom::ExpRange)


def test_dom::exprange_constructor_exists():
    assert callable(dom::ExpRange.__init__)


def test_dom::exprange_constructor_args():
    sig = inspect.signature(dom::ExpRange.__init__)
    params = list(sig.parameters.keys())



def test_dom::exprlist_is_not_abstract():
    assert not inspect.isabstract(dom::ExprList)


def test_dom::exprlist_constructor_exists():
    assert callable(dom::ExprList.__init__)


def test_dom::exprlist_constructor_args():
    sig = inspect.signature(dom::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(AssignmentStatement)


def test_assignmentstatement_constructor_exists():
    assert callable(AssignmentStatement.__init__)


def test_assignmentstatement_constructor_args():
    sig = inspect.signature(AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::specialassignmentstatement_is_not_abstract():
    assert not inspect.isabstract(dom::SpecialAssignmentStatement)


def test_dom::specialassignmentstatement_constructor_exists():
    assert callable(dom::SpecialAssignmentStatement.__init__)


def test_dom::specialassignmentstatement_constructor_args():
    sig = inspect.signature(dom::SpecialAssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_nameexpression_is_not_abstract():
    assert not inspect.isabstract(NameExpression)


def test_nameexpression_constructor_exists():
    assert callable(NameExpression.__init__)


def test_nameexpression_constructor_args():
    sig = inspect.signature(NameExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::specialnameexpression_is_not_abstract():
    assert not inspect.isabstract(dom::SpecialNameExpression)


def test_dom::specialnameexpression_constructor_exists():
    assert callable(dom::SpecialNameExpression.__init__)


def test_dom::specialnameexpression_constructor_args():
    sig = inspect.signature(dom::SpecialNameExpression.__init__)
    params = list(sig.parameters.keys())



def test_annotation_is_not_abstract():
    assert not inspect.isabstract(Annotation)


def test_annotation_constructor_exists():
    assert callable(Annotation.__init__)


def test_annotation_constructor_args():
    sig = inspect.signature(Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::simpleannotation_is_not_abstract():
    assert not inspect.isabstract(dom::SimpleAnnotation)


def test_dom::simpleannotation_constructor_exists():
    assert callable(dom::SimpleAnnotation.__init__)


def test_dom::simpleannotation_constructor_args():
    sig = inspect.signature(dom::SimpleAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::modelexpression_is_not_abstract():
    assert not inspect.isabstract(dom::ModelExpression)


def test_dom::modelexpression_constructor_exists():
    assert callable(dom::ModelExpression.__init__)


def test_dom::modelexpression_constructor_args():
    sig = inspect.signature(dom::ModelExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::shortmodeldeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(dom::ShortModelDeclarationExpression)


def test_dom::shortmodeldeclarationexpression_constructor_exists():
    assert callable(dom::ShortModelDeclarationExpression.__init__)


def test_dom::shortmodeldeclarationexpression_constructor_args():
    sig = inspect.signature(dom::ShortModelDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(SwitchCaseStatement)


def test_switchcasestatement_constructor_exists():
    assert callable(SwitchCaseStatement.__init__)


def test_switchcasestatement_constructor_args():
    sig = inspect.signature(SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::executableannotation_is_not_abstract():
    assert not inspect.isabstract(dom::ExecutableAnnotation)


def test_dom::executableannotation_constructor_exists():
    assert callable(dom::ExecutableAnnotation.__init__)


def test_dom::executableannotation_constructor_args():
    sig = inspect.signature(dom::ExecutableAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_dom::bagtype_is_not_abstract():
    assert not inspect.isabstract(dom::BagType)


def test_dom::bagtype_constructor_exists():
    assert callable(dom::BagType.__init__)


def test_dom::bagtype_constructor_args():
    sig = inspect.signature(dom::BagType.__init__)
    params = list(sig.parameters.keys())



def test_dom::sequencetype_is_not_abstract():
    assert not inspect.isabstract(dom::SequenceType)


def test_dom::sequencetype_constructor_exists():
    assert callable(dom::SequenceType.__init__)


def test_dom::sequencetype_constructor_args():
    sig = inspect.signature(dom::SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_dom::orderedsettype_is_not_abstract():
    assert not inspect.isabstract(dom::OrderedSetType)


def test_dom::orderedsettype_constructor_exists():
    assert callable(dom::OrderedSetType.__init__)


def test_dom::orderedsettype_constructor_args():
    sig = inspect.signature(dom::OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_dom::settype_is_not_abstract():
    assert not inspect.isabstract(dom::SetType)


def test_dom::settype_constructor_exists():
    assert callable(dom::SetType.__init__)


def test_dom::settype_constructor_args():
    sig = inspect.signature(dom::SetType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dom::realtype_is_not_abstract():
    assert not inspect.isabstract(dom::RealType)


def test_dom::realtype_constructor_exists():
    assert callable(dom::RealType.__init__)


def test_dom::realtype_constructor_args():
    sig = inspect.signature(dom::RealType.__init__)
    params = list(sig.parameters.keys())



def test_dom::integertype_is_not_abstract():
    assert not inspect.isabstract(dom::IntegerType)


def test_dom::integertype_constructor_exists():
    assert callable(dom::IntegerType.__init__)


def test_dom::integertype_constructor_args():
    sig = inspect.signature(dom::IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_dom::stringtype_is_not_abstract():
    assert not inspect.isabstract(dom::StringType)


def test_dom::stringtype_constructor_exists():
    assert callable(dom::StringType.__init__)


def test_dom::stringtype_constructor_args():
    sig = inspect.signature(dom::StringType.__init__)
    params = list(sig.parameters.keys())



def test_dom::booleantype_is_not_abstract():
    assert not inspect.isabstract(dom::BooleanType)


def test_dom::booleantype_constructor_exists():
    assert callable(dom::BooleanType.__init__)


def test_dom::booleantype_constructor_args():
    sig = inspect.signature(dom::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dom::modelelementtype_is_not_abstract():
    assert not inspect.isabstract(dom::ModelElementType)


def test_dom::modelelementtype_constructor_exists():
    assert callable(dom::ModelElementType.__init__)


def test_dom::modelelementtype_constructor_args():
    sig = inspect.signature(dom::ModelElementType.__init__)
    params = list(sig.parameters.keys())



def test_dom::collectiontype_is_not_abstract():
    assert not inspect.isabstract(dom::CollectionType)


def test_dom::collectiontype_constructor_exists():
    assert callable(dom::CollectionType.__init__)


def test_dom::collectiontype_constructor_args():
    sig = inspect.signature(dom::CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_dom::nativetype_is_not_abstract():
    assert not inspect.isabstract(dom::NativeType)


def test_dom::nativetype_constructor_exists():
    assert callable(dom::NativeType.__init__)


def test_dom::nativetype_constructor_args():
    sig = inspect.signature(dom::NativeType.__init__)
    params = list(sig.parameters.keys())



def test_dom::primitivetype_is_not_abstract():
    assert not inspect.isabstract(dom::PrimitiveType)


def test_dom::primitivetype_constructor_exists():
    assert callable(dom::PrimitiveType.__init__)


def test_dom::primitivetype_constructor_args():
    sig = inspect.signature(dom::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_dom::maptype_is_not_abstract():
    assert not inspect.isabstract(dom::MapType)


def test_dom::maptype_constructor_exists():
    assert callable(dom::MapType.__init__)


def test_dom::maptype_constructor_args():
    sig = inspect.signature(dom::MapType.__init__)
    params = list(sig.parameters.keys())



def test_dom::anytype_is_not_abstract():
    assert not inspect.isabstract(dom::AnyType)


def test_dom::anytype_constructor_exists():
    assert callable(dom::AnyType.__init__)


def test_dom::anytype_constructor_args():
    sig = inspect.signature(dom::AnyType.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpression_is_not_abstract():
    assert not inspect.isabstract(CollectionExpression)


def test_collectionexpression_constructor_exists():
    assert callable(CollectionExpression.__init__)


def test_collectionexpression_constructor_args():
    sig = inspect.signature(CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::sequenceexpression_is_not_abstract():
    assert not inspect.isabstract(dom::SequenceExpression)


def test_dom::sequenceexpression_constructor_exists():
    assert callable(dom::SequenceExpression.__init__)


def test_dom::sequenceexpression_constructor_args():
    sig = inspect.signature(dom::SequenceExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::orderedsetexpression_is_not_abstract():
    assert not inspect.isabstract(dom::OrderedSetExpression)


def test_dom::orderedsetexpression_constructor_exists():
    assert callable(dom::OrderedSetExpression.__init__)


def test_dom::orderedsetexpression_constructor_args():
    sig = inspect.signature(dom::OrderedSetExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::bagexpression_is_not_abstract():
    assert not inspect.isabstract(dom::BagExpression)


def test_dom::bagexpression_constructor_exists():
    assert callable(dom::BagExpression.__init__)


def test_dom::bagexpression_constructor_args():
    sig = inspect.signature(dom::BagExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::setexpression_is_not_abstract():
    assert not inspect.isabstract(dom::SetExpression)


def test_dom::setexpression_constructor_exists():
    assert callable(dom::SetExpression.__init__)


def test_dom::setexpression_constructor_args():
    sig = inspect.signature(dom::SetExpression.__init__)
    params = list(sig.parameters.keys())



def test_literalexpression_is_not_abstract():
    assert not inspect.isabstract(LiteralExpression)


def test_literalexpression_constructor_exists():
    assert callable(LiteralExpression.__init__)


def test_literalexpression_constructor_args():
    sig = inspect.signature(LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::collectionexpression_is_not_abstract():
    assert not inspect.isabstract(dom::CollectionExpression)


def test_dom::collectionexpression_constructor_exists():
    assert callable(dom::CollectionExpression.__init__)


def test_dom::collectionexpression_constructor_args():
    sig = inspect.signature(dom::CollectionExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::mapexpression_is_not_abstract():
    assert not inspect.isabstract(dom::MapExpression)


def test_dom::mapexpression_constructor_exists():
    assert callable(dom::MapExpression.__init__)


def test_dom::mapexpression_constructor_args():
    sig = inspect.signature(dom::MapExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(dom::PrimitiveExpression)


def test_dom::primitiveexpression_constructor_exists():
    assert callable(dom::PrimitiveExpression.__init__)


def test_dom::primitiveexpression_constructor_args():
    sig = inspect.signature(dom::PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchcasedefaultstatement_is_not_abstract():
    assert not inspect.isabstract(dom::SwitchCaseDefaultStatement)


def test_dom::switchcasedefaultstatement_constructor_exists():
    assert callable(dom::SwitchCaseDefaultStatement.__init__)


def test_dom::switchcasedefaultstatement_constructor_args():
    sig = inspect.signature(dom::SwitchCaseDefaultStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchcaseexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(dom::SwitchCaseExpressionStatement)


def test_dom::switchcaseexpressionstatement_constructor_exists():
    assert callable(dom::SwitchCaseExpressionStatement.__init__)


def test_dom::switchcaseexpressionstatement_constructor_args():
    sig = inspect.signature(dom::SwitchCaseExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryOperatorExpression)


def test_unaryoperatorexpression_constructor_exists():
    assert callable(UnaryOperatorExpression.__init__)


def test_unaryoperatorexpression_constructor_args():
    sig = inspect.signature(UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::notoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NotOperatorExpression)


def test_dom::notoperatorexpression_constructor_exists():
    assert callable(dom::NotOperatorExpression.__init__)


def test_dom::notoperatorexpression_constructor_args():
    sig = inspect.signature(dom::NotOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::negativeoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NegativeOperatorExpression)


def test_dom::negativeoperatorexpression_constructor_exists():
    assert callable(dom::NegativeOperatorExpression.__init__)


def test_dom::negativeoperatorexpression_constructor_args():
    sig = inspect.signature(dom::NegativeOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom::transactionstatement_is_not_abstract():
    assert not inspect.isabstract(dom::TransactionStatement)


def test_dom::transactionstatement_constructor_exists():
    assert callable(dom::TransactionStatement.__init__)


def test_dom::transactionstatement_constructor_args():
    sig = inspect.signature(dom::TransactionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::returnstatement_is_not_abstract():
    assert not inspect.isabstract(dom::ReturnStatement)


def test_dom::returnstatement_constructor_exists():
    assert callable(dom::ReturnStatement.__init__)


def test_dom::returnstatement_constructor_args():
    sig = inspect.signature(dom::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::forstatement_is_not_abstract():
    assert not inspect.isabstract(dom::ForStatement)


def test_dom::forstatement_constructor_exists():
    assert callable(dom::ForStatement.__init__)


def test_dom::forstatement_constructor_args():
    sig = inspect.signature(dom::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::continuestatement_is_not_abstract():
    assert not inspect.isabstract(dom::ContinueStatement)


def test_dom::continuestatement_constructor_exists():
    assert callable(dom::ContinueStatement.__init__)


def test_dom::continuestatement_constructor_args():
    sig = inspect.signature(dom::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchcasestatement_is_not_abstract():
    assert not inspect.isabstract(dom::SwitchCaseStatement)


def test_dom::switchcasestatement_constructor_exists():
    assert callable(dom::SwitchCaseStatement.__init__)


def test_dom::switchcasestatement_constructor_args():
    sig = inspect.signature(dom::SwitchCaseStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::breakallstatement_is_not_abstract():
    assert not inspect.isabstract(dom::BreakAllStatement)


def test_dom::breakallstatement_constructor_exists():
    assert callable(dom::BreakAllStatement.__init__)


def test_dom::breakallstatement_constructor_args():
    sig = inspect.signature(dom::BreakAllStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::throwstatement_is_not_abstract():
    assert not inspect.isabstract(dom::ThrowStatement)


def test_dom::throwstatement_constructor_exists():
    assert callable(dom::ThrowStatement.__init__)


def test_dom::throwstatement_constructor_args():
    sig = inspect.signature(dom::ThrowStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(dom::ExpressionStatement)


def test_dom::expressionstatement_constructor_exists():
    assert callable(dom::ExpressionStatement.__init__)


def test_dom::expressionstatement_constructor_args():
    sig = inspect.signature(dom::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::ifstatement_is_not_abstract():
    assert not inspect.isabstract(dom::IfStatement)


def test_dom::ifstatement_constructor_exists():
    assert callable(dom::IfStatement.__init__)


def test_dom::ifstatement_constructor_args():
    sig = inspect.signature(dom::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::breakstatement_is_not_abstract():
    assert not inspect.isabstract(dom::BreakStatement)


def test_dom::breakstatement_constructor_exists():
    assert callable(dom::BreakStatement.__init__)


def test_dom::breakstatement_constructor_args():
    sig = inspect.signature(dom::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::abortstatement_is_not_abstract():
    assert not inspect.isabstract(dom::AbortStatement)


def test_dom::abortstatement_constructor_exists():
    assert callable(dom::AbortStatement.__init__)


def test_dom::abortstatement_constructor_args():
    sig = inspect.signature(dom::AbortStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::whilestatement_is_not_abstract():
    assert not inspect.isabstract(dom::WhileStatement)


def test_dom::whilestatement_constructor_exists():
    assert callable(dom::WhileStatement.__init__)


def test_dom::whilestatement_constructor_args():
    sig = inspect.signature(dom::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::switchstatement_is_not_abstract():
    assert not inspect.isabstract(dom::SwitchStatement)


def test_dom::switchstatement_constructor_exists():
    assert callable(dom::SwitchStatement.__init__)


def test_dom::switchstatement_constructor_args():
    sig = inspect.signature(dom::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::deletestatement_is_not_abstract():
    assert not inspect.isabstract(dom::DeleteStatement)


def test_dom::deletestatement_constructor_exists():
    assert callable(dom::DeleteStatement.__init__)


def test_dom::deletestatement_constructor_args():
    sig = inspect.signature(dom::DeleteStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(dom::AssignmentStatement)


def test_dom::assignmentstatement_constructor_exists():
    assert callable(dom::AssignmentStatement.__init__)


def test_dom::assignmentstatement_constructor_args():
    sig = inspect.signature(dom::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())



def test_primitiveexpression_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExpression)


def test_primitiveexpression_constructor_exists():
    assert callable(PrimitiveExpression.__init__)


def test_primitiveexpression_constructor_args():
    sig = inspect.signature(PrimitiveExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::realexpression_is_not_abstract():
    assert not inspect.isabstract(dom::RealExpression)


def test_dom::realexpression_constructor_exists():
    assert callable(dom::RealExpression.__init__)


def test_dom::realexpression_constructor_args():
    sig = inspect.signature(dom::RealExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom::realexpression_has_val():
    assert hasattr(dom::RealExpression, "val")
    descriptor = None
    for klass in dom::RealExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom::booleanexpression_is_not_abstract():
    assert not inspect.isabstract(dom::BooleanExpression)


def test_dom::booleanexpression_constructor_exists():
    assert callable(dom::BooleanExpression.__init__)


def test_dom::booleanexpression_constructor_args():
    sig = inspect.signature(dom::BooleanExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom::booleanexpression_has_val():
    assert hasattr(dom::BooleanExpression, "val")
    descriptor = None
    for klass in dom::BooleanExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryOperatorExpression)


def test_binaryoperatorexpression_constructor_exists():
    assert callable(BinaryOperatorExpression.__init__)


def test_binaryoperatorexpression_constructor_args():
    sig = inspect.signature(BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::xoroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::XorOperatorExpression)


def test_dom::xoroperatorexpression_constructor_exists():
    assert callable(dom::XorOperatorExpression.__init__)


def test_dom::xoroperatorexpression_constructor_args():
    sig = inspect.signature(dom::XorOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::divideoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::DivideOperatorExpression)


def test_dom::divideoperatorexpression_constructor_exists():
    assert callable(dom::DivideOperatorExpression.__init__)


def test_dom::divideoperatorexpression_constructor_args():
    sig = inspect.signature(dom::DivideOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::oroperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::OrOperatorExpression)


def test_dom::oroperatorexpression_constructor_exists():
    assert callable(dom::OrOperatorExpression.__init__)


def test_dom::oroperatorexpression_constructor_args():
    sig = inspect.signature(dom::OrOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::plusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::PlusOperatorExpression)


def test_dom::plusoperatorexpression_constructor_exists():
    assert callable(dom::PlusOperatorExpression.__init__)


def test_dom::plusoperatorexpression_constructor_args():
    sig = inspect.signature(dom::PlusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::notequalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NotEqualsOperatorExpression)


def test_dom::notequalsoperatorexpression_constructor_exists():
    assert callable(dom::NotEqualsOperatorExpression.__init__)


def test_dom::notequalsoperatorexpression_constructor_args():
    sig = inspect.signature(dom::NotEqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::andoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::AndOperatorExpression)


def test_dom::andoperatorexpression_constructor_exists():
    assert callable(dom::AndOperatorExpression.__init__)


def test_dom::andoperatorexpression_constructor_args():
    sig = inspect.signature(dom::AndOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_operatorexpression_is_not_abstract():
    assert not inspect.isabstract(OperatorExpression)


def test_operatorexpression_constructor_exists():
    assert callable(OperatorExpression.__init__)


def test_operatorexpression_constructor_args():
    sig = inspect.signature(OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::unaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::UnaryOperatorExpression)


def test_dom::unaryoperatorexpression_constructor_exists():
    assert callable(dom::UnaryOperatorExpression.__init__)


def test_dom::unaryoperatorexpression_constructor_args():
    sig = inspect.signature(dom::UnaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::binaryoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::BinaryOperatorExpression)


def test_dom::binaryoperatorexpression_constructor_exists():
    assert callable(dom::BinaryOperatorExpression.__init__)


def test_dom::binaryoperatorexpression_constructor_args():
    sig = inspect.signature(dom::BinaryOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::variabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(dom::VariableDeclarationExpression)


def test_dom::variabledeclarationexpression_constructor_exists():
    assert callable(dom::VariableDeclarationExpression.__init__)


def test_dom::variabledeclarationexpression_constructor_args():
    sig = inspect.signature(dom::VariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::enumerationliteralexpression_is_not_abstract():
    assert not inspect.isabstract(dom::EnumerationLiteralExpression)


def test_dom::enumerationliteralexpression_constructor_exists():
    assert callable(dom::EnumerationLiteralExpression.__init__)


def test_dom::enumerationliteralexpression_constructor_args():
    sig = inspect.signature(dom::EnumerationLiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::newexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NewExpression)


def test_dom::newexpression_constructor_exists():
    assert callable(dom::NewExpression.__init__)


def test_dom::newexpression_constructor_args():
    sig = inspect.signature(dom::NewExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::modelelementtypeexpression_is_not_abstract():
    assert not inspect.isabstract(dom::ModelElementTypeExpression)


def test_dom::modelelementtypeexpression_constructor_exists():
    assert callable(dom::ModelElementTypeExpression.__init__)


def test_dom::modelelementtypeexpression_constructor_args():
    sig = inspect.signature(dom::ModelElementTypeExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::literalexpression_is_not_abstract():
    assert not inspect.isabstract(dom::LiteralExpression)


def test_dom::literalexpression_constructor_exists():
    assert callable(dom::LiteralExpression.__init__)


def test_dom::literalexpression_constructor_args():
    sig = inspect.signature(dom::LiteralExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::formalparameterexpression_is_not_abstract():
    assert not inspect.isabstract(dom::FormalParameterExpression)


def test_dom::formalparameterexpression_constructor_exists():
    assert callable(dom::FormalParameterExpression.__init__)


def test_dom::formalparameterexpression_constructor_args():
    sig = inspect.signature(dom::FormalParameterExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::operatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::OperatorExpression)


def test_dom::operatorexpression_constructor_exists():
    assert callable(dom::OperatorExpression.__init__)


def test_dom::operatorexpression_constructor_args():
    sig = inspect.signature(dom::OperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::multiplyoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::MultiplyOperatorExpression)


def test_dom::multiplyoperatorexpression_constructor_exists():
    assert callable(dom::MultiplyOperatorExpression.__init__)


def test_dom::multiplyoperatorexpression_constructor_args():
    sig = inspect.signature(dom::MultiplyOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::minusoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::MinusOperatorExpression)


def test_dom::minusoperatorexpression_constructor_exists():
    assert callable(dom::MinusOperatorExpression.__init__)


def test_dom::minusoperatorexpression_constructor_args():
    sig = inspect.signature(dom::MinusOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(FeatureCallExpression)


def test_featurecallexpression_constructor_exists():
    assert callable(FeatureCallExpression.__init__)


def test_featurecallexpression_constructor_args():
    sig = inspect.signature(FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::propertycallexpression_is_not_abstract():
    assert not inspect.isabstract(dom::PropertyCallExpression)


def test_dom::propertycallexpression_constructor_exists():
    assert callable(dom::PropertyCallExpression.__init__)


def test_dom::propertycallexpression_constructor_args():
    sig = inspect.signature(dom::PropertyCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::folmethodcallexpression_is_not_abstract():
    assert not inspect.isabstract(dom::FOLMethodCallExpression)


def test_dom::folmethodcallexpression_constructor_exists():
    assert callable(dom::FOLMethodCallExpression.__init__)


def test_dom::folmethodcallexpression_constructor_args():
    sig = inspect.signature(dom::FOLMethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::methodcallexpression_is_not_abstract():
    assert not inspect.isabstract(dom::MethodCallExpression)


def test_dom::methodcallexpression_constructor_exists():
    assert callable(dom::MethodCallExpression.__init__)


def test_dom::methodcallexpression_constructor_args():
    sig = inspect.signature(dom::MethodCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::lessthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::LessThanOrEqualToOperatorExpression)


def test_dom::lessthanorequaltooperatorexpression_constructor_exists():
    assert callable(dom::LessThanOrEqualToOperatorExpression.__init__)


def test_dom::lessthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(dom::LessThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::lessthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::LessThanOperatorExpression)


def test_dom::lessthanoperatorexpression_constructor_exists():
    assert callable(dom::LessThanOperatorExpression.__init__)


def test_dom::lessthanoperatorexpression_constructor_args():
    sig = inspect.signature(dom::LessThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::integerexpression_is_not_abstract():
    assert not inspect.isabstract(dom::IntegerExpression)


def test_dom::integerexpression_constructor_exists():
    assert callable(dom::IntegerExpression.__init__)


def test_dom::integerexpression_constructor_args():
    sig = inspect.signature(dom::IntegerExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom::integerexpression_has_val():
    assert hasattr(dom::IntegerExpression, "val")
    descriptor = None
    for klass in dom::IntegerExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom::impliesoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::ImpliesOperatorExpression)


def test_dom::impliesoperatorexpression_constructor_exists():
    assert callable(dom::ImpliesOperatorExpression.__init__)


def test_dom::impliesoperatorexpression_constructor_args():
    sig = inspect.signature(dom::ImpliesOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::greaterthanorequaltooperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::GreaterThanOrEqualToOperatorExpression)


def test_dom::greaterthanorequaltooperatorexpression_constructor_exists():
    assert callable(dom::GreaterThanOrEqualToOperatorExpression.__init__)


def test_dom::greaterthanorequaltooperatorexpression_constructor_args():
    sig = inspect.signature(dom::GreaterThanOrEqualToOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::greaterthanoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::GreaterThanOperatorExpression)


def test_dom::greaterthanoperatorexpression_constructor_exists():
    assert callable(dom::GreaterThanOperatorExpression.__init__)


def test_dom::greaterthanoperatorexpression_constructor_args():
    sig = inspect.signature(dom::GreaterThanOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::featurecallexpression_is_not_abstract():
    assert not inspect.isabstract(dom::FeatureCallExpression)


def test_dom::featurecallexpression_constructor_exists():
    assert callable(dom::FeatureCallExpression.__init__)


def test_dom::featurecallexpression_constructor_args():
    sig = inspect.signature(dom::FeatureCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::equalsoperatorexpression_is_not_abstract():
    assert not inspect.isabstract(dom::EqualsOperatorExpression)


def test_dom::equalsoperatorexpression_constructor_exists():
    assert callable(dom::EqualsOperatorExpression.__init__)


def test_dom::equalsoperatorexpression_constructor_args():
    sig = inspect.signature(dom::EqualsOperatorExpression.__init__)
    params = list(sig.parameters.keys())



def test_dom::domelement_is_not_abstract():
    assert not inspect.isabstract(dom::DomElement)


def test_dom::domelement_constructor_exists():
    assert callable(dom::DomElement.__init__)


def test_dom::domelement_constructor_args():
    sig = inspect.signature(dom::DomElement.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "line" in params, "Missing parameter 'line'"

def test_dom::domelement_has_column():
    assert hasattr(dom::DomElement, "column")
    descriptor = None
    for klass in dom::DomElement.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_dom::domelement_has_line():
    assert hasattr(dom::DomElement, "line")
    descriptor = None
    for klass in dom::DomElement.__mro__:
        if "line" in klass.__dict__:
            descriptor = klass.__dict__["line"]
            break
    assert isinstance(descriptor, property)



def test_dom::stringexpression_is_not_abstract():
    assert not inspect.isabstract(dom::StringExpression)


def test_dom::stringexpression_constructor_exists():
    assert callable(dom::StringExpression.__init__)


def test_dom::stringexpression_constructor_args():
    sig = inspect.signature(dom::StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_dom::stringexpression_has_val():
    assert hasattr(dom::StringExpression, "val")
    descriptor = None
    for klass in dom::StringExpression.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_dom::modeldeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(dom::ModelDeclarationStatement)


def test_dom::modeldeclarationstatement_constructor_exists():
    assert callable(dom::ModelDeclarationStatement.__init__)


def test_dom::modeldeclarationstatement_constructor_args():
    sig = inspect.signature(dom::ModelDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_dom::nameexpression_is_not_abstract():
    assert not inspect.isabstract(dom::NameExpression)


def test_dom::nameexpression_constructor_exists():
    assert callable(dom::NameExpression.__init__)


def test_dom::nameexpression_constructor_args():
    sig = inspect.signature(dom::NameExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dom::nameexpression_has_name():
    assert hasattr(dom::NameExpression, "name")
    descriptor = None
    for klass in dom::NameExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domelement_is_not_abstract():
    assert not inspect.isabstract(DomElement)


def test_domelement_constructor_exists():
    assert callable(DomElement.__init__)


def test_domelement_constructor_args():
    sig = inspect.signature(DomElement.__init__)
    params = list(sig.parameters.keys())



def test_dom::block_is_not_abstract():
    assert not inspect.isabstract(dom::Block)


def test_dom::block_constructor_exists():
    assert callable(dom::Block.__init__)


def test_dom::block_constructor_args():
    sig = inspect.signature(dom::Block.__init__)
    params = list(sig.parameters.keys())



def test_dom::type_is_not_abstract():
    assert not inspect.isabstract(dom::Type)


def test_dom::type_constructor_exists():
    assert callable(dom::Type.__init__)


def test_dom::type_constructor_args():
    sig = inspect.signature(dom::Type.__init__)
    params = list(sig.parameters.keys())



def test_dom::operationdefinition_is_not_abstract():
    assert not inspect.isabstract(dom::OperationDefinition)


def test_dom::operationdefinition_constructor_exists():
    assert callable(dom::OperationDefinition.__init__)


def test_dom::operationdefinition_constructor_args():
    sig = inspect.signature(dom::OperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_dom::import_is_not_abstract():
    assert not inspect.isabstract(dom::Import)


def test_dom::import_constructor_exists():
    assert callable(dom::Import.__init__)


def test_dom::import_constructor_args():
    sig = inspect.signature(dom::Import.__init__)
    params = list(sig.parameters.keys())



def test_dom::collectioninitvalue_is_not_abstract():
    assert not inspect.isabstract(dom::CollectionInitValue)


def test_dom::collectioninitvalue_constructor_exists():
    assert callable(dom::CollectionInitValue.__init__)


def test_dom::collectioninitvalue_constructor_args():
    sig = inspect.signature(dom::CollectionInitValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::statement_is_not_abstract():
    assert not inspect.isabstract(dom::Statement)


def test_dom::statement_constructor_exists():
    assert callable(dom::Statement.__init__)


def test_dom::statement_constructor_args():
    sig = inspect.signature(dom::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dom::expression_is_not_abstract():
    assert not inspect.isabstract(dom::Expression)


def test_dom::expression_constructor_exists():
    assert callable(dom::Expression.__init__)


def test_dom::expression_constructor_args():
    sig = inspect.signature(dom::Expression.__init__)
    params = list(sig.parameters.keys())



def test_dom::keyvalue_is_not_abstract():
    assert not inspect.isabstract(dom::KeyValue)


def test_dom::keyvalue_constructor_exists():
    assert callable(dom::KeyValue.__init__)


def test_dom::keyvalue_constructor_args():
    sig = inspect.signature(dom::KeyValue.__init__)
    params = list(sig.parameters.keys())



def test_dom::modeldeclarationparameter_is_not_abstract():
    assert not inspect.isabstract(dom::ModelDeclarationParameter)


def test_dom::modeldeclarationparameter_constructor_exists():
    assert callable(dom::ModelDeclarationParameter.__init__)


def test_dom::modeldeclarationparameter_constructor_args():
    sig = inspect.signature(dom::ModelDeclarationParameter.__init__)
    params = list(sig.parameters.keys())



def test_dom::annotation_is_not_abstract():
    assert not inspect.isabstract(dom::Annotation)


def test_dom::annotation_constructor_exists():
    assert callable(dom::Annotation.__init__)


def test_dom::annotation_constructor_args():
    sig = inspect.signature(dom::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_dom::annotationblock_is_not_abstract():
    assert not inspect.isabstract(dom::AnnotationBlock)


def test_dom::annotationblock_constructor_exists():
    assert callable(dom::AnnotationBlock.__init__)


def test_dom::annotationblock_constructor_args():
    sig = inspect.signature(dom::AnnotationBlock.__init__)
    params = list(sig.parameters.keys())



def test_dom::program_is_not_abstract():
    assert not inspect.isabstract(dom::Program)


def test_dom::program_constructor_exists():
    assert callable(dom::Program.__init__)


def test_dom::program_constructor_args():
    sig = inspect.signature(dom::Program.__init__)
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
CollectionInitValue_strategy = st.builds(
    CollectionInitValue,
)
dom::ExpRange_strategy = st.builds(
    dom::ExpRange,
)
dom::ExprList_strategy = st.builds(
    dom::ExprList,
)
AssignmentStatement_strategy = st.builds(
    AssignmentStatement,
)
dom::SpecialAssignmentStatement_strategy = st.builds(
    dom::SpecialAssignmentStatement,
)
NameExpression_strategy = st.builds(
    NameExpression,
)
dom::SpecialNameExpression_strategy = st.builds(
    dom::SpecialNameExpression,
)
Annotation_strategy = st.builds(
    Annotation,
)
dom::SimpleAnnotation_strategy = st.builds(
    dom::SimpleAnnotation,
)
dom::ModelExpression_strategy = st.builds(
    dom::ModelExpression,
)
dom::ShortModelDeclarationExpression_strategy = st.builds(
    dom::ShortModelDeclarationExpression,
)
SwitchCaseStatement_strategy = st.builds(
    SwitchCaseStatement,
)
dom::ExecutableAnnotation_strategy = st.builds(
    dom::ExecutableAnnotation,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
dom::BagType_strategy = st.builds(
    dom::BagType,
)
dom::SequenceType_strategy = st.builds(
    dom::SequenceType,
)
dom::OrderedSetType_strategy = st.builds(
    dom::OrderedSetType,
)
dom::SetType_strategy = st.builds(
    dom::SetType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
dom::RealType_strategy = st.builds(
    dom::RealType,
)
dom::IntegerType_strategy = st.builds(
    dom::IntegerType,
)
dom::StringType_strategy = st.builds(
    dom::StringType,
)
dom::BooleanType_strategy = st.builds(
    dom::BooleanType,
)
Type_strategy = st.builds(
    Type,
)
dom::ModelElementType_strategy = st.builds(
    dom::ModelElementType,
)
dom::CollectionType_strategy = st.builds(
    dom::CollectionType,
)
dom::NativeType_strategy = st.builds(
    dom::NativeType,
)
dom::PrimitiveType_strategy = st.builds(
    dom::PrimitiveType,
)
dom::MapType_strategy = st.builds(
    dom::MapType,
)
dom::AnyType_strategy = st.builds(
    dom::AnyType,
)
CollectionExpression_strategy = st.builds(
    CollectionExpression,
)
dom::SequenceExpression_strategy = st.builds(
    dom::SequenceExpression,
)
dom::OrderedSetExpression_strategy = st.builds(
    dom::OrderedSetExpression,
)
dom::BagExpression_strategy = st.builds(
    dom::BagExpression,
)
dom::SetExpression_strategy = st.builds(
    dom::SetExpression,
)
LiteralExpression_strategy = st.builds(
    LiteralExpression,
)
dom::CollectionExpression_strategy = st.builds(
    dom::CollectionExpression,
)
dom::MapExpression_strategy = st.builds(
    dom::MapExpression,
)
dom::PrimitiveExpression_strategy = st.builds(
    dom::PrimitiveExpression,
)
dom::SwitchCaseDefaultStatement_strategy = st.builds(
    dom::SwitchCaseDefaultStatement,
)
dom::SwitchCaseExpressionStatement_strategy = st.builds(
    dom::SwitchCaseExpressionStatement,
)
UnaryOperatorExpression_strategy = st.builds(
    UnaryOperatorExpression,
)
dom::NotOperatorExpression_strategy = st.builds(
    dom::NotOperatorExpression,
)
dom::NegativeOperatorExpression_strategy = st.builds(
    dom::NegativeOperatorExpression,
)
Statement_strategy = st.builds(
    Statement,
)
dom::TransactionStatement_strategy = st.builds(
    dom::TransactionStatement,
)
dom::ReturnStatement_strategy = st.builds(
    dom::ReturnStatement,
)
dom::ForStatement_strategy = st.builds(
    dom::ForStatement,
)
dom::ContinueStatement_strategy = st.builds(
    dom::ContinueStatement,
)
dom::SwitchCaseStatement_strategy = st.builds(
    dom::SwitchCaseStatement,
)
dom::BreakAllStatement_strategy = st.builds(
    dom::BreakAllStatement,
)
dom::ThrowStatement_strategy = st.builds(
    dom::ThrowStatement,
)
dom::ExpressionStatement_strategy = st.builds(
    dom::ExpressionStatement,
)
dom::IfStatement_strategy = st.builds(
    dom::IfStatement,
)
dom::BreakStatement_strategy = st.builds(
    dom::BreakStatement,
)
dom::AbortStatement_strategy = st.builds(
    dom::AbortStatement,
)
dom::WhileStatement_strategy = st.builds(
    dom::WhileStatement,
)
dom::SwitchStatement_strategy = st.builds(
    dom::SwitchStatement,
)
dom::DeleteStatement_strategy = st.builds(
    dom::DeleteStatement,
)
dom::AssignmentStatement_strategy = st.builds(
    dom::AssignmentStatement,
)
PrimitiveExpression_strategy = st.builds(
    PrimitiveExpression,
)
dom::RealExpression_strategy = st.builds(
    dom::RealExpression,
    val=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
dom::BooleanExpression_strategy = st.builds(
    dom::BooleanExpression,
    val=
        st.booleans()
)
BinaryOperatorExpression_strategy = st.builds(
    BinaryOperatorExpression,
)
dom::XorOperatorExpression_strategy = st.builds(
    dom::XorOperatorExpression,
)
dom::DivideOperatorExpression_strategy = st.builds(
    dom::DivideOperatorExpression,
)
dom::OrOperatorExpression_strategy = st.builds(
    dom::OrOperatorExpression,
)
dom::PlusOperatorExpression_strategy = st.builds(
    dom::PlusOperatorExpression,
)
dom::NotEqualsOperatorExpression_strategy = st.builds(
    dom::NotEqualsOperatorExpression,
)
dom::AndOperatorExpression_strategy = st.builds(
    dom::AndOperatorExpression,
)
OperatorExpression_strategy = st.builds(
    OperatorExpression,
)
dom::UnaryOperatorExpression_strategy = st.builds(
    dom::UnaryOperatorExpression,
)
dom::BinaryOperatorExpression_strategy = st.builds(
    dom::BinaryOperatorExpression,
)
Expression_strategy = st.builds(
    Expression,
)
dom::VariableDeclarationExpression_strategy = st.builds(
    dom::VariableDeclarationExpression,
)
dom::EnumerationLiteralExpression_strategy = st.builds(
    dom::EnumerationLiteralExpression,
)
dom::NewExpression_strategy = st.builds(
    dom::NewExpression,
)
dom::ModelElementTypeExpression_strategy = st.builds(
    dom::ModelElementTypeExpression,
)
dom::LiteralExpression_strategy = st.builds(
    dom::LiteralExpression,
)
dom::FormalParameterExpression_strategy = st.builds(
    dom::FormalParameterExpression,
)
dom::OperatorExpression_strategy = st.builds(
    dom::OperatorExpression,
)
dom::MultiplyOperatorExpression_strategy = st.builds(
    dom::MultiplyOperatorExpression,
)
dom::MinusOperatorExpression_strategy = st.builds(
    dom::MinusOperatorExpression,
)
FeatureCallExpression_strategy = st.builds(
    FeatureCallExpression,
)
dom::PropertyCallExpression_strategy = st.builds(
    dom::PropertyCallExpression,
)
dom::FOLMethodCallExpression_strategy = st.builds(
    dom::FOLMethodCallExpression,
)
dom::MethodCallExpression_strategy = st.builds(
    dom::MethodCallExpression,
)
dom::LessThanOrEqualToOperatorExpression_strategy = st.builds(
    dom::LessThanOrEqualToOperatorExpression,
)
dom::LessThanOperatorExpression_strategy = st.builds(
    dom::LessThanOperatorExpression,
)
dom::IntegerExpression_strategy = st.builds(
    dom::IntegerExpression,
    val=
        st.integers()
)
dom::ImpliesOperatorExpression_strategy = st.builds(
    dom::ImpliesOperatorExpression,
)
dom::GreaterThanOrEqualToOperatorExpression_strategy = st.builds(
    dom::GreaterThanOrEqualToOperatorExpression,
)
dom::GreaterThanOperatorExpression_strategy = st.builds(
    dom::GreaterThanOperatorExpression,
)
dom::FeatureCallExpression_strategy = st.builds(
    dom::FeatureCallExpression,
)
dom::EqualsOperatorExpression_strategy = st.builds(
    dom::EqualsOperatorExpression,
)
dom::DomElement_strategy = st.builds(
    dom::DomElement,
    column=
        st.integers(),
    line=
        st.integers()
)
dom::StringExpression_strategy = st.builds(
    dom::StringExpression,
    val=
        safe_text
)
dom::ModelDeclarationStatement_strategy = st.builds(
    dom::ModelDeclarationStatement,
)
dom::NameExpression_strategy = st.builds(
    dom::NameExpression,
    name=
        safe_text
)
DomElement_strategy = st.builds(
    DomElement,
)
dom::Block_strategy = st.builds(
    dom::Block,
)
dom::Type_strategy = st.builds(
    dom::Type,
)
dom::OperationDefinition_strategy = st.builds(
    dom::OperationDefinition,
)
dom::Import_strategy = st.builds(
    dom::Import,
)
dom::CollectionInitValue_strategy = st.builds(
    dom::CollectionInitValue,
)
dom::Statement_strategy = st.builds(
    dom::Statement,
)
dom::Expression_strategy = st.builds(
    dom::Expression,
)
dom::KeyValue_strategy = st.builds(
    dom::KeyValue,
)
dom::ModelDeclarationParameter_strategy = st.builds(
    dom::ModelDeclarationParameter,
)
dom::Annotation_strategy = st.builds(
    dom::Annotation,
)
dom::AnnotationBlock_strategy = st.builds(
    dom::AnnotationBlock,
)
dom::Program_strategy = st.builds(
    dom::Program,
)

@given(instance=CollectionInitValue_strategy)
@settings(max_examples=50)
def test_collectioninitvalue_instantiation(instance):
    assert isinstance(instance, CollectionInitValue)

@given(instance=dom::ExpRange_strategy)
@settings(max_examples=50)
def test_dom::exprange_instantiation(instance):
    assert isinstance(instance, dom::ExpRange)

@given(instance=dom::ExprList_strategy)
@settings(max_examples=50)
def test_dom::exprlist_instantiation(instance):
    assert isinstance(instance, dom::ExprList)

@given(instance=AssignmentStatement_strategy)
@settings(max_examples=50)
def test_assignmentstatement_instantiation(instance):
    assert isinstance(instance, AssignmentStatement)

@given(instance=dom::SpecialAssignmentStatement_strategy)
@settings(max_examples=50)
def test_dom::specialassignmentstatement_instantiation(instance):
    assert isinstance(instance, dom::SpecialAssignmentStatement)

@given(instance=NameExpression_strategy)
@settings(max_examples=50)
def test_nameexpression_instantiation(instance):
    assert isinstance(instance, NameExpression)

@given(instance=dom::SpecialNameExpression_strategy)
@settings(max_examples=50)
def test_dom::specialnameexpression_instantiation(instance):
    assert isinstance(instance, dom::SpecialNameExpression)

@given(instance=Annotation_strategy)
@settings(max_examples=50)
def test_annotation_instantiation(instance):
    assert isinstance(instance, Annotation)

@given(instance=dom::SimpleAnnotation_strategy)
@settings(max_examples=50)
def test_dom::simpleannotation_instantiation(instance):
    assert isinstance(instance, dom::SimpleAnnotation)

@given(instance=dom::ModelExpression_strategy)
@settings(max_examples=50)
def test_dom::modelexpression_instantiation(instance):
    assert isinstance(instance, dom::ModelExpression)

@given(instance=dom::ShortModelDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom::shortmodeldeclarationexpression_instantiation(instance):
    assert isinstance(instance, dom::ShortModelDeclarationExpression)

@given(instance=SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_switchcasestatement_instantiation(instance):
    assert isinstance(instance, SwitchCaseStatement)

@given(instance=dom::ExecutableAnnotation_strategy)
@settings(max_examples=50)
def test_dom::executableannotation_instantiation(instance):
    assert isinstance(instance, dom::ExecutableAnnotation)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=dom::BagType_strategy)
@settings(max_examples=50)
def test_dom::bagtype_instantiation(instance):
    assert isinstance(instance, dom::BagType)

@given(instance=dom::SequenceType_strategy)
@settings(max_examples=50)
def test_dom::sequencetype_instantiation(instance):
    assert isinstance(instance, dom::SequenceType)

@given(instance=dom::OrderedSetType_strategy)
@settings(max_examples=50)
def test_dom::orderedsettype_instantiation(instance):
    assert isinstance(instance, dom::OrderedSetType)

@given(instance=dom::SetType_strategy)
@settings(max_examples=50)
def test_dom::settype_instantiation(instance):
    assert isinstance(instance, dom::SetType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=dom::RealType_strategy)
@settings(max_examples=50)
def test_dom::realtype_instantiation(instance):
    assert isinstance(instance, dom::RealType)

@given(instance=dom::IntegerType_strategy)
@settings(max_examples=50)
def test_dom::integertype_instantiation(instance):
    assert isinstance(instance, dom::IntegerType)

@given(instance=dom::StringType_strategy)
@settings(max_examples=50)
def test_dom::stringtype_instantiation(instance):
    assert isinstance(instance, dom::StringType)

@given(instance=dom::BooleanType_strategy)
@settings(max_examples=50)
def test_dom::booleantype_instantiation(instance):
    assert isinstance(instance, dom::BooleanType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dom::ModelElementType_strategy)
@settings(max_examples=50)
def test_dom::modelelementtype_instantiation(instance):
    assert isinstance(instance, dom::ModelElementType)

@given(instance=dom::CollectionType_strategy)
@settings(max_examples=50)
def test_dom::collectiontype_instantiation(instance):
    assert isinstance(instance, dom::CollectionType)

@given(instance=dom::NativeType_strategy)
@settings(max_examples=50)
def test_dom::nativetype_instantiation(instance):
    assert isinstance(instance, dom::NativeType)

@given(instance=dom::PrimitiveType_strategy)
@settings(max_examples=50)
def test_dom::primitivetype_instantiation(instance):
    assert isinstance(instance, dom::PrimitiveType)

@given(instance=dom::MapType_strategy)
@settings(max_examples=50)
def test_dom::maptype_instantiation(instance):
    assert isinstance(instance, dom::MapType)

@given(instance=dom::AnyType_strategy)
@settings(max_examples=50)
def test_dom::anytype_instantiation(instance):
    assert isinstance(instance, dom::AnyType)

@given(instance=CollectionExpression_strategy)
@settings(max_examples=50)
def test_collectionexpression_instantiation(instance):
    assert isinstance(instance, CollectionExpression)

@given(instance=dom::SequenceExpression_strategy)
@settings(max_examples=50)
def test_dom::sequenceexpression_instantiation(instance):
    assert isinstance(instance, dom::SequenceExpression)

@given(instance=dom::OrderedSetExpression_strategy)
@settings(max_examples=50)
def test_dom::orderedsetexpression_instantiation(instance):
    assert isinstance(instance, dom::OrderedSetExpression)

@given(instance=dom::BagExpression_strategy)
@settings(max_examples=50)
def test_dom::bagexpression_instantiation(instance):
    assert isinstance(instance, dom::BagExpression)

@given(instance=dom::SetExpression_strategy)
@settings(max_examples=50)
def test_dom::setexpression_instantiation(instance):
    assert isinstance(instance, dom::SetExpression)

@given(instance=LiteralExpression_strategy)
@settings(max_examples=50)
def test_literalexpression_instantiation(instance):
    assert isinstance(instance, LiteralExpression)

@given(instance=dom::CollectionExpression_strategy)
@settings(max_examples=50)
def test_dom::collectionexpression_instantiation(instance):
    assert isinstance(instance, dom::CollectionExpression)

@given(instance=dom::MapExpression_strategy)
@settings(max_examples=50)
def test_dom::mapexpression_instantiation(instance):
    assert isinstance(instance, dom::MapExpression)

@given(instance=dom::PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_dom::primitiveexpression_instantiation(instance):
    assert isinstance(instance, dom::PrimitiveExpression)

@given(instance=dom::SwitchCaseDefaultStatement_strategy)
@settings(max_examples=50)
def test_dom::switchcasedefaultstatement_instantiation(instance):
    assert isinstance(instance, dom::SwitchCaseDefaultStatement)

@given(instance=dom::SwitchCaseExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom::switchcaseexpressionstatement_instantiation(instance):
    assert isinstance(instance, dom::SwitchCaseExpressionStatement)

@given(instance=UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, UnaryOperatorExpression)

@given(instance=dom::NotOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::notoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::NotOperatorExpression)

@given(instance=dom::NegativeOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::negativeoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::NegativeOperatorExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dom::TransactionStatement_strategy)
@settings(max_examples=50)
def test_dom::transactionstatement_instantiation(instance):
    assert isinstance(instance, dom::TransactionStatement)

@given(instance=dom::ReturnStatement_strategy)
@settings(max_examples=50)
def test_dom::returnstatement_instantiation(instance):
    assert isinstance(instance, dom::ReturnStatement)

@given(instance=dom::ForStatement_strategy)
@settings(max_examples=50)
def test_dom::forstatement_instantiation(instance):
    assert isinstance(instance, dom::ForStatement)

@given(instance=dom::ContinueStatement_strategy)
@settings(max_examples=50)
def test_dom::continuestatement_instantiation(instance):
    assert isinstance(instance, dom::ContinueStatement)

@given(instance=dom::SwitchCaseStatement_strategy)
@settings(max_examples=50)
def test_dom::switchcasestatement_instantiation(instance):
    assert isinstance(instance, dom::SwitchCaseStatement)

@given(instance=dom::BreakAllStatement_strategy)
@settings(max_examples=50)
def test_dom::breakallstatement_instantiation(instance):
    assert isinstance(instance, dom::BreakAllStatement)

@given(instance=dom::ThrowStatement_strategy)
@settings(max_examples=50)
def test_dom::throwstatement_instantiation(instance):
    assert isinstance(instance, dom::ThrowStatement)

@given(instance=dom::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_dom::expressionstatement_instantiation(instance):
    assert isinstance(instance, dom::ExpressionStatement)

@given(instance=dom::IfStatement_strategy)
@settings(max_examples=50)
def test_dom::ifstatement_instantiation(instance):
    assert isinstance(instance, dom::IfStatement)

@given(instance=dom::BreakStatement_strategy)
@settings(max_examples=50)
def test_dom::breakstatement_instantiation(instance):
    assert isinstance(instance, dom::BreakStatement)

@given(instance=dom::AbortStatement_strategy)
@settings(max_examples=50)
def test_dom::abortstatement_instantiation(instance):
    assert isinstance(instance, dom::AbortStatement)

@given(instance=dom::WhileStatement_strategy)
@settings(max_examples=50)
def test_dom::whilestatement_instantiation(instance):
    assert isinstance(instance, dom::WhileStatement)

@given(instance=dom::SwitchStatement_strategy)
@settings(max_examples=50)
def test_dom::switchstatement_instantiation(instance):
    assert isinstance(instance, dom::SwitchStatement)

@given(instance=dom::DeleteStatement_strategy)
@settings(max_examples=50)
def test_dom::deletestatement_instantiation(instance):
    assert isinstance(instance, dom::DeleteStatement)

@given(instance=dom::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_dom::assignmentstatement_instantiation(instance):
    assert isinstance(instance, dom::AssignmentStatement)

@given(instance=PrimitiveExpression_strategy)
@settings(max_examples=50)
def test_primitiveexpression_instantiation(instance):
    assert isinstance(instance, PrimitiveExpression)

@given(instance=dom::RealExpression_strategy)
@settings(max_examples=50)
def test_dom::realexpression_instantiation(instance):
    assert isinstance(instance, dom::RealExpression)

@given(instance=dom::RealExpression_strategy)
def test_dom::realexpression_val_type(instance):
    assert isinstance(instance.val, float)


@given(instance=dom::RealExpression_strategy)
def test_dom::realexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom::BooleanExpression_strategy)
@settings(max_examples=50)
def test_dom::booleanexpression_instantiation(instance):
    assert isinstance(instance, dom::BooleanExpression)

@given(instance=dom::BooleanExpression_strategy)
def test_dom::booleanexpression_val_type(instance):
    assert isinstance(instance.val, bool)


@given(instance=dom::BooleanExpression_strategy)
def test_dom::booleanexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, BinaryOperatorExpression)

@given(instance=dom::XorOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::xoroperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::XorOperatorExpression)

@given(instance=dom::DivideOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::divideoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::DivideOperatorExpression)

@given(instance=dom::OrOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::oroperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::OrOperatorExpression)

@given(instance=dom::PlusOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::plusoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::PlusOperatorExpression)

@given(instance=dom::NotEqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::notequalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::NotEqualsOperatorExpression)

@given(instance=dom::AndOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::andoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::AndOperatorExpression)

@given(instance=OperatorExpression_strategy)
@settings(max_examples=50)
def test_operatorexpression_instantiation(instance):
    assert isinstance(instance, OperatorExpression)

@given(instance=dom::UnaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::unaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::UnaryOperatorExpression)

@given(instance=dom::BinaryOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::binaryoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::BinaryOperatorExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dom::VariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_dom::variabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, dom::VariableDeclarationExpression)

@given(instance=dom::EnumerationLiteralExpression_strategy)
@settings(max_examples=50)
def test_dom::enumerationliteralexpression_instantiation(instance):
    assert isinstance(instance, dom::EnumerationLiteralExpression)

@given(instance=dom::NewExpression_strategy)
@settings(max_examples=50)
def test_dom::newexpression_instantiation(instance):
    assert isinstance(instance, dom::NewExpression)

@given(instance=dom::ModelElementTypeExpression_strategy)
@settings(max_examples=50)
def test_dom::modelelementtypeexpression_instantiation(instance):
    assert isinstance(instance, dom::ModelElementTypeExpression)

@given(instance=dom::LiteralExpression_strategy)
@settings(max_examples=50)
def test_dom::literalexpression_instantiation(instance):
    assert isinstance(instance, dom::LiteralExpression)

@given(instance=dom::FormalParameterExpression_strategy)
@settings(max_examples=50)
def test_dom::formalparameterexpression_instantiation(instance):
    assert isinstance(instance, dom::FormalParameterExpression)

@given(instance=dom::OperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::operatorexpression_instantiation(instance):
    assert isinstance(instance, dom::OperatorExpression)

@given(instance=dom::MultiplyOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::multiplyoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::MultiplyOperatorExpression)

@given(instance=dom::MinusOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::minusoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::MinusOperatorExpression)

@given(instance=FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_featurecallexpression_instantiation(instance):
    assert isinstance(instance, FeatureCallExpression)

@given(instance=dom::PropertyCallExpression_strategy)
@settings(max_examples=50)
def test_dom::propertycallexpression_instantiation(instance):
    assert isinstance(instance, dom::PropertyCallExpression)

@given(instance=dom::FOLMethodCallExpression_strategy)
@settings(max_examples=50)
def test_dom::folmethodcallexpression_instantiation(instance):
    assert isinstance(instance, dom::FOLMethodCallExpression)

@given(instance=dom::MethodCallExpression_strategy)
@settings(max_examples=50)
def test_dom::methodcallexpression_instantiation(instance):
    assert isinstance(instance, dom::MethodCallExpression)

@given(instance=dom::LessThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::lessthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::LessThanOrEqualToOperatorExpression)

@given(instance=dom::LessThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::lessthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::LessThanOperatorExpression)

@given(instance=dom::IntegerExpression_strategy)
@settings(max_examples=50)
def test_dom::integerexpression_instantiation(instance):
    assert isinstance(instance, dom::IntegerExpression)

@given(instance=dom::IntegerExpression_strategy)
def test_dom::integerexpression_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=dom::IntegerExpression_strategy)
def test_dom::integerexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom::ImpliesOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::impliesoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::ImpliesOperatorExpression)

@given(instance=dom::GreaterThanOrEqualToOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::greaterthanorequaltooperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::GreaterThanOrEqualToOperatorExpression)

@given(instance=dom::GreaterThanOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::greaterthanoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::GreaterThanOperatorExpression)

@given(instance=dom::FeatureCallExpression_strategy)
@settings(max_examples=50)
def test_dom::featurecallexpression_instantiation(instance):
    assert isinstance(instance, dom::FeatureCallExpression)

@given(instance=dom::EqualsOperatorExpression_strategy)
@settings(max_examples=50)
def test_dom::equalsoperatorexpression_instantiation(instance):
    assert isinstance(instance, dom::EqualsOperatorExpression)

@given(instance=dom::DomElement_strategy)
@settings(max_examples=50)
def test_dom::domelement_instantiation(instance):
    assert isinstance(instance, dom::DomElement)

@given(instance=dom::DomElement_strategy)
def test_dom::domelement_column_type(instance):
    assert isinstance(instance.column, int)


@given(instance=dom::DomElement_strategy)
def test_dom::domelement_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=dom::DomElement_strategy)
def test_dom::domelement_line_type(instance):
    assert isinstance(instance.line, int)


@given(instance=dom::DomElement_strategy)
def test_dom::domelement_line_setter(instance):
    original = instance.line
    instance.line = original
    assert instance.line == original

@given(instance=dom::StringExpression_strategy)
@settings(max_examples=50)
def test_dom::stringexpression_instantiation(instance):
    assert isinstance(instance, dom::StringExpression)

@given(instance=dom::StringExpression_strategy)
def test_dom::stringexpression_val_type(instance):
    assert isinstance(instance.val, str)


@given(instance=dom::StringExpression_strategy)
def test_dom::stringexpression_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=dom::ModelDeclarationStatement_strategy)
@settings(max_examples=50)
def test_dom::modeldeclarationstatement_instantiation(instance):
    assert isinstance(instance, dom::ModelDeclarationStatement)

@given(instance=dom::NameExpression_strategy)
@settings(max_examples=50)
def test_dom::nameexpression_instantiation(instance):
    assert isinstance(instance, dom::NameExpression)

@given(instance=dom::NameExpression_strategy)
def test_dom::nameexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dom::NameExpression_strategy)
def test_dom::nameexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DomElement_strategy)
@settings(max_examples=50)
def test_domelement_instantiation(instance):
    assert isinstance(instance, DomElement)

@given(instance=dom::Block_strategy)
@settings(max_examples=50)
def test_dom::block_instantiation(instance):
    assert isinstance(instance, dom::Block)

@given(instance=dom::Type_strategy)
@settings(max_examples=50)
def test_dom::type_instantiation(instance):
    assert isinstance(instance, dom::Type)

@given(instance=dom::OperationDefinition_strategy)
@settings(max_examples=50)
def test_dom::operationdefinition_instantiation(instance):
    assert isinstance(instance, dom::OperationDefinition)

@given(instance=dom::Import_strategy)
@settings(max_examples=50)
def test_dom::import_instantiation(instance):
    assert isinstance(instance, dom::Import)

@given(instance=dom::CollectionInitValue_strategy)
@settings(max_examples=50)
def test_dom::collectioninitvalue_instantiation(instance):
    assert isinstance(instance, dom::CollectionInitValue)

@given(instance=dom::Statement_strategy)
@settings(max_examples=50)
def test_dom::statement_instantiation(instance):
    assert isinstance(instance, dom::Statement)

@given(instance=dom::Expression_strategy)
@settings(max_examples=50)
def test_dom::expression_instantiation(instance):
    assert isinstance(instance, dom::Expression)

@given(instance=dom::KeyValue_strategy)
@settings(max_examples=50)
def test_dom::keyvalue_instantiation(instance):
    assert isinstance(instance, dom::KeyValue)

@given(instance=dom::ModelDeclarationParameter_strategy)
@settings(max_examples=50)
def test_dom::modeldeclarationparameter_instantiation(instance):
    assert isinstance(instance, dom::ModelDeclarationParameter)

@given(instance=dom::Annotation_strategy)
@settings(max_examples=50)
def test_dom::annotation_instantiation(instance):
    assert isinstance(instance, dom::Annotation)

@given(instance=dom::AnnotationBlock_strategy)
@settings(max_examples=50)
def test_dom::annotationblock_instantiation(instance):
    assert isinstance(instance, dom::AnnotationBlock)

@given(instance=dom::Program_strategy)
@settings(max_examples=50)
def test_dom::program_instantiation(instance):
    assert isinstance(instance, dom::Program)
