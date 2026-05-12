import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    componentModel_Type,
    DelegationConnector,
    componentModel_RequiredDelegationConnector,
    componentModel_RequiredRole,
    componentModel_ProvidedRole,
    AssemblyViewType,
    componentModel_AssemblyContext,
    componentModel_ViewType,
    componentModel_Signature,
    Action,
    componentModel_InternalAction,
    componentModel_Loop,
    componentModel_ExternalCall,
    componentModel_Branch,
    componentModel_Action,
    componentModel_Service,
    componentModel_DelegationConnector,
    componentModel_AssemblyConnector,
    componentModel_InterfaceServiceMapTuple,
    componentModel_ServiceEffectSpecification,
    componentModel_Interface,
    componentModel_Component,
    ViewType,
    componentModel_Repository,
    ViewPoint,
    componentModel_AssemblyViewPoint,
    componentModel_SystemIndependentViewPoint,
    ParameterTyp,
    componentModel_SimpleParameterType,
    componentModel_ComplexParameterType,
    Type,
    componentModel_Void,
    componentModel_ParameterTyp,
    SimpleParameterType,
    componentModel_Map,
    componentModel_Boolean,
    componentModel_Int,
    componentModel_Float,
    componentModel_List,
    componentModel_Char,
    componentModel_Long,
    componentModel_String,
    componentModel_Parameter,
    componentModel_Double,
    componentModel_Date,
    componentModel_AllocationViewType,
    componentModel_EnvironmentViewType,
    componentModel_RepositoryViewType,
    componentModel_DeploymentViewPoint,
    componentModel_AssemblyViewType,
    Component,
    componentModel_CompositeComponent,
    componentModel_ViewPoint,
    componentModel_ProvidedDelegationConnector,
    componentModel_System,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_componentmodel_type_is_not_abstract():
    assert not inspect.isabstract(componentModel_Type)


def test_componentmodel_type_constructor_exists():
    assert callable(componentModel_Type.__init__)


def test_componentmodel_type_constructor_args():
    sig = inspect.signature(componentModel_Type.__init__)
    params = list(sig.parameters.keys())



def test_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(DelegationConnector)


def test_delegationconnector_constructor_exists():
    assert callable(DelegationConnector.__init__)


def test_delegationconnector_constructor_args():
    sig = inspect.signature(DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_requireddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_RequiredDelegationConnector)


def test_componentmodel_requireddelegationconnector_constructor_exists():
    assert callable(componentModel_RequiredDelegationConnector.__init__)


def test_componentmodel_requireddelegationconnector_constructor_args():
    sig = inspect.signature(componentModel_RequiredDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_requiredrole_is_not_abstract():
    assert not inspect.isabstract(componentModel_RequiredRole)


def test_componentmodel_requiredrole_constructor_exists():
    assert callable(componentModel_RequiredRole.__init__)


def test_componentmodel_requiredrole_constructor_args():
    sig = inspect.signature(componentModel_RequiredRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_requiredrole_has_name():
    assert hasattr(componentModel_RequiredRole, "name")
    descriptor = None
    for klass in componentModel_RequiredRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel_providedrole_is_not_abstract():
    assert not inspect.isabstract(componentModel_ProvidedRole)


def test_componentmodel_providedrole_constructor_exists():
    assert callable(componentModel_ProvidedRole.__init__)


def test_componentmodel_providedrole_constructor_args():
    sig = inspect.signature(componentModel_ProvidedRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_providedrole_has_name():
    assert hasattr(componentModel_ProvidedRole, "name")
    descriptor = None
    for klass in componentModel_ProvidedRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_assemblyviewtype_is_not_abstract():
    assert not inspect.isabstract(AssemblyViewType)


def test_assemblyviewtype_constructor_exists():
    assert callable(AssemblyViewType.__init__)


def test_assemblyviewtype_constructor_args():
    sig = inspect.signature(AssemblyViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_assemblycontext_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyContext)


def test_componentmodel_assemblycontext_constructor_exists():
    assert callable(componentModel_AssemblyContext.__init__)


def test_componentmodel_assemblycontext_constructor_args():
    sig = inspect.signature(componentModel_AssemblyContext.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_assemblycontext_has_name():
    assert hasattr(componentModel_AssemblyContext, "name")
    descriptor = None
    for klass in componentModel_AssemblyContext.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel_viewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_ViewType)


def test_componentmodel_viewtype_constructor_exists():
    assert callable(componentModel_ViewType.__init__)


def test_componentmodel_viewtype_constructor_args():
    sig = inspect.signature(componentModel_ViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_signature_is_not_abstract():
    assert not inspect.isabstract(componentModel_Signature)


def test_componentmodel_signature_constructor_exists():
    assert callable(componentModel_Signature.__init__)


def test_componentmodel_signature_constructor_args():
    sig = inspect.signature(componentModel_Signature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_signature_has_name():
    assert hasattr(componentModel_Signature, "name")
    descriptor = None
    for klass in componentModel_Signature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_internalaction_is_not_abstract():
    assert not inspect.isabstract(componentModel_InternalAction)


def test_componentmodel_internalaction_constructor_exists():
    assert callable(componentModel_InternalAction.__init__)


def test_componentmodel_internalaction_constructor_args():
    sig = inspect.signature(componentModel_InternalAction.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_loop_is_not_abstract():
    assert not inspect.isabstract(componentModel_Loop)


def test_componentmodel_loop_constructor_exists():
    assert callable(componentModel_Loop.__init__)


def test_componentmodel_loop_constructor_args():
    sig = inspect.signature(componentModel_Loop.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_externalcall_is_not_abstract():
    assert not inspect.isabstract(componentModel_ExternalCall)


def test_componentmodel_externalcall_constructor_exists():
    assert callable(componentModel_ExternalCall.__init__)


def test_componentmodel_externalcall_constructor_args():
    sig = inspect.signature(componentModel_ExternalCall.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_branch_is_not_abstract():
    assert not inspect.isabstract(componentModel_Branch)


def test_componentmodel_branch_constructor_exists():
    assert callable(componentModel_Branch.__init__)


def test_componentmodel_branch_constructor_args():
    sig = inspect.signature(componentModel_Branch.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_action_is_not_abstract():
    assert not inspect.isabstract(componentModel_Action)


def test_componentmodel_action_constructor_exists():
    assert callable(componentModel_Action.__init__)


def test_componentmodel_action_constructor_args():
    sig = inspect.signature(componentModel_Action.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_service_is_not_abstract():
    assert not inspect.isabstract(componentModel_Service)


def test_componentmodel_service_constructor_exists():
    assert callable(componentModel_Service.__init__)


def test_componentmodel_service_constructor_args():
    sig = inspect.signature(componentModel_Service.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_delegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_DelegationConnector)


def test_componentmodel_delegationconnector_constructor_exists():
    assert callable(componentModel_DelegationConnector.__init__)


def test_componentmodel_delegationconnector_constructor_args():
    sig = inspect.signature(componentModel_DelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_assemblyconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyConnector)


def test_componentmodel_assemblyconnector_constructor_exists():
    assert callable(componentModel_AssemblyConnector.__init__)


def test_componentmodel_assemblyconnector_constructor_args():
    sig = inspect.signature(componentModel_AssemblyConnector.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_interfaceservicemaptuple_is_not_abstract():
    assert not inspect.isabstract(componentModel_InterfaceServiceMapTuple)


def test_componentmodel_interfaceservicemaptuple_constructor_exists():
    assert callable(componentModel_InterfaceServiceMapTuple.__init__)


def test_componentmodel_interfaceservicemaptuple_constructor_args():
    sig = inspect.signature(componentModel_InterfaceServiceMapTuple.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_serviceeffectspecification_is_not_abstract():
    assert not inspect.isabstract(componentModel_ServiceEffectSpecification)


def test_componentmodel_serviceeffectspecification_constructor_exists():
    assert callable(componentModel_ServiceEffectSpecification.__init__)


def test_componentmodel_serviceeffectspecification_constructor_args():
    sig = inspect.signature(componentModel_ServiceEffectSpecification.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_interface_is_not_abstract():
    assert not inspect.isabstract(componentModel_Interface)


def test_componentmodel_interface_constructor_exists():
    assert callable(componentModel_Interface.__init__)


def test_componentmodel_interface_constructor_args():
    sig = inspect.signature(componentModel_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_interface_has_name():
    assert hasattr(componentModel_Interface, "name")
    descriptor = None
    for klass in componentModel_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel_component_is_not_abstract():
    assert not inspect.isabstract(componentModel_Component)


def test_componentmodel_component_constructor_exists():
    assert callable(componentModel_Component.__init__)


def test_componentmodel_component_constructor_args():
    sig = inspect.signature(componentModel_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_component_has_name():
    assert hasattr(componentModel_Component, "name")
    descriptor = None
    for klass in componentModel_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_viewtype_is_not_abstract():
    assert not inspect.isabstract(ViewType)


def test_viewtype_constructor_exists():
    assert callable(ViewType.__init__)


def test_viewtype_constructor_args():
    sig = inspect.signature(ViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_repository_is_not_abstract():
    assert not inspect.isabstract(componentModel_Repository)


def test_componentmodel_repository_constructor_exists():
    assert callable(componentModel_Repository.__init__)


def test_componentmodel_repository_constructor_args():
    sig = inspect.signature(componentModel_Repository.__init__)
    params = list(sig.parameters.keys())



def test_viewpoint_is_not_abstract():
    assert not inspect.isabstract(ViewPoint)


def test_viewpoint_constructor_exists():
    assert callable(ViewPoint.__init__)


def test_viewpoint_constructor_args():
    sig = inspect.signature(ViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_assemblyviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyViewPoint)


def test_componentmodel_assemblyviewpoint_constructor_exists():
    assert callable(componentModel_AssemblyViewPoint.__init__)


def test_componentmodel_assemblyviewpoint_constructor_args():
    sig = inspect.signature(componentModel_AssemblyViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_systemindependentviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_SystemIndependentViewPoint)


def test_componentmodel_systemindependentviewpoint_constructor_exists():
    assert callable(componentModel_SystemIndependentViewPoint.__init__)


def test_componentmodel_systemindependentviewpoint_constructor_args():
    sig = inspect.signature(componentModel_SystemIndependentViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_parametertyp_is_not_abstract():
    assert not inspect.isabstract(ParameterTyp)


def test_parametertyp_constructor_exists():
    assert callable(ParameterTyp.__init__)


def test_parametertyp_constructor_args():
    sig = inspect.signature(ParameterTyp.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_simpleparametertype_is_not_abstract():
    assert not inspect.isabstract(componentModel_SimpleParameterType)


def test_componentmodel_simpleparametertype_constructor_exists():
    assert callable(componentModel_SimpleParameterType.__init__)


def test_componentmodel_simpleparametertype_constructor_args():
    sig = inspect.signature(componentModel_SimpleParameterType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_complexparametertype_is_not_abstract():
    assert not inspect.isabstract(componentModel_ComplexParameterType)


def test_componentmodel_complexparametertype_constructor_exists():
    assert callable(componentModel_ComplexParameterType.__init__)


def test_componentmodel_complexparametertype_constructor_args():
    sig = inspect.signature(componentModel_ComplexParameterType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_void_is_not_abstract():
    assert not inspect.isabstract(componentModel_Void)


def test_componentmodel_void_constructor_exists():
    assert callable(componentModel_Void.__init__)


def test_componentmodel_void_constructor_args():
    sig = inspect.signature(componentModel_Void.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_parametertyp_is_not_abstract():
    assert not inspect.isabstract(componentModel_ParameterTyp)


def test_componentmodel_parametertyp_constructor_exists():
    assert callable(componentModel_ParameterTyp.__init__)


def test_componentmodel_parametertyp_constructor_args():
    sig = inspect.signature(componentModel_ParameterTyp.__init__)
    params = list(sig.parameters.keys())



def test_simpleparametertype_is_not_abstract():
    assert not inspect.isabstract(SimpleParameterType)


def test_simpleparametertype_constructor_exists():
    assert callable(SimpleParameterType.__init__)


def test_simpleparametertype_constructor_args():
    sig = inspect.signature(SimpleParameterType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_map_is_not_abstract():
    assert not inspect.isabstract(componentModel_Map)


def test_componentmodel_map_constructor_exists():
    assert callable(componentModel_Map.__init__)


def test_componentmodel_map_constructor_args():
    sig = inspect.signature(componentModel_Map.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_boolean_is_not_abstract():
    assert not inspect.isabstract(componentModel_Boolean)


def test_componentmodel_boolean_constructor_exists():
    assert callable(componentModel_Boolean.__init__)


def test_componentmodel_boolean_constructor_args():
    sig = inspect.signature(componentModel_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_int_is_not_abstract():
    assert not inspect.isabstract(componentModel_Int)


def test_componentmodel_int_constructor_exists():
    assert callable(componentModel_Int.__init__)


def test_componentmodel_int_constructor_args():
    sig = inspect.signature(componentModel_Int.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_float_is_not_abstract():
    assert not inspect.isabstract(componentModel_Float)


def test_componentmodel_float_constructor_exists():
    assert callable(componentModel_Float.__init__)


def test_componentmodel_float_constructor_args():
    sig = inspect.signature(componentModel_Float.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_list_is_not_abstract():
    assert not inspect.isabstract(componentModel_List)


def test_componentmodel_list_constructor_exists():
    assert callable(componentModel_List.__init__)


def test_componentmodel_list_constructor_args():
    sig = inspect.signature(componentModel_List.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_char_is_not_abstract():
    assert not inspect.isabstract(componentModel_Char)


def test_componentmodel_char_constructor_exists():
    assert callable(componentModel_Char.__init__)


def test_componentmodel_char_constructor_args():
    sig = inspect.signature(componentModel_Char.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_long_is_not_abstract():
    assert not inspect.isabstract(componentModel_Long)


def test_componentmodel_long_constructor_exists():
    assert callable(componentModel_Long.__init__)


def test_componentmodel_long_constructor_args():
    sig = inspect.signature(componentModel_Long.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_string_is_not_abstract():
    assert not inspect.isabstract(componentModel_String)


def test_componentmodel_string_constructor_exists():
    assert callable(componentModel_String.__init__)


def test_componentmodel_string_constructor_args():
    sig = inspect.signature(componentModel_String.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(componentModel_Parameter)


def test_componentmodel_parameter_constructor_exists():
    assert callable(componentModel_Parameter.__init__)


def test_componentmodel_parameter_constructor_args():
    sig = inspect.signature(componentModel_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_componentmodel_parameter_has_name():
    assert hasattr(componentModel_Parameter, "name")
    descriptor = None
    for klass in componentModel_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_componentmodel_double_is_not_abstract():
    assert not inspect.isabstract(componentModel_Double)


def test_componentmodel_double_constructor_exists():
    assert callable(componentModel_Double.__init__)


def test_componentmodel_double_constructor_args():
    sig = inspect.signature(componentModel_Double.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_date_is_not_abstract():
    assert not inspect.isabstract(componentModel_Date)


def test_componentmodel_date_constructor_exists():
    assert callable(componentModel_Date.__init__)


def test_componentmodel_date_constructor_args():
    sig = inspect.signature(componentModel_Date.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_allocationviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_AllocationViewType)


def test_componentmodel_allocationviewtype_constructor_exists():
    assert callable(componentModel_AllocationViewType.__init__)


def test_componentmodel_allocationviewtype_constructor_args():
    sig = inspect.signature(componentModel_AllocationViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_environmentviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_EnvironmentViewType)


def test_componentmodel_environmentviewtype_constructor_exists():
    assert callable(componentModel_EnvironmentViewType.__init__)


def test_componentmodel_environmentviewtype_constructor_args():
    sig = inspect.signature(componentModel_EnvironmentViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_repositoryviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_RepositoryViewType)


def test_componentmodel_repositoryviewtype_constructor_exists():
    assert callable(componentModel_RepositoryViewType.__init__)


def test_componentmodel_repositoryviewtype_constructor_args():
    sig = inspect.signature(componentModel_RepositoryViewType.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_deploymentviewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_DeploymentViewPoint)


def test_componentmodel_deploymentviewpoint_constructor_exists():
    assert callable(componentModel_DeploymentViewPoint.__init__)


def test_componentmodel_deploymentviewpoint_constructor_args():
    sig = inspect.signature(componentModel_DeploymentViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_assemblyviewtype_is_not_abstract():
    assert not inspect.isabstract(componentModel_AssemblyViewType)


def test_componentmodel_assemblyviewtype_constructor_exists():
    assert callable(componentModel_AssemblyViewType.__init__)


def test_componentmodel_assemblyviewtype_constructor_args():
    sig = inspect.signature(componentModel_AssemblyViewType.__init__)
    params = list(sig.parameters.keys())



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_compositecomponent_is_not_abstract():
    assert not inspect.isabstract(componentModel_CompositeComponent)


def test_componentmodel_compositecomponent_constructor_exists():
    assert callable(componentModel_CompositeComponent.__init__)


def test_componentmodel_compositecomponent_constructor_args():
    sig = inspect.signature(componentModel_CompositeComponent.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_viewpoint_is_not_abstract():
    assert not inspect.isabstract(componentModel_ViewPoint)


def test_componentmodel_viewpoint_constructor_exists():
    assert callable(componentModel_ViewPoint.__init__)


def test_componentmodel_viewpoint_constructor_args():
    sig = inspect.signature(componentModel_ViewPoint.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_provideddelegationconnector_is_not_abstract():
    assert not inspect.isabstract(componentModel_ProvidedDelegationConnector)


def test_componentmodel_provideddelegationconnector_constructor_exists():
    assert callable(componentModel_ProvidedDelegationConnector.__init__)


def test_componentmodel_provideddelegationconnector_constructor_args():
    sig = inspect.signature(componentModel_ProvidedDelegationConnector.__init__)
    params = list(sig.parameters.keys())



def test_componentmodel_system_is_not_abstract():
    assert not inspect.isabstract(componentModel_System)


def test_componentmodel_system_constructor_exists():
    assert callable(componentModel_System.__init__)


def test_componentmodel_system_constructor_args():
    sig = inspect.signature(componentModel_System.__init__)
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
componentModel_Type_strategy = st.builds(
    componentModel_Type,
)
DelegationConnector_strategy = st.builds(
    DelegationConnector,
)
componentModel_RequiredDelegationConnector_strategy = st.builds(
    componentModel_RequiredDelegationConnector,
)
componentModel_RequiredRole_strategy = st.builds(
    componentModel_RequiredRole,
    name=
        safe_text
)
componentModel_ProvidedRole_strategy = st.builds(
    componentModel_ProvidedRole,
    name=
        safe_text
)
AssemblyViewType_strategy = st.builds(
    AssemblyViewType,
)
componentModel_AssemblyContext_strategy = st.builds(
    componentModel_AssemblyContext,
    name=
        safe_text
)
componentModel_ViewType_strategy = st.builds(
    componentModel_ViewType,
)
componentModel_Signature_strategy = st.builds(
    componentModel_Signature,
    name=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
componentModel_InternalAction_strategy = st.builds(
    componentModel_InternalAction,
)
componentModel_Loop_strategy = st.builds(
    componentModel_Loop,
)
componentModel_ExternalCall_strategy = st.builds(
    componentModel_ExternalCall,
)
componentModel_Branch_strategy = st.builds(
    componentModel_Branch,
)
componentModel_Action_strategy = st.builds(
    componentModel_Action,
)
componentModel_Service_strategy = st.builds(
    componentModel_Service,
)
componentModel_DelegationConnector_strategy = st.builds(
    componentModel_DelegationConnector,
)
componentModel_AssemblyConnector_strategy = st.builds(
    componentModel_AssemblyConnector,
)
componentModel_InterfaceServiceMapTuple_strategy = st.builds(
    componentModel_InterfaceServiceMapTuple,
)
componentModel_ServiceEffectSpecification_strategy = st.builds(
    componentModel_ServiceEffectSpecification,
)
componentModel_Interface_strategy = st.builds(
    componentModel_Interface,
    name=
        safe_text
)
componentModel_Component_strategy = st.builds(
    componentModel_Component,
    name=
        safe_text
)
ViewType_strategy = st.builds(
    ViewType,
)
componentModel_Repository_strategy = st.builds(
    componentModel_Repository,
)
ViewPoint_strategy = st.builds(
    ViewPoint,
)
componentModel_AssemblyViewPoint_strategy = st.builds(
    componentModel_AssemblyViewPoint,
)
componentModel_SystemIndependentViewPoint_strategy = st.builds(
    componentModel_SystemIndependentViewPoint,
)
ParameterTyp_strategy = st.builds(
    ParameterTyp,
)
componentModel_SimpleParameterType_strategy = st.builds(
    componentModel_SimpleParameterType,
)
componentModel_ComplexParameterType_strategy = st.builds(
    componentModel_ComplexParameterType,
)
Type_strategy = st.builds(
    Type,
)
componentModel_Void_strategy = st.builds(
    componentModel_Void,
)
componentModel_ParameterTyp_strategy = st.builds(
    componentModel_ParameterTyp,
)
SimpleParameterType_strategy = st.builds(
    SimpleParameterType,
)
componentModel_Map_strategy = st.builds(
    componentModel_Map,
)
componentModel_Boolean_strategy = st.builds(
    componentModel_Boolean,
)
componentModel_Int_strategy = st.builds(
    componentModel_Int,
)
componentModel_Float_strategy = st.builds(
    componentModel_Float,
)
componentModel_List_strategy = st.builds(
    componentModel_List,
)
componentModel_Char_strategy = st.builds(
    componentModel_Char,
)
componentModel_Long_strategy = st.builds(
    componentModel_Long,
)
componentModel_String_strategy = st.builds(
    componentModel_String,
)
componentModel_Parameter_strategy = st.builds(
    componentModel_Parameter,
    name=
        safe_text
)
componentModel_Double_strategy = st.builds(
    componentModel_Double,
)
componentModel_Date_strategy = st.builds(
    componentModel_Date,
)
componentModel_AllocationViewType_strategy = st.builds(
    componentModel_AllocationViewType,
)
componentModel_EnvironmentViewType_strategy = st.builds(
    componentModel_EnvironmentViewType,
)
componentModel_RepositoryViewType_strategy = st.builds(
    componentModel_RepositoryViewType,
)
componentModel_DeploymentViewPoint_strategy = st.builds(
    componentModel_DeploymentViewPoint,
)
componentModel_AssemblyViewType_strategy = st.builds(
    componentModel_AssemblyViewType,
)
Component_strategy = st.builds(
    Component,
)
componentModel_CompositeComponent_strategy = st.builds(
    componentModel_CompositeComponent,
)
componentModel_ViewPoint_strategy = st.builds(
    componentModel_ViewPoint,
)
componentModel_ProvidedDelegationConnector_strategy = st.builds(
    componentModel_ProvidedDelegationConnector,
)
componentModel_System_strategy = st.builds(
    componentModel_System,
)

@given(instance=componentModel_Type_strategy)
@settings(max_examples=50)
def test_componentmodel_type_instantiation(instance):
    assert isinstance(instance, componentModel_Type)

@given(instance=DelegationConnector_strategy)
@settings(max_examples=50)
def test_delegationconnector_instantiation(instance):
    assert isinstance(instance, DelegationConnector)

@given(instance=componentModel_RequiredDelegationConnector_strategy)
@settings(max_examples=50)
def test_componentmodel_requireddelegationconnector_instantiation(instance):
    assert isinstance(instance, componentModel_RequiredDelegationConnector)

@given(instance=componentModel_RequiredRole_strategy)
@settings(max_examples=50)
def test_componentmodel_requiredrole_instantiation(instance):
    assert isinstance(instance, componentModel_RequiredRole)



@given(instance=componentModel_RequiredRole_strategy)
def test_componentmodel_requiredrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentModel_ProvidedRole_strategy)
@settings(max_examples=50)
def test_componentmodel_providedrole_instantiation(instance):
    assert isinstance(instance, componentModel_ProvidedRole)



@given(instance=componentModel_ProvidedRole_strategy)
def test_componentmodel_providedrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AssemblyViewType_strategy)
@settings(max_examples=50)
def test_assemblyviewtype_instantiation(instance):
    assert isinstance(instance, AssemblyViewType)

@given(instance=componentModel_AssemblyContext_strategy)
@settings(max_examples=50)
def test_componentmodel_assemblycontext_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyContext)



@given(instance=componentModel_AssemblyContext_strategy)
def test_componentmodel_assemblycontext_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentModel_ViewType_strategy)
@settings(max_examples=50)
def test_componentmodel_viewtype_instantiation(instance):
    assert isinstance(instance, componentModel_ViewType)

@given(instance=componentModel_Signature_strategy)
@settings(max_examples=50)
def test_componentmodel_signature_instantiation(instance):
    assert isinstance(instance, componentModel_Signature)



@given(instance=componentModel_Signature_strategy)
def test_componentmodel_signature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=componentModel_InternalAction_strategy)
@settings(max_examples=50)
def test_componentmodel_internalaction_instantiation(instance):
    assert isinstance(instance, componentModel_InternalAction)

@given(instance=componentModel_Loop_strategy)
@settings(max_examples=50)
def test_componentmodel_loop_instantiation(instance):
    assert isinstance(instance, componentModel_Loop)

@given(instance=componentModel_ExternalCall_strategy)
@settings(max_examples=50)
def test_componentmodel_externalcall_instantiation(instance):
    assert isinstance(instance, componentModel_ExternalCall)

@given(instance=componentModel_Branch_strategy)
@settings(max_examples=50)
def test_componentmodel_branch_instantiation(instance):
    assert isinstance(instance, componentModel_Branch)

@given(instance=componentModel_Action_strategy)
@settings(max_examples=50)
def test_componentmodel_action_instantiation(instance):
    assert isinstance(instance, componentModel_Action)

@given(instance=componentModel_Service_strategy)
@settings(max_examples=50)
def test_componentmodel_service_instantiation(instance):
    assert isinstance(instance, componentModel_Service)

@given(instance=componentModel_DelegationConnector_strategy)
@settings(max_examples=50)
def test_componentmodel_delegationconnector_instantiation(instance):
    assert isinstance(instance, componentModel_DelegationConnector)

@given(instance=componentModel_AssemblyConnector_strategy)
@settings(max_examples=50)
def test_componentmodel_assemblyconnector_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyConnector)

@given(instance=componentModel_InterfaceServiceMapTuple_strategy)
@settings(max_examples=50)
def test_componentmodel_interfaceservicemaptuple_instantiation(instance):
    assert isinstance(instance, componentModel_InterfaceServiceMapTuple)

@given(instance=componentModel_ServiceEffectSpecification_strategy)
@settings(max_examples=50)
def test_componentmodel_serviceeffectspecification_instantiation(instance):
    assert isinstance(instance, componentModel_ServiceEffectSpecification)

@given(instance=componentModel_Interface_strategy)
@settings(max_examples=50)
def test_componentmodel_interface_instantiation(instance):
    assert isinstance(instance, componentModel_Interface)



@given(instance=componentModel_Interface_strategy)
def test_componentmodel_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentModel_Component_strategy)
@settings(max_examples=50)
def test_componentmodel_component_instantiation(instance):
    assert isinstance(instance, componentModel_Component)



@given(instance=componentModel_Component_strategy)
def test_componentmodel_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ViewType_strategy)
@settings(max_examples=50)
def test_viewtype_instantiation(instance):
    assert isinstance(instance, ViewType)

@given(instance=componentModel_Repository_strategy)
@settings(max_examples=50)
def test_componentmodel_repository_instantiation(instance):
    assert isinstance(instance, componentModel_Repository)

@given(instance=ViewPoint_strategy)
@settings(max_examples=50)
def test_viewpoint_instantiation(instance):
    assert isinstance(instance, ViewPoint)

@given(instance=componentModel_AssemblyViewPoint_strategy)
@settings(max_examples=50)
def test_componentmodel_assemblyviewpoint_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyViewPoint)

@given(instance=componentModel_SystemIndependentViewPoint_strategy)
@settings(max_examples=50)
def test_componentmodel_systemindependentviewpoint_instantiation(instance):
    assert isinstance(instance, componentModel_SystemIndependentViewPoint)

@given(instance=ParameterTyp_strategy)
@settings(max_examples=50)
def test_parametertyp_instantiation(instance):
    assert isinstance(instance, ParameterTyp)

@given(instance=componentModel_SimpleParameterType_strategy)
@settings(max_examples=50)
def test_componentmodel_simpleparametertype_instantiation(instance):
    assert isinstance(instance, componentModel_SimpleParameterType)

@given(instance=componentModel_ComplexParameterType_strategy)
@settings(max_examples=50)
def test_componentmodel_complexparametertype_instantiation(instance):
    assert isinstance(instance, componentModel_ComplexParameterType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=componentModel_Void_strategy)
@settings(max_examples=50)
def test_componentmodel_void_instantiation(instance):
    assert isinstance(instance, componentModel_Void)

@given(instance=componentModel_ParameterTyp_strategy)
@settings(max_examples=50)
def test_componentmodel_parametertyp_instantiation(instance):
    assert isinstance(instance, componentModel_ParameterTyp)

@given(instance=SimpleParameterType_strategy)
@settings(max_examples=50)
def test_simpleparametertype_instantiation(instance):
    assert isinstance(instance, SimpleParameterType)

@given(instance=componentModel_Map_strategy)
@settings(max_examples=50)
def test_componentmodel_map_instantiation(instance):
    assert isinstance(instance, componentModel_Map)

@given(instance=componentModel_Boolean_strategy)
@settings(max_examples=50)
def test_componentmodel_boolean_instantiation(instance):
    assert isinstance(instance, componentModel_Boolean)

@given(instance=componentModel_Int_strategy)
@settings(max_examples=50)
def test_componentmodel_int_instantiation(instance):
    assert isinstance(instance, componentModel_Int)

@given(instance=componentModel_Float_strategy)
@settings(max_examples=50)
def test_componentmodel_float_instantiation(instance):
    assert isinstance(instance, componentModel_Float)

@given(instance=componentModel_List_strategy)
@settings(max_examples=50)
def test_componentmodel_list_instantiation(instance):
    assert isinstance(instance, componentModel_List)

@given(instance=componentModel_Char_strategy)
@settings(max_examples=50)
def test_componentmodel_char_instantiation(instance):
    assert isinstance(instance, componentModel_Char)

@given(instance=componentModel_Long_strategy)
@settings(max_examples=50)
def test_componentmodel_long_instantiation(instance):
    assert isinstance(instance, componentModel_Long)

@given(instance=componentModel_String_strategy)
@settings(max_examples=50)
def test_componentmodel_string_instantiation(instance):
    assert isinstance(instance, componentModel_String)

@given(instance=componentModel_Parameter_strategy)
@settings(max_examples=50)
def test_componentmodel_parameter_instantiation(instance):
    assert isinstance(instance, componentModel_Parameter)



@given(instance=componentModel_Parameter_strategy)
def test_componentmodel_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=componentModel_Double_strategy)
@settings(max_examples=50)
def test_componentmodel_double_instantiation(instance):
    assert isinstance(instance, componentModel_Double)

@given(instance=componentModel_Date_strategy)
@settings(max_examples=50)
def test_componentmodel_date_instantiation(instance):
    assert isinstance(instance, componentModel_Date)

@given(instance=componentModel_AllocationViewType_strategy)
@settings(max_examples=50)
def test_componentmodel_allocationviewtype_instantiation(instance):
    assert isinstance(instance, componentModel_AllocationViewType)

@given(instance=componentModel_EnvironmentViewType_strategy)
@settings(max_examples=50)
def test_componentmodel_environmentviewtype_instantiation(instance):
    assert isinstance(instance, componentModel_EnvironmentViewType)

@given(instance=componentModel_RepositoryViewType_strategy)
@settings(max_examples=50)
def test_componentmodel_repositoryviewtype_instantiation(instance):
    assert isinstance(instance, componentModel_RepositoryViewType)

@given(instance=componentModel_DeploymentViewPoint_strategy)
@settings(max_examples=50)
def test_componentmodel_deploymentviewpoint_instantiation(instance):
    assert isinstance(instance, componentModel_DeploymentViewPoint)

@given(instance=componentModel_AssemblyViewType_strategy)
@settings(max_examples=50)
def test_componentmodel_assemblyviewtype_instantiation(instance):
    assert isinstance(instance, componentModel_AssemblyViewType)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=componentModel_CompositeComponent_strategy)
@settings(max_examples=50)
def test_componentmodel_compositecomponent_instantiation(instance):
    assert isinstance(instance, componentModel_CompositeComponent)

@given(instance=componentModel_ViewPoint_strategy)
@settings(max_examples=50)
def test_componentmodel_viewpoint_instantiation(instance):
    assert isinstance(instance, componentModel_ViewPoint)

@given(instance=componentModel_ProvidedDelegationConnector_strategy)
@settings(max_examples=50)
def test_componentmodel_provideddelegationconnector_instantiation(instance):
    assert isinstance(instance, componentModel_ProvidedDelegationConnector)

@given(instance=componentModel_System_strategy)
@settings(max_examples=50)
def test_componentmodel_system_instantiation(instance):
    assert isinstance(instance, componentModel_System)
