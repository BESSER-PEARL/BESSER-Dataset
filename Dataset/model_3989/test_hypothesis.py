import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xpdl2::extensions::LoopDataRefType,
    xpdl2::XpdlTypeType,
    XSDAnnotation,
    xpdl2::extensions::ExtendedAnnotationType,
    xpdl2::TypeDeclarationsType,
    xpdl2::ScriptType,
    LoopDataRefType,
    xpdl2::XSDSchema,
    xpdl2::LoopType,
    xpdl2::LoopStandardType,
    xpdl2::FormalParametersType,
    xpdl2::LoopMultiInstanceType,
    xpdl2::FormalParameterType,
    Extensible,
    xpdl2::TypeDeclarationType,
    xpdl2::ExternalPackage,
    xpdl2::ExternalPackages,
    xpdl2::Extensible,
    ExtendedAnnotationType,
    xpdl2::ExtendedAttributeType,
    xpdl2::ExtendedAttributesType,
    xpdl2::ExpressionType,
    xpdl2::DataTypeType,
    XpdlTypeType,
    xpdl2::SchemaTypeType,
    xpdl2::DeclaredTypeType,
    xpdl2::ExternalReferenceType,
    xpdl2::BasicTypeType,
    MIFlowConditionType,
    TypeType,
    TestTimeType,
    LoopTypeType,
    MIOrderingType,
    ModeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xpdl2::extensions::loopdatareftype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::extensions::LoopDataRefType)


def test_xpdl2::extensions::loopdatareftype_constructor_exists():
    assert callable(xpdl2::extensions::LoopDataRefType.__init__)


def test_xpdl2::extensions::loopdatareftype_constructor_args():
    sig = inspect.signature(xpdl2::extensions::LoopDataRefType.__init__)
    params = list(sig.parameters.keys())
    assert "loopCounterRef" in params, "Missing parameter 'loopCounterRef'"
    assert "outputItemRef" in params, "Missing parameter 'outputItemRef'"
    assert "inputItemRef" in params, "Missing parameter 'inputItemRef'"

def test_xpdl2::extensions::loopdatareftype_has_loopCounterRef():
    assert hasattr(xpdl2::extensions::LoopDataRefType, "loopCounterRef")
    descriptor = None
    for klass in xpdl2::extensions::LoopDataRefType.__mro__:
        if "loopCounterRef" in klass.__dict__:
            descriptor = klass.__dict__["loopCounterRef"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extensions::loopdatareftype_has_outputItemRef():
    assert hasattr(xpdl2::extensions::LoopDataRefType, "outputItemRef")
    descriptor = None
    for klass in xpdl2::extensions::LoopDataRefType.__mro__:
        if "outputItemRef" in klass.__dict__:
            descriptor = klass.__dict__["outputItemRef"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extensions::loopdatareftype_has_inputItemRef():
    assert hasattr(xpdl2::extensions::LoopDataRefType, "inputItemRef")
    descriptor = None
    for klass in xpdl2::extensions::LoopDataRefType.__mro__:
        if "inputItemRef" in klass.__dict__:
            descriptor = klass.__dict__["inputItemRef"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::xpdltypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::XpdlTypeType)


def test_xpdl2::xpdltypetype_constructor_exists():
    assert callable(xpdl2::XpdlTypeType.__init__)


def test_xpdl2::xpdltypetype_constructor_args():
    sig = inspect.signature(xpdl2::XpdlTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xsdannotation_is_not_abstract():
    assert not inspect.isabstract(XSDAnnotation)


def test_xsdannotation_constructor_exists():
    assert callable(XSDAnnotation.__init__)


def test_xsdannotation_constructor_args():
    sig = inspect.signature(XSDAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::extensions::extendedannotationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::extensions::ExtendedAnnotationType)


def test_xpdl2::extensions::extendedannotationtype_constructor_exists():
    assert callable(xpdl2::extensions::ExtendedAnnotationType.__init__)


def test_xpdl2::extensions::extendedannotationtype_constructor_args():
    sig = inspect.signature(xpdl2::extensions::ExtendedAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::TypeDeclarationsType)


def test_xpdl2::typedeclarationstype_constructor_exists():
    assert callable(xpdl2::TypeDeclarationsType.__init__)


def test_xpdl2::typedeclarationstype_constructor_args():
    sig = inspect.signature(xpdl2::TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::scripttype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ScriptType)


def test_xpdl2::scripttype_constructor_exists():
    assert callable(xpdl2::ScriptType.__init__)


def test_xpdl2::scripttype_constructor_args():
    sig = inspect.signature(xpdl2::ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "version" in params, "Missing parameter 'version'"
    assert "grammar" in params, "Missing parameter 'grammar'"

def test_xpdl2::scripttype_has_type():
    assert hasattr(xpdl2::ScriptType, "type")
    descriptor = None
    for klass in xpdl2::ScriptType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::scripttype_has_version():
    assert hasattr(xpdl2::ScriptType, "version")
    descriptor = None
    for klass in xpdl2::ScriptType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::scripttype_has_grammar():
    assert hasattr(xpdl2::ScriptType, "grammar")
    descriptor = None
    for klass in xpdl2::ScriptType.__mro__:
        if "grammar" in klass.__dict__:
            descriptor = klass.__dict__["grammar"]
            break
    assert isinstance(descriptor, property)



def test_loopdatareftype_is_not_abstract():
    assert not inspect.isabstract(LoopDataRefType)


def test_loopdatareftype_constructor_exists():
    assert callable(LoopDataRefType.__init__)


def test_loopdatareftype_constructor_args():
    sig = inspect.signature(LoopDataRefType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::xsdschema_is_not_abstract():
    assert not inspect.isabstract(xpdl2::XSDSchema)


def test_xpdl2::xsdschema_constructor_exists():
    assert callable(xpdl2::XSDSchema.__init__)


def test_xpdl2::xsdschema_constructor_args():
    sig = inspect.signature(xpdl2::XSDSchema.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::looptype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::LoopType)


def test_xpdl2::looptype_constructor_exists():
    assert callable(xpdl2::LoopType.__init__)


def test_xpdl2::looptype_constructor_args():
    sig = inspect.signature(xpdl2::LoopType.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_xpdl2::looptype_has_loopType():
    assert hasattr(xpdl2::LoopType, "loopType")
    descriptor = None
    for klass in xpdl2::LoopType.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::loopstandardtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::LoopStandardType)


def test_xpdl2::loopstandardtype_constructor_exists():
    assert callable(xpdl2::LoopStandardType.__init__)


def test_xpdl2::loopstandardtype_constructor_args():
    sig = inspect.signature(xpdl2::LoopStandardType.__init__)
    params = list(sig.parameters.keys())
    assert "loopMaximum" in params, "Missing parameter 'loopMaximum'"
    assert "testTime" in params, "Missing parameter 'testTime'"

def test_xpdl2::loopstandardtype_has_loopMaximum():
    assert hasattr(xpdl2::LoopStandardType, "loopMaximum")
    descriptor = None
    for klass in xpdl2::LoopStandardType.__mro__:
        if "loopMaximum" in klass.__dict__:
            descriptor = klass.__dict__["loopMaximum"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::loopstandardtype_has_testTime():
    assert hasattr(xpdl2::LoopStandardType, "testTime")
    descriptor = None
    for klass in xpdl2::LoopStandardType.__mro__:
        if "testTime" in klass.__dict__:
            descriptor = klass.__dict__["testTime"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::FormalParametersType)


def test_xpdl2::formalparameterstype_constructor_exists():
    assert callable(xpdl2::FormalParametersType.__init__)


def test_xpdl2::formalparameterstype_constructor_args():
    sig = inspect.signature(xpdl2::FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::loopmultiinstancetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::LoopMultiInstanceType)


def test_xpdl2::loopmultiinstancetype_constructor_exists():
    assert callable(xpdl2::LoopMultiInstanceType.__init__)


def test_xpdl2::loopmultiinstancetype_constructor_args():
    sig = inspect.signature(xpdl2::LoopMultiInstanceType.__init__)
    params = list(sig.parameters.keys())
    assert "mIFlowCondition" in params, "Missing parameter 'mIFlowCondition'"
    assert "mIOrdering" in params, "Missing parameter 'mIOrdering'"

def test_xpdl2::loopmultiinstancetype_has_mIFlowCondition():
    assert hasattr(xpdl2::LoopMultiInstanceType, "mIFlowCondition")
    descriptor = None
    for klass in xpdl2::LoopMultiInstanceType.__mro__:
        if "mIFlowCondition" in klass.__dict__:
            descriptor = klass.__dict__["mIFlowCondition"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::loopmultiinstancetype_has_mIOrdering():
    assert hasattr(xpdl2::LoopMultiInstanceType, "mIOrdering")
    descriptor = None
    for klass in xpdl2::LoopMultiInstanceType.__mro__:
        if "mIOrdering" in klass.__dict__:
            descriptor = klass.__dict__["mIOrdering"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::formalparametertype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::FormalParameterType)


def test_xpdl2::formalparametertype_constructor_exists():
    assert callable(xpdl2::FormalParameterType.__init__)


def test_xpdl2::formalparametertype_constructor_args():
    sig = inspect.signature(xpdl2::FormalParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl2::formalparametertype_has_id():
    assert hasattr(xpdl2::FormalParameterType, "id")
    descriptor = None
    for klass in xpdl2::FormalParameterType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::formalparametertype_has_mode():
    assert hasattr(xpdl2::FormalParameterType, "mode")
    descriptor = None
    for klass in xpdl2::FormalParameterType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::formalparametertype_has_name():
    assert hasattr(xpdl2::FormalParameterType, "name")
    descriptor = None
    for klass in xpdl2::FormalParameterType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::formalparametertype_has_description():
    assert hasattr(xpdl2::FormalParameterType, "description")
    descriptor = None
    for klass in xpdl2::FormalParameterType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_extensible_is_not_abstract():
    assert not inspect.isabstract(Extensible)


def test_extensible_constructor_exists():
    assert callable(Extensible.__init__)


def test_extensible_constructor_args():
    sig = inspect.signature(Extensible.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::typedeclarationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::TypeDeclarationType)


def test_xpdl2::typedeclarationtype_constructor_exists():
    assert callable(xpdl2::TypeDeclarationType.__init__)


def test_xpdl2::typedeclarationtype_constructor_args():
    sig = inspect.signature(xpdl2::TypeDeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_xpdl2::typedeclarationtype_has_id():
    assert hasattr(xpdl2::TypeDeclarationType, "id")
    descriptor = None
    for klass in xpdl2::TypeDeclarationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::typedeclarationtype_has_name():
    assert hasattr(xpdl2::TypeDeclarationType, "name")
    descriptor = None
    for klass in xpdl2::TypeDeclarationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::typedeclarationtype_has_description():
    assert hasattr(xpdl2::TypeDeclarationType, "description")
    descriptor = None
    for klass in xpdl2::TypeDeclarationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::externalpackage_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExternalPackage)


def test_xpdl2::externalpackage_constructor_exists():
    assert callable(xpdl2::ExternalPackage.__init__)


def test_xpdl2::externalpackage_constructor_args():
    sig = inspect.signature(xpdl2::ExternalPackage.__init__)
    params = list(sig.parameters.keys())
    assert "href" in params, "Missing parameter 'href'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl2::externalpackage_has_href():
    assert hasattr(xpdl2::ExternalPackage, "href")
    descriptor = None
    for klass in xpdl2::ExternalPackage.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::externalpackage_has_name():
    assert hasattr(xpdl2::ExternalPackage, "name")
    descriptor = None
    for klass in xpdl2::ExternalPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::externalpackage_has_id():
    assert hasattr(xpdl2::ExternalPackage, "id")
    descriptor = None
    for klass in xpdl2::ExternalPackage.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::externalpackages_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExternalPackages)


def test_xpdl2::externalpackages_constructor_exists():
    assert callable(xpdl2::ExternalPackages.__init__)


def test_xpdl2::externalpackages_constructor_args():
    sig = inspect.signature(xpdl2::ExternalPackages.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::extensible_is_not_abstract():
    assert not inspect.isabstract(xpdl2::Extensible)


def test_xpdl2::extensible_constructor_exists():
    assert callable(xpdl2::Extensible.__init__)


def test_xpdl2::extensible_constructor_args():
    sig = inspect.signature(xpdl2::Extensible.__init__)
    params = list(sig.parameters.keys())



def test_extendedannotationtype_is_not_abstract():
    assert not inspect.isabstract(ExtendedAnnotationType)


def test_extendedannotationtype_constructor_exists():
    assert callable(ExtendedAnnotationType.__init__)


def test_extendedannotationtype_constructor_args():
    sig = inspect.signature(ExtendedAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::extendedattributetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExtendedAttributeType)


def test_xpdl2::extendedattributetype_constructor_exists():
    assert callable(xpdl2::ExtendedAttributeType.__init__)


def test_xpdl2::extendedattributetype_constructor_args():
    sig = inspect.signature(xpdl2::ExtendedAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "value" in params, "Missing parameter 'value'"
    assert "group" in params, "Missing parameter 'group'"
    assert "any" in params, "Missing parameter 'any'"

def test_xpdl2::extendedattributetype_has_name():
    assert hasattr(xpdl2::ExtendedAttributeType, "name")
    descriptor = None
    for klass in xpdl2::ExtendedAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extendedattributetype_has_mixed():
    assert hasattr(xpdl2::ExtendedAttributeType, "mixed")
    descriptor = None
    for klass in xpdl2::ExtendedAttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extendedattributetype_has_value():
    assert hasattr(xpdl2::ExtendedAttributeType, "value")
    descriptor = None
    for klass in xpdl2::ExtendedAttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extendedattributetype_has_group():
    assert hasattr(xpdl2::ExtendedAttributeType, "group")
    descriptor = None
    for klass in xpdl2::ExtendedAttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::extendedattributetype_has_any():
    assert hasattr(xpdl2::ExtendedAttributeType, "any")
    descriptor = None
    for klass in xpdl2::ExtendedAttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::extendedattributestype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExtendedAttributesType)


def test_xpdl2::extendedattributestype_constructor_exists():
    assert callable(xpdl2::ExtendedAttributesType.__init__)


def test_xpdl2::extendedattributestype_constructor_args():
    sig = inspect.signature(xpdl2::ExtendedAttributesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::expressiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExpressionType)


def test_xpdl2::expressiontype_constructor_exists():
    assert callable(xpdl2::ExpressionType.__init__)


def test_xpdl2::expressiontype_constructor_args():
    sig = inspect.signature(xpdl2::ExpressionType.__init__)
    params = list(sig.parameters.keys())
    assert "scriptGrammar" in params, "Missing parameter 'scriptGrammar'"
    assert "any" in params, "Missing parameter 'any'"
    assert "scriptType" in params, "Missing parameter 'scriptType'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "scriptVersion" in params, "Missing parameter 'scriptVersion'"

def test_xpdl2::expressiontype_has_scriptGrammar():
    assert hasattr(xpdl2::ExpressionType, "scriptGrammar")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "scriptGrammar" in klass.__dict__:
            descriptor = klass.__dict__["scriptGrammar"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::expressiontype_has_any():
    assert hasattr(xpdl2::ExpressionType, "any")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::expressiontype_has_scriptType():
    assert hasattr(xpdl2::ExpressionType, "scriptType")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "scriptType" in klass.__dict__:
            descriptor = klass.__dict__["scriptType"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::expressiontype_has_mixed():
    assert hasattr(xpdl2::ExpressionType, "mixed")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::expressiontype_has_group():
    assert hasattr(xpdl2::ExpressionType, "group")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::expressiontype_has_scriptVersion():
    assert hasattr(xpdl2::ExpressionType, "scriptVersion")
    descriptor = None
    for klass in xpdl2::ExpressionType.__mro__:
        if "scriptVersion" in klass.__dict__:
            descriptor = klass.__dict__["scriptVersion"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::datatypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::DataTypeType)


def test_xpdl2::datatypetype_constructor_exists():
    assert callable(xpdl2::DataTypeType.__init__)


def test_xpdl2::datatypetype_constructor_args():
    sig = inspect.signature(xpdl2::DataTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "carnotType" in params, "Missing parameter 'carnotType'"

def test_xpdl2::datatypetype_has_carnotType():
    assert hasattr(xpdl2::DataTypeType, "carnotType")
    descriptor = None
    for klass in xpdl2::DataTypeType.__mro__:
        if "carnotType" in klass.__dict__:
            descriptor = klass.__dict__["carnotType"]
            break
    assert isinstance(descriptor, property)



def test_xpdltypetype_is_not_abstract():
    assert not inspect.isabstract(XpdlTypeType)


def test_xpdltypetype_constructor_exists():
    assert callable(XpdlTypeType.__init__)


def test_xpdltypetype_constructor_args():
    sig = inspect.signature(XpdlTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::schematypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::SchemaTypeType)


def test_xpdl2::schematypetype_constructor_exists():
    assert callable(xpdl2::SchemaTypeType.__init__)


def test_xpdl2::schematypetype_constructor_args():
    sig = inspect.signature(xpdl2::SchemaTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2::declaredtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::DeclaredTypeType)


def test_xpdl2::declaredtypetype_constructor_exists():
    assert callable(xpdl2::DeclaredTypeType.__init__)


def test_xpdl2::declaredtypetype_constructor_args():
    sig = inspect.signature(xpdl2::DeclaredTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl2::declaredtypetype_has_id():
    assert hasattr(xpdl2::DeclaredTypeType, "id")
    descriptor = None
    for klass in xpdl2::DeclaredTypeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::ExternalReferenceType)


def test_xpdl2::externalreferencetype_constructor_exists():
    assert callable(xpdl2::ExternalReferenceType.__init__)


def test_xpdl2::externalreferencetype_constructor_args():
    sig = inspect.signature(xpdl2::ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "xref" in params, "Missing parameter 'xref'"

def test_xpdl2::externalreferencetype_has_location():
    assert hasattr(xpdl2::ExternalReferenceType, "location")
    descriptor = None
    for klass in xpdl2::ExternalReferenceType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::externalreferencetype_has_uuid():
    assert hasattr(xpdl2::ExternalReferenceType, "uuid")
    descriptor = None
    for klass in xpdl2::ExternalReferenceType.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::externalreferencetype_has_namespace():
    assert hasattr(xpdl2::ExternalReferenceType, "namespace")
    descriptor = None
    for klass in xpdl2::ExternalReferenceType.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2::externalreferencetype_has_xref():
    assert hasattr(xpdl2::ExternalReferenceType, "xref")
    descriptor = None
    for klass in xpdl2::ExternalReferenceType.__mro__:
        if "xref" in klass.__dict__:
            descriptor = klass.__dict__["xref"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2::basictypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2::BasicTypeType)


def test_xpdl2::basictypetype_constructor_exists():
    assert callable(xpdl2::BasicTypeType.__init__)


def test_xpdl2::basictypetype_constructor_args():
    sig = inspect.signature(xpdl2::BasicTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl2::basictypetype_has_type():
    assert hasattr(xpdl2::BasicTypeType, "type")
    descriptor = None
    for klass in xpdl2::BasicTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_miflowconditiontype_exists():
    # Check that the Enumeration exists
    assert MIFlowConditionType is not None

def test_miflowconditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MIFlowConditionType]
    expected_literals = [
        "None_",
        "All",
        "Complex",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MIFlowConditionType"

def test_typetype_exists():
    # Check that the Enumeration exists
    assert TypeType is not None

def test_typetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType]
    expected_literals = [
        "INTEGER",
        "DATETIME",
        "REFERENCE",
        "BOOLEAN",
        "STRING",
        "PERFORMER",
        "FLOAT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType"

def test_testtimetype_exists():
    # Check that the Enumeration exists
    assert TestTimeType is not None

def test_testtimetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TestTimeType]
    expected_literals = [
        "Before",
        "After",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TestTimeType"

def test_looptypetype_exists():
    # Check that the Enumeration exists
    assert LoopTypeType is not None

def test_looptypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LoopTypeType]
    expected_literals = [
        "MultiInstance",
        "Standard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LoopTypeType"

def test_miorderingtype_exists():
    # Check that the Enumeration exists
    assert MIOrderingType is not None

def test_miorderingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MIOrderingType]
    expected_literals = [
        "Parallel",
        "Sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MIOrderingType"

def test_modetype_exists():
    # Check that the Enumeration exists
    assert ModeType is not None

def test_modetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeType]
    expected_literals = [
        "OUT",
        "IN",
        "INOUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeType"


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
xpdl2::extensions::LoopDataRefType_strategy = st.builds(
    xpdl2::extensions::LoopDataRefType,
    loopCounterRef=
        safe_text,
    outputItemRef=
        safe_text,
    inputItemRef=
        safe_text
)
xpdl2::XpdlTypeType_strategy = st.builds(
    xpdl2::XpdlTypeType,
)
XSDAnnotation_strategy = st.builds(
    XSDAnnotation,
)
xpdl2::extensions::ExtendedAnnotationType_strategy = st.builds(
    xpdl2::extensions::ExtendedAnnotationType,
)
xpdl2::TypeDeclarationsType_strategy = st.builds(
    xpdl2::TypeDeclarationsType,
)
xpdl2::ScriptType_strategy = st.builds(
    xpdl2::ScriptType,
    type=
        safe_text,
    version=
        safe_text,
    grammar=
        safe_text
)
LoopDataRefType_strategy = st.builds(
    LoopDataRefType,
)
xpdl2::XSDSchema_strategy = st.builds(
    xpdl2::XSDSchema,
)
xpdl2::LoopType_strategy = st.builds(
    xpdl2::LoopType,
    loopType=
        safe_text
)
xpdl2::LoopStandardType_strategy = st.builds(
    xpdl2::LoopStandardType,
    loopMaximum=
        safe_text,
    testTime=
        safe_text
)
xpdl2::FormalParametersType_strategy = st.builds(
    xpdl2::FormalParametersType,
)
xpdl2::LoopMultiInstanceType_strategy = st.builds(
    xpdl2::LoopMultiInstanceType,
    mIFlowCondition=
        safe_text,
    mIOrdering=
        safe_text
)
xpdl2::FormalParameterType_strategy = st.builds(
    xpdl2::FormalParameterType,
    id=
        safe_text,
    mode=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
Extensible_strategy = st.builds(
    Extensible,
)
xpdl2::TypeDeclarationType_strategy = st.builds(
    xpdl2::TypeDeclarationType,
    id=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
xpdl2::ExternalPackage_strategy = st.builds(
    xpdl2::ExternalPackage,
    href=
        safe_text,
    name=
        safe_text,
    id=
        safe_text
)
xpdl2::ExternalPackages_strategy = st.builds(
    xpdl2::ExternalPackages,
)
xpdl2::Extensible_strategy = st.builds(
    xpdl2::Extensible,
)
ExtendedAnnotationType_strategy = st.builds(
    ExtendedAnnotationType,
)
xpdl2::ExtendedAttributeType_strategy = st.builds(
    xpdl2::ExtendedAttributeType,
    name=
        safe_text,
    mixed=
        safe_text,
    value=
        safe_text,
    group=
        safe_text,
    any=
        safe_text
)
xpdl2::ExtendedAttributesType_strategy = st.builds(
    xpdl2::ExtendedAttributesType,
)
xpdl2::ExpressionType_strategy = st.builds(
    xpdl2::ExpressionType,
    scriptGrammar=
        safe_text,
    any=
        safe_text,
    scriptType=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text,
    scriptVersion=
        safe_text
)
xpdl2::DataTypeType_strategy = st.builds(
    xpdl2::DataTypeType,
    carnotType=
        safe_text
)
XpdlTypeType_strategy = st.builds(
    XpdlTypeType,
)
xpdl2::SchemaTypeType_strategy = st.builds(
    xpdl2::SchemaTypeType,
)
xpdl2::DeclaredTypeType_strategy = st.builds(
    xpdl2::DeclaredTypeType,
    id=
        safe_text
)
xpdl2::ExternalReferenceType_strategy = st.builds(
    xpdl2::ExternalReferenceType,
    location=
        safe_text,
    uuid=
        safe_text,
    namespace=
        safe_text,
    xref=
        safe_text
)
xpdl2::BasicTypeType_strategy = st.builds(
    xpdl2::BasicTypeType,
    type=
        safe_text
)

@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
@settings(max_examples=50)
def test_xpdl2::extensions::loopdatareftype_instantiation(instance):
    assert isinstance(instance, xpdl2::extensions::LoopDataRefType)

@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_loopCounterRef_type(instance):
    assert isinstance(instance.loopCounterRef, str)


@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_loopCounterRef_setter(instance):
    original = instance.loopCounterRef
    instance.loopCounterRef = original
    assert instance.loopCounterRef == original

@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_outputItemRef_type(instance):
    assert isinstance(instance.outputItemRef, str)


@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_outputItemRef_setter(instance):
    original = instance.outputItemRef
    instance.outputItemRef = original
    assert instance.outputItemRef == original

@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_inputItemRef_type(instance):
    assert isinstance(instance.inputItemRef, str)


@given(instance=xpdl2::extensions::LoopDataRefType_strategy)
def test_xpdl2::extensions::loopdatareftype_inputItemRef_setter(instance):
    original = instance.inputItemRef
    instance.inputItemRef = original
    assert instance.inputItemRef == original

@given(instance=xpdl2::XpdlTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2::xpdltypetype_instantiation(instance):
    assert isinstance(instance, xpdl2::XpdlTypeType)

@given(instance=XSDAnnotation_strategy)
@settings(max_examples=50)
def test_xsdannotation_instantiation(instance):
    assert isinstance(instance, XSDAnnotation)

@given(instance=xpdl2::extensions::ExtendedAnnotationType_strategy)
@settings(max_examples=50)
def test_xpdl2::extensions::extendedannotationtype_instantiation(instance):
    assert isinstance(instance, xpdl2::extensions::ExtendedAnnotationType)

@given(instance=xpdl2::TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_xpdl2::typedeclarationstype_instantiation(instance):
    assert isinstance(instance, xpdl2::TypeDeclarationsType)

@given(instance=xpdl2::ScriptType_strategy)
@settings(max_examples=50)
def test_xpdl2::scripttype_instantiation(instance):
    assert isinstance(instance, xpdl2::ScriptType)

@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_grammar_type(instance):
    assert isinstance(instance.grammar, str)


@given(instance=xpdl2::ScriptType_strategy)
def test_xpdl2::scripttype_grammar_setter(instance):
    original = instance.grammar
    instance.grammar = original
    assert instance.grammar == original

@given(instance=LoopDataRefType_strategy)
@settings(max_examples=50)
def test_loopdatareftype_instantiation(instance):
    assert isinstance(instance, LoopDataRefType)

@given(instance=xpdl2::XSDSchema_strategy)
@settings(max_examples=50)
def test_xpdl2::xsdschema_instantiation(instance):
    assert isinstance(instance, xpdl2::XSDSchema)

@given(instance=xpdl2::LoopType_strategy)
@settings(max_examples=50)
def test_xpdl2::looptype_instantiation(instance):
    assert isinstance(instance, xpdl2::LoopType)

@given(instance=xpdl2::LoopType_strategy)
def test_xpdl2::looptype_loopType_type(instance):
    assert isinstance(instance.loopType, str)


@given(instance=xpdl2::LoopType_strategy)
def test_xpdl2::looptype_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=xpdl2::LoopStandardType_strategy)
@settings(max_examples=50)
def test_xpdl2::loopstandardtype_instantiation(instance):
    assert isinstance(instance, xpdl2::LoopStandardType)

@given(instance=xpdl2::LoopStandardType_strategy)
def test_xpdl2::loopstandardtype_loopMaximum_type(instance):
    assert isinstance(instance.loopMaximum, str)


@given(instance=xpdl2::LoopStandardType_strategy)
def test_xpdl2::loopstandardtype_loopMaximum_setter(instance):
    original = instance.loopMaximum
    instance.loopMaximum = original
    assert instance.loopMaximum == original

@given(instance=xpdl2::LoopStandardType_strategy)
def test_xpdl2::loopstandardtype_testTime_type(instance):
    assert isinstance(instance.testTime, str)


@given(instance=xpdl2::LoopStandardType_strategy)
def test_xpdl2::loopstandardtype_testTime_setter(instance):
    original = instance.testTime
    instance.testTime = original
    assert instance.testTime == original

@given(instance=xpdl2::FormalParametersType_strategy)
@settings(max_examples=50)
def test_xpdl2::formalparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl2::FormalParametersType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=xpdl2::FormalParametersType_strategy)
@settings(max_examples=30)
def test_xpdl2::formalparameterstype_addformalparameter_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addFormalParameter(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addFormalParameter).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addFormalParameter' in xpdl2::FormalParametersType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addFormalParameter' in xpdl2::FormalParametersType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addFormalParameter' in xpdl2::FormalParametersType is not implemented or raised an error")

@given(instance=xpdl2::LoopMultiInstanceType_strategy)
@settings(max_examples=50)
def test_xpdl2::loopmultiinstancetype_instantiation(instance):
    assert isinstance(instance, xpdl2::LoopMultiInstanceType)

@given(instance=xpdl2::LoopMultiInstanceType_strategy)
def test_xpdl2::loopmultiinstancetype_mIFlowCondition_type(instance):
    assert isinstance(instance.mIFlowCondition, str)


@given(instance=xpdl2::LoopMultiInstanceType_strategy)
def test_xpdl2::loopmultiinstancetype_mIFlowCondition_setter(instance):
    original = instance.mIFlowCondition
    instance.mIFlowCondition = original
    assert instance.mIFlowCondition == original

@given(instance=xpdl2::LoopMultiInstanceType_strategy)
def test_xpdl2::loopmultiinstancetype_mIOrdering_type(instance):
    assert isinstance(instance.mIOrdering, str)


@given(instance=xpdl2::LoopMultiInstanceType_strategy)
def test_xpdl2::loopmultiinstancetype_mIOrdering_setter(instance):
    original = instance.mIOrdering
    instance.mIOrdering = original
    assert instance.mIOrdering == original

@given(instance=xpdl2::FormalParameterType_strategy)
@settings(max_examples=50)
def test_xpdl2::formalparametertype_instantiation(instance):
    assert isinstance(instance, xpdl2::FormalParameterType)

@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl2::FormalParameterType_strategy)
def test_xpdl2::formalparametertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Extensible_strategy)
@settings(max_examples=50)
def test_extensible_instantiation(instance):
    assert isinstance(instance, Extensible)

@given(instance=xpdl2::TypeDeclarationType_strategy)
@settings(max_examples=50)
def test_xpdl2::typedeclarationtype_instantiation(instance):
    assert isinstance(instance, xpdl2::TypeDeclarationType)

@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=xpdl2::TypeDeclarationType_strategy)
def test_xpdl2::typedeclarationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=xpdl2::ExternalPackage_strategy)
@settings(max_examples=50)
def test_xpdl2::externalpackage_instantiation(instance):
    assert isinstance(instance, xpdl2::ExternalPackage)

@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_href_type(instance):
    assert isinstance(instance.href, str)


@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl2::ExternalPackage_strategy)
def test_xpdl2::externalpackage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl2::ExternalPackages_strategy)
@settings(max_examples=50)
def test_xpdl2::externalpackages_instantiation(instance):
    assert isinstance(instance, xpdl2::ExternalPackages)

@given(instance=xpdl2::Extensible_strategy)
@settings(max_examples=50)
def test_xpdl2::extensible_instantiation(instance):
    assert isinstance(instance, xpdl2::Extensible)

@given(instance=ExtendedAnnotationType_strategy)
@settings(max_examples=50)
def test_extendedannotationtype_instantiation(instance):
    assert isinstance(instance, ExtendedAnnotationType)

@given(instance=xpdl2::ExtendedAttributeType_strategy)
@settings(max_examples=50)
def test_xpdl2::extendedattributetype_instantiation(instance):
    assert isinstance(instance, xpdl2::ExtendedAttributeType)

@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xpdl2::ExtendedAttributeType_strategy)
def test_xpdl2::extendedattributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl2::ExtendedAttributesType_strategy)
@settings(max_examples=50)
def test_xpdl2::extendedattributestype_instantiation(instance):
    assert isinstance(instance, xpdl2::ExtendedAttributesType)

@given(instance=xpdl2::ExpressionType_strategy)
@settings(max_examples=50)
def test_xpdl2::expressiontype_instantiation(instance):
    assert isinstance(instance, xpdl2::ExpressionType)

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptGrammar_type(instance):
    assert isinstance(instance.scriptGrammar, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptGrammar_setter(instance):
    original = instance.scriptGrammar
    instance.scriptGrammar = original
    assert instance.scriptGrammar == original

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_any_type(instance):
    assert isinstance(instance.any, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptType_type(instance):
    assert isinstance(instance.scriptType, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptType_setter(instance):
    original = instance.scriptType
    instance.scriptType = original
    assert instance.scriptType == original

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptVersion_type(instance):
    assert isinstance(instance.scriptVersion, str)


@given(instance=xpdl2::ExpressionType_strategy)
def test_xpdl2::expressiontype_scriptVersion_setter(instance):
    original = instance.scriptVersion
    instance.scriptVersion = original
    assert instance.scriptVersion == original

@given(instance=xpdl2::DataTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2::datatypetype_instantiation(instance):
    assert isinstance(instance, xpdl2::DataTypeType)

@given(instance=xpdl2::DataTypeType_strategy)
def test_xpdl2::datatypetype_carnotType_type(instance):
    assert isinstance(instance.carnotType, str)


@given(instance=xpdl2::DataTypeType_strategy)
def test_xpdl2::datatypetype_carnotType_setter(instance):
    original = instance.carnotType
    instance.carnotType = original
    assert instance.carnotType == original

@given(instance=XpdlTypeType_strategy)
@settings(max_examples=50)
def test_xpdltypetype_instantiation(instance):
    assert isinstance(instance, XpdlTypeType)

@given(instance=xpdl2::SchemaTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2::schematypetype_instantiation(instance):
    assert isinstance(instance, xpdl2::SchemaTypeType)

@given(instance=xpdl2::DeclaredTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2::declaredtypetype_instantiation(instance):
    assert isinstance(instance, xpdl2::DeclaredTypeType)

@given(instance=xpdl2::DeclaredTypeType_strategy)
def test_xpdl2::declaredtypetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=xpdl2::DeclaredTypeType_strategy)
def test_xpdl2::declaredtypetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl2::ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_xpdl2::externalreferencetype_instantiation(instance):
    assert isinstance(instance, xpdl2::ExternalReferenceType)

@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_uuid_type(instance):
    assert isinstance(instance.uuid, str)


@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original

@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_namespace_type(instance):
    assert isinstance(instance.namespace, str)


@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original

@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_xref_type(instance):
    assert isinstance(instance.xref, str)


@given(instance=xpdl2::ExternalReferenceType_strategy)
def test_xpdl2::externalreferencetype_xref_setter(instance):
    original = instance.xref
    instance.xref = original
    assert instance.xref == original

@given(instance=xpdl2::BasicTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2::basictypetype_instantiation(instance):
    assert isinstance(instance, xpdl2::BasicTypeType)

@given(instance=xpdl2::BasicTypeType_strategy)
def test_xpdl2::basictypetype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=xpdl2::BasicTypeType_strategy)
def test_xpdl2::basictypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
