import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    properties_SqlGroup,
    Sql,
    properties_SqlParameter,
    properties_Sql,
    properties_SqlFile,
    properties_SqlQuery,
    properties_SpecificDBMSProperties,
    properties_EStringToStringMapEntry,
    properties_DocumentRoot,
    properties_DatabasePropertiesListType,
    properties_Property,
    properties_SqlProperties,
    properties_DatabaseProperties,
    properties_DatabaseAlias,
    ParameterType,
    DBMS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_properties_sqlgroup_is_not_abstract():
    assert not inspect.isabstract(properties_SqlGroup)


def test_properties_sqlgroup_constructor_exists():
    assert callable(properties_SqlGroup.__init__)


def test_properties_sqlgroup_constructor_args():
    sig = inspect.signature(properties_SqlGroup.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_properties_sqlgroup_has_id():
    assert hasattr(properties_SqlGroup, "id")
    descriptor = None
    for klass in properties_SqlGroup.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_properties_sqlgroup_has_description():
    assert hasattr(properties_SqlGroup, "description")
    descriptor = None
    for klass in properties_SqlGroup.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_sql_is_not_abstract():
    assert not inspect.isabstract(Sql)


def test_sql_constructor_exists():
    assert callable(Sql.__init__)


def test_sql_constructor_args():
    sig = inspect.signature(Sql.__init__)
    params = list(sig.parameters.keys())



def test_properties_sqlparameter_is_not_abstract():
    assert not inspect.isabstract(properties_SqlParameter)


def test_properties_sqlparameter_constructor_exists():
    assert callable(properties_SqlParameter.__init__)


def test_properties_sqlparameter_constructor_args():
    sig = inspect.signature(properties_SqlParameter.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_properties_sqlparameter_has_type():
    assert hasattr(properties_SqlParameter, "type")
    descriptor = None
    for klass in properties_SqlParameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_properties_sqlparameter_has_index():
    assert hasattr(properties_SqlParameter, "index")
    descriptor = None
    for klass in properties_SqlParameter.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_properties_sqlparameter_has_name():
    assert hasattr(properties_SqlParameter, "name")
    descriptor = None
    for klass in properties_SqlParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_properties_sql_is_not_abstract():
    assert not inspect.isabstract(properties_Sql)


def test_properties_sql_constructor_exists():
    assert callable(properties_Sql.__init__)


def test_properties_sql_constructor_args():
    sig = inspect.signature(properties_Sql.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "hqlQuery" in params, "Missing parameter 'hqlQuery'"

def test_properties_sql_has_id():
    assert hasattr(properties_Sql, "id")
    descriptor = None
    for klass in properties_Sql.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_properties_sql_has_hqlQuery():
    assert hasattr(properties_Sql, "hqlQuery")
    descriptor = None
    for klass in properties_Sql.__mro__:
        if "hqlQuery" in klass.__dict__:
            descriptor = klass.__dict__["hqlQuery"]
            break
    assert isinstance(descriptor, property)



def test_properties_sqlfile_is_not_abstract():
    assert not inspect.isabstract(properties_SqlFile)


def test_properties_sqlfile_constructor_exists():
    assert callable(properties_SqlFile.__init__)


def test_properties_sqlfile_constructor_args():
    sig = inspect.signature(properties_SqlFile.__init__)
    params = list(sig.parameters.keys())
    assert "filePath" in params, "Missing parameter 'filePath'"

def test_properties_sqlfile_has_filePath():
    assert hasattr(properties_SqlFile, "filePath")
    descriptor = None
    for klass in properties_SqlFile.__mro__:
        if "filePath" in klass.__dict__:
            descriptor = klass.__dict__["filePath"]
            break
    assert isinstance(descriptor, property)



def test_properties_sqlquery_is_not_abstract():
    assert not inspect.isabstract(properties_SqlQuery)


def test_properties_sqlquery_constructor_exists():
    assert callable(properties_SqlQuery.__init__)


def test_properties_sqlquery_constructor_args():
    sig = inspect.signature(properties_SqlQuery.__init__)
    params = list(sig.parameters.keys())
    assert "queryString" in params, "Missing parameter 'queryString'"

def test_properties_sqlquery_has_queryString():
    assert hasattr(properties_SqlQuery, "queryString")
    descriptor = None
    for klass in properties_SqlQuery.__mro__:
        if "queryString" in klass.__dict__:
            descriptor = klass.__dict__["queryString"]
            break
    assert isinstance(descriptor, property)



def test_properties_specificdbmsproperties_is_not_abstract():
    assert not inspect.isabstract(properties_SpecificDBMSProperties)


def test_properties_specificdbmsproperties_constructor_exists():
    assert callable(properties_SpecificDBMSProperties.__init__)


def test_properties_specificdbmsproperties_constructor_args():
    sig = inspect.signature(properties_SpecificDBMSProperties.__init__)
    params = list(sig.parameters.keys())
    assert "dBMS" in params, "Missing parameter 'dBMS'"

def test_properties_specificdbmsproperties_has_dBMS():
    assert hasattr(properties_SpecificDBMSProperties, "dBMS")
    descriptor = None
    for klass in properties_SpecificDBMSProperties.__mro__:
        if "dBMS" in klass.__dict__:
            descriptor = klass.__dict__["dBMS"]
            break
    assert isinstance(descriptor, property)



def test_properties_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(properties_EStringToStringMapEntry)


def test_properties_estringtostringmapentry_constructor_exists():
    assert callable(properties_EStringToStringMapEntry.__init__)


def test_properties_estringtostringmapentry_constructor_args():
    sig = inspect.signature(properties_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_properties_documentroot_is_not_abstract():
    assert not inspect.isabstract(properties_DocumentRoot)


def test_properties_documentroot_constructor_exists():
    assert callable(properties_DocumentRoot.__init__)


def test_properties_documentroot_constructor_args():
    sig = inspect.signature(properties_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_properties_documentroot_has_mixed():
    assert hasattr(properties_DocumentRoot, "mixed")
    descriptor = None
    for klass in properties_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_properties_databasepropertieslisttype_is_not_abstract():
    assert not inspect.isabstract(properties_DatabasePropertiesListType)


def test_properties_databasepropertieslisttype_constructor_exists():
    assert callable(properties_DatabasePropertiesListType.__init__)


def test_properties_databasepropertieslisttype_constructor_args():
    sig = inspect.signature(properties_DatabasePropertiesListType.__init__)
    params = list(sig.parameters.keys())



def test_properties_property_is_not_abstract():
    assert not inspect.isabstract(properties_Property)


def test_properties_property_constructor_exists():
    assert callable(properties_Property.__init__)


def test_properties_property_constructor_args():
    sig = inspect.signature(properties_Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_properties_property_has_key():
    assert hasattr(properties_Property, "key")
    descriptor = None
    for klass in properties_Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_properties_property_has_value():
    assert hasattr(properties_Property, "value")
    descriptor = None
    for klass in properties_Property.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_properties_sqlproperties_is_not_abstract():
    assert not inspect.isabstract(properties_SqlProperties)


def test_properties_sqlproperties_constructor_exists():
    assert callable(properties_SqlProperties.__init__)


def test_properties_sqlproperties_constructor_args():
    sig = inspect.signature(properties_SqlProperties.__init__)
    params = list(sig.parameters.keys())



def test_properties_databaseproperties_is_not_abstract():
    assert not inspect.isabstract(properties_DatabaseProperties)


def test_properties_databaseproperties_constructor_exists():
    assert callable(properties_DatabaseProperties.__init__)


def test_properties_databaseproperties_constructor_args():
    sig = inspect.signature(properties_DatabaseProperties.__init__)
    params = list(sig.parameters.keys())
    assert "persistenceUnitName" in params, "Missing parameter 'persistenceUnitName'"
    assert "serverURL" in params, "Missing parameter 'serverURL'"
    assert "dBMS" in params, "Missing parameter 'dBMS'"
    assert "port" in params, "Missing parameter 'port'"
    assert "id" in params, "Missing parameter 'id'"
    assert "dialect" in params, "Missing parameter 'dialect'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "databaseName" in params, "Missing parameter 'databaseName'"
    assert "driverClassName" in params, "Missing parameter 'driverClassName'"

def test_properties_databaseproperties_has_persistenceUnitName():
    assert hasattr(properties_DatabaseProperties, "persistenceUnitName")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "persistenceUnitName" in klass.__dict__:
            descriptor = klass.__dict__["persistenceUnitName"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_serverURL():
    assert hasattr(properties_DatabaseProperties, "serverURL")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "serverURL" in klass.__dict__:
            descriptor = klass.__dict__["serverURL"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_dBMS():
    assert hasattr(properties_DatabaseProperties, "dBMS")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "dBMS" in klass.__dict__:
            descriptor = klass.__dict__["dBMS"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_port():
    assert hasattr(properties_DatabaseProperties, "port")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_id():
    assert hasattr(properties_DatabaseProperties, "id")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_dialect():
    assert hasattr(properties_DatabaseProperties, "dialect")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "dialect" in klass.__dict__:
            descriptor = klass.__dict__["dialect"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_namespace():
    assert hasattr(properties_DatabaseProperties, "namespace")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_password():
    assert hasattr(properties_DatabaseProperties, "password")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_username():
    assert hasattr(properties_DatabaseProperties, "username")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_databaseName():
    assert hasattr(properties_DatabaseProperties, "databaseName")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "databaseName" in klass.__dict__:
            descriptor = klass.__dict__["databaseName"]
            break
    assert isinstance(descriptor, property)

def test_properties_databaseproperties_has_driverClassName():
    assert hasattr(properties_DatabaseProperties, "driverClassName")
    descriptor = None
    for klass in properties_DatabaseProperties.__mro__:
        if "driverClassName" in klass.__dict__:
            descriptor = klass.__dict__["driverClassName"]
            break
    assert isinstance(descriptor, property)



def test_properties_databasealias_is_not_abstract():
    assert not inspect.isabstract(properties_DatabaseAlias)


def test_properties_databasealias_constructor_exists():
    assert callable(properties_DatabaseAlias.__init__)


def test_properties_databasealias_constructor_args():
    sig = inspect.signature(properties_DatabaseAlias.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "id" in params, "Missing parameter 'id'"

def test_properties_databasealias_has_alias():
    assert hasattr(properties_DatabaseAlias, "alias")
    descriptor = None
    for klass in properties_DatabaseAlias.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_properties_databasealias_has_id():
    assert hasattr(properties_DatabaseAlias, "id")
    descriptor = None
    for klass in properties_DatabaseAlias.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_parametertype_exists():
    # Check that the Enumeration exists
    assert ParameterType is not None

def test_parametertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterType]
    expected_literals = [
        "Double",
        "BinaryStream",
        "Bytes",
        "URL",
        "Float",
        "Token",
        "Timestamp",
        "DateCalendar",
        "Short",
        "Int",
        "Time",
        "CharacterStream",
        "Object",
        "Byte",
        "BigDecimal",
        "AsciiStream",
        "String",
        "Boolean",
        "TimeStampCalendar",
        "Clob",
        "Array",
        "Long",
        "Ref",
        "TimeCalendar",
        "Date",
        "Blob",
        "UnicodeStream",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterType"

def test_dbms_exists():
    # Check that the Enumeration exists
    assert DBMS is not None

def test_dbms_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DBMS]
    expected_literals = [
        "PgSQL",
        "MySQL",
        "SQLite",
        "HSQLDB",
        "MSAccess",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DBMS"


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
properties_SqlGroup_strategy = st.builds(
    properties_SqlGroup,
    id=
        safe_text,
    description=
        safe_text
)
Sql_strategy = st.builds(
    Sql,
)
properties_SqlParameter_strategy = st.builds(
    properties_SqlParameter,
    type=
        safe_text,
    index=
        safe_text,
    name=
        safe_text
)
properties_Sql_strategy = st.builds(
    properties_Sql,
    id=
        safe_text,
    hqlQuery=
        safe_text
)
properties_SqlFile_strategy = st.builds(
    properties_SqlFile,
    filePath=
        safe_text
)
properties_SqlQuery_strategy = st.builds(
    properties_SqlQuery,
    queryString=
        safe_text
)
properties_SpecificDBMSProperties_strategy = st.builds(
    properties_SpecificDBMSProperties,
    dBMS=
        safe_text
)
properties_EStringToStringMapEntry_strategy = st.builds(
    properties_EStringToStringMapEntry,
)
properties_DocumentRoot_strategy = st.builds(
    properties_DocumentRoot,
    mixed=
        safe_text
)
properties_DatabasePropertiesListType_strategy = st.builds(
    properties_DatabasePropertiesListType,
)
properties_Property_strategy = st.builds(
    properties_Property,
    key=
        safe_text,
    value=
        safe_text
)
properties_SqlProperties_strategy = st.builds(
    properties_SqlProperties,
)
properties_DatabaseProperties_strategy = st.builds(
    properties_DatabaseProperties,
    persistenceUnitName=
        safe_text,
    serverURL=
        safe_text,
    dBMS=
        safe_text,
    port=
        safe_text,
    id=
        safe_text,
    dialect=
        safe_text,
    namespace=
        safe_text,
    password=
        safe_text,
    username=
        safe_text,
    databaseName=
        safe_text,
    driverClassName=
        safe_text
)
properties_DatabaseAlias_strategy = st.builds(
    properties_DatabaseAlias,
    alias=
        safe_text,
    id=
        safe_text
)

@given(instance=properties_SqlGroup_strategy)
@settings(max_examples=50)
def test_properties_sqlgroup_instantiation(instance):
    assert isinstance(instance, properties_SqlGroup)



@given(instance=properties_SqlGroup_strategy)
def test_properties_sqlgroup_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=properties_SqlGroup_strategy)
def test_properties_sqlgroup_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Sql_strategy)
@settings(max_examples=50)
def test_sql_instantiation(instance):
    assert isinstance(instance, Sql)

@given(instance=properties_SqlParameter_strategy)
@settings(max_examples=50)
def test_properties_sqlparameter_instantiation(instance):
    assert isinstance(instance, properties_SqlParameter)



@given(instance=properties_SqlParameter_strategy)
def test_properties_sqlparameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=properties_SqlParameter_strategy)
def test_properties_sqlparameter_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=properties_SqlParameter_strategy)
def test_properties_sqlparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=properties_Sql_strategy)
@settings(max_examples=50)
def test_properties_sql_instantiation(instance):
    assert isinstance(instance, properties_Sql)



@given(instance=properties_Sql_strategy)
def test_properties_sql_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=properties_Sql_strategy)
def test_properties_sql_hqlQuery_setter(instance):
    original = instance.hqlQuery
    instance.hqlQuery = original
    assert instance.hqlQuery == original

@given(instance=properties_SqlFile_strategy)
@settings(max_examples=50)
def test_properties_sqlfile_instantiation(instance):
    assert isinstance(instance, properties_SqlFile)



@given(instance=properties_SqlFile_strategy)
def test_properties_sqlfile_filePath_setter(instance):
    original = instance.filePath
    instance.filePath = original
    assert instance.filePath == original

@given(instance=properties_SqlQuery_strategy)
@settings(max_examples=50)
def test_properties_sqlquery_instantiation(instance):
    assert isinstance(instance, properties_SqlQuery)



@given(instance=properties_SqlQuery_strategy)
def test_properties_sqlquery_queryString_setter(instance):
    original = instance.queryString
    instance.queryString = original
    assert instance.queryString == original

@given(instance=properties_SpecificDBMSProperties_strategy)
@settings(max_examples=50)
def test_properties_specificdbmsproperties_instantiation(instance):
    assert isinstance(instance, properties_SpecificDBMSProperties)



@given(instance=properties_SpecificDBMSProperties_strategy)
def test_properties_specificdbmsproperties_dBMS_setter(instance):
    original = instance.dBMS
    instance.dBMS = original
    assert instance.dBMS == original

@given(instance=properties_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_properties_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, properties_EStringToStringMapEntry)

@given(instance=properties_DocumentRoot_strategy)
@settings(max_examples=50)
def test_properties_documentroot_instantiation(instance):
    assert isinstance(instance, properties_DocumentRoot)



@given(instance=properties_DocumentRoot_strategy)
def test_properties_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=properties_DatabasePropertiesListType_strategy)
@settings(max_examples=50)
def test_properties_databasepropertieslisttype_instantiation(instance):
    assert isinstance(instance, properties_DatabasePropertiesListType)

@given(instance=properties_Property_strategy)
@settings(max_examples=50)
def test_properties_property_instantiation(instance):
    assert isinstance(instance, properties_Property)



@given(instance=properties_Property_strategy)
def test_properties_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=properties_Property_strategy)
def test_properties_property_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=properties_SqlProperties_strategy)
@settings(max_examples=50)
def test_properties_sqlproperties_instantiation(instance):
    assert isinstance(instance, properties_SqlProperties)

@given(instance=properties_DatabaseProperties_strategy)
@settings(max_examples=50)
def test_properties_databaseproperties_instantiation(instance):
    assert isinstance(instance, properties_DatabaseProperties)



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_persistenceUnitName_setter(instance):
    original = instance.persistenceUnitName
    instance.persistenceUnitName = original
    assert instance.persistenceUnitName == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_serverURL_setter(instance):
    original = instance.serverURL
    instance.serverURL = original
    assert instance.serverURL == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_dBMS_setter(instance):
    original = instance.dBMS
    instance.dBMS = original
    assert instance.dBMS == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_dialect_setter(instance):
    original = instance.dialect
    instance.dialect = original
    assert instance.dialect == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_databaseName_setter(instance):
    original = instance.databaseName
    instance.databaseName = original
    assert instance.databaseName == original



@given(instance=properties_DatabaseProperties_strategy)
def test_properties_databaseproperties_driverClassName_setter(instance):
    original = instance.driverClassName
    instance.driverClassName = original
    assert instance.driverClassName == original

@given(instance=properties_DatabaseAlias_strategy)
@settings(max_examples=50)
def test_properties_databasealias_instantiation(instance):
    assert isinstance(instance, properties_DatabaseAlias)



@given(instance=properties_DatabaseAlias_strategy)
def test_properties_databasealias_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=properties_DatabaseAlias_strategy)
def test_properties_databasealias_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
