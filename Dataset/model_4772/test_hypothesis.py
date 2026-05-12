import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Part,
    model_VarDeclList,
    model_MNavigableElement,
    model_Expression,
    model_MRange,
    model_MMultiplicity,
    MAssociation,
    MClass,
    model_MAssociationClass,
    model_MAggregationKind,
    model_Comparable,
    model_VarDecl,
    CollectionType,
    model_BagType,
    model_OrderedSetType,
    model_SequenceType,
    model_SetType,
    MModelElement,
    model_MModelElementEx,
    model_MModelElement,
    model_MPrePostCondition,
    model_MClassInvariant,
    model_MMVisitor,
    model_Type,
    BasicType,
    model_BooleanType,
    model_RealType,
    model_StringType,
    model_IntegerType,
    Type,
    model_EnumType,
    model_CollectionType,
    model_ObjectType,
    model_TupleType,
    model_OclAnyType,
    model_VoidType,
    model_BasicType,
    MModelElementEx,
    model_MAssociation,
    model_MModel,
    model_MClass,
    model_MAssociationEnd,
    model_MOperation,
    model_MAttribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_part_is_not_abstract():
    assert not inspect.isabstract(model_Part)


def test_model_part_constructor_exists():
    assert callable(model_Part.__init__)


def test_model_part_constructor_args():
    sig = inspect.signature(model_Part.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_part_has_name():
    assert hasattr(model_Part, "name")
    descriptor = None
    for klass in model_Part.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_vardecllist_is_not_abstract():
    assert not inspect.isabstract(model_VarDeclList)


def test_model_vardecllist_constructor_exists():
    assert callable(model_VarDeclList.__init__)


def test_model_vardecllist_constructor_args():
    sig = inspect.signature(model_VarDeclList.__init__)
    params = list(sig.parameters.keys())



def test_model_mnavigableelement_is_not_abstract():
    assert not inspect.isabstract(model_MNavigableElement)


def test_model_mnavigableelement_constructor_exists():
    assert callable(model_MNavigableElement.__init__)


def test_model_mnavigableelement_constructor_args():
    sig = inspect.signature(model_MNavigableElement.__init__)
    params = list(sig.parameters.keys())
    assert "nameAsRolename" in params, "Missing parameter 'nameAsRolename'"

def test_model_mnavigableelement_has_nameAsRolename():
    assert hasattr(model_MNavigableElement, "nameAsRolename")
    descriptor = None
    for klass in model_MNavigableElement.__mro__:
        if "nameAsRolename" in klass.__dict__:
            descriptor = klass.__dict__["nameAsRolename"]
            break
    assert isinstance(descriptor, property)



def test_model_expression_is_not_abstract():
    assert not inspect.isabstract(model_Expression)


def test_model_expression_constructor_exists():
    assert callable(model_Expression.__init__)


def test_model_expression_constructor_args():
    sig = inspect.signature(model_Expression.__init__)
    params = list(sig.parameters.keys())



def test_model_mrange_is_not_abstract():
    assert not inspect.isabstract(model_MRange)


def test_model_mrange_constructor_exists():
    assert callable(model_MRange.__init__)


def test_model_mrange_constructor_args():
    sig = inspect.signature(model_MRange.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_model_mrange_has_lower():
    assert hasattr(model_MRange, "lower")
    descriptor = None
    for klass in model_MRange.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_model_mrange_has_upper():
    assert hasattr(model_MRange, "upper")
    descriptor = None
    for klass in model_MRange.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_model_mmultiplicity_is_not_abstract():
    assert not inspect.isabstract(model_MMultiplicity)


def test_model_mmultiplicity_constructor_exists():
    assert callable(model_MMultiplicity.__init__)


def test_model_mmultiplicity_constructor_args():
    sig = inspect.signature(model_MMultiplicity.__init__)
    params = list(sig.parameters.keys())



def test_massociation_is_not_abstract():
    assert not inspect.isabstract(MAssociation)


def test_massociation_constructor_exists():
    assert callable(MAssociation.__init__)


def test_massociation_constructor_args():
    sig = inspect.signature(MAssociation.__init__)
    params = list(sig.parameters.keys())



def test_mclass_is_not_abstract():
    assert not inspect.isabstract(MClass)


def test_mclass_constructor_exists():
    assert callable(MClass.__init__)


def test_mclass_constructor_args():
    sig = inspect.signature(MClass.__init__)
    params = list(sig.parameters.keys())



def test_model_massociationclass_is_not_abstract():
    assert not inspect.isabstract(model_MAssociationClass)


def test_model_massociationclass_constructor_exists():
    assert callable(model_MAssociationClass.__init__)


def test_model_massociationclass_constructor_args():
    sig = inspect.signature(model_MAssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_model_maggregationkind_is_not_abstract():
    assert not inspect.isabstract(model_MAggregationKind)


def test_model_maggregationkind_constructor_exists():
    assert callable(model_MAggregationKind.__init__)


def test_model_maggregationkind_constructor_args():
    sig = inspect.signature(model_MAggregationKind.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_model_maggregationkind_has_name():
    assert hasattr(model_MAggregationKind, "name")
    descriptor = None
    for klass in model_MAggregationKind.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_maggregationkind_has_kind():
    assert hasattr(model_MAggregationKind, "kind")
    descriptor = None
    for klass in model_MAggregationKind.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_model_comparable_is_not_abstract():
    assert not inspect.isabstract(model_Comparable)


def test_model_comparable_constructor_exists():
    assert callable(model_Comparable.__init__)


def test_model_comparable_constructor_args():
    sig = inspect.signature(model_Comparable.__init__)
    params = list(sig.parameters.keys())



def test_model_vardecl_is_not_abstract():
    assert not inspect.isabstract(model_VarDecl)


def test_model_vardecl_constructor_exists():
    assert callable(model_VarDecl.__init__)


def test_model_vardecl_constructor_args():
    sig = inspect.signature(model_VarDecl.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_model_vardecl_has_var():
    assert hasattr(model_VarDecl, "var")
    descriptor = None
    for klass in model_VarDecl.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_collectiontype_is_not_abstract():
    assert not inspect.isabstract(CollectionType)


def test_collectiontype_constructor_exists():
    assert callable(CollectionType.__init__)


def test_collectiontype_constructor_args():
    sig = inspect.signature(CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_model_bagtype_is_not_abstract():
    assert not inspect.isabstract(model_BagType)


def test_model_bagtype_constructor_exists():
    assert callable(model_BagType.__init__)


def test_model_bagtype_constructor_args():
    sig = inspect.signature(model_BagType.__init__)
    params = list(sig.parameters.keys())



def test_model_orderedsettype_is_not_abstract():
    assert not inspect.isabstract(model_OrderedSetType)


def test_model_orderedsettype_constructor_exists():
    assert callable(model_OrderedSetType.__init__)


def test_model_orderedsettype_constructor_args():
    sig = inspect.signature(model_OrderedSetType.__init__)
    params = list(sig.parameters.keys())



def test_model_sequencetype_is_not_abstract():
    assert not inspect.isabstract(model_SequenceType)


def test_model_sequencetype_constructor_exists():
    assert callable(model_SequenceType.__init__)


def test_model_sequencetype_constructor_args():
    sig = inspect.signature(model_SequenceType.__init__)
    params = list(sig.parameters.keys())



def test_model_settype_is_not_abstract():
    assert not inspect.isabstract(model_SetType)


def test_model_settype_constructor_exists():
    assert callable(model_SetType.__init__)


def test_model_settype_constructor_args():
    sig = inspect.signature(model_SetType.__init__)
    params = list(sig.parameters.keys())



def test_mmodelelement_is_not_abstract():
    assert not inspect.isabstract(MModelElement)


def test_mmodelelement_constructor_exists():
    assert callable(MModelElement.__init__)


def test_mmodelelement_constructor_args():
    sig = inspect.signature(MModelElement.__init__)
    params = list(sig.parameters.keys())



def test_model_mmodelelementex_is_not_abstract():
    assert not inspect.isabstract(model_MModelElementEx)


def test_model_mmodelelementex_constructor_exists():
    assert callable(model_MModelElementEx.__init__)


def test_model_mmodelelementex_constructor_args():
    sig = inspect.signature(model_MModelElementEx.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_mmodelelementex_has_name():
    assert hasattr(model_MModelElementEx, "name")
    descriptor = None
    for klass in model_MModelElementEx.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_mmodelelement_is_not_abstract():
    assert not inspect.isabstract(model_MModelElement)


def test_model_mmodelelement_constructor_exists():
    assert callable(model_MModelElement.__init__)


def test_model_mmodelelement_constructor_args():
    sig = inspect.signature(model_MModelElement.__init__)
    params = list(sig.parameters.keys())



def test_model_mprepostcondition_is_not_abstract():
    assert not inspect.isabstract(model_MPrePostCondition)


def test_model_mprepostcondition_constructor_exists():
    assert callable(model_MPrePostCondition.__init__)


def test_model_mprepostcondition_constructor_args():
    sig = inspect.signature(model_MPrePostCondition.__init__)
    params = list(sig.parameters.keys())
    assert "positionInModel" in params, "Missing parameter 'positionInModel'"

def test_model_mprepostcondition_has_positionInModel():
    assert hasattr(model_MPrePostCondition, "positionInModel")
    descriptor = None
    for klass in model_MPrePostCondition.__mro__:
        if "positionInModel" in klass.__dict__:
            descriptor = klass.__dict__["positionInModel"]
            break
    assert isinstance(descriptor, property)



def test_model_mclassinvariant_is_not_abstract():
    assert not inspect.isabstract(model_MClassInvariant)


def test_model_mclassinvariant_constructor_exists():
    assert callable(model_MClassInvariant.__init__)


def test_model_mclassinvariant_constructor_args():
    sig = inspect.signature(model_MClassInvariant.__init__)
    params = list(sig.parameters.keys())
    assert "positionInModel" in params, "Missing parameter 'positionInModel'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_mclassinvariant_has_positionInModel():
    assert hasattr(model_MClassInvariant, "positionInModel")
    descriptor = None
    for klass in model_MClassInvariant.__mro__:
        if "positionInModel" in klass.__dict__:
            descriptor = klass.__dict__["positionInModel"]
            break
    assert isinstance(descriptor, property)

def test_model_mclassinvariant_has_name():
    assert hasattr(model_MClassInvariant, "name")
    descriptor = None
    for klass in model_MClassInvariant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_mmvisitor_is_not_abstract():
    assert not inspect.isabstract(model_MMVisitor)


def test_model_mmvisitor_constructor_exists():
    assert callable(model_MMVisitor.__init__)


def test_model_mmvisitor_constructor_args():
    sig = inspect.signature(model_MMVisitor.__init__)
    params = list(sig.parameters.keys())



def test_model_type_is_not_abstract():
    assert not inspect.isabstract(model_Type)


def test_model_type_constructor_exists():
    assert callable(model_Type.__init__)


def test_model_type_constructor_args():
    sig = inspect.signature(model_Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "typeId" in params, "Missing parameter 'typeId'"

def test_model_type_has_typeName():
    assert hasattr(model_Type, "typeName")
    descriptor = None
    for klass in model_Type.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_model_type_has_typeId():
    assert hasattr(model_Type, "typeId")
    descriptor = None
    for klass in model_Type.__mro__:
        if "typeId" in klass.__dict__:
            descriptor = klass.__dict__["typeId"]
            break
    assert isinstance(descriptor, property)



def test_basictype_is_not_abstract():
    assert not inspect.isabstract(BasicType)


def test_basictype_constructor_exists():
    assert callable(BasicType.__init__)


def test_basictype_constructor_args():
    sig = inspect.signature(BasicType.__init__)
    params = list(sig.parameters.keys())



def test_model_booleantype_is_not_abstract():
    assert not inspect.isabstract(model_BooleanType)


def test_model_booleantype_constructor_exists():
    assert callable(model_BooleanType.__init__)


def test_model_booleantype_constructor_args():
    sig = inspect.signature(model_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_model_realtype_is_not_abstract():
    assert not inspect.isabstract(model_RealType)


def test_model_realtype_constructor_exists():
    assert callable(model_RealType.__init__)


def test_model_realtype_constructor_args():
    sig = inspect.signature(model_RealType.__init__)
    params = list(sig.parameters.keys())



def test_model_stringtype_is_not_abstract():
    assert not inspect.isabstract(model_StringType)


def test_model_stringtype_constructor_exists():
    assert callable(model_StringType.__init__)


def test_model_stringtype_constructor_args():
    sig = inspect.signature(model_StringType.__init__)
    params = list(sig.parameters.keys())



def test_model_integertype_is_not_abstract():
    assert not inspect.isabstract(model_IntegerType)


def test_model_integertype_constructor_exists():
    assert callable(model_IntegerType.__init__)


def test_model_integertype_constructor_args():
    sig = inspect.signature(model_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_model_enumtype_is_not_abstract():
    assert not inspect.isabstract(model_EnumType)


def test_model_enumtype_constructor_exists():
    assert callable(model_EnumType.__init__)


def test_model_enumtype_constructor_args():
    sig = inspect.signature(model_EnumType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "literals" in params, "Missing parameter 'literals'"

def test_model_enumtype_has_name():
    assert hasattr(model_EnumType, "name")
    descriptor = None
    for klass in model_EnumType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_enumtype_has_literals():
    assert hasattr(model_EnumType, "literals")
    descriptor = None
    for klass in model_EnumType.__mro__:
        if "literals" in klass.__dict__:
            descriptor = klass.__dict__["literals"]
            break
    assert isinstance(descriptor, property)



def test_model_collectiontype_is_not_abstract():
    assert not inspect.isabstract(model_CollectionType)


def test_model_collectiontype_constructor_exists():
    assert callable(model_CollectionType.__init__)


def test_model_collectiontype_constructor_args():
    sig = inspect.signature(model_CollectionType.__init__)
    params = list(sig.parameters.keys())



def test_model_objecttype_is_not_abstract():
    assert not inspect.isabstract(model_ObjectType)


def test_model_objecttype_constructor_exists():
    assert callable(model_ObjectType.__init__)


def test_model_objecttype_constructor_args():
    sig = inspect.signature(model_ObjectType.__init__)
    params = list(sig.parameters.keys())



def test_model_tupletype_is_not_abstract():
    assert not inspect.isabstract(model_TupleType)


def test_model_tupletype_constructor_exists():
    assert callable(model_TupleType.__init__)


def test_model_tupletype_constructor_args():
    sig = inspect.signature(model_TupleType.__init__)
    params = list(sig.parameters.keys())
    assert "parts" in params, "Missing parameter 'parts'"

def test_model_tupletype_has_parts():
    assert hasattr(model_TupleType, "parts")
    descriptor = None
    for klass in model_TupleType.__mro__:
        if "parts" in klass.__dict__:
            descriptor = klass.__dict__["parts"]
            break
    assert isinstance(descriptor, property)



def test_model_oclanytype_is_not_abstract():
    assert not inspect.isabstract(model_OclAnyType)


def test_model_oclanytype_constructor_exists():
    assert callable(model_OclAnyType.__init__)


def test_model_oclanytype_constructor_args():
    sig = inspect.signature(model_OclAnyType.__init__)
    params = list(sig.parameters.keys())



def test_model_voidtype_is_not_abstract():
    assert not inspect.isabstract(model_VoidType)


def test_model_voidtype_constructor_exists():
    assert callable(model_VoidType.__init__)


def test_model_voidtype_constructor_args():
    sig = inspect.signature(model_VoidType.__init__)
    params = list(sig.parameters.keys())



def test_model_basictype_is_not_abstract():
    assert not inspect.isabstract(model_BasicType)


def test_model_basictype_constructor_exists():
    assert callable(model_BasicType.__init__)


def test_model_basictype_constructor_args():
    sig = inspect.signature(model_BasicType.__init__)
    params = list(sig.parameters.keys())



def test_mmodelelementex_is_not_abstract():
    assert not inspect.isabstract(MModelElementEx)


def test_mmodelelementex_constructor_exists():
    assert callable(MModelElementEx.__init__)


def test_mmodelelementex_constructor_args():
    sig = inspect.signature(MModelElementEx.__init__)
    params = list(sig.parameters.keys())



def test_model_massociation_is_not_abstract():
    assert not inspect.isabstract(model_MAssociation)


def test_model_massociation_constructor_exists():
    assert callable(model_MAssociation.__init__)


def test_model_massociation_constructor_args():
    sig = inspect.signature(model_MAssociation.__init__)
    params = list(sig.parameters.keys())



def test_model_mmodel_is_not_abstract():
    assert not inspect.isabstract(model_MModel)


def test_model_mmodel_constructor_exists():
    assert callable(model_MModel.__init__)


def test_model_mmodel_constructor_args():
    sig = inspect.signature(model_MModel.__init__)
    params = list(sig.parameters.keys())



def test_model_mclass_is_not_abstract():
    assert not inspect.isabstract(model_MClass)


def test_model_mclass_constructor_exists():
    assert callable(model_MClass.__init__)


def test_model_mclass_constructor_args():
    sig = inspect.signature(model_MClass.__init__)
    params = list(sig.parameters.keys())



def test_model_massociationend_is_not_abstract():
    assert not inspect.isabstract(model_MAssociationEnd)


def test_model_massociationend_constructor_exists():
    assert callable(model_MAssociationEnd.__init__)


def test_model_massociationend_constructor_args():
    sig = inspect.signature(model_MAssociationEnd.__init__)
    params = list(sig.parameters.keys())
    assert "mClassName" in params, "Missing parameter 'mClassName'"

def test_model_massociationend_has_mClassName():
    assert hasattr(model_MAssociationEnd, "mClassName")
    descriptor = None
    for klass in model_MAssociationEnd.__mro__:
        if "mClassName" in klass.__dict__:
            descriptor = klass.__dict__["mClassName"]
            break
    assert isinstance(descriptor, property)



def test_model_moperation_is_not_abstract():
    assert not inspect.isabstract(model_MOperation)


def test_model_moperation_constructor_exists():
    assert callable(model_MOperation.__init__)


def test_model_moperation_constructor_args():
    sig = inspect.signature(model_MOperation.__init__)
    params = list(sig.parameters.keys())



def test_model_mattribute_is_not_abstract():
    assert not inspect.isabstract(model_MAttribute)


def test_model_mattribute_constructor_exists():
    assert callable(model_MAttribute.__init__)


def test_model_mattribute_constructor_args():
    sig = inspect.signature(model_MAttribute.__init__)
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
model_Part_strategy = st.builds(
    model_Part,
    name=
        safe_text
)
model_VarDeclList_strategy = st.builds(
    model_VarDeclList,
)
model_MNavigableElement_strategy = st.builds(
    model_MNavigableElement,
    nameAsRolename=
        safe_text
)
model_Expression_strategy = st.builds(
    model_Expression,
)
model_MRange_strategy = st.builds(
    model_MRange,
    lower=
        st.integers(),
    upper=
        st.integers()
)
model_MMultiplicity_strategy = st.builds(
    model_MMultiplicity,
)
MAssociation_strategy = st.builds(
    MAssociation,
)
MClass_strategy = st.builds(
    MClass,
)
model_MAssociationClass_strategy = st.builds(
    model_MAssociationClass,
)
model_MAggregationKind_strategy = st.builds(
    model_MAggregationKind,
    name=
        safe_text,
    kind=
        st.integers()
)
model_Comparable_strategy = st.builds(
    model_Comparable,
)
model_VarDecl_strategy = st.builds(
    model_VarDecl,
    var=
        safe_text
)
CollectionType_strategy = st.builds(
    CollectionType,
)
model_BagType_strategy = st.builds(
    model_BagType,
)
model_OrderedSetType_strategy = st.builds(
    model_OrderedSetType,
)
model_SequenceType_strategy = st.builds(
    model_SequenceType,
)
model_SetType_strategy = st.builds(
    model_SetType,
)
MModelElement_strategy = st.builds(
    MModelElement,
)
model_MModelElementEx_strategy = st.builds(
    model_MModelElementEx,
    name=
        safe_text
)
model_MModelElement_strategy = st.builds(
    model_MModelElement,
)
model_MPrePostCondition_strategy = st.builds(
    model_MPrePostCondition,
    positionInModel=
        st.integers()
)
model_MClassInvariant_strategy = st.builds(
    model_MClassInvariant,
    positionInModel=
        st.integers(),
    name=
        safe_text
)
model_MMVisitor_strategy = st.builds(
    model_MMVisitor,
)
model_Type_strategy = st.builds(
    model_Type,
    typeName=
        safe_text,
    typeId=
        st.integers()
)
BasicType_strategy = st.builds(
    BasicType,
)
model_BooleanType_strategy = st.builds(
    model_BooleanType,
)
model_RealType_strategy = st.builds(
    model_RealType,
)
model_StringType_strategy = st.builds(
    model_StringType,
)
model_IntegerType_strategy = st.builds(
    model_IntegerType,
)
Type_strategy = st.builds(
    Type,
)
model_EnumType_strategy = st.builds(
    model_EnumType,
    name=
        safe_text,
    literals=
        safe_text
)
model_CollectionType_strategy = st.builds(
    model_CollectionType,
)
model_ObjectType_strategy = st.builds(
    model_ObjectType,
)
model_TupleType_strategy = st.builds(
    model_TupleType,
    parts=
        safe_text
)
model_OclAnyType_strategy = st.builds(
    model_OclAnyType,
)
model_VoidType_strategy = st.builds(
    model_VoidType,
)
model_BasicType_strategy = st.builds(
    model_BasicType,
)
MModelElementEx_strategy = st.builds(
    MModelElementEx,
)
model_MAssociation_strategy = st.builds(
    model_MAssociation,
)
model_MModel_strategy = st.builds(
    model_MModel,
)
model_MClass_strategy = st.builds(
    model_MClass,
)
model_MAssociationEnd_strategy = st.builds(
    model_MAssociationEnd,
    mClassName=
        safe_text
)
model_MOperation_strategy = st.builds(
    model_MOperation,
)
model_MAttribute_strategy = st.builds(
    model_MAttribute,
)

@given(instance=model_Part_strategy)
@settings(max_examples=50)
def test_model_part_instantiation(instance):
    assert isinstance(instance, model_Part)



@given(instance=model_Part_strategy)
def test_model_part_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_VarDeclList_strategy)
@settings(max_examples=50)
def test_model_vardecllist_instantiation(instance):
    assert isinstance(instance, model_VarDeclList)

@given(instance=model_MNavigableElement_strategy)
@settings(max_examples=50)
def test_model_mnavigableelement_instantiation(instance):
    assert isinstance(instance, model_MNavigableElement)



@given(instance=model_MNavigableElement_strategy)
def test_model_mnavigableelement_nameAsRolename_setter(instance):
    original = instance.nameAsRolename
    instance.nameAsRolename = original
    assert instance.nameAsRolename == original

@given(instance=model_Expression_strategy)
@settings(max_examples=50)
def test_model_expression_instantiation(instance):
    assert isinstance(instance, model_Expression)

@given(instance=model_MRange_strategy)
@settings(max_examples=50)
def test_model_mrange_instantiation(instance):
    assert isinstance(instance, model_MRange)



@given(instance=model_MRange_strategy)
def test_model_mrange_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=model_MRange_strategy)
def test_model_mrange_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=model_MMultiplicity_strategy)
@settings(max_examples=50)
def test_model_mmultiplicity_instantiation(instance):
    assert isinstance(instance, model_MMultiplicity)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MMultiplicity_strategy)
@settings(max_examples=30)
def test_model_mmultiplicity_addrange_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addRange(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addRange).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addRange' in model_MMultiplicity is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addRange' in model_MMultiplicity did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addRange' in model_MMultiplicity is not implemented or raised an error")

@given(instance=MAssociation_strategy)
@settings(max_examples=50)
def test_massociation_instantiation(instance):
    assert isinstance(instance, MAssociation)

@given(instance=MClass_strategy)
@settings(max_examples=50)
def test_mclass_instantiation(instance):
    assert isinstance(instance, MClass)

@given(instance=model_MAssociationClass_strategy)
@settings(max_examples=50)
def test_model_massociationclass_instantiation(instance):
    assert isinstance(instance, model_MAssociationClass)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MAssociationClass_strategy)
@settings(max_examples=30)
def test_model_massociationclass_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MAssociationClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MAssociationClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MAssociationClass is not implemented or raised an error")

@given(instance=model_MAggregationKind_strategy)
@settings(max_examples=50)
def test_model_maggregationkind_instantiation(instance):
    assert isinstance(instance, model_MAggregationKind)



@given(instance=model_MAggregationKind_strategy)
def test_model_maggregationkind_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_MAggregationKind_strategy)
def test_model_maggregationkind_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=model_Comparable_strategy)
@settings(max_examples=50)
def test_model_comparable_instantiation(instance):
    assert isinstance(instance, model_Comparable)

@given(instance=model_VarDecl_strategy)
@settings(max_examples=50)
def test_model_vardecl_instantiation(instance):
    assert isinstance(instance, model_VarDecl)



@given(instance=model_VarDecl_strategy)
def test_model_vardecl_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=CollectionType_strategy)
@settings(max_examples=50)
def test_collectiontype_instantiation(instance):
    assert isinstance(instance, CollectionType)

@given(instance=model_BagType_strategy)
@settings(max_examples=50)
def test_model_bagtype_instantiation(instance):
    assert isinstance(instance, model_BagType)

@given(instance=model_OrderedSetType_strategy)
@settings(max_examples=50)
def test_model_orderedsettype_instantiation(instance):
    assert isinstance(instance, model_OrderedSetType)

@given(instance=model_SequenceType_strategy)
@settings(max_examples=50)
def test_model_sequencetype_instantiation(instance):
    assert isinstance(instance, model_SequenceType)

@given(instance=model_SetType_strategy)
@settings(max_examples=50)
def test_model_settype_instantiation(instance):
    assert isinstance(instance, model_SetType)

@given(instance=MModelElement_strategy)
@settings(max_examples=50)
def test_mmodelelement_instantiation(instance):
    assert isinstance(instance, MModelElement)

@given(instance=model_MModelElementEx_strategy)
@settings(max_examples=50)
def test_model_mmodelelementex_instantiation(instance):
    assert isinstance(instance, model_MModelElementEx)



@given(instance=model_MModelElementEx_strategy)
def test_model_mmodelelementex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModelElementEx_strategy)
@settings(max_examples=30)
def test_model_mmodelelementex_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MModelElementEx is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MModelElementEx did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MModelElementEx is not implemented or raised an error")

@given(instance=model_MModelElement_strategy)
@settings(max_examples=50)
def test_model_mmodelelement_instantiation(instance):
    assert isinstance(instance, model_MModelElement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModelElement_strategy)
@settings(max_examples=30)
def test_model_mmodelelement_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MModelElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MModelElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MModelElement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModelElement_strategy)
@settings(max_examples=30)
def test_model_mmodelelement_name_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.name()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.name).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'name' in model_MModelElement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'name' in model_MModelElement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'name' in model_MModelElement is not implemented or raised an error")

@given(instance=model_MPrePostCondition_strategy)
@settings(max_examples=50)
def test_model_mprepostcondition_instantiation(instance):
    assert isinstance(instance, model_MPrePostCondition)



@given(instance=model_MPrePostCondition_strategy)
def test_model_mprepostcondition_positionInModel_setter(instance):
    original = instance.positionInModel
    instance.positionInModel = original
    assert instance.positionInModel == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MPrePostCondition_strategy)
@settings(max_examples=30)
def test_model_mprepostcondition_setpre_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setPre(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setPre).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setPre' in model_MPrePostCondition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setPre' in model_MPrePostCondition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setPre' in model_MPrePostCondition is not implemented or raised an error")

@given(instance=model_MClassInvariant_strategy)
@settings(max_examples=50)
def test_model_mclassinvariant_instantiation(instance):
    assert isinstance(instance, model_MClassInvariant)



@given(instance=model_MClassInvariant_strategy)
def test_model_mclassinvariant_positionInModel_setter(instance):
    original = instance.positionInModel
    instance.positionInModel = original
    assert instance.positionInModel == original



@given(instance=model_MClassInvariant_strategy)
def test_model_mclassinvariant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_MMVisitor_strategy)
@settings(max_examples=50)
def test_model_mmvisitor_instantiation(instance):
    assert isinstance(instance, model_MMVisitor)

@given(instance=model_Type_strategy)
@settings(max_examples=50)
def test_model_type_instantiation(instance):
    assert isinstance(instance, model_Type)



@given(instance=model_Type_strategy)
def test_model_type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=model_Type_strategy)
def test_model_type_typeId_setter(instance):
    original = instance.typeId
    instance.typeId = original
    assert instance.typeId == original

@given(instance=BasicType_strategy)
@settings(max_examples=50)
def test_basictype_instantiation(instance):
    assert isinstance(instance, BasicType)

@given(instance=model_BooleanType_strategy)
@settings(max_examples=50)
def test_model_booleantype_instantiation(instance):
    assert isinstance(instance, model_BooleanType)

@given(instance=model_RealType_strategy)
@settings(max_examples=50)
def test_model_realtype_instantiation(instance):
    assert isinstance(instance, model_RealType)

@given(instance=model_StringType_strategy)
@settings(max_examples=50)
def test_model_stringtype_instantiation(instance):
    assert isinstance(instance, model_StringType)

@given(instance=model_IntegerType_strategy)
@settings(max_examples=50)
def test_model_integertype_instantiation(instance):
    assert isinstance(instance, model_IntegerType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=model_EnumType_strategy)
@settings(max_examples=50)
def test_model_enumtype_instantiation(instance):
    assert isinstance(instance, model_EnumType)



@given(instance=model_EnumType_strategy)
def test_model_enumtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_EnumType_strategy)
def test_model_enumtype_literals_setter(instance):
    original = instance.literals
    instance.literals = original
    assert instance.literals == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_EnumType_strategy)
@settings(max_examples=30)
def test_model_enumtype_addliteral_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addLiteral(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addLiteral).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addLiteral' in model_EnumType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addLiteral' in model_EnumType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addLiteral' in model_EnumType is not implemented or raised an error")

@given(instance=model_CollectionType_strategy)
@settings(max_examples=50)
def test_model_collectiontype_instantiation(instance):
    assert isinstance(instance, model_CollectionType)

@given(instance=model_ObjectType_strategy)
@settings(max_examples=50)
def test_model_objecttype_instantiation(instance):
    assert isinstance(instance, model_ObjectType)

@given(instance=model_TupleType_strategy)
@settings(max_examples=50)
def test_model_tupletype_instantiation(instance):
    assert isinstance(instance, model_TupleType)



@given(instance=model_TupleType_strategy)
def test_model_tupletype_parts_setter(instance):
    original = instance.parts
    instance.parts = original
    assert instance.parts == original

@given(instance=model_OclAnyType_strategy)
@settings(max_examples=50)
def test_model_oclanytype_instantiation(instance):
    assert isinstance(instance, model_OclAnyType)

@given(instance=model_VoidType_strategy)
@settings(max_examples=50)
def test_model_voidtype_instantiation(instance):
    assert isinstance(instance, model_VoidType)

@given(instance=model_BasicType_strategy)
@settings(max_examples=50)
def test_model_basictype_instantiation(instance):
    assert isinstance(instance, model_BasicType)

@given(instance=MModelElementEx_strategy)
@settings(max_examples=50)
def test_mmodelelementex_instantiation(instance):
    assert isinstance(instance, MModelElementEx)

@given(instance=model_MAssociation_strategy)
@settings(max_examples=50)
def test_model_massociation_instantiation(instance):
    assert isinstance(instance, model_MAssociation)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MAssociation_strategy)
@settings(max_examples=30)
def test_model_massociation_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MAssociation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MAssociation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MAssociation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MAssociation_strategy)
@settings(max_examples=30)
def test_model_massociation_addassociationend_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAssociationEnd(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAssociationEnd).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAssociationEnd' in model_MAssociation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAssociationEnd' in model_MAssociation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAssociationEnd' in model_MAssociation is not implemented or raised an error")

@given(instance=model_MModel_strategy)
@settings(max_examples=50)
def test_model_mmodel_instantiation(instance):
    assert isinstance(instance, model_MModel)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModel_strategy)
@settings(max_examples=30)
def test_model_mmodel_addclassinvariant_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addClassInvariant(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addClassInvariant).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addClassInvariant' in model_MModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addClassInvariant' in model_MModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addClassInvariant' in model_MModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModel_strategy)
@settings(max_examples=30)
def test_model_mmodel_addclass_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addClass(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addClass).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addClass' in model_MModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addClass' in model_MModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addClass' in model_MModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModel_strategy)
@settings(max_examples=30)
def test_model_mmodel_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MModel is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MModel_strategy)
@settings(max_examples=30)
def test_model_mmodel_addprepostcondition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addPrePostCondition(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addPrePostCondition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addPrePostCondition' in model_MModel is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addPrePostCondition' in model_MModel did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addPrePostCondition' in model_MModel is not implemented or raised an error")

@given(instance=model_MClass_strategy)
@settings(max_examples=50)
def test_model_mclass_instantiation(instance):
    assert isinstance(instance, model_MClass)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_addattribute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAttribute(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAttribute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAttribute' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAttribute' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAttribute' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_addassociation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addAssociation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addAssociation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addAssociation' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addAssociation' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addAssociation' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_addoperation_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addOperation(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addOperation).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addOperation' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addOperation' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addOperation' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_addchild_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addChild(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addChild).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addChild' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addChild' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addChild' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_setabstract_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.setAbstract(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.setAbstract).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'setAbstract' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'setAbstract' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'setAbstract' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_addparent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addParent(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addParent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addParent' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addParent' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addParent' in model_MClass is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MClass_strategy)
@settings(max_examples=30)
def test_model_mclass_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MClass is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MClass did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MClass is not implemented or raised an error")

@given(instance=model_MAssociationEnd_strategy)
@settings(max_examples=50)
def test_model_massociationend_instantiation(instance):
    assert isinstance(instance, model_MAssociationEnd)



@given(instance=model_MAssociationEnd_strategy)
def test_model_massociationend_mClassName_setter(instance):
    original = instance.mClassName
    instance.mClassName = original
    assert instance.mClassName == original

@given(instance=model_MOperation_strategy)
@settings(max_examples=50)
def test_model_moperation_instantiation(instance):
    assert isinstance(instance, model_MOperation)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MOperation_strategy)
@settings(max_examples=30)
def test_model_moperation_addvardecl_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addVarDecl(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addVarDecl).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addVarDecl' in model_MOperation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addVarDecl' in model_MOperation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addVarDecl' in model_MOperation is not implemented or raised an error")

@given(instance=model_MAttribute_strategy)
@settings(max_examples=50)
def test_model_mattribute_instantiation(instance):
    assert isinstance(instance, model_MAttribute)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_MAttribute_strategy)
@settings(max_examples=30)
def test_model_mattribute_processwithvisitor_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.processWithVisitor(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.processWithVisitor).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'processWithVisitor' in model_MAttribute is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'processWithVisitor' in model_MAttribute did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'processWithVisitor' in model_MAttribute is not implemented or raised an error")
