import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypedElement,
    atlext_OCL_OclExpression,
    atlext_OCL_VariableDeclaration,
    OCL_atlext_Type,
    atlext_OCL_TypedElement,
    JavaBody,
    atlext_OCL_GetAppliedStereotypesBody,
    OclExpression,
    atlext_OCL_JavaBody,
    OutPatternElement,
    ResolveTempResolution,
    atlext_OCL_OperationCallExp,
    ContextHelper,
    Callable,
    OCL_atlext_EObject,
    atlext_OCL_PropertyCallExp,
    atlext_ATL_MatchedRule,
    atlext_ATL_StringToStringMap,
    StringToStringMap,
    ATL_atlext_EObject,
    MatchedRule,
    atlext_ATL_RuleResolutionInfo,
    RuleResolutionInfo,
    atlext_OCL_ResolveTempResolution,
    atlext_ATL_Binding,
    atlext_ATL_Helper,
    atlext_ATL_ContextHelper,
    VariableDeclaration,
    ATL_atlext_Type,
    atlext_ATL_CallableParameter,
    CallableParameter,
    PropertyCallExp,
    atlext_ATL_Callable,
    atlext_ATL_OutPatternElement,
    atlext_ATL_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_oclexpression_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_OclExpression)


def test_atlext_ocl_oclexpression_constructor_exists():
    assert callable(atlext_OCL_OclExpression.__init__)


def test_atlext_ocl_oclexpression_constructor_args():
    sig = inspect.signature(atlext_OCL_OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "implicitlyCasted" in params, "Missing parameter 'implicitlyCasted'"

def test_atlext_ocl_oclexpression_has_implicitlyCasted():
    assert hasattr(atlext_OCL_OclExpression, "implicitlyCasted")
    descriptor = None
    for klass in atlext_OCL_OclExpression.__mro__:
        if "implicitlyCasted" in klass.__dict__:
            descriptor = klass.__dict__["implicitlyCasted"]
            break
    assert isinstance(descriptor, property)



def test_atlext_ocl_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_VariableDeclaration)


def test_atlext_ocl_variabledeclaration_constructor_exists():
    assert callable(atlext_OCL_VariableDeclaration.__init__)


def test_atlext_ocl_variabledeclaration_constructor_args():
    sig = inspect.signature(atlext_OCL_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ocl_atlext_type_is_not_abstract():
    assert not inspect.isabstract(OCL_atlext_Type)


def test_ocl_atlext_type_constructor_exists():
    assert callable(OCL_atlext_Type.__init__)


def test_ocl_atlext_type_constructor_args():
    sig = inspect.signature(OCL_atlext_Type.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_typedelement_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_TypedElement)


def test_atlext_ocl_typedelement_constructor_exists():
    assert callable(atlext_OCL_TypedElement.__init__)


def test_atlext_ocl_typedelement_constructor_args():
    sig = inspect.signature(atlext_OCL_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_javabody_is_not_abstract():
    assert not inspect.isabstract(JavaBody)


def test_javabody_constructor_exists():
    assert callable(JavaBody.__init__)


def test_javabody_constructor_args():
    sig = inspect.signature(JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_getappliedstereotypesbody_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_GetAppliedStereotypesBody)


def test_atlext_ocl_getappliedstereotypesbody_constructor_exists():
    assert callable(atlext_OCL_GetAppliedStereotypesBody.__init__)


def test_atlext_ocl_getappliedstereotypesbody_constructor_args():
    sig = inspect.signature(atlext_OCL_GetAppliedStereotypesBody.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_javabody_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_JavaBody)


def test_atlext_ocl_javabody_constructor_exists():
    assert callable(atlext_OCL_JavaBody.__init__)


def test_atlext_ocl_javabody_constructor_args():
    sig = inspect.signature(atlext_OCL_JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(ResolveTempResolution)


def test_resolvetempresolution_constructor_exists():
    assert callable(ResolveTempResolution.__init__)


def test_resolvetempresolution_constructor_args():
    sig = inspect.signature(ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_OperationCallExp)


def test_atlext_ocl_operationcallexp_constructor_exists():
    assert callable(atlext_OCL_OperationCallExp.__init__)


def test_atlext_ocl_operationcallexp_constructor_args():
    sig = inspect.signature(atlext_OCL_OperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_contexthelper_is_not_abstract():
    assert not inspect.isabstract(ContextHelper)


def test_contexthelper_constructor_exists():
    assert callable(ContextHelper.__init__)


def test_contexthelper_constructor_args():
    sig = inspect.signature(ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_callable_is_not_abstract():
    assert not inspect.isabstract(Callable)


def test_callable_constructor_exists():
    assert callable(Callable.__init__)


def test_callable_constructor_args():
    sig = inspect.signature(Callable.__init__)
    params = list(sig.parameters.keys())



def test_ocl_atlext_eobject_is_not_abstract():
    assert not inspect.isabstract(OCL_atlext_EObject)


def test_ocl_atlext_eobject_constructor_exists():
    assert callable(OCL_atlext_EObject.__init__)


def test_ocl_atlext_eobject_constructor_args():
    sig = inspect.signature(OCL_atlext_EObject.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_PropertyCallExp)


def test_atlext_ocl_propertycallexp_constructor_exists():
    assert callable(atlext_OCL_PropertyCallExp.__init__)


def test_atlext_ocl_propertycallexp_constructor_args():
    sig = inspect.signature(atlext_OCL_PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStaticCall" in params, "Missing parameter 'isStaticCall'"

def test_atlext_ocl_propertycallexp_has_isStaticCall():
    assert hasattr(atlext_OCL_PropertyCallExp, "isStaticCall")
    descriptor = None
    for klass in atlext_OCL_PropertyCallExp.__mro__:
        if "isStaticCall" in klass.__dict__:
            descriptor = klass.__dict__["isStaticCall"]
            break
    assert isinstance(descriptor, property)



def test_atlext_atl_matchedrule_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_MatchedRule)


def test_atlext_atl_matchedrule_constructor_exists():
    assert callable(atlext_ATL_MatchedRule.__init__)


def test_atlext_atl_matchedrule_constructor_args():
    sig = inspect.signature(atlext_ATL_MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_StringToStringMap)


def test_atlext_atl_stringtostringmap_constructor_exists():
    assert callable(atlext_ATL_StringToStringMap.__init__)


def test_atlext_atl_stringtostringmap_constructor_args():
    sig = inspect.signature(atlext_ATL_StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_atlext_atl_stringtostringmap_has_value():
    assert hasattr(atlext_ATL_StringToStringMap, "value")
    descriptor = None
    for klass in atlext_ATL_StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_atlext_atl_stringtostringmap_has_key():
    assert hasattr(atlext_ATL_StringToStringMap, "key")
    descriptor = None
    for klass in atlext_ATL_StringToStringMap.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(StringToStringMap)


def test_stringtostringmap_constructor_exists():
    assert callable(StringToStringMap.__init__)


def test_stringtostringmap_constructor_args():
    sig = inspect.signature(StringToStringMap.__init__)
    params = list(sig.parameters.keys())



def test_atl_atlext_eobject_is_not_abstract():
    assert not inspect.isabstract(ATL_atlext_EObject)


def test_atl_atlext_eobject_constructor_exists():
    assert callable(ATL_atlext_EObject.__init__)


def test_atl_atlext_eobject_constructor_args():
    sig = inspect.signature(ATL_atlext_EObject.__init__)
    params = list(sig.parameters.keys())



def test_matchedrule_is_not_abstract():
    assert not inspect.isabstract(MatchedRule)


def test_matchedrule_constructor_exists():
    assert callable(MatchedRule.__init__)


def test_matchedrule_constructor_args():
    sig = inspect.signature(MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_RuleResolutionInfo)


def test_atlext_atl_ruleresolutioninfo_constructor_exists():
    assert callable(atlext_ATL_RuleResolutionInfo.__init__)


def test_atlext_atl_ruleresolutioninfo_constructor_args():
    sig = inspect.signature(atlext_ATL_RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(RuleResolutionInfo)


def test_ruleresolutioninfo_constructor_exists():
    assert callable(RuleResolutionInfo.__init__)


def test_ruleresolutioninfo_constructor_args():
    sig = inspect.signature(RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_atlext_ocl_resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(atlext_OCL_ResolveTempResolution)


def test_atlext_ocl_resolvetempresolution_constructor_exists():
    assert callable(atlext_OCL_ResolveTempResolution.__init__)


def test_atlext_ocl_resolvetempresolution_constructor_args():
    sig = inspect.signature(atlext_OCL_ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_binding_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_Binding)


def test_atlext_atl_binding_constructor_exists():
    assert callable(atlext_ATL_Binding.__init__)


def test_atlext_atl_binding_constructor_args():
    sig = inspect.signature(atlext_ATL_Binding.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_helper_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_Helper)


def test_atlext_atl_helper_constructor_exists():
    assert callable(atlext_ATL_Helper.__init__)


def test_atlext_atl_helper_constructor_args():
    sig = inspect.signature(atlext_ATL_Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isAttribute" in params, "Missing parameter 'isAttribute'"
    assert "hasContext" in params, "Missing parameter 'hasContext'"

def test_atlext_atl_helper_has_isAttribute():
    assert hasattr(atlext_ATL_Helper, "isAttribute")
    descriptor = None
    for klass in atlext_ATL_Helper.__mro__:
        if "isAttribute" in klass.__dict__:
            descriptor = klass.__dict__["isAttribute"]
            break
    assert isinstance(descriptor, property)

def test_atlext_atl_helper_has_hasContext():
    assert hasattr(atlext_ATL_Helper, "hasContext")
    descriptor = None
    for klass in atlext_ATL_Helper.__mro__:
        if "hasContext" in klass.__dict__:
            descriptor = klass.__dict__["hasContext"]
            break
    assert isinstance(descriptor, property)



def test_atlext_atl_contexthelper_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_ContextHelper)


def test_atlext_atl_contexthelper_constructor_exists():
    assert callable(atlext_ATL_ContextHelper.__init__)


def test_atlext_atl_contexthelper_constructor_args():
    sig = inspect.signature(atlext_ATL_ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atl_atlext_type_is_not_abstract():
    assert not inspect.isabstract(ATL_atlext_Type)


def test_atl_atlext_type_constructor_exists():
    assert callable(ATL_atlext_Type.__init__)


def test_atl_atlext_type_constructor_args():
    sig = inspect.signature(ATL_atlext_Type.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_callableparameter_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_CallableParameter)


def test_atlext_atl_callableparameter_constructor_exists():
    assert callable(atlext_ATL_CallableParameter.__init__)


def test_atlext_atl_callableparameter_constructor_args():
    sig = inspect.signature(atlext_ATL_CallableParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext_atl_callableparameter_has_name():
    assert hasattr(atlext_ATL_CallableParameter, "name")
    descriptor = None
    for klass in atlext_ATL_CallableParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_callableparameter_is_not_abstract():
    assert not inspect.isabstract(CallableParameter)


def test_callableparameter_constructor_exists():
    assert callable(CallableParameter.__init__)


def test_callableparameter_constructor_args():
    sig = inspect.signature(CallableParameter.__init__)
    params = list(sig.parameters.keys())



def test_propertycallexp_is_not_abstract():
    assert not inspect.isabstract(PropertyCallExp)


def test_propertycallexp_constructor_exists():
    assert callable(PropertyCallExp.__init__)


def test_propertycallexp_constructor_args():
    sig = inspect.signature(PropertyCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_callable_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_Callable)


def test_atlext_atl_callable_constructor_exists():
    assert callable(atlext_ATL_Callable.__init__)


def test_atlext_atl_callable_constructor_args():
    sig = inspect.signature(atlext_ATL_Callable.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_OutPatternElement)


def test_atlext_atl_outpatternelement_constructor_exists():
    assert callable(atlext_ATL_OutPatternElement.__init__)


def test_atlext_atl_outpatternelement_constructor_args():
    sig = inspect.signature(atlext_ATL_OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext_atl_locatedelement_is_not_abstract():
    assert not inspect.isabstract(atlext_ATL_LocatedElement)


def test_atlext_atl_locatedelement_constructor_exists():
    assert callable(atlext_ATL_LocatedElement.__init__)


def test_atlext_atl_locatedelement_constructor_args():
    sig = inspect.signature(atlext_ATL_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "fileObject" in params, "Missing parameter 'fileObject'"
    assert "fileLocation" in params, "Missing parameter 'fileLocation'"

def test_atlext_atl_locatedelement_has_fileObject():
    assert hasattr(atlext_ATL_LocatedElement, "fileObject")
    descriptor = None
    for klass in atlext_ATL_LocatedElement.__mro__:
        if "fileObject" in klass.__dict__:
            descriptor = klass.__dict__["fileObject"]
            break
    assert isinstance(descriptor, property)

def test_atlext_atl_locatedelement_has_fileLocation():
    assert hasattr(atlext_ATL_LocatedElement, "fileLocation")
    descriptor = None
    for klass in atlext_ATL_LocatedElement.__mro__:
        if "fileLocation" in klass.__dict__:
            descriptor = klass.__dict__["fileLocation"]
            break
    assert isinstance(descriptor, property)


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
TypedElement_strategy = st.builds(
    TypedElement,
)
atlext_OCL_OclExpression_strategy = st.builds(
    atlext_OCL_OclExpression,
    implicitlyCasted=
        st.booleans()
)
atlext_OCL_VariableDeclaration_strategy = st.builds(
    atlext_OCL_VariableDeclaration,
)
OCL_atlext_Type_strategy = st.builds(
    OCL_atlext_Type,
)
atlext_OCL_TypedElement_strategy = st.builds(
    atlext_OCL_TypedElement,
)
JavaBody_strategy = st.builds(
    JavaBody,
)
atlext_OCL_GetAppliedStereotypesBody_strategy = st.builds(
    atlext_OCL_GetAppliedStereotypesBody,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atlext_OCL_JavaBody_strategy = st.builds(
    atlext_OCL_JavaBody,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
ResolveTempResolution_strategy = st.builds(
    ResolveTempResolution,
)
atlext_OCL_OperationCallExp_strategy = st.builds(
    atlext_OCL_OperationCallExp,
)
ContextHelper_strategy = st.builds(
    ContextHelper,
)
Callable_strategy = st.builds(
    Callable,
)
OCL_atlext_EObject_strategy = st.builds(
    OCL_atlext_EObject,
)
atlext_OCL_PropertyCallExp_strategy = st.builds(
    atlext_OCL_PropertyCallExp,
    isStaticCall=
        st.booleans()
)
atlext_ATL_MatchedRule_strategy = st.builds(
    atlext_ATL_MatchedRule,
)
atlext_ATL_StringToStringMap_strategy = st.builds(
    atlext_ATL_StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
StringToStringMap_strategy = st.builds(
    StringToStringMap,
)
ATL_atlext_EObject_strategy = st.builds(
    ATL_atlext_EObject,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
atlext_ATL_RuleResolutionInfo_strategy = st.builds(
    atlext_ATL_RuleResolutionInfo,
)
RuleResolutionInfo_strategy = st.builds(
    RuleResolutionInfo,
)
atlext_OCL_ResolveTempResolution_strategy = st.builds(
    atlext_OCL_ResolveTempResolution,
)
atlext_ATL_Binding_strategy = st.builds(
    atlext_ATL_Binding,
)
atlext_ATL_Helper_strategy = st.builds(
    atlext_ATL_Helper,
    isAttribute=
        st.booleans(),
    hasContext=
        st.booleans()
)
atlext_ATL_ContextHelper_strategy = st.builds(
    atlext_ATL_ContextHelper,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ATL_atlext_Type_strategy = st.builds(
    ATL_atlext_Type,
)
atlext_ATL_CallableParameter_strategy = st.builds(
    atlext_ATL_CallableParameter,
    name=
        safe_text
)
CallableParameter_strategy = st.builds(
    CallableParameter,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
atlext_ATL_Callable_strategy = st.builds(
    atlext_ATL_Callable,
)
atlext_ATL_OutPatternElement_strategy = st.builds(
    atlext_ATL_OutPatternElement,
)
atlext_ATL_LocatedElement_strategy = st.builds(
    atlext_ATL_LocatedElement,
    fileObject=
        safe_text,
    fileLocation=
        safe_text
)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=atlext_OCL_OclExpression_strategy)
@settings(max_examples=50)
def test_atlext_ocl_oclexpression_instantiation(instance):
    assert isinstance(instance, atlext_OCL_OclExpression)



@given(instance=atlext_OCL_OclExpression_strategy)
def test_atlext_ocl_oclexpression_implicitlyCasted_setter(instance):
    original = instance.implicitlyCasted
    instance.implicitlyCasted = original
    assert instance.implicitlyCasted == original

@given(instance=atlext_OCL_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlext_ocl_variabledeclaration_instantiation(instance):
    assert isinstance(instance, atlext_OCL_VariableDeclaration)

@given(instance=OCL_atlext_Type_strategy)
@settings(max_examples=50)
def test_ocl_atlext_type_instantiation(instance):
    assert isinstance(instance, OCL_atlext_Type)

@given(instance=atlext_OCL_TypedElement_strategy)
@settings(max_examples=50)
def test_atlext_ocl_typedelement_instantiation(instance):
    assert isinstance(instance, atlext_OCL_TypedElement)

@given(instance=JavaBody_strategy)
@settings(max_examples=50)
def test_javabody_instantiation(instance):
    assert isinstance(instance, JavaBody)

@given(instance=atlext_OCL_GetAppliedStereotypesBody_strategy)
@settings(max_examples=50)
def test_atlext_ocl_getappliedstereotypesbody_instantiation(instance):
    assert isinstance(instance, atlext_OCL_GetAppliedStereotypesBody)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atlext_OCL_JavaBody_strategy)
@settings(max_examples=50)
def test_atlext_ocl_javabody_instantiation(instance):
    assert isinstance(instance, atlext_OCL_JavaBody)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_resolvetempresolution_instantiation(instance):
    assert isinstance(instance, ResolveTempResolution)

@given(instance=atlext_OCL_OperationCallExp_strategy)
@settings(max_examples=50)
def test_atlext_ocl_operationcallexp_instantiation(instance):
    assert isinstance(instance, atlext_OCL_OperationCallExp)

@given(instance=ContextHelper_strategy)
@settings(max_examples=50)
def test_contexthelper_instantiation(instance):
    assert isinstance(instance, ContextHelper)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=OCL_atlext_EObject_strategy)
@settings(max_examples=50)
def test_ocl_atlext_eobject_instantiation(instance):
    assert isinstance(instance, OCL_atlext_EObject)

@given(instance=atlext_OCL_PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atlext_ocl_propertycallexp_instantiation(instance):
    assert isinstance(instance, atlext_OCL_PropertyCallExp)



@given(instance=atlext_OCL_PropertyCallExp_strategy)
def test_atlext_ocl_propertycallexp_isStaticCall_setter(instance):
    original = instance.isStaticCall
    instance.isStaticCall = original
    assert instance.isStaticCall == original

@given(instance=atlext_ATL_MatchedRule_strategy)
@settings(max_examples=50)
def test_atlext_atl_matchedrule_instantiation(instance):
    assert isinstance(instance, atlext_ATL_MatchedRule)

@given(instance=atlext_ATL_StringToStringMap_strategy)
@settings(max_examples=50)
def test_atlext_atl_stringtostringmap_instantiation(instance):
    assert isinstance(instance, atlext_ATL_StringToStringMap)



@given(instance=atlext_ATL_StringToStringMap_strategy)
def test_atlext_atl_stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=atlext_ATL_StringToStringMap_strategy)
def test_atlext_atl_stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=StringToStringMap_strategy)
@settings(max_examples=50)
def test_stringtostringmap_instantiation(instance):
    assert isinstance(instance, StringToStringMap)

@given(instance=ATL_atlext_EObject_strategy)
@settings(max_examples=50)
def test_atl_atlext_eobject_instantiation(instance):
    assert isinstance(instance, ATL_atlext_EObject)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=atlext_ATL_RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_atlext_atl_ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, atlext_ATL_RuleResolutionInfo)

@given(instance=RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, RuleResolutionInfo)

@given(instance=atlext_OCL_ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_atlext_ocl_resolvetempresolution_instantiation(instance):
    assert isinstance(instance, atlext_OCL_ResolveTempResolution)

@given(instance=atlext_ATL_Binding_strategy)
@settings(max_examples=50)
def test_atlext_atl_binding_instantiation(instance):
    assert isinstance(instance, atlext_ATL_Binding)

@given(instance=atlext_ATL_Helper_strategy)
@settings(max_examples=50)
def test_atlext_atl_helper_instantiation(instance):
    assert isinstance(instance, atlext_ATL_Helper)



@given(instance=atlext_ATL_Helper_strategy)
def test_atlext_atl_helper_isAttribute_setter(instance):
    original = instance.isAttribute
    instance.isAttribute = original
    assert instance.isAttribute == original



@given(instance=atlext_ATL_Helper_strategy)
def test_atlext_atl_helper_hasContext_setter(instance):
    original = instance.hasContext
    instance.hasContext = original
    assert instance.hasContext == original

@given(instance=atlext_ATL_ContextHelper_strategy)
@settings(max_examples=50)
def test_atlext_atl_contexthelper_instantiation(instance):
    assert isinstance(instance, atlext_ATL_ContextHelper)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ATL_atlext_Type_strategy)
@settings(max_examples=50)
def test_atl_atlext_type_instantiation(instance):
    assert isinstance(instance, ATL_atlext_Type)

@given(instance=atlext_ATL_CallableParameter_strategy)
@settings(max_examples=50)
def test_atlext_atl_callableparameter_instantiation(instance):
    assert isinstance(instance, atlext_ATL_CallableParameter)



@given(instance=atlext_ATL_CallableParameter_strategy)
def test_atlext_atl_callableparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CallableParameter_strategy)
@settings(max_examples=50)
def test_callableparameter_instantiation(instance):
    assert isinstance(instance, CallableParameter)

@given(instance=PropertyCallExp_strategy)
@settings(max_examples=50)
def test_propertycallexp_instantiation(instance):
    assert isinstance(instance, PropertyCallExp)

@given(instance=atlext_ATL_Callable_strategy)
@settings(max_examples=50)
def test_atlext_atl_callable_instantiation(instance):
    assert isinstance(instance, atlext_ATL_Callable)

@given(instance=atlext_ATL_OutPatternElement_strategy)
@settings(max_examples=50)
def test_atlext_atl_outpatternelement_instantiation(instance):
    assert isinstance(instance, atlext_ATL_OutPatternElement)

@given(instance=atlext_ATL_LocatedElement_strategy)
@settings(max_examples=50)
def test_atlext_atl_locatedelement_instantiation(instance):
    assert isinstance(instance, atlext_ATL_LocatedElement)



@given(instance=atlext_ATL_LocatedElement_strategy)
def test_atlext_atl_locatedelement_fileObject_setter(instance):
    original = instance.fileObject
    instance.fileObject = original
    assert instance.fileObject == original



@given(instance=atlext_ATL_LocatedElement_strategy)
def test_atlext_atl_locatedelement_fileLocation_setter(instance):
    original = instance.fileLocation
    instance.fileLocation = original
    assert instance.fileLocation == original
