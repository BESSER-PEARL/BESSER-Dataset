import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metrics::Value,
    metrics::MetricValueRange,
    metrics::MetricRetentionRules,
    metrics::MetricRetentionRule,
    metrics::Unit,
    metrics::Expression,
    metrics::DateTimeRange,
    Mapping,
    metrics::MappingRDBMS,
    metrics::MappingXLS,
    metrics::MappingCSV,
    Base,
    metrics::Metric,
    metrics::MappingStatistic,
    metrics::MappingColumn,
    metrics::MetricSource,
    metrics::MappingRecord,
    metrics::Mapping,
    DataKind,
    metrics::ValueDataKind,
    metrics::IdentifierDataKind,
    metrics::DataKind,
    KindHintType,
    ObjectKindType,
    MetricRetentionPeriod,
    ValueKindType,
    DatabaseTypeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metrics::value_is_not_abstract():
    assert not inspect.isabstract(metrics::Value)


def test_metrics::value_constructor_exists():
    assert callable(metrics::Value.__init__)


def test_metrics::value_constructor_args():
    sig = inspect.signature(metrics::Value.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricvaluerange_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricValueRange)


def test_metrics::metricvaluerange_constructor_exists():
    assert callable(metrics::MetricValueRange.__init__)


def test_metrics::metricvaluerange_constructor_args():
    sig = inspect.signature(metrics::MetricValueRange.__init__)
    params = list(sig.parameters.keys())
    assert "kindHint" in params, "Missing parameter 'kindHint'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"

def test_metrics::metricvaluerange_has_kindHint():
    assert hasattr(metrics::MetricValueRange, "kindHint")
    descriptor = None
    for klass in metrics::MetricValueRange.__mro__:
        if "kindHint" in klass.__dict__:
            descriptor = klass.__dict__["kindHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricvaluerange_has_intervalHint():
    assert hasattr(metrics::MetricValueRange, "intervalHint")
    descriptor = None
    for klass in metrics::MetricValueRange.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)



def test_metrics::metricretentionrules_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricRetentionRules)


def test_metrics::metricretentionrules_constructor_exists():
    assert callable(metrics::MetricRetentionRules.__init__)


def test_metrics::metricretentionrules_constructor_args():
    sig = inspect.signature(metrics::MetricRetentionRules.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metricretentionrule_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricRetentionRule)


def test_metrics::metricretentionrule_constructor_exists():
    assert callable(metrics::MetricRetentionRule.__init__)


def test_metrics::metricretentionrule_constructor_args():
    sig = inspect.signature(metrics::MetricRetentionRule.__init__)
    params = list(sig.parameters.keys())
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"
    assert "period" in params, "Missing parameter 'period'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metricretentionrule_has_intervalHint():
    assert hasattr(metrics::MetricRetentionRule, "intervalHint")
    descriptor = None
    for klass in metrics::MetricRetentionRule.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricretentionrule_has_period():
    assert hasattr(metrics::MetricRetentionRule, "period")
    descriptor = None
    for klass in metrics::MetricRetentionRule.__mro__:
        if "period" in klass.__dict__:
            descriptor = klass.__dict__["period"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricretentionrule_has_name():
    assert hasattr(metrics::MetricRetentionRule, "name")
    descriptor = None
    for klass in metrics::MetricRetentionRule.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics::unit_is_not_abstract():
    assert not inspect.isabstract(metrics::Unit)


def test_metrics::unit_constructor_exists():
    assert callable(metrics::Unit.__init__)


def test_metrics::unit_constructor_args():
    sig = inspect.signature(metrics::Unit.__init__)
    params = list(sig.parameters.keys())



def test_metrics::expression_is_not_abstract():
    assert not inspect.isabstract(metrics::Expression)


def test_metrics::expression_constructor_exists():
    assert callable(metrics::Expression.__init__)


def test_metrics::expression_constructor_args():
    sig = inspect.signature(metrics::Expression.__init__)
    params = list(sig.parameters.keys())



def test_metrics::datetimerange_is_not_abstract():
    assert not inspect.isabstract(metrics::DateTimeRange)


def test_metrics::datetimerange_constructor_exists():
    assert callable(metrics::DateTimeRange.__init__)


def test_metrics::datetimerange_constructor_args():
    sig = inspect.signature(metrics::DateTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_mapping_is_not_abstract():
    assert not inspect.isabstract(Mapping)


def test_mapping_constructor_exists():
    assert callable(Mapping.__init__)


def test_mapping_constructor_args():
    sig = inspect.signature(Mapping.__init__)
    params = list(sig.parameters.keys())



def test_metrics::mappingrdbms_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingRDBMS)


def test_metrics::mappingrdbms_constructor_exists():
    assert callable(metrics::MappingRDBMS.__init__)


def test_metrics::mappingrdbms_constructor_args():
    sig = inspect.signature(metrics::MappingRDBMS.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "dateFormat" in params, "Missing parameter 'dateFormat'"
    assert "timeFormat" in params, "Missing parameter 'timeFormat'"
    assert "databaseType" in params, "Missing parameter 'databaseType'"
    assert "dateTimeFormat" in params, "Missing parameter 'dateTimeFormat'"
    assert "user" in params, "Missing parameter 'user'"
    assert "query" in params, "Missing parameter 'query'"

def test_metrics::mappingrdbms_has_password():
    assert hasattr(metrics::MappingRDBMS, "password")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_dateFormat():
    assert hasattr(metrics::MappingRDBMS, "dateFormat")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "dateFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_timeFormat():
    assert hasattr(metrics::MappingRDBMS, "timeFormat")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "timeFormat" in klass.__dict__:
            descriptor = klass.__dict__["timeFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_databaseType():
    assert hasattr(metrics::MappingRDBMS, "databaseType")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "databaseType" in klass.__dict__:
            descriptor = klass.__dict__["databaseType"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_dateTimeFormat():
    assert hasattr(metrics::MappingRDBMS, "dateTimeFormat")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "dateTimeFormat" in klass.__dict__:
            descriptor = klass.__dict__["dateTimeFormat"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_user():
    assert hasattr(metrics::MappingRDBMS, "user")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrdbms_has_query():
    assert hasattr(metrics::MappingRDBMS, "query")
    descriptor = None
    for klass in metrics::MappingRDBMS.__mro__:
        if "query" in klass.__dict__:
            descriptor = klass.__dict__["query"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mappingxls_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingXLS)


def test_metrics::mappingxls_constructor_exists():
    assert callable(metrics::MappingXLS.__init__)


def test_metrics::mappingxls_constructor_args():
    sig = inspect.signature(metrics::MappingXLS.__init__)
    params = list(sig.parameters.keys())
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"
    assert "sheetNumber" in params, "Missing parameter 'sheetNumber'"

def test_metrics::mappingxls_has_filterPattern():
    assert hasattr(metrics::MappingXLS, "filterPattern")
    descriptor = None
    for klass in metrics::MappingXLS.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingxls_has_sheetNumber():
    assert hasattr(metrics::MappingXLS, "sheetNumber")
    descriptor = None
    for klass in metrics::MappingXLS.__mro__:
        if "sheetNumber" in klass.__dict__:
            descriptor = klass.__dict__["sheetNumber"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mappingcsv_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingCSV)


def test_metrics::mappingcsv_constructor_exists():
    assert callable(metrics::MappingCSV.__init__)


def test_metrics::mappingcsv_constructor_args():
    sig = inspect.signature(metrics::MappingCSV.__init__)
    params = list(sig.parameters.keys())
    assert "delimiter" in params, "Missing parameter 'delimiter'"
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"

def test_metrics::mappingcsv_has_delimiter():
    assert hasattr(metrics::MappingCSV, "delimiter")
    descriptor = None
    for klass in metrics::MappingCSV.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingcsv_has_filterPattern():
    assert hasattr(metrics::MappingCSV, "filterPattern")
    descriptor = None
    for klass in metrics::MappingCSV.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_metrics::metric_is_not_abstract():
    assert not inspect.isabstract(metrics::Metric)


def test_metrics::metric_constructor_exists():
    assert callable(metrics::Metric.__init__)


def test_metrics::metric_constructor_args():
    sig = inspect.signature(metrics::Metric.__init__)
    params = list(sig.parameters.keys())
    assert "measurementPoint" in params, "Missing parameter 'measurementPoint'"
    assert "measurementKind" in params, "Missing parameter 'measurementKind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_metrics::metric_has_measurementPoint():
    assert hasattr(metrics::Metric, "measurementPoint")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "measurementPoint" in klass.__dict__:
            descriptor = klass.__dict__["measurementPoint"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metric_has_measurementKind():
    assert hasattr(metrics::Metric, "measurementKind")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "measurementKind" in klass.__dict__:
            descriptor = klass.__dict__["measurementKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metric_has_name():
    assert hasattr(metrics::Metric, "name")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metric_has_description():
    assert hasattr(metrics::Metric, "description")
    descriptor = None
    for klass in metrics::Metric.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mappingstatistic_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingStatistic)


def test_metrics::mappingstatistic_constructor_exists():
    assert callable(metrics::MappingStatistic.__init__)


def test_metrics::mappingstatistic_constructor_args():
    sig = inspect.signature(metrics::MappingStatistic.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "totalRecords" in params, "Missing parameter 'totalRecords'"
    assert "intervalEstimate" in params, "Missing parameter 'intervalEstimate'"

def test_metrics::mappingstatistic_has_message():
    assert hasattr(metrics::MappingStatistic, "message")
    descriptor = None
    for klass in metrics::MappingStatistic.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingstatistic_has_totalRecords():
    assert hasattr(metrics::MappingStatistic, "totalRecords")
    descriptor = None
    for klass in metrics::MappingStatistic.__mro__:
        if "totalRecords" in klass.__dict__:
            descriptor = klass.__dict__["totalRecords"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingstatistic_has_intervalEstimate():
    assert hasattr(metrics::MappingStatistic, "intervalEstimate")
    descriptor = None
    for klass in metrics::MappingStatistic.__mro__:
        if "intervalEstimate" in klass.__dict__:
            descriptor = klass.__dict__["intervalEstimate"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mappingcolumn_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingColumn)


def test_metrics::mappingcolumn_constructor_exists():
    assert callable(metrics::MappingColumn.__init__)


def test_metrics::mappingcolumn_constructor_args():
    sig = inspect.signature(metrics::MappingColumn.__init__)
    params = list(sig.parameters.keys())
    assert "column" in params, "Missing parameter 'column'"

def test_metrics::mappingcolumn_has_column():
    assert hasattr(metrics::MappingColumn, "column")
    descriptor = None
    for klass in metrics::MappingColumn.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_metrics::metricsource_is_not_abstract():
    assert not inspect.isabstract(metrics::MetricSource)


def test_metrics::metricsource_constructor_exists():
    assert callable(metrics::MetricSource.__init__)


def test_metrics::metricsource_constructor_args():
    sig = inspect.signature(metrics::MetricSource.__init__)
    params = list(sig.parameters.keys())
    assert "metricLocation" in params, "Missing parameter 'metricLocation'"
    assert "filterPattern" in params, "Missing parameter 'filterPattern'"
    assert "name" in params, "Missing parameter 'name'"

def test_metrics::metricsource_has_metricLocation():
    assert hasattr(metrics::MetricSource, "metricLocation")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "metricLocation" in klass.__dict__:
            descriptor = klass.__dict__["metricLocation"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_filterPattern():
    assert hasattr(metrics::MetricSource, "filterPattern")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "filterPattern" in klass.__dict__:
            descriptor = klass.__dict__["filterPattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics::metricsource_has_name():
    assert hasattr(metrics::MetricSource, "name")
    descriptor = None
    for klass in metrics::MetricSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mappingrecord_is_not_abstract():
    assert not inspect.isabstract(metrics::MappingRecord)


def test_metrics::mappingrecord_constructor_exists():
    assert callable(metrics::MappingRecord.__init__)


def test_metrics::mappingrecord_constructor_args():
    sig = inspect.signature(metrics::MappingRecord.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"
    assert "count" in params, "Missing parameter 'count'"
    assert "column" in params, "Missing parameter 'column'"

def test_metrics::mappingrecord_has_message():
    assert hasattr(metrics::MappingRecord, "message")
    descriptor = None
    for klass in metrics::MappingRecord.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrecord_has_count():
    assert hasattr(metrics::MappingRecord, "count")
    descriptor = None
    for klass in metrics::MappingRecord.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mappingrecord_has_column():
    assert hasattr(metrics::MappingRecord, "column")
    descriptor = None
    for klass in metrics::MappingRecord.__mro__:
        if "column" in klass.__dict__:
            descriptor = klass.__dict__["column"]
            break
    assert isinstance(descriptor, property)



def test_metrics::mapping_is_not_abstract():
    assert not inspect.isabstract(metrics::Mapping)


def test_metrics::mapping_constructor_exists():
    assert callable(metrics::Mapping.__init__)


def test_metrics::mapping_constructor_args():
    sig = inspect.signature(metrics::Mapping.__init__)
    params = list(sig.parameters.keys())
    assert "headerRow" in params, "Missing parameter 'headerRow'"
    assert "intervalHint" in params, "Missing parameter 'intervalHint'"
    assert "firstDataRow" in params, "Missing parameter 'firstDataRow'"

def test_metrics::mapping_has_headerRow():
    assert hasattr(metrics::Mapping, "headerRow")
    descriptor = None
    for klass in metrics::Mapping.__mro__:
        if "headerRow" in klass.__dict__:
            descriptor = klass.__dict__["headerRow"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mapping_has_intervalHint():
    assert hasattr(metrics::Mapping, "intervalHint")
    descriptor = None
    for klass in metrics::Mapping.__mro__:
        if "intervalHint" in klass.__dict__:
            descriptor = klass.__dict__["intervalHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics::mapping_has_firstDataRow():
    assert hasattr(metrics::Mapping, "firstDataRow")
    descriptor = None
    for klass in metrics::Mapping.__mro__:
        if "firstDataRow" in klass.__dict__:
            descriptor = klass.__dict__["firstDataRow"]
            break
    assert isinstance(descriptor, property)



def test_datakind_is_not_abstract():
    assert not inspect.isabstract(DataKind)


def test_datakind_constructor_exists():
    assert callable(DataKind.__init__)


def test_datakind_constructor_args():
    sig = inspect.signature(DataKind.__init__)
    params = list(sig.parameters.keys())



def test_metrics::valuedatakind_is_not_abstract():
    assert not inspect.isabstract(metrics::ValueDataKind)


def test_metrics::valuedatakind_constructor_exists():
    assert callable(metrics::ValueDataKind.__init__)


def test_metrics::valuedatakind_constructor_args():
    sig = inspect.signature(metrics::ValueDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "valueKind" in params, "Missing parameter 'valueKind'"
    assert "kindHint" in params, "Missing parameter 'kindHint'"
    assert "format" in params, "Missing parameter 'format'"

def test_metrics::valuedatakind_has_valueKind():
    assert hasattr(metrics::ValueDataKind, "valueKind")
    descriptor = None
    for klass in metrics::ValueDataKind.__mro__:
        if "valueKind" in klass.__dict__:
            descriptor = klass.__dict__["valueKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics::valuedatakind_has_kindHint():
    assert hasattr(metrics::ValueDataKind, "kindHint")
    descriptor = None
    for klass in metrics::ValueDataKind.__mro__:
        if "kindHint" in klass.__dict__:
            descriptor = klass.__dict__["kindHint"]
            break
    assert isinstance(descriptor, property)

def test_metrics::valuedatakind_has_format():
    assert hasattr(metrics::ValueDataKind, "format")
    descriptor = None
    for klass in metrics::ValueDataKind.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_metrics::identifierdatakind_is_not_abstract():
    assert not inspect.isabstract(metrics::IdentifierDataKind)


def test_metrics::identifierdatakind_constructor_exists():
    assert callable(metrics::IdentifierDataKind.__init__)


def test_metrics::identifierdatakind_constructor_args():
    sig = inspect.signature(metrics::IdentifierDataKind.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "objectKind" in params, "Missing parameter 'objectKind'"
    assert "objectProperty" in params, "Missing parameter 'objectProperty'"

def test_metrics::identifierdatakind_has_pattern():
    assert hasattr(metrics::IdentifierDataKind, "pattern")
    descriptor = None
    for klass in metrics::IdentifierDataKind.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_metrics::identifierdatakind_has_objectKind():
    assert hasattr(metrics::IdentifierDataKind, "objectKind")
    descriptor = None
    for klass in metrics::IdentifierDataKind.__mro__:
        if "objectKind" in klass.__dict__:
            descriptor = klass.__dict__["objectKind"]
            break
    assert isinstance(descriptor, property)

def test_metrics::identifierdatakind_has_objectProperty():
    assert hasattr(metrics::IdentifierDataKind, "objectProperty")
    descriptor = None
    for klass in metrics::IdentifierDataKind.__mro__:
        if "objectProperty" in klass.__dict__:
            descriptor = klass.__dict__["objectProperty"]
            break
    assert isinstance(descriptor, property)



def test_metrics::datakind_is_not_abstract():
    assert not inspect.isabstract(metrics::DataKind)


def test_metrics::datakind_constructor_exists():
    assert callable(metrics::DataKind.__init__)


def test_metrics::datakind_constructor_args():
    sig = inspect.signature(metrics::DataKind.__init__)
    params = list(sig.parameters.keys())

def test_kindhinttype_exists():
    # Check that the Enumeration exists
    assert KindHintType is not None

def test_kindhinttype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in KindHintType]
    expected_literals = [
        "AVG",
        "BH",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in KindHintType"

def test_objectkindtype_exists():
    # Check that the Enumeration exists
    assert ObjectKindType is not None

def test_objectkindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectKindType]
    expected_literals = [
        "NODE",
        "RELATIONSHIP",
        "EQUIPMENT",
        "FUNCTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectKindType"

def test_metricretentionperiod_exists():
    # Check that the Enumeration exists
    assert MetricRetentionPeriod is not None

def test_metricretentionperiod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MetricRetentionPeriod]
    expected_literals = [
        "OneMonth",
        "OneYear",
        "OneWeek",
        "Always",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MetricRetentionPeriod"

def test_valuekindtype_exists():
    # Check that the Enumeration exists
    assert ValueKindType is not None

def test_valuekindtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueKindType]
    expected_literals = [
        "INTERVAL",
        "METRIC",
        "NULL",
        "DATETIME",
        "TIME",
        "DATE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueKindType"

def test_databasetypetype_exists():
    # Check that the Enumeration exists
    assert DatabaseTypeType is not None

def test_databasetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseTypeType]
    expected_literals = [
        "Postgres",
        "Oracle",
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
metrics::Value_strategy = st.builds(
    metrics::Value,
)
metrics::MetricValueRange_strategy = st.builds(
    metrics::MetricValueRange,
    kindHint=
        safe_text,
    intervalHint=
        safe_text
)
metrics::MetricRetentionRules_strategy = st.builds(
    metrics::MetricRetentionRules,
)
metrics::MetricRetentionRule_strategy = st.builds(
    metrics::MetricRetentionRule,
    intervalHint=
        safe_text,
    period=
        safe_text,
    name=
        safe_text
)
metrics::Unit_strategy = st.builds(
    metrics::Unit,
)
metrics::Expression_strategy = st.builds(
    metrics::Expression,
)
metrics::DateTimeRange_strategy = st.builds(
    metrics::DateTimeRange,
)
Mapping_strategy = st.builds(
    Mapping,
)
metrics::MappingRDBMS_strategy = st.builds(
    metrics::MappingRDBMS,
    password=
        safe_text,
    dateFormat=
        safe_text,
    timeFormat=
        safe_text,
    databaseType=
        safe_text,
    dateTimeFormat=
        safe_text,
    user=
        safe_text,
    query=
        safe_text
)
metrics::MappingXLS_strategy = st.builds(
    metrics::MappingXLS,
    filterPattern=
        safe_text,
    sheetNumber=
        safe_text
)
metrics::MappingCSV_strategy = st.builds(
    metrics::MappingCSV,
    delimiter=
        safe_text,
    filterPattern=
        safe_text
)
Base_strategy = st.builds(
    Base,
)
metrics::Metric_strategy = st.builds(
    metrics::Metric,
    measurementPoint=
        safe_text,
    measurementKind=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
metrics::MappingStatistic_strategy = st.builds(
    metrics::MappingStatistic,
    message=
        safe_text,
    totalRecords=
        safe_text,
    intervalEstimate=
        safe_text
)
metrics::MappingColumn_strategy = st.builds(
    metrics::MappingColumn,
    column=
        safe_text
)
metrics::MetricSource_strategy = st.builds(
    metrics::MetricSource,
    metricLocation=
        safe_text,
    filterPattern=
        safe_text,
    name=
        safe_text
)
metrics::MappingRecord_strategy = st.builds(
    metrics::MappingRecord,
    message=
        safe_text,
    count=
        safe_text,
    column=
        safe_text
)
metrics::Mapping_strategy = st.builds(
    metrics::Mapping,
    headerRow=
        safe_text,
    intervalHint=
        safe_text,
    firstDataRow=
        safe_text
)
DataKind_strategy = st.builds(
    DataKind,
)
metrics::ValueDataKind_strategy = st.builds(
    metrics::ValueDataKind,
    valueKind=
        safe_text,
    kindHint=
        safe_text,
    format=
        safe_text
)
metrics::IdentifierDataKind_strategy = st.builds(
    metrics::IdentifierDataKind,
    pattern=
        safe_text,
    objectKind=
        safe_text,
    objectProperty=
        safe_text
)
metrics::DataKind_strategy = st.builds(
    metrics::DataKind,
)

@given(instance=metrics::Value_strategy)
@settings(max_examples=50)
def test_metrics::value_instantiation(instance):
    assert isinstance(instance, metrics::Value)

@given(instance=metrics::MetricValueRange_strategy)
@settings(max_examples=50)
def test_metrics::metricvaluerange_instantiation(instance):
    assert isinstance(instance, metrics::MetricValueRange)

@given(instance=metrics::MetricValueRange_strategy)
def test_metrics::metricvaluerange_kindHint_type(instance):
    assert isinstance(instance.kindHint, str)


@given(instance=metrics::MetricValueRange_strategy)
def test_metrics::metricvaluerange_kindHint_setter(instance):
    original = instance.kindHint
    instance.kindHint = original
    assert instance.kindHint == original

@given(instance=metrics::MetricValueRange_strategy)
def test_metrics::metricvaluerange_intervalHint_type(instance):
    assert isinstance(instance.intervalHint, str)


@given(instance=metrics::MetricValueRange_strategy)
def test_metrics::metricvaluerange_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=metrics::MetricRetentionRules_strategy)
@settings(max_examples=50)
def test_metrics::metricretentionrules_instantiation(instance):
    assert isinstance(instance, metrics::MetricRetentionRules)

@given(instance=metrics::MetricRetentionRule_strategy)
@settings(max_examples=50)
def test_metrics::metricretentionrule_instantiation(instance):
    assert isinstance(instance, metrics::MetricRetentionRule)

@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_intervalHint_type(instance):
    assert isinstance(instance.intervalHint, str)


@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_period_type(instance):
    assert isinstance(instance.period, str)


@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_period_setter(instance):
    original = instance.period
    instance.period = original
    assert instance.period == original

@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricRetentionRule_strategy)
def test_metrics::metricretentionrule_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::Unit_strategy)
@settings(max_examples=50)
def test_metrics::unit_instantiation(instance):
    assert isinstance(instance, metrics::Unit)

@given(instance=metrics::Expression_strategy)
@settings(max_examples=50)
def test_metrics::expression_instantiation(instance):
    assert isinstance(instance, metrics::Expression)

@given(instance=metrics::DateTimeRange_strategy)
@settings(max_examples=50)
def test_metrics::datetimerange_instantiation(instance):
    assert isinstance(instance, metrics::DateTimeRange)

@given(instance=Mapping_strategy)
@settings(max_examples=50)
def test_mapping_instantiation(instance):
    assert isinstance(instance, Mapping)

@given(instance=metrics::MappingRDBMS_strategy)
@settings(max_examples=50)
def test_metrics::mappingrdbms_instantiation(instance):
    assert isinstance(instance, metrics::MappingRDBMS)

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_dateFormat_type(instance):
    assert isinstance(instance.dateFormat, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_dateFormat_setter(instance):
    original = instance.dateFormat
    instance.dateFormat = original
    assert instance.dateFormat == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_timeFormat_type(instance):
    assert isinstance(instance.timeFormat, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_timeFormat_setter(instance):
    original = instance.timeFormat
    instance.timeFormat = original
    assert instance.timeFormat == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_databaseType_type(instance):
    assert isinstance(instance.databaseType, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_databaseType_setter(instance):
    original = instance.databaseType
    instance.databaseType = original
    assert instance.databaseType == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_dateTimeFormat_type(instance):
    assert isinstance(instance.dateTimeFormat, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_dateTimeFormat_setter(instance):
    original = instance.dateTimeFormat
    instance.dateTimeFormat = original
    assert instance.dateTimeFormat == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_user_type(instance):
    assert isinstance(instance.user, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_query_type(instance):
    assert isinstance(instance.query, str)


@given(instance=metrics::MappingRDBMS_strategy)
def test_metrics::mappingrdbms_query_setter(instance):
    original = instance.query
    instance.query = original
    assert instance.query == original

@given(instance=metrics::MappingXLS_strategy)
@settings(max_examples=50)
def test_metrics::mappingxls_instantiation(instance):
    assert isinstance(instance, metrics::MappingXLS)

@given(instance=metrics::MappingXLS_strategy)
def test_metrics::mappingxls_filterPattern_type(instance):
    assert isinstance(instance.filterPattern, str)


@given(instance=metrics::MappingXLS_strategy)
def test_metrics::mappingxls_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original

@given(instance=metrics::MappingXLS_strategy)
def test_metrics::mappingxls_sheetNumber_type(instance):
    assert isinstance(instance.sheetNumber, str)


@given(instance=metrics::MappingXLS_strategy)
def test_metrics::mappingxls_sheetNumber_setter(instance):
    original = instance.sheetNumber
    instance.sheetNumber = original
    assert instance.sheetNumber == original

@given(instance=metrics::MappingCSV_strategy)
@settings(max_examples=50)
def test_metrics::mappingcsv_instantiation(instance):
    assert isinstance(instance, metrics::MappingCSV)

@given(instance=metrics::MappingCSV_strategy)
def test_metrics::mappingcsv_delimiter_type(instance):
    assert isinstance(instance.delimiter, str)


@given(instance=metrics::MappingCSV_strategy)
def test_metrics::mappingcsv_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original

@given(instance=metrics::MappingCSV_strategy)
def test_metrics::mappingcsv_filterPattern_type(instance):
    assert isinstance(instance.filterPattern, str)


@given(instance=metrics::MappingCSV_strategy)
def test_metrics::mappingcsv_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=metrics::Metric_strategy)
@settings(max_examples=50)
def test_metrics::metric_instantiation(instance):
    assert isinstance(instance, metrics::Metric)

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_measurementPoint_type(instance):
    assert isinstance(instance.measurementPoint, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_measurementPoint_setter(instance):
    original = instance.measurementPoint
    instance.measurementPoint = original
    assert instance.measurementPoint == original

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_measurementKind_type(instance):
    assert isinstance(instance.measurementKind, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_measurementKind_setter(instance):
    original = instance.measurementKind
    instance.measurementKind = original
    assert instance.measurementKind == original

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::Metric_strategy)
def test_metrics::metric_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=metrics::Metric_strategy)
def test_metrics::metric_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=metrics::MappingStatistic_strategy)
@settings(max_examples=50)
def test_metrics::mappingstatistic_instantiation(instance):
    assert isinstance(instance, metrics::MappingStatistic)

@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_totalRecords_type(instance):
    assert isinstance(instance.totalRecords, str)


@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_totalRecords_setter(instance):
    original = instance.totalRecords
    instance.totalRecords = original
    assert instance.totalRecords == original

@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_intervalEstimate_type(instance):
    assert isinstance(instance.intervalEstimate, str)


@given(instance=metrics::MappingStatistic_strategy)
def test_metrics::mappingstatistic_intervalEstimate_setter(instance):
    original = instance.intervalEstimate
    instance.intervalEstimate = original
    assert instance.intervalEstimate == original

@given(instance=metrics::MappingColumn_strategy)
@settings(max_examples=50)
def test_metrics::mappingcolumn_instantiation(instance):
    assert isinstance(instance, metrics::MappingColumn)

@given(instance=metrics::MappingColumn_strategy)
def test_metrics::mappingcolumn_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=metrics::MappingColumn_strategy)
def test_metrics::mappingcolumn_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=metrics::MetricSource_strategy)
@settings(max_examples=50)
def test_metrics::metricsource_instantiation(instance):
    assert isinstance(instance, metrics::MetricSource)

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metricLocation_type(instance):
    assert isinstance(instance.metricLocation, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_metricLocation_setter(instance):
    original = instance.metricLocation
    instance.metricLocation = original
    assert instance.metricLocation == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_filterPattern_type(instance):
    assert isinstance(instance.filterPattern, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_filterPattern_setter(instance):
    original = instance.filterPattern
    instance.filterPattern = original
    assert instance.filterPattern == original

@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=metrics::MetricSource_strategy)
def test_metrics::metricsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=metrics::MappingRecord_strategy)
@settings(max_examples=50)
def test_metrics::mappingrecord_instantiation(instance):
    assert isinstance(instance, metrics::MappingRecord)

@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_message_type(instance):
    assert isinstance(instance.message, str)


@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_count_type(instance):
    assert isinstance(instance.count, str)


@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_column_type(instance):
    assert isinstance(instance.column, str)


@given(instance=metrics::MappingRecord_strategy)
def test_metrics::mappingrecord_column_setter(instance):
    original = instance.column
    instance.column = original
    assert instance.column == original

@given(instance=metrics::Mapping_strategy)
@settings(max_examples=50)
def test_metrics::mapping_instantiation(instance):
    assert isinstance(instance, metrics::Mapping)

@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_headerRow_type(instance):
    assert isinstance(instance.headerRow, str)


@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_headerRow_setter(instance):
    original = instance.headerRow
    instance.headerRow = original
    assert instance.headerRow == original

@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_intervalHint_type(instance):
    assert isinstance(instance.intervalHint, str)


@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_intervalHint_setter(instance):
    original = instance.intervalHint
    instance.intervalHint = original
    assert instance.intervalHint == original

@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_firstDataRow_type(instance):
    assert isinstance(instance.firstDataRow, str)


@given(instance=metrics::Mapping_strategy)
def test_metrics::mapping_firstDataRow_setter(instance):
    original = instance.firstDataRow
    instance.firstDataRow = original
    assert instance.firstDataRow == original

@given(instance=DataKind_strategy)
@settings(max_examples=50)
def test_datakind_instantiation(instance):
    assert isinstance(instance, DataKind)

@given(instance=metrics::ValueDataKind_strategy)
@settings(max_examples=50)
def test_metrics::valuedatakind_instantiation(instance):
    assert isinstance(instance, metrics::ValueDataKind)

@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_valueKind_type(instance):
    assert isinstance(instance.valueKind, str)


@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_valueKind_setter(instance):
    original = instance.valueKind
    instance.valueKind = original
    assert instance.valueKind == original

@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_kindHint_type(instance):
    assert isinstance(instance.kindHint, str)


@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_kindHint_setter(instance):
    original = instance.kindHint
    instance.kindHint = original
    assert instance.kindHint == original

@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=metrics::ValueDataKind_strategy)
def test_metrics::valuedatakind_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=metrics::IdentifierDataKind_strategy)
@settings(max_examples=50)
def test_metrics::identifierdatakind_instantiation(instance):
    assert isinstance(instance, metrics::IdentifierDataKind)

@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_objectKind_type(instance):
    assert isinstance(instance.objectKind, str)


@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_objectKind_setter(instance):
    original = instance.objectKind
    instance.objectKind = original
    assert instance.objectKind == original

@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_objectProperty_type(instance):
    assert isinstance(instance.objectProperty, str)


@given(instance=metrics::IdentifierDataKind_strategy)
def test_metrics::identifierdatakind_objectProperty_setter(instance):
    original = instance.objectProperty
    instance.objectProperty = original
    assert instance.objectProperty == original

@given(instance=metrics::DataKind_strategy)
@settings(max_examples=50)
def test_metrics::datakind_instantiation(instance):
    assert isinstance(instance, metrics::DataKind)
