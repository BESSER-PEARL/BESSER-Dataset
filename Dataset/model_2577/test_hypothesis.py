import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    siddhi::MILLISECONDS,
    siddhi::SECONDS,
    siddhi::OUTER,
    siddhi::INNER,
    siddhi::JOIN,
    siddhi::FULL,
    siddhi::RIGHT,
    siddhi::LEFT,
    siddhi::WITHIN,
    siddhi::YEARS,
    siddhi::PER,
    siddhi::SET,
    siddhi::AGGREGATE,
    siddhi::AGGREGATION,
    siddhi::WITH,
    siddhi::PARTITION,
    siddhi::END,
    siddhi::UPDATE,
    siddhi::FOR,
    siddhi::DELETE,
    siddhi::PLAN,
    siddhi::BEGIN,
    siddhi::INTO,
    siddhi::INSERT,
    siddhi::FIRST,
    siddhi::SNAPSHOT,
    siddhi::HAVING,
    siddhi::BY,
    siddhi::GROUP,
    siddhi::SELECT,
    siddhi::DOUBLE,
    siddhi::LONG,
    siddhi::INTS,
    siddhi::STRINGS,
    siddhi::OUTPUT,
    siddhi::WINDOW,
    siddhi::TABLE,
    siddhi::FROM,
    siddhi::RETURN,
    siddhi::FUNCTION,
    siddhi::AT,
    siddhi::TRIGGER,
    siddhi::NULL,
    siddhi::IS,
    siddhi::LAST,
    siddhi::CURRENT,
    siddhi::EXPIRED,
    siddhi::RAW,
    siddhi::EVENTS,
    siddhi::ALL,
    siddhi::OBJECT,
    siddhi::BOOL,
    siddhi::FLOAT,
    EveryAbsentSequenceSourceChain,
    EverySequenceSourceChain,
    BasicAbsentPatternSource,
    siddhi::DEFINE,
    siddhi::STREAM,
    AppAnnotation,
    siddhi::APP,
    siddhi::IN,
    RightAbsentPatternSource,
    LeftAbsentPatternSource,
    EveryAbsentPatternSource,
    LogicalAbsentStatefulSource,
    Name,
    siddhi::L,
    SignedLongValue,
    siddhi::LONG::LITERAL,
    siddhi::F,
    SignedFloatValue,
    siddhi::FLOAT::LITERAL,
    siddhi::D,
    siddhi::E,
    SignedDoubleValue,
    siddhi::DOUBLE::LITERAL,
    MILLISECONDS,
    siddhi::MillisecondValue,
    siddhi::FunctionId,
    siddhi::FunctionNamespace,
    siddhi::SignedLongValue,
    FALSE,
    TRUE,
    siddhi::AttributeList,
    siddhi::FeaturesOrOutAttr,
    siddhi::FeaturesOrOutAttrReference,
    siddhi::SignedFloatValue,
    siddhi::SignedDoubleValue,
    siddhi::BoolValue,
    siddhi::AttributeNameReference,
    siddhi::Source1OrStandardStatefulSource,
    PatternCollectionStatefulSource,
    SequenceCollectionStatefulSource,
    siddhi::Literal,
    MathDivmulOperation,
    siddhi::MathOtherOperations,
    MathAddsubOperation,
    siddhi::MathDivmulOperation,
    siddhi::SourceOrEventReference,
    SetAssignment,
    siddhi::ConstantValue,
    siddhi::StreamReference,
    NULL,
    IS,
    MathOtherOperations,
    siddhi::NullCheck,
    siddhi::BasicSourceStreamHandlers,
    MathOperation,
    siddhi::MathAddsubOperation,
    Expression,
    siddhi::MathOperation,
    siddhi::StreamFunction,
    siddhi::Filter,
    siddhi::BasicSourceStreamHandler,
    siddhi::UNIDIRECTIONAL,
    siddhi::JoinSource,
    StandardStream,
    JoinSource,
    siddhi::MainSource,
    JoinStream,
    INNER,
    FULL,
    RIGHT,
    JOIN,
    OUTER,
    LEFT,
    PER,
    WITHIN,
    siddhi::joins,
    siddhi::Per1,
    siddhi::WithinTimeRange,
    AbsentPatternSourceChain,
    siddhi::EveryAbsentPatternSource,
    siddhi::RightAbsentPatternSource,
    siddhi::LeftAbsentPatternSource,
    siddhi::PatternCollectionStatefulSource,
    siddhi::PatternSource,
    siddhi::BasicSource,
    siddhi::NOT,
    siddhi::Collect,
    siddhi::AND,
    SequenceSource,
    siddhi::LogicalAbsentStatefulSource,
    siddhi::LogicalStatefulSource,
    siddhi::SequenceCollectionStatefulSource,
    SequenceSourceChain,
    siddhi::PatternSourceChain,
    PatternStream,
    siddhi::AbsentPatternSourceChain,
    siddhi::EveryPatternSourceChain,
    siddhi::RightAbsentSequenceSource,
    siddhi::LeftAbsentSequenceSource,
    siddhi::BasicAbsentPatternSource,
    siddhi::EObject,
    HAVING,
    GROUP,
    siddhi::HavingExpr,
    siddhi::AbsentSequenceSourceChain,
    siddhi::SequenceSourceChain,
    siddhi::WithinTime,
    siddhi::SequenceSource,
    siddhi::EveryAbsentSequenceSourceChain,
    siddhi::EverySequenceSourceChain,
    siddhi::PatternStream,
    siddhi::SequenceStream,
    siddhi::JoinStream,
    siddhi::Attribute,
    siddhi::OutputAttribute,
    SELECT,
    FIRST,
    LAST,
    siddhi::AttributeIndex,
    siddhi::MathGtLtOperation,
    siddhi::MathInOperation,
    siddhi::NotOperation,
    siddhi::MathEqualOperation,
    siddhi::MINUTES,
    siddhi::HOURS,
    siddhi::DAYS,
    siddhi::WEEKS,
    siddhi::MONTHS,
    siddhi::MathLogicalOperation,
    siddhi::RightAbsentPatternSource1,
    siddhi::LeftAbsentPatternSource1,
    RightAbsentSequenceSource,
    siddhi::RightAbsentSequenceSource1,
    LeftAbsentSequenceSource,
    siddhi::LeftAbsentSequenceSource1,
    siddhi::TRUE,
    siddhi::FALSE,
    SNAPSHOT,
    CURRENT,
    EXPIRED,
    RAW,
    EVENTS,
    ALL,
    siddhi::OutputRateType,
    siddhi::SetAssignment,
    SET,
    siddhi::SetClause,
    siddhi::OR,
    siddhi::ConditionRange,
    siddhi::OF,
    PartitionWithStream,
    siddhi::ConditionRanges,
    siddhi::ON,
    siddhi::Target,
    UPDATE,
    FOR,
    siddhi::ForTime,
    DELETE,
    INTO,
    INSERT,
    siddhi::QuerySection,
    siddhi::QueryInput,
    siddhi::AS,
    siddhi::Expression,
    siddhi::PropertyValue,
    siddhi::PartitionWithStream,
    END,
    BEGIN,
    WITH,
    PARTITION,
    Source1OrStandardStatefulSource,
    siddhi::StreamAlias,
    siddhi::StandardStatefulSource,
    siddhi::Source,
    OBJECT,
    BOOL,
    DOUBLE,
    FLOAT,
    LONG,
    INTS,
    STRINGS,
    FeaturesOrOutAttr,
    siddhi::OutAttr,
    siddhi::PropertySeparator,
    siddhi::AttributeReference,
    siddhi::GroupByQuerySelection,
    siddhi::StandardStream,
    BY,
    siddhi::GroupBy,
    siddhi::PropertyName,
    siddhi::AnnotationElement,
    siddhi::Name,
    YEARS,
    siddhi::YearValue,
    MONTHS,
    siddhi::MonthValue,
    WEEKS,
    siddhi::WeekValue,
    DAYS,
    siddhi::DayValue,
    HOURS,
    siddhi::HourValue,
    MINUTES,
    siddhi::MinuteValue,
    SECONDS,
    siddhi::SecondValue,
    AggregationTime,
    siddhi::AggregationTimeRange,
    siddhi::AggregationTimeInterval,
    siddhi::AggregationTimeDuration,
    siddhi::AggregationTime,
    OUTPUT,
    siddhi::OutputRate,
    WINDOW,
    siddhi::Win,
    siddhi::BasicSourceStreamHandlers1,
    AGGREGATE,
    FROM,
    AGGREGATION,
    siddhi::FunctionBody,
    siddhi::AttributeType,
    siddhi::LanguageName,
    siddhi::FunctionName,
    RETURN,
    siddhi::QueryOutput,
    siddhi::AnonymousStream,
    FUNCTION,
    siddhi::StringValue,
    siddhi::TimeValue,
    siddhi::EVERY,
    siddhi::TriggerName,
    AT,
    TRIGGER,
    siddhi::OutputEventType,
    siddhi::FunctionOperation,
    siddhi::AppAnnotation,
    siddhi::ExecutionPlan,
    TABLE,
    siddhi::Features,
    siddhi::Source1,
    siddhi::Annotation,
    STREAM,
    DEFINE,
    siddhi::Keyword,
    siddhi::DefinitionTable,
    siddhi::DefinitionStream,
    siddhi::Query,
    siddhi::ExecPartition,
    siddhi::ExecutionElement,
    siddhi::DefinitionAggregation,
    siddhi::DefinitionFunction,
    siddhi::DefinitionTrigger,
    siddhi::DefinitionWindow,
    siddhi::SiddhiQL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_siddhi::milliseconds_is_not_abstract():
    assert not inspect.isabstract(siddhi::MILLISECONDS)


def test_siddhi::milliseconds_constructor_exists():
    assert callable(siddhi::MILLISECONDS.__init__)


def test_siddhi::milliseconds_constructor_args():
    sig = inspect.signature(siddhi::MILLISECONDS.__init__)
    params = list(sig.parameters.keys())
    assert "millisec" in params, "Missing parameter 'millisec'"
    assert "millisecond" in params, "Missing parameter 'millisecond'"
    assert "milliseconds" in params, "Missing parameter 'milliseconds'"

def test_siddhi::milliseconds_has_millisec():
    assert hasattr(siddhi::MILLISECONDS, "millisec")
    descriptor = None
    for klass in siddhi::MILLISECONDS.__mro__:
        if "millisec" in klass.__dict__:
            descriptor = klass.__dict__["millisec"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::milliseconds_has_millisecond():
    assert hasattr(siddhi::MILLISECONDS, "millisecond")
    descriptor = None
    for klass in siddhi::MILLISECONDS.__mro__:
        if "millisecond" in klass.__dict__:
            descriptor = klass.__dict__["millisecond"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::milliseconds_has_milliseconds():
    assert hasattr(siddhi::MILLISECONDS, "milliseconds")
    descriptor = None
    for klass in siddhi::MILLISECONDS.__mro__:
        if "milliseconds" in klass.__dict__:
            descriptor = klass.__dict__["milliseconds"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::seconds_is_not_abstract():
    assert not inspect.isabstract(siddhi::SECONDS)


def test_siddhi::seconds_constructor_exists():
    assert callable(siddhi::SECONDS.__init__)


def test_siddhi::seconds_constructor_args():
    sig = inspect.signature(siddhi::SECONDS.__init__)
    params = list(sig.parameters.keys())
    assert "sec" in params, "Missing parameter 'sec'"
    assert "seconds" in params, "Missing parameter 'seconds'"
    assert "second" in params, "Missing parameter 'second'"

def test_siddhi::seconds_has_sec():
    assert hasattr(siddhi::SECONDS, "sec")
    descriptor = None
    for klass in siddhi::SECONDS.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::seconds_has_seconds():
    assert hasattr(siddhi::SECONDS, "seconds")
    descriptor = None
    for klass in siddhi::SECONDS.__mro__:
        if "seconds" in klass.__dict__:
            descriptor = klass.__dict__["seconds"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::seconds_has_second():
    assert hasattr(siddhi::SECONDS, "second")
    descriptor = None
    for klass in siddhi::SECONDS.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::outer_is_not_abstract():
    assert not inspect.isabstract(siddhi::OUTER)


def test_siddhi::outer_constructor_exists():
    assert callable(siddhi::OUTER.__init__)


def test_siddhi::outer_constructor_args():
    sig = inspect.signature(siddhi::OUTER.__init__)
    params = list(sig.parameters.keys())
    assert "outer" in params, "Missing parameter 'outer'"

def test_siddhi::outer_has_outer():
    assert hasattr(siddhi::OUTER, "outer")
    descriptor = None
    for klass in siddhi::OUTER.__mro__:
        if "outer" in klass.__dict__:
            descriptor = klass.__dict__["outer"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::inner_is_not_abstract():
    assert not inspect.isabstract(siddhi::INNER)


def test_siddhi::inner_constructor_exists():
    assert callable(siddhi::INNER.__init__)


def test_siddhi::inner_constructor_args():
    sig = inspect.signature(siddhi::INNER.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"

def test_siddhi::inner_has_inner():
    assert hasattr(siddhi::INNER, "inner")
    descriptor = None
    for klass in siddhi::INNER.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::join_is_not_abstract():
    assert not inspect.isabstract(siddhi::JOIN)


def test_siddhi::join_constructor_exists():
    assert callable(siddhi::JOIN.__init__)


def test_siddhi::join_constructor_args():
    sig = inspect.signature(siddhi::JOIN.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"

def test_siddhi::join_has_join():
    assert hasattr(siddhi::JOIN, "join")
    descriptor = None
    for klass in siddhi::JOIN.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::full_is_not_abstract():
    assert not inspect.isabstract(siddhi::FULL)


def test_siddhi::full_constructor_exists():
    assert callable(siddhi::FULL.__init__)


def test_siddhi::full_constructor_args():
    sig = inspect.signature(siddhi::FULL.__init__)
    params = list(sig.parameters.keys())
    assert "full" in params, "Missing parameter 'full'"

def test_siddhi::full_has_full():
    assert hasattr(siddhi::FULL, "full")
    descriptor = None
    for klass in siddhi::FULL.__mro__:
        if "full" in klass.__dict__:
            descriptor = klass.__dict__["full"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::right_is_not_abstract():
    assert not inspect.isabstract(siddhi::RIGHT)


def test_siddhi::right_constructor_exists():
    assert callable(siddhi::RIGHT.__init__)


def test_siddhi::right_constructor_args():
    sig = inspect.signature(siddhi::RIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_siddhi::right_has_right():
    assert hasattr(siddhi::RIGHT, "right")
    descriptor = None
    for klass in siddhi::RIGHT.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::left_is_not_abstract():
    assert not inspect.isabstract(siddhi::LEFT)


def test_siddhi::left_constructor_exists():
    assert callable(siddhi::LEFT.__init__)


def test_siddhi::left_constructor_args():
    sig = inspect.signature(siddhi::LEFT.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"

def test_siddhi::left_has_left():
    assert hasattr(siddhi::LEFT, "left")
    descriptor = None
    for klass in siddhi::LEFT.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::within_is_not_abstract():
    assert not inspect.isabstract(siddhi::WITHIN)


def test_siddhi::within_constructor_exists():
    assert callable(siddhi::WITHIN.__init__)


def test_siddhi::within_constructor_args():
    sig = inspect.signature(siddhi::WITHIN.__init__)
    params = list(sig.parameters.keys())
    assert "within" in params, "Missing parameter 'within'"

def test_siddhi::within_has_within():
    assert hasattr(siddhi::WITHIN, "within")
    descriptor = None
    for klass in siddhi::WITHIN.__mro__:
        if "within" in klass.__dict__:
            descriptor = klass.__dict__["within"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::years_is_not_abstract():
    assert not inspect.isabstract(siddhi::YEARS)


def test_siddhi::years_constructor_exists():
    assert callable(siddhi::YEARS.__init__)


def test_siddhi::years_constructor_args():
    sig = inspect.signature(siddhi::YEARS.__init__)
    params = list(sig.parameters.keys())
    assert "years" in params, "Missing parameter 'years'"
    assert "year" in params, "Missing parameter 'year'"

def test_siddhi::years_has_years():
    assert hasattr(siddhi::YEARS, "years")
    descriptor = None
    for klass in siddhi::YEARS.__mro__:
        if "years" in klass.__dict__:
            descriptor = klass.__dict__["years"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::years_has_year():
    assert hasattr(siddhi::YEARS, "year")
    descriptor = None
    for klass in siddhi::YEARS.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::per_is_not_abstract():
    assert not inspect.isabstract(siddhi::PER)


def test_siddhi::per_constructor_exists():
    assert callable(siddhi::PER.__init__)


def test_siddhi::per_constructor_args():
    sig = inspect.signature(siddhi::PER.__init__)
    params = list(sig.parameters.keys())
    assert "per" in params, "Missing parameter 'per'"

def test_siddhi::per_has_per():
    assert hasattr(siddhi::PER, "per")
    descriptor = None
    for klass in siddhi::PER.__mro__:
        if "per" in klass.__dict__:
            descriptor = klass.__dict__["per"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::set_is_not_abstract():
    assert not inspect.isabstract(siddhi::SET)


def test_siddhi::set_constructor_exists():
    assert callable(siddhi::SET.__init__)


def test_siddhi::set_constructor_args():
    sig = inspect.signature(siddhi::SET.__init__)
    params = list(sig.parameters.keys())
    assert "set" in params, "Missing parameter 'set'"

def test_siddhi::set_has_set():
    assert hasattr(siddhi::SET, "set")
    descriptor = None
    for klass in siddhi::SET.__mro__:
        if "set" in klass.__dict__:
            descriptor = klass.__dict__["set"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::aggregate_is_not_abstract():
    assert not inspect.isabstract(siddhi::AGGREGATE)


def test_siddhi::aggregate_constructor_exists():
    assert callable(siddhi::AGGREGATE.__init__)


def test_siddhi::aggregate_constructor_args():
    sig = inspect.signature(siddhi::AGGREGATE.__init__)
    params = list(sig.parameters.keys())
    assert "agrregate" in params, "Missing parameter 'agrregate'"

def test_siddhi::aggregate_has_agrregate():
    assert hasattr(siddhi::AGGREGATE, "agrregate")
    descriptor = None
    for klass in siddhi::AGGREGATE.__mro__:
        if "agrregate" in klass.__dict__:
            descriptor = klass.__dict__["agrregate"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::aggregation_is_not_abstract():
    assert not inspect.isabstract(siddhi::AGGREGATION)


def test_siddhi::aggregation_constructor_exists():
    assert callable(siddhi::AGGREGATION.__init__)


def test_siddhi::aggregation_constructor_args():
    sig = inspect.signature(siddhi::AGGREGATION.__init__)
    params = list(sig.parameters.keys())
    assert "aggre" in params, "Missing parameter 'aggre'"

def test_siddhi::aggregation_has_aggre():
    assert hasattr(siddhi::AGGREGATION, "aggre")
    descriptor = None
    for klass in siddhi::AGGREGATION.__mro__:
        if "aggre" in klass.__dict__:
            descriptor = klass.__dict__["aggre"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::with_is_not_abstract():
    assert not inspect.isabstract(siddhi::WITH)


def test_siddhi::with_constructor_exists():
    assert callable(siddhi::WITH.__init__)


def test_siddhi::with_constructor_args():
    sig = inspect.signature(siddhi::WITH.__init__)
    params = list(sig.parameters.keys())
    assert "wi" in params, "Missing parameter 'wi'"

def test_siddhi::with_has_wi():
    assert hasattr(siddhi::WITH, "wi")
    descriptor = None
    for klass in siddhi::WITH.__mro__:
        if "wi" in klass.__dict__:
            descriptor = klass.__dict__["wi"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::partition_is_not_abstract():
    assert not inspect.isabstract(siddhi::PARTITION)


def test_siddhi::partition_constructor_exists():
    assert callable(siddhi::PARTITION.__init__)


def test_siddhi::partition_constructor_args():
    sig = inspect.signature(siddhi::PARTITION.__init__)
    params = list(sig.parameters.keys())
    assert "partition" in params, "Missing parameter 'partition'"

def test_siddhi::partition_has_partition():
    assert hasattr(siddhi::PARTITION, "partition")
    descriptor = None
    for klass in siddhi::PARTITION.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::end_is_not_abstract():
    assert not inspect.isabstract(siddhi::END)


def test_siddhi::end_constructor_exists():
    assert callable(siddhi::END.__init__)


def test_siddhi::end_constructor_args():
    sig = inspect.signature(siddhi::END.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_siddhi::end_has_end():
    assert hasattr(siddhi::END, "end")
    descriptor = None
    for klass in siddhi::END.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::update_is_not_abstract():
    assert not inspect.isabstract(siddhi::UPDATE)


def test_siddhi::update_constructor_exists():
    assert callable(siddhi::UPDATE.__init__)


def test_siddhi::update_constructor_args():
    sig = inspect.signature(siddhi::UPDATE.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"

def test_siddhi::update_has_update():
    assert hasattr(siddhi::UPDATE, "update")
    descriptor = None
    for klass in siddhi::UPDATE.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::for_is_not_abstract():
    assert not inspect.isabstract(siddhi::FOR)


def test_siddhi::for_constructor_exists():
    assert callable(siddhi::FOR.__init__)


def test_siddhi::for_constructor_args():
    sig = inspect.signature(siddhi::FOR.__init__)
    params = list(sig.parameters.keys())
    assert "for_" in params, "Missing parameter 'for_'"

def test_siddhi::for_has_for_():
    assert hasattr(siddhi::FOR, "for_")
    descriptor = None
    for klass in siddhi::FOR.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::delete_is_not_abstract():
    assert not inspect.isabstract(siddhi::DELETE)


def test_siddhi::delete_constructor_exists():
    assert callable(siddhi::DELETE.__init__)


def test_siddhi::delete_constructor_args():
    sig = inspect.signature(siddhi::DELETE.__init__)
    params = list(sig.parameters.keys())
    assert "delete" in params, "Missing parameter 'delete'"

def test_siddhi::delete_has_delete():
    assert hasattr(siddhi::DELETE, "delete")
    descriptor = None
    for klass in siddhi::DELETE.__mro__:
        if "delete" in klass.__dict__:
            descriptor = klass.__dict__["delete"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::plan_is_not_abstract():
    assert not inspect.isabstract(siddhi::PLAN)


def test_siddhi::plan_constructor_exists():
    assert callable(siddhi::PLAN.__init__)


def test_siddhi::plan_constructor_args():
    sig = inspect.signature(siddhi::PLAN.__init__)
    params = list(sig.parameters.keys())
    assert "plan" in params, "Missing parameter 'plan'"

def test_siddhi::plan_has_plan():
    assert hasattr(siddhi::PLAN, "plan")
    descriptor = None
    for klass in siddhi::PLAN.__mro__:
        if "plan" in klass.__dict__:
            descriptor = klass.__dict__["plan"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::begin_is_not_abstract():
    assert not inspect.isabstract(siddhi::BEGIN)


def test_siddhi::begin_constructor_exists():
    assert callable(siddhi::BEGIN.__init__)


def test_siddhi::begin_constructor_args():
    sig = inspect.signature(siddhi::BEGIN.__init__)
    params = list(sig.parameters.keys())
    assert "begin" in params, "Missing parameter 'begin'"

def test_siddhi::begin_has_begin():
    assert hasattr(siddhi::BEGIN, "begin")
    descriptor = None
    for klass in siddhi::BEGIN.__mro__:
        if "begin" in klass.__dict__:
            descriptor = klass.__dict__["begin"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::into_is_not_abstract():
    assert not inspect.isabstract(siddhi::INTO)


def test_siddhi::into_constructor_exists():
    assert callable(siddhi::INTO.__init__)


def test_siddhi::into_constructor_args():
    sig = inspect.signature(siddhi::INTO.__init__)
    params = list(sig.parameters.keys())
    assert "into" in params, "Missing parameter 'into'"

def test_siddhi::into_has_into():
    assert hasattr(siddhi::INTO, "into")
    descriptor = None
    for klass in siddhi::INTO.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::insert_is_not_abstract():
    assert not inspect.isabstract(siddhi::INSERT)


def test_siddhi::insert_constructor_exists():
    assert callable(siddhi::INSERT.__init__)


def test_siddhi::insert_constructor_args():
    sig = inspect.signature(siddhi::INSERT.__init__)
    params = list(sig.parameters.keys())
    assert "insert" in params, "Missing parameter 'insert'"

def test_siddhi::insert_has_insert():
    assert hasattr(siddhi::INSERT, "insert")
    descriptor = None
    for klass in siddhi::INSERT.__mro__:
        if "insert" in klass.__dict__:
            descriptor = klass.__dict__["insert"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::first_is_not_abstract():
    assert not inspect.isabstract(siddhi::FIRST)


def test_siddhi::first_constructor_exists():
    assert callable(siddhi::FIRST.__init__)


def test_siddhi::first_constructor_args():
    sig = inspect.signature(siddhi::FIRST.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"

def test_siddhi::first_has_first():
    assert hasattr(siddhi::FIRST, "first")
    descriptor = None
    for klass in siddhi::FIRST.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::snapshot_is_not_abstract():
    assert not inspect.isabstract(siddhi::SNAPSHOT)


def test_siddhi::snapshot_constructor_exists():
    assert callable(siddhi::SNAPSHOT.__init__)


def test_siddhi::snapshot_constructor_args():
    sig = inspect.signature(siddhi::SNAPSHOT.__init__)
    params = list(sig.parameters.keys())
    assert "snapshot" in params, "Missing parameter 'snapshot'"

def test_siddhi::snapshot_has_snapshot():
    assert hasattr(siddhi::SNAPSHOT, "snapshot")
    descriptor = None
    for klass in siddhi::SNAPSHOT.__mro__:
        if "snapshot" in klass.__dict__:
            descriptor = klass.__dict__["snapshot"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::having_is_not_abstract():
    assert not inspect.isabstract(siddhi::HAVING)


def test_siddhi::having_constructor_exists():
    assert callable(siddhi::HAVING.__init__)


def test_siddhi::having_constructor_args():
    sig = inspect.signature(siddhi::HAVING.__init__)
    params = list(sig.parameters.keys())
    assert "having" in params, "Missing parameter 'having'"

def test_siddhi::having_has_having():
    assert hasattr(siddhi::HAVING, "having")
    descriptor = None
    for klass in siddhi::HAVING.__mro__:
        if "having" in klass.__dict__:
            descriptor = klass.__dict__["having"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::by_is_not_abstract():
    assert not inspect.isabstract(siddhi::BY)


def test_siddhi::by_constructor_exists():
    assert callable(siddhi::BY.__init__)


def test_siddhi::by_constructor_args():
    sig = inspect.signature(siddhi::BY.__init__)
    params = list(sig.parameters.keys())
    assert "by" in params, "Missing parameter 'by'"

def test_siddhi::by_has_by():
    assert hasattr(siddhi::BY, "by")
    descriptor = None
    for klass in siddhi::BY.__mro__:
        if "by" in klass.__dict__:
            descriptor = klass.__dict__["by"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::group_is_not_abstract():
    assert not inspect.isabstract(siddhi::GROUP)


def test_siddhi::group_constructor_exists():
    assert callable(siddhi::GROUP.__init__)


def test_siddhi::group_constructor_args():
    sig = inspect.signature(siddhi::GROUP.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_siddhi::group_has_group():
    assert hasattr(siddhi::GROUP, "group")
    descriptor = None
    for klass in siddhi::GROUP.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::select_is_not_abstract():
    assert not inspect.isabstract(siddhi::SELECT)


def test_siddhi::select_constructor_exists():
    assert callable(siddhi::SELECT.__init__)


def test_siddhi::select_constructor_args():
    sig = inspect.signature(siddhi::SELECT.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_siddhi::select_has_select():
    assert hasattr(siddhi::SELECT, "select")
    descriptor = None
    for klass in siddhi::SELECT.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::double_is_not_abstract():
    assert not inspect.isabstract(siddhi::DOUBLE)


def test_siddhi::double_constructor_exists():
    assert callable(siddhi::DOUBLE.__init__)


def test_siddhi::double_constructor_args():
    sig = inspect.signature(siddhi::DOUBLE.__init__)
    params = list(sig.parameters.keys())
    assert "double" in params, "Missing parameter 'double'"

def test_siddhi::double_has_double():
    assert hasattr(siddhi::DOUBLE, "double")
    descriptor = None
    for klass in siddhi::DOUBLE.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::long_is_not_abstract():
    assert not inspect.isabstract(siddhi::LONG)


def test_siddhi::long_constructor_exists():
    assert callable(siddhi::LONG.__init__)


def test_siddhi::long_constructor_args():
    sig = inspect.signature(siddhi::LONG.__init__)
    params = list(sig.parameters.keys())
    assert "long" in params, "Missing parameter 'long'"

def test_siddhi::long_has_long():
    assert hasattr(siddhi::LONG, "long")
    descriptor = None
    for klass in siddhi::LONG.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::ints_is_not_abstract():
    assert not inspect.isabstract(siddhi::INTS)


def test_siddhi::ints_constructor_exists():
    assert callable(siddhi::INTS.__init__)


def test_siddhi::ints_constructor_args():
    sig = inspect.signature(siddhi::INTS.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_siddhi::ints_has_int():
    assert hasattr(siddhi::INTS, "int")
    descriptor = None
    for klass in siddhi::INTS.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::strings_is_not_abstract():
    assert not inspect.isabstract(siddhi::STRINGS)


def test_siddhi::strings_constructor_exists():
    assert callable(siddhi::STRINGS.__init__)


def test_siddhi::strings_constructor_args():
    sig = inspect.signature(siddhi::STRINGS.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_siddhi::strings_has_string():
    assert hasattr(siddhi::STRINGS, "string")
    descriptor = None
    for klass in siddhi::STRINGS.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::output_is_not_abstract():
    assert not inspect.isabstract(siddhi::OUTPUT)


def test_siddhi::output_constructor_exists():
    assert callable(siddhi::OUTPUT.__init__)


def test_siddhi::output_constructor_args():
    sig = inspect.signature(siddhi::OUTPUT.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"

def test_siddhi::output_has_output():
    assert hasattr(siddhi::OUTPUT, "output")
    descriptor = None
    for klass in siddhi::OUTPUT.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::window_is_not_abstract():
    assert not inspect.isabstract(siddhi::WINDOW)


def test_siddhi::window_constructor_exists():
    assert callable(siddhi::WINDOW.__init__)


def test_siddhi::window_constructor_args():
    sig = inspect.signature(siddhi::WINDOW.__init__)
    params = list(sig.parameters.keys())
    assert "window" in params, "Missing parameter 'window'"

def test_siddhi::window_has_window():
    assert hasattr(siddhi::WINDOW, "window")
    descriptor = None
    for klass in siddhi::WINDOW.__mro__:
        if "window" in klass.__dict__:
            descriptor = klass.__dict__["window"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::table_is_not_abstract():
    assert not inspect.isabstract(siddhi::TABLE)


def test_siddhi::table_constructor_exists():
    assert callable(siddhi::TABLE.__init__)


def test_siddhi::table_constructor_args():
    sig = inspect.signature(siddhi::TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"

def test_siddhi::table_has_table():
    assert hasattr(siddhi::TABLE, "table")
    descriptor = None
    for klass in siddhi::TABLE.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::from_is_not_abstract():
    assert not inspect.isabstract(siddhi::FROM)


def test_siddhi::from_constructor_exists():
    assert callable(siddhi::FROM.__init__)


def test_siddhi::from_constructor_args():
    sig = inspect.signature(siddhi::FROM.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"

def test_siddhi::from_has_from_():
    assert hasattr(siddhi::FROM, "from_")
    descriptor = None
    for klass in siddhi::FROM.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::return_is_not_abstract():
    assert not inspect.isabstract(siddhi::RETURN)


def test_siddhi::return_constructor_exists():
    assert callable(siddhi::RETURN.__init__)


def test_siddhi::return_constructor_args():
    sig = inspect.signature(siddhi::RETURN.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"

def test_siddhi::return_has_return_():
    assert hasattr(siddhi::RETURN, "return_")
    descriptor = None
    for klass in siddhi::RETURN.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::function_is_not_abstract():
    assert not inspect.isabstract(siddhi::FUNCTION)


def test_siddhi::function_constructor_exists():
    assert callable(siddhi::FUNCTION.__init__)


def test_siddhi::function_constructor_args():
    sig = inspect.signature(siddhi::FUNCTION.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_siddhi::function_has_function():
    assert hasattr(siddhi::FUNCTION, "function")
    descriptor = None
    for klass in siddhi::FUNCTION.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::at_is_not_abstract():
    assert not inspect.isabstract(siddhi::AT)


def test_siddhi::at_constructor_exists():
    assert callable(siddhi::AT.__init__)


def test_siddhi::at_constructor_args():
    sig = inspect.signature(siddhi::AT.__init__)
    params = list(sig.parameters.keys())
    assert "at" in params, "Missing parameter 'at'"

def test_siddhi::at_has_at():
    assert hasattr(siddhi::AT, "at")
    descriptor = None
    for klass in siddhi::AT.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::trigger_is_not_abstract():
    assert not inspect.isabstract(siddhi::TRIGGER)


def test_siddhi::trigger_constructor_exists():
    assert callable(siddhi::TRIGGER.__init__)


def test_siddhi::trigger_constructor_args():
    sig = inspect.signature(siddhi::TRIGGER.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_siddhi::trigger_has_trigger():
    assert hasattr(siddhi::TRIGGER, "trigger")
    descriptor = None
    for klass in siddhi::TRIGGER.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::null_is_not_abstract():
    assert not inspect.isabstract(siddhi::NULL)


def test_siddhi::null_constructor_exists():
    assert callable(siddhi::NULL.__init__)


def test_siddhi::null_constructor_args():
    sig = inspect.signature(siddhi::NULL.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_siddhi::null_has_null():
    assert hasattr(siddhi::NULL, "null")
    descriptor = None
    for klass in siddhi::NULL.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::is_is_not_abstract():
    assert not inspect.isabstract(siddhi::IS)


def test_siddhi::is_constructor_exists():
    assert callable(siddhi::IS.__init__)


def test_siddhi::is_constructor_args():
    sig = inspect.signature(siddhi::IS.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"

def test_siddhi::is_has_is_():
    assert hasattr(siddhi::IS, "is_")
    descriptor = None
    for klass in siddhi::IS.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::last_is_not_abstract():
    assert not inspect.isabstract(siddhi::LAST)


def test_siddhi::last_constructor_exists():
    assert callable(siddhi::LAST.__init__)


def test_siddhi::last_constructor_args():
    sig = inspect.signature(siddhi::LAST.__init__)
    params = list(sig.parameters.keys())
    assert "last" in params, "Missing parameter 'last'"

def test_siddhi::last_has_last():
    assert hasattr(siddhi::LAST, "last")
    descriptor = None
    for klass in siddhi::LAST.__mro__:
        if "last" in klass.__dict__:
            descriptor = klass.__dict__["last"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::current_is_not_abstract():
    assert not inspect.isabstract(siddhi::CURRENT)


def test_siddhi::current_constructor_exists():
    assert callable(siddhi::CURRENT.__init__)


def test_siddhi::current_constructor_args():
    sig = inspect.signature(siddhi::CURRENT.__init__)
    params = list(sig.parameters.keys())
    assert "currt" in params, "Missing parameter 'currt'"

def test_siddhi::current_has_currt():
    assert hasattr(siddhi::CURRENT, "currt")
    descriptor = None
    for klass in siddhi::CURRENT.__mro__:
        if "currt" in klass.__dict__:
            descriptor = klass.__dict__["currt"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::expired_is_not_abstract():
    assert not inspect.isabstract(siddhi::EXPIRED)


def test_siddhi::expired_constructor_exists():
    assert callable(siddhi::EXPIRED.__init__)


def test_siddhi::expired_constructor_args():
    sig = inspect.signature(siddhi::EXPIRED.__init__)
    params = list(sig.parameters.keys())
    assert "expired" in params, "Missing parameter 'expired'"

def test_siddhi::expired_has_expired():
    assert hasattr(siddhi::EXPIRED, "expired")
    descriptor = None
    for klass in siddhi::EXPIRED.__mro__:
        if "expired" in klass.__dict__:
            descriptor = klass.__dict__["expired"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::raw_is_not_abstract():
    assert not inspect.isabstract(siddhi::RAW)


def test_siddhi::raw_constructor_exists():
    assert callable(siddhi::RAW.__init__)


def test_siddhi::raw_constructor_args():
    sig = inspect.signature(siddhi::RAW.__init__)
    params = list(sig.parameters.keys())
    assert "raw" in params, "Missing parameter 'raw'"

def test_siddhi::raw_has_raw():
    assert hasattr(siddhi::RAW, "raw")
    descriptor = None
    for klass in siddhi::RAW.__mro__:
        if "raw" in klass.__dict__:
            descriptor = klass.__dict__["raw"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::events_is_not_abstract():
    assert not inspect.isabstract(siddhi::EVENTS)


def test_siddhi::events_constructor_exists():
    assert callable(siddhi::EVENTS.__init__)


def test_siddhi::events_constructor_args():
    sig = inspect.signature(siddhi::EVENTS.__init__)
    params = list(sig.parameters.keys())
    assert "events" in params, "Missing parameter 'events'"

def test_siddhi::events_has_events():
    assert hasattr(siddhi::EVENTS, "events")
    descriptor = None
    for klass in siddhi::EVENTS.__mro__:
        if "events" in klass.__dict__:
            descriptor = klass.__dict__["events"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::all_is_not_abstract():
    assert not inspect.isabstract(siddhi::ALL)


def test_siddhi::all_constructor_exists():
    assert callable(siddhi::ALL.__init__)


def test_siddhi::all_constructor_args():
    sig = inspect.signature(siddhi::ALL.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_siddhi::all_has_all():
    assert hasattr(siddhi::ALL, "all")
    descriptor = None
    for klass in siddhi::ALL.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::object_is_not_abstract():
    assert not inspect.isabstract(siddhi::OBJECT)


def test_siddhi::object_constructor_exists():
    assert callable(siddhi::OBJECT.__init__)


def test_siddhi::object_constructor_args():
    sig = inspect.signature(siddhi::OBJECT.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"

def test_siddhi::object_has_object():
    assert hasattr(siddhi::OBJECT, "object")
    descriptor = None
    for klass in siddhi::OBJECT.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::bool_is_not_abstract():
    assert not inspect.isabstract(siddhi::BOOL)


def test_siddhi::bool_constructor_exists():
    assert callable(siddhi::BOOL.__init__)


def test_siddhi::bool_constructor_args():
    sig = inspect.signature(siddhi::BOOL.__init__)
    params = list(sig.parameters.keys())
    assert "bool" in params, "Missing parameter 'bool'"

def test_siddhi::bool_has_bool():
    assert hasattr(siddhi::BOOL, "bool")
    descriptor = None
    for klass in siddhi::BOOL.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::float_is_not_abstract():
    assert not inspect.isabstract(siddhi::FLOAT)


def test_siddhi::float_constructor_exists():
    assert callable(siddhi::FLOAT.__init__)


def test_siddhi::float_constructor_args():
    sig = inspect.signature(siddhi::FLOAT.__init__)
    params = list(sig.parameters.keys())
    assert "float" in params, "Missing parameter 'float'"

def test_siddhi::float_has_float():
    assert hasattr(siddhi::FLOAT, "float")
    descriptor = None
    for klass in siddhi::FLOAT.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)



def test_everyabsentsequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(EveryAbsentSequenceSourceChain)


def test_everyabsentsequencesourcechain_constructor_exists():
    assert callable(EveryAbsentSequenceSourceChain.__init__)


def test_everyabsentsequencesourcechain_constructor_args():
    sig = inspect.signature(EveryAbsentSequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_everysequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(EverySequenceSourceChain)


def test_everysequencesourcechain_constructor_exists():
    assert callable(EverySequenceSourceChain.__init__)


def test_everysequencesourcechain_constructor_args():
    sig = inspect.signature(EverySequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_basicabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(BasicAbsentPatternSource)


def test_basicabsentpatternsource_constructor_exists():
    assert callable(BasicAbsentPatternSource.__init__)


def test_basicabsentpatternsource_constructor_args():
    sig = inspect.signature(BasicAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::define_is_not_abstract():
    assert not inspect.isabstract(siddhi::DEFINE)


def test_siddhi::define_constructor_exists():
    assert callable(siddhi::DEFINE.__init__)


def test_siddhi::define_constructor_args():
    sig = inspect.signature(siddhi::DEFINE.__init__)
    params = list(sig.parameters.keys())
    assert "define" in params, "Missing parameter 'define'"

def test_siddhi::define_has_define():
    assert hasattr(siddhi::DEFINE, "define")
    descriptor = None
    for klass in siddhi::DEFINE.__mro__:
        if "define" in klass.__dict__:
            descriptor = klass.__dict__["define"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::stream_is_not_abstract():
    assert not inspect.isabstract(siddhi::STREAM)


def test_siddhi::stream_constructor_exists():
    assert callable(siddhi::STREAM.__init__)


def test_siddhi::stream_constructor_args():
    sig = inspect.signature(siddhi::STREAM.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_siddhi::stream_has_str():
    assert hasattr(siddhi::STREAM, "str")
    descriptor = None
    for klass in siddhi::STREAM.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_appannotation_is_not_abstract():
    assert not inspect.isabstract(AppAnnotation)


def test_appannotation_constructor_exists():
    assert callable(AppAnnotation.__init__)


def test_appannotation_constructor_args():
    sig = inspect.signature(AppAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::app_is_not_abstract():
    assert not inspect.isabstract(siddhi::APP)


def test_siddhi::app_constructor_exists():
    assert callable(siddhi::APP.__init__)


def test_siddhi::app_constructor_args():
    sig = inspect.signature(siddhi::APP.__init__)
    params = list(sig.parameters.keys())
    assert "ap" in params, "Missing parameter 'ap'"

def test_siddhi::app_has_ap():
    assert hasattr(siddhi::APP, "ap")
    descriptor = None
    for klass in siddhi::APP.__mro__:
        if "ap" in klass.__dict__:
            descriptor = klass.__dict__["ap"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::in_is_not_abstract():
    assert not inspect.isabstract(siddhi::IN)


def test_siddhi::in_constructor_exists():
    assert callable(siddhi::IN.__init__)


def test_siddhi::in_constructor_args():
    sig = inspect.signature(siddhi::IN.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_siddhi::in_has_in_():
    assert hasattr(siddhi::IN, "in_")
    descriptor = None
    for klass in siddhi::IN.__mro__:
        if "in_" in klass.__dict__:
            descriptor = klass.__dict__["in_"]
            break
    assert isinstance(descriptor, property)



def test_rightabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(RightAbsentPatternSource)


def test_rightabsentpatternsource_constructor_exists():
    assert callable(RightAbsentPatternSource.__init__)


def test_rightabsentpatternsource_constructor_args():
    sig = inspect.signature(RightAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_leftabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(LeftAbsentPatternSource)


def test_leftabsentpatternsource_constructor_exists():
    assert callable(LeftAbsentPatternSource.__init__)


def test_leftabsentpatternsource_constructor_args():
    sig = inspect.signature(LeftAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_everyabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(EveryAbsentPatternSource)


def test_everyabsentpatternsource_constructor_exists():
    assert callable(EveryAbsentPatternSource.__init__)


def test_everyabsentpatternsource_constructor_args():
    sig = inspect.signature(EveryAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_logicalabsentstatefulsource_is_not_abstract():
    assert not inspect.isabstract(LogicalAbsentStatefulSource)


def test_logicalabsentstatefulsource_constructor_exists():
    assert callable(LogicalAbsentStatefulSource.__init__)


def test_logicalabsentstatefulsource_constructor_args():
    sig = inspect.signature(LogicalAbsentStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::l_is_not_abstract():
    assert not inspect.isabstract(siddhi::L)


def test_siddhi::l_constructor_exists():
    assert callable(siddhi::L.__init__)


def test_siddhi::l_constructor_args():
    sig = inspect.signature(siddhi::L.__init__)
    params = list(sig.parameters.keys())
    assert "l" in params, "Missing parameter 'l'"

def test_siddhi::l_has_l():
    assert hasattr(siddhi::L, "l")
    descriptor = None
    for klass in siddhi::L.__mro__:
        if "l" in klass.__dict__:
            descriptor = klass.__dict__["l"]
            break
    assert isinstance(descriptor, property)



def test_signedlongvalue_is_not_abstract():
    assert not inspect.isabstract(SignedLongValue)


def test_signedlongvalue_constructor_exists():
    assert callable(SignedLongValue.__init__)


def test_signedlongvalue_constructor_args():
    sig = inspect.signature(SignedLongValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::long::literal_is_not_abstract():
    assert not inspect.isabstract(siddhi::LONG::LITERAL)


def test_siddhi::long::literal_constructor_exists():
    assert callable(siddhi::LONG::LITERAL.__init__)


def test_siddhi::long::literal_constructor_args():
    sig = inspect.signature(siddhi::LONG::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::f_is_not_abstract():
    assert not inspect.isabstract(siddhi::F)


def test_siddhi::f_constructor_exists():
    assert callable(siddhi::F.__init__)


def test_siddhi::f_constructor_args():
    sig = inspect.signature(siddhi::F.__init__)
    params = list(sig.parameters.keys())
    assert "f" in params, "Missing parameter 'f'"

def test_siddhi::f_has_f():
    assert hasattr(siddhi::F, "f")
    descriptor = None
    for klass in siddhi::F.__mro__:
        if "f" in klass.__dict__:
            descriptor = klass.__dict__["f"]
            break
    assert isinstance(descriptor, property)



def test_signedfloatvalue_is_not_abstract():
    assert not inspect.isabstract(SignedFloatValue)


def test_signedfloatvalue_constructor_exists():
    assert callable(SignedFloatValue.__init__)


def test_signedfloatvalue_constructor_args():
    sig = inspect.signature(SignedFloatValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::float::literal_is_not_abstract():
    assert not inspect.isabstract(siddhi::FLOAT::LITERAL)


def test_siddhi::float::literal_constructor_exists():
    assert callable(siddhi::FLOAT::LITERAL.__init__)


def test_siddhi::float::literal_constructor_args():
    sig = inspect.signature(siddhi::FLOAT::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::d_is_not_abstract():
    assert not inspect.isabstract(siddhi::D)


def test_siddhi::d_constructor_exists():
    assert callable(siddhi::D.__init__)


def test_siddhi::d_constructor_args():
    sig = inspect.signature(siddhi::D.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"

def test_siddhi::d_has_d():
    assert hasattr(siddhi::D, "d")
    descriptor = None
    for klass in siddhi::D.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::e_is_not_abstract():
    assert not inspect.isabstract(siddhi::E)


def test_siddhi::e_constructor_exists():
    assert callable(siddhi::E.__init__)


def test_siddhi::e_constructor_args():
    sig = inspect.signature(siddhi::E.__init__)
    params = list(sig.parameters.keys())
    assert "e" in params, "Missing parameter 'e'"

def test_siddhi::e_has_e():
    assert hasattr(siddhi::E, "e")
    descriptor = None
    for klass in siddhi::E.__mro__:
        if "e" in klass.__dict__:
            descriptor = klass.__dict__["e"]
            break
    assert isinstance(descriptor, property)



def test_signeddoublevalue_is_not_abstract():
    assert not inspect.isabstract(SignedDoubleValue)


def test_signeddoublevalue_constructor_exists():
    assert callable(SignedDoubleValue.__init__)


def test_signeddoublevalue_constructor_args():
    sig = inspect.signature(SignedDoubleValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::double::literal_is_not_abstract():
    assert not inspect.isabstract(siddhi::DOUBLE::LITERAL)


def test_siddhi::double::literal_constructor_exists():
    assert callable(siddhi::DOUBLE::LITERAL.__init__)


def test_siddhi::double::literal_constructor_args():
    sig = inspect.signature(siddhi::DOUBLE::LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_milliseconds_is_not_abstract():
    assert not inspect.isabstract(MILLISECONDS)


def test_milliseconds_constructor_exists():
    assert callable(MILLISECONDS.__init__)


def test_milliseconds_constructor_args():
    sig = inspect.signature(MILLISECONDS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::millisecondvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::MillisecondValue)


def test_siddhi::millisecondvalue_constructor_exists():
    assert callable(siddhi::MillisecondValue.__init__)


def test_siddhi::millisecondvalue_constructor_args():
    sig = inspect.signature(siddhi::MillisecondValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::functionid_is_not_abstract():
    assert not inspect.isabstract(siddhi::FunctionId)


def test_siddhi::functionid_constructor_exists():
    assert callable(siddhi::FunctionId.__init__)


def test_siddhi::functionid_constructor_args():
    sig = inspect.signature(siddhi::FunctionId.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::functionnamespace_is_not_abstract():
    assert not inspect.isabstract(siddhi::FunctionNamespace)


def test_siddhi::functionnamespace_constructor_exists():
    assert callable(siddhi::FunctionNamespace.__init__)


def test_siddhi::functionnamespace_constructor_args():
    sig = inspect.signature(siddhi::FunctionNamespace.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::signedlongvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::SignedLongValue)


def test_siddhi::signedlongvalue_constructor_exists():
    assert callable(siddhi::SignedLongValue.__init__)


def test_siddhi::signedlongvalue_constructor_args():
    sig = inspect.signature(siddhi::SignedLongValue.__init__)
    params = list(sig.parameters.keys())



def test_false_is_not_abstract():
    assert not inspect.isabstract(FALSE)


def test_false_constructor_exists():
    assert callable(FALSE.__init__)


def test_false_constructor_args():
    sig = inspect.signature(FALSE.__init__)
    params = list(sig.parameters.keys())



def test_true_is_not_abstract():
    assert not inspect.isabstract(TRUE)


def test_true_constructor_exists():
    assert callable(TRUE.__init__)


def test_true_constructor_args():
    sig = inspect.signature(TRUE.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::attributelist_is_not_abstract():
    assert not inspect.isabstract(siddhi::AttributeList)


def test_siddhi::attributelist_constructor_exists():
    assert callable(siddhi::AttributeList.__init__)


def test_siddhi::attributelist_constructor_args():
    sig = inspect.signature(siddhi::AttributeList.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::featuresoroutattr_is_not_abstract():
    assert not inspect.isabstract(siddhi::FeaturesOrOutAttr)


def test_siddhi::featuresoroutattr_constructor_exists():
    assert callable(siddhi::FeaturesOrOutAttr.__init__)


def test_siddhi::featuresoroutattr_constructor_args():
    sig = inspect.signature(siddhi::FeaturesOrOutAttr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_siddhi::featuresoroutattr_has_name():
    assert hasattr(siddhi::FeaturesOrOutAttr, "name")
    descriptor = None
    for klass in siddhi::FeaturesOrOutAttr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::featuresoroutattrreference_is_not_abstract():
    assert not inspect.isabstract(siddhi::FeaturesOrOutAttrReference)


def test_siddhi::featuresoroutattrreference_constructor_exists():
    assert callable(siddhi::FeaturesOrOutAttrReference.__init__)


def test_siddhi::featuresoroutattrreference_constructor_args():
    sig = inspect.signature(siddhi::FeaturesOrOutAttrReference.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::signedfloatvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::SignedFloatValue)


def test_siddhi::signedfloatvalue_constructor_exists():
    assert callable(siddhi::SignedFloatValue.__init__)


def test_siddhi::signedfloatvalue_constructor_args():
    sig = inspect.signature(siddhi::SignedFloatValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::signeddoublevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::SignedDoubleValue)


def test_siddhi::signeddoublevalue_constructor_exists():
    assert callable(siddhi::SignedDoubleValue.__init__)


def test_siddhi::signeddoublevalue_constructor_args():
    sig = inspect.signature(siddhi::SignedDoubleValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::boolvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::BoolValue)


def test_siddhi::boolvalue_constructor_exists():
    assert callable(siddhi::BoolValue.__init__)


def test_siddhi::boolvalue_constructor_args():
    sig = inspect.signature(siddhi::BoolValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::attributenamereference_is_not_abstract():
    assert not inspect.isabstract(siddhi::AttributeNameReference)


def test_siddhi::attributenamereference_constructor_exists():
    assert callable(siddhi::AttributeNameReference.__init__)


def test_siddhi::attributenamereference_constructor_args():
    sig = inspect.signature(siddhi::AttributeNameReference.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::source1orstandardstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::Source1OrStandardStatefulSource)


def test_siddhi::source1orstandardstatefulsource_constructor_exists():
    assert callable(siddhi::Source1OrStandardStatefulSource.__init__)


def test_siddhi::source1orstandardstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::Source1OrStandardStatefulSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_siddhi::source1orstandardstatefulsource_has_name():
    assert hasattr(siddhi::Source1OrStandardStatefulSource, "name")
    descriptor = None
    for klass in siddhi::Source1OrStandardStatefulSource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_patterncollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(PatternCollectionStatefulSource)


def test_patterncollectionstatefulsource_constructor_exists():
    assert callable(PatternCollectionStatefulSource.__init__)


def test_patterncollectionstatefulsource_constructor_args():
    sig = inspect.signature(PatternCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_sequencecollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(SequenceCollectionStatefulSource)


def test_sequencecollectionstatefulsource_constructor_exists():
    assert callable(SequenceCollectionStatefulSource.__init__)


def test_sequencecollectionstatefulsource_constructor_args():
    sig = inspect.signature(SequenceCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::literal_is_not_abstract():
    assert not inspect.isabstract(siddhi::Literal)


def test_siddhi::literal_constructor_exists():
    assert callable(siddhi::Literal.__init__)


def test_siddhi::literal_constructor_args():
    sig = inspect.signature(siddhi::Literal.__init__)
    params = list(sig.parameters.keys())



def test_mathdivmuloperation_is_not_abstract():
    assert not inspect.isabstract(MathDivmulOperation)


def test_mathdivmuloperation_constructor_exists():
    assert callable(MathDivmulOperation.__init__)


def test_mathdivmuloperation_constructor_args():
    sig = inspect.signature(MathDivmulOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathotheroperations_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathOtherOperations)


def test_siddhi::mathotheroperations_constructor_exists():
    assert callable(siddhi::MathOtherOperations.__init__)


def test_siddhi::mathotheroperations_constructor_args():
    sig = inspect.signature(siddhi::MathOtherOperations.__init__)
    params = list(sig.parameters.keys())



def test_mathaddsuboperation_is_not_abstract():
    assert not inspect.isabstract(MathAddsubOperation)


def test_mathaddsuboperation_constructor_exists():
    assert callable(MathAddsubOperation.__init__)


def test_mathaddsuboperation_constructor_args():
    sig = inspect.signature(MathAddsubOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathdivmuloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathDivmulOperation)


def test_siddhi::mathdivmuloperation_constructor_exists():
    assert callable(siddhi::MathDivmulOperation.__init__)


def test_siddhi::mathdivmuloperation_constructor_args():
    sig = inspect.signature(siddhi::MathDivmulOperation.__init__)
    params = list(sig.parameters.keys())
    assert "multiply" in params, "Missing parameter 'multiply'"
    assert "devide" in params, "Missing parameter 'devide'"
    assert "mod" in params, "Missing parameter 'mod'"

def test_siddhi::mathdivmuloperation_has_multiply():
    assert hasattr(siddhi::MathDivmulOperation, "multiply")
    descriptor = None
    for klass in siddhi::MathDivmulOperation.__mro__:
        if "multiply" in klass.__dict__:
            descriptor = klass.__dict__["multiply"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathdivmuloperation_has_devide():
    assert hasattr(siddhi::MathDivmulOperation, "devide")
    descriptor = None
    for klass in siddhi::MathDivmulOperation.__mro__:
        if "devide" in klass.__dict__:
            descriptor = klass.__dict__["devide"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathdivmuloperation_has_mod():
    assert hasattr(siddhi::MathDivmulOperation, "mod")
    descriptor = None
    for klass in siddhi::MathDivmulOperation.__mro__:
        if "mod" in klass.__dict__:
            descriptor = klass.__dict__["mod"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::sourceoreventreference_is_not_abstract():
    assert not inspect.isabstract(siddhi::SourceOrEventReference)


def test_siddhi::sourceoreventreference_constructor_exists():
    assert callable(siddhi::SourceOrEventReference.__init__)


def test_siddhi::sourceoreventreference_constructor_args():
    sig = inspect.signature(siddhi::SourceOrEventReference.__init__)
    params = list(sig.parameters.keys())



def test_setassignment_is_not_abstract():
    assert not inspect.isabstract(SetAssignment)


def test_setassignment_constructor_exists():
    assert callable(SetAssignment.__init__)


def test_setassignment_constructor_args():
    sig = inspect.signature(SetAssignment.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::constantvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::ConstantValue)


def test_siddhi::constantvalue_constructor_exists():
    assert callable(siddhi::ConstantValue.__init__)


def test_siddhi::constantvalue_constructor_args():
    sig = inspect.signature(siddhi::ConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "siv" in params, "Missing parameter 'siv'"

def test_siddhi::constantvalue_has_siv():
    assert hasattr(siddhi::ConstantValue, "siv")
    descriptor = None
    for klass in siddhi::ConstantValue.__mro__:
        if "siv" in klass.__dict__:
            descriptor = klass.__dict__["siv"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::streamreference_is_not_abstract():
    assert not inspect.isabstract(siddhi::StreamReference)


def test_siddhi::streamreference_constructor_exists():
    assert callable(siddhi::StreamReference.__init__)


def test_siddhi::streamreference_constructor_args():
    sig = inspect.signature(siddhi::StreamReference.__init__)
    params = list(sig.parameters.keys())
    assert "hash" in params, "Missing parameter 'hash'"

def test_siddhi::streamreference_has_hash():
    assert hasattr(siddhi::StreamReference, "hash")
    descriptor = None
    for klass in siddhi::StreamReference.__mro__:
        if "hash" in klass.__dict__:
            descriptor = klass.__dict__["hash"]
            break
    assert isinstance(descriptor, property)



def test_null_is_not_abstract():
    assert not inspect.isabstract(NULL)


def test_null_constructor_exists():
    assert callable(NULL.__init__)


def test_null_constructor_args():
    sig = inspect.signature(NULL.__init__)
    params = list(sig.parameters.keys())



def test_is_is_not_abstract():
    assert not inspect.isabstract(IS)


def test_is_constructor_exists():
    assert callable(IS.__init__)


def test_is_constructor_args():
    sig = inspect.signature(IS.__init__)
    params = list(sig.parameters.keys())



def test_mathotheroperations_is_not_abstract():
    assert not inspect.isabstract(MathOtherOperations)


def test_mathotheroperations_constructor_exists():
    assert callable(MathOtherOperations.__init__)


def test_mathotheroperations_constructor_args():
    sig = inspect.signature(MathOtherOperations.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::nullcheck_is_not_abstract():
    assert not inspect.isabstract(siddhi::NullCheck)


def test_siddhi::nullcheck_constructor_exists():
    assert callable(siddhi::NullCheck.__init__)


def test_siddhi::nullcheck_constructor_args():
    sig = inspect.signature(siddhi::NullCheck.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::basicsourcestreamhandlers_is_not_abstract():
    assert not inspect.isabstract(siddhi::BasicSourceStreamHandlers)


def test_siddhi::basicsourcestreamhandlers_constructor_exists():
    assert callable(siddhi::BasicSourceStreamHandlers.__init__)


def test_siddhi::basicsourcestreamhandlers_constructor_args():
    sig = inspect.signature(siddhi::BasicSourceStreamHandlers.__init__)
    params = list(sig.parameters.keys())



def test_mathoperation_is_not_abstract():
    assert not inspect.isabstract(MathOperation)


def test_mathoperation_constructor_exists():
    assert callable(MathOperation.__init__)


def test_mathoperation_constructor_args():
    sig = inspect.signature(MathOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathaddsuboperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathAddsubOperation)


def test_siddhi::mathaddsuboperation_constructor_exists():
    assert callable(siddhi::MathAddsubOperation.__init__)


def test_siddhi::mathaddsuboperation_constructor_args():
    sig = inspect.signature(siddhi::MathAddsubOperation.__init__)
    params = list(sig.parameters.keys())
    assert "substract" in params, "Missing parameter 'substract'"
    assert "add" in params, "Missing parameter 'add'"

def test_siddhi::mathaddsuboperation_has_substract():
    assert hasattr(siddhi::MathAddsubOperation, "substract")
    descriptor = None
    for klass in siddhi::MathAddsubOperation.__mro__:
        if "substract" in klass.__dict__:
            descriptor = klass.__dict__["substract"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathaddsuboperation_has_add():
    assert hasattr(siddhi::MathAddsubOperation, "add")
    descriptor = None
    for klass in siddhi::MathAddsubOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathOperation)


def test_siddhi::mathoperation_constructor_exists():
    assert callable(siddhi::MathOperation.__init__)


def test_siddhi::mathoperation_constructor_args():
    sig = inspect.signature(siddhi::MathOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::streamfunction_is_not_abstract():
    assert not inspect.isabstract(siddhi::StreamFunction)


def test_siddhi::streamfunction_constructor_exists():
    assert callable(siddhi::StreamFunction.__init__)


def test_siddhi::streamfunction_constructor_args():
    sig = inspect.signature(siddhi::StreamFunction.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::filter_is_not_abstract():
    assert not inspect.isabstract(siddhi::Filter)


def test_siddhi::filter_constructor_exists():
    assert callable(siddhi::Filter.__init__)


def test_siddhi::filter_constructor_args():
    sig = inspect.signature(siddhi::Filter.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::basicsourcestreamhandler_is_not_abstract():
    assert not inspect.isabstract(siddhi::BasicSourceStreamHandler)


def test_siddhi::basicsourcestreamhandler_constructor_exists():
    assert callable(siddhi::BasicSourceStreamHandler.__init__)


def test_siddhi::basicsourcestreamhandler_constructor_args():
    sig = inspect.signature(siddhi::BasicSourceStreamHandler.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::unidirectional_is_not_abstract():
    assert not inspect.isabstract(siddhi::UNIDIRECTIONAL)


def test_siddhi::unidirectional_constructor_exists():
    assert callable(siddhi::UNIDIRECTIONAL.__init__)


def test_siddhi::unidirectional_constructor_args():
    sig = inspect.signature(siddhi::UNIDIRECTIONAL.__init__)
    params = list(sig.parameters.keys())
    assert "unidirectional" in params, "Missing parameter 'unidirectional'"

def test_siddhi::unidirectional_has_unidirectional():
    assert hasattr(siddhi::UNIDIRECTIONAL, "unidirectional")
    descriptor = None
    for klass in siddhi::UNIDIRECTIONAL.__mro__:
        if "unidirectional" in klass.__dict__:
            descriptor = klass.__dict__["unidirectional"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::joinsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::JoinSource)


def test_siddhi::joinsource_constructor_exists():
    assert callable(siddhi::JoinSource.__init__)


def test_siddhi::joinsource_constructor_args():
    sig = inspect.signature(siddhi::JoinSource.__init__)
    params = list(sig.parameters.keys())



def test_standardstream_is_not_abstract():
    assert not inspect.isabstract(StandardStream)


def test_standardstream_constructor_exists():
    assert callable(StandardStream.__init__)


def test_standardstream_constructor_args():
    sig = inspect.signature(StandardStream.__init__)
    params = list(sig.parameters.keys())



def test_joinsource_is_not_abstract():
    assert not inspect.isabstract(JoinSource)


def test_joinsource_constructor_exists():
    assert callable(JoinSource.__init__)


def test_joinsource_constructor_args():
    sig = inspect.signature(JoinSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mainsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::MainSource)


def test_siddhi::mainsource_constructor_exists():
    assert callable(siddhi::MainSource.__init__)


def test_siddhi::mainsource_constructor_args():
    sig = inspect.signature(siddhi::MainSource.__init__)
    params = list(sig.parameters.keys())



def test_joinstream_is_not_abstract():
    assert not inspect.isabstract(JoinStream)


def test_joinstream_constructor_exists():
    assert callable(JoinStream.__init__)


def test_joinstream_constructor_args():
    sig = inspect.signature(JoinStream.__init__)
    params = list(sig.parameters.keys())



def test_inner_is_not_abstract():
    assert not inspect.isabstract(INNER)


def test_inner_constructor_exists():
    assert callable(INNER.__init__)


def test_inner_constructor_args():
    sig = inspect.signature(INNER.__init__)
    params = list(sig.parameters.keys())



def test_full_is_not_abstract():
    assert not inspect.isabstract(FULL)


def test_full_constructor_exists():
    assert callable(FULL.__init__)


def test_full_constructor_args():
    sig = inspect.signature(FULL.__init__)
    params = list(sig.parameters.keys())



def test_right_is_not_abstract():
    assert not inspect.isabstract(RIGHT)


def test_right_constructor_exists():
    assert callable(RIGHT.__init__)


def test_right_constructor_args():
    sig = inspect.signature(RIGHT.__init__)
    params = list(sig.parameters.keys())



def test_join_is_not_abstract():
    assert not inspect.isabstract(JOIN)


def test_join_constructor_exists():
    assert callable(JOIN.__init__)


def test_join_constructor_args():
    sig = inspect.signature(JOIN.__init__)
    params = list(sig.parameters.keys())



def test_outer_is_not_abstract():
    assert not inspect.isabstract(OUTER)


def test_outer_constructor_exists():
    assert callable(OUTER.__init__)


def test_outer_constructor_args():
    sig = inspect.signature(OUTER.__init__)
    params = list(sig.parameters.keys())



def test_left_is_not_abstract():
    assert not inspect.isabstract(LEFT)


def test_left_constructor_exists():
    assert callable(LEFT.__init__)


def test_left_constructor_args():
    sig = inspect.signature(LEFT.__init__)
    params = list(sig.parameters.keys())



def test_per_is_not_abstract():
    assert not inspect.isabstract(PER)


def test_per_constructor_exists():
    assert callable(PER.__init__)


def test_per_constructor_args():
    sig = inspect.signature(PER.__init__)
    params = list(sig.parameters.keys())



def test_within_is_not_abstract():
    assert not inspect.isabstract(WITHIN)


def test_within_constructor_exists():
    assert callable(WITHIN.__init__)


def test_within_constructor_args():
    sig = inspect.signature(WITHIN.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::joins_is_not_abstract():
    assert not inspect.isabstract(siddhi::joins)


def test_siddhi::joins_constructor_exists():
    assert callable(siddhi::joins.__init__)


def test_siddhi::joins_constructor_args():
    sig = inspect.signature(siddhi::joins.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::per1_is_not_abstract():
    assert not inspect.isabstract(siddhi::Per1)


def test_siddhi::per1_constructor_exists():
    assert callable(siddhi::Per1.__init__)


def test_siddhi::per1_constructor_args():
    sig = inspect.signature(siddhi::Per1.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::withintimerange_is_not_abstract():
    assert not inspect.isabstract(siddhi::WithinTimeRange)


def test_siddhi::withintimerange_constructor_exists():
    assert callable(siddhi::WithinTimeRange.__init__)


def test_siddhi::withintimerange_constructor_args():
    sig = inspect.signature(siddhi::WithinTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_absentpatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(AbsentPatternSourceChain)


def test_absentpatternsourcechain_constructor_exists():
    assert callable(AbsentPatternSourceChain.__init__)


def test_absentpatternsourcechain_constructor_args():
    sig = inspect.signature(AbsentPatternSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::everyabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::EveryAbsentPatternSource)


def test_siddhi::everyabsentpatternsource_constructor_exists():
    assert callable(siddhi::EveryAbsentPatternSource.__init__)


def test_siddhi::everyabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi::EveryAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::rightabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::RightAbsentPatternSource)


def test_siddhi::rightabsentpatternsource_constructor_exists():
    assert callable(siddhi::RightAbsentPatternSource.__init__)


def test_siddhi::rightabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi::RightAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())
    assert "fb2" in params, "Missing parameter 'fb2'"

def test_siddhi::rightabsentpatternsource_has_fb2():
    assert hasattr(siddhi::RightAbsentPatternSource, "fb2")
    descriptor = None
    for klass in siddhi::RightAbsentPatternSource.__mro__:
        if "fb2" in klass.__dict__:
            descriptor = klass.__dict__["fb2"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::leftabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::LeftAbsentPatternSource)


def test_siddhi::leftabsentpatternsource_constructor_exists():
    assert callable(siddhi::LeftAbsentPatternSource.__init__)


def test_siddhi::leftabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi::LeftAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())
    assert "fb1" in params, "Missing parameter 'fb1'"

def test_siddhi::leftabsentpatternsource_has_fb1():
    assert hasattr(siddhi::LeftAbsentPatternSource, "fb1")
    descriptor = None
    for klass in siddhi::LeftAbsentPatternSource.__mro__:
        if "fb1" in klass.__dict__:
            descriptor = klass.__dict__["fb1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::patterncollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::PatternCollectionStatefulSource)


def test_siddhi::patterncollectionstatefulsource_constructor_exists():
    assert callable(siddhi::PatternCollectionStatefulSource.__init__)


def test_siddhi::patterncollectionstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::PatternCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::patternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::PatternSource)


def test_siddhi::patternsource_constructor_exists():
    assert callable(siddhi::PatternSource.__init__)


def test_siddhi::patternsource_constructor_args():
    sig = inspect.signature(siddhi::PatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::basicsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::BasicSource)


def test_siddhi::basicsource_constructor_exists():
    assert callable(siddhi::BasicSource.__init__)


def test_siddhi::basicsource_constructor_args():
    sig = inspect.signature(siddhi::BasicSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::not_is_not_abstract():
    assert not inspect.isabstract(siddhi::NOT)


def test_siddhi::not_constructor_exists():
    assert callable(siddhi::NOT.__init__)


def test_siddhi::not_constructor_args():
    sig = inspect.signature(siddhi::NOT.__init__)
    params = list(sig.parameters.keys())
    assert "not1" in params, "Missing parameter 'not1'"

def test_siddhi::not_has_not1():
    assert hasattr(siddhi::NOT, "not1")
    descriptor = None
    for klass in siddhi::NOT.__mro__:
        if "not1" in klass.__dict__:
            descriptor = klass.__dict__["not1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::collect_is_not_abstract():
    assert not inspect.isabstract(siddhi::Collect)


def test_siddhi::collect_constructor_exists():
    assert callable(siddhi::Collect.__init__)


def test_siddhi::collect_constructor_args():
    sig = inspect.signature(siddhi::Collect.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_siddhi::collect_has_start():
    assert hasattr(siddhi::Collect, "start")
    descriptor = None
    for klass in siddhi::Collect.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::collect_has_end():
    assert hasattr(siddhi::Collect, "end")
    descriptor = None
    for klass in siddhi::Collect.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::and_is_not_abstract():
    assert not inspect.isabstract(siddhi::AND)


def test_siddhi::and_constructor_exists():
    assert callable(siddhi::AND.__init__)


def test_siddhi::and_constructor_args():
    sig = inspect.signature(siddhi::AND.__init__)
    params = list(sig.parameters.keys())
    assert "and_" in params, "Missing parameter 'and_'"

def test_siddhi::and_has_and_():
    assert hasattr(siddhi::AND, "and_")
    descriptor = None
    for klass in siddhi::AND.__mro__:
        if "and_" in klass.__dict__:
            descriptor = klass.__dict__["and_"]
            break
    assert isinstance(descriptor, property)



def test_sequencesource_is_not_abstract():
    assert not inspect.isabstract(SequenceSource)


def test_sequencesource_constructor_exists():
    assert callable(SequenceSource.__init__)


def test_sequencesource_constructor_args():
    sig = inspect.signature(SequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::logicalabsentstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::LogicalAbsentStatefulSource)


def test_siddhi::logicalabsentstatefulsource_constructor_exists():
    assert callable(siddhi::LogicalAbsentStatefulSource.__init__)


def test_siddhi::logicalabsentstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::LogicalAbsentStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::logicalstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::LogicalStatefulSource)


def test_siddhi::logicalstatefulsource_constructor_exists():
    assert callable(siddhi::LogicalStatefulSource.__init__)


def test_siddhi::logicalstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::LogicalStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::sequencecollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::SequenceCollectionStatefulSource)


def test_siddhi::sequencecollectionstatefulsource_constructor_exists():
    assert callable(siddhi::SequenceCollectionStatefulSource.__init__)


def test_siddhi::sequencecollectionstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::SequenceCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_sequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(SequenceSourceChain)


def test_sequencesourcechain_constructor_exists():
    assert callable(SequenceSourceChain.__init__)


def test_sequencesourcechain_constructor_args():
    sig = inspect.signature(SequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::patternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::PatternSourceChain)


def test_siddhi::patternsourcechain_constructor_exists():
    assert callable(siddhi::PatternSourceChain.__init__)


def test_siddhi::patternsourcechain_constructor_args():
    sig = inspect.signature(siddhi::PatternSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi::patternsourcechain_has_op():
    assert hasattr(siddhi::PatternSourceChain, "op")
    descriptor = None
    for klass in siddhi::PatternSourceChain.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_patternstream_is_not_abstract():
    assert not inspect.isabstract(PatternStream)


def test_patternstream_constructor_exists():
    assert callable(PatternStream.__init__)


def test_patternstream_constructor_args():
    sig = inspect.signature(PatternStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::absentpatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::AbsentPatternSourceChain)


def test_siddhi::absentpatternsourcechain_constructor_exists():
    assert callable(siddhi::AbsentPatternSourceChain.__init__)


def test_siddhi::absentpatternsourcechain_constructor_args():
    sig = inspect.signature(siddhi::AbsentPatternSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::everypatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::EveryPatternSourceChain)


def test_siddhi::everypatternsourcechain_constructor_exists():
    assert callable(siddhi::EveryPatternSourceChain.__init__)


def test_siddhi::everypatternsourcechain_constructor_args():
    sig = inspect.signature(siddhi::EveryPatternSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi::everypatternsourcechain_has_op():
    assert hasattr(siddhi::EveryPatternSourceChain, "op")
    descriptor = None
    for klass in siddhi::EveryPatternSourceChain.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::rightabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi::RightAbsentSequenceSource)


def test_siddhi::rightabsentsequencesource_constructor_exists():
    assert callable(siddhi::RightAbsentSequenceSource.__init__)


def test_siddhi::rightabsentsequencesource_constructor_args():
    sig = inspect.signature(siddhi::RightAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "cp" in params, "Missing parameter 'cp'"
    assert "comma" in params, "Missing parameter 'comma'"
    assert "comm" in params, "Missing parameter 'comm'"

def test_siddhi::rightabsentsequencesource_has_op():
    assert hasattr(siddhi::RightAbsentSequenceSource, "op")
    descriptor = None
    for klass in siddhi::RightAbsentSequenceSource.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::rightabsentsequencesource_has_cp():
    assert hasattr(siddhi::RightAbsentSequenceSource, "cp")
    descriptor = None
    for klass in siddhi::RightAbsentSequenceSource.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::rightabsentsequencesource_has_comma():
    assert hasattr(siddhi::RightAbsentSequenceSource, "comma")
    descriptor = None
    for klass in siddhi::RightAbsentSequenceSource.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::rightabsentsequencesource_has_comm():
    assert hasattr(siddhi::RightAbsentSequenceSource, "comm")
    descriptor = None
    for klass in siddhi::RightAbsentSequenceSource.__mro__:
        if "comm" in klass.__dict__:
            descriptor = klass.__dict__["comm"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::leftabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi::LeftAbsentSequenceSource)


def test_siddhi::leftabsentsequencesource_constructor_exists():
    assert callable(siddhi::LeftAbsentSequenceSource.__init__)


def test_siddhi::leftabsentsequencesource_constructor_args():
    sig = inspect.signature(siddhi::LeftAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "comma" in params, "Missing parameter 'comma'"
    assert "op" in params, "Missing parameter 'op'"
    assert "comm" in params, "Missing parameter 'comm'"

def test_siddhi::leftabsentsequencesource_has_cp():
    assert hasattr(siddhi::LeftAbsentSequenceSource, "cp")
    descriptor = None
    for klass in siddhi::LeftAbsentSequenceSource.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::leftabsentsequencesource_has_comma():
    assert hasattr(siddhi::LeftAbsentSequenceSource, "comma")
    descriptor = None
    for klass in siddhi::LeftAbsentSequenceSource.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::leftabsentsequencesource_has_op():
    assert hasattr(siddhi::LeftAbsentSequenceSource, "op")
    descriptor = None
    for klass in siddhi::LeftAbsentSequenceSource.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::leftabsentsequencesource_has_comm():
    assert hasattr(siddhi::LeftAbsentSequenceSource, "comm")
    descriptor = None
    for klass in siddhi::LeftAbsentSequenceSource.__mro__:
        if "comm" in klass.__dict__:
            descriptor = klass.__dict__["comm"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::basicabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::BasicAbsentPatternSource)


def test_siddhi::basicabsentpatternsource_constructor_exists():
    assert callable(siddhi::BasicAbsentPatternSource.__init__)


def test_siddhi::basicabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi::BasicAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::eobject_is_not_abstract():
    assert not inspect.isabstract(siddhi::EObject)


def test_siddhi::eobject_constructor_exists():
    assert callable(siddhi::EObject.__init__)


def test_siddhi::eobject_constructor_args():
    sig = inspect.signature(siddhi::EObject.__init__)
    params = list(sig.parameters.keys())



def test_having_is_not_abstract():
    assert not inspect.isabstract(HAVING)


def test_having_constructor_exists():
    assert callable(HAVING.__init__)


def test_having_constructor_args():
    sig = inspect.signature(HAVING.__init__)
    params = list(sig.parameters.keys())



def test_group_is_not_abstract():
    assert not inspect.isabstract(GROUP)


def test_group_constructor_exists():
    assert callable(GROUP.__init__)


def test_group_constructor_args():
    sig = inspect.signature(GROUP.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::havingexpr_is_not_abstract():
    assert not inspect.isabstract(siddhi::HavingExpr)


def test_siddhi::havingexpr_constructor_exists():
    assert callable(siddhi::HavingExpr.__init__)


def test_siddhi::havingexpr_constructor_args():
    sig = inspect.signature(siddhi::HavingExpr.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::absentsequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::AbsentSequenceSourceChain)


def test_siddhi::absentsequencesourcechain_constructor_exists():
    assert callable(siddhi::AbsentSequenceSourceChain.__init__)


def test_siddhi::absentsequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi::AbsentSequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::sequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::SequenceSourceChain)


def test_siddhi::sequencesourcechain_constructor_exists():
    assert callable(siddhi::SequenceSourceChain.__init__)


def test_siddhi::sequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi::SequenceSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi::sequencesourcechain_has_op():
    assert hasattr(siddhi::SequenceSourceChain, "op")
    descriptor = None
    for klass in siddhi::SequenceSourceChain.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::withintime_is_not_abstract():
    assert not inspect.isabstract(siddhi::WithinTime)


def test_siddhi::withintime_constructor_exists():
    assert callable(siddhi::WithinTime.__init__)


def test_siddhi::withintime_constructor_args():
    sig = inspect.signature(siddhi::WithinTime.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::sequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi::SequenceSource)


def test_siddhi::sequencesource_constructor_exists():
    assert callable(siddhi::SequenceSource.__init__)


def test_siddhi::sequencesource_constructor_args():
    sig = inspect.signature(siddhi::SequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::everyabsentsequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::EveryAbsentSequenceSourceChain)


def test_siddhi::everyabsentsequencesourcechain_constructor_exists():
    assert callable(siddhi::EveryAbsentSequenceSourceChain.__init__)


def test_siddhi::everyabsentsequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi::EveryAbsentSequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::everysequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi::EverySequenceSourceChain)


def test_siddhi::everysequencesourcechain_constructor_exists():
    assert callable(siddhi::EverySequenceSourceChain.__init__)


def test_siddhi::everysequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi::EverySequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::patternstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::PatternStream)


def test_siddhi::patternstream_constructor_exists():
    assert callable(siddhi::PatternStream.__init__)


def test_siddhi::patternstream_constructor_args():
    sig = inspect.signature(siddhi::PatternStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::sequencestream_is_not_abstract():
    assert not inspect.isabstract(siddhi::SequenceStream)


def test_siddhi::sequencestream_constructor_exists():
    assert callable(siddhi::SequenceStream.__init__)


def test_siddhi::sequencestream_constructor_args():
    sig = inspect.signature(siddhi::SequenceStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::joinstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::JoinStream)


def test_siddhi::joinstream_constructor_exists():
    assert callable(siddhi::JoinStream.__init__)


def test_siddhi::joinstream_constructor_args():
    sig = inspect.signature(siddhi::JoinStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::attribute_is_not_abstract():
    assert not inspect.isabstract(siddhi::Attribute)


def test_siddhi::attribute_constructor_exists():
    assert callable(siddhi::Attribute.__init__)


def test_siddhi::attribute_constructor_args():
    sig = inspect.signature(siddhi::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::outputattribute_is_not_abstract():
    assert not inspect.isabstract(siddhi::OutputAttribute)


def test_siddhi::outputattribute_constructor_exists():
    assert callable(siddhi::OutputAttribute.__init__)


def test_siddhi::outputattribute_constructor_args():
    sig = inspect.signature(siddhi::OutputAttribute.__init__)
    params = list(sig.parameters.keys())



def test_select_is_not_abstract():
    assert not inspect.isabstract(SELECT)


def test_select_constructor_exists():
    assert callable(SELECT.__init__)


def test_select_constructor_args():
    sig = inspect.signature(SELECT.__init__)
    params = list(sig.parameters.keys())



def test_first_is_not_abstract():
    assert not inspect.isabstract(FIRST)


def test_first_constructor_exists():
    assert callable(FIRST.__init__)


def test_first_constructor_args():
    sig = inspect.signature(FIRST.__init__)
    params = list(sig.parameters.keys())



def test_last_is_not_abstract():
    assert not inspect.isabstract(LAST)


def test_last_constructor_exists():
    assert callable(LAST.__init__)


def test_last_constructor_args():
    sig = inspect.signature(LAST.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::attributeindex_is_not_abstract():
    assert not inspect.isabstract(siddhi::AttributeIndex)


def test_siddhi::attributeindex_constructor_exists():
    assert callable(siddhi::AttributeIndex.__init__)


def test_siddhi::attributeindex_constructor_args():
    sig = inspect.signature(siddhi::AttributeIndex.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathgtltoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathGtLtOperation)


def test_siddhi::mathgtltoperation_constructor_exists():
    assert callable(siddhi::MathGtLtOperation.__init__)


def test_siddhi::mathgtltoperation_constructor_args():
    sig = inspect.signature(siddhi::MathGtLtOperation.__init__)
    params = list(sig.parameters.keys())
    assert "lt" in params, "Missing parameter 'lt'"
    assert "gt_eq" in params, "Missing parameter 'gt_eq'"
    assert "gt" in params, "Missing parameter 'gt'"
    assert "lt_eq" in params, "Missing parameter 'lt_eq'"

def test_siddhi::mathgtltoperation_has_lt():
    assert hasattr(siddhi::MathGtLtOperation, "lt")
    descriptor = None
    for klass in siddhi::MathGtLtOperation.__mro__:
        if "lt" in klass.__dict__:
            descriptor = klass.__dict__["lt"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathgtltoperation_has_gt_eq():
    assert hasattr(siddhi::MathGtLtOperation, "gt_eq")
    descriptor = None
    for klass in siddhi::MathGtLtOperation.__mro__:
        if "gt_eq" in klass.__dict__:
            descriptor = klass.__dict__["gt_eq"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathgtltoperation_has_gt():
    assert hasattr(siddhi::MathGtLtOperation, "gt")
    descriptor = None
    for klass in siddhi::MathGtLtOperation.__mro__:
        if "gt" in klass.__dict__:
            descriptor = klass.__dict__["gt"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathgtltoperation_has_lt_eq():
    assert hasattr(siddhi::MathGtLtOperation, "lt_eq")
    descriptor = None
    for klass in siddhi::MathGtLtOperation.__mro__:
        if "lt_eq" in klass.__dict__:
            descriptor = klass.__dict__["lt_eq"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::mathinoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathInOperation)


def test_siddhi::mathinoperation_constructor_exists():
    assert callable(siddhi::MathInOperation.__init__)


def test_siddhi::mathinoperation_constructor_args():
    sig = inspect.signature(siddhi::MathInOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::notoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::NotOperation)


def test_siddhi::notoperation_constructor_exists():
    assert callable(siddhi::NotOperation.__init__)


def test_siddhi::notoperation_constructor_args():
    sig = inspect.signature(siddhi::NotOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::mathequaloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathEqualOperation)


def test_siddhi::mathequaloperation_constructor_exists():
    assert callable(siddhi::MathEqualOperation.__init__)


def test_siddhi::mathequaloperation_constructor_args():
    sig = inspect.signature(siddhi::MathEqualOperation.__init__)
    params = list(sig.parameters.keys())
    assert "not_eq" in params, "Missing parameter 'not_eq'"
    assert "eq" in params, "Missing parameter 'eq'"

def test_siddhi::mathequaloperation_has_not_eq():
    assert hasattr(siddhi::MathEqualOperation, "not_eq")
    descriptor = None
    for klass in siddhi::MathEqualOperation.__mro__:
        if "not_eq" in klass.__dict__:
            descriptor = klass.__dict__["not_eq"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::mathequaloperation_has_eq():
    assert hasattr(siddhi::MathEqualOperation, "eq")
    descriptor = None
    for klass in siddhi::MathEqualOperation.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::minutes_is_not_abstract():
    assert not inspect.isabstract(siddhi::MINUTES)


def test_siddhi::minutes_constructor_exists():
    assert callable(siddhi::MINUTES.__init__)


def test_siddhi::minutes_constructor_args():
    sig = inspect.signature(siddhi::MINUTES.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "min" in params, "Missing parameter 'min'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_siddhi::minutes_has_minutes():
    assert hasattr(siddhi::MINUTES, "minutes")
    descriptor = None
    for klass in siddhi::MINUTES.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::minutes_has_min():
    assert hasattr(siddhi::MINUTES, "min")
    descriptor = None
    for klass in siddhi::MINUTES.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::minutes_has_minute():
    assert hasattr(siddhi::MINUTES, "minute")
    descriptor = None
    for klass in siddhi::MINUTES.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::hours_is_not_abstract():
    assert not inspect.isabstract(siddhi::HOURS)


def test_siddhi::hours_constructor_exists():
    assert callable(siddhi::HOURS.__init__)


def test_siddhi::hours_constructor_args():
    sig = inspect.signature(siddhi::HOURS.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_siddhi::hours_has_hours():
    assert hasattr(siddhi::HOURS, "hours")
    descriptor = None
    for klass in siddhi::HOURS.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::hours_has_hour():
    assert hasattr(siddhi::HOURS, "hour")
    descriptor = None
    for klass in siddhi::HOURS.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::days_is_not_abstract():
    assert not inspect.isabstract(siddhi::DAYS)


def test_siddhi::days_constructor_exists():
    assert callable(siddhi::DAYS.__init__)


def test_siddhi::days_constructor_args():
    sig = inspect.signature(siddhi::DAYS.__init__)
    params = list(sig.parameters.keys())
    assert "days" in params, "Missing parameter 'days'"
    assert "day" in params, "Missing parameter 'day'"

def test_siddhi::days_has_days():
    assert hasattr(siddhi::DAYS, "days")
    descriptor = None
    for klass in siddhi::DAYS.__mro__:
        if "days" in klass.__dict__:
            descriptor = klass.__dict__["days"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::days_has_day():
    assert hasattr(siddhi::DAYS, "day")
    descriptor = None
    for klass in siddhi::DAYS.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::weeks_is_not_abstract():
    assert not inspect.isabstract(siddhi::WEEKS)


def test_siddhi::weeks_constructor_exists():
    assert callable(siddhi::WEEKS.__init__)


def test_siddhi::weeks_constructor_args():
    sig = inspect.signature(siddhi::WEEKS.__init__)
    params = list(sig.parameters.keys())
    assert "weeks" in params, "Missing parameter 'weeks'"
    assert "week" in params, "Missing parameter 'week'"

def test_siddhi::weeks_has_weeks():
    assert hasattr(siddhi::WEEKS, "weeks")
    descriptor = None
    for klass in siddhi::WEEKS.__mro__:
        if "weeks" in klass.__dict__:
            descriptor = klass.__dict__["weeks"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::weeks_has_week():
    assert hasattr(siddhi::WEEKS, "week")
    descriptor = None
    for klass in siddhi::WEEKS.__mro__:
        if "week" in klass.__dict__:
            descriptor = klass.__dict__["week"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::months_is_not_abstract():
    assert not inspect.isabstract(siddhi::MONTHS)


def test_siddhi::months_constructor_exists():
    assert callable(siddhi::MONTHS.__init__)


def test_siddhi::months_constructor_args():
    sig = inspect.signature(siddhi::MONTHS.__init__)
    params = list(sig.parameters.keys())
    assert "months" in params, "Missing parameter 'months'"
    assert "month" in params, "Missing parameter 'month'"

def test_siddhi::months_has_months():
    assert hasattr(siddhi::MONTHS, "months")
    descriptor = None
    for klass in siddhi::MONTHS.__mro__:
        if "months" in klass.__dict__:
            descriptor = klass.__dict__["months"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::months_has_month():
    assert hasattr(siddhi::MONTHS, "month")
    descriptor = None
    for klass in siddhi::MONTHS.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::mathlogicaloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::MathLogicalOperation)


def test_siddhi::mathlogicaloperation_constructor_exists():
    assert callable(siddhi::MathLogicalOperation.__init__)


def test_siddhi::mathlogicaloperation_constructor_args():
    sig = inspect.signature(siddhi::MathLogicalOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::rightabsentpatternsource1_is_not_abstract():
    assert not inspect.isabstract(siddhi::RightAbsentPatternSource1)


def test_siddhi::rightabsentpatternsource1_constructor_exists():
    assert callable(siddhi::RightAbsentPatternSource1.__init__)


def test_siddhi::rightabsentpatternsource1_constructor_args():
    sig = inspect.signature(siddhi::RightAbsentPatternSource1.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"

def test_siddhi::rightabsentpatternsource1_has_fb():
    assert hasattr(siddhi::RightAbsentPatternSource1, "fb")
    descriptor = None
    for klass in siddhi::RightAbsentPatternSource1.__mro__:
        if "fb" in klass.__dict__:
            descriptor = klass.__dict__["fb"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::leftabsentpatternsource1_is_not_abstract():
    assert not inspect.isabstract(siddhi::LeftAbsentPatternSource1)


def test_siddhi::leftabsentpatternsource1_constructor_exists():
    assert callable(siddhi::LeftAbsentPatternSource1.__init__)


def test_siddhi::leftabsentpatternsource1_constructor_args():
    sig = inspect.signature(siddhi::LeftAbsentPatternSource1.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"

def test_siddhi::leftabsentpatternsource1_has_fb():
    assert hasattr(siddhi::LeftAbsentPatternSource1, "fb")
    descriptor = None
    for klass in siddhi::LeftAbsentPatternSource1.__mro__:
        if "fb" in klass.__dict__:
            descriptor = klass.__dict__["fb"]
            break
    assert isinstance(descriptor, property)



def test_rightabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(RightAbsentSequenceSource)


def test_rightabsentsequencesource_constructor_exists():
    assert callable(RightAbsentSequenceSource.__init__)


def test_rightabsentsequencesource_constructor_args():
    sig = inspect.signature(RightAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::rightabsentsequencesource1_is_not_abstract():
    assert not inspect.isabstract(siddhi::RightAbsentSequenceSource1)


def test_siddhi::rightabsentsequencesource1_constructor_exists():
    assert callable(siddhi::RightAbsentSequenceSource1.__init__)


def test_siddhi::rightabsentsequencesource1_constructor_args():
    sig = inspect.signature(siddhi::RightAbsentSequenceSource1.__init__)
    params = list(sig.parameters.keys())



def test_leftabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(LeftAbsentSequenceSource)


def test_leftabsentsequencesource_constructor_exists():
    assert callable(LeftAbsentSequenceSource.__init__)


def test_leftabsentsequencesource_constructor_args():
    sig = inspect.signature(LeftAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::leftabsentsequencesource1_is_not_abstract():
    assert not inspect.isabstract(siddhi::LeftAbsentSequenceSource1)


def test_siddhi::leftabsentsequencesource1_constructor_exists():
    assert callable(siddhi::LeftAbsentSequenceSource1.__init__)


def test_siddhi::leftabsentsequencesource1_constructor_args():
    sig = inspect.signature(siddhi::LeftAbsentSequenceSource1.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::true_is_not_abstract():
    assert not inspect.isabstract(siddhi::TRUE)


def test_siddhi::true_constructor_exists():
    assert callable(siddhi::TRUE.__init__)


def test_siddhi::true_constructor_args():
    sig = inspect.signature(siddhi::TRUE.__init__)
    params = list(sig.parameters.keys())
    assert "tr" in params, "Missing parameter 'tr'"

def test_siddhi::true_has_tr():
    assert hasattr(siddhi::TRUE, "tr")
    descriptor = None
    for klass in siddhi::TRUE.__mro__:
        if "tr" in klass.__dict__:
            descriptor = klass.__dict__["tr"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::false_is_not_abstract():
    assert not inspect.isabstract(siddhi::FALSE)


def test_siddhi::false_constructor_exists():
    assert callable(siddhi::FALSE.__init__)


def test_siddhi::false_constructor_args():
    sig = inspect.signature(siddhi::FALSE.__init__)
    params = list(sig.parameters.keys())
    assert "fals" in params, "Missing parameter 'fals'"

def test_siddhi::false_has_fals():
    assert hasattr(siddhi::FALSE, "fals")
    descriptor = None
    for klass in siddhi::FALSE.__mro__:
        if "fals" in klass.__dict__:
            descriptor = klass.__dict__["fals"]
            break
    assert isinstance(descriptor, property)



def test_snapshot_is_not_abstract():
    assert not inspect.isabstract(SNAPSHOT)


def test_snapshot_constructor_exists():
    assert callable(SNAPSHOT.__init__)


def test_snapshot_constructor_args():
    sig = inspect.signature(SNAPSHOT.__init__)
    params = list(sig.parameters.keys())



def test_current_is_not_abstract():
    assert not inspect.isabstract(CURRENT)


def test_current_constructor_exists():
    assert callable(CURRENT.__init__)


def test_current_constructor_args():
    sig = inspect.signature(CURRENT.__init__)
    params = list(sig.parameters.keys())



def test_expired_is_not_abstract():
    assert not inspect.isabstract(EXPIRED)


def test_expired_constructor_exists():
    assert callable(EXPIRED.__init__)


def test_expired_constructor_args():
    sig = inspect.signature(EXPIRED.__init__)
    params = list(sig.parameters.keys())



def test_raw_is_not_abstract():
    assert not inspect.isabstract(RAW)


def test_raw_constructor_exists():
    assert callable(RAW.__init__)


def test_raw_constructor_args():
    sig = inspect.signature(RAW.__init__)
    params = list(sig.parameters.keys())



def test_events_is_not_abstract():
    assert not inspect.isabstract(EVENTS)


def test_events_constructor_exists():
    assert callable(EVENTS.__init__)


def test_events_constructor_args():
    sig = inspect.signature(EVENTS.__init__)
    params = list(sig.parameters.keys())



def test_all_is_not_abstract():
    assert not inspect.isabstract(ALL)


def test_all_constructor_exists():
    assert callable(ALL.__init__)


def test_all_constructor_args():
    sig = inspect.signature(ALL.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::outputratetype_is_not_abstract():
    assert not inspect.isabstract(siddhi::OutputRateType)


def test_siddhi::outputratetype_constructor_exists():
    assert callable(siddhi::OutputRateType.__init__)


def test_siddhi::outputratetype_constructor_args():
    sig = inspect.signature(siddhi::OutputRateType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::setassignment_is_not_abstract():
    assert not inspect.isabstract(siddhi::SetAssignment)


def test_siddhi::setassignment_constructor_exists():
    assert callable(siddhi::SetAssignment.__init__)


def test_siddhi::setassignment_constructor_args():
    sig = inspect.signature(siddhi::SetAssignment.__init__)
    params = list(sig.parameters.keys())



def test_set_is_not_abstract():
    assert not inspect.isabstract(SET)


def test_set_constructor_exists():
    assert callable(SET.__init__)


def test_set_constructor_args():
    sig = inspect.signature(SET.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::setclause_is_not_abstract():
    assert not inspect.isabstract(siddhi::SetClause)


def test_siddhi::setclause_constructor_exists():
    assert callable(siddhi::SetClause.__init__)


def test_siddhi::setclause_constructor_args():
    sig = inspect.signature(siddhi::SetClause.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::or_is_not_abstract():
    assert not inspect.isabstract(siddhi::OR)


def test_siddhi::or_constructor_exists():
    assert callable(siddhi::OR.__init__)


def test_siddhi::or_constructor_args():
    sig = inspect.signature(siddhi::OR.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"

def test_siddhi::or_has_or_():
    assert hasattr(siddhi::OR, "or_")
    descriptor = None
    for klass in siddhi::OR.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::conditionrange_is_not_abstract():
    assert not inspect.isabstract(siddhi::ConditionRange)


def test_siddhi::conditionrange_constructor_exists():
    assert callable(siddhi::ConditionRange.__init__)


def test_siddhi::conditionrange_constructor_args():
    sig = inspect.signature(siddhi::ConditionRange.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::of_is_not_abstract():
    assert not inspect.isabstract(siddhi::OF)


def test_siddhi::of_constructor_exists():
    assert callable(siddhi::OF.__init__)


def test_siddhi::of_constructor_args():
    sig = inspect.signature(siddhi::OF.__init__)
    params = list(sig.parameters.keys())
    assert "of" in params, "Missing parameter 'of'"

def test_siddhi::of_has_of():
    assert hasattr(siddhi::OF, "of")
    descriptor = None
    for klass in siddhi::OF.__mro__:
        if "of" in klass.__dict__:
            descriptor = klass.__dict__["of"]
            break
    assert isinstance(descriptor, property)



def test_partitionwithstream_is_not_abstract():
    assert not inspect.isabstract(PartitionWithStream)


def test_partitionwithstream_constructor_exists():
    assert callable(PartitionWithStream.__init__)


def test_partitionwithstream_constructor_args():
    sig = inspect.signature(PartitionWithStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::conditionranges_is_not_abstract():
    assert not inspect.isabstract(siddhi::ConditionRanges)


def test_siddhi::conditionranges_constructor_exists():
    assert callable(siddhi::ConditionRanges.__init__)


def test_siddhi::conditionranges_constructor_args():
    sig = inspect.signature(siddhi::ConditionRanges.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::on_is_not_abstract():
    assert not inspect.isabstract(siddhi::ON)


def test_siddhi::on_constructor_exists():
    assert callable(siddhi::ON.__init__)


def test_siddhi::on_constructor_args():
    sig = inspect.signature(siddhi::ON.__init__)
    params = list(sig.parameters.keys())
    assert "on" in params, "Missing parameter 'on'"

def test_siddhi::on_has_on():
    assert hasattr(siddhi::ON, "on")
    descriptor = None
    for klass in siddhi::ON.__mro__:
        if "on" in klass.__dict__:
            descriptor = klass.__dict__["on"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::target_is_not_abstract():
    assert not inspect.isabstract(siddhi::Target)


def test_siddhi::target_constructor_exists():
    assert callable(siddhi::Target.__init__)


def test_siddhi::target_constructor_args():
    sig = inspect.signature(siddhi::Target.__init__)
    params = list(sig.parameters.keys())



def test_update_is_not_abstract():
    assert not inspect.isabstract(UPDATE)


def test_update_constructor_exists():
    assert callable(UPDATE.__init__)


def test_update_constructor_args():
    sig = inspect.signature(UPDATE.__init__)
    params = list(sig.parameters.keys())



def test_for_is_not_abstract():
    assert not inspect.isabstract(FOR)


def test_for_constructor_exists():
    assert callable(FOR.__init__)


def test_for_constructor_args():
    sig = inspect.signature(FOR.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::fortime_is_not_abstract():
    assert not inspect.isabstract(siddhi::ForTime)


def test_siddhi::fortime_constructor_exists():
    assert callable(siddhi::ForTime.__init__)


def test_siddhi::fortime_constructor_args():
    sig = inspect.signature(siddhi::ForTime.__init__)
    params = list(sig.parameters.keys())



def test_delete_is_not_abstract():
    assert not inspect.isabstract(DELETE)


def test_delete_constructor_exists():
    assert callable(DELETE.__init__)


def test_delete_constructor_args():
    sig = inspect.signature(DELETE.__init__)
    params = list(sig.parameters.keys())



def test_into_is_not_abstract():
    assert not inspect.isabstract(INTO)


def test_into_constructor_exists():
    assert callable(INTO.__init__)


def test_into_constructor_args():
    sig = inspect.signature(INTO.__init__)
    params = list(sig.parameters.keys())



def test_insert_is_not_abstract():
    assert not inspect.isabstract(INSERT)


def test_insert_constructor_exists():
    assert callable(INSERT.__init__)


def test_insert_constructor_args():
    sig = inspect.signature(INSERT.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::querysection_is_not_abstract():
    assert not inspect.isabstract(siddhi::QuerySection)


def test_siddhi::querysection_constructor_exists():
    assert callable(siddhi::QuerySection.__init__)


def test_siddhi::querysection_constructor_args():
    sig = inspect.signature(siddhi::QuerySection.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::queryinput_is_not_abstract():
    assert not inspect.isabstract(siddhi::QueryInput)


def test_siddhi::queryinput_constructor_exists():
    assert callable(siddhi::QueryInput.__init__)


def test_siddhi::queryinput_constructor_args():
    sig = inspect.signature(siddhi::QueryInput.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::as_is_not_abstract():
    assert not inspect.isabstract(siddhi::AS)


def test_siddhi::as_constructor_exists():
    assert callable(siddhi::AS.__init__)


def test_siddhi::as_constructor_args():
    sig = inspect.signature(siddhi::AS.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_siddhi::as_has_a():
    assert hasattr(siddhi::AS, "a")
    descriptor = None
    for klass in siddhi::AS.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::expression_is_not_abstract():
    assert not inspect.isabstract(siddhi::Expression)


def test_siddhi::expression_constructor_exists():
    assert callable(siddhi::Expression.__init__)


def test_siddhi::expression_constructor_args():
    sig = inspect.signature(siddhi::Expression.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::propertyvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::PropertyValue)


def test_siddhi::propertyvalue_constructor_exists():
    assert callable(siddhi::PropertyValue.__init__)


def test_siddhi::propertyvalue_constructor_args():
    sig = inspect.signature(siddhi::PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::partitionwithstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::PartitionWithStream)


def test_siddhi::partitionwithstream_constructor_exists():
    assert callable(siddhi::PartitionWithStream.__init__)


def test_siddhi::partitionwithstream_constructor_args():
    sig = inspect.signature(siddhi::PartitionWithStream.__init__)
    params = list(sig.parameters.keys())



def test_end_is_not_abstract():
    assert not inspect.isabstract(END)


def test_end_constructor_exists():
    assert callable(END.__init__)


def test_end_constructor_args():
    sig = inspect.signature(END.__init__)
    params = list(sig.parameters.keys())



def test_begin_is_not_abstract():
    assert not inspect.isabstract(BEGIN)


def test_begin_constructor_exists():
    assert callable(BEGIN.__init__)


def test_begin_constructor_args():
    sig = inspect.signature(BEGIN.__init__)
    params = list(sig.parameters.keys())



def test_with_is_not_abstract():
    assert not inspect.isabstract(WITH)


def test_with_constructor_exists():
    assert callable(WITH.__init__)


def test_with_constructor_args():
    sig = inspect.signature(WITH.__init__)
    params = list(sig.parameters.keys())



def test_partition_is_not_abstract():
    assert not inspect.isabstract(PARTITION)


def test_partition_constructor_exists():
    assert callable(PARTITION.__init__)


def test_partition_constructor_args():
    sig = inspect.signature(PARTITION.__init__)
    params = list(sig.parameters.keys())



def test_source1orstandardstatefulsource_is_not_abstract():
    assert not inspect.isabstract(Source1OrStandardStatefulSource)


def test_source1orstandardstatefulsource_constructor_exists():
    assert callable(Source1OrStandardStatefulSource.__init__)


def test_source1orstandardstatefulsource_constructor_args():
    sig = inspect.signature(Source1OrStandardStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::streamalias_is_not_abstract():
    assert not inspect.isabstract(siddhi::StreamAlias)


def test_siddhi::streamalias_constructor_exists():
    assert callable(siddhi::StreamAlias.__init__)


def test_siddhi::streamalias_constructor_args():
    sig = inspect.signature(siddhi::StreamAlias.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::standardstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi::StandardStatefulSource)


def test_siddhi::standardstatefulsource_constructor_exists():
    assert callable(siddhi::StandardStatefulSource.__init__)


def test_siddhi::standardstatefulsource_constructor_args():
    sig = inspect.signature(siddhi::StandardStatefulSource.__init__)
    params = list(sig.parameters.keys())
    assert "one_or_more" in params, "Missing parameter 'one_or_more'"
    assert "zero_or_more" in params, "Missing parameter 'zero_or_more'"
    assert "zero_or_one" in params, "Missing parameter 'zero_or_one'"

def test_siddhi::standardstatefulsource_has_one_or_more():
    assert hasattr(siddhi::StandardStatefulSource, "one_or_more")
    descriptor = None
    for klass in siddhi::StandardStatefulSource.__mro__:
        if "one_or_more" in klass.__dict__:
            descriptor = klass.__dict__["one_or_more"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::standardstatefulsource_has_zero_or_more():
    assert hasattr(siddhi::StandardStatefulSource, "zero_or_more")
    descriptor = None
    for klass in siddhi::StandardStatefulSource.__mro__:
        if "zero_or_more" in klass.__dict__:
            descriptor = klass.__dict__["zero_or_more"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::standardstatefulsource_has_zero_or_one():
    assert hasattr(siddhi::StandardStatefulSource, "zero_or_one")
    descriptor = None
    for klass in siddhi::StandardStatefulSource.__mro__:
        if "zero_or_one" in klass.__dict__:
            descriptor = klass.__dict__["zero_or_one"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::source_is_not_abstract():
    assert not inspect.isabstract(siddhi::Source)


def test_siddhi::source_constructor_exists():
    assert callable(siddhi::Source.__init__)


def test_siddhi::source_constructor_args():
    sig = inspect.signature(siddhi::Source.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(OBJECT)


def test_object_constructor_exists():
    assert callable(OBJECT.__init__)


def test_object_constructor_args():
    sig = inspect.signature(OBJECT.__init__)
    params = list(sig.parameters.keys())



def test_bool_is_not_abstract():
    assert not inspect.isabstract(BOOL)


def test_bool_constructor_exists():
    assert callable(BOOL.__init__)


def test_bool_constructor_args():
    sig = inspect.signature(BOOL.__init__)
    params = list(sig.parameters.keys())



def test_double_is_not_abstract():
    assert not inspect.isabstract(DOUBLE)


def test_double_constructor_exists():
    assert callable(DOUBLE.__init__)


def test_double_constructor_args():
    sig = inspect.signature(DOUBLE.__init__)
    params = list(sig.parameters.keys())



def test_float_is_not_abstract():
    assert not inspect.isabstract(FLOAT)


def test_float_constructor_exists():
    assert callable(FLOAT.__init__)


def test_float_constructor_args():
    sig = inspect.signature(FLOAT.__init__)
    params = list(sig.parameters.keys())



def test_long_is_not_abstract():
    assert not inspect.isabstract(LONG)


def test_long_constructor_exists():
    assert callable(LONG.__init__)


def test_long_constructor_args():
    sig = inspect.signature(LONG.__init__)
    params = list(sig.parameters.keys())



def test_ints_is_not_abstract():
    assert not inspect.isabstract(INTS)


def test_ints_constructor_exists():
    assert callable(INTS.__init__)


def test_ints_constructor_args():
    sig = inspect.signature(INTS.__init__)
    params = list(sig.parameters.keys())



def test_strings_is_not_abstract():
    assert not inspect.isabstract(STRINGS)


def test_strings_constructor_exists():
    assert callable(STRINGS.__init__)


def test_strings_constructor_args():
    sig = inspect.signature(STRINGS.__init__)
    params = list(sig.parameters.keys())



def test_featuresoroutattr_is_not_abstract():
    assert not inspect.isabstract(FeaturesOrOutAttr)


def test_featuresoroutattr_constructor_exists():
    assert callable(FeaturesOrOutAttr.__init__)


def test_featuresoroutattr_constructor_args():
    sig = inspect.signature(FeaturesOrOutAttr.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::outattr_is_not_abstract():
    assert not inspect.isabstract(siddhi::OutAttr)


def test_siddhi::outattr_constructor_exists():
    assert callable(siddhi::OutAttr.__init__)


def test_siddhi::outattr_constructor_args():
    sig = inspect.signature(siddhi::OutAttr.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::propertyseparator_is_not_abstract():
    assert not inspect.isabstract(siddhi::PropertySeparator)


def test_siddhi::propertyseparator_constructor_exists():
    assert callable(siddhi::PropertySeparator.__init__)


def test_siddhi::propertyseparator_constructor_args():
    sig = inspect.signature(siddhi::PropertySeparator.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::attributereference_is_not_abstract():
    assert not inspect.isabstract(siddhi::AttributeReference)


def test_siddhi::attributereference_constructor_exists():
    assert callable(siddhi::AttributeReference.__init__)


def test_siddhi::attributereference_constructor_args():
    sig = inspect.signature(siddhi::AttributeReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hash2" in params, "Missing parameter 'hash2'"
    assert "hash1" in params, "Missing parameter 'hash1'"

def test_siddhi::attributereference_has_name():
    assert hasattr(siddhi::AttributeReference, "name")
    descriptor = None
    for klass in siddhi::AttributeReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::attributereference_has_hash2():
    assert hasattr(siddhi::AttributeReference, "hash2")
    descriptor = None
    for klass in siddhi::AttributeReference.__mro__:
        if "hash2" in klass.__dict__:
            descriptor = klass.__dict__["hash2"]
            break
    assert isinstance(descriptor, property)

def test_siddhi::attributereference_has_hash1():
    assert hasattr(siddhi::AttributeReference, "hash1")
    descriptor = None
    for klass in siddhi::AttributeReference.__mro__:
        if "hash1" in klass.__dict__:
            descriptor = klass.__dict__["hash1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::groupbyqueryselection_is_not_abstract():
    assert not inspect.isabstract(siddhi::GroupByQuerySelection)


def test_siddhi::groupbyqueryselection_constructor_exists():
    assert callable(siddhi::GroupByQuerySelection.__init__)


def test_siddhi::groupbyqueryselection_constructor_args():
    sig = inspect.signature(siddhi::GroupByQuerySelection.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::standardstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::StandardStream)


def test_siddhi::standardstream_constructor_exists():
    assert callable(siddhi::StandardStream.__init__)


def test_siddhi::standardstream_constructor_args():
    sig = inspect.signature(siddhi::StandardStream.__init__)
    params = list(sig.parameters.keys())



def test_by_is_not_abstract():
    assert not inspect.isabstract(BY)


def test_by_constructor_exists():
    assert callable(BY.__init__)


def test_by_constructor_args():
    sig = inspect.signature(BY.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::groupby_is_not_abstract():
    assert not inspect.isabstract(siddhi::GroupBy)


def test_siddhi::groupby_constructor_exists():
    assert callable(siddhi::GroupBy.__init__)


def test_siddhi::groupby_constructor_args():
    sig = inspect.signature(siddhi::GroupBy.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::propertyname_is_not_abstract():
    assert not inspect.isabstract(siddhi::PropertyName)


def test_siddhi::propertyname_constructor_exists():
    assert callable(siddhi::PropertyName.__init__)


def test_siddhi::propertyname_constructor_args():
    sig = inspect.signature(siddhi::PropertyName.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::annotationelement_is_not_abstract():
    assert not inspect.isabstract(siddhi::AnnotationElement)


def test_siddhi::annotationelement_constructor_exists():
    assert callable(siddhi::AnnotationElement.__init__)


def test_siddhi::annotationelement_constructor_args():
    sig = inspect.signature(siddhi::AnnotationElement.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::name_is_not_abstract():
    assert not inspect.isabstract(siddhi::Name)


def test_siddhi::name_constructor_exists():
    assert callable(siddhi::Name.__init__)


def test_siddhi::name_constructor_args():
    sig = inspect.signature(siddhi::Name.__init__)
    params = list(sig.parameters.keys())
    assert "na" in params, "Missing parameter 'na'"

def test_siddhi::name_has_na():
    assert hasattr(siddhi::Name, "na")
    descriptor = None
    for klass in siddhi::Name.__mro__:
        if "na" in klass.__dict__:
            descriptor = klass.__dict__["na"]
            break
    assert isinstance(descriptor, property)



def test_years_is_not_abstract():
    assert not inspect.isabstract(YEARS)


def test_years_constructor_exists():
    assert callable(YEARS.__init__)


def test_years_constructor_args():
    sig = inspect.signature(YEARS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::yearvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::YearValue)


def test_siddhi::yearvalue_constructor_exists():
    assert callable(siddhi::YearValue.__init__)


def test_siddhi::yearvalue_constructor_args():
    sig = inspect.signature(siddhi::YearValue.__init__)
    params = list(sig.parameters.keys())



def test_months_is_not_abstract():
    assert not inspect.isabstract(MONTHS)


def test_months_constructor_exists():
    assert callable(MONTHS.__init__)


def test_months_constructor_args():
    sig = inspect.signature(MONTHS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::monthvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::MonthValue)


def test_siddhi::monthvalue_constructor_exists():
    assert callable(siddhi::MonthValue.__init__)


def test_siddhi::monthvalue_constructor_args():
    sig = inspect.signature(siddhi::MonthValue.__init__)
    params = list(sig.parameters.keys())



def test_weeks_is_not_abstract():
    assert not inspect.isabstract(WEEKS)


def test_weeks_constructor_exists():
    assert callable(WEEKS.__init__)


def test_weeks_constructor_args():
    sig = inspect.signature(WEEKS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::weekvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::WeekValue)


def test_siddhi::weekvalue_constructor_exists():
    assert callable(siddhi::WeekValue.__init__)


def test_siddhi::weekvalue_constructor_args():
    sig = inspect.signature(siddhi::WeekValue.__init__)
    params = list(sig.parameters.keys())



def test_days_is_not_abstract():
    assert not inspect.isabstract(DAYS)


def test_days_constructor_exists():
    assert callable(DAYS.__init__)


def test_days_constructor_args():
    sig = inspect.signature(DAYS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::dayvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::DayValue)


def test_siddhi::dayvalue_constructor_exists():
    assert callable(siddhi::DayValue.__init__)


def test_siddhi::dayvalue_constructor_args():
    sig = inspect.signature(siddhi::DayValue.__init__)
    params = list(sig.parameters.keys())



def test_hours_is_not_abstract():
    assert not inspect.isabstract(HOURS)


def test_hours_constructor_exists():
    assert callable(HOURS.__init__)


def test_hours_constructor_args():
    sig = inspect.signature(HOURS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::hourvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::HourValue)


def test_siddhi::hourvalue_constructor_exists():
    assert callable(siddhi::HourValue.__init__)


def test_siddhi::hourvalue_constructor_args():
    sig = inspect.signature(siddhi::HourValue.__init__)
    params = list(sig.parameters.keys())



def test_minutes_is_not_abstract():
    assert not inspect.isabstract(MINUTES)


def test_minutes_constructor_exists():
    assert callable(MINUTES.__init__)


def test_minutes_constructor_args():
    sig = inspect.signature(MINUTES.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::minutevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::MinuteValue)


def test_siddhi::minutevalue_constructor_exists():
    assert callable(siddhi::MinuteValue.__init__)


def test_siddhi::minutevalue_constructor_args():
    sig = inspect.signature(siddhi::MinuteValue.__init__)
    params = list(sig.parameters.keys())



def test_seconds_is_not_abstract():
    assert not inspect.isabstract(SECONDS)


def test_seconds_constructor_exists():
    assert callable(SECONDS.__init__)


def test_seconds_constructor_args():
    sig = inspect.signature(SECONDS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::secondvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::SecondValue)


def test_siddhi::secondvalue_constructor_exists():
    assert callable(siddhi::SecondValue.__init__)


def test_siddhi::secondvalue_constructor_args():
    sig = inspect.signature(siddhi::SecondValue.__init__)
    params = list(sig.parameters.keys())



def test_aggregationtime_is_not_abstract():
    assert not inspect.isabstract(AggregationTime)


def test_aggregationtime_constructor_exists():
    assert callable(AggregationTime.__init__)


def test_aggregationtime_constructor_args():
    sig = inspect.signature(AggregationTime.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::aggregationtimerange_is_not_abstract():
    assert not inspect.isabstract(siddhi::AggregationTimeRange)


def test_siddhi::aggregationtimerange_constructor_exists():
    assert callable(siddhi::AggregationTimeRange.__init__)


def test_siddhi::aggregationtimerange_constructor_args():
    sig = inspect.signature(siddhi::AggregationTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::aggregationtimeinterval_is_not_abstract():
    assert not inspect.isabstract(siddhi::AggregationTimeInterval)


def test_siddhi::aggregationtimeinterval_constructor_exists():
    assert callable(siddhi::AggregationTimeInterval.__init__)


def test_siddhi::aggregationtimeinterval_constructor_args():
    sig = inspect.signature(siddhi::AggregationTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::aggregationtimeduration_is_not_abstract():
    assert not inspect.isabstract(siddhi::AggregationTimeDuration)


def test_siddhi::aggregationtimeduration_constructor_exists():
    assert callable(siddhi::AggregationTimeDuration.__init__)


def test_siddhi::aggregationtimeduration_constructor_args():
    sig = inspect.signature(siddhi::AggregationTimeDuration.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::aggregationtime_is_not_abstract():
    assert not inspect.isabstract(siddhi::AggregationTime)


def test_siddhi::aggregationtime_constructor_exists():
    assert callable(siddhi::AggregationTime.__init__)


def test_siddhi::aggregationtime_constructor_args():
    sig = inspect.signature(siddhi::AggregationTime.__init__)
    params = list(sig.parameters.keys())



def test_output_is_not_abstract():
    assert not inspect.isabstract(OUTPUT)


def test_output_constructor_exists():
    assert callable(OUTPUT.__init__)


def test_output_constructor_args():
    sig = inspect.signature(OUTPUT.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::outputrate_is_not_abstract():
    assert not inspect.isabstract(siddhi::OutputRate)


def test_siddhi::outputrate_constructor_exists():
    assert callable(siddhi::OutputRate.__init__)


def test_siddhi::outputrate_constructor_args():
    sig = inspect.signature(siddhi::OutputRate.__init__)
    params = list(sig.parameters.keys())



def test_window_is_not_abstract():
    assert not inspect.isabstract(WINDOW)


def test_window_constructor_exists():
    assert callable(WINDOW.__init__)


def test_window_constructor_args():
    sig = inspect.signature(WINDOW.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::win_is_not_abstract():
    assert not inspect.isabstract(siddhi::Win)


def test_siddhi::win_constructor_exists():
    assert callable(siddhi::Win.__init__)


def test_siddhi::win_constructor_args():
    sig = inspect.signature(siddhi::Win.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::basicsourcestreamhandlers1_is_not_abstract():
    assert not inspect.isabstract(siddhi::BasicSourceStreamHandlers1)


def test_siddhi::basicsourcestreamhandlers1_constructor_exists():
    assert callable(siddhi::BasicSourceStreamHandlers1.__init__)


def test_siddhi::basicsourcestreamhandlers1_constructor_args():
    sig = inspect.signature(siddhi::BasicSourceStreamHandlers1.__init__)
    params = list(sig.parameters.keys())



def test_aggregate_is_not_abstract():
    assert not inspect.isabstract(AGGREGATE)


def test_aggregate_constructor_exists():
    assert callable(AGGREGATE.__init__)


def test_aggregate_constructor_args():
    sig = inspect.signature(AGGREGATE.__init__)
    params = list(sig.parameters.keys())



def test_from_is_not_abstract():
    assert not inspect.isabstract(FROM)


def test_from_constructor_exists():
    assert callable(FROM.__init__)


def test_from_constructor_args():
    sig = inspect.signature(FROM.__init__)
    params = list(sig.parameters.keys())



def test_aggregation_is_not_abstract():
    assert not inspect.isabstract(AGGREGATION)


def test_aggregation_constructor_exists():
    assert callable(AGGREGATION.__init__)


def test_aggregation_constructor_args():
    sig = inspect.signature(AGGREGATION.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::functionbody_is_not_abstract():
    assert not inspect.isabstract(siddhi::FunctionBody)


def test_siddhi::functionbody_constructor_exists():
    assert callable(siddhi::FunctionBody.__init__)


def test_siddhi::functionbody_constructor_args():
    sig = inspect.signature(siddhi::FunctionBody.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_siddhi::functionbody_has_value():
    assert hasattr(siddhi::FunctionBody, "value")
    descriptor = None
    for klass in siddhi::FunctionBody.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::attributetype_is_not_abstract():
    assert not inspect.isabstract(siddhi::AttributeType)


def test_siddhi::attributetype_constructor_exists():
    assert callable(siddhi::AttributeType.__init__)


def test_siddhi::attributetype_constructor_args():
    sig = inspect.signature(siddhi::AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::languagename_is_not_abstract():
    assert not inspect.isabstract(siddhi::LanguageName)


def test_siddhi::languagename_constructor_exists():
    assert callable(siddhi::LanguageName.__init__)


def test_siddhi::languagename_constructor_args():
    sig = inspect.signature(siddhi::LanguageName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi::languagename_has_id():
    assert hasattr(siddhi::LanguageName, "id")
    descriptor = None
    for klass in siddhi::LanguageName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::functionname_is_not_abstract():
    assert not inspect.isabstract(siddhi::FunctionName)


def test_siddhi::functionname_constructor_exists():
    assert callable(siddhi::FunctionName.__init__)


def test_siddhi::functionname_constructor_args():
    sig = inspect.signature(siddhi::FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi::functionname_has_id():
    assert hasattr(siddhi::FunctionName, "id")
    descriptor = None
    for klass in siddhi::FunctionName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_return_is_not_abstract():
    assert not inspect.isabstract(RETURN)


def test_return_constructor_exists():
    assert callable(RETURN.__init__)


def test_return_constructor_args():
    sig = inspect.signature(RETURN.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::queryoutput_is_not_abstract():
    assert not inspect.isabstract(siddhi::QueryOutput)


def test_siddhi::queryoutput_constructor_exists():
    assert callable(siddhi::QueryOutput.__init__)


def test_siddhi::queryoutput_constructor_args():
    sig = inspect.signature(siddhi::QueryOutput.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::anonymousstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::AnonymousStream)


def test_siddhi::anonymousstream_constructor_exists():
    assert callable(siddhi::AnonymousStream.__init__)


def test_siddhi::anonymousstream_constructor_args():
    sig = inspect.signature(siddhi::AnonymousStream.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(FUNCTION)


def test_function_constructor_exists():
    assert callable(FUNCTION.__init__)


def test_function_constructor_args():
    sig = inspect.signature(FUNCTION.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::stringvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::StringValue)


def test_siddhi::stringvalue_constructor_exists():
    assert callable(siddhi::StringValue.__init__)


def test_siddhi::stringvalue_constructor_args():
    sig = inspect.signature(siddhi::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "sl" in params, "Missing parameter 'sl'"

def test_siddhi::stringvalue_has_sl():
    assert hasattr(siddhi::StringValue, "sl")
    descriptor = None
    for klass in siddhi::StringValue.__mro__:
        if "sl" in klass.__dict__:
            descriptor = klass.__dict__["sl"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::timevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi::TimeValue)


def test_siddhi::timevalue_constructor_exists():
    assert callable(siddhi::TimeValue.__init__)


def test_siddhi::timevalue_constructor_args():
    sig = inspect.signature(siddhi::TimeValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::every_is_not_abstract():
    assert not inspect.isabstract(siddhi::EVERY)


def test_siddhi::every_constructor_exists():
    assert callable(siddhi::EVERY.__init__)


def test_siddhi::every_constructor_args():
    sig = inspect.signature(siddhi::EVERY.__init__)
    params = list(sig.parameters.keys())
    assert "every1" in params, "Missing parameter 'every1'"

def test_siddhi::every_has_every1():
    assert hasattr(siddhi::EVERY, "every1")
    descriptor = None
    for klass in siddhi::EVERY.__mro__:
        if "every1" in klass.__dict__:
            descriptor = klass.__dict__["every1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::triggername_is_not_abstract():
    assert not inspect.isabstract(siddhi::TriggerName)


def test_siddhi::triggername_constructor_exists():
    assert callable(siddhi::TriggerName.__init__)


def test_siddhi::triggername_constructor_args():
    sig = inspect.signature(siddhi::TriggerName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi::triggername_has_id():
    assert hasattr(siddhi::TriggerName, "id")
    descriptor = None
    for klass in siddhi::TriggerName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_at_is_not_abstract():
    assert not inspect.isabstract(AT)


def test_at_constructor_exists():
    assert callable(AT.__init__)


def test_at_constructor_args():
    sig = inspect.signature(AT.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(TRIGGER)


def test_trigger_constructor_exists():
    assert callable(TRIGGER.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(TRIGGER.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::outputeventtype_is_not_abstract():
    assert not inspect.isabstract(siddhi::OutputEventType)


def test_siddhi::outputeventtype_constructor_exists():
    assert callable(siddhi::OutputEventType.__init__)


def test_siddhi::outputeventtype_constructor_args():
    sig = inspect.signature(siddhi::OutputEventType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::functionoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi::FunctionOperation)


def test_siddhi::functionoperation_constructor_exists():
    assert callable(siddhi::FunctionOperation.__init__)


def test_siddhi::functionoperation_constructor_args():
    sig = inspect.signature(siddhi::FunctionOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::appannotation_is_not_abstract():
    assert not inspect.isabstract(siddhi::AppAnnotation)


def test_siddhi::appannotation_constructor_exists():
    assert callable(siddhi::AppAnnotation.__init__)


def test_siddhi::appannotation_constructor_args():
    sig = inspect.signature(siddhi::AppAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::executionplan_is_not_abstract():
    assert not inspect.isabstract(siddhi::ExecutionPlan)


def test_siddhi::executionplan_constructor_exists():
    assert callable(siddhi::ExecutionPlan.__init__)


def test_siddhi::executionplan_constructor_args():
    sig = inspect.signature(siddhi::ExecutionPlan.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(TABLE)


def test_table_constructor_exists():
    assert callable(TABLE.__init__)


def test_table_constructor_args():
    sig = inspect.signature(TABLE.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::features_is_not_abstract():
    assert not inspect.isabstract(siddhi::Features)


def test_siddhi::features_constructor_exists():
    assert callable(siddhi::Features.__init__)


def test_siddhi::features_constructor_args():
    sig = inspect.signature(siddhi::Features.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::source1_is_not_abstract():
    assert not inspect.isabstract(siddhi::Source1)


def test_siddhi::source1_constructor_exists():
    assert callable(siddhi::Source1.__init__)


def test_siddhi::source1_constructor_args():
    sig = inspect.signature(siddhi::Source1.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"

def test_siddhi::source1_has_inner():
    assert hasattr(siddhi::Source1, "inner")
    descriptor = None
    for klass in siddhi::Source1.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_siddhi::annotation_is_not_abstract():
    assert not inspect.isabstract(siddhi::Annotation)


def test_siddhi::annotation_constructor_exists():
    assert callable(siddhi::Annotation.__init__)


def test_siddhi::annotation_constructor_args():
    sig = inspect.signature(siddhi::Annotation.__init__)
    params = list(sig.parameters.keys())



def test_stream_is_not_abstract():
    assert not inspect.isabstract(STREAM)


def test_stream_constructor_exists():
    assert callable(STREAM.__init__)


def test_stream_constructor_args():
    sig = inspect.signature(STREAM.__init__)
    params = list(sig.parameters.keys())



def test_define_is_not_abstract():
    assert not inspect.isabstract(DEFINE)


def test_define_constructor_exists():
    assert callable(DEFINE.__init__)


def test_define_constructor_args():
    sig = inspect.signature(DEFINE.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::keyword_is_not_abstract():
    assert not inspect.isabstract(siddhi::Keyword)


def test_siddhi::keyword_constructor_exists():
    assert callable(siddhi::Keyword.__init__)


def test_siddhi::keyword_constructor_args():
    sig = inspect.signature(siddhi::Keyword.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitiontable_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionTable)


def test_siddhi::definitiontable_constructor_exists():
    assert callable(siddhi::DefinitionTable.__init__)


def test_siddhi::definitiontable_constructor_args():
    sig = inspect.signature(siddhi::DefinitionTable.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitionstream_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionStream)


def test_siddhi::definitionstream_constructor_exists():
    assert callable(siddhi::DefinitionStream.__init__)


def test_siddhi::definitionstream_constructor_args():
    sig = inspect.signature(siddhi::DefinitionStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::query_is_not_abstract():
    assert not inspect.isabstract(siddhi::Query)


def test_siddhi::query_constructor_exists():
    assert callable(siddhi::Query.__init__)


def test_siddhi::query_constructor_args():
    sig = inspect.signature(siddhi::Query.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::execpartition_is_not_abstract():
    assert not inspect.isabstract(siddhi::ExecPartition)


def test_siddhi::execpartition_constructor_exists():
    assert callable(siddhi::ExecPartition.__init__)


def test_siddhi::execpartition_constructor_args():
    sig = inspect.signature(siddhi::ExecPartition.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::executionelement_is_not_abstract():
    assert not inspect.isabstract(siddhi::ExecutionElement)


def test_siddhi::executionelement_constructor_exists():
    assert callable(siddhi::ExecutionElement.__init__)


def test_siddhi::executionelement_constructor_args():
    sig = inspect.signature(siddhi::ExecutionElement.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitionaggregation_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionAggregation)


def test_siddhi::definitionaggregation_constructor_exists():
    assert callable(siddhi::DefinitionAggregation.__init__)


def test_siddhi::definitionaggregation_constructor_args():
    sig = inspect.signature(siddhi::DefinitionAggregation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitionfunction_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionFunction)


def test_siddhi::definitionfunction_constructor_exists():
    assert callable(siddhi::DefinitionFunction.__init__)


def test_siddhi::definitionfunction_constructor_args():
    sig = inspect.signature(siddhi::DefinitionFunction.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitiontrigger_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionTrigger)


def test_siddhi::definitiontrigger_constructor_exists():
    assert callable(siddhi::DefinitionTrigger.__init__)


def test_siddhi::definitiontrigger_constructor_args():
    sig = inspect.signature(siddhi::DefinitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::definitionwindow_is_not_abstract():
    assert not inspect.isabstract(siddhi::DefinitionWindow)


def test_siddhi::definitionwindow_constructor_exists():
    assert callable(siddhi::DefinitionWindow.__init__)


def test_siddhi::definitionwindow_constructor_args():
    sig = inspect.signature(siddhi::DefinitionWindow.__init__)
    params = list(sig.parameters.keys())



def test_siddhi::siddhiql_is_not_abstract():
    assert not inspect.isabstract(siddhi::SiddhiQL)


def test_siddhi::siddhiql_constructor_exists():
    assert callable(siddhi::SiddhiQL.__init__)


def test_siddhi::siddhiql_constructor_args():
    sig = inspect.signature(siddhi::SiddhiQL.__init__)
    params = list(sig.parameters.keys())


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
siddhi::MILLISECONDS_strategy = st.builds(
    siddhi::MILLISECONDS,
    millisec=
        safe_text,
    millisecond=
        safe_text,
    milliseconds=
        safe_text
)
siddhi::SECONDS_strategy = st.builds(
    siddhi::SECONDS,
    sec=
        safe_text,
    seconds=
        safe_text,
    second=
        safe_text
)
siddhi::OUTER_strategy = st.builds(
    siddhi::OUTER,
    outer=
        safe_text
)
siddhi::INNER_strategy = st.builds(
    siddhi::INNER,
    inner=
        safe_text
)
siddhi::JOIN_strategy = st.builds(
    siddhi::JOIN,
    join=
        safe_text
)
siddhi::FULL_strategy = st.builds(
    siddhi::FULL,
    full=
        safe_text
)
siddhi::RIGHT_strategy = st.builds(
    siddhi::RIGHT,
    right=
        safe_text
)
siddhi::LEFT_strategy = st.builds(
    siddhi::LEFT,
    left=
        safe_text
)
siddhi::WITHIN_strategy = st.builds(
    siddhi::WITHIN,
    within=
        safe_text
)
siddhi::YEARS_strategy = st.builds(
    siddhi::YEARS,
    years=
        safe_text,
    year=
        safe_text
)
siddhi::PER_strategy = st.builds(
    siddhi::PER,
    per=
        safe_text
)
siddhi::SET_strategy = st.builds(
    siddhi::SET,
    set=
        safe_text
)
siddhi::AGGREGATE_strategy = st.builds(
    siddhi::AGGREGATE,
    agrregate=
        safe_text
)
siddhi::AGGREGATION_strategy = st.builds(
    siddhi::AGGREGATION,
    aggre=
        safe_text
)
siddhi::WITH_strategy = st.builds(
    siddhi::WITH,
    wi=
        safe_text
)
siddhi::PARTITION_strategy = st.builds(
    siddhi::PARTITION,
    partition=
        safe_text
)
siddhi::END_strategy = st.builds(
    siddhi::END,
    end=
        safe_text
)
siddhi::UPDATE_strategy = st.builds(
    siddhi::UPDATE,
    update=
        safe_text
)
siddhi::FOR_strategy = st.builds(
    siddhi::FOR,
    for_=
        safe_text
)
siddhi::DELETE_strategy = st.builds(
    siddhi::DELETE,
    delete=
        safe_text
)
siddhi::PLAN_strategy = st.builds(
    siddhi::PLAN,
    plan=
        safe_text
)
siddhi::BEGIN_strategy = st.builds(
    siddhi::BEGIN,
    begin=
        safe_text
)
siddhi::INTO_strategy = st.builds(
    siddhi::INTO,
    into=
        safe_text
)
siddhi::INSERT_strategy = st.builds(
    siddhi::INSERT,
    insert=
        safe_text
)
siddhi::FIRST_strategy = st.builds(
    siddhi::FIRST,
    first=
        safe_text
)
siddhi::SNAPSHOT_strategy = st.builds(
    siddhi::SNAPSHOT,
    snapshot=
        safe_text
)
siddhi::HAVING_strategy = st.builds(
    siddhi::HAVING,
    having=
        safe_text
)
siddhi::BY_strategy = st.builds(
    siddhi::BY,
    by=
        safe_text
)
siddhi::GROUP_strategy = st.builds(
    siddhi::GROUP,
    group=
        safe_text
)
siddhi::SELECT_strategy = st.builds(
    siddhi::SELECT,
    select=
        safe_text
)
siddhi::DOUBLE_strategy = st.builds(
    siddhi::DOUBLE,
    double=
        safe_text
)
siddhi::LONG_strategy = st.builds(
    siddhi::LONG,
    long=
        safe_text
)
siddhi::INTS_strategy = st.builds(
    siddhi::INTS,
    int=
        safe_text
)
siddhi::STRINGS_strategy = st.builds(
    siddhi::STRINGS,
    string=
        safe_text
)
siddhi::OUTPUT_strategy = st.builds(
    siddhi::OUTPUT,
    output=
        safe_text
)
siddhi::WINDOW_strategy = st.builds(
    siddhi::WINDOW,
    window=
        safe_text
)
siddhi::TABLE_strategy = st.builds(
    siddhi::TABLE,
    table=
        safe_text
)
siddhi::FROM_strategy = st.builds(
    siddhi::FROM,
    from_=
        safe_text
)
siddhi::RETURN_strategy = st.builds(
    siddhi::RETURN,
    return_=
        safe_text
)
siddhi::FUNCTION_strategy = st.builds(
    siddhi::FUNCTION,
    function=
        safe_text
)
siddhi::AT_strategy = st.builds(
    siddhi::AT,
    at=
        safe_text
)
siddhi::TRIGGER_strategy = st.builds(
    siddhi::TRIGGER,
    trigger=
        safe_text
)
siddhi::NULL_strategy = st.builds(
    siddhi::NULL,
    null=
        safe_text
)
siddhi::IS_strategy = st.builds(
    siddhi::IS,
    is_=
        safe_text
)
siddhi::LAST_strategy = st.builds(
    siddhi::LAST,
    last=
        safe_text
)
siddhi::CURRENT_strategy = st.builds(
    siddhi::CURRENT,
    currt=
        safe_text
)
siddhi::EXPIRED_strategy = st.builds(
    siddhi::EXPIRED,
    expired=
        safe_text
)
siddhi::RAW_strategy = st.builds(
    siddhi::RAW,
    raw=
        safe_text
)
siddhi::EVENTS_strategy = st.builds(
    siddhi::EVENTS,
    events=
        safe_text
)
siddhi::ALL_strategy = st.builds(
    siddhi::ALL,
    all=
        safe_text
)
siddhi::OBJECT_strategy = st.builds(
    siddhi::OBJECT,
    object=
        safe_text
)
siddhi::BOOL_strategy = st.builds(
    siddhi::BOOL,
    bool=
        safe_text
)
siddhi::FLOAT_strategy = st.builds(
    siddhi::FLOAT,
    float=
        safe_text
)
EveryAbsentSequenceSourceChain_strategy = st.builds(
    EveryAbsentSequenceSourceChain,
)
EverySequenceSourceChain_strategy = st.builds(
    EverySequenceSourceChain,
)
BasicAbsentPatternSource_strategy = st.builds(
    BasicAbsentPatternSource,
)
siddhi::DEFINE_strategy = st.builds(
    siddhi::DEFINE,
    define=
        safe_text
)
siddhi::STREAM_strategy = st.builds(
    siddhi::STREAM,
    str=
        safe_text
)
AppAnnotation_strategy = st.builds(
    AppAnnotation,
)
siddhi::APP_strategy = st.builds(
    siddhi::APP,
    ap=
        safe_text
)
siddhi::IN_strategy = st.builds(
    siddhi::IN,
    in_=
        safe_text
)
RightAbsentPatternSource_strategy = st.builds(
    RightAbsentPatternSource,
)
LeftAbsentPatternSource_strategy = st.builds(
    LeftAbsentPatternSource,
)
EveryAbsentPatternSource_strategy = st.builds(
    EveryAbsentPatternSource,
)
LogicalAbsentStatefulSource_strategy = st.builds(
    LogicalAbsentStatefulSource,
)
Name_strategy = st.builds(
    Name,
)
siddhi::L_strategy = st.builds(
    siddhi::L,
    l=
        safe_text
)
SignedLongValue_strategy = st.builds(
    SignedLongValue,
)
siddhi::LONG::LITERAL_strategy = st.builds(
    siddhi::LONG::LITERAL,
)
siddhi::F_strategy = st.builds(
    siddhi::F,
    f=
        safe_text
)
SignedFloatValue_strategy = st.builds(
    SignedFloatValue,
)
siddhi::FLOAT::LITERAL_strategy = st.builds(
    siddhi::FLOAT::LITERAL,
)
siddhi::D_strategy = st.builds(
    siddhi::D,
    d=
        safe_text
)
siddhi::E_strategy = st.builds(
    siddhi::E,
    e=
        safe_text
)
SignedDoubleValue_strategy = st.builds(
    SignedDoubleValue,
)
siddhi::DOUBLE::LITERAL_strategy = st.builds(
    siddhi::DOUBLE::LITERAL,
)
MILLISECONDS_strategy = st.builds(
    MILLISECONDS,
)
siddhi::MillisecondValue_strategy = st.builds(
    siddhi::MillisecondValue,
)
siddhi::FunctionId_strategy = st.builds(
    siddhi::FunctionId,
)
siddhi::FunctionNamespace_strategy = st.builds(
    siddhi::FunctionNamespace,
)
siddhi::SignedLongValue_strategy = st.builds(
    siddhi::SignedLongValue,
)
FALSE_strategy = st.builds(
    FALSE,
)
TRUE_strategy = st.builds(
    TRUE,
)
siddhi::AttributeList_strategy = st.builds(
    siddhi::AttributeList,
)
siddhi::FeaturesOrOutAttr_strategy = st.builds(
    siddhi::FeaturesOrOutAttr,
    name=
        safe_text
)
siddhi::FeaturesOrOutAttrReference_strategy = st.builds(
    siddhi::FeaturesOrOutAttrReference,
)
siddhi::SignedFloatValue_strategy = st.builds(
    siddhi::SignedFloatValue,
)
siddhi::SignedDoubleValue_strategy = st.builds(
    siddhi::SignedDoubleValue,
)
siddhi::BoolValue_strategy = st.builds(
    siddhi::BoolValue,
)
siddhi::AttributeNameReference_strategy = st.builds(
    siddhi::AttributeNameReference,
)
siddhi::Source1OrStandardStatefulSource_strategy = st.builds(
    siddhi::Source1OrStandardStatefulSource,
    name=
        safe_text
)
PatternCollectionStatefulSource_strategy = st.builds(
    PatternCollectionStatefulSource,
)
SequenceCollectionStatefulSource_strategy = st.builds(
    SequenceCollectionStatefulSource,
)
siddhi::Literal_strategy = st.builds(
    siddhi::Literal,
)
MathDivmulOperation_strategy = st.builds(
    MathDivmulOperation,
)
siddhi::MathOtherOperations_strategy = st.builds(
    siddhi::MathOtherOperations,
)
MathAddsubOperation_strategy = st.builds(
    MathAddsubOperation,
)
siddhi::MathDivmulOperation_strategy = st.builds(
    siddhi::MathDivmulOperation,
    multiply=
        safe_text,
    devide=
        safe_text,
    mod=
        safe_text
)
siddhi::SourceOrEventReference_strategy = st.builds(
    siddhi::SourceOrEventReference,
)
SetAssignment_strategy = st.builds(
    SetAssignment,
)
siddhi::ConstantValue_strategy = st.builds(
    siddhi::ConstantValue,
    siv=
        safe_text
)
siddhi::StreamReference_strategy = st.builds(
    siddhi::StreamReference,
    hash=
        safe_text
)
NULL_strategy = st.builds(
    NULL,
)
IS_strategy = st.builds(
    IS,
)
MathOtherOperations_strategy = st.builds(
    MathOtherOperations,
)
siddhi::NullCheck_strategy = st.builds(
    siddhi::NullCheck,
)
siddhi::BasicSourceStreamHandlers_strategy = st.builds(
    siddhi::BasicSourceStreamHandlers,
)
MathOperation_strategy = st.builds(
    MathOperation,
)
siddhi::MathAddsubOperation_strategy = st.builds(
    siddhi::MathAddsubOperation,
    substract=
        safe_text,
    add=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
siddhi::MathOperation_strategy = st.builds(
    siddhi::MathOperation,
)
siddhi::StreamFunction_strategy = st.builds(
    siddhi::StreamFunction,
)
siddhi::Filter_strategy = st.builds(
    siddhi::Filter,
)
siddhi::BasicSourceStreamHandler_strategy = st.builds(
    siddhi::BasicSourceStreamHandler,
)
siddhi::UNIDIRECTIONAL_strategy = st.builds(
    siddhi::UNIDIRECTIONAL,
    unidirectional=
        safe_text
)
siddhi::JoinSource_strategy = st.builds(
    siddhi::JoinSource,
)
StandardStream_strategy = st.builds(
    StandardStream,
)
JoinSource_strategy = st.builds(
    JoinSource,
)
siddhi::MainSource_strategy = st.builds(
    siddhi::MainSource,
)
JoinStream_strategy = st.builds(
    JoinStream,
)
INNER_strategy = st.builds(
    INNER,
)
FULL_strategy = st.builds(
    FULL,
)
RIGHT_strategy = st.builds(
    RIGHT,
)
JOIN_strategy = st.builds(
    JOIN,
)
OUTER_strategy = st.builds(
    OUTER,
)
LEFT_strategy = st.builds(
    LEFT,
)
PER_strategy = st.builds(
    PER,
)
WITHIN_strategy = st.builds(
    WITHIN,
)
siddhi::joins_strategy = st.builds(
    siddhi::joins,
)
siddhi::Per1_strategy = st.builds(
    siddhi::Per1,
)
siddhi::WithinTimeRange_strategy = st.builds(
    siddhi::WithinTimeRange,
)
AbsentPatternSourceChain_strategy = st.builds(
    AbsentPatternSourceChain,
)
siddhi::EveryAbsentPatternSource_strategy = st.builds(
    siddhi::EveryAbsentPatternSource,
)
siddhi::RightAbsentPatternSource_strategy = st.builds(
    siddhi::RightAbsentPatternSource,
    fb2=
        safe_text
)
siddhi::LeftAbsentPatternSource_strategy = st.builds(
    siddhi::LeftAbsentPatternSource,
    fb1=
        safe_text
)
siddhi::PatternCollectionStatefulSource_strategy = st.builds(
    siddhi::PatternCollectionStatefulSource,
)
siddhi::PatternSource_strategy = st.builds(
    siddhi::PatternSource,
)
siddhi::BasicSource_strategy = st.builds(
    siddhi::BasicSource,
)
siddhi::NOT_strategy = st.builds(
    siddhi::NOT,
    not1=
        safe_text
)
siddhi::Collect_strategy = st.builds(
    siddhi::Collect,
    start=
        safe_text,
    end=
        safe_text
)
siddhi::AND_strategy = st.builds(
    siddhi::AND,
    and_=
        safe_text
)
SequenceSource_strategy = st.builds(
    SequenceSource,
)
siddhi::LogicalAbsentStatefulSource_strategy = st.builds(
    siddhi::LogicalAbsentStatefulSource,
)
siddhi::LogicalStatefulSource_strategy = st.builds(
    siddhi::LogicalStatefulSource,
)
siddhi::SequenceCollectionStatefulSource_strategy = st.builds(
    siddhi::SequenceCollectionStatefulSource,
)
SequenceSourceChain_strategy = st.builds(
    SequenceSourceChain,
)
siddhi::PatternSourceChain_strategy = st.builds(
    siddhi::PatternSourceChain,
    op=
        safe_text
)
PatternStream_strategy = st.builds(
    PatternStream,
)
siddhi::AbsentPatternSourceChain_strategy = st.builds(
    siddhi::AbsentPatternSourceChain,
)
siddhi::EveryPatternSourceChain_strategy = st.builds(
    siddhi::EveryPatternSourceChain,
    op=
        safe_text
)
siddhi::RightAbsentSequenceSource_strategy = st.builds(
    siddhi::RightAbsentSequenceSource,
    op=
        safe_text,
    cp=
        safe_text,
    comma=
        safe_text,
    comm=
        safe_text
)
siddhi::LeftAbsentSequenceSource_strategy = st.builds(
    siddhi::LeftAbsentSequenceSource,
    cp=
        safe_text,
    comma=
        safe_text,
    op=
        safe_text,
    comm=
        safe_text
)
siddhi::BasicAbsentPatternSource_strategy = st.builds(
    siddhi::BasicAbsentPatternSource,
)
siddhi::EObject_strategy = st.builds(
    siddhi::EObject,
)
HAVING_strategy = st.builds(
    HAVING,
)
GROUP_strategy = st.builds(
    GROUP,
)
siddhi::HavingExpr_strategy = st.builds(
    siddhi::HavingExpr,
)
siddhi::AbsentSequenceSourceChain_strategy = st.builds(
    siddhi::AbsentSequenceSourceChain,
)
siddhi::SequenceSourceChain_strategy = st.builds(
    siddhi::SequenceSourceChain,
    op=
        safe_text
)
siddhi::WithinTime_strategy = st.builds(
    siddhi::WithinTime,
)
siddhi::SequenceSource_strategy = st.builds(
    siddhi::SequenceSource,
)
siddhi::EveryAbsentSequenceSourceChain_strategy = st.builds(
    siddhi::EveryAbsentSequenceSourceChain,
)
siddhi::EverySequenceSourceChain_strategy = st.builds(
    siddhi::EverySequenceSourceChain,
)
siddhi::PatternStream_strategy = st.builds(
    siddhi::PatternStream,
)
siddhi::SequenceStream_strategy = st.builds(
    siddhi::SequenceStream,
)
siddhi::JoinStream_strategy = st.builds(
    siddhi::JoinStream,
)
siddhi::Attribute_strategy = st.builds(
    siddhi::Attribute,
)
siddhi::OutputAttribute_strategy = st.builds(
    siddhi::OutputAttribute,
)
SELECT_strategy = st.builds(
    SELECT,
)
FIRST_strategy = st.builds(
    FIRST,
)
LAST_strategy = st.builds(
    LAST,
)
siddhi::AttributeIndex_strategy = st.builds(
    siddhi::AttributeIndex,
)
siddhi::MathGtLtOperation_strategy = st.builds(
    siddhi::MathGtLtOperation,
    lt=
        safe_text,
    gt_eq=
        safe_text,
    gt=
        safe_text,
    lt_eq=
        safe_text
)
siddhi::MathInOperation_strategy = st.builds(
    siddhi::MathInOperation,
)
siddhi::NotOperation_strategy = st.builds(
    siddhi::NotOperation,
)
siddhi::MathEqualOperation_strategy = st.builds(
    siddhi::MathEqualOperation,
    not_eq=
        safe_text,
    eq=
        safe_text
)
siddhi::MINUTES_strategy = st.builds(
    siddhi::MINUTES,
    minutes=
        safe_text,
    min=
        safe_text,
    minute=
        safe_text
)
siddhi::HOURS_strategy = st.builds(
    siddhi::HOURS,
    hours=
        safe_text,
    hour=
        safe_text
)
siddhi::DAYS_strategy = st.builds(
    siddhi::DAYS,
    days=
        safe_text,
    day=
        safe_text
)
siddhi::WEEKS_strategy = st.builds(
    siddhi::WEEKS,
    weeks=
        safe_text,
    week=
        safe_text
)
siddhi::MONTHS_strategy = st.builds(
    siddhi::MONTHS,
    months=
        safe_text,
    month=
        safe_text
)
siddhi::MathLogicalOperation_strategy = st.builds(
    siddhi::MathLogicalOperation,
)
siddhi::RightAbsentPatternSource1_strategy = st.builds(
    siddhi::RightAbsentPatternSource1,
    fb=
        safe_text
)
siddhi::LeftAbsentPatternSource1_strategy = st.builds(
    siddhi::LeftAbsentPatternSource1,
    fb=
        safe_text
)
RightAbsentSequenceSource_strategy = st.builds(
    RightAbsentSequenceSource,
)
siddhi::RightAbsentSequenceSource1_strategy = st.builds(
    siddhi::RightAbsentSequenceSource1,
)
LeftAbsentSequenceSource_strategy = st.builds(
    LeftAbsentSequenceSource,
)
siddhi::LeftAbsentSequenceSource1_strategy = st.builds(
    siddhi::LeftAbsentSequenceSource1,
)
siddhi::TRUE_strategy = st.builds(
    siddhi::TRUE,
    tr=
        safe_text
)
siddhi::FALSE_strategy = st.builds(
    siddhi::FALSE,
    fals=
        safe_text
)
SNAPSHOT_strategy = st.builds(
    SNAPSHOT,
)
CURRENT_strategy = st.builds(
    CURRENT,
)
EXPIRED_strategy = st.builds(
    EXPIRED,
)
RAW_strategy = st.builds(
    RAW,
)
EVENTS_strategy = st.builds(
    EVENTS,
)
ALL_strategy = st.builds(
    ALL,
)
siddhi::OutputRateType_strategy = st.builds(
    siddhi::OutputRateType,
)
siddhi::SetAssignment_strategy = st.builds(
    siddhi::SetAssignment,
)
SET_strategy = st.builds(
    SET,
)
siddhi::SetClause_strategy = st.builds(
    siddhi::SetClause,
)
siddhi::OR_strategy = st.builds(
    siddhi::OR,
    or_=
        safe_text
)
siddhi::ConditionRange_strategy = st.builds(
    siddhi::ConditionRange,
)
siddhi::OF_strategy = st.builds(
    siddhi::OF,
    of=
        safe_text
)
PartitionWithStream_strategy = st.builds(
    PartitionWithStream,
)
siddhi::ConditionRanges_strategy = st.builds(
    siddhi::ConditionRanges,
)
siddhi::ON_strategy = st.builds(
    siddhi::ON,
    on=
        safe_text
)
siddhi::Target_strategy = st.builds(
    siddhi::Target,
)
UPDATE_strategy = st.builds(
    UPDATE,
)
FOR_strategy = st.builds(
    FOR,
)
siddhi::ForTime_strategy = st.builds(
    siddhi::ForTime,
)
DELETE_strategy = st.builds(
    DELETE,
)
INTO_strategy = st.builds(
    INTO,
)
INSERT_strategy = st.builds(
    INSERT,
)
siddhi::QuerySection_strategy = st.builds(
    siddhi::QuerySection,
)
siddhi::QueryInput_strategy = st.builds(
    siddhi::QueryInput,
)
siddhi::AS_strategy = st.builds(
    siddhi::AS,
    a=
        safe_text
)
siddhi::Expression_strategy = st.builds(
    siddhi::Expression,
)
siddhi::PropertyValue_strategy = st.builds(
    siddhi::PropertyValue,
)
siddhi::PartitionWithStream_strategy = st.builds(
    siddhi::PartitionWithStream,
)
END_strategy = st.builds(
    END,
)
BEGIN_strategy = st.builds(
    BEGIN,
)
WITH_strategy = st.builds(
    WITH,
)
PARTITION_strategy = st.builds(
    PARTITION,
)
Source1OrStandardStatefulSource_strategy = st.builds(
    Source1OrStandardStatefulSource,
)
siddhi::StreamAlias_strategy = st.builds(
    siddhi::StreamAlias,
)
siddhi::StandardStatefulSource_strategy = st.builds(
    siddhi::StandardStatefulSource,
    one_or_more=
        safe_text,
    zero_or_more=
        safe_text,
    zero_or_one=
        safe_text
)
siddhi::Source_strategy = st.builds(
    siddhi::Source,
)
OBJECT_strategy = st.builds(
    OBJECT,
)
BOOL_strategy = st.builds(
    BOOL,
)
DOUBLE_strategy = st.builds(
    DOUBLE,
)
FLOAT_strategy = st.builds(
    FLOAT,
)
LONG_strategy = st.builds(
    LONG,
)
INTS_strategy = st.builds(
    INTS,
)
STRINGS_strategy = st.builds(
    STRINGS,
)
FeaturesOrOutAttr_strategy = st.builds(
    FeaturesOrOutAttr,
)
siddhi::OutAttr_strategy = st.builds(
    siddhi::OutAttr,
)
siddhi::PropertySeparator_strategy = st.builds(
    siddhi::PropertySeparator,
)
siddhi::AttributeReference_strategy = st.builds(
    siddhi::AttributeReference,
    name=
        safe_text,
    hash2=
        safe_text,
    hash1=
        safe_text
)
siddhi::GroupByQuerySelection_strategy = st.builds(
    siddhi::GroupByQuerySelection,
)
siddhi::StandardStream_strategy = st.builds(
    siddhi::StandardStream,
)
BY_strategy = st.builds(
    BY,
)
siddhi::GroupBy_strategy = st.builds(
    siddhi::GroupBy,
)
siddhi::PropertyName_strategy = st.builds(
    siddhi::PropertyName,
)
siddhi::AnnotationElement_strategy = st.builds(
    siddhi::AnnotationElement,
)
siddhi::Name_strategy = st.builds(
    siddhi::Name,
    na=
        safe_text
)
YEARS_strategy = st.builds(
    YEARS,
)
siddhi::YearValue_strategy = st.builds(
    siddhi::YearValue,
)
MONTHS_strategy = st.builds(
    MONTHS,
)
siddhi::MonthValue_strategy = st.builds(
    siddhi::MonthValue,
)
WEEKS_strategy = st.builds(
    WEEKS,
)
siddhi::WeekValue_strategy = st.builds(
    siddhi::WeekValue,
)
DAYS_strategy = st.builds(
    DAYS,
)
siddhi::DayValue_strategy = st.builds(
    siddhi::DayValue,
)
HOURS_strategy = st.builds(
    HOURS,
)
siddhi::HourValue_strategy = st.builds(
    siddhi::HourValue,
)
MINUTES_strategy = st.builds(
    MINUTES,
)
siddhi::MinuteValue_strategy = st.builds(
    siddhi::MinuteValue,
)
SECONDS_strategy = st.builds(
    SECONDS,
)
siddhi::SecondValue_strategy = st.builds(
    siddhi::SecondValue,
)
AggregationTime_strategy = st.builds(
    AggregationTime,
)
siddhi::AggregationTimeRange_strategy = st.builds(
    siddhi::AggregationTimeRange,
)
siddhi::AggregationTimeInterval_strategy = st.builds(
    siddhi::AggregationTimeInterval,
)
siddhi::AggregationTimeDuration_strategy = st.builds(
    siddhi::AggregationTimeDuration,
)
siddhi::AggregationTime_strategy = st.builds(
    siddhi::AggregationTime,
)
OUTPUT_strategy = st.builds(
    OUTPUT,
)
siddhi::OutputRate_strategy = st.builds(
    siddhi::OutputRate,
)
WINDOW_strategy = st.builds(
    WINDOW,
)
siddhi::Win_strategy = st.builds(
    siddhi::Win,
)
siddhi::BasicSourceStreamHandlers1_strategy = st.builds(
    siddhi::BasicSourceStreamHandlers1,
)
AGGREGATE_strategy = st.builds(
    AGGREGATE,
)
FROM_strategy = st.builds(
    FROM,
)
AGGREGATION_strategy = st.builds(
    AGGREGATION,
)
siddhi::FunctionBody_strategy = st.builds(
    siddhi::FunctionBody,
    value=
        safe_text
)
siddhi::AttributeType_strategy = st.builds(
    siddhi::AttributeType,
)
siddhi::LanguageName_strategy = st.builds(
    siddhi::LanguageName,
    id=
        safe_text
)
siddhi::FunctionName_strategy = st.builds(
    siddhi::FunctionName,
    id=
        safe_text
)
RETURN_strategy = st.builds(
    RETURN,
)
siddhi::QueryOutput_strategy = st.builds(
    siddhi::QueryOutput,
)
siddhi::AnonymousStream_strategy = st.builds(
    siddhi::AnonymousStream,
)
FUNCTION_strategy = st.builds(
    FUNCTION,
)
siddhi::StringValue_strategy = st.builds(
    siddhi::StringValue,
    sl=
        safe_text
)
siddhi::TimeValue_strategy = st.builds(
    siddhi::TimeValue,
)
siddhi::EVERY_strategy = st.builds(
    siddhi::EVERY,
    every1=
        safe_text
)
siddhi::TriggerName_strategy = st.builds(
    siddhi::TriggerName,
    id=
        safe_text
)
AT_strategy = st.builds(
    AT,
)
TRIGGER_strategy = st.builds(
    TRIGGER,
)
siddhi::OutputEventType_strategy = st.builds(
    siddhi::OutputEventType,
)
siddhi::FunctionOperation_strategy = st.builds(
    siddhi::FunctionOperation,
)
siddhi::AppAnnotation_strategy = st.builds(
    siddhi::AppAnnotation,
)
siddhi::ExecutionPlan_strategy = st.builds(
    siddhi::ExecutionPlan,
)
TABLE_strategy = st.builds(
    TABLE,
)
siddhi::Features_strategy = st.builds(
    siddhi::Features,
)
siddhi::Source1_strategy = st.builds(
    siddhi::Source1,
    inner=
        safe_text
)
siddhi::Annotation_strategy = st.builds(
    siddhi::Annotation,
)
STREAM_strategy = st.builds(
    STREAM,
)
DEFINE_strategy = st.builds(
    DEFINE,
)
siddhi::Keyword_strategy = st.builds(
    siddhi::Keyword,
)
siddhi::DefinitionTable_strategy = st.builds(
    siddhi::DefinitionTable,
)
siddhi::DefinitionStream_strategy = st.builds(
    siddhi::DefinitionStream,
)
siddhi::Query_strategy = st.builds(
    siddhi::Query,
)
siddhi::ExecPartition_strategy = st.builds(
    siddhi::ExecPartition,
)
siddhi::ExecutionElement_strategy = st.builds(
    siddhi::ExecutionElement,
)
siddhi::DefinitionAggregation_strategy = st.builds(
    siddhi::DefinitionAggregation,
)
siddhi::DefinitionFunction_strategy = st.builds(
    siddhi::DefinitionFunction,
)
siddhi::DefinitionTrigger_strategy = st.builds(
    siddhi::DefinitionTrigger,
)
siddhi::DefinitionWindow_strategy = st.builds(
    siddhi::DefinitionWindow,
)
siddhi::SiddhiQL_strategy = st.builds(
    siddhi::SiddhiQL,
)

@given(instance=siddhi::MILLISECONDS_strategy)
@settings(max_examples=50)
def test_siddhi::milliseconds_instantiation(instance):
    assert isinstance(instance, siddhi::MILLISECONDS)

@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_millisec_type(instance):
    assert isinstance(instance.millisec, str)


@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_millisec_setter(instance):
    original = instance.millisec
    instance.millisec = original
    assert instance.millisec == original

@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_millisecond_type(instance):
    assert isinstance(instance.millisecond, str)


@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_millisecond_setter(instance):
    original = instance.millisecond
    instance.millisecond = original
    assert instance.millisecond == original

@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_milliseconds_type(instance):
    assert isinstance(instance.milliseconds, str)


@given(instance=siddhi::MILLISECONDS_strategy)
def test_siddhi::milliseconds_milliseconds_setter(instance):
    original = instance.milliseconds
    instance.milliseconds = original
    assert instance.milliseconds == original

@given(instance=siddhi::SECONDS_strategy)
@settings(max_examples=50)
def test_siddhi::seconds_instantiation(instance):
    assert isinstance(instance, siddhi::SECONDS)

@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_sec_type(instance):
    assert isinstance(instance.sec, str)


@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original

@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_seconds_type(instance):
    assert isinstance(instance.seconds, str)


@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_seconds_setter(instance):
    original = instance.seconds
    instance.seconds = original
    assert instance.seconds == original

@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_second_type(instance):
    assert isinstance(instance.second, str)


@given(instance=siddhi::SECONDS_strategy)
def test_siddhi::seconds_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=siddhi::OUTER_strategy)
@settings(max_examples=50)
def test_siddhi::outer_instantiation(instance):
    assert isinstance(instance, siddhi::OUTER)

@given(instance=siddhi::OUTER_strategy)
def test_siddhi::outer_outer_type(instance):
    assert isinstance(instance.outer, str)


@given(instance=siddhi::OUTER_strategy)
def test_siddhi::outer_outer_setter(instance):
    original = instance.outer
    instance.outer = original
    assert instance.outer == original

@given(instance=siddhi::INNER_strategy)
@settings(max_examples=50)
def test_siddhi::inner_instantiation(instance):
    assert isinstance(instance, siddhi::INNER)

@given(instance=siddhi::INNER_strategy)
def test_siddhi::inner_inner_type(instance):
    assert isinstance(instance.inner, str)


@given(instance=siddhi::INNER_strategy)
def test_siddhi::inner_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=siddhi::JOIN_strategy)
@settings(max_examples=50)
def test_siddhi::join_instantiation(instance):
    assert isinstance(instance, siddhi::JOIN)

@given(instance=siddhi::JOIN_strategy)
def test_siddhi::join_join_type(instance):
    assert isinstance(instance.join, str)


@given(instance=siddhi::JOIN_strategy)
def test_siddhi::join_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=siddhi::FULL_strategy)
@settings(max_examples=50)
def test_siddhi::full_instantiation(instance):
    assert isinstance(instance, siddhi::FULL)

@given(instance=siddhi::FULL_strategy)
def test_siddhi::full_full_type(instance):
    assert isinstance(instance.full, str)


@given(instance=siddhi::FULL_strategy)
def test_siddhi::full_full_setter(instance):
    original = instance.full
    instance.full = original
    assert instance.full == original

@given(instance=siddhi::RIGHT_strategy)
@settings(max_examples=50)
def test_siddhi::right_instantiation(instance):
    assert isinstance(instance, siddhi::RIGHT)

@given(instance=siddhi::RIGHT_strategy)
def test_siddhi::right_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=siddhi::RIGHT_strategy)
def test_siddhi::right_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=siddhi::LEFT_strategy)
@settings(max_examples=50)
def test_siddhi::left_instantiation(instance):
    assert isinstance(instance, siddhi::LEFT)

@given(instance=siddhi::LEFT_strategy)
def test_siddhi::left_left_type(instance):
    assert isinstance(instance.left, str)


@given(instance=siddhi::LEFT_strategy)
def test_siddhi::left_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=siddhi::WITHIN_strategy)
@settings(max_examples=50)
def test_siddhi::within_instantiation(instance):
    assert isinstance(instance, siddhi::WITHIN)

@given(instance=siddhi::WITHIN_strategy)
def test_siddhi::within_within_type(instance):
    assert isinstance(instance.within, str)


@given(instance=siddhi::WITHIN_strategy)
def test_siddhi::within_within_setter(instance):
    original = instance.within
    instance.within = original
    assert instance.within == original

@given(instance=siddhi::YEARS_strategy)
@settings(max_examples=50)
def test_siddhi::years_instantiation(instance):
    assert isinstance(instance, siddhi::YEARS)

@given(instance=siddhi::YEARS_strategy)
def test_siddhi::years_years_type(instance):
    assert isinstance(instance.years, str)


@given(instance=siddhi::YEARS_strategy)
def test_siddhi::years_years_setter(instance):
    original = instance.years
    instance.years = original
    assert instance.years == original

@given(instance=siddhi::YEARS_strategy)
def test_siddhi::years_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=siddhi::YEARS_strategy)
def test_siddhi::years_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=siddhi::PER_strategy)
@settings(max_examples=50)
def test_siddhi::per_instantiation(instance):
    assert isinstance(instance, siddhi::PER)

@given(instance=siddhi::PER_strategy)
def test_siddhi::per_per_type(instance):
    assert isinstance(instance.per, str)


@given(instance=siddhi::PER_strategy)
def test_siddhi::per_per_setter(instance):
    original = instance.per
    instance.per = original
    assert instance.per == original

@given(instance=siddhi::SET_strategy)
@settings(max_examples=50)
def test_siddhi::set_instantiation(instance):
    assert isinstance(instance, siddhi::SET)

@given(instance=siddhi::SET_strategy)
def test_siddhi::set_set_type(instance):
    assert isinstance(instance.set, str)


@given(instance=siddhi::SET_strategy)
def test_siddhi::set_set_setter(instance):
    original = instance.set
    instance.set = original
    assert instance.set == original

@given(instance=siddhi::AGGREGATE_strategy)
@settings(max_examples=50)
def test_siddhi::aggregate_instantiation(instance):
    assert isinstance(instance, siddhi::AGGREGATE)

@given(instance=siddhi::AGGREGATE_strategy)
def test_siddhi::aggregate_agrregate_type(instance):
    assert isinstance(instance.agrregate, str)


@given(instance=siddhi::AGGREGATE_strategy)
def test_siddhi::aggregate_agrregate_setter(instance):
    original = instance.agrregate
    instance.agrregate = original
    assert instance.agrregate == original

@given(instance=siddhi::AGGREGATION_strategy)
@settings(max_examples=50)
def test_siddhi::aggregation_instantiation(instance):
    assert isinstance(instance, siddhi::AGGREGATION)

@given(instance=siddhi::AGGREGATION_strategy)
def test_siddhi::aggregation_aggre_type(instance):
    assert isinstance(instance.aggre, str)


@given(instance=siddhi::AGGREGATION_strategy)
def test_siddhi::aggregation_aggre_setter(instance):
    original = instance.aggre
    instance.aggre = original
    assert instance.aggre == original

@given(instance=siddhi::WITH_strategy)
@settings(max_examples=50)
def test_siddhi::with_instantiation(instance):
    assert isinstance(instance, siddhi::WITH)

@given(instance=siddhi::WITH_strategy)
def test_siddhi::with_wi_type(instance):
    assert isinstance(instance.wi, str)


@given(instance=siddhi::WITH_strategy)
def test_siddhi::with_wi_setter(instance):
    original = instance.wi
    instance.wi = original
    assert instance.wi == original

@given(instance=siddhi::PARTITION_strategy)
@settings(max_examples=50)
def test_siddhi::partition_instantiation(instance):
    assert isinstance(instance, siddhi::PARTITION)

@given(instance=siddhi::PARTITION_strategy)
def test_siddhi::partition_partition_type(instance):
    assert isinstance(instance.partition, str)


@given(instance=siddhi::PARTITION_strategy)
def test_siddhi::partition_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original

@given(instance=siddhi::END_strategy)
@settings(max_examples=50)
def test_siddhi::end_instantiation(instance):
    assert isinstance(instance, siddhi::END)

@given(instance=siddhi::END_strategy)
def test_siddhi::end_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=siddhi::END_strategy)
def test_siddhi::end_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=siddhi::UPDATE_strategy)
@settings(max_examples=50)
def test_siddhi::update_instantiation(instance):
    assert isinstance(instance, siddhi::UPDATE)

@given(instance=siddhi::UPDATE_strategy)
def test_siddhi::update_update_type(instance):
    assert isinstance(instance.update, str)


@given(instance=siddhi::UPDATE_strategy)
def test_siddhi::update_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=siddhi::FOR_strategy)
@settings(max_examples=50)
def test_siddhi::for_instantiation(instance):
    assert isinstance(instance, siddhi::FOR)

@given(instance=siddhi::FOR_strategy)
def test_siddhi::for_for__type(instance):
    assert isinstance(instance.for_, str)


@given(instance=siddhi::FOR_strategy)
def test_siddhi::for_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=siddhi::DELETE_strategy)
@settings(max_examples=50)
def test_siddhi::delete_instantiation(instance):
    assert isinstance(instance, siddhi::DELETE)

@given(instance=siddhi::DELETE_strategy)
def test_siddhi::delete_delete_type(instance):
    assert isinstance(instance.delete, str)


@given(instance=siddhi::DELETE_strategy)
def test_siddhi::delete_delete_setter(instance):
    original = instance.delete
    instance.delete = original
    assert instance.delete == original

@given(instance=siddhi::PLAN_strategy)
@settings(max_examples=50)
def test_siddhi::plan_instantiation(instance):
    assert isinstance(instance, siddhi::PLAN)

@given(instance=siddhi::PLAN_strategy)
def test_siddhi::plan_plan_type(instance):
    assert isinstance(instance.plan, str)


@given(instance=siddhi::PLAN_strategy)
def test_siddhi::plan_plan_setter(instance):
    original = instance.plan
    instance.plan = original
    assert instance.plan == original

@given(instance=siddhi::BEGIN_strategy)
@settings(max_examples=50)
def test_siddhi::begin_instantiation(instance):
    assert isinstance(instance, siddhi::BEGIN)

@given(instance=siddhi::BEGIN_strategy)
def test_siddhi::begin_begin_type(instance):
    assert isinstance(instance.begin, str)


@given(instance=siddhi::BEGIN_strategy)
def test_siddhi::begin_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original

@given(instance=siddhi::INTO_strategy)
@settings(max_examples=50)
def test_siddhi::into_instantiation(instance):
    assert isinstance(instance, siddhi::INTO)

@given(instance=siddhi::INTO_strategy)
def test_siddhi::into_into_type(instance):
    assert isinstance(instance.into, str)


@given(instance=siddhi::INTO_strategy)
def test_siddhi::into_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=siddhi::INSERT_strategy)
@settings(max_examples=50)
def test_siddhi::insert_instantiation(instance):
    assert isinstance(instance, siddhi::INSERT)

@given(instance=siddhi::INSERT_strategy)
def test_siddhi::insert_insert_type(instance):
    assert isinstance(instance.insert, str)


@given(instance=siddhi::INSERT_strategy)
def test_siddhi::insert_insert_setter(instance):
    original = instance.insert
    instance.insert = original
    assert instance.insert == original

@given(instance=siddhi::FIRST_strategy)
@settings(max_examples=50)
def test_siddhi::first_instantiation(instance):
    assert isinstance(instance, siddhi::FIRST)

@given(instance=siddhi::FIRST_strategy)
def test_siddhi::first_first_type(instance):
    assert isinstance(instance.first, str)


@given(instance=siddhi::FIRST_strategy)
def test_siddhi::first_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=siddhi::SNAPSHOT_strategy)
@settings(max_examples=50)
def test_siddhi::snapshot_instantiation(instance):
    assert isinstance(instance, siddhi::SNAPSHOT)

@given(instance=siddhi::SNAPSHOT_strategy)
def test_siddhi::snapshot_snapshot_type(instance):
    assert isinstance(instance.snapshot, str)


@given(instance=siddhi::SNAPSHOT_strategy)
def test_siddhi::snapshot_snapshot_setter(instance):
    original = instance.snapshot
    instance.snapshot = original
    assert instance.snapshot == original

@given(instance=siddhi::HAVING_strategy)
@settings(max_examples=50)
def test_siddhi::having_instantiation(instance):
    assert isinstance(instance, siddhi::HAVING)

@given(instance=siddhi::HAVING_strategy)
def test_siddhi::having_having_type(instance):
    assert isinstance(instance.having, str)


@given(instance=siddhi::HAVING_strategy)
def test_siddhi::having_having_setter(instance):
    original = instance.having
    instance.having = original
    assert instance.having == original

@given(instance=siddhi::BY_strategy)
@settings(max_examples=50)
def test_siddhi::by_instantiation(instance):
    assert isinstance(instance, siddhi::BY)

@given(instance=siddhi::BY_strategy)
def test_siddhi::by_by_type(instance):
    assert isinstance(instance.by, str)


@given(instance=siddhi::BY_strategy)
def test_siddhi::by_by_setter(instance):
    original = instance.by
    instance.by = original
    assert instance.by == original

@given(instance=siddhi::GROUP_strategy)
@settings(max_examples=50)
def test_siddhi::group_instantiation(instance):
    assert isinstance(instance, siddhi::GROUP)

@given(instance=siddhi::GROUP_strategy)
def test_siddhi::group_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=siddhi::GROUP_strategy)
def test_siddhi::group_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=siddhi::SELECT_strategy)
@settings(max_examples=50)
def test_siddhi::select_instantiation(instance):
    assert isinstance(instance, siddhi::SELECT)

@given(instance=siddhi::SELECT_strategy)
def test_siddhi::select_select_type(instance):
    assert isinstance(instance.select, str)


@given(instance=siddhi::SELECT_strategy)
def test_siddhi::select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=siddhi::DOUBLE_strategy)
@settings(max_examples=50)
def test_siddhi::double_instantiation(instance):
    assert isinstance(instance, siddhi::DOUBLE)

@given(instance=siddhi::DOUBLE_strategy)
def test_siddhi::double_double_type(instance):
    assert isinstance(instance.double, str)


@given(instance=siddhi::DOUBLE_strategy)
def test_siddhi::double_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=siddhi::LONG_strategy)
@settings(max_examples=50)
def test_siddhi::long_instantiation(instance):
    assert isinstance(instance, siddhi::LONG)

@given(instance=siddhi::LONG_strategy)
def test_siddhi::long_long_type(instance):
    assert isinstance(instance.long, str)


@given(instance=siddhi::LONG_strategy)
def test_siddhi::long_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=siddhi::INTS_strategy)
@settings(max_examples=50)
def test_siddhi::ints_instantiation(instance):
    assert isinstance(instance, siddhi::INTS)

@given(instance=siddhi::INTS_strategy)
def test_siddhi::ints_int_type(instance):
    assert isinstance(instance.int, str)


@given(instance=siddhi::INTS_strategy)
def test_siddhi::ints_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=siddhi::STRINGS_strategy)
@settings(max_examples=50)
def test_siddhi::strings_instantiation(instance):
    assert isinstance(instance, siddhi::STRINGS)

@given(instance=siddhi::STRINGS_strategy)
def test_siddhi::strings_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=siddhi::STRINGS_strategy)
def test_siddhi::strings_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=siddhi::OUTPUT_strategy)
@settings(max_examples=50)
def test_siddhi::output_instantiation(instance):
    assert isinstance(instance, siddhi::OUTPUT)

@given(instance=siddhi::OUTPUT_strategy)
def test_siddhi::output_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=siddhi::OUTPUT_strategy)
def test_siddhi::output_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=siddhi::WINDOW_strategy)
@settings(max_examples=50)
def test_siddhi::window_instantiation(instance):
    assert isinstance(instance, siddhi::WINDOW)

@given(instance=siddhi::WINDOW_strategy)
def test_siddhi::window_window_type(instance):
    assert isinstance(instance.window, str)


@given(instance=siddhi::WINDOW_strategy)
def test_siddhi::window_window_setter(instance):
    original = instance.window
    instance.window = original
    assert instance.window == original

@given(instance=siddhi::TABLE_strategy)
@settings(max_examples=50)
def test_siddhi::table_instantiation(instance):
    assert isinstance(instance, siddhi::TABLE)

@given(instance=siddhi::TABLE_strategy)
def test_siddhi::table_table_type(instance):
    assert isinstance(instance.table, str)


@given(instance=siddhi::TABLE_strategy)
def test_siddhi::table_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=siddhi::FROM_strategy)
@settings(max_examples=50)
def test_siddhi::from_instantiation(instance):
    assert isinstance(instance, siddhi::FROM)

@given(instance=siddhi::FROM_strategy)
def test_siddhi::from_from__type(instance):
    assert isinstance(instance.from_, str)


@given(instance=siddhi::FROM_strategy)
def test_siddhi::from_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=siddhi::RETURN_strategy)
@settings(max_examples=50)
def test_siddhi::return_instantiation(instance):
    assert isinstance(instance, siddhi::RETURN)

@given(instance=siddhi::RETURN_strategy)
def test_siddhi::return_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=siddhi::RETURN_strategy)
def test_siddhi::return_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=siddhi::FUNCTION_strategy)
@settings(max_examples=50)
def test_siddhi::function_instantiation(instance):
    assert isinstance(instance, siddhi::FUNCTION)

@given(instance=siddhi::FUNCTION_strategy)
def test_siddhi::function_function_type(instance):
    assert isinstance(instance.function, str)


@given(instance=siddhi::FUNCTION_strategy)
def test_siddhi::function_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=siddhi::AT_strategy)
@settings(max_examples=50)
def test_siddhi::at_instantiation(instance):
    assert isinstance(instance, siddhi::AT)

@given(instance=siddhi::AT_strategy)
def test_siddhi::at_at_type(instance):
    assert isinstance(instance.at, str)


@given(instance=siddhi::AT_strategy)
def test_siddhi::at_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=siddhi::TRIGGER_strategy)
@settings(max_examples=50)
def test_siddhi::trigger_instantiation(instance):
    assert isinstance(instance, siddhi::TRIGGER)

@given(instance=siddhi::TRIGGER_strategy)
def test_siddhi::trigger_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=siddhi::TRIGGER_strategy)
def test_siddhi::trigger_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=siddhi::NULL_strategy)
@settings(max_examples=50)
def test_siddhi::null_instantiation(instance):
    assert isinstance(instance, siddhi::NULL)

@given(instance=siddhi::NULL_strategy)
def test_siddhi::null_null_type(instance):
    assert isinstance(instance.null, str)


@given(instance=siddhi::NULL_strategy)
def test_siddhi::null_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=siddhi::IS_strategy)
@settings(max_examples=50)
def test_siddhi::is_instantiation(instance):
    assert isinstance(instance, siddhi::IS)

@given(instance=siddhi::IS_strategy)
def test_siddhi::is_is__type(instance):
    assert isinstance(instance.is_, str)


@given(instance=siddhi::IS_strategy)
def test_siddhi::is_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original

@given(instance=siddhi::LAST_strategy)
@settings(max_examples=50)
def test_siddhi::last_instantiation(instance):
    assert isinstance(instance, siddhi::LAST)

@given(instance=siddhi::LAST_strategy)
def test_siddhi::last_last_type(instance):
    assert isinstance(instance.last, str)


@given(instance=siddhi::LAST_strategy)
def test_siddhi::last_last_setter(instance):
    original = instance.last
    instance.last = original
    assert instance.last == original

@given(instance=siddhi::CURRENT_strategy)
@settings(max_examples=50)
def test_siddhi::current_instantiation(instance):
    assert isinstance(instance, siddhi::CURRENT)

@given(instance=siddhi::CURRENT_strategy)
def test_siddhi::current_currt_type(instance):
    assert isinstance(instance.currt, str)


@given(instance=siddhi::CURRENT_strategy)
def test_siddhi::current_currt_setter(instance):
    original = instance.currt
    instance.currt = original
    assert instance.currt == original

@given(instance=siddhi::EXPIRED_strategy)
@settings(max_examples=50)
def test_siddhi::expired_instantiation(instance):
    assert isinstance(instance, siddhi::EXPIRED)

@given(instance=siddhi::EXPIRED_strategy)
def test_siddhi::expired_expired_type(instance):
    assert isinstance(instance.expired, str)


@given(instance=siddhi::EXPIRED_strategy)
def test_siddhi::expired_expired_setter(instance):
    original = instance.expired
    instance.expired = original
    assert instance.expired == original

@given(instance=siddhi::RAW_strategy)
@settings(max_examples=50)
def test_siddhi::raw_instantiation(instance):
    assert isinstance(instance, siddhi::RAW)

@given(instance=siddhi::RAW_strategy)
def test_siddhi::raw_raw_type(instance):
    assert isinstance(instance.raw, str)


@given(instance=siddhi::RAW_strategy)
def test_siddhi::raw_raw_setter(instance):
    original = instance.raw
    instance.raw = original
    assert instance.raw == original

@given(instance=siddhi::EVENTS_strategy)
@settings(max_examples=50)
def test_siddhi::events_instantiation(instance):
    assert isinstance(instance, siddhi::EVENTS)

@given(instance=siddhi::EVENTS_strategy)
def test_siddhi::events_events_type(instance):
    assert isinstance(instance.events, str)


@given(instance=siddhi::EVENTS_strategy)
def test_siddhi::events_events_setter(instance):
    original = instance.events
    instance.events = original
    assert instance.events == original

@given(instance=siddhi::ALL_strategy)
@settings(max_examples=50)
def test_siddhi::all_instantiation(instance):
    assert isinstance(instance, siddhi::ALL)

@given(instance=siddhi::ALL_strategy)
def test_siddhi::all_all_type(instance):
    assert isinstance(instance.all, str)


@given(instance=siddhi::ALL_strategy)
def test_siddhi::all_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=siddhi::OBJECT_strategy)
@settings(max_examples=50)
def test_siddhi::object_instantiation(instance):
    assert isinstance(instance, siddhi::OBJECT)

@given(instance=siddhi::OBJECT_strategy)
def test_siddhi::object_object_type(instance):
    assert isinstance(instance.object, str)


@given(instance=siddhi::OBJECT_strategy)
def test_siddhi::object_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=siddhi::BOOL_strategy)
@settings(max_examples=50)
def test_siddhi::bool_instantiation(instance):
    assert isinstance(instance, siddhi::BOOL)

@given(instance=siddhi::BOOL_strategy)
def test_siddhi::bool_bool_type(instance):
    assert isinstance(instance.bool, str)


@given(instance=siddhi::BOOL_strategy)
def test_siddhi::bool_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=siddhi::FLOAT_strategy)
@settings(max_examples=50)
def test_siddhi::float_instantiation(instance):
    assert isinstance(instance, siddhi::FLOAT)

@given(instance=siddhi::FLOAT_strategy)
def test_siddhi::float_float_type(instance):
    assert isinstance(instance.float, str)


@given(instance=siddhi::FLOAT_strategy)
def test_siddhi::float_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=EveryAbsentSequenceSourceChain_strategy)
@settings(max_examples=50)
def test_everyabsentsequencesourcechain_instantiation(instance):
    assert isinstance(instance, EveryAbsentSequenceSourceChain)

@given(instance=EverySequenceSourceChain_strategy)
@settings(max_examples=50)
def test_everysequencesourcechain_instantiation(instance):
    assert isinstance(instance, EverySequenceSourceChain)

@given(instance=BasicAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_basicabsentpatternsource_instantiation(instance):
    assert isinstance(instance, BasicAbsentPatternSource)

@given(instance=siddhi::DEFINE_strategy)
@settings(max_examples=50)
def test_siddhi::define_instantiation(instance):
    assert isinstance(instance, siddhi::DEFINE)

@given(instance=siddhi::DEFINE_strategy)
def test_siddhi::define_define_type(instance):
    assert isinstance(instance.define, str)


@given(instance=siddhi::DEFINE_strategy)
def test_siddhi::define_define_setter(instance):
    original = instance.define
    instance.define = original
    assert instance.define == original

@given(instance=siddhi::STREAM_strategy)
@settings(max_examples=50)
def test_siddhi::stream_instantiation(instance):
    assert isinstance(instance, siddhi::STREAM)

@given(instance=siddhi::STREAM_strategy)
def test_siddhi::stream_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=siddhi::STREAM_strategy)
def test_siddhi::stream_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=AppAnnotation_strategy)
@settings(max_examples=50)
def test_appannotation_instantiation(instance):
    assert isinstance(instance, AppAnnotation)

@given(instance=siddhi::APP_strategy)
@settings(max_examples=50)
def test_siddhi::app_instantiation(instance):
    assert isinstance(instance, siddhi::APP)

@given(instance=siddhi::APP_strategy)
def test_siddhi::app_ap_type(instance):
    assert isinstance(instance.ap, str)


@given(instance=siddhi::APP_strategy)
def test_siddhi::app_ap_setter(instance):
    original = instance.ap
    instance.ap = original
    assert instance.ap == original

@given(instance=siddhi::IN_strategy)
@settings(max_examples=50)
def test_siddhi::in_instantiation(instance):
    assert isinstance(instance, siddhi::IN)

@given(instance=siddhi::IN_strategy)
def test_siddhi::in_in__type(instance):
    assert isinstance(instance.in_, str)


@given(instance=siddhi::IN_strategy)
def test_siddhi::in_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=RightAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_rightabsentpatternsource_instantiation(instance):
    assert isinstance(instance, RightAbsentPatternSource)

@given(instance=LeftAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_leftabsentpatternsource_instantiation(instance):
    assert isinstance(instance, LeftAbsentPatternSource)

@given(instance=EveryAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_everyabsentpatternsource_instantiation(instance):
    assert isinstance(instance, EveryAbsentPatternSource)

@given(instance=LogicalAbsentStatefulSource_strategy)
@settings(max_examples=50)
def test_logicalabsentstatefulsource_instantiation(instance):
    assert isinstance(instance, LogicalAbsentStatefulSource)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=siddhi::L_strategy)
@settings(max_examples=50)
def test_siddhi::l_instantiation(instance):
    assert isinstance(instance, siddhi::L)

@given(instance=siddhi::L_strategy)
def test_siddhi::l_l_type(instance):
    assert isinstance(instance.l, str)


@given(instance=siddhi::L_strategy)
def test_siddhi::l_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=SignedLongValue_strategy)
@settings(max_examples=50)
def test_signedlongvalue_instantiation(instance):
    assert isinstance(instance, SignedLongValue)

@given(instance=siddhi::LONG::LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi::long::literal_instantiation(instance):
    assert isinstance(instance, siddhi::LONG::LITERAL)

@given(instance=siddhi::F_strategy)
@settings(max_examples=50)
def test_siddhi::f_instantiation(instance):
    assert isinstance(instance, siddhi::F)

@given(instance=siddhi::F_strategy)
def test_siddhi::f_f_type(instance):
    assert isinstance(instance.f, str)


@given(instance=siddhi::F_strategy)
def test_siddhi::f_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=SignedFloatValue_strategy)
@settings(max_examples=50)
def test_signedfloatvalue_instantiation(instance):
    assert isinstance(instance, SignedFloatValue)

@given(instance=siddhi::FLOAT::LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi::float::literal_instantiation(instance):
    assert isinstance(instance, siddhi::FLOAT::LITERAL)

@given(instance=siddhi::D_strategy)
@settings(max_examples=50)
def test_siddhi::d_instantiation(instance):
    assert isinstance(instance, siddhi::D)

@given(instance=siddhi::D_strategy)
def test_siddhi::d_d_type(instance):
    assert isinstance(instance.d, str)


@given(instance=siddhi::D_strategy)
def test_siddhi::d_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=siddhi::E_strategy)
@settings(max_examples=50)
def test_siddhi::e_instantiation(instance):
    assert isinstance(instance, siddhi::E)

@given(instance=siddhi::E_strategy)
def test_siddhi::e_e_type(instance):
    assert isinstance(instance.e, str)


@given(instance=siddhi::E_strategy)
def test_siddhi::e_e_setter(instance):
    original = instance.e
    instance.e = original
    assert instance.e == original

@given(instance=SignedDoubleValue_strategy)
@settings(max_examples=50)
def test_signeddoublevalue_instantiation(instance):
    assert isinstance(instance, SignedDoubleValue)

@given(instance=siddhi::DOUBLE::LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi::double::literal_instantiation(instance):
    assert isinstance(instance, siddhi::DOUBLE::LITERAL)

@given(instance=MILLISECONDS_strategy)
@settings(max_examples=50)
def test_milliseconds_instantiation(instance):
    assert isinstance(instance, MILLISECONDS)

@given(instance=siddhi::MillisecondValue_strategy)
@settings(max_examples=50)
def test_siddhi::millisecondvalue_instantiation(instance):
    assert isinstance(instance, siddhi::MillisecondValue)

@given(instance=siddhi::FunctionId_strategy)
@settings(max_examples=50)
def test_siddhi::functionid_instantiation(instance):
    assert isinstance(instance, siddhi::FunctionId)

@given(instance=siddhi::FunctionNamespace_strategy)
@settings(max_examples=50)
def test_siddhi::functionnamespace_instantiation(instance):
    assert isinstance(instance, siddhi::FunctionNamespace)

@given(instance=siddhi::SignedLongValue_strategy)
@settings(max_examples=50)
def test_siddhi::signedlongvalue_instantiation(instance):
    assert isinstance(instance, siddhi::SignedLongValue)

@given(instance=FALSE_strategy)
@settings(max_examples=50)
def test_false_instantiation(instance):
    assert isinstance(instance, FALSE)

@given(instance=TRUE_strategy)
@settings(max_examples=50)
def test_true_instantiation(instance):
    assert isinstance(instance, TRUE)

@given(instance=siddhi::AttributeList_strategy)
@settings(max_examples=50)
def test_siddhi::attributelist_instantiation(instance):
    assert isinstance(instance, siddhi::AttributeList)

@given(instance=siddhi::FeaturesOrOutAttr_strategy)
@settings(max_examples=50)
def test_siddhi::featuresoroutattr_instantiation(instance):
    assert isinstance(instance, siddhi::FeaturesOrOutAttr)

@given(instance=siddhi::FeaturesOrOutAttr_strategy)
def test_siddhi::featuresoroutattr_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=siddhi::FeaturesOrOutAttr_strategy)
def test_siddhi::featuresoroutattr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=siddhi::FeaturesOrOutAttrReference_strategy)
@settings(max_examples=50)
def test_siddhi::featuresoroutattrreference_instantiation(instance):
    assert isinstance(instance, siddhi::FeaturesOrOutAttrReference)

@given(instance=siddhi::SignedFloatValue_strategy)
@settings(max_examples=50)
def test_siddhi::signedfloatvalue_instantiation(instance):
    assert isinstance(instance, siddhi::SignedFloatValue)

@given(instance=siddhi::SignedDoubleValue_strategy)
@settings(max_examples=50)
def test_siddhi::signeddoublevalue_instantiation(instance):
    assert isinstance(instance, siddhi::SignedDoubleValue)

@given(instance=siddhi::BoolValue_strategy)
@settings(max_examples=50)
def test_siddhi::boolvalue_instantiation(instance):
    assert isinstance(instance, siddhi::BoolValue)

@given(instance=siddhi::AttributeNameReference_strategy)
@settings(max_examples=50)
def test_siddhi::attributenamereference_instantiation(instance):
    assert isinstance(instance, siddhi::AttributeNameReference)

@given(instance=siddhi::Source1OrStandardStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::source1orstandardstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::Source1OrStandardStatefulSource)

@given(instance=siddhi::Source1OrStandardStatefulSource_strategy)
def test_siddhi::source1orstandardstatefulsource_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=siddhi::Source1OrStandardStatefulSource_strategy)
def test_siddhi::source1orstandardstatefulsource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PatternCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_patterncollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, PatternCollectionStatefulSource)

@given(instance=SequenceCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_sequencecollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, SequenceCollectionStatefulSource)

@given(instance=siddhi::Literal_strategy)
@settings(max_examples=50)
def test_siddhi::literal_instantiation(instance):
    assert isinstance(instance, siddhi::Literal)

@given(instance=MathDivmulOperation_strategy)
@settings(max_examples=50)
def test_mathdivmuloperation_instantiation(instance):
    assert isinstance(instance, MathDivmulOperation)

@given(instance=siddhi::MathOtherOperations_strategy)
@settings(max_examples=50)
def test_siddhi::mathotheroperations_instantiation(instance):
    assert isinstance(instance, siddhi::MathOtherOperations)

@given(instance=MathAddsubOperation_strategy)
@settings(max_examples=50)
def test_mathaddsuboperation_instantiation(instance):
    assert isinstance(instance, MathAddsubOperation)

@given(instance=siddhi::MathDivmulOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathdivmuloperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathDivmulOperation)

@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_multiply_type(instance):
    assert isinstance(instance.multiply, str)


@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_multiply_setter(instance):
    original = instance.multiply
    instance.multiply = original
    assert instance.multiply == original

@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_devide_type(instance):
    assert isinstance(instance.devide, str)


@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_devide_setter(instance):
    original = instance.devide
    instance.devide = original
    assert instance.devide == original

@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_mod_type(instance):
    assert isinstance(instance.mod, str)


@given(instance=siddhi::MathDivmulOperation_strategy)
def test_siddhi::mathdivmuloperation_mod_setter(instance):
    original = instance.mod
    instance.mod = original
    assert instance.mod == original

@given(instance=siddhi::SourceOrEventReference_strategy)
@settings(max_examples=50)
def test_siddhi::sourceoreventreference_instantiation(instance):
    assert isinstance(instance, siddhi::SourceOrEventReference)

@given(instance=SetAssignment_strategy)
@settings(max_examples=50)
def test_setassignment_instantiation(instance):
    assert isinstance(instance, SetAssignment)

@given(instance=siddhi::ConstantValue_strategy)
@settings(max_examples=50)
def test_siddhi::constantvalue_instantiation(instance):
    assert isinstance(instance, siddhi::ConstantValue)

@given(instance=siddhi::ConstantValue_strategy)
def test_siddhi::constantvalue_siv_type(instance):
    assert isinstance(instance.siv, str)


@given(instance=siddhi::ConstantValue_strategy)
def test_siddhi::constantvalue_siv_setter(instance):
    original = instance.siv
    instance.siv = original
    assert instance.siv == original

@given(instance=siddhi::StreamReference_strategy)
@settings(max_examples=50)
def test_siddhi::streamreference_instantiation(instance):
    assert isinstance(instance, siddhi::StreamReference)

@given(instance=siddhi::StreamReference_strategy)
def test_siddhi::streamreference_hash_type(instance):
    assert isinstance(instance.hash, str)


@given(instance=siddhi::StreamReference_strategy)
def test_siddhi::streamreference_hash_setter(instance):
    original = instance.hash
    instance.hash = original
    assert instance.hash == original

@given(instance=NULL_strategy)
@settings(max_examples=50)
def test_null_instantiation(instance):
    assert isinstance(instance, NULL)

@given(instance=IS_strategy)
@settings(max_examples=50)
def test_is_instantiation(instance):
    assert isinstance(instance, IS)

@given(instance=MathOtherOperations_strategy)
@settings(max_examples=50)
def test_mathotheroperations_instantiation(instance):
    assert isinstance(instance, MathOtherOperations)

@given(instance=siddhi::NullCheck_strategy)
@settings(max_examples=50)
def test_siddhi::nullcheck_instantiation(instance):
    assert isinstance(instance, siddhi::NullCheck)

@given(instance=siddhi::BasicSourceStreamHandlers_strategy)
@settings(max_examples=50)
def test_siddhi::basicsourcestreamhandlers_instantiation(instance):
    assert isinstance(instance, siddhi::BasicSourceStreamHandlers)

@given(instance=MathOperation_strategy)
@settings(max_examples=50)
def test_mathoperation_instantiation(instance):
    assert isinstance(instance, MathOperation)

@given(instance=siddhi::MathAddsubOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathaddsuboperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathAddsubOperation)

@given(instance=siddhi::MathAddsubOperation_strategy)
def test_siddhi::mathaddsuboperation_substract_type(instance):
    assert isinstance(instance.substract, str)


@given(instance=siddhi::MathAddsubOperation_strategy)
def test_siddhi::mathaddsuboperation_substract_setter(instance):
    original = instance.substract
    instance.substract = original
    assert instance.substract == original

@given(instance=siddhi::MathAddsubOperation_strategy)
def test_siddhi::mathaddsuboperation_add_type(instance):
    assert isinstance(instance.add, str)


@given(instance=siddhi::MathAddsubOperation_strategy)
def test_siddhi::mathaddsuboperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=siddhi::MathOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathoperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathOperation)

@given(instance=siddhi::StreamFunction_strategy)
@settings(max_examples=50)
def test_siddhi::streamfunction_instantiation(instance):
    assert isinstance(instance, siddhi::StreamFunction)

@given(instance=siddhi::Filter_strategy)
@settings(max_examples=50)
def test_siddhi::filter_instantiation(instance):
    assert isinstance(instance, siddhi::Filter)

@given(instance=siddhi::BasicSourceStreamHandler_strategy)
@settings(max_examples=50)
def test_siddhi::basicsourcestreamhandler_instantiation(instance):
    assert isinstance(instance, siddhi::BasicSourceStreamHandler)

@given(instance=siddhi::UNIDIRECTIONAL_strategy)
@settings(max_examples=50)
def test_siddhi::unidirectional_instantiation(instance):
    assert isinstance(instance, siddhi::UNIDIRECTIONAL)

@given(instance=siddhi::UNIDIRECTIONAL_strategy)
def test_siddhi::unidirectional_unidirectional_type(instance):
    assert isinstance(instance.unidirectional, str)


@given(instance=siddhi::UNIDIRECTIONAL_strategy)
def test_siddhi::unidirectional_unidirectional_setter(instance):
    original = instance.unidirectional
    instance.unidirectional = original
    assert instance.unidirectional == original

@given(instance=siddhi::JoinSource_strategy)
@settings(max_examples=50)
def test_siddhi::joinsource_instantiation(instance):
    assert isinstance(instance, siddhi::JoinSource)

@given(instance=StandardStream_strategy)
@settings(max_examples=50)
def test_standardstream_instantiation(instance):
    assert isinstance(instance, StandardStream)

@given(instance=JoinSource_strategy)
@settings(max_examples=50)
def test_joinsource_instantiation(instance):
    assert isinstance(instance, JoinSource)

@given(instance=siddhi::MainSource_strategy)
@settings(max_examples=50)
def test_siddhi::mainsource_instantiation(instance):
    assert isinstance(instance, siddhi::MainSource)

@given(instance=JoinStream_strategy)
@settings(max_examples=50)
def test_joinstream_instantiation(instance):
    assert isinstance(instance, JoinStream)

@given(instance=INNER_strategy)
@settings(max_examples=50)
def test_inner_instantiation(instance):
    assert isinstance(instance, INNER)

@given(instance=FULL_strategy)
@settings(max_examples=50)
def test_full_instantiation(instance):
    assert isinstance(instance, FULL)

@given(instance=RIGHT_strategy)
@settings(max_examples=50)
def test_right_instantiation(instance):
    assert isinstance(instance, RIGHT)

@given(instance=JOIN_strategy)
@settings(max_examples=50)
def test_join_instantiation(instance):
    assert isinstance(instance, JOIN)

@given(instance=OUTER_strategy)
@settings(max_examples=50)
def test_outer_instantiation(instance):
    assert isinstance(instance, OUTER)

@given(instance=LEFT_strategy)
@settings(max_examples=50)
def test_left_instantiation(instance):
    assert isinstance(instance, LEFT)

@given(instance=PER_strategy)
@settings(max_examples=50)
def test_per_instantiation(instance):
    assert isinstance(instance, PER)

@given(instance=WITHIN_strategy)
@settings(max_examples=50)
def test_within_instantiation(instance):
    assert isinstance(instance, WITHIN)

@given(instance=siddhi::joins_strategy)
@settings(max_examples=50)
def test_siddhi::joins_instantiation(instance):
    assert isinstance(instance, siddhi::joins)

@given(instance=siddhi::Per1_strategy)
@settings(max_examples=50)
def test_siddhi::per1_instantiation(instance):
    assert isinstance(instance, siddhi::Per1)

@given(instance=siddhi::WithinTimeRange_strategy)
@settings(max_examples=50)
def test_siddhi::withintimerange_instantiation(instance):
    assert isinstance(instance, siddhi::WithinTimeRange)

@given(instance=AbsentPatternSourceChain_strategy)
@settings(max_examples=50)
def test_absentpatternsourcechain_instantiation(instance):
    assert isinstance(instance, AbsentPatternSourceChain)

@given(instance=siddhi::EveryAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi::everyabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi::EveryAbsentPatternSource)

@given(instance=siddhi::RightAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi::rightabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi::RightAbsentPatternSource)

@given(instance=siddhi::RightAbsentPatternSource_strategy)
def test_siddhi::rightabsentpatternsource_fb2_type(instance):
    assert isinstance(instance.fb2, str)


@given(instance=siddhi::RightAbsentPatternSource_strategy)
def test_siddhi::rightabsentpatternsource_fb2_setter(instance):
    original = instance.fb2
    instance.fb2 = original
    assert instance.fb2 == original

@given(instance=siddhi::LeftAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi::leftabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi::LeftAbsentPatternSource)

@given(instance=siddhi::LeftAbsentPatternSource_strategy)
def test_siddhi::leftabsentpatternsource_fb1_type(instance):
    assert isinstance(instance.fb1, str)


@given(instance=siddhi::LeftAbsentPatternSource_strategy)
def test_siddhi::leftabsentpatternsource_fb1_setter(instance):
    original = instance.fb1
    instance.fb1 = original
    assert instance.fb1 == original

@given(instance=siddhi::PatternCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::patterncollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::PatternCollectionStatefulSource)

@given(instance=siddhi::PatternSource_strategy)
@settings(max_examples=50)
def test_siddhi::patternsource_instantiation(instance):
    assert isinstance(instance, siddhi::PatternSource)

@given(instance=siddhi::BasicSource_strategy)
@settings(max_examples=50)
def test_siddhi::basicsource_instantiation(instance):
    assert isinstance(instance, siddhi::BasicSource)

@given(instance=siddhi::NOT_strategy)
@settings(max_examples=50)
def test_siddhi::not_instantiation(instance):
    assert isinstance(instance, siddhi::NOT)

@given(instance=siddhi::NOT_strategy)
def test_siddhi::not_not1_type(instance):
    assert isinstance(instance.not1, str)


@given(instance=siddhi::NOT_strategy)
def test_siddhi::not_not1_setter(instance):
    original = instance.not1
    instance.not1 = original
    assert instance.not1 == original

@given(instance=siddhi::Collect_strategy)
@settings(max_examples=50)
def test_siddhi::collect_instantiation(instance):
    assert isinstance(instance, siddhi::Collect)

@given(instance=siddhi::Collect_strategy)
def test_siddhi::collect_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=siddhi::Collect_strategy)
def test_siddhi::collect_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=siddhi::Collect_strategy)
def test_siddhi::collect_end_type(instance):
    assert isinstance(instance.end, str)


@given(instance=siddhi::Collect_strategy)
def test_siddhi::collect_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=siddhi::AND_strategy)
@settings(max_examples=50)
def test_siddhi::and_instantiation(instance):
    assert isinstance(instance, siddhi::AND)

@given(instance=siddhi::AND_strategy)
def test_siddhi::and_and__type(instance):
    assert isinstance(instance.and_, str)


@given(instance=siddhi::AND_strategy)
def test_siddhi::and_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=SequenceSource_strategy)
@settings(max_examples=50)
def test_sequencesource_instantiation(instance):
    assert isinstance(instance, SequenceSource)

@given(instance=siddhi::LogicalAbsentStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::logicalabsentstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::LogicalAbsentStatefulSource)

@given(instance=siddhi::LogicalStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::logicalstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::LogicalStatefulSource)

@given(instance=siddhi::SequenceCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::sequencecollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::SequenceCollectionStatefulSource)

@given(instance=SequenceSourceChain_strategy)
@settings(max_examples=50)
def test_sequencesourcechain_instantiation(instance):
    assert isinstance(instance, SequenceSourceChain)

@given(instance=siddhi::PatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::patternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::PatternSourceChain)

@given(instance=siddhi::PatternSourceChain_strategy)
def test_siddhi::patternsourcechain_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=siddhi::PatternSourceChain_strategy)
def test_siddhi::patternsourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=PatternStream_strategy)
@settings(max_examples=50)
def test_patternstream_instantiation(instance):
    assert isinstance(instance, PatternStream)

@given(instance=siddhi::AbsentPatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::absentpatternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::AbsentPatternSourceChain)

@given(instance=siddhi::EveryPatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::everypatternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::EveryPatternSourceChain)

@given(instance=siddhi::EveryPatternSourceChain_strategy)
def test_siddhi::everypatternsourcechain_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=siddhi::EveryPatternSourceChain_strategy)
def test_siddhi::everypatternsourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi::RightAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi::rightabsentsequencesource_instantiation(instance):
    assert isinstance(instance, siddhi::RightAbsentSequenceSource)

@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_cp_type(instance):
    assert isinstance(instance.cp, str)


@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original

@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_comma_type(instance):
    assert isinstance(instance.comma, str)


@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original

@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_comm_type(instance):
    assert isinstance(instance.comm, str)


@given(instance=siddhi::RightAbsentSequenceSource_strategy)
def test_siddhi::rightabsentsequencesource_comm_setter(instance):
    original = instance.comm
    instance.comm = original
    assert instance.comm == original

@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi::leftabsentsequencesource_instantiation(instance):
    assert isinstance(instance, siddhi::LeftAbsentSequenceSource)

@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_cp_type(instance):
    assert isinstance(instance.cp, str)


@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original

@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_comma_type(instance):
    assert isinstance(instance.comma, str)


@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original

@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_comm_type(instance):
    assert isinstance(instance.comm, str)


@given(instance=siddhi::LeftAbsentSequenceSource_strategy)
def test_siddhi::leftabsentsequencesource_comm_setter(instance):
    original = instance.comm
    instance.comm = original
    assert instance.comm == original

@given(instance=siddhi::BasicAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi::basicabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi::BasicAbsentPatternSource)

@given(instance=siddhi::EObject_strategy)
@settings(max_examples=50)
def test_siddhi::eobject_instantiation(instance):
    assert isinstance(instance, siddhi::EObject)

@given(instance=HAVING_strategy)
@settings(max_examples=50)
def test_having_instantiation(instance):
    assert isinstance(instance, HAVING)

@given(instance=GROUP_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, GROUP)

@given(instance=siddhi::HavingExpr_strategy)
@settings(max_examples=50)
def test_siddhi::havingexpr_instantiation(instance):
    assert isinstance(instance, siddhi::HavingExpr)

@given(instance=siddhi::AbsentSequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::absentsequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::AbsentSequenceSourceChain)

@given(instance=siddhi::SequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::sequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::SequenceSourceChain)

@given(instance=siddhi::SequenceSourceChain_strategy)
def test_siddhi::sequencesourcechain_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=siddhi::SequenceSourceChain_strategy)
def test_siddhi::sequencesourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi::WithinTime_strategy)
@settings(max_examples=50)
def test_siddhi::withintime_instantiation(instance):
    assert isinstance(instance, siddhi::WithinTime)

@given(instance=siddhi::SequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi::sequencesource_instantiation(instance):
    assert isinstance(instance, siddhi::SequenceSource)

@given(instance=siddhi::EveryAbsentSequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::everyabsentsequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::EveryAbsentSequenceSourceChain)

@given(instance=siddhi::EverySequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi::everysequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi::EverySequenceSourceChain)

@given(instance=siddhi::PatternStream_strategy)
@settings(max_examples=50)
def test_siddhi::patternstream_instantiation(instance):
    assert isinstance(instance, siddhi::PatternStream)

@given(instance=siddhi::SequenceStream_strategy)
@settings(max_examples=50)
def test_siddhi::sequencestream_instantiation(instance):
    assert isinstance(instance, siddhi::SequenceStream)

@given(instance=siddhi::JoinStream_strategy)
@settings(max_examples=50)
def test_siddhi::joinstream_instantiation(instance):
    assert isinstance(instance, siddhi::JoinStream)

@given(instance=siddhi::Attribute_strategy)
@settings(max_examples=50)
def test_siddhi::attribute_instantiation(instance):
    assert isinstance(instance, siddhi::Attribute)

@given(instance=siddhi::OutputAttribute_strategy)
@settings(max_examples=50)
def test_siddhi::outputattribute_instantiation(instance):
    assert isinstance(instance, siddhi::OutputAttribute)

@given(instance=SELECT_strategy)
@settings(max_examples=50)
def test_select_instantiation(instance):
    assert isinstance(instance, SELECT)

@given(instance=FIRST_strategy)
@settings(max_examples=50)
def test_first_instantiation(instance):
    assert isinstance(instance, FIRST)

@given(instance=LAST_strategy)
@settings(max_examples=50)
def test_last_instantiation(instance):
    assert isinstance(instance, LAST)

@given(instance=siddhi::AttributeIndex_strategy)
@settings(max_examples=50)
def test_siddhi::attributeindex_instantiation(instance):
    assert isinstance(instance, siddhi::AttributeIndex)

@given(instance=siddhi::MathGtLtOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathgtltoperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathGtLtOperation)

@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_lt_type(instance):
    assert isinstance(instance.lt, str)


@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_lt_setter(instance):
    original = instance.lt
    instance.lt = original
    assert instance.lt == original

@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_gt_eq_type(instance):
    assert isinstance(instance.gt_eq, str)


@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_gt_eq_setter(instance):
    original = instance.gt_eq
    instance.gt_eq = original
    assert instance.gt_eq == original

@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_gt_type(instance):
    assert isinstance(instance.gt, str)


@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_gt_setter(instance):
    original = instance.gt
    instance.gt = original
    assert instance.gt == original

@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_lt_eq_type(instance):
    assert isinstance(instance.lt_eq, str)


@given(instance=siddhi::MathGtLtOperation_strategy)
def test_siddhi::mathgtltoperation_lt_eq_setter(instance):
    original = instance.lt_eq
    instance.lt_eq = original
    assert instance.lt_eq == original

@given(instance=siddhi::MathInOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathinoperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathInOperation)

@given(instance=siddhi::NotOperation_strategy)
@settings(max_examples=50)
def test_siddhi::notoperation_instantiation(instance):
    assert isinstance(instance, siddhi::NotOperation)

@given(instance=siddhi::MathEqualOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathequaloperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathEqualOperation)

@given(instance=siddhi::MathEqualOperation_strategy)
def test_siddhi::mathequaloperation_not_eq_type(instance):
    assert isinstance(instance.not_eq, str)


@given(instance=siddhi::MathEqualOperation_strategy)
def test_siddhi::mathequaloperation_not_eq_setter(instance):
    original = instance.not_eq
    instance.not_eq = original
    assert instance.not_eq == original

@given(instance=siddhi::MathEqualOperation_strategy)
def test_siddhi::mathequaloperation_eq_type(instance):
    assert isinstance(instance.eq, str)


@given(instance=siddhi::MathEqualOperation_strategy)
def test_siddhi::mathequaloperation_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=siddhi::MINUTES_strategy)
@settings(max_examples=50)
def test_siddhi::minutes_instantiation(instance):
    assert isinstance(instance, siddhi::MINUTES)

@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_minutes_type(instance):
    assert isinstance(instance.minutes, str)


@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original

@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_min_type(instance):
    assert isinstance(instance.min, str)


@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=siddhi::MINUTES_strategy)
def test_siddhi::minutes_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=siddhi::HOURS_strategy)
@settings(max_examples=50)
def test_siddhi::hours_instantiation(instance):
    assert isinstance(instance, siddhi::HOURS)

@given(instance=siddhi::HOURS_strategy)
def test_siddhi::hours_hours_type(instance):
    assert isinstance(instance.hours, str)


@given(instance=siddhi::HOURS_strategy)
def test_siddhi::hours_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original

@given(instance=siddhi::HOURS_strategy)
def test_siddhi::hours_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=siddhi::HOURS_strategy)
def test_siddhi::hours_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=siddhi::DAYS_strategy)
@settings(max_examples=50)
def test_siddhi::days_instantiation(instance):
    assert isinstance(instance, siddhi::DAYS)

@given(instance=siddhi::DAYS_strategy)
def test_siddhi::days_days_type(instance):
    assert isinstance(instance.days, str)


@given(instance=siddhi::DAYS_strategy)
def test_siddhi::days_days_setter(instance):
    original = instance.days
    instance.days = original
    assert instance.days == original

@given(instance=siddhi::DAYS_strategy)
def test_siddhi::days_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=siddhi::DAYS_strategy)
def test_siddhi::days_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=siddhi::WEEKS_strategy)
@settings(max_examples=50)
def test_siddhi::weeks_instantiation(instance):
    assert isinstance(instance, siddhi::WEEKS)

@given(instance=siddhi::WEEKS_strategy)
def test_siddhi::weeks_weeks_type(instance):
    assert isinstance(instance.weeks, str)


@given(instance=siddhi::WEEKS_strategy)
def test_siddhi::weeks_weeks_setter(instance):
    original = instance.weeks
    instance.weeks = original
    assert instance.weeks == original

@given(instance=siddhi::WEEKS_strategy)
def test_siddhi::weeks_week_type(instance):
    assert isinstance(instance.week, str)


@given(instance=siddhi::WEEKS_strategy)
def test_siddhi::weeks_week_setter(instance):
    original = instance.week
    instance.week = original
    assert instance.week == original

@given(instance=siddhi::MONTHS_strategy)
@settings(max_examples=50)
def test_siddhi::months_instantiation(instance):
    assert isinstance(instance, siddhi::MONTHS)

@given(instance=siddhi::MONTHS_strategy)
def test_siddhi::months_months_type(instance):
    assert isinstance(instance.months, str)


@given(instance=siddhi::MONTHS_strategy)
def test_siddhi::months_months_setter(instance):
    original = instance.months
    instance.months = original
    assert instance.months == original

@given(instance=siddhi::MONTHS_strategy)
def test_siddhi::months_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=siddhi::MONTHS_strategy)
def test_siddhi::months_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=siddhi::MathLogicalOperation_strategy)
@settings(max_examples=50)
def test_siddhi::mathlogicaloperation_instantiation(instance):
    assert isinstance(instance, siddhi::MathLogicalOperation)

@given(instance=siddhi::RightAbsentPatternSource1_strategy)
@settings(max_examples=50)
def test_siddhi::rightabsentpatternsource1_instantiation(instance):
    assert isinstance(instance, siddhi::RightAbsentPatternSource1)

@given(instance=siddhi::RightAbsentPatternSource1_strategy)
def test_siddhi::rightabsentpatternsource1_fb_type(instance):
    assert isinstance(instance.fb, str)


@given(instance=siddhi::RightAbsentPatternSource1_strategy)
def test_siddhi::rightabsentpatternsource1_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original

@given(instance=siddhi::LeftAbsentPatternSource1_strategy)
@settings(max_examples=50)
def test_siddhi::leftabsentpatternsource1_instantiation(instance):
    assert isinstance(instance, siddhi::LeftAbsentPatternSource1)

@given(instance=siddhi::LeftAbsentPatternSource1_strategy)
def test_siddhi::leftabsentpatternsource1_fb_type(instance):
    assert isinstance(instance.fb, str)


@given(instance=siddhi::LeftAbsentPatternSource1_strategy)
def test_siddhi::leftabsentpatternsource1_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original

@given(instance=RightAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_rightabsentsequencesource_instantiation(instance):
    assert isinstance(instance, RightAbsentSequenceSource)

@given(instance=siddhi::RightAbsentSequenceSource1_strategy)
@settings(max_examples=50)
def test_siddhi::rightabsentsequencesource1_instantiation(instance):
    assert isinstance(instance, siddhi::RightAbsentSequenceSource1)

@given(instance=LeftAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_leftabsentsequencesource_instantiation(instance):
    assert isinstance(instance, LeftAbsentSequenceSource)

@given(instance=siddhi::LeftAbsentSequenceSource1_strategy)
@settings(max_examples=50)
def test_siddhi::leftabsentsequencesource1_instantiation(instance):
    assert isinstance(instance, siddhi::LeftAbsentSequenceSource1)

@given(instance=siddhi::TRUE_strategy)
@settings(max_examples=50)
def test_siddhi::true_instantiation(instance):
    assert isinstance(instance, siddhi::TRUE)

@given(instance=siddhi::TRUE_strategy)
def test_siddhi::true_tr_type(instance):
    assert isinstance(instance.tr, str)


@given(instance=siddhi::TRUE_strategy)
def test_siddhi::true_tr_setter(instance):
    original = instance.tr
    instance.tr = original
    assert instance.tr == original

@given(instance=siddhi::FALSE_strategy)
@settings(max_examples=50)
def test_siddhi::false_instantiation(instance):
    assert isinstance(instance, siddhi::FALSE)

@given(instance=siddhi::FALSE_strategy)
def test_siddhi::false_fals_type(instance):
    assert isinstance(instance.fals, str)


@given(instance=siddhi::FALSE_strategy)
def test_siddhi::false_fals_setter(instance):
    original = instance.fals
    instance.fals = original
    assert instance.fals == original

@given(instance=SNAPSHOT_strategy)
@settings(max_examples=50)
def test_snapshot_instantiation(instance):
    assert isinstance(instance, SNAPSHOT)

@given(instance=CURRENT_strategy)
@settings(max_examples=50)
def test_current_instantiation(instance):
    assert isinstance(instance, CURRENT)

@given(instance=EXPIRED_strategy)
@settings(max_examples=50)
def test_expired_instantiation(instance):
    assert isinstance(instance, EXPIRED)

@given(instance=RAW_strategy)
@settings(max_examples=50)
def test_raw_instantiation(instance):
    assert isinstance(instance, RAW)

@given(instance=EVENTS_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, EVENTS)

@given(instance=ALL_strategy)
@settings(max_examples=50)
def test_all_instantiation(instance):
    assert isinstance(instance, ALL)

@given(instance=siddhi::OutputRateType_strategy)
@settings(max_examples=50)
def test_siddhi::outputratetype_instantiation(instance):
    assert isinstance(instance, siddhi::OutputRateType)

@given(instance=siddhi::SetAssignment_strategy)
@settings(max_examples=50)
def test_siddhi::setassignment_instantiation(instance):
    assert isinstance(instance, siddhi::SetAssignment)

@given(instance=SET_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, SET)

@given(instance=siddhi::SetClause_strategy)
@settings(max_examples=50)
def test_siddhi::setclause_instantiation(instance):
    assert isinstance(instance, siddhi::SetClause)

@given(instance=siddhi::OR_strategy)
@settings(max_examples=50)
def test_siddhi::or_instantiation(instance):
    assert isinstance(instance, siddhi::OR)

@given(instance=siddhi::OR_strategy)
def test_siddhi::or_or__type(instance):
    assert isinstance(instance.or_, str)


@given(instance=siddhi::OR_strategy)
def test_siddhi::or_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=siddhi::ConditionRange_strategy)
@settings(max_examples=50)
def test_siddhi::conditionrange_instantiation(instance):
    assert isinstance(instance, siddhi::ConditionRange)

@given(instance=siddhi::OF_strategy)
@settings(max_examples=50)
def test_siddhi::of_instantiation(instance):
    assert isinstance(instance, siddhi::OF)

@given(instance=siddhi::OF_strategy)
def test_siddhi::of_of_type(instance):
    assert isinstance(instance.of, str)


@given(instance=siddhi::OF_strategy)
def test_siddhi::of_of_setter(instance):
    original = instance.of
    instance.of = original
    assert instance.of == original

@given(instance=PartitionWithStream_strategy)
@settings(max_examples=50)
def test_partitionwithstream_instantiation(instance):
    assert isinstance(instance, PartitionWithStream)

@given(instance=siddhi::ConditionRanges_strategy)
@settings(max_examples=50)
def test_siddhi::conditionranges_instantiation(instance):
    assert isinstance(instance, siddhi::ConditionRanges)

@given(instance=siddhi::ON_strategy)
@settings(max_examples=50)
def test_siddhi::on_instantiation(instance):
    assert isinstance(instance, siddhi::ON)

@given(instance=siddhi::ON_strategy)
def test_siddhi::on_on_type(instance):
    assert isinstance(instance.on, str)


@given(instance=siddhi::ON_strategy)
def test_siddhi::on_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original

@given(instance=siddhi::Target_strategy)
@settings(max_examples=50)
def test_siddhi::target_instantiation(instance):
    assert isinstance(instance, siddhi::Target)

@given(instance=UPDATE_strategy)
@settings(max_examples=50)
def test_update_instantiation(instance):
    assert isinstance(instance, UPDATE)

@given(instance=FOR_strategy)
@settings(max_examples=50)
def test_for_instantiation(instance):
    assert isinstance(instance, FOR)

@given(instance=siddhi::ForTime_strategy)
@settings(max_examples=50)
def test_siddhi::fortime_instantiation(instance):
    assert isinstance(instance, siddhi::ForTime)

@given(instance=DELETE_strategy)
@settings(max_examples=50)
def test_delete_instantiation(instance):
    assert isinstance(instance, DELETE)

@given(instance=INTO_strategy)
@settings(max_examples=50)
def test_into_instantiation(instance):
    assert isinstance(instance, INTO)

@given(instance=INSERT_strategy)
@settings(max_examples=50)
def test_insert_instantiation(instance):
    assert isinstance(instance, INSERT)

@given(instance=siddhi::QuerySection_strategy)
@settings(max_examples=50)
def test_siddhi::querysection_instantiation(instance):
    assert isinstance(instance, siddhi::QuerySection)

@given(instance=siddhi::QueryInput_strategy)
@settings(max_examples=50)
def test_siddhi::queryinput_instantiation(instance):
    assert isinstance(instance, siddhi::QueryInput)

@given(instance=siddhi::AS_strategy)
@settings(max_examples=50)
def test_siddhi::as_instantiation(instance):
    assert isinstance(instance, siddhi::AS)

@given(instance=siddhi::AS_strategy)
def test_siddhi::as_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=siddhi::AS_strategy)
def test_siddhi::as_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=siddhi::Expression_strategy)
@settings(max_examples=50)
def test_siddhi::expression_instantiation(instance):
    assert isinstance(instance, siddhi::Expression)

@given(instance=siddhi::PropertyValue_strategy)
@settings(max_examples=50)
def test_siddhi::propertyvalue_instantiation(instance):
    assert isinstance(instance, siddhi::PropertyValue)

@given(instance=siddhi::PartitionWithStream_strategy)
@settings(max_examples=50)
def test_siddhi::partitionwithstream_instantiation(instance):
    assert isinstance(instance, siddhi::PartitionWithStream)

@given(instance=END_strategy)
@settings(max_examples=50)
def test_end_instantiation(instance):
    assert isinstance(instance, END)

@given(instance=BEGIN_strategy)
@settings(max_examples=50)
def test_begin_instantiation(instance):
    assert isinstance(instance, BEGIN)

@given(instance=WITH_strategy)
@settings(max_examples=50)
def test_with_instantiation(instance):
    assert isinstance(instance, WITH)

@given(instance=PARTITION_strategy)
@settings(max_examples=50)
def test_partition_instantiation(instance):
    assert isinstance(instance, PARTITION)

@given(instance=Source1OrStandardStatefulSource_strategy)
@settings(max_examples=50)
def test_source1orstandardstatefulsource_instantiation(instance):
    assert isinstance(instance, Source1OrStandardStatefulSource)

@given(instance=siddhi::StreamAlias_strategy)
@settings(max_examples=50)
def test_siddhi::streamalias_instantiation(instance):
    assert isinstance(instance, siddhi::StreamAlias)

@given(instance=siddhi::StandardStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi::standardstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi::StandardStatefulSource)

@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_one_or_more_type(instance):
    assert isinstance(instance.one_or_more, str)


@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_one_or_more_setter(instance):
    original = instance.one_or_more
    instance.one_or_more = original
    assert instance.one_or_more == original

@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_zero_or_more_type(instance):
    assert isinstance(instance.zero_or_more, str)


@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_zero_or_more_setter(instance):
    original = instance.zero_or_more
    instance.zero_or_more = original
    assert instance.zero_or_more == original

@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_zero_or_one_type(instance):
    assert isinstance(instance.zero_or_one, str)


@given(instance=siddhi::StandardStatefulSource_strategy)
def test_siddhi::standardstatefulsource_zero_or_one_setter(instance):
    original = instance.zero_or_one
    instance.zero_or_one = original
    assert instance.zero_or_one == original

@given(instance=siddhi::Source_strategy)
@settings(max_examples=50)
def test_siddhi::source_instantiation(instance):
    assert isinstance(instance, siddhi::Source)

@given(instance=OBJECT_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, OBJECT)

@given(instance=BOOL_strategy)
@settings(max_examples=50)
def test_bool_instantiation(instance):
    assert isinstance(instance, BOOL)

@given(instance=DOUBLE_strategy)
@settings(max_examples=50)
def test_double_instantiation(instance):
    assert isinstance(instance, DOUBLE)

@given(instance=FLOAT_strategy)
@settings(max_examples=50)
def test_float_instantiation(instance):
    assert isinstance(instance, FLOAT)

@given(instance=LONG_strategy)
@settings(max_examples=50)
def test_long_instantiation(instance):
    assert isinstance(instance, LONG)

@given(instance=INTS_strategy)
@settings(max_examples=50)
def test_ints_instantiation(instance):
    assert isinstance(instance, INTS)

@given(instance=STRINGS_strategy)
@settings(max_examples=50)
def test_strings_instantiation(instance):
    assert isinstance(instance, STRINGS)

@given(instance=FeaturesOrOutAttr_strategy)
@settings(max_examples=50)
def test_featuresoroutattr_instantiation(instance):
    assert isinstance(instance, FeaturesOrOutAttr)

@given(instance=siddhi::OutAttr_strategy)
@settings(max_examples=50)
def test_siddhi::outattr_instantiation(instance):
    assert isinstance(instance, siddhi::OutAttr)

@given(instance=siddhi::PropertySeparator_strategy)
@settings(max_examples=50)
def test_siddhi::propertyseparator_instantiation(instance):
    assert isinstance(instance, siddhi::PropertySeparator)

@given(instance=siddhi::AttributeReference_strategy)
@settings(max_examples=50)
def test_siddhi::attributereference_instantiation(instance):
    assert isinstance(instance, siddhi::AttributeReference)

@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_hash2_type(instance):
    assert isinstance(instance.hash2, str)


@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_hash2_setter(instance):
    original = instance.hash2
    instance.hash2 = original
    assert instance.hash2 == original

@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_hash1_type(instance):
    assert isinstance(instance.hash1, str)


@given(instance=siddhi::AttributeReference_strategy)
def test_siddhi::attributereference_hash1_setter(instance):
    original = instance.hash1
    instance.hash1 = original
    assert instance.hash1 == original

@given(instance=siddhi::GroupByQuerySelection_strategy)
@settings(max_examples=50)
def test_siddhi::groupbyqueryselection_instantiation(instance):
    assert isinstance(instance, siddhi::GroupByQuerySelection)

@given(instance=siddhi::StandardStream_strategy)
@settings(max_examples=50)
def test_siddhi::standardstream_instantiation(instance):
    assert isinstance(instance, siddhi::StandardStream)

@given(instance=BY_strategy)
@settings(max_examples=50)
def test_by_instantiation(instance):
    assert isinstance(instance, BY)

@given(instance=siddhi::GroupBy_strategy)
@settings(max_examples=50)
def test_siddhi::groupby_instantiation(instance):
    assert isinstance(instance, siddhi::GroupBy)

@given(instance=siddhi::PropertyName_strategy)
@settings(max_examples=50)
def test_siddhi::propertyname_instantiation(instance):
    assert isinstance(instance, siddhi::PropertyName)

@given(instance=siddhi::AnnotationElement_strategy)
@settings(max_examples=50)
def test_siddhi::annotationelement_instantiation(instance):
    assert isinstance(instance, siddhi::AnnotationElement)

@given(instance=siddhi::Name_strategy)
@settings(max_examples=50)
def test_siddhi::name_instantiation(instance):
    assert isinstance(instance, siddhi::Name)

@given(instance=siddhi::Name_strategy)
def test_siddhi::name_na_type(instance):
    assert isinstance(instance.na, str)


@given(instance=siddhi::Name_strategy)
def test_siddhi::name_na_setter(instance):
    original = instance.na
    instance.na = original
    assert instance.na == original

@given(instance=YEARS_strategy)
@settings(max_examples=50)
def test_years_instantiation(instance):
    assert isinstance(instance, YEARS)

@given(instance=siddhi::YearValue_strategy)
@settings(max_examples=50)
def test_siddhi::yearvalue_instantiation(instance):
    assert isinstance(instance, siddhi::YearValue)

@given(instance=MONTHS_strategy)
@settings(max_examples=50)
def test_months_instantiation(instance):
    assert isinstance(instance, MONTHS)

@given(instance=siddhi::MonthValue_strategy)
@settings(max_examples=50)
def test_siddhi::monthvalue_instantiation(instance):
    assert isinstance(instance, siddhi::MonthValue)

@given(instance=WEEKS_strategy)
@settings(max_examples=50)
def test_weeks_instantiation(instance):
    assert isinstance(instance, WEEKS)

@given(instance=siddhi::WeekValue_strategy)
@settings(max_examples=50)
def test_siddhi::weekvalue_instantiation(instance):
    assert isinstance(instance, siddhi::WeekValue)

@given(instance=DAYS_strategy)
@settings(max_examples=50)
def test_days_instantiation(instance):
    assert isinstance(instance, DAYS)

@given(instance=siddhi::DayValue_strategy)
@settings(max_examples=50)
def test_siddhi::dayvalue_instantiation(instance):
    assert isinstance(instance, siddhi::DayValue)

@given(instance=HOURS_strategy)
@settings(max_examples=50)
def test_hours_instantiation(instance):
    assert isinstance(instance, HOURS)

@given(instance=siddhi::HourValue_strategy)
@settings(max_examples=50)
def test_siddhi::hourvalue_instantiation(instance):
    assert isinstance(instance, siddhi::HourValue)

@given(instance=MINUTES_strategy)
@settings(max_examples=50)
def test_minutes_instantiation(instance):
    assert isinstance(instance, MINUTES)

@given(instance=siddhi::MinuteValue_strategy)
@settings(max_examples=50)
def test_siddhi::minutevalue_instantiation(instance):
    assert isinstance(instance, siddhi::MinuteValue)

@given(instance=SECONDS_strategy)
@settings(max_examples=50)
def test_seconds_instantiation(instance):
    assert isinstance(instance, SECONDS)

@given(instance=siddhi::SecondValue_strategy)
@settings(max_examples=50)
def test_siddhi::secondvalue_instantiation(instance):
    assert isinstance(instance, siddhi::SecondValue)

@given(instance=AggregationTime_strategy)
@settings(max_examples=50)
def test_aggregationtime_instantiation(instance):
    assert isinstance(instance, AggregationTime)

@given(instance=siddhi::AggregationTimeRange_strategy)
@settings(max_examples=50)
def test_siddhi::aggregationtimerange_instantiation(instance):
    assert isinstance(instance, siddhi::AggregationTimeRange)

@given(instance=siddhi::AggregationTimeInterval_strategy)
@settings(max_examples=50)
def test_siddhi::aggregationtimeinterval_instantiation(instance):
    assert isinstance(instance, siddhi::AggregationTimeInterval)

@given(instance=siddhi::AggregationTimeDuration_strategy)
@settings(max_examples=50)
def test_siddhi::aggregationtimeduration_instantiation(instance):
    assert isinstance(instance, siddhi::AggregationTimeDuration)

@given(instance=siddhi::AggregationTime_strategy)
@settings(max_examples=50)
def test_siddhi::aggregationtime_instantiation(instance):
    assert isinstance(instance, siddhi::AggregationTime)

@given(instance=OUTPUT_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, OUTPUT)

@given(instance=siddhi::OutputRate_strategy)
@settings(max_examples=50)
def test_siddhi::outputrate_instantiation(instance):
    assert isinstance(instance, siddhi::OutputRate)

@given(instance=WINDOW_strategy)
@settings(max_examples=50)
def test_window_instantiation(instance):
    assert isinstance(instance, WINDOW)

@given(instance=siddhi::Win_strategy)
@settings(max_examples=50)
def test_siddhi::win_instantiation(instance):
    assert isinstance(instance, siddhi::Win)

@given(instance=siddhi::BasicSourceStreamHandlers1_strategy)
@settings(max_examples=50)
def test_siddhi::basicsourcestreamhandlers1_instantiation(instance):
    assert isinstance(instance, siddhi::BasicSourceStreamHandlers1)

@given(instance=AGGREGATE_strategy)
@settings(max_examples=50)
def test_aggregate_instantiation(instance):
    assert isinstance(instance, AGGREGATE)

@given(instance=FROM_strategy)
@settings(max_examples=50)
def test_from_instantiation(instance):
    assert isinstance(instance, FROM)

@given(instance=AGGREGATION_strategy)
@settings(max_examples=50)
def test_aggregation_instantiation(instance):
    assert isinstance(instance, AGGREGATION)

@given(instance=siddhi::FunctionBody_strategy)
@settings(max_examples=50)
def test_siddhi::functionbody_instantiation(instance):
    assert isinstance(instance, siddhi::FunctionBody)

@given(instance=siddhi::FunctionBody_strategy)
def test_siddhi::functionbody_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=siddhi::FunctionBody_strategy)
def test_siddhi::functionbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=siddhi::AttributeType_strategy)
@settings(max_examples=50)
def test_siddhi::attributetype_instantiation(instance):
    assert isinstance(instance, siddhi::AttributeType)

@given(instance=siddhi::LanguageName_strategy)
@settings(max_examples=50)
def test_siddhi::languagename_instantiation(instance):
    assert isinstance(instance, siddhi::LanguageName)

@given(instance=siddhi::LanguageName_strategy)
def test_siddhi::languagename_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=siddhi::LanguageName_strategy)
def test_siddhi::languagename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=siddhi::FunctionName_strategy)
@settings(max_examples=50)
def test_siddhi::functionname_instantiation(instance):
    assert isinstance(instance, siddhi::FunctionName)

@given(instance=siddhi::FunctionName_strategy)
def test_siddhi::functionname_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=siddhi::FunctionName_strategy)
def test_siddhi::functionname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=RETURN_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, RETURN)

@given(instance=siddhi::QueryOutput_strategy)
@settings(max_examples=50)
def test_siddhi::queryoutput_instantiation(instance):
    assert isinstance(instance, siddhi::QueryOutput)

@given(instance=siddhi::AnonymousStream_strategy)
@settings(max_examples=50)
def test_siddhi::anonymousstream_instantiation(instance):
    assert isinstance(instance, siddhi::AnonymousStream)

@given(instance=FUNCTION_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, FUNCTION)

@given(instance=siddhi::StringValue_strategy)
@settings(max_examples=50)
def test_siddhi::stringvalue_instantiation(instance):
    assert isinstance(instance, siddhi::StringValue)

@given(instance=siddhi::StringValue_strategy)
def test_siddhi::stringvalue_sl_type(instance):
    assert isinstance(instance.sl, str)


@given(instance=siddhi::StringValue_strategy)
def test_siddhi::stringvalue_sl_setter(instance):
    original = instance.sl
    instance.sl = original
    assert instance.sl == original

@given(instance=siddhi::TimeValue_strategy)
@settings(max_examples=50)
def test_siddhi::timevalue_instantiation(instance):
    assert isinstance(instance, siddhi::TimeValue)

@given(instance=siddhi::EVERY_strategy)
@settings(max_examples=50)
def test_siddhi::every_instantiation(instance):
    assert isinstance(instance, siddhi::EVERY)

@given(instance=siddhi::EVERY_strategy)
def test_siddhi::every_every1_type(instance):
    assert isinstance(instance.every1, str)


@given(instance=siddhi::EVERY_strategy)
def test_siddhi::every_every1_setter(instance):
    original = instance.every1
    instance.every1 = original
    assert instance.every1 == original

@given(instance=siddhi::TriggerName_strategy)
@settings(max_examples=50)
def test_siddhi::triggername_instantiation(instance):
    assert isinstance(instance, siddhi::TriggerName)

@given(instance=siddhi::TriggerName_strategy)
def test_siddhi::triggername_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=siddhi::TriggerName_strategy)
def test_siddhi::triggername_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AT_strategy)
@settings(max_examples=50)
def test_at_instantiation(instance):
    assert isinstance(instance, AT)

@given(instance=TRIGGER_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, TRIGGER)

@given(instance=siddhi::OutputEventType_strategy)
@settings(max_examples=50)
def test_siddhi::outputeventtype_instantiation(instance):
    assert isinstance(instance, siddhi::OutputEventType)

@given(instance=siddhi::FunctionOperation_strategy)
@settings(max_examples=50)
def test_siddhi::functionoperation_instantiation(instance):
    assert isinstance(instance, siddhi::FunctionOperation)

@given(instance=siddhi::AppAnnotation_strategy)
@settings(max_examples=50)
def test_siddhi::appannotation_instantiation(instance):
    assert isinstance(instance, siddhi::AppAnnotation)

@given(instance=siddhi::ExecutionPlan_strategy)
@settings(max_examples=50)
def test_siddhi::executionplan_instantiation(instance):
    assert isinstance(instance, siddhi::ExecutionPlan)

@given(instance=TABLE_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, TABLE)

@given(instance=siddhi::Features_strategy)
@settings(max_examples=50)
def test_siddhi::features_instantiation(instance):
    assert isinstance(instance, siddhi::Features)

@given(instance=siddhi::Source1_strategy)
@settings(max_examples=50)
def test_siddhi::source1_instantiation(instance):
    assert isinstance(instance, siddhi::Source1)

@given(instance=siddhi::Source1_strategy)
def test_siddhi::source1_inner_type(instance):
    assert isinstance(instance.inner, str)


@given(instance=siddhi::Source1_strategy)
def test_siddhi::source1_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=siddhi::Annotation_strategy)
@settings(max_examples=50)
def test_siddhi::annotation_instantiation(instance):
    assert isinstance(instance, siddhi::Annotation)

@given(instance=STREAM_strategy)
@settings(max_examples=50)
def test_stream_instantiation(instance):
    assert isinstance(instance, STREAM)

@given(instance=DEFINE_strategy)
@settings(max_examples=50)
def test_define_instantiation(instance):
    assert isinstance(instance, DEFINE)

@given(instance=siddhi::Keyword_strategy)
@settings(max_examples=50)
def test_siddhi::keyword_instantiation(instance):
    assert isinstance(instance, siddhi::Keyword)

@given(instance=siddhi::DefinitionTable_strategy)
@settings(max_examples=50)
def test_siddhi::definitiontable_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionTable)

@given(instance=siddhi::DefinitionStream_strategy)
@settings(max_examples=50)
def test_siddhi::definitionstream_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionStream)

@given(instance=siddhi::Query_strategy)
@settings(max_examples=50)
def test_siddhi::query_instantiation(instance):
    assert isinstance(instance, siddhi::Query)

@given(instance=siddhi::ExecPartition_strategy)
@settings(max_examples=50)
def test_siddhi::execpartition_instantiation(instance):
    assert isinstance(instance, siddhi::ExecPartition)

@given(instance=siddhi::ExecutionElement_strategy)
@settings(max_examples=50)
def test_siddhi::executionelement_instantiation(instance):
    assert isinstance(instance, siddhi::ExecutionElement)

@given(instance=siddhi::DefinitionAggregation_strategy)
@settings(max_examples=50)
def test_siddhi::definitionaggregation_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionAggregation)

@given(instance=siddhi::DefinitionFunction_strategy)
@settings(max_examples=50)
def test_siddhi::definitionfunction_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionFunction)

@given(instance=siddhi::DefinitionTrigger_strategy)
@settings(max_examples=50)
def test_siddhi::definitiontrigger_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionTrigger)

@given(instance=siddhi::DefinitionWindow_strategy)
@settings(max_examples=50)
def test_siddhi::definitionwindow_instantiation(instance):
    assert isinstance(instance, siddhi::DefinitionWindow)

@given(instance=siddhi::SiddhiQL_strategy)
@settings(max_examples=50)
def test_siddhi::siddhiql_instantiation(instance):
    assert isinstance(instance, siddhi::SiddhiQL)
