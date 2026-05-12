import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ir_FeatureRef,
    ir_Constraint,
    ir_EFMetamodel,
    AbstractFunction,
    ir_Specification,
    ir_EFType,
    TypedElement,
    ir_AbstractFunction,
    ir_TypeRef,
    ir_TypedElement,
    ir_Operation,
    ir_ocl_OclAnyLibElement,
    CollectionLiteralExp,
    ir_ocl_OrderedSetLiteralExp,
    ir_ocl_SequenceLiteralExp,
    ir_ocl_BagLiteralExp,
    ir_ocl_SetLiteralExp,
    ocl_ir_EFEnumLiteral,
    ocl_ir_MetaTypeRef,
    ir_ocl_TuplePart,
    TuplePart,
    ocl_ir_EFTupleType,
    LiteralExp,
    ir_ocl_EnumLiteralExp,
    ir_ocl_IntegerLiteralExp,
    ir_ocl_TupleLiteralExp,
    ir_ocl_CollectionLiteralExp,
    ir_ocl_OclUndefined,
    ir_ocl_OclInvalid,
    ir_ocl_RealLiteralExp,
    ir_ocl_StringLiteralExp,
    ir_ocl_BooleanLiteralExp,
    LoopExp,
    ir_ocl_IterateExp,
    ir_ocl_IteratorExp,
    Iterator,
    ocl_ir_PropertyFeatureRef,
    ocl_ir_OperationFeatureRef,
    AbstractOperationCallExp,
    ir_ocl_CollectionCallExp,
    ir_ocl_OperationCallExp,
    CallExp,
    ir_ocl_OperatorCallExp,
    ir_ocl_LoopExp,
    ir_ocl_PropertyCallExp,
    ir_ocl_AbstractOperationCallExp,
    ocl_ir_TypeRef,
    ir_ocl_OclExpression,
    Operation,
    DerivedProperty,
    OclExpression,
    ir_ocl_LiteralExp,
    ir_ocl_ModelElement,
    ir_ocl_CallExp,
    ir_ocl_UnsupportedExp,
    ir_ocl_VarExp,
    ir_ocl_LetExp,
    ir_ocl_IfExp,
    ocl_ir_EFClass,
    ocl_WithContextVariable,
    ir_ocl_OclOperation,
    ir_ocl_OclDerivedProperty,
    Constraint,
    ir_ocl_OclInvariant,
    ocl_ir_VariableDeclaration,
    ir_ocl_WithContextVariable,
    CollectionTypeRef,
    ir_OrderedSetTypeRef,
    ir_BagTypeRef,
    ir_SequenceTypeRef,
    ir_SetTypeRef,
    TypeRef,
    ir_CollectionTypeRef,
    ir_InvalidTypeRef,
    ir_MetaTypeRef,
    ir_TupleTypeElement,
    ir_EFEnumLiteral,
    ir_EEnum,
    ir_EClass,
    EFType,
    ir_EFTupleType,
    ir_EFPrimitiveType,
    ir_EFEnum,
    ir_EPackage,
    ir_EFPackage,
    VariableDeclaration,
    ir_ocl_Iterator,
    ir_Parameter,
    ir_VariableDeclaration,
    ir_EStructuralFeature,
    PropertyFeatureRef,
    ir_DerivedPropertyRef,
    ir_MetamodelFeatureRef,
    ir_BuiltinPropertyRef,
    ir_TupleFieldRef,
    ir_DerivedProperty,
    OperationFeatureRef,
    ir_DefinedOperationRef,
    ir_BuiltinOperationRef,
    ir_EFClass,
    FeatureRef,
    ir_PropertyFeatureRef,
    ir_OperationFeatureRef,
    OperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ir_featureref_is_not_abstract():
    assert not inspect.isabstract(ir_FeatureRef)


def test_ir_featureref_constructor_exists():
    assert callable(ir_FeatureRef.__init__)


def test_ir_featureref_constructor_args():
    sig = inspect.signature(ir_FeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_constraint_is_not_abstract():
    assert not inspect.isabstract(ir_Constraint)


def test_ir_constraint_constructor_exists():
    assert callable(ir_Constraint.__init__)


def test_ir_constraint_constructor_args():
    sig = inspect.signature(ir_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_constraint_has_name():
    assert hasattr(ir_Constraint, "name")
    descriptor = None
    for klass in ir_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_efmetamodel_is_not_abstract():
    assert not inspect.isabstract(ir_EFMetamodel)


def test_ir_efmetamodel_constructor_exists():
    assert callable(ir_EFMetamodel.__init__)


def test_ir_efmetamodel_constructor_args():
    sig = inspect.signature(ir_EFMetamodel.__init__)
    params = list(sig.parameters.keys())



def test_abstractfunction_is_not_abstract():
    assert not inspect.isabstract(AbstractFunction)


def test_abstractfunction_constructor_exists():
    assert callable(AbstractFunction.__init__)


def test_abstractfunction_constructor_args():
    sig = inspect.signature(AbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_ir_specification_is_not_abstract():
    assert not inspect.isabstract(ir_Specification)


def test_ir_specification_constructor_exists():
    assert callable(ir_Specification.__init__)


def test_ir_specification_constructor_args():
    sig = inspect.signature(ir_Specification.__init__)
    params = list(sig.parameters.keys())



def test_ir_eftype_is_not_abstract():
    assert not inspect.isabstract(ir_EFType)


def test_ir_eftype_constructor_exists():
    assert callable(ir_EFType.__init__)


def test_ir_eftype_constructor_args():
    sig = inspect.signature(ir_EFType.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ir_abstractfunction_is_not_abstract():
    assert not inspect.isabstract(ir_AbstractFunction)


def test_ir_abstractfunction_constructor_exists():
    assert callable(ir_AbstractFunction.__init__)


def test_ir_abstractfunction_constructor_args():
    sig = inspect.signature(ir_AbstractFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_abstractfunction_has_name():
    assert hasattr(ir_AbstractFunction, "name")
    descriptor = None
    for klass in ir_AbstractFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_typeref_is_not_abstract():
    assert not inspect.isabstract(ir_TypeRef)


def test_ir_typeref_constructor_exists():
    assert callable(ir_TypeRef.__init__)


def test_ir_typeref_constructor_args():
    sig = inspect.signature(ir_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_typedelement_is_not_abstract():
    assert not inspect.isabstract(ir_TypedElement)


def test_ir_typedelement_constructor_exists():
    assert callable(ir_TypedElement.__init__)


def test_ir_typedelement_constructor_args():
    sig = inspect.signature(ir_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_ir_operation_is_not_abstract():
    assert not inspect.isabstract(ir_Operation)


def test_ir_operation_constructor_exists():
    assert callable(ir_Operation.__init__)


def test_ir_operation_constructor_args():
    sig = inspect.signature(ir_Operation.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclanylibelement_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclAnyLibElement)


def test_ir_ocl_oclanylibelement_constructor_exists():
    assert callable(ir_ocl_OclAnyLibElement.__init__)


def test_ir_ocl_oclanylibelement_constructor_args():
    sig = inspect.signature(ir_ocl_OclAnyLibElement.__init__)
    params = list(sig.parameters.keys())



def test_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(CollectionLiteralExp)


def test_collectionliteralexp_constructor_exists():
    assert callable(CollectionLiteralExp.__init__)


def test_collectionliteralexp_constructor_args():
    sig = inspect.signature(CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_orderedsetliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OrderedSetLiteralExp)


def test_ir_ocl_orderedsetliteralexp_constructor_exists():
    assert callable(ir_ocl_OrderedSetLiteralExp.__init__)


def test_ir_ocl_orderedsetliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_OrderedSetLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_sequenceliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_SequenceLiteralExp)


def test_ir_ocl_sequenceliteralexp_constructor_exists():
    assert callable(ir_ocl_SequenceLiteralExp.__init__)


def test_ir_ocl_sequenceliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_SequenceLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_bagliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_BagLiteralExp)


def test_ir_ocl_bagliteralexp_constructor_exists():
    assert callable(ir_ocl_BagLiteralExp.__init__)


def test_ir_ocl_bagliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_BagLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_setliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_SetLiteralExp)


def test_ir_ocl_setliteralexp_constructor_exists():
    assert callable(ir_ocl_SetLiteralExp.__init__)


def test_ir_ocl_setliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_SetLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_efenumliteral_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_EFEnumLiteral)


def test_ocl_ir_efenumliteral_constructor_exists():
    assert callable(ocl_ir_EFEnumLiteral.__init__)


def test_ocl_ir_efenumliteral_constructor_args():
    sig = inspect.signature(ocl_ir_EFEnumLiteral.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_metatyperef_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_MetaTypeRef)


def test_ocl_ir_metatyperef_constructor_exists():
    assert callable(ocl_ir_MetaTypeRef.__init__)


def test_ocl_ir_metatyperef_constructor_args():
    sig = inspect.signature(ocl_ir_MetaTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_TuplePart)


def test_ir_ocl_tuplepart_constructor_exists():
    assert callable(ir_ocl_TuplePart.__init__)


def test_ir_ocl_tuplepart_constructor_args():
    sig = inspect.signature(ir_ocl_TuplePart.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_ocl_tuplepart_has_name():
    assert hasattr(ir_ocl_TuplePart, "name")
    descriptor = None
    for klass in ir_ocl_TuplePart.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tuplepart_is_not_abstract():
    assert not inspect.isabstract(TuplePart)


def test_tuplepart_constructor_exists():
    assert callable(TuplePart.__init__)


def test_tuplepart_constructor_args():
    sig = inspect.signature(TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_eftupletype_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_EFTupleType)


def test_ocl_ir_eftupletype_constructor_exists():
    assert callable(ocl_ir_EFTupleType.__init__)


def test_ocl_ir_eftupletype_constructor_args():
    sig = inspect.signature(ocl_ir_EFTupleType.__init__)
    params = list(sig.parameters.keys())



def test_literalexp_is_not_abstract():
    assert not inspect.isabstract(LiteralExp)


def test_literalexp_constructor_exists():
    assert callable(LiteralExp.__init__)


def test_literalexp_constructor_args():
    sig = inspect.signature(LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_EnumLiteralExp)


def test_ir_ocl_enumliteralexp_constructor_exists():
    assert callable(ir_ocl_EnumLiteralExp.__init__)


def test_ir_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_integerliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_IntegerLiteralExp)


def test_ir_ocl_integerliteralexp_constructor_exists():
    assert callable(ir_ocl_IntegerLiteralExp.__init__)


def test_ir_ocl_integerliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_IntegerLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_ocl_integerliteralexp_has_value():
    assert hasattr(ir_ocl_IntegerLiteralExp, "value")
    descriptor = None
    for klass in ir_ocl_IntegerLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_tupleliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_TupleLiteralExp)


def test_ir_ocl_tupleliteralexp_constructor_exists():
    assert callable(ir_ocl_TupleLiteralExp.__init__)


def test_ir_ocl_tupleliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_TupleLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_collectionliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_CollectionLiteralExp)


def test_ir_ocl_collectionliteralexp_constructor_exists():
    assert callable(ir_ocl_CollectionLiteralExp.__init__)


def test_ir_ocl_collectionliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_CollectionLiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclundefined_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclUndefined)


def test_ir_ocl_oclundefined_constructor_exists():
    assert callable(ir_ocl_OclUndefined.__init__)


def test_ir_ocl_oclundefined_constructor_args():
    sig = inspect.signature(ir_ocl_OclUndefined.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclinvalid_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclInvalid)


def test_ir_ocl_oclinvalid_constructor_exists():
    assert callable(ir_ocl_OclInvalid.__init__)


def test_ir_ocl_oclinvalid_constructor_args():
    sig = inspect.signature(ir_ocl_OclInvalid.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_realliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_RealLiteralExp)


def test_ir_ocl_realliteralexp_constructor_exists():
    assert callable(ir_ocl_RealLiteralExp.__init__)


def test_ir_ocl_realliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_RealLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_ocl_realliteralexp_has_value():
    assert hasattr(ir_ocl_RealLiteralExp, "value")
    descriptor = None
    for klass in ir_ocl_RealLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_stringliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_StringLiteralExp)


def test_ir_ocl_stringliteralexp_constructor_exists():
    assert callable(ir_ocl_StringLiteralExp.__init__)


def test_ir_ocl_stringliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_StringLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_ocl_stringliteralexp_has_value():
    assert hasattr(ir_ocl_StringLiteralExp, "value")
    descriptor = None
    for klass in ir_ocl_StringLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_booleanliteralexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_BooleanLiteralExp)


def test_ir_ocl_booleanliteralexp_constructor_exists():
    assert callable(ir_ocl_BooleanLiteralExp.__init__)


def test_ir_ocl_booleanliteralexp_constructor_args():
    sig = inspect.signature(ir_ocl_BooleanLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ir_ocl_booleanliteralexp_has_value():
    assert hasattr(ir_ocl_BooleanLiteralExp, "value")
    descriptor = None
    for klass in ir_ocl_BooleanLiteralExp.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_loopexp_is_not_abstract():
    assert not inspect.isabstract(LoopExp)


def test_loopexp_constructor_exists():
    assert callable(LoopExp.__init__)


def test_loopexp_constructor_args():
    sig = inspect.signature(LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_IterateExp)


def test_ir_ocl_iterateexp_constructor_exists():
    assert callable(ir_ocl_IterateExp.__init__)


def test_ir_ocl_iterateexp_constructor_args():
    sig = inspect.signature(ir_ocl_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_IteratorExp)


def test_ir_ocl_iteratorexp_constructor_exists():
    assert callable(ir_ocl_IteratorExp.__init__)


def test_ir_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(ir_ocl_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_ocl_iteratorexp_has_name():
    assert hasattr(ir_ocl_IteratorExp, "name")
    descriptor = None
    for klass in ir_ocl_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_PropertyFeatureRef)


def test_ocl_ir_propertyfeatureref_constructor_exists():
    assert callable(ocl_ir_PropertyFeatureRef.__init__)


def test_ocl_ir_propertyfeatureref_constructor_args():
    sig = inspect.signature(ocl_ir_PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_OperationFeatureRef)


def test_ocl_ir_operationfeatureref_constructor_exists():
    assert callable(ocl_ir_OperationFeatureRef.__init__)


def test_ocl_ir_operationfeatureref_constructor_args():
    sig = inspect.signature(ocl_ir_OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_abstractoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(AbstractOperationCallExp)


def test_abstractoperationcallexp_constructor_exists():
    assert callable(AbstractOperationCallExp.__init__)


def test_abstractoperationcallexp_constructor_args():
    sig = inspect.signature(AbstractOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_collectioncallexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_CollectionCallExp)


def test_ir_ocl_collectioncallexp_constructor_exists():
    assert callable(ir_ocl_CollectionCallExp.__init__)


def test_ir_ocl_collectioncallexp_constructor_args():
    sig = inspect.signature(ir_ocl_CollectionCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_ocl_collectioncallexp_has_name():
    assert hasattr(ir_ocl_CollectionCallExp, "name")
    descriptor = None
    for klass in ir_ocl_CollectionCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OperationCallExp)


def test_ir_ocl_operationcallexp_constructor_exists():
    assert callable(ir_ocl_OperationCallExp.__init__)


def test_ir_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(ir_ocl_OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_ocl_operationcallexp_has_name():
    assert hasattr(ir_ocl_OperationCallExp, "name")
    descriptor = None
    for klass in ir_ocl_OperationCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_callexp_is_not_abstract():
    assert not inspect.isabstract(CallExp)


def test_callexp_constructor_exists():
    assert callable(CallExp.__init__)


def test_callexp_constructor_args():
    sig = inspect.signature(CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OperatorCallExp)


def test_ir_ocl_operatorcallexp_constructor_exists():
    assert callable(ir_ocl_OperatorCallExp.__init__)


def test_ir_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(ir_ocl_OperatorCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_ir_ocl_operatorcallexp_has_operator():
    assert hasattr(ir_ocl_OperatorCallExp, "operator")
    descriptor = None
    for klass in ir_ocl_OperatorCallExp.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_LoopExp)


def test_ir_ocl_loopexp_constructor_exists():
    assert callable(ir_ocl_LoopExp.__init__)


def test_ir_ocl_loopexp_constructor_args():
    sig = inspect.signature(ir_ocl_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_PropertyCallExp)


def test_ir_ocl_propertycallexp_constructor_exists():
    assert callable(ir_ocl_PropertyCallExp.__init__)


def test_ir_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(ir_ocl_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_ocl_propertycallexp_has_name():
    assert hasattr(ir_ocl_PropertyCallExp, "name")
    descriptor = None
    for klass in ir_ocl_PropertyCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_abstractoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_AbstractOperationCallExp)


def test_ir_ocl_abstractoperationcallexp_constructor_exists():
    assert callable(ir_ocl_AbstractOperationCallExp.__init__)


def test_ir_ocl_abstractoperationcallexp_constructor_args():
    sig = inspect.signature(ir_ocl_AbstractOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_typeref_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_TypeRef)


def test_ocl_ir_typeref_constructor_exists():
    assert callable(ocl_ir_TypeRef.__init__)


def test_ocl_ir_typeref_constructor_args():
    sig = inspect.signature(ocl_ir_TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclExpression)


def test_ir_ocl_oclexpression_constructor_exists():
    assert callable(ir_ocl_OclExpression.__init__)


def test_ir_ocl_oclexpression_constructor_args():
    sig = inspect.signature(ir_ocl_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_derivedproperty_is_not_abstract():
    assert not inspect.isabstract(DerivedProperty)


def test_derivedproperty_constructor_exists():
    assert callable(DerivedProperty.__init__)


def test_derivedproperty_constructor_args():
    sig = inspect.signature(DerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_literalexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_LiteralExp)


def test_ir_ocl_literalexp_constructor_exists():
    assert callable(ir_ocl_LiteralExp.__init__)


def test_ir_ocl_literalexp_constructor_args():
    sig = inspect.signature(ir_ocl_LiteralExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_modelelement_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_ModelElement)


def test_ir_ocl_modelelement_constructor_exists():
    assert callable(ir_ocl_ModelElement.__init__)


def test_ir_ocl_modelelement_constructor_args():
    sig = inspect.signature(ir_ocl_ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_callexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_CallExp)


def test_ir_ocl_callexp_constructor_exists():
    assert callable(ir_ocl_CallExp.__init__)


def test_ir_ocl_callexp_constructor_args():
    sig = inspect.signature(ir_ocl_CallExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_unsupportedexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_UnsupportedExp)


def test_ir_ocl_unsupportedexp_constructor_exists():
    assert callable(ir_ocl_UnsupportedExp.__init__)


def test_ir_ocl_unsupportedexp_constructor_args():
    sig = inspect.signature(ir_ocl_UnsupportedExp.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "reason" in params, "Missing parameter 'reason'"

def test_ir_ocl_unsupportedexp_has_description():
    assert hasattr(ir_ocl_UnsupportedExp, "description")
    descriptor = None
    for klass in ir_ocl_UnsupportedExp.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ir_ocl_unsupportedexp_has_reason():
    assert hasattr(ir_ocl_UnsupportedExp, "reason")
    descriptor = None
    for klass in ir_ocl_UnsupportedExp.__mro__:
        if "reason" in klass.__dict__:
            descriptor = klass.__dict__["reason"]
            break
    assert isinstance(descriptor, property)



def test_ir_ocl_varexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_VarExp)


def test_ir_ocl_varexp_constructor_exists():
    assert callable(ir_ocl_VarExp.__init__)


def test_ir_ocl_varexp_constructor_args():
    sig = inspect.signature(ir_ocl_VarExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_LetExp)


def test_ir_ocl_letexp_constructor_exists():
    assert callable(ir_ocl_LetExp.__init__)


def test_ir_ocl_letexp_constructor_args():
    sig = inspect.signature(ir_ocl_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_IfExp)


def test_ir_ocl_ifexp_constructor_exists():
    assert callable(ir_ocl_IfExp.__init__)


def test_ir_ocl_ifexp_constructor_args():
    sig = inspect.signature(ir_ocl_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_efclass_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_EFClass)


def test_ocl_ir_efclass_constructor_exists():
    assert callable(ocl_ir_EFClass.__init__)


def test_ocl_ir_efclass_constructor_args():
    sig = inspect.signature(ocl_ir_EFClass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_withcontextvariable_is_not_abstract():
    assert not inspect.isabstract(ocl_WithContextVariable)


def test_ocl_withcontextvariable_constructor_exists():
    assert callable(ocl_WithContextVariable.__init__)


def test_ocl_withcontextvariable_constructor_args():
    sig = inspect.signature(ocl_WithContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_ocloperation_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclOperation)


def test_ir_ocl_ocloperation_constructor_exists():
    assert callable(ir_ocl_OclOperation.__init__)


def test_ir_ocl_ocloperation_constructor_args():
    sig = inspect.signature(ir_ocl_OclOperation.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclderivedproperty_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclDerivedProperty)


def test_ir_ocl_oclderivedproperty_constructor_exists():
    assert callable(ir_ocl_OclDerivedProperty.__init__)


def test_ir_ocl_oclderivedproperty_constructor_args():
    sig = inspect.signature(ir_ocl_OclDerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_oclinvariant_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_OclInvariant)


def test_ir_ocl_oclinvariant_constructor_exists():
    assert callable(ir_ocl_OclInvariant.__init__)


def test_ir_ocl_oclinvariant_constructor_args():
    sig = inspect.signature(ir_ocl_OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_ocl_ir_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ocl_ir_VariableDeclaration)


def test_ocl_ir_variabledeclaration_constructor_exists():
    assert callable(ocl_ir_VariableDeclaration.__init__)


def test_ocl_ir_variabledeclaration_constructor_args():
    sig = inspect.signature(ocl_ir_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_withcontextvariable_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_WithContextVariable)


def test_ir_ocl_withcontextvariable_constructor_exists():
    assert callable(ir_ocl_WithContextVariable.__init__)


def test_ir_ocl_withcontextvariable_constructor_args():
    sig = inspect.signature(ir_ocl_WithContextVariable.__init__)
    params = list(sig.parameters.keys())



def test_collectiontyperef_is_not_abstract():
    assert not inspect.isabstract(CollectionTypeRef)


def test_collectiontyperef_constructor_exists():
    assert callable(CollectionTypeRef.__init__)


def test_collectiontyperef_constructor_args():
    sig = inspect.signature(CollectionTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_orderedsettyperef_is_not_abstract():
    assert not inspect.isabstract(ir_OrderedSetTypeRef)


def test_ir_orderedsettyperef_constructor_exists():
    assert callable(ir_OrderedSetTypeRef.__init__)


def test_ir_orderedsettyperef_constructor_args():
    sig = inspect.signature(ir_OrderedSetTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_bagtyperef_is_not_abstract():
    assert not inspect.isabstract(ir_BagTypeRef)


def test_ir_bagtyperef_constructor_exists():
    assert callable(ir_BagTypeRef.__init__)


def test_ir_bagtyperef_constructor_args():
    sig = inspect.signature(ir_BagTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_sequencetyperef_is_not_abstract():
    assert not inspect.isabstract(ir_SequenceTypeRef)


def test_ir_sequencetyperef_constructor_exists():
    assert callable(ir_SequenceTypeRef.__init__)


def test_ir_sequencetyperef_constructor_args():
    sig = inspect.signature(ir_SequenceTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_settyperef_is_not_abstract():
    assert not inspect.isabstract(ir_SetTypeRef)


def test_ir_settyperef_constructor_exists():
    assert callable(ir_SetTypeRef.__init__)


def test_ir_settyperef_constructor_args():
    sig = inspect.signature(ir_SetTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_typeref_is_not_abstract():
    assert not inspect.isabstract(TypeRef)


def test_typeref_constructor_exists():
    assert callable(TypeRef.__init__)


def test_typeref_constructor_args():
    sig = inspect.signature(TypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_collectiontyperef_is_not_abstract():
    assert not inspect.isabstract(ir_CollectionTypeRef)


def test_ir_collectiontyperef_constructor_exists():
    assert callable(ir_CollectionTypeRef.__init__)


def test_ir_collectiontyperef_constructor_args():
    sig = inspect.signature(ir_CollectionTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_invalidtyperef_is_not_abstract():
    assert not inspect.isabstract(ir_InvalidTypeRef)


def test_ir_invalidtyperef_constructor_exists():
    assert callable(ir_InvalidTypeRef.__init__)


def test_ir_invalidtyperef_constructor_args():
    sig = inspect.signature(ir_InvalidTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_metatyperef_is_not_abstract():
    assert not inspect.isabstract(ir_MetaTypeRef)


def test_ir_metatyperef_constructor_exists():
    assert callable(ir_MetaTypeRef.__init__)


def test_ir_metatyperef_constructor_args():
    sig = inspect.signature(ir_MetaTypeRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_tupletypeelement_is_not_abstract():
    assert not inspect.isabstract(ir_TupleTypeElement)


def test_ir_tupletypeelement_constructor_exists():
    assert callable(ir_TupleTypeElement.__init__)


def test_ir_tupletypeelement_constructor_args():
    sig = inspect.signature(ir_TupleTypeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_tupletypeelement_has_name():
    assert hasattr(ir_TupleTypeElement, "name")
    descriptor = None
    for klass in ir_TupleTypeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_efenumliteral_is_not_abstract():
    assert not inspect.isabstract(ir_EFEnumLiteral)


def test_ir_efenumliteral_constructor_exists():
    assert callable(ir_EFEnumLiteral.__init__)


def test_ir_efenumliteral_constructor_args():
    sig = inspect.signature(ir_EFEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_efenumliteral_has_name():
    assert hasattr(ir_EFEnumLiteral, "name")
    descriptor = None
    for klass in ir_EFEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_eenum_is_not_abstract():
    assert not inspect.isabstract(ir_EEnum)


def test_ir_eenum_constructor_exists():
    assert callable(ir_EEnum.__init__)


def test_ir_eenum_constructor_args():
    sig = inspect.signature(ir_EEnum.__init__)
    params = list(sig.parameters.keys())



def test_ir_eclass_is_not_abstract():
    assert not inspect.isabstract(ir_EClass)


def test_ir_eclass_constructor_exists():
    assert callable(ir_EClass.__init__)


def test_ir_eclass_constructor_args():
    sig = inspect.signature(ir_EClass.__init__)
    params = list(sig.parameters.keys())



def test_eftype_is_not_abstract():
    assert not inspect.isabstract(EFType)


def test_eftype_constructor_exists():
    assert callable(EFType.__init__)


def test_eftype_constructor_args():
    sig = inspect.signature(EFType.__init__)
    params = list(sig.parameters.keys())



def test_ir_eftupletype_is_not_abstract():
    assert not inspect.isabstract(ir_EFTupleType)


def test_ir_eftupletype_constructor_exists():
    assert callable(ir_EFTupleType.__init__)


def test_ir_eftupletype_constructor_args():
    sig = inspect.signature(ir_EFTupleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_ir_eftupletype_has_id():
    assert hasattr(ir_EFTupleType, "id")
    descriptor = None
    for klass in ir_EFTupleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_ir_efprimitivetype_is_not_abstract():
    assert not inspect.isabstract(ir_EFPrimitiveType)


def test_ir_efprimitivetype_constructor_exists():
    assert callable(ir_EFPrimitiveType.__init__)


def test_ir_efprimitivetype_constructor_args():
    sig = inspect.signature(ir_EFPrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_efprimitivetype_has_name():
    assert hasattr(ir_EFPrimitiveType, "name")
    descriptor = None
    for klass in ir_EFPrimitiveType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_efenum_is_not_abstract():
    assert not inspect.isabstract(ir_EFEnum)


def test_ir_efenum_constructor_exists():
    assert callable(ir_EFEnum.__init__)


def test_ir_efenum_constructor_args():
    sig = inspect.signature(ir_EFEnum.__init__)
    params = list(sig.parameters.keys())



def test_ir_epackage_is_not_abstract():
    assert not inspect.isabstract(ir_EPackage)


def test_ir_epackage_constructor_exists():
    assert callable(ir_EPackage.__init__)


def test_ir_epackage_constructor_args():
    sig = inspect.signature(ir_EPackage.__init__)
    params = list(sig.parameters.keys())



def test_ir_efpackage_is_not_abstract():
    assert not inspect.isabstract(ir_EFPackage)


def test_ir_efpackage_constructor_exists():
    assert callable(ir_EFPackage.__init__)


def test_ir_efpackage_constructor_args():
    sig = inspect.signature(ir_EFPackage.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ir_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(ir_ocl_Iterator)


def test_ir_ocl_iterator_constructor_exists():
    assert callable(ir_ocl_Iterator.__init__)


def test_ir_ocl_iterator_constructor_args():
    sig = inspect.signature(ir_ocl_Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ir_parameter_is_not_abstract():
    assert not inspect.isabstract(ir_Parameter)


def test_ir_parameter_constructor_exists():
    assert callable(ir_Parameter.__init__)


def test_ir_parameter_constructor_args():
    sig = inspect.signature(ir_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ir_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ir_VariableDeclaration)


def test_ir_variabledeclaration_constructor_exists():
    assert callable(ir_VariableDeclaration.__init__)


def test_ir_variabledeclaration_constructor_args():
    sig = inspect.signature(ir_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_variabledeclaration_has_name():
    assert hasattr(ir_VariableDeclaration, "name")
    descriptor = None
    for klass in ir_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_estructuralfeature_is_not_abstract():
    assert not inspect.isabstract(ir_EStructuralFeature)


def test_ir_estructuralfeature_constructor_exists():
    assert callable(ir_EStructuralFeature.__init__)


def test_ir_estructuralfeature_constructor_args():
    sig = inspect.signature(ir_EStructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(PropertyFeatureRef)


def test_propertyfeatureref_constructor_exists():
    assert callable(PropertyFeatureRef.__init__)


def test_propertyfeatureref_constructor_args():
    sig = inspect.signature(PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_derivedpropertyref_is_not_abstract():
    assert not inspect.isabstract(ir_DerivedPropertyRef)


def test_ir_derivedpropertyref_constructor_exists():
    assert callable(ir_DerivedPropertyRef.__init__)


def test_ir_derivedpropertyref_constructor_args():
    sig = inspect.signature(ir_DerivedPropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_metamodelfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir_MetamodelFeatureRef)


def test_ir_metamodelfeatureref_constructor_exists():
    assert callable(ir_MetamodelFeatureRef.__init__)


def test_ir_metamodelfeatureref_constructor_args():
    sig = inspect.signature(ir_MetamodelFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_builtinpropertyref_is_not_abstract():
    assert not inspect.isabstract(ir_BuiltinPropertyRef)


def test_ir_builtinpropertyref_constructor_exists():
    assert callable(ir_BuiltinPropertyRef.__init__)


def test_ir_builtinpropertyref_constructor_args():
    sig = inspect.signature(ir_BuiltinPropertyRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_tuplefieldref_is_not_abstract():
    assert not inspect.isabstract(ir_TupleFieldRef)


def test_ir_tuplefieldref_constructor_exists():
    assert callable(ir_TupleFieldRef.__init__)


def test_ir_tuplefieldref_constructor_args():
    sig = inspect.signature(ir_TupleFieldRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ir_tuplefieldref_has_name():
    assert hasattr(ir_TupleFieldRef, "name")
    descriptor = None
    for klass in ir_TupleFieldRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ir_derivedproperty_is_not_abstract():
    assert not inspect.isabstract(ir_DerivedProperty)


def test_ir_derivedproperty_constructor_exists():
    assert callable(ir_DerivedProperty.__init__)


def test_ir_derivedproperty_constructor_args():
    sig = inspect.signature(ir_DerivedProperty.__init__)
    params = list(sig.parameters.keys())



def test_operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(OperationFeatureRef)


def test_operationfeatureref_constructor_exists():
    assert callable(OperationFeatureRef.__init__)


def test_operationfeatureref_constructor_args():
    sig = inspect.signature(OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_definedoperationref_is_not_abstract():
    assert not inspect.isabstract(ir_DefinedOperationRef)


def test_ir_definedoperationref_constructor_exists():
    assert callable(ir_DefinedOperationRef.__init__)


def test_ir_definedoperationref_constructor_args():
    sig = inspect.signature(ir_DefinedOperationRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_builtinoperationref_is_not_abstract():
    assert not inspect.isabstract(ir_BuiltinOperationRef)


def test_ir_builtinoperationref_constructor_exists():
    assert callable(ir_BuiltinOperationRef.__init__)


def test_ir_builtinoperationref_constructor_args():
    sig = inspect.signature(ir_BuiltinOperationRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_efclass_is_not_abstract():
    assert not inspect.isabstract(ir_EFClass)


def test_ir_efclass_constructor_exists():
    assert callable(ir_EFClass.__init__)


def test_ir_efclass_constructor_args():
    sig = inspect.signature(ir_EFClass.__init__)
    params = list(sig.parameters.keys())



def test_featureref_is_not_abstract():
    assert not inspect.isabstract(FeatureRef)


def test_featureref_constructor_exists():
    assert callable(FeatureRef.__init__)


def test_featureref_constructor_args():
    sig = inspect.signature(FeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_propertyfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir_PropertyFeatureRef)


def test_ir_propertyfeatureref_constructor_exists():
    assert callable(ir_PropertyFeatureRef.__init__)


def test_ir_propertyfeatureref_constructor_args():
    sig = inspect.signature(ir_PropertyFeatureRef.__init__)
    params = list(sig.parameters.keys())



def test_ir_operationfeatureref_is_not_abstract():
    assert not inspect.isabstract(ir_OperationFeatureRef)


def test_ir_operationfeatureref_constructor_exists():
    assert callable(ir_OperationFeatureRef.__init__)


def test_ir_operationfeatureref_constructor_args():
    sig = inspect.signature(ir_OperationFeatureRef.__init__)
    params = list(sig.parameters.keys())

def test_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "NOT",
        "EQUAL",
        "GREATER_OR_EQUAL",
        "MUL",
        "AND",
        "XOR",
        "PLUS",
        "DISTINCT",
        "OR",
        "MINUS",
        "GREATER",
        "DIV",
        "LESS",
        "LESS_OR_EQUAL",
        "IMPLIES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"


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
ir_FeatureRef_strategy = st.builds(
    ir_FeatureRef,
)
ir_Constraint_strategy = st.builds(
    ir_Constraint,
    name=
        safe_text
)
ir_EFMetamodel_strategy = st.builds(
    ir_EFMetamodel,
)
AbstractFunction_strategy = st.builds(
    AbstractFunction,
)
ir_Specification_strategy = st.builds(
    ir_Specification,
)
ir_EFType_strategy = st.builds(
    ir_EFType,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ir_AbstractFunction_strategy = st.builds(
    ir_AbstractFunction,
    name=
        safe_text
)
ir_TypeRef_strategy = st.builds(
    ir_TypeRef,
)
ir_TypedElement_strategy = st.builds(
    ir_TypedElement,
)
ir_Operation_strategy = st.builds(
    ir_Operation,
)
ir_ocl_OclAnyLibElement_strategy = st.builds(
    ir_ocl_OclAnyLibElement,
)
CollectionLiteralExp_strategy = st.builds(
    CollectionLiteralExp,
)
ir_ocl_OrderedSetLiteralExp_strategy = st.builds(
    ir_ocl_OrderedSetLiteralExp,
)
ir_ocl_SequenceLiteralExp_strategy = st.builds(
    ir_ocl_SequenceLiteralExp,
)
ir_ocl_BagLiteralExp_strategy = st.builds(
    ir_ocl_BagLiteralExp,
)
ir_ocl_SetLiteralExp_strategy = st.builds(
    ir_ocl_SetLiteralExp,
)
ocl_ir_EFEnumLiteral_strategy = st.builds(
    ocl_ir_EFEnumLiteral,
)
ocl_ir_MetaTypeRef_strategy = st.builds(
    ocl_ir_MetaTypeRef,
)
ir_ocl_TuplePart_strategy = st.builds(
    ir_ocl_TuplePart,
    name=
        safe_text
)
TuplePart_strategy = st.builds(
    TuplePart,
)
ocl_ir_EFTupleType_strategy = st.builds(
    ocl_ir_EFTupleType,
)
LiteralExp_strategy = st.builds(
    LiteralExp,
)
ir_ocl_EnumLiteralExp_strategy = st.builds(
    ir_ocl_EnumLiteralExp,
)
ir_ocl_IntegerLiteralExp_strategy = st.builds(
    ir_ocl_IntegerLiteralExp,
    value=
        safe_text
)
ir_ocl_TupleLiteralExp_strategy = st.builds(
    ir_ocl_TupleLiteralExp,
)
ir_ocl_CollectionLiteralExp_strategy = st.builds(
    ir_ocl_CollectionLiteralExp,
)
ir_ocl_OclUndefined_strategy = st.builds(
    ir_ocl_OclUndefined,
)
ir_ocl_OclInvalid_strategy = st.builds(
    ir_ocl_OclInvalid,
)
ir_ocl_RealLiteralExp_strategy = st.builds(
    ir_ocl_RealLiteralExp,
    value=
        safe_text
)
ir_ocl_StringLiteralExp_strategy = st.builds(
    ir_ocl_StringLiteralExp,
    value=
        safe_text
)
ir_ocl_BooleanLiteralExp_strategy = st.builds(
    ir_ocl_BooleanLiteralExp,
    value=
        st.booleans()
)
LoopExp_strategy = st.builds(
    LoopExp,
)
ir_ocl_IterateExp_strategy = st.builds(
    ir_ocl_IterateExp,
)
ir_ocl_IteratorExp_strategy = st.builds(
    ir_ocl_IteratorExp,
    name=
        safe_text
)
Iterator_strategy = st.builds(
    Iterator,
)
ocl_ir_PropertyFeatureRef_strategy = st.builds(
    ocl_ir_PropertyFeatureRef,
)
ocl_ir_OperationFeatureRef_strategy = st.builds(
    ocl_ir_OperationFeatureRef,
)
AbstractOperationCallExp_strategy = st.builds(
    AbstractOperationCallExp,
)
ir_ocl_CollectionCallExp_strategy = st.builds(
    ir_ocl_CollectionCallExp,
    name=
        safe_text
)
ir_ocl_OperationCallExp_strategy = st.builds(
    ir_ocl_OperationCallExp,
    name=
        safe_text
)
CallExp_strategy = st.builds(
    CallExp,
)
ir_ocl_OperatorCallExp_strategy = st.builds(
    ir_ocl_OperatorCallExp,
    operator=
        safe_text
)
ir_ocl_LoopExp_strategy = st.builds(
    ir_ocl_LoopExp,
)
ir_ocl_PropertyCallExp_strategy = st.builds(
    ir_ocl_PropertyCallExp,
    name=
        safe_text
)
ir_ocl_AbstractOperationCallExp_strategy = st.builds(
    ir_ocl_AbstractOperationCallExp,
)
ocl_ir_TypeRef_strategy = st.builds(
    ocl_ir_TypeRef,
)
ir_ocl_OclExpression_strategy = st.builds(
    ir_ocl_OclExpression,
)
Operation_strategy = st.builds(
    Operation,
)
DerivedProperty_strategy = st.builds(
    DerivedProperty,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
ir_ocl_LiteralExp_strategy = st.builds(
    ir_ocl_LiteralExp,
)
ir_ocl_ModelElement_strategy = st.builds(
    ir_ocl_ModelElement,
)
ir_ocl_CallExp_strategy = st.builds(
    ir_ocl_CallExp,
)
ir_ocl_UnsupportedExp_strategy = st.builds(
    ir_ocl_UnsupportedExp,
    description=
        safe_text,
    reason=
        safe_text
)
ir_ocl_VarExp_strategy = st.builds(
    ir_ocl_VarExp,
)
ir_ocl_LetExp_strategy = st.builds(
    ir_ocl_LetExp,
)
ir_ocl_IfExp_strategy = st.builds(
    ir_ocl_IfExp,
)
ocl_ir_EFClass_strategy = st.builds(
    ocl_ir_EFClass,
)
ocl_WithContextVariable_strategy = st.builds(
    ocl_WithContextVariable,
)
ir_ocl_OclOperation_strategy = st.builds(
    ir_ocl_OclOperation,
)
ir_ocl_OclDerivedProperty_strategy = st.builds(
    ir_ocl_OclDerivedProperty,
)
Constraint_strategy = st.builds(
    Constraint,
)
ir_ocl_OclInvariant_strategy = st.builds(
    ir_ocl_OclInvariant,
)
ocl_ir_VariableDeclaration_strategy = st.builds(
    ocl_ir_VariableDeclaration,
)
ir_ocl_WithContextVariable_strategy = st.builds(
    ir_ocl_WithContextVariable,
)
CollectionTypeRef_strategy = st.builds(
    CollectionTypeRef,
)
ir_OrderedSetTypeRef_strategy = st.builds(
    ir_OrderedSetTypeRef,
)
ir_BagTypeRef_strategy = st.builds(
    ir_BagTypeRef,
)
ir_SequenceTypeRef_strategy = st.builds(
    ir_SequenceTypeRef,
)
ir_SetTypeRef_strategy = st.builds(
    ir_SetTypeRef,
)
TypeRef_strategy = st.builds(
    TypeRef,
)
ir_CollectionTypeRef_strategy = st.builds(
    ir_CollectionTypeRef,
)
ir_InvalidTypeRef_strategy = st.builds(
    ir_InvalidTypeRef,
)
ir_MetaTypeRef_strategy = st.builds(
    ir_MetaTypeRef,
)
ir_TupleTypeElement_strategy = st.builds(
    ir_TupleTypeElement,
    name=
        safe_text
)
ir_EFEnumLiteral_strategy = st.builds(
    ir_EFEnumLiteral,
    name=
        safe_text
)
ir_EEnum_strategy = st.builds(
    ir_EEnum,
)
ir_EClass_strategy = st.builds(
    ir_EClass,
)
EFType_strategy = st.builds(
    EFType,
)
ir_EFTupleType_strategy = st.builds(
    ir_EFTupleType,
    id=
        safe_text
)
ir_EFPrimitiveType_strategy = st.builds(
    ir_EFPrimitiveType,
    name=
        safe_text
)
ir_EFEnum_strategy = st.builds(
    ir_EFEnum,
)
ir_EPackage_strategy = st.builds(
    ir_EPackage,
)
ir_EFPackage_strategy = st.builds(
    ir_EFPackage,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ir_ocl_Iterator_strategy = st.builds(
    ir_ocl_Iterator,
)
ir_Parameter_strategy = st.builds(
    ir_Parameter,
)
ir_VariableDeclaration_strategy = st.builds(
    ir_VariableDeclaration,
    name=
        safe_text
)
ir_EStructuralFeature_strategy = st.builds(
    ir_EStructuralFeature,
)
PropertyFeatureRef_strategy = st.builds(
    PropertyFeatureRef,
)
ir_DerivedPropertyRef_strategy = st.builds(
    ir_DerivedPropertyRef,
)
ir_MetamodelFeatureRef_strategy = st.builds(
    ir_MetamodelFeatureRef,
)
ir_BuiltinPropertyRef_strategy = st.builds(
    ir_BuiltinPropertyRef,
)
ir_TupleFieldRef_strategy = st.builds(
    ir_TupleFieldRef,
    name=
        safe_text
)
ir_DerivedProperty_strategy = st.builds(
    ir_DerivedProperty,
)
OperationFeatureRef_strategy = st.builds(
    OperationFeatureRef,
)
ir_DefinedOperationRef_strategy = st.builds(
    ir_DefinedOperationRef,
)
ir_BuiltinOperationRef_strategy = st.builds(
    ir_BuiltinOperationRef,
)
ir_EFClass_strategy = st.builds(
    ir_EFClass,
)
FeatureRef_strategy = st.builds(
    FeatureRef,
)
ir_PropertyFeatureRef_strategy = st.builds(
    ir_PropertyFeatureRef,
)
ir_OperationFeatureRef_strategy = st.builds(
    ir_OperationFeatureRef,
)

@given(instance=ir_FeatureRef_strategy)
@settings(max_examples=50)
def test_ir_featureref_instantiation(instance):
    assert isinstance(instance, ir_FeatureRef)

@given(instance=ir_Constraint_strategy)
@settings(max_examples=50)
def test_ir_constraint_instantiation(instance):
    assert isinstance(instance, ir_Constraint)



@given(instance=ir_Constraint_strategy)
def test_ir_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_EFMetamodel_strategy)
@settings(max_examples=50)
def test_ir_efmetamodel_instantiation(instance):
    assert isinstance(instance, ir_EFMetamodel)

@given(instance=AbstractFunction_strategy)
@settings(max_examples=50)
def test_abstractfunction_instantiation(instance):
    assert isinstance(instance, AbstractFunction)

@given(instance=ir_Specification_strategy)
@settings(max_examples=50)
def test_ir_specification_instantiation(instance):
    assert isinstance(instance, ir_Specification)

@given(instance=ir_EFType_strategy)
@settings(max_examples=50)
def test_ir_eftype_instantiation(instance):
    assert isinstance(instance, ir_EFType)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ir_AbstractFunction_strategy)
@settings(max_examples=50)
def test_ir_abstractfunction_instantiation(instance):
    assert isinstance(instance, ir_AbstractFunction)



@given(instance=ir_AbstractFunction_strategy)
def test_ir_abstractfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_TypeRef_strategy)
@settings(max_examples=50)
def test_ir_typeref_instantiation(instance):
    assert isinstance(instance, ir_TypeRef)

@given(instance=ir_TypedElement_strategy)
@settings(max_examples=50)
def test_ir_typedelement_instantiation(instance):
    assert isinstance(instance, ir_TypedElement)

@given(instance=ir_Operation_strategy)
@settings(max_examples=50)
def test_ir_operation_instantiation(instance):
    assert isinstance(instance, ir_Operation)

@given(instance=ir_ocl_OclAnyLibElement_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclanylibelement_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclAnyLibElement)

@given(instance=CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, CollectionLiteralExp)

@given(instance=ir_ocl_OrderedSetLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_orderedsetliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_OrderedSetLiteralExp)

@given(instance=ir_ocl_SequenceLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_sequenceliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_SequenceLiteralExp)

@given(instance=ir_ocl_BagLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_bagliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_BagLiteralExp)

@given(instance=ir_ocl_SetLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_setliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_SetLiteralExp)

@given(instance=ocl_ir_EFEnumLiteral_strategy)
@settings(max_examples=50)
def test_ocl_ir_efenumliteral_instantiation(instance):
    assert isinstance(instance, ocl_ir_EFEnumLiteral)

@given(instance=ocl_ir_MetaTypeRef_strategy)
@settings(max_examples=50)
def test_ocl_ir_metatyperef_instantiation(instance):
    assert isinstance(instance, ocl_ir_MetaTypeRef)

@given(instance=ir_ocl_TuplePart_strategy)
@settings(max_examples=50)
def test_ir_ocl_tuplepart_instantiation(instance):
    assert isinstance(instance, ir_ocl_TuplePart)



@given(instance=ir_ocl_TuplePart_strategy)
def test_ir_ocl_tuplepart_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TuplePart_strategy)
@settings(max_examples=50)
def test_tuplepart_instantiation(instance):
    assert isinstance(instance, TuplePart)

@given(instance=ocl_ir_EFTupleType_strategy)
@settings(max_examples=50)
def test_ocl_ir_eftupletype_instantiation(instance):
    assert isinstance(instance, ocl_ir_EFTupleType)

@given(instance=LiteralExp_strategy)
@settings(max_examples=50)
def test_literalexp_instantiation(instance):
    assert isinstance(instance, LiteralExp)

@given(instance=ir_ocl_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_EnumLiteralExp)

@given(instance=ir_ocl_IntegerLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_integerliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_IntegerLiteralExp)



@given(instance=ir_ocl_IntegerLiteralExp_strategy)
def test_ir_ocl_integerliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_ocl_TupleLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_tupleliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_TupleLiteralExp)

@given(instance=ir_ocl_CollectionLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_collectionliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_CollectionLiteralExp)

@given(instance=ir_ocl_OclUndefined_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclundefined_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclUndefined)

@given(instance=ir_ocl_OclInvalid_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclinvalid_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclInvalid)

@given(instance=ir_ocl_RealLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_realliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_RealLiteralExp)



@given(instance=ir_ocl_RealLiteralExp_strategy)
def test_ir_ocl_realliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_ocl_StringLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_stringliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_StringLiteralExp)



@given(instance=ir_ocl_StringLiteralExp_strategy)
def test_ir_ocl_stringliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ir_ocl_BooleanLiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_booleanliteralexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_BooleanLiteralExp)



@given(instance=ir_ocl_BooleanLiteralExp_strategy)
def test_ir_ocl_booleanliteralexp_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=ir_ocl_IterateExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_iterateexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_IterateExp)

@given(instance=ir_ocl_IteratorExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_IteratorExp)



@given(instance=ir_ocl_IteratorExp_strategy)
def test_ir_ocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=ocl_ir_PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_ocl_ir_propertyfeatureref_instantiation(instance):
    assert isinstance(instance, ocl_ir_PropertyFeatureRef)

@given(instance=ocl_ir_OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_ocl_ir_operationfeatureref_instantiation(instance):
    assert isinstance(instance, ocl_ir_OperationFeatureRef)

@given(instance=AbstractOperationCallExp_strategy)
@settings(max_examples=50)
def test_abstractoperationcallexp_instantiation(instance):
    assert isinstance(instance, AbstractOperationCallExp)

@given(instance=ir_ocl_CollectionCallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_collectioncallexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_CollectionCallExp)



@given(instance=ir_ocl_CollectionCallExp_strategy)
def test_ir_ocl_collectioncallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_ocl_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_OperationCallExp)



@given(instance=ir_ocl_OperationCallExp_strategy)
def test_ir_ocl_operationcallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CallExp_strategy)
@settings(max_examples=50)
def test_callexp_instantiation(instance):
    assert isinstance(instance, CallExp)

@given(instance=ir_ocl_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_OperatorCallExp)



@given(instance=ir_ocl_OperatorCallExp_strategy)
def test_ir_ocl_operatorcallexp_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=ir_ocl_LoopExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_loopexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_LoopExp)

@given(instance=ir_ocl_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_PropertyCallExp)



@given(instance=ir_ocl_PropertyCallExp_strategy)
def test_ir_ocl_propertycallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_ocl_AbstractOperationCallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_abstractoperationcallexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_AbstractOperationCallExp)

@given(instance=ocl_ir_TypeRef_strategy)
@settings(max_examples=50)
def test_ocl_ir_typeref_instantiation(instance):
    assert isinstance(instance, ocl_ir_TypeRef)

@given(instance=ir_ocl_OclExpression_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclExpression)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=DerivedProperty_strategy)
@settings(max_examples=50)
def test_derivedproperty_instantiation(instance):
    assert isinstance(instance, DerivedProperty)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=ir_ocl_LiteralExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_literalexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_LiteralExp)

@given(instance=ir_ocl_ModelElement_strategy)
@settings(max_examples=50)
def test_ir_ocl_modelelement_instantiation(instance):
    assert isinstance(instance, ir_ocl_ModelElement)

@given(instance=ir_ocl_CallExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_callexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_CallExp)

@given(instance=ir_ocl_UnsupportedExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_unsupportedexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_UnsupportedExp)



@given(instance=ir_ocl_UnsupportedExp_strategy)
def test_ir_ocl_unsupportedexp_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ir_ocl_UnsupportedExp_strategy)
def test_ir_ocl_unsupportedexp_reason_setter(instance):
    original = instance.reason
    instance.reason = original
    assert instance.reason == original

@given(instance=ir_ocl_VarExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_varexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_VarExp)

@given(instance=ir_ocl_LetExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_letexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_LetExp)

@given(instance=ir_ocl_IfExp_strategy)
@settings(max_examples=50)
def test_ir_ocl_ifexp_instantiation(instance):
    assert isinstance(instance, ir_ocl_IfExp)

@given(instance=ocl_ir_EFClass_strategy)
@settings(max_examples=50)
def test_ocl_ir_efclass_instantiation(instance):
    assert isinstance(instance, ocl_ir_EFClass)

@given(instance=ocl_WithContextVariable_strategy)
@settings(max_examples=50)
def test_ocl_withcontextvariable_instantiation(instance):
    assert isinstance(instance, ocl_WithContextVariable)

@given(instance=ir_ocl_OclOperation_strategy)
@settings(max_examples=50)
def test_ir_ocl_ocloperation_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclOperation)

@given(instance=ir_ocl_OclDerivedProperty_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclderivedproperty_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclDerivedProperty)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=ir_ocl_OclInvariant_strategy)
@settings(max_examples=50)
def test_ir_ocl_oclinvariant_instantiation(instance):
    assert isinstance(instance, ir_ocl_OclInvariant)

@given(instance=ocl_ir_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ocl_ir_variabledeclaration_instantiation(instance):
    assert isinstance(instance, ocl_ir_VariableDeclaration)

@given(instance=ir_ocl_WithContextVariable_strategy)
@settings(max_examples=50)
def test_ir_ocl_withcontextvariable_instantiation(instance):
    assert isinstance(instance, ir_ocl_WithContextVariable)

@given(instance=CollectionTypeRef_strategy)
@settings(max_examples=50)
def test_collectiontyperef_instantiation(instance):
    assert isinstance(instance, CollectionTypeRef)

@given(instance=ir_OrderedSetTypeRef_strategy)
@settings(max_examples=50)
def test_ir_orderedsettyperef_instantiation(instance):
    assert isinstance(instance, ir_OrderedSetTypeRef)

@given(instance=ir_BagTypeRef_strategy)
@settings(max_examples=50)
def test_ir_bagtyperef_instantiation(instance):
    assert isinstance(instance, ir_BagTypeRef)

@given(instance=ir_SequenceTypeRef_strategy)
@settings(max_examples=50)
def test_ir_sequencetyperef_instantiation(instance):
    assert isinstance(instance, ir_SequenceTypeRef)

@given(instance=ir_SetTypeRef_strategy)
@settings(max_examples=50)
def test_ir_settyperef_instantiation(instance):
    assert isinstance(instance, ir_SetTypeRef)

@given(instance=TypeRef_strategy)
@settings(max_examples=50)
def test_typeref_instantiation(instance):
    assert isinstance(instance, TypeRef)

@given(instance=ir_CollectionTypeRef_strategy)
@settings(max_examples=50)
def test_ir_collectiontyperef_instantiation(instance):
    assert isinstance(instance, ir_CollectionTypeRef)

@given(instance=ir_InvalidTypeRef_strategy)
@settings(max_examples=50)
def test_ir_invalidtyperef_instantiation(instance):
    assert isinstance(instance, ir_InvalidTypeRef)

@given(instance=ir_MetaTypeRef_strategy)
@settings(max_examples=50)
def test_ir_metatyperef_instantiation(instance):
    assert isinstance(instance, ir_MetaTypeRef)

@given(instance=ir_TupleTypeElement_strategy)
@settings(max_examples=50)
def test_ir_tupletypeelement_instantiation(instance):
    assert isinstance(instance, ir_TupleTypeElement)



@given(instance=ir_TupleTypeElement_strategy)
def test_ir_tupletypeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_EFEnumLiteral_strategy)
@settings(max_examples=50)
def test_ir_efenumliteral_instantiation(instance):
    assert isinstance(instance, ir_EFEnumLiteral)



@given(instance=ir_EFEnumLiteral_strategy)
def test_ir_efenumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_EEnum_strategy)
@settings(max_examples=50)
def test_ir_eenum_instantiation(instance):
    assert isinstance(instance, ir_EEnum)

@given(instance=ir_EClass_strategy)
@settings(max_examples=50)
def test_ir_eclass_instantiation(instance):
    assert isinstance(instance, ir_EClass)

@given(instance=EFType_strategy)
@settings(max_examples=50)
def test_eftype_instantiation(instance):
    assert isinstance(instance, EFType)

@given(instance=ir_EFTupleType_strategy)
@settings(max_examples=50)
def test_ir_eftupletype_instantiation(instance):
    assert isinstance(instance, ir_EFTupleType)



@given(instance=ir_EFTupleType_strategy)
def test_ir_eftupletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ir_EFPrimitiveType_strategy)
@settings(max_examples=50)
def test_ir_efprimitivetype_instantiation(instance):
    assert isinstance(instance, ir_EFPrimitiveType)



@given(instance=ir_EFPrimitiveType_strategy)
def test_ir_efprimitivetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_EFEnum_strategy)
@settings(max_examples=50)
def test_ir_efenum_instantiation(instance):
    assert isinstance(instance, ir_EFEnum)

@given(instance=ir_EPackage_strategy)
@settings(max_examples=50)
def test_ir_epackage_instantiation(instance):
    assert isinstance(instance, ir_EPackage)

@given(instance=ir_EFPackage_strategy)
@settings(max_examples=50)
def test_ir_efpackage_instantiation(instance):
    assert isinstance(instance, ir_EFPackage)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ir_ocl_Iterator_strategy)
@settings(max_examples=50)
def test_ir_ocl_iterator_instantiation(instance):
    assert isinstance(instance, ir_ocl_Iterator)

@given(instance=ir_Parameter_strategy)
@settings(max_examples=50)
def test_ir_parameter_instantiation(instance):
    assert isinstance(instance, ir_Parameter)

@given(instance=ir_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ir_variabledeclaration_instantiation(instance):
    assert isinstance(instance, ir_VariableDeclaration)



@given(instance=ir_VariableDeclaration_strategy)
def test_ir_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_EStructuralFeature_strategy)
@settings(max_examples=50)
def test_ir_estructuralfeature_instantiation(instance):
    assert isinstance(instance, ir_EStructuralFeature)

@given(instance=PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_propertyfeatureref_instantiation(instance):
    assert isinstance(instance, PropertyFeatureRef)

@given(instance=ir_DerivedPropertyRef_strategy)
@settings(max_examples=50)
def test_ir_derivedpropertyref_instantiation(instance):
    assert isinstance(instance, ir_DerivedPropertyRef)

@given(instance=ir_MetamodelFeatureRef_strategy)
@settings(max_examples=50)
def test_ir_metamodelfeatureref_instantiation(instance):
    assert isinstance(instance, ir_MetamodelFeatureRef)

@given(instance=ir_BuiltinPropertyRef_strategy)
@settings(max_examples=50)
def test_ir_builtinpropertyref_instantiation(instance):
    assert isinstance(instance, ir_BuiltinPropertyRef)

@given(instance=ir_TupleFieldRef_strategy)
@settings(max_examples=50)
def test_ir_tuplefieldref_instantiation(instance):
    assert isinstance(instance, ir_TupleFieldRef)



@given(instance=ir_TupleFieldRef_strategy)
def test_ir_tuplefieldref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ir_DerivedProperty_strategy)
@settings(max_examples=50)
def test_ir_derivedproperty_instantiation(instance):
    assert isinstance(instance, ir_DerivedProperty)

@given(instance=OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_operationfeatureref_instantiation(instance):
    assert isinstance(instance, OperationFeatureRef)

@given(instance=ir_DefinedOperationRef_strategy)
@settings(max_examples=50)
def test_ir_definedoperationref_instantiation(instance):
    assert isinstance(instance, ir_DefinedOperationRef)

@given(instance=ir_BuiltinOperationRef_strategy)
@settings(max_examples=50)
def test_ir_builtinoperationref_instantiation(instance):
    assert isinstance(instance, ir_BuiltinOperationRef)

@given(instance=ir_EFClass_strategy)
@settings(max_examples=50)
def test_ir_efclass_instantiation(instance):
    assert isinstance(instance, ir_EFClass)

@given(instance=FeatureRef_strategy)
@settings(max_examples=50)
def test_featureref_instantiation(instance):
    assert isinstance(instance, FeatureRef)

@given(instance=ir_PropertyFeatureRef_strategy)
@settings(max_examples=50)
def test_ir_propertyfeatureref_instantiation(instance):
    assert isinstance(instance, ir_PropertyFeatureRef)

@given(instance=ir_OperationFeatureRef_strategy)
@settings(max_examples=50)
def test_ir_operationfeatureref_instantiation(instance):
    assert isinstance(instance, ir_OperationFeatureRef)
