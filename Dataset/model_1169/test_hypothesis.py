import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OclModelElement,
    OclFeature,
    TupleType,
    atlstatic_OCL_Operation,
    atlstatic_OCL_Attribute,
    CollectionType,
    atlstatic_OCL_SetType,
    atlstatic_OCL_SequenceType,
    MapType,
    OclContextDefinition,
    VariableExp,
    IterateExp,
    atlstatic_OCL_OrderedSetType,
    atlstatic_OCL_BagType,
    NumericType,
    atlstatic_OCL_RealType,
    atlstatic_OCL_IntegerType,
    Primitive,
    atlstatic_OCL_NumericType,
    atlstatic_OCL_BooleanType,
    atlstatic_OCL_StringType,
    TupleTypeAttribute,
    Attribute,
    Operation,
    MapExp,
    MapElement,
    TupleExp,
    TuplePart,
    IfExp,
    OclType,
    atlstatic_OCL_MapType,
    atlstatic_OCL_TupleType,
    atlstatic_OCL_OclAnyType,
    atlstatic_OCL_Primitive,
    atlstatic_OCL_OclModelElement,
    atlstatic_OCL_CollectionType,
    OperationCallExp,
    LoopExp,
    atlstatic_OCL_IteratorExp,
    LetExp,
    CollectionExp,
    PropertyCallExp,
    Iterator,
    Binding,
    PatternElement,
    atlstatic_ATL_OutPatternElement,
    Statement,
    atlstatic_ATL_IfStat,
    atlstatic_ATL_BindingStat,
    atlstatic_ATL_ForStat,
    atlstatic_ATL_ExpressionStat,
    InPatternElement,
    atlstatic_ATL_SimpleInPatternElement,
    Parameter,
    MatchedRule,
    atlstatic_ATL_LazyMatchedRule,
    InPattern,
    Rule,
    atlstatic_ATL_CalledRule,
    atlstatic_ATL_MatchedRule,
    RuleVariableDeclaration,
    ActionBlock,
    OutPattern,
    atlstatic_ATL_InPatternElement,
    VariableDeclaration,
    atlstatic_OCL_Iterator,
    atlstatic_ATL_RuleVariableDeclaration,
    atlstatic_OCL_TuplePart,
    atlstatic_OCL_Parameter,
    atlstatic_ATL_PatternElement,
    OutPatternElement,
    atlstatic_ATL_ForEachOutPatternElement,
    atlstatic_ATL_SimpleOutPatternElement,
    DropPattern,
    OclModel,
    OclExpression,
    atlstatic_OCL_LetExp,
    atlstatic_OCL_OclType,
    atlstatic_OCL_VariableExp,
    atlstatic_OCL_MapExp,
    atlstatic_OCL_IfExp,
    Helper,
    Unit,
    atlstatic_ATL_Module,
    atlstatic_ATL_Query,
    atlstatic_ATL_Library,
    LibraryRef,
    LocatedElement,
    atlstatic_ATL_ActionBlock,
    atlstatic_ATL_Statement,
    atlstatic_ATL_Binding,
    atlstatic_ATL_InPattern,
    atlstatic_OCL_TupleTypeAttribute,
    atlstatic_OCL_OclModel,
    atlstatic_OCL_OclExpression,
    atlstatic_ATL_OutPattern,
    atlstatic_ATL_LibraryRef,
    atlstatic_ATL_DropPattern,
    atlstatic_OCL_OclContextDefinition,
    atlstatic_OCL_OclFeatureDefinition,
    atlstatic_OCL_OclFeature,
    atlstatic_OCL_MapElement,
    atlstatic_ATL_Unit,
    atlstatic_ATL_LocatedElement,
    OclFeatureDefinition,
    Library,
    Query,
    atlstatic_ATL_ModuleElement,
    ModuleElement,
    atlstatic_ATL_Rule,
    atlstatic_ATL_Helper,
    atlstatic_OCL_IterateExp,
    atlstatic_OCL_VariableDeclaration,
    atlstatic_OCL_PropertyCallExp,
    atlstatic_OCL_OclUndefinedExp,
    atlstatic_OCL_EnumLiteralExp,
    atlstatic_OCL_LoopExp,
    atlstatic_OCL_CollectionOperationCallExp,
    atlstatic_OCL_OperatorCallExp,
    atlstatic_OCL_OperationCallExp,
    atlstatic_OCL_NavigationOrAttributeCallExp,
    atlstatic_OCL_TupleExp,
    atlstatic_OCL_SetExp,
    atlstatic_OCL_SequenceExp,
    atlstatic_OCL_OrderedSetExp,
    atlstatic_OCL_BagExp,
    atlstatic_OCL_CollectionExp,
    NumericExp,
    atlstatic_OCL_IntegerExp,
    atlstatic_OCL_RealExp,
    PrimitiveExp,
    atlstatic_OCL_BooleanExp,
    atlstatic_OCL_NumericExp,
    atlstatic_OCL_StringExp,
    atlstatic_OCL_PrimitiveExp,
    atlstatic_OCL_SuperExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_Operation)


def test_atlstatic_ocl_operation_constructor_exists():
    assert callable(atlstatic_OCL_Operation.__init__)


def test_atlstatic_ocl_operation_constructor_args():
    sig = inspect.signature(atlstatic_OCL_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_operation_has_name():
    assert hasattr(atlstatic_OCL_Operation, "name")
    descriptor = None
    for klass in atlstatic_OCL_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_attribute_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_Attribute)


def test_atlstatic_ocl_attribute_constructor_exists():
    assert callable(atlstatic_OCL_Attribute.__init__)


def test_atlstatic_ocl_attribute_constructor_args():
    sig = inspect.signature(atlstatic_OCL_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_attribute_has_name():
    assert hasattr(atlstatic_OCL_Attribute, "name")
    descriptor = None
    for klass in atlstatic_OCL_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_settype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_SetType)


def test_atlstatic_ocl_settype_constructor_exists():
    assert callable(atlstatic_OCL_SetType.__init__)


def test_atlstatic_ocl_settype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_SequenceType)


def test_atlstatic_ocl_sequencetype_constructor_exists():
    assert callable(atlstatic_OCL_SequenceType.__init__)


def test_atlstatic_ocl_sequencetype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_maptype_is_not_abstract():
    assert not inspect.isabstract(MapType)


def test_maptype_constructor_exists():
    assert callable(MapType.__init__)


def test_maptype_constructor_args():
    sig = inspect.signature(MapType.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_variableexp_is_not_abstract():
    assert not inspect.isabstract(VariableExp)


def test_variableexp_constructor_exists():
    assert callable(VariableExp.__init__)


def test_variableexp_constructor_args():
    sig = inspect.signature(VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_iterateexp_is_not_abstract():
    assert not inspect.isabstract(IterateExp)


def test_iterateexp_constructor_exists():
    assert callable(IterateExp.__init__)


def test_iterateexp_constructor_args():
    sig = inspect.signature(IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OrderedSetType)


def test_atlstatic_ocl_orderedsettype_constructor_exists():
    assert callable(atlstatic_OCL_OrderedSetType.__init__)


def test_atlstatic_ocl_orderedsettype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_BagType)


def test_atlstatic_ocl_bagtype_constructor_exists():
    assert callable(atlstatic_OCL_BagType.__init__)


def test_atlstatic_ocl_bagtype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_realtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_RealType)


def test_atlstatic_ocl_realtype_constructor_exists():
    assert callable(atlstatic_OCL_RealType.__init__)


def test_atlstatic_ocl_realtype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_RealType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_integertype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_IntegerType)


def test_atlstatic_ocl_integertype_constructor_exists():
    assert callable(atlstatic_OCL_IntegerType.__init__)


def test_atlstatic_ocl_integertype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_NumericType)


def test_atlstatic_ocl_numerictype_constructor_exists():
    assert callable(atlstatic_OCL_NumericType.__init__)


def test_atlstatic_ocl_numerictype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_BooleanType)


def test_atlstatic_ocl_booleantype_constructor_exists():
    assert callable(atlstatic_OCL_BooleanType.__init__)


def test_atlstatic_ocl_booleantype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_StringType)


def test_atlstatic_ocl_stringtype_constructor_exists():
    assert callable(atlstatic_OCL_StringType.__init__)


def test_atlstatic_ocl_stringtype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_StringType.__init__)
    params = list(sig.parameters.keys())



def test_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(TupleTypeAttribute)


def test_tupletypeattribute_constructor_exists():
    assert callable(TupleTypeAttribute.__init__)


def test_tupletypeattribute_constructor_args():
    sig = inspect.signature(TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_attribute_is_not_abstract():
    assert not inspect.isabstract(Attribute)


def test_attribute_constructor_exists():
    assert callable(Attribute.__init__)


def test_attribute_constructor_args():
    sig = inspect.signature(Attribute.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_mapexp_is_not_abstract():
    assert not inspect.isabstract(MapExp)


def test_mapexp_constructor_exists():
    assert callable(MapExp.__init__)


def test_mapexp_constructor_args():
    sig = inspect.signature(MapExp.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_tupleexp_is_not_abstract():
    assert not inspect.isabstract(TupleExp)


def test_tupleexp_constructor_exists():
    assert callable(TupleExp.__init__)


def test_tupleexp_constructor_args():
    sig = inspect.signature(TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_ifexp_is_not_abstract():
    assert not inspect.isabstract(IfExp)


def test_ifexp_constructor_exists():
    assert callable(IfExp.__init__)


def test_ifexp_constructor_args():
    sig = inspect.signature(IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocltype_is_not_abstract():
    assert not inspect.isabstract(OclType)


def test_ocltype_constructor_exists():
    assert callable(OclType.__init__)


def test_ocltype_constructor_args():
    sig = inspect.signature(OclType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_maptype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_MapType)


def test_atlstatic_ocl_maptype_constructor_exists():
    assert callable(atlstatic_OCL_MapType.__init__)


def test_atlstatic_ocl_maptype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_MapType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_TupleType)


def test_atlstatic_ocl_tupletype_constructor_exists():
    assert callable(atlstatic_OCL_TupleType.__init__)


def test_atlstatic_ocl_tupletype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclAnyType)


def test_atlstatic_ocl_oclanytype_constructor_exists():
    assert callable(atlstatic_OCL_OclAnyType.__init__)


def test_atlstatic_ocl_oclanytype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_primitive_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_Primitive)


def test_atlstatic_ocl_primitive_constructor_exists():
    assert callable(atlstatic_OCL_Primitive.__init__)


def test_atlstatic_ocl_primitive_constructor_args():
    sig = inspect.signature(atlstatic_OCL_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclModelElement)


def test_atlstatic_ocl_oclmodelelement_constructor_exists():
    assert callable(atlstatic_OCL_OclModelElement.__init__)


def test_atlstatic_ocl_oclmodelelement_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_CollectionType)


def test_atlstatic_ocl_collectiontype_constructor_exists():
    assert callable(atlstatic_OCL_CollectionType.__init__)


def test_atlstatic_ocl_collectiontype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_IteratorExp)


def test_atlstatic_ocl_iteratorexp_constructor_exists():
    assert callable(atlstatic_OCL_IteratorExp.__init__)


def test_atlstatic_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_iteratorexp_has_name():
    assert hasattr(atlstatic_OCL_IteratorExp, "name")
    descriptor = None
    for klass in atlstatic_OCL_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_letexp_is_not_abstract():
    assert not inspect.isabstract(LetExp)


def test_letexp_constructor_exists():
    assert callable(LetExp.__init__)


def test_letexp_constructor_args():
    sig = inspect.signature(LetExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionexp_is_not_abstract():
    assert not inspect.isabstract(CollectionExp)


def test_collectionexp_constructor_exists():
    assert callable(CollectionExp.__init__)


def test_collectionexp_constructor_args():
    sig = inspect.signature(CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_binding_is_not_abstract():
    assert not inspect.isabstract(Binding)


def test_binding_constructor_exists():
    assert callable(Binding.__init__)


def test_binding_constructor_args():
    sig = inspect.signature(Binding.__init__)
    params = list(sig.parameters.keys())



def test_patternelement_is_not_abstract():
    assert not inspect.isabstract(PatternElement)


def test_patternelement_constructor_exists():
    assert callable(PatternElement.__init__)


def test_patternelement_constructor_args():
    sig = inspect.signature(PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_OutPatternElement)


def test_atlstatic_atl_outpatternelement_constructor_exists():
    assert callable(atlstatic_ATL_OutPatternElement.__init__)


def test_atlstatic_atl_outpatternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_ifstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_IfStat)


def test_atlstatic_atl_ifstat_constructor_exists():
    assert callable(atlstatic_ATL_IfStat.__init__)


def test_atlstatic_atl_ifstat_constructor_args():
    sig = inspect.signature(atlstatic_ATL_IfStat.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_bindingstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_BindingStat)


def test_atlstatic_atl_bindingstat_constructor_exists():
    assert callable(atlstatic_ATL_BindingStat.__init__)


def test_atlstatic_atl_bindingstat_constructor_args():
    sig = inspect.signature(atlstatic_ATL_BindingStat.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"

def test_atlstatic_atl_bindingstat_has_propertyName():
    assert hasattr(atlstatic_ATL_BindingStat, "propertyName")
    descriptor = None
    for klass in atlstatic_ATL_BindingStat.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_bindingstat_has_isAssignment():
    assert hasattr(atlstatic_ATL_BindingStat, "isAssignment")
    descriptor = None
    for klass in atlstatic_ATL_BindingStat.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_forstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_ForStat)


def test_atlstatic_atl_forstat_constructor_exists():
    assert callable(atlstatic_ATL_ForStat.__init__)


def test_atlstatic_atl_forstat_constructor_args():
    sig = inspect.signature(atlstatic_ATL_ForStat.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_expressionstat_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_ExpressionStat)


def test_atlstatic_atl_expressionstat_constructor_exists():
    assert callable(atlstatic_ATL_ExpressionStat.__init__)


def test_atlstatic_atl_expressionstat_constructor_args():
    sig = inspect.signature(atlstatic_ATL_ExpressionStat.__init__)
    params = list(sig.parameters.keys())



def test_inpatternelement_is_not_abstract():
    assert not inspect.isabstract(InPatternElement)


def test_inpatternelement_constructor_exists():
    assert callable(InPatternElement.__init__)


def test_inpatternelement_constructor_args():
    sig = inspect.signature(InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_simpleinpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_SimpleInPatternElement)


def test_atlstatic_atl_simpleinpatternelement_constructor_exists():
    assert callable(atlstatic_ATL_SimpleInPatternElement.__init__)


def test_atlstatic_atl_simpleinpatternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_SimpleInPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_matchedrule_is_not_abstract():
    assert not inspect.isabstract(MatchedRule)


def test_matchedrule_constructor_exists():
    assert callable(MatchedRule.__init__)


def test_matchedrule_constructor_args():
    sig = inspect.signature(MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_lazymatchedrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_LazyMatchedRule)


def test_atlstatic_atl_lazymatchedrule_constructor_exists():
    assert callable(atlstatic_ATL_LazyMatchedRule.__init__)


def test_atlstatic_atl_lazymatchedrule_constructor_args():
    sig = inspect.signature(atlstatic_ATL_LazyMatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_atlstatic_atl_lazymatchedrule_has_isUnique():
    assert hasattr(atlstatic_ATL_LazyMatchedRule, "isUnique")
    descriptor = None
    for klass in atlstatic_ATL_LazyMatchedRule.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_inpattern_is_not_abstract():
    assert not inspect.isabstract(InPattern)


def test_inpattern_constructor_exists():
    assert callable(InPattern.__init__)


def test_inpattern_constructor_args():
    sig = inspect.signature(InPattern.__init__)
    params = list(sig.parameters.keys())



def test_rule_is_not_abstract():
    assert not inspect.isabstract(Rule)


def test_rule_constructor_exists():
    assert callable(Rule.__init__)


def test_rule_constructor_args():
    sig = inspect.signature(Rule.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_calledrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_CalledRule)


def test_atlstatic_atl_calledrule_constructor_exists():
    assert callable(atlstatic_ATL_CalledRule.__init__)


def test_atlstatic_atl_calledrule_constructor_args():
    sig = inspect.signature(atlstatic_ATL_CalledRule.__init__)
    params = list(sig.parameters.keys())
    assert "isEndpoint" in params, "Missing parameter 'isEndpoint'"
    assert "isEntrypoint" in params, "Missing parameter 'isEntrypoint'"

def test_atlstatic_atl_calledrule_has_isEndpoint():
    assert hasattr(atlstatic_ATL_CalledRule, "isEndpoint")
    descriptor = None
    for klass in atlstatic_ATL_CalledRule.__mro__:
        if "isEndpoint" in klass.__dict__:
            descriptor = klass.__dict__["isEndpoint"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_calledrule_has_isEntrypoint():
    assert hasattr(atlstatic_ATL_CalledRule, "isEntrypoint")
    descriptor = None
    for klass in atlstatic_ATL_CalledRule.__mro__:
        if "isEntrypoint" in klass.__dict__:
            descriptor = klass.__dict__["isEntrypoint"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_matchedrule_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_MatchedRule)


def test_atlstatic_atl_matchedrule_constructor_exists():
    assert callable(atlstatic_ATL_MatchedRule.__init__)


def test_atlstatic_atl_matchedrule_constructor_args():
    sig = inspect.signature(atlstatic_ATL_MatchedRule.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"
    assert "isNoDefault" in params, "Missing parameter 'isNoDefault'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_atlstatic_atl_matchedrule_has_isRefining():
    assert hasattr(atlstatic_ATL_MatchedRule, "isRefining")
    descriptor = None
    for klass in atlstatic_ATL_MatchedRule.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_matchedrule_has_isNoDefault():
    assert hasattr(atlstatic_ATL_MatchedRule, "isNoDefault")
    descriptor = None
    for klass in atlstatic_ATL_MatchedRule.__mro__:
        if "isNoDefault" in klass.__dict__:
            descriptor = klass.__dict__["isNoDefault"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_matchedrule_has_isAbstract():
    assert hasattr(atlstatic_ATL_MatchedRule, "isAbstract")
    descriptor = None
    for klass in atlstatic_ATL_MatchedRule.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(RuleVariableDeclaration)


def test_rulevariabledeclaration_constructor_exists():
    assert callable(RuleVariableDeclaration.__init__)


def test_rulevariabledeclaration_constructor_args():
    sig = inspect.signature(RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_actionblock_is_not_abstract():
    assert not inspect.isabstract(ActionBlock)


def test_actionblock_constructor_exists():
    assert callable(ActionBlock.__init__)


def test_actionblock_constructor_args():
    sig = inspect.signature(ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_outpattern_is_not_abstract():
    assert not inspect.isabstract(OutPattern)


def test_outpattern_constructor_exists():
    assert callable(OutPattern.__init__)


def test_outpattern_constructor_args():
    sig = inspect.signature(OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_inpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_InPatternElement)


def test_atlstatic_atl_inpatternelement_constructor_exists():
    assert callable(atlstatic_ATL_InPatternElement.__init__)


def test_atlstatic_atl_inpatternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_InPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_Iterator)


def test_atlstatic_ocl_iterator_constructor_exists():
    assert callable(atlstatic_OCL_Iterator.__init__)


def test_atlstatic_ocl_iterator_constructor_args():
    sig = inspect.signature(atlstatic_OCL_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_rulevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_RuleVariableDeclaration)


def test_atlstatic_atl_rulevariabledeclaration_constructor_exists():
    assert callable(atlstatic_ATL_RuleVariableDeclaration.__init__)


def test_atlstatic_atl_rulevariabledeclaration_constructor_args():
    sig = inspect.signature(atlstatic_ATL_RuleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_TuplePart)


def test_atlstatic_ocl_tuplepart_constructor_exists():
    assert callable(atlstatic_OCL_TuplePart.__init__)


def test_atlstatic_ocl_tuplepart_constructor_args():
    sig = inspect.signature(atlstatic_OCL_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_parameter_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_Parameter)


def test_atlstatic_ocl_parameter_constructor_exists():
    assert callable(atlstatic_OCL_Parameter.__init__)


def test_atlstatic_ocl_parameter_constructor_args():
    sig = inspect.signature(atlstatic_OCL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_patternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_PatternElement)


def test_atlstatic_atl_patternelement_constructor_exists():
    assert callable(atlstatic_ATL_PatternElement.__init__)


def test_atlstatic_atl_patternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_PatternElement.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_foreachoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_ForEachOutPatternElement)


def test_atlstatic_atl_foreachoutpatternelement_constructor_exists():
    assert callable(atlstatic_ATL_ForEachOutPatternElement.__init__)


def test_atlstatic_atl_foreachoutpatternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_ForEachOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_simpleoutpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_SimpleOutPatternElement)


def test_atlstatic_atl_simpleoutpatternelement_constructor_exists():
    assert callable(atlstatic_ATL_SimpleOutPatternElement.__init__)


def test_atlstatic_atl_simpleoutpatternelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_SimpleOutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_droppattern_is_not_abstract():
    assert not inspect.isabstract(DropPattern)


def test_droppattern_constructor_exists():
    assert callable(DropPattern.__init__)


def test_droppattern_constructor_args():
    sig = inspect.signature(DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_LetExp)


def test_atlstatic_ocl_letexp_constructor_exists():
    assert callable(atlstatic_OCL_LetExp.__init__)


def test_atlstatic_ocl_letexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclType)


def test_atlstatic_ocl_ocltype_constructor_exists():
    assert callable(atlstatic_OCL_OclType.__init__)


def test_atlstatic_ocl_ocltype_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_ocltype_has_name():
    assert hasattr(atlstatic_OCL_OclType, "name")
    descriptor = None
    for klass in atlstatic_OCL_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_VariableExp)


def test_atlstatic_ocl_variableexp_constructor_exists():
    assert callable(atlstatic_OCL_VariableExp.__init__)


def test_atlstatic_ocl_variableexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_MapExp)


def test_atlstatic_ocl_mapexp_constructor_exists():
    assert callable(atlstatic_OCL_MapExp.__init__)


def test_atlstatic_ocl_mapexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_IfExp)


def test_atlstatic_ocl_ifexp_constructor_exists():
    assert callable(atlstatic_OCL_IfExp.__init__)


def test_atlstatic_ocl_ifexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_helper_is_not_abstract():
    assert not inspect.isabstract(Helper)


def test_helper_constructor_exists():
    assert callable(Helper.__init__)


def test_helper_constructor_args():
    sig = inspect.signature(Helper.__init__)
    params = list(sig.parameters.keys())



def test_unit_is_not_abstract():
    assert not inspect.isabstract(Unit)


def test_unit_constructor_exists():
    assert callable(Unit.__init__)


def test_unit_constructor_args():
    sig = inspect.signature(Unit.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_module_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Module)


def test_atlstatic_atl_module_constructor_exists():
    assert callable(atlstatic_ATL_Module.__init__)


def test_atlstatic_atl_module_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Module.__init__)
    params = list(sig.parameters.keys())
    assert "isRefining" in params, "Missing parameter 'isRefining'"

def test_atlstatic_atl_module_has_isRefining():
    assert hasattr(atlstatic_ATL_Module, "isRefining")
    descriptor = None
    for klass in atlstatic_ATL_Module.__mro__:
        if "isRefining" in klass.__dict__:
            descriptor = klass.__dict__["isRefining"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_query_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Query)


def test_atlstatic_atl_query_constructor_exists():
    assert callable(atlstatic_ATL_Query.__init__)


def test_atlstatic_atl_query_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Query.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_library_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Library)


def test_atlstatic_atl_library_constructor_exists():
    assert callable(atlstatic_ATL_Library.__init__)


def test_atlstatic_atl_library_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Library.__init__)
    params = list(sig.parameters.keys())



def test_libraryref_is_not_abstract():
    assert not inspect.isabstract(LibraryRef)


def test_libraryref_constructor_exists():
    assert callable(LibraryRef.__init__)


def test_libraryref_constructor_args():
    sig = inspect.signature(LibraryRef.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_actionblock_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_ActionBlock)


def test_atlstatic_atl_actionblock_constructor_exists():
    assert callable(atlstatic_ATL_ActionBlock.__init__)


def test_atlstatic_atl_actionblock_constructor_args():
    sig = inspect.signature(atlstatic_ATL_ActionBlock.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_statement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Statement)


def test_atlstatic_atl_statement_constructor_exists():
    assert callable(atlstatic_ATL_Statement.__init__)


def test_atlstatic_atl_statement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Statement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_binding_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Binding)


def test_atlstatic_atl_binding_constructor_exists():
    assert callable(atlstatic_ATL_Binding.__init__)


def test_atlstatic_atl_binding_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Binding.__init__)
    params = list(sig.parameters.keys())
    assert "isAssignment" in params, "Missing parameter 'isAssignment'"
    assert "propertyName" in params, "Missing parameter 'propertyName'"

def test_atlstatic_atl_binding_has_isAssignment():
    assert hasattr(atlstatic_ATL_Binding, "isAssignment")
    descriptor = None
    for klass in atlstatic_ATL_Binding.__mro__:
        if "isAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isAssignment"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_binding_has_propertyName():
    assert hasattr(atlstatic_ATL_Binding, "propertyName")
    descriptor = None
    for klass in atlstatic_ATL_Binding.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_inpattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_InPattern)


def test_atlstatic_atl_inpattern_constructor_exists():
    assert callable(atlstatic_ATL_InPattern.__init__)


def test_atlstatic_atl_inpattern_constructor_args():
    sig = inspect.signature(atlstatic_ATL_InPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_TupleTypeAttribute)


def test_atlstatic_ocl_tupletypeattribute_constructor_exists():
    assert callable(atlstatic_OCL_TupleTypeAttribute.__init__)


def test_atlstatic_ocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(atlstatic_OCL_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_tupletypeattribute_has_name():
    assert hasattr(atlstatic_OCL_TupleTypeAttribute, "name")
    descriptor = None
    for klass in atlstatic_OCL_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclModel)


def test_atlstatic_ocl_oclmodel_constructor_exists():
    assert callable(atlstatic_OCL_OclModel.__init__)


def test_atlstatic_ocl_oclmodel_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_oclmodel_has_name():
    assert hasattr(atlstatic_OCL_OclModel, "name")
    descriptor = None
    for klass in atlstatic_OCL_OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclExpression)


def test_atlstatic_ocl_oclexpression_constructor_exists():
    assert callable(atlstatic_OCL_OclExpression.__init__)


def test_atlstatic_ocl_oclexpression_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_outpattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_OutPattern)


def test_atlstatic_atl_outpattern_constructor_exists():
    assert callable(atlstatic_ATL_OutPattern.__init__)


def test_atlstatic_atl_outpattern_constructor_args():
    sig = inspect.signature(atlstatic_ATL_OutPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_libraryref_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_LibraryRef)


def test_atlstatic_atl_libraryref_constructor_exists():
    assert callable(atlstatic_ATL_LibraryRef.__init__)


def test_atlstatic_atl_libraryref_constructor_args():
    sig = inspect.signature(atlstatic_ATL_LibraryRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_atl_libraryref_has_name():
    assert hasattr(atlstatic_ATL_LibraryRef, "name")
    descriptor = None
    for klass in atlstatic_ATL_LibraryRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_droppattern_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_DropPattern)


def test_atlstatic_atl_droppattern_constructor_exists():
    assert callable(atlstatic_ATL_DropPattern.__init__)


def test_atlstatic_atl_droppattern_constructor_args():
    sig = inspect.signature(atlstatic_ATL_DropPattern.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclContextDefinition)


def test_atlstatic_ocl_oclcontextdefinition_constructor_exists():
    assert callable(atlstatic_OCL_OclContextDefinition.__init__)


def test_atlstatic_ocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclFeatureDefinition)


def test_atlstatic_ocl_oclfeaturedefinition_constructor_exists():
    assert callable(atlstatic_OCL_OclFeatureDefinition.__init__)


def test_atlstatic_ocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclFeature)


def test_atlstatic_ocl_oclfeature_constructor_exists():
    assert callable(atlstatic_OCL_OclFeature.__init__)


def test_atlstatic_ocl_oclfeature_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_MapElement)


def test_atlstatic_ocl_mapelement_constructor_exists():
    assert callable(atlstatic_OCL_MapElement.__init__)


def test_atlstatic_ocl_mapelement_constructor_args():
    sig = inspect.signature(atlstatic_OCL_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_unit_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Unit)


def test_atlstatic_atl_unit_constructor_exists():
    assert callable(atlstatic_ATL_Unit.__init__)


def test_atlstatic_atl_unit_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Unit.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_atl_unit_has_name():
    assert hasattr(atlstatic_ATL_Unit, "name")
    descriptor = None
    for klass in atlstatic_ATL_Unit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_LocatedElement)


def test_atlstatic_atl_locatedelement_constructor_exists():
    assert callable(atlstatic_ATL_LocatedElement.__init__)


def test_atlstatic_atl_locatedelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_atlstatic_atl_locatedelement_has_location():
    assert hasattr(atlstatic_ATL_LocatedElement, "location")
    descriptor = None
    for klass in atlstatic_ATL_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_locatedelement_has_commentsBefore():
    assert hasattr(atlstatic_ATL_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in atlstatic_ATL_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_atl_locatedelement_has_commentsAfter():
    assert hasattr(atlstatic_ATL_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in atlstatic_ATL_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())



def test_query_is_not_abstract():
    assert not inspect.isabstract(Query)


def test_query_constructor_exists():
    assert callable(Query.__init__)


def test_query_constructor_args():
    sig = inspect.signature(Query.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_moduleelement_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_ModuleElement)


def test_atlstatic_atl_moduleelement_constructor_exists():
    assert callable(atlstatic_ATL_ModuleElement.__init__)


def test_atlstatic_atl_moduleelement_constructor_args():
    sig = inspect.signature(atlstatic_ATL_ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_moduleelement_is_not_abstract():
    assert not inspect.isabstract(ModuleElement)


def test_moduleelement_constructor_exists():
    assert callable(ModuleElement.__init__)


def test_moduleelement_constructor_args():
    sig = inspect.signature(ModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_atl_rule_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Rule)


def test_atlstatic_atl_rule_constructor_exists():
    assert callable(atlstatic_ATL_Rule.__init__)


def test_atlstatic_atl_rule_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Rule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_atl_rule_has_name():
    assert hasattr(atlstatic_ATL_Rule, "name")
    descriptor = None
    for klass in atlstatic_ATL_Rule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_atl_helper_is_not_abstract():
    assert not inspect.isabstract(atlstatic_ATL_Helper)


def test_atlstatic_atl_helper_constructor_exists():
    assert callable(atlstatic_ATL_Helper.__init__)


def test_atlstatic_atl_helper_constructor_args():
    sig = inspect.signature(atlstatic_ATL_Helper.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_IterateExp)


def test_atlstatic_ocl_iterateexp_constructor_exists():
    assert callable(atlstatic_OCL_IterateExp.__init__)


def test_atlstatic_ocl_iterateexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_VariableDeclaration)


def test_atlstatic_ocl_variabledeclaration_constructor_exists():
    assert callable(atlstatic_OCL_VariableDeclaration.__init__)


def test_atlstatic_ocl_variabledeclaration_constructor_args():
    sig = inspect.signature(atlstatic_OCL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_atlstatic_ocl_variabledeclaration_has_id():
    assert hasattr(atlstatic_OCL_VariableDeclaration, "id")
    descriptor = None
    for klass in atlstatic_OCL_VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_atlstatic_ocl_variabledeclaration_has_varName():
    assert hasattr(atlstatic_OCL_VariableDeclaration, "varName")
    descriptor = None
    for klass in atlstatic_OCL_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_PropertyCallExp)


def test_atlstatic_ocl_propertycallexp_constructor_exists():
    assert callable(atlstatic_OCL_PropertyCallExp.__init__)


def test_atlstatic_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OclUndefinedExp)


def test_atlstatic_ocl_oclundefinedexp_constructor_exists():
    assert callable(atlstatic_OCL_OclUndefinedExp.__init__)


def test_atlstatic_ocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_EnumLiteralExp)


def test_atlstatic_ocl_enumliteralexp_constructor_exists():
    assert callable(atlstatic_OCL_EnumLiteralExp.__init__)


def test_atlstatic_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_enumliteralexp_has_name():
    assert hasattr(atlstatic_OCL_EnumLiteralExp, "name")
    descriptor = None
    for klass in atlstatic_OCL_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_LoopExp)


def test_atlstatic_ocl_loopexp_constructor_exists():
    assert callable(atlstatic_OCL_LoopExp.__init__)


def test_atlstatic_ocl_loopexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_CollectionOperationCallExp)


def test_atlstatic_ocl_collectionoperationcallexp_constructor_exists():
    assert callable(atlstatic_OCL_CollectionOperationCallExp.__init__)


def test_atlstatic_ocl_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OperatorCallExp)


def test_atlstatic_ocl_operatorcallexp_constructor_exists():
    assert callable(atlstatic_OCL_OperatorCallExp.__init__)


def test_atlstatic_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OperationCallExp)


def test_atlstatic_ocl_operationcallexp_constructor_exists():
    assert callable(atlstatic_OCL_OperationCallExp.__init__)


def test_atlstatic_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_atlstatic_ocl_operationcallexp_has_operationName():
    assert hasattr(atlstatic_OCL_OperationCallExp, "operationName")
    descriptor = None
    for klass in atlstatic_OCL_OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_NavigationOrAttributeCallExp)


def test_atlstatic_ocl_navigationorattributecallexp_constructor_exists():
    assert callable(atlstatic_OCL_NavigationOrAttributeCallExp.__init__)


def test_atlstatic_ocl_navigationorattributecallexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlstatic_ocl_navigationorattributecallexp_has_name():
    assert hasattr(atlstatic_OCL_NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in atlstatic_OCL_NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_TupleExp)


def test_atlstatic_ocl_tupleexp_constructor_exists():
    assert callable(atlstatic_OCL_TupleExp.__init__)


def test_atlstatic_ocl_tupleexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_setexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_SetExp)


def test_atlstatic_ocl_setexp_constructor_exists():
    assert callable(atlstatic_OCL_SetExp.__init__)


def test_atlstatic_ocl_setexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_SequenceExp)


def test_atlstatic_ocl_sequenceexp_constructor_exists():
    assert callable(atlstatic_OCL_SequenceExp.__init__)


def test_atlstatic_ocl_sequenceexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_OrderedSetExp)


def test_atlstatic_ocl_orderedsetexp_constructor_exists():
    assert callable(atlstatic_OCL_OrderedSetExp.__init__)


def test_atlstatic_ocl_orderedsetexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_BagExp)


def test_atlstatic_ocl_bagexp_constructor_exists():
    assert callable(atlstatic_OCL_BagExp.__init__)


def test_atlstatic_ocl_bagexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_CollectionExp)


def test_atlstatic_ocl_collectionexp_constructor_exists():
    assert callable(atlstatic_OCL_CollectionExp.__init__)


def test_atlstatic_ocl_collectionexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_IntegerExp)


def test_atlstatic_ocl_integerexp_constructor_exists():
    assert callable(atlstatic_OCL_IntegerExp.__init__)


def test_atlstatic_ocl_integerexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_atlstatic_ocl_integerexp_has_integerSymbol():
    assert hasattr(atlstatic_OCL_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in atlstatic_OCL_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_realexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_RealExp)


def test_atlstatic_ocl_realexp_constructor_exists():
    assert callable(atlstatic_OCL_RealExp.__init__)


def test_atlstatic_ocl_realexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_atlstatic_ocl_realexp_has_realSymbol():
    assert hasattr(atlstatic_OCL_RealExp, "realSymbol")
    descriptor = None
    for klass in atlstatic_OCL_RealExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveExp)


def test_primitiveexp_constructor_exists():
    assert callable(PrimitiveExp.__init__)


def test_primitiveexp_constructor_args():
    sig = inspect.signature(PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_BooleanExp)


def test_atlstatic_ocl_booleanexp_constructor_exists():
    assert callable(atlstatic_OCL_BooleanExp.__init__)


def test_atlstatic_ocl_booleanexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_atlstatic_ocl_booleanexp_has_booleanSymbol():
    assert hasattr(atlstatic_OCL_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in atlstatic_OCL_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_NumericExp)


def test_atlstatic_ocl_numericexp_constructor_exists():
    assert callable(atlstatic_OCL_NumericExp.__init__)


def test_atlstatic_ocl_numericexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_StringExp)


def test_atlstatic_ocl_stringexp_constructor_exists():
    assert callable(atlstatic_OCL_StringExp.__init__)


def test_atlstatic_ocl_stringexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_atlstatic_ocl_stringexp_has_stringSymbol():
    assert hasattr(atlstatic_OCL_StringExp, "stringSymbol")
    descriptor = None
    for klass in atlstatic_OCL_StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_atlstatic_ocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_PrimitiveExp)


def test_atlstatic_ocl_primitiveexp_constructor_exists():
    assert callable(atlstatic_OCL_PrimitiveExp.__init__)


def test_atlstatic_ocl_primitiveexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_atlstatic_ocl_superexp_is_not_abstract():
    assert not inspect.isabstract(atlstatic_OCL_SuperExp)


def test_atlstatic_ocl_superexp_constructor_exists():
    assert callable(atlstatic_OCL_SuperExp.__init__)


def test_atlstatic_ocl_superexp_constructor_args():
    sig = inspect.signature(atlstatic_OCL_SuperExp.__init__)
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
OclModelElement_strategy = st.builds(
    OclModelElement,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
TupleType_strategy = st.builds(
    TupleType,
)
atlstatic_OCL_Operation_strategy = st.builds(
    atlstatic_OCL_Operation,
    name=
        safe_text
)
atlstatic_OCL_Attribute_strategy = st.builds(
    atlstatic_OCL_Attribute,
    name=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
atlstatic_OCL_SetType_strategy = st.builds(
    atlstatic_OCL_SetType,
)
atlstatic_OCL_SequenceType_strategy = st.builds(
    atlstatic_OCL_SequenceType,
)
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
atlstatic_OCL_OrderedSetType_strategy = st.builds(
    atlstatic_OCL_OrderedSetType,
)
atlstatic_OCL_BagType_strategy = st.builds(
    atlstatic_OCL_BagType,
)
NumericType_strategy = st.builds(
    NumericType,
)
atlstatic_OCL_RealType_strategy = st.builds(
    atlstatic_OCL_RealType,
)
atlstatic_OCL_IntegerType_strategy = st.builds(
    atlstatic_OCL_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
atlstatic_OCL_NumericType_strategy = st.builds(
    atlstatic_OCL_NumericType,
)
atlstatic_OCL_BooleanType_strategy = st.builds(
    atlstatic_OCL_BooleanType,
)
atlstatic_OCL_StringType_strategy = st.builds(
    atlstatic_OCL_StringType,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
MapExp_strategy = st.builds(
    MapExp,
)
MapElement_strategy = st.builds(
    MapElement,
)
TupleExp_strategy = st.builds(
    TupleExp,
)
TuplePart_strategy = st.builds(
    TuplePart,
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
atlstatic_OCL_MapType_strategy = st.builds(
    atlstatic_OCL_MapType,
)
atlstatic_OCL_TupleType_strategy = st.builds(
    atlstatic_OCL_TupleType,
)
atlstatic_OCL_OclAnyType_strategy = st.builds(
    atlstatic_OCL_OclAnyType,
)
atlstatic_OCL_Primitive_strategy = st.builds(
    atlstatic_OCL_Primitive,
)
atlstatic_OCL_OclModelElement_strategy = st.builds(
    atlstatic_OCL_OclModelElement,
)
atlstatic_OCL_CollectionType_strategy = st.builds(
    atlstatic_OCL_CollectionType,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
atlstatic_OCL_IteratorExp_strategy = st.builds(
    atlstatic_OCL_IteratorExp,
    name=
        safe_text
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
Binding_strategy = st.builds(
    Binding,
)
PatternElement_strategy = st.builds(
    PatternElement,
)
atlstatic_ATL_OutPatternElement_strategy = st.builds(
    atlstatic_ATL_OutPatternElement,
)
Statement_strategy = st.builds(
    Statement,
)
atlstatic_ATL_IfStat_strategy = st.builds(
    atlstatic_ATL_IfStat,
)
atlstatic_ATL_BindingStat_strategy = st.builds(
    atlstatic_ATL_BindingStat,
    propertyName=
        safe_text,
    isAssignment=
        safe_text
)
atlstatic_ATL_ForStat_strategy = st.builds(
    atlstatic_ATL_ForStat,
)
atlstatic_ATL_ExpressionStat_strategy = st.builds(
    atlstatic_ATL_ExpressionStat,
)
InPatternElement_strategy = st.builds(
    InPatternElement,
)
atlstatic_ATL_SimpleInPatternElement_strategy = st.builds(
    atlstatic_ATL_SimpleInPatternElement,
)
Parameter_strategy = st.builds(
    Parameter,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
atlstatic_ATL_LazyMatchedRule_strategy = st.builds(
    atlstatic_ATL_LazyMatchedRule,
    isUnique=
        safe_text
)
InPattern_strategy = st.builds(
    InPattern,
)
Rule_strategy = st.builds(
    Rule,
)
atlstatic_ATL_CalledRule_strategy = st.builds(
    atlstatic_ATL_CalledRule,
    isEndpoint=
        safe_text,
    isEntrypoint=
        safe_text
)
atlstatic_ATL_MatchedRule_strategy = st.builds(
    atlstatic_ATL_MatchedRule,
    isRefining=
        safe_text,
    isNoDefault=
        safe_text,
    isAbstract=
        safe_text
)
RuleVariableDeclaration_strategy = st.builds(
    RuleVariableDeclaration,
)
ActionBlock_strategy = st.builds(
    ActionBlock,
)
OutPattern_strategy = st.builds(
    OutPattern,
)
atlstatic_ATL_InPatternElement_strategy = st.builds(
    atlstatic_ATL_InPatternElement,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
atlstatic_OCL_Iterator_strategy = st.builds(
    atlstatic_OCL_Iterator,
)
atlstatic_ATL_RuleVariableDeclaration_strategy = st.builds(
    atlstatic_ATL_RuleVariableDeclaration,
)
atlstatic_OCL_TuplePart_strategy = st.builds(
    atlstatic_OCL_TuplePart,
)
atlstatic_OCL_Parameter_strategy = st.builds(
    atlstatic_OCL_Parameter,
)
atlstatic_ATL_PatternElement_strategy = st.builds(
    atlstatic_ATL_PatternElement,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
atlstatic_ATL_ForEachOutPatternElement_strategy = st.builds(
    atlstatic_ATL_ForEachOutPatternElement,
)
atlstatic_ATL_SimpleOutPatternElement_strategy = st.builds(
    atlstatic_ATL_SimpleOutPatternElement,
)
DropPattern_strategy = st.builds(
    DropPattern,
)
OclModel_strategy = st.builds(
    OclModel,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atlstatic_OCL_LetExp_strategy = st.builds(
    atlstatic_OCL_LetExp,
)
atlstatic_OCL_OclType_strategy = st.builds(
    atlstatic_OCL_OclType,
    name=
        safe_text
)
atlstatic_OCL_VariableExp_strategy = st.builds(
    atlstatic_OCL_VariableExp,
)
atlstatic_OCL_MapExp_strategy = st.builds(
    atlstatic_OCL_MapExp,
)
atlstatic_OCL_IfExp_strategy = st.builds(
    atlstatic_OCL_IfExp,
)
Helper_strategy = st.builds(
    Helper,
)
Unit_strategy = st.builds(
    Unit,
)
atlstatic_ATL_Module_strategy = st.builds(
    atlstatic_ATL_Module,
    isRefining=
        safe_text
)
atlstatic_ATL_Query_strategy = st.builds(
    atlstatic_ATL_Query,
)
atlstatic_ATL_Library_strategy = st.builds(
    atlstatic_ATL_Library,
)
LibraryRef_strategy = st.builds(
    LibraryRef,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
atlstatic_ATL_ActionBlock_strategy = st.builds(
    atlstatic_ATL_ActionBlock,
)
atlstatic_ATL_Statement_strategy = st.builds(
    atlstatic_ATL_Statement,
)
atlstatic_ATL_Binding_strategy = st.builds(
    atlstatic_ATL_Binding,
    isAssignment=
        safe_text,
    propertyName=
        safe_text
)
atlstatic_ATL_InPattern_strategy = st.builds(
    atlstatic_ATL_InPattern,
)
atlstatic_OCL_TupleTypeAttribute_strategy = st.builds(
    atlstatic_OCL_TupleTypeAttribute,
    name=
        safe_text
)
atlstatic_OCL_OclModel_strategy = st.builds(
    atlstatic_OCL_OclModel,
    name=
        safe_text
)
atlstatic_OCL_OclExpression_strategy = st.builds(
    atlstatic_OCL_OclExpression,
)
atlstatic_ATL_OutPattern_strategy = st.builds(
    atlstatic_ATL_OutPattern,
)
atlstatic_ATL_LibraryRef_strategy = st.builds(
    atlstatic_ATL_LibraryRef,
    name=
        safe_text
)
atlstatic_ATL_DropPattern_strategy = st.builds(
    atlstatic_ATL_DropPattern,
)
atlstatic_OCL_OclContextDefinition_strategy = st.builds(
    atlstatic_OCL_OclContextDefinition,
)
atlstatic_OCL_OclFeatureDefinition_strategy = st.builds(
    atlstatic_OCL_OclFeatureDefinition,
)
atlstatic_OCL_OclFeature_strategy = st.builds(
    atlstatic_OCL_OclFeature,
)
atlstatic_OCL_MapElement_strategy = st.builds(
    atlstatic_OCL_MapElement,
)
atlstatic_ATL_Unit_strategy = st.builds(
    atlstatic_ATL_Unit,
    name=
        safe_text
)
atlstatic_ATL_LocatedElement_strategy = st.builds(
    atlstatic_ATL_LocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
Library_strategy = st.builds(
    Library,
)
Query_strategy = st.builds(
    Query,
)
atlstatic_ATL_ModuleElement_strategy = st.builds(
    atlstatic_ATL_ModuleElement,
)
ModuleElement_strategy = st.builds(
    ModuleElement,
)
atlstatic_ATL_Rule_strategy = st.builds(
    atlstatic_ATL_Rule,
    name=
        safe_text
)
atlstatic_ATL_Helper_strategy = st.builds(
    atlstatic_ATL_Helper,
)
atlstatic_OCL_IterateExp_strategy = st.builds(
    atlstatic_OCL_IterateExp,
)
atlstatic_OCL_VariableDeclaration_strategy = st.builds(
    atlstatic_OCL_VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
atlstatic_OCL_PropertyCallExp_strategy = st.builds(
    atlstatic_OCL_PropertyCallExp,
)
atlstatic_OCL_OclUndefinedExp_strategy = st.builds(
    atlstatic_OCL_OclUndefinedExp,
)
atlstatic_OCL_EnumLiteralExp_strategy = st.builds(
    atlstatic_OCL_EnumLiteralExp,
    name=
        safe_text
)
atlstatic_OCL_LoopExp_strategy = st.builds(
    atlstatic_OCL_LoopExp,
)
atlstatic_OCL_CollectionOperationCallExp_strategy = st.builds(
    atlstatic_OCL_CollectionOperationCallExp,
)
atlstatic_OCL_OperatorCallExp_strategy = st.builds(
    atlstatic_OCL_OperatorCallExp,
)
atlstatic_OCL_OperationCallExp_strategy = st.builds(
    atlstatic_OCL_OperationCallExp,
    operationName=
        safe_text
)
atlstatic_OCL_NavigationOrAttributeCallExp_strategy = st.builds(
    atlstatic_OCL_NavigationOrAttributeCallExp,
    name=
        safe_text
)
atlstatic_OCL_TupleExp_strategy = st.builds(
    atlstatic_OCL_TupleExp,
)
atlstatic_OCL_SetExp_strategy = st.builds(
    atlstatic_OCL_SetExp,
)
atlstatic_OCL_SequenceExp_strategy = st.builds(
    atlstatic_OCL_SequenceExp,
)
atlstatic_OCL_OrderedSetExp_strategy = st.builds(
    atlstatic_OCL_OrderedSetExp,
)
atlstatic_OCL_BagExp_strategy = st.builds(
    atlstatic_OCL_BagExp,
)
atlstatic_OCL_CollectionExp_strategy = st.builds(
    atlstatic_OCL_CollectionExp,
)
NumericExp_strategy = st.builds(
    NumericExp,
)
atlstatic_OCL_IntegerExp_strategy = st.builds(
    atlstatic_OCL_IntegerExp,
    integerSymbol=
        safe_text
)
atlstatic_OCL_RealExp_strategy = st.builds(
    atlstatic_OCL_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
atlstatic_OCL_BooleanExp_strategy = st.builds(
    atlstatic_OCL_BooleanExp,
    booleanSymbol=
        safe_text
)
atlstatic_OCL_NumericExp_strategy = st.builds(
    atlstatic_OCL_NumericExp,
)
atlstatic_OCL_StringExp_strategy = st.builds(
    atlstatic_OCL_StringExp,
    stringSymbol=
        safe_text
)
atlstatic_OCL_PrimitiveExp_strategy = st.builds(
    atlstatic_OCL_PrimitiveExp,
)
atlstatic_OCL_SuperExp_strategy = st.builds(
    atlstatic_OCL_SuperExp,
)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=atlstatic_OCL_Operation_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_operation_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_Operation)



@given(instance=atlstatic_OCL_Operation_strategy)
def test_atlstatic_ocl_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_Attribute_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_attribute_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_Attribute)



@given(instance=atlstatic_OCL_Attribute_strategy)
def test_atlstatic_ocl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=atlstatic_OCL_SetType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_settype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_SetType)

@given(instance=atlstatic_OCL_SequenceType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_sequencetype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_SequenceType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=atlstatic_OCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OrderedSetType)

@given(instance=atlstatic_OCL_BagType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_bagtype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_BagType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=atlstatic_OCL_RealType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_realtype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_RealType)

@given(instance=atlstatic_OCL_IntegerType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_integertype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=atlstatic_OCL_NumericType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_numerictype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_NumericType)

@given(instance=atlstatic_OCL_BooleanType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_booleantype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_BooleanType)

@given(instance=atlstatic_OCL_StringType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_stringtype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_StringType)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=MapExp_strategy)
@settings(max_examples=50)
def test_mapexp_instantiation(instance):
    assert isinstance(instance, MapExp)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=TupleExp_strategy)
@settings(max_examples=50)
def test_tupleexp_instantiation(instance):
    assert isinstance(instance, TupleExp)

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=atlstatic_OCL_MapType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_maptype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_MapType)

@given(instance=atlstatic_OCL_TupleType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_tupletype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_TupleType)

@given(instance=atlstatic_OCL_OclAnyType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclanytype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclAnyType)

@given(instance=atlstatic_OCL_Primitive_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_primitive_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_Primitive)

@given(instance=atlstatic_OCL_OclModelElement_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclModelElement)

@given(instance=atlstatic_OCL_CollectionType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_collectiontype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_CollectionType)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=atlstatic_OCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_IteratorExp)



@given(instance=atlstatic_OCL_IteratorExp_strategy)
def test_atlstatic_ocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=Binding_strategy)
@settings(max_examples=50)
def test_binding_instantiation(instance):
    assert isinstance(instance, Binding)

@given(instance=PatternElement_strategy)
@settings(max_examples=50)
def test_patternelement_instantiation(instance):
    assert isinstance(instance, PatternElement)

@given(instance=atlstatic_ATL_OutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_outpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_OutPatternElement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=atlstatic_ATL_IfStat_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_ifstat_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_IfStat)

@given(instance=atlstatic_ATL_BindingStat_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_bindingstat_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_BindingStat)



@given(instance=atlstatic_ATL_BindingStat_strategy)
def test_atlstatic_atl_bindingstat_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original



@given(instance=atlstatic_ATL_BindingStat_strategy)
def test_atlstatic_atl_bindingstat_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original

@given(instance=atlstatic_ATL_ForStat_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_forstat_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_ForStat)

@given(instance=atlstatic_ATL_ExpressionStat_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_expressionstat_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_ExpressionStat)

@given(instance=InPatternElement_strategy)
@settings(max_examples=50)
def test_inpatternelement_instantiation(instance):
    assert isinstance(instance, InPatternElement)

@given(instance=atlstatic_ATL_SimpleInPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_simpleinpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_SimpleInPatternElement)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=atlstatic_ATL_LazyMatchedRule_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_lazymatchedrule_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_LazyMatchedRule)



@given(instance=atlstatic_ATL_LazyMatchedRule_strategy)
def test_atlstatic_atl_lazymatchedrule_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=InPattern_strategy)
@settings(max_examples=50)
def test_inpattern_instantiation(instance):
    assert isinstance(instance, InPattern)

@given(instance=Rule_strategy)
@settings(max_examples=50)
def test_rule_instantiation(instance):
    assert isinstance(instance, Rule)

@given(instance=atlstatic_ATL_CalledRule_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_calledrule_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_CalledRule)



@given(instance=atlstatic_ATL_CalledRule_strategy)
def test_atlstatic_atl_calledrule_isEndpoint_setter(instance):
    original = instance.isEndpoint
    instance.isEndpoint = original
    assert instance.isEndpoint == original



@given(instance=atlstatic_ATL_CalledRule_strategy)
def test_atlstatic_atl_calledrule_isEntrypoint_setter(instance):
    original = instance.isEntrypoint
    instance.isEntrypoint = original
    assert instance.isEntrypoint == original

@given(instance=atlstatic_ATL_MatchedRule_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_matchedrule_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_MatchedRule)



@given(instance=atlstatic_ATL_MatchedRule_strategy)
def test_atlstatic_atl_matchedrule_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original



@given(instance=atlstatic_ATL_MatchedRule_strategy)
def test_atlstatic_atl_matchedrule_isNoDefault_setter(instance):
    original = instance.isNoDefault
    instance.isNoDefault = original
    assert instance.isNoDefault == original



@given(instance=atlstatic_ATL_MatchedRule_strategy)
def test_atlstatic_atl_matchedrule_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, RuleVariableDeclaration)

@given(instance=ActionBlock_strategy)
@settings(max_examples=50)
def test_actionblock_instantiation(instance):
    assert isinstance(instance, ActionBlock)

@given(instance=OutPattern_strategy)
@settings(max_examples=50)
def test_outpattern_instantiation(instance):
    assert isinstance(instance, OutPattern)

@given(instance=atlstatic_ATL_InPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_inpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_InPatternElement)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=atlstatic_OCL_Iterator_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_iterator_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_Iterator)

@given(instance=atlstatic_ATL_RuleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_rulevariabledeclaration_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_RuleVariableDeclaration)

@given(instance=atlstatic_OCL_TuplePart_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_tuplepart_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_TuplePart)

@given(instance=atlstatic_OCL_Parameter_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_parameter_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_Parameter)

@given(instance=atlstatic_ATL_PatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_patternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_PatternElement)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=atlstatic_ATL_ForEachOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_foreachoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_ForEachOutPatternElement)

@given(instance=atlstatic_ATL_SimpleOutPatternElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_simpleoutpatternelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_SimpleOutPatternElement)

@given(instance=DropPattern_strategy)
@settings(max_examples=50)
def test_droppattern_instantiation(instance):
    assert isinstance(instance, DropPattern)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atlstatic_OCL_LetExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_letexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_LetExp)

@given(instance=atlstatic_OCL_OclType_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_ocltype_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclType)



@given(instance=atlstatic_OCL_OclType_strategy)
def test_atlstatic_ocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_VariableExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_variableexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_VariableExp)

@given(instance=atlstatic_OCL_MapExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_mapexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_MapExp)

@given(instance=atlstatic_OCL_IfExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_ifexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_IfExp)

@given(instance=Helper_strategy)
@settings(max_examples=50)
def test_helper_instantiation(instance):
    assert isinstance(instance, Helper)

@given(instance=Unit_strategy)
@settings(max_examples=50)
def test_unit_instantiation(instance):
    assert isinstance(instance, Unit)

@given(instance=atlstatic_ATL_Module_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_module_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Module)



@given(instance=atlstatic_ATL_Module_strategy)
def test_atlstatic_atl_module_isRefining_setter(instance):
    original = instance.isRefining
    instance.isRefining = original
    assert instance.isRefining == original

@given(instance=atlstatic_ATL_Query_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_query_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Query)

@given(instance=atlstatic_ATL_Library_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_library_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Library)

@given(instance=LibraryRef_strategy)
@settings(max_examples=50)
def test_libraryref_instantiation(instance):
    assert isinstance(instance, LibraryRef)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=atlstatic_ATL_ActionBlock_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_actionblock_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_ActionBlock)

@given(instance=atlstatic_ATL_Statement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_statement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Statement)

@given(instance=atlstatic_ATL_Binding_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_binding_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Binding)



@given(instance=atlstatic_ATL_Binding_strategy)
def test_atlstatic_atl_binding_isAssignment_setter(instance):
    original = instance.isAssignment
    instance.isAssignment = original
    assert instance.isAssignment == original



@given(instance=atlstatic_ATL_Binding_strategy)
def test_atlstatic_atl_binding_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original

@given(instance=atlstatic_ATL_InPattern_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_inpattern_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_InPattern)

@given(instance=atlstatic_OCL_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_TupleTypeAttribute)



@given(instance=atlstatic_OCL_TupleTypeAttribute_strategy)
def test_atlstatic_ocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_OclModel_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclmodel_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclModel)



@given(instance=atlstatic_OCL_OclModel_strategy)
def test_atlstatic_ocl_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_OclExpression_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclExpression)

@given(instance=atlstatic_ATL_OutPattern_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_outpattern_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_OutPattern)

@given(instance=atlstatic_ATL_LibraryRef_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_libraryref_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_LibraryRef)



@given(instance=atlstatic_ATL_LibraryRef_strategy)
def test_atlstatic_atl_libraryref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_ATL_DropPattern_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_droppattern_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_DropPattern)

@given(instance=atlstatic_OCL_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclContextDefinition)

@given(instance=atlstatic_OCL_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclFeatureDefinition)

@given(instance=atlstatic_OCL_OclFeature_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclfeature_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclFeature)

@given(instance=atlstatic_OCL_MapElement_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_mapelement_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_MapElement)

@given(instance=atlstatic_ATL_Unit_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_unit_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Unit)



@given(instance=atlstatic_ATL_Unit_strategy)
def test_atlstatic_atl_unit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_ATL_LocatedElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_locatedelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_LocatedElement)



@given(instance=atlstatic_ATL_LocatedElement_strategy)
def test_atlstatic_atl_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=atlstatic_ATL_LocatedElement_strategy)
def test_atlstatic_atl_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=atlstatic_ATL_LocatedElement_strategy)
def test_atlstatic_atl_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)

@given(instance=Query_strategy)
@settings(max_examples=50)
def test_query_instantiation(instance):
    assert isinstance(instance, Query)

@given(instance=atlstatic_ATL_ModuleElement_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_moduleelement_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_ModuleElement)

@given(instance=ModuleElement_strategy)
@settings(max_examples=50)
def test_moduleelement_instantiation(instance):
    assert isinstance(instance, ModuleElement)

@given(instance=atlstatic_ATL_Rule_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_rule_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Rule)



@given(instance=atlstatic_ATL_Rule_strategy)
def test_atlstatic_atl_rule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_ATL_Helper_strategy)
@settings(max_examples=50)
def test_atlstatic_atl_helper_instantiation(instance):
    assert isinstance(instance, atlstatic_ATL_Helper)

@given(instance=atlstatic_OCL_IterateExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_iterateexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_IterateExp)

@given(instance=atlstatic_OCL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_VariableDeclaration)



@given(instance=atlstatic_OCL_VariableDeclaration_strategy)
def test_atlstatic_ocl_variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=atlstatic_OCL_VariableDeclaration_strategy)
def test_atlstatic_ocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=atlstatic_OCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_PropertyCallExp)

@given(instance=atlstatic_OCL_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OclUndefinedExp)

@given(instance=atlstatic_OCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_EnumLiteralExp)



@given(instance=atlstatic_OCL_EnumLiteralExp_strategy)
def test_atlstatic_ocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_LoopExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_loopexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_LoopExp)

@given(instance=atlstatic_OCL_CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_CollectionOperationCallExp)

@given(instance=atlstatic_OCL_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OperatorCallExp)

@given(instance=atlstatic_OCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OperationCallExp)



@given(instance=atlstatic_OCL_OperationCallExp_strategy)
def test_atlstatic_ocl_operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=atlstatic_OCL_NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_NavigationOrAttributeCallExp)



@given(instance=atlstatic_OCL_NavigationOrAttributeCallExp_strategy)
def test_atlstatic_ocl_navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=atlstatic_OCL_TupleExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_tupleexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_TupleExp)

@given(instance=atlstatic_OCL_SetExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_setexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_SetExp)

@given(instance=atlstatic_OCL_SequenceExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_SequenceExp)

@given(instance=atlstatic_OCL_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_OrderedSetExp)

@given(instance=atlstatic_OCL_BagExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_bagexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_BagExp)

@given(instance=atlstatic_OCL_CollectionExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_collectionexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_CollectionExp)

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=atlstatic_OCL_IntegerExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_integerexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_IntegerExp)



@given(instance=atlstatic_OCL_IntegerExp_strategy)
def test_atlstatic_ocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=atlstatic_OCL_RealExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_realexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_RealExp)



@given(instance=atlstatic_OCL_RealExp_strategy)
def test_atlstatic_ocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=atlstatic_OCL_BooleanExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_booleanexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_BooleanExp)



@given(instance=atlstatic_OCL_BooleanExp_strategy)
def test_atlstatic_ocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=atlstatic_OCL_NumericExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_numericexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_NumericExp)

@given(instance=atlstatic_OCL_StringExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_stringexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_StringExp)



@given(instance=atlstatic_OCL_StringExp_strategy)
def test_atlstatic_ocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=atlstatic_OCL_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_PrimitiveExp)

@given(instance=atlstatic_OCL_SuperExp_strategy)
@settings(max_examples=50)
def test_atlstatic_ocl_superexp_instantiation(instance):
    assert isinstance(instance, atlstatic_OCL_SuperExp)
