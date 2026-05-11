import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    standard::Abstraction,
    standard::Derive,
    standard::Call,
    standard::Usage,
    standard::BehavioralFeature,
    standard::Create,
    standard::Source,
    standard::Service,
    standard::Classifier,
    standard::Realization,
    standard::Process,
    standard::Library,
    standard::File,
    standard::Executable,
    standard::Entity,
    standard::Document,
    standard::SystemModel,
    standard::Model,
    standard::Metamodel,
    standard::Subsystem,
    standard::Specification,
    standard::Send,
    standard::Artifact,
    standard::Script,
    standard::Responsibility,
    standard::Refine,
    standard::ModelLibrary,
    standard::Metaclass,
    standard::Instantiate,
    standard::ImplementationClass,
    standard::Implement,
    standard::Package,
    standard::Framework,
    standard::Focus,
    standard::Utility,
    standard::Type,
    standard::Trace,
    standard::Component,
    standard::BuildComponent,
    standard::Class,
    standard::Auxiliary,
    standard::Destroy,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_standard::abstraction_is_not_abstract():
    assert not inspect.isabstract(standard::Abstraction)


def test_standard::abstraction_constructor_exists():
    assert callable(standard::Abstraction.__init__)


def test_standard::abstraction_constructor_args():
    sig = inspect.signature(standard::Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_standard::derive_is_not_abstract():
    assert not inspect.isabstract(standard::Derive)


def test_standard::derive_constructor_exists():
    assert callable(standard::Derive.__init__)


def test_standard::derive_constructor_args():
    sig = inspect.signature(standard::Derive.__init__)
    params = list(sig.parameters.keys())



def test_standard::call_is_not_abstract():
    assert not inspect.isabstract(standard::Call)


def test_standard::call_constructor_exists():
    assert callable(standard::Call.__init__)


def test_standard::call_constructor_args():
    sig = inspect.signature(standard::Call.__init__)
    params = list(sig.parameters.keys())



def test_standard::usage_is_not_abstract():
    assert not inspect.isabstract(standard::Usage)


def test_standard::usage_constructor_exists():
    assert callable(standard::Usage.__init__)


def test_standard::usage_constructor_args():
    sig = inspect.signature(standard::Usage.__init__)
    params = list(sig.parameters.keys())



def test_standard::behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(standard::BehavioralFeature)


def test_standard::behavioralfeature_constructor_exists():
    assert callable(standard::BehavioralFeature.__init__)


def test_standard::behavioralfeature_constructor_args():
    sig = inspect.signature(standard::BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_standard::create_is_not_abstract():
    assert not inspect.isabstract(standard::Create)


def test_standard::create_constructor_exists():
    assert callable(standard::Create.__init__)


def test_standard::create_constructor_args():
    sig = inspect.signature(standard::Create.__init__)
    params = list(sig.parameters.keys())



def test_standard::source_is_not_abstract():
    assert not inspect.isabstract(standard::Source)


def test_standard::source_constructor_exists():
    assert callable(standard::Source.__init__)


def test_standard::source_constructor_args():
    sig = inspect.signature(standard::Source.__init__)
    params = list(sig.parameters.keys())



def test_standard::service_is_not_abstract():
    assert not inspect.isabstract(standard::Service)


def test_standard::service_constructor_exists():
    assert callable(standard::Service.__init__)


def test_standard::service_constructor_args():
    sig = inspect.signature(standard::Service.__init__)
    params = list(sig.parameters.keys())



def test_standard::classifier_is_not_abstract():
    assert not inspect.isabstract(standard::Classifier)


def test_standard::classifier_constructor_exists():
    assert callable(standard::Classifier.__init__)


def test_standard::classifier_constructor_args():
    sig = inspect.signature(standard::Classifier.__init__)
    params = list(sig.parameters.keys())



def test_standard::realization_is_not_abstract():
    assert not inspect.isabstract(standard::Realization)


def test_standard::realization_constructor_exists():
    assert callable(standard::Realization.__init__)


def test_standard::realization_constructor_args():
    sig = inspect.signature(standard::Realization.__init__)
    params = list(sig.parameters.keys())



def test_standard::process_is_not_abstract():
    assert not inspect.isabstract(standard::Process)


def test_standard::process_constructor_exists():
    assert callable(standard::Process.__init__)


def test_standard::process_constructor_args():
    sig = inspect.signature(standard::Process.__init__)
    params = list(sig.parameters.keys())



def test_standard::library_is_not_abstract():
    assert not inspect.isabstract(standard::Library)


def test_standard::library_constructor_exists():
    assert callable(standard::Library.__init__)


def test_standard::library_constructor_args():
    sig = inspect.signature(standard::Library.__init__)
    params = list(sig.parameters.keys())



def test_standard::file_is_not_abstract():
    assert not inspect.isabstract(standard::File)


def test_standard::file_constructor_exists():
    assert callable(standard::File.__init__)


def test_standard::file_constructor_args():
    sig = inspect.signature(standard::File.__init__)
    params = list(sig.parameters.keys())



def test_standard::executable_is_not_abstract():
    assert not inspect.isabstract(standard::Executable)


def test_standard::executable_constructor_exists():
    assert callable(standard::Executable.__init__)


def test_standard::executable_constructor_args():
    sig = inspect.signature(standard::Executable.__init__)
    params = list(sig.parameters.keys())



def test_standard::entity_is_not_abstract():
    assert not inspect.isabstract(standard::Entity)


def test_standard::entity_constructor_exists():
    assert callable(standard::Entity.__init__)


def test_standard::entity_constructor_args():
    sig = inspect.signature(standard::Entity.__init__)
    params = list(sig.parameters.keys())



def test_standard::document_is_not_abstract():
    assert not inspect.isabstract(standard::Document)


def test_standard::document_constructor_exists():
    assert callable(standard::Document.__init__)


def test_standard::document_constructor_args():
    sig = inspect.signature(standard::Document.__init__)
    params = list(sig.parameters.keys())



def test_standard::systemmodel_is_not_abstract():
    assert not inspect.isabstract(standard::SystemModel)


def test_standard::systemmodel_constructor_exists():
    assert callable(standard::SystemModel.__init__)


def test_standard::systemmodel_constructor_args():
    sig = inspect.signature(standard::SystemModel.__init__)
    params = list(sig.parameters.keys())



def test_standard::model_is_not_abstract():
    assert not inspect.isabstract(standard::Model)


def test_standard::model_constructor_exists():
    assert callable(standard::Model.__init__)


def test_standard::model_constructor_args():
    sig = inspect.signature(standard::Model.__init__)
    params = list(sig.parameters.keys())



def test_standard::metamodel_is_not_abstract():
    assert not inspect.isabstract(standard::Metamodel)


def test_standard::metamodel_constructor_exists():
    assert callable(standard::Metamodel.__init__)


def test_standard::metamodel_constructor_args():
    sig = inspect.signature(standard::Metamodel.__init__)
    params = list(sig.parameters.keys())



def test_standard::subsystem_is_not_abstract():
    assert not inspect.isabstract(standard::Subsystem)


def test_standard::subsystem_constructor_exists():
    assert callable(standard::Subsystem.__init__)


def test_standard::subsystem_constructor_args():
    sig = inspect.signature(standard::Subsystem.__init__)
    params = list(sig.parameters.keys())



def test_standard::specification_is_not_abstract():
    assert not inspect.isabstract(standard::Specification)


def test_standard::specification_constructor_exists():
    assert callable(standard::Specification.__init__)


def test_standard::specification_constructor_args():
    sig = inspect.signature(standard::Specification.__init__)
    params = list(sig.parameters.keys())



def test_standard::send_is_not_abstract():
    assert not inspect.isabstract(standard::Send)


def test_standard::send_constructor_exists():
    assert callable(standard::Send.__init__)


def test_standard::send_constructor_args():
    sig = inspect.signature(standard::Send.__init__)
    params = list(sig.parameters.keys())



def test_standard::artifact_is_not_abstract():
    assert not inspect.isabstract(standard::Artifact)


def test_standard::artifact_constructor_exists():
    assert callable(standard::Artifact.__init__)


def test_standard::artifact_constructor_args():
    sig = inspect.signature(standard::Artifact.__init__)
    params = list(sig.parameters.keys())



def test_standard::script_is_not_abstract():
    assert not inspect.isabstract(standard::Script)


def test_standard::script_constructor_exists():
    assert callable(standard::Script.__init__)


def test_standard::script_constructor_args():
    sig = inspect.signature(standard::Script.__init__)
    params = list(sig.parameters.keys())



def test_standard::responsibility_is_not_abstract():
    assert not inspect.isabstract(standard::Responsibility)


def test_standard::responsibility_constructor_exists():
    assert callable(standard::Responsibility.__init__)


def test_standard::responsibility_constructor_args():
    sig = inspect.signature(standard::Responsibility.__init__)
    params = list(sig.parameters.keys())



def test_standard::refine_is_not_abstract():
    assert not inspect.isabstract(standard::Refine)


def test_standard::refine_constructor_exists():
    assert callable(standard::Refine.__init__)


def test_standard::refine_constructor_args():
    sig = inspect.signature(standard::Refine.__init__)
    params = list(sig.parameters.keys())



def test_standard::modellibrary_is_not_abstract():
    assert not inspect.isabstract(standard::ModelLibrary)


def test_standard::modellibrary_constructor_exists():
    assert callable(standard::ModelLibrary.__init__)


def test_standard::modellibrary_constructor_args():
    sig = inspect.signature(standard::ModelLibrary.__init__)
    params = list(sig.parameters.keys())



def test_standard::metaclass_is_not_abstract():
    assert not inspect.isabstract(standard::Metaclass)


def test_standard::metaclass_constructor_exists():
    assert callable(standard::Metaclass.__init__)


def test_standard::metaclass_constructor_args():
    sig = inspect.signature(standard::Metaclass.__init__)
    params = list(sig.parameters.keys())



def test_standard::instantiate_is_not_abstract():
    assert not inspect.isabstract(standard::Instantiate)


def test_standard::instantiate_constructor_exists():
    assert callable(standard::Instantiate.__init__)


def test_standard::instantiate_constructor_args():
    sig = inspect.signature(standard::Instantiate.__init__)
    params = list(sig.parameters.keys())



def test_standard::implementationclass_is_not_abstract():
    assert not inspect.isabstract(standard::ImplementationClass)


def test_standard::implementationclass_constructor_exists():
    assert callable(standard::ImplementationClass.__init__)


def test_standard::implementationclass_constructor_args():
    sig = inspect.signature(standard::ImplementationClass.__init__)
    params = list(sig.parameters.keys())



def test_standard::implement_is_not_abstract():
    assert not inspect.isabstract(standard::Implement)


def test_standard::implement_constructor_exists():
    assert callable(standard::Implement.__init__)


def test_standard::implement_constructor_args():
    sig = inspect.signature(standard::Implement.__init__)
    params = list(sig.parameters.keys())



def test_standard::package_is_not_abstract():
    assert not inspect.isabstract(standard::Package)


def test_standard::package_constructor_exists():
    assert callable(standard::Package.__init__)


def test_standard::package_constructor_args():
    sig = inspect.signature(standard::Package.__init__)
    params = list(sig.parameters.keys())



def test_standard::framework_is_not_abstract():
    assert not inspect.isabstract(standard::Framework)


def test_standard::framework_constructor_exists():
    assert callable(standard::Framework.__init__)


def test_standard::framework_constructor_args():
    sig = inspect.signature(standard::Framework.__init__)
    params = list(sig.parameters.keys())



def test_standard::focus_is_not_abstract():
    assert not inspect.isabstract(standard::Focus)


def test_standard::focus_constructor_exists():
    assert callable(standard::Focus.__init__)


def test_standard::focus_constructor_args():
    sig = inspect.signature(standard::Focus.__init__)
    params = list(sig.parameters.keys())



def test_standard::utility_is_not_abstract():
    assert not inspect.isabstract(standard::Utility)


def test_standard::utility_constructor_exists():
    assert callable(standard::Utility.__init__)


def test_standard::utility_constructor_args():
    sig = inspect.signature(standard::Utility.__init__)
    params = list(sig.parameters.keys())



def test_standard::type_is_not_abstract():
    assert not inspect.isabstract(standard::Type)


def test_standard::type_constructor_exists():
    assert callable(standard::Type.__init__)


def test_standard::type_constructor_args():
    sig = inspect.signature(standard::Type.__init__)
    params = list(sig.parameters.keys())



def test_standard::trace_is_not_abstract():
    assert not inspect.isabstract(standard::Trace)


def test_standard::trace_constructor_exists():
    assert callable(standard::Trace.__init__)


def test_standard::trace_constructor_args():
    sig = inspect.signature(standard::Trace.__init__)
    params = list(sig.parameters.keys())



def test_standard::component_is_not_abstract():
    assert not inspect.isabstract(standard::Component)


def test_standard::component_constructor_exists():
    assert callable(standard::Component.__init__)


def test_standard::component_constructor_args():
    sig = inspect.signature(standard::Component.__init__)
    params = list(sig.parameters.keys())



def test_standard::buildcomponent_is_not_abstract():
    assert not inspect.isabstract(standard::BuildComponent)


def test_standard::buildcomponent_constructor_exists():
    assert callable(standard::BuildComponent.__init__)


def test_standard::buildcomponent_constructor_args():
    sig = inspect.signature(standard::BuildComponent.__init__)
    params = list(sig.parameters.keys())



def test_standard::class_is_not_abstract():
    assert not inspect.isabstract(standard::Class)


def test_standard::class_constructor_exists():
    assert callable(standard::Class.__init__)


def test_standard::class_constructor_args():
    sig = inspect.signature(standard::Class.__init__)
    params = list(sig.parameters.keys())



def test_standard::auxiliary_is_not_abstract():
    assert not inspect.isabstract(standard::Auxiliary)


def test_standard::auxiliary_constructor_exists():
    assert callable(standard::Auxiliary.__init__)


def test_standard::auxiliary_constructor_args():
    sig = inspect.signature(standard::Auxiliary.__init__)
    params = list(sig.parameters.keys())



def test_standard::destroy_is_not_abstract():
    assert not inspect.isabstract(standard::Destroy)


def test_standard::destroy_constructor_exists():
    assert callable(standard::Destroy.__init__)


def test_standard::destroy_constructor_args():
    sig = inspect.signature(standard::Destroy.__init__)
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
standard::Abstraction_strategy = st.builds(
    standard::Abstraction,
)
standard::Derive_strategy = st.builds(
    standard::Derive,
)
standard::Call_strategy = st.builds(
    standard::Call,
)
standard::Usage_strategy = st.builds(
    standard::Usage,
)
standard::BehavioralFeature_strategy = st.builds(
    standard::BehavioralFeature,
)
standard::Create_strategy = st.builds(
    standard::Create,
)
standard::Source_strategy = st.builds(
    standard::Source,
)
standard::Service_strategy = st.builds(
    standard::Service,
)
standard::Classifier_strategy = st.builds(
    standard::Classifier,
)
standard::Realization_strategy = st.builds(
    standard::Realization,
)
standard::Process_strategy = st.builds(
    standard::Process,
)
standard::Library_strategy = st.builds(
    standard::Library,
)
standard::File_strategy = st.builds(
    standard::File,
)
standard::Executable_strategy = st.builds(
    standard::Executable,
)
standard::Entity_strategy = st.builds(
    standard::Entity,
)
standard::Document_strategy = st.builds(
    standard::Document,
)
standard::SystemModel_strategy = st.builds(
    standard::SystemModel,
)
standard::Model_strategy = st.builds(
    standard::Model,
)
standard::Metamodel_strategy = st.builds(
    standard::Metamodel,
)
standard::Subsystem_strategy = st.builds(
    standard::Subsystem,
)
standard::Specification_strategy = st.builds(
    standard::Specification,
)
standard::Send_strategy = st.builds(
    standard::Send,
)
standard::Artifact_strategy = st.builds(
    standard::Artifact,
)
standard::Script_strategy = st.builds(
    standard::Script,
)
standard::Responsibility_strategy = st.builds(
    standard::Responsibility,
)
standard::Refine_strategy = st.builds(
    standard::Refine,
)
standard::ModelLibrary_strategy = st.builds(
    standard::ModelLibrary,
)
standard::Metaclass_strategy = st.builds(
    standard::Metaclass,
)
standard::Instantiate_strategy = st.builds(
    standard::Instantiate,
)
standard::ImplementationClass_strategy = st.builds(
    standard::ImplementationClass,
)
standard::Implement_strategy = st.builds(
    standard::Implement,
)
standard::Package_strategy = st.builds(
    standard::Package,
)
standard::Framework_strategy = st.builds(
    standard::Framework,
)
standard::Focus_strategy = st.builds(
    standard::Focus,
)
standard::Utility_strategy = st.builds(
    standard::Utility,
)
standard::Type_strategy = st.builds(
    standard::Type,
)
standard::Trace_strategy = st.builds(
    standard::Trace,
)
standard::Component_strategy = st.builds(
    standard::Component,
)
standard::BuildComponent_strategy = st.builds(
    standard::BuildComponent,
)
standard::Class_strategy = st.builds(
    standard::Class,
)
standard::Auxiliary_strategy = st.builds(
    standard::Auxiliary,
)
standard::Destroy_strategy = st.builds(
    standard::Destroy,
)

@given(instance=standard::Abstraction_strategy)
@settings(max_examples=50)
def test_standard::abstraction_instantiation(instance):
    assert isinstance(instance, standard::Abstraction)

@given(instance=standard::Derive_strategy)
@settings(max_examples=50)
def test_standard::derive_instantiation(instance):
    assert isinstance(instance, standard::Derive)

@given(instance=standard::Call_strategy)
@settings(max_examples=50)
def test_standard::call_instantiation(instance):
    assert isinstance(instance, standard::Call)

@given(instance=standard::Usage_strategy)
@settings(max_examples=50)
def test_standard::usage_instantiation(instance):
    assert isinstance(instance, standard::Usage)

@given(instance=standard::BehavioralFeature_strategy)
@settings(max_examples=50)
def test_standard::behavioralfeature_instantiation(instance):
    assert isinstance(instance, standard::BehavioralFeature)

@given(instance=standard::Create_strategy)
@settings(max_examples=50)
def test_standard::create_instantiation(instance):
    assert isinstance(instance, standard::Create)

@given(instance=standard::Source_strategy)
@settings(max_examples=50)
def test_standard::source_instantiation(instance):
    assert isinstance(instance, standard::Source)

@given(instance=standard::Service_strategy)
@settings(max_examples=50)
def test_standard::service_instantiation(instance):
    assert isinstance(instance, standard::Service)

@given(instance=standard::Classifier_strategy)
@settings(max_examples=50)
def test_standard::classifier_instantiation(instance):
    assert isinstance(instance, standard::Classifier)

@given(instance=standard::Realization_strategy)
@settings(max_examples=50)
def test_standard::realization_instantiation(instance):
    assert isinstance(instance, standard::Realization)

@given(instance=standard::Process_strategy)
@settings(max_examples=50)
def test_standard::process_instantiation(instance):
    assert isinstance(instance, standard::Process)

@given(instance=standard::Library_strategy)
@settings(max_examples=50)
def test_standard::library_instantiation(instance):
    assert isinstance(instance, standard::Library)

@given(instance=standard::File_strategy)
@settings(max_examples=50)
def test_standard::file_instantiation(instance):
    assert isinstance(instance, standard::File)

@given(instance=standard::Executable_strategy)
@settings(max_examples=50)
def test_standard::executable_instantiation(instance):
    assert isinstance(instance, standard::Executable)

@given(instance=standard::Entity_strategy)
@settings(max_examples=50)
def test_standard::entity_instantiation(instance):
    assert isinstance(instance, standard::Entity)

@given(instance=standard::Document_strategy)
@settings(max_examples=50)
def test_standard::document_instantiation(instance):
    assert isinstance(instance, standard::Document)

@given(instance=standard::SystemModel_strategy)
@settings(max_examples=50)
def test_standard::systemmodel_instantiation(instance):
    assert isinstance(instance, standard::SystemModel)

@given(instance=standard::Model_strategy)
@settings(max_examples=50)
def test_standard::model_instantiation(instance):
    assert isinstance(instance, standard::Model)

@given(instance=standard::Metamodel_strategy)
@settings(max_examples=50)
def test_standard::metamodel_instantiation(instance):
    assert isinstance(instance, standard::Metamodel)

@given(instance=standard::Subsystem_strategy)
@settings(max_examples=50)
def test_standard::subsystem_instantiation(instance):
    assert isinstance(instance, standard::Subsystem)

@given(instance=standard::Specification_strategy)
@settings(max_examples=50)
def test_standard::specification_instantiation(instance):
    assert isinstance(instance, standard::Specification)

@given(instance=standard::Send_strategy)
@settings(max_examples=50)
def test_standard::send_instantiation(instance):
    assert isinstance(instance, standard::Send)

@given(instance=standard::Artifact_strategy)
@settings(max_examples=50)
def test_standard::artifact_instantiation(instance):
    assert isinstance(instance, standard::Artifact)

@given(instance=standard::Script_strategy)
@settings(max_examples=50)
def test_standard::script_instantiation(instance):
    assert isinstance(instance, standard::Script)

@given(instance=standard::Responsibility_strategy)
@settings(max_examples=50)
def test_standard::responsibility_instantiation(instance):
    assert isinstance(instance, standard::Responsibility)

@given(instance=standard::Refine_strategy)
@settings(max_examples=50)
def test_standard::refine_instantiation(instance):
    assert isinstance(instance, standard::Refine)

@given(instance=standard::ModelLibrary_strategy)
@settings(max_examples=50)
def test_standard::modellibrary_instantiation(instance):
    assert isinstance(instance, standard::ModelLibrary)

@given(instance=standard::Metaclass_strategy)
@settings(max_examples=50)
def test_standard::metaclass_instantiation(instance):
    assert isinstance(instance, standard::Metaclass)

@given(instance=standard::Instantiate_strategy)
@settings(max_examples=50)
def test_standard::instantiate_instantiation(instance):
    assert isinstance(instance, standard::Instantiate)

@given(instance=standard::ImplementationClass_strategy)
@settings(max_examples=50)
def test_standard::implementationclass_instantiation(instance):
    assert isinstance(instance, standard::ImplementationClass)

@given(instance=standard::Implement_strategy)
@settings(max_examples=50)
def test_standard::implement_instantiation(instance):
    assert isinstance(instance, standard::Implement)

@given(instance=standard::Package_strategy)
@settings(max_examples=50)
def test_standard::package_instantiation(instance):
    assert isinstance(instance, standard::Package)

@given(instance=standard::Framework_strategy)
@settings(max_examples=50)
def test_standard::framework_instantiation(instance):
    assert isinstance(instance, standard::Framework)

@given(instance=standard::Focus_strategy)
@settings(max_examples=50)
def test_standard::focus_instantiation(instance):
    assert isinstance(instance, standard::Focus)

@given(instance=standard::Utility_strategy)
@settings(max_examples=50)
def test_standard::utility_instantiation(instance):
    assert isinstance(instance, standard::Utility)

@given(instance=standard::Type_strategy)
@settings(max_examples=50)
def test_standard::type_instantiation(instance):
    assert isinstance(instance, standard::Type)

@given(instance=standard::Trace_strategy)
@settings(max_examples=50)
def test_standard::trace_instantiation(instance):
    assert isinstance(instance, standard::Trace)

@given(instance=standard::Component_strategy)
@settings(max_examples=50)
def test_standard::component_instantiation(instance):
    assert isinstance(instance, standard::Component)

@given(instance=standard::BuildComponent_strategy)
@settings(max_examples=50)
def test_standard::buildcomponent_instantiation(instance):
    assert isinstance(instance, standard::BuildComponent)

@given(instance=standard::Class_strategy)
@settings(max_examples=50)
def test_standard::class_instantiation(instance):
    assert isinstance(instance, standard::Class)

@given(instance=standard::Auxiliary_strategy)
@settings(max_examples=50)
def test_standard::auxiliary_instantiation(instance):
    assert isinstance(instance, standard::Auxiliary)

@given(instance=standard::Destroy_strategy)
@settings(max_examples=50)
def test_standard::destroy_instantiation(instance):
    assert isinstance(instance, standard::Destroy)
