import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Relational::EnumeratedLiteral,
    Domain,
    Relational::EnumerationType,
    Relational::PrimitiveType,
    CandidateKey,
    Relational::Schema,
    Relational::ForeignKey,
    Relational::Attribute,
    Relational::CandidateKey,
    Relational::Constraint,
    Relational::Domain,
    Relational::Table,
    AttributeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational::enumeratedliteral_is_not_abstract():
    assert not inspect.isabstract(Relational::EnumeratedLiteral)


def test_relational::enumeratedliteral_constructor_exists():
    assert callable(Relational::EnumeratedLiteral.__init__)


def test_relational::enumeratedliteral_constructor_args():
    sig = inspect.signature(Relational::EnumeratedLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::enumeratedliteral_has_name():
    assert hasattr(Relational::EnumeratedLiteral, "name")
    descriptor = None
    for klass in Relational::EnumeratedLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_domain_is_not_abstract():
    assert not inspect.isabstract(Domain)


def test_domain_constructor_exists():
    assert callable(Domain.__init__)


def test_domain_constructor_args():
    sig = inspect.signature(Domain.__init__)
    params = list(sig.parameters.keys())



def test_relational::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(Relational::EnumerationType)


def test_relational::enumerationtype_constructor_exists():
    assert callable(Relational::EnumerationType.__init__)


def test_relational::enumerationtype_constructor_args():
    sig = inspect.signature(Relational::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_relational::primitivetype_is_not_abstract():
    assert not inspect.isabstract(Relational::PrimitiveType)


def test_relational::primitivetype_constructor_exists():
    assert callable(Relational::PrimitiveType.__init__)


def test_relational::primitivetype_constructor_args():
    sig = inspect.signature(Relational::PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_candidatekey_is_not_abstract():
    assert not inspect.isabstract(CandidateKey)


def test_candidatekey_constructor_exists():
    assert callable(CandidateKey.__init__)


def test_candidatekey_constructor_args():
    sig = inspect.signature(CandidateKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::schema_is_not_abstract():
    assert not inspect.isabstract(Relational::Schema)


def test_relational::schema_constructor_exists():
    assert callable(Relational::Schema.__init__)


def test_relational::schema_constructor_args():
    sig = inspect.signature(Relational::Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::schema_has_name():
    assert hasattr(Relational::Schema, "name")
    descriptor = None
    for klass in Relational::Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::foreignkey_is_not_abstract():
    assert not inspect.isabstract(Relational::ForeignKey)


def test_relational::foreignkey_constructor_exists():
    assert callable(Relational::ForeignKey.__init__)


def test_relational::foreignkey_constructor_args():
    sig = inspect.signature(Relational::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational::attribute_is_not_abstract():
    assert not inspect.isabstract(Relational::Attribute)


def test_relational::attribute_constructor_exists():
    assert callable(Relational::Attribute.__init__)


def test_relational::attribute_constructor_args():
    sig = inspect.signature(Relational::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "type" in params, "Missing parameter 'type'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_relational::attribute_has_name():
    assert hasattr(Relational::Attribute, "name")
    descriptor = None
    for klass in Relational::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational::attribute_has_multiplicity():
    assert hasattr(Relational::Attribute, "multiplicity")
    descriptor = None
    for klass in Relational::Attribute.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_relational::attribute_has_type():
    assert hasattr(Relational::Attribute, "type")
    descriptor = None
    for klass in Relational::Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_relational::attribute_has_nullable():
    assert hasattr(Relational::Attribute, "nullable")
    descriptor = None
    for klass in Relational::Attribute.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_relational::candidatekey_is_not_abstract():
    assert not inspect.isabstract(Relational::CandidateKey)


def test_relational::candidatekey_constructor_exists():
    assert callable(Relational::CandidateKey.__init__)


def test_relational::candidatekey_constructor_args():
    sig = inspect.signature(Relational::CandidateKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::candidatekey_has_name():
    assert hasattr(Relational::CandidateKey, "name")
    descriptor = None
    for klass in Relational::CandidateKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::constraint_is_not_abstract():
    assert not inspect.isabstract(Relational::Constraint)


def test_relational::constraint_constructor_exists():
    assert callable(Relational::Constraint.__init__)


def test_relational::constraint_constructor_args():
    sig = inspect.signature(Relational::Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational::constraint_has_description():
    assert hasattr(Relational::Constraint, "description")
    descriptor = None
    for klass in Relational::Constraint.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_relational::constraint_has_name():
    assert hasattr(Relational::Constraint, "name")
    descriptor = None
    for klass in Relational::Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::domain_is_not_abstract():
    assert not inspect.isabstract(Relational::Domain)


def test_relational::domain_constructor_exists():
    assert callable(Relational::Domain.__init__)


def test_relational::domain_constructor_args():
    sig = inspect.signature(Relational::Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::domain_has_name():
    assert hasattr(Relational::Domain, "name")
    descriptor = None
    for klass in Relational::Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational::table_is_not_abstract():
    assert not inspect.isabstract(Relational::Table)


def test_relational::table_constructor_exists():
    assert callable(Relational::Table.__init__)


def test_relational::table_constructor_args():
    sig = inspect.signature(Relational::Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational::table_has_name():
    assert hasattr(Relational::Table, "name")
    descriptor = None
    for klass in Relational::Table.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "Derivate",
        "Simple",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"


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
Relational::EnumeratedLiteral_strategy = st.builds(
    Relational::EnumeratedLiteral,
    name=
        safe_text
)
Domain_strategy = st.builds(
    Domain,
)
Relational::EnumerationType_strategy = st.builds(
    Relational::EnumerationType,
)
Relational::PrimitiveType_strategy = st.builds(
    Relational::PrimitiveType,
)
CandidateKey_strategy = st.builds(
    CandidateKey,
)
Relational::Schema_strategy = st.builds(
    Relational::Schema,
    name=
        safe_text
)
Relational::ForeignKey_strategy = st.builds(
    Relational::ForeignKey,
)
Relational::Attribute_strategy = st.builds(
    Relational::Attribute,
    name=
        safe_text,
    multiplicity=
        st.integers(),
    type=
        safe_text,
    nullable=
        st.booleans()
)
Relational::CandidateKey_strategy = st.builds(
    Relational::CandidateKey,
    name=
        safe_text
)
Relational::Constraint_strategy = st.builds(
    Relational::Constraint,
    description=
        safe_text,
    name=
        safe_text
)
Relational::Domain_strategy = st.builds(
    Relational::Domain,
    name=
        safe_text
)
Relational::Table_strategy = st.builds(
    Relational::Table,
    name=
        safe_text
)

@given(instance=Relational::EnumeratedLiteral_strategy)
@settings(max_examples=50)
def test_relational::enumeratedliteral_instantiation(instance):
    assert isinstance(instance, Relational::EnumeratedLiteral)

@given(instance=Relational::EnumeratedLiteral_strategy)
def test_relational::enumeratedliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::EnumeratedLiteral_strategy)
def test_relational::enumeratedliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Relational::EnumerationType_strategy)
@settings(max_examples=50)
def test_relational::enumerationtype_instantiation(instance):
    assert isinstance(instance, Relational::EnumerationType)

@given(instance=Relational::PrimitiveType_strategy)
@settings(max_examples=50)
def test_relational::primitivetype_instantiation(instance):
    assert isinstance(instance, Relational::PrimitiveType)

@given(instance=CandidateKey_strategy)
@settings(max_examples=50)
def test_candidatekey_instantiation(instance):
    assert isinstance(instance, CandidateKey)

@given(instance=Relational::Schema_strategy)
@settings(max_examples=50)
def test_relational::schema_instantiation(instance):
    assert isinstance(instance, Relational::Schema)

@given(instance=Relational::Schema_strategy)
def test_relational::schema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Schema_strategy)
def test_relational::schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::ForeignKey_strategy)
@settings(max_examples=50)
def test_relational::foreignkey_instantiation(instance):
    assert isinstance(instance, Relational::ForeignKey)

@given(instance=Relational::Attribute_strategy)
@settings(max_examples=50)
def test_relational::attribute_instantiation(instance):
    assert isinstance(instance, Relational::Attribute)

@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_multiplicity_type(instance):
    assert isinstance(instance.multiplicity, int)


@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original

@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=Relational::Attribute_strategy)
def test_relational::attribute_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=Relational::CandidateKey_strategy)
@settings(max_examples=50)
def test_relational::candidatekey_instantiation(instance):
    assert isinstance(instance, Relational::CandidateKey)

@given(instance=Relational::CandidateKey_strategy)
def test_relational::candidatekey_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::CandidateKey_strategy)
def test_relational::candidatekey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Constraint_strategy)
@settings(max_examples=50)
def test_relational::constraint_instantiation(instance):
    assert isinstance(instance, Relational::Constraint)

@given(instance=Relational::Constraint_strategy)
def test_relational::constraint_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Relational::Constraint_strategy)
def test_relational::constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Relational::Constraint_strategy)
def test_relational::constraint_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Constraint_strategy)
def test_relational::constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Domain_strategy)
@settings(max_examples=50)
def test_relational::domain_instantiation(instance):
    assert isinstance(instance, Relational::Domain)

@given(instance=Relational::Domain_strategy)
def test_relational::domain_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Domain_strategy)
def test_relational::domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational::Table_strategy)
@settings(max_examples=50)
def test_relational::table_instantiation(instance):
    assert isinstance(instance, Relational::Table)

@given(instance=Relational::Table_strategy)
def test_relational::table_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Relational::Table_strategy)
def test_relational::table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
