import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SOS::Condition,
    Variable,
    SOS::Conclusion,
    SOS::PremisseList,
    ADT,
    SetMembership,
    SOS::set::ForAllIn,
    SOS::set::ExistsIn,
    VariableRef,
    SetOperator,
    SOS::set::Excluding,
    SOS::set::Intersection,
    SOS::set::Union,
    set::SOS::AlgebraicConditionList,
    SOS::adtmm::AbstractEquation,
    SetTerm,
    SOS::set::ModelSet,
    SOS::set::SetOperator,
    SOS::set::SetConstructor,
    SOS::set::SetMembership,
    SOS::adtmm::AbstractOperation,
    SOS::adtmm::SortDeclaration,
    SOS::adtmm::AbstractSort,
    Sort,
    SOS::adtmm::AtomicSort,
    SOS::set::Set,
    SOS::set::ModelSort,
    AbstractOperation,
    SOS::adtmm::AbstractGenericOp,
    SOS::adtmm::Operation,
    SOS::adtmm::Sort,
    CondEquation,
    SOS::adtmm::Term,
    Equation,
    SOS::adtmm::CondEquation,
    SOS::adtmm::Variable,
    Term,
    SOS::set::ModelClassAttribute,
    SOS::adtmm::CTerm,
    SOS::set::SetTerm,
    SOS::set::ModelRelation,
    SOS::adtmm::VariableRef,
    Operation,
    SortDeclaration,
    SOS::adtmm::ADT,
    SOS::AlgebraicConditionList,
    AbstractEquation,
    SOS::adtmm::Inequation,
    SOS::adtmm::Equation,
    SOS::Rule,
    SOS::Semantics,
    Condition,
    SOS::TypeJudment,
    SOS::AlgebraicCondition,
    SOS::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sos::condition_is_not_abstract():
    assert not inspect.isabstract(SOS::Condition)


def test_sos::condition_constructor_exists():
    assert callable(SOS::Condition.__init__)


def test_sos::condition_constructor_args():
    sig = inspect.signature(SOS::Condition.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_sos::conclusion_is_not_abstract():
    assert not inspect.isabstract(SOS::Conclusion)


def test_sos::conclusion_constructor_exists():
    assert callable(SOS::Conclusion.__init__)


def test_sos::conclusion_constructor_args():
    sig = inspect.signature(SOS::Conclusion.__init__)
    params = list(sig.parameters.keys())



def test_sos::premisselist_is_not_abstract():
    assert not inspect.isabstract(SOS::PremisseList)


def test_sos::premisselist_constructor_exists():
    assert callable(SOS::PremisseList.__init__)


def test_sos::premisselist_constructor_args():
    sig = inspect.signature(SOS::PremisseList.__init__)
    params = list(sig.parameters.keys())



def test_adt_is_not_abstract():
    assert not inspect.isabstract(ADT)


def test_adt_constructor_exists():
    assert callable(ADT.__init__)


def test_adt_constructor_args():
    sig = inspect.signature(ADT.__init__)
    params = list(sig.parameters.keys())



def test_setmembership_is_not_abstract():
    assert not inspect.isabstract(SetMembership)


def test_setmembership_constructor_exists():
    assert callable(SetMembership.__init__)


def test_setmembership_constructor_args():
    sig = inspect.signature(SetMembership.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::forallin_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ForAllIn)


def test_sos::set::forallin_constructor_exists():
    assert callable(SOS::set::ForAllIn.__init__)


def test_sos::set::forallin_constructor_args():
    sig = inspect.signature(SOS::set::ForAllIn.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::existsin_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ExistsIn)


def test_sos::set::existsin_constructor_exists():
    assert callable(SOS::set::ExistsIn.__init__)


def test_sos::set::existsin_constructor_args():
    sig = inspect.signature(SOS::set::ExistsIn.__init__)
    params = list(sig.parameters.keys())



def test_variableref_is_not_abstract():
    assert not inspect.isabstract(VariableRef)


def test_variableref_constructor_exists():
    assert callable(VariableRef.__init__)


def test_variableref_constructor_args():
    sig = inspect.signature(VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_setoperator_is_not_abstract():
    assert not inspect.isabstract(SetOperator)


def test_setoperator_constructor_exists():
    assert callable(SetOperator.__init__)


def test_setoperator_constructor_args():
    sig = inspect.signature(SetOperator.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::excluding_is_not_abstract():
    assert not inspect.isabstract(SOS::set::Excluding)


def test_sos::set::excluding_constructor_exists():
    assert callable(SOS::set::Excluding.__init__)


def test_sos::set::excluding_constructor_args():
    sig = inspect.signature(SOS::set::Excluding.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::intersection_is_not_abstract():
    assert not inspect.isabstract(SOS::set::Intersection)


def test_sos::set::intersection_constructor_exists():
    assert callable(SOS::set::Intersection.__init__)


def test_sos::set::intersection_constructor_args():
    sig = inspect.signature(SOS::set::Intersection.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::union_is_not_abstract():
    assert not inspect.isabstract(SOS::set::Union)


def test_sos::set::union_constructor_exists():
    assert callable(SOS::set::Union.__init__)


def test_sos::set::union_constructor_args():
    sig = inspect.signature(SOS::set::Union.__init__)
    params = list(sig.parameters.keys())



def test_set::sos::algebraicconditionlist_is_not_abstract():
    assert not inspect.isabstract(set::SOS::AlgebraicConditionList)


def test_set::sos::algebraicconditionlist_constructor_exists():
    assert callable(set::SOS::AlgebraicConditionList.__init__)


def test_set::sos::algebraicconditionlist_constructor_args():
    sig = inspect.signature(set::SOS::AlgebraicConditionList.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::abstractequation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::AbstractEquation)


def test_sos::adtmm::abstractequation_constructor_exists():
    assert callable(SOS::adtmm::AbstractEquation.__init__)


def test_sos::adtmm::abstractequation_constructor_args():
    sig = inspect.signature(SOS::adtmm::AbstractEquation.__init__)
    params = list(sig.parameters.keys())



def test_setterm_is_not_abstract():
    assert not inspect.isabstract(SetTerm)


def test_setterm_constructor_exists():
    assert callable(SetTerm.__init__)


def test_setterm_constructor_args():
    sig = inspect.signature(SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::modelset_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ModelSet)


def test_sos::set::modelset_constructor_exists():
    assert callable(SOS::set::ModelSet.__init__)


def test_sos::set::modelset_constructor_args():
    sig = inspect.signature(SOS::set::ModelSet.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::setoperator_is_not_abstract():
    assert not inspect.isabstract(SOS::set::SetOperator)


def test_sos::set::setoperator_constructor_exists():
    assert callable(SOS::set::SetOperator.__init__)


def test_sos::set::setoperator_constructor_args():
    sig = inspect.signature(SOS::set::SetOperator.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::setconstructor_is_not_abstract():
    assert not inspect.isabstract(SOS::set::SetConstructor)


def test_sos::set::setconstructor_constructor_exists():
    assert callable(SOS::set::SetConstructor.__init__)


def test_sos::set::setconstructor_constructor_args():
    sig = inspect.signature(SOS::set::SetConstructor.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::setmembership_is_not_abstract():
    assert not inspect.isabstract(SOS::set::SetMembership)


def test_sos::set::setmembership_constructor_exists():
    assert callable(SOS::set::SetMembership.__init__)


def test_sos::set::setmembership_constructor_args():
    sig = inspect.signature(SOS::set::SetMembership.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::abstractoperation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::AbstractOperation)


def test_sos::adtmm::abstractoperation_constructor_exists():
    assert callable(SOS::adtmm::AbstractOperation.__init__)


def test_sos::adtmm::abstractoperation_constructor_args():
    sig = inspect.signature(SOS::adtmm::AbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos::adtmm::abstractoperation_has_name():
    assert hasattr(SOS::adtmm::AbstractOperation, "name")
    descriptor = None
    for klass in SOS::adtmm::AbstractOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos::adtmm::sortdeclaration_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::SortDeclaration)


def test_sos::adtmm::sortdeclaration_constructor_exists():
    assert callable(SOS::adtmm::SortDeclaration.__init__)


def test_sos::adtmm::sortdeclaration_constructor_args():
    sig = inspect.signature(SOS::adtmm::SortDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos::adtmm::sortdeclaration_has_name():
    assert hasattr(SOS::adtmm::SortDeclaration, "name")
    descriptor = None
    for klass in SOS::adtmm::SortDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos::adtmm::abstractsort_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::AbstractSort)


def test_sos::adtmm::abstractsort_constructor_exists():
    assert callable(SOS::adtmm::AbstractSort.__init__)


def test_sos::adtmm::abstractsort_constructor_args():
    sig = inspect.signature(SOS::adtmm::AbstractSort.__init__)
    params = list(sig.parameters.keys())



def test_sort_is_not_abstract():
    assert not inspect.isabstract(Sort)


def test_sort_constructor_exists():
    assert callable(Sort.__init__)


def test_sort_constructor_args():
    sig = inspect.signature(Sort.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::atomicsort_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::AtomicSort)


def test_sos::adtmm::atomicsort_constructor_exists():
    assert callable(SOS::adtmm::AtomicSort.__init__)


def test_sos::adtmm::atomicsort_constructor_args():
    sig = inspect.signature(SOS::adtmm::AtomicSort.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::set_is_not_abstract():
    assert not inspect.isabstract(SOS::set::Set)


def test_sos::set::set_constructor_exists():
    assert callable(SOS::set::Set.__init__)


def test_sos::set::set_constructor_args():
    sig = inspect.signature(SOS::set::Set.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::modelsort_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ModelSort)


def test_sos::set::modelsort_constructor_exists():
    assert callable(SOS::set::ModelSort.__init__)


def test_sos::set::modelsort_constructor_args():
    sig = inspect.signature(SOS::set::ModelSort.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "className" in params, "Missing parameter 'className'"

def test_sos::set::modelsort_has_packageName():
    assert hasattr(SOS::set::ModelSort, "packageName")
    descriptor = None
    for klass in SOS::set::ModelSort.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_sos::set::modelsort_has_className():
    assert hasattr(SOS::set::ModelSort, "className")
    descriptor = None
    for klass in SOS::set::ModelSort.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(AbstractOperation)


def test_abstractoperation_constructor_exists():
    assert callable(AbstractOperation.__init__)


def test_abstractoperation_constructor_args():
    sig = inspect.signature(AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::abstractgenericop_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::AbstractGenericOp)


def test_sos::adtmm::abstractgenericop_constructor_exists():
    assert callable(SOS::adtmm::AbstractGenericOp.__init__)


def test_sos::adtmm::abstractgenericop_constructor_args():
    sig = inspect.signature(SOS::adtmm::AbstractGenericOp.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::operation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Operation)


def test_sos::adtmm::operation_constructor_exists():
    assert callable(SOS::adtmm::Operation.__init__)


def test_sos::adtmm::operation_constructor_args():
    sig = inspect.signature(SOS::adtmm::Operation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::sort_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Sort)


def test_sos::adtmm::sort_constructor_exists():
    assert callable(SOS::adtmm::Sort.__init__)


def test_sos::adtmm::sort_constructor_args():
    sig = inspect.signature(SOS::adtmm::Sort.__init__)
    params = list(sig.parameters.keys())



def test_condequation_is_not_abstract():
    assert not inspect.isabstract(CondEquation)


def test_condequation_constructor_exists():
    assert callable(CondEquation.__init__)


def test_condequation_constructor_args():
    sig = inspect.signature(CondEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::term_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Term)


def test_sos::adtmm::term_constructor_exists():
    assert callable(SOS::adtmm::Term.__init__)


def test_sos::adtmm::term_constructor_args():
    sig = inspect.signature(SOS::adtmm::Term.__init__)
    params = list(sig.parameters.keys())



def test_equation_is_not_abstract():
    assert not inspect.isabstract(Equation)


def test_equation_constructor_exists():
    assert callable(Equation.__init__)


def test_equation_constructor_args():
    sig = inspect.signature(Equation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::condequation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::CondEquation)


def test_sos::adtmm::condequation_constructor_exists():
    assert callable(SOS::adtmm::CondEquation.__init__)


def test_sos::adtmm::condequation_constructor_args():
    sig = inspect.signature(SOS::adtmm::CondEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::variable_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Variable)


def test_sos::adtmm::variable_constructor_exists():
    assert callable(SOS::adtmm::Variable.__init__)


def test_sos::adtmm::variable_constructor_args():
    sig = inspect.signature(SOS::adtmm::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos::adtmm::variable_has_name():
    assert hasattr(SOS::adtmm::Variable, "name")
    descriptor = None
    for klass in SOS::adtmm::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_term_is_not_abstract():
    assert not inspect.isabstract(Term)


def test_term_constructor_exists():
    assert callable(Term.__init__)


def test_term_constructor_args():
    sig = inspect.signature(Term.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::modelclassattribute_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ModelClassAttribute)


def test_sos::set::modelclassattribute_constructor_exists():
    assert callable(SOS::set::ModelClassAttribute.__init__)


def test_sos::set::modelclassattribute_constructor_args():
    sig = inspect.signature(SOS::set::ModelClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_sos::set::modelclassattribute_has_attributeName():
    assert hasattr(SOS::set::ModelClassAttribute, "attributeName")
    descriptor = None
    for klass in SOS::set::ModelClassAttribute.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_sos::adtmm::cterm_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::CTerm)


def test_sos::adtmm::cterm_constructor_exists():
    assert callable(SOS::adtmm::CTerm.__init__)


def test_sos::adtmm::cterm_constructor_args():
    sig = inspect.signature(SOS::adtmm::CTerm.__init__)
    params = list(sig.parameters.keys())
    assert "iter" in params, "Missing parameter 'iter'"

def test_sos::adtmm::cterm_has_iter():
    assert hasattr(SOS::adtmm::CTerm, "iter")
    descriptor = None
    for klass in SOS::adtmm::CTerm.__mro__:
        if "iter" in klass.__dict__:
            descriptor = klass.__dict__["iter"]
            break
    assert isinstance(descriptor, property)



def test_sos::set::setterm_is_not_abstract():
    assert not inspect.isabstract(SOS::set::SetTerm)


def test_sos::set::setterm_constructor_exists():
    assert callable(SOS::set::SetTerm.__init__)


def test_sos::set::setterm_constructor_args():
    sig = inspect.signature(SOS::set::SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_sos::set::modelrelation_is_not_abstract():
    assert not inspect.isabstract(SOS::set::ModelRelation)


def test_sos::set::modelrelation_constructor_exists():
    assert callable(SOS::set::ModelRelation.__init__)


def test_sos::set::modelrelation_constructor_args():
    sig = inspect.signature(SOS::set::ModelRelation.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_sos::set::modelrelation_has_referenceName():
    assert hasattr(SOS::set::ModelRelation, "referenceName")
    descriptor = None
    for klass in SOS::set::ModelRelation.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_sos::adtmm::variableref_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::VariableRef)


def test_sos::adtmm::variableref_constructor_exists():
    assert callable(SOS::adtmm::VariableRef.__init__)


def test_sos::adtmm::variableref_constructor_args():
    sig = inspect.signature(SOS::adtmm::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_sortdeclaration_is_not_abstract():
    assert not inspect.isabstract(SortDeclaration)


def test_sortdeclaration_constructor_exists():
    assert callable(SortDeclaration.__init__)


def test_sortdeclaration_constructor_args():
    sig = inspect.signature(SortDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::adt_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::ADT)


def test_sos::adtmm::adt_constructor_exists():
    assert callable(SOS::adtmm::ADT.__init__)


def test_sos::adtmm::adt_constructor_args():
    sig = inspect.signature(SOS::adtmm::ADT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos::adtmm::adt_has_name():
    assert hasattr(SOS::adtmm::ADT, "name")
    descriptor = None
    for klass in SOS::adtmm::ADT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos::algebraicconditionlist_is_not_abstract():
    assert not inspect.isabstract(SOS::AlgebraicConditionList)


def test_sos::algebraicconditionlist_constructor_exists():
    assert callable(SOS::AlgebraicConditionList.__init__)


def test_sos::algebraicconditionlist_constructor_args():
    sig = inspect.signature(SOS::AlgebraicConditionList.__init__)
    params = list(sig.parameters.keys())



def test_abstractequation_is_not_abstract():
    assert not inspect.isabstract(AbstractEquation)


def test_abstractequation_constructor_exists():
    assert callable(AbstractEquation.__init__)


def test_abstractequation_constructor_args():
    sig = inspect.signature(AbstractEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::inequation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Inequation)


def test_sos::adtmm::inequation_constructor_exists():
    assert callable(SOS::adtmm::Inequation.__init__)


def test_sos::adtmm::inequation_constructor_args():
    sig = inspect.signature(SOS::adtmm::Inequation.__init__)
    params = list(sig.parameters.keys())



def test_sos::adtmm::equation_is_not_abstract():
    assert not inspect.isabstract(SOS::adtmm::Equation)


def test_sos::adtmm::equation_constructor_exists():
    assert callable(SOS::adtmm::Equation.__init__)


def test_sos::adtmm::equation_constructor_args():
    sig = inspect.signature(SOS::adtmm::Equation.__init__)
    params = list(sig.parameters.keys())



def test_sos::rule_is_not_abstract():
    assert not inspect.isabstract(SOS::Rule)


def test_sos::rule_constructor_exists():
    assert callable(SOS::Rule.__init__)


def test_sos::rule_constructor_args():
    sig = inspect.signature(SOS::Rule.__init__)
    params = list(sig.parameters.keys())



def test_sos::semantics_is_not_abstract():
    assert not inspect.isabstract(SOS::Semantics)


def test_sos::semantics_constructor_exists():
    assert callable(SOS::Semantics.__init__)


def test_sos::semantics_constructor_args():
    sig = inspect.signature(SOS::Semantics.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sos::typejudment_is_not_abstract():
    assert not inspect.isabstract(SOS::TypeJudment)


def test_sos::typejudment_constructor_exists():
    assert callable(SOS::TypeJudment.__init__)


def test_sos::typejudment_constructor_args():
    sig = inspect.signature(SOS::TypeJudment.__init__)
    params = list(sig.parameters.keys())



def test_sos::algebraiccondition_is_not_abstract():
    assert not inspect.isabstract(SOS::AlgebraicCondition)


def test_sos::algebraiccondition_constructor_exists():
    assert callable(SOS::AlgebraicCondition.__init__)


def test_sos::algebraiccondition_constructor_args():
    sig = inspect.signature(SOS::AlgebraicCondition.__init__)
    params = list(sig.parameters.keys())



def test_sos::transition_is_not_abstract():
    assert not inspect.isabstract(SOS::Transition)


def test_sos::transition_constructor_exists():
    assert callable(SOS::Transition.__init__)


def test_sos::transition_constructor_args():
    sig = inspect.signature(SOS::Transition.__init__)
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
SOS::Condition_strategy = st.builds(
    SOS::Condition,
)
Variable_strategy = st.builds(
    Variable,
)
SOS::Conclusion_strategy = st.builds(
    SOS::Conclusion,
)
SOS::PremisseList_strategy = st.builds(
    SOS::PremisseList,
)
ADT_strategy = st.builds(
    ADT,
)
SetMembership_strategy = st.builds(
    SetMembership,
)
SOS::set::ForAllIn_strategy = st.builds(
    SOS::set::ForAllIn,
)
SOS::set::ExistsIn_strategy = st.builds(
    SOS::set::ExistsIn,
)
VariableRef_strategy = st.builds(
    VariableRef,
)
SetOperator_strategy = st.builds(
    SetOperator,
)
SOS::set::Excluding_strategy = st.builds(
    SOS::set::Excluding,
)
SOS::set::Intersection_strategy = st.builds(
    SOS::set::Intersection,
)
SOS::set::Union_strategy = st.builds(
    SOS::set::Union,
)
set::SOS::AlgebraicConditionList_strategy = st.builds(
    set::SOS::AlgebraicConditionList,
)
SOS::adtmm::AbstractEquation_strategy = st.builds(
    SOS::adtmm::AbstractEquation,
)
SetTerm_strategy = st.builds(
    SetTerm,
)
SOS::set::ModelSet_strategy = st.builds(
    SOS::set::ModelSet,
)
SOS::set::SetOperator_strategy = st.builds(
    SOS::set::SetOperator,
)
SOS::set::SetConstructor_strategy = st.builds(
    SOS::set::SetConstructor,
)
SOS::set::SetMembership_strategy = st.builds(
    SOS::set::SetMembership,
)
SOS::adtmm::AbstractOperation_strategy = st.builds(
    SOS::adtmm::AbstractOperation,
    name=
        safe_text
)
SOS::adtmm::SortDeclaration_strategy = st.builds(
    SOS::adtmm::SortDeclaration,
    name=
        safe_text
)
SOS::adtmm::AbstractSort_strategy = st.builds(
    SOS::adtmm::AbstractSort,
)
Sort_strategy = st.builds(
    Sort,
)
SOS::adtmm::AtomicSort_strategy = st.builds(
    SOS::adtmm::AtomicSort,
)
SOS::set::Set_strategy = st.builds(
    SOS::set::Set,
)
SOS::set::ModelSort_strategy = st.builds(
    SOS::set::ModelSort,
    packageName=
        safe_text,
    className=
        safe_text
)
AbstractOperation_strategy = st.builds(
    AbstractOperation,
)
SOS::adtmm::AbstractGenericOp_strategy = st.builds(
    SOS::adtmm::AbstractGenericOp,
)
SOS::adtmm::Operation_strategy = st.builds(
    SOS::adtmm::Operation,
)
SOS::adtmm::Sort_strategy = st.builds(
    SOS::adtmm::Sort,
)
CondEquation_strategy = st.builds(
    CondEquation,
)
SOS::adtmm::Term_strategy = st.builds(
    SOS::adtmm::Term,
)
Equation_strategy = st.builds(
    Equation,
)
SOS::adtmm::CondEquation_strategy = st.builds(
    SOS::adtmm::CondEquation,
)
SOS::adtmm::Variable_strategy = st.builds(
    SOS::adtmm::Variable,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
SOS::set::ModelClassAttribute_strategy = st.builds(
    SOS::set::ModelClassAttribute,
    attributeName=
        safe_text
)
SOS::adtmm::CTerm_strategy = st.builds(
    SOS::adtmm::CTerm,
    iter=
        st.integers()
)
SOS::set::SetTerm_strategy = st.builds(
    SOS::set::SetTerm,
)
SOS::set::ModelRelation_strategy = st.builds(
    SOS::set::ModelRelation,
    referenceName=
        safe_text
)
SOS::adtmm::VariableRef_strategy = st.builds(
    SOS::adtmm::VariableRef,
)
Operation_strategy = st.builds(
    Operation,
)
SortDeclaration_strategy = st.builds(
    SortDeclaration,
)
SOS::adtmm::ADT_strategy = st.builds(
    SOS::adtmm::ADT,
    name=
        safe_text
)
SOS::AlgebraicConditionList_strategy = st.builds(
    SOS::AlgebraicConditionList,
)
AbstractEquation_strategy = st.builds(
    AbstractEquation,
)
SOS::adtmm::Inequation_strategy = st.builds(
    SOS::adtmm::Inequation,
)
SOS::adtmm::Equation_strategy = st.builds(
    SOS::adtmm::Equation,
)
SOS::Rule_strategy = st.builds(
    SOS::Rule,
)
SOS::Semantics_strategy = st.builds(
    SOS::Semantics,
)
Condition_strategy = st.builds(
    Condition,
)
SOS::TypeJudment_strategy = st.builds(
    SOS::TypeJudment,
)
SOS::AlgebraicCondition_strategy = st.builds(
    SOS::AlgebraicCondition,
)
SOS::Transition_strategy = st.builds(
    SOS::Transition,
)

@given(instance=SOS::Condition_strategy)
@settings(max_examples=50)
def test_sos::condition_instantiation(instance):
    assert isinstance(instance, SOS::Condition)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=SOS::Conclusion_strategy)
@settings(max_examples=50)
def test_sos::conclusion_instantiation(instance):
    assert isinstance(instance, SOS::Conclusion)

@given(instance=SOS::PremisseList_strategy)
@settings(max_examples=50)
def test_sos::premisselist_instantiation(instance):
    assert isinstance(instance, SOS::PremisseList)

@given(instance=ADT_strategy)
@settings(max_examples=50)
def test_adt_instantiation(instance):
    assert isinstance(instance, ADT)

@given(instance=SetMembership_strategy)
@settings(max_examples=50)
def test_setmembership_instantiation(instance):
    assert isinstance(instance, SetMembership)

@given(instance=SOS::set::ForAllIn_strategy)
@settings(max_examples=50)
def test_sos::set::forallin_instantiation(instance):
    assert isinstance(instance, SOS::set::ForAllIn)

@given(instance=SOS::set::ExistsIn_strategy)
@settings(max_examples=50)
def test_sos::set::existsin_instantiation(instance):
    assert isinstance(instance, SOS::set::ExistsIn)

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=SetOperator_strategy)
@settings(max_examples=50)
def test_setoperator_instantiation(instance):
    assert isinstance(instance, SetOperator)

@given(instance=SOS::set::Excluding_strategy)
@settings(max_examples=50)
def test_sos::set::excluding_instantiation(instance):
    assert isinstance(instance, SOS::set::Excluding)

@given(instance=SOS::set::Intersection_strategy)
@settings(max_examples=50)
def test_sos::set::intersection_instantiation(instance):
    assert isinstance(instance, SOS::set::Intersection)

@given(instance=SOS::set::Union_strategy)
@settings(max_examples=50)
def test_sos::set::union_instantiation(instance):
    assert isinstance(instance, SOS::set::Union)

@given(instance=set::SOS::AlgebraicConditionList_strategy)
@settings(max_examples=50)
def test_set::sos::algebraicconditionlist_instantiation(instance):
    assert isinstance(instance, set::SOS::AlgebraicConditionList)

@given(instance=SOS::adtmm::AbstractEquation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::abstractequation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::AbstractEquation)

@given(instance=SetTerm_strategy)
@settings(max_examples=50)
def test_setterm_instantiation(instance):
    assert isinstance(instance, SetTerm)

@given(instance=SOS::set::ModelSet_strategy)
@settings(max_examples=50)
def test_sos::set::modelset_instantiation(instance):
    assert isinstance(instance, SOS::set::ModelSet)

@given(instance=SOS::set::SetOperator_strategy)
@settings(max_examples=50)
def test_sos::set::setoperator_instantiation(instance):
    assert isinstance(instance, SOS::set::SetOperator)

@given(instance=SOS::set::SetConstructor_strategy)
@settings(max_examples=50)
def test_sos::set::setconstructor_instantiation(instance):
    assert isinstance(instance, SOS::set::SetConstructor)

@given(instance=SOS::set::SetMembership_strategy)
@settings(max_examples=50)
def test_sos::set::setmembership_instantiation(instance):
    assert isinstance(instance, SOS::set::SetMembership)

@given(instance=SOS::adtmm::AbstractOperation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::abstractoperation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::AbstractOperation)

@given(instance=SOS::adtmm::AbstractOperation_strategy)
def test_sos::adtmm::abstractoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SOS::adtmm::AbstractOperation_strategy)
def test_sos::adtmm::abstractoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS::adtmm::SortDeclaration_strategy)
@settings(max_examples=50)
def test_sos::adtmm::sortdeclaration_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::SortDeclaration)

@given(instance=SOS::adtmm::SortDeclaration_strategy)
def test_sos::adtmm::sortdeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SOS::adtmm::SortDeclaration_strategy)
def test_sos::adtmm::sortdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS::adtmm::AbstractSort_strategy)
@settings(max_examples=50)
def test_sos::adtmm::abstractsort_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::AbstractSort)

@given(instance=Sort_strategy)
@settings(max_examples=50)
def test_sort_instantiation(instance):
    assert isinstance(instance, Sort)

@given(instance=SOS::adtmm::AtomicSort_strategy)
@settings(max_examples=50)
def test_sos::adtmm::atomicsort_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::AtomicSort)

@given(instance=SOS::set::Set_strategy)
@settings(max_examples=50)
def test_sos::set::set_instantiation(instance):
    assert isinstance(instance, SOS::set::Set)

@given(instance=SOS::set::ModelSort_strategy)
@settings(max_examples=50)
def test_sos::set::modelsort_instantiation(instance):
    assert isinstance(instance, SOS::set::ModelSort)

@given(instance=SOS::set::ModelSort_strategy)
def test_sos::set::modelsort_packageName_type(instance):
    assert isinstance(instance.packageName, str)


@given(instance=SOS::set::ModelSort_strategy)
def test_sos::set::modelsort_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original

@given(instance=SOS::set::ModelSort_strategy)
def test_sos::set::modelsort_className_type(instance):
    assert isinstance(instance.className, str)


@given(instance=SOS::set::ModelSort_strategy)
def test_sos::set::modelsort_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=AbstractOperation_strategy)
@settings(max_examples=50)
def test_abstractoperation_instantiation(instance):
    assert isinstance(instance, AbstractOperation)

@given(instance=SOS::adtmm::AbstractGenericOp_strategy)
@settings(max_examples=50)
def test_sos::adtmm::abstractgenericop_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::AbstractGenericOp)

@given(instance=SOS::adtmm::Operation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::operation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Operation)

@given(instance=SOS::adtmm::Sort_strategy)
@settings(max_examples=50)
def test_sos::adtmm::sort_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Sort)

@given(instance=CondEquation_strategy)
@settings(max_examples=50)
def test_condequation_instantiation(instance):
    assert isinstance(instance, CondEquation)

@given(instance=SOS::adtmm::Term_strategy)
@settings(max_examples=50)
def test_sos::adtmm::term_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Term)

@given(instance=Equation_strategy)
@settings(max_examples=50)
def test_equation_instantiation(instance):
    assert isinstance(instance, Equation)

@given(instance=SOS::adtmm::CondEquation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::condequation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::CondEquation)

@given(instance=SOS::adtmm::Variable_strategy)
@settings(max_examples=50)
def test_sos::adtmm::variable_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Variable)

@given(instance=SOS::adtmm::Variable_strategy)
def test_sos::adtmm::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SOS::adtmm::Variable_strategy)
def test_sos::adtmm::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=SOS::set::ModelClassAttribute_strategy)
@settings(max_examples=50)
def test_sos::set::modelclassattribute_instantiation(instance):
    assert isinstance(instance, SOS::set::ModelClassAttribute)

@given(instance=SOS::set::ModelClassAttribute_strategy)
def test_sos::set::modelclassattribute_attributeName_type(instance):
    assert isinstance(instance.attributeName, str)


@given(instance=SOS::set::ModelClassAttribute_strategy)
def test_sos::set::modelclassattribute_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=SOS::adtmm::CTerm_strategy)
@settings(max_examples=50)
def test_sos::adtmm::cterm_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::CTerm)

@given(instance=SOS::adtmm::CTerm_strategy)
def test_sos::adtmm::cterm_iter_type(instance):
    assert isinstance(instance.iter, int)


@given(instance=SOS::adtmm::CTerm_strategy)
def test_sos::adtmm::cterm_iter_setter(instance):
    original = instance.iter
    instance.iter = original
    assert instance.iter == original

@given(instance=SOS::set::SetTerm_strategy)
@settings(max_examples=50)
def test_sos::set::setterm_instantiation(instance):
    assert isinstance(instance, SOS::set::SetTerm)

@given(instance=SOS::set::ModelRelation_strategy)
@settings(max_examples=50)
def test_sos::set::modelrelation_instantiation(instance):
    assert isinstance(instance, SOS::set::ModelRelation)

@given(instance=SOS::set::ModelRelation_strategy)
def test_sos::set::modelrelation_referenceName_type(instance):
    assert isinstance(instance.referenceName, str)


@given(instance=SOS::set::ModelRelation_strategy)
def test_sos::set::modelrelation_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=SOS::adtmm::VariableRef_strategy)
@settings(max_examples=50)
def test_sos::adtmm::variableref_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::VariableRef)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=SortDeclaration_strategy)
@settings(max_examples=50)
def test_sortdeclaration_instantiation(instance):
    assert isinstance(instance, SortDeclaration)

@given(instance=SOS::adtmm::ADT_strategy)
@settings(max_examples=50)
def test_sos::adtmm::adt_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::ADT)

@given(instance=SOS::adtmm::ADT_strategy)
def test_sos::adtmm::adt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=SOS::adtmm::ADT_strategy)
def test_sos::adtmm::adt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS::AlgebraicConditionList_strategy)
@settings(max_examples=50)
def test_sos::algebraicconditionlist_instantiation(instance):
    assert isinstance(instance, SOS::AlgebraicConditionList)

@given(instance=AbstractEquation_strategy)
@settings(max_examples=50)
def test_abstractequation_instantiation(instance):
    assert isinstance(instance, AbstractEquation)

@given(instance=SOS::adtmm::Inequation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::inequation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Inequation)

@given(instance=SOS::adtmm::Equation_strategy)
@settings(max_examples=50)
def test_sos::adtmm::equation_instantiation(instance):
    assert isinstance(instance, SOS::adtmm::Equation)

@given(instance=SOS::Rule_strategy)
@settings(max_examples=50)
def test_sos::rule_instantiation(instance):
    assert isinstance(instance, SOS::Rule)

@given(instance=SOS::Semantics_strategy)
@settings(max_examples=50)
def test_sos::semantics_instantiation(instance):
    assert isinstance(instance, SOS::Semantics)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=SOS::TypeJudment_strategy)
@settings(max_examples=50)
def test_sos::typejudment_instantiation(instance):
    assert isinstance(instance, SOS::TypeJudment)

@given(instance=SOS::AlgebraicCondition_strategy)
@settings(max_examples=50)
def test_sos::algebraiccondition_instantiation(instance):
    assert isinstance(instance, SOS::AlgebraicCondition)

@given(instance=SOS::Transition_strategy)
@settings(max_examples=50)
def test_sos::transition_instantiation(instance):
    assert isinstance(instance, SOS::Transition)
