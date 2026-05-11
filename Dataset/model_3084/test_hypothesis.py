import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cppmodel::XTClass,
    OOPLUserDefinedType,
    OOPLStructMember,
    OOPLStructType,
    OOPLEnumerator,
    OOPLEnumType,
    OOPLSequence,
    OOPLBasicType,
    cppmodel::CPPExternalLibrary,
    cppmodel::Parameter,
    cppmodel::XTEvent,
    cppmodel::Transition,
    cppmodel::TypedMultiplicityElement,
    cppmodel::State,
    cppmodel::OOPLDataType,
    cppmodel::CPPSequence,
    cppmodel::Attribute,
    OOPLClassRefAssocCollection,
    OOPLClassRefSimpleCollection,
    OOPLClassReferenceStorage,
    OOPLClassReference,
    cppmodel::XTProtocolOperationImplementation,
    cppmodel::XTProtocolOperationDefinition,
    cppmodel::XTPort,
    cppmodel::Snippet,
    cppmodel::Signal,
    cppmodel::Operation,
    OOPLRelation,
    cppmodel::CPPExternalHeader,
    cppmodel::XTComponent,
    CPPSourceFile,
    cppmodel::CPPMakeFile,
    cppmodel::CPPExternalHeaderInclusion,
    cppmodel::CPPSourceFile,
    cppmodel::XTProtocol,
    OOPLClass,
    cppmodel::Package,
    cppmodel::CPPDirectory,
    cppmodel::CPPHeaderFile,
    cppmodel::CPPBodyFile,
    cppmodel::Model,
    CPPQualifiedNamedElement,
    cppmodel::CPPReturnValue,
    cppmodel::CPPClassRefSimpleCollection,
    cppmodel::CPPProtocolOperationDefinition,
    cppmodel::CPPAttribute,
    cppmodel::CPPState,
    cppmodel::CPPProtocolOperationImplementation,
    cppmodel::CPPRelation,
    cppmodel::CPPClassReferenceStorage,
    cppmodel::CPPClass,
    cppmodel::CPPPort,
    cppmodel::CPPStructType,
    cppmodel::CPPProtocol,
    cppmodel::CPPOperation,
    cppmodel::CPPTransition,
    cppmodel::CPPUserDefinedType,
    cppmodel::CPPClassReference,
    cppmodel::CPPBasicType,
    cppmodel::CPPFormalParameter,
    cppmodel::CPPComponent,
    cppmodel::CPPClassRefAssocCollection,
    cppmodel::CPPSignal,
    cppmodel::CPPEnumType,
    cppmodel::CPPPackage,
    cppmodel::CPPEvent,
    cppmodel::CPPEnumerator,
    cppmodel::CPPStructMember,
    cppmodel::CPPExternalBridge,
    cppmodel::CPPModel,
    CPPNamedElement,
    cppmodel::CPPQualifiedNamedElement,
    cppmodel::OOPLNameProvider,
    cppmodel::CPPNamedElement,
    CPPParameterPassingKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cppmodel::xtclass_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTClass)


def test_cppmodel::xtclass_constructor_exists():
    assert callable(cppmodel::XTClass.__init__)


def test_cppmodel::xtclass_constructor_args():
    sig = inspect.signature(cppmodel::XTClass.__init__)
    params = list(sig.parameters.keys())



def test_oopluserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(OOPLUserDefinedType)


def test_oopluserdefinedtype_constructor_exists():
    assert callable(OOPLUserDefinedType.__init__)


def test_oopluserdefinedtype_constructor_args():
    sig = inspect.signature(OOPLUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_ooplstructmember_is_not_abstract():
    assert not inspect.isabstract(OOPLStructMember)


def test_ooplstructmember_constructor_exists():
    assert callable(OOPLStructMember.__init__)


def test_ooplstructmember_constructor_args():
    sig = inspect.signature(OOPLStructMember.__init__)
    params = list(sig.parameters.keys())



def test_ooplstructtype_is_not_abstract():
    assert not inspect.isabstract(OOPLStructType)


def test_ooplstructtype_constructor_exists():
    assert callable(OOPLStructType.__init__)


def test_ooplstructtype_constructor_args():
    sig = inspect.signature(OOPLStructType.__init__)
    params = list(sig.parameters.keys())



def test_ooplenumerator_is_not_abstract():
    assert not inspect.isabstract(OOPLEnumerator)


def test_ooplenumerator_constructor_exists():
    assert callable(OOPLEnumerator.__init__)


def test_ooplenumerator_constructor_args():
    sig = inspect.signature(OOPLEnumerator.__init__)
    params = list(sig.parameters.keys())



def test_ooplenumtype_is_not_abstract():
    assert not inspect.isabstract(OOPLEnumType)


def test_ooplenumtype_constructor_exists():
    assert callable(OOPLEnumType.__init__)


def test_ooplenumtype_constructor_args():
    sig = inspect.signature(OOPLEnumType.__init__)
    params = list(sig.parameters.keys())



def test_ooplsequence_is_not_abstract():
    assert not inspect.isabstract(OOPLSequence)


def test_ooplsequence_constructor_exists():
    assert callable(OOPLSequence.__init__)


def test_ooplsequence_constructor_args():
    sig = inspect.signature(OOPLSequence.__init__)
    params = list(sig.parameters.keys())



def test_ooplbasictype_is_not_abstract():
    assert not inspect.isabstract(OOPLBasicType)


def test_ooplbasictype_constructor_exists():
    assert callable(OOPLBasicType.__init__)


def test_ooplbasictype_constructor_args():
    sig = inspect.signature(OOPLBasicType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppexternallibrary_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPExternalLibrary)


def test_cppmodel::cppexternallibrary_constructor_exists():
    assert callable(cppmodel::CPPExternalLibrary.__init__)


def test_cppmodel::cppexternallibrary_constructor_args():
    sig = inspect.signature(cppmodel::CPPExternalLibrary.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::parameter_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Parameter)


def test_cppmodel::parameter_constructor_exists():
    assert callable(cppmodel::Parameter.__init__)


def test_cppmodel::parameter_constructor_args():
    sig = inspect.signature(cppmodel::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::xtevent_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTEvent)


def test_cppmodel::xtevent_constructor_exists():
    assert callable(cppmodel::XTEvent.__init__)


def test_cppmodel::xtevent_constructor_args():
    sig = inspect.signature(cppmodel::XTEvent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::transition_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Transition)


def test_cppmodel::transition_constructor_exists():
    assert callable(cppmodel::Transition.__init__)


def test_cppmodel::transition_constructor_args():
    sig = inspect.signature(cppmodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::typedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel::TypedMultiplicityElement)


def test_cppmodel::typedmultiplicityelement_constructor_exists():
    assert callable(cppmodel::TypedMultiplicityElement.__init__)


def test_cppmodel::typedmultiplicityelement_constructor_args():
    sig = inspect.signature(cppmodel::TypedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::state_is_not_abstract():
    assert not inspect.isabstract(cppmodel::State)


def test_cppmodel::state_constructor_exists():
    assert callable(cppmodel::State.__init__)


def test_cppmodel::state_constructor_args():
    sig = inspect.signature(cppmodel::State.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::oopldatatype_is_not_abstract():
    assert not inspect.isabstract(cppmodel::OOPLDataType)


def test_cppmodel::oopldatatype_constructor_exists():
    assert callable(cppmodel::OOPLDataType.__init__)


def test_cppmodel::oopldatatype_constructor_args():
    sig = inspect.signature(cppmodel::OOPLDataType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppsequence_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPSequence)


def test_cppmodel::cppsequence_constructor_exists():
    assert callable(cppmodel::CPPSequence.__init__)


def test_cppmodel::cppsequence_constructor_args():
    sig = inspect.signature(cppmodel::CPPSequence.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel::cppsequence_has_cppContainer():
    assert hasattr(cppmodel::CPPSequence, "cppContainer")
    descriptor = None
    for klass in cppmodel::CPPSequence.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::attribute_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Attribute)


def test_cppmodel::attribute_constructor_exists():
    assert callable(cppmodel::Attribute.__init__)


def test_cppmodel::attribute_constructor_args():
    sig = inspect.signature(cppmodel::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_ooplclassrefassoccollection_is_not_abstract():
    assert not inspect.isabstract(OOPLClassRefAssocCollection)


def test_ooplclassrefassoccollection_constructor_exists():
    assert callable(OOPLClassRefAssocCollection.__init__)


def test_ooplclassrefassoccollection_constructor_args():
    sig = inspect.signature(OOPLClassRefAssocCollection.__init__)
    params = list(sig.parameters.keys())



def test_ooplclassrefsimplecollection_is_not_abstract():
    assert not inspect.isabstract(OOPLClassRefSimpleCollection)


def test_ooplclassrefsimplecollection_constructor_exists():
    assert callable(OOPLClassRefSimpleCollection.__init__)


def test_ooplclassrefsimplecollection_constructor_args():
    sig = inspect.signature(OOPLClassRefSimpleCollection.__init__)
    params = list(sig.parameters.keys())



def test_ooplclassreferencestorage_is_not_abstract():
    assert not inspect.isabstract(OOPLClassReferenceStorage)


def test_ooplclassreferencestorage_constructor_exists():
    assert callable(OOPLClassReferenceStorage.__init__)


def test_ooplclassreferencestorage_constructor_args():
    sig = inspect.signature(OOPLClassReferenceStorage.__init__)
    params = list(sig.parameters.keys())



def test_ooplclassreference_is_not_abstract():
    assert not inspect.isabstract(OOPLClassReference)


def test_ooplclassreference_constructor_exists():
    assert callable(OOPLClassReference.__init__)


def test_ooplclassreference_constructor_args():
    sig = inspect.signature(OOPLClassReference.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::xtprotocoloperationimplementation_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTProtocolOperationImplementation)


def test_cppmodel::xtprotocoloperationimplementation_constructor_exists():
    assert callable(cppmodel::XTProtocolOperationImplementation.__init__)


def test_cppmodel::xtprotocoloperationimplementation_constructor_args():
    sig = inspect.signature(cppmodel::XTProtocolOperationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::xtprotocoloperationdefinition_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTProtocolOperationDefinition)


def test_cppmodel::xtprotocoloperationdefinition_constructor_exists():
    assert callable(cppmodel::XTProtocolOperationDefinition.__init__)


def test_cppmodel::xtprotocoloperationdefinition_constructor_args():
    sig = inspect.signature(cppmodel::XTProtocolOperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::xtport_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTPort)


def test_cppmodel::xtport_constructor_exists():
    assert callable(cppmodel::XTPort.__init__)


def test_cppmodel::xtport_constructor_args():
    sig = inspect.signature(cppmodel::XTPort.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::snippet_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Snippet)


def test_cppmodel::snippet_constructor_exists():
    assert callable(cppmodel::Snippet.__init__)


def test_cppmodel::snippet_constructor_args():
    sig = inspect.signature(cppmodel::Snippet.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::signal_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Signal)


def test_cppmodel::signal_constructor_exists():
    assert callable(cppmodel::Signal.__init__)


def test_cppmodel::signal_constructor_args():
    sig = inspect.signature(cppmodel::Signal.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::operation_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Operation)


def test_cppmodel::operation_constructor_exists():
    assert callable(cppmodel::Operation.__init__)


def test_cppmodel::operation_constructor_args():
    sig = inspect.signature(cppmodel::Operation.__init__)
    params = list(sig.parameters.keys())



def test_ooplrelation_is_not_abstract():
    assert not inspect.isabstract(OOPLRelation)


def test_ooplrelation_constructor_exists():
    assert callable(OOPLRelation.__init__)


def test_ooplrelation_constructor_args():
    sig = inspect.signature(OOPLRelation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppexternalheader_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPExternalHeader)


def test_cppmodel::cppexternalheader_constructor_exists():
    assert callable(cppmodel::CPPExternalHeader.__init__)


def test_cppmodel::cppexternalheader_constructor_args():
    sig = inspect.signature(cppmodel::CPPExternalHeader.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cppmodel::cppexternalheader_has_name():
    assert hasattr(cppmodel::CPPExternalHeader, "name")
    descriptor = None
    for klass in cppmodel::CPPExternalHeader.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::xtcomponent_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTComponent)


def test_cppmodel::xtcomponent_constructor_exists():
    assert callable(cppmodel::XTComponent.__init__)


def test_cppmodel::xtcomponent_constructor_args():
    sig = inspect.signature(cppmodel::XTComponent.__init__)
    params = list(sig.parameters.keys())



def test_cppsourcefile_is_not_abstract():
    assert not inspect.isabstract(CPPSourceFile)


def test_cppsourcefile_constructor_exists():
    assert callable(CPPSourceFile.__init__)


def test_cppsourcefile_constructor_args():
    sig = inspect.signature(CPPSourceFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppmakefile_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPMakeFile)


def test_cppmodel::cppmakefile_constructor_exists():
    assert callable(cppmodel::CPPMakeFile.__init__)


def test_cppmodel::cppmakefile_constructor_args():
    sig = inspect.signature(cppmodel::CPPMakeFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppexternalheaderinclusion_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPExternalHeaderInclusion)


def test_cppmodel::cppexternalheaderinclusion_constructor_exists():
    assert callable(cppmodel::CPPExternalHeaderInclusion.__init__)


def test_cppmodel::cppexternalheaderinclusion_constructor_args():
    sig = inspect.signature(cppmodel::CPPExternalHeaderInclusion.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cppmodel::cppexternalheaderinclusion_has_comment():
    assert hasattr(cppmodel::CPPExternalHeaderInclusion, "comment")
    descriptor = None
    for klass in cppmodel::CPPExternalHeaderInclusion.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppsourcefile_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPSourceFile)


def test_cppmodel::cppsourcefile_constructor_exists():
    assert callable(cppmodel::CPPSourceFile.__init__)


def test_cppmodel::cppsourcefile_constructor_args():
    sig = inspect.signature(cppmodel::CPPSourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "generationName" in params, "Missing parameter 'generationName'"
    assert "generationPath" in params, "Missing parameter 'generationPath'"
    assert "generationDirectory" in params, "Missing parameter 'generationDirectory'"

def test_cppmodel::cppsourcefile_has_generationName():
    assert hasattr(cppmodel::CPPSourceFile, "generationName")
    descriptor = None
    for klass in cppmodel::CPPSourceFile.__mro__:
        if "generationName" in klass.__dict__:
            descriptor = klass.__dict__["generationName"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppsourcefile_has_generationPath():
    assert hasattr(cppmodel::CPPSourceFile, "generationPath")
    descriptor = None
    for klass in cppmodel::CPPSourceFile.__mro__:
        if "generationPath" in klass.__dict__:
            descriptor = klass.__dict__["generationPath"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppsourcefile_has_generationDirectory():
    assert hasattr(cppmodel::CPPSourceFile, "generationDirectory")
    descriptor = None
    for klass in cppmodel::CPPSourceFile.__mro__:
        if "generationDirectory" in klass.__dict__:
            descriptor = klass.__dict__["generationDirectory"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::xtprotocol_is_not_abstract():
    assert not inspect.isabstract(cppmodel::XTProtocol)


def test_cppmodel::xtprotocol_constructor_exists():
    assert callable(cppmodel::XTProtocol.__init__)


def test_cppmodel::xtprotocol_constructor_args():
    sig = inspect.signature(cppmodel::XTProtocol.__init__)
    params = list(sig.parameters.keys())



def test_ooplclass_is_not_abstract():
    assert not inspect.isabstract(OOPLClass)


def test_ooplclass_constructor_exists():
    assert callable(OOPLClass.__init__)


def test_ooplclass_constructor_args():
    sig = inspect.signature(OOPLClass.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::package_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Package)


def test_cppmodel::package_constructor_exists():
    assert callable(cppmodel::Package.__init__)


def test_cppmodel::package_constructor_args():
    sig = inspect.signature(cppmodel::Package.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppdirectory_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPDirectory)


def test_cppmodel::cppdirectory_constructor_exists():
    assert callable(cppmodel::CPPDirectory.__init__)


def test_cppmodel::cppdirectory_constructor_args():
    sig = inspect.signature(cppmodel::CPPDirectory.__init__)
    params = list(sig.parameters.keys())
    assert "parentDirectory" in params, "Missing parameter 'parentDirectory'"
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_cppmodel::cppdirectory_has_parentDirectory():
    assert hasattr(cppmodel::CPPDirectory, "parentDirectory")
    descriptor = None
    for klass in cppmodel::CPPDirectory.__mro__:
        if "parentDirectory" in klass.__dict__:
            descriptor = klass.__dict__["parentDirectory"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppdirectory_has_path():
    assert hasattr(cppmodel::CPPDirectory, "path")
    descriptor = None
    for klass in cppmodel::CPPDirectory.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppdirectory_has_name():
    assert hasattr(cppmodel::CPPDirectory, "name")
    descriptor = None
    for klass in cppmodel::CPPDirectory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppheaderfile_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPHeaderFile)


def test_cppmodel::cppheaderfile_constructor_exists():
    assert callable(cppmodel::CPPHeaderFile.__init__)


def test_cppmodel::cppheaderfile_constructor_args():
    sig = inspect.signature(cppmodel::CPPHeaderFile.__init__)
    params = list(sig.parameters.keys())
    assert "includePath" in params, "Missing parameter 'includePath'"
    assert "includeName" in params, "Missing parameter 'includeName'"
    assert "includeDirectory" in params, "Missing parameter 'includeDirectory'"

def test_cppmodel::cppheaderfile_has_includePath():
    assert hasattr(cppmodel::CPPHeaderFile, "includePath")
    descriptor = None
    for klass in cppmodel::CPPHeaderFile.__mro__:
        if "includePath" in klass.__dict__:
            descriptor = klass.__dict__["includePath"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppheaderfile_has_includeName():
    assert hasattr(cppmodel::CPPHeaderFile, "includeName")
    descriptor = None
    for klass in cppmodel::CPPHeaderFile.__mro__:
        if "includeName" in klass.__dict__:
            descriptor = klass.__dict__["includeName"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppheaderfile_has_includeDirectory():
    assert hasattr(cppmodel::CPPHeaderFile, "includeDirectory")
    descriptor = None
    for klass in cppmodel::CPPHeaderFile.__mro__:
        if "includeDirectory" in klass.__dict__:
            descriptor = klass.__dict__["includeDirectory"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppbodyfile_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPBodyFile)


def test_cppmodel::cppbodyfile_constructor_exists():
    assert callable(cppmodel::CPPBodyFile.__init__)


def test_cppmodel::cppbodyfile_constructor_args():
    sig = inspect.signature(cppmodel::CPPBodyFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::model_is_not_abstract():
    assert not inspect.isabstract(cppmodel::Model)


def test_cppmodel::model_constructor_exists():
    assert callable(cppmodel::Model.__init__)


def test_cppmodel::model_constructor_args():
    sig = inspect.signature(cppmodel::Model.__init__)
    params = list(sig.parameters.keys())



def test_cppqualifiednamedelement_is_not_abstract():
    assert not inspect.isabstract(CPPQualifiedNamedElement)


def test_cppqualifiednamedelement_constructor_exists():
    assert callable(CPPQualifiedNamedElement.__init__)


def test_cppqualifiednamedelement_constructor_args():
    sig = inspect.signature(CPPQualifiedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppreturnvalue_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPReturnValue)


def test_cppmodel::cppreturnvalue_constructor_exists():
    assert callable(cppmodel::CPPReturnValue.__init__)


def test_cppmodel::cppreturnvalue_constructor_args():
    sig = inspect.signature(cppmodel::CPPReturnValue.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppclassrefsimplecollection_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPClassRefSimpleCollection)


def test_cppmodel::cppclassrefsimplecollection_constructor_exists():
    assert callable(cppmodel::CPPClassRefSimpleCollection.__init__)


def test_cppmodel::cppclassrefsimplecollection_constructor_args():
    sig = inspect.signature(cppmodel::CPPClassRefSimpleCollection.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel::cppclassrefsimplecollection_has_cppContainer():
    assert hasattr(cppmodel::CPPClassRefSimpleCollection, "cppContainer")
    descriptor = None
    for klass in cppmodel::CPPClassRefSimpleCollection.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppprotocoloperationdefinition_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPProtocolOperationDefinition)


def test_cppmodel::cppprotocoloperationdefinition_constructor_exists():
    assert callable(cppmodel::CPPProtocolOperationDefinition.__init__)


def test_cppmodel::cppprotocoloperationdefinition_constructor_args():
    sig = inspect.signature(cppmodel::CPPProtocolOperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppattribute_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPAttribute)


def test_cppmodel::cppattribute_constructor_exists():
    assert callable(cppmodel::CPPAttribute.__init__)


def test_cppmodel::cppattribute_constructor_args():
    sig = inspect.signature(cppmodel::CPPAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppstate_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPState)


def test_cppmodel::cppstate_constructor_exists():
    assert callable(cppmodel::CPPState.__init__)


def test_cppmodel::cppstate_constructor_args():
    sig = inspect.signature(cppmodel::CPPState.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppprotocoloperationimplementation_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPProtocolOperationImplementation)


def test_cppmodel::cppprotocoloperationimplementation_constructor_exists():
    assert callable(cppmodel::CPPProtocolOperationImplementation.__init__)


def test_cppmodel::cppprotocoloperationimplementation_constructor_args():
    sig = inspect.signature(cppmodel::CPPProtocolOperationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cpprelation_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPRelation)


def test_cppmodel::cpprelation_constructor_exists():
    assert callable(cppmodel::CPPRelation.__init__)


def test_cppmodel::cpprelation_constructor_args():
    sig = inspect.signature(cppmodel::CPPRelation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppclassreferencestorage_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPClassReferenceStorage)


def test_cppmodel::cppclassreferencestorage_constructor_exists():
    assert callable(cppmodel::CPPClassReferenceStorage.__init__)


def test_cppmodel::cppclassreferencestorage_constructor_args():
    sig = inspect.signature(cppmodel::CPPClassReferenceStorage.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppclass_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPClass)


def test_cppmodel::cppclass_constructor_exists():
    assert callable(cppmodel::CPPClass.__init__)


def test_cppmodel::cppclass_constructor_args():
    sig = inspect.signature(cppmodel::CPPClass.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppport_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPPort)


def test_cppmodel::cppport_constructor_exists():
    assert callable(cppmodel::CPPPort.__init__)


def test_cppmodel::cppport_constructor_args():
    sig = inspect.signature(cppmodel::CPPPort.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppstructtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPStructType)


def test_cppmodel::cppstructtype_constructor_exists():
    assert callable(cppmodel::CPPStructType.__init__)


def test_cppmodel::cppstructtype_constructor_args():
    sig = inspect.signature(cppmodel::CPPStructType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppprotocol_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPProtocol)


def test_cppmodel::cppprotocol_constructor_exists():
    assert callable(cppmodel::CPPProtocol.__init__)


def test_cppmodel::cppprotocol_constructor_args():
    sig = inspect.signature(cppmodel::CPPProtocol.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppoperation_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPOperation)


def test_cppmodel::cppoperation_constructor_exists():
    assert callable(cppmodel::CPPOperation.__init__)


def test_cppmodel::cppoperation_constructor_args():
    sig = inspect.signature(cppmodel::CPPOperation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cpptransition_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPTransition)


def test_cppmodel::cpptransition_constructor_exists():
    assert callable(cppmodel::CPPTransition.__init__)


def test_cppmodel::cpptransition_constructor_args():
    sig = inspect.signature(cppmodel::CPPTransition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPUserDefinedType)


def test_cppmodel::cppuserdefinedtype_constructor_exists():
    assert callable(cppmodel::CPPUserDefinedType.__init__)


def test_cppmodel::cppuserdefinedtype_constructor_args():
    sig = inspect.signature(cppmodel::CPPUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppclassreference_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPClassReference)


def test_cppmodel::cppclassreference_constructor_exists():
    assert callable(cppmodel::CPPClassReference.__init__)


def test_cppmodel::cppclassreference_constructor_args():
    sig = inspect.signature(cppmodel::CPPClassReference.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppbasictype_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPBasicType)


def test_cppmodel::cppbasictype_constructor_exists():
    assert callable(cppmodel::CPPBasicType.__init__)


def test_cppmodel::cppbasictype_constructor_args():
    sig = inspect.signature(cppmodel::CPPBasicType.__init__)
    params = list(sig.parameters.keys())
    assert "cppSpecifier" in params, "Missing parameter 'cppSpecifier'"

def test_cppmodel::cppbasictype_has_cppSpecifier():
    assert hasattr(cppmodel::CPPBasicType, "cppSpecifier")
    descriptor = None
    for klass in cppmodel::CPPBasicType.__mro__:
        if "cppSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["cppSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppformalparameter_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPFormalParameter)


def test_cppmodel::cppformalparameter_constructor_exists():
    assert callable(cppmodel::CPPFormalParameter.__init__)


def test_cppmodel::cppformalparameter_constructor_args():
    sig = inspect.signature(cppmodel::CPPFormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "passingMode" in params, "Missing parameter 'passingMode'"

def test_cppmodel::cppformalparameter_has_passingMode():
    assert hasattr(cppmodel::CPPFormalParameter, "passingMode")
    descriptor = None
    for klass in cppmodel::CPPFormalParameter.__mro__:
        if "passingMode" in klass.__dict__:
            descriptor = klass.__dict__["passingMode"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppcomponent_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPComponent)


def test_cppmodel::cppcomponent_constructor_exists():
    assert callable(cppmodel::CPPComponent.__init__)


def test_cppmodel::cppcomponent_constructor_args():
    sig = inspect.signature(cppmodel::CPPComponent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppclassrefassoccollection_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPClassRefAssocCollection)


def test_cppmodel::cppclassrefassoccollection_constructor_exists():
    assert callable(cppmodel::CPPClassRefAssocCollection.__init__)


def test_cppmodel::cppclassrefassoccollection_constructor_args():
    sig = inspect.signature(cppmodel::CPPClassRefAssocCollection.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel::cppclassrefassoccollection_has_cppContainer():
    assert hasattr(cppmodel::CPPClassRefAssocCollection, "cppContainer")
    descriptor = None
    for klass in cppmodel::CPPClassRefAssocCollection.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppsignal_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPSignal)


def test_cppmodel::cppsignal_constructor_exists():
    assert callable(cppmodel::CPPSignal.__init__)


def test_cppmodel::cppsignal_constructor_args():
    sig = inspect.signature(cppmodel::CPPSignal.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppenumtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPEnumType)


def test_cppmodel::cppenumtype_constructor_exists():
    assert callable(cppmodel::CPPEnumType.__init__)


def test_cppmodel::cppenumtype_constructor_args():
    sig = inspect.signature(cppmodel::CPPEnumType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cpppackage_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPPackage)


def test_cppmodel::cpppackage_constructor_exists():
    assert callable(cppmodel::CPPPackage.__init__)


def test_cppmodel::cpppackage_constructor_args():
    sig = inspect.signature(cppmodel::CPPPackage.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppevent_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPEvent)


def test_cppmodel::cppevent_constructor_exists():
    assert callable(cppmodel::CPPEvent.__init__)


def test_cppmodel::cppevent_constructor_args():
    sig = inspect.signature(cppmodel::CPPEvent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppenumerator_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPEnumerator)


def test_cppmodel::cppenumerator_constructor_exists():
    assert callable(cppmodel::CPPEnumerator.__init__)


def test_cppmodel::cppenumerator_constructor_args():
    sig = inspect.signature(cppmodel::CPPEnumerator.__init__)
    params = list(sig.parameters.keys())
    assert "cppValue" in params, "Missing parameter 'cppValue'"

def test_cppmodel::cppenumerator_has_cppValue():
    assert hasattr(cppmodel::CPPEnumerator, "cppValue")
    descriptor = None
    for klass in cppmodel::CPPEnumerator.__mro__:
        if "cppValue" in klass.__dict__:
            descriptor = klass.__dict__["cppValue"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppstructmember_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPStructMember)


def test_cppmodel::cppstructmember_constructor_exists():
    assert callable(cppmodel::CPPStructMember.__init__)


def test_cppmodel::cppstructmember_constructor_args():
    sig = inspect.signature(cppmodel::CPPStructMember.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppexternalbridge_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPExternalBridge)


def test_cppmodel::cppexternalbridge_constructor_exists():
    assert callable(cppmodel::CPPExternalBridge.__init__)


def test_cppmodel::cppexternalbridge_constructor_args():
    sig = inspect.signature(cppmodel::CPPExternalBridge.__init__)
    params = list(sig.parameters.keys())
    assert "cppExternalNamespace" in params, "Missing parameter 'cppExternalNamespace'"

def test_cppmodel::cppexternalbridge_has_cppExternalNamespace():
    assert hasattr(cppmodel::CPPExternalBridge, "cppExternalNamespace")
    descriptor = None
    for klass in cppmodel::CPPExternalBridge.__mro__:
        if "cppExternalNamespace" in klass.__dict__:
            descriptor = klass.__dict__["cppExternalNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::cppmodel_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPModel)


def test_cppmodel::cppmodel_constructor_exists():
    assert callable(cppmodel::CPPModel.__init__)


def test_cppmodel::cppmodel_constructor_args():
    sig = inspect.signature(cppmodel::CPPModel.__init__)
    params = list(sig.parameters.keys())



def test_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(CPPNamedElement)


def test_cppnamedelement_constructor_exists():
    assert callable(CPPNamedElement.__init__)


def test_cppnamedelement_constructor_args():
    sig = inspect.signature(CPPNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppqualifiednamedelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPQualifiedNamedElement)


def test_cppmodel::cppqualifiednamedelement_constructor_exists():
    assert callable(cppmodel::CPPQualifiedNamedElement.__init__)


def test_cppmodel::cppqualifiednamedelement_constructor_args():
    sig = inspect.signature(cppmodel::CPPQualifiedNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "cppPrefix" in params, "Missing parameter 'cppPrefix'"
    assert "cppQualifiedName" in params, "Missing parameter 'cppQualifiedName'"

def test_cppmodel::cppqualifiednamedelement_has_cppPrefix():
    assert hasattr(cppmodel::CPPQualifiedNamedElement, "cppPrefix")
    descriptor = None
    for klass in cppmodel::CPPQualifiedNamedElement.__mro__:
        if "cppPrefix" in klass.__dict__:
            descriptor = klass.__dict__["cppPrefix"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel::cppqualifiednamedelement_has_cppQualifiedName():
    assert hasattr(cppmodel::CPPQualifiedNamedElement, "cppQualifiedName")
    descriptor = None
    for klass in cppmodel::CPPQualifiedNamedElement.__mro__:
        if "cppQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["cppQualifiedName"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel::ooplnameprovider_is_not_abstract():
    assert not inspect.isabstract(cppmodel::OOPLNameProvider)


def test_cppmodel::ooplnameprovider_constructor_exists():
    assert callable(cppmodel::OOPLNameProvider.__init__)


def test_cppmodel::ooplnameprovider_constructor_args():
    sig = inspect.signature(cppmodel::OOPLNameProvider.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel::cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel::CPPNamedElement)


def test_cppmodel::cppnamedelement_constructor_exists():
    assert callable(cppmodel::CPPNamedElement.__init__)


def test_cppmodel::cppnamedelement_constructor_args():
    sig = inspect.signature(cppmodel::CPPNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "cppName" in params, "Missing parameter 'cppName'"

def test_cppmodel::cppnamedelement_has_cppName():
    assert hasattr(cppmodel::CPPNamedElement, "cppName")
    descriptor = None
    for klass in cppmodel::CPPNamedElement.__mro__:
        if "cppName" in klass.__dict__:
            descriptor = klass.__dict__["cppName"]
            break
    assert isinstance(descriptor, property)

def test_cppparameterpassingkind_exists():
    # Check that the Enumeration exists
    assert CPPParameterPassingKind is not None

def test_cppparameterpassingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CPPParameterPassingKind]
    expected_literals = [
        "BY_VALUE",
        "BY_CONSTANT_REFERENCE",
        "BY_REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CPPParameterPassingKind"


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
cppmodel::XTClass_strategy = st.builds(
    cppmodel::XTClass,
)
OOPLUserDefinedType_strategy = st.builds(
    OOPLUserDefinedType,
)
OOPLStructMember_strategy = st.builds(
    OOPLStructMember,
)
OOPLStructType_strategy = st.builds(
    OOPLStructType,
)
OOPLEnumerator_strategy = st.builds(
    OOPLEnumerator,
)
OOPLEnumType_strategy = st.builds(
    OOPLEnumType,
)
OOPLSequence_strategy = st.builds(
    OOPLSequence,
)
OOPLBasicType_strategy = st.builds(
    OOPLBasicType,
)
cppmodel::CPPExternalLibrary_strategy = st.builds(
    cppmodel::CPPExternalLibrary,
)
cppmodel::Parameter_strategy = st.builds(
    cppmodel::Parameter,
)
cppmodel::XTEvent_strategy = st.builds(
    cppmodel::XTEvent,
)
cppmodel::Transition_strategy = st.builds(
    cppmodel::Transition,
)
cppmodel::TypedMultiplicityElement_strategy = st.builds(
    cppmodel::TypedMultiplicityElement,
)
cppmodel::State_strategy = st.builds(
    cppmodel::State,
)
cppmodel::OOPLDataType_strategy = st.builds(
    cppmodel::OOPLDataType,
)
cppmodel::CPPSequence_strategy = st.builds(
    cppmodel::CPPSequence,
    cppContainer=
        safe_text
)
cppmodel::Attribute_strategy = st.builds(
    cppmodel::Attribute,
)
OOPLClassRefAssocCollection_strategy = st.builds(
    OOPLClassRefAssocCollection,
)
OOPLClassRefSimpleCollection_strategy = st.builds(
    OOPLClassRefSimpleCollection,
)
OOPLClassReferenceStorage_strategy = st.builds(
    OOPLClassReferenceStorage,
)
OOPLClassReference_strategy = st.builds(
    OOPLClassReference,
)
cppmodel::XTProtocolOperationImplementation_strategy = st.builds(
    cppmodel::XTProtocolOperationImplementation,
)
cppmodel::XTProtocolOperationDefinition_strategy = st.builds(
    cppmodel::XTProtocolOperationDefinition,
)
cppmodel::XTPort_strategy = st.builds(
    cppmodel::XTPort,
)
cppmodel::Snippet_strategy = st.builds(
    cppmodel::Snippet,
)
cppmodel::Signal_strategy = st.builds(
    cppmodel::Signal,
)
cppmodel::Operation_strategy = st.builds(
    cppmodel::Operation,
)
OOPLRelation_strategy = st.builds(
    OOPLRelation,
)
cppmodel::CPPExternalHeader_strategy = st.builds(
    cppmodel::CPPExternalHeader,
    name=
        safe_text
)
cppmodel::XTComponent_strategy = st.builds(
    cppmodel::XTComponent,
)
CPPSourceFile_strategy = st.builds(
    CPPSourceFile,
)
cppmodel::CPPMakeFile_strategy = st.builds(
    cppmodel::CPPMakeFile,
)
cppmodel::CPPExternalHeaderInclusion_strategy = st.builds(
    cppmodel::CPPExternalHeaderInclusion,
    comment=
        safe_text
)
cppmodel::CPPSourceFile_strategy = st.builds(
    cppmodel::CPPSourceFile,
    generationName=
        safe_text,
    generationPath=
        safe_text,
    generationDirectory=
        safe_text
)
cppmodel::XTProtocol_strategy = st.builds(
    cppmodel::XTProtocol,
)
OOPLClass_strategy = st.builds(
    OOPLClass,
)
cppmodel::Package_strategy = st.builds(
    cppmodel::Package,
)
cppmodel::CPPDirectory_strategy = st.builds(
    cppmodel::CPPDirectory,
    parentDirectory=
        safe_text,
    path=
        safe_text,
    name=
        safe_text
)
cppmodel::CPPHeaderFile_strategy = st.builds(
    cppmodel::CPPHeaderFile,
    includePath=
        safe_text,
    includeName=
        safe_text,
    includeDirectory=
        safe_text
)
cppmodel::CPPBodyFile_strategy = st.builds(
    cppmodel::CPPBodyFile,
)
cppmodel::Model_strategy = st.builds(
    cppmodel::Model,
)
CPPQualifiedNamedElement_strategy = st.builds(
    CPPQualifiedNamedElement,
)
cppmodel::CPPReturnValue_strategy = st.builds(
    cppmodel::CPPReturnValue,
)
cppmodel::CPPClassRefSimpleCollection_strategy = st.builds(
    cppmodel::CPPClassRefSimpleCollection,
    cppContainer=
        safe_text
)
cppmodel::CPPProtocolOperationDefinition_strategy = st.builds(
    cppmodel::CPPProtocolOperationDefinition,
)
cppmodel::CPPAttribute_strategy = st.builds(
    cppmodel::CPPAttribute,
)
cppmodel::CPPState_strategy = st.builds(
    cppmodel::CPPState,
)
cppmodel::CPPProtocolOperationImplementation_strategy = st.builds(
    cppmodel::CPPProtocolOperationImplementation,
)
cppmodel::CPPRelation_strategy = st.builds(
    cppmodel::CPPRelation,
)
cppmodel::CPPClassReferenceStorage_strategy = st.builds(
    cppmodel::CPPClassReferenceStorage,
)
cppmodel::CPPClass_strategy = st.builds(
    cppmodel::CPPClass,
)
cppmodel::CPPPort_strategy = st.builds(
    cppmodel::CPPPort,
)
cppmodel::CPPStructType_strategy = st.builds(
    cppmodel::CPPStructType,
)
cppmodel::CPPProtocol_strategy = st.builds(
    cppmodel::CPPProtocol,
)
cppmodel::CPPOperation_strategy = st.builds(
    cppmodel::CPPOperation,
)
cppmodel::CPPTransition_strategy = st.builds(
    cppmodel::CPPTransition,
)
cppmodel::CPPUserDefinedType_strategy = st.builds(
    cppmodel::CPPUserDefinedType,
)
cppmodel::CPPClassReference_strategy = st.builds(
    cppmodel::CPPClassReference,
)
cppmodel::CPPBasicType_strategy = st.builds(
    cppmodel::CPPBasicType,
    cppSpecifier=
        safe_text
)
cppmodel::CPPFormalParameter_strategy = st.builds(
    cppmodel::CPPFormalParameter,
    passingMode=
        safe_text
)
cppmodel::CPPComponent_strategy = st.builds(
    cppmodel::CPPComponent,
)
cppmodel::CPPClassRefAssocCollection_strategy = st.builds(
    cppmodel::CPPClassRefAssocCollection,
    cppContainer=
        safe_text
)
cppmodel::CPPSignal_strategy = st.builds(
    cppmodel::CPPSignal,
)
cppmodel::CPPEnumType_strategy = st.builds(
    cppmodel::CPPEnumType,
)
cppmodel::CPPPackage_strategy = st.builds(
    cppmodel::CPPPackage,
)
cppmodel::CPPEvent_strategy = st.builds(
    cppmodel::CPPEvent,
)
cppmodel::CPPEnumerator_strategy = st.builds(
    cppmodel::CPPEnumerator,
    cppValue=
        safe_text
)
cppmodel::CPPStructMember_strategy = st.builds(
    cppmodel::CPPStructMember,
)
cppmodel::CPPExternalBridge_strategy = st.builds(
    cppmodel::CPPExternalBridge,
    cppExternalNamespace=
        safe_text
)
cppmodel::CPPModel_strategy = st.builds(
    cppmodel::CPPModel,
)
CPPNamedElement_strategy = st.builds(
    CPPNamedElement,
)
cppmodel::CPPQualifiedNamedElement_strategy = st.builds(
    cppmodel::CPPQualifiedNamedElement,
    cppPrefix=
        safe_text,
    cppQualifiedName=
        safe_text
)
cppmodel::OOPLNameProvider_strategy = st.builds(
    cppmodel::OOPLNameProvider,
)
cppmodel::CPPNamedElement_strategy = st.builds(
    cppmodel::CPPNamedElement,
    cppName=
        safe_text
)

@given(instance=cppmodel::XTClass_strategy)
@settings(max_examples=50)
def test_cppmodel::xtclass_instantiation(instance):
    assert isinstance(instance, cppmodel::XTClass)

@given(instance=OOPLUserDefinedType_strategy)
@settings(max_examples=50)
def test_oopluserdefinedtype_instantiation(instance):
    assert isinstance(instance, OOPLUserDefinedType)

@given(instance=OOPLStructMember_strategy)
@settings(max_examples=50)
def test_ooplstructmember_instantiation(instance):
    assert isinstance(instance, OOPLStructMember)

@given(instance=OOPLStructType_strategy)
@settings(max_examples=50)
def test_ooplstructtype_instantiation(instance):
    assert isinstance(instance, OOPLStructType)

@given(instance=OOPLEnumerator_strategy)
@settings(max_examples=50)
def test_ooplenumerator_instantiation(instance):
    assert isinstance(instance, OOPLEnumerator)

@given(instance=OOPLEnumType_strategy)
@settings(max_examples=50)
def test_ooplenumtype_instantiation(instance):
    assert isinstance(instance, OOPLEnumType)

@given(instance=OOPLSequence_strategy)
@settings(max_examples=50)
def test_ooplsequence_instantiation(instance):
    assert isinstance(instance, OOPLSequence)

@given(instance=OOPLBasicType_strategy)
@settings(max_examples=50)
def test_ooplbasictype_instantiation(instance):
    assert isinstance(instance, OOPLBasicType)

@given(instance=cppmodel::CPPExternalLibrary_strategy)
@settings(max_examples=50)
def test_cppmodel::cppexternallibrary_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPExternalLibrary)

@given(instance=cppmodel::Parameter_strategy)
@settings(max_examples=50)
def test_cppmodel::parameter_instantiation(instance):
    assert isinstance(instance, cppmodel::Parameter)

@given(instance=cppmodel::XTEvent_strategy)
@settings(max_examples=50)
def test_cppmodel::xtevent_instantiation(instance):
    assert isinstance(instance, cppmodel::XTEvent)

@given(instance=cppmodel::Transition_strategy)
@settings(max_examples=50)
def test_cppmodel::transition_instantiation(instance):
    assert isinstance(instance, cppmodel::Transition)

@given(instance=cppmodel::TypedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_cppmodel::typedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, cppmodel::TypedMultiplicityElement)

@given(instance=cppmodel::State_strategy)
@settings(max_examples=50)
def test_cppmodel::state_instantiation(instance):
    assert isinstance(instance, cppmodel::State)

@given(instance=cppmodel::OOPLDataType_strategy)
@settings(max_examples=50)
def test_cppmodel::oopldatatype_instantiation(instance):
    assert isinstance(instance, cppmodel::OOPLDataType)

@given(instance=cppmodel::CPPSequence_strategy)
@settings(max_examples=50)
def test_cppmodel::cppsequence_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPSequence)

@given(instance=cppmodel::CPPSequence_strategy)
def test_cppmodel::cppsequence_cppContainer_type(instance):
    assert isinstance(instance.cppContainer, str)


@given(instance=cppmodel::CPPSequence_strategy)
def test_cppmodel::cppsequence_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel::Attribute_strategy)
@settings(max_examples=50)
def test_cppmodel::attribute_instantiation(instance):
    assert isinstance(instance, cppmodel::Attribute)

@given(instance=OOPLClassRefAssocCollection_strategy)
@settings(max_examples=50)
def test_ooplclassrefassoccollection_instantiation(instance):
    assert isinstance(instance, OOPLClassRefAssocCollection)

@given(instance=OOPLClassRefSimpleCollection_strategy)
@settings(max_examples=50)
def test_ooplclassrefsimplecollection_instantiation(instance):
    assert isinstance(instance, OOPLClassRefSimpleCollection)

@given(instance=OOPLClassReferenceStorage_strategy)
@settings(max_examples=50)
def test_ooplclassreferencestorage_instantiation(instance):
    assert isinstance(instance, OOPLClassReferenceStorage)

@given(instance=OOPLClassReference_strategy)
@settings(max_examples=50)
def test_ooplclassreference_instantiation(instance):
    assert isinstance(instance, OOPLClassReference)

@given(instance=cppmodel::XTProtocolOperationImplementation_strategy)
@settings(max_examples=50)
def test_cppmodel::xtprotocoloperationimplementation_instantiation(instance):
    assert isinstance(instance, cppmodel::XTProtocolOperationImplementation)

@given(instance=cppmodel::XTProtocolOperationDefinition_strategy)
@settings(max_examples=50)
def test_cppmodel::xtprotocoloperationdefinition_instantiation(instance):
    assert isinstance(instance, cppmodel::XTProtocolOperationDefinition)

@given(instance=cppmodel::XTPort_strategy)
@settings(max_examples=50)
def test_cppmodel::xtport_instantiation(instance):
    assert isinstance(instance, cppmodel::XTPort)

@given(instance=cppmodel::Snippet_strategy)
@settings(max_examples=50)
def test_cppmodel::snippet_instantiation(instance):
    assert isinstance(instance, cppmodel::Snippet)

@given(instance=cppmodel::Signal_strategy)
@settings(max_examples=50)
def test_cppmodel::signal_instantiation(instance):
    assert isinstance(instance, cppmodel::Signal)

@given(instance=cppmodel::Operation_strategy)
@settings(max_examples=50)
def test_cppmodel::operation_instantiation(instance):
    assert isinstance(instance, cppmodel::Operation)

@given(instance=OOPLRelation_strategy)
@settings(max_examples=50)
def test_ooplrelation_instantiation(instance):
    assert isinstance(instance, OOPLRelation)

@given(instance=cppmodel::CPPExternalHeader_strategy)
@settings(max_examples=50)
def test_cppmodel::cppexternalheader_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPExternalHeader)

@given(instance=cppmodel::CPPExternalHeader_strategy)
def test_cppmodel::cppexternalheader_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cppmodel::CPPExternalHeader_strategy)
def test_cppmodel::cppexternalheader_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cppmodel::XTComponent_strategy)
@settings(max_examples=50)
def test_cppmodel::xtcomponent_instantiation(instance):
    assert isinstance(instance, cppmodel::XTComponent)

@given(instance=CPPSourceFile_strategy)
@settings(max_examples=50)
def test_cppsourcefile_instantiation(instance):
    assert isinstance(instance, CPPSourceFile)

@given(instance=cppmodel::CPPMakeFile_strategy)
@settings(max_examples=50)
def test_cppmodel::cppmakefile_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPMakeFile)

@given(instance=cppmodel::CPPExternalHeaderInclusion_strategy)
@settings(max_examples=50)
def test_cppmodel::cppexternalheaderinclusion_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPExternalHeaderInclusion)

@given(instance=cppmodel::CPPExternalHeaderInclusion_strategy)
def test_cppmodel::cppexternalheaderinclusion_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=cppmodel::CPPExternalHeaderInclusion_strategy)
def test_cppmodel::cppexternalheaderinclusion_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cppmodel::CPPSourceFile_strategy)
@settings(max_examples=50)
def test_cppmodel::cppsourcefile_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPSourceFile)

@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationName_type(instance):
    assert isinstance(instance.generationName, str)


@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationName_setter(instance):
    original = instance.generationName
    instance.generationName = original
    assert instance.generationName == original

@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationPath_type(instance):
    assert isinstance(instance.generationPath, str)


@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationPath_setter(instance):
    original = instance.generationPath
    instance.generationPath = original
    assert instance.generationPath == original

@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationDirectory_type(instance):
    assert isinstance(instance.generationDirectory, str)


@given(instance=cppmodel::CPPSourceFile_strategy)
def test_cppmodel::cppsourcefile_generationDirectory_setter(instance):
    original = instance.generationDirectory
    instance.generationDirectory = original
    assert instance.generationDirectory == original

@given(instance=cppmodel::XTProtocol_strategy)
@settings(max_examples=50)
def test_cppmodel::xtprotocol_instantiation(instance):
    assert isinstance(instance, cppmodel::XTProtocol)

@given(instance=OOPLClass_strategy)
@settings(max_examples=50)
def test_ooplclass_instantiation(instance):
    assert isinstance(instance, OOPLClass)

@given(instance=cppmodel::Package_strategy)
@settings(max_examples=50)
def test_cppmodel::package_instantiation(instance):
    assert isinstance(instance, cppmodel::Package)

@given(instance=cppmodel::CPPDirectory_strategy)
@settings(max_examples=50)
def test_cppmodel::cppdirectory_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPDirectory)

@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_parentDirectory_type(instance):
    assert isinstance(instance.parentDirectory, str)


@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_parentDirectory_setter(instance):
    original = instance.parentDirectory
    instance.parentDirectory = original
    assert instance.parentDirectory == original

@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cppmodel::CPPDirectory_strategy)
def test_cppmodel::cppdirectory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cppmodel::CPPHeaderFile_strategy)
@settings(max_examples=50)
def test_cppmodel::cppheaderfile_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPHeaderFile)

@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includePath_type(instance):
    assert isinstance(instance.includePath, str)


@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includePath_setter(instance):
    original = instance.includePath
    instance.includePath = original
    assert instance.includePath == original

@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includeName_type(instance):
    assert isinstance(instance.includeName, str)


@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includeName_setter(instance):
    original = instance.includeName
    instance.includeName = original
    assert instance.includeName == original

@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includeDirectory_type(instance):
    assert isinstance(instance.includeDirectory, str)


@given(instance=cppmodel::CPPHeaderFile_strategy)
def test_cppmodel::cppheaderfile_includeDirectory_setter(instance):
    original = instance.includeDirectory
    instance.includeDirectory = original
    assert instance.includeDirectory == original

@given(instance=cppmodel::CPPBodyFile_strategy)
@settings(max_examples=50)
def test_cppmodel::cppbodyfile_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPBodyFile)

@given(instance=cppmodel::Model_strategy)
@settings(max_examples=50)
def test_cppmodel::model_instantiation(instance):
    assert isinstance(instance, cppmodel::Model)

@given(instance=CPPQualifiedNamedElement_strategy)
@settings(max_examples=50)
def test_cppqualifiednamedelement_instantiation(instance):
    assert isinstance(instance, CPPQualifiedNamedElement)

@given(instance=cppmodel::CPPReturnValue_strategy)
@settings(max_examples=50)
def test_cppmodel::cppreturnvalue_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPReturnValue)

@given(instance=cppmodel::CPPClassRefSimpleCollection_strategy)
@settings(max_examples=50)
def test_cppmodel::cppclassrefsimplecollection_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPClassRefSimpleCollection)

@given(instance=cppmodel::CPPClassRefSimpleCollection_strategy)
def test_cppmodel::cppclassrefsimplecollection_cppContainer_type(instance):
    assert isinstance(instance.cppContainer, str)


@given(instance=cppmodel::CPPClassRefSimpleCollection_strategy)
def test_cppmodel::cppclassrefsimplecollection_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel::CPPProtocolOperationDefinition_strategy)
@settings(max_examples=50)
def test_cppmodel::cppprotocoloperationdefinition_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPProtocolOperationDefinition)

@given(instance=cppmodel::CPPAttribute_strategy)
@settings(max_examples=50)
def test_cppmodel::cppattribute_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPAttribute)

@given(instance=cppmodel::CPPState_strategy)
@settings(max_examples=50)
def test_cppmodel::cppstate_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPState)

@given(instance=cppmodel::CPPProtocolOperationImplementation_strategy)
@settings(max_examples=50)
def test_cppmodel::cppprotocoloperationimplementation_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPProtocolOperationImplementation)

@given(instance=cppmodel::CPPRelation_strategy)
@settings(max_examples=50)
def test_cppmodel::cpprelation_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPRelation)

@given(instance=cppmodel::CPPClassReferenceStorage_strategy)
@settings(max_examples=50)
def test_cppmodel::cppclassreferencestorage_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPClassReferenceStorage)

@given(instance=cppmodel::CPPClass_strategy)
@settings(max_examples=50)
def test_cppmodel::cppclass_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPClass)

@given(instance=cppmodel::CPPPort_strategy)
@settings(max_examples=50)
def test_cppmodel::cppport_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPPort)

@given(instance=cppmodel::CPPStructType_strategy)
@settings(max_examples=50)
def test_cppmodel::cppstructtype_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPStructType)

@given(instance=cppmodel::CPPProtocol_strategy)
@settings(max_examples=50)
def test_cppmodel::cppprotocol_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPProtocol)

@given(instance=cppmodel::CPPOperation_strategy)
@settings(max_examples=50)
def test_cppmodel::cppoperation_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPOperation)

@given(instance=cppmodel::CPPTransition_strategy)
@settings(max_examples=50)
def test_cppmodel::cpptransition_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPTransition)

@given(instance=cppmodel::CPPUserDefinedType_strategy)
@settings(max_examples=50)
def test_cppmodel::cppuserdefinedtype_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPUserDefinedType)

@given(instance=cppmodel::CPPClassReference_strategy)
@settings(max_examples=50)
def test_cppmodel::cppclassreference_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPClassReference)

@given(instance=cppmodel::CPPBasicType_strategy)
@settings(max_examples=50)
def test_cppmodel::cppbasictype_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPBasicType)

@given(instance=cppmodel::CPPBasicType_strategy)
def test_cppmodel::cppbasictype_cppSpecifier_type(instance):
    assert isinstance(instance.cppSpecifier, str)


@given(instance=cppmodel::CPPBasicType_strategy)
def test_cppmodel::cppbasictype_cppSpecifier_setter(instance):
    original = instance.cppSpecifier
    instance.cppSpecifier = original
    assert instance.cppSpecifier == original

@given(instance=cppmodel::CPPFormalParameter_strategy)
@settings(max_examples=50)
def test_cppmodel::cppformalparameter_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPFormalParameter)

@given(instance=cppmodel::CPPFormalParameter_strategy)
def test_cppmodel::cppformalparameter_passingMode_type(instance):
    assert isinstance(instance.passingMode, str)


@given(instance=cppmodel::CPPFormalParameter_strategy)
def test_cppmodel::cppformalparameter_passingMode_setter(instance):
    original = instance.passingMode
    instance.passingMode = original
    assert instance.passingMode == original

@given(instance=cppmodel::CPPComponent_strategy)
@settings(max_examples=50)
def test_cppmodel::cppcomponent_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPComponent)

@given(instance=cppmodel::CPPClassRefAssocCollection_strategy)
@settings(max_examples=50)
def test_cppmodel::cppclassrefassoccollection_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPClassRefAssocCollection)

@given(instance=cppmodel::CPPClassRefAssocCollection_strategy)
def test_cppmodel::cppclassrefassoccollection_cppContainer_type(instance):
    assert isinstance(instance.cppContainer, str)


@given(instance=cppmodel::CPPClassRefAssocCollection_strategy)
def test_cppmodel::cppclassrefassoccollection_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel::CPPSignal_strategy)
@settings(max_examples=50)
def test_cppmodel::cppsignal_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPSignal)

@given(instance=cppmodel::CPPEnumType_strategy)
@settings(max_examples=50)
def test_cppmodel::cppenumtype_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPEnumType)

@given(instance=cppmodel::CPPPackage_strategy)
@settings(max_examples=50)
def test_cppmodel::cpppackage_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPPackage)

@given(instance=cppmodel::CPPEvent_strategy)
@settings(max_examples=50)
def test_cppmodel::cppevent_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPEvent)

@given(instance=cppmodel::CPPEnumerator_strategy)
@settings(max_examples=50)
def test_cppmodel::cppenumerator_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPEnumerator)

@given(instance=cppmodel::CPPEnumerator_strategy)
def test_cppmodel::cppenumerator_cppValue_type(instance):
    assert isinstance(instance.cppValue, str)


@given(instance=cppmodel::CPPEnumerator_strategy)
def test_cppmodel::cppenumerator_cppValue_setter(instance):
    original = instance.cppValue
    instance.cppValue = original
    assert instance.cppValue == original

@given(instance=cppmodel::CPPStructMember_strategy)
@settings(max_examples=50)
def test_cppmodel::cppstructmember_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPStructMember)

@given(instance=cppmodel::CPPExternalBridge_strategy)
@settings(max_examples=50)
def test_cppmodel::cppexternalbridge_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPExternalBridge)

@given(instance=cppmodel::CPPExternalBridge_strategy)
def test_cppmodel::cppexternalbridge_cppExternalNamespace_type(instance):
    assert isinstance(instance.cppExternalNamespace, str)


@given(instance=cppmodel::CPPExternalBridge_strategy)
def test_cppmodel::cppexternalbridge_cppExternalNamespace_setter(instance):
    original = instance.cppExternalNamespace
    instance.cppExternalNamespace = original
    assert instance.cppExternalNamespace == original

@given(instance=cppmodel::CPPModel_strategy)
@settings(max_examples=50)
def test_cppmodel::cppmodel_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPModel)

@given(instance=CPPNamedElement_strategy)
@settings(max_examples=50)
def test_cppnamedelement_instantiation(instance):
    assert isinstance(instance, CPPNamedElement)

@given(instance=cppmodel::CPPQualifiedNamedElement_strategy)
@settings(max_examples=50)
def test_cppmodel::cppqualifiednamedelement_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPQualifiedNamedElement)

@given(instance=cppmodel::CPPQualifiedNamedElement_strategy)
def test_cppmodel::cppqualifiednamedelement_cppPrefix_type(instance):
    assert isinstance(instance.cppPrefix, str)


@given(instance=cppmodel::CPPQualifiedNamedElement_strategy)
def test_cppmodel::cppqualifiednamedelement_cppPrefix_setter(instance):
    original = instance.cppPrefix
    instance.cppPrefix = original
    assert instance.cppPrefix == original

@given(instance=cppmodel::CPPQualifiedNamedElement_strategy)
def test_cppmodel::cppqualifiednamedelement_cppQualifiedName_type(instance):
    assert isinstance(instance.cppQualifiedName, str)


@given(instance=cppmodel::CPPQualifiedNamedElement_strategy)
def test_cppmodel::cppqualifiednamedelement_cppQualifiedName_setter(instance):
    original = instance.cppQualifiedName
    instance.cppQualifiedName = original
    assert instance.cppQualifiedName == original

@given(instance=cppmodel::OOPLNameProvider_strategy)
@settings(max_examples=50)
def test_cppmodel::ooplnameprovider_instantiation(instance):
    assert isinstance(instance, cppmodel::OOPLNameProvider)

@given(instance=cppmodel::CPPNamedElement_strategy)
@settings(max_examples=50)
def test_cppmodel::cppnamedelement_instantiation(instance):
    assert isinstance(instance, cppmodel::CPPNamedElement)

@given(instance=cppmodel::CPPNamedElement_strategy)
def test_cppmodel::cppnamedelement_cppName_type(instance):
    assert isinstance(instance.cppName, str)


@given(instance=cppmodel::CPPNamedElement_strategy)
def test_cppmodel::cppnamedelement_cppName_setter(instance):
    original = instance.cppName
    instance.cppName = original
    assert instance.cppName == original
