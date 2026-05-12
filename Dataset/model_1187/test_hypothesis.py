import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Iterator,
    NumericLiteralExp,
    OCL_IntegerLiteralExp,
    OperationCallExp,
    OCL_OperatorCallExp,
    OCL_CollectionOperationCallExp,
    FeaturePropertyCall,
    OCL_PropertyCallExp,
    OCL_OperationCallExp,
    LoopExp,
    OCL_IteratorExp,
    OCL_IterateExp,
    PrimitiveLiteralExp,
    OCL_StringLiteralExp,
    OCL_NumericLiteralExp,
    CollectionLiteralPart,
    OCL_CollectionItem,
    OCL_CollectionRange,
    TupleLiteralPart,
    CallExp,
    OCL_LoopExp,
    OCL_FeaturePropertyCall,
    LiteralExp,
    OCL_TupleLiteralExp,
    OCL_NullLiteralExp,
    OCL_PrimitiveLiteralExp,
    OCL_CollectionLiteralExp,
    OCL_InvalidLiteralExp,
    OCL_EnumLiteralExp,
    CollectionType,
    OCL_SequenceType,
    OCL_OrderedSetType,
    OCL_BagType,
    OCL_SetType,
    Type,
    OCL_Class,
    OCL_VoidType,
    OCL_InvalidType,
    PrimitiveType,
    OCL_StringType,
    OCL_RealType,
    OCL_BooleanType,
    OCL_IntegerType,
    DataType,
    OCL_CollectionType,
    OCL_TupleType,
    OCL_PrimitiveType,
    Extent,
    OCL_URIExtent,
    NamedElement,
    OCL_EnumerationLiteral,
    OCL_TypedElement,
    EnumerationLiteral,
    OCL_Enumeration,
    Object,
    OCL_Element,
    OCL_Extent,
    OCL_Object,
    OCL_MultiplicityElement,
    OCL_Package,
    OCL_Type,
    OCL_DataType,
    MultiplicityElement,
    TypedElement,
    OCL_CollectionLiteralPart,
    OCL_Variable,
    OCL_Operation,
    OCL_Parameter,
    OCL_Property,
    OCL_TupleLiteralPart,
    OCL_OclModuleElement,
    OCL_OclFeature,
    Property,
    OclExpression,
    OCL_VariableExp,
    OCL_LetExp,
    OCL_LiteralExp,
    Variable,
    OCL_Iterator,
    OclFeature,
    OCL_OclProperty,
    Operation,
    OCL_OclOperation,
    Package,
    OCL_OclModule,
    Class,
    OCL_AnyType,
    Element,
    OCL_Comment,
    OCL_NamedElement,
    OCL_Tag,
    OCL_OclContextDefinition,
    Parameter,
    OclModuleElement,
    OCL_DeriveOclModuleElement,
    OCL_Invariant,
    OCL_DefOclModuleElement,
    OclContextDefinition,
    OCL_RealLiteralExp,
    OCL_BooleanLiteralExp,
    OCL_CallExp,
    OCL_OclExpression,
    OCL_IfExp,
    CollectionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(NumericLiteralExp)


def test_numericliteralexp_constructor_exists():
    assert callable(NumericLiteralExp.__init__)


def test_numericliteralexp_constructor_args():
    sig = inspect.signature(NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerLiteralExp)


def test_ocl_integerliteralexp_constructor_exists():
    assert callable(OCL_IntegerLiteralExp.__init__)


def test_ocl_integerliteralexp_constructor_args():
    sig = inspect.signature(OCL_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl_integerliteralexp_has_integerSymbol():
    assert hasattr(OCL_IntegerLiteralExp, "integerSymbol")
    descriptor = None
    for klass in OCL_IntegerLiteralExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OperationCallExp)


def test_operationcallexp_constructor_exists():
    assert callable(OperationCallExp.__init__)


def test_operationcallexp_constructor_args():
    sig = inspect.signature(OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperatorCallExp)


def test_ocl_operatorcallexp_constructor_exists():
    assert callable(OCL_OperatorCallExp.__init__)


def test_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(OCL_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionOperationCallExp)


def test_ocl_collectionoperationcallexp_constructor_exists():
    assert callable(OCL_CollectionOperationCallExp.__init__)


def test_ocl_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCL_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(FeaturePropertyCall)


def test_featurepropertycall_constructor_exists():
    assert callable(FeaturePropertyCall.__init__)


def test_featurepropertycall_constructor_args():
    sig = inspect.signature(FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PropertyCallExp)


def test_ocl_propertycallexp_constructor_exists():
    assert callable(OCL_PropertyCallExp.__init__)


def test_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperationCallExp)


def test_ocl_operationcallexp_constructor_exists():
    assert callable(OCL_OperationCallExp.__init__)


def test_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(OCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IteratorExp)


def test_ocl_iteratorexp_constructor_exists():
    assert callable(OCL_IteratorExp.__init__)


def test_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(OCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IterateExp)


def test_ocl_iterateexp_constructor_exists():
    assert callable(OCL_IterateExp.__init__)


def test_ocl_iterateexp_constructor_args():
    sig = inspect.signature(OCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(PrimitiveLiteralExp)


def test_primitiveliteralexp_constructor_exists():
    assert callable(PrimitiveLiteralExp.__init__)


def test_primitiveliteralexp_constructor_args():
    sig = inspect.signature(PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_StringLiteralExp)


def test_ocl_stringliteralexp_constructor_exists():
    assert callable(OCL_StringLiteralExp.__init__)


def test_ocl_stringliteralexp_constructor_args():
    sig = inspect.signature(OCL_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl_stringliteralexp_has_stringSymbol():
    assert hasattr(OCL_StringLiteralExp, "stringSymbol")
    descriptor = None
    for klass in OCL_StringLiteralExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_numericliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NumericLiteralExp)


def test_ocl_numericliteralexp_constructor_exists():
    assert callable(OCL_NumericLiteralExp.__init__)


def test_ocl_numericliteralexp_constructor_args():
    sig = inspect.signature(OCL_NumericLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralPart)


def test_collectionliteralpart_constructor_exists():
    assert callable(CollectionLiteralPart.__init__)


def test_collectionliteralpart_constructor_args():
    sig = inspect.signature(CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionitem_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionItem)


def test_ocl_collectionitem_constructor_exists():
    assert callable(OCL_CollectionItem.__init__)


def test_ocl_collectionitem_constructor_args():
    sig = inspect.signature(OCL_CollectionItem.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionrange_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionRange)


def test_ocl_collectionrange_constructor_exists():
    assert callable(OCL_CollectionRange.__init__)


def test_ocl_collectionrange_constructor_args():
    sig = inspect.signature(OCL_CollectionRange.__init__)
    params = list(sig.parameters.keys())



def test_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(TupleLiteralPart)


def test_tupleliteralpart_constructor_exists():
    assert callable(TupleLiteralPart.__init__)


def test_tupleliteralpart_constructor_args():
    sig = inspect.signature(TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LoopExp)


def test_ocl_loopexp_constructor_exists():
    assert callable(OCL_LoopExp.__init__)


def test_ocl_loopexp_constructor_args():
    sig = inspect.signature(OCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_featurepropertycall_is_not_abstract():
    assert not inspect.isabstract(OCL_FeaturePropertyCall)


def test_ocl_featurepropertycall_constructor_exists():
    assert callable(OCL_FeaturePropertyCall.__init__)


def test_ocl_featurepropertycall_constructor_args():
    sig = inspect.signature(OCL_FeaturePropertyCall.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleLiteralExp)


def test_ocl_tupleliteralexp_constructor_exists():
    assert callable(OCL_TupleLiteralExp.__init__)


def test_ocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(OCL_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_nullliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NullLiteralExp)


def test_ocl_nullliteralexp_constructor_exists():
    assert callable(OCL_NullLiteralExp.__init__)


def test_ocl_nullliteralexp_constructor_args():
    sig = inspect.signature(OCL_NullLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_primitiveliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PrimitiveLiteralExp)


def test_ocl_primitiveliteralexp_constructor_exists():
    assert callable(OCL_PrimitiveLiteralExp.__init__)


def test_ocl_primitiveliteralexp_constructor_args():
    sig = inspect.signature(OCL_PrimitiveLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionLiteralExp)


def test_ocl_collectionliteralexp_constructor_exists():
    assert callable(OCL_CollectionLiteralExp.__init__)


def test_ocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(OCL_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_ocl_collectionliteralexp_has_kind():
    assert hasattr(OCL_CollectionLiteralExp, "kind")
    descriptor = None
    for klass in OCL_CollectionLiteralExp.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_ocl_invalidliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_InvalidLiteralExp)


def test_ocl_invalidliteralexp_constructor_exists():
    assert callable(OCL_InvalidLiteralExp.__init__)


def test_ocl_invalidliteralexp_constructor_args():
    sig = inspect.signature(OCL_InvalidLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_EnumLiteralExp)


def test_ocl_enumliteralexp_constructor_exists():
    assert callable(OCL_EnumLiteralExp.__init__)


def test_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(OCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_sequencetype_is_not_abstract():
    assert not inspect.isabstract(OCL_SequenceType)


def test_ocl_sequencetype_constructor_exists():
    assert callable(OCL_SequenceType.__init__)


def test_ocl_sequencetype_constructor_args():
    sig = inspect.signature(OCL_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(OCL_OrderedSetType)


def test_ocl_orderedsettype_constructor_exists():
    assert callable(OCL_OrderedSetType.__init__)


def test_ocl_orderedsettype_constructor_args():
    sig = inspect.signature(OCL_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(OCL_BagType)


def test_ocl_bagtype_constructor_exists():
    assert callable(OCL_BagType.__init__)


def test_ocl_bagtype_constructor_args():
    sig = inspect.signature(OCL_BagType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_settype_is_not_abstract():
    assert not inspect.isabstract(OCL_SetType)


def test_ocl_settype_constructor_exists():
    assert callable(OCL_SetType.__init__)


def test_ocl_settype_constructor_args():
    sig = inspect.signature(OCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_ocl_class_is_not_abstract():
    assert not inspect.isabstract(OCL_Class)


def test_ocl_class_constructor_exists():
    assert callable(OCL_Class.__init__)


def test_ocl_class_constructor_args():
    sig = inspect.signature(OCL_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_ocl_class_has_isAbstract():
    assert hasattr(OCL_Class, "isAbstract")
    descriptor = None
    for klass in OCL_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_ocl_voidtype_is_not_abstract():
    assert not inspect.isabstract(OCL_VoidType)


def test_ocl_voidtype_constructor_exists():
    assert callable(OCL_VoidType.__init__)


def test_ocl_voidtype_constructor_args():
    sig = inspect.signature(OCL_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_invalidtype_is_not_abstract():
    assert not inspect.isabstract(OCL_InvalidType)


def test_ocl_invalidtype_constructor_exists():
    assert callable(OCL_InvalidType.__init__)


def test_ocl_invalidtype_constructor_args():
    sig = inspect.signature(OCL_InvalidType.__init__)
    params = list(sig.parameters.keys())



def test_primitivetype_is_not_abstract():
    assert not inspect.isabstract(PrimitiveType)


def test_primitivetype_constructor_exists():
    assert callable(PrimitiveType.__init__)


def test_primitivetype_constructor_args():
    sig = inspect.signature(PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(OCL_StringType)


def test_ocl_stringtype_constructor_exists():
    assert callable(OCL_StringType.__init__)


def test_ocl_stringtype_constructor_args():
    sig = inspect.signature(OCL_StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_realtype_is_not_abstract():
    assert not inspect.isabstract(OCL_RealType)


def test_ocl_realtype_constructor_exists():
    assert callable(OCL_RealType.__init__)


def test_ocl_realtype_constructor_args():
    sig = inspect.signature(OCL_RealType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanType)


def test_ocl_booleantype_constructor_exists():
    assert callable(OCL_BooleanType.__init__)


def test_ocl_booleantype_constructor_args():
    sig = inspect.signature(OCL_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_integertype_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerType)


def test_ocl_integertype_constructor_exists():
    assert callable(OCL_IntegerType.__init__)


def test_ocl_integertype_constructor_args():
    sig = inspect.signature(OCL_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionType)


def test_ocl_collectiontype_constructor_exists():
    assert callable(OCL_CollectionType.__init__)


def test_ocl_collectiontype_constructor_args():
    sig = inspect.signature(OCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleType)


def test_ocl_tupletype_constructor_exists():
    assert callable(OCL_TupleType.__init__)


def test_ocl_tupletype_constructor_args():
    sig = inspect.signature(OCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_primitivetype_is_not_abstract():
    assert not inspect.isabstract(OCL_PrimitiveType)


def test_ocl_primitivetype_constructor_exists():
    assert callable(OCL_PrimitiveType.__init__)


def test_ocl_primitivetype_constructor_args():
    sig = inspect.signature(OCL_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_extent_is_not_abstract():
    assert not inspect.isabstract(Extent)


def test_extent_constructor_exists():
    assert callable(Extent.__init__)


def test_extent_constructor_args():
    sig = inspect.signature(Extent.__init__)
    params = list(sig.parameters.keys())



def test_ocl_uriextent_is_not_abstract():
    assert not inspect.isabstract(OCL_URIExtent)


def test_ocl_uriextent_constructor_exists():
    assert callable(OCL_URIExtent.__init__)


def test_ocl_uriextent_constructor_args():
    sig = inspect.signature(OCL_URIExtent.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(OCL_EnumerationLiteral)


def test_ocl_enumerationliteral_constructor_exists():
    assert callable(OCL_EnumerationLiteral.__init__)


def test_ocl_enumerationliteral_constructor_args():
    sig = inspect.signature(OCL_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl_typedelement_is_not_abstract():
    assert not inspect.isabstract(OCL_TypedElement)


def test_ocl_typedelement_constructor_exists():
    assert callable(OCL_TypedElement.__init__)


def test_ocl_typedelement_constructor_args():
    sig = inspect.signature(OCL_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(EnumerationLiteral)


def test_enumerationliteral_constructor_exists():
    assert callable(EnumerationLiteral.__init__)


def test_enumerationliteral_constructor_args():
    sig = inspect.signature(EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl_enumeration_is_not_abstract():
    assert not inspect.isabstract(OCL_Enumeration)


def test_ocl_enumeration_constructor_exists():
    assert callable(OCL_Enumeration.__init__)


def test_ocl_enumeration_constructor_args():
    sig = inspect.signature(OCL_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_ocl_element_is_not_abstract():
    assert not inspect.isabstract(OCL_Element)


def test_ocl_element_constructor_exists():
    assert callable(OCL_Element.__init__)


def test_ocl_element_constructor_args():
    sig = inspect.signature(OCL_Element.__init__)
    params = list(sig.parameters.keys())



def test_ocl_extent_is_not_abstract():
    assert not inspect.isabstract(OCL_Extent)


def test_ocl_extent_constructor_exists():
    assert callable(OCL_Extent.__init__)


def test_ocl_extent_constructor_args():
    sig = inspect.signature(OCL_Extent.__init__)
    params = list(sig.parameters.keys())



def test_ocl_object_is_not_abstract():
    assert not inspect.isabstract(OCL_Object)


def test_ocl_object_constructor_exists():
    assert callable(OCL_Object.__init__)


def test_ocl_object_constructor_args():
    sig = inspect.signature(OCL_Object.__init__)
    params = list(sig.parameters.keys())



def test_ocl_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(OCL_MultiplicityElement)


def test_ocl_multiplicityelement_constructor_exists():
    assert callable(OCL_MultiplicityElement.__init__)


def test_ocl_multiplicityelement_constructor_args():
    sig = inspect.signature(OCL_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_ocl_multiplicityelement_has_isOrdered():
    assert hasattr(OCL_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in OCL_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_ocl_multiplicityelement_has_lower():
    assert hasattr(OCL_MultiplicityElement, "lower")
    descriptor = None
    for klass in OCL_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_ocl_multiplicityelement_has_upper():
    assert hasattr(OCL_MultiplicityElement, "upper")
    descriptor = None
    for klass in OCL_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_ocl_multiplicityelement_has_isUnique():
    assert hasattr(OCL_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in OCL_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_ocl_package_is_not_abstract():
    assert not inspect.isabstract(OCL_Package)


def test_ocl_package_constructor_exists():
    assert callable(OCL_Package.__init__)


def test_ocl_package_constructor_args():
    sig = inspect.signature(OCL_Package.__init__)
    params = list(sig.parameters.keys())
    assert "uri" in params, "Missing parameter 'uri'"

def test_ocl_package_has_uri():
    assert hasattr(OCL_Package, "uri")
    descriptor = None
    for klass in OCL_Package.__mro__:
        if "uri" in klass.__dict__:
            descriptor = klass.__dict__["uri"]
            break
    assert isinstance(descriptor, property)



def test_ocl_type_is_not_abstract():
    assert not inspect.isabstract(OCL_Type)


def test_ocl_type_constructor_exists():
    assert callable(OCL_Type.__init__)


def test_ocl_type_constructor_args():
    sig = inspect.signature(OCL_Type.__init__)
    params = list(sig.parameters.keys())



def test_ocl_datatype_is_not_abstract():
    assert not inspect.isabstract(OCL_DataType)


def test_ocl_datatype_constructor_exists():
    assert callable(OCL_DataType.__init__)


def test_ocl_datatype_constructor_args():
    sig = inspect.signature(OCL_DataType.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionLiteralPart)


def test_ocl_collectionliteralpart_constructor_exists():
    assert callable(OCL_CollectionLiteralPart.__init__)


def test_ocl_collectionliteralpart_constructor_args():
    sig = inspect.signature(OCL_CollectionLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_variable_is_not_abstract():
    assert not inspect.isabstract(OCL_Variable)


def test_ocl_variable_constructor_exists():
    assert callable(OCL_Variable.__init__)


def test_ocl_variable_constructor_args():
    sig = inspect.signature(OCL_Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(OCL_Operation)


def test_ocl_operation_constructor_exists():
    assert callable(OCL_Operation.__init__)


def test_ocl_operation_constructor_args():
    sig = inspect.signature(OCL_Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_parameter_is_not_abstract():
    assert not inspect.isabstract(OCL_Parameter)


def test_ocl_parameter_constructor_exists():
    assert callable(OCL_Parameter.__init__)


def test_ocl_parameter_constructor_args():
    sig = inspect.signature(OCL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocl_property_is_not_abstract():
    assert not inspect.isabstract(OCL_Property)


def test_ocl_property_constructor_exists():
    assert callable(OCL_Property.__init__)


def test_ocl_property_constructor_args():
    sig = inspect.signature(OCL_Property.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isId" in params, "Missing parameter 'isId'"

def test_ocl_property_has_isReadOnly():
    assert hasattr(OCL_Property, "isReadOnly")
    descriptor = None
    for klass in OCL_Property.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_ocl_property_has_isDerived():
    assert hasattr(OCL_Property, "isDerived")
    descriptor = None
    for klass in OCL_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_ocl_property_has_default():
    assert hasattr(OCL_Property, "default")
    descriptor = None
    for klass in OCL_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_ocl_property_has_isComposite():
    assert hasattr(OCL_Property, "isComposite")
    descriptor = None
    for klass in OCL_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_ocl_property_has_isId():
    assert hasattr(OCL_Property, "isId")
    descriptor = None
    for klass in OCL_Property.__mro__:
        if "isId" in klass.__dict__:
            descriptor = klass.__dict__["isId"]
            break
    assert isinstance(descriptor, property)



def test_ocl_tupleliteralpart_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleLiteralPart)


def test_ocl_tupleliteralpart_constructor_exists():
    assert callable(OCL_TupleLiteralPart.__init__)


def test_ocl_tupleliteralpart_constructor_args():
    sig = inspect.signature(OCL_TupleLiteralPart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModuleElement)


def test_ocl_oclmoduleelement_constructor_exists():
    assert callable(OCL_OclModuleElement.__init__)


def test_ocl_oclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL_OclFeature)


def test_ocl_oclfeature_constructor_exists():
    assert callable(OCL_OclFeature.__init__)


def test_ocl_oclfeature_constructor_args():
    sig = inspect.signature(OCL_OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_variableexp_is_not_abstract():
    assert not inspect.isabstract(OCL_VariableExp)


def test_ocl_variableexp_constructor_exists():
    assert callable(OCL_VariableExp.__init__)


def test_ocl_variableexp_constructor_args():
    sig = inspect.signature(OCL_VariableExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LetExp)


def test_ocl_letexp_constructor_exists():
    assert callable(OCL_LetExp.__init__)


def test_ocl_letexp_constructor_args():
    sig = inspect.signature(OCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LiteralExp)


def test_ocl_literalexp_constructor_exists():
    assert callable(OCL_LiteralExp.__init__)


def test_ocl_literalexp_constructor_args():
    sig = inspect.signature(OCL_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(OCL_Iterator)


def test_ocl_iterator_constructor_exists():
    assert callable(OCL_Iterator.__init__)


def test_ocl_iterator_constructor_args():
    sig = inspect.signature(OCL_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclproperty_is_not_abstract():
    assert not inspect.isabstract(OCL_OclProperty)


def test_ocl_oclproperty_constructor_exists():
    assert callable(OCL_OclProperty.__init__)


def test_ocl_oclproperty_constructor_args():
    sig = inspect.signature(OCL_OclProperty.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ocloperation_is_not_abstract():
    assert not inspect.isabstract(OCL_OclOperation)


def test_ocl_ocloperation_constructor_exists():
    assert callable(OCL_OclOperation.__init__)


def test_ocl_ocloperation_constructor_args():
    sig = inspect.signature(OCL_OclOperation.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclmodule_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModule)


def test_ocl_oclmodule_constructor_exists():
    assert callable(OCL_OclModule.__init__)


def test_ocl_oclmodule_constructor_args():
    sig = inspect.signature(OCL_OclModule.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_ocl_anytype_is_not_abstract():
    assert not inspect.isabstract(OCL_AnyType)


def test_ocl_anytype_constructor_exists():
    assert callable(OCL_AnyType.__init__)


def test_ocl_anytype_constructor_args():
    sig = inspect.signature(OCL_AnyType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_ocl_comment_is_not_abstract():
    assert not inspect.isabstract(OCL_Comment)


def test_ocl_comment_constructor_exists():
    assert callable(OCL_Comment.__init__)


def test_ocl_comment_constructor_args():
    sig = inspect.signature(OCL_Comment.__init__)
    params = list(sig.parameters.keys())



def test_ocl_namedelement_is_not_abstract():
    assert not inspect.isabstract(OCL_NamedElement)


def test_ocl_namedelement_constructor_exists():
    assert callable(OCL_NamedElement.__init__)


def test_ocl_namedelement_constructor_args():
    sig = inspect.signature(OCL_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_namedelement_has_name():
    assert hasattr(OCL_NamedElement, "name")
    descriptor = None
    for klass in OCL_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_tag_is_not_abstract():
    assert not inspect.isabstract(OCL_Tag)


def test_ocl_tag_constructor_exists():
    assert callable(OCL_Tag.__init__)


def test_ocl_tag_constructor_args():
    sig = inspect.signature(OCL_Tag.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_ocl_tag_has_name():
    assert hasattr(OCL_Tag, "name")
    descriptor = None
    for klass in OCL_Tag.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocl_tag_has_value():
    assert hasattr(OCL_Tag, "value")
    descriptor = None
    for klass in OCL_Tag.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL_OclContextDefinition)


def test_ocl_oclcontextdefinition_constructor_exists():
    assert callable(OCL_OclContextDefinition.__init__)


def test_ocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_oclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OclModuleElement)


def test_oclmoduleelement_constructor_exists():
    assert callable(OclModuleElement.__init__)


def test_oclmoduleelement_constructor_args():
    sig = inspect.signature(OclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_deriveoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_DeriveOclModuleElement)


def test_ocl_deriveoclmoduleelement_constructor_exists():
    assert callable(OCL_DeriveOclModuleElement.__init__)


def test_ocl_deriveoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_DeriveOclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_invariant_is_not_abstract():
    assert not inspect.isabstract(OCL_Invariant)


def test_ocl_invariant_constructor_exists():
    assert callable(OCL_Invariant.__init__)


def test_ocl_invariant_constructor_args():
    sig = inspect.signature(OCL_Invariant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_invariant_has_name():
    assert hasattr(OCL_Invariant, "name")
    descriptor = None
    for klass in OCL_Invariant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_defoclmoduleelement_is_not_abstract():
    assert not inspect.isabstract(OCL_DefOclModuleElement)


def test_ocl_defoclmoduleelement_constructor_exists():
    assert callable(OCL_DefOclModuleElement.__init__)


def test_ocl_defoclmoduleelement_constructor_args():
    sig = inspect.signature(OCL_DefOclModuleElement.__init__)
    params = list(sig.parameters.keys())



def test_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OclContextDefinition)


def test_oclcontextdefinition_constructor_exists():
    assert callable(OclContextDefinition.__init__)


def test_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_RealLiteralExp)


def test_ocl_realliteralexp_constructor_exists():
    assert callable(OCL_RealLiteralExp.__init__)


def test_ocl_realliteralexp_constructor_args():
    sig = inspect.signature(OCL_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl_realliteralexp_has_realSymbol():
    assert hasattr(OCL_RealLiteralExp, "realSymbol")
    descriptor = None
    for klass in OCL_RealLiteralExp.__mro__:
        if "realSymbol" in klass.__dict__:
            descriptor = klass.__dict__["realSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanLiteralExp)


def test_ocl_booleanliteralexp_constructor_exists():
    assert callable(OCL_BooleanLiteralExp.__init__)


def test_ocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(OCL_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl_booleanliteralexp_has_booleanSymbol():
    assert hasattr(OCL_BooleanLiteralExp, "booleanSymbol")
    descriptor = None
    for klass in OCL_BooleanLiteralExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_callexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CallExp)


def test_ocl_callexp_constructor_exists():
    assert callable(OCL_CallExp.__init__)


def test_ocl_callexp_constructor_args():
    sig = inspect.signature(OCL_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL_OclExpression)


def test_ocl_oclexpression_constructor_exists():
    assert callable(OCL_OclExpression.__init__)


def test_ocl_oclexpression_constructor_args():
    sig = inspect.signature(OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IfExp)


def test_ocl_ifexp_constructor_exists():
    assert callable(OCL_IfExp.__init__)


def test_ocl_ifexp_constructor_args():
    sig = inspect.signature(OCL_IfExp.__init__)
    params = list(sig.parameters.keys())

def test_collectionkind_exists():
    # Check that the Enumeration exists
    assert CollectionKind is not None

def test_collectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionKind]
    expected_literals = [
        "Bag",
        "OrderedSet",
        "Sequence",
        "Set",
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
Iterator_strategy = st.builds(
    Iterator,
)
NumericLiteralExp_strategy = st.builds(
    NumericLiteralExp,
)
OCL_IntegerLiteralExp_strategy = st.builds(
    OCL_IntegerLiteralExp,
    integerSymbol=
        safe_text
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
OCL_OperatorCallExp_strategy = st.builds(
    OCL_OperatorCallExp,
)
OCL_CollectionOperationCallExp_strategy = st.builds(
    OCL_CollectionOperationCallExp,
)
FeaturePropertyCall_strategy = st.builds(
    FeaturePropertyCall,
)
OCL_PropertyCallExp_strategy = st.builds(
    OCL_PropertyCallExp,
)
OCL_OperationCallExp_strategy = st.builds(
    OCL_OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
OCL_IteratorExp_strategy = st.builds(
    OCL_IteratorExp,
)
OCL_IterateExp_strategy = st.builds(
    OCL_IterateExp,
)
PrimitiveLiteralExp_strategy = st.builds(
    PrimitiveLiteralExp,
)
OCL_StringLiteralExp_strategy = st.builds(
    OCL_StringLiteralExp,
    stringSymbol=
        safe_text
)
OCL_NumericLiteralExp_strategy = st.builds(
    OCL_NumericLiteralExp,
)
CollectionLiteralPart_strategy = st.builds(
    CollectionLiteralPart,
)
OCL_CollectionItem_strategy = st.builds(
    OCL_CollectionItem,
)
OCL_CollectionRange_strategy = st.builds(
    OCL_CollectionRange,
)
TupleLiteralPart_strategy = st.builds(
    TupleLiteralPart,
)
CallExp_strategy = st.builds(
    CallExp,
)
OCL_LoopExp_strategy = st.builds(
    OCL_LoopExp,
)
OCL_FeaturePropertyCall_strategy = st.builds(
    OCL_FeaturePropertyCall,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
OCL_TupleLiteralExp_strategy = st.builds(
    OCL_TupleLiteralExp,
)
OCL_NullLiteralExp_strategy = st.builds(
    OCL_NullLiteralExp,
)
OCL_PrimitiveLiteralExp_strategy = st.builds(
    OCL_PrimitiveLiteralExp,
)
OCL_CollectionLiteralExp_strategy = st.builds(
    OCL_CollectionLiteralExp,
    kind=
        safe_text
)
OCL_InvalidLiteralExp_strategy = st.builds(
    OCL_InvalidLiteralExp,
)
OCL_EnumLiteralExp_strategy = st.builds(
    OCL_EnumLiteralExp,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCL_SequenceType_strategy = st.builds(
    OCL_SequenceType,
)
OCL_OrderedSetType_strategy = st.builds(
    OCL_OrderedSetType,
)
OCL_BagType_strategy = st.builds(
    OCL_BagType,
)
OCL_SetType_strategy = st.builds(
    OCL_SetType,
)
Type_strategy = st.builds(
    Type,
)
OCL_Class_strategy = st.builds(
    OCL_Class,
    isAbstract=
        safe_text
)
OCL_VoidType_strategy = st.builds(
    OCL_VoidType,
)
OCL_InvalidType_strategy = st.builds(
    OCL_InvalidType,
)
PrimitiveType_strategy = st.builds(
    PrimitiveType,
)
OCL_StringType_strategy = st.builds(
    OCL_StringType,
)
OCL_RealType_strategy = st.builds(
    OCL_RealType,
)
OCL_BooleanType_strategy = st.builds(
    OCL_BooleanType,
)
OCL_IntegerType_strategy = st.builds(
    OCL_IntegerType,
)
DataType_strategy = st.builds(
    DataType,
)
OCL_CollectionType_strategy = st.builds(
    OCL_CollectionType,
)
OCL_TupleType_strategy = st.builds(
    OCL_TupleType,
)
OCL_PrimitiveType_strategy = st.builds(
    OCL_PrimitiveType,
)
Extent_strategy = st.builds(
    Extent,
)
OCL_URIExtent_strategy = st.builds(
    OCL_URIExtent,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
OCL_EnumerationLiteral_strategy = st.builds(
    OCL_EnumerationLiteral,
)
OCL_TypedElement_strategy = st.builds(
    OCL_TypedElement,
)
EnumerationLiteral_strategy = st.builds(
    EnumerationLiteral,
)
OCL_Enumeration_strategy = st.builds(
    OCL_Enumeration,
)
Object_strategy = st.builds(
    Object,
)
OCL_Element_strategy = st.builds(
    OCL_Element,
)
OCL_Extent_strategy = st.builds(
    OCL_Extent,
)
OCL_Object_strategy = st.builds(
    OCL_Object,
)
OCL_MultiplicityElement_strategy = st.builds(
    OCL_MultiplicityElement,
    isOrdered=
        safe_text,
    lower=
        safe_text,
    upper=
        safe_text,
    isUnique=
        safe_text
)
OCL_Package_strategy = st.builds(
    OCL_Package,
    uri=
        safe_text
)
OCL_Type_strategy = st.builds(
    OCL_Type,
)
OCL_DataType_strategy = st.builds(
    OCL_DataType,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
OCL_CollectionLiteralPart_strategy = st.builds(
    OCL_CollectionLiteralPart,
)
OCL_Variable_strategy = st.builds(
    OCL_Variable,
)
OCL_Operation_strategy = st.builds(
    OCL_Operation,
)
OCL_Parameter_strategy = st.builds(
    OCL_Parameter,
)
OCL_Property_strategy = st.builds(
    OCL_Property,
    isReadOnly=
        safe_text,
    isDerived=
        safe_text,
    default=
        safe_text,
    isComposite=
        safe_text,
    isId=
        safe_text
)
OCL_TupleLiteralPart_strategy = st.builds(
    OCL_TupleLiteralPart,
)
OCL_OclModuleElement_strategy = st.builds(
    OCL_OclModuleElement,
)
OCL_OclFeature_strategy = st.builds(
    OCL_OclFeature,
)
Property_strategy = st.builds(
    Property,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL_VariableExp_strategy = st.builds(
    OCL_VariableExp,
)
OCL_LetExp_strategy = st.builds(
    OCL_LetExp,
)
OCL_LiteralExp_strategy = st.builds(
    OCL_LiteralExp,
)
Variable_strategy = st.builds(
    Variable,
)
OCL_Iterator_strategy = st.builds(
    OCL_Iterator,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL_OclProperty_strategy = st.builds(
    OCL_OclProperty,
)
Operation_strategy = st.builds(
    Operation,
)
OCL_OclOperation_strategy = st.builds(
    OCL_OclOperation,
)
Package_strategy = st.builds(
    Package,
)
OCL_OclModule_strategy = st.builds(
    OCL_OclModule,
)
Class_strategy = st.builds(
    Class,
)
OCL_AnyType_strategy = st.builds(
    OCL_AnyType,
)
Element_strategy = st.builds(
    Element,
)
OCL_Comment_strategy = st.builds(
    OCL_Comment,
)
OCL_NamedElement_strategy = st.builds(
    OCL_NamedElement,
    name=
        safe_text
)
OCL_Tag_strategy = st.builds(
    OCL_Tag,
    name=
        safe_text,
    value=
        safe_text
)
OCL_OclContextDefinition_strategy = st.builds(
    OCL_OclContextDefinition,
)
Parameter_strategy = st.builds(
    Parameter,
)
OclModuleElement_strategy = st.builds(
    OclModuleElement,
)
OCL_DeriveOclModuleElement_strategy = st.builds(
    OCL_DeriveOclModuleElement,
)
OCL_Invariant_strategy = st.builds(
    OCL_Invariant,
    name=
        safe_text
)
OCL_DefOclModuleElement_strategy = st.builds(
    OCL_DefOclModuleElement,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
OCL_RealLiteralExp_strategy = st.builds(
    OCL_RealLiteralExp,
    realSymbol=
        safe_text
)
OCL_BooleanLiteralExp_strategy = st.builds(
    OCL_BooleanLiteralExp,
    booleanSymbol=
        safe_text
)
OCL_CallExp_strategy = st.builds(
    OCL_CallExp,
)
OCL_OclExpression_strategy = st.builds(
    OCL_OclExpression,
)
OCL_IfExp_strategy = st.builds(
    OCL_IfExp,
)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_numericliteralexp_instantiation(instance):
    assert isinstance(instance, NumericLiteralExp)

@given(instance=OCL_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_IntegerLiteralExp)



@given(instance=OCL_IntegerLiteralExp_strategy)
def test_ocl_integerliteralexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=OCL_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCL_OperatorCallExp)

@given(instance=OCL_CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionOperationCallExp)

@given(instance=FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_featurepropertycall_instantiation(instance):
    assert isinstance(instance, FeaturePropertyCall)

@given(instance=OCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, OCL_PropertyCallExp)

@given(instance=OCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, OCL_OperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=OCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, OCL_IteratorExp)

@given(instance=OCL_IterateExp_strategy)
@settings(max_examples=50)
def test_ocl_iterateexp_instantiation(instance):
    assert isinstance(instance, OCL_IterateExp)

@given(instance=PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, PrimitiveLiteralExp)

@given(instance=OCL_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_StringLiteralExp)



@given(instance=OCL_StringLiteralExp_strategy)
def test_ocl_stringliteralexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=OCL_NumericLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_numericliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_NumericLiteralExp)

@given(instance=CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, CollectionLiteralPart)

@given(instance=OCL_CollectionItem_strategy)
@settings(max_examples=50)
def test_ocl_collectionitem_instantiation(instance):
    assert isinstance(instance, OCL_CollectionItem)

@given(instance=OCL_CollectionRange_strategy)
@settings(max_examples=50)
def test_ocl_collectionrange_instantiation(instance):
    assert isinstance(instance, OCL_CollectionRange)

@given(instance=TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, TupleLiteralPart)

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=OCL_LoopExp_strategy)
@settings(max_examples=50)
def test_ocl_loopexp_instantiation(instance):
    assert isinstance(instance, OCL_LoopExp)

@given(instance=OCL_FeaturePropertyCall_strategy)
@settings(max_examples=50)
def test_ocl_featurepropertycall_instantiation(instance):
    assert isinstance(instance, OCL_FeaturePropertyCall)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=OCL_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_TupleLiteralExp)

@given(instance=OCL_NullLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_nullliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_NullLiteralExp)

@given(instance=OCL_PrimitiveLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_primitiveliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_PrimitiveLiteralExp)

@given(instance=OCL_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionLiteralExp)



@given(instance=OCL_CollectionLiteralExp_strategy)
def test_ocl_collectionliteralexp_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=OCL_InvalidLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_invalidliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_InvalidLiteralExp)

@given(instance=OCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_EnumLiteralExp)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=OCL_SequenceType_strategy)
@settings(max_examples=50)
def test_ocl_sequencetype_instantiation(instance):
    assert isinstance(instance, OCL_SequenceType)

@given(instance=OCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, OCL_OrderedSetType)

@given(instance=OCL_BagType_strategy)
@settings(max_examples=50)
def test_ocl_bagtype_instantiation(instance):
    assert isinstance(instance, OCL_BagType)

@given(instance=OCL_SetType_strategy)
@settings(max_examples=50)
def test_ocl_settype_instantiation(instance):
    assert isinstance(instance, OCL_SetType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=OCL_Class_strategy)
@settings(max_examples=50)
def test_ocl_class_instantiation(instance):
    assert isinstance(instance, OCL_Class)



@given(instance=OCL_Class_strategy)
def test_ocl_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=OCL_VoidType_strategy)
@settings(max_examples=50)
def test_ocl_voidtype_instantiation(instance):
    assert isinstance(instance, OCL_VoidType)

@given(instance=OCL_InvalidType_strategy)
@settings(max_examples=50)
def test_ocl_invalidtype_instantiation(instance):
    assert isinstance(instance, OCL_InvalidType)

@given(instance=PrimitiveType_strategy)
@settings(max_examples=50)
def test_primitivetype_instantiation(instance):
    assert isinstance(instance, PrimitiveType)

@given(instance=OCL_StringType_strategy)
@settings(max_examples=50)
def test_ocl_stringtype_instantiation(instance):
    assert isinstance(instance, OCL_StringType)

@given(instance=OCL_RealType_strategy)
@settings(max_examples=50)
def test_ocl_realtype_instantiation(instance):
    assert isinstance(instance, OCL_RealType)

@given(instance=OCL_BooleanType_strategy)
@settings(max_examples=50)
def test_ocl_booleantype_instantiation(instance):
    assert isinstance(instance, OCL_BooleanType)

@given(instance=OCL_IntegerType_strategy)
@settings(max_examples=50)
def test_ocl_integertype_instantiation(instance):
    assert isinstance(instance, OCL_IntegerType)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=OCL_CollectionType_strategy)
@settings(max_examples=50)
def test_ocl_collectiontype_instantiation(instance):
    assert isinstance(instance, OCL_CollectionType)

@given(instance=OCL_TupleType_strategy)
@settings(max_examples=50)
def test_ocl_tupletype_instantiation(instance):
    assert isinstance(instance, OCL_TupleType)

@given(instance=OCL_PrimitiveType_strategy)
@settings(max_examples=50)
def test_ocl_primitivetype_instantiation(instance):
    assert isinstance(instance, OCL_PrimitiveType)

@given(instance=Extent_strategy)
@settings(max_examples=50)
def test_extent_instantiation(instance):
    assert isinstance(instance, Extent)

@given(instance=OCL_URIExtent_strategy)
@settings(max_examples=50)
def test_ocl_uriextent_instantiation(instance):
    assert isinstance(instance, OCL_URIExtent)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=OCL_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_ocl_enumerationliteral_instantiation(instance):
    assert isinstance(instance, OCL_EnumerationLiteral)

@given(instance=OCL_TypedElement_strategy)
@settings(max_examples=50)
def test_ocl_typedelement_instantiation(instance):
    assert isinstance(instance, OCL_TypedElement)

@given(instance=EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_enumerationliteral_instantiation(instance):
    assert isinstance(instance, EnumerationLiteral)

@given(instance=OCL_Enumeration_strategy)
@settings(max_examples=50)
def test_ocl_enumeration_instantiation(instance):
    assert isinstance(instance, OCL_Enumeration)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=OCL_Element_strategy)
@settings(max_examples=50)
def test_ocl_element_instantiation(instance):
    assert isinstance(instance, OCL_Element)

@given(instance=OCL_Extent_strategy)
@settings(max_examples=50)
def test_ocl_extent_instantiation(instance):
    assert isinstance(instance, OCL_Extent)

@given(instance=OCL_Object_strategy)
@settings(max_examples=50)
def test_ocl_object_instantiation(instance):
    assert isinstance(instance, OCL_Object)

@given(instance=OCL_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_ocl_multiplicityelement_instantiation(instance):
    assert isinstance(instance, OCL_MultiplicityElement)



@given(instance=OCL_MultiplicityElement_strategy)
def test_ocl_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_ocl_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_ocl_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=OCL_MultiplicityElement_strategy)
def test_ocl_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=OCL_Package_strategy)
@settings(max_examples=50)
def test_ocl_package_instantiation(instance):
    assert isinstance(instance, OCL_Package)



@given(instance=OCL_Package_strategy)
def test_ocl_package_uri_setter(instance):
    original = instance.uri
    instance.uri = original
    assert instance.uri == original

@given(instance=OCL_Type_strategy)
@settings(max_examples=50)
def test_ocl_type_instantiation(instance):
    assert isinstance(instance, OCL_Type)

@given(instance=OCL_DataType_strategy)
@settings(max_examples=50)
def test_ocl_datatype_instantiation(instance):
    assert isinstance(instance, OCL_DataType)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=OCL_CollectionLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_collectionliteralpart_instantiation(instance):
    assert isinstance(instance, OCL_CollectionLiteralPart)

@given(instance=OCL_Variable_strategy)
@settings(max_examples=50)
def test_ocl_variable_instantiation(instance):
    assert isinstance(instance, OCL_Variable)

@given(instance=OCL_Operation_strategy)
@settings(max_examples=50)
def test_ocl_operation_instantiation(instance):
    assert isinstance(instance, OCL_Operation)

@given(instance=OCL_Parameter_strategy)
@settings(max_examples=50)
def test_ocl_parameter_instantiation(instance):
    assert isinstance(instance, OCL_Parameter)

@given(instance=OCL_Property_strategy)
@settings(max_examples=50)
def test_ocl_property_instantiation(instance):
    assert isinstance(instance, OCL_Property)



@given(instance=OCL_Property_strategy)
def test_ocl_property_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=OCL_Property_strategy)
def test_ocl_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=OCL_Property_strategy)
def test_ocl_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=OCL_Property_strategy)
def test_ocl_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=OCL_Property_strategy)
def test_ocl_property_isId_setter(instance):
    original = instance.isId
    instance.isId = original
    assert instance.isId == original

@given(instance=OCL_TupleLiteralPart_strategy)
@settings(max_examples=50)
def test_ocl_tupleliteralpart_instantiation(instance):
    assert isinstance(instance, OCL_TupleLiteralPart)

@given(instance=OCL_OclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl_oclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL_OclModuleElement)

@given(instance=OCL_OclFeature_strategy)
@settings(max_examples=50)
def test_ocl_oclfeature_instantiation(instance):
    assert isinstance(instance, OCL_OclFeature)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCL_VariableExp_strategy)
@settings(max_examples=50)
def test_ocl_variableexp_instantiation(instance):
    assert isinstance(instance, OCL_VariableExp)

@given(instance=OCL_LetExp_strategy)
@settings(max_examples=50)
def test_ocl_letexp_instantiation(instance):
    assert isinstance(instance, OCL_LetExp)

@given(instance=OCL_LiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_literalexp_instantiation(instance):
    assert isinstance(instance, OCL_LiteralExp)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=OCL_Iterator_strategy)
@settings(max_examples=50)
def test_ocl_iterator_instantiation(instance):
    assert isinstance(instance, OCL_Iterator)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OCL_OclProperty_strategy)
@settings(max_examples=50)
def test_ocl_oclproperty_instantiation(instance):
    assert isinstance(instance, OCL_OclProperty)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=OCL_OclOperation_strategy)
@settings(max_examples=50)
def test_ocl_ocloperation_instantiation(instance):
    assert isinstance(instance, OCL_OclOperation)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=OCL_OclModule_strategy)
@settings(max_examples=50)
def test_ocl_oclmodule_instantiation(instance):
    assert isinstance(instance, OCL_OclModule)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OCL_AnyType_strategy)
@settings(max_examples=50)
def test_ocl_anytype_instantiation(instance):
    assert isinstance(instance, OCL_AnyType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=OCL_Comment_strategy)
@settings(max_examples=50)
def test_ocl_comment_instantiation(instance):
    assert isinstance(instance, OCL_Comment)

@given(instance=OCL_NamedElement_strategy)
@settings(max_examples=50)
def test_ocl_namedelement_instantiation(instance):
    assert isinstance(instance, OCL_NamedElement)



@given(instance=OCL_NamedElement_strategy)
def test_ocl_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_Tag_strategy)
@settings(max_examples=50)
def test_ocl_tag_instantiation(instance):
    assert isinstance(instance, OCL_Tag)



@given(instance=OCL_Tag_strategy)
def test_ocl_tag_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=OCL_Tag_strategy)
def test_ocl_tag_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=OCL_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_ocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCL_OclContextDefinition)

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=OclModuleElement_strategy)
@settings(max_examples=50)
def test_oclmoduleelement_instantiation(instance):
    assert isinstance(instance, OclModuleElement)

@given(instance=OCL_DeriveOclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl_deriveoclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL_DeriveOclModuleElement)

@given(instance=OCL_Invariant_strategy)
@settings(max_examples=50)
def test_ocl_invariant_instantiation(instance):
    assert isinstance(instance, OCL_Invariant)



@given(instance=OCL_Invariant_strategy)
def test_ocl_invariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_DefOclModuleElement_strategy)
@settings(max_examples=50)
def test_ocl_defoclmoduleelement_instantiation(instance):
    assert isinstance(instance, OCL_DefOclModuleElement)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=OCL_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_RealLiteralExp)



@given(instance=OCL_RealLiteralExp_strategy)
def test_ocl_realliteralexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=OCL_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_BooleanLiteralExp)



@given(instance=OCL_BooleanLiteralExp_strategy)
def test_ocl_booleanliteralexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OCL_CallExp_strategy)
@settings(max_examples=50)
def test_ocl_callexp_instantiation(instance):
    assert isinstance(instance, OCL_CallExp)

@given(instance=OCL_OclExpression_strategy)
@settings(max_examples=50)
def test_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, OCL_OclExpression)

@given(instance=OCL_IfExp_strategy)
@settings(max_examples=50)
def test_ocl_ifexp_instantiation(instance):
    assert isinstance(instance, OCL_IfExp)
