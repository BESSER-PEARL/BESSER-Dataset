import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    oracle_OracleSequenceProperty,
    ExtensibleModel,
    oracle_OracleUser,
    oracle_OraclePrivilege,
    oracle_DatabaseModuleExtensibleProperty,
    oracle_TableSpaceRelation,
    oracle_TableSpace,
    DatabaseResourceData,
    oracle_SequenceResourceData,
    oracle_OracleUserResourceData,
    oracle_TriggerResourceData,
    oracle_OracleSpaceResourceData,
    oracle_OracleModuleProperty,
    oracle_OracleViewProperty,
    oracle_OracleIndexProperty,
    oracle_OracleTableProperty,
    table_type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_oracle_oraclesequenceproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleSequenceProperty)


def test_oracle_oraclesequenceproperty_constructor_exists():
    assert callable(oracle_OracleSequenceProperty.__init__)


def test_oracle_oraclesequenceproperty_constructor_args():
    sig = inspect.signature(oracle_OracleSequenceProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle_oraclesequenceproperty_has_space():
    assert hasattr(oracle_OracleSequenceProperty, "space")
    descriptor = None
    for klass in oracle_OracleSequenceProperty.__mro__:
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



def test_oracle_oracleuser_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleUser)


def test_oracle_oracleuser_constructor_exists():
    assert callable(oracle_OracleUser.__init__)


def test_oracle_oracleuser_constructor_args():
    sig = inspect.signature(oracle_OracleUser.__init__)
    params = list(sig.parameters.keys())
    assert "defaultTableSpace" in params, "Missing parameter 'defaultTableSpace'"
    assert "enable" in params, "Missing parameter 'enable'"
    assert "name" in params, "Missing parameter 'name'"
    assert "attributes" in params, "Missing parameter 'attributes'"
    assert "password" in params, "Missing parameter 'password'"
    assert "decription" in params, "Missing parameter 'decription'"

def test_oracle_oracleuser_has_defaultTableSpace():
    assert hasattr(oracle_OracleUser, "defaultTableSpace")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "defaultTableSpace" in klass.__dict__:
            descriptor = klass.__dict__["defaultTableSpace"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleuser_has_enable():
    assert hasattr(oracle_OracleUser, "enable")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "enable" in klass.__dict__:
            descriptor = klass.__dict__["enable"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleuser_has_name():
    assert hasattr(oracle_OracleUser, "name")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleuser_has_attributes():
    assert hasattr(oracle_OracleUser, "attributes")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "attributes" in klass.__dict__:
            descriptor = klass.__dict__["attributes"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleuser_has_password():
    assert hasattr(oracle_OracleUser, "password")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleuser_has_decription():
    assert hasattr(oracle_OracleUser, "decription")
    descriptor = None
    for klass in oracle_OracleUser.__mro__:
        if "decription" in klass.__dict__:
            descriptor = klass.__dict__["decription"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oracleprivilege_is_not_abstract():
    assert not inspect.isabstract(oracle_OraclePrivilege)


def test_oracle_oracleprivilege_constructor_exists():
    assert callable(oracle_OraclePrivilege.__init__)


def test_oracle_oracleprivilege_constructor_args():
    sig = inspect.signature(oracle_OraclePrivilege.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "decription" in params, "Missing parameter 'decription'"

def test_oracle_oracleprivilege_has_name():
    assert hasattr(oracle_OraclePrivilege, "name")
    descriptor = None
    for klass in oracle_OraclePrivilege.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleprivilege_has_type():
    assert hasattr(oracle_OraclePrivilege, "type")
    descriptor = None
    for klass in oracle_OraclePrivilege.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracleprivilege_has_decription():
    assert hasattr(oracle_OraclePrivilege, "decription")
    descriptor = None
    for klass in oracle_OraclePrivilege.__mro__:
        if "decription" in klass.__dict__:
            descriptor = klass.__dict__["decription"]
            break
    assert isinstance(descriptor, property)



def test_oracle_databasemoduleextensibleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_DatabaseModuleExtensibleProperty)


def test_oracle_databasemoduleextensibleproperty_constructor_exists():
    assert callable(oracle_DatabaseModuleExtensibleProperty.__init__)


def test_oracle_databasemoduleextensibleproperty_constructor_args():
    sig = inspect.signature(oracle_DatabaseModuleExtensibleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "splitNum" in params, "Missing parameter 'splitNum'"
    assert "tableType" in params, "Missing parameter 'tableType'"
    assert "bizPkg" in params, "Missing parameter 'bizPkg'"
    assert "splitField" in params, "Missing parameter 'splitField'"
    assert "space" in params, "Missing parameter 'space'"

def test_oracle_databasemoduleextensibleproperty_has_startDate():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "startDate")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_oracle_databasemoduleextensibleproperty_has_splitNum():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "splitNum")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "splitNum" in klass.__dict__:
            descriptor = klass.__dict__["splitNum"]
            break
    assert isinstance(descriptor, property)

def test_oracle_databasemoduleextensibleproperty_has_tableType():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "tableType")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "tableType" in klass.__dict__:
            descriptor = klass.__dict__["tableType"]
            break
    assert isinstance(descriptor, property)

def test_oracle_databasemoduleextensibleproperty_has_bizPkg():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "bizPkg")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "bizPkg" in klass.__dict__:
            descriptor = klass.__dict__["bizPkg"]
            break
    assert isinstance(descriptor, property)

def test_oracle_databasemoduleextensibleproperty_has_splitField():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "splitField")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "splitField" in klass.__dict__:
            descriptor = klass.__dict__["splitField"]
            break
    assert isinstance(descriptor, property)

def test_oracle_databasemoduleextensibleproperty_has_space():
    assert hasattr(oracle_DatabaseModuleExtensibleProperty, "space")
    descriptor = None
    for klass in oracle_DatabaseModuleExtensibleProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_oracle_tablespacerelation_is_not_abstract():
    assert not inspect.isabstract(oracle_TableSpaceRelation)


def test_oracle_tablespacerelation_constructor_exists():
    assert callable(oracle_TableSpaceRelation.__init__)


def test_oracle_tablespacerelation_constructor_args():
    sig = inspect.signature(oracle_TableSpaceRelation.__init__)
    params = list(sig.parameters.keys())
    assert "mainSpace" in params, "Missing parameter 'mainSpace'"
    assert "indexSpace" in params, "Missing parameter 'indexSpace'"

def test_oracle_tablespacerelation_has_mainSpace():
    assert hasattr(oracle_TableSpaceRelation, "mainSpace")
    descriptor = None
    for klass in oracle_TableSpaceRelation.__mro__:
        if "mainSpace" in klass.__dict__:
            descriptor = klass.__dict__["mainSpace"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespacerelation_has_indexSpace():
    assert hasattr(oracle_TableSpaceRelation, "indexSpace")
    descriptor = None
    for klass in oracle_TableSpaceRelation.__mro__:
        if "indexSpace" in klass.__dict__:
            descriptor = klass.__dict__["indexSpace"]
            break
    assert isinstance(descriptor, property)



def test_oracle_tablespace_is_not_abstract():
    assert not inspect.isabstract(oracle_TableSpace)


def test_oracle_tablespace_constructor_exists():
    assert callable(oracle_TableSpace.__init__)


def test_oracle_tablespace_constructor_args():
    sig = inspect.signature(oracle_TableSpace.__init__)
    params = list(sig.parameters.keys())
    assert "logicName" in params, "Missing parameter 'logicName'"
    assert "size" in params, "Missing parameter 'size'"
    assert "file" in params, "Missing parameter 'file'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "user" in params, "Missing parameter 'user'"
    assert "chineseName" in params, "Missing parameter 'chineseName'"

def test_oracle_tablespace_has_logicName():
    assert hasattr(oracle_TableSpace, "logicName")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "logicName" in klass.__dict__:
            descriptor = klass.__dict__["logicName"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_size():
    assert hasattr(oracle_TableSpace, "size")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_file():
    assert hasattr(oracle_TableSpace, "file")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_description():
    assert hasattr(oracle_TableSpace, "description")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_name():
    assert hasattr(oracle_TableSpace, "name")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_user():
    assert hasattr(oracle_TableSpace, "user")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_oracle_tablespace_has_chineseName():
    assert hasattr(oracle_TableSpace, "chineseName")
    descriptor = None
    for klass in oracle_TableSpace.__mro__:
        if "chineseName" in klass.__dict__:
            descriptor = klass.__dict__["chineseName"]
            break
    assert isinstance(descriptor, property)



def test_databaseresourcedata_is_not_abstract():
    assert not inspect.isabstract(DatabaseResourceData)


def test_databaseresourcedata_constructor_exists():
    assert callable(DatabaseResourceData.__init__)


def test_databaseresourcedata_constructor_args():
    sig = inspect.signature(DatabaseResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle_sequenceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_SequenceResourceData)


def test_oracle_sequenceresourcedata_constructor_exists():
    assert callable(oracle_SequenceResourceData.__init__)


def test_oracle_sequenceresourcedata_constructor_args():
    sig = inspect.signature(oracle_SequenceResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "useCache" in params, "Missing parameter 'useCache'"
    assert "increment" in params, "Missing parameter 'increment'"
    assert "tableName" in params, "Missing parameter 'tableName'"
    assert "maxValue" in params, "Missing parameter 'maxValue'"
    assert "minValue" in params, "Missing parameter 'minValue'"
    assert "cycle" in params, "Missing parameter 'cycle'"
    assert "start" in params, "Missing parameter 'start'"
    assert "isHistory" in params, "Missing parameter 'isHistory'"
    assert "cache" in params, "Missing parameter 'cache'"

def test_oracle_sequenceresourcedata_has_useCache():
    assert hasattr(oracle_SequenceResourceData, "useCache")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "useCache" in klass.__dict__:
            descriptor = klass.__dict__["useCache"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_increment():
    assert hasattr(oracle_SequenceResourceData, "increment")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "increment" in klass.__dict__:
            descriptor = klass.__dict__["increment"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_tableName():
    assert hasattr(oracle_SequenceResourceData, "tableName")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "tableName" in klass.__dict__:
            descriptor = klass.__dict__["tableName"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_maxValue():
    assert hasattr(oracle_SequenceResourceData, "maxValue")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "maxValue" in klass.__dict__:
            descriptor = klass.__dict__["maxValue"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_minValue():
    assert hasattr(oracle_SequenceResourceData, "minValue")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "minValue" in klass.__dict__:
            descriptor = klass.__dict__["minValue"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_cycle():
    assert hasattr(oracle_SequenceResourceData, "cycle")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "cycle" in klass.__dict__:
            descriptor = klass.__dict__["cycle"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_start():
    assert hasattr(oracle_SequenceResourceData, "start")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_isHistory():
    assert hasattr(oracle_SequenceResourceData, "isHistory")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "isHistory" in klass.__dict__:
            descriptor = klass.__dict__["isHistory"]
            break
    assert isinstance(descriptor, property)

def test_oracle_sequenceresourcedata_has_cache():
    assert hasattr(oracle_SequenceResourceData, "cache")
    descriptor = None
    for klass in oracle_SequenceResourceData.__mro__:
        if "cache" in klass.__dict__:
            descriptor = klass.__dict__["cache"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oracleuserresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleUserResourceData)


def test_oracle_oracleuserresourcedata_constructor_exists():
    assert callable(oracle_OracleUserResourceData.__init__)


def test_oracle_oracleuserresourcedata_constructor_args():
    sig = inspect.signature(oracle_OracleUserResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle_triggerresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_TriggerResourceData)


def test_oracle_triggerresourcedata_constructor_exists():
    assert callable(oracle_TriggerResourceData.__init__)


def test_oracle_triggerresourcedata_constructor_args():
    sig = inspect.signature(oracle_TriggerResourceData.__init__)
    params = list(sig.parameters.keys())
    assert "sql" in params, "Missing parameter 'sql'"

def test_oracle_triggerresourcedata_has_sql():
    assert hasattr(oracle_TriggerResourceData, "sql")
    descriptor = None
    for klass in oracle_TriggerResourceData.__mro__:
        if "sql" in klass.__dict__:
            descriptor = klass.__dict__["sql"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oraclespaceresourcedata_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleSpaceResourceData)


def test_oracle_oraclespaceresourcedata_constructor_exists():
    assert callable(oracle_OracleSpaceResourceData.__init__)


def test_oracle_oraclespaceresourcedata_constructor_args():
    sig = inspect.signature(oracle_OracleSpaceResourceData.__init__)
    params = list(sig.parameters.keys())



def test_oracle_oraclemoduleproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleModuleProperty)


def test_oracle_oraclemoduleproperty_constructor_exists():
    assert callable(oracle_OracleModuleProperty.__init__)


def test_oracle_oraclemoduleproperty_constructor_args():
    sig = inspect.signature(oracle_OracleModuleProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle_oraclemoduleproperty_has_space():
    assert hasattr(oracle_OracleModuleProperty, "space")
    descriptor = None
    for klass in oracle_OracleModuleProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oracleviewproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleViewProperty)


def test_oracle_oracleviewproperty_constructor_exists():
    assert callable(oracle_OracleViewProperty.__init__)


def test_oracle_oracleviewproperty_constructor_args():
    sig = inspect.signature(oracle_OracleViewProperty.__init__)
    params = list(sig.parameters.keys())
    assert "space" in params, "Missing parameter 'space'"

def test_oracle_oracleviewproperty_has_space():
    assert hasattr(oracle_OracleViewProperty, "space")
    descriptor = None
    for klass in oracle_OracleViewProperty.__mro__:
        if "space" in klass.__dict__:
            descriptor = klass.__dict__["space"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oracleindexproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleIndexProperty)


def test_oracle_oracleindexproperty_constructor_exists():
    assert callable(oracle_OracleIndexProperty.__init__)


def test_oracle_oracleindexproperty_constructor_args():
    sig = inspect.signature(oracle_OracleIndexProperty.__init__)
    params = list(sig.parameters.keys())
    assert "reverse" in params, "Missing parameter 'reverse'"

def test_oracle_oracleindexproperty_has_reverse():
    assert hasattr(oracle_OracleIndexProperty, "reverse")
    descriptor = None
    for klass in oracle_OracleIndexProperty.__mro__:
        if "reverse" in klass.__dict__:
            descriptor = klass.__dict__["reverse"]
            break
    assert isinstance(descriptor, property)



def test_oracle_oracletableproperty_is_not_abstract():
    assert not inspect.isabstract(oracle_OracleTableProperty)


def test_oracle_oracletableproperty_constructor_exists():
    assert callable(oracle_OracleTableProperty.__init__)


def test_oracle_oracletableproperty_constructor_args():
    sig = inspect.signature(oracle_OracleTableProperty.__init__)
    params = list(sig.parameters.keys())
    assert "tabletype" in params, "Missing parameter 'tabletype'"
    assert "space" in params, "Missing parameter 'space'"

def test_oracle_oracletableproperty_has_tabletype():
    assert hasattr(oracle_OracleTableProperty, "tabletype")
    descriptor = None
    for klass in oracle_OracleTableProperty.__mro__:
        if "tabletype" in klass.__dict__:
            descriptor = klass.__dict__["tabletype"]
            break
    assert isinstance(descriptor, property)

def test_oracle_oracletableproperty_has_space():
    assert hasattr(oracle_OracleTableProperty, "space")
    descriptor = None
    for klass in oracle_OracleTableProperty.__mro__:
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
        "TEMP_NO_VALUE",
        "COMMON",
        "TEMP_WITH_VALUE",
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
oracle_OracleSequenceProperty_strategy = st.builds(
    oracle_OracleSequenceProperty,
    space=
        safe_text
)
ExtensibleModel_strategy = st.builds(
    ExtensibleModel,
)
oracle_OracleUser_strategy = st.builds(
    oracle_OracleUser,
    defaultTableSpace=
        safe_text,
    enable=
        st.booleans(),
    name=
        safe_text,
    attributes=
        safe_text,
    password=
        safe_text,
    decription=
        safe_text
)
oracle_OraclePrivilege_strategy = st.builds(
    oracle_OraclePrivilege,
    name=
        safe_text,
    type=
        safe_text,
    decription=
        safe_text
)
oracle_DatabaseModuleExtensibleProperty_strategy = st.builds(
    oracle_DatabaseModuleExtensibleProperty,
    startDate=
        safe_text,
    splitNum=
        safe_text,
    tableType=
        safe_text,
    bizPkg=
        safe_text,
    splitField=
        safe_text,
    space=
        safe_text
)
oracle_TableSpaceRelation_strategy = st.builds(
    oracle_TableSpaceRelation,
    mainSpace=
        safe_text,
    indexSpace=
        safe_text
)
oracle_TableSpace_strategy = st.builds(
    oracle_TableSpace,
    logicName=
        safe_text,
    size=
        safe_text,
    file=
        safe_text,
    description=
        safe_text,
    name=
        safe_text,
    user=
        safe_text,
    chineseName=
        safe_text
)
DatabaseResourceData_strategy = st.builds(
    DatabaseResourceData,
)
oracle_SequenceResourceData_strategy = st.builds(
    oracle_SequenceResourceData,
    useCache=
        st.booleans(),
    increment=
        safe_text,
    tableName=
        safe_text,
    maxValue=
        safe_text,
    minValue=
        safe_text,
    cycle=
        st.booleans(),
    start=
        safe_text,
    isHistory=
        st.booleans(),
    cache=
        safe_text
)
oracle_OracleUserResourceData_strategy = st.builds(
    oracle_OracleUserResourceData,
)
oracle_TriggerResourceData_strategy = st.builds(
    oracle_TriggerResourceData,
    sql=
        safe_text
)
oracle_OracleSpaceResourceData_strategy = st.builds(
    oracle_OracleSpaceResourceData,
)
oracle_OracleModuleProperty_strategy = st.builds(
    oracle_OracleModuleProperty,
    space=
        safe_text
)
oracle_OracleViewProperty_strategy = st.builds(
    oracle_OracleViewProperty,
    space=
        safe_text
)
oracle_OracleIndexProperty_strategy = st.builds(
    oracle_OracleIndexProperty,
    reverse=
        st.booleans()
)
oracle_OracleTableProperty_strategy = st.builds(
    oracle_OracleTableProperty,
    tabletype=
        safe_text,
    space=
        safe_text
)

@given(instance=oracle_OracleSequenceProperty_strategy)
@settings(max_examples=50)
def test_oracle_oraclesequenceproperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleSequenceProperty)



@given(instance=oracle_OracleSequenceProperty_strategy)
def test_oracle_oraclesequenceproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=ExtensibleModel_strategy)
@settings(max_examples=50)
def test_extensiblemodel_instantiation(instance):
    assert isinstance(instance, ExtensibleModel)

@given(instance=oracle_OracleUser_strategy)
@settings(max_examples=50)
def test_oracle_oracleuser_instantiation(instance):
    assert isinstance(instance, oracle_OracleUser)



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_defaultTableSpace_setter(instance):
    original = instance.defaultTableSpace
    instance.defaultTableSpace = original
    assert instance.defaultTableSpace == original



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_enable_setter(instance):
    original = instance.enable
    instance.enable = original
    assert instance.enable == original



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_attributes_setter(instance):
    original = instance.attributes
    instance.attributes = original
    assert instance.attributes == original



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=oracle_OracleUser_strategy)
def test_oracle_oracleuser_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original

@given(instance=oracle_OraclePrivilege_strategy)
@settings(max_examples=50)
def test_oracle_oracleprivilege_instantiation(instance):
    assert isinstance(instance, oracle_OraclePrivilege)



@given(instance=oracle_OraclePrivilege_strategy)
def test_oracle_oracleprivilege_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_OraclePrivilege_strategy)
def test_oracle_oracleprivilege_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=oracle_OraclePrivilege_strategy)
def test_oracle_oracleprivilege_decription_setter(instance):
    original = instance.decription
    instance.decription = original
    assert instance.decription == original

@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
@settings(max_examples=50)
def test_oracle_databasemoduleextensibleproperty_instantiation(instance):
    assert isinstance(instance, oracle_DatabaseModuleExtensibleProperty)



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_splitNum_setter(instance):
    original = instance.splitNum
    instance.splitNum = original
    assert instance.splitNum == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_tableType_setter(instance):
    original = instance.tableType
    instance.tableType = original
    assert instance.tableType == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_bizPkg_setter(instance):
    original = instance.bizPkg
    instance.bizPkg = original
    assert instance.bizPkg == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_splitField_setter(instance):
    original = instance.splitField
    instance.splitField = original
    assert instance.splitField == original



@given(instance=oracle_DatabaseModuleExtensibleProperty_strategy)
def test_oracle_databasemoduleextensibleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle_TableSpaceRelation_strategy)
@settings(max_examples=50)
def test_oracle_tablespacerelation_instantiation(instance):
    assert isinstance(instance, oracle_TableSpaceRelation)



@given(instance=oracle_TableSpaceRelation_strategy)
def test_oracle_tablespacerelation_mainSpace_setter(instance):
    original = instance.mainSpace
    instance.mainSpace = original
    assert instance.mainSpace == original



@given(instance=oracle_TableSpaceRelation_strategy)
def test_oracle_tablespacerelation_indexSpace_setter(instance):
    original = instance.indexSpace
    instance.indexSpace = original
    assert instance.indexSpace == original

@given(instance=oracle_TableSpace_strategy)
@settings(max_examples=50)
def test_oracle_tablespace_instantiation(instance):
    assert isinstance(instance, oracle_TableSpace)



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_logicName_setter(instance):
    original = instance.logicName
    instance.logicName = original
    assert instance.logicName == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=oracle_TableSpace_strategy)
def test_oracle_tablespace_chineseName_setter(instance):
    original = instance.chineseName
    instance.chineseName = original
    assert instance.chineseName == original

@given(instance=DatabaseResourceData_strategy)
@settings(max_examples=50)
def test_databaseresourcedata_instantiation(instance):
    assert isinstance(instance, DatabaseResourceData)

@given(instance=oracle_SequenceResourceData_strategy)
@settings(max_examples=50)
def test_oracle_sequenceresourcedata_instantiation(instance):
    assert isinstance(instance, oracle_SequenceResourceData)



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_useCache_setter(instance):
    original = instance.useCache
    instance.useCache = original
    assert instance.useCache == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_increment_setter(instance):
    original = instance.increment
    instance.increment = original
    assert instance.increment == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_tableName_setter(instance):
    original = instance.tableName
    instance.tableName = original
    assert instance.tableName == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_maxValue_setter(instance):
    original = instance.maxValue
    instance.maxValue = original
    assert instance.maxValue == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_minValue_setter(instance):
    original = instance.minValue
    instance.minValue = original
    assert instance.minValue == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_cycle_setter(instance):
    original = instance.cycle
    instance.cycle = original
    assert instance.cycle == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_isHistory_setter(instance):
    original = instance.isHistory
    instance.isHistory = original
    assert instance.isHistory == original



@given(instance=oracle_SequenceResourceData_strategy)
def test_oracle_sequenceresourcedata_cache_setter(instance):
    original = instance.cache
    instance.cache = original
    assert instance.cache == original

@given(instance=oracle_OracleUserResourceData_strategy)
@settings(max_examples=50)
def test_oracle_oracleuserresourcedata_instantiation(instance):
    assert isinstance(instance, oracle_OracleUserResourceData)

@given(instance=oracle_TriggerResourceData_strategy)
@settings(max_examples=50)
def test_oracle_triggerresourcedata_instantiation(instance):
    assert isinstance(instance, oracle_TriggerResourceData)



@given(instance=oracle_TriggerResourceData_strategy)
def test_oracle_triggerresourcedata_sql_setter(instance):
    original = instance.sql
    instance.sql = original
    assert instance.sql == original

@given(instance=oracle_OracleSpaceResourceData_strategy)
@settings(max_examples=50)
def test_oracle_oraclespaceresourcedata_instantiation(instance):
    assert isinstance(instance, oracle_OracleSpaceResourceData)

@given(instance=oracle_OracleModuleProperty_strategy)
@settings(max_examples=50)
def test_oracle_oraclemoduleproperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleModuleProperty)



@given(instance=oracle_OracleModuleProperty_strategy)
def test_oracle_oraclemoduleproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle_OracleViewProperty_strategy)
@settings(max_examples=50)
def test_oracle_oracleviewproperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleViewProperty)



@given(instance=oracle_OracleViewProperty_strategy)
def test_oracle_oracleviewproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original

@given(instance=oracle_OracleIndexProperty_strategy)
@settings(max_examples=50)
def test_oracle_oracleindexproperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleIndexProperty)



@given(instance=oracle_OracleIndexProperty_strategy)
def test_oracle_oracleindexproperty_reverse_setter(instance):
    original = instance.reverse
    instance.reverse = original
    assert instance.reverse == original

@given(instance=oracle_OracleTableProperty_strategy)
@settings(max_examples=50)
def test_oracle_oracletableproperty_instantiation(instance):
    assert isinstance(instance, oracle_OracleTableProperty)



@given(instance=oracle_OracleTableProperty_strategy)
def test_oracle_oracletableproperty_tabletype_setter(instance):
    original = instance.tabletype
    instance.tabletype = original
    assert instance.tabletype == original



@given(instance=oracle_OracleTableProperty_strategy)
def test_oracle_oracletableproperty_space_setter(instance):
    original = instance.space
    instance.space = original
    assert instance.space == original
