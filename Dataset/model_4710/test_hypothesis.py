import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SetMembership,
    SOS_set_ForAllIn,
    SOS_set_ExistsIn,
    VariableRef,
    SetOperator,
    SOS_set_Intersection,
    SOS_set_Excluding,
    SOS_set_Union,
    set_SOS_AlgebraicConditionList,
    SOS_adtmm_AbstractEquation,
    SetTerm,
    SOS_set_ModelSet,
    SOS_set_SetConstructor,
    SOS_set_SetOperator,
    SOS_set_SetMembership,
    SOS_adtmm_AbstractOperation,
    SOS_adtmm_SortDeclaration,
    SOS_adtmm_AbstractSort,
    Sort,
    SOS_adtmm_AtomicSort,
    SOS_set_ModelSort,
    SOS_set_Set,
    AbstractOperation,
    SOS_adtmm_AbstractGenericOp,
    SOS_adtmm_Operation,
    SOS_adtmm_Sort,
    CondEquation,
    SOS_adtmm_Term,
    Equation,
    SOS_adtmm_CondEquation,
    SOS_adtmm_Variable,
    Term,
    SOS_set_ModelClassAttribute,
    SOS_set_SetTerm,
    SOS_set_ModelRelation,
    SOS_adtmm_CTerm,
    SOS_adtmm_VariableRef,
    Operation,
    SortDeclaration,
    SOS_adtmm_ADT,
    SOS_AlgebraicConditionList,
    AbstractEquation,
    SOS_adtmm_Equation,
    SOS_adtmm_Inequation,
    SOS_Rule,
    SOS_Semantics,
    Condition,
    SOS_AlgebraicCondition,
    SOS_TypeJudment,
    SOS_Transition,
    SOS_Condition,
    Variable,
    SOS_Conclusion,
    SOS_PremisseList,
    ADT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_setmembership_is_not_abstract():
    assert not inspect.isabstract(SetMembership)


def test_setmembership_constructor_exists():
    assert callable(SetMembership.__init__)


def test_setmembership_constructor_args():
    sig = inspect.signature(SetMembership.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_forallin_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ForAllIn)


def test_sos_set_forallin_constructor_exists():
    assert callable(SOS_set_ForAllIn.__init__)


def test_sos_set_forallin_constructor_args():
    sig = inspect.signature(SOS_set_ForAllIn.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_existsin_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ExistsIn)


def test_sos_set_existsin_constructor_exists():
    assert callable(SOS_set_ExistsIn.__init__)


def test_sos_set_existsin_constructor_args():
    sig = inspect.signature(SOS_set_ExistsIn.__init__)
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



def test_sos_set_intersection_is_not_abstract():
    assert not inspect.isabstract(SOS_set_Intersection)


def test_sos_set_intersection_constructor_exists():
    assert callable(SOS_set_Intersection.__init__)


def test_sos_set_intersection_constructor_args():
    sig = inspect.signature(SOS_set_Intersection.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_excluding_is_not_abstract():
    assert not inspect.isabstract(SOS_set_Excluding)


def test_sos_set_excluding_constructor_exists():
    assert callable(SOS_set_Excluding.__init__)


def test_sos_set_excluding_constructor_args():
    sig = inspect.signature(SOS_set_Excluding.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_union_is_not_abstract():
    assert not inspect.isabstract(SOS_set_Union)


def test_sos_set_union_constructor_exists():
    assert callable(SOS_set_Union.__init__)


def test_sos_set_union_constructor_args():
    sig = inspect.signature(SOS_set_Union.__init__)
    params = list(sig.parameters.keys())



def test_set_sos_algebraicconditionlist_is_not_abstract():
    assert not inspect.isabstract(set_SOS_AlgebraicConditionList)


def test_set_sos_algebraicconditionlist_constructor_exists():
    assert callable(set_SOS_AlgebraicConditionList.__init__)


def test_set_sos_algebraicconditionlist_constructor_args():
    sig = inspect.signature(set_SOS_AlgebraicConditionList.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_abstractequation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_AbstractEquation)


def test_sos_adtmm_abstractequation_constructor_exists():
    assert callable(SOS_adtmm_AbstractEquation.__init__)


def test_sos_adtmm_abstractequation_constructor_args():
    sig = inspect.signature(SOS_adtmm_AbstractEquation.__init__)
    params = list(sig.parameters.keys())



def test_setterm_is_not_abstract():
    assert not inspect.isabstract(SetTerm)


def test_setterm_constructor_exists():
    assert callable(SetTerm.__init__)


def test_setterm_constructor_args():
    sig = inspect.signature(SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_modelset_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ModelSet)


def test_sos_set_modelset_constructor_exists():
    assert callable(SOS_set_ModelSet.__init__)


def test_sos_set_modelset_constructor_args():
    sig = inspect.signature(SOS_set_ModelSet.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_setconstructor_is_not_abstract():
    assert not inspect.isabstract(SOS_set_SetConstructor)


def test_sos_set_setconstructor_constructor_exists():
    assert callable(SOS_set_SetConstructor.__init__)


def test_sos_set_setconstructor_constructor_args():
    sig = inspect.signature(SOS_set_SetConstructor.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_setoperator_is_not_abstract():
    assert not inspect.isabstract(SOS_set_SetOperator)


def test_sos_set_setoperator_constructor_exists():
    assert callable(SOS_set_SetOperator.__init__)


def test_sos_set_setoperator_constructor_args():
    sig = inspect.signature(SOS_set_SetOperator.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_setmembership_is_not_abstract():
    assert not inspect.isabstract(SOS_set_SetMembership)


def test_sos_set_setmembership_constructor_exists():
    assert callable(SOS_set_SetMembership.__init__)


def test_sos_set_setmembership_constructor_args():
    sig = inspect.signature(SOS_set_SetMembership.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_AbstractOperation)


def test_sos_adtmm_abstractoperation_constructor_exists():
    assert callable(SOS_adtmm_AbstractOperation.__init__)


def test_sos_adtmm_abstractoperation_constructor_args():
    sig = inspect.signature(SOS_adtmm_AbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos_adtmm_abstractoperation_has_name():
    assert hasattr(SOS_adtmm_AbstractOperation, "name")
    descriptor = None
    for klass in SOS_adtmm_AbstractOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos_adtmm_sortdeclaration_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_SortDeclaration)


def test_sos_adtmm_sortdeclaration_constructor_exists():
    assert callable(SOS_adtmm_SortDeclaration.__init__)


def test_sos_adtmm_sortdeclaration_constructor_args():
    sig = inspect.signature(SOS_adtmm_SortDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos_adtmm_sortdeclaration_has_name():
    assert hasattr(SOS_adtmm_SortDeclaration, "name")
    descriptor = None
    for klass in SOS_adtmm_SortDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos_adtmm_abstractsort_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_AbstractSort)


def test_sos_adtmm_abstractsort_constructor_exists():
    assert callable(SOS_adtmm_AbstractSort.__init__)


def test_sos_adtmm_abstractsort_constructor_args():
    sig = inspect.signature(SOS_adtmm_AbstractSort.__init__)
    params = list(sig.parameters.keys())



def test_sort_is_not_abstract():
    assert not inspect.isabstract(Sort)


def test_sort_constructor_exists():
    assert callable(Sort.__init__)


def test_sort_constructor_args():
    sig = inspect.signature(Sort.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_atomicsort_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_AtomicSort)


def test_sos_adtmm_atomicsort_constructor_exists():
    assert callable(SOS_adtmm_AtomicSort.__init__)


def test_sos_adtmm_atomicsort_constructor_args():
    sig = inspect.signature(SOS_adtmm_AtomicSort.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_modelsort_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ModelSort)


def test_sos_set_modelsort_constructor_exists():
    assert callable(SOS_set_ModelSort.__init__)


def test_sos_set_modelsort_constructor_args():
    sig = inspect.signature(SOS_set_ModelSort.__init__)
    params = list(sig.parameters.keys())
    assert "packageName" in params, "Missing parameter 'packageName'"
    assert "className" in params, "Missing parameter 'className'"

def test_sos_set_modelsort_has_packageName():
    assert hasattr(SOS_set_ModelSort, "packageName")
    descriptor = None
    for klass in SOS_set_ModelSort.__mro__:
        if "packageName" in klass.__dict__:
            descriptor = klass.__dict__["packageName"]
            break
    assert isinstance(descriptor, property)

def test_sos_set_modelsort_has_className():
    assert hasattr(SOS_set_ModelSort, "className")
    descriptor = None
    for klass in SOS_set_ModelSort.__mro__:
        if "className" in klass.__dict__:
            descriptor = klass.__dict__["className"]
            break
    assert isinstance(descriptor, property)



def test_sos_set_set_is_not_abstract():
    assert not inspect.isabstract(SOS_set_Set)


def test_sos_set_set_constructor_exists():
    assert callable(SOS_set_Set.__init__)


def test_sos_set_set_constructor_args():
    sig = inspect.signature(SOS_set_Set.__init__)
    params = list(sig.parameters.keys())



def test_abstractoperation_is_not_abstract():
    assert not inspect.isabstract(AbstractOperation)


def test_abstractoperation_constructor_exists():
    assert callable(AbstractOperation.__init__)


def test_abstractoperation_constructor_args():
    sig = inspect.signature(AbstractOperation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_abstractgenericop_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_AbstractGenericOp)


def test_sos_adtmm_abstractgenericop_constructor_exists():
    assert callable(SOS_adtmm_AbstractGenericOp.__init__)


def test_sos_adtmm_abstractgenericop_constructor_args():
    sig = inspect.signature(SOS_adtmm_AbstractGenericOp.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_operation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Operation)


def test_sos_adtmm_operation_constructor_exists():
    assert callable(SOS_adtmm_Operation.__init__)


def test_sos_adtmm_operation_constructor_args():
    sig = inspect.signature(SOS_adtmm_Operation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_sort_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Sort)


def test_sos_adtmm_sort_constructor_exists():
    assert callable(SOS_adtmm_Sort.__init__)


def test_sos_adtmm_sort_constructor_args():
    sig = inspect.signature(SOS_adtmm_Sort.__init__)
    params = list(sig.parameters.keys())



def test_condequation_is_not_abstract():
    assert not inspect.isabstract(CondEquation)


def test_condequation_constructor_exists():
    assert callable(CondEquation.__init__)


def test_condequation_constructor_args():
    sig = inspect.signature(CondEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_term_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Term)


def test_sos_adtmm_term_constructor_exists():
    assert callable(SOS_adtmm_Term.__init__)


def test_sos_adtmm_term_constructor_args():
    sig = inspect.signature(SOS_adtmm_Term.__init__)
    params = list(sig.parameters.keys())



def test_equation_is_not_abstract():
    assert not inspect.isabstract(Equation)


def test_equation_constructor_exists():
    assert callable(Equation.__init__)


def test_equation_constructor_args():
    sig = inspect.signature(Equation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_condequation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_CondEquation)


def test_sos_adtmm_condequation_constructor_exists():
    assert callable(SOS_adtmm_CondEquation.__init__)


def test_sos_adtmm_condequation_constructor_args():
    sig = inspect.signature(SOS_adtmm_CondEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_variable_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Variable)


def test_sos_adtmm_variable_constructor_exists():
    assert callable(SOS_adtmm_Variable.__init__)


def test_sos_adtmm_variable_constructor_args():
    sig = inspect.signature(SOS_adtmm_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos_adtmm_variable_has_name():
    assert hasattr(SOS_adtmm_Variable, "name")
    descriptor = None
    for klass in SOS_adtmm_Variable.__mro__:
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



def test_sos_set_modelclassattribute_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ModelClassAttribute)


def test_sos_set_modelclassattribute_constructor_exists():
    assert callable(SOS_set_ModelClassAttribute.__init__)


def test_sos_set_modelclassattribute_constructor_args():
    sig = inspect.signature(SOS_set_ModelClassAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "attributeName" in params, "Missing parameter 'attributeName'"

def test_sos_set_modelclassattribute_has_attributeName():
    assert hasattr(SOS_set_ModelClassAttribute, "attributeName")
    descriptor = None
    for klass in SOS_set_ModelClassAttribute.__mro__:
        if "attributeName" in klass.__dict__:
            descriptor = klass.__dict__["attributeName"]
            break
    assert isinstance(descriptor, property)



def test_sos_set_setterm_is_not_abstract():
    assert not inspect.isabstract(SOS_set_SetTerm)


def test_sos_set_setterm_constructor_exists():
    assert callable(SOS_set_SetTerm.__init__)


def test_sos_set_setterm_constructor_args():
    sig = inspect.signature(SOS_set_SetTerm.__init__)
    params = list(sig.parameters.keys())



def test_sos_set_modelrelation_is_not_abstract():
    assert not inspect.isabstract(SOS_set_ModelRelation)


def test_sos_set_modelrelation_constructor_exists():
    assert callable(SOS_set_ModelRelation.__init__)


def test_sos_set_modelrelation_constructor_args():
    sig = inspect.signature(SOS_set_ModelRelation.__init__)
    params = list(sig.parameters.keys())
    assert "referenceName" in params, "Missing parameter 'referenceName'"

def test_sos_set_modelrelation_has_referenceName():
    assert hasattr(SOS_set_ModelRelation, "referenceName")
    descriptor = None
    for klass in SOS_set_ModelRelation.__mro__:
        if "referenceName" in klass.__dict__:
            descriptor = klass.__dict__["referenceName"]
            break
    assert isinstance(descriptor, property)



def test_sos_adtmm_cterm_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_CTerm)


def test_sos_adtmm_cterm_constructor_exists():
    assert callable(SOS_adtmm_CTerm.__init__)


def test_sos_adtmm_cterm_constructor_args():
    sig = inspect.signature(SOS_adtmm_CTerm.__init__)
    params = list(sig.parameters.keys())
    assert "iter" in params, "Missing parameter 'iter'"

def test_sos_adtmm_cterm_has_iter():
    assert hasattr(SOS_adtmm_CTerm, "iter")
    descriptor = None
    for klass in SOS_adtmm_CTerm.__mro__:
        if "iter" in klass.__dict__:
            descriptor = klass.__dict__["iter"]
            break
    assert isinstance(descriptor, property)



def test_sos_adtmm_variableref_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_VariableRef)


def test_sos_adtmm_variableref_constructor_exists():
    assert callable(SOS_adtmm_VariableRef.__init__)


def test_sos_adtmm_variableref_constructor_args():
    sig = inspect.signature(SOS_adtmm_VariableRef.__init__)
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



def test_sos_adtmm_adt_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_ADT)


def test_sos_adtmm_adt_constructor_exists():
    assert callable(SOS_adtmm_ADT.__init__)


def test_sos_adtmm_adt_constructor_args():
    sig = inspect.signature(SOS_adtmm_ADT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sos_adtmm_adt_has_name():
    assert hasattr(SOS_adtmm_ADT, "name")
    descriptor = None
    for klass in SOS_adtmm_ADT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sos_algebraicconditionlist_is_not_abstract():
    assert not inspect.isabstract(SOS_AlgebraicConditionList)


def test_sos_algebraicconditionlist_constructor_exists():
    assert callable(SOS_AlgebraicConditionList.__init__)


def test_sos_algebraicconditionlist_constructor_args():
    sig = inspect.signature(SOS_AlgebraicConditionList.__init__)
    params = list(sig.parameters.keys())



def test_abstractequation_is_not_abstract():
    assert not inspect.isabstract(AbstractEquation)


def test_abstractequation_constructor_exists():
    assert callable(AbstractEquation.__init__)


def test_abstractequation_constructor_args():
    sig = inspect.signature(AbstractEquation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_equation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Equation)


def test_sos_adtmm_equation_constructor_exists():
    assert callable(SOS_adtmm_Equation.__init__)


def test_sos_adtmm_equation_constructor_args():
    sig = inspect.signature(SOS_adtmm_Equation.__init__)
    params = list(sig.parameters.keys())



def test_sos_adtmm_inequation_is_not_abstract():
    assert not inspect.isabstract(SOS_adtmm_Inequation)


def test_sos_adtmm_inequation_constructor_exists():
    assert callable(SOS_adtmm_Inequation.__init__)


def test_sos_adtmm_inequation_constructor_args():
    sig = inspect.signature(SOS_adtmm_Inequation.__init__)
    params = list(sig.parameters.keys())



def test_sos_rule_is_not_abstract():
    assert not inspect.isabstract(SOS_Rule)


def test_sos_rule_constructor_exists():
    assert callable(SOS_Rule.__init__)


def test_sos_rule_constructor_args():
    sig = inspect.signature(SOS_Rule.__init__)
    params = list(sig.parameters.keys())



def test_sos_semantics_is_not_abstract():
    assert not inspect.isabstract(SOS_Semantics)


def test_sos_semantics_constructor_exists():
    assert callable(SOS_Semantics.__init__)


def test_sos_semantics_constructor_args():
    sig = inspect.signature(SOS_Semantics.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sos_algebraiccondition_is_not_abstract():
    assert not inspect.isabstract(SOS_AlgebraicCondition)


def test_sos_algebraiccondition_constructor_exists():
    assert callable(SOS_AlgebraicCondition.__init__)


def test_sos_algebraiccondition_constructor_args():
    sig = inspect.signature(SOS_AlgebraicCondition.__init__)
    params = list(sig.parameters.keys())



def test_sos_typejudment_is_not_abstract():
    assert not inspect.isabstract(SOS_TypeJudment)


def test_sos_typejudment_constructor_exists():
    assert callable(SOS_TypeJudment.__init__)


def test_sos_typejudment_constructor_args():
    sig = inspect.signature(SOS_TypeJudment.__init__)
    params = list(sig.parameters.keys())



def test_sos_transition_is_not_abstract():
    assert not inspect.isabstract(SOS_Transition)


def test_sos_transition_constructor_exists():
    assert callable(SOS_Transition.__init__)


def test_sos_transition_constructor_args():
    sig = inspect.signature(SOS_Transition.__init__)
    params = list(sig.parameters.keys())



def test_sos_condition_is_not_abstract():
    assert not inspect.isabstract(SOS_Condition)


def test_sos_condition_constructor_exists():
    assert callable(SOS_Condition.__init__)


def test_sos_condition_constructor_args():
    sig = inspect.signature(SOS_Condition.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_sos_conclusion_is_not_abstract():
    assert not inspect.isabstract(SOS_Conclusion)


def test_sos_conclusion_constructor_exists():
    assert callable(SOS_Conclusion.__init__)


def test_sos_conclusion_constructor_args():
    sig = inspect.signature(SOS_Conclusion.__init__)
    params = list(sig.parameters.keys())



def test_sos_premisselist_is_not_abstract():
    assert not inspect.isabstract(SOS_PremisseList)


def test_sos_premisselist_constructor_exists():
    assert callable(SOS_PremisseList.__init__)


def test_sos_premisselist_constructor_args():
    sig = inspect.signature(SOS_PremisseList.__init__)
    params = list(sig.parameters.keys())



def test_adt_is_not_abstract():
    assert not inspect.isabstract(ADT)


def test_adt_constructor_exists():
    assert callable(ADT.__init__)


def test_adt_constructor_args():
    sig = inspect.signature(ADT.__init__)
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
SetMembership_strategy = st.builds(
    SetMembership,
)
SOS_set_ForAllIn_strategy = st.builds(
    SOS_set_ForAllIn,
)
SOS_set_ExistsIn_strategy = st.builds(
    SOS_set_ExistsIn,
)
VariableRef_strategy = st.builds(
    VariableRef,
)
SetOperator_strategy = st.builds(
    SetOperator,
)
SOS_set_Intersection_strategy = st.builds(
    SOS_set_Intersection,
)
SOS_set_Excluding_strategy = st.builds(
    SOS_set_Excluding,
)
SOS_set_Union_strategy = st.builds(
    SOS_set_Union,
)
set_SOS_AlgebraicConditionList_strategy = st.builds(
    set_SOS_AlgebraicConditionList,
)
SOS_adtmm_AbstractEquation_strategy = st.builds(
    SOS_adtmm_AbstractEquation,
)
SetTerm_strategy = st.builds(
    SetTerm,
)
SOS_set_ModelSet_strategy = st.builds(
    SOS_set_ModelSet,
)
SOS_set_SetConstructor_strategy = st.builds(
    SOS_set_SetConstructor,
)
SOS_set_SetOperator_strategy = st.builds(
    SOS_set_SetOperator,
)
SOS_set_SetMembership_strategy = st.builds(
    SOS_set_SetMembership,
)
SOS_adtmm_AbstractOperation_strategy = st.builds(
    SOS_adtmm_AbstractOperation,
    name=
        safe_text
)
SOS_adtmm_SortDeclaration_strategy = st.builds(
    SOS_adtmm_SortDeclaration,
    name=
        safe_text
)
SOS_adtmm_AbstractSort_strategy = st.builds(
    SOS_adtmm_AbstractSort,
)
Sort_strategy = st.builds(
    Sort,
)
SOS_adtmm_AtomicSort_strategy = st.builds(
    SOS_adtmm_AtomicSort,
)
SOS_set_ModelSort_strategy = st.builds(
    SOS_set_ModelSort,
    packageName=
        safe_text,
    className=
        safe_text
)
SOS_set_Set_strategy = st.builds(
    SOS_set_Set,
)
AbstractOperation_strategy = st.builds(
    AbstractOperation,
)
SOS_adtmm_AbstractGenericOp_strategy = st.builds(
    SOS_adtmm_AbstractGenericOp,
)
SOS_adtmm_Operation_strategy = st.builds(
    SOS_adtmm_Operation,
)
SOS_adtmm_Sort_strategy = st.builds(
    SOS_adtmm_Sort,
)
CondEquation_strategy = st.builds(
    CondEquation,
)
SOS_adtmm_Term_strategy = st.builds(
    SOS_adtmm_Term,
)
Equation_strategy = st.builds(
    Equation,
)
SOS_adtmm_CondEquation_strategy = st.builds(
    SOS_adtmm_CondEquation,
)
SOS_adtmm_Variable_strategy = st.builds(
    SOS_adtmm_Variable,
    name=
        safe_text
)
Term_strategy = st.builds(
    Term,
)
SOS_set_ModelClassAttribute_strategy = st.builds(
    SOS_set_ModelClassAttribute,
    attributeName=
        safe_text
)
SOS_set_SetTerm_strategy = st.builds(
    SOS_set_SetTerm,
)
SOS_set_ModelRelation_strategy = st.builds(
    SOS_set_ModelRelation,
    referenceName=
        safe_text
)
SOS_adtmm_CTerm_strategy = st.builds(
    SOS_adtmm_CTerm,
    iter=
        st.integers()
)
SOS_adtmm_VariableRef_strategy = st.builds(
    SOS_adtmm_VariableRef,
)
Operation_strategy = st.builds(
    Operation,
)
SortDeclaration_strategy = st.builds(
    SortDeclaration,
)
SOS_adtmm_ADT_strategy = st.builds(
    SOS_adtmm_ADT,
    name=
        safe_text
)
SOS_AlgebraicConditionList_strategy = st.builds(
    SOS_AlgebraicConditionList,
)
AbstractEquation_strategy = st.builds(
    AbstractEquation,
)
SOS_adtmm_Equation_strategy = st.builds(
    SOS_adtmm_Equation,
)
SOS_adtmm_Inequation_strategy = st.builds(
    SOS_adtmm_Inequation,
)
SOS_Rule_strategy = st.builds(
    SOS_Rule,
)
SOS_Semantics_strategy = st.builds(
    SOS_Semantics,
)
Condition_strategy = st.builds(
    Condition,
)
SOS_AlgebraicCondition_strategy = st.builds(
    SOS_AlgebraicCondition,
)
SOS_TypeJudment_strategy = st.builds(
    SOS_TypeJudment,
)
SOS_Transition_strategy = st.builds(
    SOS_Transition,
)
SOS_Condition_strategy = st.builds(
    SOS_Condition,
)
Variable_strategy = st.builds(
    Variable,
)
SOS_Conclusion_strategy = st.builds(
    SOS_Conclusion,
)
SOS_PremisseList_strategy = st.builds(
    SOS_PremisseList,
)
ADT_strategy = st.builds(
    ADT,
)

@given(instance=SetMembership_strategy)
@settings(max_examples=50)
def test_setmembership_instantiation(instance):
    assert isinstance(instance, SetMembership)

@given(instance=SOS_set_ForAllIn_strategy)
@settings(max_examples=50)
def test_sos_set_forallin_instantiation(instance):
    assert isinstance(instance, SOS_set_ForAllIn)

@given(instance=SOS_set_ExistsIn_strategy)
@settings(max_examples=50)
def test_sos_set_existsin_instantiation(instance):
    assert isinstance(instance, SOS_set_ExistsIn)

@given(instance=VariableRef_strategy)
@settings(max_examples=50)
def test_variableref_instantiation(instance):
    assert isinstance(instance, VariableRef)

@given(instance=SetOperator_strategy)
@settings(max_examples=50)
def test_setoperator_instantiation(instance):
    assert isinstance(instance, SetOperator)

@given(instance=SOS_set_Intersection_strategy)
@settings(max_examples=50)
def test_sos_set_intersection_instantiation(instance):
    assert isinstance(instance, SOS_set_Intersection)

@given(instance=SOS_set_Excluding_strategy)
@settings(max_examples=50)
def test_sos_set_excluding_instantiation(instance):
    assert isinstance(instance, SOS_set_Excluding)

@given(instance=SOS_set_Union_strategy)
@settings(max_examples=50)
def test_sos_set_union_instantiation(instance):
    assert isinstance(instance, SOS_set_Union)

@given(instance=set_SOS_AlgebraicConditionList_strategy)
@settings(max_examples=50)
def test_set_sos_algebraicconditionlist_instantiation(instance):
    assert isinstance(instance, set_SOS_AlgebraicConditionList)

@given(instance=SOS_adtmm_AbstractEquation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_abstractequation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_AbstractEquation)

@given(instance=SetTerm_strategy)
@settings(max_examples=50)
def test_setterm_instantiation(instance):
    assert isinstance(instance, SetTerm)

@given(instance=SOS_set_ModelSet_strategy)
@settings(max_examples=50)
def test_sos_set_modelset_instantiation(instance):
    assert isinstance(instance, SOS_set_ModelSet)

@given(instance=SOS_set_SetConstructor_strategy)
@settings(max_examples=50)
def test_sos_set_setconstructor_instantiation(instance):
    assert isinstance(instance, SOS_set_SetConstructor)

@given(instance=SOS_set_SetOperator_strategy)
@settings(max_examples=50)
def test_sos_set_setoperator_instantiation(instance):
    assert isinstance(instance, SOS_set_SetOperator)

@given(instance=SOS_set_SetMembership_strategy)
@settings(max_examples=50)
def test_sos_set_setmembership_instantiation(instance):
    assert isinstance(instance, SOS_set_SetMembership)

@given(instance=SOS_adtmm_AbstractOperation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_abstractoperation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_AbstractOperation)



@given(instance=SOS_adtmm_AbstractOperation_strategy)
def test_sos_adtmm_abstractoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS_adtmm_SortDeclaration_strategy)
@settings(max_examples=50)
def test_sos_adtmm_sortdeclaration_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_SortDeclaration)



@given(instance=SOS_adtmm_SortDeclaration_strategy)
def test_sos_adtmm_sortdeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS_adtmm_AbstractSort_strategy)
@settings(max_examples=50)
def test_sos_adtmm_abstractsort_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_AbstractSort)

@given(instance=Sort_strategy)
@settings(max_examples=50)
def test_sort_instantiation(instance):
    assert isinstance(instance, Sort)

@given(instance=SOS_adtmm_AtomicSort_strategy)
@settings(max_examples=50)
def test_sos_adtmm_atomicsort_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_AtomicSort)

@given(instance=SOS_set_ModelSort_strategy)
@settings(max_examples=50)
def test_sos_set_modelsort_instantiation(instance):
    assert isinstance(instance, SOS_set_ModelSort)



@given(instance=SOS_set_ModelSort_strategy)
def test_sos_set_modelsort_packageName_setter(instance):
    original = instance.packageName
    instance.packageName = original
    assert instance.packageName == original



@given(instance=SOS_set_ModelSort_strategy)
def test_sos_set_modelsort_className_setter(instance):
    original = instance.className
    instance.className = original
    assert instance.className == original

@given(instance=SOS_set_Set_strategy)
@settings(max_examples=50)
def test_sos_set_set_instantiation(instance):
    assert isinstance(instance, SOS_set_Set)

@given(instance=AbstractOperation_strategy)
@settings(max_examples=50)
def test_abstractoperation_instantiation(instance):
    assert isinstance(instance, AbstractOperation)

@given(instance=SOS_adtmm_AbstractGenericOp_strategy)
@settings(max_examples=50)
def test_sos_adtmm_abstractgenericop_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_AbstractGenericOp)

@given(instance=SOS_adtmm_Operation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_operation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Operation)

@given(instance=SOS_adtmm_Sort_strategy)
@settings(max_examples=50)
def test_sos_adtmm_sort_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Sort)

@given(instance=CondEquation_strategy)
@settings(max_examples=50)
def test_condequation_instantiation(instance):
    assert isinstance(instance, CondEquation)

@given(instance=SOS_adtmm_Term_strategy)
@settings(max_examples=50)
def test_sos_adtmm_term_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Term)

@given(instance=Equation_strategy)
@settings(max_examples=50)
def test_equation_instantiation(instance):
    assert isinstance(instance, Equation)

@given(instance=SOS_adtmm_CondEquation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_condequation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_CondEquation)

@given(instance=SOS_adtmm_Variable_strategy)
@settings(max_examples=50)
def test_sos_adtmm_variable_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Variable)



@given(instance=SOS_adtmm_Variable_strategy)
def test_sos_adtmm_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Term_strategy)
@settings(max_examples=50)
def test_term_instantiation(instance):
    assert isinstance(instance, Term)

@given(instance=SOS_set_ModelClassAttribute_strategy)
@settings(max_examples=50)
def test_sos_set_modelclassattribute_instantiation(instance):
    assert isinstance(instance, SOS_set_ModelClassAttribute)



@given(instance=SOS_set_ModelClassAttribute_strategy)
def test_sos_set_modelclassattribute_attributeName_setter(instance):
    original = instance.attributeName
    instance.attributeName = original
    assert instance.attributeName == original

@given(instance=SOS_set_SetTerm_strategy)
@settings(max_examples=50)
def test_sos_set_setterm_instantiation(instance):
    assert isinstance(instance, SOS_set_SetTerm)

@given(instance=SOS_set_ModelRelation_strategy)
@settings(max_examples=50)
def test_sos_set_modelrelation_instantiation(instance):
    assert isinstance(instance, SOS_set_ModelRelation)



@given(instance=SOS_set_ModelRelation_strategy)
def test_sos_set_modelrelation_referenceName_setter(instance):
    original = instance.referenceName
    instance.referenceName = original
    assert instance.referenceName == original

@given(instance=SOS_adtmm_CTerm_strategy)
@settings(max_examples=50)
def test_sos_adtmm_cterm_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_CTerm)



@given(instance=SOS_adtmm_CTerm_strategy)
def test_sos_adtmm_cterm_iter_setter(instance):
    original = instance.iter
    instance.iter = original
    assert instance.iter == original

@given(instance=SOS_adtmm_VariableRef_strategy)
@settings(max_examples=50)
def test_sos_adtmm_variableref_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_VariableRef)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=SortDeclaration_strategy)
@settings(max_examples=50)
def test_sortdeclaration_instantiation(instance):
    assert isinstance(instance, SortDeclaration)

@given(instance=SOS_adtmm_ADT_strategy)
@settings(max_examples=50)
def test_sos_adtmm_adt_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_ADT)



@given(instance=SOS_adtmm_ADT_strategy)
def test_sos_adtmm_adt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SOS_AlgebraicConditionList_strategy)
@settings(max_examples=50)
def test_sos_algebraicconditionlist_instantiation(instance):
    assert isinstance(instance, SOS_AlgebraicConditionList)

@given(instance=AbstractEquation_strategy)
@settings(max_examples=50)
def test_abstractequation_instantiation(instance):
    assert isinstance(instance, AbstractEquation)

@given(instance=SOS_adtmm_Equation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_equation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Equation)

@given(instance=SOS_adtmm_Inequation_strategy)
@settings(max_examples=50)
def test_sos_adtmm_inequation_instantiation(instance):
    assert isinstance(instance, SOS_adtmm_Inequation)

@given(instance=SOS_Rule_strategy)
@settings(max_examples=50)
def test_sos_rule_instantiation(instance):
    assert isinstance(instance, SOS_Rule)

@given(instance=SOS_Semantics_strategy)
@settings(max_examples=50)
def test_sos_semantics_instantiation(instance):
    assert isinstance(instance, SOS_Semantics)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=SOS_AlgebraicCondition_strategy)
@settings(max_examples=50)
def test_sos_algebraiccondition_instantiation(instance):
    assert isinstance(instance, SOS_AlgebraicCondition)

@given(instance=SOS_TypeJudment_strategy)
@settings(max_examples=50)
def test_sos_typejudment_instantiation(instance):
    assert isinstance(instance, SOS_TypeJudment)

@given(instance=SOS_Transition_strategy)
@settings(max_examples=50)
def test_sos_transition_instantiation(instance):
    assert isinstance(instance, SOS_Transition)

@given(instance=SOS_Condition_strategy)
@settings(max_examples=50)
def test_sos_condition_instantiation(instance):
    assert isinstance(instance, SOS_Condition)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=SOS_Conclusion_strategy)
@settings(max_examples=50)
def test_sos_conclusion_instantiation(instance):
    assert isinstance(instance, SOS_Conclusion)

@given(instance=SOS_PremisseList_strategy)
@settings(max_examples=50)
def test_sos_premisselist_instantiation(instance):
    assert isinstance(instance, SOS_PremisseList)

@given(instance=ADT_strategy)
@settings(max_examples=50)
def test_adt_instantiation(instance):
    assert isinstance(instance, ADT)
