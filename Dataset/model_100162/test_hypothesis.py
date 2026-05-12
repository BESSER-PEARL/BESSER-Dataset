import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    oracle::OracleSequenceProperty,
    ExtensibleModel,
    oracle::DatabaseModuleExtensibleProperty,
    oracle::OracleUser,
    oracle::OraclePrivilege,
    oracle::TableSpaceRelation,
    oracle::TableSpace,
    DatabaseResourceData,
    oracle::OracleUserResourceData,
    oracle::SequenceResourceData,
    oracle::TriggerResourceData,
    oracle::OracleSpaceResourceData,
    oracle::OracleModuleProperty,
    oracle::OracleViewProperty,
    oracle::OracleIndexProperty,
    oracle::OracleTableProperty,
    table_type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oracle::oraclesequenceproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleSequenceProperty)


def test_oracle::oraclesequenceproperty_constructor_exists():
    assert callable(oracle::OracleSequenceProperty.__init__)


def test_oracle::oraclesequenceproperty_constructor_args():
    sig = inspect.signature(oracle::OracleSequenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle::oraclesequenceproperty_has_space():
    assert hasattr(oracle::OracleSequenceProperty, "space")
    descriptor = None
    for klass in oracle::OracleSequenceProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_extensiblemodel_is_not_abstract():
    assert not inspect.isabstract(ExtensibleModel)


def test_extensiblemodel_constructor_exists():
    assert callable(ExtensibleModel.__init__)


def test_extensiblemodel_constructor_args():
    sig = inspect.signature(ExtensibleModel.__init__)
    params = list(sig.parameters.keys())



def test_oracle::databasemoduleextensibleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::DatabaseModuleExtensibleProperty)


def test_oracle::databasemoduleextensibleproperty_constructor_exists():
    assert callable(oracle::DatabaseModuleExtensibleProperty.__init__)


def test_oracle::databasemoduleextensibleproperty_constructor_args():
    sig = inspect.signature(oracle::DatabaseModuleExtensibleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "splitField" in params, "Missing parameter 'splitField'"
    assert "space" in params, "Missing parameter 'space'"
    assert "splitNum" in params, "Missing parameter 'splitNum'"
    assert "tableType" in params, "Missing parameter 'tableType'"
    assert "bizPkg" in params, "Missing parameter 'bizPkg'"
    assert "startDate" in params, "Missing parameter 'startDate'"

def test_oracle::databasemoduleextensibleproperty_has_splitField():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "splitField")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "splitField" in klass.__dict__:
            descriptor = klass.__dict__["splitField"]
            break
    assert isinstance(descriptor, property)

def test_oracle::databasemoduleextensibleproperty_has_space():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "space")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_oracle::databasemoduleextensibleproperty_has_splitNum():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "splitNum")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "splitNum" in klass.__dict__:
            descriptor = klass.__dict__["splitNum"]
            break
    assert isinstance(descriptor, property)

def test_oracle::databasemoduleextensibleproperty_has_tableType():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "tableType")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "tableType" in klass.__dict__:
            descriptor = klass.__dict__["tableType"]
            break
    assert isinstance(descriptor, property)

def test_oracle::databasemoduleextensibleproperty_has_bizPkg():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "bizPkg")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "bizPkg" in klass.__dict__:
            descriptor = klass.__dict__["bizPkg"]
            break
    assert isinstance(descriptor, property)

def test_oracle::databasemoduleextensibleproperty_has_startDate():
    assert hasattr(oracle::DatabaseModuleExtensibleProperty, "startDate")
    descriptor = None
    for klass in oracle::DatabaseModuleExtensibleProperty.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oracleuser_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleUser)


def test_oracle::oracleuser_constructor_exists():
    assert callable(oracle::OracleUser.__init__)


def test_oracle::oracleuser_constructor_args():
    sig = inspect.signature(oracle::OracleUser.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "defaultTableSpace" in params, "Missing parameter 'defaultTableSpace'"
    assert "enable" in params, "Missing parameter 'enable'"
    assert "decription" in params, "Missing parameter 'decription'"
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "name" in params, "Missing parameter 'name'"

def test_oracle::oracleuser_has_password():
    assert hasattr(oracle::OracleUser, "password")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleuser_has_defaultTableSpace():
    assert hasattr(oracle::OracleUser, "defaultTableSpace")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "defaultTableSpace" in klass.__dict__:
            descriptor = klass.__dict__["defaultTableSpace"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleuser_has_enable():
    assert hasattr(oracle::OracleUser, "enable")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "enable" in klass.__dict__:
            descriptor = klass.__dict__["enable"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleuser_has_decription():
    assert hasattr(oracle::OracleUser, "decription")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "decription" in klass.__dict__:
            descriptor = klass.__dict__["decription"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleuser_has_attributes():
    assert hasattr(oracle::OracleUser, "attributes")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleuser_has_name():
    assert hasattr(oracle::OracleUser, "name")
    descriptor = None
    for klass in oracle::OracleUser.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oracleprivilege_is_not_abstract():
    assert not inspect.isabstract(oracle::OraclePrivilege)


def test_oracle::oracleprivilege_constructor_exists():
    assert callable(oracle::OraclePrivilege.__init__)


def test_oracle::oracleprivilege_constructor_args():
    sig = inspect.signature(oracle::OraclePrivilege.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "decription" in params, "Missing parameter 'decription'"
    assert "name" in params, "Missing parameter 'name'"

def test_oracle::oracleprivilege_has_type():
    assert hasattr(oracle::OraclePrivilege, "type")
    descriptor = None
    for klass in oracle::OraclePrivilege.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleprivilege_has_decription():
    assert hasattr(oracle::OraclePrivilege, "decription")
    descriptor = None
    for klass in oracle::OraclePrivilege.__mro__:
        if "decription" in klass.__dict__:
            descriptor = klass.__dict__["decription"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracleprivilege_has_name():
    assert hasattr(oracle::OraclePrivilege, "name")
    descriptor = None
    for klass in oracle::OraclePrivilege.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_oracle::tablespacerelation_is_not_abstract():
    assert not inspect.isabstract(oracle::TableSpaceRelation)


def test_oracle::tablespacerelation_constructor_exists():
    assert callable(oracle::TableSpaceRelation.__init__)


def test_oracle::tablespacerelation_constructor_args():
    sig = inspect.signature(oracle::TableSpaceRelation.__init__)
    params = list(sig.parameters.keys())
    assert "mainSpace" in params, "Missing parameter 'mainSpace'"
    assert "indexSpace" in params, "Missing parameter 'indexSpace'"

def test_oracle::tablespacerelation_has_mainSpace():
    assert hasattr(oracle::TableSpaceRelation, "mainSpace")
    descriptor = None
    for klass in oracle::TableSpaceRelation.__mro__:
        if "mainSpace" in klass.__dict__:
            descriptor = klass.__dict__["mainSpace"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespacerelation_has_indexSpace():
    assert hasattr(oracle::TableSpaceRelation, "indexSpace")
    descriptor = None
    for klass in oracle::TableSpaceRelation.__mro__:
        if "indexSpace" in klass.__dict__:
            descriptor = klass.__dict__["indexSpace"]
            break
    assert isinstance(descriptor, property)



def test_oracle::tablespace_is_not_abstract():
    assert not inspect.isabstract(oracle::TableSpace)


def test_oracle::tablespace_constructor_exists():
    assert callable(oracle::TableSpace.__init__)


def test_oracle::tablespace_constructor_args():
    sig = inspect.signature(oracle::TableSpace.__init__)
    params = list(sig.parameters.keys())
    assert "logicName" in params, "Missing parameter 'logicName'"
    assert "chineseName" in params, "Missing parameter 'chineseName'"
    assert "user" in params, "Missing parameter 'user'"
    assert "file" in params, "Missing parameter 'file'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "size" in params, "Missing parameter 'size'"

def test_oracle::tablespace_has_logicName():
    assert hasattr(oracle::TableSpace, "logicName")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "logicName" in klass.__dict__:
            descriptor = klass.__dict__["logicName"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_chineseName():
    assert hasattr(oracle::TableSpace, "chineseName")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "chineseName" in klass.__dict__:
            descriptor = klass.__dict__["chineseName"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_user():
    assert hasattr(oracle::TableSpace, "user")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_file():
    assert hasattr(oracle::TableSpace, "file")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_name():
    assert hasattr(oracle::TableSpace, "name")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_description():
    assert hasattr(oracle::TableSpace, "description")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_oracle::tablespace_has_size():
    assert hasattr(oracle::TableSpace, "size")
    descriptor = None
    for klass in oracle::TableSpace.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_databaseresourcedata_is_not_abstract():
    assert not inspect.isabstract(DatabaseResourceData)


def test_databaseresourcedata_constructor_exists():
    assert callable(DatabaseResourceData.__init__)


def test_databaseresourcedata_constructor_args():
    sig = inspect.signature(DatabaseResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle::oracleuserresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleUserResourceData)


def test_oracle::oracleuserresourcedata_constructor_exists():
    assert callable(oracle::OracleUserResourceData.__init__)


def test_oracle::oracleuserresourcedata_constructor_args():
    sig = inspect.signature(oracle::OracleUserResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle::sequenceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle::SequenceResourceData)


def test_oracle::sequenceresourcedata_constructor_exists():
    assert callable(oracle::SequenceResourceData.__init__)


def test_oracle::sequenceresourcedata_constructor_args():
    sig = inspect.signature(oracle::SequenceResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "useCache" in params, "Missing parameter 'useCache'"
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "start" in params, "Missing parameter 'start'"
    assert "cache" in params, "Missing parameter 'cache'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"

def test_oracle::sequenceresourcedata_has_cycle():
    assert hasattr(oracle::SequenceResourceData, "cycle")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_useCache():
    assert hasattr(oracle::SequenceResourceData, "useCache")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "useCache" in klass.__dict__:
            descriptor = klass.__dict__["useCache"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_isHistory():
    assert hasattr(oracle::SequenceResourceData, "isHistory")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "isHistory" in klass.__dict__:
            descriptor = klass.__dict__["isHistory"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_minValue():
    assert hasattr(oracle::SequenceResourceData, "minValue")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_increment():
    assert hasattr(oracle::SequenceResourceData, "increment")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_tableName():
    assert hasattr(oracle::SequenceResourceData, "tableName")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_start():
    assert hasattr(oracle::SequenceResourceData, "start")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_cache():
    assert hasattr(oracle::SequenceResourceData, "cache")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "cache" in klass.__dict__:
            descriptor = klass.__dict__["cache"]
            break
    assert isinstance(descriptor, property)

def test_oracle::sequenceresourcedata_has_maxValue():
    assert hasattr(oracle::SequenceResourceData, "maxValue")
    descriptor = None
    for klass in oracle::SequenceResourceData.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)



def test_oracle::triggerresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle::TriggerResourceData)


def test_oracle::triggerresourcedata_constructor_exists():
    assert callable(oracle::TriggerResourceData.__init__)


def test_oracle::triggerresourcedata_constructor_args():
    sig = inspect.signature(oracle::TriggerResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_oracle::triggerresourcedata_has_sql():
    assert hasattr(oracle::TriggerResourceData, "sql")
    descriptor = None
    for klass in oracle::TriggerResourceData.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oraclespaceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleSpaceResourceData)


def test_oracle::oraclespaceresourcedata_constructor_exists():
    assert callable(oracle::OracleSpaceResourceData.__init__)


def test_oracle::oraclespaceresourcedata_constructor_args():
    sig = inspect.signature(oracle::OracleSpaceResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle::oraclemoduleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleModuleProperty)


def test_oracle::oraclemoduleproperty_constructor_exists():
    assert callable(oracle::OracleModuleProperty.__init__)


def test_oracle::oraclemoduleproperty_constructor_args():
    sig = inspect.signature(oracle::OracleModuleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle::oraclemoduleproperty_has_space():
    assert hasattr(oracle::OracleModuleProperty, "space")
    descriptor = None
    for klass in oracle::OracleModuleProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oracleviewproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleViewProperty)


def test_oracle::oracleviewproperty_constructor_exists():
    assert callable(oracle::OracleViewProperty.__init__)


def test_oracle::oracleviewproperty_constructor_args():
    sig = inspect.signature(oracle::OracleViewProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle::oracleviewproperty_has_space():
    assert hasattr(oracle::OracleViewProperty, "space")
    descriptor = None
    for klass in oracle::OracleViewProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oracleindexproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleIndexProperty)


def test_oracle::oracleindexproperty_constructor_exists():
    assert callable(oracle::OracleIndexProperty.__init__)


def test_oracle::oracleindexproperty_constructor_args():
    sig = inspect.signature(oracle::OracleIndexProperty.__init__)
    params = list(sig.parameters.keys())
    assert "reverse" in params, "Missing parameter 'reverse'"

def test_oracle::oracleindexproperty_has_reverse():
    assert hasattr(oracle::OracleIndexProperty, "reverse")
    descriptor = None
    for klass in oracle::OracleIndexProperty.__mro__:
        if "reverse" in klass.__dict__:
            descriptor = klass.__dict__["reverse"]
            break
    assert isinstance(descriptor, property)



def test_oracle::oracletableproperty_is_not_abstract():
    assert not inspect.isabstract(oracle::OracleTableProperty)


def test_oracle::oracletableproperty_constructor_exists():
    assert callable(oracle::OracleTableProperty.__init__)


def test_oracle::oracletableproperty_constructor_args():
    sig = inspect.signature(oracle::OracleTableProperty.__init__)
    params = list(sig.parameters.keys())
    assert "tabletype" in params, "Missing parameter 'tabletype'"
    assert "space" in params, "Missing parameter 'space'"

def test_oracle::oracletableproperty_has_tabletype():
    assert hasattr(oracle::OracleTableProperty, "tabletype")
    descriptor = None
    for klass in oracle::OracleTableProperty.__mro__:
        if "tabletype" in klass.__dict__:
            descriptor = klass.__dict__["tabletype"]
            break
    assert isinstance(descriptor, property)

def test_oracle::oracletableproperty_has_space():
    assert hasattr(oracle::OracleTableProperty, "space")
    descriptor = None
    for klass in oracle::OracleTableProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)

def test_table_type_exists():
    # Check that the Enumeration exists
    assert table_type is not None

def test_table_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in table_type]
    expected_literals = [
        "COMMON",
        "TEMP_WITH_VALUE",
        "TEMP_NO_VALUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in table_type"


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
oracle::OracleSequenceProperty_strategy = st.builds(
    oracle::OracleSequenceProperty,
    space=
        safe_text
)
ExtensibleModel_strategy = st.builds(
    ExtensibleModel,
)
oracle::DatabaseModuleExtensibleProperty_strategy = st.builds(
    oracle::DatabaseModuleExtensibleProperty,
    splitField=
        safe_text,
    space=
        safe_text,
    splitNum=
        safe_text,
    tableType=
        safe_text,
    bizPkg=
        safe_text,
    startDate=
        safe_text
)
oracle::OracleUser_strategy = st.builds(
    oracle::OracleUser,
    password=
        safe_text,
    defaultTableSpace=
        safe_text,
    enable=
        st.booleans(),
    decription=
        safe_text,
    attributes=
        safe_text,
    name=
        safe_text
)
oracle::OraclePrivilege_strategy = st.builds(
    oracle::OraclePrivilege,
    type=
        safe_text,
    decription=
        safe_text,
    name=
        safe_text
)
oracle::TableSpaceRelation_strategy = st.builds(
    oracle::TableSpaceRelation,
    mainSpace=
        safe_text,
    indexSpace=
        safe_text
)
oracle::TableSpace_strategy = st.builds(
    oracle::TableSpace,
    logicName=
        safe_text,
    chineseName=
        safe_text,
    user=
        safe_text,
    file=
        safe_text,
    name=
        safe_text,
    description=
        safe_text,
    size=
        safe_text
)
DatabaseResourceData_strategy = st.builds(
    DatabaseResourceData,
)
oracle::OracleUserResourceData_strategy = st.builds(
    oracle::OracleUserResourceData,
)
oracle::SequenceResourceData_strategy = st.builds(
    oracle::SequenceResourceData,
    cycle=
        st.booleans(),
    useCache=
        st.booleans(),
    isHistory=
        st.booleans(),
    minValue=
        safe_text,
    increment=
        safe_text,
    tableName=
        safe_text,
    start=
        safe_text,
    cache=
        safe_text,
    maxValue=
        safe_text
)
oracle::TriggerResourceData_strategy = st.builds(
    oracle::TriggerResourceData,
    sql=
        safe_text
)
oracle::OracleSpaceResourceData_strategy = st.builds(
    oracle::OracleSpaceResourceData,
)
oracle::OracleModuleProperty_strategy = st.builds(
    oracle::OracleModuleProperty,
    space=
        safe_text
)
oracle::OracleViewProperty_strategy = st.builds(
    oracle::OracleViewProperty,
    space=
        safe_text
)
oracle::OracleIndexProperty_strategy = st.builds(
    oracle::OracleIndexProperty,
    reverse=
        st.booleans()
)
oracle::OracleTableProperty_strategy = st.builds(
    oracle::OracleTableProperty,
    tabletype=
        safe_text,
    space=
        safe_text
)

@given(instance=oracle::OracleSequenceProperty_strategy)
@settings(max_examples=50)
def test_oracle::oraclesequenceproperty_instantiation(instance):
    assert isinstance(instance, oracle::OracleSequenceProperty)

@given(instance=oracle::OracleSequenceProperty_strategy)
def test_oracle::oraclesequenceproperty_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=oracle::OracleSequenceProperty_strategy)
def test_oracle::oraclesequenceproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=ExtensibleModel_strategy)
@settings(max_examples=50)
def test_extensiblemodel_instantiation(instance):
    assert isinstance(instance, ExtensibleModel)

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
@settings(max_examples=50)
def test_oracle::databasemoduleextensibleproperty_instantiation(instance):
    assert isinstance(instance, oracle::DatabaseModuleExtensibleProperty)

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_splitField_type(instance):
    assert isinstance(instance.splitField, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_splitField_setter(instance):
    original = instance.splitField
    instance.splitField = original
    assert instance.splitField == original

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_splitNum_type(instance):
    assert isinstance(instance.splitNum, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_splitNum_setter(instance):
    original = instance.splitNum
    instance.splitNum = original
    assert instance.splitNum == original

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_tableType_type(instance):
    assert isinstance(instance.tableType, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_tableType_setter(instance):
    original = instance.tableType
    instance.tableType = original
    assert instance.tableType == original

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_bizPkg_type(instance):
    assert isinstance(instance.bizPkg, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_bizPkg_setter(instance):
    original = instance.bizPkg
    instance.bizPkg = original
    assert instance.bizPkg == original

@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_startDate_type(instance):
    assert isinstance(instance.startDate, str)


@given(instance=oracle::DatabaseModuleExtensibleProperty_strategy)
def test_oracle::databasemoduleextensibleproperty_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=oracle::OracleUser_strategy)
@settings(max_examples=50)
def test_oracle::oracleuser_instantiation(instance):
    assert isinstance(instance, oracle::OracleUser)

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_defaultTableSpace_type(instance):
    assert isinstance(instance.defaultTableSpace, str)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_defaultTableSpace_setter(instance):
    original = instance.defaultTableSpace
    instance.defaultTableSpace = original
    assert instance.defaultTableSpace == original

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_enable_type(instance):
    assert isinstance(instance.enable, bool)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_decription_type(instance):
    assert isinstance(instance.decription, str)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_attributes_type(instance):
    assert isinstance(instance.attributes, str)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original

@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oracle::OracleUser_strategy)
def test_oracle::oracleuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oracle::OraclePrivilege_strategy)
@settings(max_examples=50)
def test_oracle::oracleprivilege_instantiation(instance):
    assert isinstance(instance, oracle::OraclePrivilege)

@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_decription_type(instance):
    assert isinstance(instance.decription, str)


@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original

@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oracle::OraclePrivilege_strategy)
def test_oracle::oracleprivilege_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oracle::TableSpaceRelation_strategy)
@settings(max_examples=50)
def test_oracle::tablespacerelation_instantiation(instance):
    assert isinstance(instance, oracle::TableSpaceRelation)

@given(instance=oracle::TableSpaceRelation_strategy)
def test_oracle::tablespacerelation_mainSpace_type(instance):
    assert isinstance(instance.mainSpace, str)


@given(instance=oracle::TableSpaceRelation_strategy)
def test_oracle::tablespacerelation_mainSpace_setter(instance):
    original = instance.mainSpace
    instance.mainSpace = original
    assert instance.mainSpace == original

@given(instance=oracle::TableSpaceRelation_strategy)
def test_oracle::tablespacerelation_indexSpace_type(instance):
    assert isinstance(instance.indexSpace, str)


@given(instance=oracle::TableSpaceRelation_strategy)
def test_oracle::tablespacerelation_indexSpace_setter(instance):
    original = instance.indexSpace
    instance.indexSpace = original
    assert instance.indexSpace == original

@given(instance=oracle::TableSpace_strategy)
@settings(max_examples=50)
def test_oracle::tablespace_instantiation(instance):
    assert isinstance(instance, oracle::TableSpace)

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_logicName_type(instance):
    assert isinstance(instance.logicName, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_logicName_setter(instance):
    original = instance.logicName
    instance.logicName = original
    assert instance.logicName == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_chineseName_type(instance):
    assert isinstance(instance.chineseName, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_chineseName_setter(instance):
    original = instance.chineseName
    instance.chineseName = original
    assert instance.chineseName == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=oracle::TableSpace_strategy)
def test_oracle::tablespace_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=DatabaseResourceData_strategy)
@settings(max_examples=50)
def test_databaseresourcedata_instantiation(instance):
    assert isinstance(instance, DatabaseResourceData)

@given(instance=oracle::OracleUserResourceData_strategy)
@settings(max_examples=50)
def test_oracle::oracleuserresourcedata_instantiation(instance):
    assert isinstance(instance, oracle::OracleUserResourceData)

@given(instance=oracle::SequenceResourceData_strategy)
@settings(max_examples=50)
def test_oracle::sequenceresourcedata_instantiation(instance):
    assert isinstance(instance, oracle::SequenceResourceData)

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_cycle_type(instance):
    assert isinstance(instance.cycle, bool)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_useCache_type(instance):
    assert isinstance(instance.useCache, bool)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_useCache_setter(instance):
    original = instance.useCache
    instance.useCache = original
    assert instance.useCache == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_isHistory_type(instance):
    assert isinstance(instance.isHistory, bool)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_minValue_type(instance):
    assert isinstance(instance.minValue, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_increment_type(instance):
    assert isinstance(instance.increment, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_tableName_type(instance):
    assert isinstance(instance.tableName, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_cache_type(instance):
    assert isinstance(instance.cache, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_cache_setter(instance):
    original = instance.cache
    instance.cache = original
    assert instance.cache == original

@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_maxValue_type(instance):
    assert isinstance(instance.maxValue, str)


@given(instance=oracle::SequenceResourceData_strategy)
def test_oracle::sequenceresourcedata_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original

@given(instance=oracle::TriggerResourceData_strategy)
@settings(max_examples=50)
def test_oracle::triggerresourcedata_instantiation(instance):
    assert isinstance(instance, oracle::TriggerResourceData)

@given(instance=oracle::TriggerResourceData_strategy)
def test_oracle::triggerresourcedata_sql_type(instance):
    assert isinstance(instance.sql, str)


@given(instance=oracle::TriggerResourceData_strategy)
def test_oracle::triggerresourcedata_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=oracle::OracleSpaceResourceData_strategy)
@settings(max_examples=50)
def test_oracle::oraclespaceresourcedata_instantiation(instance):
    assert isinstance(instance, oracle::OracleSpaceResourceData)

@given(instance=oracle::OracleModuleProperty_strategy)
@settings(max_examples=50)
def test_oracle::oraclemoduleproperty_instantiation(instance):
    assert isinstance(instance, oracle::OracleModuleProperty)

@given(instance=oracle::OracleModuleProperty_strategy)
def test_oracle::oraclemoduleproperty_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=oracle::OracleModuleProperty_strategy)
def test_oracle::oraclemoduleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle::OracleViewProperty_strategy)
@settings(max_examples=50)
def test_oracle::oracleviewproperty_instantiation(instance):
    assert isinstance(instance, oracle::OracleViewProperty)

@given(instance=oracle::OracleViewProperty_strategy)
def test_oracle::oracleviewproperty_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=oracle::OracleViewProperty_strategy)
def test_oracle::oracleviewproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle::OracleIndexProperty_strategy)
@settings(max_examples=50)
def test_oracle::oracleindexproperty_instantiation(instance):
    assert isinstance(instance, oracle::OracleIndexProperty)

@given(instance=oracle::OracleIndexProperty_strategy)
def test_oracle::oracleindexproperty_reverse_type(instance):
    assert isinstance(instance.reverse, bool)


@given(instance=oracle::OracleIndexProperty_strategy)
def test_oracle::oracleindexproperty_reverse_setter(instance):
    original = instance.reverse
    instance.reverse = original
    assert instance.reverse == original

@given(instance=oracle::OracleTableProperty_strategy)
@settings(max_examples=50)
def test_oracle::oracletableproperty_instantiation(instance):
    assert isinstance(instance, oracle::OracleTableProperty)

@given(instance=oracle::OracleTableProperty_strategy)
def test_oracle::oracletableproperty_tabletype_type(instance):
    assert isinstance(instance.tabletype, str)


@given(instance=oracle::OracleTableProperty_strategy)
def test_oracle::oracletableproperty_tabletype_setter(instance):
    original = instance.tabletype
    instance.tabletype = original
    assert instance.tabletype == original

@given(instance=oracle::OracleTableProperty_strategy)
def test_oracle::oracletableproperty_space_type(instance):
    assert isinstance(instance.space, str)


@given(instance=oracle::OracleTableProperty_strategy)
def test_oracle::oracletableproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original
