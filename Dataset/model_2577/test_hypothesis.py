import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Name,
    siddhi_L,
    SignedLongValue,
    siddhi_LONG_LITERAL,
    siddhi_F,
    SignedFloatValue,
    siddhi_FLOAT_LITERAL,
    siddhi_D,
    siddhi_E,
    SignedDoubleValue,
    siddhi_DOUBLE_LITERAL,
    MILLISECONDS,
    siddhi_FunctionId,
    siddhi_FunctionNamespace,
    siddhi_SignedLongValue,
    FALSE,
    TRUE,
    siddhi_AttributeList,
    siddhi_FeaturesOrOutAttr,
    siddhi_FeaturesOrOutAttrReference,
    siddhi_SignedFloatValue,
    siddhi_SignedDoubleValue,
    siddhi_BoolValue,
    siddhi_AttributeNameReference,
    siddhi_Source1OrStandardStatefulSource,
    PatternCollectionStatefulSource,
    SequenceCollectionStatefulSource,
    siddhi_Literal,
    MathDivmulOperation,
    siddhi_MathOtherOperations,
    MathAddsubOperation,
    siddhi_MathDivmulOperation,
    siddhi_SourceOrEventReference,
    SetAssignment,
    siddhi_ConstantValue,
    siddhi_StreamReference,
    NULL,
    IS,
    MathOtherOperations,
    siddhi_NullCheck,
    siddhi_BasicSourceStreamHandlers,
    MathOperation,
    siddhi_MathAddsubOperation,
    Expression,
    siddhi_MathOperation,
    siddhi_StreamFunction,
    siddhi_Filter,
    siddhi_BasicSourceStreamHandler,
    siddhi_MathGtLtOperation,
    siddhi_MathInOperation,
    siddhi_NotOperation,
    siddhi_MathEqualOperation,
    siddhi_MINUTES,
    siddhi_HOURS,
    siddhi_DAYS,
    siddhi_WEEKS,
    siddhi_MONTHS,
    siddhi_MathLogicalOperation,
    RightAbsentSequenceSource,
    siddhi_RightAbsentSequenceSource1,
    LeftAbsentSequenceSource,
    siddhi_LeftAbsentSequenceSource1,
    siddhi_TRUE,
    siddhi_FALSE,
    siddhi_MILLISECONDS,
    siddhi_SECONDS,
    siddhi_OUTER,
    siddhi_INNER,
    siddhi_JOIN,
    siddhi_FULL,
    siddhi_RIGHT,
    siddhi_LEFT,
    siddhi_WITHIN,
    siddhi_YEARS,
    siddhi_PER,
    siddhi_SET,
    siddhi_AGGREGATE,
    siddhi_AGGREGATION,
    siddhi_WITH,
    siddhi_PARTITION,
    siddhi_END,
    siddhi_UPDATE,
    siddhi_FOR,
    siddhi_DELETE,
    siddhi_PLAN,
    siddhi_BEGIN,
    siddhi_INTO,
    siddhi_INSERT,
    siddhi_FIRST,
    siddhi_SNAPSHOT,
    siddhi_HAVING,
    siddhi_BY,
    siddhi_GROUP,
    siddhi_SELECT,
    siddhi_DOUBLE,
    siddhi_LONG,
    siddhi_INTS,
    siddhi_STRINGS,
    siddhi_OUTPUT,
    siddhi_WINDOW,
    siddhi_TABLE,
    siddhi_FROM,
    siddhi_RETURN,
    siddhi_FUNCTION,
    siddhi_AT,
    siddhi_TRIGGER,
    siddhi_NULL,
    siddhi_IS,
    siddhi_LAST,
    siddhi_CURRENT,
    siddhi_EXPIRED,
    siddhi_RAW,
    siddhi_EVENTS,
    siddhi_ALL,
    siddhi_OBJECT,
    siddhi_BOOL,
    siddhi_FLOAT,
    EveryAbsentSequenceSourceChain,
    EverySequenceSourceChain,
    BasicAbsentPatternSource,
    siddhi_DEFINE,
    siddhi_STREAM,
    AppAnnotation,
    siddhi_APP,
    siddhi_IN,
    RightAbsentPatternSource,
    siddhi_RightAbsentPatternSource1,
    LeftAbsentPatternSource,
    siddhi_LeftAbsentPatternSource1,
    EveryAbsentPatternSource,
    LogicalAbsentStatefulSource,
    siddhi_MillisecondValue,
    siddhi_UNIDIRECTIONAL,
    siddhi_JoinSource,
    StandardStream,
    JoinSource,
    siddhi_MainSource,
    JoinStream,
    INNER,
    FULL,
    RIGHT,
    JOIN,
    OUTER,
    LEFT,
    PER,
    WITHIN,
    siddhi_joins,
    siddhi_Per1,
    siddhi_WithinTimeRange,
    AbsentPatternSourceChain,
    siddhi_EveryAbsentPatternSource,
    siddhi_RightAbsentPatternSource,
    siddhi_LeftAbsentPatternSource,
    siddhi_PatternCollectionStatefulSource,
    siddhi_PatternSource,
    siddhi_BasicSource,
    siddhi_NOT,
    siddhi_Collect,
    siddhi_AND,
    SequenceSource,
    siddhi_LogicalStatefulSource,
    siddhi_LogicalAbsentStatefulSource,
    siddhi_SequenceCollectionStatefulSource,
    SequenceSourceChain,
    siddhi_PatternSourceChain,
    PatternStream,
    siddhi_AbsentPatternSourceChain,
    siddhi_EveryPatternSourceChain,
    siddhi_RightAbsentSequenceSource,
    siddhi_LeftAbsentSequenceSource,
    siddhi_BasicAbsentPatternSource,
    siddhi_EObject,
    HAVING,
    GROUP,
    siddhi_HavingExpr,
    siddhi_AbsentSequenceSourceChain,
    siddhi_SequenceSourceChain,
    siddhi_WithinTime,
    siddhi_SequenceSource,
    siddhi_EveryAbsentSequenceSourceChain,
    siddhi_EverySequenceSourceChain,
    siddhi_PatternStream,
    siddhi_SequenceStream,
    siddhi_JoinStream,
    siddhi_Attribute,
    siddhi_OutputAttribute,
    SELECT,
    FIRST,
    LAST,
    siddhi_AttributeIndex,
    SNAPSHOT,
    CURRENT,
    EXPIRED,
    RAW,
    EVENTS,
    ALL,
    siddhi_OutputRateType,
    siddhi_SetAssignment,
    SET,
    siddhi_SetClause,
    siddhi_OR,
    siddhi_ConditionRange,
    siddhi_OF,
    PartitionWithStream,
    siddhi_ConditionRanges,
    siddhi_ON,
    siddhi_Target,
    UPDATE,
    FOR,
    siddhi_ForTime,
    DELETE,
    INTO,
    INSERT,
    siddhi_QuerySection,
    siddhi_QueryInput,
    siddhi_AS,
    siddhi_Expression,
    siddhi_PropertyValue,
    siddhi_PartitionWithStream,
    END,
    BEGIN,
    WITH,
    PARTITION,
    Source1OrStandardStatefulSource,
    siddhi_StreamAlias,
    siddhi_StandardStatefulSource,
    siddhi_Source,
    OBJECT,
    BOOL,
    DOUBLE,
    FLOAT,
    LONG,
    INTS,
    STRINGS,
    FeaturesOrOutAttr,
    siddhi_OutAttr,
    siddhi_PropertySeparator,
    siddhi_AttributeReference,
    siddhi_GroupByQuerySelection,
    siddhi_StandardStream,
    BY,
    siddhi_GroupBy,
    siddhi_PropertyName,
    siddhi_AnnotationElement,
    siddhi_Name,
    YEARS,
    siddhi_YearValue,
    MONTHS,
    siddhi_MonthValue,
    WEEKS,
    siddhi_WeekValue,
    DAYS,
    siddhi_DayValue,
    HOURS,
    siddhi_HourValue,
    MINUTES,
    siddhi_MinuteValue,
    SECONDS,
    siddhi_SecondValue,
    AggregationTime,
    siddhi_AggregationTimeRange,
    siddhi_AggregationTimeInterval,
    siddhi_AggregationTimeDuration,
    siddhi_AggregationTime,
    OUTPUT,
    siddhi_OutputRate,
    WINDOW,
    siddhi_Win,
    siddhi_BasicSourceStreamHandlers1,
    AGGREGATE,
    FROM,
    AGGREGATION,
    siddhi_FunctionBody,
    siddhi_AttributeType,
    siddhi_LanguageName,
    siddhi_FunctionName,
    RETURN,
    siddhi_AnonymousStream,
    siddhi_QueryOutput,
    FUNCTION,
    siddhi_StringValue,
    siddhi_TimeValue,
    siddhi_EVERY,
    siddhi_TriggerName,
    AT,
    TRIGGER,
    siddhi_OutputEventType,
    siddhi_FunctionOperation,
    siddhi_AppAnnotation,
    siddhi_ExecutionPlan,
    TABLE,
    siddhi_Features,
    siddhi_Source1,
    siddhi_Annotation,
    STREAM,
    DEFINE,
    siddhi_DefinitionStream,
    siddhi_DefinitionTable,
    siddhi_Keyword,
    siddhi_Query,
    siddhi_ExecPartition,
    siddhi_ExecutionElement,
    siddhi_DefinitionAggregation,
    siddhi_DefinitionFunction,
    siddhi_DefinitionTrigger,
    siddhi_DefinitionWindow,
    siddhi_SiddhiQL,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_name_is_not_abstract():
    assert not inspect.isabstract(Name)


def test_name_constructor_exists():
    assert callable(Name.__init__)


def test_name_constructor_args():
    sig = inspect.signature(Name.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_l_is_not_abstract():
    assert not inspect.isabstract(siddhi_L)


def test_siddhi_l_constructor_exists():
    assert callable(siddhi_L.__init__)


def test_siddhi_l_constructor_args():
    sig = inspect.signature(siddhi_L.__init__)
    params = list(sig.parameters.keys())
    assert "l" in params, "Missing parameter 'l'"

def test_siddhi_l_has_l():
    assert hasattr(siddhi_L, "l")
    descriptor = None
    for klass in siddhi_L.__mro__:
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



def test_siddhi_long_literal_is_not_abstract():
    assert not inspect.isabstract(siddhi_LONG_LITERAL)


def test_siddhi_long_literal_constructor_exists():
    assert callable(siddhi_LONG_LITERAL.__init__)


def test_siddhi_long_literal_constructor_args():
    sig = inspect.signature(siddhi_LONG_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_f_is_not_abstract():
    assert not inspect.isabstract(siddhi_F)


def test_siddhi_f_constructor_exists():
    assert callable(siddhi_F.__init__)


def test_siddhi_f_constructor_args():
    sig = inspect.signature(siddhi_F.__init__)
    params = list(sig.parameters.keys())
    assert "f" in params, "Missing parameter 'f'"

def test_siddhi_f_has_f():
    assert hasattr(siddhi_F, "f")
    descriptor = None
    for klass in siddhi_F.__mro__:
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



def test_siddhi_float_literal_is_not_abstract():
    assert not inspect.isabstract(siddhi_FLOAT_LITERAL)


def test_siddhi_float_literal_constructor_exists():
    assert callable(siddhi_FLOAT_LITERAL.__init__)


def test_siddhi_float_literal_constructor_args():
    sig = inspect.signature(siddhi_FLOAT_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_d_is_not_abstract():
    assert not inspect.isabstract(siddhi_D)


def test_siddhi_d_constructor_exists():
    assert callable(siddhi_D.__init__)


def test_siddhi_d_constructor_args():
    sig = inspect.signature(siddhi_D.__init__)
    params = list(sig.parameters.keys())
    assert "d" in params, "Missing parameter 'd'"

def test_siddhi_d_has_d():
    assert hasattr(siddhi_D, "d")
    descriptor = None
    for klass in siddhi_D.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_e_is_not_abstract():
    assert not inspect.isabstract(siddhi_E)


def test_siddhi_e_constructor_exists():
    assert callable(siddhi_E.__init__)


def test_siddhi_e_constructor_args():
    sig = inspect.signature(siddhi_E.__init__)
    params = list(sig.parameters.keys())
    assert "e" in params, "Missing parameter 'e'"

def test_siddhi_e_has_e():
    assert hasattr(siddhi_E, "e")
    descriptor = None
    for klass in siddhi_E.__mro__:
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



def test_siddhi_double_literal_is_not_abstract():
    assert not inspect.isabstract(siddhi_DOUBLE_LITERAL)


def test_siddhi_double_literal_constructor_exists():
    assert callable(siddhi_DOUBLE_LITERAL.__init__)


def test_siddhi_double_literal_constructor_args():
    sig = inspect.signature(siddhi_DOUBLE_LITERAL.__init__)
    params = list(sig.parameters.keys())



def test_milliseconds_is_not_abstract():
    assert not inspect.isabstract(MILLISECONDS)


def test_milliseconds_constructor_exists():
    assert callable(MILLISECONDS.__init__)


def test_milliseconds_constructor_args():
    sig = inspect.signature(MILLISECONDS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_functionid_is_not_abstract():
    assert not inspect.isabstract(siddhi_FunctionId)


def test_siddhi_functionid_constructor_exists():
    assert callable(siddhi_FunctionId.__init__)


def test_siddhi_functionid_constructor_args():
    sig = inspect.signature(siddhi_FunctionId.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_functionnamespace_is_not_abstract():
    assert not inspect.isabstract(siddhi_FunctionNamespace)


def test_siddhi_functionnamespace_constructor_exists():
    assert callable(siddhi_FunctionNamespace.__init__)


def test_siddhi_functionnamespace_constructor_args():
    sig = inspect.signature(siddhi_FunctionNamespace.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_signedlongvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_SignedLongValue)


def test_siddhi_signedlongvalue_constructor_exists():
    assert callable(siddhi_SignedLongValue.__init__)


def test_siddhi_signedlongvalue_constructor_args():
    sig = inspect.signature(siddhi_SignedLongValue.__init__)
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



def test_siddhi_attributelist_is_not_abstract():
    assert not inspect.isabstract(siddhi_AttributeList)


def test_siddhi_attributelist_constructor_exists():
    assert callable(siddhi_AttributeList.__init__)


def test_siddhi_attributelist_constructor_args():
    sig = inspect.signature(siddhi_AttributeList.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_featuresoroutattr_is_not_abstract():
    assert not inspect.isabstract(siddhi_FeaturesOrOutAttr)


def test_siddhi_featuresoroutattr_constructor_exists():
    assert callable(siddhi_FeaturesOrOutAttr.__init__)


def test_siddhi_featuresoroutattr_constructor_args():
    sig = inspect.signature(siddhi_FeaturesOrOutAttr.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_siddhi_featuresoroutattr_has_name():
    assert hasattr(siddhi_FeaturesOrOutAttr, "name")
    descriptor = None
    for klass in siddhi_FeaturesOrOutAttr.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_featuresoroutattrreference_is_not_abstract():
    assert not inspect.isabstract(siddhi_FeaturesOrOutAttrReference)


def test_siddhi_featuresoroutattrreference_constructor_exists():
    assert callable(siddhi_FeaturesOrOutAttrReference.__init__)


def test_siddhi_featuresoroutattrreference_constructor_args():
    sig = inspect.signature(siddhi_FeaturesOrOutAttrReference.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_signedfloatvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_SignedFloatValue)


def test_siddhi_signedfloatvalue_constructor_exists():
    assert callable(siddhi_SignedFloatValue.__init__)


def test_siddhi_signedfloatvalue_constructor_args():
    sig = inspect.signature(siddhi_SignedFloatValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_signeddoublevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_SignedDoubleValue)


def test_siddhi_signeddoublevalue_constructor_exists():
    assert callable(siddhi_SignedDoubleValue.__init__)


def test_siddhi_signeddoublevalue_constructor_args():
    sig = inspect.signature(siddhi_SignedDoubleValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_boolvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_BoolValue)


def test_siddhi_boolvalue_constructor_exists():
    assert callable(siddhi_BoolValue.__init__)


def test_siddhi_boolvalue_constructor_args():
    sig = inspect.signature(siddhi_BoolValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_attributenamereference_is_not_abstract():
    assert not inspect.isabstract(siddhi_AttributeNameReference)


def test_siddhi_attributenamereference_constructor_exists():
    assert callable(siddhi_AttributeNameReference.__init__)


def test_siddhi_attributenamereference_constructor_args():
    sig = inspect.signature(siddhi_AttributeNameReference.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_source1orstandardstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_Source1OrStandardStatefulSource)


def test_siddhi_source1orstandardstatefulsource_constructor_exists():
    assert callable(siddhi_Source1OrStandardStatefulSource.__init__)


def test_siddhi_source1orstandardstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_Source1OrStandardStatefulSource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_siddhi_source1orstandardstatefulsource_has_name():
    assert hasattr(siddhi_Source1OrStandardStatefulSource, "name")
    descriptor = None
    for klass in siddhi_Source1OrStandardStatefulSource.__mro__:
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



def test_siddhi_literal_is_not_abstract():
    assert not inspect.isabstract(siddhi_Literal)


def test_siddhi_literal_constructor_exists():
    assert callable(siddhi_Literal.__init__)


def test_siddhi_literal_constructor_args():
    sig = inspect.signature(siddhi_Literal.__init__)
    params = list(sig.parameters.keys())



def test_mathdivmuloperation_is_not_abstract():
    assert not inspect.isabstract(MathDivmulOperation)


def test_mathdivmuloperation_constructor_exists():
    assert callable(MathDivmulOperation.__init__)


def test_mathdivmuloperation_constructor_args():
    sig = inspect.signature(MathDivmulOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathotheroperations_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathOtherOperations)


def test_siddhi_mathotheroperations_constructor_exists():
    assert callable(siddhi_MathOtherOperations.__init__)


def test_siddhi_mathotheroperations_constructor_args():
    sig = inspect.signature(siddhi_MathOtherOperations.__init__)
    params = list(sig.parameters.keys())



def test_mathaddsuboperation_is_not_abstract():
    assert not inspect.isabstract(MathAddsubOperation)


def test_mathaddsuboperation_constructor_exists():
    assert callable(MathAddsubOperation.__init__)


def test_mathaddsuboperation_constructor_args():
    sig = inspect.signature(MathAddsubOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathdivmuloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathDivmulOperation)


def test_siddhi_mathdivmuloperation_constructor_exists():
    assert callable(siddhi_MathDivmulOperation.__init__)


def test_siddhi_mathdivmuloperation_constructor_args():
    sig = inspect.signature(siddhi_MathDivmulOperation.__init__)
    params = list(sig.parameters.keys())
    assert "devide" in params, "Missing parameter 'devide'"
    assert "multiply" in params, "Missing parameter 'multiply'"
    assert "mod" in params, "Missing parameter 'mod'"

def test_siddhi_mathdivmuloperation_has_devide():
    assert hasattr(siddhi_MathDivmulOperation, "devide")
    descriptor = None
    for klass in siddhi_MathDivmulOperation.__mro__:
        if "devide" in klass.__dict__:
            descriptor = klass.__dict__["devide"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathdivmuloperation_has_multiply():
    assert hasattr(siddhi_MathDivmulOperation, "multiply")
    descriptor = None
    for klass in siddhi_MathDivmulOperation.__mro__:
        if "multiply" in klass.__dict__:
            descriptor = klass.__dict__["multiply"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathdivmuloperation_has_mod():
    assert hasattr(siddhi_MathDivmulOperation, "mod")
    descriptor = None
    for klass in siddhi_MathDivmulOperation.__mro__:
        if "mod" in klass.__dict__:
            descriptor = klass.__dict__["mod"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_sourceoreventreference_is_not_abstract():
    assert not inspect.isabstract(siddhi_SourceOrEventReference)


def test_siddhi_sourceoreventreference_constructor_exists():
    assert callable(siddhi_SourceOrEventReference.__init__)


def test_siddhi_sourceoreventreference_constructor_args():
    sig = inspect.signature(siddhi_SourceOrEventReference.__init__)
    params = list(sig.parameters.keys())



def test_setassignment_is_not_abstract():
    assert not inspect.isabstract(SetAssignment)


def test_setassignment_constructor_exists():
    assert callable(SetAssignment.__init__)


def test_setassignment_constructor_args():
    sig = inspect.signature(SetAssignment.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_constantvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_ConstantValue)


def test_siddhi_constantvalue_constructor_exists():
    assert callable(siddhi_ConstantValue.__init__)


def test_siddhi_constantvalue_constructor_args():
    sig = inspect.signature(siddhi_ConstantValue.__init__)
    params = list(sig.parameters.keys())
    assert "siv" in params, "Missing parameter 'siv'"

def test_siddhi_constantvalue_has_siv():
    assert hasattr(siddhi_ConstantValue, "siv")
    descriptor = None
    for klass in siddhi_ConstantValue.__mro__:
        if "siv" in klass.__dict__:
            descriptor = klass.__dict__["siv"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_streamreference_is_not_abstract():
    assert not inspect.isabstract(siddhi_StreamReference)


def test_siddhi_streamreference_constructor_exists():
    assert callable(siddhi_StreamReference.__init__)


def test_siddhi_streamreference_constructor_args():
    sig = inspect.signature(siddhi_StreamReference.__init__)
    params = list(sig.parameters.keys())
    assert "hash" in params, "Missing parameter 'hash'"

def test_siddhi_streamreference_has_hash():
    assert hasattr(siddhi_StreamReference, "hash")
    descriptor = None
    for klass in siddhi_StreamReference.__mro__:
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



def test_siddhi_nullcheck_is_not_abstract():
    assert not inspect.isabstract(siddhi_NullCheck)


def test_siddhi_nullcheck_constructor_exists():
    assert callable(siddhi_NullCheck.__init__)


def test_siddhi_nullcheck_constructor_args():
    sig = inspect.signature(siddhi_NullCheck.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_basicsourcestreamhandlers_is_not_abstract():
    assert not inspect.isabstract(siddhi_BasicSourceStreamHandlers)


def test_siddhi_basicsourcestreamhandlers_constructor_exists():
    assert callable(siddhi_BasicSourceStreamHandlers.__init__)


def test_siddhi_basicsourcestreamhandlers_constructor_args():
    sig = inspect.signature(siddhi_BasicSourceStreamHandlers.__init__)
    params = list(sig.parameters.keys())



def test_mathoperation_is_not_abstract():
    assert not inspect.isabstract(MathOperation)


def test_mathoperation_constructor_exists():
    assert callable(MathOperation.__init__)


def test_mathoperation_constructor_args():
    sig = inspect.signature(MathOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathaddsuboperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathAddsubOperation)


def test_siddhi_mathaddsuboperation_constructor_exists():
    assert callable(siddhi_MathAddsubOperation.__init__)


def test_siddhi_mathaddsuboperation_constructor_args():
    sig = inspect.signature(siddhi_MathAddsubOperation.__init__)
    params = list(sig.parameters.keys())
    assert "add" in params, "Missing parameter 'add'"
    assert "substract" in params, "Missing parameter 'substract'"

def test_siddhi_mathaddsuboperation_has_add():
    assert hasattr(siddhi_MathAddsubOperation, "add")
    descriptor = None
    for klass in siddhi_MathAddsubOperation.__mro__:
        if "add" in klass.__dict__:
            descriptor = klass.__dict__["add"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathaddsuboperation_has_substract():
    assert hasattr(siddhi_MathAddsubOperation, "substract")
    descriptor = None
    for klass in siddhi_MathAddsubOperation.__mro__:
        if "substract" in klass.__dict__:
            descriptor = klass.__dict__["substract"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathOperation)


def test_siddhi_mathoperation_constructor_exists():
    assert callable(siddhi_MathOperation.__init__)


def test_siddhi_mathoperation_constructor_args():
    sig = inspect.signature(siddhi_MathOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_streamfunction_is_not_abstract():
    assert not inspect.isabstract(siddhi_StreamFunction)


def test_siddhi_streamfunction_constructor_exists():
    assert callable(siddhi_StreamFunction.__init__)


def test_siddhi_streamfunction_constructor_args():
    sig = inspect.signature(siddhi_StreamFunction.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_filter_is_not_abstract():
    assert not inspect.isabstract(siddhi_Filter)


def test_siddhi_filter_constructor_exists():
    assert callable(siddhi_Filter.__init__)


def test_siddhi_filter_constructor_args():
    sig = inspect.signature(siddhi_Filter.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_basicsourcestreamhandler_is_not_abstract():
    assert not inspect.isabstract(siddhi_BasicSourceStreamHandler)


def test_siddhi_basicsourcestreamhandler_constructor_exists():
    assert callable(siddhi_BasicSourceStreamHandler.__init__)


def test_siddhi_basicsourcestreamhandler_constructor_args():
    sig = inspect.signature(siddhi_BasicSourceStreamHandler.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathgtltoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathGtLtOperation)


def test_siddhi_mathgtltoperation_constructor_exists():
    assert callable(siddhi_MathGtLtOperation.__init__)


def test_siddhi_mathgtltoperation_constructor_args():
    sig = inspect.signature(siddhi_MathGtLtOperation.__init__)
    params = list(sig.parameters.keys())
    assert "lt_eq" in params, "Missing parameter 'lt_eq'"
    assert "gt" in params, "Missing parameter 'gt'"
    assert "gt_eq" in params, "Missing parameter 'gt_eq'"
    assert "lt" in params, "Missing parameter 'lt'"

def test_siddhi_mathgtltoperation_has_lt_eq():
    assert hasattr(siddhi_MathGtLtOperation, "lt_eq")
    descriptor = None
    for klass in siddhi_MathGtLtOperation.__mro__:
        if "lt_eq" in klass.__dict__:
            descriptor = klass.__dict__["lt_eq"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathgtltoperation_has_gt():
    assert hasattr(siddhi_MathGtLtOperation, "gt")
    descriptor = None
    for klass in siddhi_MathGtLtOperation.__mro__:
        if "gt" in klass.__dict__:
            descriptor = klass.__dict__["gt"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathgtltoperation_has_gt_eq():
    assert hasattr(siddhi_MathGtLtOperation, "gt_eq")
    descriptor = None
    for klass in siddhi_MathGtLtOperation.__mro__:
        if "gt_eq" in klass.__dict__:
            descriptor = klass.__dict__["gt_eq"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathgtltoperation_has_lt():
    assert hasattr(siddhi_MathGtLtOperation, "lt")
    descriptor = None
    for klass in siddhi_MathGtLtOperation.__mro__:
        if "lt" in klass.__dict__:
            descriptor = klass.__dict__["lt"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_mathinoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathInOperation)


def test_siddhi_mathinoperation_constructor_exists():
    assert callable(siddhi_MathInOperation.__init__)


def test_siddhi_mathinoperation_constructor_args():
    sig = inspect.signature(siddhi_MathInOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_notoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_NotOperation)


def test_siddhi_notoperation_constructor_exists():
    assert callable(siddhi_NotOperation.__init__)


def test_siddhi_notoperation_constructor_args():
    sig = inspect.signature(siddhi_NotOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_mathequaloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathEqualOperation)


def test_siddhi_mathequaloperation_constructor_exists():
    assert callable(siddhi_MathEqualOperation.__init__)


def test_siddhi_mathequaloperation_constructor_args():
    sig = inspect.signature(siddhi_MathEqualOperation.__init__)
    params = list(sig.parameters.keys())
    assert "not_eq" in params, "Missing parameter 'not_eq'"
    assert "eq" in params, "Missing parameter 'eq'"

def test_siddhi_mathequaloperation_has_not_eq():
    assert hasattr(siddhi_MathEqualOperation, "not_eq")
    descriptor = None
    for klass in siddhi_MathEqualOperation.__mro__:
        if "not_eq" in klass.__dict__:
            descriptor = klass.__dict__["not_eq"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_mathequaloperation_has_eq():
    assert hasattr(siddhi_MathEqualOperation, "eq")
    descriptor = None
    for klass in siddhi_MathEqualOperation.__mro__:
        if "eq" in klass.__dict__:
            descriptor = klass.__dict__["eq"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_minutes_is_not_abstract():
    assert not inspect.isabstract(siddhi_MINUTES)


def test_siddhi_minutes_constructor_exists():
    assert callable(siddhi_MINUTES.__init__)


def test_siddhi_minutes_constructor_args():
    sig = inspect.signature(siddhi_MINUTES.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "min" in params, "Missing parameter 'min'"

def test_siddhi_minutes_has_minutes():
    assert hasattr(siddhi_MINUTES, "minutes")
    descriptor = None
    for klass in siddhi_MINUTES.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_minutes_has_minute():
    assert hasattr(siddhi_MINUTES, "minute")
    descriptor = None
    for klass in siddhi_MINUTES.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_minutes_has_min():
    assert hasattr(siddhi_MINUTES, "min")
    descriptor = None
    for klass in siddhi_MINUTES.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_hours_is_not_abstract():
    assert not inspect.isabstract(siddhi_HOURS)


def test_siddhi_hours_constructor_exists():
    assert callable(siddhi_HOURS.__init__)


def test_siddhi_hours_constructor_args():
    sig = inspect.signature(siddhi_HOURS.__init__)
    params = list(sig.parameters.keys())
    assert "hours" in params, "Missing parameter 'hours'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_siddhi_hours_has_hours():
    assert hasattr(siddhi_HOURS, "hours")
    descriptor = None
    for klass in siddhi_HOURS.__mro__:
        if "hours" in klass.__dict__:
            descriptor = klass.__dict__["hours"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_hours_has_hour():
    assert hasattr(siddhi_HOURS, "hour")
    descriptor = None
    for klass in siddhi_HOURS.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_days_is_not_abstract():
    assert not inspect.isabstract(siddhi_DAYS)


def test_siddhi_days_constructor_exists():
    assert callable(siddhi_DAYS.__init__)


def test_siddhi_days_constructor_args():
    sig = inspect.signature(siddhi_DAYS.__init__)
    params = list(sig.parameters.keys())
    assert "days" in params, "Missing parameter 'days'"
    assert "day" in params, "Missing parameter 'day'"

def test_siddhi_days_has_days():
    assert hasattr(siddhi_DAYS, "days")
    descriptor = None
    for klass in siddhi_DAYS.__mro__:
        if "days" in klass.__dict__:
            descriptor = klass.__dict__["days"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_days_has_day():
    assert hasattr(siddhi_DAYS, "day")
    descriptor = None
    for klass in siddhi_DAYS.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_weeks_is_not_abstract():
    assert not inspect.isabstract(siddhi_WEEKS)


def test_siddhi_weeks_constructor_exists():
    assert callable(siddhi_WEEKS.__init__)


def test_siddhi_weeks_constructor_args():
    sig = inspect.signature(siddhi_WEEKS.__init__)
    params = list(sig.parameters.keys())
    assert "weeks" in params, "Missing parameter 'weeks'"
    assert "week" in params, "Missing parameter 'week'"

def test_siddhi_weeks_has_weeks():
    assert hasattr(siddhi_WEEKS, "weeks")
    descriptor = None
    for klass in siddhi_WEEKS.__mro__:
        if "weeks" in klass.__dict__:
            descriptor = klass.__dict__["weeks"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_weeks_has_week():
    assert hasattr(siddhi_WEEKS, "week")
    descriptor = None
    for klass in siddhi_WEEKS.__mro__:
        if "week" in klass.__dict__:
            descriptor = klass.__dict__["week"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_months_is_not_abstract():
    assert not inspect.isabstract(siddhi_MONTHS)


def test_siddhi_months_constructor_exists():
    assert callable(siddhi_MONTHS.__init__)


def test_siddhi_months_constructor_args():
    sig = inspect.signature(siddhi_MONTHS.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "months" in params, "Missing parameter 'months'"

def test_siddhi_months_has_month():
    assert hasattr(siddhi_MONTHS, "month")
    descriptor = None
    for klass in siddhi_MONTHS.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_months_has_months():
    assert hasattr(siddhi_MONTHS, "months")
    descriptor = None
    for klass in siddhi_MONTHS.__mro__:
        if "months" in klass.__dict__:
            descriptor = klass.__dict__["months"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_mathlogicaloperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_MathLogicalOperation)


def test_siddhi_mathlogicaloperation_constructor_exists():
    assert callable(siddhi_MathLogicalOperation.__init__)


def test_siddhi_mathlogicaloperation_constructor_args():
    sig = inspect.signature(siddhi_MathLogicalOperation.__init__)
    params = list(sig.parameters.keys())



def test_rightabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(RightAbsentSequenceSource)


def test_rightabsentsequencesource_constructor_exists():
    assert callable(RightAbsentSequenceSource.__init__)


def test_rightabsentsequencesource_constructor_args():
    sig = inspect.signature(RightAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_rightabsentsequencesource1_is_not_abstract():
    assert not inspect.isabstract(siddhi_RightAbsentSequenceSource1)


def test_siddhi_rightabsentsequencesource1_constructor_exists():
    assert callable(siddhi_RightAbsentSequenceSource1.__init__)


def test_siddhi_rightabsentsequencesource1_constructor_args():
    sig = inspect.signature(siddhi_RightAbsentSequenceSource1.__init__)
    params = list(sig.parameters.keys())



def test_leftabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(LeftAbsentSequenceSource)


def test_leftabsentsequencesource_constructor_exists():
    assert callable(LeftAbsentSequenceSource.__init__)


def test_leftabsentsequencesource_constructor_args():
    sig = inspect.signature(LeftAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_leftabsentsequencesource1_is_not_abstract():
    assert not inspect.isabstract(siddhi_LeftAbsentSequenceSource1)


def test_siddhi_leftabsentsequencesource1_constructor_exists():
    assert callable(siddhi_LeftAbsentSequenceSource1.__init__)


def test_siddhi_leftabsentsequencesource1_constructor_args():
    sig = inspect.signature(siddhi_LeftAbsentSequenceSource1.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_true_is_not_abstract():
    assert not inspect.isabstract(siddhi_TRUE)


def test_siddhi_true_constructor_exists():
    assert callable(siddhi_TRUE.__init__)


def test_siddhi_true_constructor_args():
    sig = inspect.signature(siddhi_TRUE.__init__)
    params = list(sig.parameters.keys())
    assert "tr" in params, "Missing parameter 'tr'"

def test_siddhi_true_has_tr():
    assert hasattr(siddhi_TRUE, "tr")
    descriptor = None
    for klass in siddhi_TRUE.__mro__:
        if "tr" in klass.__dict__:
            descriptor = klass.__dict__["tr"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_false_is_not_abstract():
    assert not inspect.isabstract(siddhi_FALSE)


def test_siddhi_false_constructor_exists():
    assert callable(siddhi_FALSE.__init__)


def test_siddhi_false_constructor_args():
    sig = inspect.signature(siddhi_FALSE.__init__)
    params = list(sig.parameters.keys())
    assert "fals" in params, "Missing parameter 'fals'"

def test_siddhi_false_has_fals():
    assert hasattr(siddhi_FALSE, "fals")
    descriptor = None
    for klass in siddhi_FALSE.__mro__:
        if "fals" in klass.__dict__:
            descriptor = klass.__dict__["fals"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_milliseconds_is_not_abstract():
    assert not inspect.isabstract(siddhi_MILLISECONDS)


def test_siddhi_milliseconds_constructor_exists():
    assert callable(siddhi_MILLISECONDS.__init__)


def test_siddhi_milliseconds_constructor_args():
    sig = inspect.signature(siddhi_MILLISECONDS.__init__)
    params = list(sig.parameters.keys())
    assert "millisecond" in params, "Missing parameter 'millisecond'"
    assert "millisec" in params, "Missing parameter 'millisec'"
    assert "milliseconds" in params, "Missing parameter 'milliseconds'"

def test_siddhi_milliseconds_has_millisecond():
    assert hasattr(siddhi_MILLISECONDS, "millisecond")
    descriptor = None
    for klass in siddhi_MILLISECONDS.__mro__:
        if "millisecond" in klass.__dict__:
            descriptor = klass.__dict__["millisecond"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_milliseconds_has_millisec():
    assert hasattr(siddhi_MILLISECONDS, "millisec")
    descriptor = None
    for klass in siddhi_MILLISECONDS.__mro__:
        if "millisec" in klass.__dict__:
            descriptor = klass.__dict__["millisec"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_milliseconds_has_milliseconds():
    assert hasattr(siddhi_MILLISECONDS, "milliseconds")
    descriptor = None
    for klass in siddhi_MILLISECONDS.__mro__:
        if "milliseconds" in klass.__dict__:
            descriptor = klass.__dict__["milliseconds"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_seconds_is_not_abstract():
    assert not inspect.isabstract(siddhi_SECONDS)


def test_siddhi_seconds_constructor_exists():
    assert callable(siddhi_SECONDS.__init__)


def test_siddhi_seconds_constructor_args():
    sig = inspect.signature(siddhi_SECONDS.__init__)
    params = list(sig.parameters.keys())
    assert "seconds" in params, "Missing parameter 'seconds'"
    assert "sec" in params, "Missing parameter 'sec'"
    assert "second" in params, "Missing parameter 'second'"

def test_siddhi_seconds_has_seconds():
    assert hasattr(siddhi_SECONDS, "seconds")
    descriptor = None
    for klass in siddhi_SECONDS.__mro__:
        if "seconds" in klass.__dict__:
            descriptor = klass.__dict__["seconds"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_seconds_has_sec():
    assert hasattr(siddhi_SECONDS, "sec")
    descriptor = None
    for klass in siddhi_SECONDS.__mro__:
        if "sec" in klass.__dict__:
            descriptor = klass.__dict__["sec"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_seconds_has_second():
    assert hasattr(siddhi_SECONDS, "second")
    descriptor = None
    for klass in siddhi_SECONDS.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_outer_is_not_abstract():
    assert not inspect.isabstract(siddhi_OUTER)


def test_siddhi_outer_constructor_exists():
    assert callable(siddhi_OUTER.__init__)


def test_siddhi_outer_constructor_args():
    sig = inspect.signature(siddhi_OUTER.__init__)
    params = list(sig.parameters.keys())
    assert "outer" in params, "Missing parameter 'outer'"

def test_siddhi_outer_has_outer():
    assert hasattr(siddhi_OUTER, "outer")
    descriptor = None
    for klass in siddhi_OUTER.__mro__:
        if "outer" in klass.__dict__:
            descriptor = klass.__dict__["outer"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_inner_is_not_abstract():
    assert not inspect.isabstract(siddhi_INNER)


def test_siddhi_inner_constructor_exists():
    assert callable(siddhi_INNER.__init__)


def test_siddhi_inner_constructor_args():
    sig = inspect.signature(siddhi_INNER.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"

def test_siddhi_inner_has_inner():
    assert hasattr(siddhi_INNER, "inner")
    descriptor = None
    for klass in siddhi_INNER.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_join_is_not_abstract():
    assert not inspect.isabstract(siddhi_JOIN)


def test_siddhi_join_constructor_exists():
    assert callable(siddhi_JOIN.__init__)


def test_siddhi_join_constructor_args():
    sig = inspect.signature(siddhi_JOIN.__init__)
    params = list(sig.parameters.keys())
    assert "join" in params, "Missing parameter 'join'"

def test_siddhi_join_has_join():
    assert hasattr(siddhi_JOIN, "join")
    descriptor = None
    for klass in siddhi_JOIN.__mro__:
        if "join" in klass.__dict__:
            descriptor = klass.__dict__["join"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_full_is_not_abstract():
    assert not inspect.isabstract(siddhi_FULL)


def test_siddhi_full_constructor_exists():
    assert callable(siddhi_FULL.__init__)


def test_siddhi_full_constructor_args():
    sig = inspect.signature(siddhi_FULL.__init__)
    params = list(sig.parameters.keys())
    assert "full" in params, "Missing parameter 'full'"

def test_siddhi_full_has_full():
    assert hasattr(siddhi_FULL, "full")
    descriptor = None
    for klass in siddhi_FULL.__mro__:
        if "full" in klass.__dict__:
            descriptor = klass.__dict__["full"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_right_is_not_abstract():
    assert not inspect.isabstract(siddhi_RIGHT)


def test_siddhi_right_constructor_exists():
    assert callable(siddhi_RIGHT.__init__)


def test_siddhi_right_constructor_args():
    sig = inspect.signature(siddhi_RIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_siddhi_right_has_right():
    assert hasattr(siddhi_RIGHT, "right")
    descriptor = None
    for klass in siddhi_RIGHT.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_left_is_not_abstract():
    assert not inspect.isabstract(siddhi_LEFT)


def test_siddhi_left_constructor_exists():
    assert callable(siddhi_LEFT.__init__)


def test_siddhi_left_constructor_args():
    sig = inspect.signature(siddhi_LEFT.__init__)
    params = list(sig.parameters.keys())
    assert "left" in params, "Missing parameter 'left'"

def test_siddhi_left_has_left():
    assert hasattr(siddhi_LEFT, "left")
    descriptor = None
    for klass in siddhi_LEFT.__mro__:
        if "left" in klass.__dict__:
            descriptor = klass.__dict__["left"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_within_is_not_abstract():
    assert not inspect.isabstract(siddhi_WITHIN)


def test_siddhi_within_constructor_exists():
    assert callable(siddhi_WITHIN.__init__)


def test_siddhi_within_constructor_args():
    sig = inspect.signature(siddhi_WITHIN.__init__)
    params = list(sig.parameters.keys())
    assert "within" in params, "Missing parameter 'within'"

def test_siddhi_within_has_within():
    assert hasattr(siddhi_WITHIN, "within")
    descriptor = None
    for klass in siddhi_WITHIN.__mro__:
        if "within" in klass.__dict__:
            descriptor = klass.__dict__["within"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_years_is_not_abstract():
    assert not inspect.isabstract(siddhi_YEARS)


def test_siddhi_years_constructor_exists():
    assert callable(siddhi_YEARS.__init__)


def test_siddhi_years_constructor_args():
    sig = inspect.signature(siddhi_YEARS.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "years" in params, "Missing parameter 'years'"

def test_siddhi_years_has_year():
    assert hasattr(siddhi_YEARS, "year")
    descriptor = None
    for klass in siddhi_YEARS.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_years_has_years():
    assert hasattr(siddhi_YEARS, "years")
    descriptor = None
    for klass in siddhi_YEARS.__mro__:
        if "years" in klass.__dict__:
            descriptor = klass.__dict__["years"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_per_is_not_abstract():
    assert not inspect.isabstract(siddhi_PER)


def test_siddhi_per_constructor_exists():
    assert callable(siddhi_PER.__init__)


def test_siddhi_per_constructor_args():
    sig = inspect.signature(siddhi_PER.__init__)
    params = list(sig.parameters.keys())
    assert "per" in params, "Missing parameter 'per'"

def test_siddhi_per_has_per():
    assert hasattr(siddhi_PER, "per")
    descriptor = None
    for klass in siddhi_PER.__mro__:
        if "per" in klass.__dict__:
            descriptor = klass.__dict__["per"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_set_is_not_abstract():
    assert not inspect.isabstract(siddhi_SET)


def test_siddhi_set_constructor_exists():
    assert callable(siddhi_SET.__init__)


def test_siddhi_set_constructor_args():
    sig = inspect.signature(siddhi_SET.__init__)
    params = list(sig.parameters.keys())
    assert "set" in params, "Missing parameter 'set'"

def test_siddhi_set_has_set():
    assert hasattr(siddhi_SET, "set")
    descriptor = None
    for klass in siddhi_SET.__mro__:
        if "set" in klass.__dict__:
            descriptor = klass.__dict__["set"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_aggregate_is_not_abstract():
    assert not inspect.isabstract(siddhi_AGGREGATE)


def test_siddhi_aggregate_constructor_exists():
    assert callable(siddhi_AGGREGATE.__init__)


def test_siddhi_aggregate_constructor_args():
    sig = inspect.signature(siddhi_AGGREGATE.__init__)
    params = list(sig.parameters.keys())
    assert "agrregate" in params, "Missing parameter 'agrregate'"

def test_siddhi_aggregate_has_agrregate():
    assert hasattr(siddhi_AGGREGATE, "agrregate")
    descriptor = None
    for klass in siddhi_AGGREGATE.__mro__:
        if "agrregate" in klass.__dict__:
            descriptor = klass.__dict__["agrregate"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_aggregation_is_not_abstract():
    assert not inspect.isabstract(siddhi_AGGREGATION)


def test_siddhi_aggregation_constructor_exists():
    assert callable(siddhi_AGGREGATION.__init__)


def test_siddhi_aggregation_constructor_args():
    sig = inspect.signature(siddhi_AGGREGATION.__init__)
    params = list(sig.parameters.keys())
    assert "aggre" in params, "Missing parameter 'aggre'"

def test_siddhi_aggregation_has_aggre():
    assert hasattr(siddhi_AGGREGATION, "aggre")
    descriptor = None
    for klass in siddhi_AGGREGATION.__mro__:
        if "aggre" in klass.__dict__:
            descriptor = klass.__dict__["aggre"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_with_is_not_abstract():
    assert not inspect.isabstract(siddhi_WITH)


def test_siddhi_with_constructor_exists():
    assert callable(siddhi_WITH.__init__)


def test_siddhi_with_constructor_args():
    sig = inspect.signature(siddhi_WITH.__init__)
    params = list(sig.parameters.keys())
    assert "wi" in params, "Missing parameter 'wi'"

def test_siddhi_with_has_wi():
    assert hasattr(siddhi_WITH, "wi")
    descriptor = None
    for klass in siddhi_WITH.__mro__:
        if "wi" in klass.__dict__:
            descriptor = klass.__dict__["wi"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_partition_is_not_abstract():
    assert not inspect.isabstract(siddhi_PARTITION)


def test_siddhi_partition_constructor_exists():
    assert callable(siddhi_PARTITION.__init__)


def test_siddhi_partition_constructor_args():
    sig = inspect.signature(siddhi_PARTITION.__init__)
    params = list(sig.parameters.keys())
    assert "partition" in params, "Missing parameter 'partition'"

def test_siddhi_partition_has_partition():
    assert hasattr(siddhi_PARTITION, "partition")
    descriptor = None
    for klass in siddhi_PARTITION.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_end_is_not_abstract():
    assert not inspect.isabstract(siddhi_END)


def test_siddhi_end_constructor_exists():
    assert callable(siddhi_END.__init__)


def test_siddhi_end_constructor_args():
    sig = inspect.signature(siddhi_END.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_siddhi_end_has_end():
    assert hasattr(siddhi_END, "end")
    descriptor = None
    for klass in siddhi_END.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_update_is_not_abstract():
    assert not inspect.isabstract(siddhi_UPDATE)


def test_siddhi_update_constructor_exists():
    assert callable(siddhi_UPDATE.__init__)


def test_siddhi_update_constructor_args():
    sig = inspect.signature(siddhi_UPDATE.__init__)
    params = list(sig.parameters.keys())
    assert "update" in params, "Missing parameter 'update'"

def test_siddhi_update_has_update():
    assert hasattr(siddhi_UPDATE, "update")
    descriptor = None
    for klass in siddhi_UPDATE.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_for_is_not_abstract():
    assert not inspect.isabstract(siddhi_FOR)


def test_siddhi_for_constructor_exists():
    assert callable(siddhi_FOR.__init__)


def test_siddhi_for_constructor_args():
    sig = inspect.signature(siddhi_FOR.__init__)
    params = list(sig.parameters.keys())
    assert "for_" in params, "Missing parameter 'for_'"

def test_siddhi_for_has_for_():
    assert hasattr(siddhi_FOR, "for_")
    descriptor = None
    for klass in siddhi_FOR.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_delete_is_not_abstract():
    assert not inspect.isabstract(siddhi_DELETE)


def test_siddhi_delete_constructor_exists():
    assert callable(siddhi_DELETE.__init__)


def test_siddhi_delete_constructor_args():
    sig = inspect.signature(siddhi_DELETE.__init__)
    params = list(sig.parameters.keys())
    assert "delete" in params, "Missing parameter 'delete'"

def test_siddhi_delete_has_delete():
    assert hasattr(siddhi_DELETE, "delete")
    descriptor = None
    for klass in siddhi_DELETE.__mro__:
        if "delete" in klass.__dict__:
            descriptor = klass.__dict__["delete"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_plan_is_not_abstract():
    assert not inspect.isabstract(siddhi_PLAN)


def test_siddhi_plan_constructor_exists():
    assert callable(siddhi_PLAN.__init__)


def test_siddhi_plan_constructor_args():
    sig = inspect.signature(siddhi_PLAN.__init__)
    params = list(sig.parameters.keys())
    assert "plan" in params, "Missing parameter 'plan'"

def test_siddhi_plan_has_plan():
    assert hasattr(siddhi_PLAN, "plan")
    descriptor = None
    for klass in siddhi_PLAN.__mro__:
        if "plan" in klass.__dict__:
            descriptor = klass.__dict__["plan"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_begin_is_not_abstract():
    assert not inspect.isabstract(siddhi_BEGIN)


def test_siddhi_begin_constructor_exists():
    assert callable(siddhi_BEGIN.__init__)


def test_siddhi_begin_constructor_args():
    sig = inspect.signature(siddhi_BEGIN.__init__)
    params = list(sig.parameters.keys())
    assert "begin" in params, "Missing parameter 'begin'"

def test_siddhi_begin_has_begin():
    assert hasattr(siddhi_BEGIN, "begin")
    descriptor = None
    for klass in siddhi_BEGIN.__mro__:
        if "begin" in klass.__dict__:
            descriptor = klass.__dict__["begin"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_into_is_not_abstract():
    assert not inspect.isabstract(siddhi_INTO)


def test_siddhi_into_constructor_exists():
    assert callable(siddhi_INTO.__init__)


def test_siddhi_into_constructor_args():
    sig = inspect.signature(siddhi_INTO.__init__)
    params = list(sig.parameters.keys())
    assert "into" in params, "Missing parameter 'into'"

def test_siddhi_into_has_into():
    assert hasattr(siddhi_INTO, "into")
    descriptor = None
    for klass in siddhi_INTO.__mro__:
        if "into" in klass.__dict__:
            descriptor = klass.__dict__["into"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_insert_is_not_abstract():
    assert not inspect.isabstract(siddhi_INSERT)


def test_siddhi_insert_constructor_exists():
    assert callable(siddhi_INSERT.__init__)


def test_siddhi_insert_constructor_args():
    sig = inspect.signature(siddhi_INSERT.__init__)
    params = list(sig.parameters.keys())
    assert "insert" in params, "Missing parameter 'insert'"

def test_siddhi_insert_has_insert():
    assert hasattr(siddhi_INSERT, "insert")
    descriptor = None
    for klass in siddhi_INSERT.__mro__:
        if "insert" in klass.__dict__:
            descriptor = klass.__dict__["insert"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_first_is_not_abstract():
    assert not inspect.isabstract(siddhi_FIRST)


def test_siddhi_first_constructor_exists():
    assert callable(siddhi_FIRST.__init__)


def test_siddhi_first_constructor_args():
    sig = inspect.signature(siddhi_FIRST.__init__)
    params = list(sig.parameters.keys())
    assert "first" in params, "Missing parameter 'first'"

def test_siddhi_first_has_first():
    assert hasattr(siddhi_FIRST, "first")
    descriptor = None
    for klass in siddhi_FIRST.__mro__:
        if "first" in klass.__dict__:
            descriptor = klass.__dict__["first"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_snapshot_is_not_abstract():
    assert not inspect.isabstract(siddhi_SNAPSHOT)


def test_siddhi_snapshot_constructor_exists():
    assert callable(siddhi_SNAPSHOT.__init__)


def test_siddhi_snapshot_constructor_args():
    sig = inspect.signature(siddhi_SNAPSHOT.__init__)
    params = list(sig.parameters.keys())
    assert "snapshot" in params, "Missing parameter 'snapshot'"

def test_siddhi_snapshot_has_snapshot():
    assert hasattr(siddhi_SNAPSHOT, "snapshot")
    descriptor = None
    for klass in siddhi_SNAPSHOT.__mro__:
        if "snapshot" in klass.__dict__:
            descriptor = klass.__dict__["snapshot"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_having_is_not_abstract():
    assert not inspect.isabstract(siddhi_HAVING)


def test_siddhi_having_constructor_exists():
    assert callable(siddhi_HAVING.__init__)


def test_siddhi_having_constructor_args():
    sig = inspect.signature(siddhi_HAVING.__init__)
    params = list(sig.parameters.keys())
    assert "having" in params, "Missing parameter 'having'"

def test_siddhi_having_has_having():
    assert hasattr(siddhi_HAVING, "having")
    descriptor = None
    for klass in siddhi_HAVING.__mro__:
        if "having" in klass.__dict__:
            descriptor = klass.__dict__["having"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_by_is_not_abstract():
    assert not inspect.isabstract(siddhi_BY)


def test_siddhi_by_constructor_exists():
    assert callable(siddhi_BY.__init__)


def test_siddhi_by_constructor_args():
    sig = inspect.signature(siddhi_BY.__init__)
    params = list(sig.parameters.keys())
    assert "by" in params, "Missing parameter 'by'"

def test_siddhi_by_has_by():
    assert hasattr(siddhi_BY, "by")
    descriptor = None
    for klass in siddhi_BY.__mro__:
        if "by" in klass.__dict__:
            descriptor = klass.__dict__["by"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_group_is_not_abstract():
    assert not inspect.isabstract(siddhi_GROUP)


def test_siddhi_group_constructor_exists():
    assert callable(siddhi_GROUP.__init__)


def test_siddhi_group_constructor_args():
    sig = inspect.signature(siddhi_GROUP.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_siddhi_group_has_group():
    assert hasattr(siddhi_GROUP, "group")
    descriptor = None
    for klass in siddhi_GROUP.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_select_is_not_abstract():
    assert not inspect.isabstract(siddhi_SELECT)


def test_siddhi_select_constructor_exists():
    assert callable(siddhi_SELECT.__init__)


def test_siddhi_select_constructor_args():
    sig = inspect.signature(siddhi_SELECT.__init__)
    params = list(sig.parameters.keys())
    assert "select" in params, "Missing parameter 'select'"

def test_siddhi_select_has_select():
    assert hasattr(siddhi_SELECT, "select")
    descriptor = None
    for klass in siddhi_SELECT.__mro__:
        if "select" in klass.__dict__:
            descriptor = klass.__dict__["select"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_double_is_not_abstract():
    assert not inspect.isabstract(siddhi_DOUBLE)


def test_siddhi_double_constructor_exists():
    assert callable(siddhi_DOUBLE.__init__)


def test_siddhi_double_constructor_args():
    sig = inspect.signature(siddhi_DOUBLE.__init__)
    params = list(sig.parameters.keys())
    assert "double" in params, "Missing parameter 'double'"

def test_siddhi_double_has_double():
    assert hasattr(siddhi_DOUBLE, "double")
    descriptor = None
    for klass in siddhi_DOUBLE.__mro__:
        if "double" in klass.__dict__:
            descriptor = klass.__dict__["double"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_long_is_not_abstract():
    assert not inspect.isabstract(siddhi_LONG)


def test_siddhi_long_constructor_exists():
    assert callable(siddhi_LONG.__init__)


def test_siddhi_long_constructor_args():
    sig = inspect.signature(siddhi_LONG.__init__)
    params = list(sig.parameters.keys())
    assert "long" in params, "Missing parameter 'long'"

def test_siddhi_long_has_long():
    assert hasattr(siddhi_LONG, "long")
    descriptor = None
    for klass in siddhi_LONG.__mro__:
        if "long" in klass.__dict__:
            descriptor = klass.__dict__["long"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_ints_is_not_abstract():
    assert not inspect.isabstract(siddhi_INTS)


def test_siddhi_ints_constructor_exists():
    assert callable(siddhi_INTS.__init__)


def test_siddhi_ints_constructor_args():
    sig = inspect.signature(siddhi_INTS.__init__)
    params = list(sig.parameters.keys())
    assert "int" in params, "Missing parameter 'int'"

def test_siddhi_ints_has_int():
    assert hasattr(siddhi_INTS, "int")
    descriptor = None
    for klass in siddhi_INTS.__mro__:
        if "int" in klass.__dict__:
            descriptor = klass.__dict__["int"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_strings_is_not_abstract():
    assert not inspect.isabstract(siddhi_STRINGS)


def test_siddhi_strings_constructor_exists():
    assert callable(siddhi_STRINGS.__init__)


def test_siddhi_strings_constructor_args():
    sig = inspect.signature(siddhi_STRINGS.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"

def test_siddhi_strings_has_string():
    assert hasattr(siddhi_STRINGS, "string")
    descriptor = None
    for klass in siddhi_STRINGS.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_output_is_not_abstract():
    assert not inspect.isabstract(siddhi_OUTPUT)


def test_siddhi_output_constructor_exists():
    assert callable(siddhi_OUTPUT.__init__)


def test_siddhi_output_constructor_args():
    sig = inspect.signature(siddhi_OUTPUT.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"

def test_siddhi_output_has_output():
    assert hasattr(siddhi_OUTPUT, "output")
    descriptor = None
    for klass in siddhi_OUTPUT.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_window_is_not_abstract():
    assert not inspect.isabstract(siddhi_WINDOW)


def test_siddhi_window_constructor_exists():
    assert callable(siddhi_WINDOW.__init__)


def test_siddhi_window_constructor_args():
    sig = inspect.signature(siddhi_WINDOW.__init__)
    params = list(sig.parameters.keys())
    assert "window" in params, "Missing parameter 'window'"

def test_siddhi_window_has_window():
    assert hasattr(siddhi_WINDOW, "window")
    descriptor = None
    for klass in siddhi_WINDOW.__mro__:
        if "window" in klass.__dict__:
            descriptor = klass.__dict__["window"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_table_is_not_abstract():
    assert not inspect.isabstract(siddhi_TABLE)


def test_siddhi_table_constructor_exists():
    assert callable(siddhi_TABLE.__init__)


def test_siddhi_table_constructor_args():
    sig = inspect.signature(siddhi_TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "table" in params, "Missing parameter 'table'"

def test_siddhi_table_has_table():
    assert hasattr(siddhi_TABLE, "table")
    descriptor = None
    for klass in siddhi_TABLE.__mro__:
        if "table" in klass.__dict__:
            descriptor = klass.__dict__["table"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_from_is_not_abstract():
    assert not inspect.isabstract(siddhi_FROM)


def test_siddhi_from_constructor_exists():
    assert callable(siddhi_FROM.__init__)


def test_siddhi_from_constructor_args():
    sig = inspect.signature(siddhi_FROM.__init__)
    params = list(sig.parameters.keys())
    assert "from_" in params, "Missing parameter 'from_'"

def test_siddhi_from_has_from_():
    assert hasattr(siddhi_FROM, "from_")
    descriptor = None
    for klass in siddhi_FROM.__mro__:
        if "from_" in klass.__dict__:
            descriptor = klass.__dict__["from_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_return_is_not_abstract():
    assert not inspect.isabstract(siddhi_RETURN)


def test_siddhi_return_constructor_exists():
    assert callable(siddhi_RETURN.__init__)


def test_siddhi_return_constructor_args():
    sig = inspect.signature(siddhi_RETURN.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"

def test_siddhi_return_has_return_():
    assert hasattr(siddhi_RETURN, "return_")
    descriptor = None
    for klass in siddhi_RETURN.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_function_is_not_abstract():
    assert not inspect.isabstract(siddhi_FUNCTION)


def test_siddhi_function_constructor_exists():
    assert callable(siddhi_FUNCTION.__init__)


def test_siddhi_function_constructor_args():
    sig = inspect.signature(siddhi_FUNCTION.__init__)
    params = list(sig.parameters.keys())
    assert "function" in params, "Missing parameter 'function'"

def test_siddhi_function_has_function():
    assert hasattr(siddhi_FUNCTION, "function")
    descriptor = None
    for klass in siddhi_FUNCTION.__mro__:
        if "function" in klass.__dict__:
            descriptor = klass.__dict__["function"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_at_is_not_abstract():
    assert not inspect.isabstract(siddhi_AT)


def test_siddhi_at_constructor_exists():
    assert callable(siddhi_AT.__init__)


def test_siddhi_at_constructor_args():
    sig = inspect.signature(siddhi_AT.__init__)
    params = list(sig.parameters.keys())
    assert "at" in params, "Missing parameter 'at'"

def test_siddhi_at_has_at():
    assert hasattr(siddhi_AT, "at")
    descriptor = None
    for klass in siddhi_AT.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_trigger_is_not_abstract():
    assert not inspect.isabstract(siddhi_TRIGGER)


def test_siddhi_trigger_constructor_exists():
    assert callable(siddhi_TRIGGER.__init__)


def test_siddhi_trigger_constructor_args():
    sig = inspect.signature(siddhi_TRIGGER.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_siddhi_trigger_has_trigger():
    assert hasattr(siddhi_TRIGGER, "trigger")
    descriptor = None
    for klass in siddhi_TRIGGER.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_null_is_not_abstract():
    assert not inspect.isabstract(siddhi_NULL)


def test_siddhi_null_constructor_exists():
    assert callable(siddhi_NULL.__init__)


def test_siddhi_null_constructor_args():
    sig = inspect.signature(siddhi_NULL.__init__)
    params = list(sig.parameters.keys())
    assert "null" in params, "Missing parameter 'null'"

def test_siddhi_null_has_null():
    assert hasattr(siddhi_NULL, "null")
    descriptor = None
    for klass in siddhi_NULL.__mro__:
        if "null" in klass.__dict__:
            descriptor = klass.__dict__["null"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_is_is_not_abstract():
    assert not inspect.isabstract(siddhi_IS)


def test_siddhi_is_constructor_exists():
    assert callable(siddhi_IS.__init__)


def test_siddhi_is_constructor_args():
    sig = inspect.signature(siddhi_IS.__init__)
    params = list(sig.parameters.keys())
    assert "is_" in params, "Missing parameter 'is_'"

def test_siddhi_is_has_is_():
    assert hasattr(siddhi_IS, "is_")
    descriptor = None
    for klass in siddhi_IS.__mro__:
        if "is_" in klass.__dict__:
            descriptor = klass.__dict__["is_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_last_is_not_abstract():
    assert not inspect.isabstract(siddhi_LAST)


def test_siddhi_last_constructor_exists():
    assert callable(siddhi_LAST.__init__)


def test_siddhi_last_constructor_args():
    sig = inspect.signature(siddhi_LAST.__init__)
    params = list(sig.parameters.keys())
    assert "last" in params, "Missing parameter 'last'"

def test_siddhi_last_has_last():
    assert hasattr(siddhi_LAST, "last")
    descriptor = None
    for klass in siddhi_LAST.__mro__:
        if "last" in klass.__dict__:
            descriptor = klass.__dict__["last"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_current_is_not_abstract():
    assert not inspect.isabstract(siddhi_CURRENT)


def test_siddhi_current_constructor_exists():
    assert callable(siddhi_CURRENT.__init__)


def test_siddhi_current_constructor_args():
    sig = inspect.signature(siddhi_CURRENT.__init__)
    params = list(sig.parameters.keys())
    assert "currt" in params, "Missing parameter 'currt'"

def test_siddhi_current_has_currt():
    assert hasattr(siddhi_CURRENT, "currt")
    descriptor = None
    for klass in siddhi_CURRENT.__mro__:
        if "currt" in klass.__dict__:
            descriptor = klass.__dict__["currt"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_expired_is_not_abstract():
    assert not inspect.isabstract(siddhi_EXPIRED)


def test_siddhi_expired_constructor_exists():
    assert callable(siddhi_EXPIRED.__init__)


def test_siddhi_expired_constructor_args():
    sig = inspect.signature(siddhi_EXPIRED.__init__)
    params = list(sig.parameters.keys())
    assert "expired" in params, "Missing parameter 'expired'"

def test_siddhi_expired_has_expired():
    assert hasattr(siddhi_EXPIRED, "expired")
    descriptor = None
    for klass in siddhi_EXPIRED.__mro__:
        if "expired" in klass.__dict__:
            descriptor = klass.__dict__["expired"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_raw_is_not_abstract():
    assert not inspect.isabstract(siddhi_RAW)


def test_siddhi_raw_constructor_exists():
    assert callable(siddhi_RAW.__init__)


def test_siddhi_raw_constructor_args():
    sig = inspect.signature(siddhi_RAW.__init__)
    params = list(sig.parameters.keys())
    assert "raw" in params, "Missing parameter 'raw'"

def test_siddhi_raw_has_raw():
    assert hasattr(siddhi_RAW, "raw")
    descriptor = None
    for klass in siddhi_RAW.__mro__:
        if "raw" in klass.__dict__:
            descriptor = klass.__dict__["raw"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_events_is_not_abstract():
    assert not inspect.isabstract(siddhi_EVENTS)


def test_siddhi_events_constructor_exists():
    assert callable(siddhi_EVENTS.__init__)


def test_siddhi_events_constructor_args():
    sig = inspect.signature(siddhi_EVENTS.__init__)
    params = list(sig.parameters.keys())
    assert "events" in params, "Missing parameter 'events'"

def test_siddhi_events_has_events():
    assert hasattr(siddhi_EVENTS, "events")
    descriptor = None
    for klass in siddhi_EVENTS.__mro__:
        if "events" in klass.__dict__:
            descriptor = klass.__dict__["events"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_all_is_not_abstract():
    assert not inspect.isabstract(siddhi_ALL)


def test_siddhi_all_constructor_exists():
    assert callable(siddhi_ALL.__init__)


def test_siddhi_all_constructor_args():
    sig = inspect.signature(siddhi_ALL.__init__)
    params = list(sig.parameters.keys())
    assert "all" in params, "Missing parameter 'all'"

def test_siddhi_all_has_all():
    assert hasattr(siddhi_ALL, "all")
    descriptor = None
    for klass in siddhi_ALL.__mro__:
        if "all" in klass.__dict__:
            descriptor = klass.__dict__["all"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_object_is_not_abstract():
    assert not inspect.isabstract(siddhi_OBJECT)


def test_siddhi_object_constructor_exists():
    assert callable(siddhi_OBJECT.__init__)


def test_siddhi_object_constructor_args():
    sig = inspect.signature(siddhi_OBJECT.__init__)
    params = list(sig.parameters.keys())
    assert "object" in params, "Missing parameter 'object'"

def test_siddhi_object_has_object():
    assert hasattr(siddhi_OBJECT, "object")
    descriptor = None
    for klass in siddhi_OBJECT.__mro__:
        if "object" in klass.__dict__:
            descriptor = klass.__dict__["object"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_bool_is_not_abstract():
    assert not inspect.isabstract(siddhi_BOOL)


def test_siddhi_bool_constructor_exists():
    assert callable(siddhi_BOOL.__init__)


def test_siddhi_bool_constructor_args():
    sig = inspect.signature(siddhi_BOOL.__init__)
    params = list(sig.parameters.keys())
    assert "bool" in params, "Missing parameter 'bool'"

def test_siddhi_bool_has_bool():
    assert hasattr(siddhi_BOOL, "bool")
    descriptor = None
    for klass in siddhi_BOOL.__mro__:
        if "bool" in klass.__dict__:
            descriptor = klass.__dict__["bool"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_float_is_not_abstract():
    assert not inspect.isabstract(siddhi_FLOAT)


def test_siddhi_float_constructor_exists():
    assert callable(siddhi_FLOAT.__init__)


def test_siddhi_float_constructor_args():
    sig = inspect.signature(siddhi_FLOAT.__init__)
    params = list(sig.parameters.keys())
    assert "float" in params, "Missing parameter 'float'"

def test_siddhi_float_has_float():
    assert hasattr(siddhi_FLOAT, "float")
    descriptor = None
    for klass in siddhi_FLOAT.__mro__:
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



def test_siddhi_define_is_not_abstract():
    assert not inspect.isabstract(siddhi_DEFINE)


def test_siddhi_define_constructor_exists():
    assert callable(siddhi_DEFINE.__init__)


def test_siddhi_define_constructor_args():
    sig = inspect.signature(siddhi_DEFINE.__init__)
    params = list(sig.parameters.keys())
    assert "define" in params, "Missing parameter 'define'"

def test_siddhi_define_has_define():
    assert hasattr(siddhi_DEFINE, "define")
    descriptor = None
    for klass in siddhi_DEFINE.__mro__:
        if "define" in klass.__dict__:
            descriptor = klass.__dict__["define"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_stream_is_not_abstract():
    assert not inspect.isabstract(siddhi_STREAM)


def test_siddhi_stream_constructor_exists():
    assert callable(siddhi_STREAM.__init__)


def test_siddhi_stream_constructor_args():
    sig = inspect.signature(siddhi_STREAM.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_siddhi_stream_has_str():
    assert hasattr(siddhi_STREAM, "str")
    descriptor = None
    for klass in siddhi_STREAM.__mro__:
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



def test_siddhi_app_is_not_abstract():
    assert not inspect.isabstract(siddhi_APP)


def test_siddhi_app_constructor_exists():
    assert callable(siddhi_APP.__init__)


def test_siddhi_app_constructor_args():
    sig = inspect.signature(siddhi_APP.__init__)
    params = list(sig.parameters.keys())
    assert "ap" in params, "Missing parameter 'ap'"

def test_siddhi_app_has_ap():
    assert hasattr(siddhi_APP, "ap")
    descriptor = None
    for klass in siddhi_APP.__mro__:
        if "ap" in klass.__dict__:
            descriptor = klass.__dict__["ap"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_in_is_not_abstract():
    assert not inspect.isabstract(siddhi_IN)


def test_siddhi_in_constructor_exists():
    assert callable(siddhi_IN.__init__)


def test_siddhi_in_constructor_args():
    sig = inspect.signature(siddhi_IN.__init__)
    params = list(sig.parameters.keys())
    assert "in_" in params, "Missing parameter 'in_'"

def test_siddhi_in_has_in_():
    assert hasattr(siddhi_IN, "in_")
    descriptor = None
    for klass in siddhi_IN.__mro__:
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



def test_siddhi_rightabsentpatternsource1_is_not_abstract():
    assert not inspect.isabstract(siddhi_RightAbsentPatternSource1)


def test_siddhi_rightabsentpatternsource1_constructor_exists():
    assert callable(siddhi_RightAbsentPatternSource1.__init__)


def test_siddhi_rightabsentpatternsource1_constructor_args():
    sig = inspect.signature(siddhi_RightAbsentPatternSource1.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"

def test_siddhi_rightabsentpatternsource1_has_fb():
    assert hasattr(siddhi_RightAbsentPatternSource1, "fb")
    descriptor = None
    for klass in siddhi_RightAbsentPatternSource1.__mro__:
        if "fb" in klass.__dict__:
            descriptor = klass.__dict__["fb"]
            break
    assert isinstance(descriptor, property)



def test_leftabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(LeftAbsentPatternSource)


def test_leftabsentpatternsource_constructor_exists():
    assert callable(LeftAbsentPatternSource.__init__)


def test_leftabsentpatternsource_constructor_args():
    sig = inspect.signature(LeftAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_leftabsentpatternsource1_is_not_abstract():
    assert not inspect.isabstract(siddhi_LeftAbsentPatternSource1)


def test_siddhi_leftabsentpatternsource1_constructor_exists():
    assert callable(siddhi_LeftAbsentPatternSource1.__init__)


def test_siddhi_leftabsentpatternsource1_constructor_args():
    sig = inspect.signature(siddhi_LeftAbsentPatternSource1.__init__)
    params = list(sig.parameters.keys())
    assert "fb" in params, "Missing parameter 'fb'"

def test_siddhi_leftabsentpatternsource1_has_fb():
    assert hasattr(siddhi_LeftAbsentPatternSource1, "fb")
    descriptor = None
    for klass in siddhi_LeftAbsentPatternSource1.__mro__:
        if "fb" in klass.__dict__:
            descriptor = klass.__dict__["fb"]
            break
    assert isinstance(descriptor, property)



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



def test_siddhi_millisecondvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_MillisecondValue)


def test_siddhi_millisecondvalue_constructor_exists():
    assert callable(siddhi_MillisecondValue.__init__)


def test_siddhi_millisecondvalue_constructor_args():
    sig = inspect.signature(siddhi_MillisecondValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_unidirectional_is_not_abstract():
    assert not inspect.isabstract(siddhi_UNIDIRECTIONAL)


def test_siddhi_unidirectional_constructor_exists():
    assert callable(siddhi_UNIDIRECTIONAL.__init__)


def test_siddhi_unidirectional_constructor_args():
    sig = inspect.signature(siddhi_UNIDIRECTIONAL.__init__)
    params = list(sig.parameters.keys())
    assert "unidirectional" in params, "Missing parameter 'unidirectional'"

def test_siddhi_unidirectional_has_unidirectional():
    assert hasattr(siddhi_UNIDIRECTIONAL, "unidirectional")
    descriptor = None
    for klass in siddhi_UNIDIRECTIONAL.__mro__:
        if "unidirectional" in klass.__dict__:
            descriptor = klass.__dict__["unidirectional"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_joinsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_JoinSource)


def test_siddhi_joinsource_constructor_exists():
    assert callable(siddhi_JoinSource.__init__)


def test_siddhi_joinsource_constructor_args():
    sig = inspect.signature(siddhi_JoinSource.__init__)
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



def test_siddhi_mainsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_MainSource)


def test_siddhi_mainsource_constructor_exists():
    assert callable(siddhi_MainSource.__init__)


def test_siddhi_mainsource_constructor_args():
    sig = inspect.signature(siddhi_MainSource.__init__)
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



def test_siddhi_joins_is_not_abstract():
    assert not inspect.isabstract(siddhi_joins)


def test_siddhi_joins_constructor_exists():
    assert callable(siddhi_joins.__init__)


def test_siddhi_joins_constructor_args():
    sig = inspect.signature(siddhi_joins.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_per1_is_not_abstract():
    assert not inspect.isabstract(siddhi_Per1)


def test_siddhi_per1_constructor_exists():
    assert callable(siddhi_Per1.__init__)


def test_siddhi_per1_constructor_args():
    sig = inspect.signature(siddhi_Per1.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_withintimerange_is_not_abstract():
    assert not inspect.isabstract(siddhi_WithinTimeRange)


def test_siddhi_withintimerange_constructor_exists():
    assert callable(siddhi_WithinTimeRange.__init__)


def test_siddhi_withintimerange_constructor_args():
    sig = inspect.signature(siddhi_WithinTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_absentpatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(AbsentPatternSourceChain)


def test_absentpatternsourcechain_constructor_exists():
    assert callable(AbsentPatternSourceChain.__init__)


def test_absentpatternsourcechain_constructor_args():
    sig = inspect.signature(AbsentPatternSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_everyabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_EveryAbsentPatternSource)


def test_siddhi_everyabsentpatternsource_constructor_exists():
    assert callable(siddhi_EveryAbsentPatternSource.__init__)


def test_siddhi_everyabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi_EveryAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_rightabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_RightAbsentPatternSource)


def test_siddhi_rightabsentpatternsource_constructor_exists():
    assert callable(siddhi_RightAbsentPatternSource.__init__)


def test_siddhi_rightabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi_RightAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())
    assert "fb2" in params, "Missing parameter 'fb2'"

def test_siddhi_rightabsentpatternsource_has_fb2():
    assert hasattr(siddhi_RightAbsentPatternSource, "fb2")
    descriptor = None
    for klass in siddhi_RightAbsentPatternSource.__mro__:
        if "fb2" in klass.__dict__:
            descriptor = klass.__dict__["fb2"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_leftabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_LeftAbsentPatternSource)


def test_siddhi_leftabsentpatternsource_constructor_exists():
    assert callable(siddhi_LeftAbsentPatternSource.__init__)


def test_siddhi_leftabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi_LeftAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())
    assert "fb1" in params, "Missing parameter 'fb1'"

def test_siddhi_leftabsentpatternsource_has_fb1():
    assert hasattr(siddhi_LeftAbsentPatternSource, "fb1")
    descriptor = None
    for klass in siddhi_LeftAbsentPatternSource.__mro__:
        if "fb1" in klass.__dict__:
            descriptor = klass.__dict__["fb1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_patterncollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_PatternCollectionStatefulSource)


def test_siddhi_patterncollectionstatefulsource_constructor_exists():
    assert callable(siddhi_PatternCollectionStatefulSource.__init__)


def test_siddhi_patterncollectionstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_PatternCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_patternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_PatternSource)


def test_siddhi_patternsource_constructor_exists():
    assert callable(siddhi_PatternSource.__init__)


def test_siddhi_patternsource_constructor_args():
    sig = inspect.signature(siddhi_PatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_basicsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_BasicSource)


def test_siddhi_basicsource_constructor_exists():
    assert callable(siddhi_BasicSource.__init__)


def test_siddhi_basicsource_constructor_args():
    sig = inspect.signature(siddhi_BasicSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_not_is_not_abstract():
    assert not inspect.isabstract(siddhi_NOT)


def test_siddhi_not_constructor_exists():
    assert callable(siddhi_NOT.__init__)


def test_siddhi_not_constructor_args():
    sig = inspect.signature(siddhi_NOT.__init__)
    params = list(sig.parameters.keys())
    assert "not1" in params, "Missing parameter 'not1'"

def test_siddhi_not_has_not1():
    assert hasattr(siddhi_NOT, "not1")
    descriptor = None
    for klass in siddhi_NOT.__mro__:
        if "not1" in klass.__dict__:
            descriptor = klass.__dict__["not1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_collect_is_not_abstract():
    assert not inspect.isabstract(siddhi_Collect)


def test_siddhi_collect_constructor_exists():
    assert callable(siddhi_Collect.__init__)


def test_siddhi_collect_constructor_args():
    sig = inspect.signature(siddhi_Collect.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "end" in params, "Missing parameter 'end'"

def test_siddhi_collect_has_start():
    assert hasattr(siddhi_Collect, "start")
    descriptor = None
    for klass in siddhi_Collect.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_collect_has_end():
    assert hasattr(siddhi_Collect, "end")
    descriptor = None
    for klass in siddhi_Collect.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_and_is_not_abstract():
    assert not inspect.isabstract(siddhi_AND)


def test_siddhi_and_constructor_exists():
    assert callable(siddhi_AND.__init__)


def test_siddhi_and_constructor_args():
    sig = inspect.signature(siddhi_AND.__init__)
    params = list(sig.parameters.keys())
    assert "and_" in params, "Missing parameter 'and_'"

def test_siddhi_and_has_and_():
    assert hasattr(siddhi_AND, "and_")
    descriptor = None
    for klass in siddhi_AND.__mro__:
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



def test_siddhi_logicalstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_LogicalStatefulSource)


def test_siddhi_logicalstatefulsource_constructor_exists():
    assert callable(siddhi_LogicalStatefulSource.__init__)


def test_siddhi_logicalstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_LogicalStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_logicalabsentstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_LogicalAbsentStatefulSource)


def test_siddhi_logicalabsentstatefulsource_constructor_exists():
    assert callable(siddhi_LogicalAbsentStatefulSource.__init__)


def test_siddhi_logicalabsentstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_LogicalAbsentStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_sequencecollectionstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_SequenceCollectionStatefulSource)


def test_siddhi_sequencecollectionstatefulsource_constructor_exists():
    assert callable(siddhi_SequenceCollectionStatefulSource.__init__)


def test_siddhi_sequencecollectionstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_SequenceCollectionStatefulSource.__init__)
    params = list(sig.parameters.keys())



def test_sequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(SequenceSourceChain)


def test_sequencesourcechain_constructor_exists():
    assert callable(SequenceSourceChain.__init__)


def test_sequencesourcechain_constructor_args():
    sig = inspect.signature(SequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_patternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_PatternSourceChain)


def test_siddhi_patternsourcechain_constructor_exists():
    assert callable(siddhi_PatternSourceChain.__init__)


def test_siddhi_patternsourcechain_constructor_args():
    sig = inspect.signature(siddhi_PatternSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi_patternsourcechain_has_op():
    assert hasattr(siddhi_PatternSourceChain, "op")
    descriptor = None
    for klass in siddhi_PatternSourceChain.__mro__:
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



def test_siddhi_absentpatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_AbsentPatternSourceChain)


def test_siddhi_absentpatternsourcechain_constructor_exists():
    assert callable(siddhi_AbsentPatternSourceChain.__init__)


def test_siddhi_absentpatternsourcechain_constructor_args():
    sig = inspect.signature(siddhi_AbsentPatternSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_everypatternsourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_EveryPatternSourceChain)


def test_siddhi_everypatternsourcechain_constructor_exists():
    assert callable(siddhi_EveryPatternSourceChain.__init__)


def test_siddhi_everypatternsourcechain_constructor_args():
    sig = inspect.signature(siddhi_EveryPatternSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi_everypatternsourcechain_has_op():
    assert hasattr(siddhi_EveryPatternSourceChain, "op")
    descriptor = None
    for klass in siddhi_EveryPatternSourceChain.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_rightabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi_RightAbsentSequenceSource)


def test_siddhi_rightabsentsequencesource_constructor_exists():
    assert callable(siddhi_RightAbsentSequenceSource.__init__)


def test_siddhi_rightabsentsequencesource_constructor_args():
    sig = inspect.signature(siddhi_RightAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())
    assert "cp" in params, "Missing parameter 'cp'"
    assert "comma" in params, "Missing parameter 'comma'"
    assert "comm" in params, "Missing parameter 'comm'"
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi_rightabsentsequencesource_has_cp():
    assert hasattr(siddhi_RightAbsentSequenceSource, "cp")
    descriptor = None
    for klass in siddhi_RightAbsentSequenceSource.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_rightabsentsequencesource_has_comma():
    assert hasattr(siddhi_RightAbsentSequenceSource, "comma")
    descriptor = None
    for klass in siddhi_RightAbsentSequenceSource.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_rightabsentsequencesource_has_comm():
    assert hasattr(siddhi_RightAbsentSequenceSource, "comm")
    descriptor = None
    for klass in siddhi_RightAbsentSequenceSource.__mro__:
        if "comm" in klass.__dict__:
            descriptor = klass.__dict__["comm"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_rightabsentsequencesource_has_op():
    assert hasattr(siddhi_RightAbsentSequenceSource, "op")
    descriptor = None
    for klass in siddhi_RightAbsentSequenceSource.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_leftabsentsequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi_LeftAbsentSequenceSource)


def test_siddhi_leftabsentsequencesource_constructor_exists():
    assert callable(siddhi_LeftAbsentSequenceSource.__init__)


def test_siddhi_leftabsentsequencesource_constructor_args():
    sig = inspect.signature(siddhi_LeftAbsentSequenceSource.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"
    assert "comma" in params, "Missing parameter 'comma'"
    assert "comm" in params, "Missing parameter 'comm'"
    assert "cp" in params, "Missing parameter 'cp'"

def test_siddhi_leftabsentsequencesource_has_op():
    assert hasattr(siddhi_LeftAbsentSequenceSource, "op")
    descriptor = None
    for klass in siddhi_LeftAbsentSequenceSource.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_leftabsentsequencesource_has_comma():
    assert hasattr(siddhi_LeftAbsentSequenceSource, "comma")
    descriptor = None
    for klass in siddhi_LeftAbsentSequenceSource.__mro__:
        if "comma" in klass.__dict__:
            descriptor = klass.__dict__["comma"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_leftabsentsequencesource_has_comm():
    assert hasattr(siddhi_LeftAbsentSequenceSource, "comm")
    descriptor = None
    for klass in siddhi_LeftAbsentSequenceSource.__mro__:
        if "comm" in klass.__dict__:
            descriptor = klass.__dict__["comm"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_leftabsentsequencesource_has_cp():
    assert hasattr(siddhi_LeftAbsentSequenceSource, "cp")
    descriptor = None
    for klass in siddhi_LeftAbsentSequenceSource.__mro__:
        if "cp" in klass.__dict__:
            descriptor = klass.__dict__["cp"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_basicabsentpatternsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_BasicAbsentPatternSource)


def test_siddhi_basicabsentpatternsource_constructor_exists():
    assert callable(siddhi_BasicAbsentPatternSource.__init__)


def test_siddhi_basicabsentpatternsource_constructor_args():
    sig = inspect.signature(siddhi_BasicAbsentPatternSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_eobject_is_not_abstract():
    assert not inspect.isabstract(siddhi_EObject)


def test_siddhi_eobject_constructor_exists():
    assert callable(siddhi_EObject.__init__)


def test_siddhi_eobject_constructor_args():
    sig = inspect.signature(siddhi_EObject.__init__)
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



def test_siddhi_havingexpr_is_not_abstract():
    assert not inspect.isabstract(siddhi_HavingExpr)


def test_siddhi_havingexpr_constructor_exists():
    assert callable(siddhi_HavingExpr.__init__)


def test_siddhi_havingexpr_constructor_args():
    sig = inspect.signature(siddhi_HavingExpr.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_absentsequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_AbsentSequenceSourceChain)


def test_siddhi_absentsequencesourcechain_constructor_exists():
    assert callable(siddhi_AbsentSequenceSourceChain.__init__)


def test_siddhi_absentsequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi_AbsentSequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_sequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_SequenceSourceChain)


def test_siddhi_sequencesourcechain_constructor_exists():
    assert callable(siddhi_SequenceSourceChain.__init__)


def test_siddhi_sequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi_SequenceSourceChain.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_siddhi_sequencesourcechain_has_op():
    assert hasattr(siddhi_SequenceSourceChain, "op")
    descriptor = None
    for klass in siddhi_SequenceSourceChain.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_withintime_is_not_abstract():
    assert not inspect.isabstract(siddhi_WithinTime)


def test_siddhi_withintime_constructor_exists():
    assert callable(siddhi_WithinTime.__init__)


def test_siddhi_withintime_constructor_args():
    sig = inspect.signature(siddhi_WithinTime.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_sequencesource_is_not_abstract():
    assert not inspect.isabstract(siddhi_SequenceSource)


def test_siddhi_sequencesource_constructor_exists():
    assert callable(siddhi_SequenceSource.__init__)


def test_siddhi_sequencesource_constructor_args():
    sig = inspect.signature(siddhi_SequenceSource.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_everyabsentsequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_EveryAbsentSequenceSourceChain)


def test_siddhi_everyabsentsequencesourcechain_constructor_exists():
    assert callable(siddhi_EveryAbsentSequenceSourceChain.__init__)


def test_siddhi_everyabsentsequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi_EveryAbsentSequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_everysequencesourcechain_is_not_abstract():
    assert not inspect.isabstract(siddhi_EverySequenceSourceChain)


def test_siddhi_everysequencesourcechain_constructor_exists():
    assert callable(siddhi_EverySequenceSourceChain.__init__)


def test_siddhi_everysequencesourcechain_constructor_args():
    sig = inspect.signature(siddhi_EverySequenceSourceChain.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_patternstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_PatternStream)


def test_siddhi_patternstream_constructor_exists():
    assert callable(siddhi_PatternStream.__init__)


def test_siddhi_patternstream_constructor_args():
    sig = inspect.signature(siddhi_PatternStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_sequencestream_is_not_abstract():
    assert not inspect.isabstract(siddhi_SequenceStream)


def test_siddhi_sequencestream_constructor_exists():
    assert callable(siddhi_SequenceStream.__init__)


def test_siddhi_sequencestream_constructor_args():
    sig = inspect.signature(siddhi_SequenceStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_joinstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_JoinStream)


def test_siddhi_joinstream_constructor_exists():
    assert callable(siddhi_JoinStream.__init__)


def test_siddhi_joinstream_constructor_args():
    sig = inspect.signature(siddhi_JoinStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_attribute_is_not_abstract():
    assert not inspect.isabstract(siddhi_Attribute)


def test_siddhi_attribute_constructor_exists():
    assert callable(siddhi_Attribute.__init__)


def test_siddhi_attribute_constructor_args():
    sig = inspect.signature(siddhi_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_outputattribute_is_not_abstract():
    assert not inspect.isabstract(siddhi_OutputAttribute)


def test_siddhi_outputattribute_constructor_exists():
    assert callable(siddhi_OutputAttribute.__init__)


def test_siddhi_outputattribute_constructor_args():
    sig = inspect.signature(siddhi_OutputAttribute.__init__)
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



def test_siddhi_attributeindex_is_not_abstract():
    assert not inspect.isabstract(siddhi_AttributeIndex)


def test_siddhi_attributeindex_constructor_exists():
    assert callable(siddhi_AttributeIndex.__init__)


def test_siddhi_attributeindex_constructor_args():
    sig = inspect.signature(siddhi_AttributeIndex.__init__)
    params = list(sig.parameters.keys())



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



def test_siddhi_outputratetype_is_not_abstract():
    assert not inspect.isabstract(siddhi_OutputRateType)


def test_siddhi_outputratetype_constructor_exists():
    assert callable(siddhi_OutputRateType.__init__)


def test_siddhi_outputratetype_constructor_args():
    sig = inspect.signature(siddhi_OutputRateType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_setassignment_is_not_abstract():
    assert not inspect.isabstract(siddhi_SetAssignment)


def test_siddhi_setassignment_constructor_exists():
    assert callable(siddhi_SetAssignment.__init__)


def test_siddhi_setassignment_constructor_args():
    sig = inspect.signature(siddhi_SetAssignment.__init__)
    params = list(sig.parameters.keys())



def test_set_is_not_abstract():
    assert not inspect.isabstract(SET)


def test_set_constructor_exists():
    assert callable(SET.__init__)


def test_set_constructor_args():
    sig = inspect.signature(SET.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_setclause_is_not_abstract():
    assert not inspect.isabstract(siddhi_SetClause)


def test_siddhi_setclause_constructor_exists():
    assert callable(siddhi_SetClause.__init__)


def test_siddhi_setclause_constructor_args():
    sig = inspect.signature(siddhi_SetClause.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_or_is_not_abstract():
    assert not inspect.isabstract(siddhi_OR)


def test_siddhi_or_constructor_exists():
    assert callable(siddhi_OR.__init__)


def test_siddhi_or_constructor_args():
    sig = inspect.signature(siddhi_OR.__init__)
    params = list(sig.parameters.keys())
    assert "or_" in params, "Missing parameter 'or_'"

def test_siddhi_or_has_or_():
    assert hasattr(siddhi_OR, "or_")
    descriptor = None
    for klass in siddhi_OR.__mro__:
        if "or_" in klass.__dict__:
            descriptor = klass.__dict__["or_"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_conditionrange_is_not_abstract():
    assert not inspect.isabstract(siddhi_ConditionRange)


def test_siddhi_conditionrange_constructor_exists():
    assert callable(siddhi_ConditionRange.__init__)


def test_siddhi_conditionrange_constructor_args():
    sig = inspect.signature(siddhi_ConditionRange.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_of_is_not_abstract():
    assert not inspect.isabstract(siddhi_OF)


def test_siddhi_of_constructor_exists():
    assert callable(siddhi_OF.__init__)


def test_siddhi_of_constructor_args():
    sig = inspect.signature(siddhi_OF.__init__)
    params = list(sig.parameters.keys())
    assert "of" in params, "Missing parameter 'of'"

def test_siddhi_of_has_of():
    assert hasattr(siddhi_OF, "of")
    descriptor = None
    for klass in siddhi_OF.__mro__:
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



def test_siddhi_conditionranges_is_not_abstract():
    assert not inspect.isabstract(siddhi_ConditionRanges)


def test_siddhi_conditionranges_constructor_exists():
    assert callable(siddhi_ConditionRanges.__init__)


def test_siddhi_conditionranges_constructor_args():
    sig = inspect.signature(siddhi_ConditionRanges.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_on_is_not_abstract():
    assert not inspect.isabstract(siddhi_ON)


def test_siddhi_on_constructor_exists():
    assert callable(siddhi_ON.__init__)


def test_siddhi_on_constructor_args():
    sig = inspect.signature(siddhi_ON.__init__)
    params = list(sig.parameters.keys())
    assert "on" in params, "Missing parameter 'on'"

def test_siddhi_on_has_on():
    assert hasattr(siddhi_ON, "on")
    descriptor = None
    for klass in siddhi_ON.__mro__:
        if "on" in klass.__dict__:
            descriptor = klass.__dict__["on"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_target_is_not_abstract():
    assert not inspect.isabstract(siddhi_Target)


def test_siddhi_target_constructor_exists():
    assert callable(siddhi_Target.__init__)


def test_siddhi_target_constructor_args():
    sig = inspect.signature(siddhi_Target.__init__)
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



def test_siddhi_fortime_is_not_abstract():
    assert not inspect.isabstract(siddhi_ForTime)


def test_siddhi_fortime_constructor_exists():
    assert callable(siddhi_ForTime.__init__)


def test_siddhi_fortime_constructor_args():
    sig = inspect.signature(siddhi_ForTime.__init__)
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



def test_siddhi_querysection_is_not_abstract():
    assert not inspect.isabstract(siddhi_QuerySection)


def test_siddhi_querysection_constructor_exists():
    assert callable(siddhi_QuerySection.__init__)


def test_siddhi_querysection_constructor_args():
    sig = inspect.signature(siddhi_QuerySection.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_queryinput_is_not_abstract():
    assert not inspect.isabstract(siddhi_QueryInput)


def test_siddhi_queryinput_constructor_exists():
    assert callable(siddhi_QueryInput.__init__)


def test_siddhi_queryinput_constructor_args():
    sig = inspect.signature(siddhi_QueryInput.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_as_is_not_abstract():
    assert not inspect.isabstract(siddhi_AS)


def test_siddhi_as_constructor_exists():
    assert callable(siddhi_AS.__init__)


def test_siddhi_as_constructor_args():
    sig = inspect.signature(siddhi_AS.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_siddhi_as_has_a():
    assert hasattr(siddhi_AS, "a")
    descriptor = None
    for klass in siddhi_AS.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_expression_is_not_abstract():
    assert not inspect.isabstract(siddhi_Expression)


def test_siddhi_expression_constructor_exists():
    assert callable(siddhi_Expression.__init__)


def test_siddhi_expression_constructor_args():
    sig = inspect.signature(siddhi_Expression.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_propertyvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_PropertyValue)


def test_siddhi_propertyvalue_constructor_exists():
    assert callable(siddhi_PropertyValue.__init__)


def test_siddhi_propertyvalue_constructor_args():
    sig = inspect.signature(siddhi_PropertyValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_partitionwithstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_PartitionWithStream)


def test_siddhi_partitionwithstream_constructor_exists():
    assert callable(siddhi_PartitionWithStream.__init__)


def test_siddhi_partitionwithstream_constructor_args():
    sig = inspect.signature(siddhi_PartitionWithStream.__init__)
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



def test_siddhi_streamalias_is_not_abstract():
    assert not inspect.isabstract(siddhi_StreamAlias)


def test_siddhi_streamalias_constructor_exists():
    assert callable(siddhi_StreamAlias.__init__)


def test_siddhi_streamalias_constructor_args():
    sig = inspect.signature(siddhi_StreamAlias.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_standardstatefulsource_is_not_abstract():
    assert not inspect.isabstract(siddhi_StandardStatefulSource)


def test_siddhi_standardstatefulsource_constructor_exists():
    assert callable(siddhi_StandardStatefulSource.__init__)


def test_siddhi_standardstatefulsource_constructor_args():
    sig = inspect.signature(siddhi_StandardStatefulSource.__init__)
    params = list(sig.parameters.keys())
    assert "zero_or_more" in params, "Missing parameter 'zero_or_more'"
    assert "zero_or_one" in params, "Missing parameter 'zero_or_one'"
    assert "one_or_more" in params, "Missing parameter 'one_or_more'"

def test_siddhi_standardstatefulsource_has_zero_or_more():
    assert hasattr(siddhi_StandardStatefulSource, "zero_or_more")
    descriptor = None
    for klass in siddhi_StandardStatefulSource.__mro__:
        if "zero_or_more" in klass.__dict__:
            descriptor = klass.__dict__["zero_or_more"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_standardstatefulsource_has_zero_or_one():
    assert hasattr(siddhi_StandardStatefulSource, "zero_or_one")
    descriptor = None
    for klass in siddhi_StandardStatefulSource.__mro__:
        if "zero_or_one" in klass.__dict__:
            descriptor = klass.__dict__["zero_or_one"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_standardstatefulsource_has_one_or_more():
    assert hasattr(siddhi_StandardStatefulSource, "one_or_more")
    descriptor = None
    for klass in siddhi_StandardStatefulSource.__mro__:
        if "one_or_more" in klass.__dict__:
            descriptor = klass.__dict__["one_or_more"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_source_is_not_abstract():
    assert not inspect.isabstract(siddhi_Source)


def test_siddhi_source_constructor_exists():
    assert callable(siddhi_Source.__init__)


def test_siddhi_source_constructor_args():
    sig = inspect.signature(siddhi_Source.__init__)
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



def test_siddhi_outattr_is_not_abstract():
    assert not inspect.isabstract(siddhi_OutAttr)


def test_siddhi_outattr_constructor_exists():
    assert callable(siddhi_OutAttr.__init__)


def test_siddhi_outattr_constructor_args():
    sig = inspect.signature(siddhi_OutAttr.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_propertyseparator_is_not_abstract():
    assert not inspect.isabstract(siddhi_PropertySeparator)


def test_siddhi_propertyseparator_constructor_exists():
    assert callable(siddhi_PropertySeparator.__init__)


def test_siddhi_propertyseparator_constructor_args():
    sig = inspect.signature(siddhi_PropertySeparator.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_attributereference_is_not_abstract():
    assert not inspect.isabstract(siddhi_AttributeReference)


def test_siddhi_attributereference_constructor_exists():
    assert callable(siddhi_AttributeReference.__init__)


def test_siddhi_attributereference_constructor_args():
    sig = inspect.signature(siddhi_AttributeReference.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hash2" in params, "Missing parameter 'hash2'"
    assert "hash1" in params, "Missing parameter 'hash1'"

def test_siddhi_attributereference_has_name():
    assert hasattr(siddhi_AttributeReference, "name")
    descriptor = None
    for klass in siddhi_AttributeReference.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_attributereference_has_hash2():
    assert hasattr(siddhi_AttributeReference, "hash2")
    descriptor = None
    for klass in siddhi_AttributeReference.__mro__:
        if "hash2" in klass.__dict__:
            descriptor = klass.__dict__["hash2"]
            break
    assert isinstance(descriptor, property)

def test_siddhi_attributereference_has_hash1():
    assert hasattr(siddhi_AttributeReference, "hash1")
    descriptor = None
    for klass in siddhi_AttributeReference.__mro__:
        if "hash1" in klass.__dict__:
            descriptor = klass.__dict__["hash1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_groupbyqueryselection_is_not_abstract():
    assert not inspect.isabstract(siddhi_GroupByQuerySelection)


def test_siddhi_groupbyqueryselection_constructor_exists():
    assert callable(siddhi_GroupByQuerySelection.__init__)


def test_siddhi_groupbyqueryselection_constructor_args():
    sig = inspect.signature(siddhi_GroupByQuerySelection.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_standardstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_StandardStream)


def test_siddhi_standardstream_constructor_exists():
    assert callable(siddhi_StandardStream.__init__)


def test_siddhi_standardstream_constructor_args():
    sig = inspect.signature(siddhi_StandardStream.__init__)
    params = list(sig.parameters.keys())



def test_by_is_not_abstract():
    assert not inspect.isabstract(BY)


def test_by_constructor_exists():
    assert callable(BY.__init__)


def test_by_constructor_args():
    sig = inspect.signature(BY.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_groupby_is_not_abstract():
    assert not inspect.isabstract(siddhi_GroupBy)


def test_siddhi_groupby_constructor_exists():
    assert callable(siddhi_GroupBy.__init__)


def test_siddhi_groupby_constructor_args():
    sig = inspect.signature(siddhi_GroupBy.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_propertyname_is_not_abstract():
    assert not inspect.isabstract(siddhi_PropertyName)


def test_siddhi_propertyname_constructor_exists():
    assert callable(siddhi_PropertyName.__init__)


def test_siddhi_propertyname_constructor_args():
    sig = inspect.signature(siddhi_PropertyName.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_annotationelement_is_not_abstract():
    assert not inspect.isabstract(siddhi_AnnotationElement)


def test_siddhi_annotationelement_constructor_exists():
    assert callable(siddhi_AnnotationElement.__init__)


def test_siddhi_annotationelement_constructor_args():
    sig = inspect.signature(siddhi_AnnotationElement.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_name_is_not_abstract():
    assert not inspect.isabstract(siddhi_Name)


def test_siddhi_name_constructor_exists():
    assert callable(siddhi_Name.__init__)


def test_siddhi_name_constructor_args():
    sig = inspect.signature(siddhi_Name.__init__)
    params = list(sig.parameters.keys())
    assert "na" in params, "Missing parameter 'na'"

def test_siddhi_name_has_na():
    assert hasattr(siddhi_Name, "na")
    descriptor = None
    for klass in siddhi_Name.__mro__:
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



def test_siddhi_yearvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_YearValue)


def test_siddhi_yearvalue_constructor_exists():
    assert callable(siddhi_YearValue.__init__)


def test_siddhi_yearvalue_constructor_args():
    sig = inspect.signature(siddhi_YearValue.__init__)
    params = list(sig.parameters.keys())



def test_months_is_not_abstract():
    assert not inspect.isabstract(MONTHS)


def test_months_constructor_exists():
    assert callable(MONTHS.__init__)


def test_months_constructor_args():
    sig = inspect.signature(MONTHS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_monthvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_MonthValue)


def test_siddhi_monthvalue_constructor_exists():
    assert callable(siddhi_MonthValue.__init__)


def test_siddhi_monthvalue_constructor_args():
    sig = inspect.signature(siddhi_MonthValue.__init__)
    params = list(sig.parameters.keys())



def test_weeks_is_not_abstract():
    assert not inspect.isabstract(WEEKS)


def test_weeks_constructor_exists():
    assert callable(WEEKS.__init__)


def test_weeks_constructor_args():
    sig = inspect.signature(WEEKS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_weekvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_WeekValue)


def test_siddhi_weekvalue_constructor_exists():
    assert callable(siddhi_WeekValue.__init__)


def test_siddhi_weekvalue_constructor_args():
    sig = inspect.signature(siddhi_WeekValue.__init__)
    params = list(sig.parameters.keys())



def test_days_is_not_abstract():
    assert not inspect.isabstract(DAYS)


def test_days_constructor_exists():
    assert callable(DAYS.__init__)


def test_days_constructor_args():
    sig = inspect.signature(DAYS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_dayvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_DayValue)


def test_siddhi_dayvalue_constructor_exists():
    assert callable(siddhi_DayValue.__init__)


def test_siddhi_dayvalue_constructor_args():
    sig = inspect.signature(siddhi_DayValue.__init__)
    params = list(sig.parameters.keys())



def test_hours_is_not_abstract():
    assert not inspect.isabstract(HOURS)


def test_hours_constructor_exists():
    assert callable(HOURS.__init__)


def test_hours_constructor_args():
    sig = inspect.signature(HOURS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_hourvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_HourValue)


def test_siddhi_hourvalue_constructor_exists():
    assert callable(siddhi_HourValue.__init__)


def test_siddhi_hourvalue_constructor_args():
    sig = inspect.signature(siddhi_HourValue.__init__)
    params = list(sig.parameters.keys())



def test_minutes_is_not_abstract():
    assert not inspect.isabstract(MINUTES)


def test_minutes_constructor_exists():
    assert callable(MINUTES.__init__)


def test_minutes_constructor_args():
    sig = inspect.signature(MINUTES.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_minutevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_MinuteValue)


def test_siddhi_minutevalue_constructor_exists():
    assert callable(siddhi_MinuteValue.__init__)


def test_siddhi_minutevalue_constructor_args():
    sig = inspect.signature(siddhi_MinuteValue.__init__)
    params = list(sig.parameters.keys())



def test_seconds_is_not_abstract():
    assert not inspect.isabstract(SECONDS)


def test_seconds_constructor_exists():
    assert callable(SECONDS.__init__)


def test_seconds_constructor_args():
    sig = inspect.signature(SECONDS.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_secondvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_SecondValue)


def test_siddhi_secondvalue_constructor_exists():
    assert callable(siddhi_SecondValue.__init__)


def test_siddhi_secondvalue_constructor_args():
    sig = inspect.signature(siddhi_SecondValue.__init__)
    params = list(sig.parameters.keys())



def test_aggregationtime_is_not_abstract():
    assert not inspect.isabstract(AggregationTime)


def test_aggregationtime_constructor_exists():
    assert callable(AggregationTime.__init__)


def test_aggregationtime_constructor_args():
    sig = inspect.signature(AggregationTime.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_aggregationtimerange_is_not_abstract():
    assert not inspect.isabstract(siddhi_AggregationTimeRange)


def test_siddhi_aggregationtimerange_constructor_exists():
    assert callable(siddhi_AggregationTimeRange.__init__)


def test_siddhi_aggregationtimerange_constructor_args():
    sig = inspect.signature(siddhi_AggregationTimeRange.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_aggregationtimeinterval_is_not_abstract():
    assert not inspect.isabstract(siddhi_AggregationTimeInterval)


def test_siddhi_aggregationtimeinterval_constructor_exists():
    assert callable(siddhi_AggregationTimeInterval.__init__)


def test_siddhi_aggregationtimeinterval_constructor_args():
    sig = inspect.signature(siddhi_AggregationTimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_aggregationtimeduration_is_not_abstract():
    assert not inspect.isabstract(siddhi_AggregationTimeDuration)


def test_siddhi_aggregationtimeduration_constructor_exists():
    assert callable(siddhi_AggregationTimeDuration.__init__)


def test_siddhi_aggregationtimeduration_constructor_args():
    sig = inspect.signature(siddhi_AggregationTimeDuration.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_aggregationtime_is_not_abstract():
    assert not inspect.isabstract(siddhi_AggregationTime)


def test_siddhi_aggregationtime_constructor_exists():
    assert callable(siddhi_AggregationTime.__init__)


def test_siddhi_aggregationtime_constructor_args():
    sig = inspect.signature(siddhi_AggregationTime.__init__)
    params = list(sig.parameters.keys())



def test_output_is_not_abstract():
    assert not inspect.isabstract(OUTPUT)


def test_output_constructor_exists():
    assert callable(OUTPUT.__init__)


def test_output_constructor_args():
    sig = inspect.signature(OUTPUT.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_outputrate_is_not_abstract():
    assert not inspect.isabstract(siddhi_OutputRate)


def test_siddhi_outputrate_constructor_exists():
    assert callable(siddhi_OutputRate.__init__)


def test_siddhi_outputrate_constructor_args():
    sig = inspect.signature(siddhi_OutputRate.__init__)
    params = list(sig.parameters.keys())



def test_window_is_not_abstract():
    assert not inspect.isabstract(WINDOW)


def test_window_constructor_exists():
    assert callable(WINDOW.__init__)


def test_window_constructor_args():
    sig = inspect.signature(WINDOW.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_win_is_not_abstract():
    assert not inspect.isabstract(siddhi_Win)


def test_siddhi_win_constructor_exists():
    assert callable(siddhi_Win.__init__)


def test_siddhi_win_constructor_args():
    sig = inspect.signature(siddhi_Win.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_basicsourcestreamhandlers1_is_not_abstract():
    assert not inspect.isabstract(siddhi_BasicSourceStreamHandlers1)


def test_siddhi_basicsourcestreamhandlers1_constructor_exists():
    assert callable(siddhi_BasicSourceStreamHandlers1.__init__)


def test_siddhi_basicsourcestreamhandlers1_constructor_args():
    sig = inspect.signature(siddhi_BasicSourceStreamHandlers1.__init__)
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



def test_siddhi_functionbody_is_not_abstract():
    assert not inspect.isabstract(siddhi_FunctionBody)


def test_siddhi_functionbody_constructor_exists():
    assert callable(siddhi_FunctionBody.__init__)


def test_siddhi_functionbody_constructor_args():
    sig = inspect.signature(siddhi_FunctionBody.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_siddhi_functionbody_has_value():
    assert hasattr(siddhi_FunctionBody, "value")
    descriptor = None
    for klass in siddhi_FunctionBody.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_attributetype_is_not_abstract():
    assert not inspect.isabstract(siddhi_AttributeType)


def test_siddhi_attributetype_constructor_exists():
    assert callable(siddhi_AttributeType.__init__)


def test_siddhi_attributetype_constructor_args():
    sig = inspect.signature(siddhi_AttributeType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_languagename_is_not_abstract():
    assert not inspect.isabstract(siddhi_LanguageName)


def test_siddhi_languagename_constructor_exists():
    assert callable(siddhi_LanguageName.__init__)


def test_siddhi_languagename_constructor_args():
    sig = inspect.signature(siddhi_LanguageName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi_languagename_has_id():
    assert hasattr(siddhi_LanguageName, "id")
    descriptor = None
    for klass in siddhi_LanguageName.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_functionname_is_not_abstract():
    assert not inspect.isabstract(siddhi_FunctionName)


def test_siddhi_functionname_constructor_exists():
    assert callable(siddhi_FunctionName.__init__)


def test_siddhi_functionname_constructor_args():
    sig = inspect.signature(siddhi_FunctionName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi_functionname_has_id():
    assert hasattr(siddhi_FunctionName, "id")
    descriptor = None
    for klass in siddhi_FunctionName.__mro__:
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



def test_siddhi_anonymousstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_AnonymousStream)


def test_siddhi_anonymousstream_constructor_exists():
    assert callable(siddhi_AnonymousStream.__init__)


def test_siddhi_anonymousstream_constructor_args():
    sig = inspect.signature(siddhi_AnonymousStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_queryoutput_is_not_abstract():
    assert not inspect.isabstract(siddhi_QueryOutput)


def test_siddhi_queryoutput_constructor_exists():
    assert callable(siddhi_QueryOutput.__init__)


def test_siddhi_queryoutput_constructor_args():
    sig = inspect.signature(siddhi_QueryOutput.__init__)
    params = list(sig.parameters.keys())



def test_function_is_not_abstract():
    assert not inspect.isabstract(FUNCTION)


def test_function_constructor_exists():
    assert callable(FUNCTION.__init__)


def test_function_constructor_args():
    sig = inspect.signature(FUNCTION.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_stringvalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_StringValue)


def test_siddhi_stringvalue_constructor_exists():
    assert callable(siddhi_StringValue.__init__)


def test_siddhi_stringvalue_constructor_args():
    sig = inspect.signature(siddhi_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "sl" in params, "Missing parameter 'sl'"

def test_siddhi_stringvalue_has_sl():
    assert hasattr(siddhi_StringValue, "sl")
    descriptor = None
    for klass in siddhi_StringValue.__mro__:
        if "sl" in klass.__dict__:
            descriptor = klass.__dict__["sl"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_timevalue_is_not_abstract():
    assert not inspect.isabstract(siddhi_TimeValue)


def test_siddhi_timevalue_constructor_exists():
    assert callable(siddhi_TimeValue.__init__)


def test_siddhi_timevalue_constructor_args():
    sig = inspect.signature(siddhi_TimeValue.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_every_is_not_abstract():
    assert not inspect.isabstract(siddhi_EVERY)


def test_siddhi_every_constructor_exists():
    assert callable(siddhi_EVERY.__init__)


def test_siddhi_every_constructor_args():
    sig = inspect.signature(siddhi_EVERY.__init__)
    params = list(sig.parameters.keys())
    assert "every1" in params, "Missing parameter 'every1'"

def test_siddhi_every_has_every1():
    assert hasattr(siddhi_EVERY, "every1")
    descriptor = None
    for klass in siddhi_EVERY.__mro__:
        if "every1" in klass.__dict__:
            descriptor = klass.__dict__["every1"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_triggername_is_not_abstract():
    assert not inspect.isabstract(siddhi_TriggerName)


def test_siddhi_triggername_constructor_exists():
    assert callable(siddhi_TriggerName.__init__)


def test_siddhi_triggername_constructor_args():
    sig = inspect.signature(siddhi_TriggerName.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_siddhi_triggername_has_id():
    assert hasattr(siddhi_TriggerName, "id")
    descriptor = None
    for klass in siddhi_TriggerName.__mro__:
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



def test_siddhi_outputeventtype_is_not_abstract():
    assert not inspect.isabstract(siddhi_OutputEventType)


def test_siddhi_outputeventtype_constructor_exists():
    assert callable(siddhi_OutputEventType.__init__)


def test_siddhi_outputeventtype_constructor_args():
    sig = inspect.signature(siddhi_OutputEventType.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_functionoperation_is_not_abstract():
    assert not inspect.isabstract(siddhi_FunctionOperation)


def test_siddhi_functionoperation_constructor_exists():
    assert callable(siddhi_FunctionOperation.__init__)


def test_siddhi_functionoperation_constructor_args():
    sig = inspect.signature(siddhi_FunctionOperation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_appannotation_is_not_abstract():
    assert not inspect.isabstract(siddhi_AppAnnotation)


def test_siddhi_appannotation_constructor_exists():
    assert callable(siddhi_AppAnnotation.__init__)


def test_siddhi_appannotation_constructor_args():
    sig = inspect.signature(siddhi_AppAnnotation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_executionplan_is_not_abstract():
    assert not inspect.isabstract(siddhi_ExecutionPlan)


def test_siddhi_executionplan_constructor_exists():
    assert callable(siddhi_ExecutionPlan.__init__)


def test_siddhi_executionplan_constructor_args():
    sig = inspect.signature(siddhi_ExecutionPlan.__init__)
    params = list(sig.parameters.keys())



def test_table_is_not_abstract():
    assert not inspect.isabstract(TABLE)


def test_table_constructor_exists():
    assert callable(TABLE.__init__)


def test_table_constructor_args():
    sig = inspect.signature(TABLE.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_features_is_not_abstract():
    assert not inspect.isabstract(siddhi_Features)


def test_siddhi_features_constructor_exists():
    assert callable(siddhi_Features.__init__)


def test_siddhi_features_constructor_args():
    sig = inspect.signature(siddhi_Features.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_source1_is_not_abstract():
    assert not inspect.isabstract(siddhi_Source1)


def test_siddhi_source1_constructor_exists():
    assert callable(siddhi_Source1.__init__)


def test_siddhi_source1_constructor_args():
    sig = inspect.signature(siddhi_Source1.__init__)
    params = list(sig.parameters.keys())
    assert "inner" in params, "Missing parameter 'inner'"

def test_siddhi_source1_has_inner():
    assert hasattr(siddhi_Source1, "inner")
    descriptor = None
    for klass in siddhi_Source1.__mro__:
        if "inner" in klass.__dict__:
            descriptor = klass.__dict__["inner"]
            break
    assert isinstance(descriptor, property)



def test_siddhi_annotation_is_not_abstract():
    assert not inspect.isabstract(siddhi_Annotation)


def test_siddhi_annotation_constructor_exists():
    assert callable(siddhi_Annotation.__init__)


def test_siddhi_annotation_constructor_args():
    sig = inspect.signature(siddhi_Annotation.__init__)
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



def test_siddhi_definitionstream_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionStream)


def test_siddhi_definitionstream_constructor_exists():
    assert callable(siddhi_DefinitionStream.__init__)


def test_siddhi_definitionstream_constructor_args():
    sig = inspect.signature(siddhi_DefinitionStream.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_definitiontable_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionTable)


def test_siddhi_definitiontable_constructor_exists():
    assert callable(siddhi_DefinitionTable.__init__)


def test_siddhi_definitiontable_constructor_args():
    sig = inspect.signature(siddhi_DefinitionTable.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_keyword_is_not_abstract():
    assert not inspect.isabstract(siddhi_Keyword)


def test_siddhi_keyword_constructor_exists():
    assert callable(siddhi_Keyword.__init__)


def test_siddhi_keyword_constructor_args():
    sig = inspect.signature(siddhi_Keyword.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_query_is_not_abstract():
    assert not inspect.isabstract(siddhi_Query)


def test_siddhi_query_constructor_exists():
    assert callable(siddhi_Query.__init__)


def test_siddhi_query_constructor_args():
    sig = inspect.signature(siddhi_Query.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_execpartition_is_not_abstract():
    assert not inspect.isabstract(siddhi_ExecPartition)


def test_siddhi_execpartition_constructor_exists():
    assert callable(siddhi_ExecPartition.__init__)


def test_siddhi_execpartition_constructor_args():
    sig = inspect.signature(siddhi_ExecPartition.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_executionelement_is_not_abstract():
    assert not inspect.isabstract(siddhi_ExecutionElement)


def test_siddhi_executionelement_constructor_exists():
    assert callable(siddhi_ExecutionElement.__init__)


def test_siddhi_executionelement_constructor_args():
    sig = inspect.signature(siddhi_ExecutionElement.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_definitionaggregation_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionAggregation)


def test_siddhi_definitionaggregation_constructor_exists():
    assert callable(siddhi_DefinitionAggregation.__init__)


def test_siddhi_definitionaggregation_constructor_args():
    sig = inspect.signature(siddhi_DefinitionAggregation.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_definitionfunction_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionFunction)


def test_siddhi_definitionfunction_constructor_exists():
    assert callable(siddhi_DefinitionFunction.__init__)


def test_siddhi_definitionfunction_constructor_args():
    sig = inspect.signature(siddhi_DefinitionFunction.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_definitiontrigger_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionTrigger)


def test_siddhi_definitiontrigger_constructor_exists():
    assert callable(siddhi_DefinitionTrigger.__init__)


def test_siddhi_definitiontrigger_constructor_args():
    sig = inspect.signature(siddhi_DefinitionTrigger.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_definitionwindow_is_not_abstract():
    assert not inspect.isabstract(siddhi_DefinitionWindow)


def test_siddhi_definitionwindow_constructor_exists():
    assert callable(siddhi_DefinitionWindow.__init__)


def test_siddhi_definitionwindow_constructor_args():
    sig = inspect.signature(siddhi_DefinitionWindow.__init__)
    params = list(sig.parameters.keys())



def test_siddhi_siddhiql_is_not_abstract():
    assert not inspect.isabstract(siddhi_SiddhiQL)


def test_siddhi_siddhiql_constructor_exists():
    assert callable(siddhi_SiddhiQL.__init__)


def test_siddhi_siddhiql_constructor_args():
    sig = inspect.signature(siddhi_SiddhiQL.__init__)
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
Name_strategy = st.builds(
    Name,
)
siddhi_L_strategy = st.builds(
    siddhi_L,
    l=
        safe_text
)
SignedLongValue_strategy = st.builds(
    SignedLongValue,
)
siddhi_LONG_LITERAL_strategy = st.builds(
    siddhi_LONG_LITERAL,
)
siddhi_F_strategy = st.builds(
    siddhi_F,
    f=
        safe_text
)
SignedFloatValue_strategy = st.builds(
    SignedFloatValue,
)
siddhi_FLOAT_LITERAL_strategy = st.builds(
    siddhi_FLOAT_LITERAL,
)
siddhi_D_strategy = st.builds(
    siddhi_D,
    d=
        safe_text
)
siddhi_E_strategy = st.builds(
    siddhi_E,
    e=
        safe_text
)
SignedDoubleValue_strategy = st.builds(
    SignedDoubleValue,
)
siddhi_DOUBLE_LITERAL_strategy = st.builds(
    siddhi_DOUBLE_LITERAL,
)
MILLISECONDS_strategy = st.builds(
    MILLISECONDS,
)
siddhi_FunctionId_strategy = st.builds(
    siddhi_FunctionId,
)
siddhi_FunctionNamespace_strategy = st.builds(
    siddhi_FunctionNamespace,
)
siddhi_SignedLongValue_strategy = st.builds(
    siddhi_SignedLongValue,
)
FALSE_strategy = st.builds(
    FALSE,
)
TRUE_strategy = st.builds(
    TRUE,
)
siddhi_AttributeList_strategy = st.builds(
    siddhi_AttributeList,
)
siddhi_FeaturesOrOutAttr_strategy = st.builds(
    siddhi_FeaturesOrOutAttr,
    name=
        safe_text
)
siddhi_FeaturesOrOutAttrReference_strategy = st.builds(
    siddhi_FeaturesOrOutAttrReference,
)
siddhi_SignedFloatValue_strategy = st.builds(
    siddhi_SignedFloatValue,
)
siddhi_SignedDoubleValue_strategy = st.builds(
    siddhi_SignedDoubleValue,
)
siddhi_BoolValue_strategy = st.builds(
    siddhi_BoolValue,
)
siddhi_AttributeNameReference_strategy = st.builds(
    siddhi_AttributeNameReference,
)
siddhi_Source1OrStandardStatefulSource_strategy = st.builds(
    siddhi_Source1OrStandardStatefulSource,
    name=
        safe_text
)
PatternCollectionStatefulSource_strategy = st.builds(
    PatternCollectionStatefulSource,
)
SequenceCollectionStatefulSource_strategy = st.builds(
    SequenceCollectionStatefulSource,
)
siddhi_Literal_strategy = st.builds(
    siddhi_Literal,
)
MathDivmulOperation_strategy = st.builds(
    MathDivmulOperation,
)
siddhi_MathOtherOperations_strategy = st.builds(
    siddhi_MathOtherOperations,
)
MathAddsubOperation_strategy = st.builds(
    MathAddsubOperation,
)
siddhi_MathDivmulOperation_strategy = st.builds(
    siddhi_MathDivmulOperation,
    devide=
        safe_text,
    multiply=
        safe_text,
    mod=
        safe_text
)
siddhi_SourceOrEventReference_strategy = st.builds(
    siddhi_SourceOrEventReference,
)
SetAssignment_strategy = st.builds(
    SetAssignment,
)
siddhi_ConstantValue_strategy = st.builds(
    siddhi_ConstantValue,
    siv=
        safe_text
)
siddhi_StreamReference_strategy = st.builds(
    siddhi_StreamReference,
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
siddhi_NullCheck_strategy = st.builds(
    siddhi_NullCheck,
)
siddhi_BasicSourceStreamHandlers_strategy = st.builds(
    siddhi_BasicSourceStreamHandlers,
)
MathOperation_strategy = st.builds(
    MathOperation,
)
siddhi_MathAddsubOperation_strategy = st.builds(
    siddhi_MathAddsubOperation,
    add=
        safe_text,
    substract=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
siddhi_MathOperation_strategy = st.builds(
    siddhi_MathOperation,
)
siddhi_StreamFunction_strategy = st.builds(
    siddhi_StreamFunction,
)
siddhi_Filter_strategy = st.builds(
    siddhi_Filter,
)
siddhi_BasicSourceStreamHandler_strategy = st.builds(
    siddhi_BasicSourceStreamHandler,
)
siddhi_MathGtLtOperation_strategy = st.builds(
    siddhi_MathGtLtOperation,
    lt_eq=
        safe_text,
    gt=
        safe_text,
    gt_eq=
        safe_text,
    lt=
        safe_text
)
siddhi_MathInOperation_strategy = st.builds(
    siddhi_MathInOperation,
)
siddhi_NotOperation_strategy = st.builds(
    siddhi_NotOperation,
)
siddhi_MathEqualOperation_strategy = st.builds(
    siddhi_MathEqualOperation,
    not_eq=
        safe_text,
    eq=
        safe_text
)
siddhi_MINUTES_strategy = st.builds(
    siddhi_MINUTES,
    minutes=
        safe_text,
    minute=
        safe_text,
    min=
        safe_text
)
siddhi_HOURS_strategy = st.builds(
    siddhi_HOURS,
    hours=
        safe_text,
    hour=
        safe_text
)
siddhi_DAYS_strategy = st.builds(
    siddhi_DAYS,
    days=
        safe_text,
    day=
        safe_text
)
siddhi_WEEKS_strategy = st.builds(
    siddhi_WEEKS,
    weeks=
        safe_text,
    week=
        safe_text
)
siddhi_MONTHS_strategy = st.builds(
    siddhi_MONTHS,
    month=
        safe_text,
    months=
        safe_text
)
siddhi_MathLogicalOperation_strategy = st.builds(
    siddhi_MathLogicalOperation,
)
RightAbsentSequenceSource_strategy = st.builds(
    RightAbsentSequenceSource,
)
siddhi_RightAbsentSequenceSource1_strategy = st.builds(
    siddhi_RightAbsentSequenceSource1,
)
LeftAbsentSequenceSource_strategy = st.builds(
    LeftAbsentSequenceSource,
)
siddhi_LeftAbsentSequenceSource1_strategy = st.builds(
    siddhi_LeftAbsentSequenceSource1,
)
siddhi_TRUE_strategy = st.builds(
    siddhi_TRUE,
    tr=
        safe_text
)
siddhi_FALSE_strategy = st.builds(
    siddhi_FALSE,
    fals=
        safe_text
)
siddhi_MILLISECONDS_strategy = st.builds(
    siddhi_MILLISECONDS,
    millisecond=
        safe_text,
    millisec=
        safe_text,
    milliseconds=
        safe_text
)
siddhi_SECONDS_strategy = st.builds(
    siddhi_SECONDS,
    seconds=
        safe_text,
    sec=
        safe_text,
    second=
        safe_text
)
siddhi_OUTER_strategy = st.builds(
    siddhi_OUTER,
    outer=
        safe_text
)
siddhi_INNER_strategy = st.builds(
    siddhi_INNER,
    inner=
        safe_text
)
siddhi_JOIN_strategy = st.builds(
    siddhi_JOIN,
    join=
        safe_text
)
siddhi_FULL_strategy = st.builds(
    siddhi_FULL,
    full=
        safe_text
)
siddhi_RIGHT_strategy = st.builds(
    siddhi_RIGHT,
    right=
        safe_text
)
siddhi_LEFT_strategy = st.builds(
    siddhi_LEFT,
    left=
        safe_text
)
siddhi_WITHIN_strategy = st.builds(
    siddhi_WITHIN,
    within=
        safe_text
)
siddhi_YEARS_strategy = st.builds(
    siddhi_YEARS,
    year=
        safe_text,
    years=
        safe_text
)
siddhi_PER_strategy = st.builds(
    siddhi_PER,
    per=
        safe_text
)
siddhi_SET_strategy = st.builds(
    siddhi_SET,
    set=
        safe_text
)
siddhi_AGGREGATE_strategy = st.builds(
    siddhi_AGGREGATE,
    agrregate=
        safe_text
)
siddhi_AGGREGATION_strategy = st.builds(
    siddhi_AGGREGATION,
    aggre=
        safe_text
)
siddhi_WITH_strategy = st.builds(
    siddhi_WITH,
    wi=
        safe_text
)
siddhi_PARTITION_strategy = st.builds(
    siddhi_PARTITION,
    partition=
        safe_text
)
siddhi_END_strategy = st.builds(
    siddhi_END,
    end=
        safe_text
)
siddhi_UPDATE_strategy = st.builds(
    siddhi_UPDATE,
    update=
        safe_text
)
siddhi_FOR_strategy = st.builds(
    siddhi_FOR,
    for_=
        safe_text
)
siddhi_DELETE_strategy = st.builds(
    siddhi_DELETE,
    delete=
        safe_text
)
siddhi_PLAN_strategy = st.builds(
    siddhi_PLAN,
    plan=
        safe_text
)
siddhi_BEGIN_strategy = st.builds(
    siddhi_BEGIN,
    begin=
        safe_text
)
siddhi_INTO_strategy = st.builds(
    siddhi_INTO,
    into=
        safe_text
)
siddhi_INSERT_strategy = st.builds(
    siddhi_INSERT,
    insert=
        safe_text
)
siddhi_FIRST_strategy = st.builds(
    siddhi_FIRST,
    first=
        safe_text
)
siddhi_SNAPSHOT_strategy = st.builds(
    siddhi_SNAPSHOT,
    snapshot=
        safe_text
)
siddhi_HAVING_strategy = st.builds(
    siddhi_HAVING,
    having=
        safe_text
)
siddhi_BY_strategy = st.builds(
    siddhi_BY,
    by=
        safe_text
)
siddhi_GROUP_strategy = st.builds(
    siddhi_GROUP,
    group=
        safe_text
)
siddhi_SELECT_strategy = st.builds(
    siddhi_SELECT,
    select=
        safe_text
)
siddhi_DOUBLE_strategy = st.builds(
    siddhi_DOUBLE,
    double=
        safe_text
)
siddhi_LONG_strategy = st.builds(
    siddhi_LONG,
    long=
        safe_text
)
siddhi_INTS_strategy = st.builds(
    siddhi_INTS,
    int=
        safe_text
)
siddhi_STRINGS_strategy = st.builds(
    siddhi_STRINGS,
    string=
        safe_text
)
siddhi_OUTPUT_strategy = st.builds(
    siddhi_OUTPUT,
    output=
        safe_text
)
siddhi_WINDOW_strategy = st.builds(
    siddhi_WINDOW,
    window=
        safe_text
)
siddhi_TABLE_strategy = st.builds(
    siddhi_TABLE,
    table=
        safe_text
)
siddhi_FROM_strategy = st.builds(
    siddhi_FROM,
    from_=
        safe_text
)
siddhi_RETURN_strategy = st.builds(
    siddhi_RETURN,
    return_=
        safe_text
)
siddhi_FUNCTION_strategy = st.builds(
    siddhi_FUNCTION,
    function=
        safe_text
)
siddhi_AT_strategy = st.builds(
    siddhi_AT,
    at=
        safe_text
)
siddhi_TRIGGER_strategy = st.builds(
    siddhi_TRIGGER,
    trigger=
        safe_text
)
siddhi_NULL_strategy = st.builds(
    siddhi_NULL,
    null=
        safe_text
)
siddhi_IS_strategy = st.builds(
    siddhi_IS,
    is_=
        safe_text
)
siddhi_LAST_strategy = st.builds(
    siddhi_LAST,
    last=
        safe_text
)
siddhi_CURRENT_strategy = st.builds(
    siddhi_CURRENT,
    currt=
        safe_text
)
siddhi_EXPIRED_strategy = st.builds(
    siddhi_EXPIRED,
    expired=
        safe_text
)
siddhi_RAW_strategy = st.builds(
    siddhi_RAW,
    raw=
        safe_text
)
siddhi_EVENTS_strategy = st.builds(
    siddhi_EVENTS,
    events=
        safe_text
)
siddhi_ALL_strategy = st.builds(
    siddhi_ALL,
    all=
        safe_text
)
siddhi_OBJECT_strategy = st.builds(
    siddhi_OBJECT,
    object=
        safe_text
)
siddhi_BOOL_strategy = st.builds(
    siddhi_BOOL,
    bool=
        safe_text
)
siddhi_FLOAT_strategy = st.builds(
    siddhi_FLOAT,
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
siddhi_DEFINE_strategy = st.builds(
    siddhi_DEFINE,
    define=
        safe_text
)
siddhi_STREAM_strategy = st.builds(
    siddhi_STREAM,
    str=
        safe_text
)
AppAnnotation_strategy = st.builds(
    AppAnnotation,
)
siddhi_APP_strategy = st.builds(
    siddhi_APP,
    ap=
        safe_text
)
siddhi_IN_strategy = st.builds(
    siddhi_IN,
    in_=
        safe_text
)
RightAbsentPatternSource_strategy = st.builds(
    RightAbsentPatternSource,
)
siddhi_RightAbsentPatternSource1_strategy = st.builds(
    siddhi_RightAbsentPatternSource1,
    fb=
        safe_text
)
LeftAbsentPatternSource_strategy = st.builds(
    LeftAbsentPatternSource,
)
siddhi_LeftAbsentPatternSource1_strategy = st.builds(
    siddhi_LeftAbsentPatternSource1,
    fb=
        safe_text
)
EveryAbsentPatternSource_strategy = st.builds(
    EveryAbsentPatternSource,
)
LogicalAbsentStatefulSource_strategy = st.builds(
    LogicalAbsentStatefulSource,
)
siddhi_MillisecondValue_strategy = st.builds(
    siddhi_MillisecondValue,
)
siddhi_UNIDIRECTIONAL_strategy = st.builds(
    siddhi_UNIDIRECTIONAL,
    unidirectional=
        safe_text
)
siddhi_JoinSource_strategy = st.builds(
    siddhi_JoinSource,
)
StandardStream_strategy = st.builds(
    StandardStream,
)
JoinSource_strategy = st.builds(
    JoinSource,
)
siddhi_MainSource_strategy = st.builds(
    siddhi_MainSource,
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
siddhi_joins_strategy = st.builds(
    siddhi_joins,
)
siddhi_Per1_strategy = st.builds(
    siddhi_Per1,
)
siddhi_WithinTimeRange_strategy = st.builds(
    siddhi_WithinTimeRange,
)
AbsentPatternSourceChain_strategy = st.builds(
    AbsentPatternSourceChain,
)
siddhi_EveryAbsentPatternSource_strategy = st.builds(
    siddhi_EveryAbsentPatternSource,
)
siddhi_RightAbsentPatternSource_strategy = st.builds(
    siddhi_RightAbsentPatternSource,
    fb2=
        safe_text
)
siddhi_LeftAbsentPatternSource_strategy = st.builds(
    siddhi_LeftAbsentPatternSource,
    fb1=
        safe_text
)
siddhi_PatternCollectionStatefulSource_strategy = st.builds(
    siddhi_PatternCollectionStatefulSource,
)
siddhi_PatternSource_strategy = st.builds(
    siddhi_PatternSource,
)
siddhi_BasicSource_strategy = st.builds(
    siddhi_BasicSource,
)
siddhi_NOT_strategy = st.builds(
    siddhi_NOT,
    not1=
        safe_text
)
siddhi_Collect_strategy = st.builds(
    siddhi_Collect,
    start=
        safe_text,
    end=
        safe_text
)
siddhi_AND_strategy = st.builds(
    siddhi_AND,
    and_=
        safe_text
)
SequenceSource_strategy = st.builds(
    SequenceSource,
)
siddhi_LogicalStatefulSource_strategy = st.builds(
    siddhi_LogicalStatefulSource,
)
siddhi_LogicalAbsentStatefulSource_strategy = st.builds(
    siddhi_LogicalAbsentStatefulSource,
)
siddhi_SequenceCollectionStatefulSource_strategy = st.builds(
    siddhi_SequenceCollectionStatefulSource,
)
SequenceSourceChain_strategy = st.builds(
    SequenceSourceChain,
)
siddhi_PatternSourceChain_strategy = st.builds(
    siddhi_PatternSourceChain,
    op=
        safe_text
)
PatternStream_strategy = st.builds(
    PatternStream,
)
siddhi_AbsentPatternSourceChain_strategy = st.builds(
    siddhi_AbsentPatternSourceChain,
)
siddhi_EveryPatternSourceChain_strategy = st.builds(
    siddhi_EveryPatternSourceChain,
    op=
        safe_text
)
siddhi_RightAbsentSequenceSource_strategy = st.builds(
    siddhi_RightAbsentSequenceSource,
    cp=
        safe_text,
    comma=
        safe_text,
    comm=
        safe_text,
    op=
        safe_text
)
siddhi_LeftAbsentSequenceSource_strategy = st.builds(
    siddhi_LeftAbsentSequenceSource,
    op=
        safe_text,
    comma=
        safe_text,
    comm=
        safe_text,
    cp=
        safe_text
)
siddhi_BasicAbsentPatternSource_strategy = st.builds(
    siddhi_BasicAbsentPatternSource,
)
siddhi_EObject_strategy = st.builds(
    siddhi_EObject,
)
HAVING_strategy = st.builds(
    HAVING,
)
GROUP_strategy = st.builds(
    GROUP,
)
siddhi_HavingExpr_strategy = st.builds(
    siddhi_HavingExpr,
)
siddhi_AbsentSequenceSourceChain_strategy = st.builds(
    siddhi_AbsentSequenceSourceChain,
)
siddhi_SequenceSourceChain_strategy = st.builds(
    siddhi_SequenceSourceChain,
    op=
        safe_text
)
siddhi_WithinTime_strategy = st.builds(
    siddhi_WithinTime,
)
siddhi_SequenceSource_strategy = st.builds(
    siddhi_SequenceSource,
)
siddhi_EveryAbsentSequenceSourceChain_strategy = st.builds(
    siddhi_EveryAbsentSequenceSourceChain,
)
siddhi_EverySequenceSourceChain_strategy = st.builds(
    siddhi_EverySequenceSourceChain,
)
siddhi_PatternStream_strategy = st.builds(
    siddhi_PatternStream,
)
siddhi_SequenceStream_strategy = st.builds(
    siddhi_SequenceStream,
)
siddhi_JoinStream_strategy = st.builds(
    siddhi_JoinStream,
)
siddhi_Attribute_strategy = st.builds(
    siddhi_Attribute,
)
siddhi_OutputAttribute_strategy = st.builds(
    siddhi_OutputAttribute,
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
siddhi_AttributeIndex_strategy = st.builds(
    siddhi_AttributeIndex,
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
siddhi_OutputRateType_strategy = st.builds(
    siddhi_OutputRateType,
)
siddhi_SetAssignment_strategy = st.builds(
    siddhi_SetAssignment,
)
SET_strategy = st.builds(
    SET,
)
siddhi_SetClause_strategy = st.builds(
    siddhi_SetClause,
)
siddhi_OR_strategy = st.builds(
    siddhi_OR,
    or_=
        safe_text
)
siddhi_ConditionRange_strategy = st.builds(
    siddhi_ConditionRange,
)
siddhi_OF_strategy = st.builds(
    siddhi_OF,
    of=
        safe_text
)
PartitionWithStream_strategy = st.builds(
    PartitionWithStream,
)
siddhi_ConditionRanges_strategy = st.builds(
    siddhi_ConditionRanges,
)
siddhi_ON_strategy = st.builds(
    siddhi_ON,
    on=
        safe_text
)
siddhi_Target_strategy = st.builds(
    siddhi_Target,
)
UPDATE_strategy = st.builds(
    UPDATE,
)
FOR_strategy = st.builds(
    FOR,
)
siddhi_ForTime_strategy = st.builds(
    siddhi_ForTime,
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
siddhi_QuerySection_strategy = st.builds(
    siddhi_QuerySection,
)
siddhi_QueryInput_strategy = st.builds(
    siddhi_QueryInput,
)
siddhi_AS_strategy = st.builds(
    siddhi_AS,
    a=
        safe_text
)
siddhi_Expression_strategy = st.builds(
    siddhi_Expression,
)
siddhi_PropertyValue_strategy = st.builds(
    siddhi_PropertyValue,
)
siddhi_PartitionWithStream_strategy = st.builds(
    siddhi_PartitionWithStream,
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
siddhi_StreamAlias_strategy = st.builds(
    siddhi_StreamAlias,
)
siddhi_StandardStatefulSource_strategy = st.builds(
    siddhi_StandardStatefulSource,
    zero_or_more=
        safe_text,
    zero_or_one=
        safe_text,
    one_or_more=
        safe_text
)
siddhi_Source_strategy = st.builds(
    siddhi_Source,
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
siddhi_OutAttr_strategy = st.builds(
    siddhi_OutAttr,
)
siddhi_PropertySeparator_strategy = st.builds(
    siddhi_PropertySeparator,
)
siddhi_AttributeReference_strategy = st.builds(
    siddhi_AttributeReference,
    name=
        safe_text,
    hash2=
        safe_text,
    hash1=
        safe_text
)
siddhi_GroupByQuerySelection_strategy = st.builds(
    siddhi_GroupByQuerySelection,
)
siddhi_StandardStream_strategy = st.builds(
    siddhi_StandardStream,
)
BY_strategy = st.builds(
    BY,
)
siddhi_GroupBy_strategy = st.builds(
    siddhi_GroupBy,
)
siddhi_PropertyName_strategy = st.builds(
    siddhi_PropertyName,
)
siddhi_AnnotationElement_strategy = st.builds(
    siddhi_AnnotationElement,
)
siddhi_Name_strategy = st.builds(
    siddhi_Name,
    na=
        safe_text
)
YEARS_strategy = st.builds(
    YEARS,
)
siddhi_YearValue_strategy = st.builds(
    siddhi_YearValue,
)
MONTHS_strategy = st.builds(
    MONTHS,
)
siddhi_MonthValue_strategy = st.builds(
    siddhi_MonthValue,
)
WEEKS_strategy = st.builds(
    WEEKS,
)
siddhi_WeekValue_strategy = st.builds(
    siddhi_WeekValue,
)
DAYS_strategy = st.builds(
    DAYS,
)
siddhi_DayValue_strategy = st.builds(
    siddhi_DayValue,
)
HOURS_strategy = st.builds(
    HOURS,
)
siddhi_HourValue_strategy = st.builds(
    siddhi_HourValue,
)
MINUTES_strategy = st.builds(
    MINUTES,
)
siddhi_MinuteValue_strategy = st.builds(
    siddhi_MinuteValue,
)
SECONDS_strategy = st.builds(
    SECONDS,
)
siddhi_SecondValue_strategy = st.builds(
    siddhi_SecondValue,
)
AggregationTime_strategy = st.builds(
    AggregationTime,
)
siddhi_AggregationTimeRange_strategy = st.builds(
    siddhi_AggregationTimeRange,
)
siddhi_AggregationTimeInterval_strategy = st.builds(
    siddhi_AggregationTimeInterval,
)
siddhi_AggregationTimeDuration_strategy = st.builds(
    siddhi_AggregationTimeDuration,
)
siddhi_AggregationTime_strategy = st.builds(
    siddhi_AggregationTime,
)
OUTPUT_strategy = st.builds(
    OUTPUT,
)
siddhi_OutputRate_strategy = st.builds(
    siddhi_OutputRate,
)
WINDOW_strategy = st.builds(
    WINDOW,
)
siddhi_Win_strategy = st.builds(
    siddhi_Win,
)
siddhi_BasicSourceStreamHandlers1_strategy = st.builds(
    siddhi_BasicSourceStreamHandlers1,
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
siddhi_FunctionBody_strategy = st.builds(
    siddhi_FunctionBody,
    value=
        safe_text
)
siddhi_AttributeType_strategy = st.builds(
    siddhi_AttributeType,
)
siddhi_LanguageName_strategy = st.builds(
    siddhi_LanguageName,
    id=
        safe_text
)
siddhi_FunctionName_strategy = st.builds(
    siddhi_FunctionName,
    id=
        safe_text
)
RETURN_strategy = st.builds(
    RETURN,
)
siddhi_AnonymousStream_strategy = st.builds(
    siddhi_AnonymousStream,
)
siddhi_QueryOutput_strategy = st.builds(
    siddhi_QueryOutput,
)
FUNCTION_strategy = st.builds(
    FUNCTION,
)
siddhi_StringValue_strategy = st.builds(
    siddhi_StringValue,
    sl=
        safe_text
)
siddhi_TimeValue_strategy = st.builds(
    siddhi_TimeValue,
)
siddhi_EVERY_strategy = st.builds(
    siddhi_EVERY,
    every1=
        safe_text
)
siddhi_TriggerName_strategy = st.builds(
    siddhi_TriggerName,
    id=
        safe_text
)
AT_strategy = st.builds(
    AT,
)
TRIGGER_strategy = st.builds(
    TRIGGER,
)
siddhi_OutputEventType_strategy = st.builds(
    siddhi_OutputEventType,
)
siddhi_FunctionOperation_strategy = st.builds(
    siddhi_FunctionOperation,
)
siddhi_AppAnnotation_strategy = st.builds(
    siddhi_AppAnnotation,
)
siddhi_ExecutionPlan_strategy = st.builds(
    siddhi_ExecutionPlan,
)
TABLE_strategy = st.builds(
    TABLE,
)
siddhi_Features_strategy = st.builds(
    siddhi_Features,
)
siddhi_Source1_strategy = st.builds(
    siddhi_Source1,
    inner=
        safe_text
)
siddhi_Annotation_strategy = st.builds(
    siddhi_Annotation,
)
STREAM_strategy = st.builds(
    STREAM,
)
DEFINE_strategy = st.builds(
    DEFINE,
)
siddhi_DefinitionStream_strategy = st.builds(
    siddhi_DefinitionStream,
)
siddhi_DefinitionTable_strategy = st.builds(
    siddhi_DefinitionTable,
)
siddhi_Keyword_strategy = st.builds(
    siddhi_Keyword,
)
siddhi_Query_strategy = st.builds(
    siddhi_Query,
)
siddhi_ExecPartition_strategy = st.builds(
    siddhi_ExecPartition,
)
siddhi_ExecutionElement_strategy = st.builds(
    siddhi_ExecutionElement,
)
siddhi_DefinitionAggregation_strategy = st.builds(
    siddhi_DefinitionAggregation,
)
siddhi_DefinitionFunction_strategy = st.builds(
    siddhi_DefinitionFunction,
)
siddhi_DefinitionTrigger_strategy = st.builds(
    siddhi_DefinitionTrigger,
)
siddhi_DefinitionWindow_strategy = st.builds(
    siddhi_DefinitionWindow,
)
siddhi_SiddhiQL_strategy = st.builds(
    siddhi_SiddhiQL,
)

@given(instance=Name_strategy)
@settings(max_examples=50)
def test_name_instantiation(instance):
    assert isinstance(instance, Name)

@given(instance=siddhi_L_strategy)
@settings(max_examples=50)
def test_siddhi_l_instantiation(instance):
    assert isinstance(instance, siddhi_L)



@given(instance=siddhi_L_strategy)
def test_siddhi_l_l_setter(instance):
    original = instance.l
    instance.l = original
    assert instance.l == original

@given(instance=SignedLongValue_strategy)
@settings(max_examples=50)
def test_signedlongvalue_instantiation(instance):
    assert isinstance(instance, SignedLongValue)

@given(instance=siddhi_LONG_LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi_long_literal_instantiation(instance):
    assert isinstance(instance, siddhi_LONG_LITERAL)

@given(instance=siddhi_F_strategy)
@settings(max_examples=50)
def test_siddhi_f_instantiation(instance):
    assert isinstance(instance, siddhi_F)



@given(instance=siddhi_F_strategy)
def test_siddhi_f_f_setter(instance):
    original = instance.f
    instance.f = original
    assert instance.f == original

@given(instance=SignedFloatValue_strategy)
@settings(max_examples=50)
def test_signedfloatvalue_instantiation(instance):
    assert isinstance(instance, SignedFloatValue)

@given(instance=siddhi_FLOAT_LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi_float_literal_instantiation(instance):
    assert isinstance(instance, siddhi_FLOAT_LITERAL)

@given(instance=siddhi_D_strategy)
@settings(max_examples=50)
def test_siddhi_d_instantiation(instance):
    assert isinstance(instance, siddhi_D)



@given(instance=siddhi_D_strategy)
def test_siddhi_d_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=siddhi_E_strategy)
@settings(max_examples=50)
def test_siddhi_e_instantiation(instance):
    assert isinstance(instance, siddhi_E)



@given(instance=siddhi_E_strategy)
def test_siddhi_e_e_setter(instance):
    original = instance.e
    instance.e = original
    assert instance.e == original

@given(instance=SignedDoubleValue_strategy)
@settings(max_examples=50)
def test_signeddoublevalue_instantiation(instance):
    assert isinstance(instance, SignedDoubleValue)

@given(instance=siddhi_DOUBLE_LITERAL_strategy)
@settings(max_examples=50)
def test_siddhi_double_literal_instantiation(instance):
    assert isinstance(instance, siddhi_DOUBLE_LITERAL)

@given(instance=MILLISECONDS_strategy)
@settings(max_examples=50)
def test_milliseconds_instantiation(instance):
    assert isinstance(instance, MILLISECONDS)

@given(instance=siddhi_FunctionId_strategy)
@settings(max_examples=50)
def test_siddhi_functionid_instantiation(instance):
    assert isinstance(instance, siddhi_FunctionId)

@given(instance=siddhi_FunctionNamespace_strategy)
@settings(max_examples=50)
def test_siddhi_functionnamespace_instantiation(instance):
    assert isinstance(instance, siddhi_FunctionNamespace)

@given(instance=siddhi_SignedLongValue_strategy)
@settings(max_examples=50)
def test_siddhi_signedlongvalue_instantiation(instance):
    assert isinstance(instance, siddhi_SignedLongValue)

@given(instance=FALSE_strategy)
@settings(max_examples=50)
def test_false_instantiation(instance):
    assert isinstance(instance, FALSE)

@given(instance=TRUE_strategy)
@settings(max_examples=50)
def test_true_instantiation(instance):
    assert isinstance(instance, TRUE)

@given(instance=siddhi_AttributeList_strategy)
@settings(max_examples=50)
def test_siddhi_attributelist_instantiation(instance):
    assert isinstance(instance, siddhi_AttributeList)

@given(instance=siddhi_FeaturesOrOutAttr_strategy)
@settings(max_examples=50)
def test_siddhi_featuresoroutattr_instantiation(instance):
    assert isinstance(instance, siddhi_FeaturesOrOutAttr)



@given(instance=siddhi_FeaturesOrOutAttr_strategy)
def test_siddhi_featuresoroutattr_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=siddhi_FeaturesOrOutAttrReference_strategy)
@settings(max_examples=50)
def test_siddhi_featuresoroutattrreference_instantiation(instance):
    assert isinstance(instance, siddhi_FeaturesOrOutAttrReference)

@given(instance=siddhi_SignedFloatValue_strategy)
@settings(max_examples=50)
def test_siddhi_signedfloatvalue_instantiation(instance):
    assert isinstance(instance, siddhi_SignedFloatValue)

@given(instance=siddhi_SignedDoubleValue_strategy)
@settings(max_examples=50)
def test_siddhi_signeddoublevalue_instantiation(instance):
    assert isinstance(instance, siddhi_SignedDoubleValue)

@given(instance=siddhi_BoolValue_strategy)
@settings(max_examples=50)
def test_siddhi_boolvalue_instantiation(instance):
    assert isinstance(instance, siddhi_BoolValue)

@given(instance=siddhi_AttributeNameReference_strategy)
@settings(max_examples=50)
def test_siddhi_attributenamereference_instantiation(instance):
    assert isinstance(instance, siddhi_AttributeNameReference)

@given(instance=siddhi_Source1OrStandardStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_source1orstandardstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_Source1OrStandardStatefulSource)



@given(instance=siddhi_Source1OrStandardStatefulSource_strategy)
def test_siddhi_source1orstandardstatefulsource_name_setter(instance):
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

@given(instance=siddhi_Literal_strategy)
@settings(max_examples=50)
def test_siddhi_literal_instantiation(instance):
    assert isinstance(instance, siddhi_Literal)

@given(instance=MathDivmulOperation_strategy)
@settings(max_examples=50)
def test_mathdivmuloperation_instantiation(instance):
    assert isinstance(instance, MathDivmulOperation)

@given(instance=siddhi_MathOtherOperations_strategy)
@settings(max_examples=50)
def test_siddhi_mathotheroperations_instantiation(instance):
    assert isinstance(instance, siddhi_MathOtherOperations)

@given(instance=MathAddsubOperation_strategy)
@settings(max_examples=50)
def test_mathaddsuboperation_instantiation(instance):
    assert isinstance(instance, MathAddsubOperation)

@given(instance=siddhi_MathDivmulOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathdivmuloperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathDivmulOperation)



@given(instance=siddhi_MathDivmulOperation_strategy)
def test_siddhi_mathdivmuloperation_devide_setter(instance):
    original = instance.devide
    instance.devide = original
    assert instance.devide == original



@given(instance=siddhi_MathDivmulOperation_strategy)
def test_siddhi_mathdivmuloperation_multiply_setter(instance):
    original = instance.multiply
    instance.multiply = original
    assert instance.multiply == original



@given(instance=siddhi_MathDivmulOperation_strategy)
def test_siddhi_mathdivmuloperation_mod_setter(instance):
    original = instance.mod
    instance.mod = original
    assert instance.mod == original

@given(instance=siddhi_SourceOrEventReference_strategy)
@settings(max_examples=50)
def test_siddhi_sourceoreventreference_instantiation(instance):
    assert isinstance(instance, siddhi_SourceOrEventReference)

@given(instance=SetAssignment_strategy)
@settings(max_examples=50)
def test_setassignment_instantiation(instance):
    assert isinstance(instance, SetAssignment)

@given(instance=siddhi_ConstantValue_strategy)
@settings(max_examples=50)
def test_siddhi_constantvalue_instantiation(instance):
    assert isinstance(instance, siddhi_ConstantValue)



@given(instance=siddhi_ConstantValue_strategy)
def test_siddhi_constantvalue_siv_setter(instance):
    original = instance.siv
    instance.siv = original
    assert instance.siv == original

@given(instance=siddhi_StreamReference_strategy)
@settings(max_examples=50)
def test_siddhi_streamreference_instantiation(instance):
    assert isinstance(instance, siddhi_StreamReference)



@given(instance=siddhi_StreamReference_strategy)
def test_siddhi_streamreference_hash_setter(instance):
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

@given(instance=siddhi_NullCheck_strategy)
@settings(max_examples=50)
def test_siddhi_nullcheck_instantiation(instance):
    assert isinstance(instance, siddhi_NullCheck)

@given(instance=siddhi_BasicSourceStreamHandlers_strategy)
@settings(max_examples=50)
def test_siddhi_basicsourcestreamhandlers_instantiation(instance):
    assert isinstance(instance, siddhi_BasicSourceStreamHandlers)

@given(instance=MathOperation_strategy)
@settings(max_examples=50)
def test_mathoperation_instantiation(instance):
    assert isinstance(instance, MathOperation)

@given(instance=siddhi_MathAddsubOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathaddsuboperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathAddsubOperation)



@given(instance=siddhi_MathAddsubOperation_strategy)
def test_siddhi_mathaddsuboperation_add_setter(instance):
    original = instance.add
    instance.add = original
    assert instance.add == original



@given(instance=siddhi_MathAddsubOperation_strategy)
def test_siddhi_mathaddsuboperation_substract_setter(instance):
    original = instance.substract
    instance.substract = original
    assert instance.substract == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=siddhi_MathOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathoperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathOperation)

@given(instance=siddhi_StreamFunction_strategy)
@settings(max_examples=50)
def test_siddhi_streamfunction_instantiation(instance):
    assert isinstance(instance, siddhi_StreamFunction)

@given(instance=siddhi_Filter_strategy)
@settings(max_examples=50)
def test_siddhi_filter_instantiation(instance):
    assert isinstance(instance, siddhi_Filter)

@given(instance=siddhi_BasicSourceStreamHandler_strategy)
@settings(max_examples=50)
def test_siddhi_basicsourcestreamhandler_instantiation(instance):
    assert isinstance(instance, siddhi_BasicSourceStreamHandler)

@given(instance=siddhi_MathGtLtOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathgtltoperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathGtLtOperation)



@given(instance=siddhi_MathGtLtOperation_strategy)
def test_siddhi_mathgtltoperation_lt_eq_setter(instance):
    original = instance.lt_eq
    instance.lt_eq = original
    assert instance.lt_eq == original



@given(instance=siddhi_MathGtLtOperation_strategy)
def test_siddhi_mathgtltoperation_gt_setter(instance):
    original = instance.gt
    instance.gt = original
    assert instance.gt == original



@given(instance=siddhi_MathGtLtOperation_strategy)
def test_siddhi_mathgtltoperation_gt_eq_setter(instance):
    original = instance.gt_eq
    instance.gt_eq = original
    assert instance.gt_eq == original



@given(instance=siddhi_MathGtLtOperation_strategy)
def test_siddhi_mathgtltoperation_lt_setter(instance):
    original = instance.lt
    instance.lt = original
    assert instance.lt == original

@given(instance=siddhi_MathInOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathinoperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathInOperation)

@given(instance=siddhi_NotOperation_strategy)
@settings(max_examples=50)
def test_siddhi_notoperation_instantiation(instance):
    assert isinstance(instance, siddhi_NotOperation)

@given(instance=siddhi_MathEqualOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathequaloperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathEqualOperation)



@given(instance=siddhi_MathEqualOperation_strategy)
def test_siddhi_mathequaloperation_not_eq_setter(instance):
    original = instance.not_eq
    instance.not_eq = original
    assert instance.not_eq == original



@given(instance=siddhi_MathEqualOperation_strategy)
def test_siddhi_mathequaloperation_eq_setter(instance):
    original = instance.eq
    instance.eq = original
    assert instance.eq == original

@given(instance=siddhi_MINUTES_strategy)
@settings(max_examples=50)
def test_siddhi_minutes_instantiation(instance):
    assert isinstance(instance, siddhi_MINUTES)



@given(instance=siddhi_MINUTES_strategy)
def test_siddhi_minutes_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=siddhi_MINUTES_strategy)
def test_siddhi_minutes_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=siddhi_MINUTES_strategy)
def test_siddhi_minutes_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=siddhi_HOURS_strategy)
@settings(max_examples=50)
def test_siddhi_hours_instantiation(instance):
    assert isinstance(instance, siddhi_HOURS)



@given(instance=siddhi_HOURS_strategy)
def test_siddhi_hours_hours_setter(instance):
    original = instance.hours
    instance.hours = original
    assert instance.hours == original



@given(instance=siddhi_HOURS_strategy)
def test_siddhi_hours_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=siddhi_DAYS_strategy)
@settings(max_examples=50)
def test_siddhi_days_instantiation(instance):
    assert isinstance(instance, siddhi_DAYS)



@given(instance=siddhi_DAYS_strategy)
def test_siddhi_days_days_setter(instance):
    original = instance.days
    instance.days = original
    assert instance.days == original



@given(instance=siddhi_DAYS_strategy)
def test_siddhi_days_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=siddhi_WEEKS_strategy)
@settings(max_examples=50)
def test_siddhi_weeks_instantiation(instance):
    assert isinstance(instance, siddhi_WEEKS)



@given(instance=siddhi_WEEKS_strategy)
def test_siddhi_weeks_weeks_setter(instance):
    original = instance.weeks
    instance.weeks = original
    assert instance.weeks == original



@given(instance=siddhi_WEEKS_strategy)
def test_siddhi_weeks_week_setter(instance):
    original = instance.week
    instance.week = original
    assert instance.week == original

@given(instance=siddhi_MONTHS_strategy)
@settings(max_examples=50)
def test_siddhi_months_instantiation(instance):
    assert isinstance(instance, siddhi_MONTHS)



@given(instance=siddhi_MONTHS_strategy)
def test_siddhi_months_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=siddhi_MONTHS_strategy)
def test_siddhi_months_months_setter(instance):
    original = instance.months
    instance.months = original
    assert instance.months == original

@given(instance=siddhi_MathLogicalOperation_strategy)
@settings(max_examples=50)
def test_siddhi_mathlogicaloperation_instantiation(instance):
    assert isinstance(instance, siddhi_MathLogicalOperation)

@given(instance=RightAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_rightabsentsequencesource_instantiation(instance):
    assert isinstance(instance, RightAbsentSequenceSource)

@given(instance=siddhi_RightAbsentSequenceSource1_strategy)
@settings(max_examples=50)
def test_siddhi_rightabsentsequencesource1_instantiation(instance):
    assert isinstance(instance, siddhi_RightAbsentSequenceSource1)

@given(instance=LeftAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_leftabsentsequencesource_instantiation(instance):
    assert isinstance(instance, LeftAbsentSequenceSource)

@given(instance=siddhi_LeftAbsentSequenceSource1_strategy)
@settings(max_examples=50)
def test_siddhi_leftabsentsequencesource1_instantiation(instance):
    assert isinstance(instance, siddhi_LeftAbsentSequenceSource1)

@given(instance=siddhi_TRUE_strategy)
@settings(max_examples=50)
def test_siddhi_true_instantiation(instance):
    assert isinstance(instance, siddhi_TRUE)



@given(instance=siddhi_TRUE_strategy)
def test_siddhi_true_tr_setter(instance):
    original = instance.tr
    instance.tr = original
    assert instance.tr == original

@given(instance=siddhi_FALSE_strategy)
@settings(max_examples=50)
def test_siddhi_false_instantiation(instance):
    assert isinstance(instance, siddhi_FALSE)



@given(instance=siddhi_FALSE_strategy)
def test_siddhi_false_fals_setter(instance):
    original = instance.fals
    instance.fals = original
    assert instance.fals == original

@given(instance=siddhi_MILLISECONDS_strategy)
@settings(max_examples=50)
def test_siddhi_milliseconds_instantiation(instance):
    assert isinstance(instance, siddhi_MILLISECONDS)



@given(instance=siddhi_MILLISECONDS_strategy)
def test_siddhi_milliseconds_millisecond_setter(instance):
    original = instance.millisecond
    instance.millisecond = original
    assert instance.millisecond == original



@given(instance=siddhi_MILLISECONDS_strategy)
def test_siddhi_milliseconds_millisec_setter(instance):
    original = instance.millisec
    instance.millisec = original
    assert instance.millisec == original



@given(instance=siddhi_MILLISECONDS_strategy)
def test_siddhi_milliseconds_milliseconds_setter(instance):
    original = instance.milliseconds
    instance.milliseconds = original
    assert instance.milliseconds == original

@given(instance=siddhi_SECONDS_strategy)
@settings(max_examples=50)
def test_siddhi_seconds_instantiation(instance):
    assert isinstance(instance, siddhi_SECONDS)



@given(instance=siddhi_SECONDS_strategy)
def test_siddhi_seconds_seconds_setter(instance):
    original = instance.seconds
    instance.seconds = original
    assert instance.seconds == original



@given(instance=siddhi_SECONDS_strategy)
def test_siddhi_seconds_sec_setter(instance):
    original = instance.sec
    instance.sec = original
    assert instance.sec == original



@given(instance=siddhi_SECONDS_strategy)
def test_siddhi_seconds_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=siddhi_OUTER_strategy)
@settings(max_examples=50)
def test_siddhi_outer_instantiation(instance):
    assert isinstance(instance, siddhi_OUTER)



@given(instance=siddhi_OUTER_strategy)
def test_siddhi_outer_outer_setter(instance):
    original = instance.outer
    instance.outer = original
    assert instance.outer == original

@given(instance=siddhi_INNER_strategy)
@settings(max_examples=50)
def test_siddhi_inner_instantiation(instance):
    assert isinstance(instance, siddhi_INNER)



@given(instance=siddhi_INNER_strategy)
def test_siddhi_inner_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=siddhi_JOIN_strategy)
@settings(max_examples=50)
def test_siddhi_join_instantiation(instance):
    assert isinstance(instance, siddhi_JOIN)



@given(instance=siddhi_JOIN_strategy)
def test_siddhi_join_join_setter(instance):
    original = instance.join
    instance.join = original
    assert instance.join == original

@given(instance=siddhi_FULL_strategy)
@settings(max_examples=50)
def test_siddhi_full_instantiation(instance):
    assert isinstance(instance, siddhi_FULL)



@given(instance=siddhi_FULL_strategy)
def test_siddhi_full_full_setter(instance):
    original = instance.full
    instance.full = original
    assert instance.full == original

@given(instance=siddhi_RIGHT_strategy)
@settings(max_examples=50)
def test_siddhi_right_instantiation(instance):
    assert isinstance(instance, siddhi_RIGHT)



@given(instance=siddhi_RIGHT_strategy)
def test_siddhi_right_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=siddhi_LEFT_strategy)
@settings(max_examples=50)
def test_siddhi_left_instantiation(instance):
    assert isinstance(instance, siddhi_LEFT)



@given(instance=siddhi_LEFT_strategy)
def test_siddhi_left_left_setter(instance):
    original = instance.left
    instance.left = original
    assert instance.left == original

@given(instance=siddhi_WITHIN_strategy)
@settings(max_examples=50)
def test_siddhi_within_instantiation(instance):
    assert isinstance(instance, siddhi_WITHIN)



@given(instance=siddhi_WITHIN_strategy)
def test_siddhi_within_within_setter(instance):
    original = instance.within
    instance.within = original
    assert instance.within == original

@given(instance=siddhi_YEARS_strategy)
@settings(max_examples=50)
def test_siddhi_years_instantiation(instance):
    assert isinstance(instance, siddhi_YEARS)



@given(instance=siddhi_YEARS_strategy)
def test_siddhi_years_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=siddhi_YEARS_strategy)
def test_siddhi_years_years_setter(instance):
    original = instance.years
    instance.years = original
    assert instance.years == original

@given(instance=siddhi_PER_strategy)
@settings(max_examples=50)
def test_siddhi_per_instantiation(instance):
    assert isinstance(instance, siddhi_PER)



@given(instance=siddhi_PER_strategy)
def test_siddhi_per_per_setter(instance):
    original = instance.per
    instance.per = original
    assert instance.per == original

@given(instance=siddhi_SET_strategy)
@settings(max_examples=50)
def test_siddhi_set_instantiation(instance):
    assert isinstance(instance, siddhi_SET)



@given(instance=siddhi_SET_strategy)
def test_siddhi_set_set_setter(instance):
    original = instance.set
    instance.set = original
    assert instance.set == original

@given(instance=siddhi_AGGREGATE_strategy)
@settings(max_examples=50)
def test_siddhi_aggregate_instantiation(instance):
    assert isinstance(instance, siddhi_AGGREGATE)



@given(instance=siddhi_AGGREGATE_strategy)
def test_siddhi_aggregate_agrregate_setter(instance):
    original = instance.agrregate
    instance.agrregate = original
    assert instance.agrregate == original

@given(instance=siddhi_AGGREGATION_strategy)
@settings(max_examples=50)
def test_siddhi_aggregation_instantiation(instance):
    assert isinstance(instance, siddhi_AGGREGATION)



@given(instance=siddhi_AGGREGATION_strategy)
def test_siddhi_aggregation_aggre_setter(instance):
    original = instance.aggre
    instance.aggre = original
    assert instance.aggre == original

@given(instance=siddhi_WITH_strategy)
@settings(max_examples=50)
def test_siddhi_with_instantiation(instance):
    assert isinstance(instance, siddhi_WITH)



@given(instance=siddhi_WITH_strategy)
def test_siddhi_with_wi_setter(instance):
    original = instance.wi
    instance.wi = original
    assert instance.wi == original

@given(instance=siddhi_PARTITION_strategy)
@settings(max_examples=50)
def test_siddhi_partition_instantiation(instance):
    assert isinstance(instance, siddhi_PARTITION)



@given(instance=siddhi_PARTITION_strategy)
def test_siddhi_partition_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original

@given(instance=siddhi_END_strategy)
@settings(max_examples=50)
def test_siddhi_end_instantiation(instance):
    assert isinstance(instance, siddhi_END)



@given(instance=siddhi_END_strategy)
def test_siddhi_end_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=siddhi_UPDATE_strategy)
@settings(max_examples=50)
def test_siddhi_update_instantiation(instance):
    assert isinstance(instance, siddhi_UPDATE)



@given(instance=siddhi_UPDATE_strategy)
def test_siddhi_update_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original

@given(instance=siddhi_FOR_strategy)
@settings(max_examples=50)
def test_siddhi_for_instantiation(instance):
    assert isinstance(instance, siddhi_FOR)



@given(instance=siddhi_FOR_strategy)
def test_siddhi_for_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=siddhi_DELETE_strategy)
@settings(max_examples=50)
def test_siddhi_delete_instantiation(instance):
    assert isinstance(instance, siddhi_DELETE)



@given(instance=siddhi_DELETE_strategy)
def test_siddhi_delete_delete_setter(instance):
    original = instance.delete
    instance.delete = original
    assert instance.delete == original

@given(instance=siddhi_PLAN_strategy)
@settings(max_examples=50)
def test_siddhi_plan_instantiation(instance):
    assert isinstance(instance, siddhi_PLAN)



@given(instance=siddhi_PLAN_strategy)
def test_siddhi_plan_plan_setter(instance):
    original = instance.plan
    instance.plan = original
    assert instance.plan == original

@given(instance=siddhi_BEGIN_strategy)
@settings(max_examples=50)
def test_siddhi_begin_instantiation(instance):
    assert isinstance(instance, siddhi_BEGIN)



@given(instance=siddhi_BEGIN_strategy)
def test_siddhi_begin_begin_setter(instance):
    original = instance.begin
    instance.begin = original
    assert instance.begin == original

@given(instance=siddhi_INTO_strategy)
@settings(max_examples=50)
def test_siddhi_into_instantiation(instance):
    assert isinstance(instance, siddhi_INTO)



@given(instance=siddhi_INTO_strategy)
def test_siddhi_into_into_setter(instance):
    original = instance.into
    instance.into = original
    assert instance.into == original

@given(instance=siddhi_INSERT_strategy)
@settings(max_examples=50)
def test_siddhi_insert_instantiation(instance):
    assert isinstance(instance, siddhi_INSERT)



@given(instance=siddhi_INSERT_strategy)
def test_siddhi_insert_insert_setter(instance):
    original = instance.insert
    instance.insert = original
    assert instance.insert == original

@given(instance=siddhi_FIRST_strategy)
@settings(max_examples=50)
def test_siddhi_first_instantiation(instance):
    assert isinstance(instance, siddhi_FIRST)



@given(instance=siddhi_FIRST_strategy)
def test_siddhi_first_first_setter(instance):
    original = instance.first
    instance.first = original
    assert instance.first == original

@given(instance=siddhi_SNAPSHOT_strategy)
@settings(max_examples=50)
def test_siddhi_snapshot_instantiation(instance):
    assert isinstance(instance, siddhi_SNAPSHOT)



@given(instance=siddhi_SNAPSHOT_strategy)
def test_siddhi_snapshot_snapshot_setter(instance):
    original = instance.snapshot
    instance.snapshot = original
    assert instance.snapshot == original

@given(instance=siddhi_HAVING_strategy)
@settings(max_examples=50)
def test_siddhi_having_instantiation(instance):
    assert isinstance(instance, siddhi_HAVING)



@given(instance=siddhi_HAVING_strategy)
def test_siddhi_having_having_setter(instance):
    original = instance.having
    instance.having = original
    assert instance.having == original

@given(instance=siddhi_BY_strategy)
@settings(max_examples=50)
def test_siddhi_by_instantiation(instance):
    assert isinstance(instance, siddhi_BY)



@given(instance=siddhi_BY_strategy)
def test_siddhi_by_by_setter(instance):
    original = instance.by
    instance.by = original
    assert instance.by == original

@given(instance=siddhi_GROUP_strategy)
@settings(max_examples=50)
def test_siddhi_group_instantiation(instance):
    assert isinstance(instance, siddhi_GROUP)



@given(instance=siddhi_GROUP_strategy)
def test_siddhi_group_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=siddhi_SELECT_strategy)
@settings(max_examples=50)
def test_siddhi_select_instantiation(instance):
    assert isinstance(instance, siddhi_SELECT)



@given(instance=siddhi_SELECT_strategy)
def test_siddhi_select_select_setter(instance):
    original = instance.select
    instance.select = original
    assert instance.select == original

@given(instance=siddhi_DOUBLE_strategy)
@settings(max_examples=50)
def test_siddhi_double_instantiation(instance):
    assert isinstance(instance, siddhi_DOUBLE)



@given(instance=siddhi_DOUBLE_strategy)
def test_siddhi_double_double_setter(instance):
    original = instance.double
    instance.double = original
    assert instance.double == original

@given(instance=siddhi_LONG_strategy)
@settings(max_examples=50)
def test_siddhi_long_instantiation(instance):
    assert isinstance(instance, siddhi_LONG)



@given(instance=siddhi_LONG_strategy)
def test_siddhi_long_long_setter(instance):
    original = instance.long
    instance.long = original
    assert instance.long == original

@given(instance=siddhi_INTS_strategy)
@settings(max_examples=50)
def test_siddhi_ints_instantiation(instance):
    assert isinstance(instance, siddhi_INTS)



@given(instance=siddhi_INTS_strategy)
def test_siddhi_ints_int_setter(instance):
    original = instance.int
    instance.int = original
    assert instance.int == original

@given(instance=siddhi_STRINGS_strategy)
@settings(max_examples=50)
def test_siddhi_strings_instantiation(instance):
    assert isinstance(instance, siddhi_STRINGS)



@given(instance=siddhi_STRINGS_strategy)
def test_siddhi_strings_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=siddhi_OUTPUT_strategy)
@settings(max_examples=50)
def test_siddhi_output_instantiation(instance):
    assert isinstance(instance, siddhi_OUTPUT)



@given(instance=siddhi_OUTPUT_strategy)
def test_siddhi_output_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=siddhi_WINDOW_strategy)
@settings(max_examples=50)
def test_siddhi_window_instantiation(instance):
    assert isinstance(instance, siddhi_WINDOW)



@given(instance=siddhi_WINDOW_strategy)
def test_siddhi_window_window_setter(instance):
    original = instance.window
    instance.window = original
    assert instance.window == original

@given(instance=siddhi_TABLE_strategy)
@settings(max_examples=50)
def test_siddhi_table_instantiation(instance):
    assert isinstance(instance, siddhi_TABLE)



@given(instance=siddhi_TABLE_strategy)
def test_siddhi_table_table_setter(instance):
    original = instance.table
    instance.table = original
    assert instance.table == original

@given(instance=siddhi_FROM_strategy)
@settings(max_examples=50)
def test_siddhi_from_instantiation(instance):
    assert isinstance(instance, siddhi_FROM)



@given(instance=siddhi_FROM_strategy)
def test_siddhi_from_from__setter(instance):
    original = instance.from_
    instance.from_ = original
    assert instance.from_ == original

@given(instance=siddhi_RETURN_strategy)
@settings(max_examples=50)
def test_siddhi_return_instantiation(instance):
    assert isinstance(instance, siddhi_RETURN)



@given(instance=siddhi_RETURN_strategy)
def test_siddhi_return_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=siddhi_FUNCTION_strategy)
@settings(max_examples=50)
def test_siddhi_function_instantiation(instance):
    assert isinstance(instance, siddhi_FUNCTION)



@given(instance=siddhi_FUNCTION_strategy)
def test_siddhi_function_function_setter(instance):
    original = instance.function
    instance.function = original
    assert instance.function == original

@given(instance=siddhi_AT_strategy)
@settings(max_examples=50)
def test_siddhi_at_instantiation(instance):
    assert isinstance(instance, siddhi_AT)



@given(instance=siddhi_AT_strategy)
def test_siddhi_at_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=siddhi_TRIGGER_strategy)
@settings(max_examples=50)
def test_siddhi_trigger_instantiation(instance):
    assert isinstance(instance, siddhi_TRIGGER)



@given(instance=siddhi_TRIGGER_strategy)
def test_siddhi_trigger_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=siddhi_NULL_strategy)
@settings(max_examples=50)
def test_siddhi_null_instantiation(instance):
    assert isinstance(instance, siddhi_NULL)



@given(instance=siddhi_NULL_strategy)
def test_siddhi_null_null_setter(instance):
    original = instance.null
    instance.null = original
    assert instance.null == original

@given(instance=siddhi_IS_strategy)
@settings(max_examples=50)
def test_siddhi_is_instantiation(instance):
    assert isinstance(instance, siddhi_IS)



@given(instance=siddhi_IS_strategy)
def test_siddhi_is_is__setter(instance):
    original = instance.is_
    instance.is_ = original
    assert instance.is_ == original

@given(instance=siddhi_LAST_strategy)
@settings(max_examples=50)
def test_siddhi_last_instantiation(instance):
    assert isinstance(instance, siddhi_LAST)



@given(instance=siddhi_LAST_strategy)
def test_siddhi_last_last_setter(instance):
    original = instance.last
    instance.last = original
    assert instance.last == original

@given(instance=siddhi_CURRENT_strategy)
@settings(max_examples=50)
def test_siddhi_current_instantiation(instance):
    assert isinstance(instance, siddhi_CURRENT)



@given(instance=siddhi_CURRENT_strategy)
def test_siddhi_current_currt_setter(instance):
    original = instance.currt
    instance.currt = original
    assert instance.currt == original

@given(instance=siddhi_EXPIRED_strategy)
@settings(max_examples=50)
def test_siddhi_expired_instantiation(instance):
    assert isinstance(instance, siddhi_EXPIRED)



@given(instance=siddhi_EXPIRED_strategy)
def test_siddhi_expired_expired_setter(instance):
    original = instance.expired
    instance.expired = original
    assert instance.expired == original

@given(instance=siddhi_RAW_strategy)
@settings(max_examples=50)
def test_siddhi_raw_instantiation(instance):
    assert isinstance(instance, siddhi_RAW)



@given(instance=siddhi_RAW_strategy)
def test_siddhi_raw_raw_setter(instance):
    original = instance.raw
    instance.raw = original
    assert instance.raw == original

@given(instance=siddhi_EVENTS_strategy)
@settings(max_examples=50)
def test_siddhi_events_instantiation(instance):
    assert isinstance(instance, siddhi_EVENTS)



@given(instance=siddhi_EVENTS_strategy)
def test_siddhi_events_events_setter(instance):
    original = instance.events
    instance.events = original
    assert instance.events == original

@given(instance=siddhi_ALL_strategy)
@settings(max_examples=50)
def test_siddhi_all_instantiation(instance):
    assert isinstance(instance, siddhi_ALL)



@given(instance=siddhi_ALL_strategy)
def test_siddhi_all_all_setter(instance):
    original = instance.all
    instance.all = original
    assert instance.all == original

@given(instance=siddhi_OBJECT_strategy)
@settings(max_examples=50)
def test_siddhi_object_instantiation(instance):
    assert isinstance(instance, siddhi_OBJECT)



@given(instance=siddhi_OBJECT_strategy)
def test_siddhi_object_object_setter(instance):
    original = instance.object
    instance.object = original
    assert instance.object == original

@given(instance=siddhi_BOOL_strategy)
@settings(max_examples=50)
def test_siddhi_bool_instantiation(instance):
    assert isinstance(instance, siddhi_BOOL)



@given(instance=siddhi_BOOL_strategy)
def test_siddhi_bool_bool_setter(instance):
    original = instance.bool
    instance.bool = original
    assert instance.bool == original

@given(instance=siddhi_FLOAT_strategy)
@settings(max_examples=50)
def test_siddhi_float_instantiation(instance):
    assert isinstance(instance, siddhi_FLOAT)



@given(instance=siddhi_FLOAT_strategy)
def test_siddhi_float_float_setter(instance):
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

@given(instance=siddhi_DEFINE_strategy)
@settings(max_examples=50)
def test_siddhi_define_instantiation(instance):
    assert isinstance(instance, siddhi_DEFINE)



@given(instance=siddhi_DEFINE_strategy)
def test_siddhi_define_define_setter(instance):
    original = instance.define
    instance.define = original
    assert instance.define == original

@given(instance=siddhi_STREAM_strategy)
@settings(max_examples=50)
def test_siddhi_stream_instantiation(instance):
    assert isinstance(instance, siddhi_STREAM)



@given(instance=siddhi_STREAM_strategy)
def test_siddhi_stream_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=AppAnnotation_strategy)
@settings(max_examples=50)
def test_appannotation_instantiation(instance):
    assert isinstance(instance, AppAnnotation)

@given(instance=siddhi_APP_strategy)
@settings(max_examples=50)
def test_siddhi_app_instantiation(instance):
    assert isinstance(instance, siddhi_APP)



@given(instance=siddhi_APP_strategy)
def test_siddhi_app_ap_setter(instance):
    original = instance.ap
    instance.ap = original
    assert instance.ap == original

@given(instance=siddhi_IN_strategy)
@settings(max_examples=50)
def test_siddhi_in_instantiation(instance):
    assert isinstance(instance, siddhi_IN)



@given(instance=siddhi_IN_strategy)
def test_siddhi_in_in__setter(instance):
    original = instance.in_
    instance.in_ = original
    assert instance.in_ == original

@given(instance=RightAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_rightabsentpatternsource_instantiation(instance):
    assert isinstance(instance, RightAbsentPatternSource)

@given(instance=siddhi_RightAbsentPatternSource1_strategy)
@settings(max_examples=50)
def test_siddhi_rightabsentpatternsource1_instantiation(instance):
    assert isinstance(instance, siddhi_RightAbsentPatternSource1)



@given(instance=siddhi_RightAbsentPatternSource1_strategy)
def test_siddhi_rightabsentpatternsource1_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original

@given(instance=LeftAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_leftabsentpatternsource_instantiation(instance):
    assert isinstance(instance, LeftAbsentPatternSource)

@given(instance=siddhi_LeftAbsentPatternSource1_strategy)
@settings(max_examples=50)
def test_siddhi_leftabsentpatternsource1_instantiation(instance):
    assert isinstance(instance, siddhi_LeftAbsentPatternSource1)



@given(instance=siddhi_LeftAbsentPatternSource1_strategy)
def test_siddhi_leftabsentpatternsource1_fb_setter(instance):
    original = instance.fb
    instance.fb = original
    assert instance.fb == original

@given(instance=EveryAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_everyabsentpatternsource_instantiation(instance):
    assert isinstance(instance, EveryAbsentPatternSource)

@given(instance=LogicalAbsentStatefulSource_strategy)
@settings(max_examples=50)
def test_logicalabsentstatefulsource_instantiation(instance):
    assert isinstance(instance, LogicalAbsentStatefulSource)

@given(instance=siddhi_MillisecondValue_strategy)
@settings(max_examples=50)
def test_siddhi_millisecondvalue_instantiation(instance):
    assert isinstance(instance, siddhi_MillisecondValue)

@given(instance=siddhi_UNIDIRECTIONAL_strategy)
@settings(max_examples=50)
def test_siddhi_unidirectional_instantiation(instance):
    assert isinstance(instance, siddhi_UNIDIRECTIONAL)



@given(instance=siddhi_UNIDIRECTIONAL_strategy)
def test_siddhi_unidirectional_unidirectional_setter(instance):
    original = instance.unidirectional
    instance.unidirectional = original
    assert instance.unidirectional == original

@given(instance=siddhi_JoinSource_strategy)
@settings(max_examples=50)
def test_siddhi_joinsource_instantiation(instance):
    assert isinstance(instance, siddhi_JoinSource)

@given(instance=StandardStream_strategy)
@settings(max_examples=50)
def test_standardstream_instantiation(instance):
    assert isinstance(instance, StandardStream)

@given(instance=JoinSource_strategy)
@settings(max_examples=50)
def test_joinsource_instantiation(instance):
    assert isinstance(instance, JoinSource)

@given(instance=siddhi_MainSource_strategy)
@settings(max_examples=50)
def test_siddhi_mainsource_instantiation(instance):
    assert isinstance(instance, siddhi_MainSource)

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

@given(instance=siddhi_joins_strategy)
@settings(max_examples=50)
def test_siddhi_joins_instantiation(instance):
    assert isinstance(instance, siddhi_joins)

@given(instance=siddhi_Per1_strategy)
@settings(max_examples=50)
def test_siddhi_per1_instantiation(instance):
    assert isinstance(instance, siddhi_Per1)

@given(instance=siddhi_WithinTimeRange_strategy)
@settings(max_examples=50)
def test_siddhi_withintimerange_instantiation(instance):
    assert isinstance(instance, siddhi_WithinTimeRange)

@given(instance=AbsentPatternSourceChain_strategy)
@settings(max_examples=50)
def test_absentpatternsourcechain_instantiation(instance):
    assert isinstance(instance, AbsentPatternSourceChain)

@given(instance=siddhi_EveryAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi_everyabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi_EveryAbsentPatternSource)

@given(instance=siddhi_RightAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi_rightabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi_RightAbsentPatternSource)



@given(instance=siddhi_RightAbsentPatternSource_strategy)
def test_siddhi_rightabsentpatternsource_fb2_setter(instance):
    original = instance.fb2
    instance.fb2 = original
    assert instance.fb2 == original

@given(instance=siddhi_LeftAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi_leftabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi_LeftAbsentPatternSource)



@given(instance=siddhi_LeftAbsentPatternSource_strategy)
def test_siddhi_leftabsentpatternsource_fb1_setter(instance):
    original = instance.fb1
    instance.fb1 = original
    assert instance.fb1 == original

@given(instance=siddhi_PatternCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_patterncollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_PatternCollectionStatefulSource)

@given(instance=siddhi_PatternSource_strategy)
@settings(max_examples=50)
def test_siddhi_patternsource_instantiation(instance):
    assert isinstance(instance, siddhi_PatternSource)

@given(instance=siddhi_BasicSource_strategy)
@settings(max_examples=50)
def test_siddhi_basicsource_instantiation(instance):
    assert isinstance(instance, siddhi_BasicSource)

@given(instance=siddhi_NOT_strategy)
@settings(max_examples=50)
def test_siddhi_not_instantiation(instance):
    assert isinstance(instance, siddhi_NOT)



@given(instance=siddhi_NOT_strategy)
def test_siddhi_not_not1_setter(instance):
    original = instance.not1
    instance.not1 = original
    assert instance.not1 == original

@given(instance=siddhi_Collect_strategy)
@settings(max_examples=50)
def test_siddhi_collect_instantiation(instance):
    assert isinstance(instance, siddhi_Collect)



@given(instance=siddhi_Collect_strategy)
def test_siddhi_collect_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=siddhi_Collect_strategy)
def test_siddhi_collect_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=siddhi_AND_strategy)
@settings(max_examples=50)
def test_siddhi_and_instantiation(instance):
    assert isinstance(instance, siddhi_AND)



@given(instance=siddhi_AND_strategy)
def test_siddhi_and_and__setter(instance):
    original = instance.and_
    instance.and_ = original
    assert instance.and_ == original

@given(instance=SequenceSource_strategy)
@settings(max_examples=50)
def test_sequencesource_instantiation(instance):
    assert isinstance(instance, SequenceSource)

@given(instance=siddhi_LogicalStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_logicalstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_LogicalStatefulSource)

@given(instance=siddhi_LogicalAbsentStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_logicalabsentstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_LogicalAbsentStatefulSource)

@given(instance=siddhi_SequenceCollectionStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_sequencecollectionstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_SequenceCollectionStatefulSource)

@given(instance=SequenceSourceChain_strategy)
@settings(max_examples=50)
def test_sequencesourcechain_instantiation(instance):
    assert isinstance(instance, SequenceSourceChain)

@given(instance=siddhi_PatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_patternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_PatternSourceChain)



@given(instance=siddhi_PatternSourceChain_strategy)
def test_siddhi_patternsourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=PatternStream_strategy)
@settings(max_examples=50)
def test_patternstream_instantiation(instance):
    assert isinstance(instance, PatternStream)

@given(instance=siddhi_AbsentPatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_absentpatternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_AbsentPatternSourceChain)

@given(instance=siddhi_EveryPatternSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_everypatternsourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_EveryPatternSourceChain)



@given(instance=siddhi_EveryPatternSourceChain_strategy)
def test_siddhi_everypatternsourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi_RightAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi_rightabsentsequencesource_instantiation(instance):
    assert isinstance(instance, siddhi_RightAbsentSequenceSource)



@given(instance=siddhi_RightAbsentSequenceSource_strategy)
def test_siddhi_rightabsentsequencesource_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original



@given(instance=siddhi_RightAbsentSequenceSource_strategy)
def test_siddhi_rightabsentsequencesource_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original



@given(instance=siddhi_RightAbsentSequenceSource_strategy)
def test_siddhi_rightabsentsequencesource_comm_setter(instance):
    original = instance.comm
    instance.comm = original
    assert instance.comm == original



@given(instance=siddhi_RightAbsentSequenceSource_strategy)
def test_siddhi_rightabsentsequencesource_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi_LeftAbsentSequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi_leftabsentsequencesource_instantiation(instance):
    assert isinstance(instance, siddhi_LeftAbsentSequenceSource)



@given(instance=siddhi_LeftAbsentSequenceSource_strategy)
def test_siddhi_leftabsentsequencesource_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original



@given(instance=siddhi_LeftAbsentSequenceSource_strategy)
def test_siddhi_leftabsentsequencesource_comma_setter(instance):
    original = instance.comma
    instance.comma = original
    assert instance.comma == original



@given(instance=siddhi_LeftAbsentSequenceSource_strategy)
def test_siddhi_leftabsentsequencesource_comm_setter(instance):
    original = instance.comm
    instance.comm = original
    assert instance.comm == original



@given(instance=siddhi_LeftAbsentSequenceSource_strategy)
def test_siddhi_leftabsentsequencesource_cp_setter(instance):
    original = instance.cp
    instance.cp = original
    assert instance.cp == original

@given(instance=siddhi_BasicAbsentPatternSource_strategy)
@settings(max_examples=50)
def test_siddhi_basicabsentpatternsource_instantiation(instance):
    assert isinstance(instance, siddhi_BasicAbsentPatternSource)

@given(instance=siddhi_EObject_strategy)
@settings(max_examples=50)
def test_siddhi_eobject_instantiation(instance):
    assert isinstance(instance, siddhi_EObject)

@given(instance=HAVING_strategy)
@settings(max_examples=50)
def test_having_instantiation(instance):
    assert isinstance(instance, HAVING)

@given(instance=GROUP_strategy)
@settings(max_examples=50)
def test_group_instantiation(instance):
    assert isinstance(instance, GROUP)

@given(instance=siddhi_HavingExpr_strategy)
@settings(max_examples=50)
def test_siddhi_havingexpr_instantiation(instance):
    assert isinstance(instance, siddhi_HavingExpr)

@given(instance=siddhi_AbsentSequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_absentsequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_AbsentSequenceSourceChain)

@given(instance=siddhi_SequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_sequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_SequenceSourceChain)



@given(instance=siddhi_SequenceSourceChain_strategy)
def test_siddhi_sequencesourcechain_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=siddhi_WithinTime_strategy)
@settings(max_examples=50)
def test_siddhi_withintime_instantiation(instance):
    assert isinstance(instance, siddhi_WithinTime)

@given(instance=siddhi_SequenceSource_strategy)
@settings(max_examples=50)
def test_siddhi_sequencesource_instantiation(instance):
    assert isinstance(instance, siddhi_SequenceSource)

@given(instance=siddhi_EveryAbsentSequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_everyabsentsequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_EveryAbsentSequenceSourceChain)

@given(instance=siddhi_EverySequenceSourceChain_strategy)
@settings(max_examples=50)
def test_siddhi_everysequencesourcechain_instantiation(instance):
    assert isinstance(instance, siddhi_EverySequenceSourceChain)

@given(instance=siddhi_PatternStream_strategy)
@settings(max_examples=50)
def test_siddhi_patternstream_instantiation(instance):
    assert isinstance(instance, siddhi_PatternStream)

@given(instance=siddhi_SequenceStream_strategy)
@settings(max_examples=50)
def test_siddhi_sequencestream_instantiation(instance):
    assert isinstance(instance, siddhi_SequenceStream)

@given(instance=siddhi_JoinStream_strategy)
@settings(max_examples=50)
def test_siddhi_joinstream_instantiation(instance):
    assert isinstance(instance, siddhi_JoinStream)

@given(instance=siddhi_Attribute_strategy)
@settings(max_examples=50)
def test_siddhi_attribute_instantiation(instance):
    assert isinstance(instance, siddhi_Attribute)

@given(instance=siddhi_OutputAttribute_strategy)
@settings(max_examples=50)
def test_siddhi_outputattribute_instantiation(instance):
    assert isinstance(instance, siddhi_OutputAttribute)

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

@given(instance=siddhi_AttributeIndex_strategy)
@settings(max_examples=50)
def test_siddhi_attributeindex_instantiation(instance):
    assert isinstance(instance, siddhi_AttributeIndex)

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

@given(instance=siddhi_OutputRateType_strategy)
@settings(max_examples=50)
def test_siddhi_outputratetype_instantiation(instance):
    assert isinstance(instance, siddhi_OutputRateType)

@given(instance=siddhi_SetAssignment_strategy)
@settings(max_examples=50)
def test_siddhi_setassignment_instantiation(instance):
    assert isinstance(instance, siddhi_SetAssignment)

@given(instance=SET_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, SET)

@given(instance=siddhi_SetClause_strategy)
@settings(max_examples=50)
def test_siddhi_setclause_instantiation(instance):
    assert isinstance(instance, siddhi_SetClause)

@given(instance=siddhi_OR_strategy)
@settings(max_examples=50)
def test_siddhi_or_instantiation(instance):
    assert isinstance(instance, siddhi_OR)



@given(instance=siddhi_OR_strategy)
def test_siddhi_or_or__setter(instance):
    original = instance.or_
    instance.or_ = original
    assert instance.or_ == original

@given(instance=siddhi_ConditionRange_strategy)
@settings(max_examples=50)
def test_siddhi_conditionrange_instantiation(instance):
    assert isinstance(instance, siddhi_ConditionRange)

@given(instance=siddhi_OF_strategy)
@settings(max_examples=50)
def test_siddhi_of_instantiation(instance):
    assert isinstance(instance, siddhi_OF)



@given(instance=siddhi_OF_strategy)
def test_siddhi_of_of_setter(instance):
    original = instance.of
    instance.of = original
    assert instance.of == original

@given(instance=PartitionWithStream_strategy)
@settings(max_examples=50)
def test_partitionwithstream_instantiation(instance):
    assert isinstance(instance, PartitionWithStream)

@given(instance=siddhi_ConditionRanges_strategy)
@settings(max_examples=50)
def test_siddhi_conditionranges_instantiation(instance):
    assert isinstance(instance, siddhi_ConditionRanges)

@given(instance=siddhi_ON_strategy)
@settings(max_examples=50)
def test_siddhi_on_instantiation(instance):
    assert isinstance(instance, siddhi_ON)



@given(instance=siddhi_ON_strategy)
def test_siddhi_on_on_setter(instance):
    original = instance.on
    instance.on = original
    assert instance.on == original

@given(instance=siddhi_Target_strategy)
@settings(max_examples=50)
def test_siddhi_target_instantiation(instance):
    assert isinstance(instance, siddhi_Target)

@given(instance=UPDATE_strategy)
@settings(max_examples=50)
def test_update_instantiation(instance):
    assert isinstance(instance, UPDATE)

@given(instance=FOR_strategy)
@settings(max_examples=50)
def test_for_instantiation(instance):
    assert isinstance(instance, FOR)

@given(instance=siddhi_ForTime_strategy)
@settings(max_examples=50)
def test_siddhi_fortime_instantiation(instance):
    assert isinstance(instance, siddhi_ForTime)

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

@given(instance=siddhi_QuerySection_strategy)
@settings(max_examples=50)
def test_siddhi_querysection_instantiation(instance):
    assert isinstance(instance, siddhi_QuerySection)

@given(instance=siddhi_QueryInput_strategy)
@settings(max_examples=50)
def test_siddhi_queryinput_instantiation(instance):
    assert isinstance(instance, siddhi_QueryInput)

@given(instance=siddhi_AS_strategy)
@settings(max_examples=50)
def test_siddhi_as_instantiation(instance):
    assert isinstance(instance, siddhi_AS)



@given(instance=siddhi_AS_strategy)
def test_siddhi_as_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=siddhi_Expression_strategy)
@settings(max_examples=50)
def test_siddhi_expression_instantiation(instance):
    assert isinstance(instance, siddhi_Expression)

@given(instance=siddhi_PropertyValue_strategy)
@settings(max_examples=50)
def test_siddhi_propertyvalue_instantiation(instance):
    assert isinstance(instance, siddhi_PropertyValue)

@given(instance=siddhi_PartitionWithStream_strategy)
@settings(max_examples=50)
def test_siddhi_partitionwithstream_instantiation(instance):
    assert isinstance(instance, siddhi_PartitionWithStream)

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

@given(instance=siddhi_StreamAlias_strategy)
@settings(max_examples=50)
def test_siddhi_streamalias_instantiation(instance):
    assert isinstance(instance, siddhi_StreamAlias)

@given(instance=siddhi_StandardStatefulSource_strategy)
@settings(max_examples=50)
def test_siddhi_standardstatefulsource_instantiation(instance):
    assert isinstance(instance, siddhi_StandardStatefulSource)



@given(instance=siddhi_StandardStatefulSource_strategy)
def test_siddhi_standardstatefulsource_zero_or_more_setter(instance):
    original = instance.zero_or_more
    instance.zero_or_more = original
    assert instance.zero_or_more == original



@given(instance=siddhi_StandardStatefulSource_strategy)
def test_siddhi_standardstatefulsource_zero_or_one_setter(instance):
    original = instance.zero_or_one
    instance.zero_or_one = original
    assert instance.zero_or_one == original



@given(instance=siddhi_StandardStatefulSource_strategy)
def test_siddhi_standardstatefulsource_one_or_more_setter(instance):
    original = instance.one_or_more
    instance.one_or_more = original
    assert instance.one_or_more == original

@given(instance=siddhi_Source_strategy)
@settings(max_examples=50)
def test_siddhi_source_instantiation(instance):
    assert isinstance(instance, siddhi_Source)

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

@given(instance=siddhi_OutAttr_strategy)
@settings(max_examples=50)
def test_siddhi_outattr_instantiation(instance):
    assert isinstance(instance, siddhi_OutAttr)

@given(instance=siddhi_PropertySeparator_strategy)
@settings(max_examples=50)
def test_siddhi_propertyseparator_instantiation(instance):
    assert isinstance(instance, siddhi_PropertySeparator)

@given(instance=siddhi_AttributeReference_strategy)
@settings(max_examples=50)
def test_siddhi_attributereference_instantiation(instance):
    assert isinstance(instance, siddhi_AttributeReference)



@given(instance=siddhi_AttributeReference_strategy)
def test_siddhi_attributereference_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=siddhi_AttributeReference_strategy)
def test_siddhi_attributereference_hash2_setter(instance):
    original = instance.hash2
    instance.hash2 = original
    assert instance.hash2 == original



@given(instance=siddhi_AttributeReference_strategy)
def test_siddhi_attributereference_hash1_setter(instance):
    original = instance.hash1
    instance.hash1 = original
    assert instance.hash1 == original

@given(instance=siddhi_GroupByQuerySelection_strategy)
@settings(max_examples=50)
def test_siddhi_groupbyqueryselection_instantiation(instance):
    assert isinstance(instance, siddhi_GroupByQuerySelection)

@given(instance=siddhi_StandardStream_strategy)
@settings(max_examples=50)
def test_siddhi_standardstream_instantiation(instance):
    assert isinstance(instance, siddhi_StandardStream)

@given(instance=BY_strategy)
@settings(max_examples=50)
def test_by_instantiation(instance):
    assert isinstance(instance, BY)

@given(instance=siddhi_GroupBy_strategy)
@settings(max_examples=50)
def test_siddhi_groupby_instantiation(instance):
    assert isinstance(instance, siddhi_GroupBy)

@given(instance=siddhi_PropertyName_strategy)
@settings(max_examples=50)
def test_siddhi_propertyname_instantiation(instance):
    assert isinstance(instance, siddhi_PropertyName)

@given(instance=siddhi_AnnotationElement_strategy)
@settings(max_examples=50)
def test_siddhi_annotationelement_instantiation(instance):
    assert isinstance(instance, siddhi_AnnotationElement)

@given(instance=siddhi_Name_strategy)
@settings(max_examples=50)
def test_siddhi_name_instantiation(instance):
    assert isinstance(instance, siddhi_Name)



@given(instance=siddhi_Name_strategy)
def test_siddhi_name_na_setter(instance):
    original = instance.na
    instance.na = original
    assert instance.na == original

@given(instance=YEARS_strategy)
@settings(max_examples=50)
def test_years_instantiation(instance):
    assert isinstance(instance, YEARS)

@given(instance=siddhi_YearValue_strategy)
@settings(max_examples=50)
def test_siddhi_yearvalue_instantiation(instance):
    assert isinstance(instance, siddhi_YearValue)

@given(instance=MONTHS_strategy)
@settings(max_examples=50)
def test_months_instantiation(instance):
    assert isinstance(instance, MONTHS)

@given(instance=siddhi_MonthValue_strategy)
@settings(max_examples=50)
def test_siddhi_monthvalue_instantiation(instance):
    assert isinstance(instance, siddhi_MonthValue)

@given(instance=WEEKS_strategy)
@settings(max_examples=50)
def test_weeks_instantiation(instance):
    assert isinstance(instance, WEEKS)

@given(instance=siddhi_WeekValue_strategy)
@settings(max_examples=50)
def test_siddhi_weekvalue_instantiation(instance):
    assert isinstance(instance, siddhi_WeekValue)

@given(instance=DAYS_strategy)
@settings(max_examples=50)
def test_days_instantiation(instance):
    assert isinstance(instance, DAYS)

@given(instance=siddhi_DayValue_strategy)
@settings(max_examples=50)
def test_siddhi_dayvalue_instantiation(instance):
    assert isinstance(instance, siddhi_DayValue)

@given(instance=HOURS_strategy)
@settings(max_examples=50)
def test_hours_instantiation(instance):
    assert isinstance(instance, HOURS)

@given(instance=siddhi_HourValue_strategy)
@settings(max_examples=50)
def test_siddhi_hourvalue_instantiation(instance):
    assert isinstance(instance, siddhi_HourValue)

@given(instance=MINUTES_strategy)
@settings(max_examples=50)
def test_minutes_instantiation(instance):
    assert isinstance(instance, MINUTES)

@given(instance=siddhi_MinuteValue_strategy)
@settings(max_examples=50)
def test_siddhi_minutevalue_instantiation(instance):
    assert isinstance(instance, siddhi_MinuteValue)

@given(instance=SECONDS_strategy)
@settings(max_examples=50)
def test_seconds_instantiation(instance):
    assert isinstance(instance, SECONDS)

@given(instance=siddhi_SecondValue_strategy)
@settings(max_examples=50)
def test_siddhi_secondvalue_instantiation(instance):
    assert isinstance(instance, siddhi_SecondValue)

@given(instance=AggregationTime_strategy)
@settings(max_examples=50)
def test_aggregationtime_instantiation(instance):
    assert isinstance(instance, AggregationTime)

@given(instance=siddhi_AggregationTimeRange_strategy)
@settings(max_examples=50)
def test_siddhi_aggregationtimerange_instantiation(instance):
    assert isinstance(instance, siddhi_AggregationTimeRange)

@given(instance=siddhi_AggregationTimeInterval_strategy)
@settings(max_examples=50)
def test_siddhi_aggregationtimeinterval_instantiation(instance):
    assert isinstance(instance, siddhi_AggregationTimeInterval)

@given(instance=siddhi_AggregationTimeDuration_strategy)
@settings(max_examples=50)
def test_siddhi_aggregationtimeduration_instantiation(instance):
    assert isinstance(instance, siddhi_AggregationTimeDuration)

@given(instance=siddhi_AggregationTime_strategy)
@settings(max_examples=50)
def test_siddhi_aggregationtime_instantiation(instance):
    assert isinstance(instance, siddhi_AggregationTime)

@given(instance=OUTPUT_strategy)
@settings(max_examples=50)
def test_output_instantiation(instance):
    assert isinstance(instance, OUTPUT)

@given(instance=siddhi_OutputRate_strategy)
@settings(max_examples=50)
def test_siddhi_outputrate_instantiation(instance):
    assert isinstance(instance, siddhi_OutputRate)

@given(instance=WINDOW_strategy)
@settings(max_examples=50)
def test_window_instantiation(instance):
    assert isinstance(instance, WINDOW)

@given(instance=siddhi_Win_strategy)
@settings(max_examples=50)
def test_siddhi_win_instantiation(instance):
    assert isinstance(instance, siddhi_Win)

@given(instance=siddhi_BasicSourceStreamHandlers1_strategy)
@settings(max_examples=50)
def test_siddhi_basicsourcestreamhandlers1_instantiation(instance):
    assert isinstance(instance, siddhi_BasicSourceStreamHandlers1)

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

@given(instance=siddhi_FunctionBody_strategy)
@settings(max_examples=50)
def test_siddhi_functionbody_instantiation(instance):
    assert isinstance(instance, siddhi_FunctionBody)



@given(instance=siddhi_FunctionBody_strategy)
def test_siddhi_functionbody_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=siddhi_AttributeType_strategy)
@settings(max_examples=50)
def test_siddhi_attributetype_instantiation(instance):
    assert isinstance(instance, siddhi_AttributeType)

@given(instance=siddhi_LanguageName_strategy)
@settings(max_examples=50)
def test_siddhi_languagename_instantiation(instance):
    assert isinstance(instance, siddhi_LanguageName)



@given(instance=siddhi_LanguageName_strategy)
def test_siddhi_languagename_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=siddhi_FunctionName_strategy)
@settings(max_examples=50)
def test_siddhi_functionname_instantiation(instance):
    assert isinstance(instance, siddhi_FunctionName)



@given(instance=siddhi_FunctionName_strategy)
def test_siddhi_functionname_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=RETURN_strategy)
@settings(max_examples=50)
def test_return_instantiation(instance):
    assert isinstance(instance, RETURN)

@given(instance=siddhi_AnonymousStream_strategy)
@settings(max_examples=50)
def test_siddhi_anonymousstream_instantiation(instance):
    assert isinstance(instance, siddhi_AnonymousStream)

@given(instance=siddhi_QueryOutput_strategy)
@settings(max_examples=50)
def test_siddhi_queryoutput_instantiation(instance):
    assert isinstance(instance, siddhi_QueryOutput)

@given(instance=FUNCTION_strategy)
@settings(max_examples=50)
def test_function_instantiation(instance):
    assert isinstance(instance, FUNCTION)

@given(instance=siddhi_StringValue_strategy)
@settings(max_examples=50)
def test_siddhi_stringvalue_instantiation(instance):
    assert isinstance(instance, siddhi_StringValue)



@given(instance=siddhi_StringValue_strategy)
def test_siddhi_stringvalue_sl_setter(instance):
    original = instance.sl
    instance.sl = original
    assert instance.sl == original

@given(instance=siddhi_TimeValue_strategy)
@settings(max_examples=50)
def test_siddhi_timevalue_instantiation(instance):
    assert isinstance(instance, siddhi_TimeValue)

@given(instance=siddhi_EVERY_strategy)
@settings(max_examples=50)
def test_siddhi_every_instantiation(instance):
    assert isinstance(instance, siddhi_EVERY)



@given(instance=siddhi_EVERY_strategy)
def test_siddhi_every_every1_setter(instance):
    original = instance.every1
    instance.every1 = original
    assert instance.every1 == original

@given(instance=siddhi_TriggerName_strategy)
@settings(max_examples=50)
def test_siddhi_triggername_instantiation(instance):
    assert isinstance(instance, siddhi_TriggerName)



@given(instance=siddhi_TriggerName_strategy)
def test_siddhi_triggername_id_setter(instance):
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

@given(instance=siddhi_OutputEventType_strategy)
@settings(max_examples=50)
def test_siddhi_outputeventtype_instantiation(instance):
    assert isinstance(instance, siddhi_OutputEventType)

@given(instance=siddhi_FunctionOperation_strategy)
@settings(max_examples=50)
def test_siddhi_functionoperation_instantiation(instance):
    assert isinstance(instance, siddhi_FunctionOperation)

@given(instance=siddhi_AppAnnotation_strategy)
@settings(max_examples=50)
def test_siddhi_appannotation_instantiation(instance):
    assert isinstance(instance, siddhi_AppAnnotation)

@given(instance=siddhi_ExecutionPlan_strategy)
@settings(max_examples=50)
def test_siddhi_executionplan_instantiation(instance):
    assert isinstance(instance, siddhi_ExecutionPlan)

@given(instance=TABLE_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, TABLE)

@given(instance=siddhi_Features_strategy)
@settings(max_examples=50)
def test_siddhi_features_instantiation(instance):
    assert isinstance(instance, siddhi_Features)

@given(instance=siddhi_Source1_strategy)
@settings(max_examples=50)
def test_siddhi_source1_instantiation(instance):
    assert isinstance(instance, siddhi_Source1)



@given(instance=siddhi_Source1_strategy)
def test_siddhi_source1_inner_setter(instance):
    original = instance.inner
    instance.inner = original
    assert instance.inner == original

@given(instance=siddhi_Annotation_strategy)
@settings(max_examples=50)
def test_siddhi_annotation_instantiation(instance):
    assert isinstance(instance, siddhi_Annotation)

@given(instance=STREAM_strategy)
@settings(max_examples=50)
def test_stream_instantiation(instance):
    assert isinstance(instance, STREAM)

@given(instance=DEFINE_strategy)
@settings(max_examples=50)
def test_define_instantiation(instance):
    assert isinstance(instance, DEFINE)

@given(instance=siddhi_DefinitionStream_strategy)
@settings(max_examples=50)
def test_siddhi_definitionstream_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionStream)

@given(instance=siddhi_DefinitionTable_strategy)
@settings(max_examples=50)
def test_siddhi_definitiontable_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionTable)

@given(instance=siddhi_Keyword_strategy)
@settings(max_examples=50)
def test_siddhi_keyword_instantiation(instance):
    assert isinstance(instance, siddhi_Keyword)

@given(instance=siddhi_Query_strategy)
@settings(max_examples=50)
def test_siddhi_query_instantiation(instance):
    assert isinstance(instance, siddhi_Query)

@given(instance=siddhi_ExecPartition_strategy)
@settings(max_examples=50)
def test_siddhi_execpartition_instantiation(instance):
    assert isinstance(instance, siddhi_ExecPartition)

@given(instance=siddhi_ExecutionElement_strategy)
@settings(max_examples=50)
def test_siddhi_executionelement_instantiation(instance):
    assert isinstance(instance, siddhi_ExecutionElement)

@given(instance=siddhi_DefinitionAggregation_strategy)
@settings(max_examples=50)
def test_siddhi_definitionaggregation_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionAggregation)

@given(instance=siddhi_DefinitionFunction_strategy)
@settings(max_examples=50)
def test_siddhi_definitionfunction_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionFunction)

@given(instance=siddhi_DefinitionTrigger_strategy)
@settings(max_examples=50)
def test_siddhi_definitiontrigger_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionTrigger)

@given(instance=siddhi_DefinitionWindow_strategy)
@settings(max_examples=50)
def test_siddhi_definitionwindow_instantiation(instance):
    assert isinstance(instance, siddhi_DefinitionWindow)

@given(instance=siddhi_SiddhiQL_strategy)
@settings(max_examples=50)
def test_siddhi_siddhiql_instantiation(instance):
    assert isinstance(instance, siddhi_SiddhiQL)
