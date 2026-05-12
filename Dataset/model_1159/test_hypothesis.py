import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MapExp,
    MapElement,
    TupleExp,
    TuplePart,
    NumericExp,
    OCL_IntegerExp,
    OCL_RealExp,
    PrimitiveExp,
    OCL_BooleanExp,
    OCL_NumericExp,
    OCL_StringExp,
    Attribute,
    Operation,
    OperationCallExp,
    LoopExp,
    LetExp,
    CollectionExp,
    OCL_SetExp,
    OCL_SequenceExp,
    OCL_BagExp,
    OCL_OrderedSetExp,
    PropertyCallExp,
    OCL_OperationCallExp,
    OCL_NavigationOrAttributeCallExp,
    IfExp,
    OclType,
    ocl_constraints_LocatedElement,
    OclExpression,
    OCL_VariableExp,
    OCL_PrimitiveExp,
    OCL_SuperExp,
    OCL_OclUndefinedExp,
    OCL_EnumLiteralExp,
    OCL_CollectionExp,
    OCL_MapExp,
    OCL_TupleExp,
    OCL_PropertyCallExp,
    OclPrecondition,
    OclInvariant,
    OclConstraintsModel,
    Metaclass,
    ocl_constraints_UMLClass,
    VariableDeclaration,
    OCL_TuplePart,
    Context,
    LocatedElement,
    ocl_constraints_OclInvariant,
    ocl_constraints_OclPrecondition,
    OCL_MapElement,
    ocl_constraints_Context,
    ocl_constraints_Metaclass,
    OCL_OclExpression,
    ocl_constraints_OclConstraintsModel,
    UMLClass,
    OclModelElement,
    OCL_OclModel,
    Parameter,
    OCL_OclFeature,
    OclFeatureDefinition,
    OCL_OclContextDefinition,
    OclFeature,
    OCL_Attribute,
    OCL_Operation,
    OCL_OclFeatureDefinition,
    OCL_MapType,
    OclModel,
    OCL_OclModelElement,
    TupleType,
    OCL_TupleTypeAttribute,
    OCL_OclAnyType,
    NumericType,
    OCL_RealType,
    OCL_IntegerType,
    Primitive,
    OCL_NumericType,
    OCL_BooleanType,
    OCL_StringType,
    OCL_Primitive,
    TupleTypeAttribute,
    CollectionType,
    OCL_SetType,
    OCL_BagType,
    OCL_SequenceType,
    OCL_OrderedSetType,
    MapType,
    OclContextDefinition,
    OCL_OclType,
    OCL_TupleType,
    OCL_Parameter,
    OCL_Iterator,
    VariableExp,
    IterateExp,
    OCL_CollectionType,
    OCL_VariableDeclaration,
    OCL_IfExp,
    OCL_LetExp,
    OCL_IteratorExp,
    OCL_IterateExp,
    Iterator,
    OCL_LoopExp,
    OCL_CollectionOperationCallExp,
    OCL_OperatorCallExp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_numericexp_is_not_abstract():
    assert not inspect.isabstract(NumericExp)


def test_numericexp_constructor_exists():
    assert callable(NumericExp.__init__)


def test_numericexp_constructor_args():
    sig = inspect.signature(NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_integerexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerExp)


def test_ocl_integerexp_constructor_exists():
    assert callable(OCL_IntegerExp.__init__)


def test_ocl_integerexp_constructor_args():
    sig = inspect.signature(OCL_IntegerExp.__init__)
    params = list(sig.parameters.keys())
    assert "integerSymbol" in params, "Missing parameter 'integerSymbol'"

def test_ocl_integerexp_has_integerSymbol():
    assert hasattr(OCL_IntegerExp, "integerSymbol")
    descriptor = None
    for klass in OCL_IntegerExp.__mro__:
        if "integerSymbol" in klass.__dict__:
            descriptor = klass.__dict__["integerSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_realexp_is_not_abstract():
    assert not inspect.isabstract(OCL_RealExp)


def test_ocl_realexp_constructor_exists():
    assert callable(OCL_RealExp.__init__)


def test_ocl_realexp_constructor_args():
    sig = inspect.signature(OCL_RealExp.__init__)
    params = list(sig.parameters.keys())
    assert "realSymbol" in params, "Missing parameter 'realSymbol'"

def test_ocl_realexp_has_realSymbol():
    assert hasattr(OCL_RealExp, "realSymbol")
    descriptor = None
    for klass in OCL_RealExp.__mro__:
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



def test_ocl_booleanexp_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanExp)


def test_ocl_booleanexp_constructor_exists():
    assert callable(OCL_BooleanExp.__init__)


def test_ocl_booleanexp_constructor_args():
    sig = inspect.signature(OCL_BooleanExp.__init__)
    params = list(sig.parameters.keys())
    assert "booleanSymbol" in params, "Missing parameter 'booleanSymbol'"

def test_ocl_booleanexp_has_booleanSymbol():
    assert hasattr(OCL_BooleanExp, "booleanSymbol")
    descriptor = None
    for klass in OCL_BooleanExp.__mro__:
        if "booleanSymbol" in klass.__dict__:
            descriptor = klass.__dict__["booleanSymbol"]
            break
    assert isinstance(descriptor, property)



def test_ocl_numericexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NumericExp)


def test_ocl_numericexp_constructor_exists():
    assert callable(OCL_NumericExp.__init__)


def test_ocl_numericexp_constructor_args():
    sig = inspect.signature(OCL_NumericExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_stringexp_is_not_abstract():
    assert not inspect.isabstract(OCL_StringExp)


def test_ocl_stringexp_constructor_exists():
    assert callable(OCL_StringExp.__init__)


def test_ocl_stringexp_constructor_args():
    sig = inspect.signature(OCL_StringExp.__init__)
    params = list(sig.parameters.keys())
    assert "stringSymbol" in params, "Missing parameter 'stringSymbol'"

def test_ocl_stringexp_has_stringSymbol():
    assert hasattr(OCL_StringExp, "stringSymbol")
    descriptor = None
    for klass in OCL_StringExp.__mro__:
        if "stringSymbol" in klass.__dict__:
            descriptor = klass.__dict__["stringSymbol"]
            break
    assert isinstance(descriptor, property)



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



def test_ocl_setexp_is_not_abstract():
    assert not inspect.isabstract(OCL_SetExp)


def test_ocl_setexp_constructor_exists():
    assert callable(OCL_SetExp.__init__)


def test_ocl_setexp_constructor_args():
    sig = inspect.signature(OCL_SetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_sequenceexp_is_not_abstract():
    assert not inspect.isabstract(OCL_SequenceExp)


def test_ocl_sequenceexp_constructor_exists():
    assert callable(OCL_SequenceExp.__init__)


def test_ocl_sequenceexp_constructor_args():
    sig = inspect.signature(OCL_SequenceExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_bagexp_is_not_abstract():
    assert not inspect.isabstract(OCL_BagExp)


def test_ocl_bagexp_constructor_exists():
    assert callable(OCL_BagExp.__init__)


def test_ocl_bagexp_constructor_args():
    sig = inspect.signature(OCL_BagExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_orderedsetexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OrderedSetExp)


def test_ocl_orderedsetexp_constructor_exists():
    assert callable(OCL_OrderedSetExp.__init__)


def test_ocl_orderedsetexp_constructor_args():
    sig = inspect.signature(OCL_OrderedSetExp.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperationCallExp)


def test_ocl_operationcallexp_constructor_exists():
    assert callable(OCL_OperationCallExp.__init__)


def test_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(OCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "operationName" in params, "Missing parameter 'operationName'"

def test_ocl_operationcallexp_has_operationName():
    assert hasattr(OCL_OperationCallExp, "operationName")
    descriptor = None
    for klass in OCL_OperationCallExp.__mro__:
        if "operationName" in klass.__dict__:
            descriptor = klass.__dict__["operationName"]
            break
    assert isinstance(descriptor, property)



def test_ocl_navigationorattributecallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_NavigationOrAttributeCallExp)


def test_ocl_navigationorattributecallexp_constructor_exists():
    assert callable(OCL_NavigationOrAttributeCallExp.__init__)


def test_ocl_navigationorattributecallexp_constructor_args():
    sig = inspect.signature(OCL_NavigationOrAttributeCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_navigationorattributecallexp_has_name():
    assert hasattr(OCL_NavigationOrAttributeCallExp, "name")
    descriptor = None
    for klass in OCL_NavigationOrAttributeCallExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



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



def test_ocl_constraints_locatedelement_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_LocatedElement)


def test_ocl_constraints_locatedelement_constructor_exists():
    assert callable(ocl_constraints_LocatedElement.__init__)


def test_ocl_constraints_locatedelement_constructor_args():
    sig = inspect.signature(ocl_constraints_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_ocl_constraints_locatedelement_has_location():
    assert hasattr(ocl_constraints_LocatedElement, "location")
    descriptor = None
    for klass in ocl_constraints_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_ocl_constraints_locatedelement_has_commentsAfter():
    assert hasattr(ocl_constraints_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in ocl_constraints_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_ocl_constraints_locatedelement_has_commentsBefore():
    assert hasattr(ocl_constraints_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in ocl_constraints_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)



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



def test_ocl_primitiveexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PrimitiveExp)


def test_ocl_primitiveexp_constructor_exists():
    assert callable(OCL_PrimitiveExp.__init__)


def test_ocl_primitiveexp_constructor_args():
    sig = inspect.signature(OCL_PrimitiveExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_superexp_is_not_abstract():
    assert not inspect.isabstract(OCL_SuperExp)


def test_ocl_superexp_constructor_exists():
    assert callable(OCL_SuperExp.__init__)


def test_ocl_superexp_constructor_args():
    sig = inspect.signature(OCL_SuperExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclundefinedexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OclUndefinedExp)


def test_ocl_oclundefinedexp_constructor_exists():
    assert callable(OCL_OclUndefinedExp.__init__)


def test_ocl_oclundefinedexp_constructor_args():
    sig = inspect.signature(OCL_OclUndefinedExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_enumliteralexp_is_not_abstract():
    assert not inspect.isabstract(OCL_EnumLiteralExp)


def test_ocl_enumliteralexp_constructor_exists():
    assert callable(OCL_EnumLiteralExp.__init__)


def test_ocl_enumliteralexp_constructor_args():
    sig = inspect.signature(OCL_EnumLiteralExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_enumliteralexp_has_name():
    assert hasattr(OCL_EnumLiteralExp, "name")
    descriptor = None
    for klass in OCL_EnumLiteralExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_collectionexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionExp)


def test_ocl_collectionexp_constructor_exists():
    assert callable(OCL_CollectionExp.__init__)


def test_ocl_collectionexp_constructor_args():
    sig = inspect.signature(OCL_CollectionExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_mapexp_is_not_abstract():
    assert not inspect.isabstract(OCL_MapExp)


def test_ocl_mapexp_constructor_exists():
    assert callable(OCL_MapExp.__init__)


def test_ocl_mapexp_constructor_args():
    sig = inspect.signature(OCL_MapExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_tupleexp_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleExp)


def test_ocl_tupleexp_constructor_exists():
    assert callable(OCL_TupleExp.__init__)


def test_ocl_tupleexp_constructor_args():
    sig = inspect.signature(OCL_TupleExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_PropertyCallExp)


def test_ocl_propertycallexp_constructor_exists():
    assert callable(OCL_PropertyCallExp.__init__)


def test_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_oclprecondition_is_not_abstract():
    assert not inspect.isabstract(OclPrecondition)


def test_oclprecondition_constructor_exists():
    assert callable(OclPrecondition.__init__)


def test_oclprecondition_constructor_args():
    sig = inspect.signature(OclPrecondition.__init__)
    params = list(sig.parameters.keys())



def test_oclinvariant_is_not_abstract():
    assert not inspect.isabstract(OclInvariant)


def test_oclinvariant_constructor_exists():
    assert callable(OclInvariant.__init__)


def test_oclinvariant_constructor_args():
    sig = inspect.signature(OclInvariant.__init__)
    params = list(sig.parameters.keys())



def test_oclconstraintsmodel_is_not_abstract():
    assert not inspect.isabstract(OclConstraintsModel)


def test_oclconstraintsmodel_constructor_exists():
    assert callable(OclConstraintsModel.__init__)


def test_oclconstraintsmodel_constructor_args():
    sig = inspect.signature(OclConstraintsModel.__init__)
    params = list(sig.parameters.keys())



def test_metaclass_is_not_abstract():
    assert not inspect.isabstract(Metaclass)


def test_metaclass_constructor_exists():
    assert callable(Metaclass.__init__)


def test_metaclass_constructor_args():
    sig = inspect.signature(Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_ocl_constraints_umlclass_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_UMLClass)


def test_ocl_constraints_umlclass_constructor_exists():
    assert callable(ocl_constraints_UMLClass.__init__)


def test_ocl_constraints_umlclass_constructor_args():
    sig = inspect.signature(ocl_constraints_UMLClass.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ocl_tuplepart_is_not_abstract():
    assert not inspect.isabstract(OCL_TuplePart)


def test_ocl_tuplepart_constructor_exists():
    assert callable(OCL_TuplePart.__init__)


def test_ocl_tuplepart_constructor_args():
    sig = inspect.signature(OCL_TuplePart.__init__)
    params = list(sig.parameters.keys())



def test_context_is_not_abstract():
    assert not inspect.isabstract(Context)


def test_context_constructor_exists():
    assert callable(Context.__init__)


def test_context_constructor_args():
    sig = inspect.signature(Context.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_constraints_oclinvariant_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_OclInvariant)


def test_ocl_constraints_oclinvariant_constructor_exists():
    assert callable(ocl_constraints_OclInvariant.__init__)


def test_ocl_constraints_oclinvariant_constructor_args():
    sig = inspect.signature(ocl_constraints_OclInvariant.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_constraints_oclinvariant_has_description():
    assert hasattr(ocl_constraints_OclInvariant, "description")
    descriptor = None
    for klass in ocl_constraints_OclInvariant.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_ocl_constraints_oclinvariant_has_name():
    assert hasattr(ocl_constraints_OclInvariant, "name")
    descriptor = None
    for klass in ocl_constraints_OclInvariant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_constraints_oclprecondition_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_OclPrecondition)


def test_ocl_constraints_oclprecondition_constructor_exists():
    assert callable(ocl_constraints_OclPrecondition.__init__)


def test_ocl_constraints_oclprecondition_constructor_args():
    sig = inspect.signature(ocl_constraints_OclPrecondition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_ocl_constraints_oclprecondition_has_name():
    assert hasattr(ocl_constraints_OclPrecondition, "name")
    descriptor = None
    for klass in ocl_constraints_OclPrecondition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ocl_constraints_oclprecondition_has_description():
    assert hasattr(ocl_constraints_OclPrecondition, "description")
    descriptor = None
    for klass in ocl_constraints_OclPrecondition.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_ocl_mapelement_is_not_abstract():
    assert not inspect.isabstract(OCL_MapElement)


def test_ocl_mapelement_constructor_exists():
    assert callable(OCL_MapElement.__init__)


def test_ocl_mapelement_constructor_args():
    sig = inspect.signature(OCL_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_constraints_context_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_Context)


def test_ocl_constraints_context_constructor_exists():
    assert callable(ocl_constraints_Context.__init__)


def test_ocl_constraints_context_constructor_args():
    sig = inspect.signature(ocl_constraints_Context.__init__)
    params = list(sig.parameters.keys())



def test_ocl_constraints_metaclass_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_Metaclass)


def test_ocl_constraints_metaclass_constructor_exists():
    assert callable(ocl_constraints_Metaclass.__init__)


def test_ocl_constraints_metaclass_constructor_args():
    sig = inspect.signature(ocl_constraints_Metaclass.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_constraints_metaclass_has_name():
    assert hasattr(ocl_constraints_Metaclass, "name")
    descriptor = None
    for klass in ocl_constraints_Metaclass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OCL_OclExpression)


def test_ocl_oclexpression_constructor_exists():
    assert callable(OCL_OclExpression.__init__)


def test_ocl_oclexpression_constructor_args():
    sig = inspect.signature(OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_ocl_constraints_oclconstraintsmodel_is_not_abstract():
    assert not inspect.isabstract(ocl_constraints_OclConstraintsModel)


def test_ocl_constraints_oclconstraintsmodel_constructor_exists():
    assert callable(ocl_constraints_OclConstraintsModel.__init__)


def test_ocl_constraints_oclconstraintsmodel_constructor_args():
    sig = inspect.signature(ocl_constraints_OclConstraintsModel.__init__)
    params = list(sig.parameters.keys())
    assert "metamodel" in params, "Missing parameter 'metamodel'"
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_constraints_oclconstraintsmodel_has_metamodel():
    assert hasattr(ocl_constraints_OclConstraintsModel, "metamodel")
    descriptor = None
    for klass in ocl_constraints_OclConstraintsModel.__mro__:
        if "metamodel" in klass.__dict__:
            descriptor = klass.__dict__["metamodel"]
            break
    assert isinstance(descriptor, property)

def test_ocl_constraints_oclconstraintsmodel_has_name():
    assert hasattr(ocl_constraints_OclConstraintsModel, "name")
    descriptor = None
    for klass in ocl_constraints_OclConstraintsModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlclass_is_not_abstract():
    assert not inspect.isabstract(UMLClass)


def test_umlclass_constructor_exists():
    assert callable(UMLClass.__init__)


def test_umlclass_constructor_args():
    sig = inspect.signature(UMLClass.__init__)
    params = list(sig.parameters.keys())



def test_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OclModelElement)


def test_oclmodelelement_constructor_exists():
    assert callable(OclModelElement.__init__)


def test_oclmodelelement_constructor_args():
    sig = inspect.signature(OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModel)


def test_ocl_oclmodel_constructor_exists():
    assert callable(OCL_OclModel.__init__)


def test_ocl_oclmodel_constructor_args():
    sig = inspect.signature(OCL_OclModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_oclmodel_has_name():
    assert hasattr(OCL_OclModel, "name")
    descriptor = None
    for klass in OCL_OclModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OCL_OclFeature)


def test_ocl_oclfeature_constructor_exists():
    assert callable(OCL_OclFeature.__init__)


def test_ocl_oclfeature_constructor_args():
    sig = inspect.signature(OCL_OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OclFeatureDefinition)


def test_oclfeaturedefinition_constructor_exists():
    assert callable(OclFeatureDefinition.__init__)


def test_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclcontextdefinition_is_not_abstract():
    assert not inspect.isabstract(OCL_OclContextDefinition)


def test_ocl_oclcontextdefinition_constructor_exists():
    assert callable(OCL_OclContextDefinition.__init__)


def test_ocl_oclcontextdefinition_constructor_args():
    sig = inspect.signature(OCL_OclContextDefinition.__init__)
    params = list(sig.parameters.keys())



def test_oclfeature_is_not_abstract():
    assert not inspect.isabstract(OclFeature)


def test_oclfeature_constructor_exists():
    assert callable(OclFeature.__init__)


def test_oclfeature_constructor_args():
    sig = inspect.signature(OclFeature.__init__)
    params = list(sig.parameters.keys())



def test_ocl_attribute_is_not_abstract():
    assert not inspect.isabstract(OCL_Attribute)


def test_ocl_attribute_constructor_exists():
    assert callable(OCL_Attribute.__init__)


def test_ocl_attribute_constructor_args():
    sig = inspect.signature(OCL_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_attribute_has_name():
    assert hasattr(OCL_Attribute, "name")
    descriptor = None
    for klass in OCL_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_operation_is_not_abstract():
    assert not inspect.isabstract(OCL_Operation)


def test_ocl_operation_constructor_exists():
    assert callable(OCL_Operation.__init__)


def test_ocl_operation_constructor_args():
    sig = inspect.signature(OCL_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_operation_has_name():
    assert hasattr(OCL_Operation, "name")
    descriptor = None
    for klass in OCL_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_oclfeaturedefinition_is_not_abstract():
    assert not inspect.isabstract(OCL_OclFeatureDefinition)


def test_ocl_oclfeaturedefinition_constructor_exists():
    assert callable(OCL_OclFeatureDefinition.__init__)


def test_ocl_oclfeaturedefinition_constructor_args():
    sig = inspect.signature(OCL_OclFeatureDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ocl_maptype_is_not_abstract():
    assert not inspect.isabstract(OCL_MapType)


def test_ocl_maptype_constructor_exists():
    assert callable(OCL_MapType.__init__)


def test_ocl_maptype_constructor_args():
    sig = inspect.signature(OCL_MapType.__init__)
    params = list(sig.parameters.keys())



def test_oclmodel_is_not_abstract():
    assert not inspect.isabstract(OclModel)


def test_oclmodel_constructor_exists():
    assert callable(OclModel.__init__)


def test_oclmodel_constructor_args():
    sig = inspect.signature(OclModel.__init__)
    params = list(sig.parameters.keys())



def test_ocl_oclmodelelement_is_not_abstract():
    assert not inspect.isabstract(OCL_OclModelElement)


def test_ocl_oclmodelelement_constructor_exists():
    assert callable(OCL_OclModelElement.__init__)


def test_ocl_oclmodelelement_constructor_args():
    sig = inspect.signature(OCL_OclModelElement.__init__)
    params = list(sig.parameters.keys())



def test_tupletype_is_not_abstract():
    assert not inspect.isabstract(TupleType)


def test_tupletype_constructor_exists():
    assert callable(TupleType.__init__)


def test_tupletype_constructor_args():
    sig = inspect.signature(TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleTypeAttribute)


def test_ocl_tupletypeattribute_constructor_exists():
    assert callable(OCL_TupleTypeAttribute.__init__)


def test_ocl_tupletypeattribute_constructor_args():
    sig = inspect.signature(OCL_TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_tupletypeattribute_has_name():
    assert hasattr(OCL_TupleTypeAttribute, "name")
    descriptor = None
    for klass in OCL_TupleTypeAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_oclanytype_is_not_abstract():
    assert not inspect.isabstract(OCL_OclAnyType)


def test_ocl_oclanytype_constructor_exists():
    assert callable(OCL_OclAnyType.__init__)


def test_ocl_oclanytype_constructor_args():
    sig = inspect.signature(OCL_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_numerictype_is_not_abstract():
    assert not inspect.isabstract(NumericType)


def test_numerictype_constructor_exists():
    assert callable(NumericType.__init__)


def test_numerictype_constructor_args():
    sig = inspect.signature(NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_realtype_is_not_abstract():
    assert not inspect.isabstract(OCL_RealType)


def test_ocl_realtype_constructor_exists():
    assert callable(OCL_RealType.__init__)


def test_ocl_realtype_constructor_args():
    sig = inspect.signature(OCL_RealType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_integertype_is_not_abstract():
    assert not inspect.isabstract(OCL_IntegerType)


def test_ocl_integertype_constructor_exists():
    assert callable(OCL_IntegerType.__init__)


def test_ocl_integertype_constructor_args():
    sig = inspect.signature(OCL_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_primitive_is_not_abstract():
    assert not inspect.isabstract(Primitive)


def test_primitive_constructor_exists():
    assert callable(Primitive.__init__)


def test_primitive_constructor_args():
    sig = inspect.signature(Primitive.__init__)
    params = list(sig.parameters.keys())



def test_ocl_numerictype_is_not_abstract():
    assert not inspect.isabstract(OCL_NumericType)


def test_ocl_numerictype_constructor_exists():
    assert callable(OCL_NumericType.__init__)


def test_ocl_numerictype_constructor_args():
    sig = inspect.signature(OCL_NumericType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_booleantype_is_not_abstract():
    assert not inspect.isabstract(OCL_BooleanType)


def test_ocl_booleantype_constructor_exists():
    assert callable(OCL_BooleanType.__init__)


def test_ocl_booleantype_constructor_args():
    sig = inspect.signature(OCL_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_stringtype_is_not_abstract():
    assert not inspect.isabstract(OCL_StringType)


def test_ocl_stringtype_constructor_exists():
    assert callable(OCL_StringType.__init__)


def test_ocl_stringtype_constructor_args():
    sig = inspect.signature(OCL_StringType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_primitive_is_not_abstract():
    assert not inspect.isabstract(OCL_Primitive)


def test_ocl_primitive_constructor_exists():
    assert callable(OCL_Primitive.__init__)


def test_ocl_primitive_constructor_args():
    sig = inspect.signature(OCL_Primitive.__init__)
    params = list(sig.parameters.keys())



def test_tupletypeattribute_is_not_abstract():
    assert not inspect.isabstract(TupleTypeAttribute)


def test_tupletypeattribute_constructor_exists():
    assert callable(TupleTypeAttribute.__init__)


def test_tupletypeattribute_constructor_args():
    sig = inspect.signature(TupleTypeAttribute.__init__)
    params = list(sig.parameters.keys())



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_settype_is_not_abstract():
    assert not inspect.isabstract(OCL_SetType)


def test_ocl_settype_constructor_exists():
    assert callable(OCL_SetType.__init__)


def test_ocl_settype_constructor_args():
    sig = inspect.signature(OCL_SetType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_bagtype_is_not_abstract():
    assert not inspect.isabstract(OCL_BagType)


def test_ocl_bagtype_constructor_exists():
    assert callable(OCL_BagType.__init__)


def test_ocl_bagtype_constructor_args():
    sig = inspect.signature(OCL_BagType.__init__)
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



def test_ocl_ocltype_is_not_abstract():
    assert not inspect.isabstract(OCL_OclType)


def test_ocl_ocltype_constructor_exists():
    assert callable(OCL_OclType.__init__)


def test_ocl_ocltype_constructor_args():
    sig = inspect.signature(OCL_OclType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_ocltype_has_name():
    assert hasattr(OCL_OclType, "name")
    descriptor = None
    for klass in OCL_OclType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_tupletype_is_not_abstract():
    assert not inspect.isabstract(OCL_TupleType)


def test_ocl_tupletype_constructor_exists():
    assert callable(OCL_TupleType.__init__)


def test_ocl_tupletype_constructor_args():
    sig = inspect.signature(OCL_TupleType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_parameter_is_not_abstract():
    assert not inspect.isabstract(OCL_Parameter)


def test_ocl_parameter_constructor_exists():
    assert callable(OCL_Parameter.__init__)


def test_ocl_parameter_constructor_args():
    sig = inspect.signature(OCL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_ocl_iterator_is_not_abstract():
    assert not inspect.isabstract(OCL_Iterator)


def test_ocl_iterator_constructor_exists():
    assert callable(OCL_Iterator.__init__)


def test_ocl_iterator_constructor_args():
    sig = inspect.signature(OCL_Iterator.__init__)
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



def test_ocl_collectiontype_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionType)


def test_ocl_collectiontype_constructor_exists():
    assert callable(OCL_CollectionType.__init__)


def test_ocl_collectiontype_constructor_args():
    sig = inspect.signature(OCL_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_ocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(OCL_VariableDeclaration)


def test_ocl_variabledeclaration_constructor_exists():
    assert callable(OCL_VariableDeclaration.__init__)


def test_ocl_variabledeclaration_constructor_args():
    sig = inspect.signature(OCL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_ocl_variabledeclaration_has_id():
    assert hasattr(OCL_VariableDeclaration, "id")
    descriptor = None
    for klass in OCL_VariableDeclaration.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ocl_variabledeclaration_has_varName():
    assert hasattr(OCL_VariableDeclaration, "varName")
    descriptor = None
    for klass in OCL_VariableDeclaration.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_ocl_ifexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IfExp)


def test_ocl_ifexp_constructor_exists():
    assert callable(OCL_IfExp.__init__)


def test_ocl_ifexp_constructor_args():
    sig = inspect.signature(OCL_IfExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_letexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LetExp)


def test_ocl_letexp_constructor_exists():
    assert callable(OCL_LetExp.__init__)


def test_ocl_letexp_constructor_args():
    sig = inspect.signature(OCL_LetExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_iteratorexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IteratorExp)


def test_ocl_iteratorexp_constructor_exists():
    assert callable(OCL_IteratorExp.__init__)


def test_ocl_iteratorexp_constructor_args():
    sig = inspect.signature(OCL_IteratorExp.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ocl_iteratorexp_has_name():
    assert hasattr(OCL_IteratorExp, "name")
    descriptor = None
    for klass in OCL_IteratorExp.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ocl_iterateexp_is_not_abstract():
    assert not inspect.isabstract(OCL_IterateExp)


def test_ocl_iterateexp_constructor_exists():
    assert callable(OCL_IterateExp.__init__)


def test_ocl_iterateexp_constructor_args():
    sig = inspect.signature(OCL_IterateExp.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_ocl_loopexp_is_not_abstract():
    assert not inspect.isabstract(OCL_LoopExp)


def test_ocl_loopexp_constructor_exists():
    assert callable(OCL_LoopExp.__init__)


def test_ocl_loopexp_constructor_args():
    sig = inspect.signature(OCL_LoopExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_CollectionOperationCallExp)


def test_ocl_collectionoperationcallexp_constructor_exists():
    assert callable(OCL_CollectionOperationCallExp.__init__)


def test_ocl_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(OCL_CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_ocl_operatorcallexp_is_not_abstract():
    assert not inspect.isabstract(OCL_OperatorCallExp)


def test_ocl_operatorcallexp_constructor_exists():
    assert callable(OCL_OperatorCallExp.__init__)


def test_ocl_operatorcallexp_constructor_args():
    sig = inspect.signature(OCL_OperatorCallExp.__init__)
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
NumericExp_strategy = st.builds(
    NumericExp,
)
OCL_IntegerExp_strategy = st.builds(
    OCL_IntegerExp,
    integerSymbol=
        safe_text
)
OCL_RealExp_strategy = st.builds(
    OCL_RealExp,
    realSymbol=
        safe_text
)
PrimitiveExp_strategy = st.builds(
    PrimitiveExp,
)
OCL_BooleanExp_strategy = st.builds(
    OCL_BooleanExp,
    booleanSymbol=
        safe_text
)
OCL_NumericExp_strategy = st.builds(
    OCL_NumericExp,
)
OCL_StringExp_strategy = st.builds(
    OCL_StringExp,
    stringSymbol=
        safe_text
)
Attribute_strategy = st.builds(
    Attribute,
)
Operation_strategy = st.builds(
    Operation,
)
OperationCallExp_strategy = st.builds(
    OperationCallExp,
)
LoopExp_strategy = st.builds(
    LoopExp,
)
LetExp_strategy = st.builds(
    LetExp,
)
CollectionExp_strategy = st.builds(
    CollectionExp,
)
OCL_SetExp_strategy = st.builds(
    OCL_SetExp,
)
OCL_SequenceExp_strategy = st.builds(
    OCL_SequenceExp,
)
OCL_BagExp_strategy = st.builds(
    OCL_BagExp,
)
OCL_OrderedSetExp_strategy = st.builds(
    OCL_OrderedSetExp,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
OCL_OperationCallExp_strategy = st.builds(
    OCL_OperationCallExp,
    operationName=
        safe_text
)
OCL_NavigationOrAttributeCallExp_strategy = st.builds(
    OCL_NavigationOrAttributeCallExp,
    name=
        safe_text
)
IfExp_strategy = st.builds(
    IfExp,
)
OclType_strategy = st.builds(
    OclType,
)
ocl_constraints_LocatedElement_strategy = st.builds(
    ocl_constraints_LocatedElement,
    location=
        safe_text,
    commentsAfter=
        safe_text,
    commentsBefore=
        safe_text
)
OclExpression_strategy = st.builds(
    OclExpression,
)
OCL_VariableExp_strategy = st.builds(
    OCL_VariableExp,
)
OCL_PrimitiveExp_strategy = st.builds(
    OCL_PrimitiveExp,
)
OCL_SuperExp_strategy = st.builds(
    OCL_SuperExp,
)
OCL_OclUndefinedExp_strategy = st.builds(
    OCL_OclUndefinedExp,
)
OCL_EnumLiteralExp_strategy = st.builds(
    OCL_EnumLiteralExp,
    name=
        safe_text
)
OCL_CollectionExp_strategy = st.builds(
    OCL_CollectionExp,
)
OCL_MapExp_strategy = st.builds(
    OCL_MapExp,
)
OCL_TupleExp_strategy = st.builds(
    OCL_TupleExp,
)
OCL_PropertyCallExp_strategy = st.builds(
    OCL_PropertyCallExp,
)
OclPrecondition_strategy = st.builds(
    OclPrecondition,
)
OclInvariant_strategy = st.builds(
    OclInvariant,
)
OclConstraintsModel_strategy = st.builds(
    OclConstraintsModel,
)
Metaclass_strategy = st.builds(
    Metaclass,
)
ocl_constraints_UMLClass_strategy = st.builds(
    ocl_constraints_UMLClass,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
OCL_TuplePart_strategy = st.builds(
    OCL_TuplePart,
)
Context_strategy = st.builds(
    Context,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
ocl_constraints_OclInvariant_strategy = st.builds(
    ocl_constraints_OclInvariant,
    description=
        safe_text,
    name=
        safe_text
)
ocl_constraints_OclPrecondition_strategy = st.builds(
    ocl_constraints_OclPrecondition,
    name=
        safe_text,
    description=
        safe_text
)
OCL_MapElement_strategy = st.builds(
    OCL_MapElement,
)
ocl_constraints_Context_strategy = st.builds(
    ocl_constraints_Context,
)
ocl_constraints_Metaclass_strategy = st.builds(
    ocl_constraints_Metaclass,
    name=
        safe_text
)
OCL_OclExpression_strategy = st.builds(
    OCL_OclExpression,
)
ocl_constraints_OclConstraintsModel_strategy = st.builds(
    ocl_constraints_OclConstraintsModel,
    metamodel=
        safe_text,
    name=
        safe_text
)
UMLClass_strategy = st.builds(
    UMLClass,
)
OclModelElement_strategy = st.builds(
    OclModelElement,
)
OCL_OclModel_strategy = st.builds(
    OCL_OclModel,
    name=
        safe_text
)
Parameter_strategy = st.builds(
    Parameter,
)
OCL_OclFeature_strategy = st.builds(
    OCL_OclFeature,
)
OclFeatureDefinition_strategy = st.builds(
    OclFeatureDefinition,
)
OCL_OclContextDefinition_strategy = st.builds(
    OCL_OclContextDefinition,
)
OclFeature_strategy = st.builds(
    OclFeature,
)
OCL_Attribute_strategy = st.builds(
    OCL_Attribute,
    name=
        safe_text
)
OCL_Operation_strategy = st.builds(
    OCL_Operation,
    name=
        safe_text
)
OCL_OclFeatureDefinition_strategy = st.builds(
    OCL_OclFeatureDefinition,
)
OCL_MapType_strategy = st.builds(
    OCL_MapType,
)
OclModel_strategy = st.builds(
    OclModel,
)
OCL_OclModelElement_strategy = st.builds(
    OCL_OclModelElement,
)
TupleType_strategy = st.builds(
    TupleType,
)
OCL_TupleTypeAttribute_strategy = st.builds(
    OCL_TupleTypeAttribute,
    name=
        safe_text
)
OCL_OclAnyType_strategy = st.builds(
    OCL_OclAnyType,
)
NumericType_strategy = st.builds(
    NumericType,
)
OCL_RealType_strategy = st.builds(
    OCL_RealType,
)
OCL_IntegerType_strategy = st.builds(
    OCL_IntegerType,
)
Primitive_strategy = st.builds(
    Primitive,
)
OCL_NumericType_strategy = st.builds(
    OCL_NumericType,
)
OCL_BooleanType_strategy = st.builds(
    OCL_BooleanType,
)
OCL_StringType_strategy = st.builds(
    OCL_StringType,
)
OCL_Primitive_strategy = st.builds(
    OCL_Primitive,
)
TupleTypeAttribute_strategy = st.builds(
    TupleTypeAttribute,
)
CollectionType_strategy = st.builds(
    CollectionType,
)
OCL_SetType_strategy = st.builds(
    OCL_SetType,
)
OCL_BagType_strategy = st.builds(
    OCL_BagType,
)
OCL_SequenceType_strategy = st.builds(
    OCL_SequenceType,
)
OCL_OrderedSetType_strategy = st.builds(
    OCL_OrderedSetType,
)
MapType_strategy = st.builds(
    MapType,
)
OclContextDefinition_strategy = st.builds(
    OclContextDefinition,
)
OCL_OclType_strategy = st.builds(
    OCL_OclType,
    name=
        safe_text
)
OCL_TupleType_strategy = st.builds(
    OCL_TupleType,
)
OCL_Parameter_strategy = st.builds(
    OCL_Parameter,
)
OCL_Iterator_strategy = st.builds(
    OCL_Iterator,
)
VariableExp_strategy = st.builds(
    VariableExp,
)
IterateExp_strategy = st.builds(
    IterateExp,
)
OCL_CollectionType_strategy = st.builds(
    OCL_CollectionType,
)
OCL_VariableDeclaration_strategy = st.builds(
    OCL_VariableDeclaration,
    id=
        safe_text,
    varName=
        safe_text
)
OCL_IfExp_strategy = st.builds(
    OCL_IfExp,
)
OCL_LetExp_strategy = st.builds(
    OCL_LetExp,
)
OCL_IteratorExp_strategy = st.builds(
    OCL_IteratorExp,
    name=
        safe_text
)
OCL_IterateExp_strategy = st.builds(
    OCL_IterateExp,
)
Iterator_strategy = st.builds(
    Iterator,
)
OCL_LoopExp_strategy = st.builds(
    OCL_LoopExp,
)
OCL_CollectionOperationCallExp_strategy = st.builds(
    OCL_CollectionOperationCallExp,
)
OCL_OperatorCallExp_strategy = st.builds(
    OCL_OperatorCallExp,
)

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

@given(instance=NumericExp_strategy)
@settings(max_examples=50)
def test_numericexp_instantiation(instance):
    assert isinstance(instance, NumericExp)

@given(instance=OCL_IntegerExp_strategy)
@settings(max_examples=50)
def test_ocl_integerexp_instantiation(instance):
    assert isinstance(instance, OCL_IntegerExp)



@given(instance=OCL_IntegerExp_strategy)
def test_ocl_integerexp_integerSymbol_setter(instance):
    original = instance.integerSymbol
    instance.integerSymbol = original
    assert instance.integerSymbol == original

@given(instance=OCL_RealExp_strategy)
@settings(max_examples=50)
def test_ocl_realexp_instantiation(instance):
    assert isinstance(instance, OCL_RealExp)



@given(instance=OCL_RealExp_strategy)
def test_ocl_realexp_realSymbol_setter(instance):
    original = instance.realSymbol
    instance.realSymbol = original
    assert instance.realSymbol == original

@given(instance=PrimitiveExp_strategy)
@settings(max_examples=50)
def test_primitiveexp_instantiation(instance):
    assert isinstance(instance, PrimitiveExp)

@given(instance=OCL_BooleanExp_strategy)
@settings(max_examples=50)
def test_ocl_booleanexp_instantiation(instance):
    assert isinstance(instance, OCL_BooleanExp)



@given(instance=OCL_BooleanExp_strategy)
def test_ocl_booleanexp_booleanSymbol_setter(instance):
    original = instance.booleanSymbol
    instance.booleanSymbol = original
    assert instance.booleanSymbol == original

@given(instance=OCL_NumericExp_strategy)
@settings(max_examples=50)
def test_ocl_numericexp_instantiation(instance):
    assert isinstance(instance, OCL_NumericExp)

@given(instance=OCL_StringExp_strategy)
@settings(max_examples=50)
def test_ocl_stringexp_instantiation(instance):
    assert isinstance(instance, OCL_StringExp)



@given(instance=OCL_StringExp_strategy)
def test_ocl_stringexp_stringSymbol_setter(instance):
    original = instance.stringSymbol
    instance.stringSymbol = original
    assert instance.stringSymbol == original

@given(instance=Attribute_strategy)
@settings(max_examples=50)
def test_attribute_instantiation(instance):
    assert isinstance(instance, Attribute)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=OperationCallExp_strategy)
@settings(max_examples=50)
def test_operationcallexp_instantiation(instance):
    assert isinstance(instance, OperationCallExp)

@given(instance=LoopExp_strategy)
@settings(max_examples=50)
def test_loopexp_instantiation(instance):
    assert isinstance(instance, LoopExp)

@given(instance=LetExp_strategy)
@settings(max_examples=50)
def test_letexp_instantiation(instance):
    assert isinstance(instance, LetExp)

@given(instance=CollectionExp_strategy)
@settings(max_examples=50)
def test_collectionexp_instantiation(instance):
    assert isinstance(instance, CollectionExp)

@given(instance=OCL_SetExp_strategy)
@settings(max_examples=50)
def test_ocl_setexp_instantiation(instance):
    assert isinstance(instance, OCL_SetExp)

@given(instance=OCL_SequenceExp_strategy)
@settings(max_examples=50)
def test_ocl_sequenceexp_instantiation(instance):
    assert isinstance(instance, OCL_SequenceExp)

@given(instance=OCL_BagExp_strategy)
@settings(max_examples=50)
def test_ocl_bagexp_instantiation(instance):
    assert isinstance(instance, OCL_BagExp)

@given(instance=OCL_OrderedSetExp_strategy)
@settings(max_examples=50)
def test_ocl_orderedsetexp_instantiation(instance):
    assert isinstance(instance, OCL_OrderedSetExp)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=OCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, OCL_OperationCallExp)



@given(instance=OCL_OperationCallExp_strategy)
def test_ocl_operationcallexp_operationName_setter(instance):
    original = instance.operationName
    instance.operationName = original
    assert instance.operationName == original

@given(instance=OCL_NavigationOrAttributeCallExp_strategy)
@settings(max_examples=50)
def test_ocl_navigationorattributecallexp_instantiation(instance):
    assert isinstance(instance, OCL_NavigationOrAttributeCallExp)



@given(instance=OCL_NavigationOrAttributeCallExp_strategy)
def test_ocl_navigationorattributecallexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=IfExp_strategy)
@settings(max_examples=50)
def test_ifexp_instantiation(instance):
    assert isinstance(instance, IfExp)

@given(instance=OclType_strategy)
@settings(max_examples=50)
def test_ocltype_instantiation(instance):
    assert isinstance(instance, OclType)

@given(instance=ocl_constraints_LocatedElement_strategy)
@settings(max_examples=50)
def test_ocl_constraints_locatedelement_instantiation(instance):
    assert isinstance(instance, ocl_constraints_LocatedElement)



@given(instance=ocl_constraints_LocatedElement_strategy)
def test_ocl_constraints_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=ocl_constraints_LocatedElement_strategy)
def test_ocl_constraints_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original



@given(instance=ocl_constraints_LocatedElement_strategy)
def test_ocl_constraints_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=OCL_VariableExp_strategy)
@settings(max_examples=50)
def test_ocl_variableexp_instantiation(instance):
    assert isinstance(instance, OCL_VariableExp)

@given(instance=OCL_PrimitiveExp_strategy)
@settings(max_examples=50)
def test_ocl_primitiveexp_instantiation(instance):
    assert isinstance(instance, OCL_PrimitiveExp)

@given(instance=OCL_SuperExp_strategy)
@settings(max_examples=50)
def test_ocl_superexp_instantiation(instance):
    assert isinstance(instance, OCL_SuperExp)

@given(instance=OCL_OclUndefinedExp_strategy)
@settings(max_examples=50)
def test_ocl_oclundefinedexp_instantiation(instance):
    assert isinstance(instance, OCL_OclUndefinedExp)

@given(instance=OCL_EnumLiteralExp_strategy)
@settings(max_examples=50)
def test_ocl_enumliteralexp_instantiation(instance):
    assert isinstance(instance, OCL_EnumLiteralExp)



@given(instance=OCL_EnumLiteralExp_strategy)
def test_ocl_enumliteralexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_CollectionExp_strategy)
@settings(max_examples=50)
def test_ocl_collectionexp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionExp)

@given(instance=OCL_MapExp_strategy)
@settings(max_examples=50)
def test_ocl_mapexp_instantiation(instance):
    assert isinstance(instance, OCL_MapExp)

@given(instance=OCL_TupleExp_strategy)
@settings(max_examples=50)
def test_ocl_tupleexp_instantiation(instance):
    assert isinstance(instance, OCL_TupleExp)

@given(instance=OCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, OCL_PropertyCallExp)

@given(instance=OclPrecondition_strategy)
@settings(max_examples=50)
def test_oclprecondition_instantiation(instance):
    assert isinstance(instance, OclPrecondition)

@given(instance=OclInvariant_strategy)
@settings(max_examples=50)
def test_oclinvariant_instantiation(instance):
    assert isinstance(instance, OclInvariant)

@given(instance=OclConstraintsModel_strategy)
@settings(max_examples=50)
def test_oclconstraintsmodel_instantiation(instance):
    assert isinstance(instance, OclConstraintsModel)

@given(instance=Metaclass_strategy)
@settings(max_examples=50)
def test_metaclass_instantiation(instance):
    assert isinstance(instance, Metaclass)

@given(instance=ocl_constraints_UMLClass_strategy)
@settings(max_examples=50)
def test_ocl_constraints_umlclass_instantiation(instance):
    assert isinstance(instance, ocl_constraints_UMLClass)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=OCL_TuplePart_strategy)
@settings(max_examples=50)
def test_ocl_tuplepart_instantiation(instance):
    assert isinstance(instance, OCL_TuplePart)

@given(instance=Context_strategy)
@settings(max_examples=50)
def test_context_instantiation(instance):
    assert isinstance(instance, Context)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=ocl_constraints_OclInvariant_strategy)
@settings(max_examples=50)
def test_ocl_constraints_oclinvariant_instantiation(instance):
    assert isinstance(instance, ocl_constraints_OclInvariant)



@given(instance=ocl_constraints_OclInvariant_strategy)
def test_ocl_constraints_oclinvariant_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=ocl_constraints_OclInvariant_strategy)
def test_ocl_constraints_oclinvariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ocl_constraints_OclPrecondition_strategy)
@settings(max_examples=50)
def test_ocl_constraints_oclprecondition_instantiation(instance):
    assert isinstance(instance, ocl_constraints_OclPrecondition)



@given(instance=ocl_constraints_OclPrecondition_strategy)
def test_ocl_constraints_oclprecondition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ocl_constraints_OclPrecondition_strategy)
def test_ocl_constraints_oclprecondition_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=OCL_MapElement_strategy)
@settings(max_examples=50)
def test_ocl_mapelement_instantiation(instance):
    assert isinstance(instance, OCL_MapElement)

@given(instance=ocl_constraints_Context_strategy)
@settings(max_examples=50)
def test_ocl_constraints_context_instantiation(instance):
    assert isinstance(instance, ocl_constraints_Context)

@given(instance=ocl_constraints_Metaclass_strategy)
@settings(max_examples=50)
def test_ocl_constraints_metaclass_instantiation(instance):
    assert isinstance(instance, ocl_constraints_Metaclass)



@given(instance=ocl_constraints_Metaclass_strategy)
def test_ocl_constraints_metaclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_OclExpression_strategy)
@settings(max_examples=50)
def test_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, OCL_OclExpression)

@given(instance=ocl_constraints_OclConstraintsModel_strategy)
@settings(max_examples=50)
def test_ocl_constraints_oclconstraintsmodel_instantiation(instance):
    assert isinstance(instance, ocl_constraints_OclConstraintsModel)



@given(instance=ocl_constraints_OclConstraintsModel_strategy)
def test_ocl_constraints_oclconstraintsmodel_metamodel_setter(instance):
    original = instance.metamodel
    instance.metamodel = original
    assert instance.metamodel == original



@given(instance=ocl_constraints_OclConstraintsModel_strategy)
def test_ocl_constraints_oclconstraintsmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UMLClass_strategy)
@settings(max_examples=50)
def test_umlclass_instantiation(instance):
    assert isinstance(instance, UMLClass)

@given(instance=OclModelElement_strategy)
@settings(max_examples=50)
def test_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OclModelElement)

@given(instance=OCL_OclModel_strategy)
@settings(max_examples=50)
def test_ocl_oclmodel_instantiation(instance):
    assert isinstance(instance, OCL_OclModel)



@given(instance=OCL_OclModel_strategy)
def test_ocl_oclmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=OCL_OclFeature_strategy)
@settings(max_examples=50)
def test_ocl_oclfeature_instantiation(instance):
    assert isinstance(instance, OCL_OclFeature)

@given(instance=OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OclFeatureDefinition)

@given(instance=OCL_OclContextDefinition_strategy)
@settings(max_examples=50)
def test_ocl_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OCL_OclContextDefinition)

@given(instance=OclFeature_strategy)
@settings(max_examples=50)
def test_oclfeature_instantiation(instance):
    assert isinstance(instance, OclFeature)

@given(instance=OCL_Attribute_strategy)
@settings(max_examples=50)
def test_ocl_attribute_instantiation(instance):
    assert isinstance(instance, OCL_Attribute)



@given(instance=OCL_Attribute_strategy)
def test_ocl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_Operation_strategy)
@settings(max_examples=50)
def test_ocl_operation_instantiation(instance):
    assert isinstance(instance, OCL_Operation)



@given(instance=OCL_Operation_strategy)
def test_ocl_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_OclFeatureDefinition_strategy)
@settings(max_examples=50)
def test_ocl_oclfeaturedefinition_instantiation(instance):
    assert isinstance(instance, OCL_OclFeatureDefinition)

@given(instance=OCL_MapType_strategy)
@settings(max_examples=50)
def test_ocl_maptype_instantiation(instance):
    assert isinstance(instance, OCL_MapType)

@given(instance=OclModel_strategy)
@settings(max_examples=50)
def test_oclmodel_instantiation(instance):
    assert isinstance(instance, OclModel)

@given(instance=OCL_OclModelElement_strategy)
@settings(max_examples=50)
def test_ocl_oclmodelelement_instantiation(instance):
    assert isinstance(instance, OCL_OclModelElement)

@given(instance=TupleType_strategy)
@settings(max_examples=50)
def test_tupletype_instantiation(instance):
    assert isinstance(instance, TupleType)

@given(instance=OCL_TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_ocl_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, OCL_TupleTypeAttribute)



@given(instance=OCL_TupleTypeAttribute_strategy)
def test_ocl_tupletypeattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_OclAnyType_strategy)
@settings(max_examples=50)
def test_ocl_oclanytype_instantiation(instance):
    assert isinstance(instance, OCL_OclAnyType)

@given(instance=NumericType_strategy)
@settings(max_examples=50)
def test_numerictype_instantiation(instance):
    assert isinstance(instance, NumericType)

@given(instance=OCL_RealType_strategy)
@settings(max_examples=50)
def test_ocl_realtype_instantiation(instance):
    assert isinstance(instance, OCL_RealType)

@given(instance=OCL_IntegerType_strategy)
@settings(max_examples=50)
def test_ocl_integertype_instantiation(instance):
    assert isinstance(instance, OCL_IntegerType)

@given(instance=Primitive_strategy)
@settings(max_examples=50)
def test_primitive_instantiation(instance):
    assert isinstance(instance, Primitive)

@given(instance=OCL_NumericType_strategy)
@settings(max_examples=50)
def test_ocl_numerictype_instantiation(instance):
    assert isinstance(instance, OCL_NumericType)

@given(instance=OCL_BooleanType_strategy)
@settings(max_examples=50)
def test_ocl_booleantype_instantiation(instance):
    assert isinstance(instance, OCL_BooleanType)

@given(instance=OCL_StringType_strategy)
@settings(max_examples=50)
def test_ocl_stringtype_instantiation(instance):
    assert isinstance(instance, OCL_StringType)

@given(instance=OCL_Primitive_strategy)
@settings(max_examples=50)
def test_ocl_primitive_instantiation(instance):
    assert isinstance(instance, OCL_Primitive)

@given(instance=TupleTypeAttribute_strategy)
@settings(max_examples=50)
def test_tupletypeattribute_instantiation(instance):
    assert isinstance(instance, TupleTypeAttribute)

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=OCL_SetType_strategy)
@settings(max_examples=50)
def test_ocl_settype_instantiation(instance):
    assert isinstance(instance, OCL_SetType)

@given(instance=OCL_BagType_strategy)
@settings(max_examples=50)
def test_ocl_bagtype_instantiation(instance):
    assert isinstance(instance, OCL_BagType)

@given(instance=OCL_SequenceType_strategy)
@settings(max_examples=50)
def test_ocl_sequencetype_instantiation(instance):
    assert isinstance(instance, OCL_SequenceType)

@given(instance=OCL_OrderedSetType_strategy)
@settings(max_examples=50)
def test_ocl_orderedsettype_instantiation(instance):
    assert isinstance(instance, OCL_OrderedSetType)

@given(instance=MapType_strategy)
@settings(max_examples=50)
def test_maptype_instantiation(instance):
    assert isinstance(instance, MapType)

@given(instance=OclContextDefinition_strategy)
@settings(max_examples=50)
def test_oclcontextdefinition_instantiation(instance):
    assert isinstance(instance, OclContextDefinition)

@given(instance=OCL_OclType_strategy)
@settings(max_examples=50)
def test_ocl_ocltype_instantiation(instance):
    assert isinstance(instance, OCL_OclType)



@given(instance=OCL_OclType_strategy)
def test_ocl_ocltype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_TupleType_strategy)
@settings(max_examples=50)
def test_ocl_tupletype_instantiation(instance):
    assert isinstance(instance, OCL_TupleType)

@given(instance=OCL_Parameter_strategy)
@settings(max_examples=50)
def test_ocl_parameter_instantiation(instance):
    assert isinstance(instance, OCL_Parameter)

@given(instance=OCL_Iterator_strategy)
@settings(max_examples=50)
def test_ocl_iterator_instantiation(instance):
    assert isinstance(instance, OCL_Iterator)

@given(instance=VariableExp_strategy)
@settings(max_examples=50)
def test_variableexp_instantiation(instance):
    assert isinstance(instance, VariableExp)

@given(instance=IterateExp_strategy)
@settings(max_examples=50)
def test_iterateexp_instantiation(instance):
    assert isinstance(instance, IterateExp)

@given(instance=OCL_CollectionType_strategy)
@settings(max_examples=50)
def test_ocl_collectiontype_instantiation(instance):
    assert isinstance(instance, OCL_CollectionType)

@given(instance=OCL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_ocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, OCL_VariableDeclaration)



@given(instance=OCL_VariableDeclaration_strategy)
def test_ocl_variabledeclaration_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=OCL_VariableDeclaration_strategy)
def test_ocl_variabledeclaration_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=OCL_IfExp_strategy)
@settings(max_examples=50)
def test_ocl_ifexp_instantiation(instance):
    assert isinstance(instance, OCL_IfExp)

@given(instance=OCL_LetExp_strategy)
@settings(max_examples=50)
def test_ocl_letexp_instantiation(instance):
    assert isinstance(instance, OCL_LetExp)

@given(instance=OCL_IteratorExp_strategy)
@settings(max_examples=50)
def test_ocl_iteratorexp_instantiation(instance):
    assert isinstance(instance, OCL_IteratorExp)



@given(instance=OCL_IteratorExp_strategy)
def test_ocl_iteratorexp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=OCL_IterateExp_strategy)
@settings(max_examples=50)
def test_ocl_iterateexp_instantiation(instance):
    assert isinstance(instance, OCL_IterateExp)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=OCL_LoopExp_strategy)
@settings(max_examples=50)
def test_ocl_loopexp_instantiation(instance):
    assert isinstance(instance, OCL_LoopExp)

@given(instance=OCL_CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_ocl_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, OCL_CollectionOperationCallExp)

@given(instance=OCL_OperatorCallExp_strategy)
@settings(max_examples=50)
def test_ocl_operatorcallexp_instantiation(instance):
    assert isinstance(instance, OCL_OperatorCallExp)
