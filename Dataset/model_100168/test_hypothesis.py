import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ModelElement,
    rdbms_Table,
    rdbms_Column,
    rdbms_Database,
    rdbms_Constraints,
    rdbms_ModelElement,
    DataType,
    rdbms_UserDefinedDataType,
    rdbms_SystemDataType,
    PKeyAndUnique,
    rdbms_UniqueCon,
    rdbms_PrimaryKeyCon,
    Constraints,
    rdbms_ForeignKey,
    rdbms_CheckCon,
    rdbms_DataType,
    rdbms_PKeyAndUnique,
    ReferencingType,
    DeferredAct,
    Action,
    DeferrableAct,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_modelelement_is_not_abstract():
    assert not inspect.isabstract(ModelElement)


def test_modelelement_constructor_exists():
    assert callable(ModelElement.__init__)


def test_modelelement_constructor_args():
    sig = inspect.signature(ModelElement.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_table_is_not_abstract():
    assert not inspect.isabstract(rdbms_Table)


def test_rdbms_table_constructor_exists():
    assert callable(rdbms_Table.__init__)


def test_rdbms_table_constructor_args():
    sig = inspect.signature(rdbms_Table.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_column_is_not_abstract():
    assert not inspect.isabstract(rdbms_Column)


def test_rdbms_column_constructor_exists():
    assert callable(rdbms_Column.__init__)


def test_rdbms_column_constructor_args():
    sig = inspect.signature(rdbms_Column.__init__)
    params = list(sig.parameters.keys())
    assert "length" in params, "Missing parameter 'length'"
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "default" in params, "Missing parameter 'default'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_rdbms_column_has_length():
    assert hasattr(rdbms_Column, "length")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_nullable():
    assert hasattr(rdbms_Column, "nullable")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_default():
    assert hasattr(rdbms_Column, "default")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_column_has_precision():
    assert hasattr(rdbms_Column, "precision")
    descriptor = None
    for klass in rdbms_Column.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_database_is_not_abstract():
    assert not inspect.isabstract(rdbms_Database)


def test_rdbms_database_constructor_exists():
    assert callable(rdbms_Database.__init__)


def test_rdbms_database_constructor_args():
    sig = inspect.signature(rdbms_Database.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_constraints_is_not_abstract():
    assert not inspect.isabstract(rdbms_Constraints)


def test_rdbms_constraints_constructor_exists():
    assert callable(rdbms_Constraints.__init__)


def test_rdbms_constraints_constructor_args():
    sig = inspect.signature(rdbms_Constraints.__init__)
    params = list(sig.parameters.keys())
    assert "deferred" in params, "Missing parameter 'deferred'"
    assert "deferrable" in params, "Missing parameter 'deferrable'"

def test_rdbms_constraints_has_deferred():
    assert hasattr(rdbms_Constraints, "deferred")
    descriptor = None
    for klass in rdbms_Constraints.__mro__:
        if "deferred" in klass.__dict__:
            descriptor = klass.__dict__["deferred"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_constraints_has_deferrable():
    assert hasattr(rdbms_Constraints, "deferrable")
    descriptor = None
    for klass in rdbms_Constraints.__mro__:
        if "deferrable" in klass.__dict__:
            descriptor = klass.__dict__["deferrable"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_modelelement_is_not_abstract():
    assert not inspect.isabstract(rdbms_ModelElement)


def test_rdbms_modelelement_constructor_exists():
    assert callable(rdbms_ModelElement.__init__)


def test_rdbms_modelelement_constructor_args():
    sig = inspect.signature(rdbms_ModelElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rdbms_modelelement_has_name():
    assert hasattr(rdbms_ModelElement, "name")
    descriptor = None
    for klass in rdbms_ModelElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_userdefineddatatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_UserDefinedDataType)


def test_rdbms_userdefineddatatype_constructor_exists():
    assert callable(rdbms_UserDefinedDataType.__init__)


def test_rdbms_userdefineddatatype_constructor_args():
    sig = inspect.signature(rdbms_UserDefinedDataType.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "length" in params, "Missing parameter 'length'"
    assert "defaultValue" in params, "Missing parameter 'defaultValue'"

def test_rdbms_userdefineddatatype_has_precision():
    assert hasattr(rdbms_UserDefinedDataType, "precision")
    descriptor = None
    for klass in rdbms_UserDefinedDataType.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_userdefineddatatype_has_length():
    assert hasattr(rdbms_UserDefinedDataType, "length")
    descriptor = None
    for klass in rdbms_UserDefinedDataType.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_userdefineddatatype_has_defaultValue():
    assert hasattr(rdbms_UserDefinedDataType, "defaultValue")
    descriptor = None
    for klass in rdbms_UserDefinedDataType.__mro__:
        if "defaultValue" in klass.__dict__:
            descriptor = klass.__dict__["defaultValue"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_systemdatatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_SystemDataType)


def test_rdbms_systemdatatype_constructor_exists():
    assert callable(rdbms_SystemDataType.__init__)


def test_rdbms_systemdatatype_constructor_args():
    sig = inspect.signature(rdbms_SystemDataType.__init__)
    params = list(sig.parameters.keys())
    assert "predefinedDecPlaces" in params, "Missing parameter 'predefinedDecPlaces'"
    assert "predefinedLength" in params, "Missing parameter 'predefinedLength'"

def test_rdbms_systemdatatype_has_predefinedDecPlaces():
    assert hasattr(rdbms_SystemDataType, "predefinedDecPlaces")
    descriptor = None
    for klass in rdbms_SystemDataType.__mro__:
        if "predefinedDecPlaces" in klass.__dict__:
            descriptor = klass.__dict__["predefinedDecPlaces"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_systemdatatype_has_predefinedLength():
    assert hasattr(rdbms_SystemDataType, "predefinedLength")
    descriptor = None
    for klass in rdbms_SystemDataType.__mro__:
        if "predefinedLength" in klass.__dict__:
            descriptor = klass.__dict__["predefinedLength"]
            break
    assert isinstance(descriptor, property)



def test_pkeyandunique_is_not_abstract():
    assert not inspect.isabstract(PKeyAndUnique)


def test_pkeyandunique_constructor_exists():
    assert callable(PKeyAndUnique.__init__)


def test_pkeyandunique_constructor_args():
    sig = inspect.signature(PKeyAndUnique.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_uniquecon_is_not_abstract():
    assert not inspect.isabstract(rdbms_UniqueCon)


def test_rdbms_uniquecon_constructor_exists():
    assert callable(rdbms_UniqueCon.__init__)


def test_rdbms_uniquecon_constructor_args():
    sig = inspect.signature(rdbms_UniqueCon.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_primarykeycon_is_not_abstract():
    assert not inspect.isabstract(rdbms_PrimaryKeyCon)


def test_rdbms_primarykeycon_constructor_exists():
    assert callable(rdbms_PrimaryKeyCon.__init__)


def test_rdbms_primarykeycon_constructor_args():
    sig = inspect.signature(rdbms_PrimaryKeyCon.__init__)
    params = list(sig.parameters.keys())



def test_constraints_is_not_abstract():
    assert not inspect.isabstract(Constraints)


def test_constraints_constructor_exists():
    assert callable(Constraints.__init__)


def test_constraints_constructor_args():
    sig = inspect.signature(Constraints.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_foreignkey_is_not_abstract():
    assert not inspect.isabstract(rdbms_ForeignKey)


def test_rdbms_foreignkey_constructor_exists():
    assert callable(rdbms_ForeignKey.__init__)


def test_rdbms_foreignkey_constructor_args():
    sig = inspect.signature(rdbms_ForeignKey.__init__)
    params = list(sig.parameters.keys())
    assert "updateActionRHS" in params, "Missing parameter 'updateActionRHS'"
    assert "deleteActionRHS" in params, "Missing parameter 'deleteActionRHS'"
    assert "match" in params, "Missing parameter 'match'"
    assert "inverseReferentialIntegrityCon" in params, "Missing parameter 'inverseReferentialIntegrityCon'"

def test_rdbms_foreignkey_has_updateActionRHS():
    assert hasattr(rdbms_ForeignKey, "updateActionRHS")
    descriptor = None
    for klass in rdbms_ForeignKey.__mro__:
        if "updateActionRHS" in klass.__dict__:
            descriptor = klass.__dict__["updateActionRHS"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_deleteActionRHS():
    assert hasattr(rdbms_ForeignKey, "deleteActionRHS")
    descriptor = None
    for klass in rdbms_ForeignKey.__mro__:
        if "deleteActionRHS" in klass.__dict__:
            descriptor = klass.__dict__["deleteActionRHS"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_match():
    assert hasattr(rdbms_ForeignKey, "match")
    descriptor = None
    for klass in rdbms_ForeignKey.__mro__:
        if "match" in klass.__dict__:
            descriptor = klass.__dict__["match"]
            break
    assert isinstance(descriptor, property)

def test_rdbms_foreignkey_has_inverseReferentialIntegrityCon():
    assert hasattr(rdbms_ForeignKey, "inverseReferentialIntegrityCon")
    descriptor = None
    for klass in rdbms_ForeignKey.__mro__:
        if "inverseReferentialIntegrityCon" in klass.__dict__:
            descriptor = klass.__dict__["inverseReferentialIntegrityCon"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_checkcon_is_not_abstract():
    assert not inspect.isabstract(rdbms_CheckCon)


def test_rdbms_checkcon_constructor_exists():
    assert callable(rdbms_CheckCon.__init__)


def test_rdbms_checkcon_constructor_args():
    sig = inspect.signature(rdbms_CheckCon.__init__)
    params = list(sig.parameters.keys())
    assert "checkCondition" in params, "Missing parameter 'checkCondition'"

def test_rdbms_checkcon_has_checkCondition():
    assert hasattr(rdbms_CheckCon, "checkCondition")
    descriptor = None
    for klass in rdbms_CheckCon.__mro__:
        if "checkCondition" in klass.__dict__:
            descriptor = klass.__dict__["checkCondition"]
            break
    assert isinstance(descriptor, property)



def test_rdbms_datatype_is_not_abstract():
    assert not inspect.isabstract(rdbms_DataType)


def test_rdbms_datatype_constructor_exists():
    assert callable(rdbms_DataType.__init__)


def test_rdbms_datatype_constructor_args():
    sig = inspect.signature(rdbms_DataType.__init__)
    params = list(sig.parameters.keys())



def test_rdbms_pkeyandunique_is_not_abstract():
    assert not inspect.isabstract(rdbms_PKeyAndUnique)


def test_rdbms_pkeyandunique_constructor_exists():
    assert callable(rdbms_PKeyAndUnique.__init__)


def test_rdbms_pkeyandunique_constructor_args():
    sig = inspect.signature(rdbms_PKeyAndUnique.__init__)
    params = list(sig.parameters.keys())

def test_referencingtype_exists():
    # Check that the Enumeration exists
    assert ReferencingType is not None

def test_referencingtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReferencingType]
    expected_literals = [
        "FULL",
        "PARTIAL",
        "DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReferencingType"

def test_deferredact_exists():
    # Check that the Enumeration exists
    assert DeferredAct is not None

def test_deferredact_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeferredAct]
    expected_literals = [
        "INITIALLY_DEFERRED",
        "INITIALLY_IMMEDIATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeferredAct"

def test_action_exists():
    # Check that the Enumeration exists
    assert Action is not None

def test_action_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Action]
    expected_literals = [
        "CASCADE",
        "SET_NULL",
        "NO_ACTION",
        "RESTRICT",
        "SET_DEFAULT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Action"

def test_deferrableact_exists():
    # Check that the Enumeration exists
    assert DeferrableAct is not None

def test_deferrableact_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DeferrableAct]
    expected_literals = [
        "NOT_DEFFERABLE",
        "DEFFERABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DeferrableAct"


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
ModelElement_strategy = st.builds(
    ModelElement,
)
rdbms_Table_strategy = st.builds(
    rdbms_Table,
)
rdbms_Column_strategy = st.builds(
    rdbms_Column,
    length=
        st.integers(),
    nullable=
        st.booleans(),
    default=
        safe_text,
    precision=
        st.integers()
)
rdbms_Database_strategy = st.builds(
    rdbms_Database,
)
rdbms_Constraints_strategy = st.builds(
    rdbms_Constraints,
    deferred=
        safe_text,
    deferrable=
        safe_text
)
rdbms_ModelElement_strategy = st.builds(
    rdbms_ModelElement,
    name=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
rdbms_UserDefinedDataType_strategy = st.builds(
    rdbms_UserDefinedDataType,
    precision=
        st.integers(),
    length=
        st.integers(),
    defaultValue=
        safe_text
)
rdbms_SystemDataType_strategy = st.builds(
    rdbms_SystemDataType,
    predefinedDecPlaces=
        st.integers(),
    predefinedLength=
        st.integers()
)
PKeyAndUnique_strategy = st.builds(
    PKeyAndUnique,
)
rdbms_UniqueCon_strategy = st.builds(
    rdbms_UniqueCon,
)
rdbms_PrimaryKeyCon_strategy = st.builds(
    rdbms_PrimaryKeyCon,
)
Constraints_strategy = st.builds(
    Constraints,
)
rdbms_ForeignKey_strategy = st.builds(
    rdbms_ForeignKey,
    updateActionRHS=
        safe_text,
    deleteActionRHS=
        safe_text,
    match=
        safe_text,
    inverseReferentialIntegrityCon=
        st.booleans()
)
rdbms_CheckCon_strategy = st.builds(
    rdbms_CheckCon,
    checkCondition=
        safe_text
)
rdbms_DataType_strategy = st.builds(
    rdbms_DataType,
)
rdbms_PKeyAndUnique_strategy = st.builds(
    rdbms_PKeyAndUnique,
)

@given(instance=ModelElement_strategy)
@settings(max_examples=50)
def test_modelelement_instantiation(instance):
    assert isinstance(instance, ModelElement)

@given(instance=rdbms_Table_strategy)
@settings(max_examples=50)
def test_rdbms_table_instantiation(instance):
    assert isinstance(instance, rdbms_Table)

@given(instance=rdbms_Column_strategy)
@settings(max_examples=50)
def test_rdbms_column_instantiation(instance):
    assert isinstance(instance, rdbms_Column)



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=rdbms_Column_strategy)
def test_rdbms_column_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=rdbms_Database_strategy)
@settings(max_examples=50)
def test_rdbms_database_instantiation(instance):
    assert isinstance(instance, rdbms_Database)

@given(instance=rdbms_Constraints_strategy)
@settings(max_examples=50)
def test_rdbms_constraints_instantiation(instance):
    assert isinstance(instance, rdbms_Constraints)



@given(instance=rdbms_Constraints_strategy)
def test_rdbms_constraints_deferred_setter(instance):
    original = instance.deferred
    instance.deferred = original
    assert instance.deferred == original



@given(instance=rdbms_Constraints_strategy)
def test_rdbms_constraints_deferrable_setter(instance):
    original = instance.deferrable
    instance.deferrable = original
    assert instance.deferrable == original

@given(instance=rdbms_ModelElement_strategy)
@settings(max_examples=50)
def test_rdbms_modelelement_instantiation(instance):
    assert isinstance(instance, rdbms_ModelElement)



@given(instance=rdbms_ModelElement_strategy)
def test_rdbms_modelelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=rdbms_UserDefinedDataType_strategy)
@settings(max_examples=50)
def test_rdbms_userdefineddatatype_instantiation(instance):
    assert isinstance(instance, rdbms_UserDefinedDataType)



@given(instance=rdbms_UserDefinedDataType_strategy)
def test_rdbms_userdefineddatatype_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original



@given(instance=rdbms_UserDefinedDataType_strategy)
def test_rdbms_userdefineddatatype_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=rdbms_UserDefinedDataType_strategy)
def test_rdbms_userdefineddatatype_defaultValue_setter(instance):
    original = instance.defaultValue
    instance.defaultValue = original
    assert instance.defaultValue == original

@given(instance=rdbms_SystemDataType_strategy)
@settings(max_examples=50)
def test_rdbms_systemdatatype_instantiation(instance):
    assert isinstance(instance, rdbms_SystemDataType)



@given(instance=rdbms_SystemDataType_strategy)
def test_rdbms_systemdatatype_predefinedDecPlaces_setter(instance):
    original = instance.predefinedDecPlaces
    instance.predefinedDecPlaces = original
    assert instance.predefinedDecPlaces == original



@given(instance=rdbms_SystemDataType_strategy)
def test_rdbms_systemdatatype_predefinedLength_setter(instance):
    original = instance.predefinedLength
    instance.predefinedLength = original
    assert instance.predefinedLength == original

@given(instance=PKeyAndUnique_strategy)
@settings(max_examples=50)
def test_pkeyandunique_instantiation(instance):
    assert isinstance(instance, PKeyAndUnique)

@given(instance=rdbms_UniqueCon_strategy)
@settings(max_examples=50)
def test_rdbms_uniquecon_instantiation(instance):
    assert isinstance(instance, rdbms_UniqueCon)

@given(instance=rdbms_PrimaryKeyCon_strategy)
@settings(max_examples=50)
def test_rdbms_primarykeycon_instantiation(instance):
    assert isinstance(instance, rdbms_PrimaryKeyCon)

@given(instance=Constraints_strategy)
@settings(max_examples=50)
def test_constraints_instantiation(instance):
    assert isinstance(instance, Constraints)

@given(instance=rdbms_ForeignKey_strategy)
@settings(max_examples=50)
def test_rdbms_foreignkey_instantiation(instance):
    assert isinstance(instance, rdbms_ForeignKey)



@given(instance=rdbms_ForeignKey_strategy)
def test_rdbms_foreignkey_updateActionRHS_setter(instance):
    original = instance.updateActionRHS
    instance.updateActionRHS = original
    assert instance.updateActionRHS == original



@given(instance=rdbms_ForeignKey_strategy)
def test_rdbms_foreignkey_deleteActionRHS_setter(instance):
    original = instance.deleteActionRHS
    instance.deleteActionRHS = original
    assert instance.deleteActionRHS == original



@given(instance=rdbms_ForeignKey_strategy)
def test_rdbms_foreignkey_match_setter(instance):
    original = instance.match
    instance.match = original
    assert instance.match == original



@given(instance=rdbms_ForeignKey_strategy)
def test_rdbms_foreignkey_inverseReferentialIntegrityCon_setter(instance):
    original = instance.inverseReferentialIntegrityCon
    instance.inverseReferentialIntegrityCon = original
    assert instance.inverseReferentialIntegrityCon == original

@given(instance=rdbms_CheckCon_strategy)
@settings(max_examples=50)
def test_rdbms_checkcon_instantiation(instance):
    assert isinstance(instance, rdbms_CheckCon)



@given(instance=rdbms_CheckCon_strategy)
def test_rdbms_checkcon_checkCondition_setter(instance):
    original = instance.checkCondition
    instance.checkCondition = original
    assert instance.checkCondition == original

@given(instance=rdbms_DataType_strategy)
@settings(max_examples=50)
def test_rdbms_datatype_instantiation(instance):
    assert isinstance(instance, rdbms_DataType)

@given(instance=rdbms_PKeyAndUnique_strategy)
@settings(max_examples=50)
def test_rdbms_pkeyandunique_instantiation(instance):
    assert isinstance(instance, rdbms_PKeyAndUnique)
