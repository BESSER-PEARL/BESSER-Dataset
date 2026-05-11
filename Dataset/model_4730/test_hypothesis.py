import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AggregateExpression,
    logiclanguage::ProjectedAggregateExpression,
    logiclanguage::Count,
    ProjectedAggregateExpression,
    logiclanguage::Max,
    logiclanguage::Min,
    logiclanguage::Sum,
    logiclanguage::AggregatedParameterSubstitution,
    Relation,
    logiclanguage::RelationDefinition,
    Constant,
    logiclanguage::ConstantDeclaration,
    logiclanguage::ConstantDefinition,
    logiclanguage::ConstantAnnotation,
    Function,
    logiclanguage::FunctionDeclaration,
    logiclanguage::FunctionDefinition,
    logiclanguage::RelationDeclaration,
    logiclanguage::RelationAnnotation,
    logiclanguage::AssertionAnnotation,
    logiclanguage::Assertion,
    logiclanguage::TermDescription,
    logiclanguage::TypeDescriptor,
    NumericOperation,
    logiclanguage::Divison,
    logiclanguage::Pow,
    logiclanguage::Multiply,
    logiclanguage::Minus,
    logiclanguage::Mod,
    logiclanguage::Plus,
    BoolOperation,
    logiclanguage::Iff,
    logiclanguage::Not,
    logiclanguage::Or,
    logiclanguage::Impl,
    logiclanguage::And,
    PrimitiveRelation,
    logiclanguage::LessThan,
    logiclanguage::MoreThan,
    logiclanguage::MoreOrEqualThan,
    logiclanguage::LessOrEqualThan,
    logiclanguage::Distinct,
    logiclanguage::Equals,
    Term,
    logiclanguage::TransitiveClosure,
    logiclanguage::AggregateExpression,
    logiclanguage::InstanceOf,
    logiclanguage::NumericOperation,
    logiclanguage::PrimitiveRelation,
    logiclanguage::BoolOperation,
    logiclanguage::UnknownBecauseUninterpreted,
    logiclanguage::IfThenElse,
    logiclanguage::SymbolicValue,
    TermDescription,
    logiclanguage::SymbolicDeclaration,
    logiclanguage::Term,
    logiclanguage::FunctionAnnotation,
    PrimitiveTypeReference,
    logiclanguage::StringTypeReference,
    logiclanguage::BoolTypeReference,
    logiclanguage::RealTypeReference,
    logiclanguage::IntTypeReference,
    QuantifiedExpression,
    logiclanguage::Forall,
    logiclanguage::Exists,
    logiclanguage::QuantifiedExpression,
    AtomicTerm,
    logiclanguage::StringLiteral,
    logiclanguage::BoolLiteral,
    logiclanguage::RealLiteral,
    logiclanguage::IntLiteral,
    logiclanguage::AtomicTerm,
    TypeDescriptor,
    logiclanguage::Type,
    TypeReference,
    logiclanguage::PrimitiveTypeReference,
    logiclanguage::ComplexTypeReference,
    logiclanguage::TypeReference,
    Type,
    logiclanguage::TypeDeclaration,
    logiclanguage::TypeDefinition,
    SymbolicDeclaration,
    logiclanguage::Function,
    logiclanguage::Relation,
    logiclanguage::Variable,
    logiclanguage::Constant,
    logiclanguage::DefinedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(AggregateExpression)


def test_aggregateexpression_constructor_exists():
    assert callable(AggregateExpression.__init__)


def test_aggregateexpression_constructor_args():
    sig = inspect.signature(AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::ProjectedAggregateExpression)


def test_logiclanguage::projectedaggregateexpression_constructor_exists():
    assert callable(logiclanguage::ProjectedAggregateExpression.__init__)


def test_logiclanguage::projectedaggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage::ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "projectionIndex" in params, "Missing parameter 'projectionIndex'"

def test_logiclanguage::projectedaggregateexpression_has_projectionIndex():
    assert hasattr(logiclanguage::ProjectedAggregateExpression, "projectionIndex")
    descriptor = None
    for klass in logiclanguage::ProjectedAggregateExpression.__mro__:
        if "projectionIndex" in klass.__dict__:
            descriptor = klass.__dict__["projectionIndex"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::count_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Count)


def test_logiclanguage::count_constructor_exists():
    assert callable(logiclanguage::Count.__init__)


def test_logiclanguage::count_constructor_args():
    sig = inspect.signature(logiclanguage::Count.__init__)
    params = list(sig.parameters.keys())



def test_projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(ProjectedAggregateExpression)


def test_projectedaggregateexpression_constructor_exists():
    assert callable(ProjectedAggregateExpression.__init__)


def test_projectedaggregateexpression_constructor_args():
    sig = inspect.signature(ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::max_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Max)


def test_logiclanguage::max_constructor_exists():
    assert callable(logiclanguage::Max.__init__)


def test_logiclanguage::max_constructor_args():
    sig = inspect.signature(logiclanguage::Max.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::min_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Min)


def test_logiclanguage::min_constructor_exists():
    assert callable(logiclanguage::Min.__init__)


def test_logiclanguage::min_constructor_args():
    sig = inspect.signature(logiclanguage::Min.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::sum_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Sum)


def test_logiclanguage::sum_constructor_exists():
    assert callable(logiclanguage::Sum.__init__)


def test_logiclanguage::sum_constructor_args():
    sig = inspect.signature(logiclanguage::Sum.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::aggregatedparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::AggregatedParameterSubstitution)


def test_logiclanguage::aggregatedparametersubstitution_constructor_exists():
    assert callable(logiclanguage::AggregatedParameterSubstitution.__init__)


def test_logiclanguage::aggregatedparametersubstitution_constructor_args():
    sig = inspect.signature(logiclanguage::AggregatedParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::relationdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::RelationDefinition)


def test_logiclanguage::relationdefinition_constructor_exists():
    assert callable(logiclanguage::RelationDefinition.__init__)


def test_logiclanguage::relationdefinition_constructor_args():
    sig = inspect.signature(logiclanguage::RelationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::ConstantDeclaration)


def test_logiclanguage::constantdeclaration_constructor_exists():
    assert callable(logiclanguage::ConstantDeclaration.__init__)


def test_logiclanguage::constantdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage::ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::constantdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::ConstantDefinition)


def test_logiclanguage::constantdefinition_constructor_exists():
    assert callable(logiclanguage::ConstantDefinition.__init__)


def test_logiclanguage::constantdefinition_constructor_args():
    sig = inspect.signature(logiclanguage::ConstantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::constantannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::ConstantAnnotation)


def test_logiclanguage::constantannotation_constructor_exists():
    assert callable(logiclanguage::ConstantAnnotation.__init__)


def test_logiclanguage::constantannotation_constructor_args():
    sig = inspect.signature(logiclanguage::ConstantAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::FunctionDeclaration)


def test_logiclanguage::functiondeclaration_constructor_exists():
    assert callable(logiclanguage::FunctionDeclaration.__init__)


def test_logiclanguage::functiondeclaration_constructor_args():
    sig = inspect.signature(logiclanguage::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::functiondefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::FunctionDefinition)


def test_logiclanguage::functiondefinition_constructor_exists():
    assert callable(logiclanguage::FunctionDefinition.__init__)


def test_logiclanguage::functiondefinition_constructor_args():
    sig = inspect.signature(logiclanguage::FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::relationdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::RelationDeclaration)


def test_logiclanguage::relationdeclaration_constructor_exists():
    assert callable(logiclanguage::RelationDeclaration.__init__)


def test_logiclanguage::relationdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage::RelationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::relationannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::RelationAnnotation)


def test_logiclanguage::relationannotation_constructor_exists():
    assert callable(logiclanguage::RelationAnnotation.__init__)


def test_logiclanguage::relationannotation_constructor_args():
    sig = inspect.signature(logiclanguage::RelationAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::assertionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::AssertionAnnotation)


def test_logiclanguage::assertionannotation_constructor_exists():
    assert callable(logiclanguage::AssertionAnnotation.__init__)


def test_logiclanguage::assertionannotation_constructor_args():
    sig = inspect.signature(logiclanguage::AssertionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::assertion_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Assertion)


def test_logiclanguage::assertion_constructor_exists():
    assert callable(logiclanguage::Assertion.__init__)


def test_logiclanguage::assertion_constructor_args():
    sig = inspect.signature(logiclanguage::Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage::assertion_has_name():
    assert hasattr(logiclanguage::Assertion, "name")
    descriptor = None
    for klass in logiclanguage::Assertion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::termdescription_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TermDescription)


def test_logiclanguage::termdescription_constructor_exists():
    assert callable(logiclanguage::TermDescription.__init__)


def test_logiclanguage::termdescription_constructor_args():
    sig = inspect.signature(logiclanguage::TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::typedescriptor_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TypeDescriptor)


def test_logiclanguage::typedescriptor_constructor_exists():
    assert callable(logiclanguage::TypeDescriptor.__init__)


def test_logiclanguage::typedescriptor_constructor_args():
    sig = inspect.signature(logiclanguage::TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_numericoperation_is_not_abstract():
    assert not inspect.isabstract(NumericOperation)


def test_numericoperation_constructor_exists():
    assert callable(NumericOperation.__init__)


def test_numericoperation_constructor_args():
    sig = inspect.signature(NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::divison_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Divison)


def test_logiclanguage::divison_constructor_exists():
    assert callable(logiclanguage::Divison.__init__)


def test_logiclanguage::divison_constructor_args():
    sig = inspect.signature(logiclanguage::Divison.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::pow_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Pow)


def test_logiclanguage::pow_constructor_exists():
    assert callable(logiclanguage::Pow.__init__)


def test_logiclanguage::pow_constructor_args():
    sig = inspect.signature(logiclanguage::Pow.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::multiply_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Multiply)


def test_logiclanguage::multiply_constructor_exists():
    assert callable(logiclanguage::Multiply.__init__)


def test_logiclanguage::multiply_constructor_args():
    sig = inspect.signature(logiclanguage::Multiply.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::minus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Minus)


def test_logiclanguage::minus_constructor_exists():
    assert callable(logiclanguage::Minus.__init__)


def test_logiclanguage::minus_constructor_args():
    sig = inspect.signature(logiclanguage::Minus.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::mod_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Mod)


def test_logiclanguage::mod_constructor_exists():
    assert callable(logiclanguage::Mod.__init__)


def test_logiclanguage::mod_constructor_args():
    sig = inspect.signature(logiclanguage::Mod.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::plus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Plus)


def test_logiclanguage::plus_constructor_exists():
    assert callable(logiclanguage::Plus.__init__)


def test_logiclanguage::plus_constructor_args():
    sig = inspect.signature(logiclanguage::Plus.__init__)
    params = list(sig.parameters.keys())



def test_booloperation_is_not_abstract():
    assert not inspect.isabstract(BoolOperation)


def test_booloperation_constructor_exists():
    assert callable(BoolOperation.__init__)


def test_booloperation_constructor_args():
    sig = inspect.signature(BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::iff_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Iff)


def test_logiclanguage::iff_constructor_exists():
    assert callable(logiclanguage::Iff.__init__)


def test_logiclanguage::iff_constructor_args():
    sig = inspect.signature(logiclanguage::Iff.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::not_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Not)


def test_logiclanguage::not_constructor_exists():
    assert callable(logiclanguage::Not.__init__)


def test_logiclanguage::not_constructor_args():
    sig = inspect.signature(logiclanguage::Not.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::or_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Or)


def test_logiclanguage::or_constructor_exists():
    assert callable(logiclanguage::Or.__init__)


def test_logiclanguage::or_constructor_args():
    sig = inspect.signature(logiclanguage::Or.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::impl_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Impl)


def test_logiclanguage::impl_constructor_exists():
    assert callable(logiclanguage::Impl.__init__)


def test_logiclanguage::impl_constructor_args():
    sig = inspect.signature(logiclanguage::Impl.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::and_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::And)


def test_logiclanguage::and_constructor_exists():
    assert callable(logiclanguage::And.__init__)


def test_logiclanguage::and_constructor_args():
    sig = inspect.signature(logiclanguage::And.__init__)
    params = list(sig.parameters.keys())



def test_primitiverelation_is_not_abstract():
    assert not inspect.isabstract(PrimitiveRelation)


def test_primitiverelation_constructor_exists():
    assert callable(PrimitiveRelation.__init__)


def test_primitiverelation_constructor_args():
    sig = inspect.signature(PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::lessthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::LessThan)


def test_logiclanguage::lessthan_constructor_exists():
    assert callable(logiclanguage::LessThan.__init__)


def test_logiclanguage::lessthan_constructor_args():
    sig = inspect.signature(logiclanguage::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::morethan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::MoreThan)


def test_logiclanguage::morethan_constructor_exists():
    assert callable(logiclanguage::MoreThan.__init__)


def test_logiclanguage::morethan_constructor_args():
    sig = inspect.signature(logiclanguage::MoreThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::moreorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::MoreOrEqualThan)


def test_logiclanguage::moreorequalthan_constructor_exists():
    assert callable(logiclanguage::MoreOrEqualThan.__init__)


def test_logiclanguage::moreorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage::MoreOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::lessorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::LessOrEqualThan)


def test_logiclanguage::lessorequalthan_constructor_exists():
    assert callable(logiclanguage::LessOrEqualThan.__init__)


def test_logiclanguage::lessorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage::LessOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::distinct_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Distinct)


def test_logiclanguage::distinct_constructor_exists():
    assert callable(logiclanguage::Distinct.__init__)


def test_logiclanguage::distinct_constructor_args():
    sig = inspect.signature(logiclanguage::Distinct.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::equals_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Equals)


def test_logiclanguage::equals_constructor_exists():
    assert callable(logiclanguage::Equals.__init__)


def test_logiclanguage::equals_constructor_args():
    sig = inspect.signature(logiclanguage::Equals.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::transitiveclosure_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TransitiveClosure)


def test_logiclanguage::transitiveclosure_constructor_exists():
    assert callable(logiclanguage::TransitiveClosure.__init__)


def test_logiclanguage::transitiveclosure_constructor_args():
    sig = inspect.signature(logiclanguage::TransitiveClosure.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::AggregateExpression)


def test_logiclanguage::aggregateexpression_constructor_exists():
    assert callable(logiclanguage::AggregateExpression.__init__)


def test_logiclanguage::aggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage::AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::instanceof_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::InstanceOf)


def test_logiclanguage::instanceof_constructor_exists():
    assert callable(logiclanguage::InstanceOf.__init__)


def test_logiclanguage::instanceof_constructor_args():
    sig = inspect.signature(logiclanguage::InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::numericoperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::NumericOperation)


def test_logiclanguage::numericoperation_constructor_exists():
    assert callable(logiclanguage::NumericOperation.__init__)


def test_logiclanguage::numericoperation_constructor_args():
    sig = inspect.signature(logiclanguage::NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::primitiverelation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::PrimitiveRelation)


def test_logiclanguage::primitiverelation_constructor_exists():
    assert callable(logiclanguage::PrimitiveRelation.__init__)


def test_logiclanguage::primitiverelation_constructor_args():
    sig = inspect.signature(logiclanguage::PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::booloperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::BoolOperation)


def test_logiclanguage::booloperation_constructor_exists():
    assert callable(logiclanguage::BoolOperation.__init__)


def test_logiclanguage::booloperation_constructor_args():
    sig = inspect.signature(logiclanguage::BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::unknownbecauseuninterpreted_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::UnknownBecauseUninterpreted)


def test_logiclanguage::unknownbecauseuninterpreted_constructor_exists():
    assert callable(logiclanguage::UnknownBecauseUninterpreted.__init__)


def test_logiclanguage::unknownbecauseuninterpreted_constructor_args():
    sig = inspect.signature(logiclanguage::UnknownBecauseUninterpreted.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::IfThenElse)


def test_logiclanguage::ifthenelse_constructor_exists():
    assert callable(logiclanguage::IfThenElse.__init__)


def test_logiclanguage::ifthenelse_constructor_args():
    sig = inspect.signature(logiclanguage::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::symbolicvalue_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::SymbolicValue)


def test_logiclanguage::symbolicvalue_constructor_exists():
    assert callable(logiclanguage::SymbolicValue.__init__)


def test_logiclanguage::symbolicvalue_constructor_args():
    sig = inspect.signature(logiclanguage::SymbolicValue.__init__)
    params = list(sig.parameters.keys())



def test_termdescription_is_not_abstract():
    assert not inspect.isabstract(TermDescription)


def test_termdescription_constructor_exists():
    assert callable(TermDescription.__init__)


def test_termdescription_constructor_args():
    sig = inspect.signature(TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::SymbolicDeclaration)


def test_logiclanguage::symbolicdeclaration_constructor_exists():
    assert callable(logiclanguage::SymbolicDeclaration.__init__)


def test_logiclanguage::symbolicdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage::SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage::symbolicdeclaration_has_name():
    assert hasattr(logiclanguage::SymbolicDeclaration, "name")
    descriptor = None
    for klass in logiclanguage::SymbolicDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::term_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Term)


def test_logiclanguage::term_constructor_exists():
    assert callable(logiclanguage::Term.__init__)


def test_logiclanguage::term_constructor_args():
    sig = inspect.signature(logiclanguage::Term.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::functionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::FunctionAnnotation)


def test_logiclanguage::functionannotation_constructor_exists():
    assert callable(logiclanguage::FunctionAnnotation.__init__)


def test_logiclanguage::functionannotation_constructor_args():
    sig = inspect.signature(logiclanguage::FunctionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(PrimitiveTypeReference)


def test_primitivetypereference_constructor_exists():
    assert callable(PrimitiveTypeReference.__init__)


def test_primitivetypereference_constructor_args():
    sig = inspect.signature(PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::stringtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::StringTypeReference)


def test_logiclanguage::stringtypereference_constructor_exists():
    assert callable(logiclanguage::StringTypeReference.__init__)


def test_logiclanguage::stringtypereference_constructor_args():
    sig = inspect.signature(logiclanguage::StringTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::booltypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::BoolTypeReference)


def test_logiclanguage::booltypereference_constructor_exists():
    assert callable(logiclanguage::BoolTypeReference.__init__)


def test_logiclanguage::booltypereference_constructor_args():
    sig = inspect.signature(logiclanguage::BoolTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::realtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::RealTypeReference)


def test_logiclanguage::realtypereference_constructor_exists():
    assert callable(logiclanguage::RealTypeReference.__init__)


def test_logiclanguage::realtypereference_constructor_args():
    sig = inspect.signature(logiclanguage::RealTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::inttypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::IntTypeReference)


def test_logiclanguage::inttypereference_constructor_exists():
    assert callable(logiclanguage::IntTypeReference.__init__)


def test_logiclanguage::inttypereference_constructor_args():
    sig = inspect.signature(logiclanguage::IntTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifiedExpression)


def test_quantifiedexpression_constructor_exists():
    assert callable(QuantifiedExpression.__init__)


def test_quantifiedexpression_constructor_args():
    sig = inspect.signature(QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::forall_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Forall)


def test_logiclanguage::forall_constructor_exists():
    assert callable(logiclanguage::Forall.__init__)


def test_logiclanguage::forall_constructor_args():
    sig = inspect.signature(logiclanguage::Forall.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::exists_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Exists)


def test_logiclanguage::exists_constructor_exists():
    assert callable(logiclanguage::Exists.__init__)


def test_logiclanguage::exists_constructor_args():
    sig = inspect.signature(logiclanguage::Exists.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::QuantifiedExpression)


def test_logiclanguage::quantifiedexpression_constructor_exists():
    assert callable(logiclanguage::QuantifiedExpression.__init__)


def test_logiclanguage::quantifiedexpression_constructor_args():
    sig = inspect.signature(logiclanguage::QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicterm_is_not_abstract():
    assert not inspect.isabstract(AtomicTerm)


def test_atomicterm_constructor_exists():
    assert callable(AtomicTerm.__init__)


def test_atomicterm_constructor_args():
    sig = inspect.signature(AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::stringliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::StringLiteral)


def test_logiclanguage::stringliteral_constructor_exists():
    assert callable(logiclanguage::StringLiteral.__init__)


def test_logiclanguage::stringliteral_constructor_args():
    sig = inspect.signature(logiclanguage::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage::stringliteral_has_value():
    assert hasattr(logiclanguage::StringLiteral, "value")
    descriptor = None
    for klass in logiclanguage::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::boolliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::BoolLiteral)


def test_logiclanguage::boolliteral_constructor_exists():
    assert callable(logiclanguage::BoolLiteral.__init__)


def test_logiclanguage::boolliteral_constructor_args():
    sig = inspect.signature(logiclanguage::BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage::boolliteral_has_value():
    assert hasattr(logiclanguage::BoolLiteral, "value")
    descriptor = None
    for klass in logiclanguage::BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::realliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::RealLiteral)


def test_logiclanguage::realliteral_constructor_exists():
    assert callable(logiclanguage::RealLiteral.__init__)


def test_logiclanguage::realliteral_constructor_args():
    sig = inspect.signature(logiclanguage::RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage::realliteral_has_value():
    assert hasattr(logiclanguage::RealLiteral, "value")
    descriptor = None
    for klass in logiclanguage::RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::intliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::IntLiteral)


def test_logiclanguage::intliteral_constructor_exists():
    assert callable(logiclanguage::IntLiteral.__init__)


def test_logiclanguage::intliteral_constructor_args():
    sig = inspect.signature(logiclanguage::IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage::intliteral_has_value():
    assert hasattr(logiclanguage::IntLiteral, "value")
    descriptor = None
    for klass in logiclanguage::IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage::atomicterm_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::AtomicTerm)


def test_logiclanguage::atomicterm_constructor_exists():
    assert callable(logiclanguage::AtomicTerm.__init__)


def test_logiclanguage::atomicterm_constructor_args():
    sig = inspect.signature(logiclanguage::AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_typedescriptor_is_not_abstract():
    assert not inspect.isabstract(TypeDescriptor)


def test_typedescriptor_constructor_exists():
    assert callable(TypeDescriptor.__init__)


def test_typedescriptor_constructor_args():
    sig = inspect.signature(TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::type_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Type)


def test_logiclanguage::type_constructor_exists():
    assert callable(logiclanguage::Type.__init__)


def test_logiclanguage::type_constructor_args():
    sig = inspect.signature(logiclanguage::Type.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage::type_has_isAbstract():
    assert hasattr(logiclanguage::Type, "isAbstract")
    descriptor = None
    for klass in logiclanguage::Type.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_logiclanguage::type_has_name():
    assert hasattr(logiclanguage::Type, "name")
    descriptor = None
    for klass in logiclanguage::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_typereference_is_not_abstract():
    assert not inspect.isabstract(TypeReference)


def test_typereference_constructor_exists():
    assert callable(TypeReference.__init__)


def test_typereference_constructor_args():
    sig = inspect.signature(TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::PrimitiveTypeReference)


def test_logiclanguage::primitivetypereference_constructor_exists():
    assert callable(logiclanguage::PrimitiveTypeReference.__init__)


def test_logiclanguage::primitivetypereference_constructor_args():
    sig = inspect.signature(logiclanguage::PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::complextypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::ComplexTypeReference)


def test_logiclanguage::complextypereference_constructor_exists():
    assert callable(logiclanguage::ComplexTypeReference.__init__)


def test_logiclanguage::complextypereference_constructor_args():
    sig = inspect.signature(logiclanguage::ComplexTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::typereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TypeReference)


def test_logiclanguage::typereference_constructor_exists():
    assert callable(logiclanguage::TypeReference.__init__)


def test_logiclanguage::typereference_constructor_args():
    sig = inspect.signature(logiclanguage::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::typedeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TypeDeclaration)


def test_logiclanguage::typedeclaration_constructor_exists():
    assert callable(logiclanguage::TypeDeclaration.__init__)


def test_logiclanguage::typedeclaration_constructor_args():
    sig = inspect.signature(logiclanguage::TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::typedefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::TypeDefinition)


def test_logiclanguage::typedefinition_constructor_exists():
    assert callable(logiclanguage::TypeDefinition.__init__)


def test_logiclanguage::typedefinition_constructor_args():
    sig = inspect.signature(logiclanguage::TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(SymbolicDeclaration)


def test_symbolicdeclaration_constructor_exists():
    assert callable(SymbolicDeclaration.__init__)


def test_symbolicdeclaration_constructor_args():
    sig = inspect.signature(SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::function_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Function)


def test_logiclanguage::function_constructor_exists():
    assert callable(logiclanguage::Function.__init__)


def test_logiclanguage::function_constructor_args():
    sig = inspect.signature(logiclanguage::Function.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::relation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Relation)


def test_logiclanguage::relation_constructor_exists():
    assert callable(logiclanguage::Relation.__init__)


def test_logiclanguage::relation_constructor_args():
    sig = inspect.signature(logiclanguage::Relation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::variable_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Variable)


def test_logiclanguage::variable_constructor_exists():
    assert callable(logiclanguage::Variable.__init__)


def test_logiclanguage::variable_constructor_args():
    sig = inspect.signature(logiclanguage::Variable.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::constant_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::Constant)


def test_logiclanguage::constant_constructor_exists():
    assert callable(logiclanguage::Constant.__init__)


def test_logiclanguage::constant_constructor_args():
    sig = inspect.signature(logiclanguage::Constant.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage::definedelement_is_not_abstract():
    assert not inspect.isabstract(logiclanguage::DefinedElement)


def test_logiclanguage::definedelement_constructor_exists():
    assert callable(logiclanguage::DefinedElement.__init__)


def test_logiclanguage::definedelement_constructor_args():
    sig = inspect.signature(logiclanguage::DefinedElement.__init__)
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
AggregateExpression_strategy = st.builds(
    AggregateExpression,
)
logiclanguage::ProjectedAggregateExpression_strategy = st.builds(
    logiclanguage::ProjectedAggregateExpression,
    projectionIndex=
        st.integers()
)
logiclanguage::Count_strategy = st.builds(
    logiclanguage::Count,
)
ProjectedAggregateExpression_strategy = st.builds(
    ProjectedAggregateExpression,
)
logiclanguage::Max_strategy = st.builds(
    logiclanguage::Max,
)
logiclanguage::Min_strategy = st.builds(
    logiclanguage::Min,
)
logiclanguage::Sum_strategy = st.builds(
    logiclanguage::Sum,
)
logiclanguage::AggregatedParameterSubstitution_strategy = st.builds(
    logiclanguage::AggregatedParameterSubstitution,
)
Relation_strategy = st.builds(
    Relation,
)
logiclanguage::RelationDefinition_strategy = st.builds(
    logiclanguage::RelationDefinition,
)
Constant_strategy = st.builds(
    Constant,
)
logiclanguage::ConstantDeclaration_strategy = st.builds(
    logiclanguage::ConstantDeclaration,
)
logiclanguage::ConstantDefinition_strategy = st.builds(
    logiclanguage::ConstantDefinition,
)
logiclanguage::ConstantAnnotation_strategy = st.builds(
    logiclanguage::ConstantAnnotation,
)
Function_strategy = st.builds(
    Function,
)
logiclanguage::FunctionDeclaration_strategy = st.builds(
    logiclanguage::FunctionDeclaration,
)
logiclanguage::FunctionDefinition_strategy = st.builds(
    logiclanguage::FunctionDefinition,
)
logiclanguage::RelationDeclaration_strategy = st.builds(
    logiclanguage::RelationDeclaration,
)
logiclanguage::RelationAnnotation_strategy = st.builds(
    logiclanguage::RelationAnnotation,
)
logiclanguage::AssertionAnnotation_strategy = st.builds(
    logiclanguage::AssertionAnnotation,
)
logiclanguage::Assertion_strategy = st.builds(
    logiclanguage::Assertion,
    name=
        safe_text
)
logiclanguage::TermDescription_strategy = st.builds(
    logiclanguage::TermDescription,
)
logiclanguage::TypeDescriptor_strategy = st.builds(
    logiclanguage::TypeDescriptor,
)
NumericOperation_strategy = st.builds(
    NumericOperation,
)
logiclanguage::Divison_strategy = st.builds(
    logiclanguage::Divison,
)
logiclanguage::Pow_strategy = st.builds(
    logiclanguage::Pow,
)
logiclanguage::Multiply_strategy = st.builds(
    logiclanguage::Multiply,
)
logiclanguage::Minus_strategy = st.builds(
    logiclanguage::Minus,
)
logiclanguage::Mod_strategy = st.builds(
    logiclanguage::Mod,
)
logiclanguage::Plus_strategy = st.builds(
    logiclanguage::Plus,
)
BoolOperation_strategy = st.builds(
    BoolOperation,
)
logiclanguage::Iff_strategy = st.builds(
    logiclanguage::Iff,
)
logiclanguage::Not_strategy = st.builds(
    logiclanguage::Not,
)
logiclanguage::Or_strategy = st.builds(
    logiclanguage::Or,
)
logiclanguage::Impl_strategy = st.builds(
    logiclanguage::Impl,
)
logiclanguage::And_strategy = st.builds(
    logiclanguage::And,
)
PrimitiveRelation_strategy = st.builds(
    PrimitiveRelation,
)
logiclanguage::LessThan_strategy = st.builds(
    logiclanguage::LessThan,
)
logiclanguage::MoreThan_strategy = st.builds(
    logiclanguage::MoreThan,
)
logiclanguage::MoreOrEqualThan_strategy = st.builds(
    logiclanguage::MoreOrEqualThan,
)
logiclanguage::LessOrEqualThan_strategy = st.builds(
    logiclanguage::LessOrEqualThan,
)
logiclanguage::Distinct_strategy = st.builds(
    logiclanguage::Distinct,
)
logiclanguage::Equals_strategy = st.builds(
    logiclanguage::Equals,
)
Term_strategy = st.builds(
    Term,
)
logiclanguage::TransitiveClosure_strategy = st.builds(
    logiclanguage::TransitiveClosure,
)
logiclanguage::AggregateExpression_strategy = st.builds(
    logiclanguage::AggregateExpression,
)
logiclanguage::InstanceOf_strategy = st.builds(
    logiclanguage::InstanceOf,
)
logiclanguage::NumericOperation_strategy = st.builds(
    logiclanguage::NumericOperation,
)
logiclanguage::PrimitiveRelation_strategy = st.builds(
    logiclanguage::PrimitiveRelation,
)
logiclanguage::BoolOperation_strategy = st.builds(
    logiclanguage::BoolOperation,
)
logiclanguage::UnknownBecauseUninterpreted_strategy = st.builds(
    logiclanguage::UnknownBecauseUninterpreted,
)
logiclanguage::IfThenElse_strategy = st.builds(
    logiclanguage::IfThenElse,
)
logiclanguage::SymbolicValue_strategy = st.builds(
    logiclanguage::SymbolicValue,
)
TermDescription_strategy = st.builds(
    TermDescription,
)
logiclanguage::SymbolicDeclaration_strategy = st.builds(
    logiclanguage::SymbolicDeclaration,
    name=
        safe_text
)
logiclanguage::Term_strategy = st.builds(
    logiclanguage::Term,
)
logiclanguage::FunctionAnnotation_strategy = st.builds(
    logiclanguage::FunctionAnnotation,
)
PrimitiveTypeReference_strategy = st.builds(
    PrimitiveTypeReference,
)
logiclanguage::StringTypeReference_strategy = st.builds(
    logiclanguage::StringTypeReference,
)
logiclanguage::BoolTypeReference_strategy = st.builds(
    logiclanguage::BoolTypeReference,
)
logiclanguage::RealTypeReference_strategy = st.builds(
    logiclanguage::RealTypeReference,
)
logiclanguage::IntTypeReference_strategy = st.builds(
    logiclanguage::IntTypeReference,
)
QuantifiedExpression_strategy = st.builds(
    QuantifiedExpression,
)
logiclanguage::Forall_strategy = st.builds(
    logiclanguage::Forall,
)
logiclanguage::Exists_strategy = st.builds(
    logiclanguage::Exists,
)
logiclanguage::QuantifiedExpression_strategy = st.builds(
    logiclanguage::QuantifiedExpression,
)
AtomicTerm_strategy = st.builds(
    AtomicTerm,
)
logiclanguage::StringLiteral_strategy = st.builds(
    logiclanguage::StringLiteral,
    value=
        safe_text
)
logiclanguage::BoolLiteral_strategy = st.builds(
    logiclanguage::BoolLiteral,
    value=
        st.booleans()
)
logiclanguage::RealLiteral_strategy = st.builds(
    logiclanguage::RealLiteral,
    value=
        safe_text
)
logiclanguage::IntLiteral_strategy = st.builds(
    logiclanguage::IntLiteral,
    value=
        st.integers()
)
logiclanguage::AtomicTerm_strategy = st.builds(
    logiclanguage::AtomicTerm,
)
TypeDescriptor_strategy = st.builds(
    TypeDescriptor,
)
logiclanguage::Type_strategy = st.builds(
    logiclanguage::Type,
    isAbstract=
        st.booleans(),
    name=
        safe_text
)
TypeReference_strategy = st.builds(
    TypeReference,
)
logiclanguage::PrimitiveTypeReference_strategy = st.builds(
    logiclanguage::PrimitiveTypeReference,
)
logiclanguage::ComplexTypeReference_strategy = st.builds(
    logiclanguage::ComplexTypeReference,
)
logiclanguage::TypeReference_strategy = st.builds(
    logiclanguage::TypeReference,
)
Type_strategy = st.builds(
    Type,
)
logiclanguage::TypeDeclaration_strategy = st.builds(
    logiclanguage::TypeDeclaration,
)
logiclanguage::TypeDefinition_strategy = st.builds(
    logiclanguage::TypeDefinition,
)
SymbolicDeclaration_strategy = st.builds(
    SymbolicDeclaration,
)
logiclanguage::Function_strategy = st.builds(
    logiclanguage::Function,
)
logiclanguage::Relation_strategy = st.builds(
    logiclanguage::Relation,
)
logiclanguage::Variable_strategy = st.builds(
    logiclanguage::Variable,
)
logiclanguage::Constant_strategy = st.builds(
    logiclanguage::Constant,
)
logiclanguage::DefinedElement_strategy = st.builds(
    logiclanguage::DefinedElement,
)

@given(instance=AggregateExpression_strategy)
@settings(max_examples=50)
def test_aggregateexpression_instantiation(instance):
    assert isinstance(instance, AggregateExpression)

@given(instance=logiclanguage::ProjectedAggregateExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage::projectedaggregateexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage::ProjectedAggregateExpression)

@given(instance=logiclanguage::ProjectedAggregateExpression_strategy)
def test_logiclanguage::projectedaggregateexpression_projectionIndex_type(instance):
    assert isinstance(instance.projectionIndex, int)


@given(instance=logiclanguage::ProjectedAggregateExpression_strategy)
def test_logiclanguage::projectedaggregateexpression_projectionIndex_setter(instance):
    original = instance.projectionIndex
    instance.projectionIndex = original
    assert instance.projectionIndex == original

@given(instance=logiclanguage::Count_strategy)
@settings(max_examples=50)
def test_logiclanguage::count_instantiation(instance):
    assert isinstance(instance, logiclanguage::Count)

@given(instance=ProjectedAggregateExpression_strategy)
@settings(max_examples=50)
def test_projectedaggregateexpression_instantiation(instance):
    assert isinstance(instance, ProjectedAggregateExpression)

@given(instance=logiclanguage::Max_strategy)
@settings(max_examples=50)
def test_logiclanguage::max_instantiation(instance):
    assert isinstance(instance, logiclanguage::Max)

@given(instance=logiclanguage::Min_strategy)
@settings(max_examples=50)
def test_logiclanguage::min_instantiation(instance):
    assert isinstance(instance, logiclanguage::Min)

@given(instance=logiclanguage::Sum_strategy)
@settings(max_examples=50)
def test_logiclanguage::sum_instantiation(instance):
    assert isinstance(instance, logiclanguage::Sum)

@given(instance=logiclanguage::AggregatedParameterSubstitution_strategy)
@settings(max_examples=50)
def test_logiclanguage::aggregatedparametersubstitution_instantiation(instance):
    assert isinstance(instance, logiclanguage::AggregatedParameterSubstitution)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=logiclanguage::RelationDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage::relationdefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage::RelationDefinition)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=logiclanguage::ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage::constantdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage::ConstantDeclaration)

@given(instance=logiclanguage::ConstantDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage::constantdefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage::ConstantDefinition)

@given(instance=logiclanguage::ConstantAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage::constantannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage::ConstantAnnotation)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=logiclanguage::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage::functiondeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage::FunctionDeclaration)

@given(instance=logiclanguage::FunctionDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage::functiondefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage::FunctionDefinition)

@given(instance=logiclanguage::RelationDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage::relationdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage::RelationDeclaration)

@given(instance=logiclanguage::RelationAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage::relationannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage::RelationAnnotation)

@given(instance=logiclanguage::AssertionAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage::assertionannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage::AssertionAnnotation)

@given(instance=logiclanguage::Assertion_strategy)
@settings(max_examples=50)
def test_logiclanguage::assertion_instantiation(instance):
    assert isinstance(instance, logiclanguage::Assertion)

@given(instance=logiclanguage::Assertion_strategy)
def test_logiclanguage::assertion_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logiclanguage::Assertion_strategy)
def test_logiclanguage::assertion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logiclanguage::TermDescription_strategy)
@settings(max_examples=50)
def test_logiclanguage::termdescription_instantiation(instance):
    assert isinstance(instance, logiclanguage::TermDescription)

@given(instance=logiclanguage::TypeDescriptor_strategy)
@settings(max_examples=50)
def test_logiclanguage::typedescriptor_instantiation(instance):
    assert isinstance(instance, logiclanguage::TypeDescriptor)

@given(instance=NumericOperation_strategy)
@settings(max_examples=50)
def test_numericoperation_instantiation(instance):
    assert isinstance(instance, NumericOperation)

@given(instance=logiclanguage::Divison_strategy)
@settings(max_examples=50)
def test_logiclanguage::divison_instantiation(instance):
    assert isinstance(instance, logiclanguage::Divison)

@given(instance=logiclanguage::Pow_strategy)
@settings(max_examples=50)
def test_logiclanguage::pow_instantiation(instance):
    assert isinstance(instance, logiclanguage::Pow)

@given(instance=logiclanguage::Multiply_strategy)
@settings(max_examples=50)
def test_logiclanguage::multiply_instantiation(instance):
    assert isinstance(instance, logiclanguage::Multiply)

@given(instance=logiclanguage::Minus_strategy)
@settings(max_examples=50)
def test_logiclanguage::minus_instantiation(instance):
    assert isinstance(instance, logiclanguage::Minus)

@given(instance=logiclanguage::Mod_strategy)
@settings(max_examples=50)
def test_logiclanguage::mod_instantiation(instance):
    assert isinstance(instance, logiclanguage::Mod)

@given(instance=logiclanguage::Plus_strategy)
@settings(max_examples=50)
def test_logiclanguage::plus_instantiation(instance):
    assert isinstance(instance, logiclanguage::Plus)

@given(instance=BoolOperation_strategy)
@settings(max_examples=50)
def test_booloperation_instantiation(instance):
    assert isinstance(instance, BoolOperation)

@given(instance=logiclanguage::Iff_strategy)
@settings(max_examples=50)
def test_logiclanguage::iff_instantiation(instance):
    assert isinstance(instance, logiclanguage::Iff)

@given(instance=logiclanguage::Not_strategy)
@settings(max_examples=50)
def test_logiclanguage::not_instantiation(instance):
    assert isinstance(instance, logiclanguage::Not)

@given(instance=logiclanguage::Or_strategy)
@settings(max_examples=50)
def test_logiclanguage::or_instantiation(instance):
    assert isinstance(instance, logiclanguage::Or)

@given(instance=logiclanguage::Impl_strategy)
@settings(max_examples=50)
def test_logiclanguage::impl_instantiation(instance):
    assert isinstance(instance, logiclanguage::Impl)

@given(instance=logiclanguage::And_strategy)
@settings(max_examples=50)
def test_logiclanguage::and_instantiation(instance):
    assert isinstance(instance, logiclanguage::And)

@given(instance=PrimitiveRelation_strategy)
@settings(max_examples=50)
def test_primitiverelation_instantiation(instance):
    assert isinstance(instance, PrimitiveRelation)

@given(instance=logiclanguage::LessThan_strategy)
@settings(max_examples=50)
def test_logiclanguage::lessthan_instantiation(instance):
    assert isinstance(instance, logiclanguage::LessThan)

@given(instance=logiclanguage::MoreThan_strategy)
@settings(max_examples=50)
def test_logiclanguage::morethan_instantiation(instance):
    assert isinstance(instance, logiclanguage::MoreThan)

@given(instance=logiclanguage::MoreOrEqualThan_strategy)
@settings(max_examples=50)
def test_logiclanguage::moreorequalthan_instantiation(instance):
    assert isinstance(instance, logiclanguage::MoreOrEqualThan)

@given(instance=logiclanguage::LessOrEqualThan_strategy)
@settings(max_examples=50)
def test_logiclanguage::lessorequalthan_instantiation(instance):
    assert isinstance(instance, logiclanguage::LessOrEqualThan)

@given(instance=logiclanguage::Distinct_strategy)
@settings(max_examples=50)
def test_logiclanguage::distinct_instantiation(instance):
    assert isinstance(instance, logiclanguage::Distinct)

@given(instance=logiclanguage::Equals_strategy)
@settings(max_examples=50)
def test_logiclanguage::equals_instantiation(instance):
    assert isinstance(instance, logiclanguage::Equals)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=logiclanguage::TransitiveClosure_strategy)
@settings(max_examples=50)
def test_logiclanguage::transitiveclosure_instantiation(instance):
    assert isinstance(instance, logiclanguage::TransitiveClosure)

@given(instance=logiclanguage::AggregateExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage::aggregateexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage::AggregateExpression)

@given(instance=logiclanguage::InstanceOf_strategy)
@settings(max_examples=50)
def test_logiclanguage::instanceof_instantiation(instance):
    assert isinstance(instance, logiclanguage::InstanceOf)

@given(instance=logiclanguage::NumericOperation_strategy)
@settings(max_examples=50)
def test_logiclanguage::numericoperation_instantiation(instance):
    assert isinstance(instance, logiclanguage::NumericOperation)

@given(instance=logiclanguage::PrimitiveRelation_strategy)
@settings(max_examples=50)
def test_logiclanguage::primitiverelation_instantiation(instance):
    assert isinstance(instance, logiclanguage::PrimitiveRelation)

@given(instance=logiclanguage::BoolOperation_strategy)
@settings(max_examples=50)
def test_logiclanguage::booloperation_instantiation(instance):
    assert isinstance(instance, logiclanguage::BoolOperation)

@given(instance=logiclanguage::UnknownBecauseUninterpreted_strategy)
@settings(max_examples=50)
def test_logiclanguage::unknownbecauseuninterpreted_instantiation(instance):
    assert isinstance(instance, logiclanguage::UnknownBecauseUninterpreted)

@given(instance=logiclanguage::IfThenElse_strategy)
@settings(max_examples=50)
def test_logiclanguage::ifthenelse_instantiation(instance):
    assert isinstance(instance, logiclanguage::IfThenElse)

@given(instance=logiclanguage::SymbolicValue_strategy)
@settings(max_examples=50)
def test_logiclanguage::symbolicvalue_instantiation(instance):
    assert isinstance(instance, logiclanguage::SymbolicValue)

@given(instance=TermDescription_strategy)
@settings(max_examples=50)
def test_termdescription_instantiation(instance):
    assert isinstance(instance, TermDescription)

@given(instance=logiclanguage::SymbolicDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage::symbolicdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage::SymbolicDeclaration)

@given(instance=logiclanguage::SymbolicDeclaration_strategy)
def test_logiclanguage::symbolicdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logiclanguage::SymbolicDeclaration_strategy)
def test_logiclanguage::symbolicdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logiclanguage::Term_strategy)
@settings(max_examples=50)
def test_logiclanguage::term_instantiation(instance):
    assert isinstance(instance, logiclanguage::Term)

@given(instance=logiclanguage::FunctionAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage::functionannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage::FunctionAnnotation)

@given(instance=PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_primitivetypereference_instantiation(instance):
    assert isinstance(instance, PrimitiveTypeReference)

@given(instance=logiclanguage::StringTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::stringtypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::StringTypeReference)

@given(instance=logiclanguage::BoolTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::booltypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::BoolTypeReference)

@given(instance=logiclanguage::RealTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::realtypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::RealTypeReference)

@given(instance=logiclanguage::IntTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::inttypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::IntTypeReference)

@given(instance=QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_quantifiedexpression_instantiation(instance):
    assert isinstance(instance, QuantifiedExpression)

@given(instance=logiclanguage::Forall_strategy)
@settings(max_examples=50)
def test_logiclanguage::forall_instantiation(instance):
    assert isinstance(instance, logiclanguage::Forall)

@given(instance=logiclanguage::Exists_strategy)
@settings(max_examples=50)
def test_logiclanguage::exists_instantiation(instance):
    assert isinstance(instance, logiclanguage::Exists)

@given(instance=logiclanguage::QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage::quantifiedexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage::QuantifiedExpression)

@given(instance=AtomicTerm_strategy)
@settings(max_examples=50)
def test_atomicterm_instantiation(instance):
    assert isinstance(instance, AtomicTerm)

@given(instance=logiclanguage::StringLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage::stringliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage::StringLiteral)

@given(instance=logiclanguage::StringLiteral_strategy)
def test_logiclanguage::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=logiclanguage::StringLiteral_strategy)
def test_logiclanguage::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage::BoolLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage::boolliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage::BoolLiteral)

@given(instance=logiclanguage::BoolLiteral_strategy)
def test_logiclanguage::boolliteral_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=logiclanguage::BoolLiteral_strategy)
def test_logiclanguage::boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage::RealLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage::realliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage::RealLiteral)

@given(instance=logiclanguage::RealLiteral_strategy)
def test_logiclanguage::realliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=logiclanguage::RealLiteral_strategy)
def test_logiclanguage::realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage::IntLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage::intliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage::IntLiteral)

@given(instance=logiclanguage::IntLiteral_strategy)
def test_logiclanguage::intliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=logiclanguage::IntLiteral_strategy)
def test_logiclanguage::intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage::AtomicTerm_strategy)
@settings(max_examples=50)
def test_logiclanguage::atomicterm_instantiation(instance):
    assert isinstance(instance, logiclanguage::AtomicTerm)

@given(instance=TypeDescriptor_strategy)
@settings(max_examples=50)
def test_typedescriptor_instantiation(instance):
    assert isinstance(instance, TypeDescriptor)

@given(instance=logiclanguage::Type_strategy)
@settings(max_examples=50)
def test_logiclanguage::type_instantiation(instance):
    assert isinstance(instance, logiclanguage::Type)

@given(instance=logiclanguage::Type_strategy)
def test_logiclanguage::type_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=logiclanguage::Type_strategy)
def test_logiclanguage::type_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=logiclanguage::Type_strategy)
def test_logiclanguage::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=logiclanguage::Type_strategy)
def test_logiclanguage::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=logiclanguage::PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::primitivetypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::PrimitiveTypeReference)

@given(instance=logiclanguage::ComplexTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::complextypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::ComplexTypeReference)

@given(instance=logiclanguage::TypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage::typereference_instantiation(instance):
    assert isinstance(instance, logiclanguage::TypeReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=logiclanguage::TypeDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage::typedeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage::TypeDeclaration)

@given(instance=logiclanguage::TypeDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage::typedefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage::TypeDefinition)

@given(instance=SymbolicDeclaration_strategy)
@settings(max_examples=50)
def test_symbolicdeclaration_instantiation(instance):
    assert isinstance(instance, SymbolicDeclaration)

@given(instance=logiclanguage::Function_strategy)
@settings(max_examples=50)
def test_logiclanguage::function_instantiation(instance):
    assert isinstance(instance, logiclanguage::Function)

@given(instance=logiclanguage::Relation_strategy)
@settings(max_examples=50)
def test_logiclanguage::relation_instantiation(instance):
    assert isinstance(instance, logiclanguage::Relation)

@given(instance=logiclanguage::Variable_strategy)
@settings(max_examples=50)
def test_logiclanguage::variable_instantiation(instance):
    assert isinstance(instance, logiclanguage::Variable)

@given(instance=logiclanguage::Constant_strategy)
@settings(max_examples=50)
def test_logiclanguage::constant_instantiation(instance):
    assert isinstance(instance, logiclanguage::Constant)

@given(instance=logiclanguage::DefinedElement_strategy)
@settings(max_examples=50)
def test_logiclanguage::definedelement_instantiation(instance):
    assert isinstance(instance, logiclanguage::DefinedElement)
