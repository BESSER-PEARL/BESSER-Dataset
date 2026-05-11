import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Type,
    dataflow::TypeList,
    dataflow::TypeUndefined,
    dataflow::TypeString,
    dataflow::TypeDouble,
    dataflow::TypeInt,
    dataflow::TypeBoolean,
    dataflow::TypeUint,
    Variable,
    dataflow::Type,
    dataflow::Version,
    Attributable,
    dataflow::Variable,
    dataflow::Procedure,
    dataflow::Action,
    dataflow::Guard,
    dataflow::Network,
    dataflow::SharedVariable,
    dataflow::Port,
    dataflow::Buffer,
    dataflow::ActorClass,
    dataflow::Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_dataflow::typelist_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeList)


def test_dataflow::typelist_constructor_exists():
    assert callable(dataflow::TypeList.__init__)


def test_dataflow::typelist_constructor_args():
    sig = inspect.signature(dataflow::TypeList.__init__)
    params = list(sig.parameters.keys())
    assert "elements" in params, "Missing parameter 'elements'"

def test_dataflow::typelist_has_elements():
    assert hasattr(dataflow::TypeList, "elements")
    descriptor = None
    for klass in dataflow::TypeList.__mro__:
        if "elements" in klass.__dict__:
            descriptor = klass.__dict__["elements"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typeundefined_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeUndefined)


def test_dataflow::typeundefined_constructor_exists():
    assert callable(dataflow::TypeUndefined.__init__)


def test_dataflow::typeundefined_constructor_args():
    sig = inspect.signature(dataflow::TypeUndefined.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typeundefined_has_size():
    assert hasattr(dataflow::TypeUndefined, "size")
    descriptor = None
    for klass in dataflow::TypeUndefined.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typestring_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeString)


def test_dataflow::typestring_constructor_exists():
    assert callable(dataflow::TypeString.__init__)


def test_dataflow::typestring_constructor_args():
    sig = inspect.signature(dataflow::TypeString.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typestring_has_size():
    assert hasattr(dataflow::TypeString, "size")
    descriptor = None
    for klass in dataflow::TypeString.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typedouble_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeDouble)


def test_dataflow::typedouble_constructor_exists():
    assert callable(dataflow::TypeDouble.__init__)


def test_dataflow::typedouble_constructor_args():
    sig = inspect.signature(dataflow::TypeDouble.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typedouble_has_size():
    assert hasattr(dataflow::TypeDouble, "size")
    descriptor = None
    for klass in dataflow::TypeDouble.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typeint_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeInt)


def test_dataflow::typeint_constructor_exists():
    assert callable(dataflow::TypeInt.__init__)


def test_dataflow::typeint_constructor_args():
    sig = inspect.signature(dataflow::TypeInt.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typeint_has_size():
    assert hasattr(dataflow::TypeInt, "size")
    descriptor = None
    for klass in dataflow::TypeInt.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typeboolean_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeBoolean)


def test_dataflow::typeboolean_constructor_exists():
    assert callable(dataflow::TypeBoolean.__init__)


def test_dataflow::typeboolean_constructor_args():
    sig = inspect.signature(dataflow::TypeBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typeboolean_has_size():
    assert hasattr(dataflow::TypeBoolean, "size")
    descriptor = None
    for klass in dataflow::TypeBoolean.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::typeuint_is_not_abstract():
    assert not inspect.isabstract(dataflow::TypeUint)


def test_dataflow::typeuint_constructor_exists():
    assert callable(dataflow::TypeUint.__init__)


def test_dataflow::typeuint_constructor_args():
    sig = inspect.signature(dataflow::TypeUint.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_dataflow::typeuint_has_size():
    assert hasattr(dataflow::TypeUint, "size")
    descriptor = None
    for klass in dataflow::TypeUint.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_dataflow::type_is_not_abstract():
    assert not inspect.isabstract(dataflow::Type)


def test_dataflow::type_constructor_exists():
    assert callable(dataflow::Type.__init__)


def test_dataflow::type_constructor_args():
    sig = inspect.signature(dataflow::Type.__init__)
    params = list(sig.parameters.keys())
    assert "bits" in params, "Missing parameter 'bits'"
    assert "etype" in params, "Missing parameter 'etype'"

def test_dataflow::type_has_bits():
    assert hasattr(dataflow::Type, "bits")
    descriptor = None
    for klass in dataflow::Type.__mro__:
        if "bits" in klass.__dict__:
            descriptor = klass.__dict__["bits"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::type_has_etype():
    assert hasattr(dataflow::Type, "etype")
    descriptor = None
    for klass in dataflow::Type.__mro__:
        if "etype" in klass.__dict__:
            descriptor = klass.__dict__["etype"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::version_is_not_abstract():
    assert not inspect.isabstract(dataflow::Version)


def test_dataflow::version_constructor_exists():
    assert callable(dataflow::Version.__init__)


def test_dataflow::version_constructor_args():
    sig = inspect.signature(dataflow::Version.__init__)
    params = list(sig.parameters.keys())



def test_attributable_is_not_abstract():
    assert not inspect.isabstract(Attributable)


def test_attributable_constructor_exists():
    assert callable(Attributable.__init__)


def test_attributable_constructor_args():
    sig = inspect.signature(Attributable.__init__)
    params = list(sig.parameters.keys())



def test_dataflow::variable_is_not_abstract():
    assert not inspect.isabstract(dataflow::Variable)


def test_dataflow::variable_constructor_exists():
    assert callable(dataflow::Variable.__init__)


def test_dataflow::variable_constructor_args():
    sig = inspect.signature(dataflow::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shared" in params, "Missing parameter 'shared'"

def test_dataflow::variable_has_name():
    assert hasattr(dataflow::Variable, "name")
    descriptor = None
    for klass in dataflow::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::variable_has_shared():
    assert hasattr(dataflow::Variable, "shared")
    descriptor = None
    for klass in dataflow::Variable.__mro__:
        if "shared" in klass.__dict__:
            descriptor = klass.__dict__["shared"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::procedure_is_not_abstract():
    assert not inspect.isabstract(dataflow::Procedure)


def test_dataflow::procedure_constructor_exists():
    assert callable(dataflow::Procedure.__init__)


def test_dataflow::procedure_constructor_args():
    sig = inspect.signature(dataflow::Procedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dataflow::procedure_has_name():
    assert hasattr(dataflow::Procedure, "name")
    descriptor = None
    for klass in dataflow::Procedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::action_is_not_abstract():
    assert not inspect.isabstract(dataflow::Action)


def test_dataflow::action_constructor_exists():
    assert callable(dataflow::Action.__init__)


def test_dataflow::action_constructor_args():
    sig = inspect.signature(dataflow::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dataflow::action_has_name():
    assert hasattr(dataflow::Action, "name")
    descriptor = None
    for klass in dataflow::Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::guard_is_not_abstract():
    assert not inspect.isabstract(dataflow::Guard)


def test_dataflow::guard_constructor_exists():
    assert callable(dataflow::Guard.__init__)


def test_dataflow::guard_constructor_args():
    sig = inspect.signature(dataflow::Guard.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_dataflow::guard_has_tag():
    assert hasattr(dataflow::Guard, "tag")
    descriptor = None
    for klass in dataflow::Guard.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::network_is_not_abstract():
    assert not inspect.isabstract(dataflow::Network)


def test_dataflow::network_constructor_exists():
    assert callable(dataflow::Network.__init__)


def test_dataflow::network_constructor_args():
    sig = inspect.signature(dataflow::Network.__init__)
    params = list(sig.parameters.keys())
    assert "project" in params, "Missing parameter 'project'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sourceFile" in params, "Missing parameter 'sourceFile'"

def test_dataflow::network_has_project():
    assert hasattr(dataflow::Network, "project")
    descriptor = None
    for klass in dataflow::Network.__mro__:
        if "project" in klass.__dict__:
            descriptor = klass.__dict__["project"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::network_has_name():
    assert hasattr(dataflow::Network, "name")
    descriptor = None
    for klass in dataflow::Network.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::network_has_sourceFile():
    assert hasattr(dataflow::Network, "sourceFile")
    descriptor = None
    for klass in dataflow::Network.__mro__:
        if "sourceFile" in klass.__dict__:
            descriptor = klass.__dict__["sourceFile"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::sharedvariable_is_not_abstract():
    assert not inspect.isabstract(dataflow::SharedVariable)


def test_dataflow::sharedvariable_constructor_exists():
    assert callable(dataflow::SharedVariable.__init__)


def test_dataflow::sharedvariable_constructor_args():
    sig = inspect.signature(dataflow::SharedVariable.__init__)
    params = list(sig.parameters.keys())
    assert "tag" in params, "Missing parameter 'tag'"

def test_dataflow::sharedvariable_has_tag():
    assert hasattr(dataflow::SharedVariable, "tag")
    descriptor = None
    for klass in dataflow::SharedVariable.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::port_is_not_abstract():
    assert not inspect.isabstract(dataflow::Port)


def test_dataflow::port_constructor_exists():
    assert callable(dataflow::Port.__init__)


def test_dataflow::port_constructor_args():
    sig = inspect.signature(dataflow::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dataflow::port_has_name():
    assert hasattr(dataflow::Port, "name")
    descriptor = None
    for klass in dataflow::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::buffer_is_not_abstract():
    assert not inspect.isabstract(dataflow::Buffer)


def test_dataflow::buffer_constructor_exists():
    assert callable(dataflow::Buffer.__init__)


def test_dataflow::buffer_constructor_args():
    sig = inspect.signature(dataflow::Buffer.__init__)
    params = list(sig.parameters.keys())



def test_dataflow::actorclass_is_not_abstract():
    assert not inspect.isabstract(dataflow::ActorClass)


def test_dataflow::actorclass_constructor_exists():
    assert callable(dataflow::ActorClass.__init__)


def test_dataflow::actorclass_constructor_args():
    sig = inspect.signature(dataflow::ActorClass.__init__)
    params = list(sig.parameters.keys())
    assert "nameSpace" in params, "Missing parameter 'nameSpace'"
    assert "sourceFile" in params, "Missing parameter 'sourceFile'"
    assert "name" in params, "Missing parameter 'name'"
    assert "sourceCode" in params, "Missing parameter 'sourceCode'"

def test_dataflow::actorclass_has_nameSpace():
    assert hasattr(dataflow::ActorClass, "nameSpace")
    descriptor = None
    for klass in dataflow::ActorClass.__mro__:
        if "nameSpace" in klass.__dict__:
            descriptor = klass.__dict__["nameSpace"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::actorclass_has_sourceFile():
    assert hasattr(dataflow::ActorClass, "sourceFile")
    descriptor = None
    for klass in dataflow::ActorClass.__mro__:
        if "sourceFile" in klass.__dict__:
            descriptor = klass.__dict__["sourceFile"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::actorclass_has_name():
    assert hasattr(dataflow::ActorClass, "name")
    descriptor = None
    for klass in dataflow::ActorClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dataflow::actorclass_has_sourceCode():
    assert hasattr(dataflow::ActorClass, "sourceCode")
    descriptor = None
    for klass in dataflow::ActorClass.__mro__:
        if "sourceCode" in klass.__dict__:
            descriptor = klass.__dict__["sourceCode"]
            break
    assert isinstance(descriptor, property)



def test_dataflow::actor_is_not_abstract():
    assert not inspect.isabstract(dataflow::Actor)


def test_dataflow::actor_constructor_exists():
    assert callable(dataflow::Actor.__init__)


def test_dataflow::actor_constructor_args():
    sig = inspect.signature(dataflow::Actor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dataflow::actor_has_name():
    assert hasattr(dataflow::Actor, "name")
    descriptor = None
    for klass in dataflow::Actor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Type_strategy = st.builds(
    Type,
)
dataflow::TypeList_strategy = st.builds(
    dataflow::TypeList,
    elements=
        st.integers()
)
dataflow::TypeUndefined_strategy = st.builds(
    dataflow::TypeUndefined,
    size=
        st.integers()
)
dataflow::TypeString_strategy = st.builds(
    dataflow::TypeString,
    size=
        st.integers()
)
dataflow::TypeDouble_strategy = st.builds(
    dataflow::TypeDouble,
    size=
        st.integers()
)
dataflow::TypeInt_strategy = st.builds(
    dataflow::TypeInt,
    size=
        st.integers()
)
dataflow::TypeBoolean_strategy = st.builds(
    dataflow::TypeBoolean,
    size=
        st.integers()
)
dataflow::TypeUint_strategy = st.builds(
    dataflow::TypeUint,
    size=
        st.integers()
)
Variable_strategy = st.builds(
    Variable,
)
dataflow::Type_strategy = st.builds(
    dataflow::Type,
    bits=
        st.integers(),
    etype=
        safe_text
)
dataflow::Version_strategy = st.builds(
    dataflow::Version,
)
Attributable_strategy = st.builds(
    Attributable,
)
dataflow::Variable_strategy = st.builds(
    dataflow::Variable,
    name=
        safe_text,
    shared=
        st.booleans()
)
dataflow::Procedure_strategy = st.builds(
    dataflow::Procedure,
    name=
        safe_text
)
dataflow::Action_strategy = st.builds(
    dataflow::Action,
    name=
        safe_text
)
dataflow::Guard_strategy = st.builds(
    dataflow::Guard,
    tag=
        safe_text
)
dataflow::Network_strategy = st.builds(
    dataflow::Network,
    project=
        safe_text,
    name=
        safe_text,
    sourceFile=
        safe_text
)
dataflow::SharedVariable_strategy = st.builds(
    dataflow::SharedVariable,
    tag=
        safe_text
)
dataflow::Port_strategy = st.builds(
    dataflow::Port,
    name=
        safe_text
)
dataflow::Buffer_strategy = st.builds(
    dataflow::Buffer,
)
dataflow::ActorClass_strategy = st.builds(
    dataflow::ActorClass,
    nameSpace=
        safe_text,
    sourceFile=
        safe_text,
    name=
        safe_text,
    sourceCode=
        safe_text
)
dataflow::Actor_strategy = st.builds(
    dataflow::Actor,
    name=
        safe_text
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=dataflow::TypeList_strategy)
@settings(max_examples=50)
def test_dataflow::typelist_instantiation(instance):
    assert isinstance(instance, dataflow::TypeList)

@given(instance=dataflow::TypeList_strategy)
def test_dataflow::typelist_elements_type(instance):
    assert isinstance(instance.elements, int)


@given(instance=dataflow::TypeList_strategy)
def test_dataflow::typelist_elements_setter(instance):
    original = instance.elements
    instance.elements = original
    assert instance.elements == original

@given(instance=dataflow::TypeUndefined_strategy)
@settings(max_examples=50)
def test_dataflow::typeundefined_instantiation(instance):
    assert isinstance(instance, dataflow::TypeUndefined)

@given(instance=dataflow::TypeUndefined_strategy)
def test_dataflow::typeundefined_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeUndefined_strategy)
def test_dataflow::typeundefined_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dataflow::TypeString_strategy)
@settings(max_examples=50)
def test_dataflow::typestring_instantiation(instance):
    assert isinstance(instance, dataflow::TypeString)

@given(instance=dataflow::TypeString_strategy)
def test_dataflow::typestring_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeString_strategy)
def test_dataflow::typestring_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dataflow::TypeDouble_strategy)
@settings(max_examples=50)
def test_dataflow::typedouble_instantiation(instance):
    assert isinstance(instance, dataflow::TypeDouble)

@given(instance=dataflow::TypeDouble_strategy)
def test_dataflow::typedouble_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeDouble_strategy)
def test_dataflow::typedouble_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dataflow::TypeInt_strategy)
@settings(max_examples=50)
def test_dataflow::typeint_instantiation(instance):
    assert isinstance(instance, dataflow::TypeInt)

@given(instance=dataflow::TypeInt_strategy)
def test_dataflow::typeint_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeInt_strategy)
def test_dataflow::typeint_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dataflow::TypeBoolean_strategy)
@settings(max_examples=50)
def test_dataflow::typeboolean_instantiation(instance):
    assert isinstance(instance, dataflow::TypeBoolean)

@given(instance=dataflow::TypeBoolean_strategy)
def test_dataflow::typeboolean_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeBoolean_strategy)
def test_dataflow::typeboolean_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=dataflow::TypeUint_strategy)
@settings(max_examples=50)
def test_dataflow::typeuint_instantiation(instance):
    assert isinstance(instance, dataflow::TypeUint)

@given(instance=dataflow::TypeUint_strategy)
def test_dataflow::typeuint_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=dataflow::TypeUint_strategy)
def test_dataflow::typeuint_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=dataflow::Type_strategy)
@settings(max_examples=50)
def test_dataflow::type_instantiation(instance):
    assert isinstance(instance, dataflow::Type)

@given(instance=dataflow::Type_strategy)
def test_dataflow::type_bits_type(instance):
    assert isinstance(instance.bits, int)


@given(instance=dataflow::Type_strategy)
def test_dataflow::type_bits_setter(instance):
    original = instance.bits
    instance.bits = original
    assert instance.bits == original

@given(instance=dataflow::Type_strategy)
def test_dataflow::type_etype_type(instance):
    assert isinstance(instance.etype, str)


@given(instance=dataflow::Type_strategy)
def test_dataflow::type_etype_setter(instance):
    original = instance.etype
    instance.etype = original
    assert instance.etype == original

@given(instance=dataflow::Version_strategy)
@settings(max_examples=50)
def test_dataflow::version_instantiation(instance):
    assert isinstance(instance, dataflow::Version)

@given(instance=Attributable_strategy)
@settings(max_examples=50)
def test_attributable_instantiation(instance):
    assert isinstance(instance, Attributable)

@given(instance=dataflow::Variable_strategy)
@settings(max_examples=50)
def test_dataflow::variable_instantiation(instance):
    assert isinstance(instance, dataflow::Variable)

@given(instance=dataflow::Variable_strategy)
def test_dataflow::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Variable_strategy)
def test_dataflow::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::Variable_strategy)
def test_dataflow::variable_shared_type(instance):
    assert isinstance(instance.shared, bool)


@given(instance=dataflow::Variable_strategy)
def test_dataflow::variable_shared_setter(instance):
    original = instance.shared
    instance.shared = original
    assert instance.shared == original

@given(instance=dataflow::Procedure_strategy)
@settings(max_examples=50)
def test_dataflow::procedure_instantiation(instance):
    assert isinstance(instance, dataflow::Procedure)

@given(instance=dataflow::Procedure_strategy)
def test_dataflow::procedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Procedure_strategy)
def test_dataflow::procedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::Action_strategy)
@settings(max_examples=50)
def test_dataflow::action_instantiation(instance):
    assert isinstance(instance, dataflow::Action)

@given(instance=dataflow::Action_strategy)
def test_dataflow::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Action_strategy)
def test_dataflow::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::Guard_strategy)
@settings(max_examples=50)
def test_dataflow::guard_instantiation(instance):
    assert isinstance(instance, dataflow::Guard)

@given(instance=dataflow::Guard_strategy)
def test_dataflow::guard_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=dataflow::Guard_strategy)
def test_dataflow::guard_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=dataflow::Network_strategy)
@settings(max_examples=50)
def test_dataflow::network_instantiation(instance):
    assert isinstance(instance, dataflow::Network)

@given(instance=dataflow::Network_strategy)
def test_dataflow::network_project_type(instance):
    assert isinstance(instance.project, str)


@given(instance=dataflow::Network_strategy)
def test_dataflow::network_project_setter(instance):
    original = instance.project
    instance.project = original
    assert instance.project == original

@given(instance=dataflow::Network_strategy)
def test_dataflow::network_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Network_strategy)
def test_dataflow::network_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::Network_strategy)
def test_dataflow::network_sourceFile_type(instance):
    assert isinstance(instance.sourceFile, str)


@given(instance=dataflow::Network_strategy)
def test_dataflow::network_sourceFile_setter(instance):
    original = instance.sourceFile
    instance.sourceFile = original
    assert instance.sourceFile == original

@given(instance=dataflow::SharedVariable_strategy)
@settings(max_examples=50)
def test_dataflow::sharedvariable_instantiation(instance):
    assert isinstance(instance, dataflow::SharedVariable)

@given(instance=dataflow::SharedVariable_strategy)
def test_dataflow::sharedvariable_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=dataflow::SharedVariable_strategy)
def test_dataflow::sharedvariable_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original

@given(instance=dataflow::Port_strategy)
@settings(max_examples=50)
def test_dataflow::port_instantiation(instance):
    assert isinstance(instance, dataflow::Port)

@given(instance=dataflow::Port_strategy)
def test_dataflow::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Port_strategy)
def test_dataflow::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::Buffer_strategy)
@settings(max_examples=50)
def test_dataflow::buffer_instantiation(instance):
    assert isinstance(instance, dataflow::Buffer)

@given(instance=dataflow::ActorClass_strategy)
@settings(max_examples=50)
def test_dataflow::actorclass_instantiation(instance):
    assert isinstance(instance, dataflow::ActorClass)

@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_nameSpace_type(instance):
    assert isinstance(instance.nameSpace, str)


@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_nameSpace_setter(instance):
    original = instance.nameSpace
    instance.nameSpace = original
    assert instance.nameSpace == original

@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_sourceFile_type(instance):
    assert isinstance(instance.sourceFile, str)


@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_sourceFile_setter(instance):
    original = instance.sourceFile
    instance.sourceFile = original
    assert instance.sourceFile == original

@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_sourceCode_type(instance):
    assert isinstance(instance.sourceCode, str)


@given(instance=dataflow::ActorClass_strategy)
def test_dataflow::actorclass_sourceCode_setter(instance):
    original = instance.sourceCode
    instance.sourceCode = original
    assert instance.sourceCode == original

@given(instance=dataflow::Actor_strategy)
@settings(max_examples=50)
def test_dataflow::actor_instantiation(instance):
    assert isinstance(instance, dataflow::Actor)

@given(instance=dataflow::Actor_strategy)
def test_dataflow::actor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dataflow::Actor_strategy)
def test_dataflow::actor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
