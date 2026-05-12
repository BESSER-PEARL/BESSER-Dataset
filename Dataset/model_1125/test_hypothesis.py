import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cjsidl_taggedItemDef,
    cjsidl_valueSpec,
    containerDef,
    cjsidl_formatEnumDef,
    cjsidl_valueRange,
    cjsidl_scaledRangeDef,
    cjsidl_subField,
    cjsidl_taggedUnitsEnum,
    cjsidl_valueSetDef,
    cjsidl_declaredEventDef,
    cjsidl_scopedType,
    cjsidl_scopedConstId,
    cjsidl_constReference,
    cjsidl_footerScopedRef,
    cjsidl_footerRef,
    cjsidl_bodyScopedRef,
    cjsidl_bodyRef,
    cjsidl_headerScopedRef,
    cjsidl_headerRef,
    cjsidl_containerRef,
    cjsidl_containerDef,
    cjsidl_footerDef,
    cjsidl_bodyDef,
    cjsidl_headerDef,
    cjsidl_varFormatField,
    cjsidl_varLenField,
    cjsidl_varLenString,
    cjsidl_fixedLenString,
    cjsidl_bitfieldDef,
    cjsidl_action,
    cjsidl_varField,
    cjsidl_fixedFieldDef,
    cjsidl_sequenceDef,
    cjsidl_variantDef,
    cjsidl_listDef,
    cjsidl_recordDef,
    cjsidl_arrayDef,
    cjsidl_simpleNumericType,
    cjsidl_simpleTransition,
    cjsidl_internalTransition,
    cjsidl_guardAction,
    cjsidl_guardParam,
    cjsidl_popTransition,
    cjsidl_pushTransition,
    cjsidl_nextState,
    cjsidl_sendActionList,
    cjsidl_actionList,
    cjsidl_defaultTransition,
    cjsidl_guard,
    cjsidl_scopedEventType,
    cjsidl_transParam,
    cjsidl_transParams,
    cjsidl_stateMachine,
    cjsidl_eventDef,
    cjsidl_transition,
    cjsidl_exit,
    cjsidl_entry,
    cjsidl_defaultState,
    cjsidl_state,
    cjsidl_startState,
    cjsidl_constDef,
    cjsidl_declaredConstSetRef,
    cjsidl_messageScopedRef,
    cjsidl_messageRef,
    cjsidl_messageDef,
    cjsidl_messages,
    cjsidl_scopedTypeId,
    cjsidl_typeReference,
    cjsidl_typeDef,
    cjsidl_declaredTypeSetRef,
    cjsidl_serviceDef,
    cjsidl_EObject,
    cjsidl_jaus,
    cjsidl_refAttr,
    cjsidl_protocolBehavior,
    cjsidl_internalEventSet,
    cjsidl_messageSet,
    cjsidl_declaredTypeSet,
    cjsidl_declaredConstSet,
    cjsidl_references,
    cjsidl_description,
    FIELD_FORMAT,
    UNIT,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cjsidl_taggeditemdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_taggedItemDef)


def test_cjsidl_taggeditemdef_constructor_exists():
    assert callable(cjsidl_taggedItemDef.__init__)


def test_cjsidl_taggeditemdef_constructor_args():
    sig = inspect.signature(cjsidl_taggedItemDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_valuespec_is_not_abstract():
    assert not inspect.isabstract(cjsidl_valueSpec)


def test_cjsidl_valuespec_constructor_exists():
    assert callable(cjsidl_valueSpec.__init__)


def test_cjsidl_valuespec_constructor_args():
    sig = inspect.signature(cjsidl_valueSpec.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_valuespec_has_value():
    assert hasattr(cjsidl_valueSpec, "value")
    descriptor = None
    for klass in cjsidl_valueSpec.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuespec_has_comment():
    assert hasattr(cjsidl_valueSpec, "comment")
    descriptor = None
    for klass in cjsidl_valueSpec.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuespec_has_name():
    assert hasattr(cjsidl_valueSpec, "name")
    descriptor = None
    for klass in cjsidl_valueSpec.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_containerdef_is_not_abstract():
    assert not inspect.isabstract(containerDef)


def test_containerdef_constructor_exists():
    assert callable(containerDef.__init__)


def test_containerdef_constructor_args():
    sig = inspect.signature(containerDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_formatenumdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_formatEnumDef)


def test_cjsidl_formatenumdef_constructor_exists():
    assert callable(cjsidl_formatEnumDef.__init__)


def test_cjsidl_formatenumdef_constructor_args():
    sig = inspect.signature(cjsidl_formatEnumDef.__init__)
    params = list(sig.parameters.keys())
    assert "fieldFormat" in params, "Missing parameter 'fieldFormat'"
    assert "index" in params, "Missing parameter 'index'"
    assert "fieldFormatStr" in params, "Missing parameter 'fieldFormatStr'"

def test_cjsidl_formatenumdef_has_fieldFormat():
    assert hasattr(cjsidl_formatEnumDef, "fieldFormat")
    descriptor = None
    for klass in cjsidl_formatEnumDef.__mro__:
        if "fieldFormat" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormat"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_formatenumdef_has_index():
    assert hasattr(cjsidl_formatEnumDef, "index")
    descriptor = None
    for klass in cjsidl_formatEnumDef.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_formatenumdef_has_fieldFormatStr():
    assert hasattr(cjsidl_formatEnumDef, "fieldFormatStr")
    descriptor = None
    for klass in cjsidl_formatEnumDef.__mro__:
        if "fieldFormatStr" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormatStr"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_valuerange_is_not_abstract():
    assert not inspect.isabstract(cjsidl_valueRange)


def test_cjsidl_valuerange_constructor_exists():
    assert callable(cjsidl_valueRange.__init__)


def test_cjsidl_valuerange_constructor_args():
    sig = inspect.signature(cjsidl_valueRange.__init__)
    params = list(sig.parameters.keys())
    assert "upperLimit_type" in params, "Missing parameter 'upperLimit_type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"
    assert "lowerLimit_type" in params, "Missing parameter 'lowerLimit_type'"

def test_cjsidl_valuerange_has_upperLimit_type():
    assert hasattr(cjsidl_valueRange, "upperLimit_type")
    descriptor = None
    for klass in cjsidl_valueRange.__mro__:
        if "upperLimit_type" in klass.__dict__:
            descriptor = klass.__dict__["upperLimit_type"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuerange_has_comment():
    assert hasattr(cjsidl_valueRange, "comment")
    descriptor = None
    for klass in cjsidl_valueRange.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuerange_has_upperLim():
    assert hasattr(cjsidl_valueRange, "upperLim")
    descriptor = None
    for klass in cjsidl_valueRange.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuerange_has_lowerLim():
    assert hasattr(cjsidl_valueRange, "lowerLim")
    descriptor = None
    for klass in cjsidl_valueRange.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_valuerange_has_lowerLimit_type():
    assert hasattr(cjsidl_valueRange, "lowerLimit_type")
    descriptor = None
    for klass in cjsidl_valueRange.__mro__:
        if "lowerLimit_type" in klass.__dict__:
            descriptor = klass.__dict__["lowerLimit_type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_scaledrangedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_scaledRangeDef)


def test_cjsidl_scaledrangedef_constructor_exists():
    assert callable(cjsidl_scaledRangeDef.__init__)


def test_cjsidl_scaledrangedef_constructor_args():
    sig = inspect.signature(cjsidl_scaledRangeDef.__init__)
    params = list(sig.parameters.keys())
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "function" in params, "Missing parameter 'function'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"
    assert "interp" in params, "Missing parameter 'interp'"

def test_cjsidl_scaledrangedef_has_upperLim():
    assert hasattr(cjsidl_scaledRangeDef, "upperLim")
    descriptor = None
    for klass in cjsidl_scaledRangeDef.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_scaledrangedef_has_function():
    assert hasattr(cjsidl_scaledRangeDef, "function")
    descriptor = None
    for klass in cjsidl_scaledRangeDef.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_scaledrangedef_has_lowerLim():
    assert hasattr(cjsidl_scaledRangeDef, "lowerLim")
    descriptor = None
    for klass in cjsidl_scaledRangeDef.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_scaledrangedef_has_interp():
    assert hasattr(cjsidl_scaledRangeDef, "interp")
    descriptor = None
    for klass in cjsidl_scaledRangeDef.__mro__:
        if "interp" in klass.__dict__:
            descriptor = klass.__dict__["interp"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_subfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl_subField)


def test_cjsidl_subfield_constructor_exists():
    assert callable(cjsidl_subField.__init__)


def test_cjsidl_subfield_constructor_args():
    sig = inspect.signature(cjsidl_subField.__init__)
    params = list(sig.parameters.keys())
    assert "toIndex" in params, "Missing parameter 'toIndex'"
    assert "fromIndex" in params, "Missing parameter 'fromIndex'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_subfield_has_toIndex():
    assert hasattr(cjsidl_subField, "toIndex")
    descriptor = None
    for klass in cjsidl_subField.__mro__:
        if "toIndex" in klass.__dict__:
            descriptor = klass.__dict__["toIndex"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_subfield_has_fromIndex():
    assert hasattr(cjsidl_subField, "fromIndex")
    descriptor = None
    for klass in cjsidl_subField.__mro__:
        if "fromIndex" in klass.__dict__:
            descriptor = klass.__dict__["fromIndex"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_subfield_has_comment():
    assert hasattr(cjsidl_subField, "comment")
    descriptor = None
    for klass in cjsidl_subField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_subfield_has_name():
    assert hasattr(cjsidl_subField, "name")
    descriptor = None
    for klass in cjsidl_subField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_taggedunitsenum_is_not_abstract():
    assert not inspect.isabstract(cjsidl_taggedUnitsEnum)


def test_cjsidl_taggedunitsenum_constructor_exists():
    assert callable(cjsidl_taggedUnitsEnum.__init__)


def test_cjsidl_taggedunitsenum_constructor_args():
    sig = inspect.signature(cjsidl_taggedUnitsEnum.__init__)
    params = list(sig.parameters.keys())
    assert "fieldUnit" in params, "Missing parameter 'fieldUnit'"
    assert "const_tag" in params, "Missing parameter 'const_tag'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_taggedunitsenum_has_fieldUnit():
    assert hasattr(cjsidl_taggedUnitsEnum, "fieldUnit")
    descriptor = None
    for klass in cjsidl_taggedUnitsEnum.__mro__:
        if "fieldUnit" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnit"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_taggedunitsenum_has_const_tag():
    assert hasattr(cjsidl_taggedUnitsEnum, "const_tag")
    descriptor = None
    for klass in cjsidl_taggedUnitsEnum.__mro__:
        if "const_tag" in klass.__dict__:
            descriptor = klass.__dict__["const_tag"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_taggedunitsenum_has_name():
    assert hasattr(cjsidl_taggedUnitsEnum, "name")
    descriptor = None
    for klass in cjsidl_taggedUnitsEnum.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_valuesetdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_valueSetDef)


def test_cjsidl_valuesetdef_constructor_exists():
    assert callable(cjsidl_valueSetDef.__init__)


def test_cjsidl_valuesetdef_constructor_args():
    sig = inspect.signature(cjsidl_valueSetDef.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"

def test_cjsidl_valuesetdef_has_offset():
    assert hasattr(cjsidl_valueSetDef, "offset")
    descriptor = None
    for klass in cjsidl_valueSetDef.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_declaredeventdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_declaredEventDef)


def test_cjsidl_declaredeventdef_constructor_exists():
    assert callable(cjsidl_declaredEventDef.__init__)


def test_cjsidl_declaredeventdef_constructor_args():
    sig = inspect.signature(cjsidl_declaredEventDef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_declaredeventdef_has_comment():
    assert hasattr(cjsidl_declaredEventDef, "comment")
    descriptor = None
    for klass in cjsidl_declaredEventDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredeventdef_has_name():
    assert hasattr(cjsidl_declaredEventDef, "name")
    descriptor = None
    for klass in cjsidl_declaredEventDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_scopedtype_is_not_abstract():
    assert not inspect.isabstract(cjsidl_scopedType)


def test_cjsidl_scopedtype_constructor_exists():
    assert callable(cjsidl_scopedType.__init__)


def test_cjsidl_scopedtype_constructor_args():
    sig = inspect.signature(cjsidl_scopedType.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_scopedconstid_is_not_abstract():
    assert not inspect.isabstract(cjsidl_scopedConstId)


def test_cjsidl_scopedconstid_constructor_exists():
    assert callable(cjsidl_scopedConstId.__init__)


def test_cjsidl_scopedconstid_constructor_args():
    sig = inspect.signature(cjsidl_scopedConstId.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_constreference_is_not_abstract():
    assert not inspect.isabstract(cjsidl_constReference)


def test_cjsidl_constreference_constructor_exists():
    assert callable(cjsidl_constReference.__init__)


def test_cjsidl_constreference_constructor_args():
    sig = inspect.signature(cjsidl_constReference.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_constreference_has_comment():
    assert hasattr(cjsidl_constReference, "comment")
    descriptor = None
    for klass in cjsidl_constReference.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_footerscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_footerScopedRef)


def test_cjsidl_footerscopedref_constructor_exists():
    assert callable(cjsidl_footerScopedRef.__init__)


def test_cjsidl_footerscopedref_constructor_args():
    sig = inspect.signature(cjsidl_footerScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_footerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_footerRef)


def test_cjsidl_footerref_constructor_exists():
    assert callable(cjsidl_footerRef.__init__)


def test_cjsidl_footerref_constructor_args():
    sig = inspect.signature(cjsidl_footerRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_footerref_has_name():
    assert hasattr(cjsidl_footerRef, "name")
    descriptor = None
    for klass in cjsidl_footerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_footerref_has_comment():
    assert hasattr(cjsidl_footerRef, "comment")
    descriptor = None
    for klass in cjsidl_footerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_bodyscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_bodyScopedRef)


def test_cjsidl_bodyscopedref_constructor_exists():
    assert callable(cjsidl_bodyScopedRef.__init__)


def test_cjsidl_bodyscopedref_constructor_args():
    sig = inspect.signature(cjsidl_bodyScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_bodyref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_bodyRef)


def test_cjsidl_bodyref_constructor_exists():
    assert callable(cjsidl_bodyRef.__init__)


def test_cjsidl_bodyref_constructor_args():
    sig = inspect.signature(cjsidl_bodyRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_bodyref_has_comment():
    assert hasattr(cjsidl_bodyRef, "comment")
    descriptor = None
    for klass in cjsidl_bodyRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_bodyref_has_name():
    assert hasattr(cjsidl_bodyRef, "name")
    descriptor = None
    for klass in cjsidl_bodyRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_headerscopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_headerScopedRef)


def test_cjsidl_headerscopedref_constructor_exists():
    assert callable(cjsidl_headerScopedRef.__init__)


def test_cjsidl_headerscopedref_constructor_args():
    sig = inspect.signature(cjsidl_headerScopedRef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_headerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_headerRef)


def test_cjsidl_headerref_constructor_exists():
    assert callable(cjsidl_headerRef.__init__)


def test_cjsidl_headerref_constructor_args():
    sig = inspect.signature(cjsidl_headerRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_headerref_has_name():
    assert hasattr(cjsidl_headerRef, "name")
    descriptor = None
    for klass in cjsidl_headerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_headerref_has_comment():
    assert hasattr(cjsidl_headerRef, "comment")
    descriptor = None
    for klass in cjsidl_headerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_containerref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_containerRef)


def test_cjsidl_containerref_constructor_exists():
    assert callable(cjsidl_containerRef.__init__)


def test_cjsidl_containerref_constructor_args():
    sig = inspect.signature(cjsidl_containerRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl_containerref_has_name():
    assert hasattr(cjsidl_containerRef, "name")
    descriptor = None
    for klass in cjsidl_containerRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_containerref_has_comment():
    assert hasattr(cjsidl_containerRef, "comment")
    descriptor = None
    for klass in cjsidl_containerRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_containerref_has_optional():
    assert hasattr(cjsidl_containerRef, "optional")
    descriptor = None
    for klass in cjsidl_containerRef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_containerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_containerDef)


def test_cjsidl_containerdef_constructor_exists():
    assert callable(cjsidl_containerDef.__init__)


def test_cjsidl_containerdef_constructor_args():
    sig = inspect.signature(cjsidl_containerDef.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_containerdef_has_optional():
    assert hasattr(cjsidl_containerDef, "optional")
    descriptor = None
    for klass in cjsidl_containerDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_containerdef_has_name():
    assert hasattr(cjsidl_containerDef, "name")
    descriptor = None
    for klass in cjsidl_containerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_containerdef_has_comment():
    assert hasattr(cjsidl_containerDef, "comment")
    descriptor = None
    for klass in cjsidl_containerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_footerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_footerDef)


def test_cjsidl_footerdef_constructor_exists():
    assert callable(cjsidl_footerDef.__init__)


def test_cjsidl_footerdef_constructor_args():
    sig = inspect.signature(cjsidl_footerDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_footerdef_has_name():
    assert hasattr(cjsidl_footerDef, "name")
    descriptor = None
    for klass in cjsidl_footerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_footerdef_has_comment():
    assert hasattr(cjsidl_footerDef, "comment")
    descriptor = None
    for klass in cjsidl_footerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_bodydef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_bodyDef)


def test_cjsidl_bodydef_constructor_exists():
    assert callable(cjsidl_bodyDef.__init__)


def test_cjsidl_bodydef_constructor_args():
    sig = inspect.signature(cjsidl_bodyDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_bodydef_has_name():
    assert hasattr(cjsidl_bodyDef, "name")
    descriptor = None
    for klass in cjsidl_bodyDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_bodydef_has_comment():
    assert hasattr(cjsidl_bodyDef, "comment")
    descriptor = None
    for klass in cjsidl_bodyDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_headerdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_headerDef)


def test_cjsidl_headerdef_constructor_exists():
    assert callable(cjsidl_headerDef.__init__)


def test_cjsidl_headerdef_constructor_args():
    sig = inspect.signature(cjsidl_headerDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_headerdef_has_name():
    assert hasattr(cjsidl_headerDef, "name")
    descriptor = None
    for klass in cjsidl_headerDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_headerdef_has_comment():
    assert hasattr(cjsidl_headerDef, "comment")
    descriptor = None
    for klass in cjsidl_headerDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_varformatfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl_varFormatField)


def test_cjsidl_varformatfield_constructor_exists():
    assert callable(cjsidl_varFormatField.__init__)


def test_cjsidl_varformatfield_constructor_args():
    sig = inspect.signature(cjsidl_varFormatField.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "units" in params, "Missing parameter 'units'"
    assert "countComment" in params, "Missing parameter 'countComment'"

def test_cjsidl_varformatfield_has_optional():
    assert hasattr(cjsidl_varFormatField, "optional")
    descriptor = None
    for klass in cjsidl_varFormatField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varformatfield_has_comment():
    assert hasattr(cjsidl_varFormatField, "comment")
    descriptor = None
    for klass in cjsidl_varFormatField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varformatfield_has_name():
    assert hasattr(cjsidl_varFormatField, "name")
    descriptor = None
    for klass in cjsidl_varFormatField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varformatfield_has_units():
    assert hasattr(cjsidl_varFormatField, "units")
    descriptor = None
    for klass in cjsidl_varFormatField.__mro__:
        if "units" in klass.__dict__:
            descriptor = klass.__dict__["units"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varformatfield_has_countComment():
    assert hasattr(cjsidl_varFormatField, "countComment")
    descriptor = None
    for klass in cjsidl_varFormatField.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_varlenfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl_varLenField)


def test_cjsidl_varlenfield_constructor_exists():
    assert callable(cjsidl_varLenField.__init__)


def test_cjsidl_varlenfield_constructor_args():
    sig = inspect.signature(cjsidl_varLenField.__init__)
    params = list(sig.parameters.keys())
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "countComment" in params, "Missing parameter 'countComment'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"
    assert "fieldFormat" in params, "Missing parameter 'fieldFormat'"
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"

def test_cjsidl_varlenfield_has_upperLim():
    assert hasattr(cjsidl_varLenField, "upperLim")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_countComment():
    assert hasattr(cjsidl_varLenField, "countComment")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_comment():
    assert hasattr(cjsidl_varLenField, "comment")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_optional():
    assert hasattr(cjsidl_varLenField, "optional")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_name():
    assert hasattr(cjsidl_varLenField, "name")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_fieldFormat():
    assert hasattr(cjsidl_varLenField, "fieldFormat")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "fieldFormat" in klass.__dict__:
            descriptor = klass.__dict__["fieldFormat"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenfield_has_lowerLim():
    assert hasattr(cjsidl_varLenField, "lowerLim")
    descriptor = None
    for klass in cjsidl_varLenField.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_varlenstring_is_not_abstract():
    assert not inspect.isabstract(cjsidl_varLenString)


def test_cjsidl_varlenstring_constructor_exists():
    assert callable(cjsidl_varLenString.__init__)


def test_cjsidl_varlenstring_constructor_args():
    sig = inspect.signature(cjsidl_varLenString.__init__)
    params = list(sig.parameters.keys())
    assert "lowerLim" in params, "Missing parameter 'lowerLim'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_varlenstring_has_lowerLim():
    assert hasattr(cjsidl_varLenString, "lowerLim")
    descriptor = None
    for klass in cjsidl_varLenString.__mro__:
        if "lowerLim" in klass.__dict__:
            descriptor = klass.__dict__["lowerLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenstring_has_optional():
    assert hasattr(cjsidl_varLenString, "optional")
    descriptor = None
    for klass in cjsidl_varLenString.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenstring_has_upperLim():
    assert hasattr(cjsidl_varLenString, "upperLim")
    descriptor = None
    for klass in cjsidl_varLenString.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenstring_has_comment():
    assert hasattr(cjsidl_varLenString, "comment")
    descriptor = None
    for klass in cjsidl_varLenString.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varlenstring_has_name():
    assert hasattr(cjsidl_varLenString, "name")
    descriptor = None
    for klass in cjsidl_varLenString.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_fixedlenstring_is_not_abstract():
    assert not inspect.isabstract(cjsidl_fixedLenString)


def test_cjsidl_fixedlenstring_constructor_exists():
    assert callable(cjsidl_fixedLenString.__init__)


def test_cjsidl_fixedlenstring_constructor_args():
    sig = inspect.signature(cjsidl_fixedLenString.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "upperLim" in params, "Missing parameter 'upperLim'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_fixedlenstring_has_optional():
    assert hasattr(cjsidl_fixedLenString, "optional")
    descriptor = None
    for klass in cjsidl_fixedLenString.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedlenstring_has_comment():
    assert hasattr(cjsidl_fixedLenString, "comment")
    descriptor = None
    for klass in cjsidl_fixedLenString.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedlenstring_has_upperLim():
    assert hasattr(cjsidl_fixedLenString, "upperLim")
    descriptor = None
    for klass in cjsidl_fixedLenString.__mro__:
        if "upperLim" in klass.__dict__:
            descriptor = klass.__dict__["upperLim"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedlenstring_has_name():
    assert hasattr(cjsidl_fixedLenString, "name")
    descriptor = None
    for klass in cjsidl_fixedLenString.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_bitfielddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_bitfieldDef)


def test_cjsidl_bitfielddef_constructor_exists():
    assert callable(cjsidl_bitfieldDef.__init__)


def test_cjsidl_bitfielddef_constructor_args():
    sig = inspect.signature(cjsidl_bitfieldDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_bitfielddef_has_type():
    assert hasattr(cjsidl_bitfieldDef, "type")
    descriptor = None
    for klass in cjsidl_bitfieldDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_bitfielddef_has_comment():
    assert hasattr(cjsidl_bitfieldDef, "comment")
    descriptor = None
    for klass in cjsidl_bitfieldDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_bitfielddef_has_optional():
    assert hasattr(cjsidl_bitfieldDef, "optional")
    descriptor = None
    for klass in cjsidl_bitfieldDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_bitfielddef_has_name():
    assert hasattr(cjsidl_bitfieldDef, "name")
    descriptor = None
    for klass in cjsidl_bitfieldDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_action_is_not_abstract():
    assert not inspect.isabstract(cjsidl_action)


def test_cjsidl_action_constructor_exists():
    assert callable(cjsidl_action.__init__)


def test_cjsidl_action_constructor_args():
    sig = inspect.signature(cjsidl_action.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_action_has_comment():
    assert hasattr(cjsidl_action, "comment")
    descriptor = None
    for klass in cjsidl_action.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_action_has_name():
    assert hasattr(cjsidl_action, "name")
    descriptor = None
    for klass in cjsidl_action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_varfield_is_not_abstract():
    assert not inspect.isabstract(cjsidl_varField)


def test_cjsidl_varfield_constructor_exists():
    assert callable(cjsidl_varField.__init__)


def test_cjsidl_varfield_constructor_args():
    sig = inspect.signature(cjsidl_varField.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_varfield_has_comment():
    assert hasattr(cjsidl_varField, "comment")
    descriptor = None
    for klass in cjsidl_varField.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varfield_has_optional():
    assert hasattr(cjsidl_varField, "optional")
    descriptor = None
    for klass in cjsidl_varField.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_varfield_has_name():
    assert hasattr(cjsidl_varField, "name")
    descriptor = None
    for klass in cjsidl_varField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_fixedfielddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_fixedFieldDef)


def test_cjsidl_fixedfielddef_constructor_exists():
    assert callable(cjsidl_fixedFieldDef.__init__)


def test_cjsidl_fixedfielddef_constructor_args():
    sig = inspect.signature(cjsidl_fixedFieldDef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "fieldUnit" in params, "Missing parameter 'fieldUnit'"
    assert "name" in params, "Missing parameter 'name'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl_fixedfielddef_has_comment():
    assert hasattr(cjsidl_fixedFieldDef, "comment")
    descriptor = None
    for klass in cjsidl_fixedFieldDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedfielddef_has_fieldUnit():
    assert hasattr(cjsidl_fixedFieldDef, "fieldUnit")
    descriptor = None
    for klass in cjsidl_fixedFieldDef.__mro__:
        if "fieldUnit" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnit"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedfielddef_has_name():
    assert hasattr(cjsidl_fixedFieldDef, "name")
    descriptor = None
    for klass in cjsidl_fixedFieldDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_fixedfielddef_has_optional():
    assert hasattr(cjsidl_fixedFieldDef, "optional")
    descriptor = None
    for klass in cjsidl_fixedFieldDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_sequencedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_sequenceDef)


def test_cjsidl_sequencedef_constructor_exists():
    assert callable(cjsidl_sequenceDef.__init__)


def test_cjsidl_sequencedef_constructor_args():
    sig = inspect.signature(cjsidl_sequenceDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_variantdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_variantDef)


def test_cjsidl_variantdef_constructor_exists():
    assert callable(cjsidl_variantDef.__init__)


def test_cjsidl_variantdef_constructor_args():
    sig = inspect.signature(cjsidl_variantDef.__init__)
    params = list(sig.parameters.keys())
    assert "minCount" in params, "Missing parameter 'minCount'"
    assert "maxCount" in params, "Missing parameter 'maxCount'"
    assert "vtagComment" in params, "Missing parameter 'vtagComment'"

def test_cjsidl_variantdef_has_minCount():
    assert hasattr(cjsidl_variantDef, "minCount")
    descriptor = None
    for klass in cjsidl_variantDef.__mro__:
        if "minCount" in klass.__dict__:
            descriptor = klass.__dict__["minCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_variantdef_has_maxCount():
    assert hasattr(cjsidl_variantDef, "maxCount")
    descriptor = None
    for klass in cjsidl_variantDef.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_variantdef_has_vtagComment():
    assert hasattr(cjsidl_variantDef, "vtagComment")
    descriptor = None
    for klass in cjsidl_variantDef.__mro__:
        if "vtagComment" in klass.__dict__:
            descriptor = klass.__dict__["vtagComment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_listdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_listDef)


def test_cjsidl_listdef_constructor_exists():
    assert callable(cjsidl_listDef.__init__)


def test_cjsidl_listdef_constructor_args():
    sig = inspect.signature(cjsidl_listDef.__init__)
    params = list(sig.parameters.keys())
    assert "maxCount" in params, "Missing parameter 'maxCount'"
    assert "countComment" in params, "Missing parameter 'countComment'"
    assert "minCount" in params, "Missing parameter 'minCount'"

def test_cjsidl_listdef_has_maxCount():
    assert hasattr(cjsidl_listDef, "maxCount")
    descriptor = None
    for klass in cjsidl_listDef.__mro__:
        if "maxCount" in klass.__dict__:
            descriptor = klass.__dict__["maxCount"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_listdef_has_countComment():
    assert hasattr(cjsidl_listDef, "countComment")
    descriptor = None
    for klass in cjsidl_listDef.__mro__:
        if "countComment" in klass.__dict__:
            descriptor = klass.__dict__["countComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_listdef_has_minCount():
    assert hasattr(cjsidl_listDef, "minCount")
    descriptor = None
    for klass in cjsidl_listDef.__mro__:
        if "minCount" in klass.__dict__:
            descriptor = klass.__dict__["minCount"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_recorddef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_recordDef)


def test_cjsidl_recorddef_constructor_exists():
    assert callable(cjsidl_recordDef.__init__)


def test_cjsidl_recorddef_constructor_args():
    sig = inspect.signature(cjsidl_recordDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_arraydef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_arrayDef)


def test_cjsidl_arraydef_constructor_exists():
    assert callable(cjsidl_arrayDef.__init__)


def test_cjsidl_arraydef_constructor_args():
    sig = inspect.signature(cjsidl_arrayDef.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "arraySize" in params, "Missing parameter 'arraySize'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_arraydef_has_optional():
    assert hasattr(cjsidl_arrayDef, "optional")
    descriptor = None
    for klass in cjsidl_arrayDef.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_arraydef_has_arraySize():
    assert hasattr(cjsidl_arrayDef, "arraySize")
    descriptor = None
    for klass in cjsidl_arrayDef.__mro__:
        if "arraySize" in klass.__dict__:
            descriptor = klass.__dict__["arraySize"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_arraydef_has_comment():
    assert hasattr(cjsidl_arrayDef, "comment")
    descriptor = None
    for klass in cjsidl_arrayDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_arraydef_has_name():
    assert hasattr(cjsidl_arrayDef, "name")
    descriptor = None
    for klass in cjsidl_arrayDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_simplenumerictype_is_not_abstract():
    assert not inspect.isabstract(cjsidl_simpleNumericType)


def test_cjsidl_simplenumerictype_constructor_exists():
    assert callable(cjsidl_simpleNumericType.__init__)


def test_cjsidl_simplenumerictype_constructor_args():
    sig = inspect.signature(cjsidl_simpleNumericType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_cjsidl_simplenumerictype_has_type():
    assert hasattr(cjsidl_simpleNumericType, "type")
    descriptor = None
    for klass in cjsidl_simpleNumericType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_simpletransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_simpleTransition)


def test_cjsidl_simpletransition_constructor_exists():
    assert callable(cjsidl_simpleTransition.__init__)


def test_cjsidl_simpletransition_constructor_args():
    sig = inspect.signature(cjsidl_simpleTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_simpletransition_has_comment():
    assert hasattr(cjsidl_simpleTransition, "comment")
    descriptor = None
    for klass in cjsidl_simpleTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_internaltransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_internalTransition)


def test_cjsidl_internaltransition_constructor_exists():
    assert callable(cjsidl_internalTransition.__init__)


def test_cjsidl_internaltransition_constructor_args():
    sig = inspect.signature(cjsidl_internalTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_internaltransition_has_comment():
    assert hasattr(cjsidl_internalTransition, "comment")
    descriptor = None
    for klass in cjsidl_internalTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_guardaction_is_not_abstract():
    assert not inspect.isabstract(cjsidl_guardAction)


def test_cjsidl_guardaction_constructor_exists():
    assert callable(cjsidl_guardAction.__init__)


def test_cjsidl_guardaction_constructor_args():
    sig = inspect.signature(cjsidl_guardAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "not_" in params, "Missing parameter 'not_'"

def test_cjsidl_guardaction_has_name():
    assert hasattr(cjsidl_guardAction, "name")
    descriptor = None
    for klass in cjsidl_guardAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_guardaction_has_not_():
    assert hasattr(cjsidl_guardAction, "not_")
    descriptor = None
    for klass in cjsidl_guardAction.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_guardparam_is_not_abstract():
    assert not inspect.isabstract(cjsidl_guardParam)


def test_cjsidl_guardparam_constructor_exists():
    assert callable(cjsidl_guardParam.__init__)


def test_cjsidl_guardparam_constructor_args():
    sig = inspect.signature(cjsidl_guardParam.__init__)
    params = list(sig.parameters.keys())
    assert "guardConst" in params, "Missing parameter 'guardConst'"

def test_cjsidl_guardparam_has_guardConst():
    assert hasattr(cjsidl_guardParam, "guardConst")
    descriptor = None
    for klass in cjsidl_guardParam.__mro__:
        if "guardConst" in klass.__dict__:
            descriptor = klass.__dict__["guardConst"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_poptransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_popTransition)


def test_cjsidl_poptransition_constructor_exists():
    assert callable(cjsidl_popTransition.__init__)


def test_cjsidl_poptransition_constructor_args():
    sig = inspect.signature(cjsidl_popTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_poptransition_has_comment():
    assert hasattr(cjsidl_popTransition, "comment")
    descriptor = None
    for klass in cjsidl_popTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_pushtransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_pushTransition)


def test_cjsidl_pushtransition_constructor_exists():
    assert callable(cjsidl_pushTransition.__init__)


def test_cjsidl_pushtransition_constructor_args():
    sig = inspect.signature(cjsidl_pushTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_pushtransition_has_comment():
    assert hasattr(cjsidl_pushTransition, "comment")
    descriptor = None
    for klass in cjsidl_pushTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_nextstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl_nextState)


def test_cjsidl_nextstate_constructor_exists():
    assert callable(cjsidl_nextState.__init__)


def test_cjsidl_nextstate_constructor_args():
    sig = inspect.signature(cjsidl_nextState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_nextstate_has_comment():
    assert hasattr(cjsidl_nextState, "comment")
    descriptor = None
    for klass in cjsidl_nextState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_sendactionlist_is_not_abstract():
    assert not inspect.isabstract(cjsidl_sendActionList)


def test_cjsidl_sendactionlist_constructor_exists():
    assert callable(cjsidl_sendActionList.__init__)


def test_cjsidl_sendactionlist_constructor_args():
    sig = inspect.signature(cjsidl_sendActionList.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_actionlist_is_not_abstract():
    assert not inspect.isabstract(cjsidl_actionList)


def test_cjsidl_actionlist_constructor_exists():
    assert callable(cjsidl_actionList.__init__)


def test_cjsidl_actionlist_constructor_args():
    sig = inspect.signature(cjsidl_actionList.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_defaulttransition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_defaultTransition)


def test_cjsidl_defaulttransition_constructor_exists():
    assert callable(cjsidl_defaultTransition.__init__)


def test_cjsidl_defaulttransition_constructor_args():
    sig = inspect.signature(cjsidl_defaultTransition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "type" in params, "Missing parameter 'type'"

def test_cjsidl_defaulttransition_has_comment():
    assert hasattr(cjsidl_defaultTransition, "comment")
    descriptor = None
    for klass in cjsidl_defaultTransition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_defaulttransition_has_type():
    assert hasattr(cjsidl_defaultTransition, "type")
    descriptor = None
    for klass in cjsidl_defaultTransition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_guard_is_not_abstract():
    assert not inspect.isabstract(cjsidl_guard)


def test_cjsidl_guard_constructor_exists():
    assert callable(cjsidl_guard.__init__)


def test_cjsidl_guard_constructor_args():
    sig = inspect.signature(cjsidl_guard.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "equiv" in params, "Missing parameter 'equiv'"
    assert "logicalOperator" in params, "Missing parameter 'logicalOperator'"

def test_cjsidl_guard_has_comment():
    assert hasattr(cjsidl_guard, "comment")
    descriptor = None
    for klass in cjsidl_guard.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_guard_has_equiv():
    assert hasattr(cjsidl_guard, "equiv")
    descriptor = None
    for klass in cjsidl_guard.__mro__:
        if "equiv" in klass.__dict__:
            descriptor = klass.__dict__["equiv"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_guard_has_logicalOperator():
    assert hasattr(cjsidl_guard, "logicalOperator")
    descriptor = None
    for klass in cjsidl_guard.__mro__:
        if "logicalOperator" in klass.__dict__:
            descriptor = klass.__dict__["logicalOperator"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_scopedeventtype_is_not_abstract():
    assert not inspect.isabstract(cjsidl_scopedEventType)


def test_cjsidl_scopedeventtype_constructor_exists():
    assert callable(cjsidl_scopedEventType.__init__)


def test_cjsidl_scopedeventtype_constructor_args():
    sig = inspect.signature(cjsidl_scopedEventType.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_transparam_is_not_abstract():
    assert not inspect.isabstract(cjsidl_transParam)


def test_cjsidl_transparam_constructor_exists():
    assert callable(cjsidl_transParam.__init__)


def test_cjsidl_transparam_constructor_args():
    sig = inspect.signature(cjsidl_transParam.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "unsignedType" in params, "Missing parameter 'unsignedType'"

def test_cjsidl_transparam_has_name():
    assert hasattr(cjsidl_transParam, "name")
    descriptor = None
    for klass in cjsidl_transParam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_transparam_has_comment():
    assert hasattr(cjsidl_transParam, "comment")
    descriptor = None
    for klass in cjsidl_transParam.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_transparam_has_unsignedType():
    assert hasattr(cjsidl_transParam, "unsignedType")
    descriptor = None
    for klass in cjsidl_transParam.__mro__:
        if "unsignedType" in klass.__dict__:
            descriptor = klass.__dict__["unsignedType"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_transparams_is_not_abstract():
    assert not inspect.isabstract(cjsidl_transParams)


def test_cjsidl_transparams_constructor_exists():
    assert callable(cjsidl_transParams.__init__)


def test_cjsidl_transparams_constructor_args():
    sig = inspect.signature(cjsidl_transParams.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_statemachine_is_not_abstract():
    assert not inspect.isabstract(cjsidl_stateMachine)


def test_cjsidl_statemachine_constructor_exists():
    assert callable(cjsidl_stateMachine.__init__)


def test_cjsidl_statemachine_constructor_args():
    sig = inspect.signature(cjsidl_stateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_statemachine_has_comment():
    assert hasattr(cjsidl_stateMachine, "comment")
    descriptor = None
    for klass in cjsidl_stateMachine.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_statemachine_has_name():
    assert hasattr(cjsidl_stateMachine, "name")
    descriptor = None
    for klass in cjsidl_stateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_eventdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_eventDef)


def test_cjsidl_eventdef_constructor_exists():
    assert callable(cjsidl_eventDef.__init__)


def test_cjsidl_eventdef_constructor_args():
    sig = inspect.signature(cjsidl_eventDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_eventdef_has_name():
    assert hasattr(cjsidl_eventDef, "name")
    descriptor = None
    for klass in cjsidl_eventDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_transition_is_not_abstract():
    assert not inspect.isabstract(cjsidl_transition)


def test_cjsidl_transition_constructor_exists():
    assert callable(cjsidl_transition.__init__)


def test_cjsidl_transition_constructor_args():
    sig = inspect.signature(cjsidl_transition.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_cjsidl_transition_has_comment():
    assert hasattr(cjsidl_transition, "comment")
    descriptor = None
    for klass in cjsidl_transition.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_transition_has_name():
    assert hasattr(cjsidl_transition, "name")
    descriptor = None
    for klass in cjsidl_transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_transition_has_type():
    assert hasattr(cjsidl_transition, "type")
    descriptor = None
    for klass in cjsidl_transition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_exit_is_not_abstract():
    assert not inspect.isabstract(cjsidl_exit)


def test_cjsidl_exit_constructor_exists():
    assert callable(cjsidl_exit.__init__)


def test_cjsidl_exit_constructor_args():
    sig = inspect.signature(cjsidl_exit.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_exit_has_comment():
    assert hasattr(cjsidl_exit, "comment")
    descriptor = None
    for klass in cjsidl_exit.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_entry_is_not_abstract():
    assert not inspect.isabstract(cjsidl_entry)


def test_cjsidl_entry_constructor_exists():
    assert callable(cjsidl_entry.__init__)


def test_cjsidl_entry_constructor_args():
    sig = inspect.signature(cjsidl_entry.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_entry_has_comment():
    assert hasattr(cjsidl_entry, "comment")
    descriptor = None
    for klass in cjsidl_entry.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_defaultstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl_defaultState)


def test_cjsidl_defaultstate_constructor_exists():
    assert callable(cjsidl_defaultState.__init__)


def test_cjsidl_defaultstate_constructor_args():
    sig = inspect.signature(cjsidl_defaultState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_defaultstate_has_comment():
    assert hasattr(cjsidl_defaultState, "comment")
    descriptor = None
    for klass in cjsidl_defaultState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_state_is_not_abstract():
    assert not inspect.isabstract(cjsidl_state)


def test_cjsidl_state_constructor_exists():
    assert callable(cjsidl_state.__init__)


def test_cjsidl_state_constructor_args():
    sig = inspect.signature(cjsidl_state.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_state_has_initial():
    assert hasattr(cjsidl_state, "initial")
    descriptor = None
    for klass in cjsidl_state.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_state_has_comment():
    assert hasattr(cjsidl_state, "comment")
    descriptor = None
    for klass in cjsidl_state.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_state_has_name():
    assert hasattr(cjsidl_state, "name")
    descriptor = None
    for klass in cjsidl_state.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_startstate_is_not_abstract():
    assert not inspect.isabstract(cjsidl_startState)


def test_cjsidl_startstate_constructor_exists():
    assert callable(cjsidl_startState.__init__)


def test_cjsidl_startstate_constructor_args():
    sig = inspect.signature(cjsidl_startState.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_startstate_has_comment():
    assert hasattr(cjsidl_startState, "comment")
    descriptor = None
    for klass in cjsidl_startState.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_constdef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_constDef)


def test_cjsidl_constdef_constructor_exists():
    assert callable(cjsidl_constDef.__init__)


def test_cjsidl_constdef_constructor_args():
    sig = inspect.signature(cjsidl_constDef.__init__)
    params = list(sig.parameters.keys())
    assert "constValue" in params, "Missing parameter 'constValue'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "fieldUnits" in params, "Missing parameter 'fieldUnits'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_constdef_has_constValue():
    assert hasattr(cjsidl_constDef, "constValue")
    descriptor = None
    for klass in cjsidl_constDef.__mro__:
        if "constValue" in klass.__dict__:
            descriptor = klass.__dict__["constValue"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_constdef_has_comment():
    assert hasattr(cjsidl_constDef, "comment")
    descriptor = None
    for klass in cjsidl_constDef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_constdef_has_fieldUnits():
    assert hasattr(cjsidl_constDef, "fieldUnits")
    descriptor = None
    for klass in cjsidl_constDef.__mro__:
        if "fieldUnits" in klass.__dict__:
            descriptor = klass.__dict__["fieldUnits"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_constdef_has_name():
    assert hasattr(cjsidl_constDef, "name")
    descriptor = None
    for klass in cjsidl_constDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_declaredconstsetref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_declaredConstSetRef)


def test_cjsidl_declaredconstsetref_constructor_exists():
    assert callable(cjsidl_declaredConstSetRef.__init__)


def test_cjsidl_declaredconstsetref_constructor_args():
    sig = inspect.signature(cjsidl_declaredConstSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_declaredconstsetref_has_comment():
    assert hasattr(cjsidl_declaredConstSetRef, "comment")
    descriptor = None
    for klass in cjsidl_declaredConstSetRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredconstsetref_has_name():
    assert hasattr(cjsidl_declaredConstSetRef, "name")
    descriptor = None
    for klass in cjsidl_declaredConstSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_messagescopedref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_messageScopedRef)


def test_cjsidl_messagescopedref_constructor_exists():
    assert callable(cjsidl_messageScopedRef.__init__)


def test_cjsidl_messagescopedref_constructor_args():
    sig = inspect.signature(cjsidl_messageScopedRef.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_messagescopedref_has_comment():
    assert hasattr(cjsidl_messageScopedRef, "comment")
    descriptor = None
    for klass in cjsidl_messageScopedRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messagescopedref_has_name():
    assert hasattr(cjsidl_messageScopedRef, "name")
    descriptor = None
    for klass in cjsidl_messageScopedRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_messageref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_messageRef)


def test_cjsidl_messageref_constructor_exists():
    assert callable(cjsidl_messageRef.__init__)


def test_cjsidl_messageref_constructor_args():
    sig = inspect.signature(cjsidl_messageRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_messageref_has_name():
    assert hasattr(cjsidl_messageRef, "name")
    descriptor = None
    for klass in cjsidl_messageRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messageref_has_comment():
    assert hasattr(cjsidl_messageRef, "comment")
    descriptor = None
    for klass in cjsidl_messageRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_messagedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_messageDef)


def test_cjsidl_messagedef_constructor_exists():
    assert callable(cjsidl_messageDef.__init__)


def test_cjsidl_messagedef_constructor_args():
    sig = inspect.signature(cjsidl_messageDef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "command" in params, "Missing parameter 'command'"
    assert "messageID" in params, "Missing parameter 'messageID'"

def test_cjsidl_messagedef_has_name():
    assert hasattr(cjsidl_messageDef, "name")
    descriptor = None
    for klass in cjsidl_messageDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messagedef_has_command():
    assert hasattr(cjsidl_messageDef, "command")
    descriptor = None
    for klass in cjsidl_messageDef.__mro__:
        if "command" in klass.__dict__:
            descriptor = klass.__dict__["command"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messagedef_has_messageID():
    assert hasattr(cjsidl_messageDef, "messageID")
    descriptor = None
    for klass in cjsidl_messageDef.__mro__:
        if "messageID" in klass.__dict__:
            descriptor = klass.__dict__["messageID"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_messages_is_not_abstract():
    assert not inspect.isabstract(cjsidl_messages)


def test_cjsidl_messages_constructor_exists():
    assert callable(cjsidl_messages.__init__)


def test_cjsidl_messages_constructor_args():
    sig = inspect.signature(cjsidl_messages.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_scopedtypeid_is_not_abstract():
    assert not inspect.isabstract(cjsidl_scopedTypeId)


def test_cjsidl_scopedtypeid_constructor_exists():
    assert callable(cjsidl_scopedTypeId.__init__)


def test_cjsidl_scopedtypeid_constructor_args():
    sig = inspect.signature(cjsidl_scopedTypeId.__init__)
    params = list(sig.parameters.keys())
    assert "optional" in params, "Missing parameter 'optional'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "scopedName" in params, "Missing parameter 'scopedName'"

def test_cjsidl_scopedtypeid_has_optional():
    assert hasattr(cjsidl_scopedTypeId, "optional")
    descriptor = None
    for klass in cjsidl_scopedTypeId.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_scopedtypeid_has_comment():
    assert hasattr(cjsidl_scopedTypeId, "comment")
    descriptor = None
    for klass in cjsidl_scopedTypeId.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_scopedtypeid_has_scopedName():
    assert hasattr(cjsidl_scopedTypeId, "scopedName")
    descriptor = None
    for klass in cjsidl_scopedTypeId.__mro__:
        if "scopedName" in klass.__dict__:
            descriptor = klass.__dict__["scopedName"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_typereference_is_not_abstract():
    assert not inspect.isabstract(cjsidl_typeReference)


def test_cjsidl_typereference_constructor_exists():
    assert callable(cjsidl_typeReference.__init__)


def test_cjsidl_typereference_constructor_args():
    sig = inspect.signature(cjsidl_typeReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"
    assert "optional" in params, "Missing parameter 'optional'"

def test_cjsidl_typereference_has_name():
    assert hasattr(cjsidl_typeReference, "name")
    descriptor = None
    for klass in cjsidl_typeReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_typereference_has_comment():
    assert hasattr(cjsidl_typeReference, "comment")
    descriptor = None
    for klass in cjsidl_typeReference.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_typereference_has_optional():
    assert hasattr(cjsidl_typeReference, "optional")
    descriptor = None
    for klass in cjsidl_typeReference.__mro__:
        if "optional" in klass.__dict__:
            descriptor = klass.__dict__["optional"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_typedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_typeDef)


def test_cjsidl_typedef_constructor_exists():
    assert callable(cjsidl_typeDef.__init__)


def test_cjsidl_typedef_constructor_args():
    sig = inspect.signature(cjsidl_typeDef.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_declaredtypesetref_is_not_abstract():
    assert not inspect.isabstract(cjsidl_declaredTypeSetRef)


def test_cjsidl_declaredtypesetref_constructor_exists():
    assert callable(cjsidl_declaredTypeSetRef.__init__)


def test_cjsidl_declaredtypesetref_constructor_args():
    sig = inspect.signature(cjsidl_declaredTypeSetRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_declaredtypesetref_has_name():
    assert hasattr(cjsidl_declaredTypeSetRef, "name")
    descriptor = None
    for klass in cjsidl_declaredTypeSetRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredtypesetref_has_comment():
    assert hasattr(cjsidl_declaredTypeSetRef, "comment")
    descriptor = None
    for klass in cjsidl_declaredTypeSetRef.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_servicedef_is_not_abstract():
    assert not inspect.isabstract(cjsidl_serviceDef)


def test_cjsidl_servicedef_constructor_exists():
    assert callable(cjsidl_serviceDef.__init__)


def test_cjsidl_servicedef_constructor_args():
    sig = inspect.signature(cjsidl_serviceDef.__init__)
    params = list(sig.parameters.keys())
    assert "assumpt" in params, "Missing parameter 'assumpt'"
    assert "name" in params, "Missing parameter 'name'"
    assert "serviceVersion" in params, "Missing parameter 'serviceVersion'"
    assert "serviceName" in params, "Missing parameter 'serviceName'"

def test_cjsidl_servicedef_has_assumpt():
    assert hasattr(cjsidl_serviceDef, "assumpt")
    descriptor = None
    for klass in cjsidl_serviceDef.__mro__:
        if "assumpt" in klass.__dict__:
            descriptor = klass.__dict__["assumpt"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_servicedef_has_name():
    assert hasattr(cjsidl_serviceDef, "name")
    descriptor = None
    for klass in cjsidl_serviceDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_servicedef_has_serviceVersion():
    assert hasattr(cjsidl_serviceDef, "serviceVersion")
    descriptor = None
    for klass in cjsidl_serviceDef.__mro__:
        if "serviceVersion" in klass.__dict__:
            descriptor = klass.__dict__["serviceVersion"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_servicedef_has_serviceName():
    assert hasattr(cjsidl_serviceDef, "serviceName")
    descriptor = None
    for klass in cjsidl_serviceDef.__mro__:
        if "serviceName" in klass.__dict__:
            descriptor = klass.__dict__["serviceName"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_eobject_is_not_abstract():
    assert not inspect.isabstract(cjsidl_EObject)


def test_cjsidl_eobject_constructor_exists():
    assert callable(cjsidl_EObject.__init__)


def test_cjsidl_eobject_constructor_args():
    sig = inspect.signature(cjsidl_EObject.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_jaus_is_not_abstract():
    assert not inspect.isabstract(cjsidl_jaus)


def test_cjsidl_jaus_constructor_exists():
    assert callable(cjsidl_jaus.__init__)


def test_cjsidl_jaus_constructor_args():
    sig = inspect.signature(cjsidl_jaus.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_refattr_is_not_abstract():
    assert not inspect.isabstract(cjsidl_refAttr)


def test_cjsidl_refattr_constructor_exists():
    assert callable(cjsidl_refAttr.__init__)


def test_cjsidl_refattr_constructor_args():
    sig = inspect.signature(cjsidl_refAttr.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "name" in params, "Missing parameter 'name'"

def test_cjsidl_refattr_has_comment():
    assert hasattr(cjsidl_refAttr, "comment")
    descriptor = None
    for klass in cjsidl_refAttr.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_refattr_has_name():
    assert hasattr(cjsidl_refAttr, "name")
    descriptor = None
    for klass in cjsidl_refAttr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_protocolbehavior_is_not_abstract():
    assert not inspect.isabstract(cjsidl_protocolBehavior)


def test_cjsidl_protocolbehavior_constructor_exists():
    assert callable(cjsidl_protocolBehavior.__init__)


def test_cjsidl_protocolbehavior_constructor_args():
    sig = inspect.signature(cjsidl_protocolBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "stateless" in params, "Missing parameter 'stateless'"

def test_cjsidl_protocolbehavior_has_comment():
    assert hasattr(cjsidl_protocolBehavior, "comment")
    descriptor = None
    for klass in cjsidl_protocolBehavior.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_protocolbehavior_has_stateless():
    assert hasattr(cjsidl_protocolBehavior, "stateless")
    descriptor = None
    for klass in cjsidl_protocolBehavior.__mro__:
        if "stateless" in klass.__dict__:
            descriptor = klass.__dict__["stateless"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_internaleventset_is_not_abstract():
    assert not inspect.isabstract(cjsidl_internalEventSet)


def test_cjsidl_internaleventset_constructor_exists():
    assert callable(cjsidl_internalEventSet.__init__)


def test_cjsidl_internaleventset_constructor_args():
    sig = inspect.signature(cjsidl_internalEventSet.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cjsidl_internaleventset_has_comment():
    assert hasattr(cjsidl_internalEventSet, "comment")
    descriptor = None
    for klass in cjsidl_internalEventSet.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_messageset_is_not_abstract():
    assert not inspect.isabstract(cjsidl_messageSet)


def test_cjsidl_messageset_constructor_exists():
    assert callable(cjsidl_messageSet.__init__)


def test_cjsidl_messageset_constructor_args():
    sig = inspect.signature(cjsidl_messageSet.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"
    assert "inputComment" in params, "Missing parameter 'inputComment'"
    assert "outputComment" in params, "Missing parameter 'outputComment'"

def test_cjsidl_messageset_has_comment():
    assert hasattr(cjsidl_messageSet, "comment")
    descriptor = None
    for klass in cjsidl_messageSet.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messageset_has_inputComment():
    assert hasattr(cjsidl_messageSet, "inputComment")
    descriptor = None
    for klass in cjsidl_messageSet.__mro__:
        if "inputComment" in klass.__dict__:
            descriptor = klass.__dict__["inputComment"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_messageset_has_outputComment():
    assert hasattr(cjsidl_messageSet, "outputComment")
    descriptor = None
    for klass in cjsidl_messageSet.__mro__:
        if "outputComment" in klass.__dict__:
            descriptor = klass.__dict__["outputComment"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_declaredtypeset_is_not_abstract():
    assert not inspect.isabstract(cjsidl_declaredTypeSet)


def test_cjsidl_declaredtypeset_constructor_exists():
    assert callable(cjsidl_declaredTypeSet.__init__)


def test_cjsidl_declaredtypeset_constructor_args():
    sig = inspect.signature(cjsidl_declaredTypeSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "version" in params, "Missing parameter 'version'"

def test_cjsidl_declaredtypeset_has_name():
    assert hasattr(cjsidl_declaredTypeSet, "name")
    descriptor = None
    for klass in cjsidl_declaredTypeSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredtypeset_has_typeName():
    assert hasattr(cjsidl_declaredTypeSet, "typeName")
    descriptor = None
    for klass in cjsidl_declaredTypeSet.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredtypeset_has_version():
    assert hasattr(cjsidl_declaredTypeSet, "version")
    descriptor = None
    for klass in cjsidl_declaredTypeSet.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_declaredconstset_is_not_abstract():
    assert not inspect.isabstract(cjsidl_declaredConstSet)


def test_cjsidl_declaredconstset_constructor_exists():
    assert callable(cjsidl_declaredConstSet.__init__)


def test_cjsidl_declaredconstset_constructor_args():
    sig = inspect.signature(cjsidl_declaredConstSet.__init__)
    params = list(sig.parameters.keys())
    assert "constName" in params, "Missing parameter 'constName'"
    assert "name" in params, "Missing parameter 'name'"
    assert "constSetVersion" in params, "Missing parameter 'constSetVersion'"

def test_cjsidl_declaredconstset_has_constName():
    assert hasattr(cjsidl_declaredConstSet, "constName")
    descriptor = None
    for klass in cjsidl_declaredConstSet.__mro__:
        if "constName" in klass.__dict__:
            descriptor = klass.__dict__["constName"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredconstset_has_name():
    assert hasattr(cjsidl_declaredConstSet, "name")
    descriptor = None
    for klass in cjsidl_declaredConstSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cjsidl_declaredconstset_has_constSetVersion():
    assert hasattr(cjsidl_declaredConstSet, "constSetVersion")
    descriptor = None
    for klass in cjsidl_declaredConstSet.__mro__:
        if "constSetVersion" in klass.__dict__:
            descriptor = klass.__dict__["constSetVersion"]
            break
    assert isinstance(descriptor, property)



def test_cjsidl_references_is_not_abstract():
    assert not inspect.isabstract(cjsidl_references)


def test_cjsidl_references_constructor_exists():
    assert callable(cjsidl_references.__init__)


def test_cjsidl_references_constructor_args():
    sig = inspect.signature(cjsidl_references.__init__)
    params = list(sig.parameters.keys())



def test_cjsidl_description_is_not_abstract():
    assert not inspect.isabstract(cjsidl_description)


def test_cjsidl_description_constructor_exists():
    assert callable(cjsidl_description.__init__)


def test_cjsidl_description_constructor_args():
    sig = inspect.signature(cjsidl_description.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_cjsidl_description_has_content():
    assert hasattr(cjsidl_description, "content")
    descriptor = None
    for klass in cjsidl_description.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_field_format_exists():
    # Check that the Enumeration exists
    assert FIELD_FORMAT is not None

def test_field_format_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FIELD_FORMAT]
    expected_literals = [
        "MP3",
        "RNC",
        "MPEG1",
        "AU",
        "XSD",
        "MPEG2",
        "WAV",
        "RNG",
        "MJPEG",
        "MP4",
        "USER_DEFINED",
        "MP2",
        "RAW",
        "XML",
        "JAUS_MESSAGE",
        "JPEG",
        "BMP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FIELD_FORMAT"

def test_unit_exists():
    # Check that the Enumeration exists
    assert UNIT is not None

def test_unit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UNIT]
    expected_literals = [
        "LUX",
        "AMP_PER_METER",
        "AMPPERSQRMETER",
        "SQR_METER",
        "DEGREE",
        "JOULE_PER_MOLE",
        "WATT_PER_METER_KELVIN",
        "PASCAL",
        "KELVIN",
        "CANDELA_PER_SQUARE_METER",
        "KNOT",
        "NEWTON",
        "KATAL",
        "RAD_PER_SEC_SQR",
        "BAR",
        "RAD",
        "ARE",
        "MTON",
        "SIEVERT",
        "CUBIC_METER",
        "NEWTON_PER_METER",
        "RAD_PER_SEC",
        "PASCAL_SEC",
        "RADIAN",
        "COULOMB_PER_SQR_METER",
        "METER_PER_SEC_SQR",
        "ONE",
        "KG_PER_CUBIC_METER",
        "DAY",
        "AMP",
        "VOLT_PER_METER",
        "BECQUEREL",
        "NEPER",
        "NMILE",
        "ROENTGEN",
        "MIN",
        "WATT_PER_SQR_METER",
        "MOLE_PER_CUBIC_METER",
        "METER_PER_SEC",
        "JOULE",
        "SIEMENS",
        "FARAD_PER_METER",
        "KG",
        "HRZ",
        "CUBICMETERPERKG",
        "JOULE_PER_KELVIN",
        "STE_RAD",
        "RECIPROCAL_METER",
        "VOLT",
        "HENRY",
        "CURIE",
        "COULOMB",
        "WEBER",
        "KATAL_PER_CUBIC_METER",
        "WATT",
        "HECTARE",
        "LTR",
        "CANDELA",
        "COULOMB_PER_KG",
        "CELSIUS",
        "JOULE_PER_KG",
        "BARN",
        "HOUR",
        "COULOMB_PER_CUBIC_METER",
        "SEC",
        "METER",
        "FARAD",
        "REM",
        "NEWTON_METER",
        "MOLE",
        "OHM",
        "JOULE_PER_MOLE_KELVIN",
        "WATT_PER_SQR_METER_STERAD",
        "LUMEN",
        "JOULES_PER_CUBIC_METER",
        "BEL",
        "HENRY_PER_METER",
        "ANGSROM",
        "TESLA",
        "GRAY_PER_SEC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UNIT"


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
cjsidl_taggedItemDef_strategy = st.builds(
    cjsidl_taggedItemDef,
)
cjsidl_valueSpec_strategy = st.builds(
    cjsidl_valueSpec,
    value=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
containerDef_strategy = st.builds(
    containerDef,
)
cjsidl_formatEnumDef_strategy = st.builds(
    cjsidl_formatEnumDef,
    fieldFormat=
        safe_text,
    index=
        safe_text,
    fieldFormatStr=
        safe_text
)
cjsidl_valueRange_strategy = st.builds(
    cjsidl_valueRange,
    upperLimit_type=
        safe_text,
    comment=
        safe_text,
    upperLim=
        safe_text,
    lowerLim=
        safe_text,
    lowerLimit_type=
        safe_text
)
cjsidl_scaledRangeDef_strategy = st.builds(
    cjsidl_scaledRangeDef,
    upperLim=
        safe_text,
    function=
        safe_text,
    lowerLim=
        safe_text,
    interp=
        safe_text
)
cjsidl_subField_strategy = st.builds(
    cjsidl_subField,
    toIndex=
        safe_text,
    fromIndex=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_taggedUnitsEnum_strategy = st.builds(
    cjsidl_taggedUnitsEnum,
    fieldUnit=
        safe_text,
    const_tag=
        safe_text,
    name=
        safe_text
)
cjsidl_valueSetDef_strategy = st.builds(
    cjsidl_valueSetDef,
    offset=
        safe_text
)
cjsidl_declaredEventDef_strategy = st.builds(
    cjsidl_declaredEventDef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_scopedType_strategy = st.builds(
    cjsidl_scopedType,
)
cjsidl_scopedConstId_strategy = st.builds(
    cjsidl_scopedConstId,
)
cjsidl_constReference_strategy = st.builds(
    cjsidl_constReference,
    comment=
        safe_text
)
cjsidl_footerScopedRef_strategy = st.builds(
    cjsidl_footerScopedRef,
)
cjsidl_footerRef_strategy = st.builds(
    cjsidl_footerRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_bodyScopedRef_strategy = st.builds(
    cjsidl_bodyScopedRef,
)
cjsidl_bodyRef_strategy = st.builds(
    cjsidl_bodyRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_headerScopedRef_strategy = st.builds(
    cjsidl_headerScopedRef,
)
cjsidl_headerRef_strategy = st.builds(
    cjsidl_headerRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_containerRef_strategy = st.builds(
    cjsidl_containerRef,
    name=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text
)
cjsidl_containerDef_strategy = st.builds(
    cjsidl_containerDef,
    optional=
        safe_text,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_footerDef_strategy = st.builds(
    cjsidl_footerDef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_bodyDef_strategy = st.builds(
    cjsidl_bodyDef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_headerDef_strategy = st.builds(
    cjsidl_headerDef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_varFormatField_strategy = st.builds(
    cjsidl_varFormatField,
    optional=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text,
    units=
        safe_text,
    countComment=
        safe_text
)
cjsidl_varLenField_strategy = st.builds(
    cjsidl_varLenField,
    upperLim=
        safe_text,
    countComment=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text,
    name=
        safe_text,
    fieldFormat=
        safe_text,
    lowerLim=
        safe_text
)
cjsidl_varLenString_strategy = st.builds(
    cjsidl_varLenString,
    lowerLim=
        safe_text,
    optional=
        safe_text,
    upperLim=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_fixedLenString_strategy = st.builds(
    cjsidl_fixedLenString,
    optional=
        safe_text,
    comment=
        safe_text,
    upperLim=
        safe_text,
    name=
        safe_text
)
cjsidl_bitfieldDef_strategy = st.builds(
    cjsidl_bitfieldDef,
    type=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text,
    name=
        safe_text
)
cjsidl_action_strategy = st.builds(
    cjsidl_action,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_varField_strategy = st.builds(
    cjsidl_varField,
    comment=
        safe_text,
    optional=
        safe_text,
    name=
        safe_text
)
cjsidl_fixedFieldDef_strategy = st.builds(
    cjsidl_fixedFieldDef,
    comment=
        safe_text,
    fieldUnit=
        safe_text,
    name=
        safe_text,
    optional=
        safe_text
)
cjsidl_sequenceDef_strategy = st.builds(
    cjsidl_sequenceDef,
)
cjsidl_variantDef_strategy = st.builds(
    cjsidl_variantDef,
    minCount=
        safe_text,
    maxCount=
        safe_text,
    vtagComment=
        safe_text
)
cjsidl_listDef_strategy = st.builds(
    cjsidl_listDef,
    maxCount=
        safe_text,
    countComment=
        safe_text,
    minCount=
        safe_text
)
cjsidl_recordDef_strategy = st.builds(
    cjsidl_recordDef,
)
cjsidl_arrayDef_strategy = st.builds(
    cjsidl_arrayDef,
    optional=
        safe_text,
    arraySize=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_simpleNumericType_strategy = st.builds(
    cjsidl_simpleNumericType,
    type=
        safe_text
)
cjsidl_simpleTransition_strategy = st.builds(
    cjsidl_simpleTransition,
    comment=
        safe_text
)
cjsidl_internalTransition_strategy = st.builds(
    cjsidl_internalTransition,
    comment=
        safe_text
)
cjsidl_guardAction_strategy = st.builds(
    cjsidl_guardAction,
    name=
        safe_text,
    not_=
        safe_text
)
cjsidl_guardParam_strategy = st.builds(
    cjsidl_guardParam,
    guardConst=
        safe_text
)
cjsidl_popTransition_strategy = st.builds(
    cjsidl_popTransition,
    comment=
        safe_text
)
cjsidl_pushTransition_strategy = st.builds(
    cjsidl_pushTransition,
    comment=
        safe_text
)
cjsidl_nextState_strategy = st.builds(
    cjsidl_nextState,
    comment=
        safe_text
)
cjsidl_sendActionList_strategy = st.builds(
    cjsidl_sendActionList,
)
cjsidl_actionList_strategy = st.builds(
    cjsidl_actionList,
)
cjsidl_defaultTransition_strategy = st.builds(
    cjsidl_defaultTransition,
    comment=
        safe_text,
    type=
        safe_text
)
cjsidl_guard_strategy = st.builds(
    cjsidl_guard,
    comment=
        safe_text,
    equiv=
        safe_text,
    logicalOperator=
        safe_text
)
cjsidl_scopedEventType_strategy = st.builds(
    cjsidl_scopedEventType,
)
cjsidl_transParam_strategy = st.builds(
    cjsidl_transParam,
    name=
        safe_text,
    comment=
        safe_text,
    unsignedType=
        safe_text
)
cjsidl_transParams_strategy = st.builds(
    cjsidl_transParams,
)
cjsidl_stateMachine_strategy = st.builds(
    cjsidl_stateMachine,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_eventDef_strategy = st.builds(
    cjsidl_eventDef,
    name=
        safe_text
)
cjsidl_transition_strategy = st.builds(
    cjsidl_transition,
    comment=
        safe_text,
    name=
        safe_text,
    type=
        safe_text
)
cjsidl_exit_strategy = st.builds(
    cjsidl_exit,
    comment=
        safe_text
)
cjsidl_entry_strategy = st.builds(
    cjsidl_entry,
    comment=
        safe_text
)
cjsidl_defaultState_strategy = st.builds(
    cjsidl_defaultState,
    comment=
        safe_text
)
cjsidl_state_strategy = st.builds(
    cjsidl_state,
    initial=
        safe_text,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_startState_strategy = st.builds(
    cjsidl_startState,
    comment=
        safe_text
)
cjsidl_constDef_strategy = st.builds(
    cjsidl_constDef,
    constValue=
        safe_text,
    comment=
        safe_text,
    fieldUnits=
        safe_text,
    name=
        safe_text
)
cjsidl_declaredConstSetRef_strategy = st.builds(
    cjsidl_declaredConstSetRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_messageScopedRef_strategy = st.builds(
    cjsidl_messageScopedRef,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_messageRef_strategy = st.builds(
    cjsidl_messageRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_messageDef_strategy = st.builds(
    cjsidl_messageDef,
    name=
        safe_text,
    command=
        safe_text,
    messageID=
        safe_text
)
cjsidl_messages_strategy = st.builds(
    cjsidl_messages,
)
cjsidl_scopedTypeId_strategy = st.builds(
    cjsidl_scopedTypeId,
    optional=
        safe_text,
    comment=
        safe_text,
    scopedName=
        safe_text
)
cjsidl_typeReference_strategy = st.builds(
    cjsidl_typeReference,
    name=
        safe_text,
    comment=
        safe_text,
    optional=
        safe_text
)
cjsidl_typeDef_strategy = st.builds(
    cjsidl_typeDef,
)
cjsidl_declaredTypeSetRef_strategy = st.builds(
    cjsidl_declaredTypeSetRef,
    name=
        safe_text,
    comment=
        safe_text
)
cjsidl_serviceDef_strategy = st.builds(
    cjsidl_serviceDef,
    assumpt=
        safe_text,
    name=
        safe_text,
    serviceVersion=
        safe_text,
    serviceName=
        safe_text
)
cjsidl_EObject_strategy = st.builds(
    cjsidl_EObject,
)
cjsidl_jaus_strategy = st.builds(
    cjsidl_jaus,
)
cjsidl_refAttr_strategy = st.builds(
    cjsidl_refAttr,
    comment=
        safe_text,
    name=
        safe_text
)
cjsidl_protocolBehavior_strategy = st.builds(
    cjsidl_protocolBehavior,
    comment=
        safe_text,
    stateless=
        safe_text
)
cjsidl_internalEventSet_strategy = st.builds(
    cjsidl_internalEventSet,
    comment=
        safe_text
)
cjsidl_messageSet_strategy = st.builds(
    cjsidl_messageSet,
    comment=
        safe_text,
    inputComment=
        safe_text,
    outputComment=
        safe_text
)
cjsidl_declaredTypeSet_strategy = st.builds(
    cjsidl_declaredTypeSet,
    name=
        safe_text,
    typeName=
        safe_text,
    version=
        safe_text
)
cjsidl_declaredConstSet_strategy = st.builds(
    cjsidl_declaredConstSet,
    constName=
        safe_text,
    name=
        safe_text,
    constSetVersion=
        safe_text
)
cjsidl_references_strategy = st.builds(
    cjsidl_references,
)
cjsidl_description_strategy = st.builds(
    cjsidl_description,
    content=
        safe_text
)

@given(instance=cjsidl_taggedItemDef_strategy)
@settings(max_examples=50)
def test_cjsidl_taggeditemdef_instantiation(instance):
    assert isinstance(instance, cjsidl_taggedItemDef)

@given(instance=cjsidl_valueSpec_strategy)
@settings(max_examples=50)
def test_cjsidl_valuespec_instantiation(instance):
    assert isinstance(instance, cjsidl_valueSpec)



@given(instance=cjsidl_valueSpec_strategy)
def test_cjsidl_valuespec_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=cjsidl_valueSpec_strategy)
def test_cjsidl_valuespec_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_valueSpec_strategy)
def test_cjsidl_valuespec_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=containerDef_strategy)
@settings(max_examples=50)
def test_containerdef_instantiation(instance):
    assert isinstance(instance, containerDef)

@given(instance=cjsidl_formatEnumDef_strategy)
@settings(max_examples=50)
def test_cjsidl_formatenumdef_instantiation(instance):
    assert isinstance(instance, cjsidl_formatEnumDef)



@given(instance=cjsidl_formatEnumDef_strategy)
def test_cjsidl_formatenumdef_fieldFormat_setter(instance):
    original = instance.fieldFormat
    instance.fieldFormat = original
    assert instance.fieldFormat == original



@given(instance=cjsidl_formatEnumDef_strategy)
def test_cjsidl_formatenumdef_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=cjsidl_formatEnumDef_strategy)
def test_cjsidl_formatenumdef_fieldFormatStr_setter(instance):
    original = instance.fieldFormatStr
    instance.fieldFormatStr = original
    assert instance.fieldFormatStr == original

@given(instance=cjsidl_valueRange_strategy)
@settings(max_examples=50)
def test_cjsidl_valuerange_instantiation(instance):
    assert isinstance(instance, cjsidl_valueRange)



@given(instance=cjsidl_valueRange_strategy)
def test_cjsidl_valuerange_upperLimit_type_setter(instance):
    original = instance.upperLimit_type
    instance.upperLimit_type = original
    assert instance.upperLimit_type == original



@given(instance=cjsidl_valueRange_strategy)
def test_cjsidl_valuerange_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_valueRange_strategy)
def test_cjsidl_valuerange_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original



@given(instance=cjsidl_valueRange_strategy)
def test_cjsidl_valuerange_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original



@given(instance=cjsidl_valueRange_strategy)
def test_cjsidl_valuerange_lowerLimit_type_setter(instance):
    original = instance.lowerLimit_type
    instance.lowerLimit_type = original
    assert instance.lowerLimit_type == original

@given(instance=cjsidl_scaledRangeDef_strategy)
@settings(max_examples=50)
def test_cjsidl_scaledrangedef_instantiation(instance):
    assert isinstance(instance, cjsidl_scaledRangeDef)



@given(instance=cjsidl_scaledRangeDef_strategy)
def test_cjsidl_scaledrangedef_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original



@given(instance=cjsidl_scaledRangeDef_strategy)
def test_cjsidl_scaledrangedef_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original



@given(instance=cjsidl_scaledRangeDef_strategy)
def test_cjsidl_scaledrangedef_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original



@given(instance=cjsidl_scaledRangeDef_strategy)
def test_cjsidl_scaledrangedef_interp_setter(instance):
    original = instance.interp
    instance.interp = original
    assert instance.interp == original

@given(instance=cjsidl_subField_strategy)
@settings(max_examples=50)
def test_cjsidl_subfield_instantiation(instance):
    assert isinstance(instance, cjsidl_subField)



@given(instance=cjsidl_subField_strategy)
def test_cjsidl_subfield_toIndex_setter(instance):
    original = instance.toIndex
    instance.toIndex = original
    assert instance.toIndex == original



@given(instance=cjsidl_subField_strategy)
def test_cjsidl_subfield_fromIndex_setter(instance):
    original = instance.fromIndex
    instance.fromIndex = original
    assert instance.fromIndex == original



@given(instance=cjsidl_subField_strategy)
def test_cjsidl_subfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_subField_strategy)
def test_cjsidl_subfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_taggedUnitsEnum_strategy)
@settings(max_examples=50)
def test_cjsidl_taggedunitsenum_instantiation(instance):
    assert isinstance(instance, cjsidl_taggedUnitsEnum)



@given(instance=cjsidl_taggedUnitsEnum_strategy)
def test_cjsidl_taggedunitsenum_fieldUnit_setter(instance):
    original = instance.fieldUnit
    instance.fieldUnit = original
    assert instance.fieldUnit == original



@given(instance=cjsidl_taggedUnitsEnum_strategy)
def test_cjsidl_taggedunitsenum_const_tag_setter(instance):
    original = instance.const_tag
    instance.const_tag = original
    assert instance.const_tag == original



@given(instance=cjsidl_taggedUnitsEnum_strategy)
def test_cjsidl_taggedunitsenum_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_valueSetDef_strategy)
@settings(max_examples=50)
def test_cjsidl_valuesetdef_instantiation(instance):
    assert isinstance(instance, cjsidl_valueSetDef)



@given(instance=cjsidl_valueSetDef_strategy)
def test_cjsidl_valuesetdef_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=cjsidl_declaredEventDef_strategy)
@settings(max_examples=50)
def test_cjsidl_declaredeventdef_instantiation(instance):
    assert isinstance(instance, cjsidl_declaredEventDef)



@given(instance=cjsidl_declaredEventDef_strategy)
def test_cjsidl_declaredeventdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_declaredEventDef_strategy)
def test_cjsidl_declaredeventdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_scopedType_strategy)
@settings(max_examples=50)
def test_cjsidl_scopedtype_instantiation(instance):
    assert isinstance(instance, cjsidl_scopedType)

@given(instance=cjsidl_scopedConstId_strategy)
@settings(max_examples=50)
def test_cjsidl_scopedconstid_instantiation(instance):
    assert isinstance(instance, cjsidl_scopedConstId)

@given(instance=cjsidl_constReference_strategy)
@settings(max_examples=50)
def test_cjsidl_constreference_instantiation(instance):
    assert isinstance(instance, cjsidl_constReference)



@given(instance=cjsidl_constReference_strategy)
def test_cjsidl_constreference_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_footerScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl_footerscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl_footerScopedRef)

@given(instance=cjsidl_footerRef_strategy)
@settings(max_examples=50)
def test_cjsidl_footerref_instantiation(instance):
    assert isinstance(instance, cjsidl_footerRef)



@given(instance=cjsidl_footerRef_strategy)
def test_cjsidl_footerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_footerRef_strategy)
def test_cjsidl_footerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_bodyScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl_bodyscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl_bodyScopedRef)

@given(instance=cjsidl_bodyRef_strategy)
@settings(max_examples=50)
def test_cjsidl_bodyref_instantiation(instance):
    assert isinstance(instance, cjsidl_bodyRef)



@given(instance=cjsidl_bodyRef_strategy)
def test_cjsidl_bodyref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_bodyRef_strategy)
def test_cjsidl_bodyref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_headerScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl_headerscopedref_instantiation(instance):
    assert isinstance(instance, cjsidl_headerScopedRef)

@given(instance=cjsidl_headerRef_strategy)
@settings(max_examples=50)
def test_cjsidl_headerref_instantiation(instance):
    assert isinstance(instance, cjsidl_headerRef)



@given(instance=cjsidl_headerRef_strategy)
def test_cjsidl_headerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_headerRef_strategy)
def test_cjsidl_headerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_containerRef_strategy)
@settings(max_examples=50)
def test_cjsidl_containerref_instantiation(instance):
    assert isinstance(instance, cjsidl_containerRef)



@given(instance=cjsidl_containerRef_strategy)
def test_cjsidl_containerref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_containerRef_strategy)
def test_cjsidl_containerref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_containerRef_strategy)
def test_cjsidl_containerref_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl_containerDef_strategy)
@settings(max_examples=50)
def test_cjsidl_containerdef_instantiation(instance):
    assert isinstance(instance, cjsidl_containerDef)



@given(instance=cjsidl_containerDef_strategy)
def test_cjsidl_containerdef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_containerDef_strategy)
def test_cjsidl_containerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_containerDef_strategy)
def test_cjsidl_containerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_footerDef_strategy)
@settings(max_examples=50)
def test_cjsidl_footerdef_instantiation(instance):
    assert isinstance(instance, cjsidl_footerDef)



@given(instance=cjsidl_footerDef_strategy)
def test_cjsidl_footerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_footerDef_strategy)
def test_cjsidl_footerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_bodyDef_strategy)
@settings(max_examples=50)
def test_cjsidl_bodydef_instantiation(instance):
    assert isinstance(instance, cjsidl_bodyDef)



@given(instance=cjsidl_bodyDef_strategy)
def test_cjsidl_bodydef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_bodyDef_strategy)
def test_cjsidl_bodydef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_headerDef_strategy)
@settings(max_examples=50)
def test_cjsidl_headerdef_instantiation(instance):
    assert isinstance(instance, cjsidl_headerDef)



@given(instance=cjsidl_headerDef_strategy)
def test_cjsidl_headerdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_headerDef_strategy)
def test_cjsidl_headerdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_varFormatField_strategy)
@settings(max_examples=50)
def test_cjsidl_varformatfield_instantiation(instance):
    assert isinstance(instance, cjsidl_varFormatField)



@given(instance=cjsidl_varFormatField_strategy)
def test_cjsidl_varformatfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_varFormatField_strategy)
def test_cjsidl_varformatfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_varFormatField_strategy)
def test_cjsidl_varformatfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_varFormatField_strategy)
def test_cjsidl_varformatfield_units_setter(instance):
    original = instance.units
    instance.units = original
    assert instance.units == original



@given(instance=cjsidl_varFormatField_strategy)
def test_cjsidl_varformatfield_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original

@given(instance=cjsidl_varLenField_strategy)
@settings(max_examples=50)
def test_cjsidl_varlenfield_instantiation(instance):
    assert isinstance(instance, cjsidl_varLenField)



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_fieldFormat_setter(instance):
    original = instance.fieldFormat
    instance.fieldFormat = original
    assert instance.fieldFormat == original



@given(instance=cjsidl_varLenField_strategy)
def test_cjsidl_varlenfield_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original

@given(instance=cjsidl_varLenString_strategy)
@settings(max_examples=50)
def test_cjsidl_varlenstring_instantiation(instance):
    assert isinstance(instance, cjsidl_varLenString)



@given(instance=cjsidl_varLenString_strategy)
def test_cjsidl_varlenstring_lowerLim_setter(instance):
    original = instance.lowerLim
    instance.lowerLim = original
    assert instance.lowerLim == original



@given(instance=cjsidl_varLenString_strategy)
def test_cjsidl_varlenstring_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_varLenString_strategy)
def test_cjsidl_varlenstring_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original



@given(instance=cjsidl_varLenString_strategy)
def test_cjsidl_varlenstring_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_varLenString_strategy)
def test_cjsidl_varlenstring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_fixedLenString_strategy)
@settings(max_examples=50)
def test_cjsidl_fixedlenstring_instantiation(instance):
    assert isinstance(instance, cjsidl_fixedLenString)



@given(instance=cjsidl_fixedLenString_strategy)
def test_cjsidl_fixedlenstring_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_fixedLenString_strategy)
def test_cjsidl_fixedlenstring_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_fixedLenString_strategy)
def test_cjsidl_fixedlenstring_upperLim_setter(instance):
    original = instance.upperLim
    instance.upperLim = original
    assert instance.upperLim == original



@given(instance=cjsidl_fixedLenString_strategy)
def test_cjsidl_fixedlenstring_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_bitfieldDef_strategy)
@settings(max_examples=50)
def test_cjsidl_bitfielddef_instantiation(instance):
    assert isinstance(instance, cjsidl_bitfieldDef)



@given(instance=cjsidl_bitfieldDef_strategy)
def test_cjsidl_bitfielddef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=cjsidl_bitfieldDef_strategy)
def test_cjsidl_bitfielddef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_bitfieldDef_strategy)
def test_cjsidl_bitfielddef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_bitfieldDef_strategy)
def test_cjsidl_bitfielddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_action_strategy)
@settings(max_examples=50)
def test_cjsidl_action_instantiation(instance):
    assert isinstance(instance, cjsidl_action)



@given(instance=cjsidl_action_strategy)
def test_cjsidl_action_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_action_strategy)
def test_cjsidl_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_varField_strategy)
@settings(max_examples=50)
def test_cjsidl_varfield_instantiation(instance):
    assert isinstance(instance, cjsidl_varField)



@given(instance=cjsidl_varField_strategy)
def test_cjsidl_varfield_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_varField_strategy)
def test_cjsidl_varfield_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_varField_strategy)
def test_cjsidl_varfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_fixedFieldDef_strategy)
@settings(max_examples=50)
def test_cjsidl_fixedfielddef_instantiation(instance):
    assert isinstance(instance, cjsidl_fixedFieldDef)



@given(instance=cjsidl_fixedFieldDef_strategy)
def test_cjsidl_fixedfielddef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_fixedFieldDef_strategy)
def test_cjsidl_fixedfielddef_fieldUnit_setter(instance):
    original = instance.fieldUnit
    instance.fieldUnit = original
    assert instance.fieldUnit == original



@given(instance=cjsidl_fixedFieldDef_strategy)
def test_cjsidl_fixedfielddef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_fixedFieldDef_strategy)
def test_cjsidl_fixedfielddef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl_sequenceDef_strategy)
@settings(max_examples=50)
def test_cjsidl_sequencedef_instantiation(instance):
    assert isinstance(instance, cjsidl_sequenceDef)

@given(instance=cjsidl_variantDef_strategy)
@settings(max_examples=50)
def test_cjsidl_variantdef_instantiation(instance):
    assert isinstance(instance, cjsidl_variantDef)



@given(instance=cjsidl_variantDef_strategy)
def test_cjsidl_variantdef_minCount_setter(instance):
    original = instance.minCount
    instance.minCount = original
    assert instance.minCount == original



@given(instance=cjsidl_variantDef_strategy)
def test_cjsidl_variantdef_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original



@given(instance=cjsidl_variantDef_strategy)
def test_cjsidl_variantdef_vtagComment_setter(instance):
    original = instance.vtagComment
    instance.vtagComment = original
    assert instance.vtagComment == original

@given(instance=cjsidl_listDef_strategy)
@settings(max_examples=50)
def test_cjsidl_listdef_instantiation(instance):
    assert isinstance(instance, cjsidl_listDef)



@given(instance=cjsidl_listDef_strategy)
def test_cjsidl_listdef_maxCount_setter(instance):
    original = instance.maxCount
    instance.maxCount = original
    assert instance.maxCount == original



@given(instance=cjsidl_listDef_strategy)
def test_cjsidl_listdef_countComment_setter(instance):
    original = instance.countComment
    instance.countComment = original
    assert instance.countComment == original



@given(instance=cjsidl_listDef_strategy)
def test_cjsidl_listdef_minCount_setter(instance):
    original = instance.minCount
    instance.minCount = original
    assert instance.minCount == original

@given(instance=cjsidl_recordDef_strategy)
@settings(max_examples=50)
def test_cjsidl_recorddef_instantiation(instance):
    assert isinstance(instance, cjsidl_recordDef)

@given(instance=cjsidl_arrayDef_strategy)
@settings(max_examples=50)
def test_cjsidl_arraydef_instantiation(instance):
    assert isinstance(instance, cjsidl_arrayDef)



@given(instance=cjsidl_arrayDef_strategy)
def test_cjsidl_arraydef_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_arrayDef_strategy)
def test_cjsidl_arraydef_arraySize_setter(instance):
    original = instance.arraySize
    instance.arraySize = original
    assert instance.arraySize == original



@given(instance=cjsidl_arrayDef_strategy)
def test_cjsidl_arraydef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_arrayDef_strategy)
def test_cjsidl_arraydef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_simpleNumericType_strategy)
@settings(max_examples=50)
def test_cjsidl_simplenumerictype_instantiation(instance):
    assert isinstance(instance, cjsidl_simpleNumericType)



@given(instance=cjsidl_simpleNumericType_strategy)
def test_cjsidl_simplenumerictype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl_simpleTransition_strategy)
@settings(max_examples=50)
def test_cjsidl_simpletransition_instantiation(instance):
    assert isinstance(instance, cjsidl_simpleTransition)



@given(instance=cjsidl_simpleTransition_strategy)
def test_cjsidl_simpletransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_internalTransition_strategy)
@settings(max_examples=50)
def test_cjsidl_internaltransition_instantiation(instance):
    assert isinstance(instance, cjsidl_internalTransition)



@given(instance=cjsidl_internalTransition_strategy)
def test_cjsidl_internaltransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_guardAction_strategy)
@settings(max_examples=50)
def test_cjsidl_guardaction_instantiation(instance):
    assert isinstance(instance, cjsidl_guardAction)



@given(instance=cjsidl_guardAction_strategy)
def test_cjsidl_guardaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_guardAction_strategy)
def test_cjsidl_guardaction_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=cjsidl_guardParam_strategy)
@settings(max_examples=50)
def test_cjsidl_guardparam_instantiation(instance):
    assert isinstance(instance, cjsidl_guardParam)



@given(instance=cjsidl_guardParam_strategy)
def test_cjsidl_guardparam_guardConst_setter(instance):
    original = instance.guardConst
    instance.guardConst = original
    assert instance.guardConst == original

@given(instance=cjsidl_popTransition_strategy)
@settings(max_examples=50)
def test_cjsidl_poptransition_instantiation(instance):
    assert isinstance(instance, cjsidl_popTransition)



@given(instance=cjsidl_popTransition_strategy)
def test_cjsidl_poptransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_pushTransition_strategy)
@settings(max_examples=50)
def test_cjsidl_pushtransition_instantiation(instance):
    assert isinstance(instance, cjsidl_pushTransition)



@given(instance=cjsidl_pushTransition_strategy)
def test_cjsidl_pushtransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_nextState_strategy)
@settings(max_examples=50)
def test_cjsidl_nextstate_instantiation(instance):
    assert isinstance(instance, cjsidl_nextState)



@given(instance=cjsidl_nextState_strategy)
def test_cjsidl_nextstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_sendActionList_strategy)
@settings(max_examples=50)
def test_cjsidl_sendactionlist_instantiation(instance):
    assert isinstance(instance, cjsidl_sendActionList)

@given(instance=cjsidl_actionList_strategy)
@settings(max_examples=50)
def test_cjsidl_actionlist_instantiation(instance):
    assert isinstance(instance, cjsidl_actionList)

@given(instance=cjsidl_defaultTransition_strategy)
@settings(max_examples=50)
def test_cjsidl_defaulttransition_instantiation(instance):
    assert isinstance(instance, cjsidl_defaultTransition)



@given(instance=cjsidl_defaultTransition_strategy)
def test_cjsidl_defaulttransition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_defaultTransition_strategy)
def test_cjsidl_defaulttransition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl_guard_strategy)
@settings(max_examples=50)
def test_cjsidl_guard_instantiation(instance):
    assert isinstance(instance, cjsidl_guard)



@given(instance=cjsidl_guard_strategy)
def test_cjsidl_guard_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_guard_strategy)
def test_cjsidl_guard_equiv_setter(instance):
    original = instance.equiv
    instance.equiv = original
    assert instance.equiv == original



@given(instance=cjsidl_guard_strategy)
def test_cjsidl_guard_logicalOperator_setter(instance):
    original = instance.logicalOperator
    instance.logicalOperator = original
    assert instance.logicalOperator == original

@given(instance=cjsidl_scopedEventType_strategy)
@settings(max_examples=50)
def test_cjsidl_scopedeventtype_instantiation(instance):
    assert isinstance(instance, cjsidl_scopedEventType)

@given(instance=cjsidl_transParam_strategy)
@settings(max_examples=50)
def test_cjsidl_transparam_instantiation(instance):
    assert isinstance(instance, cjsidl_transParam)



@given(instance=cjsidl_transParam_strategy)
def test_cjsidl_transparam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_transParam_strategy)
def test_cjsidl_transparam_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_transParam_strategy)
def test_cjsidl_transparam_unsignedType_setter(instance):
    original = instance.unsignedType
    instance.unsignedType = original
    assert instance.unsignedType == original

@given(instance=cjsidl_transParams_strategy)
@settings(max_examples=50)
def test_cjsidl_transparams_instantiation(instance):
    assert isinstance(instance, cjsidl_transParams)

@given(instance=cjsidl_stateMachine_strategy)
@settings(max_examples=50)
def test_cjsidl_statemachine_instantiation(instance):
    assert isinstance(instance, cjsidl_stateMachine)



@given(instance=cjsidl_stateMachine_strategy)
def test_cjsidl_statemachine_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_stateMachine_strategy)
def test_cjsidl_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_eventDef_strategy)
@settings(max_examples=50)
def test_cjsidl_eventdef_instantiation(instance):
    assert isinstance(instance, cjsidl_eventDef)



@given(instance=cjsidl_eventDef_strategy)
def test_cjsidl_eventdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_transition_strategy)
@settings(max_examples=50)
def test_cjsidl_transition_instantiation(instance):
    assert isinstance(instance, cjsidl_transition)



@given(instance=cjsidl_transition_strategy)
def test_cjsidl_transition_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_transition_strategy)
def test_cjsidl_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_transition_strategy)
def test_cjsidl_transition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=cjsidl_exit_strategy)
@settings(max_examples=50)
def test_cjsidl_exit_instantiation(instance):
    assert isinstance(instance, cjsidl_exit)



@given(instance=cjsidl_exit_strategy)
def test_cjsidl_exit_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_entry_strategy)
@settings(max_examples=50)
def test_cjsidl_entry_instantiation(instance):
    assert isinstance(instance, cjsidl_entry)



@given(instance=cjsidl_entry_strategy)
def test_cjsidl_entry_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_defaultState_strategy)
@settings(max_examples=50)
def test_cjsidl_defaultstate_instantiation(instance):
    assert isinstance(instance, cjsidl_defaultState)



@given(instance=cjsidl_defaultState_strategy)
def test_cjsidl_defaultstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_state_strategy)
@settings(max_examples=50)
def test_cjsidl_state_instantiation(instance):
    assert isinstance(instance, cjsidl_state)



@given(instance=cjsidl_state_strategy)
def test_cjsidl_state_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original



@given(instance=cjsidl_state_strategy)
def test_cjsidl_state_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_state_strategy)
def test_cjsidl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_startState_strategy)
@settings(max_examples=50)
def test_cjsidl_startstate_instantiation(instance):
    assert isinstance(instance, cjsidl_startState)



@given(instance=cjsidl_startState_strategy)
def test_cjsidl_startstate_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_constDef_strategy)
@settings(max_examples=50)
def test_cjsidl_constdef_instantiation(instance):
    assert isinstance(instance, cjsidl_constDef)



@given(instance=cjsidl_constDef_strategy)
def test_cjsidl_constdef_constValue_setter(instance):
    original = instance.constValue
    instance.constValue = original
    assert instance.constValue == original



@given(instance=cjsidl_constDef_strategy)
def test_cjsidl_constdef_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_constDef_strategy)
def test_cjsidl_constdef_fieldUnits_setter(instance):
    original = instance.fieldUnits
    instance.fieldUnits = original
    assert instance.fieldUnits == original



@given(instance=cjsidl_constDef_strategy)
def test_cjsidl_constdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_declaredConstSetRef_strategy)
@settings(max_examples=50)
def test_cjsidl_declaredconstsetref_instantiation(instance):
    assert isinstance(instance, cjsidl_declaredConstSetRef)



@given(instance=cjsidl_declaredConstSetRef_strategy)
def test_cjsidl_declaredconstsetref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_declaredConstSetRef_strategy)
def test_cjsidl_declaredconstsetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_messageScopedRef_strategy)
@settings(max_examples=50)
def test_cjsidl_messagescopedref_instantiation(instance):
    assert isinstance(instance, cjsidl_messageScopedRef)



@given(instance=cjsidl_messageScopedRef_strategy)
def test_cjsidl_messagescopedref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_messageScopedRef_strategy)
def test_cjsidl_messagescopedref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_messageRef_strategy)
@settings(max_examples=50)
def test_cjsidl_messageref_instantiation(instance):
    assert isinstance(instance, cjsidl_messageRef)



@given(instance=cjsidl_messageRef_strategy)
def test_cjsidl_messageref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_messageRef_strategy)
def test_cjsidl_messageref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_messageDef_strategy)
@settings(max_examples=50)
def test_cjsidl_messagedef_instantiation(instance):
    assert isinstance(instance, cjsidl_messageDef)



@given(instance=cjsidl_messageDef_strategy)
def test_cjsidl_messagedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_messageDef_strategy)
def test_cjsidl_messagedef_command_setter(instance):
    original = instance.command
    instance.command = original
    assert instance.command == original



@given(instance=cjsidl_messageDef_strategy)
def test_cjsidl_messagedef_messageID_setter(instance):
    original = instance.messageID
    instance.messageID = original
    assert instance.messageID == original

@given(instance=cjsidl_messages_strategy)
@settings(max_examples=50)
def test_cjsidl_messages_instantiation(instance):
    assert isinstance(instance, cjsidl_messages)

@given(instance=cjsidl_scopedTypeId_strategy)
@settings(max_examples=50)
def test_cjsidl_scopedtypeid_instantiation(instance):
    assert isinstance(instance, cjsidl_scopedTypeId)



@given(instance=cjsidl_scopedTypeId_strategy)
def test_cjsidl_scopedtypeid_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original



@given(instance=cjsidl_scopedTypeId_strategy)
def test_cjsidl_scopedtypeid_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_scopedTypeId_strategy)
def test_cjsidl_scopedtypeid_scopedName_setter(instance):
    original = instance.scopedName
    instance.scopedName = original
    assert instance.scopedName == original

@given(instance=cjsidl_typeReference_strategy)
@settings(max_examples=50)
def test_cjsidl_typereference_instantiation(instance):
    assert isinstance(instance, cjsidl_typeReference)



@given(instance=cjsidl_typeReference_strategy)
def test_cjsidl_typereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_typeReference_strategy)
def test_cjsidl_typereference_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_typeReference_strategy)
def test_cjsidl_typereference_optional_setter(instance):
    original = instance.optional
    instance.optional = original
    assert instance.optional == original

@given(instance=cjsidl_typeDef_strategy)
@settings(max_examples=50)
def test_cjsidl_typedef_instantiation(instance):
    assert isinstance(instance, cjsidl_typeDef)

@given(instance=cjsidl_declaredTypeSetRef_strategy)
@settings(max_examples=50)
def test_cjsidl_declaredtypesetref_instantiation(instance):
    assert isinstance(instance, cjsidl_declaredTypeSetRef)



@given(instance=cjsidl_declaredTypeSetRef_strategy)
def test_cjsidl_declaredtypesetref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_declaredTypeSetRef_strategy)
def test_cjsidl_declaredtypesetref_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_serviceDef_strategy)
@settings(max_examples=50)
def test_cjsidl_servicedef_instantiation(instance):
    assert isinstance(instance, cjsidl_serviceDef)



@given(instance=cjsidl_serviceDef_strategy)
def test_cjsidl_servicedef_assumpt_setter(instance):
    original = instance.assumpt
    instance.assumpt = original
    assert instance.assumpt == original



@given(instance=cjsidl_serviceDef_strategy)
def test_cjsidl_servicedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_serviceDef_strategy)
def test_cjsidl_servicedef_serviceVersion_setter(instance):
    original = instance.serviceVersion
    instance.serviceVersion = original
    assert instance.serviceVersion == original



@given(instance=cjsidl_serviceDef_strategy)
def test_cjsidl_servicedef_serviceName_setter(instance):
    original = instance.serviceName
    instance.serviceName = original
    assert instance.serviceName == original

@given(instance=cjsidl_EObject_strategy)
@settings(max_examples=50)
def test_cjsidl_eobject_instantiation(instance):
    assert isinstance(instance, cjsidl_EObject)

@given(instance=cjsidl_jaus_strategy)
@settings(max_examples=50)
def test_cjsidl_jaus_instantiation(instance):
    assert isinstance(instance, cjsidl_jaus)

@given(instance=cjsidl_refAttr_strategy)
@settings(max_examples=50)
def test_cjsidl_refattr_instantiation(instance):
    assert isinstance(instance, cjsidl_refAttr)



@given(instance=cjsidl_refAttr_strategy)
def test_cjsidl_refattr_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_refAttr_strategy)
def test_cjsidl_refattr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cjsidl_protocolBehavior_strategy)
@settings(max_examples=50)
def test_cjsidl_protocolbehavior_instantiation(instance):
    assert isinstance(instance, cjsidl_protocolBehavior)



@given(instance=cjsidl_protocolBehavior_strategy)
def test_cjsidl_protocolbehavior_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_protocolBehavior_strategy)
def test_cjsidl_protocolbehavior_stateless_setter(instance):
    original = instance.stateless
    instance.stateless = original
    assert instance.stateless == original

@given(instance=cjsidl_internalEventSet_strategy)
@settings(max_examples=50)
def test_cjsidl_internaleventset_instantiation(instance):
    assert isinstance(instance, cjsidl_internalEventSet)



@given(instance=cjsidl_internalEventSet_strategy)
def test_cjsidl_internaleventset_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cjsidl_messageSet_strategy)
@settings(max_examples=50)
def test_cjsidl_messageset_instantiation(instance):
    assert isinstance(instance, cjsidl_messageSet)



@given(instance=cjsidl_messageSet_strategy)
def test_cjsidl_messageset_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original



@given(instance=cjsidl_messageSet_strategy)
def test_cjsidl_messageset_inputComment_setter(instance):
    original = instance.inputComment
    instance.inputComment = original
    assert instance.inputComment == original



@given(instance=cjsidl_messageSet_strategy)
def test_cjsidl_messageset_outputComment_setter(instance):
    original = instance.outputComment
    instance.outputComment = original
    assert instance.outputComment == original

@given(instance=cjsidl_declaredTypeSet_strategy)
@settings(max_examples=50)
def test_cjsidl_declaredtypeset_instantiation(instance):
    assert isinstance(instance, cjsidl_declaredTypeSet)



@given(instance=cjsidl_declaredTypeSet_strategy)
def test_cjsidl_declaredtypeset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_declaredTypeSet_strategy)
def test_cjsidl_declaredtypeset_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original



@given(instance=cjsidl_declaredTypeSet_strategy)
def test_cjsidl_declaredtypeset_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=cjsidl_declaredConstSet_strategy)
@settings(max_examples=50)
def test_cjsidl_declaredconstset_instantiation(instance):
    assert isinstance(instance, cjsidl_declaredConstSet)



@given(instance=cjsidl_declaredConstSet_strategy)
def test_cjsidl_declaredconstset_constName_setter(instance):
    original = instance.constName
    instance.constName = original
    assert instance.constName == original



@given(instance=cjsidl_declaredConstSet_strategy)
def test_cjsidl_declaredconstset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cjsidl_declaredConstSet_strategy)
def test_cjsidl_declaredconstset_constSetVersion_setter(instance):
    original = instance.constSetVersion
    instance.constSetVersion = original
    assert instance.constSetVersion == original

@given(instance=cjsidl_references_strategy)
@settings(max_examples=50)
def test_cjsidl_references_instantiation(instance):
    assert isinstance(instance, cjsidl_references)

@given(instance=cjsidl_description_strategy)
@settings(max_examples=50)
def test_cjsidl_description_instantiation(instance):
    assert isinstance(instance, cjsidl_description)



@given(instance=cjsidl_description_strategy)
def test_cjsidl_description_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original
