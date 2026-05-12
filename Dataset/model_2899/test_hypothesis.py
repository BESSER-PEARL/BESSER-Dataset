import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    domainmodel_SystemModule,
    BusinessModule,
    domainmodel_BusinessFeatures,
    domainmodel_MainFeatureOption,
    UIFeature,
    domainmodel_MainFeature,
    domainmodel_ScreenModule,
    domainmodel_ControllerElement,
    domainmodel_BusinessFeatureType,
    SystemModule,
    domainmodel_BusinessModule,
    domainmodel_UIModule,
    domainmodel_UIFeature,
    domainmodel_InterfaceMethodCallParameter,
    domainmodel_AbstractNamespaceElement,
    AbstractElement,
    domainmodel_SystemDefinition,
    domainmodel_NamespaceDeclaration,
    Type,
    AbstractNamespaceElement,
    domainmodel_DataType,
    domainmodel_Import,
    domainmodel_Type,
    domainmodel_AbstractElement,
    domainmodel_Domainmodel,
    domainmodel_SetActionReceiver,
    domainmodel_UIActionFeature,
    domainmodel_BusinessFeature,
    domainmodel_InterfaceMethodCallParameters,
    SetRestCallReceiverParameter,
    domainmodel_SetRestCallReceiverReturnTypeParameter,
    domainmodel_SetRestCallReceiverURLParameter,
    SetActionReceiver,
    domainmodel_SetRestCallReceiver,
    domainmodel_SetRestCallReceiverParameters,
    domainmodel_SetRestCallReceiverParameter,
    domainmodel_SetRestCallReceiverIDParameter,
    domainmodel_ValidatorRules,
    domainmodel_ValidatorRule,
    domainmodel_ScreenFeature,
    UIActionFeature,
    domainmodel_ExecuteAction,
    domainmodel_InterfaceMethodCall,
    domainmodel_NavigateToAction,
    domainmodel_ScreenModelParameters,
    domainmodel_ScreenModelParameter,
    domainmodel_SetUIElementReceiver,
    domainmodel_ValidatorFeature,
    InitActionFeature,
    domainmodel_AttachAction,
    domainmodel_SetAction,
    domainmodel_ValidateAction,
    ControllerElement,
    domainmodel_UIActionModule,
    domainmodel_ValidatorModule,
    domainmodel_InitActionModule,
    domainmodel_InitActionFeature,
    domainmodel_BindAction,
    domainmodel_BindSource,
    BindSource,
    domainmodel_BindEnumSource,
    domainmodel_ElementFeature,
    domainmodel_ViewElement,
    ViewElement,
    domainmodel_ContainerElement,
    domainmodel_ContentElement,
    domainmodel_InterfaceOperationUsageRule,
    BusinessFeatureType,
    domainmodel_InterfaceDeclaration,
    domainmodel_InterfaceOperation,
    domainmodel_MethodCall,
    domainmodel_MethodParameters,
    domainmodel_MethodParameter,
    domainmodel_DomainEntity,
    domainmodel_ModelFeature,
    ScreenModule,
    domainmodel_ViewModule,
    domainmodel_ControllerModule,
    domainmodel_ModelModule,
    domainmodel_EntryParametersModule,
    domainmodel_DomainRepository,
    domainmodel_StatelessComponent,
    domainmodel_InterfaceOperationsUsageRule,
    domainmodel_Feature,
    PropertyNameLiteral,
    UIElementReceiverKey,
    ContentElementLiteral,
    ContainerElementLiteral,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_domainmodel_systemmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SystemModule)


def test_domainmodel_systemmodule_constructor_exists():
    assert callable(domainmodel_SystemModule.__init__)


def test_domainmodel_systemmodule_constructor_args():
    sig = inspect.signature(domainmodel_SystemModule.__init__)
    params = list(sig.parameters.keys())



def test_businessmodule_is_not_abstract():
    assert not inspect.isabstract(BusinessModule)


def test_businessmodule_constructor_exists():
    assert callable(BusinessModule.__init__)


def test_businessmodule_constructor_args():
    sig = inspect.signature(BusinessModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_businessfeatures_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BusinessFeatures)


def test_domainmodel_businessfeatures_constructor_exists():
    assert callable(domainmodel_BusinessFeatures.__init__)


def test_domainmodel_businessfeatures_constructor_args():
    sig = inspect.signature(domainmodel_BusinessFeatures.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_mainfeatureoption_is_not_abstract():
    assert not inspect.isabstract(domainmodel_MainFeatureOption)


def test_domainmodel_mainfeatureoption_constructor_exists():
    assert callable(domainmodel_MainFeatureOption.__init__)


def test_domainmodel_mainfeatureoption_constructor_args():
    sig = inspect.signature(domainmodel_MainFeatureOption.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_mainfeatureoption_has_name():
    assert hasattr(domainmodel_MainFeatureOption, "name")
    descriptor = None
    for klass in domainmodel_MainFeatureOption.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uifeature_is_not_abstract():
    assert not inspect.isabstract(UIFeature)


def test_uifeature_constructor_exists():
    assert callable(UIFeature.__init__)


def test_uifeature_constructor_args():
    sig = inspect.signature(UIFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_mainfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_MainFeature)


def test_domainmodel_mainfeature_constructor_exists():
    assert callable(domainmodel_MainFeature.__init__)


def test_domainmodel_mainfeature_constructor_args():
    sig = inspect.signature(domainmodel_MainFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_screenmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ScreenModule)


def test_domainmodel_screenmodule_constructor_exists():
    assert callable(domainmodel_ScreenModule.__init__)


def test_domainmodel_screenmodule_constructor_args():
    sig = inspect.signature(domainmodel_ScreenModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_controllerelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ControllerElement)


def test_domainmodel_controllerelement_constructor_exists():
    assert callable(domainmodel_ControllerElement.__init__)


def test_domainmodel_controllerelement_constructor_args():
    sig = inspect.signature(domainmodel_ControllerElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_businessfeaturetype_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BusinessFeatureType)


def test_domainmodel_businessfeaturetype_constructor_exists():
    assert callable(domainmodel_BusinessFeatureType.__init__)


def test_domainmodel_businessfeaturetype_constructor_args():
    sig = inspect.signature(domainmodel_BusinessFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_systemmodule_is_not_abstract():
    assert not inspect.isabstract(SystemModule)


def test_systemmodule_constructor_exists():
    assert callable(SystemModule.__init__)


def test_systemmodule_constructor_args():
    sig = inspect.signature(SystemModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_businessmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BusinessModule)


def test_domainmodel_businessmodule_constructor_exists():
    assert callable(domainmodel_BusinessModule.__init__)


def test_domainmodel_businessmodule_constructor_args():
    sig = inspect.signature(domainmodel_BusinessModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_uimodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_UIModule)


def test_domainmodel_uimodule_constructor_exists():
    assert callable(domainmodel_UIModule.__init__)


def test_domainmodel_uimodule_constructor_args():
    sig = inspect.signature(domainmodel_UIModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_uifeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_UIFeature)


def test_domainmodel_uifeature_constructor_exists():
    assert callable(domainmodel_UIFeature.__init__)


def test_domainmodel_uifeature_constructor_args():
    sig = inspect.signature(domainmodel_UIFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_interfacemethodcallparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceMethodCallParameter)


def test_domainmodel_interfacemethodcallparameter_constructor_exists():
    assert callable(domainmodel_InterfaceMethodCallParameter.__init__)


def test_domainmodel_interfacemethodcallparameter_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceMethodCallParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterType" in params, "Missing parameter 'parameterType'"

def test_domainmodel_interfacemethodcallparameter_has_parameterType():
    assert hasattr(domainmodel_InterfaceMethodCallParameter, "parameterType")
    descriptor = None
    for klass in domainmodel_InterfaceMethodCallParameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_abstractnamespaceelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_AbstractNamespaceElement)


def test_domainmodel_abstractnamespaceelement_constructor_exists():
    assert callable(domainmodel_AbstractNamespaceElement.__init__)


def test_domainmodel_abstractnamespaceelement_constructor_args():
    sig = inspect.signature(domainmodel_AbstractNamespaceElement.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_systemdefinition_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SystemDefinition)


def test_domainmodel_systemdefinition_constructor_exists():
    assert callable(domainmodel_SystemDefinition.__init__)


def test_domainmodel_systemdefinition_constructor_args():
    sig = inspect.signature(domainmodel_SystemDefinition.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_namespacedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainmodel_NamespaceDeclaration)


def test_domainmodel_namespacedeclaration_constructor_exists():
    assert callable(domainmodel_NamespaceDeclaration.__init__)


def test_domainmodel_namespacedeclaration_constructor_args():
    sig = inspect.signature(domainmodel_NamespaceDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_abstractnamespaceelement_is_not_abstract():
    assert not inspect.isabstract(AbstractNamespaceElement)


def test_abstractnamespaceelement_constructor_exists():
    assert callable(AbstractNamespaceElement.__init__)


def test_abstractnamespaceelement_constructor_args():
    sig = inspect.signature(AbstractNamespaceElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_datatype_is_not_abstract():
    assert not inspect.isabstract(domainmodel_DataType)


def test_domainmodel_datatype_constructor_exists():
    assert callable(domainmodel_DataType.__init__)


def test_domainmodel_datatype_constructor_args():
    sig = inspect.signature(domainmodel_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "mappedType" in params, "Missing parameter 'mappedType'"
    assert "name" in params, "Missing parameter 'name'"
    assert "initValue" in params, "Missing parameter 'initValue'"

def test_domainmodel_datatype_has_mappedType():
    assert hasattr(domainmodel_DataType, "mappedType")
    descriptor = None
    for klass in domainmodel_DataType.__mro__:
        if "mappedType" in klass.__dict__:
            descriptor = klass.__dict__["mappedType"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_datatype_has_name():
    assert hasattr(domainmodel_DataType, "name")
    descriptor = None
    for klass in domainmodel_DataType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_datatype_has_initValue():
    assert hasattr(domainmodel_DataType, "initValue")
    descriptor = None
    for klass in domainmodel_DataType.__mro__:
        if "initValue" in klass.__dict__:
            descriptor = klass.__dict__["initValue"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_import_is_not_abstract():
    assert not inspect.isabstract(domainmodel_Import)


def test_domainmodel_import_constructor_exists():
    assert callable(domainmodel_Import.__init__)


def test_domainmodel_import_constructor_args():
    sig = inspect.signature(domainmodel_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_domainmodel_import_has_importedNamespace():
    assert hasattr(domainmodel_Import, "importedNamespace")
    descriptor = None
    for klass in domainmodel_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_type_is_not_abstract():
    assert not inspect.isabstract(domainmodel_Type)


def test_domainmodel_type_constructor_exists():
    assert callable(domainmodel_Type.__init__)


def test_domainmodel_type_constructor_args():
    sig = inspect.signature(domainmodel_Type.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_abstractelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_AbstractElement)


def test_domainmodel_abstractelement_constructor_exists():
    assert callable(domainmodel_AbstractElement.__init__)


def test_domainmodel_abstractelement_constructor_args():
    sig = inspect.signature(domainmodel_AbstractElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_abstractelement_has_name():
    assert hasattr(domainmodel_AbstractElement, "name")
    descriptor = None
    for klass in domainmodel_AbstractElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_domainmodel_is_not_abstract():
    assert not inspect.isabstract(domainmodel_Domainmodel)


def test_domainmodel_domainmodel_constructor_exists():
    assert callable(domainmodel_Domainmodel.__init__)


def test_domainmodel_domainmodel_constructor_args():
    sig = inspect.signature(domainmodel_Domainmodel.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setactionreceiver_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetActionReceiver)


def test_domainmodel_setactionreceiver_constructor_exists():
    assert callable(domainmodel_SetActionReceiver.__init__)


def test_domainmodel_setactionreceiver_constructor_args():
    sig = inspect.signature(domainmodel_SetActionReceiver.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_uiactionfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_UIActionFeature)


def test_domainmodel_uiactionfeature_constructor_exists():
    assert callable(domainmodel_UIActionFeature.__init__)


def test_domainmodel_uiactionfeature_constructor_args():
    sig = inspect.signature(domainmodel_UIActionFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_businessfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BusinessFeature)


def test_domainmodel_businessfeature_constructor_exists():
    assert callable(domainmodel_BusinessFeature.__init__)


def test_domainmodel_businessfeature_constructor_args():
    sig = inspect.signature(domainmodel_BusinessFeature.__init__)
    params = list(sig.parameters.keys())
    assert "connectEnd" in params, "Missing parameter 'connectEnd'"
    assert "name" in params, "Missing parameter 'name'"
    assert "connectPoint1" in params, "Missing parameter 'connectPoint1'"

def test_domainmodel_businessfeature_has_connectEnd():
    assert hasattr(domainmodel_BusinessFeature, "connectEnd")
    descriptor = None
    for klass in domainmodel_BusinessFeature.__mro__:
        if "connectEnd" in klass.__dict__:
            descriptor = klass.__dict__["connectEnd"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_businessfeature_has_name():
    assert hasattr(domainmodel_BusinessFeature, "name")
    descriptor = None
    for klass in domainmodel_BusinessFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_businessfeature_has_connectPoint1():
    assert hasattr(domainmodel_BusinessFeature, "connectPoint1")
    descriptor = None
    for klass in domainmodel_BusinessFeature.__mro__:
        if "connectPoint1" in klass.__dict__:
            descriptor = klass.__dict__["connectPoint1"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_interfacemethodcallparameters_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceMethodCallParameters)


def test_domainmodel_interfacemethodcallparameters_constructor_exists():
    assert callable(domainmodel_InterfaceMethodCallParameters.__init__)


def test_domainmodel_interfacemethodcallparameters_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceMethodCallParameters.__init__)
    params = list(sig.parameters.keys())



def test_setrestcallreceiverparameter_is_not_abstract():
    assert not inspect.isabstract(SetRestCallReceiverParameter)


def test_setrestcallreceiverparameter_constructor_exists():
    assert callable(SetRestCallReceiverParameter.__init__)


def test_setrestcallreceiverparameter_constructor_args():
    sig = inspect.signature(SetRestCallReceiverParameter.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiverreturntypeparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiverReturnTypeParameter)


def test_domainmodel_setrestcallreceiverreturntypeparameter_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiverReturnTypeParameter.__init__)


def test_domainmodel_setrestcallreceiverreturntypeparameter_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiverReturnTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiverurlparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiverURLParameter)


def test_domainmodel_setrestcallreceiverurlparameter_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiverURLParameter.__init__)


def test_domainmodel_setrestcallreceiverurlparameter_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiverURLParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterType" in params, "Missing parameter 'parameterType'"

def test_domainmodel_setrestcallreceiverurlparameter_has_parameterType():
    assert hasattr(domainmodel_SetRestCallReceiverURLParameter, "parameterType")
    descriptor = None
    for klass in domainmodel_SetRestCallReceiverURLParameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)



def test_setactionreceiver_is_not_abstract():
    assert not inspect.isabstract(SetActionReceiver)


def test_setactionreceiver_constructor_exists():
    assert callable(SetActionReceiver.__init__)


def test_setactionreceiver_constructor_args():
    sig = inspect.signature(SetActionReceiver.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiver_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiver)


def test_domainmodel_setrestcallreceiver_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiver.__init__)


def test_domainmodel_setrestcallreceiver_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiver.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiverparameters_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiverParameters)


def test_domainmodel_setrestcallreceiverparameters_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiverParameters.__init__)


def test_domainmodel_setrestcallreceiverparameters_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiverParameters.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiverparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiverParameter)


def test_domainmodel_setrestcallreceiverparameter_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiverParameter.__init__)


def test_domainmodel_setrestcallreceiverparameter_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiverParameter.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setrestcallreceiveridparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetRestCallReceiverIDParameter)


def test_domainmodel_setrestcallreceiveridparameter_constructor_exists():
    assert callable(domainmodel_SetRestCallReceiverIDParameter.__init__)


def test_domainmodel_setrestcallreceiveridparameter_constructor_args():
    sig = inspect.signature(domainmodel_SetRestCallReceiverIDParameter.__init__)
    params = list(sig.parameters.keys())
    assert "parameterType" in params, "Missing parameter 'parameterType'"

def test_domainmodel_setrestcallreceiveridparameter_has_parameterType():
    assert hasattr(domainmodel_SetRestCallReceiverIDParameter, "parameterType")
    descriptor = None
    for klass in domainmodel_SetRestCallReceiverIDParameter.__mro__:
        if "parameterType" in klass.__dict__:
            descriptor = klass.__dict__["parameterType"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_validatorrules_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ValidatorRules)


def test_domainmodel_validatorrules_constructor_exists():
    assert callable(domainmodel_ValidatorRules.__init__)


def test_domainmodel_validatorrules_constructor_args():
    sig = inspect.signature(domainmodel_ValidatorRules.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_validatorrule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ValidatorRule)


def test_domainmodel_validatorrule_constructor_exists():
    assert callable(domainmodel_ValidatorRule.__init__)


def test_domainmodel_validatorrule_constructor_args():
    sig = inspect.signature(domainmodel_ValidatorRule.__init__)
    params = list(sig.parameters.keys())
    assert "stringRule" in params, "Missing parameter 'stringRule'"

def test_domainmodel_validatorrule_has_stringRule():
    assert hasattr(domainmodel_ValidatorRule, "stringRule")
    descriptor = None
    for klass in domainmodel_ValidatorRule.__mro__:
        if "stringRule" in klass.__dict__:
            descriptor = klass.__dict__["stringRule"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_screenfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ScreenFeature)


def test_domainmodel_screenfeature_constructor_exists():
    assert callable(domainmodel_ScreenFeature.__init__)


def test_domainmodel_screenfeature_constructor_args():
    sig = inspect.signature(domainmodel_ScreenFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_screenfeature_has_name():
    assert hasattr(domainmodel_ScreenFeature, "name")
    descriptor = None
    for klass in domainmodel_ScreenFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_uiactionfeature_is_not_abstract():
    assert not inspect.isabstract(UIActionFeature)


def test_uiactionfeature_constructor_exists():
    assert callable(UIActionFeature.__init__)


def test_uiactionfeature_constructor_args():
    sig = inspect.signature(UIActionFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_executeaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ExecuteAction)


def test_domainmodel_executeaction_constructor_exists():
    assert callable(domainmodel_ExecuteAction.__init__)


def test_domainmodel_executeaction_constructor_args():
    sig = inspect.signature(domainmodel_ExecuteAction.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_interfacemethodcall_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceMethodCall)


def test_domainmodel_interfacemethodcall_constructor_exists():
    assert callable(domainmodel_InterfaceMethodCall.__init__)


def test_domainmodel_interfacemethodcall_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceMethodCall.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_navigatetoaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_NavigateToAction)


def test_domainmodel_navigatetoaction_constructor_exists():
    assert callable(domainmodel_NavigateToAction.__init__)


def test_domainmodel_navigatetoaction_constructor_args():
    sig = inspect.signature(domainmodel_NavigateToAction.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_screenmodelparameters_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ScreenModelParameters)


def test_domainmodel_screenmodelparameters_constructor_exists():
    assert callable(domainmodel_ScreenModelParameters.__init__)


def test_domainmodel_screenmodelparameters_constructor_args():
    sig = inspect.signature(domainmodel_ScreenModelParameters.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_screenmodelparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ScreenModelParameter)


def test_domainmodel_screenmodelparameter_constructor_exists():
    assert callable(domainmodel_ScreenModelParameter.__init__)


def test_domainmodel_screenmodelparameter_constructor_args():
    sig = inspect.signature(domainmodel_ScreenModelParameter.__init__)
    params = list(sig.parameters.keys())
    assert "modelFeatureValue" in params, "Missing parameter 'modelFeatureValue'"

def test_domainmodel_screenmodelparameter_has_modelFeatureValue():
    assert hasattr(domainmodel_ScreenModelParameter, "modelFeatureValue")
    descriptor = None
    for klass in domainmodel_ScreenModelParameter.__mro__:
        if "modelFeatureValue" in klass.__dict__:
            descriptor = klass.__dict__["modelFeatureValue"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_setuielementreceiver_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetUIElementReceiver)


def test_domainmodel_setuielementreceiver_constructor_exists():
    assert callable(domainmodel_SetUIElementReceiver.__init__)


def test_domainmodel_setuielementreceiver_constructor_args():
    sig = inspect.signature(domainmodel_SetUIElementReceiver.__init__)
    params = list(sig.parameters.keys())
    assert "uiKey" in params, "Missing parameter 'uiKey'"

def test_domainmodel_setuielementreceiver_has_uiKey():
    assert hasattr(domainmodel_SetUIElementReceiver, "uiKey")
    descriptor = None
    for klass in domainmodel_SetUIElementReceiver.__mro__:
        if "uiKey" in klass.__dict__:
            descriptor = klass.__dict__["uiKey"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_validatorfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ValidatorFeature)


def test_domainmodel_validatorfeature_constructor_exists():
    assert callable(domainmodel_ValidatorFeature.__init__)


def test_domainmodel_validatorfeature_constructor_args():
    sig = inspect.signature(domainmodel_ValidatorFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_validatorfeature_has_name():
    assert hasattr(domainmodel_ValidatorFeature, "name")
    descriptor = None
    for klass in domainmodel_ValidatorFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_initactionfeature_is_not_abstract():
    assert not inspect.isabstract(InitActionFeature)


def test_initactionfeature_constructor_exists():
    assert callable(InitActionFeature.__init__)


def test_initactionfeature_constructor_args():
    sig = inspect.signature(InitActionFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_attachaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_AttachAction)


def test_domainmodel_attachaction_constructor_exists():
    assert callable(domainmodel_AttachAction.__init__)


def test_domainmodel_attachaction_constructor_args():
    sig = inspect.signature(domainmodel_AttachAction.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_setaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_SetAction)


def test_domainmodel_setaction_constructor_exists():
    assert callable(domainmodel_SetAction.__init__)


def test_domainmodel_setaction_constructor_args():
    sig = inspect.signature(domainmodel_SetAction.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_validateaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ValidateAction)


def test_domainmodel_validateaction_constructor_exists():
    assert callable(domainmodel_ValidateAction.__init__)


def test_domainmodel_validateaction_constructor_args():
    sig = inspect.signature(domainmodel_ValidateAction.__init__)
    params = list(sig.parameters.keys())



def test_controllerelement_is_not_abstract():
    assert not inspect.isabstract(ControllerElement)


def test_controllerelement_constructor_exists():
    assert callable(ControllerElement.__init__)


def test_controllerelement_constructor_args():
    sig = inspect.signature(ControllerElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_uiactionmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_UIActionModule)


def test_domainmodel_uiactionmodule_constructor_exists():
    assert callable(domainmodel_UIActionModule.__init__)


def test_domainmodel_uiactionmodule_constructor_args():
    sig = inspect.signature(domainmodel_UIActionModule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_uiactionmodule_has_name():
    assert hasattr(domainmodel_UIActionModule, "name")
    descriptor = None
    for klass in domainmodel_UIActionModule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_validatormodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ValidatorModule)


def test_domainmodel_validatormodule_constructor_exists():
    assert callable(domainmodel_ValidatorModule.__init__)


def test_domainmodel_validatormodule_constructor_args():
    sig = inspect.signature(domainmodel_ValidatorModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_initactionmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InitActionModule)


def test_domainmodel_initactionmodule_constructor_exists():
    assert callable(domainmodel_InitActionModule.__init__)


def test_domainmodel_initactionmodule_constructor_args():
    sig = inspect.signature(domainmodel_InitActionModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_initactionfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InitActionFeature)


def test_domainmodel_initactionfeature_constructor_exists():
    assert callable(domainmodel_InitActionFeature.__init__)


def test_domainmodel_initactionfeature_constructor_args():
    sig = inspect.signature(domainmodel_InitActionFeature.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_bindaction_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BindAction)


def test_domainmodel_bindaction_constructor_exists():
    assert callable(domainmodel_BindAction.__init__)


def test_domainmodel_bindaction_constructor_args():
    sig = inspect.signature(domainmodel_BindAction.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_domainmodel_bindaction_has_attribute():
    assert hasattr(domainmodel_BindAction, "attribute")
    descriptor = None
    for klass in domainmodel_BindAction.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_bindsource_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BindSource)


def test_domainmodel_bindsource_constructor_exists():
    assert callable(domainmodel_BindSource.__init__)


def test_domainmodel_bindsource_constructor_args():
    sig = inspect.signature(domainmodel_BindSource.__init__)
    params = list(sig.parameters.keys())



def test_bindsource_is_not_abstract():
    assert not inspect.isabstract(BindSource)


def test_bindsource_constructor_exists():
    assert callable(BindSource.__init__)


def test_bindsource_constructor_args():
    sig = inspect.signature(BindSource.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_bindenumsource_is_not_abstract():
    assert not inspect.isabstract(domainmodel_BindEnumSource)


def test_domainmodel_bindenumsource_constructor_exists():
    assert callable(domainmodel_BindEnumSource.__init__)


def test_domainmodel_bindenumsource_constructor_args():
    sig = inspect.signature(domainmodel_BindEnumSource.__init__)
    params = list(sig.parameters.keys())
    assert "enumType" in params, "Missing parameter 'enumType'"

def test_domainmodel_bindenumsource_has_enumType():
    assert hasattr(domainmodel_BindEnumSource, "enumType")
    descriptor = None
    for klass in domainmodel_BindEnumSource.__mro__:
        if "enumType" in klass.__dict__:
            descriptor = klass.__dict__["enumType"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_elementfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ElementFeature)


def test_domainmodel_elementfeature_constructor_exists():
    assert callable(domainmodel_ElementFeature.__init__)


def test_domainmodel_elementfeature_constructor_args():
    sig = inspect.signature(domainmodel_ElementFeature.__init__)
    params = list(sig.parameters.keys())
    assert "propertyName" in params, "Missing parameter 'propertyName'"
    assert "propertyValue" in params, "Missing parameter 'propertyValue'"

def test_domainmodel_elementfeature_has_propertyName():
    assert hasattr(domainmodel_ElementFeature, "propertyName")
    descriptor = None
    for klass in domainmodel_ElementFeature.__mro__:
        if "propertyName" in klass.__dict__:
            descriptor = klass.__dict__["propertyName"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_elementfeature_has_propertyValue():
    assert hasattr(domainmodel_ElementFeature, "propertyValue")
    descriptor = None
    for klass in domainmodel_ElementFeature.__mro__:
        if "propertyValue" in klass.__dict__:
            descriptor = klass.__dict__["propertyValue"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_viewelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ViewElement)


def test_domainmodel_viewelement_constructor_exists():
    assert callable(domainmodel_ViewElement.__init__)


def test_domainmodel_viewelement_constructor_args():
    sig = inspect.signature(domainmodel_ViewElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_viewelement_has_name():
    assert hasattr(domainmodel_ViewElement, "name")
    descriptor = None
    for klass in domainmodel_ViewElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewelement_is_not_abstract():
    assert not inspect.isabstract(ViewElement)


def test_viewelement_constructor_exists():
    assert callable(ViewElement.__init__)


def test_viewelement_constructor_args():
    sig = inspect.signature(ViewElement.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_containerelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ContainerElement)


def test_domainmodel_containerelement_constructor_exists():
    assert callable(domainmodel_ContainerElement.__init__)


def test_domainmodel_containerelement_constructor_args():
    sig = inspect.signature(domainmodel_ContainerElement.__init__)
    params = list(sig.parameters.keys())
    assert "container" in params, "Missing parameter 'container'"

def test_domainmodel_containerelement_has_container():
    assert hasattr(domainmodel_ContainerElement, "container")
    descriptor = None
    for klass in domainmodel_ContainerElement.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_contentelement_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ContentElement)


def test_domainmodel_contentelement_constructor_exists():
    assert callable(domainmodel_ContentElement.__init__)


def test_domainmodel_contentelement_constructor_args():
    sig = inspect.signature(domainmodel_ContentElement.__init__)
    params = list(sig.parameters.keys())
    assert "contentElement" in params, "Missing parameter 'contentElement'"

def test_domainmodel_contentelement_has_contentElement():
    assert hasattr(domainmodel_ContentElement, "contentElement")
    descriptor = None
    for klass in domainmodel_ContentElement.__mro__:
        if "contentElement" in klass.__dict__:
            descriptor = klass.__dict__["contentElement"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_interfaceoperationusagerule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceOperationUsageRule)


def test_domainmodel_interfaceoperationusagerule_constructor_exists():
    assert callable(domainmodel_InterfaceOperationUsageRule.__init__)


def test_domainmodel_interfaceoperationusagerule_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceOperationUsageRule.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_interfaceoperationusagerule_has_name():
    assert hasattr(domainmodel_InterfaceOperationUsageRule, "name")
    descriptor = None
    for klass in domainmodel_InterfaceOperationUsageRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_businessfeaturetype_is_not_abstract():
    assert not inspect.isabstract(BusinessFeatureType)


def test_businessfeaturetype_constructor_exists():
    assert callable(BusinessFeatureType.__init__)


def test_businessfeaturetype_constructor_args():
    sig = inspect.signature(BusinessFeatureType.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_interfacedeclaration_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceDeclaration)


def test_domainmodel_interfacedeclaration_constructor_exists():
    assert callable(domainmodel_InterfaceDeclaration.__init__)


def test_domainmodel_interfacedeclaration_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_interfacedeclaration_has_name():
    assert hasattr(domainmodel_InterfaceDeclaration, "name")
    descriptor = None
    for klass in domainmodel_InterfaceDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_interfaceoperation_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceOperation)


def test_domainmodel_interfaceoperation_constructor_exists():
    assert callable(domainmodel_InterfaceOperation.__init__)


def test_domainmodel_interfaceoperation_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "restOperation" in params, "Missing parameter 'restOperation'"

def test_domainmodel_interfaceoperation_has_restOperation():
    assert hasattr(domainmodel_InterfaceOperation, "restOperation")
    descriptor = None
    for klass in domainmodel_InterfaceOperation.__mro__:
        if "restOperation" in klass.__dict__:
            descriptor = klass.__dict__["restOperation"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_methodcall_is_not_abstract():
    assert not inspect.isabstract(domainmodel_MethodCall)


def test_domainmodel_methodcall_constructor_exists():
    assert callable(domainmodel_MethodCall.__init__)


def test_domainmodel_methodcall_constructor_args():
    sig = inspect.signature(domainmodel_MethodCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_methodcall_has_name():
    assert hasattr(domainmodel_MethodCall, "name")
    descriptor = None
    for klass in domainmodel_MethodCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_methodparameters_is_not_abstract():
    assert not inspect.isabstract(domainmodel_MethodParameters)


def test_domainmodel_methodparameters_constructor_exists():
    assert callable(domainmodel_MethodParameters.__init__)


def test_domainmodel_methodparameters_constructor_args():
    sig = inspect.signature(domainmodel_MethodParameters.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_methodparameter_is_not_abstract():
    assert not inspect.isabstract(domainmodel_MethodParameter)


def test_domainmodel_methodparameter_constructor_exists():
    assert callable(domainmodel_MethodParameter.__init__)


def test_domainmodel_methodparameter_constructor_args():
    sig = inspect.signature(domainmodel_MethodParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_methodparameter_has_name():
    assert hasattr(domainmodel_MethodParameter, "name")
    descriptor = None
    for klass in domainmodel_MethodParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_domainentity_is_not_abstract():
    assert not inspect.isabstract(domainmodel_DomainEntity)


def test_domainmodel_domainentity_constructor_exists():
    assert callable(domainmodel_DomainEntity.__init__)


def test_domainmodel_domainentity_constructor_args():
    sig = inspect.signature(domainmodel_DomainEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_domainentity_has_name():
    assert hasattr(domainmodel_DomainEntity, "name")
    descriptor = None
    for klass in domainmodel_DomainEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_modelfeature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ModelFeature)


def test_domainmodel_modelfeature_constructor_exists():
    assert callable(domainmodel_ModelFeature.__init__)


def test_domainmodel_modelfeature_constructor_args():
    sig = inspect.signature(domainmodel_ModelFeature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_modelfeature_has_name():
    assert hasattr(domainmodel_ModelFeature, "name")
    descriptor = None
    for klass in domainmodel_ModelFeature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_screenmodule_is_not_abstract():
    assert not inspect.isabstract(ScreenModule)


def test_screenmodule_constructor_exists():
    assert callable(ScreenModule.__init__)


def test_screenmodule_constructor_args():
    sig = inspect.signature(ScreenModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_viewmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ViewModule)


def test_domainmodel_viewmodule_constructor_exists():
    assert callable(domainmodel_ViewModule.__init__)


def test_domainmodel_viewmodule_constructor_args():
    sig = inspect.signature(domainmodel_ViewModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_controllermodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ControllerModule)


def test_domainmodel_controllermodule_constructor_exists():
    assert callable(domainmodel_ControllerModule.__init__)


def test_domainmodel_controllermodule_constructor_args():
    sig = inspect.signature(domainmodel_ControllerModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_modelmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_ModelModule)


def test_domainmodel_modelmodule_constructor_exists():
    assert callable(domainmodel_ModelModule.__init__)


def test_domainmodel_modelmodule_constructor_args():
    sig = inspect.signature(domainmodel_ModelModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_entryparametersmodule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_EntryParametersModule)


def test_domainmodel_entryparametersmodule_constructor_exists():
    assert callable(domainmodel_EntryParametersModule.__init__)


def test_domainmodel_entryparametersmodule_constructor_args():
    sig = inspect.signature(domainmodel_EntryParametersModule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_domainrepository_is_not_abstract():
    assert not inspect.isabstract(domainmodel_DomainRepository)


def test_domainmodel_domainrepository_constructor_exists():
    assert callable(domainmodel_DomainRepository.__init__)


def test_domainmodel_domainrepository_constructor_args():
    sig = inspect.signature(domainmodel_DomainRepository.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_domainrepository_has_name():
    assert hasattr(domainmodel_DomainRepository, "name")
    descriptor = None
    for klass in domainmodel_DomainRepository.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_statelesscomponent_is_not_abstract():
    assert not inspect.isabstract(domainmodel_StatelessComponent)


def test_domainmodel_statelesscomponent_constructor_exists():
    assert callable(domainmodel_StatelessComponent.__init__)


def test_domainmodel_statelesscomponent_constructor_args():
    sig = inspect.signature(domainmodel_StatelessComponent.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_statelesscomponent_has_name():
    assert hasattr(domainmodel_StatelessComponent, "name")
    descriptor = None
    for klass in domainmodel_StatelessComponent.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domainmodel_interfaceoperationsusagerule_is_not_abstract():
    assert not inspect.isabstract(domainmodel_InterfaceOperationsUsageRule)


def test_domainmodel_interfaceoperationsusagerule_constructor_exists():
    assert callable(domainmodel_InterfaceOperationsUsageRule.__init__)


def test_domainmodel_interfaceoperationsusagerule_constructor_args():
    sig = inspect.signature(domainmodel_InterfaceOperationsUsageRule.__init__)
    params = list(sig.parameters.keys())



def test_domainmodel_feature_is_not_abstract():
    assert not inspect.isabstract(domainmodel_Feature)


def test_domainmodel_feature_constructor_exists():
    assert callable(domainmodel_Feature.__init__)


def test_domainmodel_feature_constructor_args():
    sig = inspect.signature(domainmodel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "mapName" in params, "Missing parameter 'mapName'"
    assert "mappingOption" in params, "Missing parameter 'mappingOption'"
    assert "name" in params, "Missing parameter 'name'"

def test_domainmodel_feature_has_mapName():
    assert hasattr(domainmodel_Feature, "mapName")
    descriptor = None
    for klass in domainmodel_Feature.__mro__:
        if "mapName" in klass.__dict__:
            descriptor = klass.__dict__["mapName"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_feature_has_mappingOption():
    assert hasattr(domainmodel_Feature, "mappingOption")
    descriptor = None
    for klass in domainmodel_Feature.__mro__:
        if "mappingOption" in klass.__dict__:
            descriptor = klass.__dict__["mappingOption"]
            break
    assert isinstance(descriptor, property)

def test_domainmodel_feature_has_name():
    assert hasattr(domainmodel_Feature, "name")
    descriptor = None
    for klass in domainmodel_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_propertynameliteral_exists():
    # Check that the Enumeration exists
    assert PropertyNameLiteral is not None

def test_propertynameliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PropertyNameLiteral]
    expected_literals = [
        "COLUMNS",
        "CSS_ITEM",
        "LABEL_PROVIDER",
        "STYLE",
        "TYPE",
        "RESOURCE_KEY",
        "TOOLTIP",
        "PATH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PropertyNameLiteral"

def test_uielementreceiverkey_exists():
    # Check that the Enumeration exists
    assert UIElementReceiverKey is not None

def test_uielementreceiverkey_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in UIElementReceiverKey]
    expected_literals = [
        "TEXT",
        "VALUES_",
        "ON_SELECTION",
        "SELECTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in UIElementReceiverKey"

def test_contentelementliteral_exists():
    # Check that the Enumeration exists
    assert ContentElementLiteral is not None

def test_contentelementliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContentElementLiteral]
    expected_literals = [
        "BUTTON",
        "IMAGE",
        "LABEL",
        "LIST",
        "TEXT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContentElementLiteral"

def test_containerelementliteral_exists():
    # Check that the Enumeration exists
    assert ContainerElementLiteral is not None

def test_containerelementliteral_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainerElementLiteral]
    expected_literals = [
        "LAYOUT",
        "SCREEN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainerElementLiteral"


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
domainmodel_SystemModule_strategy = st.builds(
    domainmodel_SystemModule,
)
BusinessModule_strategy = st.builds(
    BusinessModule,
)
domainmodel_BusinessFeatures_strategy = st.builds(
    domainmodel_BusinessFeatures,
)
domainmodel_MainFeatureOption_strategy = st.builds(
    domainmodel_MainFeatureOption,
    name=
        safe_text
)
UIFeature_strategy = st.builds(
    UIFeature,
)
domainmodel_MainFeature_strategy = st.builds(
    domainmodel_MainFeature,
)
domainmodel_ScreenModule_strategy = st.builds(
    domainmodel_ScreenModule,
)
domainmodel_ControllerElement_strategy = st.builds(
    domainmodel_ControllerElement,
)
domainmodel_BusinessFeatureType_strategy = st.builds(
    domainmodel_BusinessFeatureType,
)
SystemModule_strategy = st.builds(
    SystemModule,
)
domainmodel_BusinessModule_strategy = st.builds(
    domainmodel_BusinessModule,
)
domainmodel_UIModule_strategy = st.builds(
    domainmodel_UIModule,
)
domainmodel_UIFeature_strategy = st.builds(
    domainmodel_UIFeature,
)
domainmodel_InterfaceMethodCallParameter_strategy = st.builds(
    domainmodel_InterfaceMethodCallParameter,
    parameterType=
        safe_text
)
domainmodel_AbstractNamespaceElement_strategy = st.builds(
    domainmodel_AbstractNamespaceElement,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
domainmodel_SystemDefinition_strategy = st.builds(
    domainmodel_SystemDefinition,
)
domainmodel_NamespaceDeclaration_strategy = st.builds(
    domainmodel_NamespaceDeclaration,
)
Type_strategy = st.builds(
    Type,
)
AbstractNamespaceElement_strategy = st.builds(
    AbstractNamespaceElement,
)
domainmodel_DataType_strategy = st.builds(
    domainmodel_DataType,
    mappedType=
        safe_text,
    name=
        safe_text,
    initValue=
        safe_text
)
domainmodel_Import_strategy = st.builds(
    domainmodel_Import,
    importedNamespace=
        safe_text
)
domainmodel_Type_strategy = st.builds(
    domainmodel_Type,
)
domainmodel_AbstractElement_strategy = st.builds(
    domainmodel_AbstractElement,
    name=
        safe_text
)
domainmodel_Domainmodel_strategy = st.builds(
    domainmodel_Domainmodel,
)
domainmodel_SetActionReceiver_strategy = st.builds(
    domainmodel_SetActionReceiver,
)
domainmodel_UIActionFeature_strategy = st.builds(
    domainmodel_UIActionFeature,
)
domainmodel_BusinessFeature_strategy = st.builds(
    domainmodel_BusinessFeature,
    connectEnd=
        safe_text,
    name=
        safe_text,
    connectPoint1=
        safe_text
)
domainmodel_InterfaceMethodCallParameters_strategy = st.builds(
    domainmodel_InterfaceMethodCallParameters,
)
SetRestCallReceiverParameter_strategy = st.builds(
    SetRestCallReceiverParameter,
)
domainmodel_SetRestCallReceiverReturnTypeParameter_strategy = st.builds(
    domainmodel_SetRestCallReceiverReturnTypeParameter,
)
domainmodel_SetRestCallReceiverURLParameter_strategy = st.builds(
    domainmodel_SetRestCallReceiverURLParameter,
    parameterType=
        safe_text
)
SetActionReceiver_strategy = st.builds(
    SetActionReceiver,
)
domainmodel_SetRestCallReceiver_strategy = st.builds(
    domainmodel_SetRestCallReceiver,
)
domainmodel_SetRestCallReceiverParameters_strategy = st.builds(
    domainmodel_SetRestCallReceiverParameters,
)
domainmodel_SetRestCallReceiverParameter_strategy = st.builds(
    domainmodel_SetRestCallReceiverParameter,
)
domainmodel_SetRestCallReceiverIDParameter_strategy = st.builds(
    domainmodel_SetRestCallReceiverIDParameter,
    parameterType=
        safe_text
)
domainmodel_ValidatorRules_strategy = st.builds(
    domainmodel_ValidatorRules,
)
domainmodel_ValidatorRule_strategy = st.builds(
    domainmodel_ValidatorRule,
    stringRule=
        safe_text
)
domainmodel_ScreenFeature_strategy = st.builds(
    domainmodel_ScreenFeature,
    name=
        safe_text
)
UIActionFeature_strategy = st.builds(
    UIActionFeature,
)
domainmodel_ExecuteAction_strategy = st.builds(
    domainmodel_ExecuteAction,
)
domainmodel_InterfaceMethodCall_strategy = st.builds(
    domainmodel_InterfaceMethodCall,
)
domainmodel_NavigateToAction_strategy = st.builds(
    domainmodel_NavigateToAction,
)
domainmodel_ScreenModelParameters_strategy = st.builds(
    domainmodel_ScreenModelParameters,
)
domainmodel_ScreenModelParameter_strategy = st.builds(
    domainmodel_ScreenModelParameter,
    modelFeatureValue=
        safe_text
)
domainmodel_SetUIElementReceiver_strategy = st.builds(
    domainmodel_SetUIElementReceiver,
    uiKey=
        safe_text
)
domainmodel_ValidatorFeature_strategy = st.builds(
    domainmodel_ValidatorFeature,
    name=
        safe_text
)
InitActionFeature_strategy = st.builds(
    InitActionFeature,
)
domainmodel_AttachAction_strategy = st.builds(
    domainmodel_AttachAction,
)
domainmodel_SetAction_strategy = st.builds(
    domainmodel_SetAction,
)
domainmodel_ValidateAction_strategy = st.builds(
    domainmodel_ValidateAction,
)
ControllerElement_strategy = st.builds(
    ControllerElement,
)
domainmodel_UIActionModule_strategy = st.builds(
    domainmodel_UIActionModule,
    name=
        safe_text
)
domainmodel_ValidatorModule_strategy = st.builds(
    domainmodel_ValidatorModule,
)
domainmodel_InitActionModule_strategy = st.builds(
    domainmodel_InitActionModule,
)
domainmodel_InitActionFeature_strategy = st.builds(
    domainmodel_InitActionFeature,
)
domainmodel_BindAction_strategy = st.builds(
    domainmodel_BindAction,
    attribute=
        safe_text
)
domainmodel_BindSource_strategy = st.builds(
    domainmodel_BindSource,
)
BindSource_strategy = st.builds(
    BindSource,
)
domainmodel_BindEnumSource_strategy = st.builds(
    domainmodel_BindEnumSource,
    enumType=
        safe_text
)
domainmodel_ElementFeature_strategy = st.builds(
    domainmodel_ElementFeature,
    propertyName=
        safe_text,
    propertyValue=
        safe_text
)
domainmodel_ViewElement_strategy = st.builds(
    domainmodel_ViewElement,
    name=
        safe_text
)
ViewElement_strategy = st.builds(
    ViewElement,
)
domainmodel_ContainerElement_strategy = st.builds(
    domainmodel_ContainerElement,
    container=
        safe_text
)
domainmodel_ContentElement_strategy = st.builds(
    domainmodel_ContentElement,
    contentElement=
        safe_text
)
domainmodel_InterfaceOperationUsageRule_strategy = st.builds(
    domainmodel_InterfaceOperationUsageRule,
    name=
        safe_text
)
BusinessFeatureType_strategy = st.builds(
    BusinessFeatureType,
)
domainmodel_InterfaceDeclaration_strategy = st.builds(
    domainmodel_InterfaceDeclaration,
    name=
        safe_text
)
domainmodel_InterfaceOperation_strategy = st.builds(
    domainmodel_InterfaceOperation,
    restOperation=
        safe_text
)
domainmodel_MethodCall_strategy = st.builds(
    domainmodel_MethodCall,
    name=
        safe_text
)
domainmodel_MethodParameters_strategy = st.builds(
    domainmodel_MethodParameters,
)
domainmodel_MethodParameter_strategy = st.builds(
    domainmodel_MethodParameter,
    name=
        safe_text
)
domainmodel_DomainEntity_strategy = st.builds(
    domainmodel_DomainEntity,
    name=
        safe_text
)
domainmodel_ModelFeature_strategy = st.builds(
    domainmodel_ModelFeature,
    name=
        safe_text
)
ScreenModule_strategy = st.builds(
    ScreenModule,
)
domainmodel_ViewModule_strategy = st.builds(
    domainmodel_ViewModule,
)
domainmodel_ControllerModule_strategy = st.builds(
    domainmodel_ControllerModule,
)
domainmodel_ModelModule_strategy = st.builds(
    domainmodel_ModelModule,
)
domainmodel_EntryParametersModule_strategy = st.builds(
    domainmodel_EntryParametersModule,
)
domainmodel_DomainRepository_strategy = st.builds(
    domainmodel_DomainRepository,
    name=
        safe_text
)
domainmodel_StatelessComponent_strategy = st.builds(
    domainmodel_StatelessComponent,
    name=
        safe_text
)
domainmodel_InterfaceOperationsUsageRule_strategy = st.builds(
    domainmodel_InterfaceOperationsUsageRule,
)
domainmodel_Feature_strategy = st.builds(
    domainmodel_Feature,
    mapName=
        safe_text,
    mappingOption=
        safe_text,
    name=
        safe_text
)

@given(instance=domainmodel_SystemModule_strategy)
@settings(max_examples=50)
def test_domainmodel_systemmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_SystemModule)

@given(instance=BusinessModule_strategy)
@settings(max_examples=50)
def test_businessmodule_instantiation(instance):
    assert isinstance(instance, BusinessModule)

@given(instance=domainmodel_BusinessFeatures_strategy)
@settings(max_examples=50)
def test_domainmodel_businessfeatures_instantiation(instance):
    assert isinstance(instance, domainmodel_BusinessFeatures)

@given(instance=domainmodel_MainFeatureOption_strategy)
@settings(max_examples=50)
def test_domainmodel_mainfeatureoption_instantiation(instance):
    assert isinstance(instance, domainmodel_MainFeatureOption)



@given(instance=domainmodel_MainFeatureOption_strategy)
def test_domainmodel_mainfeatureoption_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UIFeature_strategy)
@settings(max_examples=50)
def test_uifeature_instantiation(instance):
    assert isinstance(instance, UIFeature)

@given(instance=domainmodel_MainFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_mainfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_MainFeature)

@given(instance=domainmodel_ScreenModule_strategy)
@settings(max_examples=50)
def test_domainmodel_screenmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_ScreenModule)

@given(instance=domainmodel_ControllerElement_strategy)
@settings(max_examples=50)
def test_domainmodel_controllerelement_instantiation(instance):
    assert isinstance(instance, domainmodel_ControllerElement)

@given(instance=domainmodel_BusinessFeatureType_strategy)
@settings(max_examples=50)
def test_domainmodel_businessfeaturetype_instantiation(instance):
    assert isinstance(instance, domainmodel_BusinessFeatureType)

@given(instance=SystemModule_strategy)
@settings(max_examples=50)
def test_systemmodule_instantiation(instance):
    assert isinstance(instance, SystemModule)

@given(instance=domainmodel_BusinessModule_strategy)
@settings(max_examples=50)
def test_domainmodel_businessmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_BusinessModule)

@given(instance=domainmodel_UIModule_strategy)
@settings(max_examples=50)
def test_domainmodel_uimodule_instantiation(instance):
    assert isinstance(instance, domainmodel_UIModule)

@given(instance=domainmodel_UIFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_uifeature_instantiation(instance):
    assert isinstance(instance, domainmodel_UIFeature)

@given(instance=domainmodel_InterfaceMethodCallParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_interfacemethodcallparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceMethodCallParameter)



@given(instance=domainmodel_InterfaceMethodCallParameter_strategy)
def test_domainmodel_interfacemethodcallparameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=domainmodel_AbstractNamespaceElement_strategy)
@settings(max_examples=50)
def test_domainmodel_abstractnamespaceelement_instantiation(instance):
    assert isinstance(instance, domainmodel_AbstractNamespaceElement)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=domainmodel_SystemDefinition_strategy)
@settings(max_examples=50)
def test_domainmodel_systemdefinition_instantiation(instance):
    assert isinstance(instance, domainmodel_SystemDefinition)

@given(instance=domainmodel_NamespaceDeclaration_strategy)
@settings(max_examples=50)
def test_domainmodel_namespacedeclaration_instantiation(instance):
    assert isinstance(instance, domainmodel_NamespaceDeclaration)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=AbstractNamespaceElement_strategy)
@settings(max_examples=50)
def test_abstractnamespaceelement_instantiation(instance):
    assert isinstance(instance, AbstractNamespaceElement)

@given(instance=domainmodel_DataType_strategy)
@settings(max_examples=50)
def test_domainmodel_datatype_instantiation(instance):
    assert isinstance(instance, domainmodel_DataType)



@given(instance=domainmodel_DataType_strategy)
def test_domainmodel_datatype_mappedType_setter(instance):
    original = instance.mappedType
    instance.mappedType = original
    assert instance.mappedType == original



@given(instance=domainmodel_DataType_strategy)
def test_domainmodel_datatype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domainmodel_DataType_strategy)
def test_domainmodel_datatype_initValue_setter(instance):
    original = instance.initValue
    instance.initValue = original
    assert instance.initValue == original

@given(instance=domainmodel_Import_strategy)
@settings(max_examples=50)
def test_domainmodel_import_instantiation(instance):
    assert isinstance(instance, domainmodel_Import)



@given(instance=domainmodel_Import_strategy)
def test_domainmodel_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=domainmodel_Type_strategy)
@settings(max_examples=50)
def test_domainmodel_type_instantiation(instance):
    assert isinstance(instance, domainmodel_Type)

@given(instance=domainmodel_AbstractElement_strategy)
@settings(max_examples=50)
def test_domainmodel_abstractelement_instantiation(instance):
    assert isinstance(instance, domainmodel_AbstractElement)



@given(instance=domainmodel_AbstractElement_strategy)
def test_domainmodel_abstractelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_Domainmodel_strategy)
@settings(max_examples=50)
def test_domainmodel_domainmodel_instantiation(instance):
    assert isinstance(instance, domainmodel_Domainmodel)

@given(instance=domainmodel_SetActionReceiver_strategy)
@settings(max_examples=50)
def test_domainmodel_setactionreceiver_instantiation(instance):
    assert isinstance(instance, domainmodel_SetActionReceiver)

@given(instance=domainmodel_UIActionFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_uiactionfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_UIActionFeature)

@given(instance=domainmodel_BusinessFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_businessfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_BusinessFeature)



@given(instance=domainmodel_BusinessFeature_strategy)
def test_domainmodel_businessfeature_connectEnd_setter(instance):
    original = instance.connectEnd
    instance.connectEnd = original
    assert instance.connectEnd == original



@given(instance=domainmodel_BusinessFeature_strategy)
def test_domainmodel_businessfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=domainmodel_BusinessFeature_strategy)
def test_domainmodel_businessfeature_connectPoint1_setter(instance):
    original = instance.connectPoint1
    instance.connectPoint1 = original
    assert instance.connectPoint1 == original

@given(instance=domainmodel_InterfaceMethodCallParameters_strategy)
@settings(max_examples=50)
def test_domainmodel_interfacemethodcallparameters_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceMethodCallParameters)

@given(instance=SetRestCallReceiverParameter_strategy)
@settings(max_examples=50)
def test_setrestcallreceiverparameter_instantiation(instance):
    assert isinstance(instance, SetRestCallReceiverParameter)

@given(instance=domainmodel_SetRestCallReceiverReturnTypeParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiverreturntypeparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiverReturnTypeParameter)

@given(instance=domainmodel_SetRestCallReceiverURLParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiverurlparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiverURLParameter)



@given(instance=domainmodel_SetRestCallReceiverURLParameter_strategy)
def test_domainmodel_setrestcallreceiverurlparameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=SetActionReceiver_strategy)
@settings(max_examples=50)
def test_setactionreceiver_instantiation(instance):
    assert isinstance(instance, SetActionReceiver)

@given(instance=domainmodel_SetRestCallReceiver_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiver_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiver)

@given(instance=domainmodel_SetRestCallReceiverParameters_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiverparameters_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiverParameters)

@given(instance=domainmodel_SetRestCallReceiverParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiverparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiverParameter)

@given(instance=domainmodel_SetRestCallReceiverIDParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_setrestcallreceiveridparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_SetRestCallReceiverIDParameter)



@given(instance=domainmodel_SetRestCallReceiverIDParameter_strategy)
def test_domainmodel_setrestcallreceiveridparameter_parameterType_setter(instance):
    original = instance.parameterType
    instance.parameterType = original
    assert instance.parameterType == original

@given(instance=domainmodel_ValidatorRules_strategy)
@settings(max_examples=50)
def test_domainmodel_validatorrules_instantiation(instance):
    assert isinstance(instance, domainmodel_ValidatorRules)

@given(instance=domainmodel_ValidatorRule_strategy)
@settings(max_examples=50)
def test_domainmodel_validatorrule_instantiation(instance):
    assert isinstance(instance, domainmodel_ValidatorRule)



@given(instance=domainmodel_ValidatorRule_strategy)
def test_domainmodel_validatorrule_stringRule_setter(instance):
    original = instance.stringRule
    instance.stringRule = original
    assert instance.stringRule == original

@given(instance=domainmodel_ScreenFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_screenfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_ScreenFeature)



@given(instance=domainmodel_ScreenFeature_strategy)
def test_domainmodel_screenfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UIActionFeature_strategy)
@settings(max_examples=50)
def test_uiactionfeature_instantiation(instance):
    assert isinstance(instance, UIActionFeature)

@given(instance=domainmodel_ExecuteAction_strategy)
@settings(max_examples=50)
def test_domainmodel_executeaction_instantiation(instance):
    assert isinstance(instance, domainmodel_ExecuteAction)

@given(instance=domainmodel_InterfaceMethodCall_strategy)
@settings(max_examples=50)
def test_domainmodel_interfacemethodcall_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceMethodCall)

@given(instance=domainmodel_NavigateToAction_strategy)
@settings(max_examples=50)
def test_domainmodel_navigatetoaction_instantiation(instance):
    assert isinstance(instance, domainmodel_NavigateToAction)

@given(instance=domainmodel_ScreenModelParameters_strategy)
@settings(max_examples=50)
def test_domainmodel_screenmodelparameters_instantiation(instance):
    assert isinstance(instance, domainmodel_ScreenModelParameters)

@given(instance=domainmodel_ScreenModelParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_screenmodelparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_ScreenModelParameter)



@given(instance=domainmodel_ScreenModelParameter_strategy)
def test_domainmodel_screenmodelparameter_modelFeatureValue_setter(instance):
    original = instance.modelFeatureValue
    instance.modelFeatureValue = original
    assert instance.modelFeatureValue == original

@given(instance=domainmodel_SetUIElementReceiver_strategy)
@settings(max_examples=50)
def test_domainmodel_setuielementreceiver_instantiation(instance):
    assert isinstance(instance, domainmodel_SetUIElementReceiver)



@given(instance=domainmodel_SetUIElementReceiver_strategy)
def test_domainmodel_setuielementreceiver_uiKey_setter(instance):
    original = instance.uiKey
    instance.uiKey = original
    assert instance.uiKey == original

@given(instance=domainmodel_ValidatorFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_validatorfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_ValidatorFeature)



@given(instance=domainmodel_ValidatorFeature_strategy)
def test_domainmodel_validatorfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=InitActionFeature_strategy)
@settings(max_examples=50)
def test_initactionfeature_instantiation(instance):
    assert isinstance(instance, InitActionFeature)

@given(instance=domainmodel_AttachAction_strategy)
@settings(max_examples=50)
def test_domainmodel_attachaction_instantiation(instance):
    assert isinstance(instance, domainmodel_AttachAction)

@given(instance=domainmodel_SetAction_strategy)
@settings(max_examples=50)
def test_domainmodel_setaction_instantiation(instance):
    assert isinstance(instance, domainmodel_SetAction)

@given(instance=domainmodel_ValidateAction_strategy)
@settings(max_examples=50)
def test_domainmodel_validateaction_instantiation(instance):
    assert isinstance(instance, domainmodel_ValidateAction)

@given(instance=ControllerElement_strategy)
@settings(max_examples=50)
def test_controllerelement_instantiation(instance):
    assert isinstance(instance, ControllerElement)

@given(instance=domainmodel_UIActionModule_strategy)
@settings(max_examples=50)
def test_domainmodel_uiactionmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_UIActionModule)



@given(instance=domainmodel_UIActionModule_strategy)
def test_domainmodel_uiactionmodule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_ValidatorModule_strategy)
@settings(max_examples=50)
def test_domainmodel_validatormodule_instantiation(instance):
    assert isinstance(instance, domainmodel_ValidatorModule)

@given(instance=domainmodel_InitActionModule_strategy)
@settings(max_examples=50)
def test_domainmodel_initactionmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_InitActionModule)

@given(instance=domainmodel_InitActionFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_initactionfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_InitActionFeature)

@given(instance=domainmodel_BindAction_strategy)
@settings(max_examples=50)
def test_domainmodel_bindaction_instantiation(instance):
    assert isinstance(instance, domainmodel_BindAction)



@given(instance=domainmodel_BindAction_strategy)
def test_domainmodel_bindaction_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=domainmodel_BindSource_strategy)
@settings(max_examples=50)
def test_domainmodel_bindsource_instantiation(instance):
    assert isinstance(instance, domainmodel_BindSource)

@given(instance=BindSource_strategy)
@settings(max_examples=50)
def test_bindsource_instantiation(instance):
    assert isinstance(instance, BindSource)

@given(instance=domainmodel_BindEnumSource_strategy)
@settings(max_examples=50)
def test_domainmodel_bindenumsource_instantiation(instance):
    assert isinstance(instance, domainmodel_BindEnumSource)



@given(instance=domainmodel_BindEnumSource_strategy)
def test_domainmodel_bindenumsource_enumType_setter(instance):
    original = instance.enumType
    instance.enumType = original
    assert instance.enumType == original

@given(instance=domainmodel_ElementFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_elementfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_ElementFeature)



@given(instance=domainmodel_ElementFeature_strategy)
def test_domainmodel_elementfeature_propertyName_setter(instance):
    original = instance.propertyName
    instance.propertyName = original
    assert instance.propertyName == original



@given(instance=domainmodel_ElementFeature_strategy)
def test_domainmodel_elementfeature_propertyValue_setter(instance):
    original = instance.propertyValue
    instance.propertyValue = original
    assert instance.propertyValue == original

@given(instance=domainmodel_ViewElement_strategy)
@settings(max_examples=50)
def test_domainmodel_viewelement_instantiation(instance):
    assert isinstance(instance, domainmodel_ViewElement)



@given(instance=domainmodel_ViewElement_strategy)
def test_domainmodel_viewelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ViewElement_strategy)
@settings(max_examples=50)
def test_viewelement_instantiation(instance):
    assert isinstance(instance, ViewElement)

@given(instance=domainmodel_ContainerElement_strategy)
@settings(max_examples=50)
def test_domainmodel_containerelement_instantiation(instance):
    assert isinstance(instance, domainmodel_ContainerElement)



@given(instance=domainmodel_ContainerElement_strategy)
def test_domainmodel_containerelement_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=domainmodel_ContentElement_strategy)
@settings(max_examples=50)
def test_domainmodel_contentelement_instantiation(instance):
    assert isinstance(instance, domainmodel_ContentElement)



@given(instance=domainmodel_ContentElement_strategy)
def test_domainmodel_contentelement_contentElement_setter(instance):
    original = instance.contentElement
    instance.contentElement = original
    assert instance.contentElement == original

@given(instance=domainmodel_InterfaceOperationUsageRule_strategy)
@settings(max_examples=50)
def test_domainmodel_interfaceoperationusagerule_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceOperationUsageRule)



@given(instance=domainmodel_InterfaceOperationUsageRule_strategy)
def test_domainmodel_interfaceoperationusagerule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BusinessFeatureType_strategy)
@settings(max_examples=50)
def test_businessfeaturetype_instantiation(instance):
    assert isinstance(instance, BusinessFeatureType)

@given(instance=domainmodel_InterfaceDeclaration_strategy)
@settings(max_examples=50)
def test_domainmodel_interfacedeclaration_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceDeclaration)



@given(instance=domainmodel_InterfaceDeclaration_strategy)
def test_domainmodel_interfacedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_InterfaceOperation_strategy)
@settings(max_examples=50)
def test_domainmodel_interfaceoperation_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceOperation)



@given(instance=domainmodel_InterfaceOperation_strategy)
def test_domainmodel_interfaceoperation_restOperation_setter(instance):
    original = instance.restOperation
    instance.restOperation = original
    assert instance.restOperation == original

@given(instance=domainmodel_MethodCall_strategy)
@settings(max_examples=50)
def test_domainmodel_methodcall_instantiation(instance):
    assert isinstance(instance, domainmodel_MethodCall)



@given(instance=domainmodel_MethodCall_strategy)
def test_domainmodel_methodcall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_MethodParameters_strategy)
@settings(max_examples=50)
def test_domainmodel_methodparameters_instantiation(instance):
    assert isinstance(instance, domainmodel_MethodParameters)

@given(instance=domainmodel_MethodParameter_strategy)
@settings(max_examples=50)
def test_domainmodel_methodparameter_instantiation(instance):
    assert isinstance(instance, domainmodel_MethodParameter)



@given(instance=domainmodel_MethodParameter_strategy)
def test_domainmodel_methodparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_DomainEntity_strategy)
@settings(max_examples=50)
def test_domainmodel_domainentity_instantiation(instance):
    assert isinstance(instance, domainmodel_DomainEntity)



@given(instance=domainmodel_DomainEntity_strategy)
def test_domainmodel_domainentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_ModelFeature_strategy)
@settings(max_examples=50)
def test_domainmodel_modelfeature_instantiation(instance):
    assert isinstance(instance, domainmodel_ModelFeature)



@given(instance=domainmodel_ModelFeature_strategy)
def test_domainmodel_modelfeature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ScreenModule_strategy)
@settings(max_examples=50)
def test_screenmodule_instantiation(instance):
    assert isinstance(instance, ScreenModule)

@given(instance=domainmodel_ViewModule_strategy)
@settings(max_examples=50)
def test_domainmodel_viewmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_ViewModule)

@given(instance=domainmodel_ControllerModule_strategy)
@settings(max_examples=50)
def test_domainmodel_controllermodule_instantiation(instance):
    assert isinstance(instance, domainmodel_ControllerModule)

@given(instance=domainmodel_ModelModule_strategy)
@settings(max_examples=50)
def test_domainmodel_modelmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_ModelModule)

@given(instance=domainmodel_EntryParametersModule_strategy)
@settings(max_examples=50)
def test_domainmodel_entryparametersmodule_instantiation(instance):
    assert isinstance(instance, domainmodel_EntryParametersModule)

@given(instance=domainmodel_DomainRepository_strategy)
@settings(max_examples=50)
def test_domainmodel_domainrepository_instantiation(instance):
    assert isinstance(instance, domainmodel_DomainRepository)



@given(instance=domainmodel_DomainRepository_strategy)
def test_domainmodel_domainrepository_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_StatelessComponent_strategy)
@settings(max_examples=50)
def test_domainmodel_statelesscomponent_instantiation(instance):
    assert isinstance(instance, domainmodel_StatelessComponent)



@given(instance=domainmodel_StatelessComponent_strategy)
def test_domainmodel_statelesscomponent_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=domainmodel_InterfaceOperationsUsageRule_strategy)
@settings(max_examples=50)
def test_domainmodel_interfaceoperationsusagerule_instantiation(instance):
    assert isinstance(instance, domainmodel_InterfaceOperationsUsageRule)

@given(instance=domainmodel_Feature_strategy)
@settings(max_examples=50)
def test_domainmodel_feature_instantiation(instance):
    assert isinstance(instance, domainmodel_Feature)



@given(instance=domainmodel_Feature_strategy)
def test_domainmodel_feature_mapName_setter(instance):
    original = instance.mapName
    instance.mapName = original
    assert instance.mapName == original



@given(instance=domainmodel_Feature_strategy)
def test_domainmodel_feature_mappingOption_setter(instance):
    original = instance.mappingOption
    instance.mappingOption = original
    assert instance.mappingOption == original



@given(instance=domainmodel_Feature_strategy)
def test_domainmodel_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
