import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sadl_ValueRow,
    sadl_ValueTable,
    sadl_IntervalValue,
    sadl_GraphPattern,
    sadl_OrderElement,
    sadl_OrderList,
    Expression,
    sadl_AskQueryExpression,
    sadl_JunctionExpression,
    sadl_UnaryOpExpression,
    sadl_ConstructExpression,
    sadl_BinaryOpExpression,
    sadl_SelectExpression,
    sadl_Expression,
    sadl_ElementSet,
    sadl_Object,
    sadl_VariableList,
    GraphPattern,
    sadl_InstAttrSPV,
    sadl_ExistentialNegation,
    sadl_InstAttrPSV,
    sadl_PropOfSubj,
    sadl_SubTypeOf,
    sadl_SubjProp,
    sadl_MergedTriples,
    sadl_EmbeddedInstanceDeclaration,
    sadl_WithPhrase,
    sadl_WithChain,
    sadl_OfPhrase,
    sadl_TypeDeclaration,
    EmbeddedInstanceDeclaration,
    InstanceDeclarationStatement,
    sadl_InstanceDeclaration,
    sadl_OfPatternReturningValues,
    sadl_PropValPartialTriple,
    sadl_IsInverseOf,
    sadl_AdditionalPropertyInfo,
    sadl_TypedBNode,
    sadl_ExplicitValue,
    sadl_EObject,
    Condition,
    sadl_CardCondition,
    sadl_MaxCardCondition,
    sadl_MinCardCondition,
    sadl_HasValueCondition,
    sadl_SomeValuesCondition,
    sadl_AllValuesCondition,
    sadl_PropertyOfClass,
    sadl_Facets,
    sadl_DataTypeRestriction,
    Statement,
    sadl_InstanceDifferentFrom,
    sadl_EnumeratedAllAndSomeValuesFrom,
    sadl_InverseProperty,
    sadl_SymmetricalProperty,
    sadl_InstancesAllDifferent,
    sadl_AllValuesFrom,
    sadl_InstanceDeclarationStatement,
    sadl_TransitiveProperty,
    sadl_EquivalentConcepts,
    sadl_MaxCardinality,
    sadl_ExistingInstanceAttribution,
    sadl_DisjointClasses,
    sadl_DefaultValue,
    sadl_HasValue,
    sadl_NecessaryAndSufficient,
    sadl_SomeValuesFrom,
    sadl_InverseFunctionalProperty,
    sadl_ComplementOfClass,
    sadl_EnumeratedAllValuesFrom,
    sadl_MinCardinality,
    sadl_PropertyDeclaration,
    sadl_FunctionalProperty,
    sadl_Cardinality,
    sadl_ClassDeclaration,
    sadl_UserDefinedDataType,
    ResourceBySetOp,
    sadl_IntersectionResource,
    sadl_UnionResource,
    sadl_RangeType,
    sadl_Range,
    sadl_AddlClassInfo,
    sadl_EnumeratedInstances,
    ModelElement,
    sadl_Expr,
    sadl_Query,
    sadl_Rule,
    sadl_Test,
    sadl_Display,
    sadl_Explanation,
    sadl_Statement,
    sadl_Condition,
    sadl_ResourceIdentifier,
    sadl_ExistingResourceList,
    ResourceIdentifier,
    sadl_ResourceByRestriction,
    sadl_ResourceBySetOp,
    sadl_ResourceByName,
    sadl_LiteralValue,
    sadl_LiteralList,
    sadl_ResourceList,
    sadl_ResourceName,
    sadl_ContentList,
    sadl_ModelElement,
    sadl_Import,
    sadl_ModelName,
    sadl_Model,
    DataType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sadl_valuerow_is_not_abstract():
    assert not inspect.isabstract(sadl_ValueRow)


def test_sadl_valuerow_constructor_exists():
    assert callable(sadl_ValueRow.__init__)


def test_sadl_valuerow_constructor_args():
    sig = inspect.signature(sadl_ValueRow.__init__)
    params = list(sig.parameters.keys())



def test_sadl_valuetable_is_not_abstract():
    assert not inspect.isabstract(sadl_ValueTable)


def test_sadl_valuetable_constructor_exists():
    assert callable(sadl_ValueTable.__init__)


def test_sadl_valuetable_constructor_args():
    sig = inspect.signature(sadl_ValueTable.__init__)
    params = list(sig.parameters.keys())



def test_sadl_intervalvalue_is_not_abstract():
    assert not inspect.isabstract(sadl_IntervalValue)


def test_sadl_intervalvalue_constructor_exists():
    assert callable(sadl_IntervalValue.__init__)


def test_sadl_intervalvalue_constructor_args():
    sig = inspect.signature(sadl_IntervalValue.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_intervalvalue_has_op():
    assert hasattr(sadl_IntervalValue, "op")
    descriptor = None
    for klass in sadl_IntervalValue.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_graphpattern_is_not_abstract():
    assert not inspect.isabstract(sadl_GraphPattern)


def test_sadl_graphpattern_constructor_exists():
    assert callable(sadl_GraphPattern.__init__)


def test_sadl_graphpattern_constructor_args():
    sig = inspect.signature(sadl_GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sadl_orderelement_is_not_abstract():
    assert not inspect.isabstract(sadl_OrderElement)


def test_sadl_orderelement_constructor_exists():
    assert callable(sadl_OrderElement.__init__)


def test_sadl_orderelement_constructor_args():
    sig = inspect.signature(sadl_OrderElement.__init__)
    params = list(sig.parameters.keys())
    assert "order" in params, "Missing parameter 'order'"

def test_sadl_orderelement_has_order():
    assert hasattr(sadl_OrderElement, "order")
    descriptor = None
    for klass in sadl_OrderElement.__mro__:
        if "order" in klass.__dict__:
            descriptor = klass.__dict__["order"]
            break
    assert isinstance(descriptor, property)



def test_sadl_orderlist_is_not_abstract():
    assert not inspect.isabstract(sadl_OrderList)


def test_sadl_orderlist_constructor_exists():
    assert callable(sadl_OrderList.__init__)


def test_sadl_orderlist_constructor_args():
    sig = inspect.signature(sadl_OrderList.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_askqueryexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_AskQueryExpression)


def test_sadl_askqueryexpression_constructor_exists():
    assert callable(sadl_AskQueryExpression.__init__)


def test_sadl_askqueryexpression_constructor_args():
    sig = inspect.signature(sadl_AskQueryExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_junctionexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_JunctionExpression)


def test_sadl_junctionexpression_constructor_exists():
    assert callable(sadl_JunctionExpression.__init__)


def test_sadl_junctionexpression_constructor_args():
    sig = inspect.signature(sadl_JunctionExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_junctionexpression_has_op():
    assert hasattr(sadl_JunctionExpression, "op")
    descriptor = None
    for klass in sadl_JunctionExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_unaryopexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_UnaryOpExpression)


def test_sadl_unaryopexpression_constructor_exists():
    assert callable(sadl_UnaryOpExpression.__init__)


def test_sadl_unaryopexpression_constructor_args():
    sig = inspect.signature(sadl_UnaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_unaryopexpression_has_op():
    assert hasattr(sadl_UnaryOpExpression, "op")
    descriptor = None
    for klass in sadl_UnaryOpExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_constructexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_ConstructExpression)


def test_sadl_constructexpression_constructor_exists():
    assert callable(sadl_ConstructExpression.__init__)


def test_sadl_constructexpression_constructor_args():
    sig = inspect.signature(sadl_ConstructExpression.__init__)
    params = list(sig.parameters.keys())



def test_sadl_binaryopexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_BinaryOpExpression)


def test_sadl_binaryopexpression_constructor_exists():
    assert callable(sadl_BinaryOpExpression.__init__)


def test_sadl_binaryopexpression_constructor_args():
    sig = inspect.signature(sadl_BinaryOpExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_sadl_binaryopexpression_has_op():
    assert hasattr(sadl_BinaryOpExpression, "op")
    descriptor = None
    for klass in sadl_BinaryOpExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_sadl_selectexpression_is_not_abstract():
    assert not inspect.isabstract(sadl_SelectExpression)


def test_sadl_selectexpression_constructor_exists():
    assert callable(sadl_SelectExpression.__init__)


def test_sadl_selectexpression_constructor_args():
    sig = inspect.signature(sadl_SelectExpression.__init__)
    params = list(sig.parameters.keys())
    assert "orderby" in params, "Missing parameter 'orderby'"
    assert "distinct" in params, "Missing parameter 'distinct'"
    assert "allVars" in params, "Missing parameter 'allVars'"

def test_sadl_selectexpression_has_orderby():
    assert hasattr(sadl_SelectExpression, "orderby")
    descriptor = None
    for klass in sadl_SelectExpression.__mro__:
        if "orderby" in klass.__dict__:
            descriptor = klass.__dict__["orderby"]
            break
    assert isinstance(descriptor, property)

def test_sadl_selectexpression_has_distinct():
    assert hasattr(sadl_SelectExpression, "distinct")
    descriptor = None
    for klass in sadl_SelectExpression.__mro__:
        if "distinct" in klass.__dict__:
            descriptor = klass.__dict__["distinct"]
            break
    assert isinstance(descriptor, property)

def test_sadl_selectexpression_has_allVars():
    assert hasattr(sadl_SelectExpression, "allVars")
    descriptor = None
    for klass in sadl_SelectExpression.__mro__:
        if "allVars" in klass.__dict__:
            descriptor = klass.__dict__["allVars"]
            break
    assert isinstance(descriptor, property)



def test_sadl_expression_is_not_abstract():
    assert not inspect.isabstract(sadl_Expression)


def test_sadl_expression_constructor_exists():
    assert callable(sadl_Expression.__init__)


def test_sadl_expression_constructor_args():
    sig = inspect.signature(sadl_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "func" in params, "Missing parameter 'func'"

def test_sadl_expression_has_func():
    assert hasattr(sadl_Expression, "func")
    descriptor = None
    for klass in sadl_Expression.__mro__:
        if "func" in klass.__dict__:
            descriptor = klass.__dict__["func"]
            break
    assert isinstance(descriptor, property)



def test_sadl_elementset_is_not_abstract():
    assert not inspect.isabstract(sadl_ElementSet)


def test_sadl_elementset_constructor_exists():
    assert callable(sadl_ElementSet.__init__)


def test_sadl_elementset_constructor_args():
    sig = inspect.signature(sadl_ElementSet.__init__)
    params = list(sig.parameters.keys())



def test_sadl_object_is_not_abstract():
    assert not inspect.isabstract(sadl_Object)


def test_sadl_object_constructor_exists():
    assert callable(sadl_Object.__init__)


def test_sadl_object_constructor_args():
    sig = inspect.signature(sadl_Object.__init__)
    params = list(sig.parameters.keys())



def test_sadl_variablelist_is_not_abstract():
    assert not inspect.isabstract(sadl_VariableList)


def test_sadl_variablelist_constructor_exists():
    assert callable(sadl_VariableList.__init__)


def test_sadl_variablelist_constructor_args():
    sig = inspect.signature(sadl_VariableList.__init__)
    params = list(sig.parameters.keys())



def test_graphpattern_is_not_abstract():
    assert not inspect.isabstract(GraphPattern)


def test_graphpattern_constructor_exists():
    assert callable(GraphPattern.__init__)


def test_graphpattern_constructor_args():
    sig = inspect.signature(GraphPattern.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instattrspv_is_not_abstract():
    assert not inspect.isabstract(sadl_InstAttrSPV)


def test_sadl_instattrspv_constructor_exists():
    assert callable(sadl_InstAttrSPV.__init__)


def test_sadl_instattrspv_constructor_args():
    sig = inspect.signature(sadl_InstAttrSPV.__init__)
    params = list(sig.parameters.keys())



def test_sadl_existentialnegation_is_not_abstract():
    assert not inspect.isabstract(sadl_ExistentialNegation)


def test_sadl_existentialnegation_constructor_exists():
    assert callable(sadl_ExistentialNegation.__init__)


def test_sadl_existentialnegation_constructor_args():
    sig = inspect.signature(sadl_ExistentialNegation.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instattrpsv_is_not_abstract():
    assert not inspect.isabstract(sadl_InstAttrPSV)


def test_sadl_instattrpsv_constructor_exists():
    assert callable(sadl_InstAttrPSV.__init__)


def test_sadl_instattrpsv_constructor_args():
    sig = inspect.signature(sadl_InstAttrPSV.__init__)
    params = list(sig.parameters.keys())



def test_sadl_propofsubj_is_not_abstract():
    assert not inspect.isabstract(sadl_PropOfSubj)


def test_sadl_propofsubj_constructor_exists():
    assert callable(sadl_PropOfSubj.__init__)


def test_sadl_propofsubj_constructor_args():
    sig = inspect.signature(sadl_PropOfSubj.__init__)
    params = list(sig.parameters.keys())



def test_sadl_subtypeof_is_not_abstract():
    assert not inspect.isabstract(sadl_SubTypeOf)


def test_sadl_subtypeof_constructor_exists():
    assert callable(sadl_SubTypeOf.__init__)


def test_sadl_subtypeof_constructor_args():
    sig = inspect.signature(sadl_SubTypeOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl_subjprop_is_not_abstract():
    assert not inspect.isabstract(sadl_SubjProp)


def test_sadl_subjprop_constructor_exists():
    assert callable(sadl_SubjProp.__init__)


def test_sadl_subjprop_constructor_args():
    sig = inspect.signature(sadl_SubjProp.__init__)
    params = list(sig.parameters.keys())



def test_sadl_mergedtriples_is_not_abstract():
    assert not inspect.isabstract(sadl_MergedTriples)


def test_sadl_mergedtriples_constructor_exists():
    assert callable(sadl_MergedTriples.__init__)


def test_sadl_mergedtriples_constructor_args():
    sig = inspect.signature(sadl_MergedTriples.__init__)
    params = list(sig.parameters.keys())



def test_sadl_embeddedinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl_EmbeddedInstanceDeclaration)


def test_sadl_embeddedinstancedeclaration_constructor_exists():
    assert callable(sadl_EmbeddedInstanceDeclaration.__init__)


def test_sadl_embeddedinstancedeclaration_constructor_args():
    sig = inspect.signature(sadl_EmbeddedInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl_withphrase_is_not_abstract():
    assert not inspect.isabstract(sadl_WithPhrase)


def test_sadl_withphrase_constructor_exists():
    assert callable(sadl_WithPhrase.__init__)


def test_sadl_withphrase_constructor_args():
    sig = inspect.signature(sadl_WithPhrase.__init__)
    params = list(sig.parameters.keys())



def test_sadl_withchain_is_not_abstract():
    assert not inspect.isabstract(sadl_WithChain)


def test_sadl_withchain_constructor_exists():
    assert callable(sadl_WithChain.__init__)


def test_sadl_withchain_constructor_args():
    sig = inspect.signature(sadl_WithChain.__init__)
    params = list(sig.parameters.keys())



def test_sadl_ofphrase_is_not_abstract():
    assert not inspect.isabstract(sadl_OfPhrase)


def test_sadl_ofphrase_constructor_exists():
    assert callable(sadl_OfPhrase.__init__)


def test_sadl_ofphrase_constructor_args():
    sig = inspect.signature(sadl_OfPhrase.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_ofphrase_has_article():
    assert hasattr(sadl_OfPhrase, "article")
    descriptor = None
    for klass in sadl_OfPhrase.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_typedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl_TypeDeclaration)


def test_sadl_typedeclaration_constructor_exists():
    assert callable(sadl_TypeDeclaration.__init__)


def test_sadl_typedeclaration_constructor_args():
    sig = inspect.signature(sadl_TypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_embeddedinstancedeclaration_is_not_abstract():
    assert not inspect.isabstract(EmbeddedInstanceDeclaration)


def test_embeddedinstancedeclaration_constructor_exists():
    assert callable(EmbeddedInstanceDeclaration.__init__)


def test_embeddedinstancedeclaration_constructor_args():
    sig = inspect.signature(EmbeddedInstanceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_instancedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(InstanceDeclarationStatement)


def test_instancedeclarationstatement_constructor_exists():
    assert callable(InstanceDeclarationStatement.__init__)


def test_instancedeclarationstatement_constructor_args():
    sig = inspect.signature(InstanceDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instancedeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl_InstanceDeclaration)


def test_sadl_instancedeclaration_constructor_exists():
    assert callable(sadl_InstanceDeclaration.__init__)


def test_sadl_instancedeclaration_constructor_args():
    sig = inspect.signature(sadl_InstanceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_instancedeclaration_has_article():
    assert hasattr(sadl_InstanceDeclaration, "article")
    descriptor = None
    for klass in sadl_InstanceDeclaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_ofpatternreturningvalues_is_not_abstract():
    assert not inspect.isabstract(sadl_OfPatternReturningValues)


def test_sadl_ofpatternreturningvalues_constructor_exists():
    assert callable(sadl_OfPatternReturningValues.__init__)


def test_sadl_ofpatternreturningvalues_constructor_args():
    sig = inspect.signature(sadl_OfPatternReturningValues.__init__)
    params = list(sig.parameters.keys())



def test_sadl_propvalpartialtriple_is_not_abstract():
    assert not inspect.isabstract(sadl_PropValPartialTriple)


def test_sadl_propvalpartialtriple_constructor_exists():
    assert callable(sadl_PropValPartialTriple.__init__)


def test_sadl_propvalpartialtriple_constructor_args():
    sig = inspect.signature(sadl_PropValPartialTriple.__init__)
    params = list(sig.parameters.keys())



def test_sadl_isinverseof_is_not_abstract():
    assert not inspect.isabstract(sadl_IsInverseOf)


def test_sadl_isinverseof_constructor_exists():
    assert callable(sadl_IsInverseOf.__init__)


def test_sadl_isinverseof_constructor_args():
    sig = inspect.signature(sadl_IsInverseOf.__init__)
    params = list(sig.parameters.keys())



def test_sadl_additionalpropertyinfo_is_not_abstract():
    assert not inspect.isabstract(sadl_AdditionalPropertyInfo)


def test_sadl_additionalpropertyinfo_constructor_exists():
    assert callable(sadl_AdditionalPropertyInfo.__init__)


def test_sadl_additionalpropertyinfo_constructor_args():
    sig = inspect.signature(sadl_AdditionalPropertyInfo.__init__)
    params = list(sig.parameters.keys())
    assert "isfunc" in params, "Missing parameter 'isfunc'"
    assert "isinvfunc" in params, "Missing parameter 'isinvfunc'"
    assert "isTrans" in params, "Missing parameter 'isTrans'"
    assert "isSym" in params, "Missing parameter 'isSym'"

def test_sadl_additionalpropertyinfo_has_isfunc():
    assert hasattr(sadl_AdditionalPropertyInfo, "isfunc")
    descriptor = None
    for klass in sadl_AdditionalPropertyInfo.__mro__:
        if "isfunc" in klass.__dict__:
            descriptor = klass.__dict__["isfunc"]
            break
    assert isinstance(descriptor, property)

def test_sadl_additionalpropertyinfo_has_isinvfunc():
    assert hasattr(sadl_AdditionalPropertyInfo, "isinvfunc")
    descriptor = None
    for klass in sadl_AdditionalPropertyInfo.__mro__:
        if "isinvfunc" in klass.__dict__:
            descriptor = klass.__dict__["isinvfunc"]
            break
    assert isinstance(descriptor, property)

def test_sadl_additionalpropertyinfo_has_isTrans():
    assert hasattr(sadl_AdditionalPropertyInfo, "isTrans")
    descriptor = None
    for klass in sadl_AdditionalPropertyInfo.__mro__:
        if "isTrans" in klass.__dict__:
            descriptor = klass.__dict__["isTrans"]
            break
    assert isinstance(descriptor, property)

def test_sadl_additionalpropertyinfo_has_isSym():
    assert hasattr(sadl_AdditionalPropertyInfo, "isSym")
    descriptor = None
    for klass in sadl_AdditionalPropertyInfo.__mro__:
        if "isSym" in klass.__dict__:
            descriptor = klass.__dict__["isSym"]
            break
    assert isinstance(descriptor, property)



def test_sadl_typedbnode_is_not_abstract():
    assert not inspect.isabstract(sadl_TypedBNode)


def test_sadl_typedbnode_constructor_exists():
    assert callable(sadl_TypedBNode.__init__)


def test_sadl_typedbnode_constructor_args():
    sig = inspect.signature(sadl_TypedBNode.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_typedbnode_has_article():
    assert hasattr(sadl_TypedBNode, "article")
    descriptor = None
    for klass in sadl_TypedBNode.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_explicitvalue_is_not_abstract():
    assert not inspect.isabstract(sadl_ExplicitValue)


def test_sadl_explicitvalue_constructor_exists():
    assert callable(sadl_ExplicitValue.__init__)


def test_sadl_explicitvalue_constructor_args():
    sig = inspect.signature(sadl_ExplicitValue.__init__)
    params = list(sig.parameters.keys())
    assert "valueList" in params, "Missing parameter 'valueList'"
    assert "term" in params, "Missing parameter 'term'"

def test_sadl_explicitvalue_has_valueList():
    assert hasattr(sadl_ExplicitValue, "valueList")
    descriptor = None
    for klass in sadl_ExplicitValue.__mro__:
        if "valueList" in klass.__dict__:
            descriptor = klass.__dict__["valueList"]
            break
    assert isinstance(descriptor, property)

def test_sadl_explicitvalue_has_term():
    assert hasattr(sadl_ExplicitValue, "term")
    descriptor = None
    for klass in sadl_ExplicitValue.__mro__:
        if "term" in klass.__dict__:
            descriptor = klass.__dict__["term"]
            break
    assert isinstance(descriptor, property)



def test_sadl_eobject_is_not_abstract():
    assert not inspect.isabstract(sadl_EObject)


def test_sadl_eobject_constructor_exists():
    assert callable(sadl_EObject.__init__)


def test_sadl_eobject_constructor_args():
    sig = inspect.signature(sadl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_cardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl_CardCondition)


def test_sadl_cardcondition_constructor_exists():
    assert callable(sadl_CardCondition.__init__)


def test_sadl_cardcondition_constructor_args():
    sig = inspect.signature(sadl_CardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl_cardcondition_has_card():
    assert hasattr(sadl_CardCondition, "card")
    descriptor = None
    for klass in sadl_CardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl_maxcardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl_MaxCardCondition)


def test_sadl_maxcardcondition_constructor_exists():
    assert callable(sadl_MaxCardCondition.__init__)


def test_sadl_maxcardcondition_constructor_args():
    sig = inspect.signature(sadl_MaxCardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl_maxcardcondition_has_card():
    assert hasattr(sadl_MaxCardCondition, "card")
    descriptor = None
    for klass in sadl_MaxCardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl_mincardcondition_is_not_abstract():
    assert not inspect.isabstract(sadl_MinCardCondition)


def test_sadl_mincardcondition_constructor_exists():
    assert callable(sadl_MinCardCondition.__init__)


def test_sadl_mincardcondition_constructor_args():
    sig = inspect.signature(sadl_MinCardCondition.__init__)
    params = list(sig.parameters.keys())
    assert "card" in params, "Missing parameter 'card'"

def test_sadl_mincardcondition_has_card():
    assert hasattr(sadl_MinCardCondition, "card")
    descriptor = None
    for klass in sadl_MinCardCondition.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)



def test_sadl_hasvaluecondition_is_not_abstract():
    assert not inspect.isabstract(sadl_HasValueCondition)


def test_sadl_hasvaluecondition_constructor_exists():
    assert callable(sadl_HasValueCondition.__init__)


def test_sadl_hasvaluecondition_constructor_args():
    sig = inspect.signature(sadl_HasValueCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_somevaluescondition_is_not_abstract():
    assert not inspect.isabstract(sadl_SomeValuesCondition)


def test_sadl_somevaluescondition_constructor_exists():
    assert callable(sadl_SomeValuesCondition.__init__)


def test_sadl_somevaluescondition_constructor_args():
    sig = inspect.signature(sadl_SomeValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_allvaluescondition_is_not_abstract():
    assert not inspect.isabstract(sadl_AllValuesCondition)


def test_sadl_allvaluescondition_constructor_exists():
    assert callable(sadl_AllValuesCondition.__init__)


def test_sadl_allvaluescondition_constructor_args():
    sig = inspect.signature(sadl_AllValuesCondition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_propertyofclass_is_not_abstract():
    assert not inspect.isabstract(sadl_PropertyOfClass)


def test_sadl_propertyofclass_constructor_exists():
    assert callable(sadl_PropertyOfClass.__init__)


def test_sadl_propertyofclass_constructor_args():
    sig = inspect.signature(sadl_PropertyOfClass.__init__)
    params = list(sig.parameters.keys())



def test_sadl_facets_is_not_abstract():
    assert not inspect.isabstract(sadl_Facets)


def test_sadl_facets_constructor_exists():
    assert callable(sadl_Facets.__init__)


def test_sadl_facets_constructor_args():
    sig = inspect.signature(sadl_Facets.__init__)
    params = list(sig.parameters.keys())
    assert "min" in params, "Missing parameter 'min'"
    assert "len" in params, "Missing parameter 'len'"
    assert "maxlen" in params, "Missing parameter 'maxlen'"
    assert "values" in params, "Missing parameter 'values'"
    assert "maxexin" in params, "Missing parameter 'maxexin'"
    assert "max" in params, "Missing parameter 'max'"
    assert "minexin" in params, "Missing parameter 'minexin'"
    assert "regex" in params, "Missing parameter 'regex'"
    assert "minlen" in params, "Missing parameter 'minlen'"

def test_sadl_facets_has_min():
    assert hasattr(sadl_Facets, "min")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_len():
    assert hasattr(sadl_Facets, "len")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "len" in klass.__dict__:
            descriptor = klass.__dict__["len"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_maxlen():
    assert hasattr(sadl_Facets, "maxlen")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "maxlen" in klass.__dict__:
            descriptor = klass.__dict__["maxlen"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_values():
    assert hasattr(sadl_Facets, "values")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_maxexin():
    assert hasattr(sadl_Facets, "maxexin")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "maxexin" in klass.__dict__:
            descriptor = klass.__dict__["maxexin"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_max():
    assert hasattr(sadl_Facets, "max")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_minexin():
    assert hasattr(sadl_Facets, "minexin")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "minexin" in klass.__dict__:
            descriptor = klass.__dict__["minexin"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_regex():
    assert hasattr(sadl_Facets, "regex")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "regex" in klass.__dict__:
            descriptor = klass.__dict__["regex"]
            break
    assert isinstance(descriptor, property)

def test_sadl_facets_has_minlen():
    assert hasattr(sadl_Facets, "minlen")
    descriptor = None
    for klass in sadl_Facets.__mro__:
        if "minlen" in klass.__dict__:
            descriptor = klass.__dict__["minlen"]
            break
    assert isinstance(descriptor, property)



def test_sadl_datatyperestriction_is_not_abstract():
    assert not inspect.isabstract(sadl_DataTypeRestriction)


def test_sadl_datatyperestriction_constructor_exists():
    assert callable(sadl_DataTypeRestriction.__init__)


def test_sadl_datatyperestriction_constructor_args():
    sig = inspect.signature(sadl_DataTypeRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "basetypes" in params, "Missing parameter 'basetypes'"
    assert "basetype" in params, "Missing parameter 'basetype'"

def test_sadl_datatyperestriction_has_basetypes():
    assert hasattr(sadl_DataTypeRestriction, "basetypes")
    descriptor = None
    for klass in sadl_DataTypeRestriction.__mro__:
        if "basetypes" in klass.__dict__:
            descriptor = klass.__dict__["basetypes"]
            break
    assert isinstance(descriptor, property)

def test_sadl_datatyperestriction_has_basetype():
    assert hasattr(sadl_DataTypeRestriction, "basetype")
    descriptor = None
    for klass in sadl_DataTypeRestriction.__mro__:
        if "basetype" in klass.__dict__:
            descriptor = klass.__dict__["basetype"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instancedifferentfrom_is_not_abstract():
    assert not inspect.isabstract(sadl_InstanceDifferentFrom)


def test_sadl_instancedifferentfrom_constructor_exists():
    assert callable(sadl_InstanceDifferentFrom.__init__)


def test_sadl_instancedifferentfrom_constructor_args():
    sig = inspect.signature(sadl_InstanceDifferentFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl_enumeratedallandsomevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl_EnumeratedAllAndSomeValuesFrom)


def test_sadl_enumeratedallandsomevaluesfrom_constructor_exists():
    assert callable(sadl_EnumeratedAllAndSomeValuesFrom.__init__)


def test_sadl_enumeratedallandsomevaluesfrom_constructor_args():
    sig = inspect.signature(sadl_EnumeratedAllAndSomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl_inverseproperty_is_not_abstract():
    assert not inspect.isabstract(sadl_InverseProperty)


def test_sadl_inverseproperty_constructor_exists():
    assert callable(sadl_InverseProperty.__init__)


def test_sadl_inverseproperty_constructor_args():
    sig = inspect.signature(sadl_InverseProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl_symmetricalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl_SymmetricalProperty)


def test_sadl_symmetricalproperty_constructor_exists():
    assert callable(sadl_SymmetricalProperty.__init__)


def test_sadl_symmetricalproperty_constructor_args():
    sig = inspect.signature(sadl_SymmetricalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instancesalldifferent_is_not_abstract():
    assert not inspect.isabstract(sadl_InstancesAllDifferent)


def test_sadl_instancesalldifferent_constructor_exists():
    assert callable(sadl_InstancesAllDifferent.__init__)


def test_sadl_instancesalldifferent_constructor_args():
    sig = inspect.signature(sadl_InstancesAllDifferent.__init__)
    params = list(sig.parameters.keys())



def test_sadl_allvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl_AllValuesFrom)


def test_sadl_allvaluesfrom_constructor_exists():
    assert callable(sadl_AllValuesFrom.__init__)


def test_sadl_allvaluesfrom_constructor_args():
    sig = inspect.signature(sadl_AllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl_instancedeclarationstatement_is_not_abstract():
    assert not inspect.isabstract(sadl_InstanceDeclarationStatement)


def test_sadl_instancedeclarationstatement_constructor_exists():
    assert callable(sadl_InstanceDeclarationStatement.__init__)


def test_sadl_instancedeclarationstatement_constructor_args():
    sig = inspect.signature(sadl_InstanceDeclarationStatement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_transitiveproperty_is_not_abstract():
    assert not inspect.isabstract(sadl_TransitiveProperty)


def test_sadl_transitiveproperty_constructor_exists():
    assert callable(sadl_TransitiveProperty.__init__)


def test_sadl_transitiveproperty_constructor_args():
    sig = inspect.signature(sadl_TransitiveProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl_equivalentconcepts_is_not_abstract():
    assert not inspect.isabstract(sadl_EquivalentConcepts)


def test_sadl_equivalentconcepts_constructor_exists():
    assert callable(sadl_EquivalentConcepts.__init__)


def test_sadl_equivalentconcepts_constructor_args():
    sig = inspect.signature(sadl_EquivalentConcepts.__init__)
    params = list(sig.parameters.keys())



def test_sadl_maxcardinality_is_not_abstract():
    assert not inspect.isabstract(sadl_MaxCardinality)


def test_sadl_maxcardinality_constructor_exists():
    assert callable(sadl_MaxCardinality.__init__)


def test_sadl_maxcardinality_constructor_args():
    sig = inspect.signature(sadl_MaxCardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl_existinginstanceattribution_is_not_abstract():
    assert not inspect.isabstract(sadl_ExistingInstanceAttribution)


def test_sadl_existinginstanceattribution_constructor_exists():
    assert callable(sadl_ExistingInstanceAttribution.__init__)


def test_sadl_existinginstanceattribution_constructor_args():
    sig = inspect.signature(sadl_ExistingInstanceAttribution.__init__)
    params = list(sig.parameters.keys())



def test_sadl_disjointclasses_is_not_abstract():
    assert not inspect.isabstract(sadl_DisjointClasses)


def test_sadl_disjointclasses_constructor_exists():
    assert callable(sadl_DisjointClasses.__init__)


def test_sadl_disjointclasses_constructor_args():
    sig = inspect.signature(sadl_DisjointClasses.__init__)
    params = list(sig.parameters.keys())



def test_sadl_defaultvalue_is_not_abstract():
    assert not inspect.isabstract(sadl_DefaultValue)


def test_sadl_defaultvalue_constructor_exists():
    assert callable(sadl_DefaultValue.__init__)


def test_sadl_defaultvalue_constructor_args():
    sig = inspect.signature(sadl_DefaultValue.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_sadl_defaultvalue_has_level():
    assert hasattr(sadl_DefaultValue, "level")
    descriptor = None
    for klass in sadl_DefaultValue.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_sadl_hasvalue_is_not_abstract():
    assert not inspect.isabstract(sadl_HasValue)


def test_sadl_hasvalue_constructor_exists():
    assert callable(sadl_HasValue.__init__)


def test_sadl_hasvalue_constructor_args():
    sig = inspect.signature(sadl_HasValue.__init__)
    params = list(sig.parameters.keys())



def test_sadl_necessaryandsufficient_is_not_abstract():
    assert not inspect.isabstract(sadl_NecessaryAndSufficient)


def test_sadl_necessaryandsufficient_constructor_exists():
    assert callable(sadl_NecessaryAndSufficient.__init__)


def test_sadl_necessaryandsufficient_constructor_args():
    sig = inspect.signature(sadl_NecessaryAndSufficient.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_necessaryandsufficient_has_article():
    assert hasattr(sadl_NecessaryAndSufficient, "article")
    descriptor = None
    for klass in sadl_NecessaryAndSufficient.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_somevaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl_SomeValuesFrom)


def test_sadl_somevaluesfrom_constructor_exists():
    assert callable(sadl_SomeValuesFrom.__init__)


def test_sadl_somevaluesfrom_constructor_args():
    sig = inspect.signature(sadl_SomeValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl_inversefunctionalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl_InverseFunctionalProperty)


def test_sadl_inversefunctionalproperty_constructor_exists():
    assert callable(sadl_InverseFunctionalProperty.__init__)


def test_sadl_inversefunctionalproperty_constructor_args():
    sig = inspect.signature(sadl_InverseFunctionalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl_complementofclass_is_not_abstract():
    assert not inspect.isabstract(sadl_ComplementOfClass)


def test_sadl_complementofclass_constructor_exists():
    assert callable(sadl_ComplementOfClass.__init__)


def test_sadl_complementofclass_constructor_args():
    sig = inspect.signature(sadl_ComplementOfClass.__init__)
    params = list(sig.parameters.keys())



def test_sadl_enumeratedallvaluesfrom_is_not_abstract():
    assert not inspect.isabstract(sadl_EnumeratedAllValuesFrom)


def test_sadl_enumeratedallvaluesfrom_constructor_exists():
    assert callable(sadl_EnumeratedAllValuesFrom.__init__)


def test_sadl_enumeratedallvaluesfrom_constructor_args():
    sig = inspect.signature(sadl_EnumeratedAllValuesFrom.__init__)
    params = list(sig.parameters.keys())



def test_sadl_mincardinality_is_not_abstract():
    assert not inspect.isabstract(sadl_MinCardinality)


def test_sadl_mincardinality_constructor_exists():
    assert callable(sadl_MinCardinality.__init__)


def test_sadl_mincardinality_constructor_args():
    sig = inspect.signature(sadl_MinCardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl_propertydeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl_PropertyDeclaration)


def test_sadl_propertydeclaration_constructor_exists():
    assert callable(sadl_PropertyDeclaration.__init__)


def test_sadl_propertydeclaration_constructor_args():
    sig = inspect.signature(sadl_PropertyDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "article" in params, "Missing parameter 'article'"

def test_sadl_propertydeclaration_has_article():
    assert hasattr(sadl_PropertyDeclaration, "article")
    descriptor = None
    for klass in sadl_PropertyDeclaration.__mro__:
        if "article" in klass.__dict__:
            descriptor = klass.__dict__["article"]
            break
    assert isinstance(descriptor, property)



def test_sadl_functionalproperty_is_not_abstract():
    assert not inspect.isabstract(sadl_FunctionalProperty)


def test_sadl_functionalproperty_constructor_exists():
    assert callable(sadl_FunctionalProperty.__init__)


def test_sadl_functionalproperty_constructor_args():
    sig = inspect.signature(sadl_FunctionalProperty.__init__)
    params = list(sig.parameters.keys())



def test_sadl_cardinality_is_not_abstract():
    assert not inspect.isabstract(sadl_Cardinality)


def test_sadl_cardinality_constructor_exists():
    assert callable(sadl_Cardinality.__init__)


def test_sadl_cardinality_constructor_args():
    sig = inspect.signature(sadl_Cardinality.__init__)
    params = list(sig.parameters.keys())



def test_sadl_classdeclaration_is_not_abstract():
    assert not inspect.isabstract(sadl_ClassDeclaration)


def test_sadl_classdeclaration_constructor_exists():
    assert callable(sadl_ClassDeclaration.__init__)


def test_sadl_classdeclaration_constructor_args():
    sig = inspect.signature(sadl_ClassDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_sadl_userdefineddatatype_is_not_abstract():
    assert not inspect.isabstract(sadl_UserDefinedDataType)


def test_sadl_userdefineddatatype_constructor_exists():
    assert callable(sadl_UserDefinedDataType.__init__)


def test_sadl_userdefineddatatype_constructor_args():
    sig = inspect.signature(sadl_UserDefinedDataType.__init__)
    params = list(sig.parameters.keys())



def test_resourcebysetop_is_not_abstract():
    assert not inspect.isabstract(ResourceBySetOp)


def test_resourcebysetop_constructor_exists():
    assert callable(ResourceBySetOp.__init__)


def test_resourcebysetop_constructor_args():
    sig = inspect.signature(ResourceBySetOp.__init__)
    params = list(sig.parameters.keys())



def test_sadl_intersectionresource_is_not_abstract():
    assert not inspect.isabstract(sadl_IntersectionResource)


def test_sadl_intersectionresource_constructor_exists():
    assert callable(sadl_IntersectionResource.__init__)


def test_sadl_intersectionresource_constructor_args():
    sig = inspect.signature(sadl_IntersectionResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl_unionresource_is_not_abstract():
    assert not inspect.isabstract(sadl_UnionResource)


def test_sadl_unionresource_constructor_exists():
    assert callable(sadl_UnionResource.__init__)


def test_sadl_unionresource_constructor_args():
    sig = inspect.signature(sadl_UnionResource.__init__)
    params = list(sig.parameters.keys())



def test_sadl_rangetype_is_not_abstract():
    assert not inspect.isabstract(sadl_RangeType)


def test_sadl_rangetype_constructor_exists():
    assert callable(sadl_RangeType.__init__)


def test_sadl_rangetype_constructor_args():
    sig = inspect.signature(sadl_RangeType.__init__)
    params = list(sig.parameters.keys())
    assert "dataType" in params, "Missing parameter 'dataType'"

def test_sadl_rangetype_has_dataType():
    assert hasattr(sadl_RangeType, "dataType")
    descriptor = None
    for klass in sadl_RangeType.__mro__:
        if "dataType" in klass.__dict__:
            descriptor = klass.__dict__["dataType"]
            break
    assert isinstance(descriptor, property)



def test_sadl_range_is_not_abstract():
    assert not inspect.isabstract(sadl_Range)


def test_sadl_range_constructor_exists():
    assert callable(sadl_Range.__init__)


def test_sadl_range_constructor_args():
    sig = inspect.signature(sadl_Range.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "lists" in params, "Missing parameter 'lists'"
    assert "list" in params, "Missing parameter 'list'"

def test_sadl_range_has_single():
    assert hasattr(sadl_Range, "single")
    descriptor = None
    for klass in sadl_Range.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_sadl_range_has_lists():
    assert hasattr(sadl_Range, "lists")
    descriptor = None
    for klass in sadl_Range.__mro__:
        if "lists" in klass.__dict__:
            descriptor = klass.__dict__["lists"]
            break
    assert isinstance(descriptor, property)

def test_sadl_range_has_list():
    assert hasattr(sadl_Range, "list")
    descriptor = None
    for klass in sadl_Range.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_sadl_addlclassinfo_is_not_abstract():
    assert not inspect.isabstract(sadl_AddlClassInfo)


def test_sadl_addlclassinfo_constructor_exists():
    assert callable(sadl_AddlClassInfo.__init__)


def test_sadl_addlclassinfo_constructor_args():
    sig = inspect.signature(sadl_AddlClassInfo.__init__)
    params = list(sig.parameters.keys())



def test_sadl_enumeratedinstances_is_not_abstract():
    assert not inspect.isabstract(sadl_EnumeratedInstances)


def test_sadl_enumeratedinstances_constructor_exists():
    assert callable(sadl_EnumeratedInstances.__init__)


def test_sadl_enumeratedinstances_constructor_args():
    sig = inspect.signature(sadl_EnumeratedInstances.__init__)
    params = list(sig.parameters.keys())



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_expr_is_not_abstract():
    assert not inspect.isabstract(sadl_Expr)


def test_sadl_expr_constructor_exists():
    assert callable(sadl_Expr.__init__)


def test_sadl_expr_constructor_args():
    sig = inspect.signature(sadl_Expr.__init__)
    params = list(sig.parameters.keys())



def test_sadl_query_is_not_abstract():
    assert not inspect.isabstract(sadl_Query)


def test_sadl_query_constructor_exists():
    assert callable(sadl_Query.__init__)


def test_sadl_query_constructor_args():
    sig = inspect.signature(sadl_Query.__init__)
    params = list(sig.parameters.keys())



def test_sadl_rule_is_not_abstract():
    assert not inspect.isabstract(sadl_Rule)


def test_sadl_rule_constructor_exists():
    assert callable(sadl_Rule.__init__)


def test_sadl_rule_constructor_args():
    sig = inspect.signature(sadl_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sadl_rule_has_name():
    assert hasattr(sadl_Rule, "name")
    descriptor = None
    for klass in sadl_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sadl_test_is_not_abstract():
    assert not inspect.isabstract(sadl_Test)


def test_sadl_test_constructor_exists():
    assert callable(sadl_Test.__init__)


def test_sadl_test_constructor_args():
    sig = inspect.signature(sadl_Test.__init__)
    params = list(sig.parameters.keys())



def test_sadl_display_is_not_abstract():
    assert not inspect.isabstract(sadl_Display)


def test_sadl_display_constructor_exists():
    assert callable(sadl_Display.__init__)


def test_sadl_display_constructor_args():
    sig = inspect.signature(sadl_Display.__init__)
    params = list(sig.parameters.keys())
    assert "displayString" in params, "Missing parameter 'displayString'"
    assert "model" in params, "Missing parameter 'model'"

def test_sadl_display_has_displayString():
    assert hasattr(sadl_Display, "displayString")
    descriptor = None
    for klass in sadl_Display.__mro__:
        if "displayString" in klass.__dict__:
            descriptor = klass.__dict__["displayString"]
            break
    assert isinstance(descriptor, property)

def test_sadl_display_has_model():
    assert hasattr(sadl_Display, "model")
    descriptor = None
    for klass in sadl_Display.__mro__:
        if "model" in klass.__dict__:
            descriptor = klass.__dict__["model"]
            break
    assert isinstance(descriptor, property)



def test_sadl_explanation_is_not_abstract():
    assert not inspect.isabstract(sadl_Explanation)


def test_sadl_explanation_constructor_exists():
    assert callable(sadl_Explanation.__init__)


def test_sadl_explanation_constructor_args():
    sig = inspect.signature(sadl_Explanation.__init__)
    params = list(sig.parameters.keys())
    assert "rulename" in params, "Missing parameter 'rulename'"

def test_sadl_explanation_has_rulename():
    assert hasattr(sadl_Explanation, "rulename")
    descriptor = None
    for klass in sadl_Explanation.__mro__:
        if "rulename" in klass.__dict__:
            descriptor = klass.__dict__["rulename"]
            break
    assert isinstance(descriptor, property)



def test_sadl_statement_is_not_abstract():
    assert not inspect.isabstract(sadl_Statement)


def test_sadl_statement_constructor_exists():
    assert callable(sadl_Statement.__init__)


def test_sadl_statement_constructor_args():
    sig = inspect.signature(sadl_Statement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_condition_is_not_abstract():
    assert not inspect.isabstract(sadl_Condition)


def test_sadl_condition_constructor_exists():
    assert callable(sadl_Condition.__init__)


def test_sadl_condition_constructor_args():
    sig = inspect.signature(sadl_Condition.__init__)
    params = list(sig.parameters.keys())



def test_sadl_resourceidentifier_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceIdentifier)


def test_sadl_resourceidentifier_constructor_exists():
    assert callable(sadl_ResourceIdentifier.__init__)


def test_sadl_resourceidentifier_constructor_args():
    sig = inspect.signature(sadl_ResourceIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sadl_existingresourcelist_is_not_abstract():
    assert not inspect.isabstract(sadl_ExistingResourceList)


def test_sadl_existingresourcelist_constructor_exists():
    assert callable(sadl_ExistingResourceList.__init__)


def test_sadl_existingresourcelist_constructor_args():
    sig = inspect.signature(sadl_ExistingResourceList.__init__)
    params = list(sig.parameters.keys())



def test_resourceidentifier_is_not_abstract():
    assert not inspect.isabstract(ResourceIdentifier)


def test_resourceidentifier_constructor_exists():
    assert callable(ResourceIdentifier.__init__)


def test_resourceidentifier_constructor_args():
    sig = inspect.signature(ResourceIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_sadl_resourcebyrestriction_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceByRestriction)


def test_sadl_resourcebyrestriction_constructor_exists():
    assert callable(sadl_ResourceByRestriction.__init__)


def test_sadl_resourcebyrestriction_constructor_args():
    sig = inspect.signature(sadl_ResourceByRestriction.__init__)
    params = list(sig.parameters.keys())
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl_resourcebyrestriction_has_annType():
    assert hasattr(sadl_ResourceByRestriction, "annType")
    descriptor = None
    for klass in sadl_ResourceByRestriction.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl_resourcebysetop_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceBySetOp)


def test_sadl_resourcebysetop_constructor_exists():
    assert callable(sadl_ResourceBySetOp.__init__)


def test_sadl_resourcebysetop_constructor_args():
    sig = inspect.signature(sadl_ResourceBySetOp.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl_resourcebysetop_has_op():
    assert hasattr(sadl_ResourceBySetOp, "op")
    descriptor = None
    for klass in sadl_ResourceBySetOp.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_sadl_resourcebysetop_has_annType():
    assert hasattr(sadl_ResourceBySetOp, "annType")
    descriptor = None
    for klass in sadl_ResourceBySetOp.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl_resourcebyname_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceByName)


def test_sadl_resourcebyname_constructor_exists():
    assert callable(sadl_ResourceByName.__init__)


def test_sadl_resourcebyname_constructor_args():
    sig = inspect.signature(sadl_ResourceByName.__init__)
    params = list(sig.parameters.keys())



def test_sadl_literalvalue_is_not_abstract():
    assert not inspect.isabstract(sadl_LiteralValue)


def test_sadl_literalvalue_constructor_exists():
    assert callable(sadl_LiteralValue.__init__)


def test_sadl_literalvalue_constructor_args():
    sig = inspect.signature(sadl_LiteralValue.__init__)
    params = list(sig.parameters.keys())
    assert "literalBoolean" in params, "Missing parameter 'literalBoolean'"
    assert "literalString" in params, "Missing parameter 'literalString'"
    assert "literalNumber" in params, "Missing parameter 'literalNumber'"

def test_sadl_literalvalue_has_literalBoolean():
    assert hasattr(sadl_LiteralValue, "literalBoolean")
    descriptor = None
    for klass in sadl_LiteralValue.__mro__:
        if "literalBoolean" in klass.__dict__:
            descriptor = klass.__dict__["literalBoolean"]
            break
    assert isinstance(descriptor, property)

def test_sadl_literalvalue_has_literalString():
    assert hasattr(sadl_LiteralValue, "literalString")
    descriptor = None
    for klass in sadl_LiteralValue.__mro__:
        if "literalString" in klass.__dict__:
            descriptor = klass.__dict__["literalString"]
            break
    assert isinstance(descriptor, property)

def test_sadl_literalvalue_has_literalNumber():
    assert hasattr(sadl_LiteralValue, "literalNumber")
    descriptor = None
    for klass in sadl_LiteralValue.__mro__:
        if "literalNumber" in klass.__dict__:
            descriptor = klass.__dict__["literalNumber"]
            break
    assert isinstance(descriptor, property)



def test_sadl_literallist_is_not_abstract():
    assert not inspect.isabstract(sadl_LiteralList)


def test_sadl_literallist_constructor_exists():
    assert callable(sadl_LiteralList.__init__)


def test_sadl_literallist_constructor_args():
    sig = inspect.signature(sadl_LiteralList.__init__)
    params = list(sig.parameters.keys())



def test_sadl_resourcelist_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceList)


def test_sadl_resourcelist_constructor_exists():
    assert callable(sadl_ResourceList.__init__)


def test_sadl_resourcelist_constructor_args():
    sig = inspect.signature(sadl_ResourceList.__init__)
    params = list(sig.parameters.keys())



def test_sadl_resourcename_is_not_abstract():
    assert not inspect.isabstract(sadl_ResourceName)


def test_sadl_resourcename_constructor_exists():
    assert callable(sadl_ResourceName.__init__)


def test_sadl_resourcename_constructor_args():
    sig = inspect.signature(sadl_ResourceName.__init__)
    params = list(sig.parameters.keys())
    assert "annType" in params, "Missing parameter 'annType'"
    assert "name" in params, "Missing parameter 'name'"

def test_sadl_resourcename_has_annType():
    assert hasattr(sadl_ResourceName, "annType")
    descriptor = None
    for klass in sadl_ResourceName.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)

def test_sadl_resourcename_has_name():
    assert hasattr(sadl_ResourceName, "name")
    descriptor = None
    for klass in sadl_ResourceName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sadl_contentlist_is_not_abstract():
    assert not inspect.isabstract(sadl_ContentList)


def test_sadl_contentlist_constructor_exists():
    assert callable(sadl_ContentList.__init__)


def test_sadl_contentlist_constructor_args():
    sig = inspect.signature(sadl_ContentList.__init__)
    params = list(sig.parameters.keys())
    assert "annContent" in params, "Missing parameter 'annContent'"

def test_sadl_contentlist_has_annContent():
    assert hasattr(sadl_ContentList, "annContent")
    descriptor = None
    for klass in sadl_ContentList.__mro__:
        if "annContent" in klass.__dict__:
            descriptor = klass.__dict__["annContent"]
            break
    assert isinstance(descriptor, property)



def test_sadl_modelelement_is_not_abstract():
    assert not inspect.isabstract(sadl_ModelElement)


def test_sadl_modelelement_constructor_exists():
    assert callable(sadl_ModelElement.__init__)


def test_sadl_modelelement_constructor_args():
    sig = inspect.signature(sadl_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_sadl_import_is_not_abstract():
    assert not inspect.isabstract(sadl_Import)


def test_sadl_import_constructor_exists():
    assert callable(sadl_Import.__init__)


def test_sadl_import_constructor_args():
    sig = inspect.signature(sadl_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importURI" in params, "Missing parameter 'importURI'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_sadl_import_has_importURI():
    assert hasattr(sadl_Import, "importURI")
    descriptor = None
    for klass in sadl_Import.__mro__:
        if "importURI" in klass.__dict__:
            descriptor = klass.__dict__["importURI"]
            break
    assert isinstance(descriptor, property)

def test_sadl_import_has_alias():
    assert hasattr(sadl_Import, "alias")
    descriptor = None
    for klass in sadl_Import.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_sadl_modelname_is_not_abstract():
    assert not inspect.isabstract(sadl_ModelName)


def test_sadl_modelname_constructor_exists():
    assert callable(sadl_ModelName.__init__)


def test_sadl_modelname_constructor_args():
    sig = inspect.signature(sadl_ModelName.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "version" in params, "Missing parameter 'version'"
    assert "baseUri" in params, "Missing parameter 'baseUri'"
    assert "annType" in params, "Missing parameter 'annType'"

def test_sadl_modelname_has_alias():
    assert hasattr(sadl_ModelName, "alias")
    descriptor = None
    for klass in sadl_ModelName.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_sadl_modelname_has_version():
    assert hasattr(sadl_ModelName, "version")
    descriptor = None
    for klass in sadl_ModelName.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_sadl_modelname_has_baseUri():
    assert hasattr(sadl_ModelName, "baseUri")
    descriptor = None
    for klass in sadl_ModelName.__mro__:
        if "baseUri" in klass.__dict__:
            descriptor = klass.__dict__["baseUri"]
            break
    assert isinstance(descriptor, property)

def test_sadl_modelname_has_annType():
    assert hasattr(sadl_ModelName, "annType")
    descriptor = None
    for klass in sadl_ModelName.__mro__:
        if "annType" in klass.__dict__:
            descriptor = klass.__dict__["annType"]
            break
    assert isinstance(descriptor, property)



def test_sadl_model_is_not_abstract():
    assert not inspect.isabstract(sadl_Model)


def test_sadl_model_constructor_exists():
    assert callable(sadl_Model.__init__)


def test_sadl_model_constructor_args():
    sig = inspect.signature(sadl_Model.__init__)
    params = list(sig.parameters.keys())

def test_datatype_exists():
    # Check that the Enumeration exists
    assert DataType is not None

def test_datatype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataType]
    expected_literals = [
        "time",
        "date",
        "int",
        "boolean",
        "dateTime",
        "long",
        "float",
        "data",
        "gYear",
        "anyURI",
        "base64Binary",
        "hexBinary",
        "double",
        "decimal",
        "string",
        "gDay",
        "gMonthDay",
        "gYearMonth",
        "duration",
        "gMonth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataType"


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
sadl_ValueRow_strategy = st.builds(
    sadl_ValueRow,
)
sadl_ValueTable_strategy = st.builds(
    sadl_ValueTable,
)
sadl_IntervalValue_strategy = st.builds(
    sadl_IntervalValue,
    op=
        safe_text
)
sadl_GraphPattern_strategy = st.builds(
    sadl_GraphPattern,
)
sadl_OrderElement_strategy = st.builds(
    sadl_OrderElement,
    order=
        safe_text
)
sadl_OrderList_strategy = st.builds(
    sadl_OrderList,
)
Expression_strategy = st.builds(
    Expression,
)
sadl_AskQueryExpression_strategy = st.builds(
    sadl_AskQueryExpression,
)
sadl_JunctionExpression_strategy = st.builds(
    sadl_JunctionExpression,
    op=
        safe_text
)
sadl_UnaryOpExpression_strategy = st.builds(
    sadl_UnaryOpExpression,
    op=
        safe_text
)
sadl_ConstructExpression_strategy = st.builds(
    sadl_ConstructExpression,
)
sadl_BinaryOpExpression_strategy = st.builds(
    sadl_BinaryOpExpression,
    op=
        safe_text
)
sadl_SelectExpression_strategy = st.builds(
    sadl_SelectExpression,
    orderby=
        safe_text,
    distinct=
        safe_text,
    allVars=
        safe_text
)
sadl_Expression_strategy = st.builds(
    sadl_Expression,
    func=
        safe_text
)
sadl_ElementSet_strategy = st.builds(
    sadl_ElementSet,
)
sadl_Object_strategy = st.builds(
    sadl_Object,
)
sadl_VariableList_strategy = st.builds(
    sadl_VariableList,
)
GraphPattern_strategy = st.builds(
    GraphPattern,
)
sadl_InstAttrSPV_strategy = st.builds(
    sadl_InstAttrSPV,
)
sadl_ExistentialNegation_strategy = st.builds(
    sadl_ExistentialNegation,
)
sadl_InstAttrPSV_strategy = st.builds(
    sadl_InstAttrPSV,
)
sadl_PropOfSubj_strategy = st.builds(
    sadl_PropOfSubj,
)
sadl_SubTypeOf_strategy = st.builds(
    sadl_SubTypeOf,
)
sadl_SubjProp_strategy = st.builds(
    sadl_SubjProp,
)
sadl_MergedTriples_strategy = st.builds(
    sadl_MergedTriples,
)
sadl_EmbeddedInstanceDeclaration_strategy = st.builds(
    sadl_EmbeddedInstanceDeclaration,
)
sadl_WithPhrase_strategy = st.builds(
    sadl_WithPhrase,
)
sadl_WithChain_strategy = st.builds(
    sadl_WithChain,
)
sadl_OfPhrase_strategy = st.builds(
    sadl_OfPhrase,
    article=
        safe_text
)
sadl_TypeDeclaration_strategy = st.builds(
    sadl_TypeDeclaration,
)
EmbeddedInstanceDeclaration_strategy = st.builds(
    EmbeddedInstanceDeclaration,
)
InstanceDeclarationStatement_strategy = st.builds(
    InstanceDeclarationStatement,
)
sadl_InstanceDeclaration_strategy = st.builds(
    sadl_InstanceDeclaration,
    article=
        safe_text
)
sadl_OfPatternReturningValues_strategy = st.builds(
    sadl_OfPatternReturningValues,
)
sadl_PropValPartialTriple_strategy = st.builds(
    sadl_PropValPartialTriple,
)
sadl_IsInverseOf_strategy = st.builds(
    sadl_IsInverseOf,
)
sadl_AdditionalPropertyInfo_strategy = st.builds(
    sadl_AdditionalPropertyInfo,
    isfunc=
        safe_text,
    isinvfunc=
        safe_text,
    isTrans=
        safe_text,
    isSym=
        safe_text
)
sadl_TypedBNode_strategy = st.builds(
    sadl_TypedBNode,
    article=
        safe_text
)
sadl_ExplicitValue_strategy = st.builds(
    sadl_ExplicitValue,
    valueList=
        safe_text,
    term=
        safe_text
)
sadl_EObject_strategy = st.builds(
    sadl_EObject,
)
Condition_strategy = st.builds(
    Condition,
)
sadl_CardCondition_strategy = st.builds(
    sadl_CardCondition,
    card=
        safe_text
)
sadl_MaxCardCondition_strategy = st.builds(
    sadl_MaxCardCondition,
    card=
        safe_text
)
sadl_MinCardCondition_strategy = st.builds(
    sadl_MinCardCondition,
    card=
        safe_text
)
sadl_HasValueCondition_strategy = st.builds(
    sadl_HasValueCondition,
)
sadl_SomeValuesCondition_strategy = st.builds(
    sadl_SomeValuesCondition,
)
sadl_AllValuesCondition_strategy = st.builds(
    sadl_AllValuesCondition,
)
sadl_PropertyOfClass_strategy = st.builds(
    sadl_PropertyOfClass,
)
sadl_Facets_strategy = st.builds(
    sadl_Facets,
    min=
        safe_text,
    len=
        safe_text,
    maxlen=
        safe_text,
    values=
        safe_text,
    maxexin=
        safe_text,
    max=
        safe_text,
    minexin=
        safe_text,
    regex=
        safe_text,
    minlen=
        safe_text
)
sadl_DataTypeRestriction_strategy = st.builds(
    sadl_DataTypeRestriction,
    basetypes=
        safe_text,
    basetype=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
sadl_InstanceDifferentFrom_strategy = st.builds(
    sadl_InstanceDifferentFrom,
)
sadl_EnumeratedAllAndSomeValuesFrom_strategy = st.builds(
    sadl_EnumeratedAllAndSomeValuesFrom,
)
sadl_InverseProperty_strategy = st.builds(
    sadl_InverseProperty,
)
sadl_SymmetricalProperty_strategy = st.builds(
    sadl_SymmetricalProperty,
)
sadl_InstancesAllDifferent_strategy = st.builds(
    sadl_InstancesAllDifferent,
)
sadl_AllValuesFrom_strategy = st.builds(
    sadl_AllValuesFrom,
)
sadl_InstanceDeclarationStatement_strategy = st.builds(
    sadl_InstanceDeclarationStatement,
)
sadl_TransitiveProperty_strategy = st.builds(
    sadl_TransitiveProperty,
)
sadl_EquivalentConcepts_strategy = st.builds(
    sadl_EquivalentConcepts,
)
sadl_MaxCardinality_strategy = st.builds(
    sadl_MaxCardinality,
)
sadl_ExistingInstanceAttribution_strategy = st.builds(
    sadl_ExistingInstanceAttribution,
)
sadl_DisjointClasses_strategy = st.builds(
    sadl_DisjointClasses,
)
sadl_DefaultValue_strategy = st.builds(
    sadl_DefaultValue,
    level=
        safe_text
)
sadl_HasValue_strategy = st.builds(
    sadl_HasValue,
)
sadl_NecessaryAndSufficient_strategy = st.builds(
    sadl_NecessaryAndSufficient,
    article=
        safe_text
)
sadl_SomeValuesFrom_strategy = st.builds(
    sadl_SomeValuesFrom,
)
sadl_InverseFunctionalProperty_strategy = st.builds(
    sadl_InverseFunctionalProperty,
)
sadl_ComplementOfClass_strategy = st.builds(
    sadl_ComplementOfClass,
)
sadl_EnumeratedAllValuesFrom_strategy = st.builds(
    sadl_EnumeratedAllValuesFrom,
)
sadl_MinCardinality_strategy = st.builds(
    sadl_MinCardinality,
)
sadl_PropertyDeclaration_strategy = st.builds(
    sadl_PropertyDeclaration,
    article=
        safe_text
)
sadl_FunctionalProperty_strategy = st.builds(
    sadl_FunctionalProperty,
)
sadl_Cardinality_strategy = st.builds(
    sadl_Cardinality,
)
sadl_ClassDeclaration_strategy = st.builds(
    sadl_ClassDeclaration,
)
sadl_UserDefinedDataType_strategy = st.builds(
    sadl_UserDefinedDataType,
)
ResourceBySetOp_strategy = st.builds(
    ResourceBySetOp,
)
sadl_IntersectionResource_strategy = st.builds(
    sadl_IntersectionResource,
)
sadl_UnionResource_strategy = st.builds(
    sadl_UnionResource,
)
sadl_RangeType_strategy = st.builds(
    sadl_RangeType,
    dataType=
        safe_text
)
sadl_Range_strategy = st.builds(
    sadl_Range,
    single=
        safe_text,
    lists=
        safe_text,
    list=
        safe_text
)
sadl_AddlClassInfo_strategy = st.builds(
    sadl_AddlClassInfo,
)
sadl_EnumeratedInstances_strategy = st.builds(
    sadl_EnumeratedInstances,
)
ModelElement_strategy = st.builds(
    ModelElement,
)
sadl_Expr_strategy = st.builds(
    sadl_Expr,
)
sadl_Query_strategy = st.builds(
    sadl_Query,
)
sadl_Rule_strategy = st.builds(
    sadl_Rule,
    name=
        safe_text
)
sadl_Test_strategy = st.builds(
    sadl_Test,
)
sadl_Display_strategy = st.builds(
    sadl_Display,
    displayString=
        safe_text,
    model=
        safe_text
)
sadl_Explanation_strategy = st.builds(
    sadl_Explanation,
    rulename=
        safe_text
)
sadl_Statement_strategy = st.builds(
    sadl_Statement,
)
sadl_Condition_strategy = st.builds(
    sadl_Condition,
)
sadl_ResourceIdentifier_strategy = st.builds(
    sadl_ResourceIdentifier,
)
sadl_ExistingResourceList_strategy = st.builds(
    sadl_ExistingResourceList,
)
ResourceIdentifier_strategy = st.builds(
    ResourceIdentifier,
)
sadl_ResourceByRestriction_strategy = st.builds(
    sadl_ResourceByRestriction,
    annType=
        safe_text
)
sadl_ResourceBySetOp_strategy = st.builds(
    sadl_ResourceBySetOp,
    op=
        safe_text,
    annType=
        safe_text
)
sadl_ResourceByName_strategy = st.builds(
    sadl_ResourceByName,
)
sadl_LiteralValue_strategy = st.builds(
    sadl_LiteralValue,
    literalBoolean=
        safe_text,
    literalString=
        safe_text,
    literalNumber=
        safe_text
)
sadl_LiteralList_strategy = st.builds(
    sadl_LiteralList,
)
sadl_ResourceList_strategy = st.builds(
    sadl_ResourceList,
)
sadl_ResourceName_strategy = st.builds(
    sadl_ResourceName,
    annType=
        safe_text,
    name=
        safe_text
)
sadl_ContentList_strategy = st.builds(
    sadl_ContentList,
    annContent=
        safe_text
)
sadl_ModelElement_strategy = st.builds(
    sadl_ModelElement,
)
sadl_Import_strategy = st.builds(
    sadl_Import,
    importURI=
        safe_text,
    alias=
        safe_text
)
sadl_ModelName_strategy = st.builds(
    sadl_ModelName,
    alias=
        safe_text,
    version=
        safe_text,
    baseUri=
        safe_text,
    annType=
        safe_text
)
sadl_Model_strategy = st.builds(
    sadl_Model,
)

@given(instance=sadl_ValueRow_strategy)
@settings(max_examples=50)
def test_sadl_valuerow_instantiation(instance):
    assert isinstance(instance, sadl_ValueRow)

@given(instance=sadl_ValueTable_strategy)
@settings(max_examples=50)
def test_sadl_valuetable_instantiation(instance):
    assert isinstance(instance, sadl_ValueTable)

@given(instance=sadl_IntervalValue_strategy)
@settings(max_examples=50)
def test_sadl_intervalvalue_instantiation(instance):
    assert isinstance(instance, sadl_IntervalValue)



@given(instance=sadl_IntervalValue_strategy)
def test_sadl_intervalvalue_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl_GraphPattern_strategy)
@settings(max_examples=50)
def test_sadl_graphpattern_instantiation(instance):
    assert isinstance(instance, sadl_GraphPattern)

@given(instance=sadl_OrderElement_strategy)
@settings(max_examples=50)
def test_sadl_orderelement_instantiation(instance):
    assert isinstance(instance, sadl_OrderElement)



@given(instance=sadl_OrderElement_strategy)
def test_sadl_orderelement_order_setter(instance):
    original = instance.order
    instance.order = original
    assert instance.order == original

@given(instance=sadl_OrderList_strategy)
@settings(max_examples=50)
def test_sadl_orderlist_instantiation(instance):
    assert isinstance(instance, sadl_OrderList)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=sadl_AskQueryExpression_strategy)
@settings(max_examples=50)
def test_sadl_askqueryexpression_instantiation(instance):
    assert isinstance(instance, sadl_AskQueryExpression)

@given(instance=sadl_JunctionExpression_strategy)
@settings(max_examples=50)
def test_sadl_junctionexpression_instantiation(instance):
    assert isinstance(instance, sadl_JunctionExpression)



@given(instance=sadl_JunctionExpression_strategy)
def test_sadl_junctionexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl_UnaryOpExpression_strategy)
@settings(max_examples=50)
def test_sadl_unaryopexpression_instantiation(instance):
    assert isinstance(instance, sadl_UnaryOpExpression)



@given(instance=sadl_UnaryOpExpression_strategy)
def test_sadl_unaryopexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl_ConstructExpression_strategy)
@settings(max_examples=50)
def test_sadl_constructexpression_instantiation(instance):
    assert isinstance(instance, sadl_ConstructExpression)

@given(instance=sadl_BinaryOpExpression_strategy)
@settings(max_examples=50)
def test_sadl_binaryopexpression_instantiation(instance):
    assert isinstance(instance, sadl_BinaryOpExpression)



@given(instance=sadl_BinaryOpExpression_strategy)
def test_sadl_binaryopexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=sadl_SelectExpression_strategy)
@settings(max_examples=50)
def test_sadl_selectexpression_instantiation(instance):
    assert isinstance(instance, sadl_SelectExpression)



@given(instance=sadl_SelectExpression_strategy)
def test_sadl_selectexpression_orderby_setter(instance):
    original = instance.orderby
    instance.orderby = original
    assert instance.orderby == original



@given(instance=sadl_SelectExpression_strategy)
def test_sadl_selectexpression_distinct_setter(instance):
    original = instance.distinct
    instance.distinct = original
    assert instance.distinct == original



@given(instance=sadl_SelectExpression_strategy)
def test_sadl_selectexpression_allVars_setter(instance):
    original = instance.allVars
    instance.allVars = original
    assert instance.allVars == original

@given(instance=sadl_Expression_strategy)
@settings(max_examples=50)
def test_sadl_expression_instantiation(instance):
    assert isinstance(instance, sadl_Expression)



@given(instance=sadl_Expression_strategy)
def test_sadl_expression_func_setter(instance):
    original = instance.func
    instance.func = original
    assert instance.func == original

@given(instance=sadl_ElementSet_strategy)
@settings(max_examples=50)
def test_sadl_elementset_instantiation(instance):
    assert isinstance(instance, sadl_ElementSet)

@given(instance=sadl_Object_strategy)
@settings(max_examples=50)
def test_sadl_object_instantiation(instance):
    assert isinstance(instance, sadl_Object)

@given(instance=sadl_VariableList_strategy)
@settings(max_examples=50)
def test_sadl_variablelist_instantiation(instance):
    assert isinstance(instance, sadl_VariableList)

@given(instance=GraphPattern_strategy)
@settings(max_examples=50)
def test_graphpattern_instantiation(instance):
    assert isinstance(instance, GraphPattern)

@given(instance=sadl_InstAttrSPV_strategy)
@settings(max_examples=50)
def test_sadl_instattrspv_instantiation(instance):
    assert isinstance(instance, sadl_InstAttrSPV)

@given(instance=sadl_ExistentialNegation_strategy)
@settings(max_examples=50)
def test_sadl_existentialnegation_instantiation(instance):
    assert isinstance(instance, sadl_ExistentialNegation)

@given(instance=sadl_InstAttrPSV_strategy)
@settings(max_examples=50)
def test_sadl_instattrpsv_instantiation(instance):
    assert isinstance(instance, sadl_InstAttrPSV)

@given(instance=sadl_PropOfSubj_strategy)
@settings(max_examples=50)
def test_sadl_propofsubj_instantiation(instance):
    assert isinstance(instance, sadl_PropOfSubj)

@given(instance=sadl_SubTypeOf_strategy)
@settings(max_examples=50)
def test_sadl_subtypeof_instantiation(instance):
    assert isinstance(instance, sadl_SubTypeOf)

@given(instance=sadl_SubjProp_strategy)
@settings(max_examples=50)
def test_sadl_subjprop_instantiation(instance):
    assert isinstance(instance, sadl_SubjProp)

@given(instance=sadl_MergedTriples_strategy)
@settings(max_examples=50)
def test_sadl_mergedtriples_instantiation(instance):
    assert isinstance(instance, sadl_MergedTriples)

@given(instance=sadl_EmbeddedInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_embeddedinstancedeclaration_instantiation(instance):
    assert isinstance(instance, sadl_EmbeddedInstanceDeclaration)

@given(instance=sadl_WithPhrase_strategy)
@settings(max_examples=50)
def test_sadl_withphrase_instantiation(instance):
    assert isinstance(instance, sadl_WithPhrase)

@given(instance=sadl_WithChain_strategy)
@settings(max_examples=50)
def test_sadl_withchain_instantiation(instance):
    assert isinstance(instance, sadl_WithChain)

@given(instance=sadl_OfPhrase_strategy)
@settings(max_examples=50)
def test_sadl_ofphrase_instantiation(instance):
    assert isinstance(instance, sadl_OfPhrase)



@given(instance=sadl_OfPhrase_strategy)
def test_sadl_ofphrase_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl_TypeDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_typedeclaration_instantiation(instance):
    assert isinstance(instance, sadl_TypeDeclaration)

@given(instance=EmbeddedInstanceDeclaration_strategy)
@settings(max_examples=50)
def test_embeddedinstancedeclaration_instantiation(instance):
    assert isinstance(instance, EmbeddedInstanceDeclaration)

@given(instance=InstanceDeclarationStatement_strategy)
@settings(max_examples=50)
def test_instancedeclarationstatement_instantiation(instance):
    assert isinstance(instance, InstanceDeclarationStatement)

@given(instance=sadl_InstanceDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_instancedeclaration_instantiation(instance):
    assert isinstance(instance, sadl_InstanceDeclaration)



@given(instance=sadl_InstanceDeclaration_strategy)
def test_sadl_instancedeclaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl_OfPatternReturningValues_strategy)
@settings(max_examples=50)
def test_sadl_ofpatternreturningvalues_instantiation(instance):
    assert isinstance(instance, sadl_OfPatternReturningValues)

@given(instance=sadl_PropValPartialTriple_strategy)
@settings(max_examples=50)
def test_sadl_propvalpartialtriple_instantiation(instance):
    assert isinstance(instance, sadl_PropValPartialTriple)

@given(instance=sadl_IsInverseOf_strategy)
@settings(max_examples=50)
def test_sadl_isinverseof_instantiation(instance):
    assert isinstance(instance, sadl_IsInverseOf)

@given(instance=sadl_AdditionalPropertyInfo_strategy)
@settings(max_examples=50)
def test_sadl_additionalpropertyinfo_instantiation(instance):
    assert isinstance(instance, sadl_AdditionalPropertyInfo)



@given(instance=sadl_AdditionalPropertyInfo_strategy)
def test_sadl_additionalpropertyinfo_isfunc_setter(instance):
    original = instance.isfunc
    instance.isfunc = original
    assert instance.isfunc == original



@given(instance=sadl_AdditionalPropertyInfo_strategy)
def test_sadl_additionalpropertyinfo_isinvfunc_setter(instance):
    original = instance.isinvfunc
    instance.isinvfunc = original
    assert instance.isinvfunc == original



@given(instance=sadl_AdditionalPropertyInfo_strategy)
def test_sadl_additionalpropertyinfo_isTrans_setter(instance):
    original = instance.isTrans
    instance.isTrans = original
    assert instance.isTrans == original



@given(instance=sadl_AdditionalPropertyInfo_strategy)
def test_sadl_additionalpropertyinfo_isSym_setter(instance):
    original = instance.isSym
    instance.isSym = original
    assert instance.isSym == original

@given(instance=sadl_TypedBNode_strategy)
@settings(max_examples=50)
def test_sadl_typedbnode_instantiation(instance):
    assert isinstance(instance, sadl_TypedBNode)



@given(instance=sadl_TypedBNode_strategy)
def test_sadl_typedbnode_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl_ExplicitValue_strategy)
@settings(max_examples=50)
def test_sadl_explicitvalue_instantiation(instance):
    assert isinstance(instance, sadl_ExplicitValue)



@given(instance=sadl_ExplicitValue_strategy)
def test_sadl_explicitvalue_valueList_setter(instance):
    original = instance.valueList
    instance.valueList = original
    assert instance.valueList == original



@given(instance=sadl_ExplicitValue_strategy)
def test_sadl_explicitvalue_term_setter(instance):
    original = instance.term
    instance.term = original
    assert instance.term == original

@given(instance=sadl_EObject_strategy)
@settings(max_examples=50)
def test_sadl_eobject_instantiation(instance):
    assert isinstance(instance, sadl_EObject)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=sadl_CardCondition_strategy)
@settings(max_examples=50)
def test_sadl_cardcondition_instantiation(instance):
    assert isinstance(instance, sadl_CardCondition)



@given(instance=sadl_CardCondition_strategy)
def test_sadl_cardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl_MaxCardCondition_strategy)
@settings(max_examples=50)
def test_sadl_maxcardcondition_instantiation(instance):
    assert isinstance(instance, sadl_MaxCardCondition)



@given(instance=sadl_MaxCardCondition_strategy)
def test_sadl_maxcardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl_MinCardCondition_strategy)
@settings(max_examples=50)
def test_sadl_mincardcondition_instantiation(instance):
    assert isinstance(instance, sadl_MinCardCondition)



@given(instance=sadl_MinCardCondition_strategy)
def test_sadl_mincardcondition_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=sadl_HasValueCondition_strategy)
@settings(max_examples=50)
def test_sadl_hasvaluecondition_instantiation(instance):
    assert isinstance(instance, sadl_HasValueCondition)

@given(instance=sadl_SomeValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl_somevaluescondition_instantiation(instance):
    assert isinstance(instance, sadl_SomeValuesCondition)

@given(instance=sadl_AllValuesCondition_strategy)
@settings(max_examples=50)
def test_sadl_allvaluescondition_instantiation(instance):
    assert isinstance(instance, sadl_AllValuesCondition)

@given(instance=sadl_PropertyOfClass_strategy)
@settings(max_examples=50)
def test_sadl_propertyofclass_instantiation(instance):
    assert isinstance(instance, sadl_PropertyOfClass)

@given(instance=sadl_Facets_strategy)
@settings(max_examples=50)
def test_sadl_facets_instantiation(instance):
    assert isinstance(instance, sadl_Facets)



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_len_setter(instance):
    original = instance.len
    instance.len = original
    assert instance.len == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_maxlen_setter(instance):
    original = instance.maxlen
    instance.maxlen = original
    assert instance.maxlen == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_maxexin_setter(instance):
    original = instance.maxexin
    instance.maxexin = original
    assert instance.maxexin == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_minexin_setter(instance):
    original = instance.minexin
    instance.minexin = original
    assert instance.minexin == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_regex_setter(instance):
    original = instance.regex
    instance.regex = original
    assert instance.regex == original



@given(instance=sadl_Facets_strategy)
def test_sadl_facets_minlen_setter(instance):
    original = instance.minlen
    instance.minlen = original
    assert instance.minlen == original

@given(instance=sadl_DataTypeRestriction_strategy)
@settings(max_examples=50)
def test_sadl_datatyperestriction_instantiation(instance):
    assert isinstance(instance, sadl_DataTypeRestriction)



@given(instance=sadl_DataTypeRestriction_strategy)
def test_sadl_datatyperestriction_basetypes_setter(instance):
    original = instance.basetypes
    instance.basetypes = original
    assert instance.basetypes == original



@given(instance=sadl_DataTypeRestriction_strategy)
def test_sadl_datatyperestriction_basetype_setter(instance):
    original = instance.basetype
    instance.basetype = original
    assert instance.basetype == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=sadl_InstanceDifferentFrom_strategy)
@settings(max_examples=50)
def test_sadl_instancedifferentfrom_instantiation(instance):
    assert isinstance(instance, sadl_InstanceDifferentFrom)

@given(instance=sadl_EnumeratedAllAndSomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl_enumeratedallandsomevaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl_EnumeratedAllAndSomeValuesFrom)

@given(instance=sadl_InverseProperty_strategy)
@settings(max_examples=50)
def test_sadl_inverseproperty_instantiation(instance):
    assert isinstance(instance, sadl_InverseProperty)

@given(instance=sadl_SymmetricalProperty_strategy)
@settings(max_examples=50)
def test_sadl_symmetricalproperty_instantiation(instance):
    assert isinstance(instance, sadl_SymmetricalProperty)

@given(instance=sadl_InstancesAllDifferent_strategy)
@settings(max_examples=50)
def test_sadl_instancesalldifferent_instantiation(instance):
    assert isinstance(instance, sadl_InstancesAllDifferent)

@given(instance=sadl_AllValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl_allvaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl_AllValuesFrom)

@given(instance=sadl_InstanceDeclarationStatement_strategy)
@settings(max_examples=50)
def test_sadl_instancedeclarationstatement_instantiation(instance):
    assert isinstance(instance, sadl_InstanceDeclarationStatement)

@given(instance=sadl_TransitiveProperty_strategy)
@settings(max_examples=50)
def test_sadl_transitiveproperty_instantiation(instance):
    assert isinstance(instance, sadl_TransitiveProperty)

@given(instance=sadl_EquivalentConcepts_strategy)
@settings(max_examples=50)
def test_sadl_equivalentconcepts_instantiation(instance):
    assert isinstance(instance, sadl_EquivalentConcepts)

@given(instance=sadl_MaxCardinality_strategy)
@settings(max_examples=50)
def test_sadl_maxcardinality_instantiation(instance):
    assert isinstance(instance, sadl_MaxCardinality)

@given(instance=sadl_ExistingInstanceAttribution_strategy)
@settings(max_examples=50)
def test_sadl_existinginstanceattribution_instantiation(instance):
    assert isinstance(instance, sadl_ExistingInstanceAttribution)

@given(instance=sadl_DisjointClasses_strategy)
@settings(max_examples=50)
def test_sadl_disjointclasses_instantiation(instance):
    assert isinstance(instance, sadl_DisjointClasses)

@given(instance=sadl_DefaultValue_strategy)
@settings(max_examples=50)
def test_sadl_defaultvalue_instantiation(instance):
    assert isinstance(instance, sadl_DefaultValue)



@given(instance=sadl_DefaultValue_strategy)
def test_sadl_defaultvalue_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=sadl_HasValue_strategy)
@settings(max_examples=50)
def test_sadl_hasvalue_instantiation(instance):
    assert isinstance(instance, sadl_HasValue)

@given(instance=sadl_NecessaryAndSufficient_strategy)
@settings(max_examples=50)
def test_sadl_necessaryandsufficient_instantiation(instance):
    assert isinstance(instance, sadl_NecessaryAndSufficient)



@given(instance=sadl_NecessaryAndSufficient_strategy)
def test_sadl_necessaryandsufficient_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl_SomeValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl_somevaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl_SomeValuesFrom)

@given(instance=sadl_InverseFunctionalProperty_strategy)
@settings(max_examples=50)
def test_sadl_inversefunctionalproperty_instantiation(instance):
    assert isinstance(instance, sadl_InverseFunctionalProperty)

@given(instance=sadl_ComplementOfClass_strategy)
@settings(max_examples=50)
def test_sadl_complementofclass_instantiation(instance):
    assert isinstance(instance, sadl_ComplementOfClass)

@given(instance=sadl_EnumeratedAllValuesFrom_strategy)
@settings(max_examples=50)
def test_sadl_enumeratedallvaluesfrom_instantiation(instance):
    assert isinstance(instance, sadl_EnumeratedAllValuesFrom)

@given(instance=sadl_MinCardinality_strategy)
@settings(max_examples=50)
def test_sadl_mincardinality_instantiation(instance):
    assert isinstance(instance, sadl_MinCardinality)

@given(instance=sadl_PropertyDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_propertydeclaration_instantiation(instance):
    assert isinstance(instance, sadl_PropertyDeclaration)



@given(instance=sadl_PropertyDeclaration_strategy)
def test_sadl_propertydeclaration_article_setter(instance):
    original = instance.article
    instance.article = original
    assert instance.article == original

@given(instance=sadl_FunctionalProperty_strategy)
@settings(max_examples=50)
def test_sadl_functionalproperty_instantiation(instance):
    assert isinstance(instance, sadl_FunctionalProperty)

@given(instance=sadl_Cardinality_strategy)
@settings(max_examples=50)
def test_sadl_cardinality_instantiation(instance):
    assert isinstance(instance, sadl_Cardinality)

@given(instance=sadl_ClassDeclaration_strategy)
@settings(max_examples=50)
def test_sadl_classdeclaration_instantiation(instance):
    assert isinstance(instance, sadl_ClassDeclaration)

@given(instance=sadl_UserDefinedDataType_strategy)
@settings(max_examples=50)
def test_sadl_userdefineddatatype_instantiation(instance):
    assert isinstance(instance, sadl_UserDefinedDataType)

@given(instance=ResourceBySetOp_strategy)
@settings(max_examples=50)
def test_resourcebysetop_instantiation(instance):
    assert isinstance(instance, ResourceBySetOp)

@given(instance=sadl_IntersectionResource_strategy)
@settings(max_examples=50)
def test_sadl_intersectionresource_instantiation(instance):
    assert isinstance(instance, sadl_IntersectionResource)

@given(instance=sadl_UnionResource_strategy)
@settings(max_examples=50)
def test_sadl_unionresource_instantiation(instance):
    assert isinstance(instance, sadl_UnionResource)

@given(instance=sadl_RangeType_strategy)
@settings(max_examples=50)
def test_sadl_rangetype_instantiation(instance):
    assert isinstance(instance, sadl_RangeType)



@given(instance=sadl_RangeType_strategy)
def test_sadl_rangetype_dataType_setter(instance):
    original = instance.dataType
    instance.dataType = original
    assert instance.dataType == original

@given(instance=sadl_Range_strategy)
@settings(max_examples=50)
def test_sadl_range_instantiation(instance):
    assert isinstance(instance, sadl_Range)



@given(instance=sadl_Range_strategy)
def test_sadl_range_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original



@given(instance=sadl_Range_strategy)
def test_sadl_range_lists_setter(instance):
    original = instance.lists
    instance.lists = original
    assert instance.lists == original



@given(instance=sadl_Range_strategy)
def test_sadl_range_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=sadl_AddlClassInfo_strategy)
@settings(max_examples=50)
def test_sadl_addlclassinfo_instantiation(instance):
    assert isinstance(instance, sadl_AddlClassInfo)

@given(instance=sadl_EnumeratedInstances_strategy)
@settings(max_examples=50)
def test_sadl_enumeratedinstances_instantiation(instance):
    assert isinstance(instance, sadl_EnumeratedInstances)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=sadl_Expr_strategy)
@settings(max_examples=50)
def test_sadl_expr_instantiation(instance):
    assert isinstance(instance, sadl_Expr)

@given(instance=sadl_Query_strategy)
@settings(max_examples=50)
def test_sadl_query_instantiation(instance):
    assert isinstance(instance, sadl_Query)

@given(instance=sadl_Rule_strategy)
@settings(max_examples=50)
def test_sadl_rule_instantiation(instance):
    assert isinstance(instance, sadl_Rule)



@given(instance=sadl_Rule_strategy)
def test_sadl_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sadl_Test_strategy)
@settings(max_examples=50)
def test_sadl_test_instantiation(instance):
    assert isinstance(instance, sadl_Test)

@given(instance=sadl_Display_strategy)
@settings(max_examples=50)
def test_sadl_display_instantiation(instance):
    assert isinstance(instance, sadl_Display)



@given(instance=sadl_Display_strategy)
def test_sadl_display_displayString_setter(instance):
    original = instance.displayString
    instance.displayString = original
    assert instance.displayString == original



@given(instance=sadl_Display_strategy)
def test_sadl_display_model_setter(instance):
    original = instance.model
    instance.model = original
    assert instance.model == original

@given(instance=sadl_Explanation_strategy)
@settings(max_examples=50)
def test_sadl_explanation_instantiation(instance):
    assert isinstance(instance, sadl_Explanation)



@given(instance=sadl_Explanation_strategy)
def test_sadl_explanation_rulename_setter(instance):
    original = instance.rulename
    instance.rulename = original
    assert instance.rulename == original

@given(instance=sadl_Statement_strategy)
@settings(max_examples=50)
def test_sadl_statement_instantiation(instance):
    assert isinstance(instance, sadl_Statement)

@given(instance=sadl_Condition_strategy)
@settings(max_examples=50)
def test_sadl_condition_instantiation(instance):
    assert isinstance(instance, sadl_Condition)

@given(instance=sadl_ResourceIdentifier_strategy)
@settings(max_examples=50)
def test_sadl_resourceidentifier_instantiation(instance):
    assert isinstance(instance, sadl_ResourceIdentifier)

@given(instance=sadl_ExistingResourceList_strategy)
@settings(max_examples=50)
def test_sadl_existingresourcelist_instantiation(instance):
    assert isinstance(instance, sadl_ExistingResourceList)

@given(instance=ResourceIdentifier_strategy)
@settings(max_examples=50)
def test_resourceidentifier_instantiation(instance):
    assert isinstance(instance, ResourceIdentifier)

@given(instance=sadl_ResourceByRestriction_strategy)
@settings(max_examples=50)
def test_sadl_resourcebyrestriction_instantiation(instance):
    assert isinstance(instance, sadl_ResourceByRestriction)



@given(instance=sadl_ResourceByRestriction_strategy)
def test_sadl_resourcebyrestriction_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl_ResourceBySetOp_strategy)
@settings(max_examples=50)
def test_sadl_resourcebysetop_instantiation(instance):
    assert isinstance(instance, sadl_ResourceBySetOp)



@given(instance=sadl_ResourceBySetOp_strategy)
def test_sadl_resourcebysetop_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=sadl_ResourceBySetOp_strategy)
def test_sadl_resourcebysetop_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl_ResourceByName_strategy)
@settings(max_examples=50)
def test_sadl_resourcebyname_instantiation(instance):
    assert isinstance(instance, sadl_ResourceByName)

@given(instance=sadl_LiteralValue_strategy)
@settings(max_examples=50)
def test_sadl_literalvalue_instantiation(instance):
    assert isinstance(instance, sadl_LiteralValue)



@given(instance=sadl_LiteralValue_strategy)
def test_sadl_literalvalue_literalBoolean_setter(instance):
    original = instance.literalBoolean
    instance.literalBoolean = original
    assert instance.literalBoolean == original



@given(instance=sadl_LiteralValue_strategy)
def test_sadl_literalvalue_literalString_setter(instance):
    original = instance.literalString
    instance.literalString = original
    assert instance.literalString == original



@given(instance=sadl_LiteralValue_strategy)
def test_sadl_literalvalue_literalNumber_setter(instance):
    original = instance.literalNumber
    instance.literalNumber = original
    assert instance.literalNumber == original

@given(instance=sadl_LiteralList_strategy)
@settings(max_examples=50)
def test_sadl_literallist_instantiation(instance):
    assert isinstance(instance, sadl_LiteralList)

@given(instance=sadl_ResourceList_strategy)
@settings(max_examples=50)
def test_sadl_resourcelist_instantiation(instance):
    assert isinstance(instance, sadl_ResourceList)

@given(instance=sadl_ResourceName_strategy)
@settings(max_examples=50)
def test_sadl_resourcename_instantiation(instance):
    assert isinstance(instance, sadl_ResourceName)



@given(instance=sadl_ResourceName_strategy)
def test_sadl_resourcename_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original



@given(instance=sadl_ResourceName_strategy)
def test_sadl_resourcename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sadl_ContentList_strategy)
@settings(max_examples=50)
def test_sadl_contentlist_instantiation(instance):
    assert isinstance(instance, sadl_ContentList)



@given(instance=sadl_ContentList_strategy)
def test_sadl_contentlist_annContent_setter(instance):
    original = instance.annContent
    instance.annContent = original
    assert instance.annContent == original

@given(instance=sadl_ModelElement_strategy)
@settings(max_examples=50)
def test_sadl_modelelement_instantiation(instance):
    assert isinstance(instance, sadl_ModelElement)

@given(instance=sadl_Import_strategy)
@settings(max_examples=50)
def test_sadl_import_instantiation(instance):
    assert isinstance(instance, sadl_Import)



@given(instance=sadl_Import_strategy)
def test_sadl_import_importURI_setter(instance):
    original = instance.importURI
    instance.importURI = original
    assert instance.importURI == original



@given(instance=sadl_Import_strategy)
def test_sadl_import_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=sadl_ModelName_strategy)
@settings(max_examples=50)
def test_sadl_modelname_instantiation(instance):
    assert isinstance(instance, sadl_ModelName)



@given(instance=sadl_ModelName_strategy)
def test_sadl_modelname_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=sadl_ModelName_strategy)
def test_sadl_modelname_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=sadl_ModelName_strategy)
def test_sadl_modelname_baseUri_setter(instance):
    original = instance.baseUri
    instance.baseUri = original
    assert instance.baseUri == original



@given(instance=sadl_ModelName_strategy)
def test_sadl_modelname_annType_setter(instance):
    original = instance.annType
    instance.annType = original
    assert instance.annType == original

@given(instance=sadl_Model_strategy)
@settings(max_examples=50)
def test_sadl_model_instantiation(instance):
    assert isinstance(instance, sadl_Model)
