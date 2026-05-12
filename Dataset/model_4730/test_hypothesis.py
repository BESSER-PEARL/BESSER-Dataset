import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AggregateExpression,
    logiclanguage_ProjectedAggregateExpression,
    logiclanguage_Count,
    ProjectedAggregateExpression,
    logiclanguage_Max,
    logiclanguage_Min,
    logiclanguage_Sum,
    logiclanguage_AggregatedParameterSubstitution,
    Relation,
    logiclanguage_RelationDefinition,
    Constant,
    logiclanguage_ConstantDeclaration,
    logiclanguage_ConstantDefinition,
    logiclanguage_ConstantAnnotation,
    Function,
    logiclanguage_FunctionDeclaration,
    logiclanguage_FunctionDefinition,
    logiclanguage_RelationDeclaration,
    logiclanguage_RelationAnnotation,
    logiclanguage_AssertionAnnotation,
    logiclanguage_Assertion,
    logiclanguage_TermDescription,
    logiclanguage_TypeDescriptor,
    NumericOperation,
    logiclanguage_Divison,
    logiclanguage_Mod,
    logiclanguage_Multiply,
    logiclanguage_Pow,
    logiclanguage_Minus,
    logiclanguage_Plus,
    BoolOperation,
    logiclanguage_Or,
    logiclanguage_Not,
    logiclanguage_Iff,
    logiclanguage_Impl,
    logiclanguage_And,
    PrimitiveRelation,
    logiclanguage_MoreOrEqualThan,
    logiclanguage_LessOrEqualThan,
    logiclanguage_Distinct,
    logiclanguage_LessThan,
    logiclanguage_MoreThan,
    logiclanguage_Equals,
    Term,
    logiclanguage_PrimitiveRelation,
    logiclanguage_IfThenElse,
    logiclanguage_BoolOperation,
    logiclanguage_NumericOperation,
    logiclanguage_UnknownBecauseUninterpreted,
    logiclanguage_AggregateExpression,
    logiclanguage_TransitiveClosure,
    logiclanguage_InstanceOf,
    logiclanguage_SymbolicValue,
    TermDescription,
    logiclanguage_SymbolicDeclaration,
    logiclanguage_Term,
    logiclanguage_FunctionAnnotation,
    PrimitiveTypeReference,
    logiclanguage_StringTypeReference,
    logiclanguage_RealTypeReference,
    logiclanguage_BoolTypeReference,
    logiclanguage_IntTypeReference,
    QuantifiedExpression,
    logiclanguage_Forall,
    logiclanguage_Exists,
    logiclanguage_QuantifiedExpression,
    AtomicTerm,
    logiclanguage_BoolLiteral,
    logiclanguage_RealLiteral,
    logiclanguage_StringLiteral,
    logiclanguage_IntLiteral,
    logiclanguage_AtomicTerm,
    TypeDescriptor,
    logiclanguage_Type,
    TypeReference,
    logiclanguage_PrimitiveTypeReference,
    logiclanguage_ComplexTypeReference,
    logiclanguage_TypeReference,
    Type,
    logiclanguage_TypeDeclaration,
    logiclanguage_TypeDefinition,
    SymbolicDeclaration,
    logiclanguage_Variable,
    logiclanguage_Constant,
    logiclanguage_Relation,
    logiclanguage_Function,
    logiclanguage_DefinedElement,
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



def test_logiclanguage_projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ProjectedAggregateExpression)


def test_logiclanguage_projectedaggregateexpression_constructor_exists():
    assert callable(logiclanguage_ProjectedAggregateExpression.__init__)


def test_logiclanguage_projectedaggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage_ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())
    assert "projectionIndex" in params, "Missing parameter 'projectionIndex'"

def test_logiclanguage_projectedaggregateexpression_has_projectionIndex():
    assert hasattr(logiclanguage_ProjectedAggregateExpression, "projectionIndex")
    descriptor = None
    for klass in logiclanguage_ProjectedAggregateExpression.__mro__:
        if "projectionIndex" in klass.__dict__:
            descriptor = klass.__dict__["projectionIndex"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_count_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Count)


def test_logiclanguage_count_constructor_exists():
    assert callable(logiclanguage_Count.__init__)


def test_logiclanguage_count_constructor_args():
    sig = inspect.signature(logiclanguage_Count.__init__)
    params = list(sig.parameters.keys())



def test_projectedaggregateexpression_is_not_abstract():
    assert not inspect.isabstract(ProjectedAggregateExpression)


def test_projectedaggregateexpression_constructor_exists():
    assert callable(ProjectedAggregateExpression.__init__)


def test_projectedaggregateexpression_constructor_args():
    sig = inspect.signature(ProjectedAggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_max_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Max)


def test_logiclanguage_max_constructor_exists():
    assert callable(logiclanguage_Max.__init__)


def test_logiclanguage_max_constructor_args():
    sig = inspect.signature(logiclanguage_Max.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_min_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Min)


def test_logiclanguage_min_constructor_exists():
    assert callable(logiclanguage_Min.__init__)


def test_logiclanguage_min_constructor_args():
    sig = inspect.signature(logiclanguage_Min.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_sum_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Sum)


def test_logiclanguage_sum_constructor_exists():
    assert callable(logiclanguage_Sum.__init__)


def test_logiclanguage_sum_constructor_args():
    sig = inspect.signature(logiclanguage_Sum.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_aggregatedparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AggregatedParameterSubstitution)


def test_logiclanguage_aggregatedparametersubstitution_constructor_exists():
    assert callable(logiclanguage_AggregatedParameterSubstitution.__init__)


def test_logiclanguage_aggregatedparametersubstitution_constructor_args():
    sig = inspect.signature(logiclanguage_AggregatedParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_relationdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationDefinition)


def test_logiclanguage_relationdefinition_constructor_exists():
    assert callable(logiclanguage_RelationDefinition.__init__)


def test_logiclanguage_relationdefinition_constructor_args():
    sig = inspect.signature(logiclanguage_RelationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_constantdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantDeclaration)


def test_logiclanguage_constantdeclaration_constructor_exists():
    assert callable(logiclanguage_ConstantDeclaration.__init__)


def test_logiclanguage_constantdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_constantdefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantDefinition)


def test_logiclanguage_constantdefinition_constructor_exists():
    assert callable(logiclanguage_ConstantDefinition.__init__)


def test_logiclanguage_constantdefinition_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantDefinition.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_constantannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ConstantAnnotation)


def test_logiclanguage_constantannotation_constructor_exists():
    assert callable(logiclanguage_ConstantAnnotation.__init__)


def test_logiclanguage_constantannotation_constructor_args():
    sig = inspect.signature(logiclanguage_ConstantAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(Function)


def test_function_constructor_exists():
    assert callable(Function.__init__)


def test_function_constructor_args():
    sig = inspect.signature(Function.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionDeclaration)


def test_logiclanguage_functiondeclaration_constructor_exists():
    assert callable(logiclanguage_FunctionDeclaration.__init__)


def test_logiclanguage_functiondeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_functiondefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionDefinition)


def test_logiclanguage_functiondefinition_constructor_exists():
    assert callable(logiclanguage_FunctionDefinition.__init__)


def test_logiclanguage_functiondefinition_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_relationdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationDeclaration)


def test_logiclanguage_relationdeclaration_constructor_exists():
    assert callable(logiclanguage_RelationDeclaration.__init__)


def test_logiclanguage_relationdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_RelationDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_relationannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RelationAnnotation)


def test_logiclanguage_relationannotation_constructor_exists():
    assert callable(logiclanguage_RelationAnnotation.__init__)


def test_logiclanguage_relationannotation_constructor_args():
    sig = inspect.signature(logiclanguage_RelationAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_assertionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AssertionAnnotation)


def test_logiclanguage_assertionannotation_constructor_exists():
    assert callable(logiclanguage_AssertionAnnotation.__init__)


def test_logiclanguage_assertionannotation_constructor_args():
    sig = inspect.signature(logiclanguage_AssertionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_assertion_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Assertion)


def test_logiclanguage_assertion_constructor_exists():
    assert callable(logiclanguage_Assertion.__init__)


def test_logiclanguage_assertion_constructor_args():
    sig = inspect.signature(logiclanguage_Assertion.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage_assertion_has_name():
    assert hasattr(logiclanguage_Assertion, "name")
    descriptor = None
    for klass in logiclanguage_Assertion.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_termdescription_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TermDescription)


def test_logiclanguage_termdescription_constructor_exists():
    assert callable(logiclanguage_TermDescription.__init__)


def test_logiclanguage_termdescription_constructor_args():
    sig = inspect.signature(logiclanguage_TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_typedescriptor_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDescriptor)


def test_logiclanguage_typedescriptor_constructor_exists():
    assert callable(logiclanguage_TypeDescriptor.__init__)


def test_logiclanguage_typedescriptor_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_numericoperation_is_not_abstract():
    assert not inspect.isabstract(NumericOperation)


def test_numericoperation_constructor_exists():
    assert callable(NumericOperation.__init__)


def test_numericoperation_constructor_args():
    sig = inspect.signature(NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_divison_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Divison)


def test_logiclanguage_divison_constructor_exists():
    assert callable(logiclanguage_Divison.__init__)


def test_logiclanguage_divison_constructor_args():
    sig = inspect.signature(logiclanguage_Divison.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_mod_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Mod)


def test_logiclanguage_mod_constructor_exists():
    assert callable(logiclanguage_Mod.__init__)


def test_logiclanguage_mod_constructor_args():
    sig = inspect.signature(logiclanguage_Mod.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_multiply_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Multiply)


def test_logiclanguage_multiply_constructor_exists():
    assert callable(logiclanguage_Multiply.__init__)


def test_logiclanguage_multiply_constructor_args():
    sig = inspect.signature(logiclanguage_Multiply.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_pow_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Pow)


def test_logiclanguage_pow_constructor_exists():
    assert callable(logiclanguage_Pow.__init__)


def test_logiclanguage_pow_constructor_args():
    sig = inspect.signature(logiclanguage_Pow.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_minus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Minus)


def test_logiclanguage_minus_constructor_exists():
    assert callable(logiclanguage_Minus.__init__)


def test_logiclanguage_minus_constructor_args():
    sig = inspect.signature(logiclanguage_Minus.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_plus_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Plus)


def test_logiclanguage_plus_constructor_exists():
    assert callable(logiclanguage_Plus.__init__)


def test_logiclanguage_plus_constructor_args():
    sig = inspect.signature(logiclanguage_Plus.__init__)
    params = list(sig.parameters.keys())



def test_booloperation_is_not_abstract():
    assert not inspect.isabstract(BoolOperation)


def test_booloperation_constructor_exists():
    assert callable(BoolOperation.__init__)


def test_booloperation_constructor_args():
    sig = inspect.signature(BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_or_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Or)


def test_logiclanguage_or_constructor_exists():
    assert callable(logiclanguage_Or.__init__)


def test_logiclanguage_or_constructor_args():
    sig = inspect.signature(logiclanguage_Or.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_not_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Not)


def test_logiclanguage_not_constructor_exists():
    assert callable(logiclanguage_Not.__init__)


def test_logiclanguage_not_constructor_args():
    sig = inspect.signature(logiclanguage_Not.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_iff_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Iff)


def test_logiclanguage_iff_constructor_exists():
    assert callable(logiclanguage_Iff.__init__)


def test_logiclanguage_iff_constructor_args():
    sig = inspect.signature(logiclanguage_Iff.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_impl_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Impl)


def test_logiclanguage_impl_constructor_exists():
    assert callable(logiclanguage_Impl.__init__)


def test_logiclanguage_impl_constructor_args():
    sig = inspect.signature(logiclanguage_Impl.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_and_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_And)


def test_logiclanguage_and_constructor_exists():
    assert callable(logiclanguage_And.__init__)


def test_logiclanguage_and_constructor_args():
    sig = inspect.signature(logiclanguage_And.__init__)
    params = list(sig.parameters.keys())



def test_primitiverelation_is_not_abstract():
    assert not inspect.isabstract(PrimitiveRelation)


def test_primitiverelation_constructor_exists():
    assert callable(PrimitiveRelation.__init__)


def test_primitiverelation_constructor_args():
    sig = inspect.signature(PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_moreorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_MoreOrEqualThan)


def test_logiclanguage_moreorequalthan_constructor_exists():
    assert callable(logiclanguage_MoreOrEqualThan.__init__)


def test_logiclanguage_moreorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage_MoreOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_lessorequalthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_LessOrEqualThan)


def test_logiclanguage_lessorequalthan_constructor_exists():
    assert callable(logiclanguage_LessOrEqualThan.__init__)


def test_logiclanguage_lessorequalthan_constructor_args():
    sig = inspect.signature(logiclanguage_LessOrEqualThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_distinct_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Distinct)


def test_logiclanguage_distinct_constructor_exists():
    assert callable(logiclanguage_Distinct.__init__)


def test_logiclanguage_distinct_constructor_args():
    sig = inspect.signature(logiclanguage_Distinct.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_lessthan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_LessThan)


def test_logiclanguage_lessthan_constructor_exists():
    assert callable(logiclanguage_LessThan.__init__)


def test_logiclanguage_lessthan_constructor_args():
    sig = inspect.signature(logiclanguage_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_morethan_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_MoreThan)


def test_logiclanguage_morethan_constructor_exists():
    assert callable(logiclanguage_MoreThan.__init__)


def test_logiclanguage_morethan_constructor_args():
    sig = inspect.signature(logiclanguage_MoreThan.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_equals_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Equals)


def test_logiclanguage_equals_constructor_exists():
    assert callable(logiclanguage_Equals.__init__)


def test_logiclanguage_equals_constructor_args():
    sig = inspect.signature(logiclanguage_Equals.__init__)
    params = list(sig.parameters.keys())



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_primitiverelation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_PrimitiveRelation)


def test_logiclanguage_primitiverelation_constructor_exists():
    assert callable(logiclanguage_PrimitiveRelation.__init__)


def test_logiclanguage_primitiverelation_constructor_args():
    sig = inspect.signature(logiclanguage_PrimitiveRelation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IfThenElse)


def test_logiclanguage_ifthenelse_constructor_exists():
    assert callable(logiclanguage_IfThenElse.__init__)


def test_logiclanguage_ifthenelse_constructor_args():
    sig = inspect.signature(logiclanguage_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_booloperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolOperation)


def test_logiclanguage_booloperation_constructor_exists():
    assert callable(logiclanguage_BoolOperation.__init__)


def test_logiclanguage_booloperation_constructor_args():
    sig = inspect.signature(logiclanguage_BoolOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_numericoperation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_NumericOperation)


def test_logiclanguage_numericoperation_constructor_exists():
    assert callable(logiclanguage_NumericOperation.__init__)


def test_logiclanguage_numericoperation_constructor_args():
    sig = inspect.signature(logiclanguage_NumericOperation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_unknownbecauseuninterpreted_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_UnknownBecauseUninterpreted)


def test_logiclanguage_unknownbecauseuninterpreted_constructor_exists():
    assert callable(logiclanguage_UnknownBecauseUninterpreted.__init__)


def test_logiclanguage_unknownbecauseuninterpreted_constructor_args():
    sig = inspect.signature(logiclanguage_UnknownBecauseUninterpreted.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_aggregateexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AggregateExpression)


def test_logiclanguage_aggregateexpression_constructor_exists():
    assert callable(logiclanguage_AggregateExpression.__init__)


def test_logiclanguage_aggregateexpression_constructor_args():
    sig = inspect.signature(logiclanguage_AggregateExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_transitiveclosure_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TransitiveClosure)


def test_logiclanguage_transitiveclosure_constructor_exists():
    assert callable(logiclanguage_TransitiveClosure.__init__)


def test_logiclanguage_transitiveclosure_constructor_args():
    sig = inspect.signature(logiclanguage_TransitiveClosure.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_instanceof_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_InstanceOf)


def test_logiclanguage_instanceof_constructor_exists():
    assert callable(logiclanguage_InstanceOf.__init__)


def test_logiclanguage_instanceof_constructor_args():
    sig = inspect.signature(logiclanguage_InstanceOf.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_symbolicvalue_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_SymbolicValue)


def test_logiclanguage_symbolicvalue_constructor_exists():
    assert callable(logiclanguage_SymbolicValue.__init__)


def test_logiclanguage_symbolicvalue_constructor_args():
    sig = inspect.signature(logiclanguage_SymbolicValue.__init__)
    params = list(sig.parameters.keys())



def test_termdescription_is_not_abstract():
    assert not inspect.isabstract(TermDescription)


def test_termdescription_constructor_exists():
    assert callable(TermDescription.__init__)


def test_termdescription_constructor_args():
    sig = inspect.signature(TermDescription.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_SymbolicDeclaration)


def test_logiclanguage_symbolicdeclaration_constructor_exists():
    assert callable(logiclanguage_SymbolicDeclaration.__init__)


def test_logiclanguage_symbolicdeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage_symbolicdeclaration_has_name():
    assert hasattr(logiclanguage_SymbolicDeclaration, "name")
    descriptor = None
    for klass in logiclanguage_SymbolicDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_term_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Term)


def test_logiclanguage_term_constructor_exists():
    assert callable(logiclanguage_Term.__init__)


def test_logiclanguage_term_constructor_args():
    sig = inspect.signature(logiclanguage_Term.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_functionannotation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_FunctionAnnotation)


def test_logiclanguage_functionannotation_constructor_exists():
    assert callable(logiclanguage_FunctionAnnotation.__init__)


def test_logiclanguage_functionannotation_constructor_args():
    sig = inspect.signature(logiclanguage_FunctionAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(PrimitiveTypeReference)


def test_primitivetypereference_constructor_exists():
    assert callable(PrimitiveTypeReference.__init__)


def test_primitivetypereference_constructor_args():
    sig = inspect.signature(PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_stringtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_StringTypeReference)


def test_logiclanguage_stringtypereference_constructor_exists():
    assert callable(logiclanguage_StringTypeReference.__init__)


def test_logiclanguage_stringtypereference_constructor_args():
    sig = inspect.signature(logiclanguage_StringTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_realtypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RealTypeReference)


def test_logiclanguage_realtypereference_constructor_exists():
    assert callable(logiclanguage_RealTypeReference.__init__)


def test_logiclanguage_realtypereference_constructor_args():
    sig = inspect.signature(logiclanguage_RealTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_booltypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolTypeReference)


def test_logiclanguage_booltypereference_constructor_exists():
    assert callable(logiclanguage_BoolTypeReference.__init__)


def test_logiclanguage_booltypereference_constructor_args():
    sig = inspect.signature(logiclanguage_BoolTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_inttypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IntTypeReference)


def test_logiclanguage_inttypereference_constructor_exists():
    assert callable(logiclanguage_IntTypeReference.__init__)


def test_logiclanguage_inttypereference_constructor_args():
    sig = inspect.signature(logiclanguage_IntTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(QuantifiedExpression)


def test_quantifiedexpression_constructor_exists():
    assert callable(QuantifiedExpression.__init__)


def test_quantifiedexpression_constructor_args():
    sig = inspect.signature(QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_forall_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Forall)


def test_logiclanguage_forall_constructor_exists():
    assert callable(logiclanguage_Forall.__init__)


def test_logiclanguage_forall_constructor_args():
    sig = inspect.signature(logiclanguage_Forall.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_exists_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Exists)


def test_logiclanguage_exists_constructor_exists():
    assert callable(logiclanguage_Exists.__init__)


def test_logiclanguage_exists_constructor_args():
    sig = inspect.signature(logiclanguage_Exists.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_quantifiedexpression_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_QuantifiedExpression)


def test_logiclanguage_quantifiedexpression_constructor_exists():
    assert callable(logiclanguage_QuantifiedExpression.__init__)


def test_logiclanguage_quantifiedexpression_constructor_args():
    sig = inspect.signature(logiclanguage_QuantifiedExpression.__init__)
    params = list(sig.parameters.keys())



def test_atomicterm_is_not_abstract():
    assert not inspect.isabstract(AtomicTerm)


def test_atomicterm_constructor_exists():
    assert callable(AtomicTerm.__init__)


def test_atomicterm_constructor_args():
    sig = inspect.signature(AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_boolliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_BoolLiteral)


def test_logiclanguage_boolliteral_constructor_exists():
    assert callable(logiclanguage_BoolLiteral.__init__)


def test_logiclanguage_boolliteral_constructor_args():
    sig = inspect.signature(logiclanguage_BoolLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage_boolliteral_has_value():
    assert hasattr(logiclanguage_BoolLiteral, "value")
    descriptor = None
    for klass in logiclanguage_BoolLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_realliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_RealLiteral)


def test_logiclanguage_realliteral_constructor_exists():
    assert callable(logiclanguage_RealLiteral.__init__)


def test_logiclanguage_realliteral_constructor_args():
    sig = inspect.signature(logiclanguage_RealLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage_realliteral_has_value():
    assert hasattr(logiclanguage_RealLiteral, "value")
    descriptor = None
    for klass in logiclanguage_RealLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_stringliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_StringLiteral)


def test_logiclanguage_stringliteral_constructor_exists():
    assert callable(logiclanguage_StringLiteral.__init__)


def test_logiclanguage_stringliteral_constructor_args():
    sig = inspect.signature(logiclanguage_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage_stringliteral_has_value():
    assert hasattr(logiclanguage_StringLiteral, "value")
    descriptor = None
    for klass in logiclanguage_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_intliteral_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_IntLiteral)


def test_logiclanguage_intliteral_constructor_exists():
    assert callable(logiclanguage_IntLiteral.__init__)


def test_logiclanguage_intliteral_constructor_args():
    sig = inspect.signature(logiclanguage_IntLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_logiclanguage_intliteral_has_value():
    assert hasattr(logiclanguage_IntLiteral, "value")
    descriptor = None
    for klass in logiclanguage_IntLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_logiclanguage_atomicterm_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_AtomicTerm)


def test_logiclanguage_atomicterm_constructor_exists():
    assert callable(logiclanguage_AtomicTerm.__init__)


def test_logiclanguage_atomicterm_constructor_args():
    sig = inspect.signature(logiclanguage_AtomicTerm.__init__)
    params = list(sig.parameters.keys())



def test_typedescriptor_is_not_abstract():
    assert not inspect.isabstract(TypeDescriptor)


def test_typedescriptor_constructor_exists():
    assert callable(TypeDescriptor.__init__)


def test_typedescriptor_constructor_args():
    sig = inspect.signature(TypeDescriptor.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_type_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Type)


def test_logiclanguage_type_constructor_exists():
    assert callable(logiclanguage_Type.__init__)


def test_logiclanguage_type_constructor_args():
    sig = inspect.signature(logiclanguage_Type.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "name" in params, "Missing parameter 'name'"

def test_logiclanguage_type_has_isAbstract():
    assert hasattr(logiclanguage_Type, "isAbstract")
    descriptor = None
    for klass in logiclanguage_Type.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_logiclanguage_type_has_name():
    assert hasattr(logiclanguage_Type, "name")
    descriptor = None
    for klass in logiclanguage_Type.__mro__:
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



def test_logiclanguage_primitivetypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_PrimitiveTypeReference)


def test_logiclanguage_primitivetypereference_constructor_exists():
    assert callable(logiclanguage_PrimitiveTypeReference.__init__)


def test_logiclanguage_primitivetypereference_constructor_args():
    sig = inspect.signature(logiclanguage_PrimitiveTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_complextypereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_ComplexTypeReference)


def test_logiclanguage_complextypereference_constructor_exists():
    assert callable(logiclanguage_ComplexTypeReference.__init__)


def test_logiclanguage_complextypereference_constructor_args():
    sig = inspect.signature(logiclanguage_ComplexTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_typereference_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeReference)


def test_logiclanguage_typereference_constructor_exists():
    assert callable(logiclanguage_TypeReference.__init__)


def test_logiclanguage_typereference_constructor_args():
    sig = inspect.signature(logiclanguage_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDeclaration)


def test_logiclanguage_typedeclaration_constructor_exists():
    assert callable(logiclanguage_TypeDeclaration.__init__)


def test_logiclanguage_typedeclaration_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_typedefinition_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_TypeDefinition)


def test_logiclanguage_typedefinition_constructor_exists():
    assert callable(logiclanguage_TypeDefinition.__init__)


def test_logiclanguage_typedefinition_constructor_args():
    sig = inspect.signature(logiclanguage_TypeDefinition.__init__)
    params = list(sig.parameters.keys())



def test_symbolicdeclaration_is_not_abstract():
    assert not inspect.isabstract(SymbolicDeclaration)


def test_symbolicdeclaration_constructor_exists():
    assert callable(SymbolicDeclaration.__init__)


def test_symbolicdeclaration_constructor_args():
    sig = inspect.signature(SymbolicDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_variable_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Variable)


def test_logiclanguage_variable_constructor_exists():
    assert callable(logiclanguage_Variable.__init__)


def test_logiclanguage_variable_constructor_args():
    sig = inspect.signature(logiclanguage_Variable.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_constant_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Constant)


def test_logiclanguage_constant_constructor_exists():
    assert callable(logiclanguage_Constant.__init__)


def test_logiclanguage_constant_constructor_args():
    sig = inspect.signature(logiclanguage_Constant.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_relation_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Relation)


def test_logiclanguage_relation_constructor_exists():
    assert callable(logiclanguage_Relation.__init__)


def test_logiclanguage_relation_constructor_args():
    sig = inspect.signature(logiclanguage_Relation.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_function_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_Function)


def test_logiclanguage_function_constructor_exists():
    assert callable(logiclanguage_Function.__init__)


def test_logiclanguage_function_constructor_args():
    sig = inspect.signature(logiclanguage_Function.__init__)
    params = list(sig.parameters.keys())



def test_logiclanguage_definedelement_is_not_abstract():
    assert not inspect.isabstract(logiclanguage_DefinedElement)


def test_logiclanguage_definedelement_constructor_exists():
    assert callable(logiclanguage_DefinedElement.__init__)


def test_logiclanguage_definedelement_constructor_args():
    sig = inspect.signature(logiclanguage_DefinedElement.__init__)
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
logiclanguage_ProjectedAggregateExpression_strategy = st.builds(
    logiclanguage_ProjectedAggregateExpression,
    projectionIndex=
        st.integers()
)
logiclanguage_Count_strategy = st.builds(
    logiclanguage_Count,
)
ProjectedAggregateExpression_strategy = st.builds(
    ProjectedAggregateExpression,
)
logiclanguage_Max_strategy = st.builds(
    logiclanguage_Max,
)
logiclanguage_Min_strategy = st.builds(
    logiclanguage_Min,
)
logiclanguage_Sum_strategy = st.builds(
    logiclanguage_Sum,
)
logiclanguage_AggregatedParameterSubstitution_strategy = st.builds(
    logiclanguage_AggregatedParameterSubstitution,
)
Relation_strategy = st.builds(
    Relation,
)
logiclanguage_RelationDefinition_strategy = st.builds(
    logiclanguage_RelationDefinition,
)
Constant_strategy = st.builds(
    Constant,
)
logiclanguage_ConstantDeclaration_strategy = st.builds(
    logiclanguage_ConstantDeclaration,
)
logiclanguage_ConstantDefinition_strategy = st.builds(
    logiclanguage_ConstantDefinition,
)
logiclanguage_ConstantAnnotation_strategy = st.builds(
    logiclanguage_ConstantAnnotation,
)
Function_strategy = st.builds(
    Function,
)
logiclanguage_FunctionDeclaration_strategy = st.builds(
    logiclanguage_FunctionDeclaration,
)
logiclanguage_FunctionDefinition_strategy = st.builds(
    logiclanguage_FunctionDefinition,
)
logiclanguage_RelationDeclaration_strategy = st.builds(
    logiclanguage_RelationDeclaration,
)
logiclanguage_RelationAnnotation_strategy = st.builds(
    logiclanguage_RelationAnnotation,
)
logiclanguage_AssertionAnnotation_strategy = st.builds(
    logiclanguage_AssertionAnnotation,
)
logiclanguage_Assertion_strategy = st.builds(
    logiclanguage_Assertion,
    name=
        safe_text
)
logiclanguage_TermDescription_strategy = st.builds(
    logiclanguage_TermDescription,
)
logiclanguage_TypeDescriptor_strategy = st.builds(
    logiclanguage_TypeDescriptor,
)
NumericOperation_strategy = st.builds(
    NumericOperation,
)
logiclanguage_Divison_strategy = st.builds(
    logiclanguage_Divison,
)
logiclanguage_Mod_strategy = st.builds(
    logiclanguage_Mod,
)
logiclanguage_Multiply_strategy = st.builds(
    logiclanguage_Multiply,
)
logiclanguage_Pow_strategy = st.builds(
    logiclanguage_Pow,
)
logiclanguage_Minus_strategy = st.builds(
    logiclanguage_Minus,
)
logiclanguage_Plus_strategy = st.builds(
    logiclanguage_Plus,
)
BoolOperation_strategy = st.builds(
    BoolOperation,
)
logiclanguage_Or_strategy = st.builds(
    logiclanguage_Or,
)
logiclanguage_Not_strategy = st.builds(
    logiclanguage_Not,
)
logiclanguage_Iff_strategy = st.builds(
    logiclanguage_Iff,
)
logiclanguage_Impl_strategy = st.builds(
    logiclanguage_Impl,
)
logiclanguage_And_strategy = st.builds(
    logiclanguage_And,
)
PrimitiveRelation_strategy = st.builds(
    PrimitiveRelation,
)
logiclanguage_MoreOrEqualThan_strategy = st.builds(
    logiclanguage_MoreOrEqualThan,
)
logiclanguage_LessOrEqualThan_strategy = st.builds(
    logiclanguage_LessOrEqualThan,
)
logiclanguage_Distinct_strategy = st.builds(
    logiclanguage_Distinct,
)
logiclanguage_LessThan_strategy = st.builds(
    logiclanguage_LessThan,
)
logiclanguage_MoreThan_strategy = st.builds(
    logiclanguage_MoreThan,
)
logiclanguage_Equals_strategy = st.builds(
    logiclanguage_Equals,
)
Term_strategy = st.builds(
    Term,
)
logiclanguage_PrimitiveRelation_strategy = st.builds(
    logiclanguage_PrimitiveRelation,
)
logiclanguage_IfThenElse_strategy = st.builds(
    logiclanguage_IfThenElse,
)
logiclanguage_BoolOperation_strategy = st.builds(
    logiclanguage_BoolOperation,
)
logiclanguage_NumericOperation_strategy = st.builds(
    logiclanguage_NumericOperation,
)
logiclanguage_UnknownBecauseUninterpreted_strategy = st.builds(
    logiclanguage_UnknownBecauseUninterpreted,
)
logiclanguage_AggregateExpression_strategy = st.builds(
    logiclanguage_AggregateExpression,
)
logiclanguage_TransitiveClosure_strategy = st.builds(
    logiclanguage_TransitiveClosure,
)
logiclanguage_InstanceOf_strategy = st.builds(
    logiclanguage_InstanceOf,
)
logiclanguage_SymbolicValue_strategy = st.builds(
    logiclanguage_SymbolicValue,
)
TermDescription_strategy = st.builds(
    TermDescription,
)
logiclanguage_SymbolicDeclaration_strategy = st.builds(
    logiclanguage_SymbolicDeclaration,
    name=
        safe_text
)
logiclanguage_Term_strategy = st.builds(
    logiclanguage_Term,
)
logiclanguage_FunctionAnnotation_strategy = st.builds(
    logiclanguage_FunctionAnnotation,
)
PrimitiveTypeReference_strategy = st.builds(
    PrimitiveTypeReference,
)
logiclanguage_StringTypeReference_strategy = st.builds(
    logiclanguage_StringTypeReference,
)
logiclanguage_RealTypeReference_strategy = st.builds(
    logiclanguage_RealTypeReference,
)
logiclanguage_BoolTypeReference_strategy = st.builds(
    logiclanguage_BoolTypeReference,
)
logiclanguage_IntTypeReference_strategy = st.builds(
    logiclanguage_IntTypeReference,
)
QuantifiedExpression_strategy = st.builds(
    QuantifiedExpression,
)
logiclanguage_Forall_strategy = st.builds(
    logiclanguage_Forall,
)
logiclanguage_Exists_strategy = st.builds(
    logiclanguage_Exists,
)
logiclanguage_QuantifiedExpression_strategy = st.builds(
    logiclanguage_QuantifiedExpression,
)
AtomicTerm_strategy = st.builds(
    AtomicTerm,
)
logiclanguage_BoolLiteral_strategy = st.builds(
    logiclanguage_BoolLiteral,
    value=
        st.booleans()
)
logiclanguage_RealLiteral_strategy = st.builds(
    logiclanguage_RealLiteral,
    value=
        safe_text
)
logiclanguage_StringLiteral_strategy = st.builds(
    logiclanguage_StringLiteral,
    value=
        safe_text
)
logiclanguage_IntLiteral_strategy = st.builds(
    logiclanguage_IntLiteral,
    value=
        st.integers()
)
logiclanguage_AtomicTerm_strategy = st.builds(
    logiclanguage_AtomicTerm,
)
TypeDescriptor_strategy = st.builds(
    TypeDescriptor,
)
logiclanguage_Type_strategy = st.builds(
    logiclanguage_Type,
    isAbstract=
        st.booleans(),
    name=
        safe_text
)
TypeReference_strategy = st.builds(
    TypeReference,
)
logiclanguage_PrimitiveTypeReference_strategy = st.builds(
    logiclanguage_PrimitiveTypeReference,
)
logiclanguage_ComplexTypeReference_strategy = st.builds(
    logiclanguage_ComplexTypeReference,
)
logiclanguage_TypeReference_strategy = st.builds(
    logiclanguage_TypeReference,
)
Type_strategy = st.builds(
    Type,
)
logiclanguage_TypeDeclaration_strategy = st.builds(
    logiclanguage_TypeDeclaration,
)
logiclanguage_TypeDefinition_strategy = st.builds(
    logiclanguage_TypeDefinition,
)
SymbolicDeclaration_strategy = st.builds(
    SymbolicDeclaration,
)
logiclanguage_Variable_strategy = st.builds(
    logiclanguage_Variable,
)
logiclanguage_Constant_strategy = st.builds(
    logiclanguage_Constant,
)
logiclanguage_Relation_strategy = st.builds(
    logiclanguage_Relation,
)
logiclanguage_Function_strategy = st.builds(
    logiclanguage_Function,
)
logiclanguage_DefinedElement_strategy = st.builds(
    logiclanguage_DefinedElement,
)

@given(instance=AggregateExpression_strategy)
@settings(max_examples=50)
def test_aggregateexpression_instantiation(instance):
    assert isinstance(instance, AggregateExpression)

@given(instance=logiclanguage_ProjectedAggregateExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage_projectedaggregateexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_ProjectedAggregateExpression)



@given(instance=logiclanguage_ProjectedAggregateExpression_strategy)
def test_logiclanguage_projectedaggregateexpression_projectionIndex_setter(instance):
    original = instance.projectionIndex
    instance.projectionIndex = original
    assert instance.projectionIndex == original

@given(instance=logiclanguage_Count_strategy)
@settings(max_examples=50)
def test_logiclanguage_count_instantiation(instance):
    assert isinstance(instance, logiclanguage_Count)

@given(instance=ProjectedAggregateExpression_strategy)
@settings(max_examples=50)
def test_projectedaggregateexpression_instantiation(instance):
    assert isinstance(instance, ProjectedAggregateExpression)

@given(instance=logiclanguage_Max_strategy)
@settings(max_examples=50)
def test_logiclanguage_max_instantiation(instance):
    assert isinstance(instance, logiclanguage_Max)

@given(instance=logiclanguage_Min_strategy)
@settings(max_examples=50)
def test_logiclanguage_min_instantiation(instance):
    assert isinstance(instance, logiclanguage_Min)

@given(instance=logiclanguage_Sum_strategy)
@settings(max_examples=50)
def test_logiclanguage_sum_instantiation(instance):
    assert isinstance(instance, logiclanguage_Sum)

@given(instance=logiclanguage_AggregatedParameterSubstitution_strategy)
@settings(max_examples=50)
def test_logiclanguage_aggregatedparametersubstitution_instantiation(instance):
    assert isinstance(instance, logiclanguage_AggregatedParameterSubstitution)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=logiclanguage_RelationDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage_relationdefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationDefinition)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=logiclanguage_ConstantDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage_constantdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantDeclaration)

@given(instance=logiclanguage_ConstantDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage_constantdefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantDefinition)

@given(instance=logiclanguage_ConstantAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage_constantannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_ConstantAnnotation)

@given(instance=Function_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, Function)

@given(instance=logiclanguage_FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage_functiondeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionDeclaration)

@given(instance=logiclanguage_FunctionDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage_functiondefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionDefinition)

@given(instance=logiclanguage_RelationDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage_relationdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationDeclaration)

@given(instance=logiclanguage_RelationAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage_relationannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_RelationAnnotation)

@given(instance=logiclanguage_AssertionAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage_assertionannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_AssertionAnnotation)

@given(instance=logiclanguage_Assertion_strategy)
@settings(max_examples=50)
def test_logiclanguage_assertion_instantiation(instance):
    assert isinstance(instance, logiclanguage_Assertion)



@given(instance=logiclanguage_Assertion_strategy)
def test_logiclanguage_assertion_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logiclanguage_TermDescription_strategy)
@settings(max_examples=50)
def test_logiclanguage_termdescription_instantiation(instance):
    assert isinstance(instance, logiclanguage_TermDescription)

@given(instance=logiclanguage_TypeDescriptor_strategy)
@settings(max_examples=50)
def test_logiclanguage_typedescriptor_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDescriptor)

@given(instance=NumericOperation_strategy)
@settings(max_examples=50)
def test_numericoperation_instantiation(instance):
    assert isinstance(instance, NumericOperation)

@given(instance=logiclanguage_Divison_strategy)
@settings(max_examples=50)
def test_logiclanguage_divison_instantiation(instance):
    assert isinstance(instance, logiclanguage_Divison)

@given(instance=logiclanguage_Mod_strategy)
@settings(max_examples=50)
def test_logiclanguage_mod_instantiation(instance):
    assert isinstance(instance, logiclanguage_Mod)

@given(instance=logiclanguage_Multiply_strategy)
@settings(max_examples=50)
def test_logiclanguage_multiply_instantiation(instance):
    assert isinstance(instance, logiclanguage_Multiply)

@given(instance=logiclanguage_Pow_strategy)
@settings(max_examples=50)
def test_logiclanguage_pow_instantiation(instance):
    assert isinstance(instance, logiclanguage_Pow)

@given(instance=logiclanguage_Minus_strategy)
@settings(max_examples=50)
def test_logiclanguage_minus_instantiation(instance):
    assert isinstance(instance, logiclanguage_Minus)

@given(instance=logiclanguage_Plus_strategy)
@settings(max_examples=50)
def test_logiclanguage_plus_instantiation(instance):
    assert isinstance(instance, logiclanguage_Plus)

@given(instance=BoolOperation_strategy)
@settings(max_examples=50)
def test_booloperation_instantiation(instance):
    assert isinstance(instance, BoolOperation)

@given(instance=logiclanguage_Or_strategy)
@settings(max_examples=50)
def test_logiclanguage_or_instantiation(instance):
    assert isinstance(instance, logiclanguage_Or)

@given(instance=logiclanguage_Not_strategy)
@settings(max_examples=50)
def test_logiclanguage_not_instantiation(instance):
    assert isinstance(instance, logiclanguage_Not)

@given(instance=logiclanguage_Iff_strategy)
@settings(max_examples=50)
def test_logiclanguage_iff_instantiation(instance):
    assert isinstance(instance, logiclanguage_Iff)

@given(instance=logiclanguage_Impl_strategy)
@settings(max_examples=50)
def test_logiclanguage_impl_instantiation(instance):
    assert isinstance(instance, logiclanguage_Impl)

@given(instance=logiclanguage_And_strategy)
@settings(max_examples=50)
def test_logiclanguage_and_instantiation(instance):
    assert isinstance(instance, logiclanguage_And)

@given(instance=PrimitiveRelation_strategy)
@settings(max_examples=50)
def test_primitiverelation_instantiation(instance):
    assert isinstance(instance, PrimitiveRelation)

@given(instance=logiclanguage_MoreOrEqualThan_strategy)
@settings(max_examples=50)
def test_logiclanguage_moreorequalthan_instantiation(instance):
    assert isinstance(instance, logiclanguage_MoreOrEqualThan)

@given(instance=logiclanguage_LessOrEqualThan_strategy)
@settings(max_examples=50)
def test_logiclanguage_lessorequalthan_instantiation(instance):
    assert isinstance(instance, logiclanguage_LessOrEqualThan)

@given(instance=logiclanguage_Distinct_strategy)
@settings(max_examples=50)
def test_logiclanguage_distinct_instantiation(instance):
    assert isinstance(instance, logiclanguage_Distinct)

@given(instance=logiclanguage_LessThan_strategy)
@settings(max_examples=50)
def test_logiclanguage_lessthan_instantiation(instance):
    assert isinstance(instance, logiclanguage_LessThan)

@given(instance=logiclanguage_MoreThan_strategy)
@settings(max_examples=50)
def test_logiclanguage_morethan_instantiation(instance):
    assert isinstance(instance, logiclanguage_MoreThan)

@given(instance=logiclanguage_Equals_strategy)
@settings(max_examples=50)
def test_logiclanguage_equals_instantiation(instance):
    assert isinstance(instance, logiclanguage_Equals)

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=logiclanguage_PrimitiveRelation_strategy)
@settings(max_examples=50)
def test_logiclanguage_primitiverelation_instantiation(instance):
    assert isinstance(instance, logiclanguage_PrimitiveRelation)

@given(instance=logiclanguage_IfThenElse_strategy)
@settings(max_examples=50)
def test_logiclanguage_ifthenelse_instantiation(instance):
    assert isinstance(instance, logiclanguage_IfThenElse)

@given(instance=logiclanguage_BoolOperation_strategy)
@settings(max_examples=50)
def test_logiclanguage_booloperation_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolOperation)

@given(instance=logiclanguage_NumericOperation_strategy)
@settings(max_examples=50)
def test_logiclanguage_numericoperation_instantiation(instance):
    assert isinstance(instance, logiclanguage_NumericOperation)

@given(instance=logiclanguage_UnknownBecauseUninterpreted_strategy)
@settings(max_examples=50)
def test_logiclanguage_unknownbecauseuninterpreted_instantiation(instance):
    assert isinstance(instance, logiclanguage_UnknownBecauseUninterpreted)

@given(instance=logiclanguage_AggregateExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage_aggregateexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_AggregateExpression)

@given(instance=logiclanguage_TransitiveClosure_strategy)
@settings(max_examples=50)
def test_logiclanguage_transitiveclosure_instantiation(instance):
    assert isinstance(instance, logiclanguage_TransitiveClosure)

@given(instance=logiclanguage_InstanceOf_strategy)
@settings(max_examples=50)
def test_logiclanguage_instanceof_instantiation(instance):
    assert isinstance(instance, logiclanguage_InstanceOf)

@given(instance=logiclanguage_SymbolicValue_strategy)
@settings(max_examples=50)
def test_logiclanguage_symbolicvalue_instantiation(instance):
    assert isinstance(instance, logiclanguage_SymbolicValue)

@given(instance=TermDescription_strategy)
@settings(max_examples=50)
def test_termdescription_instantiation(instance):
    assert isinstance(instance, TermDescription)

@given(instance=logiclanguage_SymbolicDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage_symbolicdeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_SymbolicDeclaration)



@given(instance=logiclanguage_SymbolicDeclaration_strategy)
def test_logiclanguage_symbolicdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=logiclanguage_Term_strategy)
@settings(max_examples=50)
def test_logiclanguage_term_instantiation(instance):
    assert isinstance(instance, logiclanguage_Term)

@given(instance=logiclanguage_FunctionAnnotation_strategy)
@settings(max_examples=50)
def test_logiclanguage_functionannotation_instantiation(instance):
    assert isinstance(instance, logiclanguage_FunctionAnnotation)

@given(instance=PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_primitivetypereference_instantiation(instance):
    assert isinstance(instance, PrimitiveTypeReference)

@given(instance=logiclanguage_StringTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_stringtypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_StringTypeReference)

@given(instance=logiclanguage_RealTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_realtypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_RealTypeReference)

@given(instance=logiclanguage_BoolTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_booltypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolTypeReference)

@given(instance=logiclanguage_IntTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_inttypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_IntTypeReference)

@given(instance=QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_quantifiedexpression_instantiation(instance):
    assert isinstance(instance, QuantifiedExpression)

@given(instance=logiclanguage_Forall_strategy)
@settings(max_examples=50)
def test_logiclanguage_forall_instantiation(instance):
    assert isinstance(instance, logiclanguage_Forall)

@given(instance=logiclanguage_Exists_strategy)
@settings(max_examples=50)
def test_logiclanguage_exists_instantiation(instance):
    assert isinstance(instance, logiclanguage_Exists)

@given(instance=logiclanguage_QuantifiedExpression_strategy)
@settings(max_examples=50)
def test_logiclanguage_quantifiedexpression_instantiation(instance):
    assert isinstance(instance, logiclanguage_QuantifiedExpression)

@given(instance=AtomicTerm_strategy)
@settings(max_examples=50)
def test_atomicterm_instantiation(instance):
    assert isinstance(instance, AtomicTerm)

@given(instance=logiclanguage_BoolLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage_boolliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_BoolLiteral)



@given(instance=logiclanguage_BoolLiteral_strategy)
def test_logiclanguage_boolliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage_RealLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage_realliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_RealLiteral)



@given(instance=logiclanguage_RealLiteral_strategy)
def test_logiclanguage_realliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage_StringLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage_stringliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_StringLiteral)



@given(instance=logiclanguage_StringLiteral_strategy)
def test_logiclanguage_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage_IntLiteral_strategy)
@settings(max_examples=50)
def test_logiclanguage_intliteral_instantiation(instance):
    assert isinstance(instance, logiclanguage_IntLiteral)



@given(instance=logiclanguage_IntLiteral_strategy)
def test_logiclanguage_intliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=logiclanguage_AtomicTerm_strategy)
@settings(max_examples=50)
def test_logiclanguage_atomicterm_instantiation(instance):
    assert isinstance(instance, logiclanguage_AtomicTerm)

@given(instance=TypeDescriptor_strategy)
@settings(max_examples=50)
def test_typedescriptor_instantiation(instance):
    assert isinstance(instance, TypeDescriptor)

@given(instance=logiclanguage_Type_strategy)
@settings(max_examples=50)
def test_logiclanguage_type_instantiation(instance):
    assert isinstance(instance, logiclanguage_Type)



@given(instance=logiclanguage_Type_strategy)
def test_logiclanguage_type_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=logiclanguage_Type_strategy)
def test_logiclanguage_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TypeReference_strategy)
@settings(max_examples=50)
def test_typereference_instantiation(instance):
    assert isinstance(instance, TypeReference)

@given(instance=logiclanguage_PrimitiveTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_primitivetypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_PrimitiveTypeReference)

@given(instance=logiclanguage_ComplexTypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_complextypereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_ComplexTypeReference)

@given(instance=logiclanguage_TypeReference_strategy)
@settings(max_examples=50)
def test_logiclanguage_typereference_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=logiclanguage_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_logiclanguage_typedeclaration_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDeclaration)

@given(instance=logiclanguage_TypeDefinition_strategy)
@settings(max_examples=50)
def test_logiclanguage_typedefinition_instantiation(instance):
    assert isinstance(instance, logiclanguage_TypeDefinition)

@given(instance=SymbolicDeclaration_strategy)
@settings(max_examples=50)
def test_symbolicdeclaration_instantiation(instance):
    assert isinstance(instance, SymbolicDeclaration)

@given(instance=logiclanguage_Variable_strategy)
@settings(max_examples=50)
def test_logiclanguage_variable_instantiation(instance):
    assert isinstance(instance, logiclanguage_Variable)

@given(instance=logiclanguage_Constant_strategy)
@settings(max_examples=50)
def test_logiclanguage_constant_instantiation(instance):
    assert isinstance(instance, logiclanguage_Constant)

@given(instance=logiclanguage_Relation_strategy)
@settings(max_examples=50)
def test_logiclanguage_relation_instantiation(instance):
    assert isinstance(instance, logiclanguage_Relation)

@given(instance=logiclanguage_Function_strategy)
@settings(max_examples=50)
def test_logiclanguage_function_instantiation(instance):
    assert isinstance(instance, logiclanguage_Function)

@given(instance=logiclanguage_DefinedElement_strategy)
@settings(max_examples=50)
def test_logiclanguage_definedelement_instantiation(instance):
    assert isinstance(instance, logiclanguage_DefinedElement)
