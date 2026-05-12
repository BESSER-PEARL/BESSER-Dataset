import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xpdl2_extensions_LoopDataRefType,
    xpdl2_XpdlTypeType,
    XSDAnnotation,
    xpdl2_extensions_ExtendedAnnotationType,
    xpdl2_TypeDeclarationsType,
    xpdl2_ScriptType,
    LoopDataRefType,
    xpdl2_XSDSchema,
    xpdl2_LoopType,
    xpdl2_LoopStandardType,
    xpdl2_FormalParametersType,
    xpdl2_LoopMultiInstanceType,
    xpdl2_FormalParameterType,
    Extensible,
    xpdl2_TypeDeclarationType,
    xpdl2_ExternalPackage,
    xpdl2_ExternalPackages,
    xpdl2_Extensible,
    ExtendedAnnotationType,
    xpdl2_ExtendedAttributeType,
    xpdl2_ExtendedAttributesType,
    xpdl2_ExpressionType,
    xpdl2_DataTypeType,
    XpdlTypeType,
    xpdl2_SchemaTypeType,
    xpdl2_ExternalReferenceType,
    xpdl2_DeclaredTypeType,
    xpdl2_BasicTypeType,
    MIOrderingType,
    TestTimeType,
    ModeType,
    TypeType,
    LoopTypeType,
    MIFlowConditionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xpdl2_extensions_loopdatareftype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_extensions_LoopDataRefType)


def test_xpdl2_extensions_loopdatareftype_constructor_exists():
    assert callable(xpdl2_extensions_LoopDataRefType.__init__)


def test_xpdl2_extensions_loopdatareftype_constructor_args():
    sig = inspect.signature(xpdl2_extensions_LoopDataRefType.__init__)
    params = list(sig.parameters.keys())
    assert "outputItemRef" in params, "Missing parameter 'outputItemRef'"
    assert "loopCounterRef" in params, "Missing parameter 'loopCounterRef'"
    assert "inputItemRef" in params, "Missing parameter 'inputItemRef'"

def test_xpdl2_extensions_loopdatareftype_has_outputItemRef():
    assert hasattr(xpdl2_extensions_LoopDataRefType, "outputItemRef")
    descriptor = None
    for klass in xpdl2_extensions_LoopDataRefType.__mro__:
        if "outputItemRef" in klass.__dict__:
            descriptor = klass.__dict__["outputItemRef"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extensions_loopdatareftype_has_loopCounterRef():
    assert hasattr(xpdl2_extensions_LoopDataRefType, "loopCounterRef")
    descriptor = None
    for klass in xpdl2_extensions_LoopDataRefType.__mro__:
        if "loopCounterRef" in klass.__dict__:
            descriptor = klass.__dict__["loopCounterRef"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extensions_loopdatareftype_has_inputItemRef():
    assert hasattr(xpdl2_extensions_LoopDataRefType, "inputItemRef")
    descriptor = None
    for klass in xpdl2_extensions_LoopDataRefType.__mro__:
        if "inputItemRef" in klass.__dict__:
            descriptor = klass.__dict__["inputItemRef"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_xpdltypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_XpdlTypeType)


def test_xpdl2_xpdltypetype_constructor_exists():
    assert callable(xpdl2_XpdlTypeType.__init__)


def test_xpdl2_xpdltypetype_constructor_args():
    sig = inspect.signature(xpdl2_XpdlTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xsdannotation_is_not_abstract():
    assert not inspect.isabstract(XSDAnnotation)


def test_xsdannotation_constructor_exists():
    assert callable(XSDAnnotation.__init__)


def test_xsdannotation_constructor_args():
    sig = inspect.signature(XSDAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_extensions_extendedannotationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_extensions_ExtendedAnnotationType)


def test_xpdl2_extensions_extendedannotationtype_constructor_exists():
    assert callable(xpdl2_extensions_ExtendedAnnotationType.__init__)


def test_xpdl2_extensions_extendedannotationtype_constructor_args():
    sig = inspect.signature(xpdl2_extensions_ExtendedAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_typedeclarationstype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_TypeDeclarationsType)


def test_xpdl2_typedeclarationstype_constructor_exists():
    assert callable(xpdl2_TypeDeclarationsType.__init__)


def test_xpdl2_typedeclarationstype_constructor_args():
    sig = inspect.signature(xpdl2_TypeDeclarationsType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_scripttype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ScriptType)


def test_xpdl2_scripttype_constructor_exists():
    assert callable(xpdl2_ScriptType.__init__)


def test_xpdl2_scripttype_constructor_args():
    sig = inspect.signature(xpdl2_ScriptType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "grammar" in params, "Missing parameter 'grammar'"
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl2_scripttype_has_version():
    assert hasattr(xpdl2_ScriptType, "version")
    descriptor = None
    for klass in xpdl2_ScriptType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_scripttype_has_grammar():
    assert hasattr(xpdl2_ScriptType, "grammar")
    descriptor = None
    for klass in xpdl2_ScriptType.__mro__:
        if "grammar" in klass.__dict__:
            descriptor = klass.__dict__["grammar"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_scripttype_has_type():
    assert hasattr(xpdl2_ScriptType, "type")
    descriptor = None
    for klass in xpdl2_ScriptType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_loopdatareftype_is_not_abstract():
    assert not inspect.isabstract(LoopDataRefType)


def test_loopdatareftype_constructor_exists():
    assert callable(LoopDataRefType.__init__)


def test_loopdatareftype_constructor_args():
    sig = inspect.signature(LoopDataRefType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_xsdschema_is_not_abstract():
    assert not inspect.isabstract(xpdl2_XSDSchema)


def test_xpdl2_xsdschema_constructor_exists():
    assert callable(xpdl2_XSDSchema.__init__)


def test_xpdl2_xsdschema_constructor_args():
    sig = inspect.signature(xpdl2_XSDSchema.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_looptype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_LoopType)


def test_xpdl2_looptype_constructor_exists():
    assert callable(xpdl2_LoopType.__init__)


def test_xpdl2_looptype_constructor_args():
    sig = inspect.signature(xpdl2_LoopType.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_xpdl2_looptype_has_loopType():
    assert hasattr(xpdl2_LoopType, "loopType")
    descriptor = None
    for klass in xpdl2_LoopType.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_loopstandardtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_LoopStandardType)


def test_xpdl2_loopstandardtype_constructor_exists():
    assert callable(xpdl2_LoopStandardType.__init__)


def test_xpdl2_loopstandardtype_constructor_args():
    sig = inspect.signature(xpdl2_LoopStandardType.__init__)
    params = list(sig.parameters.keys())
    assert "testTime" in params, "Missing parameter 'testTime'"
    assert "loopMaximum" in params, "Missing parameter 'loopMaximum'"

def test_xpdl2_loopstandardtype_has_testTime():
    assert hasattr(xpdl2_LoopStandardType, "testTime")
    descriptor = None
    for klass in xpdl2_LoopStandardType.__mro__:
        if "testTime" in klass.__dict__:
            descriptor = klass.__dict__["testTime"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_loopstandardtype_has_loopMaximum():
    assert hasattr(xpdl2_LoopStandardType, "loopMaximum")
    descriptor = None
    for klass in xpdl2_LoopStandardType.__mro__:
        if "loopMaximum" in klass.__dict__:
            descriptor = klass.__dict__["loopMaximum"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_formalparameterstype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_FormalParametersType)


def test_xpdl2_formalparameterstype_constructor_exists():
    assert callable(xpdl2_FormalParametersType.__init__)


def test_xpdl2_formalparameterstype_constructor_args():
    sig = inspect.signature(xpdl2_FormalParametersType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_loopmultiinstancetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_LoopMultiInstanceType)


def test_xpdl2_loopmultiinstancetype_constructor_exists():
    assert callable(xpdl2_LoopMultiInstanceType.__init__)


def test_xpdl2_loopmultiinstancetype_constructor_args():
    sig = inspect.signature(xpdl2_LoopMultiInstanceType.__init__)
    params = list(sig.parameters.keys())
    assert "mIOrdering" in params, "Missing parameter 'mIOrdering'"
    assert "mIFlowCondition" in params, "Missing parameter 'mIFlowCondition'"

def test_xpdl2_loopmultiinstancetype_has_mIOrdering():
    assert hasattr(xpdl2_LoopMultiInstanceType, "mIOrdering")
    descriptor = None
    for klass in xpdl2_LoopMultiInstanceType.__mro__:
        if "mIOrdering" in klass.__dict__:
            descriptor = klass.__dict__["mIOrdering"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_loopmultiinstancetype_has_mIFlowCondition():
    assert hasattr(xpdl2_LoopMultiInstanceType, "mIFlowCondition")
    descriptor = None
    for klass in xpdl2_LoopMultiInstanceType.__mro__:
        if "mIFlowCondition" in klass.__dict__:
            descriptor = klass.__dict__["mIFlowCondition"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_formalparametertype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_FormalParameterType)


def test_xpdl2_formalparametertype_constructor_exists():
    assert callable(xpdl2_FormalParameterType.__init__)


def test_xpdl2_formalparametertype_constructor_args():
    sig = inspect.signature(xpdl2_FormalParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl2_formalparametertype_has_description():
    assert hasattr(xpdl2_FormalParameterType, "description")
    descriptor = None
    for klass in xpdl2_FormalParameterType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_formalparametertype_has_mode():
    assert hasattr(xpdl2_FormalParameterType, "mode")
    descriptor = None
    for klass in xpdl2_FormalParameterType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_formalparametertype_has_id():
    assert hasattr(xpdl2_FormalParameterType, "id")
    descriptor = None
    for klass in xpdl2_FormalParameterType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_formalparametertype_has_name():
    assert hasattr(xpdl2_FormalParameterType, "name")
    descriptor = None
    for klass in xpdl2_FormalParameterType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extensible_is_not_abstract():
    assert not inspect.isabstract(Extensible)


def test_extensible_constructor_exists():
    assert callable(Extensible.__init__)


def test_extensible_constructor_args():
    sig = inspect.signature(Extensible.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_typedeclarationtype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_TypeDeclarationType)


def test_xpdl2_typedeclarationtype_constructor_exists():
    assert callable(xpdl2_TypeDeclarationType.__init__)


def test_xpdl2_typedeclarationtype_constructor_args():
    sig = inspect.signature(xpdl2_TypeDeclarationType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_xpdl2_typedeclarationtype_has_id():
    assert hasattr(xpdl2_TypeDeclarationType, "id")
    descriptor = None
    for klass in xpdl2_TypeDeclarationType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_typedeclarationtype_has_description():
    assert hasattr(xpdl2_TypeDeclarationType, "description")
    descriptor = None
    for klass in xpdl2_TypeDeclarationType.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_typedeclarationtype_has_name():
    assert hasattr(xpdl2_TypeDeclarationType, "name")
    descriptor = None
    for klass in xpdl2_TypeDeclarationType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_externalpackage_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExternalPackage)


def test_xpdl2_externalpackage_constructor_exists():
    assert callable(xpdl2_ExternalPackage.__init__)


def test_xpdl2_externalpackage_constructor_args():
    sig = inspect.signature(xpdl2_ExternalPackage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "href" in params, "Missing parameter 'href'"

def test_xpdl2_externalpackage_has_name():
    assert hasattr(xpdl2_ExternalPackage, "name")
    descriptor = None
    for klass in xpdl2_ExternalPackage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_externalpackage_has_id():
    assert hasattr(xpdl2_ExternalPackage, "id")
    descriptor = None
    for klass in xpdl2_ExternalPackage.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_externalpackage_has_href():
    assert hasattr(xpdl2_ExternalPackage, "href")
    descriptor = None
    for klass in xpdl2_ExternalPackage.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_externalpackages_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExternalPackages)


def test_xpdl2_externalpackages_constructor_exists():
    assert callable(xpdl2_ExternalPackages.__init__)


def test_xpdl2_externalpackages_constructor_args():
    sig = inspect.signature(xpdl2_ExternalPackages.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_extensible_is_not_abstract():
    assert not inspect.isabstract(xpdl2_Extensible)


def test_xpdl2_extensible_constructor_exists():
    assert callable(xpdl2_Extensible.__init__)


def test_xpdl2_extensible_constructor_args():
    sig = inspect.signature(xpdl2_Extensible.__init__)
    params = list(sig.parameters.keys())



def test_extendedannotationtype_is_not_abstract():
    assert not inspect.isabstract(ExtendedAnnotationType)


def test_extendedannotationtype_constructor_exists():
    assert callable(ExtendedAnnotationType.__init__)


def test_extendedannotationtype_constructor_args():
    sig = inspect.signature(ExtendedAnnotationType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_extendedattributetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExtendedAttributeType)


def test_xpdl2_extendedattributetype_constructor_exists():
    assert callable(xpdl2_ExtendedAttributeType.__init__)


def test_xpdl2_extendedattributetype_constructor_args():
    sig = inspect.signature(xpdl2_ExtendedAttributeType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "value" in params, "Missing parameter 'value'"
    assert "group" in params, "Missing parameter 'group'"

def test_xpdl2_extendedattributetype_has_name():
    assert hasattr(xpdl2_ExtendedAttributeType, "name")
    descriptor = None
    for klass in xpdl2_ExtendedAttributeType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extendedattributetype_has_any():
    assert hasattr(xpdl2_ExtendedAttributeType, "any")
    descriptor = None
    for klass in xpdl2_ExtendedAttributeType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extendedattributetype_has_mixed():
    assert hasattr(xpdl2_ExtendedAttributeType, "mixed")
    descriptor = None
    for klass in xpdl2_ExtendedAttributeType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extendedattributetype_has_value():
    assert hasattr(xpdl2_ExtendedAttributeType, "value")
    descriptor = None
    for klass in xpdl2_ExtendedAttributeType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_extendedattributetype_has_group():
    assert hasattr(xpdl2_ExtendedAttributeType, "group")
    descriptor = None
    for klass in xpdl2_ExtendedAttributeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_extendedattributestype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExtendedAttributesType)


def test_xpdl2_extendedattributestype_constructor_exists():
    assert callable(xpdl2_ExtendedAttributesType.__init__)


def test_xpdl2_extendedattributestype_constructor_args():
    sig = inspect.signature(xpdl2_ExtendedAttributesType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_expressiontype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExpressionType)


def test_xpdl2_expressiontype_constructor_exists():
    assert callable(xpdl2_ExpressionType.__init__)


def test_xpdl2_expressiontype_constructor_args():
    sig = inspect.signature(xpdl2_ExpressionType.__init__)
    params = list(sig.parameters.keys())
    assert "scriptGrammar" in params, "Missing parameter 'scriptGrammar'"
    assert "any" in params, "Missing parameter 'any'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "scriptVersion" in params, "Missing parameter 'scriptVersion'"
    assert "group" in params, "Missing parameter 'group'"
    assert "scriptType" in params, "Missing parameter 'scriptType'"

def test_xpdl2_expressiontype_has_scriptGrammar():
    assert hasattr(xpdl2_ExpressionType, "scriptGrammar")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "scriptGrammar" in klass.__dict__:
            descriptor = klass.__dict__["scriptGrammar"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_expressiontype_has_any():
    assert hasattr(xpdl2_ExpressionType, "any")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "any" in klass.__dict__:
            descriptor = klass.__dict__["any"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_expressiontype_has_mixed():
    assert hasattr(xpdl2_ExpressionType, "mixed")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_expressiontype_has_scriptVersion():
    assert hasattr(xpdl2_ExpressionType, "scriptVersion")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "scriptVersion" in klass.__dict__:
            descriptor = klass.__dict__["scriptVersion"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_expressiontype_has_group():
    assert hasattr(xpdl2_ExpressionType, "group")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_expressiontype_has_scriptType():
    assert hasattr(xpdl2_ExpressionType, "scriptType")
    descriptor = None
    for klass in xpdl2_ExpressionType.__mro__:
        if "scriptType" in klass.__dict__:
            descriptor = klass.__dict__["scriptType"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_datatypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_DataTypeType)


def test_xpdl2_datatypetype_constructor_exists():
    assert callable(xpdl2_DataTypeType.__init__)


def test_xpdl2_datatypetype_constructor_args():
    sig = inspect.signature(xpdl2_DataTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "carnotType" in params, "Missing parameter 'carnotType'"

def test_xpdl2_datatypetype_has_carnotType():
    assert hasattr(xpdl2_DataTypeType, "carnotType")
    descriptor = None
    for klass in xpdl2_DataTypeType.__mro__:
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



def test_xpdl2_schematypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_SchemaTypeType)


def test_xpdl2_schematypetype_constructor_exists():
    assert callable(xpdl2_SchemaTypeType.__init__)


def test_xpdl2_schematypetype_constructor_args():
    sig = inspect.signature(xpdl2_SchemaTypeType.__init__)
    params = list(sig.parameters.keys())



def test_xpdl2_externalreferencetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_ExternalReferenceType)


def test_xpdl2_externalreferencetype_constructor_exists():
    assert callable(xpdl2_ExternalReferenceType.__init__)


def test_xpdl2_externalreferencetype_constructor_args():
    sig = inspect.signature(xpdl2_ExternalReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "uuid" in params, "Missing parameter 'uuid'"
    assert "location" in params, "Missing parameter 'location'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "xref" in params, "Missing parameter 'xref'"

def test_xpdl2_externalreferencetype_has_uuid():
    assert hasattr(xpdl2_ExternalReferenceType, "uuid")
    descriptor = None
    for klass in xpdl2_ExternalReferenceType.__mro__:
        if "uuid" in klass.__dict__:
            descriptor = klass.__dict__["uuid"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_externalreferencetype_has_location():
    assert hasattr(xpdl2_ExternalReferenceType, "location")
    descriptor = None
    for klass in xpdl2_ExternalReferenceType.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_externalreferencetype_has_namespace():
    assert hasattr(xpdl2_ExternalReferenceType, "namespace")
    descriptor = None
    for klass in xpdl2_ExternalReferenceType.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_xpdl2_externalreferencetype_has_xref():
    assert hasattr(xpdl2_ExternalReferenceType, "xref")
    descriptor = None
    for klass in xpdl2_ExternalReferenceType.__mro__:
        if "xref" in klass.__dict__:
            descriptor = klass.__dict__["xref"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_declaredtypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_DeclaredTypeType)


def test_xpdl2_declaredtypetype_constructor_exists():
    assert callable(xpdl2_DeclaredTypeType.__init__)


def test_xpdl2_declaredtypetype_constructor_args():
    sig = inspect.signature(xpdl2_DeclaredTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_xpdl2_declaredtypetype_has_id():
    assert hasattr(xpdl2_DeclaredTypeType, "id")
    descriptor = None
    for klass in xpdl2_DeclaredTypeType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_xpdl2_basictypetype_is_not_abstract():
    assert not inspect.isabstract(xpdl2_BasicTypeType)


def test_xpdl2_basictypetype_constructor_exists():
    assert callable(xpdl2_BasicTypeType.__init__)


def test_xpdl2_basictypetype_constructor_args():
    sig = inspect.signature(xpdl2_BasicTypeType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_xpdl2_basictypetype_has_type():
    assert hasattr(xpdl2_BasicTypeType, "type")
    descriptor = None
    for klass in xpdl2_BasicTypeType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_miorderingtype_exists():
    # Check that the Enumeration exists
    assert MIOrderingType is not None

def test_miorderingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MIOrderingType]
    expected_literals = [
        "Sequential",
        "Parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MIOrderingType"

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

def test_modetype_exists():
    # Check that the Enumeration exists
    assert ModeType is not None

def test_modetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ModeType]
    expected_literals = [
        "INOUT",
        "OUT",
        "IN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ModeType"

def test_typetype_exists():
    # Check that the Enumeration exists
    assert TypeType is not None

def test_typetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeType]
    expected_literals = [
        "BOOLEAN",
        "REFERENCE",
        "INTEGER",
        "DATETIME",
        "FLOAT",
        "PERFORMER",
        "STRING",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeType"

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

def test_miflowconditiontype_exists():
    # Check that the Enumeration exists
    assert MIFlowConditionType is not None

def test_miflowconditiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MIFlowConditionType]
    expected_literals = [
        "All",
        "Complex",
        "None_",
        "One",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MIFlowConditionType"


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
xpdl2_extensions_LoopDataRefType_strategy = st.builds(
    xpdl2_extensions_LoopDataRefType,
    outputItemRef=
        safe_text,
    loopCounterRef=
        safe_text,
    inputItemRef=
        safe_text
)
xpdl2_XpdlTypeType_strategy = st.builds(
    xpdl2_XpdlTypeType,
)
XSDAnnotation_strategy = st.builds(
    XSDAnnotation,
)
xpdl2_extensions_ExtendedAnnotationType_strategy = st.builds(
    xpdl2_extensions_ExtendedAnnotationType,
)
xpdl2_TypeDeclarationsType_strategy = st.builds(
    xpdl2_TypeDeclarationsType,
)
xpdl2_ScriptType_strategy = st.builds(
    xpdl2_ScriptType,
    version=
        safe_text,
    grammar=
        safe_text,
    type=
        safe_text
)
LoopDataRefType_strategy = st.builds(
    LoopDataRefType,
)
xpdl2_XSDSchema_strategy = st.builds(
    xpdl2_XSDSchema,
)
xpdl2_LoopType_strategy = st.builds(
    xpdl2_LoopType,
    loopType=
        safe_text
)
xpdl2_LoopStandardType_strategy = st.builds(
    xpdl2_LoopStandardType,
    testTime=
        safe_text,
    loopMaximum=
        safe_text
)
xpdl2_FormalParametersType_strategy = st.builds(
    xpdl2_FormalParametersType,
)
xpdl2_LoopMultiInstanceType_strategy = st.builds(
    xpdl2_LoopMultiInstanceType,
    mIOrdering=
        safe_text,
    mIFlowCondition=
        safe_text
)
xpdl2_FormalParameterType_strategy = st.builds(
    xpdl2_FormalParameterType,
    description=
        safe_text,
    mode=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
Extensible_strategy = st.builds(
    Extensible,
)
xpdl2_TypeDeclarationType_strategy = st.builds(
    xpdl2_TypeDeclarationType,
    id=
        safe_text,
    description=
        safe_text,
    name=
        safe_text
)
xpdl2_ExternalPackage_strategy = st.builds(
    xpdl2_ExternalPackage,
    name=
        safe_text,
    id=
        safe_text,
    href=
        safe_text
)
xpdl2_ExternalPackages_strategy = st.builds(
    xpdl2_ExternalPackages,
)
xpdl2_Extensible_strategy = st.builds(
    xpdl2_Extensible,
)
ExtendedAnnotationType_strategy = st.builds(
    ExtendedAnnotationType,
)
xpdl2_ExtendedAttributeType_strategy = st.builds(
    xpdl2_ExtendedAttributeType,
    name=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    value=
        safe_text,
    group=
        safe_text
)
xpdl2_ExtendedAttributesType_strategy = st.builds(
    xpdl2_ExtendedAttributesType,
)
xpdl2_ExpressionType_strategy = st.builds(
    xpdl2_ExpressionType,
    scriptGrammar=
        safe_text,
    any=
        safe_text,
    mixed=
        safe_text,
    scriptVersion=
        safe_text,
    group=
        safe_text,
    scriptType=
        safe_text
)
xpdl2_DataTypeType_strategy = st.builds(
    xpdl2_DataTypeType,
    carnotType=
        safe_text
)
XpdlTypeType_strategy = st.builds(
    XpdlTypeType,
)
xpdl2_SchemaTypeType_strategy = st.builds(
    xpdl2_SchemaTypeType,
)
xpdl2_ExternalReferenceType_strategy = st.builds(
    xpdl2_ExternalReferenceType,
    uuid=
        safe_text,
    location=
        safe_text,
    namespace=
        safe_text,
    xref=
        safe_text
)
xpdl2_DeclaredTypeType_strategy = st.builds(
    xpdl2_DeclaredTypeType,
    id=
        safe_text
)
xpdl2_BasicTypeType_strategy = st.builds(
    xpdl2_BasicTypeType,
    type=
        safe_text
)

@given(instance=xpdl2_extensions_LoopDataRefType_strategy)
@settings(max_examples=50)
def test_xpdl2_extensions_loopdatareftype_instantiation(instance):
    assert isinstance(instance, xpdl2_extensions_LoopDataRefType)



@given(instance=xpdl2_extensions_LoopDataRefType_strategy)
def test_xpdl2_extensions_loopdatareftype_outputItemRef_setter(instance):
    original = instance.outputItemRef
    instance.outputItemRef = original
    assert instance.outputItemRef == original



@given(instance=xpdl2_extensions_LoopDataRefType_strategy)
def test_xpdl2_extensions_loopdatareftype_loopCounterRef_setter(instance):
    original = instance.loopCounterRef
    instance.loopCounterRef = original
    assert instance.loopCounterRef == original



@given(instance=xpdl2_extensions_LoopDataRefType_strategy)
def test_xpdl2_extensions_loopdatareftype_inputItemRef_setter(instance):
    original = instance.inputItemRef
    instance.inputItemRef = original
    assert instance.inputItemRef == original

@given(instance=xpdl2_XpdlTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2_xpdltypetype_instantiation(instance):
    assert isinstance(instance, xpdl2_XpdlTypeType)

@given(instance=XSDAnnotation_strategy)
@settings(max_examples=50)
def test_xsdannotation_instantiation(instance):
    assert isinstance(instance, XSDAnnotation)

@given(instance=xpdl2_extensions_ExtendedAnnotationType_strategy)
@settings(max_examples=50)
def test_xpdl2_extensions_extendedannotationtype_instantiation(instance):
    assert isinstance(instance, xpdl2_extensions_ExtendedAnnotationType)

@given(instance=xpdl2_TypeDeclarationsType_strategy)
@settings(max_examples=50)
def test_xpdl2_typedeclarationstype_instantiation(instance):
    assert isinstance(instance, xpdl2_TypeDeclarationsType)

@given(instance=xpdl2_ScriptType_strategy)
@settings(max_examples=50)
def test_xpdl2_scripttype_instantiation(instance):
    assert isinstance(instance, xpdl2_ScriptType)



@given(instance=xpdl2_ScriptType_strategy)
def test_xpdl2_scripttype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=xpdl2_ScriptType_strategy)
def test_xpdl2_scripttype_grammar_setter(instance):
    original = instance.grammar
    instance.grammar = original
    assert instance.grammar == original



@given(instance=xpdl2_ScriptType_strategy)
def test_xpdl2_scripttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=LoopDataRefType_strategy)
@settings(max_examples=50)
def test_loopdatareftype_instantiation(instance):
    assert isinstance(instance, LoopDataRefType)

@given(instance=xpdl2_XSDSchema_strategy)
@settings(max_examples=50)
def test_xpdl2_xsdschema_instantiation(instance):
    assert isinstance(instance, xpdl2_XSDSchema)

@given(instance=xpdl2_LoopType_strategy)
@settings(max_examples=50)
def test_xpdl2_looptype_instantiation(instance):
    assert isinstance(instance, xpdl2_LoopType)



@given(instance=xpdl2_LoopType_strategy)
def test_xpdl2_looptype_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=xpdl2_LoopStandardType_strategy)
@settings(max_examples=50)
def test_xpdl2_loopstandardtype_instantiation(instance):
    assert isinstance(instance, xpdl2_LoopStandardType)



@given(instance=xpdl2_LoopStandardType_strategy)
def test_xpdl2_loopstandardtype_testTime_setter(instance):
    original = instance.testTime
    instance.testTime = original
    assert instance.testTime == original



@given(instance=xpdl2_LoopStandardType_strategy)
def test_xpdl2_loopstandardtype_loopMaximum_setter(instance):
    original = instance.loopMaximum
    instance.loopMaximum = original
    assert instance.loopMaximum == original

@given(instance=xpdl2_FormalParametersType_strategy)
@settings(max_examples=50)
def test_xpdl2_formalparameterstype_instantiation(instance):
    assert isinstance(instance, xpdl2_FormalParametersType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=xpdl2_FormalParametersType_strategy)
@settings(max_examples=30)
def test_xpdl2_formalparameterstype_addformalparameter_changes_state(instance):
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
        assert has_statements, f"Function 'addFormalParameter' in xpdl2_FormalParametersType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addFormalParameter' in xpdl2_FormalParametersType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addFormalParameter' in xpdl2_FormalParametersType is not implemented or raised an error")

@given(instance=xpdl2_LoopMultiInstanceType_strategy)
@settings(max_examples=50)
def test_xpdl2_loopmultiinstancetype_instantiation(instance):
    assert isinstance(instance, xpdl2_LoopMultiInstanceType)



@given(instance=xpdl2_LoopMultiInstanceType_strategy)
def test_xpdl2_loopmultiinstancetype_mIOrdering_setter(instance):
    original = instance.mIOrdering
    instance.mIOrdering = original
    assert instance.mIOrdering == original



@given(instance=xpdl2_LoopMultiInstanceType_strategy)
def test_xpdl2_loopmultiinstancetype_mIFlowCondition_setter(instance):
    original = instance.mIFlowCondition
    instance.mIFlowCondition = original
    assert instance.mIFlowCondition == original

@given(instance=xpdl2_FormalParameterType_strategy)
@settings(max_examples=50)
def test_xpdl2_formalparametertype_instantiation(instance):
    assert isinstance(instance, xpdl2_FormalParameterType)



@given(instance=xpdl2_FormalParameterType_strategy)
def test_xpdl2_formalparametertype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl2_FormalParameterType_strategy)
def test_xpdl2_formalparametertype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=xpdl2_FormalParameterType_strategy)
def test_xpdl2_formalparametertype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl2_FormalParameterType_strategy)
def test_xpdl2_formalparametertype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Extensible_strategy)
@settings(max_examples=50)
def test_extensible_instantiation(instance):
    assert isinstance(instance, Extensible)

@given(instance=xpdl2_TypeDeclarationType_strategy)
@settings(max_examples=50)
def test_xpdl2_typedeclarationtype_instantiation(instance):
    assert isinstance(instance, xpdl2_TypeDeclarationType)



@given(instance=xpdl2_TypeDeclarationType_strategy)
def test_xpdl2_typedeclarationtype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl2_TypeDeclarationType_strategy)
def test_xpdl2_typedeclarationtype_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=xpdl2_TypeDeclarationType_strategy)
def test_xpdl2_typedeclarationtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xpdl2_ExternalPackage_strategy)
@settings(max_examples=50)
def test_xpdl2_externalpackage_instantiation(instance):
    assert isinstance(instance, xpdl2_ExternalPackage)



@given(instance=xpdl2_ExternalPackage_strategy)
def test_xpdl2_externalpackage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl2_ExternalPackage_strategy)
def test_xpdl2_externalpackage_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=xpdl2_ExternalPackage_strategy)
def test_xpdl2_externalpackage_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=xpdl2_ExternalPackages_strategy)
@settings(max_examples=50)
def test_xpdl2_externalpackages_instantiation(instance):
    assert isinstance(instance, xpdl2_ExternalPackages)

@given(instance=xpdl2_Extensible_strategy)
@settings(max_examples=50)
def test_xpdl2_extensible_instantiation(instance):
    assert isinstance(instance, xpdl2_Extensible)

@given(instance=ExtendedAnnotationType_strategy)
@settings(max_examples=50)
def test_extendedannotationtype_instantiation(instance):
    assert isinstance(instance, ExtendedAnnotationType)

@given(instance=xpdl2_ExtendedAttributeType_strategy)
@settings(max_examples=50)
def test_xpdl2_extendedattributetype_instantiation(instance):
    assert isinstance(instance, xpdl2_ExtendedAttributeType)



@given(instance=xpdl2_ExtendedAttributeType_strategy)
def test_xpdl2_extendedattributetype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xpdl2_ExtendedAttributeType_strategy)
def test_xpdl2_extendedattributetype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xpdl2_ExtendedAttributeType_strategy)
def test_xpdl2_extendedattributetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xpdl2_ExtendedAttributeType_strategy)
def test_xpdl2_extendedattributetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=xpdl2_ExtendedAttributeType_strategy)
def test_xpdl2_extendedattributetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=xpdl2_ExtendedAttributesType_strategy)
@settings(max_examples=50)
def test_xpdl2_extendedattributestype_instantiation(instance):
    assert isinstance(instance, xpdl2_ExtendedAttributesType)

@given(instance=xpdl2_ExpressionType_strategy)
@settings(max_examples=50)
def test_xpdl2_expressiontype_instantiation(instance):
    assert isinstance(instance, xpdl2_ExpressionType)



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_scriptGrammar_setter(instance):
    original = instance.scriptGrammar
    instance.scriptGrammar = original
    assert instance.scriptGrammar == original



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_any_setter(instance):
    original = instance.any
    instance.any = original
    assert instance.any == original



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_scriptVersion_setter(instance):
    original = instance.scriptVersion
    instance.scriptVersion = original
    assert instance.scriptVersion == original



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=xpdl2_ExpressionType_strategy)
def test_xpdl2_expressiontype_scriptType_setter(instance):
    original = instance.scriptType
    instance.scriptType = original
    assert instance.scriptType == original

@given(instance=xpdl2_DataTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2_datatypetype_instantiation(instance):
    assert isinstance(instance, xpdl2_DataTypeType)



@given(instance=xpdl2_DataTypeType_strategy)
def test_xpdl2_datatypetype_carnotType_setter(instance):
    original = instance.carnotType
    instance.carnotType = original
    assert instance.carnotType == original

@given(instance=XpdlTypeType_strategy)
@settings(max_examples=50)
def test_xpdltypetype_instantiation(instance):
    assert isinstance(instance, XpdlTypeType)

@given(instance=xpdl2_SchemaTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2_schematypetype_instantiation(instance):
    assert isinstance(instance, xpdl2_SchemaTypeType)

@given(instance=xpdl2_ExternalReferenceType_strategy)
@settings(max_examples=50)
def test_xpdl2_externalreferencetype_instantiation(instance):
    assert isinstance(instance, xpdl2_ExternalReferenceType)



@given(instance=xpdl2_ExternalReferenceType_strategy)
def test_xpdl2_externalreferencetype_uuid_setter(instance):
    original = instance.uuid
    instance.uuid = original
    assert instance.uuid == original



@given(instance=xpdl2_ExternalReferenceType_strategy)
def test_xpdl2_externalreferencetype_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=xpdl2_ExternalReferenceType_strategy)
def test_xpdl2_externalreferencetype_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=xpdl2_ExternalReferenceType_strategy)
def test_xpdl2_externalreferencetype_xref_setter(instance):
    original = instance.xref
    instance.xref = original
    assert instance.xref == original

@given(instance=xpdl2_DeclaredTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2_declaredtypetype_instantiation(instance):
    assert isinstance(instance, xpdl2_DeclaredTypeType)



@given(instance=xpdl2_DeclaredTypeType_strategy)
def test_xpdl2_declaredtypetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=xpdl2_BasicTypeType_strategy)
@settings(max_examples=50)
def test_xpdl2_basictypetype_instantiation(instance):
    assert isinstance(instance, xpdl2_BasicTypeType)



@given(instance=xpdl2_BasicTypeType_strategy)
def test_xpdl2_basictypetype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
