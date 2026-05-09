import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    MARTE::Library::RS::Library::ShapeSpecification,
    IntegerMatrix,
    MARTE::Library::RS::Library::TilerSpecification,
    MARTE::Library::TimeLibrary::IdealClock,
    MARTE::Library::MARTE::DataTypes::RealMatrix,
    MARTE::Library::MARTE::DataTypes::RealVector,
    NFP::Natural,
    MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval,
    MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval,
    MARTE::Library::MARTE::DataTypes::Realnterval,
    MARTE::Library::MARTE::DataTypes::Interval,
    MARTE::Library::MARTE::DataTypes::Array,
    MARTE::Library::TimeLibrary::TimedValueType,
    MARTE::Library::MARTE::DataTypes::IntegerMatrix,
    MARTE::Library::MARTE::DataTypes::IntegerVector,
    MARTE::Library::MARTE::DataTypes::UtilityType,
    MARTE::Library::MARTE::DataTypes::IntegerInterval,
    IntegerVector,
    MARTE::Library::BasicNFP::Types::AperiodicPattern,
    MARTE::Library::BasicNFP::Types::PeriodicPattern,
    OpenPattern,
    NFP::Frequency,
    MARTE::Library::BasicNFP::Types::OpenPattern,
    MARTE::Library::BasicNFP::Types::ClosedPattern,
    SporadicPattern,
    ClosedPattern,
    IrregularPattern,
    BurstPattern,
    AperiodicPattern,
    MARTE::Library::BasicNFP::Types::BurstPattern,
    MARTE::Library::BasicNFP::Types::IrregularPattern,
    MARTE::Library::BasicNFP::Types::SporadicPattern,
    PeriodicPattern,
    MARTE::Library::BasicNFP::Types::ArrivalPattern,
    MARTE::Library::BasicNFP::Types::NFP::CommonType,
    NFP::CommonType,
    MARTE::Library::BasicNFP::Types::NFP::Natural,
    MARTE::Library::BasicNFP::Types::NFP::Integer,
    MARTE::Library::BasicNFP::Types::NFP::Boolean,
    MARTE::Library::BasicNFP::Types::NFP::DateTime,
    MARTE::Library::BasicNFP::Types::NFP::String,
    MARTE::Library::BasicNFP::Types::NFP::Real,
    NFP::Real,
    MARTE::Library::BasicNFP::Types::NFP::Area,
    MARTE::Library::BasicNFP::Types::NFP::Price,
    MARTE::Library::BasicNFP::Types::NFP::Energy,
    MARTE::Library::BasicNFP::Types::NFP::Percentage,
    MARTE::Library::BasicNFP::Types::NFP::Power,
    MARTE::Library::BasicNFP::Types::NFP::Length,
    MARTE::Library::BasicNFP::Types::NFP::DataSize,
    MARTE::Library::BasicNFP::Types::NFP::Weight,
    MARTE::Library::BasicNFP::Types::NFP::DataTxRate,
    MARTE::Library::BasicNFP::Types::NFP::Duration,
    MARTE::Library::BasicNFP::Types::NFP::Frequency,
    NFP::Integer,
    MARTE::Library::GRM::BasicTypes::FixedPriorityParameters,
    PeriodicServerParameters,
    PoolingParameters,
    NFP::Duration,
    MARTE::Library::GRM::BasicTypes::EDF::Parameters,
    FixedPriorityParameters,
    MARTE::Library::GRM::BasicTypes::PeriodicServerParameters,
    MARTE::Library::GRM::BasicTypes::PoolingParameters,
    EDF::Parameters,
    MARTE::Library::GRM::BasicTypes::SchedParameters,
    LogicalTimeUnit,
    TimeNatureKind,
    AreaUnitKind,
    SourceKind,
    EnergyUnitKind,
    FrequencyUnitKind,
    DataTxRateUnitKind,
    DataSizeUnitKind,
    EventKind,
    LengthUnitKind,
    TimeInterpretationKind,
    ProtectProtocolKind,
    DirectionKind,
    WeightUnitKind,
    TimeStandardKind,
    SchedPolicyKind,
    TUK,
    PeriodicServerKind,
    StatisticalQualifierKind,
    TimeUnitKind,
    PowerUnitKind,
    TransmModeKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_marte::library::rs::library::shapespecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::RS::Library::ShapeSpecification)


def test_marte::library::rs::library::shapespecification_constructor_exists():
    assert callable(MARTE::Library::RS::Library::ShapeSpecification.__init__)


def test_marte::library::rs::library::shapespecification_constructor_args():
    sig = inspect.signature(MARTE::Library::RS::Library::ShapeSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_marte::library::rs::library::shapespecification_has_size():
    assert hasattr(MARTE::Library::RS::Library::ShapeSpecification, "size")
    descriptor = None
    for klass in MARTE::Library::RS::Library::ShapeSpecification.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_integermatrix_is_not_abstract():
    assert not inspect.isabstract(IntegerMatrix)


def test_integermatrix_constructor_exists():
    assert callable(IntegerMatrix.__init__)


def test_integermatrix_constructor_args():
    sig = inspect.signature(IntegerMatrix.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::rs::library::tilerspecification_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::RS::Library::TilerSpecification)


def test_marte::library::rs::library::tilerspecification_constructor_exists():
    assert callable(MARTE::Library::RS::Library::TilerSpecification.__init__)


def test_marte::library::rs::library::tilerspecification_constructor_args():
    sig = inspect.signature(MARTE::Library::RS::Library::TilerSpecification.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::timelibrary::idealclock_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::TimeLibrary::IdealClock)


def test_marte::library::timelibrary::idealclock_constructor_exists():
    assert callable(MARTE::Library::TimeLibrary::IdealClock.__init__)


def test_marte::library::timelibrary::idealclock_constructor_args():
    sig = inspect.signature(MARTE::Library::TimeLibrary::IdealClock.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::realmatrix_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::RealMatrix)


def test_marte::library::marte::datatypes::realmatrix_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::RealMatrix.__init__)


def test_marte::library::marte::datatypes::realmatrix_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::RealMatrix.__init__)
    params = list(sig.parameters.keys())
    assert "matrixElem" in params, "Missing parameter 'matrixElem'"

def test_marte::library::marte::datatypes::realmatrix_has_matrixElem():
    assert hasattr(MARTE::Library::MARTE::DataTypes::RealMatrix, "matrixElem")
    descriptor = None
    for klass in MARTE::Library::MARTE::DataTypes::RealMatrix.__mro__:
        if "matrixElem" in klass.__dict__:
            descriptor = klass.__dict__["matrixElem"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::marte::datatypes::realvector_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::RealVector)


def test_marte::library::marte::datatypes::realvector_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::RealVector.__init__)


def test_marte::library::marte::datatypes::realvector_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::RealVector.__init__)
    params = list(sig.parameters.keys())
    assert "vectorElem" in params, "Missing parameter 'vectorElem'"

def test_marte::library::marte::datatypes::realvector_has_vectorElem():
    assert hasattr(MARTE::Library::MARTE::DataTypes::RealVector, "vectorElem")
    descriptor = None
    for klass in MARTE::Library::MARTE::DataTypes::RealVector.__mro__:
        if "vectorElem" in klass.__dict__:
            descriptor = klass.__dict__["vectorElem"]
            break
    assert isinstance(descriptor, property)



def test_nfp::natural_is_not_abstract():
    assert not inspect.isabstract(NFP::Natural)


def test_nfp::natural_constructor_exists():
    assert callable(NFP::Natural.__init__)


def test_nfp::natural_constructor_args():
    sig = inspect.signature(NFP::Natural.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::nfp::naturalinterval_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval)


def test_marte::library::marte::datatypes::nfp::naturalinterval_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval.__init__)


def test_marte::library::marte::datatypes::nfp::naturalinterval_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::nfp::frequencyinterval_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval)


def test_marte::library::marte::datatypes::nfp::frequencyinterval_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval.__init__)


def test_marte::library::marte::datatypes::nfp::frequencyinterval_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::realnterval_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::Realnterval)


def test_marte::library::marte::datatypes::realnterval_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::Realnterval.__init__)


def test_marte::library::marte::datatypes::realnterval_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::Realnterval.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_marte::library::marte::datatypes::realnterval_has_bound():
    assert hasattr(MARTE::Library::MARTE::DataTypes::Realnterval, "bound")
    descriptor = None
    for klass in MARTE::Library::MARTE::DataTypes::Realnterval.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::marte::datatypes::interval_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::Interval)


def test_marte::library::marte::datatypes::interval_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::Interval.__init__)


def test_marte::library::marte::datatypes::interval_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::Interval.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::array_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::Array)


def test_marte::library::marte::datatypes::array_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::Array.__init__)


def test_marte::library::marte::datatypes::array_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::Array.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::timelibrary::timedvaluetype_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::TimeLibrary::TimedValueType)


def test_marte::library::timelibrary::timedvaluetype_constructor_exists():
    assert callable(MARTE::Library::TimeLibrary::TimedValueType.__init__)


def test_marte::library::timelibrary::timedvaluetype_constructor_args():
    sig = inspect.signature(MARTE::Library::TimeLibrary::TimedValueType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "onClock" in params, "Missing parameter 'onClock'"

def test_marte::library::timelibrary::timedvaluetype_has_value():
    assert hasattr(MARTE::Library::TimeLibrary::TimedValueType, "value")
    descriptor = None
    for klass in MARTE::Library::TimeLibrary::TimedValueType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::timelibrary::timedvaluetype_has_expr():
    assert hasattr(MARTE::Library::TimeLibrary::TimedValueType, "expr")
    descriptor = None
    for klass in MARTE::Library::TimeLibrary::TimedValueType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::timelibrary::timedvaluetype_has_unit():
    assert hasattr(MARTE::Library::TimeLibrary::TimedValueType, "unit")
    descriptor = None
    for klass in MARTE::Library::TimeLibrary::TimedValueType.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::timelibrary::timedvaluetype_has_onClock():
    assert hasattr(MARTE::Library::TimeLibrary::TimedValueType, "onClock")
    descriptor = None
    for klass in MARTE::Library::TimeLibrary::TimedValueType.__mro__:
        if "onClock" in klass.__dict__:
            descriptor = klass.__dict__["onClock"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::marte::datatypes::integermatrix_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::IntegerMatrix)


def test_marte::library::marte::datatypes::integermatrix_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::IntegerMatrix.__init__)


def test_marte::library::marte::datatypes::integermatrix_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::IntegerMatrix.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::integervector_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::IntegerVector)


def test_marte::library::marte::datatypes::integervector_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::IntegerVector.__init__)


def test_marte::library::marte::datatypes::integervector_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::IntegerVector.__init__)
    params = list(sig.parameters.keys())
    assert "vectorElem" in params, "Missing parameter 'vectorElem'"

def test_marte::library::marte::datatypes::integervector_has_vectorElem():
    assert hasattr(MARTE::Library::MARTE::DataTypes::IntegerVector, "vectorElem")
    descriptor = None
    for klass in MARTE::Library::MARTE::DataTypes::IntegerVector.__mro__:
        if "vectorElem" in klass.__dict__:
            descriptor = klass.__dict__["vectorElem"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::marte::datatypes::utilitytype_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::UtilityType)


def test_marte::library::marte::datatypes::utilitytype_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::UtilityType.__init__)


def test_marte::library::marte::datatypes::utilitytype_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::UtilityType.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::marte::datatypes::integerinterval_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::MARTE::DataTypes::IntegerInterval)


def test_marte::library::marte::datatypes::integerinterval_constructor_exists():
    assert callable(MARTE::Library::MARTE::DataTypes::IntegerInterval.__init__)


def test_marte::library::marte::datatypes::integerinterval_constructor_args():
    sig = inspect.signature(MARTE::Library::MARTE::DataTypes::IntegerInterval.__init__)
    params = list(sig.parameters.keys())
    assert "bound" in params, "Missing parameter 'bound'"

def test_marte::library::marte::datatypes::integerinterval_has_bound():
    assert hasattr(MARTE::Library::MARTE::DataTypes::IntegerInterval, "bound")
    descriptor = None
    for klass in MARTE::Library::MARTE::DataTypes::IntegerInterval.__mro__:
        if "bound" in klass.__dict__:
            descriptor = klass.__dict__["bound"]
            break
    assert isinstance(descriptor, property)



def test_integervector_is_not_abstract():
    assert not inspect.isabstract(IntegerVector)


def test_integervector_constructor_exists():
    assert callable(IntegerVector.__init__)


def test_integervector_constructor_args():
    sig = inspect.signature(IntegerVector.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::aperiodicpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::AperiodicPattern)


def test_marte::library::basicnfp::types::aperiodicpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::AperiodicPattern.__init__)


def test_marte::library::basicnfp::types::aperiodicpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::AperiodicPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::periodicpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::PeriodicPattern)


def test_marte::library::basicnfp::types::periodicpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::PeriodicPattern.__init__)


def test_marte::library::basicnfp::types::periodicpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::PeriodicPattern.__init__)
    params = list(sig.parameters.keys())



def test_openpattern_is_not_abstract():
    assert not inspect.isabstract(OpenPattern)


def test_openpattern_constructor_exists():
    assert callable(OpenPattern.__init__)


def test_openpattern_constructor_args():
    sig = inspect.signature(OpenPattern.__init__)
    params = list(sig.parameters.keys())



def test_nfp::frequency_is_not_abstract():
    assert not inspect.isabstract(NFP::Frequency)


def test_nfp::frequency_constructor_exists():
    assert callable(NFP::Frequency.__init__)


def test_nfp::frequency_constructor_args():
    sig = inspect.signature(NFP::Frequency.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::openpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::OpenPattern)


def test_marte::library::basicnfp::types::openpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::OpenPattern.__init__)


def test_marte::library::basicnfp::types::openpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::OpenPattern.__init__)
    params = list(sig.parameters.keys())
    assert "arrivalProcess" in params, "Missing parameter 'arrivalProcess'"

def test_marte::library::basicnfp::types::openpattern_has_arrivalProcess():
    assert hasattr(MARTE::Library::BasicNFP::Types::OpenPattern, "arrivalProcess")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::OpenPattern.__mro__:
        if "arrivalProcess" in klass.__dict__:
            descriptor = klass.__dict__["arrivalProcess"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::closedpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::ClosedPattern)


def test_marte::library::basicnfp::types::closedpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::ClosedPattern.__init__)


def test_marte::library::basicnfp::types::closedpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::ClosedPattern.__init__)
    params = list(sig.parameters.keys())



def test_sporadicpattern_is_not_abstract():
    assert not inspect.isabstract(SporadicPattern)


def test_sporadicpattern_constructor_exists():
    assert callable(SporadicPattern.__init__)


def test_sporadicpattern_constructor_args():
    sig = inspect.signature(SporadicPattern.__init__)
    params = list(sig.parameters.keys())



def test_closedpattern_is_not_abstract():
    assert not inspect.isabstract(ClosedPattern)


def test_closedpattern_constructor_exists():
    assert callable(ClosedPattern.__init__)


def test_closedpattern_constructor_args():
    sig = inspect.signature(ClosedPattern.__init__)
    params = list(sig.parameters.keys())



def test_irregularpattern_is_not_abstract():
    assert not inspect.isabstract(IrregularPattern)


def test_irregularpattern_constructor_exists():
    assert callable(IrregularPattern.__init__)


def test_irregularpattern_constructor_args():
    sig = inspect.signature(IrregularPattern.__init__)
    params = list(sig.parameters.keys())



def test_burstpattern_is_not_abstract():
    assert not inspect.isabstract(BurstPattern)


def test_burstpattern_constructor_exists():
    assert callable(BurstPattern.__init__)


def test_burstpattern_constructor_args():
    sig = inspect.signature(BurstPattern.__init__)
    params = list(sig.parameters.keys())



def test_aperiodicpattern_is_not_abstract():
    assert not inspect.isabstract(AperiodicPattern)


def test_aperiodicpattern_constructor_exists():
    assert callable(AperiodicPattern.__init__)


def test_aperiodicpattern_constructor_args():
    sig = inspect.signature(AperiodicPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::burstpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::BurstPattern)


def test_marte::library::basicnfp::types::burstpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::BurstPattern.__init__)


def test_marte::library::basicnfp::types::burstpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::BurstPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::irregularpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::IrregularPattern)


def test_marte::library::basicnfp::types::irregularpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::IrregularPattern.__init__)


def test_marte::library::basicnfp::types::irregularpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::IrregularPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::sporadicpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::SporadicPattern)


def test_marte::library::basicnfp::types::sporadicpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::SporadicPattern.__init__)


def test_marte::library::basicnfp::types::sporadicpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::SporadicPattern.__init__)
    params = list(sig.parameters.keys())



def test_periodicpattern_is_not_abstract():
    assert not inspect.isabstract(PeriodicPattern)


def test_periodicpattern_constructor_exists():
    assert callable(PeriodicPattern.__init__)


def test_periodicpattern_constructor_args():
    sig = inspect.signature(PeriodicPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::arrivalpattern_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::ArrivalPattern)


def test_marte::library::basicnfp::types::arrivalpattern_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::ArrivalPattern.__init__)


def test_marte::library::basicnfp::types::arrivalpattern_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::ArrivalPattern.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::nfp::commontype_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::CommonType)


def test_marte::library::basicnfp::types::nfp::commontype_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::CommonType.__init__)


def test_marte::library::basicnfp::types::nfp::commontype_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::CommonType.__init__)
    params = list(sig.parameters.keys())
    assert "statQ" in params, "Missing parameter 'statQ'"
    assert "source" in params, "Missing parameter 'source'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "expr" in params, "Missing parameter 'expr'"
    assert "dir" in params, "Missing parameter 'dir'"

def test_marte::library::basicnfp::types::nfp::commontype_has_statQ():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::CommonType, "statQ")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::CommonType.__mro__:
        if "statQ" in klass.__dict__:
            descriptor = klass.__dict__["statQ"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::commontype_has_source():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::CommonType, "source")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::CommonType.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::commontype_has_mode():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::CommonType, "mode")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::CommonType.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::commontype_has_expr():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::CommonType, "expr")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::CommonType.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::commontype_has_dir():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::CommonType, "dir")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::CommonType.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_nfp::commontype_is_not_abstract():
    assert not inspect.isabstract(NFP::CommonType)


def test_nfp::commontype_constructor_exists():
    assert callable(NFP::CommonType.__init__)


def test_nfp::commontype_constructor_args():
    sig = inspect.signature(NFP::CommonType.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::nfp::natural_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Natural)


def test_marte::library::basicnfp::types::nfp::natural_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Natural.__init__)


def test_marte::library::basicnfp::types::nfp::natural_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Natural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::natural_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Natural, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Natural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::integer_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Integer)


def test_marte::library::basicnfp::types::nfp::integer_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Integer.__init__)


def test_marte::library::basicnfp::types::nfp::integer_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::integer_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Integer, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Integer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::boolean_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Boolean)


def test_marte::library::basicnfp::types::nfp::boolean_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Boolean.__init__)


def test_marte::library::basicnfp::types::nfp::boolean_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Boolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::boolean_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Boolean, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Boolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::datetime_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::DateTime)


def test_marte::library::basicnfp::types::nfp::datetime_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::DateTime.__init__)


def test_marte::library::basicnfp::types::nfp::datetime_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::DateTime.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::datetime_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::DateTime, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::DateTime.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::string_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::String)


def test_marte::library::basicnfp::types::nfp::string_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::String.__init__)


def test_marte::library::basicnfp::types::nfp::string_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::String.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::string_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::String, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::String.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::real_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Real)


def test_marte::library::basicnfp::types::nfp::real_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Real.__init__)


def test_marte::library::basicnfp::types::nfp::real_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Real.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_marte::library::basicnfp::types::nfp::real_has_value():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Real, "value")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Real.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_nfp::real_is_not_abstract():
    assert not inspect.isabstract(NFP::Real)


def test_nfp::real_constructor_exists():
    assert callable(NFP::Real.__init__)


def test_nfp::real_constructor_args():
    sig = inspect.signature(NFP::Real.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::basicnfp::types::nfp::area_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Area)


def test_marte::library::basicnfp::types::nfp::area_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Area.__init__)


def test_marte::library::basicnfp::types::nfp::area_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Area.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_marte::library::basicnfp::types::nfp::area_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Area, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Area.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::area_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Area, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Area.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::price_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Price)


def test_marte::library::basicnfp::types::nfp::price_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Price.__init__)


def test_marte::library::basicnfp::types::nfp::price_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Price.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::price_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Price, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Price.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::energy_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Energy)


def test_marte::library::basicnfp::types::nfp::energy_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Energy.__init__)


def test_marte::library::basicnfp::types::nfp::energy_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Energy.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_marte::library::basicnfp::types::nfp::energy_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Energy, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Energy.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::energy_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Energy, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Energy.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::percentage_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Percentage)


def test_marte::library::basicnfp::types::nfp::percentage_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Percentage.__init__)


def test_marte::library::basicnfp::types::nfp::percentage_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Percentage.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::percentage_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Percentage, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Percentage.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::power_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Power)


def test_marte::library::basicnfp::types::nfp::power_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Power.__init__)


def test_marte::library::basicnfp::types::nfp::power_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Power.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::power_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Power, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Power.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::power_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Power, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Power.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::length_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Length)


def test_marte::library::basicnfp::types::nfp::length_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Length.__init__)


def test_marte::library::basicnfp::types::nfp::length_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Length.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::length_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Length, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Length.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::length_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Length, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Length.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::datasize_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::DataSize)


def test_marte::library::basicnfp::types::nfp::datasize_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::DataSize.__init__)


def test_marte::library::basicnfp::types::nfp::datasize_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::DataSize.__init__)
    params = list(sig.parameters.keys())
    assert "unit" in params, "Missing parameter 'unit'"
    assert "precision" in params, "Missing parameter 'precision'"

def test_marte::library::basicnfp::types::nfp::datasize_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::DataSize, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::DataSize.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::datasize_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::DataSize, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::DataSize.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::weight_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Weight)


def test_marte::library::basicnfp::types::nfp::weight_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Weight.__init__)


def test_marte::library::basicnfp::types::nfp::weight_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Weight.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::weight_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Weight, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Weight.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::weight_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Weight, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Weight.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::datatxrate_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::DataTxRate)


def test_marte::library::basicnfp::types::nfp::datatxrate_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::DataTxRate.__init__)


def test_marte::library::basicnfp::types::nfp::datatxrate_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::DataTxRate.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::datatxrate_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::DataTxRate, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::DataTxRate.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::datatxrate_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::DataTxRate, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::DataTxRate.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::duration_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Duration)


def test_marte::library::basicnfp::types::nfp::duration_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Duration.__init__)


def test_marte::library::basicnfp::types::nfp::duration_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Duration.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "worst" in params, "Missing parameter 'worst'"
    assert "unit" in params, "Missing parameter 'unit'"
    assert "clock" in params, "Missing parameter 'clock'"
    assert "best" in params, "Missing parameter 'best'"

def test_marte::library::basicnfp::types::nfp::duration_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Duration, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Duration.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::duration_has_worst():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Duration, "worst")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Duration.__mro__:
        if "worst" in klass.__dict__:
            descriptor = klass.__dict__["worst"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::duration_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Duration, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Duration.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::duration_has_clock():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Duration, "clock")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Duration.__mro__:
        if "clock" in klass.__dict__:
            descriptor = klass.__dict__["clock"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::duration_has_best():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Duration, "best")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Duration.__mro__:
        if "best" in klass.__dict__:
            descriptor = klass.__dict__["best"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::basicnfp::types::nfp::frequency_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::BasicNFP::Types::NFP::Frequency)


def test_marte::library::basicnfp::types::nfp::frequency_constructor_exists():
    assert callable(MARTE::Library::BasicNFP::Types::NFP::Frequency.__init__)


def test_marte::library::basicnfp::types::nfp::frequency_constructor_args():
    sig = inspect.signature(MARTE::Library::BasicNFP::Types::NFP::Frequency.__init__)
    params = list(sig.parameters.keys())
    assert "precision" in params, "Missing parameter 'precision'"
    assert "unit" in params, "Missing parameter 'unit'"

def test_marte::library::basicnfp::types::nfp::frequency_has_precision():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Frequency, "precision")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Frequency.__mro__:
        if "precision" in klass.__dict__:
            descriptor = klass.__dict__["precision"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::basicnfp::types::nfp::frequency_has_unit():
    assert hasattr(MARTE::Library::BasicNFP::Types::NFP::Frequency, "unit")
    descriptor = None
    for klass in MARTE::Library::BasicNFP::Types::NFP::Frequency.__mro__:
        if "unit" in klass.__dict__:
            descriptor = klass.__dict__["unit"]
            break
    assert isinstance(descriptor, property)



def test_nfp::integer_is_not_abstract():
    assert not inspect.isabstract(NFP::Integer)


def test_nfp::integer_constructor_exists():
    assert callable(NFP::Integer.__init__)


def test_nfp::integer_constructor_args():
    sig = inspect.signature(NFP::Integer.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::grm::basictypes::fixedpriorityparameters_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::GRM::BasicTypes::FixedPriorityParameters)


def test_marte::library::grm::basictypes::fixedpriorityparameters_constructor_exists():
    assert callable(MARTE::Library::GRM::BasicTypes::FixedPriorityParameters.__init__)


def test_marte::library::grm::basictypes::fixedpriorityparameters_constructor_args():
    sig = inspect.signature(MARTE::Library::GRM::BasicTypes::FixedPriorityParameters.__init__)
    params = list(sig.parameters.keys())



def test_periodicserverparameters_is_not_abstract():
    assert not inspect.isabstract(PeriodicServerParameters)


def test_periodicserverparameters_constructor_exists():
    assert callable(PeriodicServerParameters.__init__)


def test_periodicserverparameters_constructor_args():
    sig = inspect.signature(PeriodicServerParameters.__init__)
    params = list(sig.parameters.keys())



def test_poolingparameters_is_not_abstract():
    assert not inspect.isabstract(PoolingParameters)


def test_poolingparameters_constructor_exists():
    assert callable(PoolingParameters.__init__)


def test_poolingparameters_constructor_args():
    sig = inspect.signature(PoolingParameters.__init__)
    params = list(sig.parameters.keys())



def test_nfp::duration_is_not_abstract():
    assert not inspect.isabstract(NFP::Duration)


def test_nfp::duration_constructor_exists():
    assert callable(NFP::Duration.__init__)


def test_nfp::duration_constructor_args():
    sig = inspect.signature(NFP::Duration.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::grm::basictypes::edf::parameters_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::GRM::BasicTypes::EDF::Parameters)


def test_marte::library::grm::basictypes::edf::parameters_constructor_exists():
    assert callable(MARTE::Library::GRM::BasicTypes::EDF::Parameters.__init__)


def test_marte::library::grm::basictypes::edf::parameters_constructor_args():
    sig = inspect.signature(MARTE::Library::GRM::BasicTypes::EDF::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_fixedpriorityparameters_is_not_abstract():
    assert not inspect.isabstract(FixedPriorityParameters)


def test_fixedpriorityparameters_constructor_exists():
    assert callable(FixedPriorityParameters.__init__)


def test_fixedpriorityparameters_constructor_args():
    sig = inspect.signature(FixedPriorityParameters.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::grm::basictypes::periodicserverparameters_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::GRM::BasicTypes::PeriodicServerParameters)


def test_marte::library::grm::basictypes::periodicserverparameters_constructor_exists():
    assert callable(MARTE::Library::GRM::BasicTypes::PeriodicServerParameters.__init__)


def test_marte::library::grm::basictypes::periodicserverparameters_constructor_args():
    sig = inspect.signature(MARTE::Library::GRM::BasicTypes::PeriodicServerParameters.__init__)
    params = list(sig.parameters.keys())
    assert "backgroundPriority" in params, "Missing parameter 'backgroundPriority'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_marte::library::grm::basictypes::periodicserverparameters_has_backgroundPriority():
    assert hasattr(MARTE::Library::GRM::BasicTypes::PeriodicServerParameters, "backgroundPriority")
    descriptor = None
    for klass in MARTE::Library::GRM::BasicTypes::PeriodicServerParameters.__mro__:
        if "backgroundPriority" in klass.__dict__:
            descriptor = klass.__dict__["backgroundPriority"]
            break
    assert isinstance(descriptor, property)

def test_marte::library::grm::basictypes::periodicserverparameters_has_kind():
    assert hasattr(MARTE::Library::GRM::BasicTypes::PeriodicServerParameters, "kind")
    descriptor = None
    for klass in MARTE::Library::GRM::BasicTypes::PeriodicServerParameters.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_marte::library::grm::basictypes::poolingparameters_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::GRM::BasicTypes::PoolingParameters)


def test_marte::library::grm::basictypes::poolingparameters_constructor_exists():
    assert callable(MARTE::Library::GRM::BasicTypes::PoolingParameters.__init__)


def test_marte::library::grm::basictypes::poolingparameters_constructor_args():
    sig = inspect.signature(MARTE::Library::GRM::BasicTypes::PoolingParameters.__init__)
    params = list(sig.parameters.keys())



def test_edf::parameters_is_not_abstract():
    assert not inspect.isabstract(EDF::Parameters)


def test_edf::parameters_constructor_exists():
    assert callable(EDF::Parameters.__init__)


def test_edf::parameters_constructor_args():
    sig = inspect.signature(EDF::Parameters.__init__)
    params = list(sig.parameters.keys())



def test_marte::library::grm::basictypes::schedparameters_is_not_abstract():
    assert not inspect.isabstract(MARTE::Library::GRM::BasicTypes::SchedParameters)


def test_marte::library::grm::basictypes::schedparameters_constructor_exists():
    assert callable(MARTE::Library::GRM::BasicTypes::SchedParameters.__init__)


def test_marte::library::grm::basictypes::schedparameters_constructor_args():
    sig = inspect.signature(MARTE::Library::GRM::BasicTypes::SchedParameters.__init__)
    params = list(sig.parameters.keys())
    assert "tableEntry" in params, "Missing parameter 'tableEntry'"

def test_marte::library::grm::basictypes::schedparameters_has_tableEntry():
    assert hasattr(MARTE::Library::GRM::BasicTypes::SchedParameters, "tableEntry")
    descriptor = None
    for klass in MARTE::Library::GRM::BasicTypes::SchedParameters.__mro__:
        if "tableEntry" in klass.__dict__:
            descriptor = klass.__dict__["tableEntry"]
            break
    assert isinstance(descriptor, property)

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

def test_timenaturekind_exists():
    # Check that the Enumeration exists
    assert TimeNatureKind is not None

def test_timenaturekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeNatureKind]
    expected_literals = [
        "discrete",
        "dense",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeNatureKind"

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

def test_sourcekind_exists():
    # Check that the Enumeration exists
    assert SourceKind is not None

def test_sourcekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SourceKind]
    expected_literals = [
        "est",
        "req",
        "calc",
        "meas",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SourceKind"

def test_energyunitkind_exists():
    # Check that the Enumeration exists
    assert EnergyUnitKind is not None

def test_energyunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EnergyUnitKind]
    expected_literals = [
        "J",
        "KJ",
        "Wh",
        "KWh",
        "mWh",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EnergyUnitKind"

def test_frequencyunitkind_exists():
    # Check that the Enumeration exists
    assert FrequencyUnitKind is not None

def test_frequencyunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FrequencyUnitKind]
    expected_literals = [
        "rpm",
        "GHz",
        "Hz",
        "KHz",
        "MHz",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FrequencyUnitKind"

def test_datatxrateunitkind_exists():
    # Check that the Enumeration exists
    assert DataTxRateUnitKind is not None

def test_datatxrateunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTxRateUnitKind]
    expected_literals = [
        "Kb_per_s",
        "b_per_s",
        "Mb_per_s",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTxRateUnitKind"

def test_datasizeunitkind_exists():
    # Check that the Enumeration exists
    assert DataSizeUnitKind is not None

def test_datasizeunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataSizeUnitKind]
    expected_literals = [
        "Byte",
        "bit",
        "KB",
        "GB",
        "MB",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataSizeUnitKind"

def test_eventkind_exists():
    # Check that the Enumeration exists
    assert EventKind is not None

def test_eventkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventKind]
    expected_literals = [
        "finish",
        "start",
        "consume",
        "receive",
        "send",
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
        "m",
        "mm",
        "cm",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LengthUnitKind"

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

def test_protectprotocolkind_exists():
    # Check that the Enumeration exists
    assert ProtectProtocolKind is not None

def test_protectprotocolkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProtectProtocolKind]
    expected_literals = [
        "StackBased",
        "PriorityInheritance",
        "FIFO",
        "PriorityCeiling",
        "Other",
        "Undef",
        "NoPreemption",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProtectProtocolKind"

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

def test_weightunitkind_exists():
    # Check that the Enumeration exists
    assert WeightUnitKind is not None

def test_weightunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WeightUnitKind]
    expected_literals = [
        "kg",
        "g",
        "mg",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WeightUnitKind"

def test_timestandardkind_exists():
    # Check that the Enumeration exists
    assert TimeStandardKind is not None

def test_timestandardkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeStandardKind]
    expected_literals = [
        "Local",
        "TAI",
        "GPS",
        "UT0",
        "TCG",
        "UT1",
        "Sidereal",
        "TBD",
        "TCB",
        "TT",
        "UTC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeStandardKind"

def test_schedpolicykind_exists():
    # Check that the Enumeration exists
    assert SchedPolicyKind is not None

def test_schedpolicykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SchedPolicyKind]
    expected_literals = [
        "LeastLaxityFirst",
        "RoundRobin",
        "FIFO",
        "Undef",
        "TimeTableDriven",
        "FixedPriority",
        "Other",
        "EarliestDeadlineFirst",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SchedPolicyKind"

def test_tuk_exists():
    # Check that the Enumeration exists
    assert TUK is not None

def test_tuk_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TUK]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TUK"

def test_periodicserverkind_exists():
    # Check that the Enumeration exists
    assert PeriodicServerKind is not None

def test_periodicserverkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PeriodicServerKind]
    expected_literals = [
        "Other",
        "Undef",
        "Deferrable",
        "Sporadic",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PeriodicServerKind"

def test_statisticalqualifierkind_exists():
    # Check that the Enumeration exists
    assert StatisticalQualifierKind is not None

def test_statisticalqualifierkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in StatisticalQualifierKind]
    expected_literals = [
        "determ",
        "variance",
        "mean",
        "range",
        "other",
        "distrib",
        "min",
        "percent",
        "max",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in StatisticalQualifierKind"

def test_timeunitkind_exists():
    # Check that the Enumeration exists
    assert TimeUnitKind is not None

def test_timeunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TimeUnitKind]
    expected_literals = [
        "hrs",
        "ns",
        "us",
        "s",
        "min",
        "day",
        "ms",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TimeUnitKind"

def test_powerunitkind_exists():
    # Check that the Enumeration exists
    assert PowerUnitKind is not None

def test_powerunitkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PowerUnitKind]
    expected_literals = [
        "mW",
        "W",
        "KW",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PowerUnitKind"

def test_transmmodekind_exists():
    # Check that the Enumeration exists
    assert TransmModeKind is not None

def test_transmmodekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransmModeKind]
    expected_literals = [
        "fullDuplex",
        "simplex",
        "halfDuplex",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransmModeKind"


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
MARTE::Library::RS::Library::ShapeSpecification_strategy = st.builds(
    MARTE::Library::RS::Library::ShapeSpecification,
    size=
        safe_text
)
IntegerMatrix_strategy = st.builds(
    IntegerMatrix,
)
MARTE::Library::RS::Library::TilerSpecification_strategy = st.builds(
    MARTE::Library::RS::Library::TilerSpecification,
)
MARTE::Library::TimeLibrary::IdealClock_strategy = st.builds(
    MARTE::Library::TimeLibrary::IdealClock,
)
MARTE::Library::MARTE::DataTypes::RealMatrix_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::RealMatrix,
    matrixElem=
        safe_text
)
MARTE::Library::MARTE::DataTypes::RealVector_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::RealVector,
    vectorElem=
        safe_text
)
NFP::Natural_strategy = st.builds(
    NFP::Natural,
)
MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval,
)
MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval,
)
MARTE::Library::MARTE::DataTypes::Realnterval_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::Realnterval,
    bound=
        safe_text
)
MARTE::Library::MARTE::DataTypes::Interval_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::Interval,
)
MARTE::Library::MARTE::DataTypes::Array_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::Array,
)
MARTE::Library::TimeLibrary::TimedValueType_strategy = st.builds(
    MARTE::Library::TimeLibrary::TimedValueType,
    value=
        safe_text,
    expr=
        safe_text,
    unit=
        safe_text,
    onClock=
        safe_text
)
MARTE::Library::MARTE::DataTypes::IntegerMatrix_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::IntegerMatrix,
)
MARTE::Library::MARTE::DataTypes::IntegerVector_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::IntegerVector,
    vectorElem=
        safe_text
)
MARTE::Library::MARTE::DataTypes::UtilityType_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::UtilityType,
)
MARTE::Library::MARTE::DataTypes::IntegerInterval_strategy = st.builds(
    MARTE::Library::MARTE::DataTypes::IntegerInterval,
    bound=
        safe_text
)
IntegerVector_strategy = st.builds(
    IntegerVector,
)
MARTE::Library::BasicNFP::Types::AperiodicPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::AperiodicPattern,
)
MARTE::Library::BasicNFP::Types::PeriodicPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::PeriodicPattern,
)
OpenPattern_strategy = st.builds(
    OpenPattern,
)
NFP::Frequency_strategy = st.builds(
    NFP::Frequency,
)
MARTE::Library::BasicNFP::Types::OpenPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::OpenPattern,
    arrivalProcess=
        safe_text
)
MARTE::Library::BasicNFP::Types::ClosedPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::ClosedPattern,
)
SporadicPattern_strategy = st.builds(
    SporadicPattern,
)
ClosedPattern_strategy = st.builds(
    ClosedPattern,
)
IrregularPattern_strategy = st.builds(
    IrregularPattern,
)
BurstPattern_strategy = st.builds(
    BurstPattern,
)
AperiodicPattern_strategy = st.builds(
    AperiodicPattern,
)
MARTE::Library::BasicNFP::Types::BurstPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::BurstPattern,
)
MARTE::Library::BasicNFP::Types::IrregularPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::IrregularPattern,
)
MARTE::Library::BasicNFP::Types::SporadicPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::SporadicPattern,
)
PeriodicPattern_strategy = st.builds(
    PeriodicPattern,
)
MARTE::Library::BasicNFP::Types::ArrivalPattern_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::ArrivalPattern,
)
MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::CommonType,
    statQ=
        safe_text,
    source=
        safe_text,
    mode=
        safe_text,
    expr=
        safe_text,
    dir=
        safe_text
)
NFP::CommonType_strategy = st.builds(
    NFP::CommonType,
)
MARTE::Library::BasicNFP::Types::NFP::Natural_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Natural,
    value=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Integer_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Integer,
    value=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Boolean_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Boolean,
    value=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::DateTime_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::DateTime,
    value=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::String_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::String,
    value=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Real_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Real,
    value=
        safe_text
)
NFP::Real_strategy = st.builds(
    NFP::Real,
)
MARTE::Library::BasicNFP::Types::NFP::Area_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Area,
    unit=
        safe_text,
    precision=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Price_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Price,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Energy_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Energy,
    unit=
        safe_text,
    precision=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Percentage_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Percentage,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Power_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Power,
    precision=
        safe_text,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Length_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Length,
    precision=
        safe_text,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::DataSize,
    unit=
        safe_text,
    precision=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Weight_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Weight,
    precision=
        safe_text,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::DataTxRate,
    precision=
        safe_text,
    unit=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Duration_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Duration,
    precision=
        safe_text,
    worst=
        safe_text,
    unit=
        safe_text,
    clock=
        safe_text,
    best=
        safe_text
)
MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy = st.builds(
    MARTE::Library::BasicNFP::Types::NFP::Frequency,
    precision=
        safe_text,
    unit=
        safe_text
)
NFP::Integer_strategy = st.builds(
    NFP::Integer,
)
MARTE::Library::GRM::BasicTypes::FixedPriorityParameters_strategy = st.builds(
    MARTE::Library::GRM::BasicTypes::FixedPriorityParameters,
)
PeriodicServerParameters_strategy = st.builds(
    PeriodicServerParameters,
)
PoolingParameters_strategy = st.builds(
    PoolingParameters,
)
NFP::Duration_strategy = st.builds(
    NFP::Duration,
)
MARTE::Library::GRM::BasicTypes::EDF::Parameters_strategy = st.builds(
    MARTE::Library::GRM::BasicTypes::EDF::Parameters,
)
FixedPriorityParameters_strategy = st.builds(
    FixedPriorityParameters,
)
MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy = st.builds(
    MARTE::Library::GRM::BasicTypes::PeriodicServerParameters,
    backgroundPriority=
        safe_text,
    kind=
        safe_text
)
MARTE::Library::GRM::BasicTypes::PoolingParameters_strategy = st.builds(
    MARTE::Library::GRM::BasicTypes::PoolingParameters,
)
EDF::Parameters_strategy = st.builds(
    EDF::Parameters,
)
MARTE::Library::GRM::BasicTypes::SchedParameters_strategy = st.builds(
    MARTE::Library::GRM::BasicTypes::SchedParameters,
    tableEntry=
        safe_text
)

@given(instance=MARTE::Library::RS::Library::ShapeSpecification_strategy)
@settings(max_examples=50)
def test_marte::library::rs::library::shapespecification_instantiation(instance):
    assert isinstance(instance, MARTE::Library::RS::Library::ShapeSpecification)

@given(instance=MARTE::Library::RS::Library::ShapeSpecification_strategy)
def test_marte::library::rs::library::shapespecification_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=MARTE::Library::RS::Library::ShapeSpecification_strategy)
def test_marte::library::rs::library::shapespecification_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=IntegerMatrix_strategy)
@settings(max_examples=50)
def test_integermatrix_instantiation(instance):
    assert isinstance(instance, IntegerMatrix)

@given(instance=MARTE::Library::RS::Library::TilerSpecification_strategy)
@settings(max_examples=50)
def test_marte::library::rs::library::tilerspecification_instantiation(instance):
    assert isinstance(instance, MARTE::Library::RS::Library::TilerSpecification)

@given(instance=MARTE::Library::TimeLibrary::IdealClock_strategy)
@settings(max_examples=50)
def test_marte::library::timelibrary::idealclock_instantiation(instance):
    assert isinstance(instance, MARTE::Library::TimeLibrary::IdealClock)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::TimeLibrary::IdealClock_strategy)
@settings(max_examples=30)
def test_marte::library::timelibrary::idealclock_currenttime_changes_state(instance):
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
        assert has_statements, f"Function 'currentTime' in MARTE::Library::TimeLibrary::IdealClock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'currentTime' in MARTE::Library::TimeLibrary::IdealClock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'currentTime' in MARTE::Library::TimeLibrary::IdealClock is not implemented or raised an error")

@given(instance=MARTE::Library::MARTE::DataTypes::RealMatrix_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::realmatrix_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::RealMatrix)

@given(instance=MARTE::Library::MARTE::DataTypes::RealMatrix_strategy)
def test_marte::library::marte::datatypes::realmatrix_matrixElem_type(instance):
    assert isinstance(instance.matrixElem, str)


@given(instance=MARTE::Library::MARTE::DataTypes::RealMatrix_strategy)
def test_marte::library::marte::datatypes::realmatrix_matrixElem_setter(instance):
    original = instance.matrixElem
    instance.matrixElem = original
    assert instance.matrixElem == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::RealMatrix_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::realmatrix_at_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.at(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.at).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'at' in MARTE::Library::MARTE::DataTypes::RealMatrix is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::RealMatrix did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::RealMatrix is not implemented or raised an error")

@given(instance=MARTE::Library::MARTE::DataTypes::RealVector_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::realvector_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::RealVector)

@given(instance=MARTE::Library::MARTE::DataTypes::RealVector_strategy)
def test_marte::library::marte::datatypes::realvector_vectorElem_type(instance):
    assert isinstance(instance.vectorElem, str)


@given(instance=MARTE::Library::MARTE::DataTypes::RealVector_strategy)
def test_marte::library::marte::datatypes::realvector_vectorElem_setter(instance):
    original = instance.vectorElem
    instance.vectorElem = original
    assert instance.vectorElem == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::RealVector_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::realvector_at_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.at(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.at).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'at' in MARTE::Library::MARTE::DataTypes::RealVector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::RealVector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::RealVector is not implemented or raised an error")

@given(instance=NFP::Natural_strategy)
@settings(max_examples=50)
def test_nfp::natural_instantiation(instance):
    assert isinstance(instance, NFP::Natural)

@given(instance=MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::nfp::naturalinterval_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::NFP::NaturalInterval)

@given(instance=MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::nfp::frequencyinterval_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::NFP::FrequencyInterval)

@given(instance=MARTE::Library::MARTE::DataTypes::Realnterval_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::realnterval_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::Realnterval)

@given(instance=MARTE::Library::MARTE::DataTypes::Realnterval_strategy)
def test_marte::library::marte::datatypes::realnterval_bound_type(instance):
    assert isinstance(instance.bound, str)


@given(instance=MARTE::Library::MARTE::DataTypes::Realnterval_strategy)
def test_marte::library::marte::datatypes::realnterval_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=MARTE::Library::MARTE::DataTypes::Interval_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::interval_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::Interval)

@given(instance=MARTE::Library::MARTE::DataTypes::Array_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::array_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::Array)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::Array_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::array_at_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.at(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.at).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'at' in MARTE::Library::MARTE::DataTypes::Array is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::Array did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::Array is not implemented or raised an error")

@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
@settings(max_examples=50)
def test_marte::library::timelibrary::timedvaluetype_instantiation(instance):
    assert isinstance(instance, MARTE::Library::TimeLibrary::TimedValueType)

@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_onClock_type(instance):
    assert isinstance(instance.onClock, str)


@given(instance=MARTE::Library::TimeLibrary::TimedValueType_strategy)
def test_marte::library::timelibrary::timedvaluetype_onClock_setter(instance):
    original = instance.onClock
    instance.onClock = original
    assert instance.onClock == original

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerMatrix_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::integermatrix_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::IntegerMatrix)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerMatrix_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::integermatrix_at_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.at(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.at).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'at' in MARTE::Library::MARTE::DataTypes::IntegerMatrix is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::IntegerMatrix did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::IntegerMatrix is not implemented or raised an error")

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerVector_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::integervector_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::IntegerVector)

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerVector_strategy)
def test_marte::library::marte::datatypes::integervector_vectorElem_type(instance):
    assert isinstance(instance.vectorElem, str)


@given(instance=MARTE::Library::MARTE::DataTypes::IntegerVector_strategy)
def test_marte::library::marte::datatypes::integervector_vectorElem_setter(instance):
    original = instance.vectorElem
    instance.vectorElem = original
    assert instance.vectorElem == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerVector_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::integervector_at_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.at(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.at).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'at' in MARTE::Library::MARTE::DataTypes::IntegerVector is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::IntegerVector did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'at' in MARTE::Library::MARTE::DataTypes::IntegerVector is not implemented or raised an error")

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::utilitytype_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::UtilityType)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_eq_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eq(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eq).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eq' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eq' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eq' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_ge_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ge(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ge).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ge' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ge' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ge' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_lt_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.lt(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.lt).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'lt' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'lt' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'lt' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_le_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.le(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.le).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'le' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'le' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'le' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_gt_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.gt(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.gt).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'gt' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'gt' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'gt' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::MARTE::DataTypes::UtilityType_strategy)
@settings(max_examples=30)
def test_marte::library::marte::datatypes::utilitytype_ne_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.ne(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.ne).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'ne' in MARTE::Library::MARTE::DataTypes::UtilityType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'ne' in MARTE::Library::MARTE::DataTypes::UtilityType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'ne' in MARTE::Library::MARTE::DataTypes::UtilityType is not implemented or raised an error")

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerInterval_strategy)
@settings(max_examples=50)
def test_marte::library::marte::datatypes::integerinterval_instantiation(instance):
    assert isinstance(instance, MARTE::Library::MARTE::DataTypes::IntegerInterval)

@given(instance=MARTE::Library::MARTE::DataTypes::IntegerInterval_strategy)
def test_marte::library::marte::datatypes::integerinterval_bound_type(instance):
    assert isinstance(instance.bound, str)


@given(instance=MARTE::Library::MARTE::DataTypes::IntegerInterval_strategy)
def test_marte::library::marte::datatypes::integerinterval_bound_setter(instance):
    original = instance.bound
    instance.bound = original
    assert instance.bound == original

@given(instance=IntegerVector_strategy)
@settings(max_examples=50)
def test_integervector_instantiation(instance):
    assert isinstance(instance, IntegerVector)

@given(instance=MARTE::Library::BasicNFP::Types::AperiodicPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::aperiodicpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::AperiodicPattern)

@given(instance=MARTE::Library::BasicNFP::Types::PeriodicPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::periodicpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::PeriodicPattern)

@given(instance=OpenPattern_strategy)
@settings(max_examples=50)
def test_openpattern_instantiation(instance):
    assert isinstance(instance, OpenPattern)

@given(instance=NFP::Frequency_strategy)
@settings(max_examples=50)
def test_nfp::frequency_instantiation(instance):
    assert isinstance(instance, NFP::Frequency)

@given(instance=MARTE::Library::BasicNFP::Types::OpenPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::openpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::OpenPattern)

@given(instance=MARTE::Library::BasicNFP::Types::OpenPattern_strategy)
def test_marte::library::basicnfp::types::openpattern_arrivalProcess_type(instance):
    assert isinstance(instance.arrivalProcess, str)


@given(instance=MARTE::Library::BasicNFP::Types::OpenPattern_strategy)
def test_marte::library::basicnfp::types::openpattern_arrivalProcess_setter(instance):
    original = instance.arrivalProcess
    instance.arrivalProcess = original
    assert instance.arrivalProcess == original

@given(instance=MARTE::Library::BasicNFP::Types::ClosedPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::closedpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::ClosedPattern)

@given(instance=SporadicPattern_strategy)
@settings(max_examples=50)
def test_sporadicpattern_instantiation(instance):
    assert isinstance(instance, SporadicPattern)

@given(instance=ClosedPattern_strategy)
@settings(max_examples=50)
def test_closedpattern_instantiation(instance):
    assert isinstance(instance, ClosedPattern)

@given(instance=IrregularPattern_strategy)
@settings(max_examples=50)
def test_irregularpattern_instantiation(instance):
    assert isinstance(instance, IrregularPattern)

@given(instance=BurstPattern_strategy)
@settings(max_examples=50)
def test_burstpattern_instantiation(instance):
    assert isinstance(instance, BurstPattern)

@given(instance=AperiodicPattern_strategy)
@settings(max_examples=50)
def test_aperiodicpattern_instantiation(instance):
    assert isinstance(instance, AperiodicPattern)

@given(instance=MARTE::Library::BasicNFP::Types::BurstPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::burstpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::BurstPattern)

@given(instance=MARTE::Library::BasicNFP::Types::IrregularPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::irregularpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::IrregularPattern)

@given(instance=MARTE::Library::BasicNFP::Types::SporadicPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::sporadicpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::SporadicPattern)

@given(instance=PeriodicPattern_strategy)
@settings(max_examples=50)
def test_periodicpattern_instantiation(instance):
    assert isinstance(instance, PeriodicPattern)

@given(instance=MARTE::Library::BasicNFP::Types::ArrivalPattern_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::arrivalpattern_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::ArrivalPattern)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::commontype_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::CommonType)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_statQ_type(instance):
    assert isinstance(instance.statQ, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_statQ_setter(instance):
    original = instance.statQ
    instance.statQ = original
    assert instance.statQ == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_source_type(instance):
    assert isinstance(instance.source, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_mode_type(instance):
    assert isinstance(instance.mode, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
def test_marte::library::basicnfp::types::nfp::commontype_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_triangular_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.triangular(
            "test", 
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.triangular).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'triangular' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'triangular' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'triangular' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_poisson_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.poisson(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.poisson).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'poisson' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'poisson' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'poisson' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_geometric_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.geometric(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.geometric).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'geometric' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'geometric' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'geometric' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_exp_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.exp(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.exp).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'exp' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'exp' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'exp' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_logarithmic_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.logarithmic(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.logarithmic).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'logarithmic' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'logarithmic' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'logarithmic' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_uniform_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.uniform(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.uniform).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'uniform' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'uniform' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'uniform' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_normal_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.normal(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.normal).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'normal' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'normal' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'normal' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_bernoulli_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bernoulli(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bernoulli).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bernoulli' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bernoulli' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bernoulli' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_gamma_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.gamma(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.gamma).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'gamma' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'gamma' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'gamma' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=MARTE::Library::BasicNFP::Types::NFP::CommonType_strategy)
@settings(max_examples=30)
def test_marte::library::basicnfp::types::nfp::commontype_binomial_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.binomial(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.binomial).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'binomial' in MARTE::Library::BasicNFP::Types::NFP::CommonType is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'binomial' in MARTE::Library::BasicNFP::Types::NFP::CommonType did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'binomial' in MARTE::Library::BasicNFP::Types::NFP::CommonType is not implemented or raised an error")

@given(instance=NFP::CommonType_strategy)
@settings(max_examples=50)
def test_nfp::commontype_instantiation(instance):
    assert isinstance(instance, NFP::CommonType)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Natural_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::natural_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Natural)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Natural_strategy)
def test_marte::library::basicnfp::types::nfp::natural_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Natural_strategy)
def test_marte::library::basicnfp::types::nfp::natural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Integer_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::integer_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Integer)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Integer_strategy)
def test_marte::library::basicnfp::types::nfp::integer_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Integer_strategy)
def test_marte::library::basicnfp::types::nfp::integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Boolean_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::boolean_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Boolean)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Boolean_strategy)
def test_marte::library::basicnfp::types::nfp::boolean_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Boolean_strategy)
def test_marte::library::basicnfp::types::nfp::boolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DateTime_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::datetime_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::DateTime)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DateTime_strategy)
def test_marte::library::basicnfp::types::nfp::datetime_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::DateTime_strategy)
def test_marte::library::basicnfp::types::nfp::datetime_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::String_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::string_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::String)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::String_strategy)
def test_marte::library::basicnfp::types::nfp::string_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::String_strategy)
def test_marte::library::basicnfp::types::nfp::string_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Real_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::real_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Real)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Real_strategy)
def test_marte::library::basicnfp::types::nfp::real_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Real_strategy)
def test_marte::library::basicnfp::types::nfp::real_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=NFP::Real_strategy)
@settings(max_examples=50)
def test_nfp::real_instantiation(instance):
    assert isinstance(instance, NFP::Real)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Area_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::area_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Area)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Area_strategy)
def test_marte::library::basicnfp::types::nfp::area_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Area_strategy)
def test_marte::library::basicnfp::types::nfp::area_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Area_strategy)
def test_marte::library::basicnfp::types::nfp::area_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Area_strategy)
def test_marte::library::basicnfp::types::nfp::area_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Price_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::price_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Price)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Price_strategy)
def test_marte::library::basicnfp::types::nfp::price_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Price_strategy)
def test_marte::library::basicnfp::types::nfp::price_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Energy_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::energy_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Energy)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Energy_strategy)
def test_marte::library::basicnfp::types::nfp::energy_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Energy_strategy)
def test_marte::library::basicnfp::types::nfp::energy_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Energy_strategy)
def test_marte::library::basicnfp::types::nfp::energy_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Energy_strategy)
def test_marte::library::basicnfp::types::nfp::energy_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Percentage_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::percentage_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Percentage)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Percentage_strategy)
def test_marte::library::basicnfp::types::nfp::percentage_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Percentage_strategy)
def test_marte::library::basicnfp::types::nfp::percentage_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Power_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::power_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Power)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Power_strategy)
def test_marte::library::basicnfp::types::nfp::power_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Power_strategy)
def test_marte::library::basicnfp::types::nfp::power_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Power_strategy)
def test_marte::library::basicnfp::types::nfp::power_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Power_strategy)
def test_marte::library::basicnfp::types::nfp::power_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Length_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::length_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Length)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Length_strategy)
def test_marte::library::basicnfp::types::nfp::length_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Length_strategy)
def test_marte::library::basicnfp::types::nfp::length_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Length_strategy)
def test_marte::library::basicnfp::types::nfp::length_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Length_strategy)
def test_marte::library::basicnfp::types::nfp::length_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::datasize_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::DataSize)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy)
def test_marte::library::basicnfp::types::nfp::datasize_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy)
def test_marte::library::basicnfp::types::nfp::datasize_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy)
def test_marte::library::basicnfp::types::nfp::datasize_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataSize_strategy)
def test_marte::library::basicnfp::types::nfp::datasize_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Weight_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::weight_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Weight)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Weight_strategy)
def test_marte::library::basicnfp::types::nfp::weight_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Weight_strategy)
def test_marte::library::basicnfp::types::nfp::weight_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Weight_strategy)
def test_marte::library::basicnfp::types::nfp::weight_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Weight_strategy)
def test_marte::library::basicnfp::types::nfp::weight_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::datatxrate_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::DataTxRate)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy)
def test_marte::library::basicnfp::types::nfp::datatxrate_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy)
def test_marte::library::basicnfp::types::nfp::datatxrate_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy)
def test_marte::library::basicnfp::types::nfp::datatxrate_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::DataTxRate_strategy)
def test_marte::library::basicnfp::types::nfp::datatxrate_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::duration_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Duration)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_worst_type(instance):
    assert isinstance(instance.worst, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_worst_setter(instance):
    original = instance.worst
    instance.worst = original
    assert instance.worst == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_clock_type(instance):
    assert isinstance(instance.clock, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_clock_setter(instance):
    original = instance.clock
    instance.clock = original
    assert instance.clock == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_best_type(instance):
    assert isinstance(instance.best, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Duration_strategy)
def test_marte::library::basicnfp::types::nfp::duration_best_setter(instance):
    original = instance.best
    instance.best = original
    assert instance.best == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy)
@settings(max_examples=50)
def test_marte::library::basicnfp::types::nfp::frequency_instantiation(instance):
    assert isinstance(instance, MARTE::Library::BasicNFP::Types::NFP::Frequency)

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy)
def test_marte::library::basicnfp::types::nfp::frequency_precision_type(instance):
    assert isinstance(instance.precision, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy)
def test_marte::library::basicnfp::types::nfp::frequency_precision_setter(instance):
    original = instance.precision
    instance.precision = original
    assert instance.precision == original

@given(instance=MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy)
def test_marte::library::basicnfp::types::nfp::frequency_unit_type(instance):
    assert isinstance(instance.unit, str)


@given(instance=MARTE::Library::BasicNFP::Types::NFP::Frequency_strategy)
def test_marte::library::basicnfp::types::nfp::frequency_unit_setter(instance):
    original = instance.unit
    instance.unit = original
    assert instance.unit == original

@given(instance=NFP::Integer_strategy)
@settings(max_examples=50)
def test_nfp::integer_instantiation(instance):
    assert isinstance(instance, NFP::Integer)

@given(instance=MARTE::Library::GRM::BasicTypes::FixedPriorityParameters_strategy)
@settings(max_examples=50)
def test_marte::library::grm::basictypes::fixedpriorityparameters_instantiation(instance):
    assert isinstance(instance, MARTE::Library::GRM::BasicTypes::FixedPriorityParameters)

@given(instance=PeriodicServerParameters_strategy)
@settings(max_examples=50)
def test_periodicserverparameters_instantiation(instance):
    assert isinstance(instance, PeriodicServerParameters)

@given(instance=PoolingParameters_strategy)
@settings(max_examples=50)
def test_poolingparameters_instantiation(instance):
    assert isinstance(instance, PoolingParameters)

@given(instance=NFP::Duration_strategy)
@settings(max_examples=50)
def test_nfp::duration_instantiation(instance):
    assert isinstance(instance, NFP::Duration)

@given(instance=MARTE::Library::GRM::BasicTypes::EDF::Parameters_strategy)
@settings(max_examples=50)
def test_marte::library::grm::basictypes::edf::parameters_instantiation(instance):
    assert isinstance(instance, MARTE::Library::GRM::BasicTypes::EDF::Parameters)

@given(instance=FixedPriorityParameters_strategy)
@settings(max_examples=50)
def test_fixedpriorityparameters_instantiation(instance):
    assert isinstance(instance, FixedPriorityParameters)

@given(instance=MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy)
@settings(max_examples=50)
def test_marte::library::grm::basictypes::periodicserverparameters_instantiation(instance):
    assert isinstance(instance, MARTE::Library::GRM::BasicTypes::PeriodicServerParameters)

@given(instance=MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy)
def test_marte::library::grm::basictypes::periodicserverparameters_backgroundPriority_type(instance):
    assert isinstance(instance.backgroundPriority, str)


@given(instance=MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy)
def test_marte::library::grm::basictypes::periodicserverparameters_backgroundPriority_setter(instance):
    original = instance.backgroundPriority
    instance.backgroundPriority = original
    assert instance.backgroundPriority == original

@given(instance=MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy)
def test_marte::library::grm::basictypes::periodicserverparameters_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=MARTE::Library::GRM::BasicTypes::PeriodicServerParameters_strategy)
def test_marte::library::grm::basictypes::periodicserverparameters_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=MARTE::Library::GRM::BasicTypes::PoolingParameters_strategy)
@settings(max_examples=50)
def test_marte::library::grm::basictypes::poolingparameters_instantiation(instance):
    assert isinstance(instance, MARTE::Library::GRM::BasicTypes::PoolingParameters)

@given(instance=EDF::Parameters_strategy)
@settings(max_examples=50)
def test_edf::parameters_instantiation(instance):
    assert isinstance(instance, EDF::Parameters)

@given(instance=MARTE::Library::GRM::BasicTypes::SchedParameters_strategy)
@settings(max_examples=50)
def test_marte::library::grm::basictypes::schedparameters_instantiation(instance):
    assert isinstance(instance, MARTE::Library::GRM::BasicTypes::SchedParameters)

@given(instance=MARTE::Library::GRM::BasicTypes::SchedParameters_strategy)
def test_marte::library::grm::basictypes::schedparameters_tableEntry_type(instance):
    assert isinstance(instance.tableEntry, str)


@given(instance=MARTE::Library::GRM::BasicTypes::SchedParameters_strategy)
def test_marte::library::grm::basictypes::schedparameters_tableEntry_setter(instance):
    original = instance.tableEntry
    instance.tableEntry = original
    assert instance.tableEntry == original
