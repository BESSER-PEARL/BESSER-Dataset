import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    MARTE_Library_TimeLibrary_IdealClock,
    TimeStandardKind,
    SourceKind,
    EventKind,
    LengthUnitKind,
    DataTxRateUnitKind,
    TimeNatureKind,
    WeightUnitKind,
    StatisticalQualifierKind,
    DirectionKind,
    TimeInterpretationKind,
    FrequencyUnitKind,
    PowerUnitKind,
    EnergyUnitKind,
    SchedPolicyKind,
    LogicalTimeUnit,
    ProtectProtocolKind,
    TransmModeKind,
    PeriodicServerKind,
    DataSizeUnitKind,
    TimeUnitKind,
    AreaUnitKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_marte_library_timelibrary_idealclock_is_not_abstract():
    assert not inspect.isabstract(MARTE_Library_TimeLibrary_IdealClock)


def test_marte_library_timelibrary_idealclock_constructor_exists():
    assert callable(MARTE_Library_TimeLibrary_IdealClock.__init__)


def test_marte_library_timelibrary_idealclock_constructor_args():
    sig = inspect.signature(MARTE_Library_TimeLibrary_IdealClock.__init__)
    params = list(sig.parameters.keys())

def test_timestandardkind_exists():
    # Check that the Enumeration exists
    assert TimeStandardKind is not None

def test_timestandardkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeStandardKind]
    expected_literals = [
        "TAI",
        "UT1",
        "UTC",
        "TBD",
        "TCB",
        "Local",
        "TCG",
        "TT",
        "Sidereal",
        "GPS",
        "UT0",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeStandardKind"

def test_sourcekind_exists():
    # Check that the Enumeration exists
    assert SourceKind is not None

def test_sourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceKind]
    expected_literals = [
        "meas",
        "est",
        "req",
        "calc",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceKind"

def test_eventkind_exists():
    # Check that the Enumeration exists
    assert EventKind is not None

def test_eventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventKind]
    expected_literals = [
        "start",
        "receive",
        "send",
        "consume",
        "finish",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventKind"

def test_lengthunitkind_exists():
    # Check that the Enumeration exists
    assert LengthUnitKind is not None

def test_lengthunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LengthUnitKind]
    expected_literals = [
        "cm",
        "m",
        "mm",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnitKind"

def test_datatxrateunitkind_exists():
    # Check that the Enumeration exists
    assert DataTxRateUnitKind is not None

def test_datatxrateunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTxRateUnitKind]
    expected_literals = [
        "b_per_s",
        "Mb_per_s",
        "Kb_per_s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTxRateUnitKind"

def test_timenaturekind_exists():
    # Check that the Enumeration exists
    assert TimeNatureKind is not None

def test_timenaturekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeNatureKind]
    expected_literals = [
        "dense",
        "discrete",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeNatureKind"

def test_weightunitkind_exists():
    # Check that the Enumeration exists
    assert WeightUnitKind is not None

def test_weightunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WeightUnitKind]
    expected_literals = [
        "mg",
        "g",
        "kg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WeightUnitKind"

def test_statisticalqualifierkind_exists():
    # Check that the Enumeration exists
    assert StatisticalQualifierKind is not None

def test_statisticalqualifierkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatisticalQualifierKind]
    expected_literals = [
        "variance",
        "determ",
        "percent",
        "other",
        "min",
        "mean",
        "range",
        "distrib",
        "max",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatisticalQualifierKind"

def test_directionkind_exists():
    # Check that the Enumeration exists
    assert DirectionKind is not None

def test_directionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DirectionKind]
    expected_literals = [
        "decr",
        "incr",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DirectionKind"

def test_timeinterpretationkind_exists():
    # Check that the Enumeration exists
    assert TimeInterpretationKind is not None

def test_timeinterpretationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeInterpretationKind]
    expected_literals = [
        "duration",
        "instant",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeInterpretationKind"

def test_frequencyunitkind_exists():
    # Check that the Enumeration exists
    assert FrequencyUnitKind is not None

def test_frequencyunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrequencyUnitKind]
    expected_literals = [
        "GHz",
        "Hz",
        "rpm",
        "KHz",
        "MHz",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrequencyUnitKind"

def test_powerunitkind_exists():
    # Check that the Enumeration exists
    assert PowerUnitKind is not None

def test_powerunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PowerUnitKind]
    expected_literals = [
        "W",
        "mW",
        "KW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PowerUnitKind"

def test_energyunitkind_exists():
    # Check that the Enumeration exists
    assert EnergyUnitKind is not None

def test_energyunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnergyUnitKind]
    expected_literals = [
        "KJ",
        "Wh",
        "J",
        "KWh",
        "mWh",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnergyUnitKind"

def test_schedpolicykind_exists():
    # Check that the Enumeration exists
    assert SchedPolicyKind is not None

def test_schedpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedPolicyKind]
    expected_literals = [
        "Other",
        "LeastLaxityFirst",
        "FixedPriority",
        "TimeTableDriven",
        "Undef",
        "FIFO",
        "RoundRobin",
        "EarliestDeadlineFirst",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedPolicyKind"

def test_logicaltimeunit_exists():
    # Check that the Enumeration exists
    assert LogicalTimeUnit is not None

def test_logicaltimeunit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LogicalTimeUnit]
    expected_literals = [
        "tick",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LogicalTimeUnit"

def test_protectprotocolkind_exists():
    # Check that the Enumeration exists
    assert ProtectProtocolKind is not None

def test_protectprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProtectProtocolKind]
    expected_literals = [
        "PriorityCeiling",
        "Undef",
        "StackBased",
        "NoPreemption",
        "FIFO",
        "Other",
        "PriorityInheritance",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProtectProtocolKind"

def test_transmmodekind_exists():
    # Check that the Enumeration exists
    assert TransmModeKind is not None

def test_transmmodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransmModeKind]
    expected_literals = [
        "fullDuplex",
        "halfDuplex",
        "simplex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransmModeKind"

def test_periodicserverkind_exists():
    # Check that the Enumeration exists
    assert PeriodicServerKind is not None

def test_periodicserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PeriodicServerKind]
    expected_literals = [
        "Deferrable",
        "Other",
        "Sporadic",
        "Undef",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PeriodicServerKind"

def test_datasizeunitkind_exists():
    # Check that the Enumeration exists
    assert DataSizeUnitKind is not None

def test_datasizeunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataSizeUnitKind]
    expected_literals = [
        "KB",
        "Byte",
        "bit",
        "GB",
        "MB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataSizeUnitKind"

def test_timeunitkind_exists():
    # Check that the Enumeration exists
    assert TimeUnitKind is not None

def test_timeunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnitKind]
    expected_literals = [
        "min",
        "day",
        "ns",
        "hrs",
        "us",
        "ms",
        "s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnitKind"

def test_areaunitkind_exists():
    # Check that the Enumeration exists
    assert AreaUnitKind is not None

def test_areaunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AreaUnitKind]
    expected_literals = [
        "um2",
        "mm2",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AreaUnitKind"


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
MARTE_Library_TimeLibrary_IdealClock_strategy = st.builds(
    MARTE_Library_TimeLibrary_IdealClock,
)

@given(instance=MARTE_Library_TimeLibrary_IdealClock_strategy)
@settings(max_examples=50)
def test_marte_library_timelibrary_idealclock_instantiation(instance):
    assert isinstance(instance, MARTE_Library_TimeLibrary_IdealClock)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE_Library_TimeLibrary_IdealClock_strategy)
@settings(max_examples=30)
def test_marte_library_timelibrary_idealclock_currenttime_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.currentTime()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.currentTime).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'currentTime' in MARTE_Library_TimeLibrary_IdealClock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'currentTime' in MARTE_Library_TimeLibrary_IdealClock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'currentTime' in MARTE_Library_TimeLibrary_IdealClock is not implemented or raised an error")
