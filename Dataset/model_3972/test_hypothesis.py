import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    standard_Source,
    standard_Service,
    standard_Classifier,
    standard_Realization,
    standard_Process,
    standard_Library,
    standard_File,
    standard_Executable,
    standard_Entity,
    standard_Document,
    standard_SystemModel,
    standard_Model,
    standard_Metamodel,
    standard_Subsystem,
    standard_Specification,
    standard_Send,
    standard_Artifact,
    standard_Script,
    standard_Responsibility,
    standard_Refine,
    standard_ModelLibrary,
    standard_Metaclass,
    standard_Instantiate,
    standard_ImplementationClass,
    standard_Implement,
    standard_Package,
    standard_Framework,
    standard_Focus,
    standard_Utility,
    standard_Type,
    standard_Trace,
    standard_Component,
    standard_BuildComponent,
    standard_Class,
    standard_Auxiliary,
    standard_Destroy,
    standard_Abstraction,
    standard_Derive,
    standard_Call,
    standard_Usage,
    standard_BehavioralFeature,
    standard_Create,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_standard_source_is_not_abstract():
    assert not inspect.isabstract(standard_Source)


def test_standard_source_constructor_exists():
    assert callable(standard_Source.__init__)


def test_standard_source_constructor_args():
    sig = inspect.signature(standard_Source.__init__)
    params = list(sig.parameters.keys())



def test_standard_service_is_not_abstract():
    assert not inspect.isabstract(standard_Service)


def test_standard_service_constructor_exists():
    assert callable(standard_Service.__init__)


def test_standard_service_constructor_args():
    sig = inspect.signature(standard_Service.__init__)
    params = list(sig.parameters.keys())



def test_standard_classifier_is_not_abstract():
    assert not inspect.isabstract(standard_Classifier)


def test_standard_classifier_constructor_exists():
    assert callable(standard_Classifier.__init__)


def test_standard_classifier_constructor_args():
    sig = inspect.signature(standard_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_standard_realization_is_not_abstract():
    assert not inspect.isabstract(standard_Realization)


def test_standard_realization_constructor_exists():
    assert callable(standard_Realization.__init__)


def test_standard_realization_constructor_args():
    sig = inspect.signature(standard_Realization.__init__)
    params = list(sig.parameters.keys())



def test_standard_process_is_not_abstract():
    assert not inspect.isabstract(standard_Process)


def test_standard_process_constructor_exists():
    assert callable(standard_Process.__init__)


def test_standard_process_constructor_args():
    sig = inspect.signature(standard_Process.__init__)
    params = list(sig.parameters.keys())



def test_standard_library_is_not_abstract():
    assert not inspect.isabstract(standard_Library)


def test_standard_library_constructor_exists():
    assert callable(standard_Library.__init__)


def test_standard_library_constructor_args():
    sig = inspect.signature(standard_Library.__init__)
    params = list(sig.parameters.keys())



def test_standard_file_is_not_abstract():
    assert not inspect.isabstract(standard_File)


def test_standard_file_constructor_exists():
    assert callable(standard_File.__init__)


def test_standard_file_constructor_args():
    sig = inspect.signature(standard_File.__init__)
    params = list(sig.parameters.keys())



def test_standard_executable_is_not_abstract():
    assert not inspect.isabstract(standard_Executable)


def test_standard_executable_constructor_exists():
    assert callable(standard_Executable.__init__)


def test_standard_executable_constructor_args():
    sig = inspect.signature(standard_Executable.__init__)
    params = list(sig.parameters.keys())



def test_standard_entity_is_not_abstract():
    assert not inspect.isabstract(standard_Entity)


def test_standard_entity_constructor_exists():
    assert callable(standard_Entity.__init__)


def test_standard_entity_constructor_args():
    sig = inspect.signature(standard_Entity.__init__)
    params = list(sig.parameters.keys())



def test_standard_document_is_not_abstract():
    assert not inspect.isabstract(standard_Document)


def test_standard_document_constructor_exists():
    assert callable(standard_Document.__init__)


def test_standard_document_constructor_args():
    sig = inspect.signature(standard_Document.__init__)
    params = list(sig.parameters.keys())



def test_standard_systemmodel_is_not_abstract():
    assert not inspect.isabstract(standard_SystemModel)


def test_standard_systemmodel_constructor_exists():
    assert callable(standard_SystemModel.__init__)


def test_standard_systemmodel_constructor_args():
    sig = inspect.signature(standard_SystemModel.__init__)
    params = list(sig.parameters.keys())



def test_standard_model_is_not_abstract():
    assert not inspect.isabstract(standard_Model)


def test_standard_model_constructor_exists():
    assert callable(standard_Model.__init__)


def test_standard_model_constructor_args():
    sig = inspect.signature(standard_Model.__init__)
    params = list(sig.parameters.keys())



def test_standard_metamodel_is_not_abstract():
    assert not inspect.isabstract(standard_Metamodel)


def test_standard_metamodel_constructor_exists():
    assert callable(standard_Metamodel.__init__)


def test_standard_metamodel_constructor_args():
    sig = inspect.signature(standard_Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_standard_subsystem_is_not_abstract():
    assert not inspect.isabstract(standard_Subsystem)


def test_standard_subsystem_constructor_exists():
    assert callable(standard_Subsystem.__init__)


def test_standard_subsystem_constructor_args():
    sig = inspect.signature(standard_Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_standard_specification_is_not_abstract():
    assert not inspect.isabstract(standard_Specification)


def test_standard_specification_constructor_exists():
    assert callable(standard_Specification.__init__)


def test_standard_specification_constructor_args():
    sig = inspect.signature(standard_Specification.__init__)
    params = list(sig.parameters.keys())



def test_standard_send_is_not_abstract():
    assert not inspect.isabstract(standard_Send)


def test_standard_send_constructor_exists():
    assert callable(standard_Send.__init__)


def test_standard_send_constructor_args():
    sig = inspect.signature(standard_Send.__init__)
    params = list(sig.parameters.keys())



def test_standard_artifact_is_not_abstract():
    assert not inspect.isabstract(standard_Artifact)


def test_standard_artifact_constructor_exists():
    assert callable(standard_Artifact.__init__)


def test_standard_artifact_constructor_args():
    sig = inspect.signature(standard_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_standard_script_is_not_abstract():
    assert not inspect.isabstract(standard_Script)


def test_standard_script_constructor_exists():
    assert callable(standard_Script.__init__)


def test_standard_script_constructor_args():
    sig = inspect.signature(standard_Script.__init__)
    params = list(sig.parameters.keys())



def test_standard_responsibility_is_not_abstract():
    assert not inspect.isabstract(standard_Responsibility)


def test_standard_responsibility_constructor_exists():
    assert callable(standard_Responsibility.__init__)


def test_standard_responsibility_constructor_args():
    sig = inspect.signature(standard_Responsibility.__init__)
    params = list(sig.parameters.keys())



def test_standard_refine_is_not_abstract():
    assert not inspect.isabstract(standard_Refine)


def test_standard_refine_constructor_exists():
    assert callable(standard_Refine.__init__)


def test_standard_refine_constructor_args():
    sig = inspect.signature(standard_Refine.__init__)
    params = list(sig.parameters.keys())



def test_standard_modellibrary_is_not_abstract():
    assert not inspect.isabstract(standard_ModelLibrary)


def test_standard_modellibrary_constructor_exists():
    assert callable(standard_ModelLibrary.__init__)


def test_standard_modellibrary_constructor_args():
    sig = inspect.signature(standard_ModelLibrary.__init__)
    params = list(sig.parameters.keys())



def test_standard_metaclass_is_not_abstract():
    assert not inspect.isabstract(standard_Metaclass)


def test_standard_metaclass_constructor_exists():
    assert callable(standard_Metaclass.__init__)


def test_standard_metaclass_constructor_args():
    sig = inspect.signature(standard_Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_standard_instantiate_is_not_abstract():
    assert not inspect.isabstract(standard_Instantiate)


def test_standard_instantiate_constructor_exists():
    assert callable(standard_Instantiate.__init__)


def test_standard_instantiate_constructor_args():
    sig = inspect.signature(standard_Instantiate.__init__)
    params = list(sig.parameters.keys())



def test_standard_implementationclass_is_not_abstract():
    assert not inspect.isabstract(standard_ImplementationClass)


def test_standard_implementationclass_constructor_exists():
    assert callable(standard_ImplementationClass.__init__)


def test_standard_implementationclass_constructor_args():
    sig = inspect.signature(standard_ImplementationClass.__init__)
    params = list(sig.parameters.keys())



def test_standard_implement_is_not_abstract():
    assert not inspect.isabstract(standard_Implement)


def test_standard_implement_constructor_exists():
    assert callable(standard_Implement.__init__)


def test_standard_implement_constructor_args():
    sig = inspect.signature(standard_Implement.__init__)
    params = list(sig.parameters.keys())



def test_standard_package_is_not_abstract():
    assert not inspect.isabstract(standard_Package)


def test_standard_package_constructor_exists():
    assert callable(standard_Package.__init__)


def test_standard_package_constructor_args():
    sig = inspect.signature(standard_Package.__init__)
    params = list(sig.parameters.keys())



def test_standard_framework_is_not_abstract():
    assert not inspect.isabstract(standard_Framework)


def test_standard_framework_constructor_exists():
    assert callable(standard_Framework.__init__)


def test_standard_framework_constructor_args():
    sig = inspect.signature(standard_Framework.__init__)
    params = list(sig.parameters.keys())



def test_standard_focus_is_not_abstract():
    assert not inspect.isabstract(standard_Focus)


def test_standard_focus_constructor_exists():
    assert callable(standard_Focus.__init__)


def test_standard_focus_constructor_args():
    sig = inspect.signature(standard_Focus.__init__)
    params = list(sig.parameters.keys())



def test_standard_utility_is_not_abstract():
    assert not inspect.isabstract(standard_Utility)


def test_standard_utility_constructor_exists():
    assert callable(standard_Utility.__init__)


def test_standard_utility_constructor_args():
    sig = inspect.signature(standard_Utility.__init__)
    params = list(sig.parameters.keys())



def test_standard_type_is_not_abstract():
    assert not inspect.isabstract(standard_Type)


def test_standard_type_constructor_exists():
    assert callable(standard_Type.__init__)


def test_standard_type_constructor_args():
    sig = inspect.signature(standard_Type.__init__)
    params = list(sig.parameters.keys())



def test_standard_trace_is_not_abstract():
    assert not inspect.isabstract(standard_Trace)


def test_standard_trace_constructor_exists():
    assert callable(standard_Trace.__init__)


def test_standard_trace_constructor_args():
    sig = inspect.signature(standard_Trace.__init__)
    params = list(sig.parameters.keys())



def test_standard_component_is_not_abstract():
    assert not inspect.isabstract(standard_Component)


def test_standard_component_constructor_exists():
    assert callable(standard_Component.__init__)


def test_standard_component_constructor_args():
    sig = inspect.signature(standard_Component.__init__)
    params = list(sig.parameters.keys())



def test_standard_buildcomponent_is_not_abstract():
    assert not inspect.isabstract(standard_BuildComponent)


def test_standard_buildcomponent_constructor_exists():
    assert callable(standard_BuildComponent.__init__)


def test_standard_buildcomponent_constructor_args():
    sig = inspect.signature(standard_BuildComponent.__init__)
    params = list(sig.parameters.keys())



def test_standard_class_is_not_abstract():
    assert not inspect.isabstract(standard_Class)


def test_standard_class_constructor_exists():
    assert callable(standard_Class.__init__)


def test_standard_class_constructor_args():
    sig = inspect.signature(standard_Class.__init__)
    params = list(sig.parameters.keys())



def test_standard_auxiliary_is_not_abstract():
    assert not inspect.isabstract(standard_Auxiliary)


def test_standard_auxiliary_constructor_exists():
    assert callable(standard_Auxiliary.__init__)


def test_standard_auxiliary_constructor_args():
    sig = inspect.signature(standard_Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_standard_destroy_is_not_abstract():
    assert not inspect.isabstract(standard_Destroy)


def test_standard_destroy_constructor_exists():
    assert callable(standard_Destroy.__init__)


def test_standard_destroy_constructor_args():
    sig = inspect.signature(standard_Destroy.__init__)
    params = list(sig.parameters.keys())



def test_standard_abstraction_is_not_abstract():
    assert not inspect.isabstract(standard_Abstraction)


def test_standard_abstraction_constructor_exists():
    assert callable(standard_Abstraction.__init__)


def test_standard_abstraction_constructor_args():
    sig = inspect.signature(standard_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_standard_derive_is_not_abstract():
    assert not inspect.isabstract(standard_Derive)


def test_standard_derive_constructor_exists():
    assert callable(standard_Derive.__init__)


def test_standard_derive_constructor_args():
    sig = inspect.signature(standard_Derive.__init__)
    params = list(sig.parameters.keys())



def test_standard_call_is_not_abstract():
    assert not inspect.isabstract(standard_Call)


def test_standard_call_constructor_exists():
    assert callable(standard_Call.__init__)


def test_standard_call_constructor_args():
    sig = inspect.signature(standard_Call.__init__)
    params = list(sig.parameters.keys())



def test_standard_usage_is_not_abstract():
    assert not inspect.isabstract(standard_Usage)


def test_standard_usage_constructor_exists():
    assert callable(standard_Usage.__init__)


def test_standard_usage_constructor_args():
    sig = inspect.signature(standard_Usage.__init__)
    params = list(sig.parameters.keys())



def test_standard_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(standard_BehavioralFeature)


def test_standard_behavioralfeature_constructor_exists():
    assert callable(standard_BehavioralFeature.__init__)


def test_standard_behavioralfeature_constructor_args():
    sig = inspect.signature(standard_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_standard_create_is_not_abstract():
    assert not inspect.isabstract(standard_Create)


def test_standard_create_constructor_exists():
    assert callable(standard_Create.__init__)


def test_standard_create_constructor_args():
    sig = inspect.signature(standard_Create.__init__)
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
standard_Source_strategy = st.builds(
    standard_Source,
)
standard_Service_strategy = st.builds(
    standard_Service,
)
standard_Classifier_strategy = st.builds(
    standard_Classifier,
)
standard_Realization_strategy = st.builds(
    standard_Realization,
)
standard_Process_strategy = st.builds(
    standard_Process,
)
standard_Library_strategy = st.builds(
    standard_Library,
)
standard_File_strategy = st.builds(
    standard_File,
)
standard_Executable_strategy = st.builds(
    standard_Executable,
)
standard_Entity_strategy = st.builds(
    standard_Entity,
)
standard_Document_strategy = st.builds(
    standard_Document,
)
standard_SystemModel_strategy = st.builds(
    standard_SystemModel,
)
standard_Model_strategy = st.builds(
    standard_Model,
)
standard_Metamodel_strategy = st.builds(
    standard_Metamodel,
)
standard_Subsystem_strategy = st.builds(
    standard_Subsystem,
)
standard_Specification_strategy = st.builds(
    standard_Specification,
)
standard_Send_strategy = st.builds(
    standard_Send,
)
standard_Artifact_strategy = st.builds(
    standard_Artifact,
)
standard_Script_strategy = st.builds(
    standard_Script,
)
standard_Responsibility_strategy = st.builds(
    standard_Responsibility,
)
standard_Refine_strategy = st.builds(
    standard_Refine,
)
standard_ModelLibrary_strategy = st.builds(
    standard_ModelLibrary,
)
standard_Metaclass_strategy = st.builds(
    standard_Metaclass,
)
standard_Instantiate_strategy = st.builds(
    standard_Instantiate,
)
standard_ImplementationClass_strategy = st.builds(
    standard_ImplementationClass,
)
standard_Implement_strategy = st.builds(
    standard_Implement,
)
standard_Package_strategy = st.builds(
    standard_Package,
)
standard_Framework_strategy = st.builds(
    standard_Framework,
)
standard_Focus_strategy = st.builds(
    standard_Focus,
)
standard_Utility_strategy = st.builds(
    standard_Utility,
)
standard_Type_strategy = st.builds(
    standard_Type,
)
standard_Trace_strategy = st.builds(
    standard_Trace,
)
standard_Component_strategy = st.builds(
    standard_Component,
)
standard_BuildComponent_strategy = st.builds(
    standard_BuildComponent,
)
standard_Class_strategy = st.builds(
    standard_Class,
)
standard_Auxiliary_strategy = st.builds(
    standard_Auxiliary,
)
standard_Destroy_strategy = st.builds(
    standard_Destroy,
)
standard_Abstraction_strategy = st.builds(
    standard_Abstraction,
)
standard_Derive_strategy = st.builds(
    standard_Derive,
)
standard_Call_strategy = st.builds(
    standard_Call,
)
standard_Usage_strategy = st.builds(
    standard_Usage,
)
standard_BehavioralFeature_strategy = st.builds(
    standard_BehavioralFeature,
)
standard_Create_strategy = st.builds(
    standard_Create,
)

@given(instance=standard_Source_strategy)
@settings(max_examples=50)
def test_standard_source_instantiation(instance):
    assert isinstance(instance, standard_Source)

@given(instance=standard_Service_strategy)
@settings(max_examples=50)
def test_standard_service_instantiation(instance):
    assert isinstance(instance, standard_Service)

@given(instance=standard_Classifier_strategy)
@settings(max_examples=50)
def test_standard_classifier_instantiation(instance):
    assert isinstance(instance, standard_Classifier)

@given(instance=standard_Realization_strategy)
@settings(max_examples=50)
def test_standard_realization_instantiation(instance):
    assert isinstance(instance, standard_Realization)

@given(instance=standard_Process_strategy)
@settings(max_examples=50)
def test_standard_process_instantiation(instance):
    assert isinstance(instance, standard_Process)

@given(instance=standard_Library_strategy)
@settings(max_examples=50)
def test_standard_library_instantiation(instance):
    assert isinstance(instance, standard_Library)

@given(instance=standard_File_strategy)
@settings(max_examples=50)
def test_standard_file_instantiation(instance):
    assert isinstance(instance, standard_File)

@given(instance=standard_Executable_strategy)
@settings(max_examples=50)
def test_standard_executable_instantiation(instance):
    assert isinstance(instance, standard_Executable)

@given(instance=standard_Entity_strategy)
@settings(max_examples=50)
def test_standard_entity_instantiation(instance):
    assert isinstance(instance, standard_Entity)

@given(instance=standard_Document_strategy)
@settings(max_examples=50)
def test_standard_document_instantiation(instance):
    assert isinstance(instance, standard_Document)

@given(instance=standard_SystemModel_strategy)
@settings(max_examples=50)
def test_standard_systemmodel_instantiation(instance):
    assert isinstance(instance, standard_SystemModel)

@given(instance=standard_Model_strategy)
@settings(max_examples=50)
def test_standard_model_instantiation(instance):
    assert isinstance(instance, standard_Model)

@given(instance=standard_Metamodel_strategy)
@settings(max_examples=50)
def test_standard_metamodel_instantiation(instance):
    assert isinstance(instance, standard_Metamodel)

@given(instance=standard_Subsystem_strategy)
@settings(max_examples=50)
def test_standard_subsystem_instantiation(instance):
    assert isinstance(instance, standard_Subsystem)

@given(instance=standard_Specification_strategy)
@settings(max_examples=50)
def test_standard_specification_instantiation(instance):
    assert isinstance(instance, standard_Specification)

@given(instance=standard_Send_strategy)
@settings(max_examples=50)
def test_standard_send_instantiation(instance):
    assert isinstance(instance, standard_Send)

@given(instance=standard_Artifact_strategy)
@settings(max_examples=50)
def test_standard_artifact_instantiation(instance):
    assert isinstance(instance, standard_Artifact)

@given(instance=standard_Script_strategy)
@settings(max_examples=50)
def test_standard_script_instantiation(instance):
    assert isinstance(instance, standard_Script)

@given(instance=standard_Responsibility_strategy)
@settings(max_examples=50)
def test_standard_responsibility_instantiation(instance):
    assert isinstance(instance, standard_Responsibility)

@given(instance=standard_Refine_strategy)
@settings(max_examples=50)
def test_standard_refine_instantiation(instance):
    assert isinstance(instance, standard_Refine)

@given(instance=standard_ModelLibrary_strategy)
@settings(max_examples=50)
def test_standard_modellibrary_instantiation(instance):
    assert isinstance(instance, standard_ModelLibrary)

@given(instance=standard_Metaclass_strategy)
@settings(max_examples=50)
def test_standard_metaclass_instantiation(instance):
    assert isinstance(instance, standard_Metaclass)

@given(instance=standard_Instantiate_strategy)
@settings(max_examples=50)
def test_standard_instantiate_instantiation(instance):
    assert isinstance(instance, standard_Instantiate)

@given(instance=standard_ImplementationClass_strategy)
@settings(max_examples=50)
def test_standard_implementationclass_instantiation(instance):
    assert isinstance(instance, standard_ImplementationClass)

@given(instance=standard_Implement_strategy)
@settings(max_examples=50)
def test_standard_implement_instantiation(instance):
    assert isinstance(instance, standard_Implement)

@given(instance=standard_Package_strategy)
@settings(max_examples=50)
def test_standard_package_instantiation(instance):
    assert isinstance(instance, standard_Package)

@given(instance=standard_Framework_strategy)
@settings(max_examples=50)
def test_standard_framework_instantiation(instance):
    assert isinstance(instance, standard_Framework)

@given(instance=standard_Focus_strategy)
@settings(max_examples=50)
def test_standard_focus_instantiation(instance):
    assert isinstance(instance, standard_Focus)

@given(instance=standard_Utility_strategy)
@settings(max_examples=50)
def test_standard_utility_instantiation(instance):
    assert isinstance(instance, standard_Utility)

@given(instance=standard_Type_strategy)
@settings(max_examples=50)
def test_standard_type_instantiation(instance):
    assert isinstance(instance, standard_Type)

@given(instance=standard_Trace_strategy)
@settings(max_examples=50)
def test_standard_trace_instantiation(instance):
    assert isinstance(instance, standard_Trace)

@given(instance=standard_Component_strategy)
@settings(max_examples=50)
def test_standard_component_instantiation(instance):
    assert isinstance(instance, standard_Component)

@given(instance=standard_BuildComponent_strategy)
@settings(max_examples=50)
def test_standard_buildcomponent_instantiation(instance):
    assert isinstance(instance, standard_BuildComponent)

@given(instance=standard_Class_strategy)
@settings(max_examples=50)
def test_standard_class_instantiation(instance):
    assert isinstance(instance, standard_Class)

@given(instance=standard_Auxiliary_strategy)
@settings(max_examples=50)
def test_standard_auxiliary_instantiation(instance):
    assert isinstance(instance, standard_Auxiliary)

@given(instance=standard_Destroy_strategy)
@settings(max_examples=50)
def test_standard_destroy_instantiation(instance):
    assert isinstance(instance, standard_Destroy)

@given(instance=standard_Abstraction_strategy)
@settings(max_examples=50)
def test_standard_abstraction_instantiation(instance):
    assert isinstance(instance, standard_Abstraction)

@given(instance=standard_Derive_strategy)
@settings(max_examples=50)
def test_standard_derive_instantiation(instance):
    assert isinstance(instance, standard_Derive)

@given(instance=standard_Call_strategy)
@settings(max_examples=50)
def test_standard_call_instantiation(instance):
    assert isinstance(instance, standard_Call)

@given(instance=standard_Usage_strategy)
@settings(max_examples=50)
def test_standard_usage_instantiation(instance):
    assert isinstance(instance, standard_Usage)

@given(instance=standard_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_standard_behavioralfeature_instantiation(instance):
    assert isinstance(instance, standard_BehavioralFeature)

@given(instance=standard_Create_strategy)
@settings(max_examples=50)
def test_standard_create_instantiation(instance):
    assert isinstance(instance, standard_Create)
