####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
siddhi_DefinitionAggregation = Class(name="siddhi::DefinitionAggregation")
siddhi_ExecutionElement = Class(name="siddhi::ExecutionElement")
siddhi_SiddhiQL = Class(name="siddhi::SiddhiQL")
siddhi_ExecutionPlan = Class(name="siddhi::ExecutionPlan")
siddhi_AppAnnotation = Class(name="siddhi::AppAnnotation")
siddhi_DefinitionStream = Class(name="siddhi::DefinitionStream")
siddhi_DefinitionTable = Class(name="siddhi::DefinitionTable")
siddhi_DefinitionWindow = Class(name="siddhi::DefinitionWindow")
siddhi_DefinitionTrigger = Class(name="siddhi::DefinitionTrigger")
siddhi_DefinitionFunction = Class(name="siddhi::DefinitionFunction")
siddhi_ExecPartition = Class(name="siddhi::ExecPartition")
siddhi_Query = Class(name="siddhi::Query")
DEFINE = Class(name="DEFINE")
STREAM = Class(name="STREAM")
siddhi_Annotation = Class(name="siddhi::Annotation")
siddhi_Source1 = Class(name="siddhi::Source1")
siddhi_Features = Class(name="siddhi::Features")
TABLE = Class(name="TABLE")
WINDOW = Class(name="WINDOW")
OUTPUT = Class(name="OUTPUT")
siddhi_AttributeType = Class(name="siddhi::AttributeType")
siddhi_FunctionOperation = Class(name="siddhi::FunctionOperation")
siddhi_OutputEventType = Class(name="siddhi::OutputEventType")
TRIGGER = Class(name="TRIGGER")
AT = Class(name="AT")
siddhi_TriggerName = Class(name="siddhi::TriggerName")
siddhi_EVERY = Class(name="siddhi::EVERY")
siddhi_TimeValue = Class(name="siddhi::TimeValue")
siddhi_StringValue = Class(name="siddhi::StringValue")
FUNCTION = Class(name="FUNCTION")
RETURN = Class(name="RETURN")
siddhi_FunctionName = Class(name="siddhi::FunctionName")
siddhi_LanguageName = Class(name="siddhi::LanguageName")
siddhi_FunctionBody = Class(name="siddhi::FunctionBody")
AGGREGATION = Class(name="AGGREGATION")
FROM = Class(name="FROM")
AGGREGATE = Class(name="AGGREGATE")
BY = Class(name="BY")
siddhi_StandardStream = Class(name="siddhi::StandardStream")
siddhi_GroupByQuerySelection = Class(name="siddhi::GroupByQuerySelection")
siddhi_AttributeReference = Class(name="siddhi::AttributeReference")
siddhi_AggregationTime = Class(name="siddhi::AggregationTime")
siddhi_AggregationTimeDuration = Class(name="siddhi::AggregationTimeDuration")
siddhi_AggregationTimeInterval = Class(name="siddhi::AggregationTimeInterval")
AggregationTime = Class(name="AggregationTime")
SECONDS = Class(name="SECONDS")
MINUTES = Class(name="MINUTES")
HOURS = Class(name="HOURS")
DAYS = Class(name="DAYS")
WEEKS = Class(name="WEEKS")
MONTHS = Class(name="MONTHS")
YEARS = Class(name="YEARS")
siddhi_AggregationTimeRange = Class(name="siddhi::AggregationTimeRange")
siddhi_Name = Class(name="siddhi::Name")
siddhi_AnnotationElement = Class(name="siddhi::AnnotationElement")
siddhi_PropertyName = Class(name="siddhi::PropertyName")
siddhi_PropertyValue = Class(name="siddhi::PropertyValue")
siddhi_PropertySeparator = Class(name="siddhi::PropertySeparator")
FeaturesOrOutAttr = Class(name="FeaturesOrOutAttr")
STRINGS = Class(name="STRINGS")
INTS = Class(name="INTS")
LONG = Class(name="LONG")
FLOAT = Class(name="FLOAT")
DOUBLE = Class(name="DOUBLE")
BOOL = Class(name="BOOL")
OBJECT = Class(name="OBJECT")
siddhi_Source = Class(name="siddhi::Source")
Source1OrStandardStatefulSource = Class(name="Source1OrStandardStatefulSource")
PARTITION = Class(name="PARTITION")
WITH = Class(name="WITH")
BEGIN = Class(name="BEGIN")
END = Class(name="END")
siddhi_PartitionWithStream = Class(name="siddhi::PartitionWithStream")
siddhi_ConditionRanges = Class(name="siddhi::ConditionRanges")
PartitionWithStream = Class(name="PartitionWithStream")
siddhi_OF = Class(name="siddhi::OF")
siddhi_ConditionRange = Class(name="siddhi::ConditionRange")
siddhi_OR = Class(name="siddhi::OR")
SET = Class(name="SET")
siddhi_Expression = Class(name="siddhi::Expression")
siddhi_AS = Class(name="siddhi::AS")
siddhi_QueryInput = Class(name="siddhi::QueryInput")
siddhi_QuerySection = Class(name="siddhi::QuerySection")
siddhi_OutputRate = Class(name="siddhi::OutputRate")
siddhi_QueryOutput = Class(name="siddhi::QueryOutput")
INSERT = Class(name="INSERT")
INTO = Class(name="INTO")
DELETE = Class(name="DELETE")
FOR = Class(name="FOR")
UPDATE = Class(name="UPDATE")
siddhi_Target = Class(name="siddhi::Target")
siddhi_ON = Class(name="siddhi::ON")
siddhi_SetClause = Class(name="siddhi::SetClause")
siddhi_SetAssignment = Class(name="siddhi::SetAssignment")
ALL = Class(name="ALL")
EVENTS = Class(name="EVENTS")
RAW = Class(name="RAW")
EXPIRED = Class(name="EXPIRED")
CURRENT = Class(name="CURRENT")
SNAPSHOT = Class(name="SNAPSHOT")
siddhi_OutputRateType = Class(name="siddhi::OutputRateType")
LAST = Class(name="LAST")
FIRST = Class(name="FIRST")
SELECT = Class(name="SELECT")
siddhi_OutputAttribute = Class(name="siddhi::OutputAttribute")
siddhi_GroupBy = Class(name="siddhi::GroupBy")
siddhi_HavingExpr = Class(name="siddhi::HavingExpr")
GROUP = Class(name="GROUP")
HAVING = Class(name="HAVING")
siddhi_OutAttr = Class(name="siddhi::OutAttr")
siddhi_RightAbsentSequenceSource = Class(name="siddhi::RightAbsentSequenceSource")
siddhi_Attribute = Class(name="siddhi::Attribute")
siddhi_JoinStream = Class(name="siddhi::JoinStream")
siddhi_SequenceStream = Class(name="siddhi::SequenceStream")
siddhi_PatternStream = Class(name="siddhi::PatternStream")
siddhi_AnonymousStream = Class(name="siddhi::AnonymousStream")
siddhi_EverySequenceSourceChain = Class(name="siddhi::EverySequenceSourceChain")
siddhi_EveryAbsentSequenceSourceChain = Class(name="siddhi::EveryAbsentSequenceSourceChain")
siddhi_SequenceSource = Class(name="siddhi::SequenceSource")
siddhi_WithinTime = Class(name="siddhi::WithinTime")
siddhi_SequenceSourceChain = Class(name="siddhi::SequenceSourceChain")
siddhi_AbsentSequenceSourceChain = Class(name="siddhi::AbsentSequenceSourceChain")
siddhi_BasicAbsentPatternSource = Class(name="siddhi::BasicAbsentPatternSource")
siddhi_LeftAbsentSequenceSource = Class(name="siddhi::LeftAbsentSequenceSource")
siddhi_EObject = Class(name="siddhi::EObject")
SequenceSourceChain = Class(name="SequenceSourceChain")
siddhi_SequenceCollectionStatefulSource = Class(name="siddhi::SequenceCollectionStatefulSource")
SequenceSource = Class(name="SequenceSource")
siddhi_EveryPatternSourceChain = Class(name="siddhi::EveryPatternSourceChain")
PatternStream = Class(name="PatternStream")
siddhi_PatternSourceChain = Class(name="siddhi::PatternSourceChain")
siddhi_PatternSource = Class(name="siddhi::PatternSource")
siddhi_LogicalStatefulSource = Class(name="siddhi::LogicalStatefulSource")
siddhi_PatternCollectionStatefulSource = Class(name="siddhi::PatternCollectionStatefulSource")
siddhi_StandardStatefulSource = Class(name="siddhi::StandardStatefulSource")
siddhi_LogicalAbsentStatefulSource = Class(name="siddhi::LogicalAbsentStatefulSource")
siddhi_AND = Class(name="siddhi::AND")
siddhi_Collect = Class(name="siddhi::Collect")
siddhi_NOT = Class(name="siddhi::NOT")
siddhi_BasicSource = Class(name="siddhi::BasicSource")
siddhi_AbsentPatternSourceChain = Class(name="siddhi::AbsentPatternSourceChain")
siddhi_EveryAbsentPatternSource = Class(name="siddhi::EveryAbsentPatternSource")
AbsentPatternSourceChain = Class(name="AbsentPatternSourceChain")
siddhi_ForTime = Class(name="siddhi::ForTime")
siddhi_LeftAbsentPatternSource = Class(name="siddhi::LeftAbsentPatternSource")
siddhi_RightAbsentPatternSource = Class(name="siddhi::RightAbsentPatternSource")
siddhi_JoinSource = Class(name="siddhi::JoinSource")
siddhi_UNIDIRECTIONAL = Class(name="siddhi::UNIDIRECTIONAL")
siddhi_WithinTimeRange = Class(name="siddhi::WithinTimeRange")
siddhi_Per1 = Class(name="siddhi::Per1")
siddhi_joins = Class(name="siddhi::joins")
WITHIN = Class(name="WITHIN")
PER = Class(name="PER")
siddhi_StreamAlias = Class(name="siddhi::StreamAlias")
LEFT = Class(name="LEFT")
OUTER = Class(name="OUTER")
JOIN = Class(name="JOIN")
RIGHT = Class(name="RIGHT")
FULL = Class(name="FULL")
INNER = Class(name="INNER")
JoinStream = Class(name="JoinStream")
siddhi_MainSource = Class(name="siddhi::MainSource")
JoinSource = Class(name="JoinSource")
StandardStream = Class(name="StandardStream")
siddhi_Win = Class(name="siddhi::Win")
siddhi_BasicSourceStreamHandlers = Class(name="siddhi::BasicSourceStreamHandlers")
siddhi_BasicSourceStreamHandlers1 = Class(name="siddhi::BasicSourceStreamHandlers1")
siddhi_BasicSourceStreamHandler = Class(name="siddhi::BasicSourceStreamHandler")
siddhi_Filter = Class(name="siddhi::Filter")
siddhi_StreamFunction = Class(name="siddhi::StreamFunction")
siddhi_MathOperation = Class(name="siddhi::MathOperation")
Expression = Class(name="Expression")
siddhi_MathAddsubOperation = Class(name="siddhi::MathAddsubOperation")
MathOperation = Class(name="MathOperation")
siddhi_MathDivmulOperation = Class(name="siddhi::MathDivmulOperation")
MathAddsubOperation = Class(name="MathAddsubOperation")
siddhi_MathOtherOperations = Class(name="siddhi::MathOtherOperations")
MathDivmulOperation = Class(name="MathDivmulOperation")
siddhi_Literal = Class(name="siddhi::Literal")
siddhi_NullCheck = Class(name="siddhi::NullCheck")
MathOtherOperations = Class(name="MathOtherOperations")
IS = Class(name="IS")
NULL = Class(name="NULL")
siddhi_StreamReference = Class(name="siddhi::StreamReference")
siddhi_AttributeIndex = Class(name="siddhi::AttributeIndex")
siddhi_ConstantValue = Class(name="siddhi::ConstantValue")
SetAssignment = Class(name="SetAssignment")
siddhi_SourceOrEventReference = Class(name="siddhi::SourceOrEventReference")
siddhi_FeaturesOrOutAttrReference = Class(name="siddhi::FeaturesOrOutAttrReference")
siddhi_FeaturesOrOutAttr = Class(name="siddhi::FeaturesOrOutAttr")
SequenceCollectionStatefulSource = Class(name="SequenceCollectionStatefulSource")
PatternCollectionStatefulSource = Class(name="PatternCollectionStatefulSource")
siddhi_Source1OrStandardStatefulSource = Class(name="siddhi::Source1OrStandardStatefulSource")
siddhi_AttributeNameReference = Class(name="siddhi::AttributeNameReference")
siddhi_BoolValue = Class(name="siddhi::BoolValue")
siddhi_SignedDoubleValue = Class(name="siddhi::SignedDoubleValue")
siddhi_SignedFloatValue = Class(name="siddhi::SignedFloatValue")
siddhi_SignedLongValue = Class(name="siddhi::SignedLongValue")
siddhi_FunctionNamespace = Class(name="siddhi::FunctionNamespace")
siddhi_FunctionId = Class(name="siddhi::FunctionId")
siddhi_AttributeList = Class(name="siddhi::AttributeList")
TRUE = Class(name="TRUE")
FALSE = Class(name="FALSE")
siddhi_YearValue = Class(name="siddhi::YearValue")
siddhi_MonthValue = Class(name="siddhi::MonthValue")
siddhi_WeekValue = Class(name="siddhi::WeekValue")
siddhi_DayValue = Class(name="siddhi::DayValue")
siddhi_HourValue = Class(name="siddhi::HourValue")
siddhi_MinuteValue = Class(name="siddhi::MinuteValue")
siddhi_SecondValue = Class(name="siddhi::SecondValue")
siddhi_MillisecondValue = Class(name="siddhi::MillisecondValue")
MILLISECONDS = Class(name="MILLISECONDS")
siddhi_DOUBLE_LITERAL = Class(name="siddhi::DOUBLE::LITERAL")
SignedDoubleValue = Class(name="SignedDoubleValue")
siddhi_E = Class(name="siddhi::E")
siddhi_D = Class(name="siddhi::D")
siddhi_FLOAT_LITERAL = Class(name="siddhi::FLOAT::LITERAL")
SignedFloatValue = Class(name="SignedFloatValue")
siddhi_F = Class(name="siddhi::F")
siddhi_LONG_LITERAL = Class(name="siddhi::LONG::LITERAL")
SignedLongValue = Class(name="SignedLongValue")
siddhi_L = Class(name="siddhi::L")
siddhi_Keyword = Class(name="siddhi::Keyword")
Name = Class(name="Name")
siddhi_APP = Class(name="siddhi::APP")
AppAnnotation = Class(name="AppAnnotation")
LogicalAbsentStatefulSource = Class(name="LogicalAbsentStatefulSource")
BasicAbsentPatternSource = Class(name="BasicAbsentPatternSource")
siddhi_STREAM = Class(name="siddhi::STREAM")
siddhi_DEFINE = Class(name="siddhi::DEFINE")
siddhi_TABLE = Class(name="siddhi::TABLE")
siddhi_WINDOW = Class(name="siddhi::WINDOW")
EverySequenceSourceChain = Class(name="EverySequenceSourceChain")
EveryAbsentSequenceSourceChain = Class(name="EveryAbsentSequenceSourceChain")
EveryAbsentPatternSource = Class(name="EveryAbsentPatternSource")
LeftAbsentPatternSource = Class(name="LeftAbsentPatternSource")
RightAbsentPatternSource = Class(name="RightAbsentPatternSource")
siddhi_IN = Class(name="siddhi::IN")
siddhi_LONG = Class(name="siddhi::LONG")
siddhi_DOUBLE = Class(name="siddhi::DOUBLE")
siddhi_FLOAT = Class(name="siddhi::FLOAT")
siddhi_BOOL = Class(name="siddhi::BOOL")
siddhi_OBJECT = Class(name="siddhi::OBJECT")
siddhi_ALL = Class(name="siddhi::ALL")
siddhi_EVENTS = Class(name="siddhi::EVENTS")
siddhi_RAW = Class(name="siddhi::RAW")
siddhi_EXPIRED = Class(name="siddhi::EXPIRED")
siddhi_OUTPUT = Class(name="siddhi::OUTPUT")
siddhi_STRINGS = Class(name="siddhi::STRINGS")
siddhi_INTS = Class(name="siddhi::INTS")
siddhi_INTO = Class(name="siddhi::INTO")
siddhi_RETURN = Class(name="siddhi::RETURN")
siddhi_FROM = Class(name="siddhi::FROM")
siddhi_WITHIN = Class(name="siddhi::WITHIN")
siddhi_LEFT = Class(name="siddhi::LEFT")
siddhi_RIGHT = Class(name="siddhi::RIGHT")
siddhi_FULL = Class(name="siddhi::FULL")
siddhi_JOIN = Class(name="siddhi::JOIN")
siddhi_INNER = Class(name="siddhi::INNER")
siddhi_OUTER = Class(name="siddhi::OUTER")
siddhi_CURRENT = Class(name="siddhi::CURRENT")
siddhi_SELECT = Class(name="siddhi::SELECT")
siddhi_LAST = Class(name="siddhi::LAST")
siddhi_GROUP = Class(name="siddhi::GROUP")
siddhi_IS = Class(name="siddhi::IS")
siddhi_BY = Class(name="siddhi::BY")
siddhi_NULL = Class(name="siddhi::NULL")
siddhi_HAVING = Class(name="siddhi::HAVING")
siddhi_TRIGGER = Class(name="siddhi::TRIGGER")
siddhi_SNAPSHOT = Class(name="siddhi::SNAPSHOT")
siddhi_AT = Class(name="siddhi::AT")
siddhi_FIRST = Class(name="siddhi::FIRST")
siddhi_INSERT = Class(name="siddhi::INSERT")
siddhi_FUNCTION = Class(name="siddhi::FUNCTION")
siddhi_WEEKS = Class(name="siddhi::WEEKS")
siddhi_BEGIN = Class(name="siddhi::BEGIN")
siddhi_PLAN = Class(name="siddhi::PLAN")
siddhi_DELETE = Class(name="siddhi::DELETE")
siddhi_FOR = Class(name="siddhi::FOR")
siddhi_UPDATE = Class(name="siddhi::UPDATE")
siddhi_END = Class(name="siddhi::END")
siddhi_PARTITION = Class(name="siddhi::PARTITION")
siddhi_WITH = Class(name="siddhi::WITH")
siddhi_AGGREGATION = Class(name="siddhi::AGGREGATION")
siddhi_AGGREGATE = Class(name="siddhi::AGGREGATE")
siddhi_SET = Class(name="siddhi::SET")
siddhi_PER = Class(name="siddhi::PER")
siddhi_YEARS = Class(name="siddhi::YEARS")
siddhi_MONTHS = Class(name="siddhi::MONTHS")
siddhi_DAYS = Class(name="siddhi::DAYS")
siddhi_HOURS = Class(name="siddhi::HOURS")
siddhi_MINUTES = Class(name="siddhi::MINUTES")
siddhi_SECONDS = Class(name="siddhi::SECONDS")
siddhi_MILLISECONDS = Class(name="siddhi::MILLISECONDS")
siddhi_FALSE = Class(name="siddhi::FALSE")
siddhi_TRUE = Class(name="siddhi::TRUE")
siddhi_LeftAbsentSequenceSource1 = Class(name="siddhi::LeftAbsentSequenceSource1")
LeftAbsentSequenceSource = Class(name="LeftAbsentSequenceSource")
siddhi_RightAbsentSequenceSource1 = Class(name="siddhi::RightAbsentSequenceSource1")
RightAbsentSequenceSource = Class(name="RightAbsentSequenceSource")
siddhi_LeftAbsentPatternSource1 = Class(name="siddhi::LeftAbsentPatternSource1")
siddhi_RightAbsentPatternSource1 = Class(name="siddhi::RightAbsentPatternSource1")
siddhi_MathLogicalOperation = Class(name="siddhi::MathLogicalOperation")
siddhi_MathInOperation = Class(name="siddhi::MathInOperation")
siddhi_MathGtLtOperation = Class(name="siddhi::MathGtLtOperation")
siddhi_MathEqualOperation = Class(name="siddhi::MathEqualOperation")
siddhi_NotOperation = Class(name="siddhi::NotOperation")

# siddhi_DefinitionAggregation class attributes and methods

# siddhi_ExecutionElement class attributes and methods

# siddhi_SiddhiQL class attributes and methods

# siddhi_ExecutionPlan class attributes and methods

# siddhi_AppAnnotation class attributes and methods

# siddhi_DefinitionStream class attributes and methods

# siddhi_DefinitionTable class attributes and methods

# siddhi_DefinitionWindow class attributes and methods

# siddhi_DefinitionTrigger class attributes and methods

# siddhi_DefinitionFunction class attributes and methods

# siddhi_ExecPartition class attributes and methods

# siddhi_Query class attributes and methods

# DEFINE class attributes and methods

# STREAM class attributes and methods

# siddhi_Annotation class attributes and methods

# siddhi_Source1 class attributes and methods
siddhi_Source1_inner: Property = Property(name="inner", type=StringType)
siddhi_Source1.attributes={siddhi_Source1_inner}

# siddhi_Features class attributes and methods

# TABLE class attributes and methods

# WINDOW class attributes and methods

# OUTPUT class attributes and methods

# siddhi_AttributeType class attributes and methods

# siddhi_FunctionOperation class attributes and methods

# siddhi_OutputEventType class attributes and methods

# TRIGGER class attributes and methods

# AT class attributes and methods

# siddhi_TriggerName class attributes and methods
siddhi_TriggerName_id: Property = Property(name="id", type=StringType)
siddhi_TriggerName.attributes={siddhi_TriggerName_id}

# siddhi_EVERY class attributes and methods
siddhi_EVERY_every1: Property = Property(name="every1", type=StringType)
siddhi_EVERY.attributes={siddhi_EVERY_every1}

# siddhi_TimeValue class attributes and methods

# siddhi_StringValue class attributes and methods
siddhi_StringValue_sl: Property = Property(name="sl", type=StringType)
siddhi_StringValue.attributes={siddhi_StringValue_sl}

# FUNCTION class attributes and methods

# RETURN class attributes and methods

# siddhi_FunctionName class attributes and methods
siddhi_FunctionName_id: Property = Property(name="id", type=StringType)
siddhi_FunctionName.attributes={siddhi_FunctionName_id}

# siddhi_LanguageName class attributes and methods
siddhi_LanguageName_id: Property = Property(name="id", type=StringType)
siddhi_LanguageName.attributes={siddhi_LanguageName_id}

# siddhi_FunctionBody class attributes and methods
siddhi_FunctionBody_value: Property = Property(name="value", type=StringType)
siddhi_FunctionBody.attributes={siddhi_FunctionBody_value}

# AGGREGATION class attributes and methods

# FROM class attributes and methods

# AGGREGATE class attributes and methods

# BY class attributes and methods

# siddhi_StandardStream class attributes and methods

# siddhi_GroupByQuerySelection class attributes and methods

# siddhi_AttributeReference class attributes and methods
siddhi_AttributeReference_name: Property = Property(name="name", type=StringType)
siddhi_AttributeReference_hash1: Property = Property(name="hash1", type=StringType)
siddhi_AttributeReference_hash2: Property = Property(name="hash2", type=StringType)
siddhi_AttributeReference.attributes={siddhi_AttributeReference_hash1, siddhi_AttributeReference_hash2, siddhi_AttributeReference_name}

# siddhi_AggregationTime class attributes and methods

# siddhi_AggregationTimeDuration class attributes and methods

# siddhi_AggregationTimeInterval class attributes and methods

# AggregationTime class attributes and methods

# SECONDS class attributes and methods

# MINUTES class attributes and methods

# HOURS class attributes and methods

# DAYS class attributes and methods

# WEEKS class attributes and methods

# MONTHS class attributes and methods

# YEARS class attributes and methods

# siddhi_AggregationTimeRange class attributes and methods

# siddhi_Name class attributes and methods
siddhi_Name_na: Property = Property(name="na", type=StringType)
siddhi_Name.attributes={siddhi_Name_na}

# siddhi_AnnotationElement class attributes and methods

# siddhi_PropertyName class attributes and methods

# siddhi_PropertyValue class attributes and methods

# siddhi_PropertySeparator class attributes and methods

# FeaturesOrOutAttr class attributes and methods

# STRINGS class attributes and methods

# INTS class attributes and methods

# LONG class attributes and methods

# FLOAT class attributes and methods

# DOUBLE class attributes and methods

# BOOL class attributes and methods

# OBJECT class attributes and methods

# siddhi_Source class attributes and methods

# Source1OrStandardStatefulSource class attributes and methods

# PARTITION class attributes and methods

# WITH class attributes and methods

# BEGIN class attributes and methods

# END class attributes and methods

# siddhi_PartitionWithStream class attributes and methods

# siddhi_ConditionRanges class attributes and methods

# PartitionWithStream class attributes and methods

# siddhi_OF class attributes and methods
siddhi_OF_of: Property = Property(name="of", type=StringType)
siddhi_OF.attributes={siddhi_OF_of}

# siddhi_ConditionRange class attributes and methods

# siddhi_OR class attributes and methods
siddhi_OR_or: Property = Property(name="or", type=StringType)
siddhi_OR.attributes={siddhi_OR_or}

# SET class attributes and methods

# siddhi_Expression class attributes and methods

# siddhi_AS class attributes and methods
siddhi_AS_a: Property = Property(name="a", type=StringType)
siddhi_AS.attributes={siddhi_AS_a}

# siddhi_QueryInput class attributes and methods

# siddhi_QuerySection class attributes and methods

# siddhi_OutputRate class attributes and methods

# siddhi_QueryOutput class attributes and methods

# INSERT class attributes and methods

# INTO class attributes and methods

# DELETE class attributes and methods

# FOR class attributes and methods

# UPDATE class attributes and methods

# siddhi_Target class attributes and methods

# siddhi_ON class attributes and methods
siddhi_ON_on: Property = Property(name="on", type=StringType)
siddhi_ON.attributes={siddhi_ON_on}

# siddhi_SetClause class attributes and methods

# siddhi_SetAssignment class attributes and methods

# ALL class attributes and methods

# EVENTS class attributes and methods

# RAW class attributes and methods

# EXPIRED class attributes and methods

# CURRENT class attributes and methods

# SNAPSHOT class attributes and methods

# siddhi_OutputRateType class attributes and methods

# LAST class attributes and methods

# FIRST class attributes and methods

# SELECT class attributes and methods

# siddhi_OutputAttribute class attributes and methods

# siddhi_GroupBy class attributes and methods

# siddhi_HavingExpr class attributes and methods

# GROUP class attributes and methods

# HAVING class attributes and methods

# siddhi_OutAttr class attributes and methods

# siddhi_RightAbsentSequenceSource class attributes and methods
siddhi_RightAbsentSequenceSource_comm: Property = Property(name="comm", type=StringType)
siddhi_RightAbsentSequenceSource_op: Property = Property(name="op", type=StringType)
siddhi_RightAbsentSequenceSource_cp: Property = Property(name="cp", type=StringType)
siddhi_RightAbsentSequenceSource_comma: Property = Property(name="comma", type=StringType)
siddhi_RightAbsentSequenceSource.attributes={siddhi_RightAbsentSequenceSource_comm, siddhi_RightAbsentSequenceSource_cp, siddhi_RightAbsentSequenceSource_op, siddhi_RightAbsentSequenceSource_comma}

# siddhi_Attribute class attributes and methods

# siddhi_JoinStream class attributes and methods

# siddhi_SequenceStream class attributes and methods

# siddhi_PatternStream class attributes and methods

# siddhi_AnonymousStream class attributes and methods

# siddhi_EverySequenceSourceChain class attributes and methods

# siddhi_EveryAbsentSequenceSourceChain class attributes and methods

# siddhi_SequenceSource class attributes and methods

# siddhi_WithinTime class attributes and methods

# siddhi_SequenceSourceChain class attributes and methods
siddhi_SequenceSourceChain_op: Property = Property(name="op", type=StringType)
siddhi_SequenceSourceChain.attributes={siddhi_SequenceSourceChain_op}

# siddhi_AbsentSequenceSourceChain class attributes and methods

# siddhi_BasicAbsentPatternSource class attributes and methods

# siddhi_LeftAbsentSequenceSource class attributes and methods
siddhi_LeftAbsentSequenceSource_comm: Property = Property(name="comm", type=StringType)
siddhi_LeftAbsentSequenceSource_op: Property = Property(name="op", type=StringType)
siddhi_LeftAbsentSequenceSource_cp: Property = Property(name="cp", type=StringType)
siddhi_LeftAbsentSequenceSource_comma: Property = Property(name="comma", type=StringType)
siddhi_LeftAbsentSequenceSource.attributes={siddhi_LeftAbsentSequenceSource_comma, siddhi_LeftAbsentSequenceSource_comm, siddhi_LeftAbsentSequenceSource_op, siddhi_LeftAbsentSequenceSource_cp}

# siddhi_EObject class attributes and methods

# SequenceSourceChain class attributes and methods

# siddhi_SequenceCollectionStatefulSource class attributes and methods

# SequenceSource class attributes and methods

# siddhi_EveryPatternSourceChain class attributes and methods
siddhi_EveryPatternSourceChain_op: Property = Property(name="op", type=StringType)
siddhi_EveryPatternSourceChain.attributes={siddhi_EveryPatternSourceChain_op}

# PatternStream class attributes and methods

# siddhi_PatternSourceChain class attributes and methods
siddhi_PatternSourceChain_op: Property = Property(name="op", type=StringType)
siddhi_PatternSourceChain.attributes={siddhi_PatternSourceChain_op}

# siddhi_PatternSource class attributes and methods

# siddhi_LogicalStatefulSource class attributes and methods

# siddhi_PatternCollectionStatefulSource class attributes and methods

# siddhi_StandardStatefulSource class attributes and methods
siddhi_StandardStatefulSource_zero_or_more: Property = Property(name="zero_or_more", type=StringType)
siddhi_StandardStatefulSource_zero_or_one: Property = Property(name="zero_or_one", type=StringType)
siddhi_StandardStatefulSource_one_or_more: Property = Property(name="one_or_more", type=StringType)
siddhi_StandardStatefulSource.attributes={siddhi_StandardStatefulSource_zero_or_more, siddhi_StandardStatefulSource_zero_or_one, siddhi_StandardStatefulSource_one_or_more}

# siddhi_LogicalAbsentStatefulSource class attributes and methods

# siddhi_AND class attributes and methods
siddhi_AND_and: Property = Property(name="and", type=StringType)
siddhi_AND.attributes={siddhi_AND_and}

# siddhi_Collect class attributes and methods
siddhi_Collect_start: Property = Property(name="start", type=StringType)
siddhi_Collect_end: Property = Property(name="end", type=StringType)
siddhi_Collect.attributes={siddhi_Collect_end, siddhi_Collect_start}

# siddhi_NOT class attributes and methods
siddhi_NOT_not1: Property = Property(name="not1", type=StringType)
siddhi_NOT.attributes={siddhi_NOT_not1}

# siddhi_BasicSource class attributes and methods

# siddhi_AbsentPatternSourceChain class attributes and methods

# siddhi_EveryAbsentPatternSource class attributes and methods

# AbsentPatternSourceChain class attributes and methods

# siddhi_ForTime class attributes and methods

# siddhi_LeftAbsentPatternSource class attributes and methods
siddhi_LeftAbsentPatternSource_fb1: Property = Property(name="fb1", type=StringType)
siddhi_LeftAbsentPatternSource.attributes={siddhi_LeftAbsentPatternSource_fb1}

# siddhi_RightAbsentPatternSource class attributes and methods
siddhi_RightAbsentPatternSource_fb2: Property = Property(name="fb2", type=StringType)
siddhi_RightAbsentPatternSource.attributes={siddhi_RightAbsentPatternSource_fb2}

# siddhi_JoinSource class attributes and methods

# siddhi_UNIDIRECTIONAL class attributes and methods
siddhi_UNIDIRECTIONAL_unidirectional: Property = Property(name="unidirectional", type=StringType)
siddhi_UNIDIRECTIONAL.attributes={siddhi_UNIDIRECTIONAL_unidirectional}

# siddhi_WithinTimeRange class attributes and methods

# siddhi_Per1 class attributes and methods

# siddhi_joins class attributes and methods

# WITHIN class attributes and methods

# PER class attributes and methods

# siddhi_StreamAlias class attributes and methods

# LEFT class attributes and methods

# OUTER class attributes and methods

# JOIN class attributes and methods

# RIGHT class attributes and methods

# FULL class attributes and methods

# INNER class attributes and methods

# JoinStream class attributes and methods

# siddhi_MainSource class attributes and methods

# JoinSource class attributes and methods

# StandardStream class attributes and methods

# siddhi_Win class attributes and methods

# siddhi_BasicSourceStreamHandlers class attributes and methods

# siddhi_BasicSourceStreamHandlers1 class attributes and methods

# siddhi_BasicSourceStreamHandler class attributes and methods

# siddhi_Filter class attributes and methods

# siddhi_StreamFunction class attributes and methods

# siddhi_MathOperation class attributes and methods

# Expression class attributes and methods

# siddhi_MathAddsubOperation class attributes and methods
siddhi_MathAddsubOperation_add: Property = Property(name="add", type=StringType)
siddhi_MathAddsubOperation_substract: Property = Property(name="substract", type=StringType)
siddhi_MathAddsubOperation.attributes={siddhi_MathAddsubOperation_substract, siddhi_MathAddsubOperation_add}

# MathOperation class attributes and methods

# siddhi_MathDivmulOperation class attributes and methods
siddhi_MathDivmulOperation_multiply: Property = Property(name="multiply", type=StringType)
siddhi_MathDivmulOperation_devide: Property = Property(name="devide", type=StringType)
siddhi_MathDivmulOperation_mod: Property = Property(name="mod", type=StringType)
siddhi_MathDivmulOperation.attributes={siddhi_MathDivmulOperation_mod, siddhi_MathDivmulOperation_multiply, siddhi_MathDivmulOperation_devide}

# MathAddsubOperation class attributes and methods

# siddhi_MathOtherOperations class attributes and methods

# MathDivmulOperation class attributes and methods

# siddhi_Literal class attributes and methods

# siddhi_NullCheck class attributes and methods

# MathOtherOperations class attributes and methods

# IS class attributes and methods

# NULL class attributes and methods

# siddhi_StreamReference class attributes and methods
siddhi_StreamReference_hash: Property = Property(name="hash", type=StringType)
siddhi_StreamReference.attributes={siddhi_StreamReference_hash}

# siddhi_AttributeIndex class attributes and methods

# siddhi_ConstantValue class attributes and methods
siddhi_ConstantValue_siv: Property = Property(name="siv", type=StringType)
siddhi_ConstantValue.attributes={siddhi_ConstantValue_siv}

# SetAssignment class attributes and methods

# siddhi_SourceOrEventReference class attributes and methods

# siddhi_FeaturesOrOutAttrReference class attributes and methods

# siddhi_FeaturesOrOutAttr class attributes and methods
siddhi_FeaturesOrOutAttr_name: Property = Property(name="name", type=StringType)
siddhi_FeaturesOrOutAttr.attributes={siddhi_FeaturesOrOutAttr_name}

# SequenceCollectionStatefulSource class attributes and methods

# PatternCollectionStatefulSource class attributes and methods

# siddhi_Source1OrStandardStatefulSource class attributes and methods
siddhi_Source1OrStandardStatefulSource_name: Property = Property(name="name", type=StringType)
siddhi_Source1OrStandardStatefulSource.attributes={siddhi_Source1OrStandardStatefulSource_name}

# siddhi_AttributeNameReference class attributes and methods

# siddhi_BoolValue class attributes and methods

# siddhi_SignedDoubleValue class attributes and methods

# siddhi_SignedFloatValue class attributes and methods

# siddhi_SignedLongValue class attributes and methods

# siddhi_FunctionNamespace class attributes and methods

# siddhi_FunctionId class attributes and methods

# siddhi_AttributeList class attributes and methods

# TRUE class attributes and methods

# FALSE class attributes and methods

# siddhi_YearValue class attributes and methods

# siddhi_MonthValue class attributes and methods

# siddhi_WeekValue class attributes and methods

# siddhi_DayValue class attributes and methods

# siddhi_HourValue class attributes and methods

# siddhi_MinuteValue class attributes and methods

# siddhi_SecondValue class attributes and methods

# siddhi_MillisecondValue class attributes and methods

# MILLISECONDS class attributes and methods

# siddhi_DOUBLE_LITERAL class attributes and methods

# SignedDoubleValue class attributes and methods

# siddhi_E class attributes and methods
siddhi_E_e: Property = Property(name="e", type=StringType)
siddhi_E.attributes={siddhi_E_e}

# siddhi_D class attributes and methods
siddhi_D_d: Property = Property(name="d", type=StringType)
siddhi_D.attributes={siddhi_D_d}

# siddhi_FLOAT_LITERAL class attributes and methods

# SignedFloatValue class attributes and methods

# siddhi_F class attributes and methods
siddhi_F_f: Property = Property(name="f", type=StringType)
siddhi_F.attributes={siddhi_F_f}

# siddhi_LONG_LITERAL class attributes and methods

# SignedLongValue class attributes and methods

# siddhi_L class attributes and methods
siddhi_L_l: Property = Property(name="l", type=StringType)
siddhi_L.attributes={siddhi_L_l}

# siddhi_Keyword class attributes and methods

# Name class attributes and methods

# siddhi_APP class attributes and methods
siddhi_APP_ap: Property = Property(name="ap", type=StringType)
siddhi_APP.attributes={siddhi_APP_ap}

# AppAnnotation class attributes and methods

# LogicalAbsentStatefulSource class attributes and methods

# BasicAbsentPatternSource class attributes and methods

# siddhi_STREAM class attributes and methods
siddhi_STREAM_str: Property = Property(name="str", type=StringType)
siddhi_STREAM.attributes={siddhi_STREAM_str}

# siddhi_DEFINE class attributes and methods
siddhi_DEFINE_define: Property = Property(name="define", type=StringType)
siddhi_DEFINE.attributes={siddhi_DEFINE_define}

# siddhi_TABLE class attributes and methods
siddhi_TABLE_table: Property = Property(name="table", type=StringType)
siddhi_TABLE.attributes={siddhi_TABLE_table}

# siddhi_WINDOW class attributes and methods
siddhi_WINDOW_window: Property = Property(name="window", type=StringType)
siddhi_WINDOW.attributes={siddhi_WINDOW_window}

# EverySequenceSourceChain class attributes and methods

# EveryAbsentSequenceSourceChain class attributes and methods

# EveryAbsentPatternSource class attributes and methods

# LeftAbsentPatternSource class attributes and methods

# RightAbsentPatternSource class attributes and methods

# siddhi_IN class attributes and methods
siddhi_IN_in: Property = Property(name="in", type=StringType)
siddhi_IN.attributes={siddhi_IN_in}

# siddhi_LONG class attributes and methods
siddhi_LONG_long: Property = Property(name="long", type=StringType)
siddhi_LONG.attributes={siddhi_LONG_long}

# siddhi_DOUBLE class attributes and methods
siddhi_DOUBLE_double: Property = Property(name="double", type=StringType)
siddhi_DOUBLE.attributes={siddhi_DOUBLE_double}

# siddhi_FLOAT class attributes and methods
siddhi_FLOAT_float: Property = Property(name="float", type=StringType)
siddhi_FLOAT.attributes={siddhi_FLOAT_float}

# siddhi_BOOL class attributes and methods
siddhi_BOOL_bool: Property = Property(name="bool", type=StringType)
siddhi_BOOL.attributes={siddhi_BOOL_bool}

# siddhi_OBJECT class attributes and methods
siddhi_OBJECT_object: Property = Property(name="object", type=StringType)
siddhi_OBJECT.attributes={siddhi_OBJECT_object}

# siddhi_ALL class attributes and methods
siddhi_ALL_all: Property = Property(name="all", type=StringType)
siddhi_ALL.attributes={siddhi_ALL_all}

# siddhi_EVENTS class attributes and methods
siddhi_EVENTS_events: Property = Property(name="events", type=StringType)
siddhi_EVENTS.attributes={siddhi_EVENTS_events}

# siddhi_RAW class attributes and methods
siddhi_RAW_raw: Property = Property(name="raw", type=StringType)
siddhi_RAW.attributes={siddhi_RAW_raw}

# siddhi_EXPIRED class attributes and methods
siddhi_EXPIRED_expired: Property = Property(name="expired", type=StringType)
siddhi_EXPIRED.attributes={siddhi_EXPIRED_expired}

# siddhi_OUTPUT class attributes and methods
siddhi_OUTPUT_output: Property = Property(name="output", type=StringType)
siddhi_OUTPUT.attributes={siddhi_OUTPUT_output}

# siddhi_STRINGS class attributes and methods
siddhi_STRINGS_string: Property = Property(name="string", type=StringType)
siddhi_STRINGS.attributes={siddhi_STRINGS_string}

# siddhi_INTS class attributes and methods
siddhi_INTS_int: Property = Property(name="int", type=StringType)
siddhi_INTS.attributes={siddhi_INTS_int}

# siddhi_INTO class attributes and methods
siddhi_INTO_into: Property = Property(name="into", type=StringType)
siddhi_INTO.attributes={siddhi_INTO_into}

# siddhi_RETURN class attributes and methods
siddhi_RETURN_return: Property = Property(name="return", type=StringType)
siddhi_RETURN.attributes={siddhi_RETURN_return}

# siddhi_FROM class attributes and methods
siddhi_FROM_from: Property = Property(name="from", type=StringType)
siddhi_FROM.attributes={siddhi_FROM_from}

# siddhi_WITHIN class attributes and methods
siddhi_WITHIN_within: Property = Property(name="within", type=StringType)
siddhi_WITHIN.attributes={siddhi_WITHIN_within}

# siddhi_LEFT class attributes and methods
siddhi_LEFT_left: Property = Property(name="left", type=StringType)
siddhi_LEFT.attributes={siddhi_LEFT_left}

# siddhi_RIGHT class attributes and methods
siddhi_RIGHT_right: Property = Property(name="right", type=StringType)
siddhi_RIGHT.attributes={siddhi_RIGHT_right}

# siddhi_FULL class attributes and methods
siddhi_FULL_full: Property = Property(name="full", type=StringType)
siddhi_FULL.attributes={siddhi_FULL_full}

# siddhi_JOIN class attributes and methods
siddhi_JOIN_join: Property = Property(name="join", type=StringType)
siddhi_JOIN.attributes={siddhi_JOIN_join}

# siddhi_INNER class attributes and methods
siddhi_INNER_inner: Property = Property(name="inner", type=StringType)
siddhi_INNER.attributes={siddhi_INNER_inner}

# siddhi_OUTER class attributes and methods
siddhi_OUTER_outer: Property = Property(name="outer", type=StringType)
siddhi_OUTER.attributes={siddhi_OUTER_outer}

# siddhi_CURRENT class attributes and methods
siddhi_CURRENT_currt: Property = Property(name="currt", type=StringType)
siddhi_CURRENT.attributes={siddhi_CURRENT_currt}

# siddhi_SELECT class attributes and methods
siddhi_SELECT_select: Property = Property(name="select", type=StringType)
siddhi_SELECT.attributes={siddhi_SELECT_select}

# siddhi_LAST class attributes and methods
siddhi_LAST_last: Property = Property(name="last", type=StringType)
siddhi_LAST.attributes={siddhi_LAST_last}

# siddhi_GROUP class attributes and methods
siddhi_GROUP_group: Property = Property(name="group", type=StringType)
siddhi_GROUP.attributes={siddhi_GROUP_group}

# siddhi_IS class attributes and methods
siddhi_IS_is: Property = Property(name="is", type=StringType)
siddhi_IS.attributes={siddhi_IS_is}

# siddhi_BY class attributes and methods
siddhi_BY_by: Property = Property(name="by", type=StringType)
siddhi_BY.attributes={siddhi_BY_by}

# siddhi_NULL class attributes and methods
siddhi_NULL_null: Property = Property(name="null", type=StringType)
siddhi_NULL.attributes={siddhi_NULL_null}

# siddhi_HAVING class attributes and methods
siddhi_HAVING_having: Property = Property(name="having", type=StringType)
siddhi_HAVING.attributes={siddhi_HAVING_having}

# siddhi_TRIGGER class attributes and methods
siddhi_TRIGGER_trigger: Property = Property(name="trigger", type=StringType)
siddhi_TRIGGER.attributes={siddhi_TRIGGER_trigger}

# siddhi_SNAPSHOT class attributes and methods
siddhi_SNAPSHOT_snapshot: Property = Property(name="snapshot", type=StringType)
siddhi_SNAPSHOT.attributes={siddhi_SNAPSHOT_snapshot}

# siddhi_AT class attributes and methods
siddhi_AT_at: Property = Property(name="at", type=StringType)
siddhi_AT.attributes={siddhi_AT_at}

# siddhi_FIRST class attributes and methods
siddhi_FIRST_first: Property = Property(name="first", type=StringType)
siddhi_FIRST.attributes={siddhi_FIRST_first}

# siddhi_INSERT class attributes and methods
siddhi_INSERT_insert: Property = Property(name="insert", type=StringType)
siddhi_INSERT.attributes={siddhi_INSERT_insert}

# siddhi_FUNCTION class attributes and methods
siddhi_FUNCTION_function: Property = Property(name="function", type=StringType)
siddhi_FUNCTION.attributes={siddhi_FUNCTION_function}

# siddhi_WEEKS class attributes and methods
siddhi_WEEKS_week: Property = Property(name="week", type=StringType)
siddhi_WEEKS_weeks: Property = Property(name="weeks", type=StringType)
siddhi_WEEKS.attributes={siddhi_WEEKS_weeks, siddhi_WEEKS_week}

# siddhi_BEGIN class attributes and methods
siddhi_BEGIN_begin: Property = Property(name="begin", type=StringType)
siddhi_BEGIN.attributes={siddhi_BEGIN_begin}

# siddhi_PLAN class attributes and methods
siddhi_PLAN_plan: Property = Property(name="plan", type=StringType)
siddhi_PLAN.attributes={siddhi_PLAN_plan}

# siddhi_DELETE class attributes and methods
siddhi_DELETE_delete: Property = Property(name="delete", type=StringType)
siddhi_DELETE.attributes={siddhi_DELETE_delete}

# siddhi_FOR class attributes and methods
siddhi_FOR_for: Property = Property(name="for", type=StringType)
siddhi_FOR.attributes={siddhi_FOR_for}

# siddhi_UPDATE class attributes and methods
siddhi_UPDATE_update: Property = Property(name="update", type=StringType)
siddhi_UPDATE.attributes={siddhi_UPDATE_update}

# siddhi_END class attributes and methods
siddhi_END_end: Property = Property(name="end", type=StringType)
siddhi_END.attributes={siddhi_END_end}

# siddhi_PARTITION class attributes and methods
siddhi_PARTITION_partition: Property = Property(name="partition", type=StringType)
siddhi_PARTITION.attributes={siddhi_PARTITION_partition}

# siddhi_WITH class attributes and methods
siddhi_WITH_wi: Property = Property(name="wi", type=StringType)
siddhi_WITH.attributes={siddhi_WITH_wi}

# siddhi_AGGREGATION class attributes and methods
siddhi_AGGREGATION_aggre: Property = Property(name="aggre", type=StringType)
siddhi_AGGREGATION.attributes={siddhi_AGGREGATION_aggre}

# siddhi_AGGREGATE class attributes and methods
siddhi_AGGREGATE_agrregate: Property = Property(name="agrregate", type=StringType)
siddhi_AGGREGATE.attributes={siddhi_AGGREGATE_agrregate}

# siddhi_SET class attributes and methods
siddhi_SET_set: Property = Property(name="set", type=StringType)
siddhi_SET.attributes={siddhi_SET_set}

# siddhi_PER class attributes and methods
siddhi_PER_per: Property = Property(name="per", type=StringType)
siddhi_PER.attributes={siddhi_PER_per}

# siddhi_YEARS class attributes and methods
siddhi_YEARS_year: Property = Property(name="year", type=StringType)
siddhi_YEARS_years: Property = Property(name="years", type=StringType)
siddhi_YEARS.attributes={siddhi_YEARS_years, siddhi_YEARS_year}

# siddhi_MONTHS class attributes and methods
siddhi_MONTHS_month: Property = Property(name="month", type=StringType)
siddhi_MONTHS_months: Property = Property(name="months", type=StringType)
siddhi_MONTHS.attributes={siddhi_MONTHS_months, siddhi_MONTHS_month}

# siddhi_DAYS class attributes and methods
siddhi_DAYS_day: Property = Property(name="day", type=StringType)
siddhi_DAYS_days: Property = Property(name="days", type=StringType)
siddhi_DAYS.attributes={siddhi_DAYS_days, siddhi_DAYS_day}

# siddhi_HOURS class attributes and methods
siddhi_HOURS_hour: Property = Property(name="hour", type=StringType)
siddhi_HOURS_hours: Property = Property(name="hours", type=StringType)
siddhi_HOURS.attributes={siddhi_HOURS_hours, siddhi_HOURS_hour}

# siddhi_MINUTES class attributes and methods
siddhi_MINUTES_minute: Property = Property(name="minute", type=StringType)
siddhi_MINUTES_minutes: Property = Property(name="minutes", type=StringType)
siddhi_MINUTES_min: Property = Property(name="min", type=StringType)
siddhi_MINUTES.attributes={siddhi_MINUTES_minutes, siddhi_MINUTES_minute, siddhi_MINUTES_min}

# siddhi_SECONDS class attributes and methods
siddhi_SECONDS_seconds: Property = Property(name="seconds", type=StringType)
siddhi_SECONDS_second: Property = Property(name="second", type=StringType)
siddhi_SECONDS_sec: Property = Property(name="sec", type=StringType)
siddhi_SECONDS.attributes={siddhi_SECONDS_second, siddhi_SECONDS_seconds, siddhi_SECONDS_sec}

# siddhi_MILLISECONDS class attributes and methods
siddhi_MILLISECONDS_millisecond: Property = Property(name="millisecond", type=StringType)
siddhi_MILLISECONDS_milliseconds: Property = Property(name="milliseconds", type=StringType)
siddhi_MILLISECONDS_millisec: Property = Property(name="millisec", type=StringType)
siddhi_MILLISECONDS.attributes={siddhi_MILLISECONDS_millisec, siddhi_MILLISECONDS_milliseconds, siddhi_MILLISECONDS_millisecond}

# siddhi_FALSE class attributes and methods
siddhi_FALSE_fals: Property = Property(name="fals", type=StringType)
siddhi_FALSE.attributes={siddhi_FALSE_fals}

# siddhi_TRUE class attributes and methods
siddhi_TRUE_tr: Property = Property(name="tr", type=StringType)
siddhi_TRUE.attributes={siddhi_TRUE_tr}

# siddhi_LeftAbsentSequenceSource1 class attributes and methods

# LeftAbsentSequenceSource class attributes and methods

# siddhi_RightAbsentSequenceSource1 class attributes and methods

# RightAbsentSequenceSource class attributes and methods

# siddhi_LeftAbsentPatternSource1 class attributes and methods
siddhi_LeftAbsentPatternSource1_fb: Property = Property(name="fb", type=StringType)
siddhi_LeftAbsentPatternSource1.attributes={siddhi_LeftAbsentPatternSource1_fb}

# siddhi_RightAbsentPatternSource1 class attributes and methods
siddhi_RightAbsentPatternSource1_fb: Property = Property(name="fb", type=StringType)
siddhi_RightAbsentPatternSource1.attributes={siddhi_RightAbsentPatternSource1_fb}

# siddhi_MathLogicalOperation class attributes and methods

# siddhi_MathInOperation class attributes and methods

# siddhi_MathGtLtOperation class attributes and methods
siddhi_MathGtLtOperation_gt_eq: Property = Property(name="gt_eq", type=StringType)
siddhi_MathGtLtOperation_lt_eq: Property = Property(name="lt_eq", type=StringType)
siddhi_MathGtLtOperation_gt: Property = Property(name="gt", type=StringType)
siddhi_MathGtLtOperation_lt: Property = Property(name="lt", type=StringType)
siddhi_MathGtLtOperation.attributes={siddhi_MathGtLtOperation_gt_eq, siddhi_MathGtLtOperation_lt, siddhi_MathGtLtOperation_gt, siddhi_MathGtLtOperation_lt_eq}

# siddhi_MathEqualOperation class attributes and methods
siddhi_MathEqualOperation_eq: Property = Property(name="eq", type=StringType)
siddhi_MathEqualOperation_not_eq: Property = Property(name="not_eq", type=StringType)
siddhi_MathEqualOperation.attributes={siddhi_MathEqualOperation_not_eq, siddhi_MathEqualOperation_eq}

# siddhi_NotOperation class attributes and methods

# Relationships
defAggregation13: BinaryAssociation = BinaryAssociation(
    name="defAggregation13",
    ends={
        Property(name="siddhi_DefinitionAggregation", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan14", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="siddhi_ExecutionPlan", type=siddhi_SiddhiQL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SiddhiQL", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
appAnn1: BinaryAssociation = BinaryAssociation(
    name="appAnn1",
    ends={
        Property(name="siddhi_AppAnnotation", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan2", type=siddhi_AppAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defStream3: BinaryAssociation = BinaryAssociation(
    name="defStream3",
    ends={
        Property(name="siddhi_DefinitionStream", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan4", type=siddhi_DefinitionStream, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defTable5: BinaryAssociation = BinaryAssociation(
    name="defTable5",
    ends={
        Property(name="siddhi_DefinitionTable", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan6", type=siddhi_DefinitionTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
def_window7: BinaryAssociation = BinaryAssociation(
    name="def_window7",
    ends={
        Property(name="siddhi_DefinitionWindow", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan8", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defTrigger9: BinaryAssociation = BinaryAssociation(
    name="defTrigger9",
    ends={
        Property(name="siddhi_DefinitionTrigger", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan10", type=siddhi_DefinitionTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defFunction11: BinaryAssociation = BinaryAssociation(
    name="defFunction11",
    ends={
        Property(name="siddhi_DefinitionFunction", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan12", type=siddhi_DefinitionFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exElement15: BinaryAssociation = BinaryAssociation(
    name="exElement15",
    ends={
        Property(name="siddhi_ExecutionElement", type=siddhi_ExecutionPlan, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionPlan16", type=siddhi_ExecutionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
execPartition17: BinaryAssociation = BinaryAssociation(
    name="execPartition17",
    ends={
        Property(name="siddhi_ExecPartition", type=siddhi_ExecutionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionElement18", type=siddhi_ExecPartition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
que19: BinaryAssociation = BinaryAssociation(
    name="que19",
    ends={
        Property(name="siddhi_Query", type=siddhi_ExecutionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecutionElement20", type=siddhi_Query, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ann21: BinaryAssociation = BinaryAssociation(
    name="ann21",
    ends={
        Property(name="siddhi_Annotation", type=siddhi_DefinitionStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionStream22", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src23: BinaryAssociation = BinaryAssociation(
    name="src23",
    ends={
        Property(name="siddhi_Source1", type=siddhi_DefinitionStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionStream24", type=siddhi_Source1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature25: BinaryAssociation = BinaryAssociation(
    name="feature25",
    ends={
        Property(name="siddhi_Features", type=siddhi_DefinitionStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionStream26", type=siddhi_Features, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ann127: BinaryAssociation = BinaryAssociation(
    name="ann127",
    ends={
        Property(name="siddhi_Annotation29", type=siddhi_DefinitionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTable28", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src30: BinaryAssociation = BinaryAssociation(
    name="src30",
    ends={
        Property(name="siddhi_Source132", type=siddhi_DefinitionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTable31", type=siddhi_Source1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature33: BinaryAssociation = BinaryAssociation(
    name="feature33",
    ends={
        Property(name="siddhi_Features35", type=siddhi_DefinitionTable, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTable34", type=siddhi_Features, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ann236: BinaryAssociation = BinaryAssociation(
    name="ann236",
    ends={
        Property(name="siddhi_Annotation38", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionWindow37", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src39: BinaryAssociation = BinaryAssociation(
    name="src39",
    ends={
        Property(name="siddhi_Source141", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionWindow40", type=siddhi_Source1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcOp45: BinaryAssociation = BinaryAssociation(
    name="funcOp45",
    ends={
        Property(name="siddhi_FunctionOperation", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionWindow46", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature42: BinaryAssociation = BinaryAssociation(
    name="feature42",
    ends={
        Property(name="siddhi_Features44", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionWindow43", type=siddhi_Features, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opEventType47: BinaryAssociation = BinaryAssociation(
    name="opEventType47",
    ends={
        Property(name="siddhi_OutputEventType", type=siddhi_DefinitionWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionWindow48", type=siddhi_OutputEventType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tn49: BinaryAssociation = BinaryAssociation(
    name="tn49",
    ends={
        Property(name="siddhi_TriggerName", type=siddhi_DefinitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTrigger50", type=siddhi_TriggerName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
every51: BinaryAssociation = BinaryAssociation(
    name="every51",
    ends={
        Property(name="siddhi_EVERY", type=siddhi_DefinitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTrigger52", type=siddhi_EVERY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tv53: BinaryAssociation = BinaryAssociation(
    name="tv53",
    ends={
        Property(name="siddhi_TimeValue", type=siddhi_DefinitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTrigger54", type=siddhi_TimeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sv55: BinaryAssociation = BinaryAssociation(
    name="sv55",
    ends={
        Property(name="siddhi_StringValue", type=siddhi_DefinitionTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionTrigger56", type=siddhi_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fn57: BinaryAssociation = BinaryAssociation(
    name="fn57",
    ends={
        Property(name="siddhi_FunctionName", type=siddhi_DefinitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionFunction58", type=siddhi_FunctionName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ln59: BinaryAssociation = BinaryAssociation(
    name="ln59",
    ends={
        Property(name="siddhi_LanguageName", type=siddhi_DefinitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionFunction60", type=siddhi_LanguageName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propVal93: BinaryAssociation = BinaryAssociation(
    name="propVal93",
    ends={
        Property(name="siddhi_AnnotationElement94", type=siddhi_PropertyValue, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="siddhi_PropertyValue", type=siddhi_AnnotationElement, multiplicity=Multiplicity(1, 1))
    }
)
attr_type61: BinaryAssociation = BinaryAssociation(
    name="attr_type61",
    ends={
        Property(name="siddhi_AttributeType", type=siddhi_DefinitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionFunction62", type=siddhi_AttributeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func_body63: BinaryAssociation = BinaryAssociation(
    name="func_body63",
    ends={
        Property(name="siddhi_FunctionBody", type=siddhi_DefinitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionFunction64", type=siddhi_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ann65: BinaryAssociation = BinaryAssociation(
    name="ann65",
    ends={
        Property(name="siddhi_Annotation67", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation66", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
src68: BinaryAssociation = BinaryAssociation(
    name="src68",
    ends={
        Property(name="siddhi_Source170", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation69", type=siddhi_Source1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stdStream71: BinaryAssociation = BinaryAssociation(
    name="stdStream71",
    ends={
        Property(name="siddhi_StandardStream", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation72", type=siddhi_StandardStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupByQuerySel73: BinaryAssociation = BinaryAssociation(
    name="groupByQuerySel73",
    ends={
        Property(name="siddhi_GroupByQuerySelection", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation74", type=siddhi_GroupByQuerySelection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attrRef75: BinaryAssociation = BinaryAssociation(
    name="attrRef75",
    ends={
        Property(name="siddhi_AttributeReference", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation76", type=siddhi_AttributeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eve77: BinaryAssociation = BinaryAssociation(
    name="eve77",
    ends={
        Property(name="siddhi_EVERY79", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation78", type=siddhi_EVERY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggrTime80: BinaryAssociation = BinaryAssociation(
    name="aggrTime80",
    ends={
        Property(name="siddhi_AggregationTime", type=siddhi_DefinitionAggregation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DefinitionAggregation81", type=siddhi_AggregationTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aggrtimeDur82: BinaryAssociation = BinaryAssociation(
    name="aggrtimeDur82",
    ends={
        Property(name="siddhi_AggregationTimeDuration", type=siddhi_AggregationTime, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AggregationTime83", type=siddhi_AggregationTimeDuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name84: BinaryAssociation = BinaryAssociation(
    name="name84",
    ends={
        Property(name="siddhi_Name", type=siddhi_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Annotation85", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annElement86: BinaryAssociation = BinaryAssociation(
    name="annElement86",
    ends={
        Property(name="siddhi_AnnotationElement", type=siddhi_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Annotation87", type=siddhi_AnnotationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ann89: BinaryAssociation = BinaryAssociation(
    name="ann89",
    ends={
        Property(name="siddhi_Annotation90", type=siddhi_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Annotation88", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propName91: BinaryAssociation = BinaryAssociation(
    name="propName91",
    ends={
        Property(name="siddhi_PropertyName", type=siddhi_AnnotationElement, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AnnotationElement92", type=siddhi_PropertyName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or125: BinaryAssociation = BinaryAssociation(
    name="or125",
    ends={
        Property(name="siddhi_OR", type=siddhi_ConditionRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRanges126", type=siddhi_OR, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sv95: BinaryAssociation = BinaryAssociation(
    name="sv95",
    ends={
        Property(name="siddhi_StringValue97", type=siddhi_PropertyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PropertyValue96", type=siddhi_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name98: BinaryAssociation = BinaryAssociation(
    name="name98",
    ends={
        Property(name="siddhi_Name100", type=siddhi_PropertyName, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PropertyName99", type=siddhi_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ps101: BinaryAssociation = BinaryAssociation(
    name="ps101",
    ends={
        Property(name="siddhi_PropertySeparator", type=siddhi_PropertyName, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PropertyName102", type=siddhi_PropertySeparator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nam103: BinaryAssociation = BinaryAssociation(
    name="nam103",
    ends={
        Property(name="siddhi_Name105", type=siddhi_Features, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Features104", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type106: BinaryAssociation = BinaryAssociation(
    name="type106",
    ends={
        Property(name="siddhi_AttributeType108", type=siddhi_Features, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Features107", type=siddhi_AttributeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strId109: BinaryAssociation = BinaryAssociation(
    name="strId109",
    ends={
        Property(name="siddhi_Source1110", type=siddhi_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Source", type=siddhi_Source1, multiplicity=Multiplicity(0, 1))
    }
)
ann4111: BinaryAssociation = BinaryAssociation(
    name="ann4111",
    ends={
        Property(name="siddhi_Annotation113", type=siddhi_ExecPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecPartition112", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
partWithStream114: BinaryAssociation = BinaryAssociation(
    name="partWithStream114",
    ends={
        Property(name="siddhi_PartitionWithStream", type=siddhi_ExecPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecPartition115", type=siddhi_PartitionWithStream, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qu116: BinaryAssociation = BinaryAssociation(
    name="qu116",
    ends={
        Property(name="siddhi_Query118", type=siddhi_ExecPartition, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ExecPartition117", type=siddhi_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
of119: BinaryAssociation = BinaryAssociation(
    name="of119",
    ends={
        Property(name="siddhi_OF", type=siddhi_ConditionRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRanges", type=siddhi_OF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
str_id2120: BinaryAssociation = BinaryAssociation(
    name="str_id2120",
    ends={
        Property(name="siddhi_Source122", type=siddhi_ConditionRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRanges121", type=siddhi_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conRange123: BinaryAssociation = BinaryAssociation(
    name="conRange123",
    ends={
        Property(name="siddhi_ConditionRange", type=siddhi_ConditionRanges, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRanges124", type=siddhi_ConditionRange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr127: BinaryAssociation = BinaryAssociation(
    name="expr127",
    ends={
        Property(name="siddhi_Expression", type=siddhi_ConditionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRange128", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a129: BinaryAssociation = BinaryAssociation(
    name="a129",
    ends={
        Property(name="siddhi_AS", type=siddhi_ConditionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRange130", type=siddhi_AS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sv131: BinaryAssociation = BinaryAssociation(
    name="sv131",
    ends={
        Property(name="siddhi_StringValue133", type=siddhi_ConditionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConditionRange132", type=siddhi_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ann3134: BinaryAssociation = BinaryAssociation(
    name="ann3134",
    ends={
        Property(name="siddhi_Annotation136", type=siddhi_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Query135", type=siddhi_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qInp137: BinaryAssociation = BinaryAssociation(
    name="qInp137",
    ends={
        Property(name="siddhi_QueryInput", type=siddhi_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Query138", type=siddhi_QueryInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
querySec139: BinaryAssociation = BinaryAssociation(
    name="querySec139",
    ends={
        Property(name="siddhi_QuerySection", type=siddhi_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Query140", type=siddhi_QuerySection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outRate141: BinaryAssociation = BinaryAssociation(
    name="outRate141",
    ends={
        Property(name="siddhi_OutputRate", type=siddhi_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Query142", type=siddhi_OutputRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qOutput143: BinaryAssociation = BinaryAssociation(
    name="qOutput143",
    ends={
        Property(name="siddhi_QueryOutput", type=siddhi_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Query144", type=siddhi_QueryOutput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outEventType145: BinaryAssociation = BinaryAssociation(
    name="outEventType145",
    ends={
        Property(name="siddhi_OutputEventType147", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput146", type=siddhi_OutputEventType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tar148: BinaryAssociation = BinaryAssociation(
    name="tar148",
    ends={
        Property(name="siddhi_Target", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput149", type=siddhi_Target, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
on150: BinaryAssociation = BinaryAssociation(
    name="on150",
    ends={
        Property(name="siddhi_ON", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput151", type=siddhi_ON, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr152: BinaryAssociation = BinaryAssociation(
    name="expr152",
    ends={
        Property(name="siddhi_Expression154", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput153", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or155: BinaryAssociation = BinaryAssociation(
    name="or155",
    ends={
        Property(name="siddhi_OR157", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput156", type=siddhi_OR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setClause158: BinaryAssociation = BinaryAssociation(
    name="setClause158",
    ends={
        Property(name="siddhi_SetClause", type=siddhi_QueryOutput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryOutput159", type=siddhi_SetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
na160: BinaryAssociation = BinaryAssociation(
    name="na160",
    ends={
        Property(name="siddhi_Source1162", type=siddhi_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Target161", type=siddhi_Source1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src163: BinaryAssociation = BinaryAssociation(
    name="src163",
    ends={
        Property(name="siddhi_Source165", type=siddhi_Target, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Target164", type=siddhi_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
setAssignment166: BinaryAssociation = BinaryAssociation(
    name="setAssignment166",
    ends={
        Property(name="siddhi_SetAssignment", type=siddhi_SetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SetClause167", type=siddhi_SetAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op_rate_type168: BinaryAssociation = BinaryAssociation(
    name="op_rate_type168",
    ends={
        Property(name="siddhi_OutputRateType", type=siddhi_OutputRate, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutputRate169", type=siddhi_OutputRateType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
every170: BinaryAssociation = BinaryAssociation(
    name="every170",
    ends={
        Property(name="siddhi_EVERY172", type=siddhi_OutputRate, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutputRate171", type=siddhi_EVERY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tv173: BinaryAssociation = BinaryAssociation(
    name="tv173",
    ends={
        Property(name="siddhi_TimeValue175", type=siddhi_OutputRate, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutputRate174", type=siddhi_TimeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out_att176: BinaryAssociation = BinaryAssociation(
    name="out_att176",
    ends={
        Property(name="siddhi_OutputAttribute", type=siddhi_GroupByQuerySelection, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_GroupByQuerySelection177", type=siddhi_OutputAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grp_by178: BinaryAssociation = BinaryAssociation(
    name="grp_by178",
    ends={
        Property(name="siddhi_GroupBy", type=siddhi_GroupByQuerySelection, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_GroupByQuerySelection179", type=siddhi_GroupBy, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
grpByQuerySel180: BinaryAssociation = BinaryAssociation(
    name="grpByQuerySel180",
    ends={
        Property(name="siddhi_GroupByQuerySelection182", type=siddhi_QuerySection, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QuerySection181", type=siddhi_GroupByQuerySelection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
having183: BinaryAssociation = BinaryAssociation(
    name="having183",
    ends={
        Property(name="siddhi_HavingExpr", type=siddhi_QuerySection, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QuerySection184", type=siddhi_HavingExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attr_ref185: BinaryAssociation = BinaryAssociation(
    name="attr_ref185",
    ends={
        Property(name="siddhi_AttributeReference187", type=siddhi_GroupBy, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_GroupBy186", type=siddhi_AttributeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr188: BinaryAssociation = BinaryAssociation(
    name="expr188",
    ends={
        Property(name="siddhi_Expression190", type=siddhi_HavingExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_HavingExpr189", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outAttr191: BinaryAssociation = BinaryAssociation(
    name="outAttr191",
    ends={
        Property(name="siddhi_OutAttr", type=siddhi_OutputAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutputAttribute192", type=siddhi_OutAttr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attr_ref193: BinaryAssociation = BinaryAssociation(
    name="attr_ref193",
    ends={
        Property(name="siddhi_AttributeReference195", type=siddhi_OutputAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutputAttribute194", type=siddhi_AttributeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attr196: BinaryAssociation = BinaryAssociation(
    name="attr196",
    ends={
        Property(name="siddhi_Attribute", type=siddhi_OutAttr, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutAttr197", type=siddhi_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a198: BinaryAssociation = BinaryAssociation(
    name="a198",
    ends={
        Property(name="siddhi_AS200", type=siddhi_OutAttr, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_OutAttr199", type=siddhi_AS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
js201: BinaryAssociation = BinaryAssociation(
    name="js201",
    ends={
        Property(name="siddhi_JoinStream", type=siddhi_QueryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryInput202", type=siddhi_JoinStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seqSrcChanin203: BinaryAssociation = BinaryAssociation(
    name="seqSrcChanin203",
    ends={
        Property(name="siddhi_SequenceStream", type=siddhi_QueryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryInput204", type=siddhi_SequenceStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps205: BinaryAssociation = BinaryAssociation(
    name="ps205",
    ends={
        Property(name="siddhi_PatternStream", type=siddhi_QueryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryInput206", type=siddhi_PatternStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
anonStream207: BinaryAssociation = BinaryAssociation(
    name="anonStream207",
    ends={
        Property(name="siddhi_AnonymousStream", type=siddhi_QueryInput, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_QueryInput208", type=siddhi_AnonymousStream, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
everySequenceSourceChain209: BinaryAssociation = BinaryAssociation(
    name="everySequenceSourceChain209",
    ends={
        Property(name="siddhi_EverySequenceSourceChain", type=siddhi_SequenceStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceStream210", type=siddhi_EverySequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
everyAbsentSequenceSourceChain211: BinaryAssociation = BinaryAssociation(
    name="everyAbsentSequenceSourceChain211",
    ends={
        Property(name="siddhi_EveryAbsentSequenceSourceChain", type=siddhi_SequenceStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceStream212", type=siddhi_EveryAbsentSequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seqSource213: BinaryAssociation = BinaryAssociation(
    name="seqSource213",
    ends={
        Property(name="siddhi_SequenceSource", type=siddhi_EverySequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EverySequenceSourceChain214", type=siddhi_SequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt215: BinaryAssociation = BinaryAssociation(
    name="wt215",
    ends={
        Property(name="siddhi_WithinTime", type=siddhi_EverySequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EverySequenceSourceChain216", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ssc217: BinaryAssociation = BinaryAssociation(
    name="ssc217",
    ends={
        Property(name="siddhi_SequenceSourceChain", type=siddhi_EverySequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EverySequenceSourceChain218", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absSeqSrcChain219: BinaryAssociation = BinaryAssociation(
    name="absSeqSrcChain219",
    ends={
        Property(name="siddhi_AbsentSequenceSourceChain", type=siddhi_EveryAbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryAbsentSequenceSourceChain220", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seqSrcChain221: BinaryAssociation = BinaryAssociation(
    name="seqSrcChain221",
    ends={
        Property(name="siddhi_SequenceSourceChain223", type=siddhi_EveryAbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryAbsentSequenceSourceChain222", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absentSequenceSourceChain225: BinaryAssociation = BinaryAssociation(
    name="absentSequenceSourceChain225",
    ends={
        Property(name="siddhi_AbsentSequenceSourceChain226", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentSequenceSourceChain224", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt5227: BinaryAssociation = BinaryAssociation(
    name="wt5227",
    ends={
        Property(name="siddhi_WithinTime229", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentSequenceSourceChain228", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource230: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource230",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentSequenceSourceChain231", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftAbsentSequenceSource232: BinaryAssociation = BinaryAssociation(
    name="leftAbsentSequenceSource232",
    ends={
        Property(name="siddhi_LeftAbsentSequenceSource", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentSequenceSourceChain233", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightAbsentSequenceSource234: BinaryAssociation = BinaryAssociation(
    name="rightAbsentSequenceSource234",
    ends={
        Property(name="siddhi_RightAbsentSequenceSource", type=siddhi_AbsentSequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentSequenceSourceChain235", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left237: BinaryAssociation = BinaryAssociation(
    name="left237",
    ends={
        Property(name="siddhi_LeftAbsentSequenceSource238", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource236", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right239: BinaryAssociation = BinaryAssociation(
    name="right239",
    ends={
        Property(name="siddhi_EObject", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource240", type=siddhi_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftAbsentSequenceSource242: BinaryAssociation = BinaryAssociation(
    name="leftAbsentSequenceSource242",
    ends={
        Property(name="siddhi_LeftAbsentSequenceSource243", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource241", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt6244: BinaryAssociation = BinaryAssociation(
    name="wt6244",
    ends={
        Property(name="siddhi_WithinTime246", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource245", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource247: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource247",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource249", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource248", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceSourceChain250: BinaryAssociation = BinaryAssociation(
    name="sequenceSourceChain250",
    ends={
        Property(name="siddhi_SequenceSourceChain252", type=siddhi_LeftAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentSequenceSource251", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1254: BinaryAssociation = BinaryAssociation(
    name="left1254",
    ends={
        Property(name="siddhi_RightAbsentSequenceSource255", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource253", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right1257: BinaryAssociation = BinaryAssociation(
    name="right1257",
    ends={
        Property(name="siddhi_RightAbsentSequenceSource258", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource256", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightAbsentSequenceSource260: BinaryAssociation = BinaryAssociation(
    name="rightAbsentSequenceSource260",
    ends={
        Property(name="siddhi_RightAbsentSequenceSource261", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource259", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt7262: BinaryAssociation = BinaryAssociation(
    name="wt7262",
    ends={
        Property(name="siddhi_WithinTime264", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource263", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sequenceSourceChain265: BinaryAssociation = BinaryAssociation(
    name="sequenceSourceChain265",
    ends={
        Property(name="siddhi_SequenceSourceChain267", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource266", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource268: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource268",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource270", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource269", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left272: BinaryAssociation = BinaryAssociation(
    name="left272",
    ends={
        Property(name="siddhi_SequenceSourceChain273", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceSourceChain271", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right275: BinaryAssociation = BinaryAssociation(
    name="right275",
    ends={
        Property(name="siddhi_SequenceSourceChain276", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceSourceChain274", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt1277: BinaryAssociation = BinaryAssociation(
    name="wt1277",
    ends={
        Property(name="siddhi_WithinTime279", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceSourceChain278", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
wt280: BinaryAssociation = BinaryAssociation(
    name="wt280",
    ends={
        Property(name="siddhi_WithinTime282", type=siddhi_SequenceSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SequenceSource281", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qi283: BinaryAssociation = BinaryAssociation(
    name="qi283",
    ends={
        Property(name="siddhi_QueryInput285", type=siddhi_AnonymousStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AnonymousStream284", type=siddhi_QueryInput, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qs286: BinaryAssociation = BinaryAssociation(
    name="qs286",
    ends={
        Property(name="siddhi_QuerySection288", type=siddhi_AnonymousStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AnonymousStream287", type=siddhi_QuerySection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
out_rate289: BinaryAssociation = BinaryAssociation(
    name="out_rate289",
    ends={
        Property(name="siddhi_OutputRate291", type=siddhi_AnonymousStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AnonymousStream290", type=siddhi_OutputRate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op_event_type292: BinaryAssociation = BinaryAssociation(
    name="op_event_type292",
    ends={
        Property(name="siddhi_OutputEventType294", type=siddhi_AnonymousStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AnonymousStream293", type=siddhi_OutputEventType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left296: BinaryAssociation = BinaryAssociation(
    name="left296",
    ends={
        Property(name="siddhi_EveryPatternSourceChain", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain295", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right298: BinaryAssociation = BinaryAssociation(
    name="right298",
    ends={
        Property(name="siddhi_EveryPatternSourceChain299", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain297", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eps301: BinaryAssociation = BinaryAssociation(
    name="eps301",
    ends={
        Property(name="siddhi_EveryPatternSourceChain302", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain300", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt303: BinaryAssociation = BinaryAssociation(
    name="wt303",
    ends={
        Property(name="siddhi_WithinTime305", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain304", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
psc306: BinaryAssociation = BinaryAssociation(
    name="psc306",
    ends={
        Property(name="siddhi_PatternSourceChain", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain307", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
every308: BinaryAssociation = BinaryAssociation(
    name="every308",
    ends={
        Property(name="siddhi_EVERY310", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryPatternSourceChain309", type=siddhi_EVERY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left312: BinaryAssociation = BinaryAssociation(
    name="left312",
    ends={
        Property(name="siddhi_PatternSourceChain313", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSourceChain311", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right315: BinaryAssociation = BinaryAssociation(
    name="right315",
    ends={
        Property(name="siddhi_PatternSourceChain316", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSourceChain314", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
psc_2318: BinaryAssociation = BinaryAssociation(
    name="psc_2318",
    ends={
        Property(name="siddhi_PatternSourceChain319", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSourceChain317", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt320: BinaryAssociation = BinaryAssociation(
    name="wt320",
    ends={
        Property(name="siddhi_WithinTime322", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSourceChain321", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ps323: BinaryAssociation = BinaryAssociation(
    name="ps323",
    ends={
        Property(name="siddhi_PatternSource", type=siddhi_PatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSourceChain324", type=siddhi_PatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lss325: BinaryAssociation = BinaryAssociation(
    name="lss325",
    ends={
        Property(name="siddhi_LogicalStatefulSource", type=siddhi_PatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSource326", type=siddhi_LogicalStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pss327: BinaryAssociation = BinaryAssociation(
    name="pss327",
    ends={
        Property(name="siddhi_PatternCollectionStatefulSource", type=siddhi_PatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSource328", type=siddhi_PatternCollectionStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stdss329: BinaryAssociation = BinaryAssociation(
    name="stdss329",
    ends={
        Property(name="siddhi_StandardStatefulSource", type=siddhi_PatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSource330", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicalAbsStatefulSrc331: BinaryAssociation = BinaryAssociation(
    name="logicalAbsStatefulSrc331",
    ends={
        Property(name="siddhi_LogicalAbsentStatefulSource", type=siddhi_PatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_PatternSource332", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stdSource333: BinaryAssociation = BinaryAssociation(
    name="stdSource333",
    ends={
        Property(name="siddhi_StandardStatefulSource335", type=siddhi_LogicalStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalStatefulSource334", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
and336: BinaryAssociation = BinaryAssociation(
    name="and336",
    ends={
        Property(name="siddhi_AND", type=siddhi_LogicalStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalStatefulSource337", type=siddhi_AND, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or338: BinaryAssociation = BinaryAssociation(
    name="or338",
    ends={
        Property(name="siddhi_OR340", type=siddhi_LogicalStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalStatefulSource339", type=siddhi_OR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicalAbsStatefulSrc342: BinaryAssociation = BinaryAssociation(
    name="logicalAbsStatefulSrc342",
    ends={
        Property(name="siddhi_LogicalAbsentStatefulSource343", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource341", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stdSource344: BinaryAssociation = BinaryAssociation(
    name="stdSource344",
    ends={
        Property(name="siddhi_StandardStatefulSource346", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource345", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and347: BinaryAssociation = BinaryAssociation(
    name="and347",
    ends={
        Property(name="siddhi_AND349", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource348", type=siddhi_AND, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not350: BinaryAssociation = BinaryAssociation(
    name="not350",
    ends={
        Property(name="siddhi_NOT", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource351", type=siddhi_NOT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bs352: BinaryAssociation = BinaryAssociation(
    name="bs352",
    ends={
        Property(name="siddhi_BasicSource", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource353", type=siddhi_BasicSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource1354: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource1354",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource356", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource355", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource2357: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource2357",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource359", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource358", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPatternSource360: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPatternSource360",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource362", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource361", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right1398: BinaryAssociation = BinaryAssociation(
    name="right1398",
    ends={
        Property(name="siddhi_RightAbsentPatternSource399", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource397", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
o363: BinaryAssociation = BinaryAssociation(
    name="o363",
    ends={
        Property(name="siddhi_OR365", type=siddhi_LogicalAbsentStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LogicalAbsentStatefulSource364", type=siddhi_OR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
absentPatternSrcChain367: BinaryAssociation = BinaryAssociation(
    name="absentPatternSrcChain367",
    ends={
        Property(name="siddhi_AbsentPatternSourceChain", type=siddhi_AbsentPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentPatternSourceChain366", type=siddhi_AbsentPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt1368: BinaryAssociation = BinaryAssociation(
    name="wt1368",
    ends={
        Property(name="siddhi_WithinTime370", type=siddhi_AbsentPatternSourceChain, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AbsentPatternSourceChain369", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicAbsentPS371: BinaryAssociation = BinaryAssociation(
    name="basicAbsentPS371",
    ends={
        Property(name="siddhi_BasicAbsentPatternSource372", type=siddhi_EveryAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_EveryAbsentPatternSource", type=siddhi_BasicAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tv373: BinaryAssociation = BinaryAssociation(
    name="tv373",
    ends={
        Property(name="siddhi_TimeValue374", type=siddhi_ForTime, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ForTime", type=siddhi_TimeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left376: BinaryAssociation = BinaryAssociation(
    name="left376",
    ends={
        Property(name="siddhi_LeftAbsentPatternSource", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource375", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right377: BinaryAssociation = BinaryAssociation(
    name="right377",
    ends={
        Property(name="siddhi_AbsentPatternSourceChain379", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource378", type=siddhi_AbsentPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftAbsPS381: BinaryAssociation = BinaryAssociation(
    name="leftAbsPS381",
    ends={
        Property(name="siddhi_LeftAbsentPatternSource382", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource380", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt2383: BinaryAssociation = BinaryAssociation(
    name="wt2383",
    ends={
        Property(name="siddhi_WithinTime385", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource384", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
everyAbsPS386: BinaryAssociation = BinaryAssociation(
    name="everyAbsPS386",
    ends={
        Property(name="siddhi_EveryAbsentPatternSource388", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource387", type=siddhi_EveryAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
everyPSC389: BinaryAssociation = BinaryAssociation(
    name="everyPSC389",
    ends={
        Property(name="siddhi_EveryPatternSourceChain391", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource390", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leftAbsPatternSrc393: BinaryAssociation = BinaryAssociation(
    name="leftAbsPatternSrc393",
    ends={
        Property(name="siddhi_LeftAbsentPatternSource394", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LeftAbsentPatternSource392", type=siddhi_LeftAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1396: BinaryAssociation = BinaryAssociation(
    name="left1396",
    ends={
        Property(name="siddhi_RightAbsentPatternSource", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource395", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nam443: BinaryAssociation = BinaryAssociation(
    name="nam443",
    ends={
        Property(name="siddhi_Name444", type=siddhi_StreamAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StreamAlias", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rightAbsPS401: BinaryAssociation = BinaryAssociation(
    name="rightAbsPS401",
    ends={
        Property(name="siddhi_RightAbsentPatternSource402", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource400", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wt3403: BinaryAssociation = BinaryAssociation(
    name="wt3403",
    ends={
        Property(name="siddhi_WithinTime405", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource404", type=siddhi_WithinTime, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
everyPSC1406: BinaryAssociation = BinaryAssociation(
    name="everyPSC1406",
    ends={
        Property(name="siddhi_EveryPatternSourceChain408", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource407", type=siddhi_EveryPatternSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
everyAbsPS1409: BinaryAssociation = BinaryAssociation(
    name="everyAbsPS1409",
    ends={
        Property(name="siddhi_EveryAbsentPatternSource411", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource410", type=siddhi_EveryAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left_source412: BinaryAssociation = BinaryAssociation(
    name="left_source412",
    ends={
        Property(name="siddhi_JoinSource", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream413", type=siddhi_JoinSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right_source414: BinaryAssociation = BinaryAssociation(
    name="right_source414",
    ends={
        Property(name="siddhi_JoinSource416", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream415", type=siddhi_JoinSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right_uni417: BinaryAssociation = BinaryAssociation(
    name="right_uni417",
    ends={
        Property(name="siddhi_UNIDIRECTIONAL", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream418", type=siddhi_UNIDIRECTIONAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
on419: BinaryAssociation = BinaryAssociation(
    name="on419",
    ends={
        Property(name="siddhi_ON421", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream420", type=siddhi_ON, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr422: BinaryAssociation = BinaryAssociation(
    name="expr422",
    ends={
        Property(name="siddhi_Expression424", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream423", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wtr425: BinaryAssociation = BinaryAssociation(
    name="wtr425",
    ends={
        Property(name="siddhi_WithinTimeRange", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream426", type=siddhi_WithinTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
p427: BinaryAssociation = BinaryAssociation(
    name="p427",
    ends={
        Property(name="siddhi_Per1", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream428", type=siddhi_Per1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
join429: BinaryAssociation = BinaryAssociation(
    name="join429",
    ends={
        Property(name="siddhi_joins", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream430", type=siddhi_joins, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left_uni431: BinaryAssociation = BinaryAssociation(
    name="left_uni431",
    ends={
        Property(name="siddhi_UNIDIRECTIONAL433", type=siddhi_JoinStream, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_JoinStream432", type=siddhi_UNIDIRECTIONAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
startPattern434: BinaryAssociation = BinaryAssociation(
    name="startPattern434",
    ends={
        Property(name="siddhi_Expression436", type=siddhi_WithinTimeRange, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_WithinTimeRange435", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
endPattern437: BinaryAssociation = BinaryAssociation(
    name="endPattern437",
    ends={
        Property(name="siddhi_Expression439", type=siddhi_WithinTimeRange, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_WithinTimeRange438", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp440: BinaryAssociation = BinaryAssociation(
    name="exp440",
    ends={
        Property(name="siddhi_Expression442", type=siddhi_Per1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Per1441", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tv445: BinaryAssociation = BinaryAssociation(
    name="tv445",
    ends={
        Property(name="siddhi_TimeValue447", type=siddhi_WithinTime, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_WithinTime446", type=siddhi_TimeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
window448: BinaryAssociation = BinaryAssociation(
    name="window448",
    ends={
        Property(name="siddhi_Win", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource", type=siddhi_Win, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a449: BinaryAssociation = BinaryAssociation(
    name="a449",
    ends={
        Property(name="siddhi_AS451", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource450", type=siddhi_AS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
strAlias452: BinaryAssociation = BinaryAssociation(
    name="strAlias452",
    ends={
        Property(name="siddhi_StreamAlias454", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource453", type=siddhi_StreamAlias, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postWindowHandlers455: BinaryAssociation = BinaryAssociation(
    name="postWindowHandlers455",
    ends={
        Property(name="siddhi_BasicSourceStreamHandlers", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource456", type=siddhi_BasicSourceStreamHandlers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src457: BinaryAssociation = BinaryAssociation(
    name="src457",
    ends={
        Property(name="siddhi_Source459", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource458", type=siddhi_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicSSh460: BinaryAssociation = BinaryAssociation(
    name="basicSSh460",
    ends={
        Property(name="siddhi_BasicSourceStreamHandlers1", type=siddhi_MainSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MainSource461", type=siddhi_BasicSourceStreamHandlers1, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicSsHandler462: BinaryAssociation = BinaryAssociation(
    name="basicSsHandler462",
    ends={
        Property(name="siddhi_BasicSourceStreamHandler", type=siddhi_BasicSourceStreamHandlers, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandlers463", type=siddhi_BasicSourceStreamHandler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp464: BinaryAssociation = BinaryAssociation(
    name="exp464",
    ends={
        Property(name="siddhi_Expression466", type=siddhi_BasicSourceStreamHandlers1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandlers1465", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fo467: BinaryAssociation = BinaryAssociation(
    name="fo467",
    ends={
        Property(name="siddhi_FunctionOperation469", type=siddhi_BasicSourceStreamHandlers1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandlers1468", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func_op470: BinaryAssociation = BinaryAssociation(
    name="func_op470",
    ends={
        Property(name="siddhi_FunctionOperation472", type=siddhi_BasicSourceStreamHandlers1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandlers1471", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fil473: BinaryAssociation = BinaryAssociation(
    name="fil473",
    ends={
        Property(name="siddhi_Filter", type=siddhi_BasicSourceStreamHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandler474", type=siddhi_Filter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sf475: BinaryAssociation = BinaryAssociation(
    name="sf475",
    ends={
        Property(name="siddhi_StreamFunction", type=siddhi_BasicSourceStreamHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSourceStreamHandler476", type=siddhi_StreamFunction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp477: BinaryAssociation = BinaryAssociation(
    name="exp477",
    ends={
        Property(name="siddhi_Expression479", type=siddhi_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Filter478", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fo480: BinaryAssociation = BinaryAssociation(
    name="fo480",
    ends={
        Property(name="siddhi_FunctionOperation482", type=siddhi_StreamFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StreamFunction481", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
func_op483: BinaryAssociation = BinaryAssociation(
    name="func_op483",
    ends={
        Property(name="siddhi_FunctionOperation485", type=siddhi_Win, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Win484", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mlo487: BinaryAssociation = BinaryAssociation(
    name="mlo487",
    ends={
        Property(name="siddhi_MathOperation", type=siddhi_MathOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathOperation486", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left489: BinaryAssociation = BinaryAssociation(
    name="left489",
    ends={
        Property(name="siddhi_MathOperation490", type=siddhi_MathOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathOperation488", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right491: BinaryAssociation = BinaryAssociation(
    name="right491",
    ends={
        Property(name="siddhi_MathDivmulOperation", type=siddhi_MathAddsubOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathAddsubOperation", type=siddhi_MathDivmulOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op492: BinaryAssociation = BinaryAssociation(
    name="op492",
    ends={
        Property(name="siddhi_MathOperation493", type=siddhi_MathOtherOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathOtherOperations", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lit494: BinaryAssociation = BinaryAssociation(
    name="lit494",
    ends={
        Property(name="siddhi_Literal", type=siddhi_MathOtherOperations, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathOtherOperations495", type=siddhi_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stream_ref496: BinaryAssociation = BinaryAssociation(
    name="stream_ref496",
    ends={
        Property(name="siddhi_StreamReference", type=siddhi_NullCheck, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NullCheck", type=siddhi_StreamReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attr_ref497: BinaryAssociation = BinaryAssociation(
    name="attr_ref497",
    ends={
        Property(name="siddhi_AttributeReference499", type=siddhi_NullCheck, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NullCheck498", type=siddhi_AttributeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fo500: BinaryAssociation = BinaryAssociation(
    name="fo500",
    ends={
        Property(name="siddhi_FunctionOperation502", type=siddhi_NullCheck, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NullCheck501", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name503: BinaryAssociation = BinaryAssociation(
    name="name503",
    ends={
        Property(name="siddhi_Name505", type=siddhi_StreamReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StreamReference504", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aatr_index506: BinaryAssociation = BinaryAssociation(
    name="aatr_index506",
    ends={
        Property(name="siddhi_AttributeIndex", type=siddhi_StreamReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StreamReference507", type=siddhi_AttributeIndex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
const_val508: BinaryAssociation = BinaryAssociation(
    name="const_val508",
    ends={
        Property(name="siddhi_ConstantValue", type=siddhi_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Literal509", type=siddhi_ConstantValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fo510: BinaryAssociation = BinaryAssociation(
    name="fo510",
    ends={
        Property(name="siddhi_FunctionOperation512", type=siddhi_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Literal511", type=siddhi_FunctionOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attrRef513: BinaryAssociation = BinaryAssociation(
    name="attrRef513",
    ends={
        Property(name="siddhi_AttributeReference515", type=siddhi_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Literal514", type=siddhi_AttributeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression516: BinaryAssociation = BinaryAssociation(
    name="expression516",
    ends={
        Property(name="siddhi_Expression518", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference517", type=siddhi_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name1519: BinaryAssociation = BinaryAssociation(
    name="name1519",
    ends={
        Property(name="siddhi_SourceOrEventReference", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference520", type=siddhi_SourceOrEventReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OPEN_SQARE_BRACKETSattribute_index1521: BinaryAssociation = BinaryAssociation(
    name="OPEN_SQARE_BRACKETSattribute_index1521",
    ends={
        Property(name="siddhi_AttributeIndex523", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference522", type=siddhi_AttributeIndex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name2524: BinaryAssociation = BinaryAssociation(
    name="name2524",
    ends={
        Property(name="siddhi_SourceOrEventReference526", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference525", type=siddhi_SourceOrEventReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OPEN_SQARE_BRACKETSattribute_index2527: BinaryAssociation = BinaryAssociation(
    name="OPEN_SQARE_BRACKETSattribute_index2527",
    ends={
        Property(name="siddhi_AttributeIndex529", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference528", type=siddhi_AttributeIndex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featuresOrAttrRef530: BinaryAssociation = BinaryAssociation(
    name="featuresOrAttrRef530",
    ends={
        Property(name="siddhi_FeaturesOrOutAttrReference", type=siddhi_AttributeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeReference531", type=siddhi_FeaturesOrOutAttrReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
srcoutAttrref532: BinaryAssociation = BinaryAssociation(
    name="srcoutAttrref532",
    ends={
        Property(name="siddhi_FeaturesOrOutAttr", type=siddhi_FeaturesOrOutAttrReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FeaturesOrOutAttrReference533", type=siddhi_FeaturesOrOutAttr, multiplicity=Multiplicity(0, 1))
    }
)
coll534: BinaryAssociation = BinaryAssociation(
    name="coll534",
    ends={
        Property(name="siddhi_Collect", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StandardStatefulSource535", type=siddhi_Collect, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src536: BinaryAssociation = BinaryAssociation(
    name="src536",
    ends={
        Property(name="siddhi_Source538", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StandardStatefulSource537", type=siddhi_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic_ss_handlers539: BinaryAssociation = BinaryAssociation(
    name="basic_ss_handlers539",
    ends={
        Property(name="siddhi_BasicSourceStreamHandlers541", type=siddhi_StandardStatefulSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_StandardStatefulSource540", type=siddhi_BasicSourceStreamHandlers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
src542: BinaryAssociation = BinaryAssociation(
    name="src542",
    ends={
        Property(name="siddhi_Source544", type=siddhi_BasicSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSource543", type=siddhi_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basic_ss_handlers545: BinaryAssociation = BinaryAssociation(
    name="basic_ss_handlers545",
    ends={
        Property(name="siddhi_BasicSourceStreamHandlers547", type=siddhi_BasicSource, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_BasicSource546", type=siddhi_BasicSourceStreamHandlers, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
na548: BinaryAssociation = BinaryAssociation(
    name="na548",
    ends={
        Property(name="siddhi_Source1OrStandardStatefulSource", type=siddhi_SourceOrEventReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_SourceOrEventReference549", type=siddhi_Source1OrStandardStatefulSource, multiplicity=Multiplicity(0, 1))
    }
)
attrName1550: BinaryAssociation = BinaryAssociation(
    name="attrName1550",
    ends={
        Property(name="siddhi_Features551", type=siddhi_AttributeNameReference, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeNameReference", type=siddhi_Features, multiplicity=Multiplicity(0, 1))
    }
)
bv552: BinaryAssociation = BinaryAssociation(
    name="bv552",
    ends={
        Property(name="siddhi_BoolValue", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue553", type=siddhi_BoolValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sdv554: BinaryAssociation = BinaryAssociation(
    name="sdv554",
    ends={
        Property(name="siddhi_SignedDoubleValue", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue555", type=siddhi_SignedDoubleValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sfv556: BinaryAssociation = BinaryAssociation(
    name="sfv556",
    ends={
        Property(name="siddhi_SignedFloatValue", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue557", type=siddhi_SignedFloatValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
slv558: BinaryAssociation = BinaryAssociation(
    name="slv558",
    ends={
        Property(name="siddhi_SignedLongValue", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue559", type=siddhi_SignedLongValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tv560: BinaryAssociation = BinaryAssociation(
    name="tv560",
    ends={
        Property(name="siddhi_TimeValue562", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue561", type=siddhi_TimeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sv563: BinaryAssociation = BinaryAssociation(
    name="sv563",
    ends={
        Property(name="siddhi_StringValue565", type=siddhi_ConstantValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_ConstantValue564", type=siddhi_StringValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcNamespace566: BinaryAssociation = BinaryAssociation(
    name="funcNamespace566",
    ends={
        Property(name="siddhi_FunctionNamespace", type=siddhi_FunctionOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FunctionOperation567", type=siddhi_FunctionNamespace, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
funcId568: BinaryAssociation = BinaryAssociation(
    name="funcId568",
    ends={
        Property(name="siddhi_FunctionId", type=siddhi_FunctionOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FunctionOperation569", type=siddhi_FunctionId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attrList570: BinaryAssociation = BinaryAssociation(
    name="attrList570",
    ends={
        Property(name="siddhi_AttributeList", type=siddhi_FunctionOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FunctionOperation571", type=siddhi_AttributeList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name572: BinaryAssociation = BinaryAssociation(
    name="name572",
    ends={
        Property(name="siddhi_Name574", type=siddhi_FunctionNamespace, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FunctionNamespace573", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name575: BinaryAssociation = BinaryAssociation(
    name="name575",
    ends={
        Property(name="siddhi_Name577", type=siddhi_FunctionId, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FunctionId576", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attr578: BinaryAssociation = BinaryAssociation(
    name="attr578",
    ends={
        Property(name="siddhi_Attribute580", type=siddhi_AttributeList, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_AttributeList579", type=siddhi_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mathOp581: BinaryAssociation = BinaryAssociation(
    name="mathOp581",
    ends={
        Property(name="siddhi_MathOperation583", type=siddhi_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Attribute582", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sv600: BinaryAssociation = BinaryAssociation(
    name="sv600",
    ends={
        Property(name="siddhi_TimeValue601", type=siddhi_SecondValue, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="siddhi_SecondValue602", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1))
    }
)
yv584: BinaryAssociation = BinaryAssociation(
    name="yv584",
    ends={
        Property(name="siddhi_YearValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue585", type=siddhi_YearValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mv586: BinaryAssociation = BinaryAssociation(
    name="mv586",
    ends={
        Property(name="siddhi_MonthValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue587", type=siddhi_MonthValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
wv588: BinaryAssociation = BinaryAssociation(
    name="wv588",
    ends={
        Property(name="siddhi_WeekValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue589", type=siddhi_WeekValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dv590: BinaryAssociation = BinaryAssociation(
    name="dv590",
    ends={
        Property(name="siddhi_DayValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue591", type=siddhi_DayValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hv592: BinaryAssociation = BinaryAssociation(
    name="hv592",
    ends={
        Property(name="siddhi_HourValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue593", type=siddhi_HourValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minv594: BinaryAssociation = BinaryAssociation(
    name="minv594",
    ends={
        Property(name="siddhi_MinuteValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue595", type=siddhi_MinuteValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secv596: BinaryAssociation = BinaryAssociation(
    name="secv596",
    ends={
        Property(name="siddhi_SecondValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue597", type=siddhi_SecondValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msecv598: BinaryAssociation = BinaryAssociation(
    name="msecv598",
    ends={
        Property(name="siddhi_MillisecondValue", type=siddhi_TimeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_TimeValue599", type=siddhi_MillisecondValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
l610: BinaryAssociation = BinaryAssociation(
    name="l610",
    ends={
        Property(name="siddhi_L", type=siddhi_LONG_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_LONG_LITERAL", type=siddhi_L, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e603: BinaryAssociation = BinaryAssociation(
    name="e603",
    ends={
        Property(name="siddhi_E", type=siddhi_DOUBLE_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DOUBLE_LITERAL", type=siddhi_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d604: BinaryAssociation = BinaryAssociation(
    name="d604",
    ends={
        Property(name="siddhi_D", type=siddhi_DOUBLE_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_DOUBLE_LITERAL605", type=siddhi_D, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e606: BinaryAssociation = BinaryAssociation(
    name="e606",
    ends={
        Property(name="siddhi_E607", type=siddhi_FLOAT_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FLOAT_LITERAL", type=siddhi_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
f608: BinaryAssociation = BinaryAssociation(
    name="f608",
    ends={
        Property(name="siddhi_F", type=siddhi_FLOAT_LITERAL, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_FLOAT_LITERAL609", type=siddhi_F, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
on619: BinaryAssociation = BinaryAssociation(
    name="on619",
    ends={
        Property(name="siddhi_ON621", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword620", type=siddhi_ON, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
a611: BinaryAssociation = BinaryAssociation(
    name="a611",
    ends={
        Property(name="siddhi_AS612", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword", type=siddhi_AS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
every613: BinaryAssociation = BinaryAssociation(
    name="every613",
    ends={
        Property(name="siddhi_EVERY615", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword614", type=siddhi_EVERY, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uni616: BinaryAssociation = BinaryAssociation(
    name="uni616",
    ends={
        Property(name="siddhi_UNIDIRECTIONAL618", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword617", type=siddhi_UNIDIRECTIONAL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and622: BinaryAssociation = BinaryAssociation(
    name="and622",
    ends={
        Property(name="siddhi_AND624", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword623", type=siddhi_AND, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or625: BinaryAssociation = BinaryAssociation(
    name="or625",
    ends={
        Property(name="siddhi_OR627", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword626", type=siddhi_OR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not628: BinaryAssociation = BinaryAssociation(
    name="not628",
    ends={
        Property(name="siddhi_NOT630", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword629", type=siddhi_NOT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
of631: BinaryAssociation = BinaryAssociation(
    name="of631",
    ends={
        Property(name="siddhi_OF633", type=siddhi_Keyword, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_Keyword632", type=siddhi_OF, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name640: BinaryAssociation = BinaryAssociation(
    name="name640",
    ends={
        Property(name="siddhi_Name641", type=siddhi_APP, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_APP", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ann5642: BinaryAssociation = BinaryAssociation(
    name="ann5642",
    ends={
        Property(name="siddhi_AnnotationElement644", type=siddhi_APP, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_APP643", type=siddhi_AnnotationElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicSrc634: BinaryAssociation = BinaryAssociation(
    name="basicSrc634",
    ends={
        Property(name="siddhi_BasicSource636", type=siddhi_NOT, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NOT635", type=siddhi_BasicSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ft637: BinaryAssociation = BinaryAssociation(
    name="ft637",
    ends={
        Property(name="siddhi_ForTime639", type=siddhi_NOT, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NOT638", type=siddhi_ForTime, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left645: BinaryAssociation = BinaryAssociation(
    name="left645",
    ends={
        Property(name="siddhi_RightAbsentSequenceSource646", type=siddhi_RightAbsentSequenceSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource1", type=siddhi_RightAbsentSequenceSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
and655: BinaryAssociation = BinaryAssociation(
    name="and655",
    ends={
        Property(name="siddhi_AND656", type=siddhi_MathLogicalOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathLogicalOperation", type=siddhi_AND, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right647: BinaryAssociation = BinaryAssociation(
    name="right647",
    ends={
        Property(name="siddhi_SequenceSourceChain649", type=siddhi_RightAbsentSequenceSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentSequenceSource1648", type=siddhi_SequenceSourceChain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left650: BinaryAssociation = BinaryAssociation(
    name="left650",
    ends={
        Property(name="siddhi_RightAbsentPatternSource651", type=siddhi_RightAbsentPatternSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource1", type=siddhi_RightAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right652: BinaryAssociation = BinaryAssociation(
    name="right652",
    ends={
        Property(name="siddhi_EveryAbsentPatternSource654", type=siddhi_RightAbsentPatternSource1, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_RightAbsentPatternSource1653", type=siddhi_EveryAbsentPatternSource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or657: BinaryAssociation = BinaryAssociation(
    name="or657",
    ends={
        Property(name="siddhi_OR659", type=siddhi_MathLogicalOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathLogicalOperation658", type=siddhi_OR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right660: BinaryAssociation = BinaryAssociation(
    name="right660",
    ends={
        Property(name="siddhi_MathOperation662", type=siddhi_MathLogicalOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathLogicalOperation661", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
in663: BinaryAssociation = BinaryAssociation(
    name="in663",
    ends={
        Property(name="siddhi_IN", type=siddhi_MathInOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathInOperation", type=siddhi_IN, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name664: BinaryAssociation = BinaryAssociation(
    name="name664",
    ends={
        Property(name="siddhi_Name666", type=siddhi_MathInOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathInOperation665", type=siddhi_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right667: BinaryAssociation = BinaryAssociation(
    name="right667",
    ends={
        Property(name="siddhi_MathOperation668", type=siddhi_MathGtLtOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathGtLtOperation", type=siddhi_MathOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right669: BinaryAssociation = BinaryAssociation(
    name="right669",
    ends={
        Property(name="siddhi_MathAddsubOperation670", type=siddhi_MathEqualOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_MathEqualOperation", type=siddhi_MathAddsubOperation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not671: BinaryAssociation = BinaryAssociation(
    name="not671",
    ends={
        Property(name="siddhi_NOT672", type=siddhi_NotOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="siddhi_NotOperation", type=siddhi_NOT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_siddhi_DefinitionStream_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionStream)
gen_siddhi_DefinitionStream_STREAM = Generalization(general=STREAM, specific=siddhi_DefinitionStream)
gen_siddhi_DefinitionTable_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionTable)
gen_siddhi_DefinitionTable_TABLE = Generalization(general=TABLE, specific=siddhi_DefinitionTable)
gen_siddhi_DefinitionWindow_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionWindow)
gen_siddhi_DefinitionWindow_WINDOW = Generalization(general=WINDOW, specific=siddhi_DefinitionWindow)
gen_siddhi_DefinitionWindow_OUTPUT = Generalization(general=OUTPUT, specific=siddhi_DefinitionWindow)
gen_siddhi_DefinitionTrigger_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionTrigger)
gen_siddhi_DefinitionTrigger_TRIGGER = Generalization(general=TRIGGER, specific=siddhi_DefinitionTrigger)
gen_siddhi_DefinitionTrigger_AT = Generalization(general=AT, specific=siddhi_DefinitionTrigger)
gen_siddhi_DefinitionFunction_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionFunction)
gen_siddhi_DefinitionFunction_FUNCTION = Generalization(general=FUNCTION, specific=siddhi_DefinitionFunction)
gen_siddhi_DefinitionFunction_RETURN = Generalization(general=RETURN, specific=siddhi_DefinitionFunction)
gen_siddhi_DefinitionAggregation_DEFINE = Generalization(general=DEFINE, specific=siddhi_DefinitionAggregation)
gen_siddhi_DefinitionAggregation_AGGREGATION = Generalization(general=AGGREGATION, specific=siddhi_DefinitionAggregation)
gen_siddhi_DefinitionAggregation_FROM = Generalization(general=FROM, specific=siddhi_DefinitionAggregation)
gen_siddhi_DefinitionAggregation_AGGREGATE = Generalization(general=AGGREGATE, specific=siddhi_DefinitionAggregation)
gen_siddhi_DefinitionAggregation_BY = Generalization(general=BY, specific=siddhi_DefinitionAggregation)
gen_siddhi_AggregationTimeInterval_AggregationTime = Generalization(general=AggregationTime, specific=siddhi_AggregationTimeInterval)
gen_siddhi_AggregationTimeDuration_SECONDS = Generalization(general=SECONDS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_MINUTES = Generalization(general=MINUTES, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_HOURS = Generalization(general=HOURS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_DAYS = Generalization(general=DAYS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_WEEKS = Generalization(general=WEEKS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_MONTHS = Generalization(general=MONTHS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeDuration_YEARS = Generalization(general=YEARS, specific=siddhi_AggregationTimeDuration)
gen_siddhi_AggregationTimeRange_AggregationTime = Generalization(general=AggregationTime, specific=siddhi_AggregationTimeRange)
gen_siddhi_Features_FeaturesOrOutAttr = Generalization(general=FeaturesOrOutAttr, specific=siddhi_Features)
gen_siddhi_AttributeType_STRINGS = Generalization(general=STRINGS, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_INTS = Generalization(general=INTS, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_LONG = Generalization(general=LONG, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_FLOAT = Generalization(general=FLOAT, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_DOUBLE = Generalization(general=DOUBLE, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_BOOL = Generalization(general=BOOL, specific=siddhi_AttributeType)
gen_siddhi_AttributeType_OBJECT = Generalization(general=OBJECT, specific=siddhi_AttributeType)
gen_siddhi_Source1_Source1OrStandardStatefulSource = Generalization(general=Source1OrStandardStatefulSource, specific=siddhi_Source1)
gen_siddhi_ExecPartition_PARTITION = Generalization(general=PARTITION, specific=siddhi_ExecPartition)
gen_siddhi_ExecPartition_WITH = Generalization(general=WITH, specific=siddhi_ExecPartition)
gen_siddhi_ExecPartition_BEGIN = Generalization(general=BEGIN, specific=siddhi_ExecPartition)
gen_siddhi_ExecPartition_END = Generalization(general=END, specific=siddhi_ExecPartition)
gen_siddhi_ConditionRanges_PartitionWithStream = Generalization(general=PartitionWithStream, specific=siddhi_ConditionRanges)
gen_siddhi_Query_FROM = Generalization(general=FROM, specific=siddhi_Query)
gen_siddhi_QueryOutput_INSERT = Generalization(general=INSERT, specific=siddhi_QueryOutput)
gen_siddhi_QueryOutput_INTO = Generalization(general=INTO, specific=siddhi_QueryOutput)
gen_siddhi_QueryOutput_DELETE = Generalization(general=DELETE, specific=siddhi_QueryOutput)
gen_siddhi_QueryOutput_FOR = Generalization(general=FOR, specific=siddhi_QueryOutput)
gen_siddhi_QueryOutput_UPDATE = Generalization(general=UPDATE, specific=siddhi_QueryOutput)
gen_siddhi_QueryOutput_RETURN = Generalization(general=RETURN, specific=siddhi_QueryOutput)
gen_siddhi_SetClause_SET = Generalization(general=SET, specific=siddhi_SetClause)
gen_siddhi_OutputEventType_ALL = Generalization(general=ALL, specific=siddhi_OutputEventType)
gen_siddhi_OutputEventType_EVENTS = Generalization(general=EVENTS, specific=siddhi_OutputEventType)
gen_siddhi_OutputEventType_RAW = Generalization(general=RAW, specific=siddhi_OutputEventType)
gen_siddhi_OutputEventType_EXPIRED = Generalization(general=EXPIRED, specific=siddhi_OutputEventType)
gen_siddhi_OutputEventType_CURRENT = Generalization(general=CURRENT, specific=siddhi_OutputEventType)
gen_siddhi_OutputRate_OUTPUT = Generalization(general=OUTPUT, specific=siddhi_OutputRate)
gen_siddhi_OutputRate_EVENTS = Generalization(general=EVENTS, specific=siddhi_OutputRate)
gen_siddhi_OutputRate_SNAPSHOT = Generalization(general=SNAPSHOT, specific=siddhi_OutputRate)
gen_siddhi_OutputRateType_ALL = Generalization(general=ALL, specific=siddhi_OutputRateType)
gen_siddhi_OutputRateType_LAST = Generalization(general=LAST, specific=siddhi_OutputRateType)
gen_siddhi_OutputRateType_FIRST = Generalization(general=FIRST, specific=siddhi_OutputRateType)
gen_siddhi_GroupByQuerySelection_SELECT = Generalization(general=SELECT, specific=siddhi_GroupByQuerySelection)
gen_siddhi_GroupBy_GROUP = Generalization(general=GROUP, specific=siddhi_GroupBy)
gen_siddhi_GroupBy_BY = Generalization(general=BY, specific=siddhi_GroupBy)
gen_siddhi_HavingExpr_HAVING = Generalization(general=HAVING, specific=siddhi_HavingExpr)
gen_siddhi_OutAttr_FeaturesOrOutAttr = Generalization(general=FeaturesOrOutAttr, specific=siddhi_OutAttr)
gen_siddhi_SequenceSource_SequenceSourceChain = Generalization(general=SequenceSourceChain, specific=siddhi_SequenceSource)
gen_siddhi_SequenceCollectionStatefulSource_SequenceSource = Generalization(general=SequenceSource, specific=siddhi_SequenceCollectionStatefulSource)
gen_siddhi_AnonymousStream_FROM = Generalization(general=FROM, specific=siddhi_AnonymousStream)
gen_siddhi_AnonymousStream_RETURN = Generalization(general=RETURN, specific=siddhi_AnonymousStream)
gen_siddhi_EveryPatternSourceChain_PatternStream = Generalization(general=PatternStream, specific=siddhi_EveryPatternSourceChain)
gen_siddhi_LogicalStatefulSource_SequenceSource = Generalization(general=SequenceSource, specific=siddhi_LogicalStatefulSource)
gen_siddhi_LogicalAbsentStatefulSource_SequenceSource = Generalization(general=SequenceSource, specific=siddhi_LogicalAbsentStatefulSource)
gen_siddhi_AbsentPatternSourceChain_PatternStream = Generalization(general=PatternStream, specific=siddhi_AbsentPatternSourceChain)
gen_siddhi_EveryAbsentPatternSource_AbsentPatternSourceChain = Generalization(general=AbsentPatternSourceChain, specific=siddhi_EveryAbsentPatternSource)
gen_siddhi_ForTime_FOR = Generalization(general=FOR, specific=siddhi_ForTime)
gen_siddhi_LeftAbsentPatternSource_AbsentPatternSourceChain = Generalization(general=AbsentPatternSourceChain, specific=siddhi_LeftAbsentPatternSource)
gen_siddhi_RightAbsentPatternSource_AbsentPatternSourceChain = Generalization(general=AbsentPatternSourceChain, specific=siddhi_RightAbsentPatternSource)
gen_siddhi_WithinTimeRange_WITHIN = Generalization(general=WITHIN, specific=siddhi_WithinTimeRange)
gen_siddhi_Per1_PER = Generalization(general=PER, specific=siddhi_Per1)
gen_siddhi_StreamAlias_Source1OrStandardStatefulSource = Generalization(general=Source1OrStandardStatefulSource, specific=siddhi_StreamAlias)
gen_siddhi_WithinTime_WITHIN = Generalization(general=WITHIN, specific=siddhi_WithinTime)
gen_siddhi_joins_LEFT = Generalization(general=LEFT, specific=siddhi_joins)
gen_siddhi_joins_OUTER = Generalization(general=OUTER, specific=siddhi_joins)
gen_siddhi_joins_JOIN = Generalization(general=JOIN, specific=siddhi_joins)
gen_siddhi_joins_RIGHT = Generalization(general=RIGHT, specific=siddhi_joins)
gen_siddhi_joins_FULL = Generalization(general=FULL, specific=siddhi_joins)
gen_siddhi_joins_INNER = Generalization(general=INNER, specific=siddhi_joins)
gen_siddhi_StandardStream_JoinStream = Generalization(general=JoinStream, specific=siddhi_StandardStream)
gen_siddhi_MainSource_JoinSource = Generalization(general=JoinSource, specific=siddhi_MainSource)
gen_siddhi_MainSource_StandardStream = Generalization(general=StandardStream, specific=siddhi_MainSource)
gen_siddhi_BasicSourceStreamHandlers1_WINDOW = Generalization(general=WINDOW, specific=siddhi_BasicSourceStreamHandlers1)
gen_siddhi_Win_WINDOW = Generalization(general=WINDOW, specific=siddhi_Win)
gen_siddhi_MathOperation_Expression = Generalization(general=Expression, specific=siddhi_MathOperation)
gen_siddhi_MathAddsubOperation_MathOperation = Generalization(general=MathOperation, specific=siddhi_MathAddsubOperation)
gen_siddhi_MathDivmulOperation_MathAddsubOperation = Generalization(general=MathAddsubOperation, specific=siddhi_MathDivmulOperation)
gen_siddhi_MathOtherOperations_MathDivmulOperation = Generalization(general=MathDivmulOperation, specific=siddhi_MathOtherOperations)
gen_siddhi_NullCheck_MathOtherOperations = Generalization(general=MathOtherOperations, specific=siddhi_NullCheck)
gen_siddhi_NullCheck_IS = Generalization(general=IS, specific=siddhi_NullCheck)
gen_siddhi_NullCheck_NULL = Generalization(general=NULL, specific=siddhi_NullCheck)
gen_siddhi_AttributeReference_SetAssignment = Generalization(general=SetAssignment, specific=siddhi_AttributeReference)
gen_siddhi_StandardStatefulSource_SequenceSource = Generalization(general=SequenceSource, specific=siddhi_StandardStatefulSource)
gen_siddhi_StandardStatefulSource_SequenceCollectionStatefulSource = Generalization(general=SequenceCollectionStatefulSource, specific=siddhi_StandardStatefulSource)
gen_siddhi_StandardStatefulSource_PatternCollectionStatefulSource = Generalization(general=PatternCollectionStatefulSource, specific=siddhi_StandardStatefulSource)
gen_siddhi_StandardStatefulSource_Source1OrStandardStatefulSource = Generalization(general=Source1OrStandardStatefulSource, specific=siddhi_StandardStatefulSource)
gen_siddhi_AttributeIndex_LAST = Generalization(general=LAST, specific=siddhi_AttributeIndex)
gen_siddhi_BoolValue_TRUE = Generalization(general=TRUE, specific=siddhi_BoolValue)
gen_siddhi_BoolValue_FALSE = Generalization(general=FALSE, specific=siddhi_BoolValue)
gen_siddhi_YearValue_YEARS = Generalization(general=YEARS, specific=siddhi_YearValue)
gen_siddhi_MonthValue_MONTHS = Generalization(general=MONTHS, specific=siddhi_MonthValue)
gen_siddhi_WeekValue_WEEKS = Generalization(general=WEEKS, specific=siddhi_WeekValue)
gen_siddhi_DayValue_DAYS = Generalization(general=DAYS, specific=siddhi_DayValue)
gen_siddhi_HourValue_HOURS = Generalization(general=HOURS, specific=siddhi_HourValue)
gen_siddhi_MinuteValue_MINUTES = Generalization(general=MINUTES, specific=siddhi_MinuteValue)
gen_siddhi_SecondValue_SECONDS = Generalization(general=SECONDS, specific=siddhi_SecondValue)
gen_siddhi_MillisecondValue_MILLISECONDS = Generalization(general=MILLISECONDS, specific=siddhi_MillisecondValue)
gen_siddhi_DOUBLE_LITERAL_SignedDoubleValue = Generalization(general=SignedDoubleValue, specific=siddhi_DOUBLE_LITERAL)
gen_siddhi_FLOAT_LITERAL_SignedFloatValue = Generalization(general=SignedFloatValue, specific=siddhi_FLOAT_LITERAL)
gen_siddhi_LONG_LITERAL_SignedLongValue = Generalization(general=SignedLongValue, specific=siddhi_LONG_LITERAL)
gen_siddhi_Keyword_STRINGS = Generalization(general=STRINGS, specific=siddhi_Keyword)
gen_siddhi_Keyword_Name = Generalization(general=Name, specific=siddhi_Keyword)
gen_siddhi_Keyword_STREAM = Generalization(general=STREAM, specific=siddhi_Keyword)
gen_siddhi_Keyword_DEFINE = Generalization(general=DEFINE, specific=siddhi_Keyword)
gen_siddhi_Keyword_FROM = Generalization(general=FROM, specific=siddhi_Keyword)
gen_siddhi_Keyword_SELECT = Generalization(general=SELECT, specific=siddhi_Keyword)
gen_siddhi_Keyword_INSERT = Generalization(general=INSERT, specific=siddhi_Keyword)
gen_siddhi_Keyword_INTO = Generalization(general=INTO, specific=siddhi_Keyword)
gen_siddhi_Keyword_ALL = Generalization(general=ALL, specific=siddhi_Keyword)
gen_siddhi_Keyword_EVENTS = Generalization(general=EVENTS, specific=siddhi_Keyword)
gen_siddhi_Keyword_TABLE = Generalization(general=TABLE, specific=siddhi_Keyword)
gen_siddhi_Keyword_WINDOW = Generalization(general=WINDOW, specific=siddhi_Keyword)
gen_siddhi_Keyword_OUTPUT = Generalization(general=OUTPUT, specific=siddhi_Keyword)
gen_siddhi_Keyword_RAW = Generalization(general=RAW, specific=siddhi_Keyword)
gen_siddhi_Keyword_EXPIRED = Generalization(general=EXPIRED, specific=siddhi_Keyword)
gen_siddhi_Keyword_CURRENT = Generalization(general=CURRENT, specific=siddhi_Keyword)
gen_siddhi_Keyword_RETURN = Generalization(general=RETURN, specific=siddhi_Keyword)
gen_siddhi_Keyword_PARTITION = Generalization(general=PARTITION, specific=siddhi_Keyword)
gen_siddhi_Keyword_WITHIN = Generalization(general=WITHIN, specific=siddhi_Keyword)
gen_siddhi_Keyword_LEFT = Generalization(general=LEFT, specific=siddhi_Keyword)
gen_siddhi_Keyword_RIGHT = Generalization(general=RIGHT, specific=siddhi_Keyword)
gen_siddhi_Keyword_FULL = Generalization(general=FULL, specific=siddhi_Keyword)
gen_siddhi_Keyword_JOIN = Generalization(general=JOIN, specific=siddhi_Keyword)
gen_siddhi_Keyword_OUTER = Generalization(general=OUTER, specific=siddhi_Keyword)
gen_siddhi_Keyword_INNER = Generalization(general=INNER, specific=siddhi_Keyword)
gen_siddhi_Keyword_YEARS = Generalization(general=YEARS, specific=siddhi_Keyword)
gen_siddhi_Keyword_MONTHS = Generalization(general=MONTHS, specific=siddhi_Keyword)
gen_siddhi_Keyword_WEEKS = Generalization(general=WEEKS, specific=siddhi_Keyword)
gen_siddhi_Keyword_DAYS = Generalization(general=DAYS, specific=siddhi_Keyword)
gen_siddhi_Keyword_HOURS = Generalization(general=HOURS, specific=siddhi_Keyword)
gen_siddhi_Keyword_MINUTES = Generalization(general=MINUTES, specific=siddhi_Keyword)
gen_siddhi_Keyword_SECONDS = Generalization(general=SECONDS, specific=siddhi_Keyword)
gen_siddhi_Keyword_MILLISECONDS = Generalization(general=MILLISECONDS, specific=siddhi_Keyword)
gen_siddhi_Keyword_DELETE = Generalization(general=DELETE, specific=siddhi_Keyword)
gen_siddhi_Keyword_INTS = Generalization(general=INTS, specific=siddhi_Keyword)
gen_siddhi_Keyword_LONG = Generalization(general=LONG, specific=siddhi_Keyword)
gen_siddhi_Keyword_FLOAT = Generalization(general=FLOAT, specific=siddhi_Keyword)
gen_siddhi_Keyword_DOUBLE = Generalization(general=DOUBLE, specific=siddhi_Keyword)
gen_siddhi_Keyword_BOOL = Generalization(general=BOOL, specific=siddhi_Keyword)
gen_siddhi_Keyword_OBJECT = Generalization(general=OBJECT, specific=siddhi_Keyword)
gen_siddhi_Keyword_IS = Generalization(general=IS, specific=siddhi_Keyword)
gen_siddhi_Keyword_NULL = Generalization(general=NULL, specific=siddhi_Keyword)
gen_siddhi_Keyword_SNAPSHOT = Generalization(general=SNAPSHOT, specific=siddhi_Keyword)
gen_siddhi_Keyword_LAST = Generalization(general=LAST, specific=siddhi_Keyword)
gen_siddhi_Keyword_FIRST = Generalization(general=FIRST, specific=siddhi_Keyword)
gen_siddhi_Keyword_GROUP = Generalization(general=GROUP, specific=siddhi_Keyword)
gen_siddhi_Keyword_BY = Generalization(general=BY, specific=siddhi_Keyword)
gen_siddhi_Keyword_HAVING = Generalization(general=HAVING, specific=siddhi_Keyword)
gen_siddhi_Keyword_WITH = Generalization(general=WITH, specific=siddhi_Keyword)
gen_siddhi_Keyword_BEGIN = Generalization(general=BEGIN, specific=siddhi_Keyword)
gen_siddhi_Keyword_END = Generalization(general=END, specific=siddhi_Keyword)
gen_siddhi_Keyword_FOR = Generalization(general=FOR, specific=siddhi_Keyword)
gen_siddhi_Keyword_TRUE = Generalization(general=TRUE, specific=siddhi_Keyword)
gen_siddhi_Keyword_FALSE = Generalization(general=FALSE, specific=siddhi_Keyword)
gen_siddhi_Keyword_UPDATE = Generalization(general=UPDATE, specific=siddhi_Keyword)
gen_siddhi_APP_AppAnnotation = Generalization(general=AppAnnotation, specific=siddhi_APP)
gen_siddhi_NOT_LogicalAbsentStatefulSource = Generalization(general=LogicalAbsentStatefulSource, specific=siddhi_NOT)
gen_siddhi_NOT_BasicAbsentPatternSource = Generalization(general=BasicAbsentPatternSource, specific=siddhi_NOT)
gen_siddhi_EVERY_EverySequenceSourceChain = Generalization(general=EverySequenceSourceChain, specific=siddhi_EVERY)
gen_siddhi_EVERY_EveryAbsentSequenceSourceChain = Generalization(general=EveryAbsentSequenceSourceChain, specific=siddhi_EVERY)
gen_siddhi_EVERY_AbsentPatternSourceChain = Generalization(general=AbsentPatternSourceChain, specific=siddhi_EVERY)
gen_siddhi_EVERY_EveryAbsentPatternSource = Generalization(general=EveryAbsentPatternSource, specific=siddhi_EVERY)
gen_siddhi_EVERY_LeftAbsentPatternSource = Generalization(general=LeftAbsentPatternSource, specific=siddhi_EVERY)
gen_siddhi_EVERY_RightAbsentPatternSource = Generalization(general=RightAbsentPatternSource, specific=siddhi_EVERY)
gen_siddhi_LeftAbsentSequenceSource1_LeftAbsentSequenceSource = Generalization(general=LeftAbsentSequenceSource, specific=siddhi_LeftAbsentSequenceSource1)
gen_siddhi_RightAbsentSequenceSource1_RightAbsentSequenceSource = Generalization(general=RightAbsentSequenceSource, specific=siddhi_RightAbsentSequenceSource1)
gen_siddhi_LeftAbsentPatternSource1_LeftAbsentPatternSource = Generalization(general=LeftAbsentPatternSource, specific=siddhi_LeftAbsentPatternSource1)
gen_siddhi_RightAbsentPatternSource1_RightAbsentPatternSource = Generalization(general=RightAbsentPatternSource, specific=siddhi_RightAbsentPatternSource1)
gen_siddhi_MathLogicalOperation_MathOperation = Generalization(general=MathOperation, specific=siddhi_MathLogicalOperation)
gen_siddhi_MathInOperation_MathOperation = Generalization(general=MathOperation, specific=siddhi_MathInOperation)
gen_siddhi_MathGtLtOperation_MathOperation = Generalization(general=MathOperation, specific=siddhi_MathGtLtOperation)
gen_siddhi_MathEqualOperation_MathOperation = Generalization(general=MathOperation, specific=siddhi_MathEqualOperation)
gen_siddhi_NotOperation_MathOtherOperations = Generalization(general=MathOtherOperations, specific=siddhi_NotOperation)

# Domain Model
domain_model = DomainModel(
    name="siddhi",
    types={siddhi_DefinitionAggregation, siddhi_ExecutionElement, siddhi_SiddhiQL, siddhi_ExecutionPlan, siddhi_AppAnnotation, siddhi_DefinitionStream, siddhi_DefinitionTable, siddhi_DefinitionWindow, siddhi_DefinitionTrigger, siddhi_DefinitionFunction, siddhi_ExecPartition, siddhi_Query, DEFINE, STREAM, siddhi_Annotation, siddhi_Source1, siddhi_Features, TABLE, WINDOW, OUTPUT, siddhi_AttributeType, siddhi_FunctionOperation, siddhi_OutputEventType, TRIGGER, AT, siddhi_TriggerName, siddhi_EVERY, siddhi_TimeValue, siddhi_StringValue, FUNCTION, RETURN, siddhi_FunctionName, siddhi_LanguageName, siddhi_FunctionBody, AGGREGATION, FROM, AGGREGATE, BY, siddhi_StandardStream, siddhi_GroupByQuerySelection, siddhi_AttributeReference, siddhi_AggregationTime, siddhi_AggregationTimeDuration, siddhi_AggregationTimeInterval, AggregationTime, SECONDS, MINUTES, HOURS, DAYS, WEEKS, MONTHS, YEARS, siddhi_AggregationTimeRange, siddhi_Name, siddhi_AnnotationElement, siddhi_PropertyName, siddhi_PropertyValue, siddhi_PropertySeparator, FeaturesOrOutAttr, STRINGS, INTS, LONG, FLOAT, DOUBLE, BOOL, OBJECT, siddhi_Source, Source1OrStandardStatefulSource, PARTITION, WITH, BEGIN, END, siddhi_PartitionWithStream, siddhi_ConditionRanges, PartitionWithStream, siddhi_OF, siddhi_ConditionRange, siddhi_OR, SET, siddhi_Expression, siddhi_AS, siddhi_QueryInput, siddhi_QuerySection, siddhi_OutputRate, siddhi_QueryOutput, INSERT, INTO, DELETE, FOR, UPDATE, siddhi_Target, siddhi_ON, siddhi_SetClause, siddhi_SetAssignment, ALL, EVENTS, RAW, EXPIRED, CURRENT, SNAPSHOT, siddhi_OutputRateType, LAST, FIRST, SELECT, siddhi_OutputAttribute, siddhi_GroupBy, siddhi_HavingExpr, GROUP, HAVING, siddhi_OutAttr, siddhi_RightAbsentSequenceSource, siddhi_Attribute, siddhi_JoinStream, siddhi_SequenceStream, siddhi_PatternStream, siddhi_AnonymousStream, siddhi_EverySequenceSourceChain, siddhi_EveryAbsentSequenceSourceChain, siddhi_SequenceSource, siddhi_WithinTime, siddhi_SequenceSourceChain, siddhi_AbsentSequenceSourceChain, siddhi_BasicAbsentPatternSource, siddhi_LeftAbsentSequenceSource, siddhi_EObject, SequenceSourceChain, siddhi_SequenceCollectionStatefulSource, SequenceSource, siddhi_EveryPatternSourceChain, PatternStream, siddhi_PatternSourceChain, siddhi_PatternSource, siddhi_LogicalStatefulSource, siddhi_PatternCollectionStatefulSource, siddhi_StandardStatefulSource, siddhi_LogicalAbsentStatefulSource, siddhi_AND, siddhi_Collect, siddhi_NOT, siddhi_BasicSource, siddhi_AbsentPatternSourceChain, siddhi_EveryAbsentPatternSource, AbsentPatternSourceChain, siddhi_ForTime, siddhi_LeftAbsentPatternSource, siddhi_RightAbsentPatternSource, siddhi_JoinSource, siddhi_UNIDIRECTIONAL, siddhi_WithinTimeRange, siddhi_Per1, siddhi_joins, WITHIN, PER, siddhi_StreamAlias, LEFT, OUTER, JOIN, RIGHT, FULL, INNER, JoinStream, siddhi_MainSource, JoinSource, StandardStream, siddhi_Win, siddhi_BasicSourceStreamHandlers, siddhi_BasicSourceStreamHandlers1, siddhi_BasicSourceStreamHandler, siddhi_Filter, siddhi_StreamFunction, siddhi_MathOperation, Expression, siddhi_MathAddsubOperation, MathOperation, siddhi_MathDivmulOperation, MathAddsubOperation, siddhi_MathOtherOperations, MathDivmulOperation, siddhi_Literal, siddhi_NullCheck, MathOtherOperations, IS, NULL, siddhi_StreamReference, siddhi_AttributeIndex, siddhi_ConstantValue, SetAssignment, siddhi_SourceOrEventReference, siddhi_FeaturesOrOutAttrReference, siddhi_FeaturesOrOutAttr, SequenceCollectionStatefulSource, PatternCollectionStatefulSource, siddhi_Source1OrStandardStatefulSource, siddhi_AttributeNameReference, siddhi_BoolValue, siddhi_SignedDoubleValue, siddhi_SignedFloatValue, siddhi_SignedLongValue, siddhi_FunctionNamespace, siddhi_FunctionId, siddhi_AttributeList, TRUE, FALSE, siddhi_YearValue, siddhi_MonthValue, siddhi_WeekValue, siddhi_DayValue, siddhi_HourValue, siddhi_MinuteValue, siddhi_SecondValue, siddhi_MillisecondValue, MILLISECONDS, siddhi_DOUBLE_LITERAL, SignedDoubleValue, siddhi_E, siddhi_D, siddhi_FLOAT_LITERAL, SignedFloatValue, siddhi_F, siddhi_LONG_LITERAL, SignedLongValue, siddhi_L, siddhi_Keyword, Name, siddhi_APP, AppAnnotation, LogicalAbsentStatefulSource, BasicAbsentPatternSource, siddhi_STREAM, siddhi_DEFINE, siddhi_TABLE, siddhi_WINDOW, EverySequenceSourceChain, EveryAbsentSequenceSourceChain, EveryAbsentPatternSource, LeftAbsentPatternSource, RightAbsentPatternSource, siddhi_IN, siddhi_LONG, siddhi_DOUBLE, siddhi_FLOAT, siddhi_BOOL, siddhi_OBJECT, siddhi_ALL, siddhi_EVENTS, siddhi_RAW, siddhi_EXPIRED, siddhi_OUTPUT, siddhi_STRINGS, siddhi_INTS, siddhi_INTO, siddhi_RETURN, siddhi_FROM, siddhi_WITHIN, siddhi_LEFT, siddhi_RIGHT, siddhi_FULL, siddhi_JOIN, siddhi_INNER, siddhi_OUTER, siddhi_CURRENT, siddhi_SELECT, siddhi_LAST, siddhi_GROUP, siddhi_IS, siddhi_BY, siddhi_NULL, siddhi_HAVING, siddhi_TRIGGER, siddhi_SNAPSHOT, siddhi_AT, siddhi_FIRST, siddhi_INSERT, siddhi_FUNCTION, siddhi_WEEKS, siddhi_BEGIN, siddhi_PLAN, siddhi_DELETE, siddhi_FOR, siddhi_UPDATE, siddhi_END, siddhi_PARTITION, siddhi_WITH, siddhi_AGGREGATION, siddhi_AGGREGATE, siddhi_SET, siddhi_PER, siddhi_YEARS, siddhi_MONTHS, siddhi_DAYS, siddhi_HOURS, siddhi_MINUTES, siddhi_SECONDS, siddhi_MILLISECONDS, siddhi_FALSE, siddhi_TRUE, siddhi_LeftAbsentSequenceSource1, LeftAbsentSequenceSource, siddhi_RightAbsentSequenceSource1, RightAbsentSequenceSource, siddhi_LeftAbsentPatternSource1, siddhi_RightAbsentPatternSource1, siddhi_MathLogicalOperation, siddhi_MathInOperation, siddhi_MathGtLtOperation, siddhi_MathEqualOperation, siddhi_NotOperation},
    associations={defAggregation13, elements0, appAnn1, defStream3, defTable5, def_window7, defTrigger9, defFunction11, exElement15, execPartition17, que19, ann21, src23, feature25, ann127, src30, feature33, ann236, src39, funcOp45, feature42, opEventType47, tn49, every51, tv53, sv55, fn57, ln59, propVal93, attr_type61, func_body63, ann65, src68, stdStream71, groupByQuerySel73, attrRef75, eve77, aggrTime80, aggrtimeDur82, name84, annElement86, ann89, propName91, or125, sv95, name98, ps101, nam103, type106, strId109, ann4111, partWithStream114, qu116, of119, str_id2120, conRange123, expr127, a129, sv131, ann3134, qInp137, querySec139, outRate141, qOutput143, outEventType145, tar148, on150, expr152, or155, setClause158, na160, src163, setAssignment166, op_rate_type168, every170, tv173, out_att176, grp_by178, grpByQuerySel180, having183, attr_ref185, expr188, outAttr191, attr_ref193, attr196, a198, js201, seqSrcChanin203, ps205, anonStream207, everySequenceSourceChain209, everyAbsentSequenceSourceChain211, seqSource213, wt215, ssc217, absSeqSrcChain219, seqSrcChain221, absentSequenceSourceChain225, wt5227, basicAbsentPatternSource230, leftAbsentSequenceSource232, rightAbsentSequenceSource234, left237, right239, leftAbsentSequenceSource242, wt6244, basicAbsentPatternSource247, sequenceSourceChain250, left1254, right1257, rightAbsentSequenceSource260, wt7262, sequenceSourceChain265, basicAbsentPatternSource268, left272, right275, wt1277, wt280, qi283, qs286, out_rate289, op_event_type292, left296, right298, eps301, wt303, psc306, every308, left312, right315, psc_2318, wt320, ps323, lss325, pss327, stdss329, logicalAbsStatefulSrc331, stdSource333, and336, or338, logicalAbsStatefulSrc342, stdSource344, and347, not350, bs352, basicAbsentPatternSource1354, basicAbsentPatternSource2357, basicAbsentPatternSource360, right1398, o363, absentPatternSrcChain367, wt1368, basicAbsentPS371, tv373, left376, right377, leftAbsPS381, wt2383, everyAbsPS386, everyPSC389, leftAbsPatternSrc393, left1396, nam443, rightAbsPS401, wt3403, everyPSC1406, everyAbsPS1409, left_source412, right_source414, right_uni417, on419, expr422, wtr425, p427, join429, left_uni431, startPattern434, endPattern437, exp440, tv445, window448, a449, strAlias452, postWindowHandlers455, src457, basicSSh460, basicSsHandler462, exp464, fo467, func_op470, fil473, sf475, exp477, fo480, func_op483, mlo487, left489, right491, op492, lit494, stream_ref496, attr_ref497, fo500, name503, aatr_index506, const_val508, fo510, attrRef513, expression516, name1519, OPEN_SQARE_BRACKETSattribute_index1521, name2524, OPEN_SQARE_BRACKETSattribute_index2527, featuresOrAttrRef530, srcoutAttrref532, coll534, src536, basic_ss_handlers539, src542, basic_ss_handlers545, na548, attrName1550, bv552, sdv554, sfv556, slv558, tv560, sv563, funcNamespace566, funcId568, attrList570, name572, name575, attr578, mathOp581, sv600, yv584, mv586, wv588, dv590, hv592, minv594, secv596, msecv598, l610, e603, d604, e606, f608, on619, a611, every613, uni616, and622, or625, not628, of631, name640, ann5642, basicSrc634, ft637, left645, and655, right647, left650, right652, or657, right660, in663, name664, right667, right669, not671},
    generalizations={gen_siddhi_DefinitionStream_DEFINE, gen_siddhi_DefinitionStream_STREAM, gen_siddhi_DefinitionTable_DEFINE, gen_siddhi_DefinitionTable_TABLE, gen_siddhi_DefinitionWindow_DEFINE, gen_siddhi_DefinitionWindow_WINDOW, gen_siddhi_DefinitionWindow_OUTPUT, gen_siddhi_DefinitionTrigger_DEFINE, gen_siddhi_DefinitionTrigger_TRIGGER, gen_siddhi_DefinitionTrigger_AT, gen_siddhi_DefinitionFunction_DEFINE, gen_siddhi_DefinitionFunction_FUNCTION, gen_siddhi_DefinitionFunction_RETURN, gen_siddhi_DefinitionAggregation_DEFINE, gen_siddhi_DefinitionAggregation_AGGREGATION, gen_siddhi_DefinitionAggregation_FROM, gen_siddhi_DefinitionAggregation_AGGREGATE, gen_siddhi_DefinitionAggregation_BY, gen_siddhi_AggregationTimeInterval_AggregationTime, gen_siddhi_AggregationTimeDuration_SECONDS, gen_siddhi_AggregationTimeDuration_MINUTES, gen_siddhi_AggregationTimeDuration_HOURS, gen_siddhi_AggregationTimeDuration_DAYS, gen_siddhi_AggregationTimeDuration_WEEKS, gen_siddhi_AggregationTimeDuration_MONTHS, gen_siddhi_AggregationTimeDuration_YEARS, gen_siddhi_AggregationTimeRange_AggregationTime, gen_siddhi_Features_FeaturesOrOutAttr, gen_siddhi_AttributeType_STRINGS, gen_siddhi_AttributeType_INTS, gen_siddhi_AttributeType_LONG, gen_siddhi_AttributeType_FLOAT, gen_siddhi_AttributeType_DOUBLE, gen_siddhi_AttributeType_BOOL, gen_siddhi_AttributeType_OBJECT, gen_siddhi_Source1_Source1OrStandardStatefulSource, gen_siddhi_ExecPartition_PARTITION, gen_siddhi_ExecPartition_WITH, gen_siddhi_ExecPartition_BEGIN, gen_siddhi_ExecPartition_END, gen_siddhi_ConditionRanges_PartitionWithStream, gen_siddhi_Query_FROM, gen_siddhi_QueryOutput_INSERT, gen_siddhi_QueryOutput_INTO, gen_siddhi_QueryOutput_DELETE, gen_siddhi_QueryOutput_FOR, gen_siddhi_QueryOutput_UPDATE, gen_siddhi_QueryOutput_RETURN, gen_siddhi_SetClause_SET, gen_siddhi_OutputEventType_ALL, gen_siddhi_OutputEventType_EVENTS, gen_siddhi_OutputEventType_RAW, gen_siddhi_OutputEventType_EXPIRED, gen_siddhi_OutputEventType_CURRENT, gen_siddhi_OutputRate_OUTPUT, gen_siddhi_OutputRate_EVENTS, gen_siddhi_OutputRate_SNAPSHOT, gen_siddhi_OutputRateType_ALL, gen_siddhi_OutputRateType_LAST, gen_siddhi_OutputRateType_FIRST, gen_siddhi_GroupByQuerySelection_SELECT, gen_siddhi_GroupBy_GROUP, gen_siddhi_GroupBy_BY, gen_siddhi_HavingExpr_HAVING, gen_siddhi_OutAttr_FeaturesOrOutAttr, gen_siddhi_SequenceSource_SequenceSourceChain, gen_siddhi_SequenceCollectionStatefulSource_SequenceSource, gen_siddhi_AnonymousStream_FROM, gen_siddhi_AnonymousStream_RETURN, gen_siddhi_EveryPatternSourceChain_PatternStream, gen_siddhi_LogicalStatefulSource_SequenceSource, gen_siddhi_LogicalAbsentStatefulSource_SequenceSource, gen_siddhi_AbsentPatternSourceChain_PatternStream, gen_siddhi_EveryAbsentPatternSource_AbsentPatternSourceChain, gen_siddhi_ForTime_FOR, gen_siddhi_LeftAbsentPatternSource_AbsentPatternSourceChain, gen_siddhi_RightAbsentPatternSource_AbsentPatternSourceChain, gen_siddhi_WithinTimeRange_WITHIN, gen_siddhi_Per1_PER, gen_siddhi_StreamAlias_Source1OrStandardStatefulSource, gen_siddhi_WithinTime_WITHIN, gen_siddhi_joins_LEFT, gen_siddhi_joins_OUTER, gen_siddhi_joins_JOIN, gen_siddhi_joins_RIGHT, gen_siddhi_joins_FULL, gen_siddhi_joins_INNER, gen_siddhi_StandardStream_JoinStream, gen_siddhi_MainSource_JoinSource, gen_siddhi_MainSource_StandardStream, gen_siddhi_BasicSourceStreamHandlers1_WINDOW, gen_siddhi_Win_WINDOW, gen_siddhi_MathOperation_Expression, gen_siddhi_MathAddsubOperation_MathOperation, gen_siddhi_MathDivmulOperation_MathAddsubOperation, gen_siddhi_MathOtherOperations_MathDivmulOperation, gen_siddhi_NullCheck_MathOtherOperations, gen_siddhi_NullCheck_IS, gen_siddhi_NullCheck_NULL, gen_siddhi_AttributeReference_SetAssignment, gen_siddhi_StandardStatefulSource_SequenceSource, gen_siddhi_StandardStatefulSource_SequenceCollectionStatefulSource, gen_siddhi_StandardStatefulSource_PatternCollectionStatefulSource, gen_siddhi_StandardStatefulSource_Source1OrStandardStatefulSource, gen_siddhi_AttributeIndex_LAST, gen_siddhi_BoolValue_TRUE, gen_siddhi_BoolValue_FALSE, gen_siddhi_YearValue_YEARS, gen_siddhi_MonthValue_MONTHS, gen_siddhi_WeekValue_WEEKS, gen_siddhi_DayValue_DAYS, gen_siddhi_HourValue_HOURS, gen_siddhi_MinuteValue_MINUTES, gen_siddhi_SecondValue_SECONDS, gen_siddhi_MillisecondValue_MILLISECONDS, gen_siddhi_DOUBLE_LITERAL_SignedDoubleValue, gen_siddhi_FLOAT_LITERAL_SignedFloatValue, gen_siddhi_LONG_LITERAL_SignedLongValue, gen_siddhi_Keyword_STRINGS, gen_siddhi_Keyword_Name, gen_siddhi_Keyword_STREAM, gen_siddhi_Keyword_DEFINE, gen_siddhi_Keyword_FROM, gen_siddhi_Keyword_SELECT, gen_siddhi_Keyword_INSERT, gen_siddhi_Keyword_INTO, gen_siddhi_Keyword_ALL, gen_siddhi_Keyword_EVENTS, gen_siddhi_Keyword_TABLE, gen_siddhi_Keyword_WINDOW, gen_siddhi_Keyword_OUTPUT, gen_siddhi_Keyword_RAW, gen_siddhi_Keyword_EXPIRED, gen_siddhi_Keyword_CURRENT, gen_siddhi_Keyword_RETURN, gen_siddhi_Keyword_PARTITION, gen_siddhi_Keyword_WITHIN, gen_siddhi_Keyword_LEFT, gen_siddhi_Keyword_RIGHT, gen_siddhi_Keyword_FULL, gen_siddhi_Keyword_JOIN, gen_siddhi_Keyword_OUTER, gen_siddhi_Keyword_INNER, gen_siddhi_Keyword_YEARS, gen_siddhi_Keyword_MONTHS, gen_siddhi_Keyword_WEEKS, gen_siddhi_Keyword_DAYS, gen_siddhi_Keyword_HOURS, gen_siddhi_Keyword_MINUTES, gen_siddhi_Keyword_SECONDS, gen_siddhi_Keyword_MILLISECONDS, gen_siddhi_Keyword_DELETE, gen_siddhi_Keyword_INTS, gen_siddhi_Keyword_LONG, gen_siddhi_Keyword_FLOAT, gen_siddhi_Keyword_DOUBLE, gen_siddhi_Keyword_BOOL, gen_siddhi_Keyword_OBJECT, gen_siddhi_Keyword_IS, gen_siddhi_Keyword_NULL, gen_siddhi_Keyword_SNAPSHOT, gen_siddhi_Keyword_LAST, gen_siddhi_Keyword_FIRST, gen_siddhi_Keyword_GROUP, gen_siddhi_Keyword_BY, gen_siddhi_Keyword_HAVING, gen_siddhi_Keyword_WITH, gen_siddhi_Keyword_BEGIN, gen_siddhi_Keyword_END, gen_siddhi_Keyword_FOR, gen_siddhi_Keyword_TRUE, gen_siddhi_Keyword_FALSE, gen_siddhi_Keyword_UPDATE, gen_siddhi_APP_AppAnnotation, gen_siddhi_NOT_LogicalAbsentStatefulSource, gen_siddhi_NOT_BasicAbsentPatternSource, gen_siddhi_EVERY_EverySequenceSourceChain, gen_siddhi_EVERY_EveryAbsentSequenceSourceChain, gen_siddhi_EVERY_AbsentPatternSourceChain, gen_siddhi_EVERY_EveryAbsentPatternSource, gen_siddhi_EVERY_LeftAbsentPatternSource, gen_siddhi_EVERY_RightAbsentPatternSource, gen_siddhi_LeftAbsentSequenceSource1_LeftAbsentSequenceSource, gen_siddhi_RightAbsentSequenceSource1_RightAbsentSequenceSource, gen_siddhi_LeftAbsentPatternSource1_LeftAbsentPatternSource, gen_siddhi_RightAbsentPatternSource1_RightAbsentPatternSource, gen_siddhi_MathLogicalOperation_MathOperation, gen_siddhi_MathInOperation_MathOperation, gen_siddhi_MathGtLtOperation_MathOperation, gen_siddhi_MathEqualOperation_MathOperation, gen_siddhi_NotOperation_MathOtherOperations},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)