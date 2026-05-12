import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metrics_Value,
    metrics_MetricValueRange,
    metrics_MetricRetentionRules,
    metrics_MetricRetentionRule,
    metrics_Unit,
    metrics_Expression,
    metrics_DateTimeRange,
    Mapping,
    metrics_MappingRDBMS,
    metrics_MappingXLS,
    metrics_MappingCSV,
    metrics_DataKind,
    Base,
    metrics_MappingStatistic,
    metrics_MetricSource,
    metrics_MappingColumn,
    metrics_MappingRecord,
    metrics_Metric,
    metrics_Mapping,
    DataKind,
    metrics_ValueDataKind,
    metrics_IdentifierDataKind,
    ValueKindType,
    MetricRetentionPeriod,
    ObjectKindType,
    KindHintType,
    DatabaseTypeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics_value_is_not_abstract():
    assert not inspect.isabstract(metrics_Value)


def test_metrics_value_constructor_exists():
    assert callable(metrics_Value.__init__)


def test_metrics_value_constructor_args():
    sig = inspect.signature(metrics_Value.__init__)
    params = list(sig.parameters.keys())



def test_metrics_metricvaluerange_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricValueRange)


def test_metrics_metricvaluerange_constructor_exists():
    assert callable(metrics_MetricValueRange.__init__)


def test_metrics_metricvaluerange_constructor_args():
    sig = inspect.signature(metrics_MetricValueRange.__init__)
    params = list(sig.parameters.keys())
    assert "kindHint" in params, "Missing parameter 'kindHint'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"

def test_metrics_metricvaluerange_has_kindHint():
    assert hasattr(metrics_MetricValueRange, "kindHint")
    descriptor = None
    for klass in metrics_MetricValueRange.__mro__:
        if "kindHint" in klass.__dict__:
            descriptor = klass.__dict__["kindHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricvaluerange_has_intervalHint():
    assert hasattr(metrics_MetricValueRange, "intervalHint")
    descriptor = None
    for klass in metrics_MetricValueRange.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)



def test_metrics_metricretentionrules_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricRetentionRules)


def test_metrics_metricretentionrules_constructor_exists():
    assert callable(metrics_MetricRetentionRules.__init__)


def test_metrics_metricretentionrules_constructor_args():
    sig = inspect.signature(metrics_MetricRetentionRules.__init__)
    params = list(sig.parameters.keys())



def test_metrics_metricretentionrule_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricRetentionRule)


def test_metrics_metricretentionrule_constructor_exists():
    assert callable(metrics_MetricRetentionRule.__init__)


def test_metrics_metricretentionrule_constructor_args():
    sig = inspect.signature(metrics_MetricRetentionRule.__init__)
    params = list(sig.parameters.keys())
    assert "period" in params, "Missing parameter 'period'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics_metricretentionrule_has_period():
    assert hasattr(metrics_MetricRetentionRule, "period")
    descriptor = None
    for klass in metrics_MetricRetentionRule.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricretentionrule_has_intervalHint():
    assert hasattr(metrics_MetricRetentionRule, "intervalHint")
    descriptor = None
    for klass in metrics_MetricRetentionRule.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricretentionrule_has_name():
    assert hasattr(metrics_MetricRetentionRule, "name")
    descriptor = None
    for klass in metrics_MetricRetentionRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics_unit_is_not_abstract():
    assert not inspect.isabstract(metrics_Unit)


def test_metrics_unit_constructor_exists():
    assert callable(metrics_Unit.__init__)


def test_metrics_unit_constructor_args():
    sig = inspect.signature(metrics_Unit.__init__)
    params = list(sig.parameters.keys())



def test_metrics_expression_is_not_abstract():
    assert not inspect.isabstract(metrics_Expression)


def test_metrics_expression_constructor_exists():
    assert callable(metrics_Expression.__init__)


def test_metrics_expression_constructor_args():
    sig = inspect.signature(metrics_Expression.__init__)
    params = list(sig.parameters.keys())



def test_metrics_datetimerange_is_not_abstract():
    assert not inspect.isabstract(metrics_DateTimeRange)


def test_metrics_datetimerange_constructor_exists():
    assert callable(metrics_DateTimeRange.__init__)


def test_metrics_datetimerange_constructor_args():
    sig = inspect.signature(metrics_DateTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_metrics_mappingrdbms_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingRDBMS)


def test_metrics_mappingrdbms_constructor_exists():
    assert callable(metrics_MappingRDBMS.__init__)


def test_metrics_mappingrdbms_constructor_args():
    sig = inspect.signature(metrics_MappingRDBMS.__init__)
    params = list(sig.parameters.keys())
    assert "timeFormat" in params, "Missing parameter 'timeFormat'"
    assert "databaseType" in params, "Missing parameter 'databaseType'"
    assert "user" in params, "Missing parameter 'user'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"
    assert "dateTimeFormat" in params, "Missing parameter 'dateTimeFormat'"
    assert "query" in params, "Missing parameter 'query'"
    assert "password" in params, "Missing parameter 'password'"

def test_metrics_mappingrdbms_has_timeFormat():
    assert hasattr(metrics_MappingRDBMS, "timeFormat")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "timeFormat" in klass.__dict__:
            descriptor = klass.__dict__["timeFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_databaseType():
    assert hasattr(metrics_MappingRDBMS, "databaseType")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "databaseType" in klass.__dict__:
            descriptor = klass.__dict__["databaseType"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_user():
    assert hasattr(metrics_MappingRDBMS, "user")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_dateFormat():
    assert hasattr(metrics_MappingRDBMS, "dateFormat")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_dateTimeFormat():
    assert hasattr(metrics_MappingRDBMS, "dateTimeFormat")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "dateTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_query():
    assert hasattr(metrics_MappingRDBMS, "query")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrdbms_has_password():
    assert hasattr(metrics_MappingRDBMS, "password")
    descriptor = None
    for klass in metrics_MappingRDBMS.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_metrics_mappingxls_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingXLS)


def test_metrics_mappingxls_constructor_exists():
    assert callable(metrics_MappingXLS.__init__)


def test_metrics_mappingxls_constructor_args():
    sig = inspect.signature(metrics_MappingXLS.__init__)
    params = list(sig.parameters.keys())
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"
    assert "sheetNumber" in params, "Missing parameter 'sheetNumber'"

def test_metrics_mappingxls_has_filterPattern():
    assert hasattr(metrics_MappingXLS, "filterPattern")
    descriptor = None
    for klass in metrics_MappingXLS.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingxls_has_sheetNumber():
    assert hasattr(metrics_MappingXLS, "sheetNumber")
    descriptor = None
    for klass in metrics_MappingXLS.__mro__:
        if "sheetNumber" in klass.__dict__:
            descriptor = klass.__dict__["sheetNumber"]
            break
    assert isinstance(descriptor, property)



def test_metrics_mappingcsv_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingCSV)


def test_metrics_mappingcsv_constructor_exists():
    assert callable(metrics_MappingCSV.__init__)


def test_metrics_mappingcsv_constructor_args():
    sig = inspect.signature(metrics_MappingCSV.__init__)
    params = list(sig.parameters.keys())
    assert "delimiter" in params, "Missing parameter 'delimiter'"
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"

def test_metrics_mappingcsv_has_delimiter():
    assert hasattr(metrics_MappingCSV, "delimiter")
    descriptor = None
    for klass in metrics_MappingCSV.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingcsv_has_filterPattern():
    assert hasattr(metrics_MappingCSV, "filterPattern")
    descriptor = None
    for klass in metrics_MappingCSV.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)



def test_metrics_datakind_is_not_abstract():
    assert not inspect.isabstract(metrics_DataKind)


def test_metrics_datakind_constructor_exists():
    assert callable(metrics_DataKind.__init__)


def test_metrics_datakind_constructor_args():
    sig = inspect.signature(metrics_DataKind.__init__)
    params = list(sig.parameters.keys())



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_metrics_mappingstatistic_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingStatistic)


def test_metrics_mappingstatistic_constructor_exists():
    assert callable(metrics_MappingStatistic.__init__)


def test_metrics_mappingstatistic_constructor_args():
    sig = inspect.signature(metrics_MappingStatistic.__init__)
    params = list(sig.parameters.keys())
    assert "totalRecords" in params, "Missing parameter 'totalRecords'"
    assert "message" in params, "Missing parameter 'message'"
    assert "intervalEstimate" in params, "Missing parameter 'intervalEstimate'"

def test_metrics_mappingstatistic_has_totalRecords():
    assert hasattr(metrics_MappingStatistic, "totalRecords")
    descriptor = None
    for klass in metrics_MappingStatistic.__mro__:
        if "totalRecords" in klass.__dict__:
            descriptor = klass.__dict__["totalRecords"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingstatistic_has_message():
    assert hasattr(metrics_MappingStatistic, "message")
    descriptor = None
    for klass in metrics_MappingStatistic.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingstatistic_has_intervalEstimate():
    assert hasattr(metrics_MappingStatistic, "intervalEstimate")
    descriptor = None
    for klass in metrics_MappingStatistic.__mro__:
        if "intervalEstimate" in klass.__dict__:
            descriptor = klass.__dict__["intervalEstimate"]
            break
    assert isinstance(descriptor, property)



def test_metrics_metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics_MetricSource)


def test_metrics_metricsource_constructor_exists():
    assert callable(metrics_MetricSource.__init__)


def test_metrics_metricsource_constructor_args():
    sig = inspect.signature(metrics_MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"
    assert "name" in params, "Missing parameter 'name'"
    assert "metricLocation" in params, "Missing parameter 'metricLocation'"

def test_metrics_metricsource_has_filterPattern():
    assert hasattr(metrics_MetricSource, "filterPattern")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_name():
    assert hasattr(metrics_MetricSource, "name")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metricsource_has_metricLocation():
    assert hasattr(metrics_MetricSource, "metricLocation")
    descriptor = None
    for klass in metrics_MetricSource.__mro__:
        if "metricLocation" in klass.__dict__:
            descriptor = klass.__dict__["metricLocation"]
            break
    assert isinstance(descriptor, property)



def test_metrics_mappingcolumn_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingColumn)


def test_metrics_mappingcolumn_constructor_exists():
    assert callable(metrics_MappingColumn.__init__)


def test_metrics_mappingcolumn_constructor_args():
    sig = inspect.signature(metrics_MappingColumn.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_metrics_mappingcolumn_has_column():
    assert hasattr(metrics_MappingColumn, "column")
    descriptor = None
    for klass in metrics_MappingColumn.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_metrics_mappingrecord_is_not_abstract():
    assert not inspect.isabstract(metrics_MappingRecord)


def test_metrics_mappingrecord_constructor_exists():
    assert callable(metrics_MappingRecord.__init__)


def test_metrics_mappingrecord_constructor_args():
    sig = inspect.signature(metrics_MappingRecord.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"
    assert "message" in params, "Missing parameter 'message'"
    assert "count" in params, "Missing parameter 'count'"

def test_metrics_mappingrecord_has_column():
    assert hasattr(metrics_MappingRecord, "column")
    descriptor = None
    for klass in metrics_MappingRecord.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrecord_has_message():
    assert hasattr(metrics_MappingRecord, "message")
    descriptor = None
    for klass in metrics_MappingRecord.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mappingrecord_has_count():
    assert hasattr(metrics_MappingRecord, "count")
    descriptor = None
    for klass in metrics_MappingRecord.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_metrics_metric_is_not_abstract():
    assert not inspect.isabstract(metrics_Metric)


def test_metrics_metric_constructor_exists():
    assert callable(metrics_Metric.__init__)


def test_metrics_metric_constructor_args():
    sig = inspect.signature(metrics_Metric.__init__)
    params = list(sig.parameters.keys())
    assert "measurementKind" in params, "Missing parameter 'measurementKind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "measurementPoint" in params, "Missing parameter 'measurementPoint'"
    assert "description" in params, "Missing parameter 'description'"

def test_metrics_metric_has_measurementKind():
    assert hasattr(metrics_Metric, "measurementKind")
    descriptor = None
    for klass in metrics_Metric.__mro__:
        if "measurementKind" in klass.__dict__:
            descriptor = klass.__dict__["measurementKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metric_has_name():
    assert hasattr(metrics_Metric, "name")
    descriptor = None
    for klass in metrics_Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metric_has_measurementPoint():
    assert hasattr(metrics_Metric, "measurementPoint")
    descriptor = None
    for klass in metrics_Metric.__mro__:
        if "measurementPoint" in klass.__dict__:
            descriptor = klass.__dict__["measurementPoint"]
            break
    assert isinstance(descriptor, property)

def test_metrics_metric_has_description():
    assert hasattr(metrics_Metric, "description")
    descriptor = None
    for klass in metrics_Metric.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_metrics_mapping_is_not_abstract():
    assert not inspect.isabstract(metrics_Mapping)


def test_metrics_mapping_constructor_exists():
    assert callable(metrics_Mapping.__init__)


def test_metrics_mapping_constructor_args():
    sig = inspect.signature(metrics_Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "firstDataRow" in params, "Missing parameter 'firstDataRow'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"
    assert "headerRow" in params, "Missing parameter 'headerRow'"

def test_metrics_mapping_has_firstDataRow():
    assert hasattr(metrics_Mapping, "firstDataRow")
    descriptor = None
    for klass in metrics_Mapping.__mro__:
        if "firstDataRow" in klass.__dict__:
            descriptor = klass.__dict__["firstDataRow"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mapping_has_intervalHint():
    assert hasattr(metrics_Mapping, "intervalHint")
    descriptor = None
    for klass in metrics_Mapping.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics_mapping_has_headerRow():
    assert hasattr(metrics_Mapping, "headerRow")
    descriptor = None
    for klass in metrics_Mapping.__mro__:
        if "headerRow" in klass.__dict__:
            descriptor = klass.__dict__["headerRow"]
            break
    assert isinstance(descriptor, property)



def test_datakind_is_not_abstract():
    assert not inspect.isabstract(DataKind)


def test_datakind_constructor_exists():
    assert callable(DataKind.__init__)


def test_datakind_constructor_args():
    sig = inspect.signature(DataKind.__init__)
    params = list(sig.parameters.keys())



def test_metrics_valuedatakind_is_not_abstract():
    assert not inspect.isabstract(metrics_ValueDataKind)


def test_metrics_valuedatakind_constructor_exists():
    assert callable(metrics_ValueDataKind.__init__)


def test_metrics_valuedatakind_constructor_args():
    sig = inspect.signature(metrics_ValueDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "valueKind" in params, "Missing parameter 'valueKind'"
    assert "kindHint" in params, "Missing parameter 'kindHint'"
    assert "format" in params, "Missing parameter 'format'"

def test_metrics_valuedatakind_has_valueKind():
    assert hasattr(metrics_ValueDataKind, "valueKind")
    descriptor = None
    for klass in metrics_ValueDataKind.__mro__:
        if "valueKind" in klass.__dict__:
            descriptor = klass.__dict__["valueKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics_valuedatakind_has_kindHint():
    assert hasattr(metrics_ValueDataKind, "kindHint")
    descriptor = None
    for klass in metrics_ValueDataKind.__mro__:
        if "kindHint" in klass.__dict__:
            descriptor = klass.__dict__["kindHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics_valuedatakind_has_format():
    assert hasattr(metrics_ValueDataKind, "format")
    descriptor = None
    for klass in metrics_ValueDataKind.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_metrics_identifierdatakind_is_not_abstract():
    assert not inspect.isabstract(metrics_IdentifierDataKind)


def test_metrics_identifierdatakind_constructor_exists():
    assert callable(metrics_IdentifierDataKind.__init__)


def test_metrics_identifierdatakind_constructor_args():
    sig = inspect.signature(metrics_IdentifierDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "objectKind" in params, "Missing parameter 'objectKind'"
    assert "objectProperty" in params, "Missing parameter 'objectProperty'"

def test_metrics_identifierdatakind_has_pattern():
    assert hasattr(metrics_IdentifierDataKind, "pattern")
    descriptor = None
    for klass in metrics_IdentifierDataKind.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics_identifierdatakind_has_objectKind():
    assert hasattr(metrics_IdentifierDataKind, "objectKind")
    descriptor = None
    for klass in metrics_IdentifierDataKind.__mro__:
        if "objectKind" in klass.__dict__:
            descriptor = klass.__dict__["objectKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics_identifierdatakind_has_objectProperty():
    assert hasattr(metrics_IdentifierDataKind, "objectProperty")
    descriptor = None
    for klass in metrics_IdentifierDataKind.__mro__:
        if "objectProperty" in klass.__dict__:
            descriptor = klass.__dict__["objectProperty"]
            break
    assert isinstance(descriptor, property)

def test_valuekindtype_exists():
    # Check that the Enumeration exists
    assert ValueKindType is not None

def test_valuekindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueKindType]
    expected_literals = [
        "NULL",
        "DATE",
        "METRIC",
        "DATETIME",
        "TIME",
        "INTERVAL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueKindType"

def test_metricretentionperiod_exists():
    # Check that the Enumeration exists
    assert MetricRetentionPeriod is not None

def test_metricretentionperiod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricRetentionPeriod]
    expected_literals = [
        "OneYear",
        "OneWeek",
        "Always",
        "OneMonth",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricRetentionPeriod"

def test_objectkindtype_exists():
    # Check that the Enumeration exists
    assert ObjectKindType is not None

def test_objectkindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectKindType]
    expected_literals = [
        "NODE",
        "FUNCTION",
        "EQUIPMENT",
        "RELATIONSHIP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectKindType"

def test_kindhinttype_exists():
    # Check that the Enumeration exists
    assert KindHintType is not None

def test_kindhinttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindHintType]
    expected_literals = [
        "BH",
        "AVG",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindHintType"

def test_databasetypetype_exists():
    # Check that the Enumeration exists
    assert DatabaseTypeType is not None

def test_databasetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseTypeType]
    expected_literals = [
        "Oracle",
        "Postgres",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatabaseTypeType"


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
metrics_Value_strategy = st.builds(
    metrics_Value,
)
metrics_MetricValueRange_strategy = st.builds(
    metrics_MetricValueRange,
    kindHint=
        safe_text,
    intervalHint=
        safe_text
)
metrics_MetricRetentionRules_strategy = st.builds(
    metrics_MetricRetentionRules,
)
metrics_MetricRetentionRule_strategy = st.builds(
    metrics_MetricRetentionRule,
    period=
        safe_text,
    intervalHint=
        safe_text,
    name=
        safe_text
)
metrics_Unit_strategy = st.builds(
    metrics_Unit,
)
metrics_Expression_strategy = st.builds(
    metrics_Expression,
)
metrics_DateTimeRange_strategy = st.builds(
    metrics_DateTimeRange,
)
Mapping_strategy = st.builds(
    Mapping,
)
metrics_MappingRDBMS_strategy = st.builds(
    metrics_MappingRDBMS,
    timeFormat=
        safe_text,
    databaseType=
        safe_text,
    user=
        safe_text,
    dateFormat=
        safe_text,
    dateTimeFormat=
        safe_text,
    query=
        safe_text,
    password=
        safe_text
)
metrics_MappingXLS_strategy = st.builds(
    metrics_MappingXLS,
    filterPattern=
        safe_text,
    sheetNumber=
        safe_text
)
metrics_MappingCSV_strategy = st.builds(
    metrics_MappingCSV,
    delimiter=
        safe_text,
    filterPattern=
        safe_text
)
metrics_DataKind_strategy = st.builds(
    metrics_DataKind,
)
Base_strategy = st.builds(
    Base,
)
metrics_MappingStatistic_strategy = st.builds(
    metrics_MappingStatistic,
    totalRecords=
        safe_text,
    message=
        safe_text,
    intervalEstimate=
        safe_text
)
metrics_MetricSource_strategy = st.builds(
    metrics_MetricSource,
    filterPattern=
        safe_text,
    name=
        safe_text,
    metricLocation=
        safe_text
)
metrics_MappingColumn_strategy = st.builds(
    metrics_MappingColumn,
    column=
        safe_text
)
metrics_MappingRecord_strategy = st.builds(
    metrics_MappingRecord,
    column=
        safe_text,
    message=
        safe_text,
    count=
        safe_text
)
metrics_Metric_strategy = st.builds(
    metrics_Metric,
    measurementKind=
        safe_text,
    name=
        safe_text,
    measurementPoint=
        safe_text,
    description=
        safe_text
)
metrics_Mapping_strategy = st.builds(
    metrics_Mapping,
    firstDataRow=
        safe_text,
    intervalHint=
        safe_text,
    headerRow=
        safe_text
)
DataKind_strategy = st.builds(
    DataKind,
)
metrics_ValueDataKind_strategy = st.builds(
    metrics_ValueDataKind,
    valueKind=
        safe_text,
    kindHint=
        safe_text,
    format=
        safe_text
)
metrics_IdentifierDataKind_strategy = st.builds(
    metrics_IdentifierDataKind,
    pattern=
        safe_text,
    objectKind=
        safe_text,
    objectProperty=
        safe_text
)

@given(instance=metrics_Value_strategy)
@settings(max_examples=50)
def test_metrics_value_instantiation(instance):
    assert isinstance(instance, metrics_Value)

@given(instance=metrics_MetricValueRange_strategy)
@settings(max_examples=50)
def test_metrics_metricvaluerange_instantiation(instance):
    assert isinstance(instance, metrics_MetricValueRange)



@given(instance=metrics_MetricValueRange_strategy)
def test_metrics_metricvaluerange_kindHint_setter(instance):
    original = instance.kindHint
    instance.kindHint = original
    assert instance.kindHint == original



@given(instance=metrics_MetricValueRange_strategy)
def test_metrics_metricvaluerange_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=metrics_MetricRetentionRules_strategy)
@settings(max_examples=50)
def test_metrics_metricretentionrules_instantiation(instance):
    assert isinstance(instance, metrics_MetricRetentionRules)

@given(instance=metrics_MetricRetentionRule_strategy)
@settings(max_examples=50)
def test_metrics_metricretentionrule_instantiation(instance):
    assert isinstance(instance, metrics_MetricRetentionRule)



@given(instance=metrics_MetricRetentionRule_strategy)
def test_metrics_metricretentionrule_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original



@given(instance=metrics_MetricRetentionRule_strategy)
def test_metrics_metricretentionrule_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original



@given(instance=metrics_MetricRetentionRule_strategy)
def test_metrics_metricretentionrule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics_Unit_strategy)
@settings(max_examples=50)
def test_metrics_unit_instantiation(instance):
    assert isinstance(instance, metrics_Unit)

@given(instance=metrics_Expression_strategy)
@settings(max_examples=50)
def test_metrics_expression_instantiation(instance):
    assert isinstance(instance, metrics_Expression)

@given(instance=metrics_DateTimeRange_strategy)
@settings(max_examples=50)
def test_metrics_datetimerange_instantiation(instance):
    assert isinstance(instance, metrics_DateTimeRange)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=metrics_MappingRDBMS_strategy)
@settings(max_examples=50)
def test_metrics_mappingrdbms_instantiation(instance):
    assert isinstance(instance, metrics_MappingRDBMS)



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_timeFormat_setter(instance):
    original = instance.timeFormat
    instance.timeFormat = original
    assert instance.timeFormat == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_databaseType_setter(instance):
    original = instance.databaseType
    instance.databaseType = original
    assert instance.databaseType == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_dateTimeFormat_setter(instance):
    original = instance.dateTimeFormat
    instance.dateTimeFormat = original
    assert instance.dateTimeFormat == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original



@given(instance=metrics_MappingRDBMS_strategy)
def test_metrics_mappingrdbms_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=metrics_MappingXLS_strategy)
@settings(max_examples=50)
def test_metrics_mappingxls_instantiation(instance):
    assert isinstance(instance, metrics_MappingXLS)



@given(instance=metrics_MappingXLS_strategy)
def test_metrics_mappingxls_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original



@given(instance=metrics_MappingXLS_strategy)
def test_metrics_mappingxls_sheetNumber_setter(instance):
    original = instance.sheetNumber
    instance.sheetNumber = original
    assert instance.sheetNumber == original

@given(instance=metrics_MappingCSV_strategy)
@settings(max_examples=50)
def test_metrics_mappingcsv_instantiation(instance):
    assert isinstance(instance, metrics_MappingCSV)



@given(instance=metrics_MappingCSV_strategy)
def test_metrics_mappingcsv_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original



@given(instance=metrics_MappingCSV_strategy)
def test_metrics_mappingcsv_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original

@given(instance=metrics_DataKind_strategy)
@settings(max_examples=50)
def test_metrics_datakind_instantiation(instance):
    assert isinstance(instance, metrics_DataKind)

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=metrics_MappingStatistic_strategy)
@settings(max_examples=50)
def test_metrics_mappingstatistic_instantiation(instance):
    assert isinstance(instance, metrics_MappingStatistic)



@given(instance=metrics_MappingStatistic_strategy)
def test_metrics_mappingstatistic_totalRecords_setter(instance):
    original = instance.totalRecords
    instance.totalRecords = original
    assert instance.totalRecords == original



@given(instance=metrics_MappingStatistic_strategy)
def test_metrics_mappingstatistic_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=metrics_MappingStatistic_strategy)
def test_metrics_mappingstatistic_intervalEstimate_setter(instance):
    original = instance.intervalEstimate
    instance.intervalEstimate = original
    assert instance.intervalEstimate == original

@given(instance=metrics_MetricSource_strategy)
@settings(max_examples=50)
def test_metrics_metricsource_instantiation(instance):
    assert isinstance(instance, metrics_MetricSource)



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metrics_MetricSource_strategy)
def test_metrics_metricsource_metricLocation_setter(instance):
    original = instance.metricLocation
    instance.metricLocation = original
    assert instance.metricLocation == original

@given(instance=metrics_MappingColumn_strategy)
@settings(max_examples=50)
def test_metrics_mappingcolumn_instantiation(instance):
    assert isinstance(instance, metrics_MappingColumn)



@given(instance=metrics_MappingColumn_strategy)
def test_metrics_mappingcolumn_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=metrics_MappingRecord_strategy)
@settings(max_examples=50)
def test_metrics_mappingrecord_instantiation(instance):
    assert isinstance(instance, metrics_MappingRecord)



@given(instance=metrics_MappingRecord_strategy)
def test_metrics_mappingrecord_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original



@given(instance=metrics_MappingRecord_strategy)
def test_metrics_mappingrecord_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original



@given(instance=metrics_MappingRecord_strategy)
def test_metrics_mappingrecord_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=metrics_Metric_strategy)
@settings(max_examples=50)
def test_metrics_metric_instantiation(instance):
    assert isinstance(instance, metrics_Metric)



@given(instance=metrics_Metric_strategy)
def test_metrics_metric_measurementKind_setter(instance):
    original = instance.measurementKind
    instance.measurementKind = original
    assert instance.measurementKind == original



@given(instance=metrics_Metric_strategy)
def test_metrics_metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=metrics_Metric_strategy)
def test_metrics_metric_measurementPoint_setter(instance):
    original = instance.measurementPoint
    instance.measurementPoint = original
    assert instance.measurementPoint == original



@given(instance=metrics_Metric_strategy)
def test_metrics_metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=metrics_Mapping_strategy)
@settings(max_examples=50)
def test_metrics_mapping_instantiation(instance):
    assert isinstance(instance, metrics_Mapping)



@given(instance=metrics_Mapping_strategy)
def test_metrics_mapping_firstDataRow_setter(instance):
    original = instance.firstDataRow
    instance.firstDataRow = original
    assert instance.firstDataRow == original



@given(instance=metrics_Mapping_strategy)
def test_metrics_mapping_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original



@given(instance=metrics_Mapping_strategy)
def test_metrics_mapping_headerRow_setter(instance):
    original = instance.headerRow
    instance.headerRow = original
    assert instance.headerRow == original

@given(instance=DataKind_strategy)
@settings(max_examples=50)
def test_datakind_instantiation(instance):
    assert isinstance(instance, DataKind)

@given(instance=metrics_ValueDataKind_strategy)
@settings(max_examples=50)
def test_metrics_valuedatakind_instantiation(instance):
    assert isinstance(instance, metrics_ValueDataKind)



@given(instance=metrics_ValueDataKind_strategy)
def test_metrics_valuedatakind_valueKind_setter(instance):
    original = instance.valueKind
    instance.valueKind = original
    assert instance.valueKind == original



@given(instance=metrics_ValueDataKind_strategy)
def test_metrics_valuedatakind_kindHint_setter(instance):
    original = instance.kindHint
    instance.kindHint = original
    assert instance.kindHint == original



@given(instance=metrics_ValueDataKind_strategy)
def test_metrics_valuedatakind_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=metrics_IdentifierDataKind_strategy)
@settings(max_examples=50)
def test_metrics_identifierdatakind_instantiation(instance):
    assert isinstance(instance, metrics_IdentifierDataKind)



@given(instance=metrics_IdentifierDataKind_strategy)
def test_metrics_identifierdatakind_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original



@given(instance=metrics_IdentifierDataKind_strategy)
def test_metrics_identifierdatakind_objectKind_setter(instance):
    original = instance.objectKind
    instance.objectKind = original
    assert instance.objectKind == original



@given(instance=metrics_IdentifierDataKind_strategy)
def test_metrics_identifierdatakind_objectProperty_setter(instance):
    original = instance.objectProperty
    instance.objectProperty = original
    assert instance.objectProperty == original
