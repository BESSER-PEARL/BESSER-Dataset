import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleumltordbms::ForeignKey,
    simpleumltordbms::Association,
    UmlToRdbmsModelElement,
    simpleumltordbms::PrimitiveDataType,
    simpleumltordbms::Package,
    simpleumltordbms::Schema,
    simpleumltordbms::UmlToRdbmsModelElement,
    simpleumltordbms::Column,
    simpleumltordbms::ToColumn,
    simpleumltordbms::FromAttribute,
    simpleumltordbms::Class,
    simpleumltordbms::Table,
    simpleumltordbms::Key,
    simpleumltordbms::PackageToSchema,
    FromAttributeOwner,
    PrimitiveToName,
    simpleumltordbms::StringToVarchar,
    simpleumltordbms::BooleanToBoolean,
    simpleumltordbms::IntegerToNumber,
    simpleumltordbms::FromAttributeOwner,
    simpleumltordbms::Attribute,
    simpleumltordbms::PrimitiveToName,
    ToColumn,
    simpleumltordbms::AssociationToForeignKey,
    FromAttribute,
    simpleumltordbms::NonLeafAttribute,
    simpleumltordbms::AttributeToColumn,
    simpleumltordbms::ClassToTable,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleumltordbms::foreignkey_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::ForeignKey)


def test_simpleumltordbms::foreignkey_constructor_exists():
    assert callable(simpleumltordbms::ForeignKey.__init__)


def test_simpleumltordbms::foreignkey_constructor_args():
    sig = inspect.signature(simpleumltordbms::ForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::association_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Association)


def test_simpleumltordbms::association_constructor_exists():
    assert callable(simpleumltordbms::Association.__init__)


def test_simpleumltordbms::association_constructor_args():
    sig = inspect.signature(simpleumltordbms::Association.__init__)
    params = list(sig.parameters.keys())



def test_umltordbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(UmlToRdbmsModelElement)


def test_umltordbmsmodelelement_constructor_exists():
    assert callable(UmlToRdbmsModelElement.__init__)


def test_umltordbmsmodelelement_constructor_args():
    sig = inspect.signature(UmlToRdbmsModelElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::primitivedatatype_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::PrimitiveDataType)


def test_simpleumltordbms::primitivedatatype_constructor_exists():
    assert callable(simpleumltordbms::PrimitiveDataType.__init__)


def test_simpleumltordbms::primitivedatatype_constructor_args():
    sig = inspect.signature(simpleumltordbms::PrimitiveDataType.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::package_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Package)


def test_simpleumltordbms::package_constructor_exists():
    assert callable(simpleumltordbms::Package.__init__)


def test_simpleumltordbms::package_constructor_args():
    sig = inspect.signature(simpleumltordbms::Package.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::schema_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Schema)


def test_simpleumltordbms::schema_constructor_exists():
    assert callable(simpleumltordbms::Schema.__init__)


def test_simpleumltordbms::schema_constructor_args():
    sig = inspect.signature(simpleumltordbms::Schema.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::umltordbmsmodelelement_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::UmlToRdbmsModelElement)


def test_simpleumltordbms::umltordbmsmodelelement_constructor_exists():
    assert callable(simpleumltordbms::UmlToRdbmsModelElement.__init__)


def test_simpleumltordbms::umltordbmsmodelelement_constructor_args():
    sig = inspect.signature(simpleumltordbms::UmlToRdbmsModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleumltordbms::umltordbmsmodelelement_has_name():
    assert hasattr(simpleumltordbms::UmlToRdbmsModelElement, "name")
    descriptor = None
    for klass in simpleumltordbms::UmlToRdbmsModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleumltordbms::column_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Column)


def test_simpleumltordbms::column_constructor_exists():
    assert callable(simpleumltordbms::Column.__init__)


def test_simpleumltordbms::column_constructor_args():
    sig = inspect.signature(simpleumltordbms::Column.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::tocolumn_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::ToColumn)


def test_simpleumltordbms::tocolumn_constructor_exists():
    assert callable(simpleumltordbms::ToColumn.__init__)


def test_simpleumltordbms::tocolumn_constructor_args():
    sig = inspect.signature(simpleumltordbms::ToColumn.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::fromattribute_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::FromAttribute)


def test_simpleumltordbms::fromattribute_constructor_exists():
    assert callable(simpleumltordbms::FromAttribute.__init__)


def test_simpleumltordbms::fromattribute_constructor_args():
    sig = inspect.signature(simpleumltordbms::FromAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_simpleumltordbms::fromattribute_has_kind():
    assert hasattr(simpleumltordbms::FromAttribute, "kind")
    descriptor = None
    for klass in simpleumltordbms::FromAttribute.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_simpleumltordbms::class_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Class)


def test_simpleumltordbms::class_constructor_exists():
    assert callable(simpleumltordbms::Class.__init__)


def test_simpleumltordbms::class_constructor_args():
    sig = inspect.signature(simpleumltordbms::Class.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::table_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Table)


def test_simpleumltordbms::table_constructor_exists():
    assert callable(simpleumltordbms::Table.__init__)


def test_simpleumltordbms::table_constructor_args():
    sig = inspect.signature(simpleumltordbms::Table.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::key_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Key)


def test_simpleumltordbms::key_constructor_exists():
    assert callable(simpleumltordbms::Key.__init__)


def test_simpleumltordbms::key_constructor_args():
    sig = inspect.signature(simpleumltordbms::Key.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::packagetoschema_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::PackageToSchema)


def test_simpleumltordbms::packagetoschema_constructor_exists():
    assert callable(simpleumltordbms::PackageToSchema.__init__)


def test_simpleumltordbms::packagetoschema_constructor_args():
    sig = inspect.signature(simpleumltordbms::PackageToSchema.__init__)
    params = list(sig.parameters.keys())



def test_fromattributeowner_is_not_abstract():
    assert not inspect.isabstract(FromAttributeOwner)


def test_fromattributeowner_constructor_exists():
    assert callable(FromAttributeOwner.__init__)


def test_fromattributeowner_constructor_args():
    sig = inspect.signature(FromAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_primitivetoname_is_not_abstract():
    assert not inspect.isabstract(PrimitiveToName)


def test_primitivetoname_constructor_exists():
    assert callable(PrimitiveToName.__init__)


def test_primitivetoname_constructor_args():
    sig = inspect.signature(PrimitiveToName.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::stringtovarchar_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::StringToVarchar)


def test_simpleumltordbms::stringtovarchar_constructor_exists():
    assert callable(simpleumltordbms::StringToVarchar.__init__)


def test_simpleumltordbms::stringtovarchar_constructor_args():
    sig = inspect.signature(simpleumltordbms::StringToVarchar.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::booleantoboolean_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::BooleanToBoolean)


def test_simpleumltordbms::booleantoboolean_constructor_exists():
    assert callable(simpleumltordbms::BooleanToBoolean.__init__)


def test_simpleumltordbms::booleantoboolean_constructor_args():
    sig = inspect.signature(simpleumltordbms::BooleanToBoolean.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::integertonumber_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::IntegerToNumber)


def test_simpleumltordbms::integertonumber_constructor_exists():
    assert callable(simpleumltordbms::IntegerToNumber.__init__)


def test_simpleumltordbms::integertonumber_constructor_args():
    sig = inspect.signature(simpleumltordbms::IntegerToNumber.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::fromattributeowner_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::FromAttributeOwner)


def test_simpleumltordbms::fromattributeowner_constructor_exists():
    assert callable(simpleumltordbms::FromAttributeOwner.__init__)


def test_simpleumltordbms::fromattributeowner_constructor_args():
    sig = inspect.signature(simpleumltordbms::FromAttributeOwner.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::attribute_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::Attribute)


def test_simpleumltordbms::attribute_constructor_exists():
    assert callable(simpleumltordbms::Attribute.__init__)


def test_simpleumltordbms::attribute_constructor_args():
    sig = inspect.signature(simpleumltordbms::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::primitivetoname_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::PrimitiveToName)


def test_simpleumltordbms::primitivetoname_constructor_exists():
    assert callable(simpleumltordbms::PrimitiveToName.__init__)


def test_simpleumltordbms::primitivetoname_constructor_args():
    sig = inspect.signature(simpleumltordbms::PrimitiveToName.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_simpleumltordbms::primitivetoname_has_typeName():
    assert hasattr(simpleumltordbms::PrimitiveToName, "typeName")
    descriptor = None
    for klass in simpleumltordbms::PrimitiveToName.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_tocolumn_is_not_abstract():
    assert not inspect.isabstract(ToColumn)


def test_tocolumn_constructor_exists():
    assert callable(ToColumn.__init__)


def test_tocolumn_constructor_args():
    sig = inspect.signature(ToColumn.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::associationtoforeignkey_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::AssociationToForeignKey)


def test_simpleumltordbms::associationtoforeignkey_constructor_exists():
    assert callable(simpleumltordbms::AssociationToForeignKey.__init__)


def test_simpleumltordbms::associationtoforeignkey_constructor_args():
    sig = inspect.signature(simpleumltordbms::AssociationToForeignKey.__init__)
    params = list(sig.parameters.keys())



def test_fromattribute_is_not_abstract():
    assert not inspect.isabstract(FromAttribute)


def test_fromattribute_constructor_exists():
    assert callable(FromAttribute.__init__)


def test_fromattribute_constructor_args():
    sig = inspect.signature(FromAttribute.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::nonleafattribute_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::NonLeafAttribute)


def test_simpleumltordbms::nonleafattribute_constructor_exists():
    assert callable(simpleumltordbms::NonLeafAttribute.__init__)


def test_simpleumltordbms::nonleafattribute_constructor_args():
    sig = inspect.signature(simpleumltordbms::NonLeafAttribute.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::attributetocolumn_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::AttributeToColumn)


def test_simpleumltordbms::attributetocolumn_constructor_exists():
    assert callable(simpleumltordbms::AttributeToColumn.__init__)


def test_simpleumltordbms::attributetocolumn_constructor_args():
    sig = inspect.signature(simpleumltordbms::AttributeToColumn.__init__)
    params = list(sig.parameters.keys())



def test_simpleumltordbms::classtotable_is_not_abstract():
    assert not inspect.isabstract(simpleumltordbms::ClassToTable)


def test_simpleumltordbms::classtotable_constructor_exists():
    assert callable(simpleumltordbms::ClassToTable.__init__)


def test_simpleumltordbms::classtotable_constructor_args():
    sig = inspect.signature(simpleumltordbms::ClassToTable.__init__)
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
simpleumltordbms::ForeignKey_strategy = st.builds(
    simpleumltordbms::ForeignKey,
)
simpleumltordbms::Association_strategy = st.builds(
    simpleumltordbms::Association,
)
UmlToRdbmsModelElement_strategy = st.builds(
    UmlToRdbmsModelElement,
)
simpleumltordbms::PrimitiveDataType_strategy = st.builds(
    simpleumltordbms::PrimitiveDataType,
)
simpleumltordbms::Package_strategy = st.builds(
    simpleumltordbms::Package,
)
simpleumltordbms::Schema_strategy = st.builds(
    simpleumltordbms::Schema,
)
simpleumltordbms::UmlToRdbmsModelElement_strategy = st.builds(
    simpleumltordbms::UmlToRdbmsModelElement,
    name=
        safe_text
)
simpleumltordbms::Column_strategy = st.builds(
    simpleumltordbms::Column,
)
simpleumltordbms::ToColumn_strategy = st.builds(
    simpleumltordbms::ToColumn,
)
simpleumltordbms::FromAttribute_strategy = st.builds(
    simpleumltordbms::FromAttribute,
    kind=
        safe_text
)
simpleumltordbms::Class_strategy = st.builds(
    simpleumltordbms::Class,
)
simpleumltordbms::Table_strategy = st.builds(
    simpleumltordbms::Table,
)
simpleumltordbms::Key_strategy = st.builds(
    simpleumltordbms::Key,
)
simpleumltordbms::PackageToSchema_strategy = st.builds(
    simpleumltordbms::PackageToSchema,
)
FromAttributeOwner_strategy = st.builds(
    FromAttributeOwner,
)
PrimitiveToName_strategy = st.builds(
    PrimitiveToName,
)
simpleumltordbms::StringToVarchar_strategy = st.builds(
    simpleumltordbms::StringToVarchar,
)
simpleumltordbms::BooleanToBoolean_strategy = st.builds(
    simpleumltordbms::BooleanToBoolean,
)
simpleumltordbms::IntegerToNumber_strategy = st.builds(
    simpleumltordbms::IntegerToNumber,
)
simpleumltordbms::FromAttributeOwner_strategy = st.builds(
    simpleumltordbms::FromAttributeOwner,
)
simpleumltordbms::Attribute_strategy = st.builds(
    simpleumltordbms::Attribute,
)
simpleumltordbms::PrimitiveToName_strategy = st.builds(
    simpleumltordbms::PrimitiveToName,
    typeName=
        safe_text
)
ToColumn_strategy = st.builds(
    ToColumn,
)
simpleumltordbms::AssociationToForeignKey_strategy = st.builds(
    simpleumltordbms::AssociationToForeignKey,
)
FromAttribute_strategy = st.builds(
    FromAttribute,
)
simpleumltordbms::NonLeafAttribute_strategy = st.builds(
    simpleumltordbms::NonLeafAttribute,
)
simpleumltordbms::AttributeToColumn_strategy = st.builds(
    simpleumltordbms::AttributeToColumn,
)
simpleumltordbms::ClassToTable_strategy = st.builds(
    simpleumltordbms::ClassToTable,
)

@given(instance=simpleumltordbms::ForeignKey_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::foreignkey_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::ForeignKey)

@given(instance=simpleumltordbms::Association_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::association_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Association)

@given(instance=UmlToRdbmsModelElement_strategy)
@settings(max_examples=50)
def test_umltordbmsmodelelement_instantiation(instance):
    assert isinstance(instance, UmlToRdbmsModelElement)

@given(instance=simpleumltordbms::PrimitiveDataType_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::primitivedatatype_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::PrimitiveDataType)

@given(instance=simpleumltordbms::Package_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::package_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Package)

@given(instance=simpleumltordbms::Schema_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::schema_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Schema)

@given(instance=simpleumltordbms::UmlToRdbmsModelElement_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::umltordbmsmodelelement_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::UmlToRdbmsModelElement)

@given(instance=simpleumltordbms::UmlToRdbmsModelElement_strategy)
def test_simpleumltordbms::umltordbmsmodelelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleumltordbms::UmlToRdbmsModelElement_strategy)
def test_simpleumltordbms::umltordbmsmodelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleumltordbms::Column_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::column_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Column)

@given(instance=simpleumltordbms::ToColumn_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::tocolumn_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::ToColumn)

@given(instance=simpleumltordbms::FromAttribute_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::fromattribute_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::FromAttribute)

@given(instance=simpleumltordbms::FromAttribute_strategy)
def test_simpleumltordbms::fromattribute_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=simpleumltordbms::FromAttribute_strategy)
def test_simpleumltordbms::fromattribute_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=simpleumltordbms::Class_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::class_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Class)

@given(instance=simpleumltordbms::Table_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::table_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Table)

@given(instance=simpleumltordbms::Key_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::key_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Key)

@given(instance=simpleumltordbms::PackageToSchema_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::packagetoschema_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::PackageToSchema)

@given(instance=FromAttributeOwner_strategy)
@settings(max_examples=50)
def test_fromattributeowner_instantiation(instance):
    assert isinstance(instance, FromAttributeOwner)

@given(instance=PrimitiveToName_strategy)
@settings(max_examples=50)
def test_primitivetoname_instantiation(instance):
    assert isinstance(instance, PrimitiveToName)

@given(instance=simpleumltordbms::StringToVarchar_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::stringtovarchar_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::StringToVarchar)

@given(instance=simpleumltordbms::BooleanToBoolean_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::booleantoboolean_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::BooleanToBoolean)

@given(instance=simpleumltordbms::IntegerToNumber_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::integertonumber_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::IntegerToNumber)

@given(instance=simpleumltordbms::FromAttributeOwner_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::fromattributeowner_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::FromAttributeOwner)

@given(instance=simpleumltordbms::Attribute_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::attribute_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::Attribute)

@given(instance=simpleumltordbms::PrimitiveToName_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::primitivetoname_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::PrimitiveToName)

@given(instance=simpleumltordbms::PrimitiveToName_strategy)
def test_simpleumltordbms::primitivetoname_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=simpleumltordbms::PrimitiveToName_strategy)
def test_simpleumltordbms::primitivetoname_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=ToColumn_strategy)
@settings(max_examples=50)
def test_tocolumn_instantiation(instance):
    assert isinstance(instance, ToColumn)

@given(instance=simpleumltordbms::AssociationToForeignKey_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::associationtoforeignkey_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::AssociationToForeignKey)

@given(instance=FromAttribute_strategy)
@settings(max_examples=50)
def test_fromattribute_instantiation(instance):
    assert isinstance(instance, FromAttribute)

@given(instance=simpleumltordbms::NonLeafAttribute_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::nonleafattribute_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::NonLeafAttribute)

@given(instance=simpleumltordbms::AttributeToColumn_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::attributetocolumn_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::AttributeToColumn)

@given(instance=simpleumltordbms::ClassToTable_strategy)
@settings(max_examples=50)
def test_simpleumltordbms::classtotable_instantiation(instance):
    assert isinstance(instance, simpleumltordbms::ClassToTable)
