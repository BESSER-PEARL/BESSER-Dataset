import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    atlext::OCL::CollectionOperationCallExp,
    ResolveTempResolution,
    atlext::OCL::OperationCallExp,
    ContextHelper,
    Callable,
    OCL::atlext::EObject,
    atlext::OCL::PropertyCallExp,
    TypedElement,
    atlext::OCL::OclExpression,
    atlext::OCL::VariableDeclaration,
    OCL::atlext::Type,
    atlext::OCL::TypedElement,
    MatchedRule,
    atlext::ATL::RuleResolutionInfo,
    CollectionOperationCallExp,
    atlext::OCL2::SelectByKind,
    JavaBody,
    atlext::OCL::GetAppliedStereotypesBody,
    OclExpression,
    atlext::OCL::JavaBody,
    OutPatternElement,
    atlext::ATL::Helper,
    atlext::ATL::ContextHelper,
    VariableDeclaration,
    ATL::atlext::Type,
    atlext::ATL::CallableParameter,
    CallableParameter,
    PropertyCallExp,
    atlext::ATL::Callable,
    atlext::ATL::OutPatternElement,
    atlext::ATL::MatchedRule,
    atlext::ATL::StringToStringMap,
    StringToStringMap,
    ATL::atlext::EObject,
    RuleResolutionInfo,
    atlext::OCL::ResolveTempResolution,
    atlext::ATL::LocatedElement,
    atlext::ATL::Binding,
    RuleResolutionStatus,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_atlext::ocl::collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::CollectionOperationCallExp)


def test_atlext::ocl::collectionoperationcallexp_constructor_exists():
    assert callable(atlext::OCL::CollectionOperationCallExp.__init__)


def test_atlext::ocl::collectionoperationcallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(ResolveTempResolution)


def test_resolvetempresolution_constructor_exists():
    assert callable(ResolveTempResolution.__init__)


def test_resolvetempresolution_constructor_args():
    sig = inspect.signature(ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::operationcallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OperationCallExp)


def test_atlext::ocl::operationcallexp_constructor_exists():
    assert callable(atlext::OCL::OperationCallExp.__init__)


def test_atlext::ocl::operationcallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::OperationCallExp.__init__)
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



def test_ocl::atlext::eobject_is_not_abstract():
    assert not inspect.isabstract(OCL::atlext::EObject)


def test_ocl::atlext::eobject_constructor_exists():
    assert callable(OCL::atlext::EObject.__init__)


def test_ocl::atlext::eobject_constructor_args():
    sig = inspect.signature(OCL::atlext::EObject.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::propertycallexp_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::PropertyCallExp)


def test_atlext::ocl::propertycallexp_constructor_exists():
    assert callable(atlext::OCL::PropertyCallExp.__init__)


def test_atlext::ocl::propertycallexp_constructor_args():
    sig = inspect.signature(atlext::OCL::PropertyCallExp.__init__)
    params = list(sig.parameters.keys())
    assert "isStaticCall" in params, "Missing parameter 'isStaticCall'"

def test_atlext::ocl::propertycallexp_has_isStaticCall():
    assert hasattr(atlext::OCL::PropertyCallExp, "isStaticCall")
    descriptor = None
    for klass in atlext::OCL::PropertyCallExp.__mro__:
        if "isStaticCall" in klass.__dict__:
            descriptor = klass.__dict__["isStaticCall"]
            break
    assert isinstance(descriptor, property)



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::oclexpression_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::OclExpression)


def test_atlext::ocl::oclexpression_constructor_exists():
    assert callable(atlext::OCL::OclExpression.__init__)


def test_atlext::ocl::oclexpression_constructor_args():
    sig = inspect.signature(atlext::OCL::OclExpression.__init__)
    params = list(sig.parameters.keys())
    assert "implicitlyCasted" in params, "Missing parameter 'implicitlyCasted'"

def test_atlext::ocl::oclexpression_has_implicitlyCasted():
    assert hasattr(atlext::OCL::OclExpression, "implicitlyCasted")
    descriptor = None
    for klass in atlext::OCL::OclExpression.__mro__:
        if "implicitlyCasted" in klass.__dict__:
            descriptor = klass.__dict__["implicitlyCasted"]
            break
    assert isinstance(descriptor, property)



def test_atlext::ocl::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::VariableDeclaration)


def test_atlext::ocl::variabledeclaration_constructor_exists():
    assert callable(atlext::OCL::VariableDeclaration.__init__)


def test_atlext::ocl::variabledeclaration_constructor_args():
    sig = inspect.signature(atlext::OCL::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ocl::atlext::type_is_not_abstract():
    assert not inspect.isabstract(OCL::atlext::Type)


def test_ocl::atlext::type_constructor_exists():
    assert callable(OCL::atlext::Type.__init__)


def test_ocl::atlext::type_constructor_args():
    sig = inspect.signature(OCL::atlext::Type.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::typedelement_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::TypedElement)


def test_atlext::ocl::typedelement_constructor_exists():
    assert callable(atlext::OCL::TypedElement.__init__)


def test_atlext::ocl::typedelement_constructor_args():
    sig = inspect.signature(atlext::OCL::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_matchedrule_is_not_abstract():
    assert not inspect.isabstract(MatchedRule)


def test_matchedrule_constructor_exists():
    assert callable(MatchedRule.__init__)


def test_matchedrule_constructor_args():
    sig = inspect.signature(MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::RuleResolutionInfo)


def test_atlext::atl::ruleresolutioninfo_constructor_exists():
    assert callable(atlext::ATL::RuleResolutionInfo.__init__)


def test_atlext::atl::ruleresolutioninfo_constructor_args():
    sig = inspect.signature(atlext::ATL::RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"

def test_atlext::atl::ruleresolutioninfo_has_status():
    assert hasattr(atlext::ATL::RuleResolutionInfo, "status")
    descriptor = None
    for klass in atlext::ATL::RuleResolutionInfo.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_collectionoperationcallexp_is_not_abstract():
    assert not inspect.isabstract(CollectionOperationCallExp)


def test_collectionoperationcallexp_constructor_exists():
    assert callable(CollectionOperationCallExp.__init__)


def test_collectionoperationcallexp_constructor_args():
    sig = inspect.signature(CollectionOperationCallExp.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl2::selectbykind_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL2::SelectByKind)


def test_atlext::ocl2::selectbykind_constructor_exists():
    assert callable(atlext::OCL2::SelectByKind.__init__)


def test_atlext::ocl2::selectbykind_constructor_args():
    sig = inspect.signature(atlext::OCL2::SelectByKind.__init__)
    params = list(sig.parameters.keys())
    assert "isExact" in params, "Missing parameter 'isExact'"

def test_atlext::ocl2::selectbykind_has_isExact():
    assert hasattr(atlext::OCL2::SelectByKind, "isExact")
    descriptor = None
    for klass in atlext::OCL2::SelectByKind.__mro__:
        if "isExact" in klass.__dict__:
            descriptor = klass.__dict__["isExact"]
            break
    assert isinstance(descriptor, property)



def test_javabody_is_not_abstract():
    assert not inspect.isabstract(JavaBody)


def test_javabody_constructor_exists():
    assert callable(JavaBody.__init__)


def test_javabody_constructor_args():
    sig = inspect.signature(JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::getappliedstereotypesbody_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::GetAppliedStereotypesBody)


def test_atlext::ocl::getappliedstereotypesbody_constructor_exists():
    assert callable(atlext::OCL::GetAppliedStereotypesBody.__init__)


def test_atlext::ocl::getappliedstereotypesbody_constructor_args():
    sig = inspect.signature(atlext::OCL::GetAppliedStereotypesBody.__init__)
    params = list(sig.parameters.keys())



def test_oclexpression_is_not_abstract():
    assert not inspect.isabstract(OclExpression)


def test_oclexpression_constructor_exists():
    assert callable(OclExpression.__init__)


def test_oclexpression_constructor_args():
    sig = inspect.signature(OclExpression.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::javabody_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::JavaBody)


def test_atlext::ocl::javabody_constructor_exists():
    assert callable(atlext::OCL::JavaBody.__init__)


def test_atlext::ocl::javabody_constructor_args():
    sig = inspect.signature(atlext::OCL::JavaBody.__init__)
    params = list(sig.parameters.keys())



def test_outpatternelement_is_not_abstract():
    assert not inspect.isabstract(OutPatternElement)


def test_outpatternelement_constructor_exists():
    assert callable(OutPatternElement.__init__)


def test_outpatternelement_constructor_args():
    sig = inspect.signature(OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::helper_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Helper)


def test_atlext::atl::helper_constructor_exists():
    assert callable(atlext::ATL::Helper.__init__)


def test_atlext::atl::helper_constructor_args():
    sig = inspect.signature(atlext::ATL::Helper.__init__)
    params = list(sig.parameters.keys())
    assert "isAttribute" in params, "Missing parameter 'isAttribute'"
    assert "hasContext" in params, "Missing parameter 'hasContext'"

def test_atlext::atl::helper_has_isAttribute():
    assert hasattr(atlext::ATL::Helper, "isAttribute")
    descriptor = None
    for klass in atlext::ATL::Helper.__mro__:
        if "isAttribute" in klass.__dict__:
            descriptor = klass.__dict__["isAttribute"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::helper_has_hasContext():
    assert hasattr(atlext::ATL::Helper, "hasContext")
    descriptor = None
    for klass in atlext::ATL::Helper.__mro__:
        if "hasContext" in klass.__dict__:
            descriptor = klass.__dict__["hasContext"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::contexthelper_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::ContextHelper)


def test_atlext::atl::contexthelper_constructor_exists():
    assert callable(atlext::ATL::ContextHelper.__init__)


def test_atlext::atl::contexthelper_constructor_args():
    sig = inspect.signature(atlext::ATL::ContextHelper.__init__)
    params = list(sig.parameters.keys())



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_atl::atlext::type_is_not_abstract():
    assert not inspect.isabstract(ATL::atlext::Type)


def test_atl::atlext::type_constructor_exists():
    assert callable(ATL::atlext::Type.__init__)


def test_atl::atlext::type_constructor_args():
    sig = inspect.signature(ATL::atlext::Type.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::callableparameter_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::CallableParameter)


def test_atlext::atl::callableparameter_constructor_exists():
    assert callable(atlext::ATL::CallableParameter.__init__)


def test_atlext::atl::callableparameter_constructor_args():
    sig = inspect.signature(atlext::ATL::CallableParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_atlext::atl::callableparameter_has_name():
    assert hasattr(atlext::ATL::CallableParameter, "name")
    descriptor = None
    for klass in atlext::ATL::CallableParameter.__mro__:
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



def test_atlext::atl::callable_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Callable)


def test_atlext::atl::callable_constructor_exists():
    assert callable(atlext::ATL::Callable.__init__)


def test_atlext::atl::callable_constructor_args():
    sig = inspect.signature(atlext::ATL::Callable.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::outpatternelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::OutPatternElement)


def test_atlext::atl::outpatternelement_constructor_exists():
    assert callable(atlext::ATL::OutPatternElement.__init__)


def test_atlext::atl::outpatternelement_constructor_args():
    sig = inspect.signature(atlext::ATL::OutPatternElement.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::matchedrule_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::MatchedRule)


def test_atlext::atl::matchedrule_constructor_exists():
    assert callable(atlext::ATL::MatchedRule.__init__)


def test_atlext::atl::matchedrule_constructor_args():
    sig = inspect.signature(atlext::ATL::MatchedRule.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::stringtostringmap_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::StringToStringMap)


def test_atlext::atl::stringtostringmap_constructor_exists():
    assert callable(atlext::ATL::StringToStringMap.__init__)


def test_atlext::atl::stringtostringmap_constructor_args():
    sig = inspect.signature(atlext::ATL::StringToStringMap.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "key" in params, "Missing parameter 'key'"

def test_atlext::atl::stringtostringmap_has_value():
    assert hasattr(atlext::ATL::StringToStringMap, "value")
    descriptor = None
    for klass in atlext::ATL::StringToStringMap.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::stringtostringmap_has_key():
    assert hasattr(atlext::ATL::StringToStringMap, "key")
    descriptor = None
    for klass in atlext::ATL::StringToStringMap.__mro__:
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



def test_atl::atlext::eobject_is_not_abstract():
    assert not inspect.isabstract(ATL::atlext::EObject)


def test_atl::atlext::eobject_constructor_exists():
    assert callable(ATL::atlext::EObject.__init__)


def test_atl::atlext::eobject_constructor_args():
    sig = inspect.signature(ATL::atlext::EObject.__init__)
    params = list(sig.parameters.keys())



def test_ruleresolutioninfo_is_not_abstract():
    assert not inspect.isabstract(RuleResolutionInfo)


def test_ruleresolutioninfo_constructor_exists():
    assert callable(RuleResolutionInfo.__init__)


def test_ruleresolutioninfo_constructor_args():
    sig = inspect.signature(RuleResolutionInfo.__init__)
    params = list(sig.parameters.keys())



def test_atlext::ocl::resolvetempresolution_is_not_abstract():
    assert not inspect.isabstract(atlext::OCL::ResolveTempResolution)


def test_atlext::ocl::resolvetempresolution_constructor_exists():
    assert callable(atlext::OCL::ResolveTempResolution.__init__)


def test_atlext::ocl::resolvetempresolution_constructor_args():
    sig = inspect.signature(atlext::OCL::ResolveTempResolution.__init__)
    params = list(sig.parameters.keys())



def test_atlext::atl::locatedelement_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::LocatedElement)


def test_atlext::atl::locatedelement_constructor_exists():
    assert callable(atlext::ATL::LocatedElement.__init__)


def test_atlext::atl::locatedelement_constructor_args():
    sig = inspect.signature(atlext::ATL::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "fileLocation" in params, "Missing parameter 'fileLocation'"
    assert "fileObject" in params, "Missing parameter 'fileObject'"

def test_atlext::atl::locatedelement_has_fileLocation():
    assert hasattr(atlext::ATL::LocatedElement, "fileLocation")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "fileLocation" in klass.__dict__:
            descriptor = klass.__dict__["fileLocation"]
            break
    assert isinstance(descriptor, property)

def test_atlext::atl::locatedelement_has_fileObject():
    assert hasattr(atlext::ATL::LocatedElement, "fileObject")
    descriptor = None
    for klass in atlext::ATL::LocatedElement.__mro__:
        if "fileObject" in klass.__dict__:
            descriptor = klass.__dict__["fileObject"]
            break
    assert isinstance(descriptor, property)



def test_atlext::atl::binding_is_not_abstract():
    assert not inspect.isabstract(atlext::ATL::Binding)


def test_atlext::atl::binding_constructor_exists():
    assert callable(atlext::ATL::Binding.__init__)


def test_atlext::atl::binding_constructor_args():
    sig = inspect.signature(atlext::ATL::Binding.__init__)
    params = list(sig.parameters.keys())

def test_ruleresolutionstatus_exists():
    # Check that the Enumeration exists
    assert RuleResolutionStatus is not None

def test_ruleresolutionstatus_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RuleResolutionStatus]
    expected_literals = [
        "RESOLUTION_DISCARDED",
        "RESOLUTION_UNKNOWN",
        "RESOLUTION_CONFIRMED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RuleResolutionStatus"


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
atlext::OCL::CollectionOperationCallExp_strategy = st.builds(
    atlext::OCL::CollectionOperationCallExp,
)
ResolveTempResolution_strategy = st.builds(
    ResolveTempResolution,
)
atlext::OCL::OperationCallExp_strategy = st.builds(
    atlext::OCL::OperationCallExp,
)
ContextHelper_strategy = st.builds(
    ContextHelper,
)
Callable_strategy = st.builds(
    Callable,
)
OCL::atlext::EObject_strategy = st.builds(
    OCL::atlext::EObject,
)
atlext::OCL::PropertyCallExp_strategy = st.builds(
    atlext::OCL::PropertyCallExp,
    isStaticCall=
        st.booleans()
)
TypedElement_strategy = st.builds(
    TypedElement,
)
atlext::OCL::OclExpression_strategy = st.builds(
    atlext::OCL::OclExpression,
    implicitlyCasted=
        st.booleans()
)
atlext::OCL::VariableDeclaration_strategy = st.builds(
    atlext::OCL::VariableDeclaration,
)
OCL::atlext::Type_strategy = st.builds(
    OCL::atlext::Type,
)
atlext::OCL::TypedElement_strategy = st.builds(
    atlext::OCL::TypedElement,
)
MatchedRule_strategy = st.builds(
    MatchedRule,
)
atlext::ATL::RuleResolutionInfo_strategy = st.builds(
    atlext::ATL::RuleResolutionInfo,
    status=
        safe_text
)
CollectionOperationCallExp_strategy = st.builds(
    CollectionOperationCallExp,
)
atlext::OCL2::SelectByKind_strategy = st.builds(
    atlext::OCL2::SelectByKind,
    isExact=
        st.booleans()
)
JavaBody_strategy = st.builds(
    JavaBody,
)
atlext::OCL::GetAppliedStereotypesBody_strategy = st.builds(
    atlext::OCL::GetAppliedStereotypesBody,
)
OclExpression_strategy = st.builds(
    OclExpression,
)
atlext::OCL::JavaBody_strategy = st.builds(
    atlext::OCL::JavaBody,
)
OutPatternElement_strategy = st.builds(
    OutPatternElement,
)
atlext::ATL::Helper_strategy = st.builds(
    atlext::ATL::Helper,
    isAttribute=
        st.booleans(),
    hasContext=
        st.booleans()
)
atlext::ATL::ContextHelper_strategy = st.builds(
    atlext::ATL::ContextHelper,
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
ATL::atlext::Type_strategy = st.builds(
    ATL::atlext::Type,
)
atlext::ATL::CallableParameter_strategy = st.builds(
    atlext::ATL::CallableParameter,
    name=
        safe_text
)
CallableParameter_strategy = st.builds(
    CallableParameter,
)
PropertyCallExp_strategy = st.builds(
    PropertyCallExp,
)
atlext::ATL::Callable_strategy = st.builds(
    atlext::ATL::Callable,
)
atlext::ATL::OutPatternElement_strategy = st.builds(
    atlext::ATL::OutPatternElement,
)
atlext::ATL::MatchedRule_strategy = st.builds(
    atlext::ATL::MatchedRule,
)
atlext::ATL::StringToStringMap_strategy = st.builds(
    atlext::ATL::StringToStringMap,
    value=
        safe_text,
    key=
        safe_text
)
StringToStringMap_strategy = st.builds(
    StringToStringMap,
)
ATL::atlext::EObject_strategy = st.builds(
    ATL::atlext::EObject,
)
RuleResolutionInfo_strategy = st.builds(
    RuleResolutionInfo,
)
atlext::OCL::ResolveTempResolution_strategy = st.builds(
    atlext::OCL::ResolveTempResolution,
)
atlext::ATL::LocatedElement_strategy = st.builds(
    atlext::ATL::LocatedElement,
    fileLocation=
        safe_text,
    fileObject=
        safe_text
)
atlext::ATL::Binding_strategy = st.builds(
    atlext::ATL::Binding,
)

@given(instance=atlext::OCL::CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::CollectionOperationCallExp)

@given(instance=ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_resolvetempresolution_instantiation(instance):
    assert isinstance(instance, ResolveTempResolution)

@given(instance=atlext::OCL::OperationCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::operationcallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OperationCallExp)

@given(instance=ContextHelper_strategy)
@settings(max_examples=50)
def test_contexthelper_instantiation(instance):
    assert isinstance(instance, ContextHelper)

@given(instance=Callable_strategy)
@settings(max_examples=50)
def test_callable_instantiation(instance):
    assert isinstance(instance, Callable)

@given(instance=OCL::atlext::EObject_strategy)
@settings(max_examples=50)
def test_ocl::atlext::eobject_instantiation(instance):
    assert isinstance(instance, OCL::atlext::EObject)

@given(instance=atlext::OCL::PropertyCallExp_strategy)
@settings(max_examples=50)
def test_atlext::ocl::propertycallexp_instantiation(instance):
    assert isinstance(instance, atlext::OCL::PropertyCallExp)

@given(instance=atlext::OCL::PropertyCallExp_strategy)
def test_atlext::ocl::propertycallexp_isStaticCall_type(instance):
    assert isinstance(instance.isStaticCall, bool)


@given(instance=atlext::OCL::PropertyCallExp_strategy)
def test_atlext::ocl::propertycallexp_isStaticCall_setter(instance):
    original = instance.isStaticCall
    instance.isStaticCall = original
    assert instance.isStaticCall == original

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=atlext::OCL::OclExpression_strategy)
@settings(max_examples=50)
def test_atlext::ocl::oclexpression_instantiation(instance):
    assert isinstance(instance, atlext::OCL::OclExpression)

@given(instance=atlext::OCL::OclExpression_strategy)
def test_atlext::ocl::oclexpression_implicitlyCasted_type(instance):
    assert isinstance(instance.implicitlyCasted, bool)


@given(instance=atlext::OCL::OclExpression_strategy)
def test_atlext::ocl::oclexpression_implicitlyCasted_setter(instance):
    original = instance.implicitlyCasted
    instance.implicitlyCasted = original
    assert instance.implicitlyCasted == original

@given(instance=atlext::OCL::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_atlext::ocl::variabledeclaration_instantiation(instance):
    assert isinstance(instance, atlext::OCL::VariableDeclaration)

@given(instance=OCL::atlext::Type_strategy)
@settings(max_examples=50)
def test_ocl::atlext::type_instantiation(instance):
    assert isinstance(instance, OCL::atlext::Type)

@given(instance=atlext::OCL::TypedElement_strategy)
@settings(max_examples=50)
def test_atlext::ocl::typedelement_instantiation(instance):
    assert isinstance(instance, atlext::OCL::TypedElement)

@given(instance=MatchedRule_strategy)
@settings(max_examples=50)
def test_matchedrule_instantiation(instance):
    assert isinstance(instance, MatchedRule)

@given(instance=atlext::ATL::RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_atlext::atl::ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, atlext::ATL::RuleResolutionInfo)

@given(instance=atlext::ATL::RuleResolutionInfo_strategy)
def test_atlext::atl::ruleresolutioninfo_status_type(instance):
    assert isinstance(instance.status, str)


@given(instance=atlext::ATL::RuleResolutionInfo_strategy)
def test_atlext::atl::ruleresolutioninfo_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=CollectionOperationCallExp_strategy)
@settings(max_examples=50)
def test_collectionoperationcallexp_instantiation(instance):
    assert isinstance(instance, CollectionOperationCallExp)

@given(instance=atlext::OCL2::SelectByKind_strategy)
@settings(max_examples=50)
def test_atlext::ocl2::selectbykind_instantiation(instance):
    assert isinstance(instance, atlext::OCL2::SelectByKind)

@given(instance=atlext::OCL2::SelectByKind_strategy)
def test_atlext::ocl2::selectbykind_isExact_type(instance):
    assert isinstance(instance.isExact, bool)


@given(instance=atlext::OCL2::SelectByKind_strategy)
def test_atlext::ocl2::selectbykind_isExact_setter(instance):
    original = instance.isExact
    instance.isExact = original
    assert instance.isExact == original

@given(instance=JavaBody_strategy)
@settings(max_examples=50)
def test_javabody_instantiation(instance):
    assert isinstance(instance, JavaBody)

@given(instance=atlext::OCL::GetAppliedStereotypesBody_strategy)
@settings(max_examples=50)
def test_atlext::ocl::getappliedstereotypesbody_instantiation(instance):
    assert isinstance(instance, atlext::OCL::GetAppliedStereotypesBody)

@given(instance=OclExpression_strategy)
@settings(max_examples=50)
def test_oclexpression_instantiation(instance):
    assert isinstance(instance, OclExpression)

@given(instance=atlext::OCL::JavaBody_strategy)
@settings(max_examples=50)
def test_atlext::ocl::javabody_instantiation(instance):
    assert isinstance(instance, atlext::OCL::JavaBody)

@given(instance=OutPatternElement_strategy)
@settings(max_examples=50)
def test_outpatternelement_instantiation(instance):
    assert isinstance(instance, OutPatternElement)

@given(instance=atlext::ATL::Helper_strategy)
@settings(max_examples=50)
def test_atlext::atl::helper_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Helper)

@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_isAttribute_type(instance):
    assert isinstance(instance.isAttribute, bool)


@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_isAttribute_setter(instance):
    original = instance.isAttribute
    instance.isAttribute = original
    assert instance.isAttribute == original

@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_hasContext_type(instance):
    assert isinstance(instance.hasContext, bool)


@given(instance=atlext::ATL::Helper_strategy)
def test_atlext::atl::helper_hasContext_setter(instance):
    original = instance.hasContext
    instance.hasContext = original
    assert instance.hasContext == original

@given(instance=atlext::ATL::ContextHelper_strategy)
@settings(max_examples=50)
def test_atlext::atl::contexthelper_instantiation(instance):
    assert isinstance(instance, atlext::ATL::ContextHelper)

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=ATL::atlext::Type_strategy)
@settings(max_examples=50)
def test_atl::atlext::type_instantiation(instance):
    assert isinstance(instance, ATL::atlext::Type)

@given(instance=atlext::ATL::CallableParameter_strategy)
@settings(max_examples=50)
def test_atlext::atl::callableparameter_instantiation(instance):
    assert isinstance(instance, atlext::ATL::CallableParameter)

@given(instance=atlext::ATL::CallableParameter_strategy)
def test_atlext::atl::callableparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=atlext::ATL::CallableParameter_strategy)
def test_atlext::atl::callableparameter_name_setter(instance):
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

@given(instance=atlext::ATL::Callable_strategy)
@settings(max_examples=50)
def test_atlext::atl::callable_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Callable)

@given(instance=atlext::ATL::OutPatternElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::outpatternelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::OutPatternElement)

@given(instance=atlext::ATL::MatchedRule_strategy)
@settings(max_examples=50)
def test_atlext::atl::matchedrule_instantiation(instance):
    assert isinstance(instance, atlext::ATL::MatchedRule)

@given(instance=atlext::ATL::StringToStringMap_strategy)
@settings(max_examples=50)
def test_atlext::atl::stringtostringmap_instantiation(instance):
    assert isinstance(instance, atlext::ATL::StringToStringMap)

@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=atlext::ATL::StringToStringMap_strategy)
def test_atlext::atl::stringtostringmap_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=StringToStringMap_strategy)
@settings(max_examples=50)
def test_stringtostringmap_instantiation(instance):
    assert isinstance(instance, StringToStringMap)

@given(instance=ATL::atlext::EObject_strategy)
@settings(max_examples=50)
def test_atl::atlext::eobject_instantiation(instance):
    assert isinstance(instance, ATL::atlext::EObject)

@given(instance=RuleResolutionInfo_strategy)
@settings(max_examples=50)
def test_ruleresolutioninfo_instantiation(instance):
    assert isinstance(instance, RuleResolutionInfo)

@given(instance=atlext::OCL::ResolveTempResolution_strategy)
@settings(max_examples=50)
def test_atlext::ocl::resolvetempresolution_instantiation(instance):
    assert isinstance(instance, atlext::OCL::ResolveTempResolution)

@given(instance=atlext::ATL::LocatedElement_strategy)
@settings(max_examples=50)
def test_atlext::atl::locatedelement_instantiation(instance):
    assert isinstance(instance, atlext::ATL::LocatedElement)

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileLocation_type(instance):
    assert isinstance(instance.fileLocation, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileLocation_setter(instance):
    original = instance.fileLocation
    instance.fileLocation = original
    assert instance.fileLocation == original

@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileObject_type(instance):
    assert isinstance(instance.fileObject, str)


@given(instance=atlext::ATL::LocatedElement_strategy)
def test_atlext::atl::locatedelement_fileObject_setter(instance):
    original = instance.fileObject
    instance.fileObject = original
    assert instance.fileObject == original

@given(instance=atlext::ATL::Binding_strategy)
@settings(max_examples=50)
def test_atlext::atl::binding_instantiation(instance):
    assert isinstance(instance, atlext::ATL::Binding)
