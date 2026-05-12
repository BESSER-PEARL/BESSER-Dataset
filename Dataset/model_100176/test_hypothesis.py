import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relational_EnumeratedLiteral,
    Domain,
    Relational_EnumerationType,
    Relational_PrimitiveType,
    CandidateKey,
    Relational_Schema,
    Relational_ForeignKey,
    Relational_Attribute,
    Relational_CandidateKey,
    Relational_Constraint,
    Relational_Domain,
    Relational_Table,
    AttributeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relational_enumeratedliteral_is_not_abstract():
    assert not inspect.isabstract(Relational_EnumeratedLiteral)


def test_relational_enumeratedliteral_constructor_exists():
    assert callable(Relational_EnumeratedLiteral.__init__)


def test_relational_enumeratedliteral_constructor_args():
    sig = inspect.signature(Relational_EnumeratedLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_enumeratedliteral_has_name():
    assert hasattr(Relational_EnumeratedLiteral, "name")
    descriptor = None
    for klass in Relational_EnumeratedLiteral.__mro__:
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



def test_relational_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(Relational_EnumerationType)


def test_relational_enumerationtype_constructor_exists():
    assert callable(Relational_EnumerationType.__init__)


def test_relational_enumerationtype_constructor_args():
    sig = inspect.signature(Relational_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_relational_primitivetype_is_not_abstract():
    assert not inspect.isabstract(Relational_PrimitiveType)


def test_relational_primitivetype_constructor_exists():
    assert callable(Relational_PrimitiveType.__init__)


def test_relational_primitivetype_constructor_args():
    sig = inspect.signature(Relational_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_candidatekey_is_not_abstract():
    assert not inspect.isabstract(CandidateKey)


def test_candidatekey_constructor_exists():
    assert callable(CandidateKey.__init__)


def test_candidatekey_constructor_args():
    sig = inspect.signature(CandidateKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_schema_is_not_abstract():
    assert not inspect.isabstract(Relational_Schema)


def test_relational_schema_constructor_exists():
    assert callable(Relational_Schema.__init__)


def test_relational_schema_constructor_args():
    sig = inspect.signature(Relational_Schema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_schema_has_name():
    assert hasattr(Relational_Schema, "name")
    descriptor = None
    for klass in Relational_Schema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_foreignkey_is_not_abstract():
    assert not inspect.isabstract(Relational_ForeignKey)


def test_relational_foreignkey_constructor_exists():
    assert callable(Relational_ForeignKey.__init__)


def test_relational_foreignkey_constructor_args():
    sig = inspect.signature(Relational_ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_relational_attribute_is_not_abstract():
    assert not inspect.isabstract(Relational_Attribute)


def test_relational_attribute_constructor_exists():
    assert callable(Relational_Attribute.__init__)


def test_relational_attribute_constructor_args():
    sig = inspect.signature(Relational_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "multiplicity" in params, "Missing parameter 'multiplicity'"
    assert "type" in params, "Missing parameter 'type'"

def test_relational_attribute_has_name():
    assert hasattr(Relational_Attribute, "name")
    descriptor = None
    for klass in Relational_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_relational_attribute_has_nullable():
    assert hasattr(Relational_Attribute, "nullable")
    descriptor = None
    for klass in Relational_Attribute.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_relational_attribute_has_multiplicity():
    assert hasattr(Relational_Attribute, "multiplicity")
    descriptor = None
    for klass in Relational_Attribute.__mro__:
        if "multiplicity" in klass.__dict__:
            descriptor = klass.__dict__["multiplicity"]
            break
    assert isinstance(descriptor, property)

def test_relational_attribute_has_type():
    assert hasattr(Relational_Attribute, "type")
    descriptor = None
    for klass in Relational_Attribute.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_relational_candidatekey_is_not_abstract():
    assert not inspect.isabstract(Relational_CandidateKey)


def test_relational_candidatekey_constructor_exists():
    assert callable(Relational_CandidateKey.__init__)


def test_relational_candidatekey_constructor_args():
    sig = inspect.signature(Relational_CandidateKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_candidatekey_has_name():
    assert hasattr(Relational_CandidateKey, "name")
    descriptor = None
    for klass in Relational_CandidateKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_constraint_is_not_abstract():
    assert not inspect.isabstract(Relational_Constraint)


def test_relational_constraint_constructor_exists():
    assert callable(Relational_Constraint.__init__)


def test_relational_constraint_constructor_args():
    sig = inspect.signature(Relational_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_relational_constraint_has_description():
    assert hasattr(Relational_Constraint, "description")
    descriptor = None
    for klass in Relational_Constraint.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_relational_constraint_has_name():
    assert hasattr(Relational_Constraint, "name")
    descriptor = None
    for klass in Relational_Constraint.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_domain_is_not_abstract():
    assert not inspect.isabstract(Relational_Domain)


def test_relational_domain_constructor_exists():
    assert callable(Relational_Domain.__init__)


def test_relational_domain_constructor_args():
    sig = inspect.signature(Relational_Domain.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_domain_has_name():
    assert hasattr(Relational_Domain, "name")
    descriptor = None
    for klass in Relational_Domain.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_relational_table_is_not_abstract():
    assert not inspect.isabstract(Relational_Table)


def test_relational_table_constructor_exists():
    assert callable(Relational_Table.__init__)


def test_relational_table_constructor_args():
    sig = inspect.signature(Relational_Table.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_relational_table_has_name():
    assert hasattr(Relational_Table, "name")
    descriptor = None
    for klass in Relational_Table.__mro__:
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
Relational_EnumeratedLiteral_strategy = st.builds(
    Relational_EnumeratedLiteral,
    name=
        safe_text
)
Domain_strategy = st.builds(
    Domain,
)
Relational_EnumerationType_strategy = st.builds(
    Relational_EnumerationType,
)
Relational_PrimitiveType_strategy = st.builds(
    Relational_PrimitiveType,
)
CandidateKey_strategy = st.builds(
    CandidateKey,
)
Relational_Schema_strategy = st.builds(
    Relational_Schema,
    name=
        safe_text
)
Relational_ForeignKey_strategy = st.builds(
    Relational_ForeignKey,
)
Relational_Attribute_strategy = st.builds(
    Relational_Attribute,
    name=
        safe_text,
    nullable=
        st.booleans(),
    multiplicity=
        st.integers(),
    type=
        safe_text
)
Relational_CandidateKey_strategy = st.builds(
    Relational_CandidateKey,
    name=
        safe_text
)
Relational_Constraint_strategy = st.builds(
    Relational_Constraint,
    description=
        safe_text,
    name=
        safe_text
)
Relational_Domain_strategy = st.builds(
    Relational_Domain,
    name=
        safe_text
)
Relational_Table_strategy = st.builds(
    Relational_Table,
    name=
        safe_text
)

@given(instance=Relational_EnumeratedLiteral_strategy)
@settings(max_examples=50)
def test_relational_enumeratedliteral_instantiation(instance):
    assert isinstance(instance, Relational_EnumeratedLiteral)



@given(instance=Relational_EnumeratedLiteral_strategy)
def test_relational_enumeratedliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Domain_strategy)
@settings(max_examples=50)
def test_domain_instantiation(instance):
    assert isinstance(instance, Domain)

@given(instance=Relational_EnumerationType_strategy)
@settings(max_examples=50)
def test_relational_enumerationtype_instantiation(instance):
    assert isinstance(instance, Relational_EnumerationType)

@given(instance=Relational_PrimitiveType_strategy)
@settings(max_examples=50)
def test_relational_primitivetype_instantiation(instance):
    assert isinstance(instance, Relational_PrimitiveType)

@given(instance=CandidateKey_strategy)
@settings(max_examples=50)
def test_candidatekey_instantiation(instance):
    assert isinstance(instance, CandidateKey)

@given(instance=Relational_Schema_strategy)
@settings(max_examples=50)
def test_relational_schema_instantiation(instance):
    assert isinstance(instance, Relational_Schema)



@given(instance=Relational_Schema_strategy)
def test_relational_schema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_ForeignKey_strategy)
@settings(max_examples=50)
def test_relational_foreignkey_instantiation(instance):
    assert isinstance(instance, Relational_ForeignKey)

@given(instance=Relational_Attribute_strategy)
@settings(max_examples=50)
def test_relational_attribute_instantiation(instance):
    assert isinstance(instance, Relational_Attribute)



@given(instance=Relational_Attribute_strategy)
def test_relational_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Relational_Attribute_strategy)
def test_relational_attribute_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=Relational_Attribute_strategy)
def test_relational_attribute_multiplicity_setter(instance):
    original = instance.multiplicity
    instance.multiplicity = original
    assert instance.multiplicity == original



@given(instance=Relational_Attribute_strategy)
def test_relational_attribute_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Relational_CandidateKey_strategy)
@settings(max_examples=50)
def test_relational_candidatekey_instantiation(instance):
    assert isinstance(instance, Relational_CandidateKey)



@given(instance=Relational_CandidateKey_strategy)
def test_relational_candidatekey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_Constraint_strategy)
@settings(max_examples=50)
def test_relational_constraint_instantiation(instance):
    assert isinstance(instance, Relational_Constraint)



@given(instance=Relational_Constraint_strategy)
def test_relational_constraint_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=Relational_Constraint_strategy)
def test_relational_constraint_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_Domain_strategy)
@settings(max_examples=50)
def test_relational_domain_instantiation(instance):
    assert isinstance(instance, Relational_Domain)



@given(instance=Relational_Domain_strategy)
def test_relational_domain_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Relational_Table_strategy)
@settings(max_examples=50)
def test_relational_table_instantiation(instance):
    assert isinstance(instance, Relational_Table)



@given(instance=Relational_Table_strategy)
def test_relational_table_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
