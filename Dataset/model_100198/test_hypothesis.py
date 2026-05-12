import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SInlinedSQLType,
    sqlDSL::SDecimal,
    sqlDSL::SString,
    sqlDSL::SEnumLiteral,
    SExtDeclaredSQLType,
    sqlDSL::SInlinedSQLType,
    SArtifact,
    sqlDSL::SEnum,
    sqlDSL::STable,
    sqlDSL::SExtDeclaredSQLType,
    STableMember,
    sqlDSL::SJoinColumn,
    sqlDSL::SColumn,
    sqlDSL::SColumnProps,
    sqlDSL::STableMember,
    sqlDSL::SSettings,
    sqlDSL::SModel,
    sqlDSL::SArtifact,
    SIndex,
    SDBEngine,
    SSimpleTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sinlinedsqltype_is_not_abstract():
    assert not inspect.isabstract(SInlinedSQLType)


def test_sinlinedsqltype_constructor_exists():
    assert callable(SInlinedSQLType.__init__)


def test_sinlinedsqltype_constructor_args():
    sig = inspect.signature(SInlinedSQLType.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::sdecimal_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SDecimal)


def test_sqldsl::sdecimal_constructor_exists():
    assert callable(sqlDSL::SDecimal.__init__)


def test_sqldsl::sdecimal_constructor_args():
    sig = inspect.signature(sqlDSL::SDecimal.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::sstring_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SString)


def test_sqldsl::sstring_constructor_exists():
    assert callable(sqlDSL::SString.__init__)


def test_sqldsl::sstring_constructor_args():
    sig = inspect.signature(sqlDSL::SString.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::senumliteral_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SEnumLiteral)


def test_sqldsl::senumliteral_constructor_exists():
    assert callable(sqlDSL::SEnumLiteral.__init__)


def test_sqldsl::senumliteral_constructor_args():
    sig = inspect.signature(sqlDSL::SEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_sqldsl::senumliteral_has_name():
    assert hasattr(sqlDSL::SEnumLiteral, "name")
    descriptor = None
    for klass in sqlDSL::SEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::senumliteral_has_value():
    assert hasattr(sqlDSL::SEnumLiteral, "value")
    descriptor = None
    for klass in sqlDSL::SEnumLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sextdeclaredsqltype_is_not_abstract():
    assert not inspect.isabstract(SExtDeclaredSQLType)


def test_sextdeclaredsqltype_constructor_exists():
    assert callable(SExtDeclaredSQLType.__init__)


def test_sextdeclaredsqltype_constructor_args():
    sig = inspect.signature(SExtDeclaredSQLType.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::sinlinedsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SInlinedSQLType)


def test_sqldsl::sinlinedsqltype_constructor_exists():
    assert callable(sqlDSL::SInlinedSQLType.__init__)


def test_sqldsl::sinlinedsqltype_constructor_args():
    sig = inspect.signature(sqlDSL::SInlinedSQLType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqldsl::sinlinedsqltype_has_value():
    assert hasattr(sqlDSL::SInlinedSQLType, "value")
    descriptor = None
    for klass in sqlDSL::SInlinedSQLType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_sartifact_is_not_abstract():
    assert not inspect.isabstract(SArtifact)


def test_sartifact_constructor_exists():
    assert callable(SArtifact.__init__)


def test_sartifact_constructor_args():
    sig = inspect.signature(SArtifact.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::senum_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SEnum)


def test_sqldsl::senum_constructor_exists():
    assert callable(sqlDSL::SEnum.__init__)


def test_sqldsl::senum_constructor_args():
    sig = inspect.signature(sqlDSL::SEnum.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::stable_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::STable)


def test_sqldsl::stable_constructor_exists():
    assert callable(sqlDSL::STable.__init__)


def test_sqldsl::stable_constructor_args():
    sig = inspect.signature(sqlDSL::STable.__init__)
    params = list(sig.parameters.keys())
    assert "cached" in params, "Missing parameter 'cached'"
    assert "entityname" in params, "Missing parameter 'entityname'"
    assert "prefix" in params, "Missing parameter 'prefix'"

def test_sqldsl::stable_has_cached():
    assert hasattr(sqlDSL::STable, "cached")
    descriptor = None
    for klass in sqlDSL::STable.__mro__:
        if "cached" in klass.__dict__:
            descriptor = klass.__dict__["cached"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::stable_has_entityname():
    assert hasattr(sqlDSL::STable, "entityname")
    descriptor = None
    for klass in sqlDSL::STable.__mro__:
        if "entityname" in klass.__dict__:
            descriptor = klass.__dict__["entityname"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::stable_has_prefix():
    assert hasattr(sqlDSL::STable, "prefix")
    descriptor = None
    for klass in sqlDSL::STable.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::sextdeclaredsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SExtDeclaredSQLType)


def test_sqldsl::sextdeclaredsqltype_constructor_exists():
    assert callable(sqlDSL::SExtDeclaredSQLType.__init__)


def test_sqldsl::sextdeclaredsqltype_constructor_args():
    sig = inspect.signature(sqlDSL::SExtDeclaredSQLType.__init__)
    params = list(sig.parameters.keys())



def test_stablemember_is_not_abstract():
    assert not inspect.isabstract(STableMember)


def test_stablemember_constructor_exists():
    assert callable(STableMember.__init__)


def test_stablemember_constructor_args():
    sig = inspect.signature(STableMember.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::sjoincolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SJoinColumn)


def test_sqldsl::sjoincolumn_constructor_exists():
    assert callable(sqlDSL::SJoinColumn.__init__)


def test_sqldsl::sjoincolumn_constructor_args():
    sig = inspect.signature(sqlDSL::SJoinColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl::scolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SColumn)


def test_sqldsl::scolumn_constructor_exists():
    assert callable(sqlDSL::SColumn.__init__)


def test_sqldsl::scolumn_constructor_args():
    sig = inspect.signature(sqlDSL::SColumn.__init__)
    params = list(sig.parameters.keys())
    assert "simpleType" in params, "Missing parameter 'simpleType'"

def test_sqldsl::scolumn_has_simpleType():
    assert hasattr(sqlDSL::SColumn, "simpleType")
    descriptor = None
    for klass in sqlDSL::SColumn.__mro__:
        if "simpleType" in klass.__dict__:
            descriptor = klass.__dict__["simpleType"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::scolumnprops_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SColumnProps)


def test_sqldsl::scolumnprops_constructor_exists():
    assert callable(sqlDSL::SColumnProps.__init__)


def test_sqldsl::scolumnprops_constructor_args():
    sig = inspect.signature(sqlDSL::SColumnProps.__init__)
    params = list(sig.parameters.keys())
    assert "aes" in params, "Missing parameter 'aes'"
    assert "index" in params, "Missing parameter 'index'"
    assert "javacolumn" in params, "Missing parameter 'javacolumn'"
    assert "nullable" in params, "Missing parameter 'nullable'"

def test_sqldsl::scolumnprops_has_aes():
    assert hasattr(sqlDSL::SColumnProps, "aes")
    descriptor = None
    for klass in sqlDSL::SColumnProps.__mro__:
        if "aes" in klass.__dict__:
            descriptor = klass.__dict__["aes"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::scolumnprops_has_index():
    assert hasattr(sqlDSL::SColumnProps, "index")
    descriptor = None
    for klass in sqlDSL::SColumnProps.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::scolumnprops_has_javacolumn():
    assert hasattr(sqlDSL::SColumnProps, "javacolumn")
    descriptor = None
    for klass in sqlDSL::SColumnProps.__mro__:
        if "javacolumn" in klass.__dict__:
            descriptor = klass.__dict__["javacolumn"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::scolumnprops_has_nullable():
    assert hasattr(sqlDSL::SColumnProps, "nullable")
    descriptor = None
    for klass in sqlDSL::SColumnProps.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::stablemember_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::STableMember)


def test_sqldsl::stablemember_constructor_exists():
    assert callable(sqlDSL::STableMember.__init__)


def test_sqldsl::stablemember_constructor_args():
    sig = inspect.signature(sqlDSL::STableMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldsl::stablemember_has_name():
    assert hasattr(sqlDSL::STableMember, "name")
    descriptor = None
    for klass in sqlDSL::STableMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::ssettings_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SSettings)


def test_sqldsl::ssettings_constructor_exists():
    assert callable(sqlDSL::SSettings.__init__)


def test_sqldsl::ssettings_constructor_args():
    sig = inspect.signature(sqlDSL::SSettings.__init__)
    params = list(sig.parameters.keys())
    assert "javapackage" in params, "Missing parameter 'javapackage'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_sqldsl::ssettings_has_javapackage():
    assert hasattr(sqlDSL::SSettings, "javapackage")
    descriptor = None
    for klass in sqlDSL::SSettings.__mro__:
        if "javapackage" in klass.__dict__:
            descriptor = klass.__dict__["javapackage"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::ssettings_has_schema():
    assert hasattr(sqlDSL::SSettings, "schema")
    descriptor = None
    for klass in sqlDSL::SSettings.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl::ssettings_has_engine():
    assert hasattr(sqlDSL::SSettings, "engine")
    descriptor = None
    for klass in sqlDSL::SSettings.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::smodel_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SModel)


def test_sqldsl::smodel_constructor_exists():
    assert callable(sqlDSL::SModel.__init__)


def test_sqldsl::smodel_constructor_args():
    sig = inspect.signature(sqlDSL::SModel.__init__)
    params = list(sig.parameters.keys())
    assert "generatedFile" in params, "Missing parameter 'generatedFile'"

def test_sqldsl::smodel_has_generatedFile():
    assert hasattr(sqlDSL::SModel, "generatedFile")
    descriptor = None
    for klass in sqlDSL::SModel.__mro__:
        if "generatedFile" in klass.__dict__:
            descriptor = klass.__dict__["generatedFile"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl::sartifact_is_not_abstract():
    assert not inspect.isabstract(sqlDSL::SArtifact)


def test_sqldsl::sartifact_constructor_exists():
    assert callable(sqlDSL::SArtifact.__init__)


def test_sqldsl::sartifact_constructor_args():
    sig = inspect.signature(sqlDSL::SArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldsl::sartifact_has_name():
    assert hasattr(sqlDSL::SArtifact, "name")
    descriptor = None
    for klass in sqlDSL::SArtifact.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sindex_exists():
    # Check that the Enumeration exists
    assert SIndex is not None

def test_sindex_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SIndex]
    expected_literals = [
        "YES",
        "SPATIAL",
        "UNIQUE",
        "NO",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIndex"

def test_sdbengine_exists():
    # Check that the Enumeration exists
    assert SDBEngine is not None

def test_sdbengine_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SDBEngine]
    expected_literals = [
        "INNODB",
        "MYISAM",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SDBEngine"

def test_ssimpletypes_exists():
    # Check that the Enumeration exists
    assert SSimpleTypes is not None

def test_ssimpletypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SSimpleTypes]
    expected_literals = [
        "Coordinate",
        "SMALL_INT",
        "MEDIUM_INT",
        "Currency",
        "BLOB",
        "FOTO",
        "POLYGON",
        "POINT",
        "TIME",
        "TINY_INT",
        "BOOLEAN",
        "DATETIME",
        "DATE",
        "INT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SSimpleTypes"


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
SInlinedSQLType_strategy = st.builds(
    SInlinedSQLType,
)
sqlDSL::SDecimal_strategy = st.builds(
    sqlDSL::SDecimal,
)
sqlDSL::SString_strategy = st.builds(
    sqlDSL::SString,
)
sqlDSL::SEnumLiteral_strategy = st.builds(
    sqlDSL::SEnumLiteral,
    name=
        safe_text,
    value=
        st.integers()
)
SExtDeclaredSQLType_strategy = st.builds(
    SExtDeclaredSQLType,
)
sqlDSL::SInlinedSQLType_strategy = st.builds(
    sqlDSL::SInlinedSQLType,
    value=
        st.integers()
)
SArtifact_strategy = st.builds(
    SArtifact,
)
sqlDSL::SEnum_strategy = st.builds(
    sqlDSL::SEnum,
)
sqlDSL::STable_strategy = st.builds(
    sqlDSL::STable,
    cached=
        st.booleans(),
    entityname=
        safe_text,
    prefix=
        safe_text
)
sqlDSL::SExtDeclaredSQLType_strategy = st.builds(
    sqlDSL::SExtDeclaredSQLType,
)
STableMember_strategy = st.builds(
    STableMember,
)
sqlDSL::SJoinColumn_strategy = st.builds(
    sqlDSL::SJoinColumn,
)
sqlDSL::SColumn_strategy = st.builds(
    sqlDSL::SColumn,
    simpleType=
        safe_text
)
sqlDSL::SColumnProps_strategy = st.builds(
    sqlDSL::SColumnProps,
    aes=
        st.booleans(),
    index=
        safe_text,
    javacolumn=
        safe_text,
    nullable=
        st.booleans()
)
sqlDSL::STableMember_strategy = st.builds(
    sqlDSL::STableMember,
    name=
        safe_text
)
sqlDSL::SSettings_strategy = st.builds(
    sqlDSL::SSettings,
    javapackage=
        safe_text,
    schema=
        safe_text,
    engine=
        safe_text
)
sqlDSL::SModel_strategy = st.builds(
    sqlDSL::SModel,
    generatedFile=
        safe_text
)
sqlDSL::SArtifact_strategy = st.builds(
    sqlDSL::SArtifact,
    name=
        safe_text
)

@given(instance=SInlinedSQLType_strategy)
@settings(max_examples=50)
def test_sinlinedsqltype_instantiation(instance):
    assert isinstance(instance, SInlinedSQLType)

@given(instance=sqlDSL::SDecimal_strategy)
@settings(max_examples=50)
def test_sqldsl::sdecimal_instantiation(instance):
    assert isinstance(instance, sqlDSL::SDecimal)

@given(instance=sqlDSL::SString_strategy)
@settings(max_examples=50)
def test_sqldsl::sstring_instantiation(instance):
    assert isinstance(instance, sqlDSL::SString)

@given(instance=sqlDSL::SEnumLiteral_strategy)
@settings(max_examples=50)
def test_sqldsl::senumliteral_instantiation(instance):
    assert isinstance(instance, sqlDSL::SEnumLiteral)

@given(instance=sqlDSL::SEnumLiteral_strategy)
def test_sqldsl::senumliteral_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlDSL::SEnumLiteral_strategy)
def test_sqldsl::senumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlDSL::SEnumLiteral_strategy)
def test_sqldsl::senumliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=sqlDSL::SEnumLiteral_strategy)
def test_sqldsl::senumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SExtDeclaredSQLType_strategy)
@settings(max_examples=50)
def test_sextdeclaredsqltype_instantiation(instance):
    assert isinstance(instance, SExtDeclaredSQLType)

@given(instance=sqlDSL::SInlinedSQLType_strategy)
@settings(max_examples=50)
def test_sqldsl::sinlinedsqltype_instantiation(instance):
    assert isinstance(instance, sqlDSL::SInlinedSQLType)

@given(instance=sqlDSL::SInlinedSQLType_strategy)
def test_sqldsl::sinlinedsqltype_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=sqlDSL::SInlinedSQLType_strategy)
def test_sqldsl::sinlinedsqltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SArtifact_strategy)
@settings(max_examples=50)
def test_sartifact_instantiation(instance):
    assert isinstance(instance, SArtifact)

@given(instance=sqlDSL::SEnum_strategy)
@settings(max_examples=50)
def test_sqldsl::senum_instantiation(instance):
    assert isinstance(instance, sqlDSL::SEnum)

@given(instance=sqlDSL::STable_strategy)
@settings(max_examples=50)
def test_sqldsl::stable_instantiation(instance):
    assert isinstance(instance, sqlDSL::STable)

@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_cached_type(instance):
    assert isinstance(instance.cached, bool)


@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_cached_setter(instance):
    original = instance.cached
    instance.cached = original
    assert instance.cached == original

@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_entityname_type(instance):
    assert isinstance(instance.entityname, str)


@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_entityname_setter(instance):
    original = instance.entityname
    instance.entityname = original
    assert instance.entityname == original

@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_prefix_type(instance):
    assert isinstance(instance.prefix, str)


@given(instance=sqlDSL::STable_strategy)
def test_sqldsl::stable_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original

@given(instance=sqlDSL::SExtDeclaredSQLType_strategy)
@settings(max_examples=50)
def test_sqldsl::sextdeclaredsqltype_instantiation(instance):
    assert isinstance(instance, sqlDSL::SExtDeclaredSQLType)

@given(instance=STableMember_strategy)
@settings(max_examples=50)
def test_stablemember_instantiation(instance):
    assert isinstance(instance, STableMember)

@given(instance=sqlDSL::SJoinColumn_strategy)
@settings(max_examples=50)
def test_sqldsl::sjoincolumn_instantiation(instance):
    assert isinstance(instance, sqlDSL::SJoinColumn)

@given(instance=sqlDSL::SColumn_strategy)
@settings(max_examples=50)
def test_sqldsl::scolumn_instantiation(instance):
    assert isinstance(instance, sqlDSL::SColumn)

@given(instance=sqlDSL::SColumn_strategy)
def test_sqldsl::scolumn_simpleType_type(instance):
    assert isinstance(instance.simpleType, str)


@given(instance=sqlDSL::SColumn_strategy)
def test_sqldsl::scolumn_simpleType_setter(instance):
    original = instance.simpleType
    instance.simpleType = original
    assert instance.simpleType == original

@given(instance=sqlDSL::SColumnProps_strategy)
@settings(max_examples=50)
def test_sqldsl::scolumnprops_instantiation(instance):
    assert isinstance(instance, sqlDSL::SColumnProps)

@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_aes_type(instance):
    assert isinstance(instance.aes, bool)


@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_aes_setter(instance):
    original = instance.aes
    instance.aes = original
    assert instance.aes == original

@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_javacolumn_type(instance):
    assert isinstance(instance.javacolumn, str)


@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_javacolumn_setter(instance):
    original = instance.javacolumn
    instance.javacolumn = original
    assert instance.javacolumn == original

@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_nullable_type(instance):
    assert isinstance(instance.nullable, bool)


@given(instance=sqlDSL::SColumnProps_strategy)
def test_sqldsl::scolumnprops_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original

@given(instance=sqlDSL::STableMember_strategy)
@settings(max_examples=50)
def test_sqldsl::stablemember_instantiation(instance):
    assert isinstance(instance, sqlDSL::STableMember)

@given(instance=sqlDSL::STableMember_strategy)
def test_sqldsl::stablemember_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlDSL::STableMember_strategy)
def test_sqldsl::stablemember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlDSL::SSettings_strategy)
@settings(max_examples=50)
def test_sqldsl::ssettings_instantiation(instance):
    assert isinstance(instance, sqlDSL::SSettings)

@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_javapackage_type(instance):
    assert isinstance(instance.javapackage, str)


@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_javapackage_setter(instance):
    original = instance.javapackage
    instance.javapackage = original
    assert instance.javapackage == original

@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_schema_type(instance):
    assert isinstance(instance.schema, str)


@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original

@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_engine_type(instance):
    assert isinstance(instance.engine, str)


@given(instance=sqlDSL::SSettings_strategy)
def test_sqldsl::ssettings_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original

@given(instance=sqlDSL::SModel_strategy)
@settings(max_examples=50)
def test_sqldsl::smodel_instantiation(instance):
    assert isinstance(instance, sqlDSL::SModel)

@given(instance=sqlDSL::SModel_strategy)
def test_sqldsl::smodel_generatedFile_type(instance):
    assert isinstance(instance.generatedFile, str)


@given(instance=sqlDSL::SModel_strategy)
def test_sqldsl::smodel_generatedFile_setter(instance):
    original = instance.generatedFile
    instance.generatedFile = original
    assert instance.generatedFile == original

@given(instance=sqlDSL::SArtifact_strategy)
@settings(max_examples=50)
def test_sqldsl::sartifact_instantiation(instance):
    assert isinstance(instance, sqlDSL::SArtifact)

@given(instance=sqlDSL::SArtifact_strategy)
def test_sqldsl::sartifact_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sqlDSL::SArtifact_strategy)
def test_sqldsl::sartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
