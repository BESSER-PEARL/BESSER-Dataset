import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SInlinedSQLType,
    sqlDSL_SDecimal,
    sqlDSL_SString,
    sqlDSL_SEnumLiteral,
    SExtDeclaredSQLType,
    sqlDSL_SInlinedSQLType,
    SArtifact,
    sqlDSL_SEnum,
    sqlDSL_STable,
    sqlDSL_SExtDeclaredSQLType,
    STableMember,
    sqlDSL_SJoinColumn,
    sqlDSL_SColumn,
    sqlDSL_SColumnProps,
    sqlDSL_STableMember,
    sqlDSL_SSettings,
    sqlDSL_SModel,
    sqlDSL_SArtifact,
    SIndex,
    SSimpleTypes,
    SDBEngine,
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



def test_sqldsl_sdecimal_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SDecimal)


def test_sqldsl_sdecimal_constructor_exists():
    assert callable(sqlDSL_SDecimal.__init__)


def test_sqldsl_sdecimal_constructor_args():
    sig = inspect.signature(sqlDSL_SDecimal.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl_sstring_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SString)


def test_sqldsl_sstring_constructor_exists():
    assert callable(sqlDSL_SString.__init__)


def test_sqldsl_sstring_constructor_args():
    sig = inspect.signature(sqlDSL_SString.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl_senumliteral_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SEnumLiteral)


def test_sqldsl_senumliteral_constructor_exists():
    assert callable(sqlDSL_SEnumLiteral.__init__)


def test_sqldsl_senumliteral_constructor_args():
    sig = inspect.signature(sqlDSL_SEnumLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_sqldsl_senumliteral_has_name():
    assert hasattr(sqlDSL_SEnumLiteral, "name")
    descriptor = None
    for klass in sqlDSL_SEnumLiteral.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_senumliteral_has_value():
    assert hasattr(sqlDSL_SEnumLiteral, "value")
    descriptor = None
    for klass in sqlDSL_SEnumLiteral.__mro__:
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



def test_sqldsl_sinlinedsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SInlinedSQLType)


def test_sqldsl_sinlinedsqltype_constructor_exists():
    assert callable(sqlDSL_SInlinedSQLType.__init__)


def test_sqldsl_sinlinedsqltype_constructor_args():
    sig = inspect.signature(sqlDSL_SInlinedSQLType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_sqldsl_sinlinedsqltype_has_value():
    assert hasattr(sqlDSL_SInlinedSQLType, "value")
    descriptor = None
    for klass in sqlDSL_SInlinedSQLType.__mro__:
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



def test_sqldsl_senum_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SEnum)


def test_sqldsl_senum_constructor_exists():
    assert callable(sqlDSL_SEnum.__init__)


def test_sqldsl_senum_constructor_args():
    sig = inspect.signature(sqlDSL_SEnum.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl_stable_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_STable)


def test_sqldsl_stable_constructor_exists():
    assert callable(sqlDSL_STable.__init__)


def test_sqldsl_stable_constructor_args():
    sig = inspect.signature(sqlDSL_STable.__init__)
    params = list(sig.parameters.keys())
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "cached" in params, "Missing parameter 'cached'"
    assert "entityname" in params, "Missing parameter 'entityname'"

def test_sqldsl_stable_has_prefix():
    assert hasattr(sqlDSL_STable, "prefix")
    descriptor = None
    for klass in sqlDSL_STable.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_stable_has_cached():
    assert hasattr(sqlDSL_STable, "cached")
    descriptor = None
    for klass in sqlDSL_STable.__mro__:
        if "cached" in klass.__dict__:
            descriptor = klass.__dict__["cached"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_stable_has_entityname():
    assert hasattr(sqlDSL_STable, "entityname")
    descriptor = None
    for klass in sqlDSL_STable.__mro__:
        if "entityname" in klass.__dict__:
            descriptor = klass.__dict__["entityname"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_sextdeclaredsqltype_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SExtDeclaredSQLType)


def test_sqldsl_sextdeclaredsqltype_constructor_exists():
    assert callable(sqlDSL_SExtDeclaredSQLType.__init__)


def test_sqldsl_sextdeclaredsqltype_constructor_args():
    sig = inspect.signature(sqlDSL_SExtDeclaredSQLType.__init__)
    params = list(sig.parameters.keys())



def test_stablemember_is_not_abstract():
    assert not inspect.isabstract(STableMember)


def test_stablemember_constructor_exists():
    assert callable(STableMember.__init__)


def test_stablemember_constructor_args():
    sig = inspect.signature(STableMember.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl_sjoincolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SJoinColumn)


def test_sqldsl_sjoincolumn_constructor_exists():
    assert callable(sqlDSL_SJoinColumn.__init__)


def test_sqldsl_sjoincolumn_constructor_args():
    sig = inspect.signature(sqlDSL_SJoinColumn.__init__)
    params = list(sig.parameters.keys())



def test_sqldsl_scolumn_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SColumn)


def test_sqldsl_scolumn_constructor_exists():
    assert callable(sqlDSL_SColumn.__init__)


def test_sqldsl_scolumn_constructor_args():
    sig = inspect.signature(sqlDSL_SColumn.__init__)
    params = list(sig.parameters.keys())
    assert "simpleType" in params, "Missing parameter 'simpleType'"

def test_sqldsl_scolumn_has_simpleType():
    assert hasattr(sqlDSL_SColumn, "simpleType")
    descriptor = None
    for klass in sqlDSL_SColumn.__mro__:
        if "simpleType" in klass.__dict__:
            descriptor = klass.__dict__["simpleType"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_scolumnprops_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SColumnProps)


def test_sqldsl_scolumnprops_constructor_exists():
    assert callable(sqlDSL_SColumnProps.__init__)


def test_sqldsl_scolumnprops_constructor_args():
    sig = inspect.signature(sqlDSL_SColumnProps.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "aes" in params, "Missing parameter 'aes'"
    assert "index" in params, "Missing parameter 'index'"
    assert "javacolumn" in params, "Missing parameter 'javacolumn'"

def test_sqldsl_scolumnprops_has_nullable():
    assert hasattr(sqlDSL_SColumnProps, "nullable")
    descriptor = None
    for klass in sqlDSL_SColumnProps.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_scolumnprops_has_aes():
    assert hasattr(sqlDSL_SColumnProps, "aes")
    descriptor = None
    for klass in sqlDSL_SColumnProps.__mro__:
        if "aes" in klass.__dict__:
            descriptor = klass.__dict__["aes"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_scolumnprops_has_index():
    assert hasattr(sqlDSL_SColumnProps, "index")
    descriptor = None
    for klass in sqlDSL_SColumnProps.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_scolumnprops_has_javacolumn():
    assert hasattr(sqlDSL_SColumnProps, "javacolumn")
    descriptor = None
    for klass in sqlDSL_SColumnProps.__mro__:
        if "javacolumn" in klass.__dict__:
            descriptor = klass.__dict__["javacolumn"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_stablemember_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_STableMember)


def test_sqldsl_stablemember_constructor_exists():
    assert callable(sqlDSL_STableMember.__init__)


def test_sqldsl_stablemember_constructor_args():
    sig = inspect.signature(sqlDSL_STableMember.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldsl_stablemember_has_name():
    assert hasattr(sqlDSL_STableMember, "name")
    descriptor = None
    for klass in sqlDSL_STableMember.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_ssettings_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SSettings)


def test_sqldsl_ssettings_constructor_exists():
    assert callable(sqlDSL_SSettings.__init__)


def test_sqldsl_ssettings_constructor_args():
    sig = inspect.signature(sqlDSL_SSettings.__init__)
    params = list(sig.parameters.keys())
    assert "javapackage" in params, "Missing parameter 'javapackage'"
    assert "schema" in params, "Missing parameter 'schema'"
    assert "engine" in params, "Missing parameter 'engine'"

def test_sqldsl_ssettings_has_javapackage():
    assert hasattr(sqlDSL_SSettings, "javapackage")
    descriptor = None
    for klass in sqlDSL_SSettings.__mro__:
        if "javapackage" in klass.__dict__:
            descriptor = klass.__dict__["javapackage"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_ssettings_has_schema():
    assert hasattr(sqlDSL_SSettings, "schema")
    descriptor = None
    for klass in sqlDSL_SSettings.__mro__:
        if "schema" in klass.__dict__:
            descriptor = klass.__dict__["schema"]
            break
    assert isinstance(descriptor, property)

def test_sqldsl_ssettings_has_engine():
    assert hasattr(sqlDSL_SSettings, "engine")
    descriptor = None
    for klass in sqlDSL_SSettings.__mro__:
        if "engine" in klass.__dict__:
            descriptor = klass.__dict__["engine"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_smodel_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SModel)


def test_sqldsl_smodel_constructor_exists():
    assert callable(sqlDSL_SModel.__init__)


def test_sqldsl_smodel_constructor_args():
    sig = inspect.signature(sqlDSL_SModel.__init__)
    params = list(sig.parameters.keys())
    assert "generatedFile" in params, "Missing parameter 'generatedFile'"

def test_sqldsl_smodel_has_generatedFile():
    assert hasattr(sqlDSL_SModel, "generatedFile")
    descriptor = None
    for klass in sqlDSL_SModel.__mro__:
        if "generatedFile" in klass.__dict__:
            descriptor = klass.__dict__["generatedFile"]
            break
    assert isinstance(descriptor, property)



def test_sqldsl_sartifact_is_not_abstract():
    assert not inspect.isabstract(sqlDSL_SArtifact)


def test_sqldsl_sartifact_constructor_exists():
    assert callable(sqlDSL_SArtifact.__init__)


def test_sqldsl_sartifact_constructor_args():
    sig = inspect.signature(sqlDSL_SArtifact.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sqldsl_sartifact_has_name():
    assert hasattr(sqlDSL_SArtifact, "name")
    descriptor = None
    for klass in sqlDSL_SArtifact.__mro__:
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
        "UNIQUE",
        "NO",
        "SPATIAL",
        "YES",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SIndex"

def test_ssimpletypes_exists():
    # Check that the Enumeration exists
    assert SSimpleTypes is not None

def test_ssimpletypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SSimpleTypes]
    expected_literals = [
        "MEDIUM_INT",
        "DATETIME",
        "BLOB",
        "Currency",
        "POLYGON",
        "INT",
        "DATE",
        "SMALL_INT",
        "TINY_INT",
        "FOTO",
        "TIME",
        "BOOLEAN",
        "Coordinate",
        "POINT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SSimpleTypes"

def test_sdbengine_exists():
    # Check that the Enumeration exists
    assert SDBEngine is not None

def test_sdbengine_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SDBEngine]
    expected_literals = [
        "MYISAM",
        "INNODB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SDBEngine"


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
sqlDSL_SDecimal_strategy = st.builds(
    sqlDSL_SDecimal,
)
sqlDSL_SString_strategy = st.builds(
    sqlDSL_SString,
)
sqlDSL_SEnumLiteral_strategy = st.builds(
    sqlDSL_SEnumLiteral,
    name=
        safe_text,
    value=
        st.integers()
)
SExtDeclaredSQLType_strategy = st.builds(
    SExtDeclaredSQLType,
)
sqlDSL_SInlinedSQLType_strategy = st.builds(
    sqlDSL_SInlinedSQLType,
    value=
        st.integers()
)
SArtifact_strategy = st.builds(
    SArtifact,
)
sqlDSL_SEnum_strategy = st.builds(
    sqlDSL_SEnum,
)
sqlDSL_STable_strategy = st.builds(
    sqlDSL_STable,
    prefix=
        safe_text,
    cached=
        st.booleans(),
    entityname=
        safe_text
)
sqlDSL_SExtDeclaredSQLType_strategy = st.builds(
    sqlDSL_SExtDeclaredSQLType,
)
STableMember_strategy = st.builds(
    STableMember,
)
sqlDSL_SJoinColumn_strategy = st.builds(
    sqlDSL_SJoinColumn,
)
sqlDSL_SColumn_strategy = st.builds(
    sqlDSL_SColumn,
    simpleType=
        safe_text
)
sqlDSL_SColumnProps_strategy = st.builds(
    sqlDSL_SColumnProps,
    nullable=
        st.booleans(),
    aes=
        st.booleans(),
    index=
        safe_text,
    javacolumn=
        safe_text
)
sqlDSL_STableMember_strategy = st.builds(
    sqlDSL_STableMember,
    name=
        safe_text
)
sqlDSL_SSettings_strategy = st.builds(
    sqlDSL_SSettings,
    javapackage=
        safe_text,
    schema=
        safe_text,
    engine=
        safe_text
)
sqlDSL_SModel_strategy = st.builds(
    sqlDSL_SModel,
    generatedFile=
        safe_text
)
sqlDSL_SArtifact_strategy = st.builds(
    sqlDSL_SArtifact,
    name=
        safe_text
)

@given(instance=SInlinedSQLType_strategy)
@settings(max_examples=50)
def test_sinlinedsqltype_instantiation(instance):
    assert isinstance(instance, SInlinedSQLType)

@given(instance=sqlDSL_SDecimal_strategy)
@settings(max_examples=50)
def test_sqldsl_sdecimal_instantiation(instance):
    assert isinstance(instance, sqlDSL_SDecimal)

@given(instance=sqlDSL_SString_strategy)
@settings(max_examples=50)
def test_sqldsl_sstring_instantiation(instance):
    assert isinstance(instance, sqlDSL_SString)

@given(instance=sqlDSL_SEnumLiteral_strategy)
@settings(max_examples=50)
def test_sqldsl_senumliteral_instantiation(instance):
    assert isinstance(instance, sqlDSL_SEnumLiteral)



@given(instance=sqlDSL_SEnumLiteral_strategy)
def test_sqldsl_senumliteral_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sqlDSL_SEnumLiteral_strategy)
def test_sqldsl_senumliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SExtDeclaredSQLType_strategy)
@settings(max_examples=50)
def test_sextdeclaredsqltype_instantiation(instance):
    assert isinstance(instance, SExtDeclaredSQLType)

@given(instance=sqlDSL_SInlinedSQLType_strategy)
@settings(max_examples=50)
def test_sqldsl_sinlinedsqltype_instantiation(instance):
    assert isinstance(instance, sqlDSL_SInlinedSQLType)



@given(instance=sqlDSL_SInlinedSQLType_strategy)
def test_sqldsl_sinlinedsqltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=SArtifact_strategy)
@settings(max_examples=50)
def test_sartifact_instantiation(instance):
    assert isinstance(instance, SArtifact)

@given(instance=sqlDSL_SEnum_strategy)
@settings(max_examples=50)
def test_sqldsl_senum_instantiation(instance):
    assert isinstance(instance, sqlDSL_SEnum)

@given(instance=sqlDSL_STable_strategy)
@settings(max_examples=50)
def test_sqldsl_stable_instantiation(instance):
    assert isinstance(instance, sqlDSL_STable)



@given(instance=sqlDSL_STable_strategy)
def test_sqldsl_stable_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=sqlDSL_STable_strategy)
def test_sqldsl_stable_cached_setter(instance):
    original = instance.cached
    instance.cached = original
    assert instance.cached == original



@given(instance=sqlDSL_STable_strategy)
def test_sqldsl_stable_entityname_setter(instance):
    original = instance.entityname
    instance.entityname = original
    assert instance.entityname == original

@given(instance=sqlDSL_SExtDeclaredSQLType_strategy)
@settings(max_examples=50)
def test_sqldsl_sextdeclaredsqltype_instantiation(instance):
    assert isinstance(instance, sqlDSL_SExtDeclaredSQLType)

@given(instance=STableMember_strategy)
@settings(max_examples=50)
def test_stablemember_instantiation(instance):
    assert isinstance(instance, STableMember)

@given(instance=sqlDSL_SJoinColumn_strategy)
@settings(max_examples=50)
def test_sqldsl_sjoincolumn_instantiation(instance):
    assert isinstance(instance, sqlDSL_SJoinColumn)

@given(instance=sqlDSL_SColumn_strategy)
@settings(max_examples=50)
def test_sqldsl_scolumn_instantiation(instance):
    assert isinstance(instance, sqlDSL_SColumn)



@given(instance=sqlDSL_SColumn_strategy)
def test_sqldsl_scolumn_simpleType_setter(instance):
    original = instance.simpleType
    instance.simpleType = original
    assert instance.simpleType == original

@given(instance=sqlDSL_SColumnProps_strategy)
@settings(max_examples=50)
def test_sqldsl_scolumnprops_instantiation(instance):
    assert isinstance(instance, sqlDSL_SColumnProps)



@given(instance=sqlDSL_SColumnProps_strategy)
def test_sqldsl_scolumnprops_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_sqldsl_scolumnprops_aes_setter(instance):
    original = instance.aes
    instance.aes = original
    assert instance.aes == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_sqldsl_scolumnprops_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=sqlDSL_SColumnProps_strategy)
def test_sqldsl_scolumnprops_javacolumn_setter(instance):
    original = instance.javacolumn
    instance.javacolumn = original
    assert instance.javacolumn == original

@given(instance=sqlDSL_STableMember_strategy)
@settings(max_examples=50)
def test_sqldsl_stablemember_instantiation(instance):
    assert isinstance(instance, sqlDSL_STableMember)



@given(instance=sqlDSL_STableMember_strategy)
def test_sqldsl_stablemember_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sqlDSL_SSettings_strategy)
@settings(max_examples=50)
def test_sqldsl_ssettings_instantiation(instance):
    assert isinstance(instance, sqlDSL_SSettings)



@given(instance=sqlDSL_SSettings_strategy)
def test_sqldsl_ssettings_javapackage_setter(instance):
    original = instance.javapackage
    instance.javapackage = original
    assert instance.javapackage == original



@given(instance=sqlDSL_SSettings_strategy)
def test_sqldsl_ssettings_schema_setter(instance):
    original = instance.schema
    instance.schema = original
    assert instance.schema == original



@given(instance=sqlDSL_SSettings_strategy)
def test_sqldsl_ssettings_engine_setter(instance):
    original = instance.engine
    instance.engine = original
    assert instance.engine == original

@given(instance=sqlDSL_SModel_strategy)
@settings(max_examples=50)
def test_sqldsl_smodel_instantiation(instance):
    assert isinstance(instance, sqlDSL_SModel)



@given(instance=sqlDSL_SModel_strategy)
def test_sqldsl_smodel_generatedFile_setter(instance):
    original = instance.generatedFile
    instance.generatedFile = original
    assert instance.generatedFile == original

@given(instance=sqlDSL_SArtifact_strategy)
@settings(max_examples=50)
def test_sqldsl_sartifact_instantiation(instance):
    assert isinstance(instance, sqlDSL_SArtifact)



@given(instance=sqlDSL_SArtifact_strategy)
def test_sqldsl_sartifact_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
