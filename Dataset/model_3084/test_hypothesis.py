import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cppmodel_XTClass,
    OOPLUserDefinedType,
    OOPLStructMember,
    OOPLStructType,
    OOPLEnumerator,
    OOPLEnumType,
    OOPLSequence,
    OOPLBasicType,
    cppmodel_CPPExternalLibrary,
    cppmodel_Parameter,
    cppmodel_XTEvent,
    cppmodel_Transition,
    cppmodel_TypedMultiplicityElement,
    cppmodel_State,
    cppmodel_OOPLDataType,
    cppmodel_CPPSequence,
    cppmodel_Attribute,
    OOPLClassRefAssocCollection,
    OOPLClassRefSimpleCollection,
    OOPLClassReferenceStorage,
    OOPLClassReference,
    cppmodel_XTProtocolOperationImplementation,
    cppmodel_XTProtocolOperationDefinition,
    cppmodel_XTPort,
    cppmodel_Snippet,
    cppmodel_Signal,
    cppmodel_Operation,
    OOPLRelation,
    cppmodel_CPPExternalHeader,
    cppmodel_XTComponent,
    CPPSourceFile,
    cppmodel_CPPMakeFile,
    cppmodel_CPPExternalHeaderInclusion,
    cppmodel_CPPSourceFile,
    cppmodel_XTProtocol,
    OOPLClass,
    cppmodel_Package,
    cppmodel_CPPDirectory,
    cppmodel_CPPHeaderFile,
    cppmodel_CPPBodyFile,
    cppmodel_Model,
    CPPQualifiedNamedElement,
    cppmodel_CPPRelation,
    cppmodel_CPPClass,
    cppmodel_CPPProtocol,
    cppmodel_CPPBasicType,
    cppmodel_CPPClassReferenceStorage,
    cppmodel_CPPProtocolOperationImplementation,
    cppmodel_CPPPackage,
    cppmodel_CPPAttribute,
    cppmodel_CPPClassRefAssocCollection,
    cppmodel_CPPFormalParameter,
    cppmodel_CPPUserDefinedType,
    cppmodel_CPPEnumerator,
    cppmodel_CPPTransition,
    cppmodel_CPPClassRefSimpleCollection,
    cppmodel_CPPClassReference,
    cppmodel_CPPSignal,
    cppmodel_CPPReturnValue,
    cppmodel_CPPEvent,
    cppmodel_CPPComponent,
    cppmodel_CPPProtocolOperationDefinition,
    cppmodel_CPPState,
    cppmodel_CPPOperation,
    cppmodel_CPPExternalBridge,
    cppmodel_CPPPort,
    cppmodel_CPPEnumType,
    cppmodel_CPPStructType,
    cppmodel_CPPStructMember,
    cppmodel_CPPModel,
    CPPNamedElement,
    cppmodel_CPPQualifiedNamedElement,
    cppmodel_OOPLNameProvider,
    cppmodel_CPPNamedElement,
    CPPParameterPassingKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cppmodel_xtclass_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTClass)


def test_cppmodel_xtclass_constructor_exists():
    assert callable(cppmodel_XTClass.__init__)


def test_cppmodel_xtclass_constructor_args():
    sig = inspect.signature(cppmodel_XTClass.__init__)
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



def test_cppmodel_cppexternallibrary_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPExternalLibrary)


def test_cppmodel_cppexternallibrary_constructor_exists():
    assert callable(cppmodel_CPPExternalLibrary.__init__)


def test_cppmodel_cppexternallibrary_constructor_args():
    sig = inspect.signature(cppmodel_CPPExternalLibrary.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Parameter)


def test_cppmodel_parameter_constructor_exists():
    assert callable(cppmodel_Parameter.__init__)


def test_cppmodel_parameter_constructor_args():
    sig = inspect.signature(cppmodel_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_xtevent_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTEvent)


def test_cppmodel_xtevent_constructor_exists():
    assert callable(cppmodel_XTEvent.__init__)


def test_cppmodel_xtevent_constructor_args():
    sig = inspect.signature(cppmodel_XTEvent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_transition_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Transition)


def test_cppmodel_transition_constructor_exists():
    assert callable(cppmodel_Transition.__init__)


def test_cppmodel_transition_constructor_args():
    sig = inspect.signature(cppmodel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_typedmultiplicityelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel_TypedMultiplicityElement)


def test_cppmodel_typedmultiplicityelement_constructor_exists():
    assert callable(cppmodel_TypedMultiplicityElement.__init__)


def test_cppmodel_typedmultiplicityelement_constructor_args():
    sig = inspect.signature(cppmodel_TypedMultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_state_is_not_abstract():
    assert not inspect.isabstract(cppmodel_State)


def test_cppmodel_state_constructor_exists():
    assert callable(cppmodel_State.__init__)


def test_cppmodel_state_constructor_args():
    sig = inspect.signature(cppmodel_State.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_oopldatatype_is_not_abstract():
    assert not inspect.isabstract(cppmodel_OOPLDataType)


def test_cppmodel_oopldatatype_constructor_exists():
    assert callable(cppmodel_OOPLDataType.__init__)


def test_cppmodel_oopldatatype_constructor_args():
    sig = inspect.signature(cppmodel_OOPLDataType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppsequence_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPSequence)


def test_cppmodel_cppsequence_constructor_exists():
    assert callable(cppmodel_CPPSequence.__init__)


def test_cppmodel_cppsequence_constructor_args():
    sig = inspect.signature(cppmodel_CPPSequence.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel_cppsequence_has_cppContainer():
    assert hasattr(cppmodel_CPPSequence, "cppContainer")
    descriptor = None
    for klass in cppmodel_CPPSequence.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_attribute_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Attribute)


def test_cppmodel_attribute_constructor_exists():
    assert callable(cppmodel_Attribute.__init__)


def test_cppmodel_attribute_constructor_args():
    sig = inspect.signature(cppmodel_Attribute.__init__)
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



def test_cppmodel_xtprotocoloperationimplementation_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTProtocolOperationImplementation)


def test_cppmodel_xtprotocoloperationimplementation_constructor_exists():
    assert callable(cppmodel_XTProtocolOperationImplementation.__init__)


def test_cppmodel_xtprotocoloperationimplementation_constructor_args():
    sig = inspect.signature(cppmodel_XTProtocolOperationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_xtprotocoloperationdefinition_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTProtocolOperationDefinition)


def test_cppmodel_xtprotocoloperationdefinition_constructor_exists():
    assert callable(cppmodel_XTProtocolOperationDefinition.__init__)


def test_cppmodel_xtprotocoloperationdefinition_constructor_args():
    sig = inspect.signature(cppmodel_XTProtocolOperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_xtport_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTPort)


def test_cppmodel_xtport_constructor_exists():
    assert callable(cppmodel_XTPort.__init__)


def test_cppmodel_xtport_constructor_args():
    sig = inspect.signature(cppmodel_XTPort.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_snippet_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Snippet)


def test_cppmodel_snippet_constructor_exists():
    assert callable(cppmodel_Snippet.__init__)


def test_cppmodel_snippet_constructor_args():
    sig = inspect.signature(cppmodel_Snippet.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_signal_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Signal)


def test_cppmodel_signal_constructor_exists():
    assert callable(cppmodel_Signal.__init__)


def test_cppmodel_signal_constructor_args():
    sig = inspect.signature(cppmodel_Signal.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_operation_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Operation)


def test_cppmodel_operation_constructor_exists():
    assert callable(cppmodel_Operation.__init__)


def test_cppmodel_operation_constructor_args():
    sig = inspect.signature(cppmodel_Operation.__init__)
    params = list(sig.parameters.keys())



def test_ooplrelation_is_not_abstract():
    assert not inspect.isabstract(OOPLRelation)


def test_ooplrelation_constructor_exists():
    assert callable(OOPLRelation.__init__)


def test_ooplrelation_constructor_args():
    sig = inspect.signature(OOPLRelation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppexternalheader_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPExternalHeader)


def test_cppmodel_cppexternalheader_constructor_exists():
    assert callable(cppmodel_CPPExternalHeader.__init__)


def test_cppmodel_cppexternalheader_constructor_args():
    sig = inspect.signature(cppmodel_CPPExternalHeader.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cppmodel_cppexternalheader_has_name():
    assert hasattr(cppmodel_CPPExternalHeader, "name")
    descriptor = None
    for klass in cppmodel_CPPExternalHeader.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_xtcomponent_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTComponent)


def test_cppmodel_xtcomponent_constructor_exists():
    assert callable(cppmodel_XTComponent.__init__)


def test_cppmodel_xtcomponent_constructor_args():
    sig = inspect.signature(cppmodel_XTComponent.__init__)
    params = list(sig.parameters.keys())



def test_cppsourcefile_is_not_abstract():
    assert not inspect.isabstract(CPPSourceFile)


def test_cppsourcefile_constructor_exists():
    assert callable(CPPSourceFile.__init__)


def test_cppsourcefile_constructor_args():
    sig = inspect.signature(CPPSourceFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppmakefile_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPMakeFile)


def test_cppmodel_cppmakefile_constructor_exists():
    assert callable(cppmodel_CPPMakeFile.__init__)


def test_cppmodel_cppmakefile_constructor_args():
    sig = inspect.signature(cppmodel_CPPMakeFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppexternalheaderinclusion_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPExternalHeaderInclusion)


def test_cppmodel_cppexternalheaderinclusion_constructor_exists():
    assert callable(cppmodel_CPPExternalHeaderInclusion.__init__)


def test_cppmodel_cppexternalheaderinclusion_constructor_args():
    sig = inspect.signature(cppmodel_CPPExternalHeaderInclusion.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_cppmodel_cppexternalheaderinclusion_has_comment():
    assert hasattr(cppmodel_CPPExternalHeaderInclusion, "comment")
    descriptor = None
    for klass in cppmodel_CPPExternalHeaderInclusion.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppsourcefile_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPSourceFile)


def test_cppmodel_cppsourcefile_constructor_exists():
    assert callable(cppmodel_CPPSourceFile.__init__)


def test_cppmodel_cppsourcefile_constructor_args():
    sig = inspect.signature(cppmodel_CPPSourceFile.__init__)
    params = list(sig.parameters.keys())
    assert "generationName" in params, "Missing parameter 'generationName'"
    assert "generationDirectory" in params, "Missing parameter 'generationDirectory'"
    assert "generationPath" in params, "Missing parameter 'generationPath'"

def test_cppmodel_cppsourcefile_has_generationName():
    assert hasattr(cppmodel_CPPSourceFile, "generationName")
    descriptor = None
    for klass in cppmodel_CPPSourceFile.__mro__:
        if "generationName" in klass.__dict__:
            descriptor = klass.__dict__["generationName"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppsourcefile_has_generationDirectory():
    assert hasattr(cppmodel_CPPSourceFile, "generationDirectory")
    descriptor = None
    for klass in cppmodel_CPPSourceFile.__mro__:
        if "generationDirectory" in klass.__dict__:
            descriptor = klass.__dict__["generationDirectory"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppsourcefile_has_generationPath():
    assert hasattr(cppmodel_CPPSourceFile, "generationPath")
    descriptor = None
    for klass in cppmodel_CPPSourceFile.__mro__:
        if "generationPath" in klass.__dict__:
            descriptor = klass.__dict__["generationPath"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_xtprotocol_is_not_abstract():
    assert not inspect.isabstract(cppmodel_XTProtocol)


def test_cppmodel_xtprotocol_constructor_exists():
    assert callable(cppmodel_XTProtocol.__init__)


def test_cppmodel_xtprotocol_constructor_args():
    sig = inspect.signature(cppmodel_XTProtocol.__init__)
    params = list(sig.parameters.keys())



def test_ooplclass_is_not_abstract():
    assert not inspect.isabstract(OOPLClass)


def test_ooplclass_constructor_exists():
    assert callable(OOPLClass.__init__)


def test_ooplclass_constructor_args():
    sig = inspect.signature(OOPLClass.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_package_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Package)


def test_cppmodel_package_constructor_exists():
    assert callable(cppmodel_Package.__init__)


def test_cppmodel_package_constructor_args():
    sig = inspect.signature(cppmodel_Package.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppdirectory_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPDirectory)


def test_cppmodel_cppdirectory_constructor_exists():
    assert callable(cppmodel_CPPDirectory.__init__)


def test_cppmodel_cppdirectory_constructor_args():
    sig = inspect.signature(cppmodel_CPPDirectory.__init__)
    params = list(sig.parameters.keys())
    assert "parentDirectory" in params, "Missing parameter 'parentDirectory'"
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"

def test_cppmodel_cppdirectory_has_parentDirectory():
    assert hasattr(cppmodel_CPPDirectory, "parentDirectory")
    descriptor = None
    for klass in cppmodel_CPPDirectory.__mro__:
        if "parentDirectory" in klass.__dict__:
            descriptor = klass.__dict__["parentDirectory"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppdirectory_has_path():
    assert hasattr(cppmodel_CPPDirectory, "path")
    descriptor = None
    for klass in cppmodel_CPPDirectory.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppdirectory_has_name():
    assert hasattr(cppmodel_CPPDirectory, "name")
    descriptor = None
    for klass in cppmodel_CPPDirectory.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppheaderfile_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPHeaderFile)


def test_cppmodel_cppheaderfile_constructor_exists():
    assert callable(cppmodel_CPPHeaderFile.__init__)


def test_cppmodel_cppheaderfile_constructor_args():
    sig = inspect.signature(cppmodel_CPPHeaderFile.__init__)
    params = list(sig.parameters.keys())
    assert "includeDirectory" in params, "Missing parameter 'includeDirectory'"
    assert "includeName" in params, "Missing parameter 'includeName'"
    assert "includePath" in params, "Missing parameter 'includePath'"

def test_cppmodel_cppheaderfile_has_includeDirectory():
    assert hasattr(cppmodel_CPPHeaderFile, "includeDirectory")
    descriptor = None
    for klass in cppmodel_CPPHeaderFile.__mro__:
        if "includeDirectory" in klass.__dict__:
            descriptor = klass.__dict__["includeDirectory"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppheaderfile_has_includeName():
    assert hasattr(cppmodel_CPPHeaderFile, "includeName")
    descriptor = None
    for klass in cppmodel_CPPHeaderFile.__mro__:
        if "includeName" in klass.__dict__:
            descriptor = klass.__dict__["includeName"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppheaderfile_has_includePath():
    assert hasattr(cppmodel_CPPHeaderFile, "includePath")
    descriptor = None
    for klass in cppmodel_CPPHeaderFile.__mro__:
        if "includePath" in klass.__dict__:
            descriptor = klass.__dict__["includePath"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppbodyfile_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPBodyFile)


def test_cppmodel_cppbodyfile_constructor_exists():
    assert callable(cppmodel_CPPBodyFile.__init__)


def test_cppmodel_cppbodyfile_constructor_args():
    sig = inspect.signature(cppmodel_CPPBodyFile.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_model_is_not_abstract():
    assert not inspect.isabstract(cppmodel_Model)


def test_cppmodel_model_constructor_exists():
    assert callable(cppmodel_Model.__init__)


def test_cppmodel_model_constructor_args():
    sig = inspect.signature(cppmodel_Model.__init__)
    params = list(sig.parameters.keys())



def test_cppqualifiednamedelement_is_not_abstract():
    assert not inspect.isabstract(CPPQualifiedNamedElement)


def test_cppqualifiednamedelement_constructor_exists():
    assert callable(CPPQualifiedNamedElement.__init__)


def test_cppqualifiednamedelement_constructor_args():
    sig = inspect.signature(CPPQualifiedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cpprelation_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPRelation)


def test_cppmodel_cpprelation_constructor_exists():
    assert callable(cppmodel_CPPRelation.__init__)


def test_cppmodel_cpprelation_constructor_args():
    sig = inspect.signature(cppmodel_CPPRelation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppclass_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPClass)


def test_cppmodel_cppclass_constructor_exists():
    assert callable(cppmodel_CPPClass.__init__)


def test_cppmodel_cppclass_constructor_args():
    sig = inspect.signature(cppmodel_CPPClass.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppprotocol_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPProtocol)


def test_cppmodel_cppprotocol_constructor_exists():
    assert callable(cppmodel_CPPProtocol.__init__)


def test_cppmodel_cppprotocol_constructor_args():
    sig = inspect.signature(cppmodel_CPPProtocol.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppbasictype_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPBasicType)


def test_cppmodel_cppbasictype_constructor_exists():
    assert callable(cppmodel_CPPBasicType.__init__)


def test_cppmodel_cppbasictype_constructor_args():
    sig = inspect.signature(cppmodel_CPPBasicType.__init__)
    params = list(sig.parameters.keys())
    assert "cppSpecifier" in params, "Missing parameter 'cppSpecifier'"

def test_cppmodel_cppbasictype_has_cppSpecifier():
    assert hasattr(cppmodel_CPPBasicType, "cppSpecifier")
    descriptor = None
    for klass in cppmodel_CPPBasicType.__mro__:
        if "cppSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["cppSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppclassreferencestorage_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPClassReferenceStorage)


def test_cppmodel_cppclassreferencestorage_constructor_exists():
    assert callable(cppmodel_CPPClassReferenceStorage.__init__)


def test_cppmodel_cppclassreferencestorage_constructor_args():
    sig = inspect.signature(cppmodel_CPPClassReferenceStorage.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppprotocoloperationimplementation_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPProtocolOperationImplementation)


def test_cppmodel_cppprotocoloperationimplementation_constructor_exists():
    assert callable(cppmodel_CPPProtocolOperationImplementation.__init__)


def test_cppmodel_cppprotocoloperationimplementation_constructor_args():
    sig = inspect.signature(cppmodel_CPPProtocolOperationImplementation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cpppackage_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPPackage)


def test_cppmodel_cpppackage_constructor_exists():
    assert callable(cppmodel_CPPPackage.__init__)


def test_cppmodel_cpppackage_constructor_args():
    sig = inspect.signature(cppmodel_CPPPackage.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppattribute_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPAttribute)


def test_cppmodel_cppattribute_constructor_exists():
    assert callable(cppmodel_CPPAttribute.__init__)


def test_cppmodel_cppattribute_constructor_args():
    sig = inspect.signature(cppmodel_CPPAttribute.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppclassrefassoccollection_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPClassRefAssocCollection)


def test_cppmodel_cppclassrefassoccollection_constructor_exists():
    assert callable(cppmodel_CPPClassRefAssocCollection.__init__)


def test_cppmodel_cppclassrefassoccollection_constructor_args():
    sig = inspect.signature(cppmodel_CPPClassRefAssocCollection.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel_cppclassrefassoccollection_has_cppContainer():
    assert hasattr(cppmodel_CPPClassRefAssocCollection, "cppContainer")
    descriptor = None
    for klass in cppmodel_CPPClassRefAssocCollection.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppformalparameter_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPFormalParameter)


def test_cppmodel_cppformalparameter_constructor_exists():
    assert callable(cppmodel_CPPFormalParameter.__init__)


def test_cppmodel_cppformalparameter_constructor_args():
    sig = inspect.signature(cppmodel_CPPFormalParameter.__init__)
    params = list(sig.parameters.keys())
    assert "passingMode" in params, "Missing parameter 'passingMode'"

def test_cppmodel_cppformalparameter_has_passingMode():
    assert hasattr(cppmodel_CPPFormalParameter, "passingMode")
    descriptor = None
    for klass in cppmodel_CPPFormalParameter.__mro__:
        if "passingMode" in klass.__dict__:
            descriptor = klass.__dict__["passingMode"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppuserdefinedtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPUserDefinedType)


def test_cppmodel_cppuserdefinedtype_constructor_exists():
    assert callable(cppmodel_CPPUserDefinedType.__init__)


def test_cppmodel_cppuserdefinedtype_constructor_args():
    sig = inspect.signature(cppmodel_CPPUserDefinedType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppenumerator_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPEnumerator)


def test_cppmodel_cppenumerator_constructor_exists():
    assert callable(cppmodel_CPPEnumerator.__init__)


def test_cppmodel_cppenumerator_constructor_args():
    sig = inspect.signature(cppmodel_CPPEnumerator.__init__)
    params = list(sig.parameters.keys())
    assert "cppValue" in params, "Missing parameter 'cppValue'"

def test_cppmodel_cppenumerator_has_cppValue():
    assert hasattr(cppmodel_CPPEnumerator, "cppValue")
    descriptor = None
    for klass in cppmodel_CPPEnumerator.__mro__:
        if "cppValue" in klass.__dict__:
            descriptor = klass.__dict__["cppValue"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cpptransition_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPTransition)


def test_cppmodel_cpptransition_constructor_exists():
    assert callable(cppmodel_CPPTransition.__init__)


def test_cppmodel_cpptransition_constructor_args():
    sig = inspect.signature(cppmodel_CPPTransition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppclassrefsimplecollection_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPClassRefSimpleCollection)


def test_cppmodel_cppclassrefsimplecollection_constructor_exists():
    assert callable(cppmodel_CPPClassRefSimpleCollection.__init__)


def test_cppmodel_cppclassrefsimplecollection_constructor_args():
    sig = inspect.signature(cppmodel_CPPClassRefSimpleCollection.__init__)
    params = list(sig.parameters.keys())
    assert "cppContainer" in params, "Missing parameter 'cppContainer'"

def test_cppmodel_cppclassrefsimplecollection_has_cppContainer():
    assert hasattr(cppmodel_CPPClassRefSimpleCollection, "cppContainer")
    descriptor = None
    for klass in cppmodel_CPPClassRefSimpleCollection.__mro__:
        if "cppContainer" in klass.__dict__:
            descriptor = klass.__dict__["cppContainer"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppclassreference_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPClassReference)


def test_cppmodel_cppclassreference_constructor_exists():
    assert callable(cppmodel_CPPClassReference.__init__)


def test_cppmodel_cppclassreference_constructor_args():
    sig = inspect.signature(cppmodel_CPPClassReference.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppsignal_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPSignal)


def test_cppmodel_cppsignal_constructor_exists():
    assert callable(cppmodel_CPPSignal.__init__)


def test_cppmodel_cppsignal_constructor_args():
    sig = inspect.signature(cppmodel_CPPSignal.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppreturnvalue_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPReturnValue)


def test_cppmodel_cppreturnvalue_constructor_exists():
    assert callable(cppmodel_CPPReturnValue.__init__)


def test_cppmodel_cppreturnvalue_constructor_args():
    sig = inspect.signature(cppmodel_CPPReturnValue.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppevent_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPEvent)


def test_cppmodel_cppevent_constructor_exists():
    assert callable(cppmodel_CPPEvent.__init__)


def test_cppmodel_cppevent_constructor_args():
    sig = inspect.signature(cppmodel_CPPEvent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppcomponent_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPComponent)


def test_cppmodel_cppcomponent_constructor_exists():
    assert callable(cppmodel_CPPComponent.__init__)


def test_cppmodel_cppcomponent_constructor_args():
    sig = inspect.signature(cppmodel_CPPComponent.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppprotocoloperationdefinition_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPProtocolOperationDefinition)


def test_cppmodel_cppprotocoloperationdefinition_constructor_exists():
    assert callable(cppmodel_CPPProtocolOperationDefinition.__init__)


def test_cppmodel_cppprotocoloperationdefinition_constructor_args():
    sig = inspect.signature(cppmodel_CPPProtocolOperationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppstate_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPState)


def test_cppmodel_cppstate_constructor_exists():
    assert callable(cppmodel_CPPState.__init__)


def test_cppmodel_cppstate_constructor_args():
    sig = inspect.signature(cppmodel_CPPState.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppoperation_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPOperation)


def test_cppmodel_cppoperation_constructor_exists():
    assert callable(cppmodel_CPPOperation.__init__)


def test_cppmodel_cppoperation_constructor_args():
    sig = inspect.signature(cppmodel_CPPOperation.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppexternalbridge_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPExternalBridge)


def test_cppmodel_cppexternalbridge_constructor_exists():
    assert callable(cppmodel_CPPExternalBridge.__init__)


def test_cppmodel_cppexternalbridge_constructor_args():
    sig = inspect.signature(cppmodel_CPPExternalBridge.__init__)
    params = list(sig.parameters.keys())
    assert "cppExternalNamespace" in params, "Missing parameter 'cppExternalNamespace'"

def test_cppmodel_cppexternalbridge_has_cppExternalNamespace():
    assert hasattr(cppmodel_CPPExternalBridge, "cppExternalNamespace")
    descriptor = None
    for klass in cppmodel_CPPExternalBridge.__mro__:
        if "cppExternalNamespace" in klass.__dict__:
            descriptor = klass.__dict__["cppExternalNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_cppport_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPPort)


def test_cppmodel_cppport_constructor_exists():
    assert callable(cppmodel_CPPPort.__init__)


def test_cppmodel_cppport_constructor_args():
    sig = inspect.signature(cppmodel_CPPPort.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppenumtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPEnumType)


def test_cppmodel_cppenumtype_constructor_exists():
    assert callable(cppmodel_CPPEnumType.__init__)


def test_cppmodel_cppenumtype_constructor_args():
    sig = inspect.signature(cppmodel_CPPEnumType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppstructtype_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPStructType)


def test_cppmodel_cppstructtype_constructor_exists():
    assert callable(cppmodel_CPPStructType.__init__)


def test_cppmodel_cppstructtype_constructor_args():
    sig = inspect.signature(cppmodel_CPPStructType.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppstructmember_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPStructMember)


def test_cppmodel_cppstructmember_constructor_exists():
    assert callable(cppmodel_CPPStructMember.__init__)


def test_cppmodel_cppstructmember_constructor_args():
    sig = inspect.signature(cppmodel_CPPStructMember.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppmodel_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPModel)


def test_cppmodel_cppmodel_constructor_exists():
    assert callable(cppmodel_CPPModel.__init__)


def test_cppmodel_cppmodel_constructor_args():
    sig = inspect.signature(cppmodel_CPPModel.__init__)
    params = list(sig.parameters.keys())



def test_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(CPPNamedElement)


def test_cppnamedelement_constructor_exists():
    assert callable(CPPNamedElement.__init__)


def test_cppnamedelement_constructor_args():
    sig = inspect.signature(CPPNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppqualifiednamedelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPQualifiedNamedElement)


def test_cppmodel_cppqualifiednamedelement_constructor_exists():
    assert callable(cppmodel_CPPQualifiedNamedElement.__init__)


def test_cppmodel_cppqualifiednamedelement_constructor_args():
    sig = inspect.signature(cppmodel_CPPQualifiedNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "cppQualifiedName" in params, "Missing parameter 'cppQualifiedName'"
    assert "cppPrefix" in params, "Missing parameter 'cppPrefix'"

def test_cppmodel_cppqualifiednamedelement_has_cppQualifiedName():
    assert hasattr(cppmodel_CPPQualifiedNamedElement, "cppQualifiedName")
    descriptor = None
    for klass in cppmodel_CPPQualifiedNamedElement.__mro__:
        if "cppQualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["cppQualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_cppmodel_cppqualifiednamedelement_has_cppPrefix():
    assert hasattr(cppmodel_CPPQualifiedNamedElement, "cppPrefix")
    descriptor = None
    for klass in cppmodel_CPPQualifiedNamedElement.__mro__:
        if "cppPrefix" in klass.__dict__:
            descriptor = klass.__dict__["cppPrefix"]
            break
    assert isinstance(descriptor, property)



def test_cppmodel_ooplnameprovider_is_not_abstract():
    assert not inspect.isabstract(cppmodel_OOPLNameProvider)


def test_cppmodel_ooplnameprovider_constructor_exists():
    assert callable(cppmodel_OOPLNameProvider.__init__)


def test_cppmodel_ooplnameprovider_constructor_args():
    sig = inspect.signature(cppmodel_OOPLNameProvider.__init__)
    params = list(sig.parameters.keys())



def test_cppmodel_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(cppmodel_CPPNamedElement)


def test_cppmodel_cppnamedelement_constructor_exists():
    assert callable(cppmodel_CPPNamedElement.__init__)


def test_cppmodel_cppnamedelement_constructor_args():
    sig = inspect.signature(cppmodel_CPPNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "cppName" in params, "Missing parameter 'cppName'"

def test_cppmodel_cppnamedelement_has_cppName():
    assert hasattr(cppmodel_CPPNamedElement, "cppName")
    descriptor = None
    for klass in cppmodel_CPPNamedElement.__mro__:
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
        "BY_REFERENCE",
        "BY_CONSTANT_REFERENCE",
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
cppmodel_XTClass_strategy = st.builds(
    cppmodel_XTClass,
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
cppmodel_CPPExternalLibrary_strategy = st.builds(
    cppmodel_CPPExternalLibrary,
)
cppmodel_Parameter_strategy = st.builds(
    cppmodel_Parameter,
)
cppmodel_XTEvent_strategy = st.builds(
    cppmodel_XTEvent,
)
cppmodel_Transition_strategy = st.builds(
    cppmodel_Transition,
)
cppmodel_TypedMultiplicityElement_strategy = st.builds(
    cppmodel_TypedMultiplicityElement,
)
cppmodel_State_strategy = st.builds(
    cppmodel_State,
)
cppmodel_OOPLDataType_strategy = st.builds(
    cppmodel_OOPLDataType,
)
cppmodel_CPPSequence_strategy = st.builds(
    cppmodel_CPPSequence,
    cppContainer=
        safe_text
)
cppmodel_Attribute_strategy = st.builds(
    cppmodel_Attribute,
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
cppmodel_XTProtocolOperationImplementation_strategy = st.builds(
    cppmodel_XTProtocolOperationImplementation,
)
cppmodel_XTProtocolOperationDefinition_strategy = st.builds(
    cppmodel_XTProtocolOperationDefinition,
)
cppmodel_XTPort_strategy = st.builds(
    cppmodel_XTPort,
)
cppmodel_Snippet_strategy = st.builds(
    cppmodel_Snippet,
)
cppmodel_Signal_strategy = st.builds(
    cppmodel_Signal,
)
cppmodel_Operation_strategy = st.builds(
    cppmodel_Operation,
)
OOPLRelation_strategy = st.builds(
    OOPLRelation,
)
cppmodel_CPPExternalHeader_strategy = st.builds(
    cppmodel_CPPExternalHeader,
    name=
        safe_text
)
cppmodel_XTComponent_strategy = st.builds(
    cppmodel_XTComponent,
)
CPPSourceFile_strategy = st.builds(
    CPPSourceFile,
)
cppmodel_CPPMakeFile_strategy = st.builds(
    cppmodel_CPPMakeFile,
)
cppmodel_CPPExternalHeaderInclusion_strategy = st.builds(
    cppmodel_CPPExternalHeaderInclusion,
    comment=
        safe_text
)
cppmodel_CPPSourceFile_strategy = st.builds(
    cppmodel_CPPSourceFile,
    generationName=
        safe_text,
    generationDirectory=
        safe_text,
    generationPath=
        safe_text
)
cppmodel_XTProtocol_strategy = st.builds(
    cppmodel_XTProtocol,
)
OOPLClass_strategy = st.builds(
    OOPLClass,
)
cppmodel_Package_strategy = st.builds(
    cppmodel_Package,
)
cppmodel_CPPDirectory_strategy = st.builds(
    cppmodel_CPPDirectory,
    parentDirectory=
        safe_text,
    path=
        safe_text,
    name=
        safe_text
)
cppmodel_CPPHeaderFile_strategy = st.builds(
    cppmodel_CPPHeaderFile,
    includeDirectory=
        safe_text,
    includeName=
        safe_text,
    includePath=
        safe_text
)
cppmodel_CPPBodyFile_strategy = st.builds(
    cppmodel_CPPBodyFile,
)
cppmodel_Model_strategy = st.builds(
    cppmodel_Model,
)
CPPQualifiedNamedElement_strategy = st.builds(
    CPPQualifiedNamedElement,
)
cppmodel_CPPRelation_strategy = st.builds(
    cppmodel_CPPRelation,
)
cppmodel_CPPClass_strategy = st.builds(
    cppmodel_CPPClass,
)
cppmodel_CPPProtocol_strategy = st.builds(
    cppmodel_CPPProtocol,
)
cppmodel_CPPBasicType_strategy = st.builds(
    cppmodel_CPPBasicType,
    cppSpecifier=
        safe_text
)
cppmodel_CPPClassReferenceStorage_strategy = st.builds(
    cppmodel_CPPClassReferenceStorage,
)
cppmodel_CPPProtocolOperationImplementation_strategy = st.builds(
    cppmodel_CPPProtocolOperationImplementation,
)
cppmodel_CPPPackage_strategy = st.builds(
    cppmodel_CPPPackage,
)
cppmodel_CPPAttribute_strategy = st.builds(
    cppmodel_CPPAttribute,
)
cppmodel_CPPClassRefAssocCollection_strategy = st.builds(
    cppmodel_CPPClassRefAssocCollection,
    cppContainer=
        safe_text
)
cppmodel_CPPFormalParameter_strategy = st.builds(
    cppmodel_CPPFormalParameter,
    passingMode=
        safe_text
)
cppmodel_CPPUserDefinedType_strategy = st.builds(
    cppmodel_CPPUserDefinedType,
)
cppmodel_CPPEnumerator_strategy = st.builds(
    cppmodel_CPPEnumerator,
    cppValue=
        safe_text
)
cppmodel_CPPTransition_strategy = st.builds(
    cppmodel_CPPTransition,
)
cppmodel_CPPClassRefSimpleCollection_strategy = st.builds(
    cppmodel_CPPClassRefSimpleCollection,
    cppContainer=
        safe_text
)
cppmodel_CPPClassReference_strategy = st.builds(
    cppmodel_CPPClassReference,
)
cppmodel_CPPSignal_strategy = st.builds(
    cppmodel_CPPSignal,
)
cppmodel_CPPReturnValue_strategy = st.builds(
    cppmodel_CPPReturnValue,
)
cppmodel_CPPEvent_strategy = st.builds(
    cppmodel_CPPEvent,
)
cppmodel_CPPComponent_strategy = st.builds(
    cppmodel_CPPComponent,
)
cppmodel_CPPProtocolOperationDefinition_strategy = st.builds(
    cppmodel_CPPProtocolOperationDefinition,
)
cppmodel_CPPState_strategy = st.builds(
    cppmodel_CPPState,
)
cppmodel_CPPOperation_strategy = st.builds(
    cppmodel_CPPOperation,
)
cppmodel_CPPExternalBridge_strategy = st.builds(
    cppmodel_CPPExternalBridge,
    cppExternalNamespace=
        safe_text
)
cppmodel_CPPPort_strategy = st.builds(
    cppmodel_CPPPort,
)
cppmodel_CPPEnumType_strategy = st.builds(
    cppmodel_CPPEnumType,
)
cppmodel_CPPStructType_strategy = st.builds(
    cppmodel_CPPStructType,
)
cppmodel_CPPStructMember_strategy = st.builds(
    cppmodel_CPPStructMember,
)
cppmodel_CPPModel_strategy = st.builds(
    cppmodel_CPPModel,
)
CPPNamedElement_strategy = st.builds(
    CPPNamedElement,
)
cppmodel_CPPQualifiedNamedElement_strategy = st.builds(
    cppmodel_CPPQualifiedNamedElement,
    cppQualifiedName=
        safe_text,
    cppPrefix=
        safe_text
)
cppmodel_OOPLNameProvider_strategy = st.builds(
    cppmodel_OOPLNameProvider,
)
cppmodel_CPPNamedElement_strategy = st.builds(
    cppmodel_CPPNamedElement,
    cppName=
        safe_text
)

@given(instance=cppmodel_XTClass_strategy)
@settings(max_examples=50)
def test_cppmodel_xtclass_instantiation(instance):
    assert isinstance(instance, cppmodel_XTClass)

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

@given(instance=cppmodel_CPPExternalLibrary_strategy)
@settings(max_examples=50)
def test_cppmodel_cppexternallibrary_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPExternalLibrary)

@given(instance=cppmodel_Parameter_strategy)
@settings(max_examples=50)
def test_cppmodel_parameter_instantiation(instance):
    assert isinstance(instance, cppmodel_Parameter)

@given(instance=cppmodel_XTEvent_strategy)
@settings(max_examples=50)
def test_cppmodel_xtevent_instantiation(instance):
    assert isinstance(instance, cppmodel_XTEvent)

@given(instance=cppmodel_Transition_strategy)
@settings(max_examples=50)
def test_cppmodel_transition_instantiation(instance):
    assert isinstance(instance, cppmodel_Transition)

@given(instance=cppmodel_TypedMultiplicityElement_strategy)
@settings(max_examples=50)
def test_cppmodel_typedmultiplicityelement_instantiation(instance):
    assert isinstance(instance, cppmodel_TypedMultiplicityElement)

@given(instance=cppmodel_State_strategy)
@settings(max_examples=50)
def test_cppmodel_state_instantiation(instance):
    assert isinstance(instance, cppmodel_State)

@given(instance=cppmodel_OOPLDataType_strategy)
@settings(max_examples=50)
def test_cppmodel_oopldatatype_instantiation(instance):
    assert isinstance(instance, cppmodel_OOPLDataType)

@given(instance=cppmodel_CPPSequence_strategy)
@settings(max_examples=50)
def test_cppmodel_cppsequence_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPSequence)



@given(instance=cppmodel_CPPSequence_strategy)
def test_cppmodel_cppsequence_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel_Attribute_strategy)
@settings(max_examples=50)
def test_cppmodel_attribute_instantiation(instance):
    assert isinstance(instance, cppmodel_Attribute)

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

@given(instance=cppmodel_XTProtocolOperationImplementation_strategy)
@settings(max_examples=50)
def test_cppmodel_xtprotocoloperationimplementation_instantiation(instance):
    assert isinstance(instance, cppmodel_XTProtocolOperationImplementation)

@given(instance=cppmodel_XTProtocolOperationDefinition_strategy)
@settings(max_examples=50)
def test_cppmodel_xtprotocoloperationdefinition_instantiation(instance):
    assert isinstance(instance, cppmodel_XTProtocolOperationDefinition)

@given(instance=cppmodel_XTPort_strategy)
@settings(max_examples=50)
def test_cppmodel_xtport_instantiation(instance):
    assert isinstance(instance, cppmodel_XTPort)

@given(instance=cppmodel_Snippet_strategy)
@settings(max_examples=50)
def test_cppmodel_snippet_instantiation(instance):
    assert isinstance(instance, cppmodel_Snippet)

@given(instance=cppmodel_Signal_strategy)
@settings(max_examples=50)
def test_cppmodel_signal_instantiation(instance):
    assert isinstance(instance, cppmodel_Signal)

@given(instance=cppmodel_Operation_strategy)
@settings(max_examples=50)
def test_cppmodel_operation_instantiation(instance):
    assert isinstance(instance, cppmodel_Operation)

@given(instance=OOPLRelation_strategy)
@settings(max_examples=50)
def test_ooplrelation_instantiation(instance):
    assert isinstance(instance, OOPLRelation)

@given(instance=cppmodel_CPPExternalHeader_strategy)
@settings(max_examples=50)
def test_cppmodel_cppexternalheader_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPExternalHeader)



@given(instance=cppmodel_CPPExternalHeader_strategy)
def test_cppmodel_cppexternalheader_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cppmodel_XTComponent_strategy)
@settings(max_examples=50)
def test_cppmodel_xtcomponent_instantiation(instance):
    assert isinstance(instance, cppmodel_XTComponent)

@given(instance=CPPSourceFile_strategy)
@settings(max_examples=50)
def test_cppsourcefile_instantiation(instance):
    assert isinstance(instance, CPPSourceFile)

@given(instance=cppmodel_CPPMakeFile_strategy)
@settings(max_examples=50)
def test_cppmodel_cppmakefile_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPMakeFile)

@given(instance=cppmodel_CPPExternalHeaderInclusion_strategy)
@settings(max_examples=50)
def test_cppmodel_cppexternalheaderinclusion_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPExternalHeaderInclusion)



@given(instance=cppmodel_CPPExternalHeaderInclusion_strategy)
def test_cppmodel_cppexternalheaderinclusion_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=cppmodel_CPPSourceFile_strategy)
@settings(max_examples=50)
def test_cppmodel_cppsourcefile_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPSourceFile)



@given(instance=cppmodel_CPPSourceFile_strategy)
def test_cppmodel_cppsourcefile_generationName_setter(instance):
    original = instance.generationName
    instance.generationName = original
    assert instance.generationName == original



@given(instance=cppmodel_CPPSourceFile_strategy)
def test_cppmodel_cppsourcefile_generationDirectory_setter(instance):
    original = instance.generationDirectory
    instance.generationDirectory = original
    assert instance.generationDirectory == original



@given(instance=cppmodel_CPPSourceFile_strategy)
def test_cppmodel_cppsourcefile_generationPath_setter(instance):
    original = instance.generationPath
    instance.generationPath = original
    assert instance.generationPath == original

@given(instance=cppmodel_XTProtocol_strategy)
@settings(max_examples=50)
def test_cppmodel_xtprotocol_instantiation(instance):
    assert isinstance(instance, cppmodel_XTProtocol)

@given(instance=OOPLClass_strategy)
@settings(max_examples=50)
def test_ooplclass_instantiation(instance):
    assert isinstance(instance, OOPLClass)

@given(instance=cppmodel_Package_strategy)
@settings(max_examples=50)
def test_cppmodel_package_instantiation(instance):
    assert isinstance(instance, cppmodel_Package)

@given(instance=cppmodel_CPPDirectory_strategy)
@settings(max_examples=50)
def test_cppmodel_cppdirectory_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPDirectory)



@given(instance=cppmodel_CPPDirectory_strategy)
def test_cppmodel_cppdirectory_parentDirectory_setter(instance):
    original = instance.parentDirectory
    instance.parentDirectory = original
    assert instance.parentDirectory == original



@given(instance=cppmodel_CPPDirectory_strategy)
def test_cppmodel_cppdirectory_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=cppmodel_CPPDirectory_strategy)
def test_cppmodel_cppdirectory_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cppmodel_CPPHeaderFile_strategy)
@settings(max_examples=50)
def test_cppmodel_cppheaderfile_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPHeaderFile)



@given(instance=cppmodel_CPPHeaderFile_strategy)
def test_cppmodel_cppheaderfile_includeDirectory_setter(instance):
    original = instance.includeDirectory
    instance.includeDirectory = original
    assert instance.includeDirectory == original



@given(instance=cppmodel_CPPHeaderFile_strategy)
def test_cppmodel_cppheaderfile_includeName_setter(instance):
    original = instance.includeName
    instance.includeName = original
    assert instance.includeName == original



@given(instance=cppmodel_CPPHeaderFile_strategy)
def test_cppmodel_cppheaderfile_includePath_setter(instance):
    original = instance.includePath
    instance.includePath = original
    assert instance.includePath == original

@given(instance=cppmodel_CPPBodyFile_strategy)
@settings(max_examples=50)
def test_cppmodel_cppbodyfile_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPBodyFile)

@given(instance=cppmodel_Model_strategy)
@settings(max_examples=50)
def test_cppmodel_model_instantiation(instance):
    assert isinstance(instance, cppmodel_Model)

@given(instance=CPPQualifiedNamedElement_strategy)
@settings(max_examples=50)
def test_cppqualifiednamedelement_instantiation(instance):
    assert isinstance(instance, CPPQualifiedNamedElement)

@given(instance=cppmodel_CPPRelation_strategy)
@settings(max_examples=50)
def test_cppmodel_cpprelation_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPRelation)

@given(instance=cppmodel_CPPClass_strategy)
@settings(max_examples=50)
def test_cppmodel_cppclass_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPClass)

@given(instance=cppmodel_CPPProtocol_strategy)
@settings(max_examples=50)
def test_cppmodel_cppprotocol_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPProtocol)

@given(instance=cppmodel_CPPBasicType_strategy)
@settings(max_examples=50)
def test_cppmodel_cppbasictype_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPBasicType)



@given(instance=cppmodel_CPPBasicType_strategy)
def test_cppmodel_cppbasictype_cppSpecifier_setter(instance):
    original = instance.cppSpecifier
    instance.cppSpecifier = original
    assert instance.cppSpecifier == original

@given(instance=cppmodel_CPPClassReferenceStorage_strategy)
@settings(max_examples=50)
def test_cppmodel_cppclassreferencestorage_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPClassReferenceStorage)

@given(instance=cppmodel_CPPProtocolOperationImplementation_strategy)
@settings(max_examples=50)
def test_cppmodel_cppprotocoloperationimplementation_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPProtocolOperationImplementation)

@given(instance=cppmodel_CPPPackage_strategy)
@settings(max_examples=50)
def test_cppmodel_cpppackage_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPPackage)

@given(instance=cppmodel_CPPAttribute_strategy)
@settings(max_examples=50)
def test_cppmodel_cppattribute_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPAttribute)

@given(instance=cppmodel_CPPClassRefAssocCollection_strategy)
@settings(max_examples=50)
def test_cppmodel_cppclassrefassoccollection_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPClassRefAssocCollection)



@given(instance=cppmodel_CPPClassRefAssocCollection_strategy)
def test_cppmodel_cppclassrefassoccollection_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel_CPPFormalParameter_strategy)
@settings(max_examples=50)
def test_cppmodel_cppformalparameter_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPFormalParameter)



@given(instance=cppmodel_CPPFormalParameter_strategy)
def test_cppmodel_cppformalparameter_passingMode_setter(instance):
    original = instance.passingMode
    instance.passingMode = original
    assert instance.passingMode == original

@given(instance=cppmodel_CPPUserDefinedType_strategy)
@settings(max_examples=50)
def test_cppmodel_cppuserdefinedtype_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPUserDefinedType)

@given(instance=cppmodel_CPPEnumerator_strategy)
@settings(max_examples=50)
def test_cppmodel_cppenumerator_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPEnumerator)



@given(instance=cppmodel_CPPEnumerator_strategy)
def test_cppmodel_cppenumerator_cppValue_setter(instance):
    original = instance.cppValue
    instance.cppValue = original
    assert instance.cppValue == original

@given(instance=cppmodel_CPPTransition_strategy)
@settings(max_examples=50)
def test_cppmodel_cpptransition_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPTransition)

@given(instance=cppmodel_CPPClassRefSimpleCollection_strategy)
@settings(max_examples=50)
def test_cppmodel_cppclassrefsimplecollection_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPClassRefSimpleCollection)



@given(instance=cppmodel_CPPClassRefSimpleCollection_strategy)
def test_cppmodel_cppclassrefsimplecollection_cppContainer_setter(instance):
    original = instance.cppContainer
    instance.cppContainer = original
    assert instance.cppContainer == original

@given(instance=cppmodel_CPPClassReference_strategy)
@settings(max_examples=50)
def test_cppmodel_cppclassreference_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPClassReference)

@given(instance=cppmodel_CPPSignal_strategy)
@settings(max_examples=50)
def test_cppmodel_cppsignal_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPSignal)

@given(instance=cppmodel_CPPReturnValue_strategy)
@settings(max_examples=50)
def test_cppmodel_cppreturnvalue_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPReturnValue)

@given(instance=cppmodel_CPPEvent_strategy)
@settings(max_examples=50)
def test_cppmodel_cppevent_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPEvent)

@given(instance=cppmodel_CPPComponent_strategy)
@settings(max_examples=50)
def test_cppmodel_cppcomponent_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPComponent)

@given(instance=cppmodel_CPPProtocolOperationDefinition_strategy)
@settings(max_examples=50)
def test_cppmodel_cppprotocoloperationdefinition_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPProtocolOperationDefinition)

@given(instance=cppmodel_CPPState_strategy)
@settings(max_examples=50)
def test_cppmodel_cppstate_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPState)

@given(instance=cppmodel_CPPOperation_strategy)
@settings(max_examples=50)
def test_cppmodel_cppoperation_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPOperation)

@given(instance=cppmodel_CPPExternalBridge_strategy)
@settings(max_examples=50)
def test_cppmodel_cppexternalbridge_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPExternalBridge)



@given(instance=cppmodel_CPPExternalBridge_strategy)
def test_cppmodel_cppexternalbridge_cppExternalNamespace_setter(instance):
    original = instance.cppExternalNamespace
    instance.cppExternalNamespace = original
    assert instance.cppExternalNamespace == original

@given(instance=cppmodel_CPPPort_strategy)
@settings(max_examples=50)
def test_cppmodel_cppport_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPPort)

@given(instance=cppmodel_CPPEnumType_strategy)
@settings(max_examples=50)
def test_cppmodel_cppenumtype_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPEnumType)

@given(instance=cppmodel_CPPStructType_strategy)
@settings(max_examples=50)
def test_cppmodel_cppstructtype_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPStructType)

@given(instance=cppmodel_CPPStructMember_strategy)
@settings(max_examples=50)
def test_cppmodel_cppstructmember_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPStructMember)

@given(instance=cppmodel_CPPModel_strategy)
@settings(max_examples=50)
def test_cppmodel_cppmodel_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPModel)

@given(instance=CPPNamedElement_strategy)
@settings(max_examples=50)
def test_cppnamedelement_instantiation(instance):
    assert isinstance(instance, CPPNamedElement)

@given(instance=cppmodel_CPPQualifiedNamedElement_strategy)
@settings(max_examples=50)
def test_cppmodel_cppqualifiednamedelement_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPQualifiedNamedElement)



@given(instance=cppmodel_CPPQualifiedNamedElement_strategy)
def test_cppmodel_cppqualifiednamedelement_cppQualifiedName_setter(instance):
    original = instance.cppQualifiedName
    instance.cppQualifiedName = original
    assert instance.cppQualifiedName == original



@given(instance=cppmodel_CPPQualifiedNamedElement_strategy)
def test_cppmodel_cppqualifiednamedelement_cppPrefix_setter(instance):
    original = instance.cppPrefix
    instance.cppPrefix = original
    assert instance.cppPrefix == original

@given(instance=cppmodel_OOPLNameProvider_strategy)
@settings(max_examples=50)
def test_cppmodel_ooplnameprovider_instantiation(instance):
    assert isinstance(instance, cppmodel_OOPLNameProvider)

@given(instance=cppmodel_CPPNamedElement_strategy)
@settings(max_examples=50)
def test_cppmodel_cppnamedelement_instantiation(instance):
    assert isinstance(instance, cppmodel_CPPNamedElement)



@given(instance=cppmodel_CPPNamedElement_strategy)
def test_cppmodel_cppnamedelement_cppName_setter(instance):
    original = instance.cppName
    instance.cppName = original
    assert instance.cppName == original
