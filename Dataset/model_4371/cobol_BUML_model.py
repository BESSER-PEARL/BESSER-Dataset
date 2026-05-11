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

# Enumerations
Properties: Enumeration = Enumeration(
    name="Properties",
    literals={
            EnumerationLiteral(name="initial"),
			EnumerationLiteral(name="common"),
			EnumerationLiteral(name="recursive")
    }
)

Nulls: Enumeration = Enumeration(
    name="Nulls",
    literals={
            EnumerationLiteral(name="null"),
			EnumerationLiteral(name="nulls")
    }
)

Zeroes: Enumeration = Enumeration(
    name="Zeroes",
    literals={
            EnumerationLiteral(name="zero"),
			EnumerationLiteral(name="zeros"),
			EnumerationLiteral(name="zeroes")
    }
)

Quotes: Enumeration = Enumeration(
    name="Quotes",
    literals={
            EnumerationLiteral(name="quote"),
			EnumerationLiteral(name="quotes")
    }
)

LowValues: Enumeration = Enumeration(
    name="LowValues",
    literals={
            EnumerationLiteral(name="lowValue"),
			EnumerationLiteral(name="lowValues")
    }
)

HighValues: Enumeration = Enumeration(
    name="HighValues",
    literals={
            EnumerationLiteral(name="highValue"),
			EnumerationLiteral(name="highValues")
    }
)

Spaces: Enumeration = Enumeration(
    name="Spaces",
    literals={
            EnumerationLiteral(name="space"),
			EnumerationLiteral(name="spaces")
    }
)

ThroughPhrase: Enumeration = Enumeration(
    name="ThroughPhrase",
    literals={
            EnumerationLiteral(name="through"),
			EnumerationLiteral(name="thru")
    }
)

EncodingTypes: Enumeration = Enumeration(
    name="EncodingTypes",
    literals={
            EnumerationLiteral(name="alphabetic"),
			EnumerationLiteral(name="alphanumeric"),
			EnumerationLiteral(name="alphanumericEdited"),
			EnumerationLiteral(name="national"),
			EnumerationLiteral(name="nationalEdited"),
			EnumerationLiteral(name="numeric"),
			EnumerationLiteral(name="numericEdited"),
			EnumerationLiteral(name="dbcs"),
			EnumerationLiteral(name="egcs")
    }
)

Adjustings: Enumeration = Enumeration(
    name="Adjustings",
    literals={
            EnumerationLiteral(name="up"),
			EnumerationLiteral(name="down")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="on"),
			EnumerationLiteral(name="off")
    }
)

ExitLabels: Enumeration = Enumeration(
    name="ExitLabels",
    literals={
            EnumerationLiteral(name="program"),
			EnumerationLiteral(name="paragraph"),
			EnumerationLiteral(name="method")
    }
)

EOP: Enumeration = Enumeration(
    name="EOP",
    literals={
            EnumerationLiteral(name="eop"),
			EnumerationLiteral(name="endOfPage")
    }
)

IOTypes: Enumeration = Enumeration(
    name="IOTypes",
    literals={
            EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="io"),
			EnumerationLiteral(name="extend")
    }
)

Orders: Enumeration = Enumeration(
    name="Orders",
    literals={
            EnumerationLiteral(name="asc"),
			EnumerationLiteral(name="dsc")
    }
)

Corresponding: Enumeration = Enumeration(
    name="Corresponding",
    literals={
            EnumerationLiteral(name="corr"),
			EnumerationLiteral(name="corresponding")
    }
)

ProgramDescriptionInfo: Enumeration = Enumeration(
    name="ProgramDescriptionInfo",
    literals={
            EnumerationLiteral(name="author"),
			EnumerationLiteral(name="installation"),
			EnumerationLiteral(name="dateWritten"),
			EnumerationLiteral(name="dateCompleted"),
			EnumerationLiteral(name="security")
    }
)

ObjectComputerDescriptionInfo: Enumeration = Enumeration(
    name="ObjectComputerDescriptionInfo",
    literals={
            EnumerationLiteral(name="memory"),
			EnumerationLiteral(name="size"),
			EnumerationLiteral(name="words"),
			EnumerationLiteral(name="characters"),
			EnumerationLiteral(name="modules"),
			EnumerationLiteral(name="segment"),
			EnumerationLiteral(name="program"),
			EnumerationLiteral(name="collating"),
			EnumerationLiteral(name="sequence"),
			EnumerationLiteral(name="segmentLimit")
    }
)

SelectStatementClauses: Enumeration = Enumeration(
    name="SelectStatementClauses",
    literals={
            EnumerationLiteral(name="alternate"),
			EnumerationLiteral(name="record"),
			EnumerationLiteral(name="key"),
			EnumerationLiteral(name="relative"),
			EnumerationLiteral(name="delimiter"),
			EnumerationLiteral(name="standard1"),
			EnumerationLiteral(name="padding"),
			EnumerationLiteral(name="character"),
			EnumerationLiteral(name="reserve"),
			EnumerationLiteral(name="area"),
			EnumerationLiteral(name="areas"),
			EnumerationLiteral(name="access"),
			EnumerationLiteral(name="mode"),
			EnumerationLiteral(name="is_"),
			EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="random"),
			EnumerationLiteral(name="with_"),
			EnumerationLiteral(name="dynamic"),
			EnumerationLiteral(name="organization"),
			EnumerationLiteral(name="duplicates"),
			EnumerationLiteral(name="indexed")
    }
)

SpecialNamesClauses: Enumeration = Enumeration(
    name="SpecialNamesClauses",
    literals={
            EnumerationLiteral(name="decimalPoint"),
			EnumerationLiteral(name="is_"),
			EnumerationLiteral(name="comma"),
			EnumerationLiteral(name="xmlSchema")
    }
)

FileDescriptionInfo: Enumeration = Enumeration(
    name="FileDescriptionInfo",
    literals={
            EnumerationLiteral(name="block"),
			EnumerationLiteral(name="contains"),
			EnumerationLiteral(name="to"),
			EnumerationLiteral(name="characters"),
			EnumerationLiteral(name="records"),
			EnumerationLiteral(name="codeSet"),
			EnumerationLiteral(name="is_"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="record"),
			EnumerationLiteral(name="are"),
			EnumerationLiteral(name="label"),
			EnumerationLiteral(name="omitted"),
			EnumerationLiteral(name="standard"),
			EnumerationLiteral(name="linage"),
			EnumerationLiteral(name="lines"),
			EnumerationLiteral(name="with_"),
			EnumerationLiteral(name="footing"),
			EnumerationLiteral(name="at"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="varying"),
			EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="size"),
			EnumerationLiteral(name="from_"),
			EnumerationLiteral(name="depending"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="mode"),
			EnumerationLiteral(name="recording"),
			EnumerationLiteral(name="f"),
			EnumerationLiteral(name="v"),
			EnumerationLiteral(name="u"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="value"),
			EnumerationLiteral(name="of"),
			EnumerationLiteral(name="identification"),
			EnumerationLiteral(name="id"),
			EnumerationLiteral(name="report"),
			EnumerationLiteral(name="reports")
    }
)

DataDescriptionInfo: Enumeration = Enumeration(
    name="DataDescriptionInfo",
    literals={
            EnumerationLiteral(name="zeroes"),
			EnumerationLiteral(name="justified"),
			EnumerationLiteral(name="just"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="blank"),
			EnumerationLiteral(name="when"),
			EnumerationLiteral(name="zero"),
			EnumerationLiteral(name="zeros"),
			EnumerationLiteral(name="sign"),
			EnumerationLiteral(name="is_"),
			EnumerationLiteral(name="leading"),
			EnumerationLiteral(name="trailing"),
			EnumerationLiteral(name="separate"),
			EnumerationLiteral(name="character"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="format"),
			EnumerationLiteral(name="synchronized"),
			EnumerationLiteral(name="sync"),
			EnumerationLiteral(name="left")
    }
)

IOControlDescriptionInfo: Enumeration = Enumeration(
    name="IOControlDescriptionInfo",
    literals={
            EnumerationLiteral(name="rerun"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="of"),
			EnumerationLiteral(name="record"),
			EnumerationLiteral(name="records"),
			EnumerationLiteral(name="every"),
			EnumerationLiteral(name="same"),
			EnumerationLiteral(name="area"),
			EnumerationLiteral(name="for_"),
			EnumerationLiteral(name="multiple"),
			EnumerationLiteral(name="file"),
			EnumerationLiteral(name="tape"),
			EnumerationLiteral(name="contains"),
			EnumerationLiteral(name="position"),
			EnumerationLiteral(name="apply"),
			EnumerationLiteral(name="writeOnly"),
			EnumerationLiteral(name="sort"),
			EnumerationLiteral(name="sortMerge"),
			EnumerationLiteral(name="reel"),
			EnumerationLiteral(name="unit")
    }
)

RepositoryDescriptionInfo: Enumeration = Enumeration(
    name="RepositoryDescriptionInfo",
    literals={
            EnumerationLiteral(name="class_"),
			EnumerationLiteral(name="is_")
    }
)

CICSStatementTokens: Enumeration = Enumeration(
    name="CICSStatementTokens",
    literals={
            EnumerationLiteral(name="queue"),
			EnumerationLiteral(name="qname"),
			EnumerationLiteral(name="openpar"),
			EnumerationLiteral(name="closepar"),
			EnumerationLiteral(name="ts"),
			EnumerationLiteral(name="sysid"),
			EnumerationLiteral(name="sys"),
			EnumerationLiteral(name="set"),
			EnumerationLiteral(name="into"),
			EnumerationLiteral(name="length"),
			EnumerationLiteral(name="item"),
			EnumerationLiteral(name="next"),
			EnumerationLiteral(name="numitems"),
			EnumerationLiteral(name="td"),
			EnumerationLiteral(name="writeq"),
			EnumerationLiteral(name="from_"),
			EnumerationLiteral(name="rewrite"),
			EnumerationLiteral(name="nosuspend"),
			EnumerationLiteral(name="main"),
			EnumerationLiteral(name="auxiliary"),
			EnumerationLiteral(name="deleteq"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="file"),
			EnumerationLiteral(name="dataset"),
			EnumerationLiteral(name="ridfld"),
			EnumerationLiteral(name="keylength"),
			EnumerationLiteral(name="generic"),
			EnumerationLiteral(name="gteq"),
			EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="uncommitted"),
			EnumerationLiteral(name="consistent"),
			EnumerationLiteral(name="repeatable"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="token"),
			EnumerationLiteral(name="rba"),
			EnumerationLiteral(name="xrba"),
			EnumerationLiteral(name="rrn"),
			EnumerationLiteral(name="write"),
			EnumerationLiteral(name="massinsert"),
			EnumerationLiteral(name="program"),
			EnumerationLiteral(name="commarea"),
			EnumerationLiteral(name="datalength"),
			EnumerationLiteral(name="synconreturn"),
			EnumerationLiteral(name="transid"),
			EnumerationLiteral(name="inputmsg"),
			EnumerationLiteral(name="inputmsglen"),
			EnumerationLiteral(name="channel"),
			EnumerationLiteral(name="xctl"),
			EnumerationLiteral(name="load"),
			EnumerationLiteral(name="start"),
			EnumerationLiteral(name="tr")
    }
)

SQLStatementTokens: Enumeration = Enumeration(
    name="SQLStatementTokens",
    literals={
            EnumerationLiteral(name="select"),
			EnumerationLiteral(name="declare"),
			EnumerationLiteral(name="from_"),
			EnumerationLiteral(name="insert"),
			EnumerationLiteral(name="include"),
			EnumerationLiteral(name="into"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

InvokeStatementTokens: Enumeration = Enumeration(
    name="InvokeStatementTokens",
    literals={
            EnumerationLiteral(name="self"),
			EnumerationLiteral(name="super"),
			EnumerationLiteral(name="new"),
			EnumerationLiteral(name="using"),
			EnumerationLiteral(name="by"),
			EnumerationLiteral(name="value"),
			EnumerationLiteral(name="length"),
			EnumerationLiteral(name="of"),
			EnumerationLiteral(name="returning")
    }
)

AcceptStatementTokens: Enumeration = Enumeration(
    name="AcceptStatementTokens",
    literals={
            EnumerationLiteral(name="from_"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="day"),
			EnumerationLiteral(name="dow"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="dateformat1"),
			EnumerationLiteral(name="dateformat2")
    }
)

UseStatementTokens: Enumeration = Enumeration(
    name="UseStatementTokens",
    literals={
            EnumerationLiteral(name="global_"),
			EnumerationLiteral(name="after"),
			EnumerationLiteral(name="standard"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="exception"),
			EnumerationLiteral(name="procedure"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="extend"),
			EnumerationLiteral(name="for_"),
			EnumerationLiteral(name="debugging"),
			EnumerationLiteral(name="all"),
			EnumerationLiteral(name="procedures"),
			EnumerationLiteral(name="beginning"),
			EnumerationLiteral(name="ending"),
			EnumerationLiteral(name="file"),
			EnumerationLiteral(name="reel"),
			EnumerationLiteral(name="unit"),
			EnumerationLiteral(name="label"),
			EnumerationLiteral(name="io")
    }
)

CloseStatementTokens: Enumeration = Enumeration(
    name="CloseStatementTokens",
    literals={
            EnumerationLiteral(name="for_"),
			EnumerationLiteral(name="removal"),
			EnumerationLiteral(name="with_"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="rewind"),
			EnumerationLiteral(name="lock"),
			EnumerationLiteral(name="reel"),
			EnumerationLiteral(name="unit")
    }
)

OpenStatementTokens: Enumeration = Enumeration(
    name="OpenStatementTokens",
    literals={
            EnumerationLiteral(name="reversed"),
			EnumerationLiteral(name="with_"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="rewind")
    }
)

SortPhraseTokens: Enumeration = Enumeration(
    name="SortPhraseTokens",
    literals={
            EnumerationLiteral(name="with_"),
			EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="order"),
			EnumerationLiteral(name="sequence"),
			EnumerationLiteral(name="duplicates"),
			EnumerationLiteral(name="collating"),
			EnumerationLiteral(name="is_")
    }
)

Selects: Enumeration = Enumeration(
    name="Selects",
    literals={
            EnumerationLiteral(name="s1"),
			EnumerationLiteral(name="s2"),
			EnumerationLiteral(name="s3"),
			EnumerationLiteral(name="s4"),
			EnumerationLiteral(name="s5")
    }
)

UPSISwitches: Enumeration = Enumeration(
    name="UPSISwitches",
    literals={
            EnumerationLiteral(name="upsi0"),
			EnumerationLiteral(name="upsi1"),
			EnumerationLiteral(name="upsi2"),
			EnumerationLiteral(name="upsi3"),
			EnumerationLiteral(name="upsi4"),
			EnumerationLiteral(name="upsi5"),
			EnumerationLiteral(name="upsi6"),
			EnumerationLiteral(name="upsi7")
    }
)

Channels: Enumeration = Enumeration(
    name="Channels",
    literals={
            EnumerationLiteral(name="c1"),
			EnumerationLiteral(name="c2"),
			EnumerationLiteral(name="c3"),
			EnumerationLiteral(name="c4"),
			EnumerationLiteral(name="c5"),
			EnumerationLiteral(name="c6"),
			EnumerationLiteral(name="c7"),
			EnumerationLiteral(name="c8"),
			EnumerationLiteral(name="c9"),
			EnumerationLiteral(name="c10"),
			EnumerationLiteral(name="c11"),
			EnumerationLiteral(name="c12")
    }
)

SystemInputs: Enumeration = Enumeration(
    name="SystemInputs",
    literals={
            EnumerationLiteral(name="sysin"),
			EnumerationLiteral(name="sysipt")
    }
)

SystemOutputs: Enumeration = Enumeration(
    name="SystemOutputs",
    literals={
            EnumerationLiteral(name="sysout"),
			EnumerationLiteral(name="syslist"),
			EnumerationLiteral(name="syslst")
    }
)

SystemPunchDevices: Enumeration = Enumeration(
    name="SystemPunchDevices",
    literals={
            EnumerationLiteral(name="syspunch"),
			EnumerationLiteral(name="syspch")
    }
)

PictureStringCharacters: Enumeration = Enumeration(
    name="PictureStringCharacters",
    literals={
            EnumerationLiteral(name="any"),
			EnumerationLiteral(name="blank"),
			EnumerationLiteral(name="sign"),
			EnumerationLiteral(name="leadingZero"),
			EnumerationLiteral(name="decimalPoint"),
			EnumerationLiteral(name="numeric"),
			EnumerationLiteral(name="assumedDecimalPoint"),
			EnumerationLiteral(name="alphabetic"),
			EnumerationLiteral(name="national"),
			EnumerationLiteral(name="credit"),
			EnumerationLiteral(name="debit"),
			EnumerationLiteral(name="zero"),
			EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="negative"),
			EnumerationLiteral(name="exponent"),
			EnumerationLiteral(name="period"),
			EnumerationLiteral(name="comma"),
			EnumerationLiteral(name="dollar"),
			EnumerationLiteral(name="asterik"),
			EnumerationLiteral(name="slash"),
			EnumerationLiteral(name="escape")
    }
)

Usages: Enumeration = Enumeration(
    name="Usages",
    literals={
            EnumerationLiteral(name="comp3"),
			EnumerationLiteral(name="computational4"),
			EnumerationLiteral(name="comp4"),
			EnumerationLiteral(name="computational5"),
			EnumerationLiteral(name="comp5"),
			EnumerationLiteral(name="pointer"),
			EnumerationLiteral(name="procedurePointer"),
			EnumerationLiteral(name="functionPointer"),
			EnumerationLiteral(name="national"),
			EnumerationLiteral(name="binary"),
			EnumerationLiteral(name="computational"),
			EnumerationLiteral(name="comp"),
			EnumerationLiteral(name="display"),
			EnumerationLiteral(name="display1"),
			EnumerationLiteral(name="index"),
			EnumerationLiteral(name="packedDecimal"),
			EnumerationLiteral(name="computational1"),
			EnumerationLiteral(name="comp1"),
			EnumerationLiteral(name="computational2"),
			EnumerationLiteral(name="comp2"),
			EnumerationLiteral(name="computational3")
    }
)

PredefinedAlphabetTypes: Enumeration = Enumeration(
    name="PredefinedAlphabetTypes",
    literals={
            EnumerationLiteral(name="standard1"),
			EnumerationLiteral(name="standard2"),
			EnumerationLiteral(name="ebcdic"),
			EnumerationLiteral(name="native")
    }
)

FileDescriptors: Enumeration = Enumeration(
    name="FileDescriptors",
    literals={
            EnumerationLiteral(name="fd"),
			EnumerationLiteral(name="sd")
    }
)

SortingOrder: Enumeration = Enumeration(
    name="SortingOrder",
    literals={
            EnumerationLiteral(name="asc"),
			EnumerationLiteral(name="dsc")
    }
)

Positions: Enumeration = Enumeration(
    name="Positions",
    literals={
            EnumerationLiteral(name="before"),
			EnumerationLiteral(name="after")
    }
)

Occurrences: Enumeration = Enumeration(
    name="Occurrences",
    literals={
            EnumerationLiteral(name="all"),
			EnumerationLiteral(name="leading"),
			EnumerationLiteral(name="first")
    }
)

# Classes
cobol_commons_NamedElement = Class(name="cobol_commons_NamedElement", is_abstract=True)
Commentable = Class(name="Commentable")
cobol_commons_Commentable = Class(name="cobol_commons_Commentable", is_abstract=True)
cobol_commons_LabellableElement = Class(name="cobol_commons_LabellableElement", is_abstract=True)
Negate = Class(name="Negate")
cobol_conditions_NegatedConditionalExpressionChild = Class(name="cobol_conditions_NegatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_SimpleConditionChild = Class(name="cobol_conditions_SimpleConditionChild", is_abstract=True)
cobol_conditions_RelationalExpression = Class(name="cobol_conditions_RelationalExpression")
SimpleConditionChild = Class(name="SimpleConditionChild")
RelationalOperator = Class(name="RelationalOperator")
Is = Class(name="Is")
cobol_commons_URIableElement = Class(name="cobol_commons_URIableElement", is_abstract=True)
cobol_conditions_Condition = Class(name="cobol_conditions_Condition", is_abstract=True)
cobol_conditions_ConditionalOrExpression = Class(name="cobol_conditions_ConditionalOrExpression")
Condition = Class(name="Condition")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
LogicalOperator = Class(name="LogicalOperator")
cobol_conditions_ConditionalOrExpressionChild = Class(name="cobol_conditions_ConditionalOrExpressionChild", is_abstract=True)
cobol_conditions_NegatedConditionalExpression = Class(name="cobol_conditions_NegatedConditionalExpression")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
NegatedConditionalExpressionChild = Class(name="NegatedConditionalExpressionChild")
cobol_conditions_NegatedAbbreviatedConditionalExpressionChild = Class(name="cobol_conditions_NegatedAbbreviatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_AbbreviatedRelationalExpression = Class(name="cobol_conditions_AbbreviatedRelationalExpression")
AbbreviatedRelationalExpressionChild = Class(name="AbbreviatedRelationalExpressionChild")
cobol_conditions_NestedAbbreviatedConditionalExpression = Class(name="cobol_conditions_NestedAbbreviatedConditionalExpression")
cobol_conditions_SignCondition = Class(name="cobol_conditions_SignCondition")
cobol_conditions_ExpressionList = Class(name="cobol_conditions_ExpressionList")
cobol_conditions_ConditionalAndExpressionChild = Class(name="cobol_conditions_ConditionalAndExpressionChild", is_abstract=True)
cobol_conditions_ConditionalAndExpression = Class(name="cobol_conditions_ConditionalAndExpression")
cobol_conditions_AbbreviatedConditionalExpression = Class(name="cobol_conditions_AbbreviatedConditionalExpression")
AbbreviatedConditionalExpressionChild = Class(name="AbbreviatedConditionalExpressionChild")
cobol_conditions_AbbreviatedConditionalExpressionChild = Class(name="cobol_conditions_AbbreviatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_NegatedAbbreviatedConditionalExpression = Class(name="cobol_conditions_NegatedAbbreviatedConditionalExpression")
NegatedAbbreviatedConditionalExpressionChild = Class(name="NegatedAbbreviatedConditionalExpressionChild")
cobol_conditions_NestedCondition = Class(name="cobol_conditions_NestedCondition")
cobol_arithmetics_AdditiveArithmeticExpression = Class(name="cobol_arithmetics_AdditiveArithmeticExpression")
RangeExpressionChild = Class(name="RangeExpressionChild")
AdditiveArithmeticExpressionChild = Class(name="AdditiveArithmeticExpressionChild")
AdditiveOperator = Class(name="AdditiveOperator")
cobol_arithmetics_AdditiveArithmeticExpressionChild = Class(name="cobol_arithmetics_AdditiveArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_MultiplicativeArithmeticExpression = Class(name="cobol_arithmetics_MultiplicativeArithmeticExpression")
MultiplicativeArithmeticExpressionChild = Class(name="MultiplicativeArithmeticExpressionChild")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
cobol_arithmetics_MultiplicativeArithmeticExpressionChild = Class(name="cobol_arithmetics_MultiplicativeArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_PowerArithmeticExpression = Class(name="cobol_arithmetics_PowerArithmeticExpression")
SignOperator = Class(name="SignOperator")
cobol_conditions_ClassCondition = Class(name="cobol_conditions_ClassCondition")
ClassOperator = Class(name="ClassOperator")
cobol_conditions_AbbreviatedRelationalExpressionChild = Class(name="cobol_conditions_AbbreviatedRelationalExpressionChild", is_abstract=True)
Through = Class(name="Through")
cobol_arithmetics_RangeExpressionChild = Class(name="cobol_arithmetics_RangeExpressionChild", is_abstract=True)
cobol_arithmetics_NestedArithmeticExpression = Class(name="cobol_arithmetics_NestedArithmeticExpression")
PrimaryExpression = Class(name="PrimaryExpression")
cobol_arithmetics_ArithmeticExpression = Class(name="cobol_arithmetics_ArithmeticExpression", is_abstract=True)
conditions_AbbreviatedRelationalExpressionChild = Class(name="conditions_AbbreviatedRelationalExpressionChild")
conditions_SimpleConditionChild = Class(name="conditions_SimpleConditionChild")
cobol_containers_CompilationGroup = Class(name="cobol_containers_CompilationGroup")
containers_CobolRoot = Class(name="containers_CobolRoot")
commons_NamedElement = Class(name="commons_NamedElement")
CompilationUnit = Class(name="CompilationUnit")
cobol_containers_CompilationUnit = Class(name="cobol_containers_CompilationUnit")
NamedElement = Class(name="NamedElement")
IdentificationDivision = Class(name="IdentificationDivision")
PowerArithmeticExpressionChild = Class(name="PowerArithmeticExpressionChild")
cobol_arithmetics_PowerArithmeticExpressionChild = Class(name="cobol_arithmetics_PowerArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_UnaryArithmeticExpressionChild = Class(name="cobol_arithmetics_UnaryArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_UnaryArithmeticExpression = Class(name="cobol_arithmetics_UnaryArithmeticExpression")
UnaryArithmeticExpressionChild = Class(name="UnaryArithmeticExpressionChild")
UnaryOperator = Class(name="UnaryOperator")
cobol_arithmetics_PrimaryExpression = Class(name="cobol_arithmetics_PrimaryExpression", is_abstract=True)
cobol_arithmetics_AssignmentExpression = Class(name="cobol_arithmetics_AssignmentExpression")
Equal = Class(name="Equal")
ArithmeticExpression = Class(name="ArithmeticExpression")
cobol_arithmetics_RangeExpression = Class(name="cobol_arithmetics_RangeExpression")
cobol_divisions_IdentificationDivision = Class(name="cobol_divisions_IdentificationDivision")
divisions_Division = Class(name="divisions_Division")
water_IncompleteElement = Class(name="water_IncompleteElement")
cobol_divisions_ProcedureDivision = Class(name="cobol_divisions_ProcedureDivision")
parameters_Parametrizable = Class(name="parameters_Parametrizable")
Declaratives = Class(name="Declaratives")
cobol_literals_Literal = Class(name="cobol_literals_Literal", is_abstract=True)
water_SelectStatementWater = Class(name="water_SelectStatementWater")
water_SpecialNamesParagraphWater = Class(name="water_SpecialNamesParagraphWater")
water_CICSStatementWater = Class(name="water_CICSStatementWater")
operands_PrimaryOperand = Class(name="operands_PrimaryOperand")
water_InvokeStatementWater = Class(name="water_InvokeStatementWater")
EnvironmentDivision = Class(name="EnvironmentDivision")
DataDivision = Class(name="DataDivision")
ProcedureDivision = Class(name="ProcedureDivision")
cobol_containers_CobolRoot = Class(name="cobol_containers_CobolRoot", is_abstract=True)
cobol_containers_EmptyModel = Class(name="cobol_containers_EmptyModel")
CobolRoot = Class(name="CobolRoot")
cobol_divisions_Division = Class(name="cobol_divisions_Division", is_abstract=True)
Section = Class(name="Section")
Paragraph = Class(name="Paragraph")
StatementContainer = Class(name="StatementContainer")
cobol_divisions_DataDivision = Class(name="cobol_divisions_DataDivision")
Division = Class(name="Division")
cobol_divisions_EnvironmentDivision = Class(name="cobol_divisions_EnvironmentDivision")
cobol_literals_AlphanumericLiteral = Class(name="cobol_literals_AlphanumericLiteral")
Literal = Class(name="Literal")
cobol_literals_IntegerLiteral = Class(name="cobol_literals_IntegerLiteral")
literals_NumericLiteral = Class(name="literals_NumericLiteral")
water_ObjectComputerParagraphWater = Class(name="water_ObjectComputerParagraphWater")
water_FileDescriptorWater = Class(name="water_FileDescriptorWater")
water_IOControlParagraphWater = Class(name="water_IOControlParagraphWater")
cobol_literals_DecimalLiteral = Class(name="cobol_literals_DecimalLiteral", is_abstract=True)
NumericLiteral = Class(name="NumericLiteral")
cobol_literals_FigurativeConstantLiteral = Class(name="cobol_literals_FigurativeConstantLiteral", is_abstract=True)
cobol_literals_BooleanLiteral = Class(name="cobol_literals_BooleanLiteral")
cobol_literals_FloatingDecimalLiteral = Class(name="cobol_literals_FloatingDecimalLiteral")
DecimalLiteral = Class(name="DecimalLiteral")
cobol_literals_AllLiteral = Class(name="cobol_literals_AllLiteral")
FigurativeConstantLiteral = Class(name="FigurativeConstantLiteral")
ConstantLiteral = Class(name="ConstantLiteral")
cobol_literals_NumericLiteral = Class(name="cobol_literals_NumericLiteral", is_abstract=True)
cobol_literals_ConstantLiteral = Class(name="cobol_literals_ConstantLiteral", is_abstract=True)
labels_StopLabel = Class(name="labels_StopLabel")
cobol_literals_Space = Class(name="cobol_literals_Space")
cobol_literals_Any = Class(name="cobol_literals_Any")
cobol_literals_Characters = Class(name="cobol_literals_Characters")
cobol_literals_PseudoLiteral = Class(name="cobol_literals_PseudoLiteral")
cobol_literals_DBCSLiteral = Class(name="cobol_literals_DBCSLiteral", is_abstract=True)
cobol_literals_NationalLiteral = Class(name="cobol_literals_NationalLiteral")
DBCSLiteral = Class(name="DBCSLiteral")
cobol_literals_FixedDecimalLiteral = Class(name="cobol_literals_FixedDecimalLiteral")
cobol_literals_NationalHexLiteral = Class(name="cobol_literals_NationalHexLiteral")
cobol_literals_Null = Class(name="cobol_literals_Null")
cobol_literals_Zero = Class(name="cobol_literals_Zero")
cobol_literals_Quote = Class(name="cobol_literals_Quote")
cobol_literals_LowValue = Class(name="cobol_literals_LowValue")
cobol_literals_HighValue = Class(name="cobol_literals_HighValue")
cobol_operators_GreaterThanOrEqual = Class(name="cobol_operators_GreaterThanOrEqual", is_abstract=True)
cobol_operators_GreaterThan = Class(name="cobol_operators_GreaterThan", is_abstract=True)
cobol_operators_LessThan = Class(name="cobol_operators_LessThan", is_abstract=True)
cobol_operators_LessThanOrEqual = Class(name="cobol_operators_LessThanOrEqual", is_abstract=True)
cobol_operators_Equal = Class(name="cobol_operators_Equal", is_abstract=True)
cobol_operators_Power = Class(name="cobol_operators_Power")
cobol_operators_Negate = Class(name="cobol_operators_Negate")
cobol_operators_Through = Class(name="cobol_operators_Through")
cobol_operators_ClassOperator = Class(name="cobol_operators_ClassOperator", is_abstract=True)
cobol_literals_AlphanumericHexaDecimalLiteral = Class(name="cobol_literals_AlphanumericHexaDecimalLiteral")
AlphanumericLiteral = Class(name="AlphanumericLiteral")
cobol_operators_Operator = Class(name="cobol_operators_Operator", is_abstract=True)
cobol_operators_AdditiveOperator = Class(name="cobol_operators_AdditiveOperator", is_abstract=True)
Operator = Class(name="Operator")
cobol_operators_MultiplicativeOperator = Class(name="cobol_operators_MultiplicativeOperator", is_abstract=True)
cobol_operators_UnaryOperator = Class(name="cobol_operators_UnaryOperator", is_abstract=True)
cobol_operators_LogicalOperator = Class(name="cobol_operators_LogicalOperator", is_abstract=True)
cobol_operators_RelationalOperator = Class(name="cobol_operators_RelationalOperator", is_abstract=True)
cobol_operators_ConditionOr = Class(name="cobol_operators_ConditionOr")
cobol_operators_ConditionAnd = Class(name="cobol_operators_ConditionAnd")
cobol_operators_Multiplication = Class(name="cobol_operators_Multiplication")
cobol_operators_SignOperator = Class(name="cobol_operators_SignOperator", is_abstract=True)
cobol_operators_Positive = Class(name="cobol_operators_Positive")
cobol_operators_Negative = Class(name="cobol_operators_Negative")
cobol_operators_Division = Class(name="cobol_operators_Division")
cobol_operators_Addition = Class(name="cobol_operators_Addition")
operators_AdditiveOperator = Class(name="operators_AdditiveOperator")
operators_UnaryOperator = Class(name="operators_UnaryOperator")
cobol_operators_Subtraction = Class(name="cobol_operators_Subtraction")
cobol_operators_GTSign = Class(name="cobol_operators_GTSign")
cobol_operators_GTEQPhrase = Class(name="cobol_operators_GTEQPhrase")
GreaterThanOrEqual = Class(name="GreaterThanOrEqual")
cobol_operators_GTEQSign = Class(name="cobol_operators_GTEQSign")
cobol_paragraphs_Paragraph = Class(name="cobol_paragraphs_Paragraph")
labels_Procedure = Class(name="labels_Procedure")
cobol_paragraphs_SourceComputerParagraph = Class(name="cobol_paragraphs_SourceComputerParagraph")
ConfigurationSectionParagraph = Class(name="ConfigurationSectionParagraph")
DebuggingMode = Class(name="DebuggingMode")
cobol_paragraphs_ObjectComputerParagraph = Class(name="cobol_paragraphs_ObjectComputerParagraph")
paragraphs_ConfigurationSectionParagraph = Class(name="paragraphs_ConfigurationSectionParagraph")
cobol_paragraphs_FileControlParagraph = Class(name="cobol_paragraphs_FileControlParagraph")
IOSectionParagraph = Class(name="IOSectionParagraph")
SelectStatement = Class(name="SelectStatement")
cobol_paragraphs_IOControlParagraph = Class(name="cobol_paragraphs_IOControlParagraph")
paragraphs_IOSectionParagraph = Class(name="paragraphs_IOSectionParagraph")
cobol_operators_Zero = Class(name="cobol_operators_Zero")
cobol_operators_ClassName = Class(name="cobol_operators_ClassName")
cobol_operators_Alphabetic = Class(name="cobol_operators_Alphabetic")
cobol_operators_DBCS = Class(name="cobol_operators_DBCS")
cobol_operators_Numeric = Class(name="cobol_operators_Numeric")
cobol_operators_AlphabeticUpper = Class(name="cobol_operators_AlphabeticUpper")
cobol_operators_AlphabeticLower = Class(name="cobol_operators_AlphabeticLower")
cobol_operators_Kanji = Class(name="cobol_operators_Kanji")
cobol_operators_EqualPhrase = Class(name="cobol_operators_EqualPhrase")
cobol_operators_EqualSign = Class(name="cobol_operators_EqualSign")
cobol_operators_LTPhrase = Class(name="cobol_operators_LTPhrase")
LessThan = Class(name="LessThan")
cobol_operators_LTSign = Class(name="cobol_operators_LTSign")
cobol_operators_LTEQPhrase = Class(name="cobol_operators_LTEQPhrase")
LessThanOrEqual = Class(name="LessThanOrEqual")
cobol_operators_LTEQSign = Class(name="cobol_operators_LTEQSign")
cobol_operators_GTPhrase = Class(name="cobol_operators_GTPhrase")
GreaterThan = Class(name="GreaterThan")
cobol_references_SpecialNamesConditionNameReference = Class(name="cobol_references_SpecialNamesConditionNameReference")
references_ElementReference = Class(name="references_ElementReference")
references_Qualifiable = Class(name="references_Qualifiable")
references_ConditionName = Class(name="references_ConditionName")
cobol_references_FileNameReference = Class(name="cobol_references_FileNameReference")
references_IdentifierReferenceQualifier = Class(name="references_IdentifierReferenceQualifier")
cobol_references_IndexNameReference = Class(name="cobol_references_IndexNameReference")
IdentifierReference = Class(name="IdentifierReference")
cobol_references_MnemonicNameReference = Class(name="cobol_references_MnemonicNameReference")
cobol_references_AlphabetNameReference = Class(name="cobol_references_AlphabetNameReference")
ElementReference = Class(name="ElementReference")
cobol_references_ConditionName = Class(name="cobol_references_ConditionName", is_abstract=True)
cobol_references_Qualifiable = Class(name="cobol_references_Qualifiable", is_abstract=True)
cobol_references_ConditionNameReference = Class(name="cobol_references_ConditionNameReference")
identifiers_IdentifierReference = Class(name="identifiers_IdentifierReference")
cobol_references_DataNameReference = Class(name="cobol_references_DataNameReference")
cobol_references_IdentifierReferenceQualifier = Class(name="cobol_references_IdentifierReferenceQualifier")
cobol_sections_Section = Class(name="cobol_sections_Section")
cobol_paragraphs_ConfigurationSectionParagraph = Class(name="cobol_paragraphs_ConfigurationSectionParagraph", is_abstract=True)
cobol_paragraphs_IOSectionParagraph = Class(name="cobol_paragraphs_IOSectionParagraph", is_abstract=True)
cobol_paragraphs_SpecialNamesParagraph = Class(name="cobol_paragraphs_SpecialNamesParagraph")
SpecialNameStatement = Class(name="SpecialNameStatement")
SpecialNamesParagraphWater = Class(name="SpecialNamesParagraphWater")
cobol_paragraphs_RepositoryParagraph = Class(name="cobol_paragraphs_RepositoryParagraph")
cobol_paragraphs_DebuggingMode = Class(name="cobol_paragraphs_DebuggingMode")
cobol_references_Reference = Class(name="cobol_references_Reference", is_abstract=True)
cobol_references_ReferenceableElement = Class(name="cobol_references_ReferenceableElement", is_abstract=True)
ReferenceableElement = Class(name="ReferenceableElement")
cobol_references_ElementReference = Class(name="cobol_references_ElementReference", is_abstract=True)
Reference = Class(name="Reference")
FileName = Class(name="FileName")
cobol_sections_DeclarativeSection = Class(name="cobol_sections_DeclarativeSection")
cobol_sentences_StatementContainer = Class(name="cobol_sentences_StatementContainer", is_abstract=True)
cobol_sentences_EmptySentence = Class(name="cobol_sentences_EmptySentence")
Sentence = Class(name="Sentence")
cobol_sentences_UseSentence = Class(name="cobol_sentences_UseSentence")
sentences_StatementContainer = Class(name="sentences_StatementContainer")
cobol_sentences_AlteredGoTo = Class(name="cobol_sentences_AlteredGoTo")
cobol_sentences_ExitProcedure = Class(name="cobol_sentences_ExitProcedure")
cobol_sentences_EntrySentence = Class(name="cobol_sentences_EntrySentence")
cobol_sentences_ExecuteSentence = Class(name="cobol_sentences_ExecuteSentence")
cobol_sentences_Sentence = Class(name="cobol_sentences_Sentence")
cobol_operands_PrimaryOperand = Class(name="cobol_operands_PrimaryOperand", is_abstract=True)
operands_ReplacementOperand = Class(name="operands_ReplacementOperand")
operands_Operand = Class(name="operands_Operand")
arithmetics_PrimaryExpression = Class(name="arithmetics_PrimaryExpression")
operands_ArithmeticOperand = Class(name="operands_ArithmeticOperand")
cobol_sections_WorkingStorageSection = Class(name="cobol_sections_WorkingStorageSection")
DataDivisionSection = Class(name="DataDivisionSection")
cobol_operands_RoundedIdentifier = Class(name="cobol_operands_RoundedIdentifier")
cobol_sections_LocalStorageSection = Class(name="cobol_sections_LocalStorageSection")
ArithmeticOperand = Class(name="ArithmeticOperand")
cobol_sections_LinkageStorageSection = Class(name="cobol_sections_LinkageStorageSection")
cobol_sections_IOSection = Class(name="cobol_sections_IOSection")
EnvironmentDivisionSection = Class(name="EnvironmentDivisionSection")
cobol_sections_ConfigurationSection = Class(name="cobol_sections_ConfigurationSection")
cobol_sections_EnvironmentDivisionSection = Class(name="cobol_sections_EnvironmentDivisionSection", is_abstract=True)
cobol_sections_DataDivisionSection = Class(name="cobol_sections_DataDivisionSection", is_abstract=True)
Statement = Class(name="Statement")
DataItem = Class(name="DataItem")
cobol_sections_FileSection = Class(name="cobol_sections_FileSection")
cobol_statements_ArithmeticStatement = Class(name="cobol_statements_ArithmeticStatement", is_abstract=True)
statements_Statement = Class(name="statements_Statement")
statements_ErrorHandled = Class(name="statements_ErrorHandled")
cobol_statements_Add = Class(name="cobol_statements_Add")
ArithmeticStatement = Class(name="ArithmeticStatement")
cobol_statements_Subtract = Class(name="cobol_statements_Subtract")
cobol_statements_Multiply = Class(name="cobol_statements_Multiply")
cobol_statements_Divide = Class(name="cobol_statements_Divide")
cobol_statements_Perform = Class(name="cobol_statements_Perform", is_abstract=True)
cobol_statements_PerformNestedStatement = Class(name="cobol_statements_PerformNestedStatement")
statements_Perform = Class(name="statements_Perform")
statements_NestedStatement = Class(name="statements_NestedStatement")
Identifier = Class(name="Identifier")
cobol_operands_ReplacementOperand = Class(name="cobol_operands_ReplacementOperand", is_abstract=True)
Operand = Class(name="Operand")
cobol_operands_Encoding = Class(name="cobol_operands_Encoding")
ReplacementOperand = Class(name="ReplacementOperand")
cobol_operands_Operand = Class(name="cobol_operands_Operand", is_abstract=True)
cobol_operands_ArithmeticOperand = Class(name="cobol_operands_ArithmeticOperand", is_abstract=True)
cobol_statements_Statement = Class(name="cobol_statements_Statement", is_abstract=True)
cobol_statements_Exit = Class(name="cobol_statements_Exit")
cobol_statements_Condition = Class(name="cobol_statements_Condition")
statements_Conditional = Class(name="statements_Conditional")
cobol_statements_Conditional = Class(name="cobol_statements_Conditional", is_abstract=True)
cobol_statements_Stop = Class(name="cobol_statements_Stop")
StopLabel = Class(name="StopLabel")
cobol_statements_Display = Class(name="cobol_statements_Display")
Environment = Class(name="Environment")
cobol_statements_Compute = Class(name="cobol_statements_Compute")
AssignmentExpression = Class(name="AssignmentExpression")
cobol_statements_Accept = Class(name="cobol_statements_Accept")
cobol_statements_PerformProcedure = Class(name="cobol_statements_PerformProcedure")
Perform = Class(name="Perform")
ProcedureRangeLabel = Class(name="ProcedureRangeLabel")
cobol_statements_Jump = Class(name="cobol_statements_Jump", is_abstract=True)
cobol_statements_NextSentence = Class(name="cobol_statements_NextSentence")
Jump = Class(name="Jump")
cobol_statements_GoTo = Class(name="cobol_statements_GoTo")
cobol_statements_GoBack = Class(name="cobol_statements_GoBack")
cobol_statements_NestedStatement = Class(name="cobol_statements_NestedStatement", is_abstract=True)
cobol_statements_Move = Class(name="cobol_statements_Move")
PrimaryOperand = Class(name="PrimaryOperand")
SwitchStatus = Class(name="SwitchStatus")
cobol_statements_SetIndexName = Class(name="cobol_statements_SetIndexName")
IndexNameReference = Class(name="IndexNameReference")
cobol_statements_String = Class(name="cobol_statements_String")
ConcatenatingStrings = Class(name="ConcatenatingStrings")
cobol_statements_Close = Class(name="cobol_statements_Close")
statements_IOStatement = Class(name="statements_IOStatement")
cobol_statements_Cancel = Class(name="cobol_statements_Cancel")
cobol_statements_Call = Class(name="cobol_statements_Call")
functions_Argumentable = Class(name="functions_Argumentable")
cobol_statements_Execute = Class(name="cobol_statements_Execute")
cobol_statements_ErrorHandled = Class(name="cobol_statements_ErrorHandled", is_abstract=True)
Handler = Class(name="Handler")
cobol_statements_Return = Class(name="cobol_statements_Return")
FileNameReference = Class(name="FileNameReference")
cobol_statements_SetStatement = Class(name="cobol_statements_SetStatement", is_abstract=True)
cobol_statements_SetSwitches = Class(name="cobol_statements_SetSwitches")
SetStatement = Class(name="SetStatement")
SplittedString = Class(name="SplittedString")
cobol_statements_Evaluate = Class(name="cobol_statements_Evaluate")
EvaluateCase = Class(name="EvaluateCase")
ExpressionList = Class(name="ExpressionList")
cobol_statements_NormalEvaluateCase = Class(name="cobol_statements_NormalEvaluateCase")
cobol_statements_OtherEvaluateCase = Class(name="cobol_statements_OtherEvaluateCase")
cobol_statements_EvaluateCase = Class(name="cobol_statements_EvaluateCase", is_abstract=True)
NestedStatement = Class(name="NestedStatement")
cobol_statements_Replace = Class(name="cobol_statements_Replace")
cobol_statements_Entry = Class(name="cobol_statements_Entry")
cobol_statements_Inspect = Class(name="cobol_statements_Inspect")
cobol_statements_Initialize = Class(name="cobol_statements_Initialize")
Replacement = Class(name="Replacement")
cobol_statements_Open = Class(name="cobol_statements_Open")
cobol_statements_SearchStatement = Class(name="cobol_statements_SearchStatement", is_abstract=True)
NormalEvaluateCase = Class(name="NormalEvaluateCase")
cobol_statements_SerialSearch = Class(name="cobol_statements_SerialSearch")
SearchStatement = Class(name="SearchStatement")
cobol_statements_BinarySearch = Class(name="cobol_statements_BinarySearch")
cobol_statements_Unstring = Class(name="cobol_statements_Unstring")
cobol_statements_Write = Class(name="cobol_statements_Write")
IntegerLiteral = Class(name="IntegerLiteral")
MnemonicNameReference = Class(name="MnemonicNameReference")
cobol_statements_Rewrite = Class(name="cobol_statements_Rewrite")
Write = Class(name="Write")
cobol_statements_SwitchStatus = Class(name="cobol_statements_SwitchStatus")
TallyingIn = Class(name="TallyingIn")
cobol_statements_Set = Class(name="cobol_statements_Set")
cobol_statements_Read = Class(name="cobol_statements_Read")
cobol_statements_PerformFixedTimes = Class(name="cobol_statements_PerformFixedTimes", is_abstract=True)
cobol_statements_PerformProcedureUntilCondition = Class(name="cobol_statements_PerformProcedureUntilCondition")
statements_PerformUntilCondition = Class(name="statements_PerformUntilCondition")
AfterUntilCondition = Class(name="AfterUntilCondition")
cobol_statements_PerformNestedStatementFixedTimes = Class(name="cobol_statements_PerformNestedStatementFixedTimes")
statements_PerformNestedStatement = Class(name="statements_PerformNestedStatement")
cobol_statements_PerformNestedStatementUntilCondition = Class(name="cobol_statements_PerformNestedStatementUntilCondition")
cobol_statements_Continue = Class(name="cobol_statements_Continue")
cobol_statements_FileIOStatement = Class(name="cobol_statements_FileIOStatement", is_abstract=True)
cobol_statements_PerformProcedureFixedTimes = Class(name="cobol_statements_PerformProcedureFixedTimes")
statements_PerformProcedure = Class(name="statements_PerformProcedure")
InputDirective = Class(name="InputDirective")
OutputDirective = Class(name="OutputDirective")
KeyDescriptor = Class(name="KeyDescriptor")
cobol_statements_Sort = Class(name="cobol_statements_Sort")
statements_FileIOStatement = Class(name="statements_FileIOStatement")
statements_PerformFixedTimes = Class(name="statements_PerformFixedTimes")
cobol_statements_Merge = Class(name="cobol_statements_Merge")
cobol_statements_Release = Class(name="cobol_statements_Release")
cobol_statements_PerformUntilCondition = Class(name="cobol_statements_PerformUntilCondition", is_abstract=True)
statements_VaryingUntilCondition = Class(name="statements_VaryingUntilCondition")
cobol_statements_KeyDescriptor = Class(name="cobol_statements_KeyDescriptor")
cobol_statements_IOStatement = Class(name="cobol_statements_IOStatement", is_abstract=True)
IOFileDescriptor = Class(name="IOFileDescriptor")
cobol_statements_IOFileDescriptor = Class(name="cobol_statements_IOFileDescriptor")
IOFile = Class(name="IOFile")
cobol_statements_IOFile = Class(name="cobol_statements_IOFile")
IncompleteElement = Class(name="IncompleteElement")
cobol_statements_TallyingIn = Class(name="cobol_statements_TallyingIn")
Tallying = Class(name="Tallying")
cobol_statements_VaryingUntilCondition = Class(name="cobol_statements_VaryingUntilCondition", is_abstract=True)
Conditional = Class(name="Conditional")
Qualifier = Class(name="Qualifier")
cobol_statements_AfterUntilCondition = Class(name="cobol_statements_AfterUntilCondition")
VaryingUntilCondition = Class(name="VaryingUntilCondition")
cobol_statements_Start = Class(name="cobol_statements_Start")
cobol_statements_Delete = Class(name="cobol_statements_Delete")
cobol_identifiers_Subscript = Class(name="cobol_identifiers_Subscript", is_abstract=True)
cobol_identifiers_Identifier = Class(name="cobol_identifiers_Identifier", is_abstract=True)
water_AcceptStatementWater = Class(name="water_AcceptStatementWater")
water_RepositoryParagraphWater = Class(name="water_RepositoryParagraphWater")
water_IdentificationDivisionWater = Class(name="water_IdentificationDivisionWater")
water_SQLStatementWater = Class(name="water_SQLStatementWater")
water_UseStatementWater = Class(name="water_UseStatementWater")
water_DataDescriptorWater = Class(name="water_DataDescriptorWater")
water_SortPhraseWater = Class(name="water_SortPhraseWater")
ReferenceModifier = Class(name="ReferenceModifier")
cobol_identifiers_IdentifierReference = Class(name="cobol_identifiers_IdentifierReference")
identifiers_Identifier = Class(name="identifiers_Identifier")
Subscript = Class(name="Subscript")
cobol_water_ProgramDescription = Class(name="cobol_water_ProgramDescription")
IdentificationDivisionWater = Class(name="IdentificationDivisionWater")
cobol_identifiers_All = Class(name="cobol_identifiers_All")
DirectSubscript = Class(name="DirectSubscript")
cobol_identifiers_ReferenceModifier = Class(name="cobol_identifiers_ReferenceModifier")
cobol_identifiers_LinageCounter = Class(name="cobol_identifiers_LinageCounter")
cobol_identifiers_Qualifier = Class(name="cobol_identifiers_Qualifier")
cobol_identifiers_RelativeSubscript = Class(name="cobol_identifiers_RelativeSubscript")
cobol_identifiers_DirectSubscript = Class(name="cobol_identifiers_DirectSubscript")
cobol_ios_InputProcedure = Class(name="cobol_ios_InputProcedure")
ios_InputDirective = Class(name="ios_InputDirective")
ios_ProcedureDirective = Class(name="ios_ProcedureDirective")
cobol_ios_InputDirective = Class(name="cobol_ios_InputDirective", is_abstract=True)
IODirectives = Class(name="IODirectives")
cobol_ios_InputFile = Class(name="cobol_ios_InputFile")
ios_FileDirective = Class(name="ios_FileDirective")
cobol_ios_OutputDirective = Class(name="cobol_ios_OutputDirective", is_abstract=True)
cobol_ios_OutputProcedure = Class(name="cobol_ios_OutputProcedure")
ios_OutputDirective = Class(name="ios_OutputDirective")
cobol_ios_OutputFile = Class(name="cobol_ios_OutputFile")
cobol_ios_IODirectives = Class(name="cobol_ios_IODirectives", is_abstract=True)
cobol_ios_FileDirective = Class(name="cobol_ios_FileDirective", is_abstract=True)
cobol_ios_ProcedureDirective = Class(name="cobol_ios_ProcedureDirective", is_abstract=True)
Label = Class(name="Label")
cobol_water_IncompleteElement = Class(name="cobol_water_IncompleteElement", is_abstract=True)
Water = Class(name="Water")
cobol_water_IdentificationDivisionWater = Class(name="cobol_water_IdentificationDivisionWater", is_abstract=True)
cobol_water_Water = Class(name="cobol_water_Water", is_abstract=True)
cobol_water_SpecialNamesParagraphWater = Class(name="cobol_water_SpecialNamesParagraphWater", is_abstract=True)
cobol_water_SpecialNamesClause = Class(name="cobol_water_SpecialNamesClause")
cobol_water_Dot = Class(name="cobol_water_Dot")
cobol_water_ObjectComputerParagraphWater = Class(name="cobol_water_ObjectComputerParagraphWater", is_abstract=True)
cobol_water_ObjectComputerDescription = Class(name="cobol_water_ObjectComputerDescription")
ObjectComputerParagraphWater = Class(name="ObjectComputerParagraphWater")
cobol_water_PriorityNumber = Class(name="cobol_water_PriorityNumber")
cobol_water_SelectStatementWater = Class(name="cobol_water_SelectStatementWater", is_abstract=True)
cobol_water_SelectStatementClause = Class(name="cobol_water_SelectStatementClause")
SelectStatementWater = Class(name="SelectStatementWater")
cobol_water_FileDescriptorWater = Class(name="cobol_water_FileDescriptorWater", is_abstract=True)
cobol_water_FileDescription = Class(name="cobol_water_FileDescription")
FileDescriptorWater = Class(name="FileDescriptorWater")
cobol_water_DataDescriptorWater = Class(name="cobol_water_DataDescriptorWater", is_abstract=True)
cobol_water_DataDescription = Class(name="cobol_water_DataDescription")
DataDescriptorWater = Class(name="DataDescriptorWater")
cobol_water_IOControlParagraphWater = Class(name="cobol_water_IOControlParagraphWater", is_abstract=True)
cobol_water_IOControlDescription = Class(name="cobol_water_IOControlDescription")
IOControlParagraphWater = Class(name="IOControlParagraphWater")
cobol_water_RepositoryParagraphWater = Class(name="cobol_water_RepositoryParagraphWater", is_abstract=True)
cobol_water_RepositoryDescription = Class(name="cobol_water_RepositoryDescription")
RepositoryParagraphWater = Class(name="RepositoryParagraphWater")
cobol_water_SQLStatementWater = Class(name="cobol_water_SQLStatementWater", is_abstract=True)
cobol_water_CICSStatementWater = Class(name="cobol_water_CICSStatementWater", is_abstract=True)
cobol_water_SQLStatementToken = Class(name="cobol_water_SQLStatementToken")
SQLStatementWater = Class(name="SQLStatementWater")
cobol_water_CICSStatementToken = Class(name="cobol_water_CICSStatementToken")
CICSStatementWater = Class(name="CICSStatementWater")
cobol_water_AcceptStatementWater = Class(name="cobol_water_AcceptStatementWater", is_abstract=True)
cobol_water_AcceptStatementToken = Class(name="cobol_water_AcceptStatementToken")
AcceptStatementWater = Class(name="AcceptStatementWater")
cobol_water_UseStatementWater = Class(name="cobol_water_UseStatementWater", is_abstract=True)
cobol_water_UseStatementToken = Class(name="cobol_water_UseStatementToken")
UseStatementWater = Class(name="UseStatementWater")
cobol_water_CloseStatementWater = Class(name="cobol_water_CloseStatementWater", is_abstract=True)
cobol_water_CloseStatementToken = Class(name="cobol_water_CloseStatementToken")
CloseStatementWater = Class(name="CloseStatementWater")
cobol_environments_UPSI = Class(name="cobol_environments_UPSI")
cobol_water_InvokeStatementWater = Class(name="cobol_water_InvokeStatementWater", is_abstract=True)
cobol_water_InvokeStatementToken = Class(name="cobol_water_InvokeStatementToken")
InvokeStatementWater = Class(name="InvokeStatementWater")
cobol_water_OpenStatementWater = Class(name="cobol_water_OpenStatementWater", is_abstract=True)
cobol_water_OpenStatementToken = Class(name="cobol_water_OpenStatementToken")
OpenStatementWater = Class(name="OpenStatementWater")
cobol_water_SortPhraseToken = Class(name="cobol_water_SortPhraseToken")
SortPhraseWater = Class(name="SortPhraseWater")
cobol_water_SortPhraseWater = Class(name="cobol_water_SortPhraseWater", is_abstract=True)
cobol_registers_Register = Class(name="cobol_registers_Register", is_abstract=True)
cobol_registers_ShiftIn = Class(name="cobol_registers_ShiftIn")
Register = Class(name="Register")
cobol_registers_ShiftOut = Class(name="cobol_registers_ShiftOut")
cobol_registers_AddressOf = Class(name="cobol_registers_AddressOf")
cobol_registers_LengthOf = Class(name="cobol_registers_LengthOf")
cobol_registers_ReturnCode = Class(name="cobol_registers_ReturnCode")
cobol_registers_WhenCompiled = Class(name="cobol_registers_WhenCompiled")
cobol_environments_SystemDevice = Class(name="cobol_environments_SystemDevice", is_abstract=True)
cobol_environments_SystemLogicalInput = Class(name="cobol_environments_SystemLogicalInput")
SystemDevice = Class(name="SystemDevice")
cobol_environments_SystemLogicalOutput = Class(name="cobol_environments_SystemLogicalOutput")
cobol_environments_SystemPunchDevice = Class(name="cobol_environments_SystemPunchDevice")
cobol_environments_Console = Class(name="cobol_environments_Console")
cobol_environments_Channel = Class(name="cobol_environments_Channel")
cobol_environments_AdvancedFunctionPrinting = Class(name="cobol_environments_AdvancedFunctionPrinting")
cobol_environments_SuppressSpacing = Class(name="cobol_environments_SuppressSpacing")
cobol_environments_Pocket = Class(name="cobol_environments_Pocket")
cobol_environments_Environment = Class(name="cobol_environments_Environment", is_abstract=True)
cobol_dataitems_PictureString = Class(name="cobol_dataitems_PictureString")
DataItemAttribute = Class(name="DataItemAttribute")
cobol_dataitems_RenamingDataName = Class(name="cobol_dataitems_RenamingDataName")
DataName = Class(name="DataName")
RangeExpression = Class(name="RangeExpression")
cobol_dataitems_ConditionName = Class(name="cobol_dataitems_ConditionName")
cobol_dataitems_Global = Class(name="cobol_dataitems_Global")
cobol_dataitems_External = Class(name="cobol_dataitems_External")
cobol_dataitems_Value = Class(name="cobol_dataitems_Value")
cobol_dataitems_DataItemAttribute = Class(name="cobol_dataitems_DataItemAttribute", is_abstract=True)
cobol_dataitems_Usage = Class(name="cobol_dataitems_Usage")
cobol_dataitems_GroupUsage = Class(name="cobol_dataitems_GroupUsage")
cobol_dataitems_DataItem = Class(name="cobol_dataitems_DataItem")
references_ReferenceableElement = Class(name="references_ReferenceableElement")
cobol_specialnames_ExplicitAlphabetType = Class(name="cobol_specialnames_ExplicitAlphabetType")
cobol_dataitems_RecordName = Class(name="cobol_dataitems_RecordName")
cobol_dataitems_DataName = Class(name="cobol_dataitems_DataName")
cobol_dataitems_Redefines = Class(name="cobol_dataitems_Redefines")
cobol_specialnames_SpecialName = Class(name="cobol_specialnames_SpecialName", is_abstract=True)
cobol_specialnames_ConditionName = Class(name="cobol_specialnames_ConditionName", is_abstract=True)
specialnames_SpecialName = Class(name="specialnames_SpecialName")
cobol_specialnames_OnStatus = Class(name="cobol_specialnames_OnStatus")
ConditionName = Class(name="ConditionName")
cobol_specialnames_OffStatus = Class(name="cobol_specialnames_OffStatus")
cobol_specialnames_AlphabetName = Class(name="cobol_specialnames_AlphabetName")
specialnames_SpecialNameStatement = Class(name="specialnames_SpecialNameStatement")
AlphabetType = Class(name="AlphabetType")
cobol_specialnames_UPSISwitchIs = Class(name="cobol_specialnames_UPSISwitchIs")
specialnames_MnemonicName = Class(name="specialnames_MnemonicName")
cobol_specialnames_AlphabetType = Class(name="cobol_specialnames_AlphabetType", is_abstract=True)
cobol_specialnames_PredefinedAlphabetType = Class(name="cobol_specialnames_PredefinedAlphabetType")
KeyName = Class(name="KeyName")
cobol_tables_KeyName = Class(name="cobol_tables_KeyName")
cobol_specialnames_CodeNameAlphabetType = Class(name="cobol_specialnames_CodeNameAlphabetType")
cobol_specialnames_CurrencySign = Class(name="cobol_specialnames_CurrencySign")
cobol_specialnames_ClassName = Class(name="cobol_specialnames_ClassName")
cobol_specialnames_MnemonicName = Class(name="cobol_specialnames_MnemonicName", is_abstract=True)
SpecialName = Class(name="SpecialName")
cobol_specialnames_SystemDeviceIs = Class(name="cobol_specialnames_SystemDeviceIs")
cobol_specialnames_SymbolicCharacter = Class(name="cobol_specialnames_SymbolicCharacter")
cobol_specialnames_SymbolicCharacterStatement = Class(name="cobol_specialnames_SymbolicCharacterStatement")
SymbolicCharacter = Class(name="SymbolicCharacter")
AlphabetNameReference = Class(name="AlphabetNameReference")
cobol_specialnames_SpecialNameStatement = Class(name="cobol_specialnames_SpecialNameStatement", is_abstract=True)
cobol_tables_Table = Class(name="cobol_tables_Table")
dataitems_DataItem = Class(name="dataitems_DataItem")
TableDimension = Class(name="TableDimension")
IndexName = Class(name="IndexName")
cobol_parameters_Parametrizable = Class(name="cobol_parameters_Parametrizable", is_abstract=True)
Parameter_ = Class(name="Parameter")
cobol_tables_IndexName = Class(name="cobol_tables_IndexName")
AdditionalIndexName = Class(name="AdditionalIndexName")
cobol_tables_TableDimension = Class(name="cobol_tables_TableDimension")
cobol_tables_AdditionalIndexName = Class(name="cobol_tables_AdditionalIndexName")
cobol_files_FileName = Class(name="cobol_files_FileName")
cobol_files_SelectStatement = Class(name="cobol_files_SelectStatement")
FileStatus = Class(name="FileStatus")
cobol_files_FileStatus = Class(name="cobol_files_FileStatus")
cobol_labels_ProcedureLabel = Class(name="cobol_labels_ProcedureLabel")
cobol_parameters_Parameter = Class(name="cobol_parameters_Parameter", is_abstract=True)
cobol_parameters_ByReferenceParameter = Class(name="cobol_parameters_ByReferenceParameter")
cobol_parameters_ByValueParameter = Class(name="cobol_parameters_ByValueParameter")
cobol_declaratives_Declaratives = Class(name="cobol_declaratives_Declaratives")
DeclarativeSection = Class(name="DeclarativeSection")
cobol_verbs_Is = Class(name="cobol_verbs_Is")
Verb = Class(name="Verb")
cobol_verbs_Verb = Class(name="cobol_verbs_Verb", is_abstract=True)
cobol_labels_ProcedureRange = Class(name="cobol_labels_ProcedureRange")
ProcedureRangeChild = Class(name="ProcedureRangeChild")
cobol_labels_ProcedureRangeLabel = Class(name="cobol_labels_ProcedureRangeLabel", is_abstract=True)
cobol_handlers_InvalidKey = Class(name="cobol_handlers_InvalidKey")
cobol_labels_ProcedureRangeChild = Class(name="cobol_labels_ProcedureRangeChild", is_abstract=True)
cobol_handlers_NotAtEndOfPage = Class(name="cobol_handlers_NotAtEndOfPage")
Procedure = Class(name="Procedure")
cobol_labels_Procedure = Class(name="cobol_labels_Procedure", is_abstract=True)
cobol_labels_Label = Class(name="cobol_labels_Label", is_abstract=True)
cobol_labels_StopLabel = Class(name="cobol_labels_StopLabel", is_abstract=True)
cobol_labels_Run = Class(name="cobol_labels_Run")
cobol_functions_FunctionCall = Class(name="cobol_functions_FunctionCall")
cobol_functions_Argument = Class(name="cobol_functions_Argument", is_abstract=True)
cobol_functions_ByReferenceArgument = Class(name="cobol_functions_ByReferenceArgument")
Argument = Class(name="Argument")
cobol_functions_ByValueArgument = Class(name="cobol_functions_ByValueArgument")
cobol_functions_ByContentArgument = Class(name="cobol_functions_ByContentArgument")
cobol_functions_OmittedArgument = Class(name="cobol_functions_OmittedArgument")
cobol_functions_Argumentable = Class(name="cobol_functions_Argumentable", is_abstract=True)
cobol_handlers_OnSizeError = Class(name="cobol_handlers_OnSizeError")
cobol_handlers_Handler = Class(name="cobol_handlers_Handler", is_abstract=True)
cobol_handlers_NotOnSizeError = Class(name="cobol_handlers_NotOnSizeError")
NotErrorHandler = Class(name="NotErrorHandler")
cobol_handlers_OnOverflow = Class(name="cobol_handlers_OnOverflow")
cobol_handlers_OnException = Class(name="cobol_handlers_OnException")
cobol_handlers_NotOnException = Class(name="cobol_handlers_NotOnException")
cobol_handlers_NotErrorHandler = Class(name="cobol_handlers_NotErrorHandler", is_abstract=True)
cobol_handlers_NotOnOverflow = Class(name="cobol_handlers_NotOnOverflow")
cobol_handlers_NotAtEnd = Class(name="cobol_handlers_NotAtEnd")
cobol_handlers_AtEnd = Class(name="cobol_handlers_AtEnd")
cobol_handlers_AtEndOfPage = Class(name="cobol_handlers_AtEndOfPage")
cobol_strings_ReplacementOccurrence = Class(name="cobol_strings_ReplacementOccurrence")
strings_Replacement = Class(name="strings_Replacement")
cobol_handlers_NotInvalidKey = Class(name="cobol_handlers_NotInvalidKey")
cobol_strings_Tallying = Class(name="cobol_strings_Tallying", is_abstract=True)
StringManipulation = Class(name="StringManipulation")
cobol_strings_StringManipulation = Class(name="cobol_strings_StringManipulation", is_abstract=True)
String = Class(name="String")
Location = Class(name="Location")
cobol_strings_ManipulatedStrings = Class(name="cobol_strings_ManipulatedStrings", is_abstract=True)
cobol_strings_String = Class(name="cobol_strings_String", is_abstract=True)
cobol_strings_ConcatenatingStrings = Class(name="cobol_strings_ConcatenatingStrings")
ManipulatedStrings = Class(name="ManipulatedStrings")
cobol_strings_SplittedString = Class(name="cobol_strings_SplittedString")
cobol_strings_Location = Class(name="cobol_strings_Location")
cobol_strings_Replacement = Class(name="cobol_strings_Replacement", is_abstract=True)
cobol_strings_Occurrence = Class(name="cobol_strings_Occurrence", is_abstract=True)
cobol_strings_TallyingOccurrence = Class(name="cobol_strings_TallyingOccurrence")
strings_Tallying = Class(name="strings_Tallying")
strings_Occurrence = Class(name="strings_Occurrence")
cobol_strings_AnyCharacter = Class(name="cobol_strings_AnyCharacter")
cobol_strings_SpecificCharacter = Class(name="cobol_strings_SpecificCharacter")
cobol_strings_AnyCharacterBySpecificCharacter = Class(name="cobol_strings_AnyCharacterBySpecificCharacter")
cobol_strings_SpecificCharacterBySpecificCharacter = Class(name="cobol_strings_SpecificCharacterBySpecificCharacter")

# cobol_commons_NamedElement class attributes and methods
cobol_commons_NamedElement_name: Property = Property(name="name", type=StringType)
cobol_commons_NamedElement.attributes={cobol_commons_NamedElement_name}

# Commentable class attributes and methods

# cobol_commons_Commentable class attributes and methods

# cobol_commons_LabellableElement class attributes and methods
cobol_commons_LabellableElement_label: Property = Property(name="label", type=StringType)
cobol_commons_LabellableElement.attributes={cobol_commons_LabellableElement_label}

# Negate class attributes and methods

# cobol_conditions_NegatedConditionalExpressionChild class attributes and methods

# cobol_conditions_SimpleConditionChild class attributes and methods

# cobol_conditions_RelationalExpression class attributes and methods

# SimpleConditionChild class attributes and methods

# RelationalOperator class attributes and methods

# Is class attributes and methods

# cobol_commons_URIableElement class attributes and methods
cobol_commons_URIableElement_uri: Property = Property(name="uri", type=StringType)
cobol_commons_URIableElement.attributes={cobol_commons_URIableElement_uri}

# cobol_conditions_Condition class attributes and methods

# cobol_conditions_ConditionalOrExpression class attributes and methods

# Condition class attributes and methods

# ConditionalOrExpressionChild class attributes and methods

# LogicalOperator class attributes and methods

# cobol_conditions_ConditionalOrExpressionChild class attributes and methods

# cobol_conditions_NegatedConditionalExpression class attributes and methods

# ConditionalAndExpressionChild class attributes and methods

# NegatedConditionalExpressionChild class attributes and methods

# cobol_conditions_NegatedAbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_AbbreviatedRelationalExpression class attributes and methods

# AbbreviatedRelationalExpressionChild class attributes and methods

# cobol_conditions_NestedAbbreviatedConditionalExpression class attributes and methods

# cobol_conditions_SignCondition class attributes and methods

# cobol_conditions_ExpressionList class attributes and methods

# cobol_conditions_ConditionalAndExpressionChild class attributes and methods

# cobol_conditions_ConditionalAndExpression class attributes and methods

# cobol_conditions_AbbreviatedConditionalExpression class attributes and methods

# AbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_AbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_NegatedAbbreviatedConditionalExpression class attributes and methods

# NegatedAbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_NestedCondition class attributes and methods

# cobol_arithmetics_AdditiveArithmeticExpression class attributes and methods

# RangeExpressionChild class attributes and methods

# AdditiveArithmeticExpressionChild class attributes and methods

# AdditiveOperator class attributes and methods

# cobol_arithmetics_AdditiveArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_MultiplicativeArithmeticExpression class attributes and methods

# MultiplicativeArithmeticExpressionChild class attributes and methods

# MultiplicativeOperator class attributes and methods

# cobol_arithmetics_MultiplicativeArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_PowerArithmeticExpression class attributes and methods

# SignOperator class attributes and methods

# cobol_conditions_ClassCondition class attributes and methods

# ClassOperator class attributes and methods

# cobol_conditions_AbbreviatedRelationalExpressionChild class attributes and methods

# Through class attributes and methods

# cobol_arithmetics_RangeExpressionChild class attributes and methods

# cobol_arithmetics_NestedArithmeticExpression class attributes and methods

# PrimaryExpression class attributes and methods

# cobol_arithmetics_ArithmeticExpression class attributes and methods

# conditions_AbbreviatedRelationalExpressionChild class attributes and methods

# conditions_SimpleConditionChild class attributes and methods

# cobol_containers_CompilationGroup class attributes and methods

# containers_CobolRoot class attributes and methods

# commons_NamedElement class attributes and methods

# CompilationUnit class attributes and methods

# cobol_containers_CompilationUnit class attributes and methods

# NamedElement class attributes and methods

# IdentificationDivision class attributes and methods

# PowerArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_PowerArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_UnaryArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_UnaryArithmeticExpression class attributes and methods

# UnaryArithmeticExpressionChild class attributes and methods

# UnaryOperator class attributes and methods

# cobol_arithmetics_PrimaryExpression class attributes and methods

# cobol_arithmetics_AssignmentExpression class attributes and methods

# Equal class attributes and methods

# ArithmeticExpression class attributes and methods

# cobol_arithmetics_RangeExpression class attributes and methods

# cobol_divisions_IdentificationDivision class attributes and methods
cobol_divisions_IdentificationDivision_properties: Property = Property(name="properties", type=StringType)
cobol_divisions_IdentificationDivision.attributes={cobol_divisions_IdentificationDivision_properties}

# divisions_Division class attributes and methods

# water_IncompleteElement class attributes and methods

# cobol_divisions_ProcedureDivision class attributes and methods

# parameters_Parametrizable class attributes and methods

# Declaratives class attributes and methods

# cobol_literals_Literal class attributes and methods

# water_SelectStatementWater class attributes and methods

# water_SpecialNamesParagraphWater class attributes and methods

# water_CICSStatementWater class attributes and methods

# operands_PrimaryOperand class attributes and methods

# water_InvokeStatementWater class attributes and methods

# EnvironmentDivision class attributes and methods

# DataDivision class attributes and methods

# ProcedureDivision class attributes and methods

# cobol_containers_CobolRoot class attributes and methods

# cobol_containers_EmptyModel class attributes and methods

# CobolRoot class attributes and methods

# cobol_divisions_Division class attributes and methods

# Section class attributes and methods

# Paragraph class attributes and methods

# StatementContainer class attributes and methods

# cobol_divisions_DataDivision class attributes and methods

# Division class attributes and methods

# cobol_divisions_EnvironmentDivision class attributes and methods

# cobol_literals_AlphanumericLiteral class attributes and methods
cobol_literals_AlphanumericLiteral_value: Property = Property(name="value", type=StringType)
cobol_literals_AlphanumericLiteral.attributes={cobol_literals_AlphanumericLiteral_value}

# Literal class attributes and methods

# cobol_literals_IntegerLiteral class attributes and methods
cobol_literals_IntegerLiteral_value: Property = Property(name="value", type=FloatType)
cobol_literals_IntegerLiteral.attributes={cobol_literals_IntegerLiteral_value}

# literals_NumericLiteral class attributes and methods

# water_ObjectComputerParagraphWater class attributes and methods

# water_FileDescriptorWater class attributes and methods

# water_IOControlParagraphWater class attributes and methods

# cobol_literals_DecimalLiteral class attributes and methods
cobol_literals_DecimalLiteral_value: Property = Property(name="value", type=StringType)
cobol_literals_DecimalLiteral.attributes={cobol_literals_DecimalLiteral_value}

# NumericLiteral class attributes and methods

# cobol_literals_FigurativeConstantLiteral class attributes and methods

# cobol_literals_BooleanLiteral class attributes and methods
cobol_literals_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
cobol_literals_BooleanLiteral.attributes={cobol_literals_BooleanLiteral_value}

# cobol_literals_FloatingDecimalLiteral class attributes and methods

# DecimalLiteral class attributes and methods

# cobol_literals_AllLiteral class attributes and methods

# FigurativeConstantLiteral class attributes and methods

# ConstantLiteral class attributes and methods

# cobol_literals_NumericLiteral class attributes and methods

# cobol_literals_ConstantLiteral class attributes and methods

# labels_StopLabel class attributes and methods

# cobol_literals_Space class attributes and methods
cobol_literals_Space_value: Property = Property(name="value", type=StringType)
cobol_literals_Space.attributes={cobol_literals_Space_value}

# cobol_literals_Any class attributes and methods

# cobol_literals_Characters class attributes and methods

# cobol_literals_PseudoLiteral class attributes and methods
cobol_literals_PseudoLiteral_value: Property = Property(name="value", type=StringType)
cobol_literals_PseudoLiteral.attributes={cobol_literals_PseudoLiteral_value}

# cobol_literals_DBCSLiteral class attributes and methods

# cobol_literals_NationalLiteral class attributes and methods
cobol_literals_NationalLiteral_value: Property = Property(name="value", type=StringType)
cobol_literals_NationalLiteral.attributes={cobol_literals_NationalLiteral_value}

# DBCSLiteral class attributes and methods

# cobol_literals_FixedDecimalLiteral class attributes and methods

# cobol_literals_NationalHexLiteral class attributes and methods
cobol_literals_NationalHexLiteral_value: Property = Property(name="value", type=FloatType)
cobol_literals_NationalHexLiteral.attributes={cobol_literals_NationalHexLiteral_value}

# cobol_literals_Null class attributes and methods
cobol_literals_Null_value: Property = Property(name="value", type=StringType)
cobol_literals_Null.attributes={cobol_literals_Null_value}

# cobol_literals_Zero class attributes and methods
cobol_literals_Zero_value: Property = Property(name="value", type=StringType)
cobol_literals_Zero.attributes={cobol_literals_Zero_value}

# cobol_literals_Quote class attributes and methods
cobol_literals_Quote_value: Property = Property(name="value", type=StringType)
cobol_literals_Quote.attributes={cobol_literals_Quote_value}

# cobol_literals_LowValue class attributes and methods
cobol_literals_LowValue_value: Property = Property(name="value", type=StringType)
cobol_literals_LowValue.attributes={cobol_literals_LowValue_value}

# cobol_literals_HighValue class attributes and methods
cobol_literals_HighValue_value: Property = Property(name="value", type=StringType)
cobol_literals_HighValue.attributes={cobol_literals_HighValue_value}

# cobol_operators_GreaterThanOrEqual class attributes and methods
cobol_operators_GreaterThanOrEqual_than: Property = Property(name="than", type=BooleanType)
cobol_operators_GreaterThanOrEqual_to: Property = Property(name="to", type=BooleanType)
cobol_operators_GreaterThanOrEqual.attributes={cobol_operators_GreaterThanOrEqual_to, cobol_operators_GreaterThanOrEqual_than}

# cobol_operators_GreaterThan class attributes and methods
cobol_operators_GreaterThan_than: Property = Property(name="than", type=BooleanType)
cobol_operators_GreaterThan.attributes={cobol_operators_GreaterThan_than}

# cobol_operators_LessThan class attributes and methods
cobol_operators_LessThan_than: Property = Property(name="than", type=BooleanType)
cobol_operators_LessThan.attributes={cobol_operators_LessThan_than}

# cobol_operators_LessThanOrEqual class attributes and methods
cobol_operators_LessThanOrEqual_than: Property = Property(name="than", type=BooleanType)
cobol_operators_LessThanOrEqual_to: Property = Property(name="to", type=BooleanType)
cobol_operators_LessThanOrEqual.attributes={cobol_operators_LessThanOrEqual_to, cobol_operators_LessThanOrEqual_than}

# cobol_operators_Equal class attributes and methods
cobol_operators_Equal_to: Property = Property(name="to", type=BooleanType)
cobol_operators_Equal.attributes={cobol_operators_Equal_to}

# cobol_operators_Power class attributes and methods

# cobol_operators_Negate class attributes and methods

# cobol_operators_Through class attributes and methods
cobol_operators_Through_value: Property = Property(name="value", type=StringType)
cobol_operators_Through.attributes={cobol_operators_Through_value}

# cobol_operators_ClassOperator class attributes and methods

# cobol_literals_AlphanumericHexaDecimalLiteral class attributes and methods

# AlphanumericLiteral class attributes and methods

# cobol_operators_Operator class attributes and methods

# cobol_operators_AdditiveOperator class attributes and methods

# Operator class attributes and methods

# cobol_operators_MultiplicativeOperator class attributes and methods

# cobol_operators_UnaryOperator class attributes and methods

# cobol_operators_LogicalOperator class attributes and methods

# cobol_operators_RelationalOperator class attributes and methods

# cobol_operators_ConditionOr class attributes and methods

# cobol_operators_ConditionAnd class attributes and methods

# cobol_operators_Multiplication class attributes and methods

# cobol_operators_SignOperator class attributes and methods

# cobol_operators_Positive class attributes and methods

# cobol_operators_Negative class attributes and methods

# cobol_operators_Division class attributes and methods

# cobol_operators_Addition class attributes and methods

# operators_AdditiveOperator class attributes and methods

# operators_UnaryOperator class attributes and methods

# cobol_operators_Subtraction class attributes and methods

# cobol_operators_GTSign class attributes and methods

# cobol_operators_GTEQPhrase class attributes and methods

# GreaterThanOrEqual class attributes and methods

# cobol_operators_GTEQSign class attributes and methods

# cobol_paragraphs_Paragraph class attributes and methods

# labels_Procedure class attributes and methods

# cobol_paragraphs_SourceComputerParagraph class attributes and methods

# ConfigurationSectionParagraph class attributes and methods

# DebuggingMode class attributes and methods

# cobol_paragraphs_ObjectComputerParagraph class attributes and methods

# paragraphs_ConfigurationSectionParagraph class attributes and methods

# cobol_paragraphs_FileControlParagraph class attributes and methods

# IOSectionParagraph class attributes and methods

# SelectStatement class attributes and methods

# cobol_paragraphs_IOControlParagraph class attributes and methods

# paragraphs_IOSectionParagraph class attributes and methods

# cobol_operators_Zero class attributes and methods

# cobol_operators_ClassName class attributes and methods

# cobol_operators_Alphabetic class attributes and methods

# cobol_operators_DBCS class attributes and methods

# cobol_operators_Numeric class attributes and methods

# cobol_operators_AlphabeticUpper class attributes and methods

# cobol_operators_AlphabeticLower class attributes and methods

# cobol_operators_Kanji class attributes and methods

# cobol_operators_EqualPhrase class attributes and methods

# cobol_operators_EqualSign class attributes and methods

# cobol_operators_LTPhrase class attributes and methods

# LessThan class attributes and methods

# cobol_operators_LTSign class attributes and methods

# cobol_operators_LTEQPhrase class attributes and methods

# LessThanOrEqual class attributes and methods

# cobol_operators_LTEQSign class attributes and methods

# cobol_operators_GTPhrase class attributes and methods

# GreaterThan class attributes and methods

# cobol_references_SpecialNamesConditionNameReference class attributes and methods

# references_ElementReference class attributes and methods

# references_Qualifiable class attributes and methods

# references_ConditionName class attributes and methods

# cobol_references_FileNameReference class attributes and methods

# references_IdentifierReferenceQualifier class attributes and methods

# cobol_references_IndexNameReference class attributes and methods

# IdentifierReference class attributes and methods

# cobol_references_MnemonicNameReference class attributes and methods

# cobol_references_AlphabetNameReference class attributes and methods

# ElementReference class attributes and methods

# cobol_references_ConditionName class attributes and methods

# cobol_references_Qualifiable class attributes and methods

# cobol_references_ConditionNameReference class attributes and methods

# identifiers_IdentifierReference class attributes and methods

# cobol_references_DataNameReference class attributes and methods

# cobol_references_IdentifierReferenceQualifier class attributes and methods

# cobol_sections_Section class attributes and methods
cobol_sections_Section_segmentNumber: Property = Property(name="segmentNumber", type=StringType)
cobol_sections_Section.attributes={cobol_sections_Section_segmentNumber}

# cobol_paragraphs_ConfigurationSectionParagraph class attributes and methods

# cobol_paragraphs_IOSectionParagraph class attributes and methods

# cobol_paragraphs_SpecialNamesParagraph class attributes and methods

# SpecialNameStatement class attributes and methods

# SpecialNamesParagraphWater class attributes and methods

# cobol_paragraphs_RepositoryParagraph class attributes and methods

# cobol_paragraphs_DebuggingMode class attributes and methods

# cobol_references_Reference class attributes and methods

# cobol_references_ReferenceableElement class attributes and methods

# ReferenceableElement class attributes and methods

# cobol_references_ElementReference class attributes and methods

# Reference class attributes and methods

# FileName class attributes and methods

# cobol_sections_DeclarativeSection class attributes and methods

# cobol_sentences_StatementContainer class attributes and methods

# cobol_sentences_EmptySentence class attributes and methods

# Sentence class attributes and methods

# cobol_sentences_UseSentence class attributes and methods

# sentences_StatementContainer class attributes and methods

# cobol_sentences_AlteredGoTo class attributes and methods

# cobol_sentences_ExitProcedure class attributes and methods

# cobol_sentences_EntrySentence class attributes and methods

# cobol_sentences_ExecuteSentence class attributes and methods

# cobol_sentences_Sentence class attributes and methods

# cobol_operands_PrimaryOperand class attributes and methods

# operands_ReplacementOperand class attributes and methods

# operands_Operand class attributes and methods

# arithmetics_PrimaryExpression class attributes and methods

# operands_ArithmeticOperand class attributes and methods

# cobol_sections_WorkingStorageSection class attributes and methods

# DataDivisionSection class attributes and methods

# cobol_operands_RoundedIdentifier class attributes and methods

# cobol_sections_LocalStorageSection class attributes and methods

# ArithmeticOperand class attributes and methods

# cobol_sections_LinkageStorageSection class attributes and methods

# cobol_sections_IOSection class attributes and methods

# EnvironmentDivisionSection class attributes and methods

# cobol_sections_ConfigurationSection class attributes and methods

# cobol_sections_EnvironmentDivisionSection class attributes and methods

# cobol_sections_DataDivisionSection class attributes and methods

# Statement class attributes and methods

# DataItem class attributes and methods

# cobol_sections_FileSection class attributes and methods

# cobol_statements_ArithmeticStatement class attributes and methods
cobol_statements_ArithmeticStatement_corresponding: Property = Property(name="corresponding", type=StringType)
cobol_statements_ArithmeticStatement.attributes={cobol_statements_ArithmeticStatement_corresponding}

# statements_Statement class attributes and methods

# statements_ErrorHandled class attributes and methods

# cobol_statements_Add class attributes and methods

# ArithmeticStatement class attributes and methods

# cobol_statements_Subtract class attributes and methods

# cobol_statements_Multiply class attributes and methods

# cobol_statements_Divide class attributes and methods

# cobol_statements_Perform class attributes and methods

# cobol_statements_PerformNestedStatement class attributes and methods

# statements_Perform class attributes and methods

# statements_NestedStatement class attributes and methods

# Identifier class attributes and methods

# cobol_operands_ReplacementOperand class attributes and methods

# Operand class attributes and methods

# cobol_operands_Encoding class attributes and methods
cobol_operands_Encoding_type: Property = Property(name="type", type=StringType)
cobol_operands_Encoding.attributes={cobol_operands_Encoding_type}

# ReplacementOperand class attributes and methods

# cobol_operands_Operand class attributes and methods

# cobol_operands_ArithmeticOperand class attributes and methods

# cobol_statements_Statement class attributes and methods
cobol_statements_Statement_endVerb: Property = Property(name="endVerb", type=BooleanType)
cobol_statements_Statement.attributes={cobol_statements_Statement_endVerb}

# cobol_statements_Exit class attributes and methods
cobol_statements_Exit_exitLabel: Property = Property(name="exitLabel", type=StringType)
cobol_statements_Exit.attributes={cobol_statements_Exit_exitLabel}

# cobol_statements_Condition class attributes and methods

# statements_Conditional class attributes and methods

# cobol_statements_Conditional class attributes and methods

# cobol_statements_Stop class attributes and methods

# StopLabel class attributes and methods

# cobol_statements_Display class attributes and methods

# Environment class attributes and methods

# cobol_statements_Compute class attributes and methods

# AssignmentExpression class attributes and methods

# cobol_statements_Accept class attributes and methods

# cobol_statements_PerformProcedure class attributes and methods

# Perform class attributes and methods

# ProcedureRangeLabel class attributes and methods

# cobol_statements_Jump class attributes and methods

# cobol_statements_NextSentence class attributes and methods

# Jump class attributes and methods

# cobol_statements_GoTo class attributes and methods

# cobol_statements_GoBack class attributes and methods

# cobol_statements_NestedStatement class attributes and methods

# cobol_statements_Move class attributes and methods
cobol_statements_Move_corresponding: Property = Property(name="corresponding", type=StringType)
cobol_statements_Move.attributes={cobol_statements_Move_corresponding}

# PrimaryOperand class attributes and methods

# SwitchStatus class attributes and methods

# cobol_statements_SetIndexName class attributes and methods
cobol_statements_SetIndexName_adjust: Property = Property(name="adjust", type=StringType)
cobol_statements_SetIndexName.attributes={cobol_statements_SetIndexName_adjust}

# IndexNameReference class attributes and methods

# cobol_statements_String class attributes and methods

# ConcatenatingStrings class attributes and methods

# cobol_statements_Close class attributes and methods

# statements_IOStatement class attributes and methods

# cobol_statements_Cancel class attributes and methods

# cobol_statements_Call class attributes and methods

# functions_Argumentable class attributes and methods

# cobol_statements_Execute class attributes and methods
cobol_statements_Execute_water: Property = Property(name="water", type=StringType)
cobol_statements_Execute.attributes={cobol_statements_Execute_water}

# cobol_statements_ErrorHandled class attributes and methods

# Handler class attributes and methods

# cobol_statements_Return class attributes and methods

# FileNameReference class attributes and methods

# cobol_statements_SetStatement class attributes and methods

# cobol_statements_SetSwitches class attributes and methods

# SetStatement class attributes and methods

# SplittedString class attributes and methods

# cobol_statements_Evaluate class attributes and methods

# EvaluateCase class attributes and methods

# ExpressionList class attributes and methods

# cobol_statements_NormalEvaluateCase class attributes and methods

# cobol_statements_OtherEvaluateCase class attributes and methods

# cobol_statements_EvaluateCase class attributes and methods

# NestedStatement class attributes and methods

# cobol_statements_Replace class attributes and methods
cobol_statements_Replace_replaceSwitch: Property = Property(name="replaceSwitch", type=BooleanType)
cobol_statements_Replace.attributes={cobol_statements_Replace_replaceSwitch}

# cobol_statements_Entry class attributes and methods

# cobol_statements_Inspect class attributes and methods

# cobol_statements_Initialize class attributes and methods

# Replacement class attributes and methods

# cobol_statements_Open class attributes and methods

# cobol_statements_SearchStatement class attributes and methods

# NormalEvaluateCase class attributes and methods

# cobol_statements_SerialSearch class attributes and methods

# SearchStatement class attributes and methods

# cobol_statements_BinarySearch class attributes and methods

# cobol_statements_Unstring class attributes and methods

# cobol_statements_Write class attributes and methods

# IntegerLiteral class attributes and methods

# MnemonicNameReference class attributes and methods

# cobol_statements_Rewrite class attributes and methods

# Write class attributes and methods

# cobol_statements_SwitchStatus class attributes and methods
cobol_statements_SwitchStatus_status: Property = Property(name="status", type=StringType)
cobol_statements_SwitchStatus.attributes={cobol_statements_SwitchStatus_status}

# TallyingIn class attributes and methods

# cobol_statements_Set class attributes and methods

# cobol_statements_Read class attributes and methods

# cobol_statements_PerformFixedTimes class attributes and methods

# cobol_statements_PerformProcedureUntilCondition class attributes and methods

# statements_PerformUntilCondition class attributes and methods

# AfterUntilCondition class attributes and methods

# cobol_statements_PerformNestedStatementFixedTimes class attributes and methods

# statements_PerformNestedStatement class attributes and methods

# cobol_statements_PerformNestedStatementUntilCondition class attributes and methods

# cobol_statements_Continue class attributes and methods

# cobol_statements_FileIOStatement class attributes and methods

# cobol_statements_PerformProcedureFixedTimes class attributes and methods

# statements_PerformProcedure class attributes and methods

# InputDirective class attributes and methods

# OutputDirective class attributes and methods

# KeyDescriptor class attributes and methods

# cobol_statements_Sort class attributes and methods

# statements_FileIOStatement class attributes and methods

# statements_PerformFixedTimes class attributes and methods

# cobol_statements_Merge class attributes and methods

# cobol_statements_Release class attributes and methods

# cobol_statements_PerformUntilCondition class attributes and methods
cobol_statements_PerformUntilCondition_position: Property = Property(name="position", type=StringType)
cobol_statements_PerformUntilCondition.attributes={cobol_statements_PerformUntilCondition_position}

# statements_VaryingUntilCondition class attributes and methods

# cobol_statements_KeyDescriptor class attributes and methods
cobol_statements_KeyDescriptor_order: Property = Property(name="order", type=StringType)
cobol_statements_KeyDescriptor.attributes={cobol_statements_KeyDescriptor_order}

# cobol_statements_IOStatement class attributes and methods

# IOFileDescriptor class attributes and methods

# cobol_statements_IOFileDescriptor class attributes and methods
cobol_statements_IOFileDescriptor_type: Property = Property(name="type", type=StringType)
cobol_statements_IOFileDescriptor.attributes={cobol_statements_IOFileDescriptor_type}

# IOFile class attributes and methods

# cobol_statements_IOFile class attributes and methods

# IncompleteElement class attributes and methods

# cobol_statements_TallyingIn class attributes and methods

# Tallying class attributes and methods

# cobol_statements_VaryingUntilCondition class attributes and methods

# Conditional class attributes and methods

# Qualifier class attributes and methods

# cobol_statements_AfterUntilCondition class attributes and methods

# VaryingUntilCondition class attributes and methods

# cobol_statements_Start class attributes and methods

# cobol_statements_Delete class attributes and methods

# cobol_identifiers_Subscript class attributes and methods

# cobol_identifiers_Identifier class attributes and methods

# water_AcceptStatementWater class attributes and methods

# water_RepositoryParagraphWater class attributes and methods

# water_IdentificationDivisionWater class attributes and methods

# water_SQLStatementWater class attributes and methods

# water_UseStatementWater class attributes and methods

# water_DataDescriptorWater class attributes and methods

# water_SortPhraseWater class attributes and methods

# ReferenceModifier class attributes and methods

# cobol_identifiers_IdentifierReference class attributes and methods

# identifiers_Identifier class attributes and methods

# Subscript class attributes and methods

# cobol_water_ProgramDescription class attributes and methods
cobol_water_ProgramDescription_value: Property = Property(name="value", type=StringType)
cobol_water_ProgramDescription.attributes={cobol_water_ProgramDescription_value}

# IdentificationDivisionWater class attributes and methods

# cobol_identifiers_All class attributes and methods

# DirectSubscript class attributes and methods

# cobol_identifiers_ReferenceModifier class attributes and methods

# cobol_identifiers_LinageCounter class attributes and methods

# cobol_identifiers_Qualifier class attributes and methods

# cobol_identifiers_RelativeSubscript class attributes and methods

# cobol_identifiers_DirectSubscript class attributes and methods

# cobol_ios_InputProcedure class attributes and methods

# ios_InputDirective class attributes and methods

# ios_ProcedureDirective class attributes and methods

# cobol_ios_InputDirective class attributes and methods

# IODirectives class attributes and methods

# cobol_ios_InputFile class attributes and methods

# ios_FileDirective class attributes and methods

# cobol_ios_OutputDirective class attributes and methods

# cobol_ios_OutputProcedure class attributes and methods

# ios_OutputDirective class attributes and methods

# cobol_ios_OutputFile class attributes and methods

# cobol_ios_IODirectives class attributes and methods

# cobol_ios_FileDirective class attributes and methods

# cobol_ios_ProcedureDirective class attributes and methods

# Label class attributes and methods

# cobol_water_IncompleteElement class attributes and methods

# Water class attributes and methods

# cobol_water_IdentificationDivisionWater class attributes and methods

# cobol_water_Water class attributes and methods

# cobol_water_SpecialNamesParagraphWater class attributes and methods

# cobol_water_SpecialNamesClause class attributes and methods
cobol_water_SpecialNamesClause_value: Property = Property(name="value", type=StringType)
cobol_water_SpecialNamesClause.attributes={cobol_water_SpecialNamesClause_value}

# cobol_water_Dot class attributes and methods

# cobol_water_ObjectComputerParagraphWater class attributes and methods

# cobol_water_ObjectComputerDescription class attributes and methods
cobol_water_ObjectComputerDescription_value: Property = Property(name="value", type=StringType)
cobol_water_ObjectComputerDescription.attributes={cobol_water_ObjectComputerDescription_value}

# ObjectComputerParagraphWater class attributes and methods

# cobol_water_PriorityNumber class attributes and methods
cobol_water_PriorityNumber_value: Property = Property(name="value", type=StringType)
cobol_water_PriorityNumber.attributes={cobol_water_PriorityNumber_value}

# cobol_water_SelectStatementWater class attributes and methods

# cobol_water_SelectStatementClause class attributes and methods
cobol_water_SelectStatementClause_value: Property = Property(name="value", type=StringType)
cobol_water_SelectStatementClause.attributes={cobol_water_SelectStatementClause_value}

# SelectStatementWater class attributes and methods

# cobol_water_FileDescriptorWater class attributes and methods

# cobol_water_FileDescription class attributes and methods
cobol_water_FileDescription_value: Property = Property(name="value", type=StringType)
cobol_water_FileDescription.attributes={cobol_water_FileDescription_value}

# FileDescriptorWater class attributes and methods

# cobol_water_DataDescriptorWater class attributes and methods

# cobol_water_DataDescription class attributes and methods
cobol_water_DataDescription_value: Property = Property(name="value", type=StringType)
cobol_water_DataDescription.attributes={cobol_water_DataDescription_value}

# DataDescriptorWater class attributes and methods

# cobol_water_IOControlParagraphWater class attributes and methods

# cobol_water_IOControlDescription class attributes and methods
cobol_water_IOControlDescription_value: Property = Property(name="value", type=StringType)
cobol_water_IOControlDescription.attributes={cobol_water_IOControlDescription_value}

# IOControlParagraphWater class attributes and methods

# cobol_water_RepositoryParagraphWater class attributes and methods

# cobol_water_RepositoryDescription class attributes and methods
cobol_water_RepositoryDescription_value: Property = Property(name="value", type=StringType)
cobol_water_RepositoryDescription.attributes={cobol_water_RepositoryDescription_value}

# RepositoryParagraphWater class attributes and methods

# cobol_water_SQLStatementWater class attributes and methods

# cobol_water_CICSStatementWater class attributes and methods

# cobol_water_SQLStatementToken class attributes and methods
cobol_water_SQLStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_SQLStatementToken.attributes={cobol_water_SQLStatementToken_value}

# SQLStatementWater class attributes and methods

# cobol_water_CICSStatementToken class attributes and methods
cobol_water_CICSStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_CICSStatementToken.attributes={cobol_water_CICSStatementToken_value}

# CICSStatementWater class attributes and methods

# cobol_water_AcceptStatementWater class attributes and methods

# cobol_water_AcceptStatementToken class attributes and methods
cobol_water_AcceptStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_AcceptStatementToken.attributes={cobol_water_AcceptStatementToken_value}

# AcceptStatementWater class attributes and methods

# cobol_water_UseStatementWater class attributes and methods

# cobol_water_UseStatementToken class attributes and methods
cobol_water_UseStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_UseStatementToken.attributes={cobol_water_UseStatementToken_value}

# UseStatementWater class attributes and methods

# cobol_water_CloseStatementWater class attributes and methods

# cobol_water_CloseStatementToken class attributes and methods
cobol_water_CloseStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_CloseStatementToken.attributes={cobol_water_CloseStatementToken_value}

# CloseStatementWater class attributes and methods

# cobol_environments_UPSI class attributes and methods
cobol_environments_UPSI_value: Property = Property(name="value", type=StringType)
cobol_environments_UPSI.attributes={cobol_environments_UPSI_value}

# cobol_water_InvokeStatementWater class attributes and methods

# cobol_water_InvokeStatementToken class attributes and methods
cobol_water_InvokeStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_InvokeStatementToken.attributes={cobol_water_InvokeStatementToken_value}

# InvokeStatementWater class attributes and methods

# cobol_water_OpenStatementWater class attributes and methods

# cobol_water_OpenStatementToken class attributes and methods
cobol_water_OpenStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_OpenStatementToken.attributes={cobol_water_OpenStatementToken_value}

# OpenStatementWater class attributes and methods

# cobol_water_SortPhraseToken class attributes and methods
cobol_water_SortPhraseToken_value: Property = Property(name="value", type=StringType)
cobol_water_SortPhraseToken.attributes={cobol_water_SortPhraseToken_value}

# SortPhraseWater class attributes and methods

# cobol_water_SortPhraseWater class attributes and methods

# cobol_registers_Register class attributes and methods

# cobol_registers_ShiftIn class attributes and methods

# Register class attributes and methods

# cobol_registers_ShiftOut class attributes and methods

# cobol_registers_AddressOf class attributes and methods

# cobol_registers_LengthOf class attributes and methods

# cobol_registers_ReturnCode class attributes and methods

# cobol_registers_WhenCompiled class attributes and methods

# cobol_environments_SystemDevice class attributes and methods

# cobol_environments_SystemLogicalInput class attributes and methods
cobol_environments_SystemLogicalInput_value: Property = Property(name="value", type=StringType)
cobol_environments_SystemLogicalInput.attributes={cobol_environments_SystemLogicalInput_value}

# SystemDevice class attributes and methods

# cobol_environments_SystemLogicalOutput class attributes and methods
cobol_environments_SystemLogicalOutput_value: Property = Property(name="value", type=StringType)
cobol_environments_SystemLogicalOutput.attributes={cobol_environments_SystemLogicalOutput_value}

# cobol_environments_SystemPunchDevice class attributes and methods
cobol_environments_SystemPunchDevice_value: Property = Property(name="value", type=StringType)
cobol_environments_SystemPunchDevice.attributes={cobol_environments_SystemPunchDevice_value}

# cobol_environments_Console class attributes and methods

# cobol_environments_Channel class attributes and methods
cobol_environments_Channel_value: Property = Property(name="value", type=StringType)
cobol_environments_Channel.attributes={cobol_environments_Channel_value}

# cobol_environments_AdvancedFunctionPrinting class attributes and methods

# cobol_environments_SuppressSpacing class attributes and methods

# cobol_environments_Pocket class attributes and methods
cobol_environments_Pocket_value: Property = Property(name="value", type=StringType)
cobol_environments_Pocket.attributes={cobol_environments_Pocket_value}

# cobol_environments_Environment class attributes and methods

# cobol_dataitems_PictureString class attributes and methods
cobol_dataitems_PictureString_picture: Property = Property(name="picture", type=StringType)
cobol_dataitems_PictureString.attributes={cobol_dataitems_PictureString_picture}

# DataItemAttribute class attributes and methods

# cobol_dataitems_RenamingDataName class attributes and methods

# DataName class attributes and methods

# RangeExpression class attributes and methods

# cobol_dataitems_ConditionName class attributes and methods

# cobol_dataitems_Global class attributes and methods

# cobol_dataitems_External class attributes and methods

# cobol_dataitems_Value class attributes and methods

# cobol_dataitems_DataItemAttribute class attributes and methods

# cobol_dataitems_Usage class attributes and methods
cobol_dataitems_Usage_usage: Property = Property(name="usage", type=StringType)
cobol_dataitems_Usage_isNative: Property = Property(name="isNative", type=BooleanType)
cobol_dataitems_Usage.attributes={cobol_dataitems_Usage_isNative, cobol_dataitems_Usage_usage}

# cobol_dataitems_GroupUsage class attributes and methods

# cobol_dataitems_DataItem class attributes and methods
cobol_dataitems_DataItem_levelNumber: Property = Property(name="levelNumber", type=StringType)
cobol_dataitems_DataItem.attributes={cobol_dataitems_DataItem_levelNumber}

# references_ReferenceableElement class attributes and methods

# cobol_specialnames_ExplicitAlphabetType class attributes and methods

# cobol_dataitems_RecordName class attributes and methods

# cobol_dataitems_DataName class attributes and methods

# cobol_dataitems_Redefines class attributes and methods

# cobol_specialnames_SpecialName class attributes and methods

# cobol_specialnames_ConditionName class attributes and methods

# specialnames_SpecialName class attributes and methods

# cobol_specialnames_OnStatus class attributes and methods

# ConditionName class attributes and methods

# cobol_specialnames_OffStatus class attributes and methods

# cobol_specialnames_AlphabetName class attributes and methods

# specialnames_SpecialNameStatement class attributes and methods

# AlphabetType class attributes and methods

# cobol_specialnames_UPSISwitchIs class attributes and methods

# specialnames_MnemonicName class attributes and methods

# cobol_specialnames_AlphabetType class attributes and methods

# cobol_specialnames_PredefinedAlphabetType class attributes and methods
cobol_specialnames_PredefinedAlphabetType_value: Property = Property(name="value", type=StringType)
cobol_specialnames_PredefinedAlphabetType.attributes={cobol_specialnames_PredefinedAlphabetType_value}

# KeyName class attributes and methods

# cobol_tables_KeyName class attributes and methods
cobol_tables_KeyName_keyOrder: Property = Property(name="keyOrder", type=StringType)
cobol_tables_KeyName.attributes={cobol_tables_KeyName_keyOrder}

# cobol_specialnames_CodeNameAlphabetType class attributes and methods
cobol_specialnames_CodeNameAlphabetType_value: Property = Property(name="value", type=StringType)
cobol_specialnames_CodeNameAlphabetType.attributes={cobol_specialnames_CodeNameAlphabetType_value}

# cobol_specialnames_CurrencySign class attributes and methods
cobol_specialnames_CurrencySign_pictureSymbol: Property = Property(name="pictureSymbol", type=StringType)
cobol_specialnames_CurrencySign.attributes={cobol_specialnames_CurrencySign_pictureSymbol}

# cobol_specialnames_ClassName class attributes and methods

# cobol_specialnames_MnemonicName class attributes and methods

# SpecialName class attributes and methods

# cobol_specialnames_SystemDeviceIs class attributes and methods

# cobol_specialnames_SymbolicCharacter class attributes and methods

# cobol_specialnames_SymbolicCharacterStatement class attributes and methods

# SymbolicCharacter class attributes and methods

# AlphabetNameReference class attributes and methods

# cobol_specialnames_SpecialNameStatement class attributes and methods

# cobol_tables_Table class attributes and methods

# dataitems_DataItem class attributes and methods

# TableDimension class attributes and methods

# IndexName class attributes and methods

# cobol_parameters_Parametrizable class attributes and methods

# Parameter class attributes and methods

# cobol_tables_IndexName class attributes and methods

# AdditionalIndexName class attributes and methods

# cobol_tables_TableDimension class attributes and methods
cobol_tables_TableDimension_value: Property = Property(name="value", type=IntegerType)
cobol_tables_TableDimension.attributes={cobol_tables_TableDimension_value}

# cobol_tables_AdditionalIndexName class attributes and methods

# cobol_files_FileName class attributes and methods
cobol_files_FileName_fileDescriptor: Property = Property(name="fileDescriptor", type=StringType)
cobol_files_FileName.attributes={cobol_files_FileName_fileDescriptor}

# cobol_files_SelectStatement class attributes and methods
cobol_files_SelectStatement_isOptional: Property = Property(name="isOptional", type=BooleanType)
cobol_files_SelectStatement_externalFileNames: Property = Property(name="externalFileNames", type=StringType)
cobol_files_SelectStatement.attributes={cobol_files_SelectStatement_isOptional, cobol_files_SelectStatement_externalFileNames}

# FileStatus class attributes and methods

# cobol_files_FileStatus class attributes and methods

# cobol_labels_ProcedureLabel class attributes and methods

# cobol_parameters_Parameter class attributes and methods

# cobol_parameters_ByReferenceParameter class attributes and methods

# cobol_parameters_ByValueParameter class attributes and methods

# cobol_declaratives_Declaratives class attributes and methods

# DeclarativeSection class attributes and methods

# cobol_verbs_Is class attributes and methods

# Verb class attributes and methods

# cobol_verbs_Verb class attributes and methods

# cobol_labels_ProcedureRange class attributes and methods

# ProcedureRangeChild class attributes and methods

# cobol_labels_ProcedureRangeLabel class attributes and methods

# cobol_handlers_InvalidKey class attributes and methods

# cobol_labels_ProcedureRangeChild class attributes and methods

# cobol_handlers_NotAtEndOfPage class attributes and methods

# Procedure class attributes and methods

# cobol_labels_Procedure class attributes and methods

# cobol_labels_Label class attributes and methods

# cobol_labels_StopLabel class attributes and methods

# cobol_labels_Run class attributes and methods

# cobol_functions_FunctionCall class attributes and methods

# cobol_functions_Argument class attributes and methods

# cobol_functions_ByReferenceArgument class attributes and methods

# Argument class attributes and methods

# cobol_functions_ByValueArgument class attributes and methods

# cobol_functions_ByContentArgument class attributes and methods

# cobol_functions_OmittedArgument class attributes and methods

# cobol_functions_Argumentable class attributes and methods

# cobol_handlers_OnSizeError class attributes and methods

# cobol_handlers_Handler class attributes and methods

# cobol_handlers_NotOnSizeError class attributes and methods

# NotErrorHandler class attributes and methods

# cobol_handlers_OnOverflow class attributes and methods

# cobol_handlers_OnException class attributes and methods

# cobol_handlers_NotOnException class attributes and methods

# cobol_handlers_NotErrorHandler class attributes and methods

# cobol_handlers_NotOnOverflow class attributes and methods

# cobol_handlers_NotAtEnd class attributes and methods

# cobol_handlers_AtEnd class attributes and methods

# cobol_handlers_AtEndOfPage class attributes and methods
cobol_handlers_AtEndOfPage_eop: Property = Property(name="eop", type=StringType)
cobol_handlers_AtEndOfPage.attributes={cobol_handlers_AtEndOfPage_eop}

# cobol_strings_ReplacementOccurrence class attributes and methods

# strings_Replacement class attributes and methods

# cobol_handlers_NotInvalidKey class attributes and methods

# cobol_strings_Tallying class attributes and methods

# StringManipulation class attributes and methods

# cobol_strings_StringManipulation class attributes and methods

# String class attributes and methods

# Location class attributes and methods

# cobol_strings_ManipulatedStrings class attributes and methods

# cobol_strings_String class attributes and methods

# cobol_strings_ConcatenatingStrings class attributes and methods

# ManipulatedStrings class attributes and methods

# cobol_strings_SplittedString class attributes and methods

# cobol_strings_Location class attributes and methods
cobol_strings_Location_position: Property = Property(name="position", type=StringType)
cobol_strings_Location_initial: Property = Property(name="initial", type=BooleanType)
cobol_strings_Location.attributes={cobol_strings_Location_position, cobol_strings_Location_initial}

# cobol_strings_Replacement class attributes and methods

# cobol_strings_Occurrence class attributes and methods
cobol_strings_Occurrence_type: Property = Property(name="type", type=StringType)
cobol_strings_Occurrence.attributes={cobol_strings_Occurrence_type}

# cobol_strings_TallyingOccurrence class attributes and methods

# strings_Tallying class attributes and methods

# strings_Occurrence class attributes and methods

# cobol_strings_AnyCharacter class attributes and methods

# cobol_strings_SpecificCharacter class attributes and methods

# cobol_strings_AnyCharacterBySpecificCharacter class attributes and methods

# cobol_strings_SpecificCharacterBySpecificCharacter class attributes and methods

# Relationships
negateOperator4: BinaryAssociation = BinaryAssociation(
    name="negateOperator4",
    ends={
        Property(name="Negate", type=cobol_conditions_NegatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NegatedConditionalExpression5", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children6: BinaryAssociation = BinaryAssociation(
    name="children6",
    ends={
        Property(name="SimpleConditionChild", type=cobol_conditions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_RelationalExpression", type=SimpleConditionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationalOperator7: BinaryAssociation = BinaryAssociation(
    name="relationalOperator7",
    ends={
        Property(name="RelationalOperator", type=cobol_conditions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_RelationalExpression8", type=RelationalOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negateOperator9: BinaryAssociation = BinaryAssociation(
    name="negateOperator9",
    ends={
        Property(name="Negate11", type=cobol_conditions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_RelationalExpression10", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is_12: BinaryAssociation = BinaryAssociation(
    name="is_12",
    ends={
        Property(name="Is", type=cobol_conditions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_RelationalExpression13", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="ConditionalOrExpressionChild", type=cobol_conditions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ConditionalOrExpression", type=ConditionalOrExpressionChild, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalOperators1: BinaryAssociation = BinaryAssociation(
    name="logicalOperators1",
    ends={
        Property(name="LogicalOperator", type=cobol_conditions_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ConditionalOrExpression2", type=LogicalOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child3: BinaryAssociation = BinaryAssociation(
    name="child3",
    ends={
        Property(name="NegatedConditionalExpressionChild", type=cobol_conditions_NegatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NegatedConditionalExpression", type=NegatedConditionalExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negateOperator18: BinaryAssociation = BinaryAssociation(
    name="negateOperator18",
    ends={
        Property(name="Negate20", type=cobol_conditions_NegatedAbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NegatedAbbreviatedConditionalExpression19", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relationalOperator21: BinaryAssociation = BinaryAssociation(
    name="relationalOperator21",
    ends={
        Property(name="RelationalOperator22", type=cobol_conditions_AbbreviatedRelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_AbbreviatedRelationalExpression", type=RelationalOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child23: BinaryAssociation = BinaryAssociation(
    name="child23",
    ends={
        Property(name="AbbreviatedRelationalExpressionChild", type=cobol_conditions_AbbreviatedRelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_AbbreviatedRelationalExpression24", type=AbbreviatedRelationalExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negateOperator25: BinaryAssociation = BinaryAssociation(
    name="negateOperator25",
    ends={
        Property(name="Negate27", type=cobol_conditions_AbbreviatedRelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_AbbreviatedRelationalExpression26", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is_28: BinaryAssociation = BinaryAssociation(
    name="is_28",
    ends={
        Property(name="Is30", type=cobol_conditions_AbbreviatedRelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_AbbreviatedRelationalExpression29", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression31: BinaryAssociation = BinaryAssociation(
    name="expression31",
    ends={
        Property(name="Condition32", type=cobol_conditions_NestedAbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NestedAbbreviatedConditionalExpression", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rest33: BinaryAssociation = BinaryAssociation(
    name="rest33",
    ends={
        Property(name="Condition35", type=cobol_conditions_NestedAbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NestedAbbreviatedConditionalExpression34", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expressions14: BinaryAssociation = BinaryAssociation(
    name="expressions14",
    ends={
        Property(name="Condition", type=cobol_conditions_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ExpressionList", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="ConditionalAndExpressionChild", type=cobol_conditions_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ConditionalAndExpression", type=ConditionalAndExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children16: BinaryAssociation = BinaryAssociation(
    name="children16",
    ends={
        Property(name="AbbreviatedConditionalExpressionChild", type=cobol_conditions_AbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_AbbreviatedConditionalExpression", type=AbbreviatedConditionalExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child17: BinaryAssociation = BinaryAssociation(
    name="child17",
    ends={
        Property(name="NegatedAbbreviatedConditionalExpressionChild", type=cobol_conditions_NegatedAbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NegatedAbbreviatedConditionalExpression", type=NegatedAbbreviatedConditionalExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition56: BinaryAssociation = BinaryAssociation(
    name="condition56",
    ends={
        Property(name="Condition57", type=cobol_conditions_NestedCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NestedCondition", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children58: BinaryAssociation = BinaryAssociation(
    name="children58",
    ends={
        Property(name="AdditiveArithmeticExpressionChild", type=cobol_arithmetics_AdditiveArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_AdditiveArithmeticExpression", type=AdditiveArithmeticExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additiveOperators59: BinaryAssociation = BinaryAssociation(
    name="additiveOperators59",
    ends={
        Property(name="AdditiveOperator", type=cobol_arithmetics_AdditiveArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_AdditiveArithmeticExpression60", type=AdditiveOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children61: BinaryAssociation = BinaryAssociation(
    name="children61",
    ends={
        Property(name="MultiplicativeArithmeticExpressionChild", type=cobol_arithmetics_MultiplicativeArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_MultiplicativeArithmeticExpression", type=MultiplicativeArithmeticExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
multiplicativeOperators62: BinaryAssociation = BinaryAssociation(
    name="multiplicativeOperators62",
    ends={
        Property(name="MultiplicativeOperator", type=cobol_arithmetics_MultiplicativeArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_MultiplicativeArithmeticExpression63", type=MultiplicativeOperator, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child36: BinaryAssociation = BinaryAssociation(
    name="child36",
    ends={
        Property(name="SimpleConditionChild37", type=cobol_conditions_SignCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_SignCondition", type=SimpleConditionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signOperator38: BinaryAssociation = BinaryAssociation(
    name="signOperator38",
    ends={
        Property(name="SignOperator", type=cobol_conditions_SignCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_SignCondition39", type=SignOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negateOperator40: BinaryAssociation = BinaryAssociation(
    name="negateOperator40",
    ends={
        Property(name="Negate42", type=cobol_conditions_SignCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_SignCondition41", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is_43: BinaryAssociation = BinaryAssociation(
    name="is_43",
    ends={
        Property(name="Is45", type=cobol_conditions_SignCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_SignCondition44", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
child46: BinaryAssociation = BinaryAssociation(
    name="child46",
    ends={
        Property(name="SimpleConditionChild47", type=cobol_conditions_ClassCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ClassCondition", type=SimpleConditionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
classOperator48: BinaryAssociation = BinaryAssociation(
    name="classOperator48",
    ends={
        Property(name="ClassOperator", type=cobol_conditions_ClassCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ClassCondition49", type=ClassOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
negateOperator50: BinaryAssociation = BinaryAssociation(
    name="negateOperator50",
    ends={
        Property(name="Negate52", type=cobol_conditions_ClassCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ClassCondition51", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
is_53: BinaryAssociation = BinaryAssociation(
    name="is_53",
    ends={
        Property(name="Is55", type=cobol_conditions_ClassCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ClassCondition54", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children74: BinaryAssociation = BinaryAssociation(
    name="children74",
    ends={
        Property(name="RangeExpressionChild", type=cobol_arithmetics_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_RangeExpression", type=RangeExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
throughOperator75: BinaryAssociation = BinaryAssociation(
    name="throughOperator75",
    ends={
        Property(name="Through", type=cobol_arithmetics_RangeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_RangeExpression76", type=Through, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression77: BinaryAssociation = BinaryAssociation(
    name="expression77",
    ends={
        Property(name="ArithmeticExpression78", type=cobol_arithmetics_NestedArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_NestedArithmeticExpression", type=ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compilationUnits79: BinaryAssociation = BinaryAssociation(
    name="compilationUnits79",
    ends={
        Property(name="CompilationUnit", type=cobol_containers_CompilationGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationGroup", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identificationDivision80: BinaryAssociation = BinaryAssociation(
    name="identificationDivision80",
    ends={
        Property(name="IdentificationDivision", type=cobol_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationUnit", type=IdentificationDivision, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children64: BinaryAssociation = BinaryAssociation(
    name="children64",
    ends={
        Property(name="PowerArithmeticExpressionChild", type=cobol_arithmetics_PowerArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_PowerArithmeticExpression", type=PowerArithmeticExpressionChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
child65: BinaryAssociation = BinaryAssociation(
    name="child65",
    ends={
        Property(name="UnaryArithmeticExpressionChild", type=cobol_arithmetics_UnaryArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_UnaryArithmeticExpression", type=UnaryArithmeticExpressionChild, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryOperator66: BinaryAssociation = BinaryAssociation(
    name="unaryOperator66",
    ends={
        Property(name="UnaryOperator", type=cobol_arithmetics_UnaryArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_UnaryArithmeticExpression67", type=UnaryOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignmentOperator68: BinaryAssociation = BinaryAssociation(
    name="assignmentOperator68",
    ends={
        Property(name="Equal", type=cobol_arithmetics_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_AssignmentExpression", type=Equal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children69: BinaryAssociation = BinaryAssociation(
    name="children69",
    ends={
        Property(name="ArithmeticExpression", type=cobol_arithmetics_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_AssignmentExpression70", type=ArithmeticExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value71: BinaryAssociation = BinaryAssociation(
    name="value71",
    ends={
        Property(name="ArithmeticExpression73", type=cobol_arithmetics_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_arithmetics_AssignmentExpression72", type=ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaratives95: BinaryAssociation = BinaryAssociation(
    name="declaratives95",
    ends={
        Property(name="Declaratives", type=cobol_divisions_ProcedureDivision, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_divisions_ProcedureDivision", type=Declaratives, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
environmentDivision81: BinaryAssociation = BinaryAssociation(
    name="environmentDivision81",
    ends={
        Property(name="EnvironmentDivision", type=cobol_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationUnit82", type=EnvironmentDivision, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataDivision83: BinaryAssociation = BinaryAssociation(
    name="dataDivision83",
    ends={
        Property(name="DataDivision", type=cobol_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationUnit84", type=DataDivision, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
procedureDivision85: BinaryAssociation = BinaryAssociation(
    name="procedureDivision85",
    ends={
        Property(name="ProcedureDivision", type=cobol_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationUnit86", type=ProcedureDivision, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedCompilationUnits87: BinaryAssociation = BinaryAssociation(
    name="nestedCompilationUnits87",
    ends={
        Property(name="CompilationUnit89", type=cobol_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_containers_CompilationUnit88", type=CompilationUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections90: BinaryAssociation = BinaryAssociation(
    name="sections90",
    ends={
        Property(name="Section", type=cobol_divisions_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_divisions_Division", type=Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs91: BinaryAssociation = BinaryAssociation(
    name="paragraphs91",
    ends={
        Property(name="Paragraph", type=cobol_divisions_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_divisions_Division92", type=Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sentences93: BinaryAssociation = BinaryAssociation(
    name="sentences93",
    ends={
        Property(name="StatementContainer", type=cobol_divisions_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_divisions_Division94", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constant96: BinaryAssociation = BinaryAssociation(
    name="constant96",
    ends={
        Property(name="ConstantLiteral", type=cobol_literals_AllLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_literals_AllLiteral", type=ConstantLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sentences97: BinaryAssociation = BinaryAssociation(
    name="sentences97",
    ends={
        Property(name="StatementContainer98", type=cobol_paragraphs_Paragraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_paragraphs_Paragraph", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
withDebuggingMode99: BinaryAssociation = BinaryAssociation(
    name="withDebuggingMode99",
    ends={
        Property(name="DebuggingMode", type=cobol_paragraphs_SourceComputerParagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_paragraphs_SourceComputerParagraph", type=DebuggingMode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectStatements100: BinaryAssociation = BinaryAssociation(
    name="selectStatements100",
    ends={
        Property(name="SelectStatement", type=cobol_paragraphs_FileControlParagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_paragraphs_FileControlParagraph", type=SelectStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifier109: BinaryAssociation = BinaryAssociation(
    name="qualifier109",
    ends={
        Property(name="ElementReference", type=cobol_references_Qualifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_references_Qualifiable", type=ElementReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentences110: BinaryAssociation = BinaryAssociation(
    name="sentences110",
    ends={
        Property(name="StatementContainer111", type=cobol_sections_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_Section", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs112: BinaryAssociation = BinaryAssociation(
    name="paragraphs112",
    ends={
        Property(name="Paragraph114", type=cobol_sections_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_Section113", type=Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialNameStatements101: BinaryAssociation = BinaryAssociation(
    name="specialNameStatements101",
    ends={
        Property(name="SpecialNameStatement", type=cobol_paragraphs_SpecialNamesParagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_paragraphs_SpecialNamesParagraph", type=SpecialNameStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
water102: BinaryAssociation = BinaryAssociation(
    name="water102",
    ends={
        Property(name="SpecialNamesParagraphWater", type=cobol_paragraphs_SpecialNamesParagraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_paragraphs_SpecialNamesParagraph103", type=SpecialNamesParagraphWater, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliasesTo104: BinaryAssociation = BinaryAssociation(
    name="aliasesTo104",
    ends={
        Property(name="ReferenceableElement", type=cobol_references_ReferenceableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aliasesFrom", type=ReferenceableElement, multiplicity=Multiplicity(0, 9999))
    }
)
aliasesFrom105: BinaryAssociation = BinaryAssociation(
    name="aliasesFrom105",
    ends={
        Property(name="ReferenceableElement106", type=cobol_references_ReferenceableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="aliasesTo", type=ReferenceableElement, multiplicity=Multiplicity(0, 9999))
    }
)
target107: BinaryAssociation = BinaryAssociation(
    name="target107",
    ends={
        Property(name="ReferenceableElement108", type=cobol_references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(1, 1))
    }
)
fileDescriptors118: BinaryAssociation = BinaryAssociation(
    name="fileDescriptors118",
    ends={
        Property(name="FileName", type=cobol_sections_FileSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_FileSection", type=FileName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements119: BinaryAssociation = BinaryAssociation(
    name="statements119",
    ends={
        Property(name="Statement120", type=cobol_sentences_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sentences_StatementContainer", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next121: BinaryAssociation = BinaryAssociation(
    name="next121",
    ends={
        Property(name="Sentence", type=cobol_sentences_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sentences_Sentence", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
statements115: BinaryAssociation = BinaryAssociation(
    name="statements115",
    ends={
        Property(name="Statement", type=cobol_sections_DataDivisionSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_DataDivisionSection", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records116: BinaryAssociation = BinaryAssociation(
    name="records116",
    ends={
        Property(name="DataItem", type=cobol_sections_DataDivisionSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_DataDivisionSection117", type=DataItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next123: BinaryAssociation = BinaryAssociation(
    name="next123",
    ends={
        Property(name="cobol_statements_Statement", type=Statement, multiplicity=Multiplicity(0, 1)),
        Property(name="Statement124", type=cobol_statements_Statement, multiplicity=Multiplicity(1, 1))
    }
)
operands125: BinaryAssociation = BinaryAssociation(
    name="operands125",
    ends={
        Property(name="ArithmeticOperand", type=cobol_statements_ArithmeticStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ArithmeticStatement", type=ArithmeticOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
givings126: BinaryAssociation = BinaryAssociation(
    name="givings126",
    ends={
        Property(name="ArithmeticOperand128", type=cobol_statements_ArithmeticStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ArithmeticStatement127", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tos129: BinaryAssociation = BinaryAssociation(
    name="tos129",
    ends={
        Property(name="ArithmeticOperand130", type=cobol_statements_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Add", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
froms131: BinaryAssociation = BinaryAssociation(
    name="froms131",
    ends={
        Property(name="ArithmeticOperand132", type=cobol_statements_Subtract, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Subtract", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bys133: BinaryAssociation = BinaryAssociation(
    name="bys133",
    ends={
        Property(name="ArithmeticOperand134", type=cobol_statements_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Multiply", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
intos135: BinaryAssociation = BinaryAssociation(
    name="intos135",
    ends={
        Property(name="ArithmeticOperand136", type=cobol_statements_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Divide", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
remainders137: BinaryAssociation = BinaryAssociation(
    name="remainders137",
    ends={
        Property(name="Identifier139", type=cobol_statements_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Divide138", type=Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier122: BinaryAssociation = BinaryAssociation(
    name="identifier122",
    ends={
        Property(name="Identifier", type=cobol_operands_RoundedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_operands_RoundedIdentifier", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sender147: BinaryAssociation = BinaryAssociation(
    name="sender147",
    ends={
        Property(name="PrimaryOperand149", type=cobol_statements_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Move148", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseStatements150: BinaryAssociation = BinaryAssociation(
    name="elseStatements150",
    ends={
        Property(name="Statement151", type=cobol_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Condition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition152: BinaryAssociation = BinaryAssociation(
    name="condition152",
    ends={
        Property(name="Condition153", type=cobol_statements_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Conditional", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label154: BinaryAssociation = BinaryAssociation(
    name="label154",
    ends={
        Property(name="StopLabel", type=cobol_statements_Stop, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Stop", type=StopLabel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands155: BinaryAssociation = BinaryAssociation(
    name="operands155",
    ends={
        Property(name="PrimaryOperand156", type=cobol_statements_Display, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Display", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output157: BinaryAssociation = BinaryAssociation(
    name="output157",
    ends={
        Property(name="Environment", type=cobol_statements_Display, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Display158", type=Environment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression159: BinaryAssociation = BinaryAssociation(
    name="expression159",
    ends={
        Property(name="AssignmentExpression", type=cobol_statements_Compute, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Compute", type=AssignmentExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label140: BinaryAssociation = BinaryAssociation(
    name="label140",
    ends={
        Property(name="ProcedureRangeLabel", type=cobol_statements_PerformProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformProcedure", type=ProcedureRangeLabel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labels141: BinaryAssociation = BinaryAssociation(
    name="labels141",
    ends={
        Property(name="ProcedureRangeLabel142", type=cobol_statements_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Jump", type=ProcedureRangeLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependsOn143: BinaryAssociation = BinaryAssociation(
    name="dependsOn143",
    ends={
        Property(name="IdentifierReference", type=cobol_statements_GoTo, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_GoTo", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements144: BinaryAssociation = BinaryAssociation(
    name="statements144",
    ends={
        Property(name="Statement145", type=cobol_statements_NestedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_NestedStatement", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
receivers146: BinaryAssociation = BinaryAssociation(
    name="receivers146",
    ends={
        Property(name="PrimaryOperand", type=cobol_statements_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Move", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
switches169: BinaryAssociation = BinaryAssociation(
    name="switches169",
    ends={
        Property(name="SwitchStatus", type=cobol_statements_SetSwitches, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetSwitches", type=SwitchStatus, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
receivers170: BinaryAssociation = BinaryAssociation(
    name="receivers170",
    ends={
        Property(name="IndexNameReference", type=cobol_statements_SetIndexName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetIndexName", type=IndexNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pointer171: BinaryAssociation = BinaryAssociation(
    name="pointer171",
    ends={
        Property(name="Identifier172", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver173: BinaryAssociation = BinaryAssociation(
    name="receiver173",
    ends={
        Property(name="Identifier175", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String174", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
senders176: BinaryAssociation = BinaryAssociation(
    name="senders176",
    ends={
        Property(name="ConcatenatingStrings", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String177", type=ConcatenatingStrings, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subprograms178: BinaryAssociation = BinaryAssociation(
    name="subprograms178",
    ends={
        Property(name="PrimaryOperand179", type=cobol_statements_Cancel, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Cancel", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subprogram180: BinaryAssociation = BinaryAssociation(
    name="subprogram180",
    ends={
        Property(name="PrimaryOperand181", type=cobol_statements_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Call", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiver160: BinaryAssociation = BinaryAssociation(
    name="receiver160",
    ends={
        Property(name="PrimaryOperand161", type=cobol_statements_Accept, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Accept", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
handlers162: BinaryAssociation = BinaryAssociation(
    name="handlers162",
    ends={
        Property(name="Handler", type=cobol_statements_ErrorHandled, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ErrorHandled", type=Handler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileName163: BinaryAssociation = BinaryAssociation(
    name="fileName163",
    ends={
        Property(name="FileNameReference", type=cobol_statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Return", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
output164: BinaryAssociation = BinaryAssociation(
    name="output164",
    ends={
        Property(name="IdentifierReference166", type=cobol_statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Return165", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender167: BinaryAssociation = BinaryAssociation(
    name="sender167",
    ends={
        Property(name="PrimaryOperand168", type=cobol_statements_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetStatement", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pointer192: BinaryAssociation = BinaryAssociation(
    name="pointer192",
    ends={
        Property(name="cobol_statements_Unstring", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Identifier193", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1))
    }
)
tally194: BinaryAssociation = BinaryAssociation(
    name="tally194",
    ends={
        Property(name="IdentifierReference196", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring195", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender197: BinaryAssociation = BinaryAssociation(
    name="sender197",
    ends={
        Property(name="Identifier199", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring198", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receivers200: BinaryAssociation = BinaryAssociation(
    name="receivers200",
    ends={
        Property(name="SplittedString", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring201", type=SplittedString, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
delimiter202: BinaryAssociation = BinaryAssociation(
    name="delimiter202",
    ends={
        Property(name="Condition204", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring203", type=Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counter205: BinaryAssociation = BinaryAssociation(
    name="counter205",
    ends={
        Property(name="Identifier207", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring206", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases208: BinaryAssociation = BinaryAssociation(
    name="cases208",
    ends={
        Property(name="EvaluateCase", type=cobol_statements_Evaluate, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Evaluate", type=EvaluateCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subject209: BinaryAssociation = BinaryAssociation(
    name="subject209",
    ends={
        Property(name="ExpressionList", type=cobol_statements_Evaluate, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Evaluate210", type=ExpressionList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objects211: BinaryAssociation = BinaryAssociation(
    name="objects211",
    ends={
        Property(name="ExpressionList212", type=cobol_statements_EvaluateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_EvaluateCase", type=ExpressionList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subprograms182: BinaryAssociation = BinaryAssociation(
    name="subprograms182",
    ends={
        Property(name="Identifier183", type=cobol_statements_Initialize, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Initialize", type=Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacements184: BinaryAssociation = BinaryAssociation(
    name="replacements184",
    ends={
        Property(name="Replacement", type=cobol_statements_Initialize, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Initialize185", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases186: BinaryAssociation = BinaryAssociation(
    name="cases186",
    ends={
        Property(name="NormalEvaluateCase", type=cobol_statements_SearchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SearchStatement", type=NormalEvaluateCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
table187: BinaryAssociation = BinaryAssociation(
    name="table187",
    ends={
        Property(name="PrimaryOperand189", type=cobol_statements_SearchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SearchStatement188", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable190: BinaryAssociation = BinaryAssociation(
    name="variable190",
    ends={
        Property(name="Identifier191", type=cobol_statements_SerialSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SerialSearch", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver225: BinaryAssociation = BinaryAssociation(
    name="receiver225",
    ends={
        Property(name="Identifier226", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyName227: BinaryAssociation = BinaryAssociation(
    name="keyName227",
    ends={
        Property(name="Identifier229", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read228", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileName230: BinaryAssociation = BinaryAssociation(
    name="fileName230",
    ends={
        Property(name="FileNameReference232", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read231", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
recordName233: BinaryAssociation = BinaryAssociation(
    name="recordName233",
    ends={
        Property(name="Identifier234", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numLines235: BinaryAssociation = BinaryAssociation(
    name="numLines235",
    ends={
        Property(name="Identifier237", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write236", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer238: BinaryAssociation = BinaryAssociation(
    name="integer238",
    ends={
        Property(name="IntegerLiteral", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write239", type=IntegerLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mnemonicName240: BinaryAssociation = BinaryAssociation(
    name="mnemonicName240",
    ends={
        Property(name="MnemonicNameReference", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write241", type=MnemonicNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender242: BinaryAssociation = BinaryAssociation(
    name="sender242",
    ends={
        Property(name="Identifier244", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write243", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mnemonicNames245: BinaryAssociation = BinaryAssociation(
    name="mnemonicNames245",
    ends={
        Property(name="MnemonicNameReference246", type=cobol_statements_SwitchStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SwitchStatus", type=MnemonicNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tallyingIns213: BinaryAssociation = BinaryAssociation(
    name="tallyingIns213",
    ends={
        Property(name="TallyingIn", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect", type=TallyingIn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacements214: BinaryAssociation = BinaryAssociation(
    name="replacements214",
    ends={
        Property(name="Replacement216", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect215", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversions217: BinaryAssociation = BinaryAssociation(
    name="conversions217",
    ends={
        Property(name="Replacement219", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect218", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
string220: BinaryAssociation = BinaryAssociation(
    name="string220",
    ends={
        Property(name="PrimaryOperand222", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect221", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receivers223: BinaryAssociation = BinaryAssociation(
    name="receivers223",
    ends={
        Property(name="IdentifierReference224", type=cobol_statements_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Set", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sender262: BinaryAssociation = BinaryAssociation(
    name="sender262",
    ends={
        Property(name="IdentifierReference264", type=cobol_statements_Release, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Release263", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions247: BinaryAssociation = BinaryAssociation(
    name="conditions247",
    ends={
        Property(name="Condition248", type=cobol_statements_PerformUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformUntilCondition", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
iterations249: BinaryAssociation = BinaryAssociation(
    name="iterations249",
    ends={
        Property(name="PrimaryOperand250", type=cobol_statements_PerformFixedTimes, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformFixedTimes", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
afters251: BinaryAssociation = BinaryAssociation(
    name="afters251",
    ends={
        Property(name="AfterUntilCondition", type=cobol_statements_PerformProcedureUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformProcedureUntilCondition", type=AfterUntilCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileName252: BinaryAssociation = BinaryAssociation(
    name="fileName252",
    ends={
        Property(name="FileNameReference253", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
input254: BinaryAssociation = BinaryAssociation(
    name="input254",
    ends={
        Property(name="InputDirective", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement255", type=InputDirective, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output256: BinaryAssociation = BinaryAssociation(
    name="output256",
    ends={
        Property(name="OutputDirective", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement257", type=OutputDirective, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyDescriptors258: BinaryAssociation = BinaryAssociation(
    name="keyDescriptors258",
    ends={
        Property(name="KeyDescriptor", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement259", type=KeyDescriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
recordName260: BinaryAssociation = BinaryAssociation(
    name="recordName260",
    ends={
        Property(name="IdentifierReference261", type=cobol_statements_Release, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Release", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable275: BinaryAssociation = BinaryAssociation(
    name="variable275",
    ends={
        Property(name="IdentifierReference276", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyNames265: BinaryAssociation = BinaryAssociation(
    name="keyNames265",
    ends={
        Property(name="IdentifierReference266", type=cobol_statements_KeyDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_KeyDescriptor", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ioFileDescriptors267: BinaryAssociation = BinaryAssociation(
    name="ioFileDescriptors267",
    ends={
        Property(name="IOFileDescriptor", type=cobol_statements_IOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOStatement", type=IOFileDescriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ioFiles268: BinaryAssociation = BinaryAssociation(
    name="ioFiles268",
    ends={
        Property(name="IOFile", type=cobol_statements_IOFileDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOFileDescriptor", type=IOFile, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fileName269: BinaryAssociation = BinaryAssociation(
    name="fileName269",
    ends={
        Property(name="FileNameReference270", type=cobol_statements_IOFile, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOFile", type=FileNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occurrences271: BinaryAssociation = BinaryAssociation(
    name="occurrences271",
    ends={
        Property(name="Tallying", type=cobol_statements_TallyingIn, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_TallyingIn", type=Tallying, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
counter272: BinaryAssociation = BinaryAssociation(
    name="counter272",
    ends={
        Property(name="Identifier274", type=cobol_statements_TallyingIn, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_TallyingIn273", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
qualifiers299: BinaryAssociation = BinaryAssociation(
    name="qualifiers299",
    ends={
        Property(name="Qualifier", type=cobol_identifiers_IdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_IdentifierReference300", type=Qualifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init277: BinaryAssociation = BinaryAssociation(
    name="init277",
    ends={
        Property(name="PrimaryOperand279", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition278", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
increment280: BinaryAssociation = BinaryAssociation(
    name="increment280",
    ends={
        Property(name="PrimaryOperand282", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition281", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileName283: BinaryAssociation = BinaryAssociation(
    name="fileName283",
    ends={
        Property(name="FileNameReference284", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator285: BinaryAssociation = BinaryAssociation(
    name="operator285",
    ends={
        Property(name="RelationalOperator287", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start286", type=RelationalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataName288: BinaryAssociation = BinaryAssociation(
    name="dataName288",
    ends={
        Property(name="Identifier290", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start289", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not_291: BinaryAssociation = BinaryAssociation(
    name="not_291",
    ends={
        Property(name="Negate293", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start292", type=Negate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileName294: BinaryAssociation = BinaryAssociation(
    name="fileName294",
    ends={
        Property(name="FileNameReference295", type=cobol_statements_Delete, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Delete", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subscript296: BinaryAssociation = BinaryAssociation(
    name="subscript296",
    ends={
        Property(name="Operand", type=cobol_identifiers_Subscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_Subscript", type=Operand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier297: BinaryAssociation = BinaryAssociation(
    name="modifier297",
    ends={
        Property(name="ReferenceModifier", type=cobol_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_Identifier", type=ReferenceModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts298: BinaryAssociation = BinaryAssociation(
    name="subscripts298",
    ends={
        Property(name="Subscript", type=cobol_identifiers_IdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_IdentifierReference", type=Subscript, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start301: BinaryAssociation = BinaryAssociation(
    name="start301",
    ends={
        Property(name="ArithmeticExpression302", type=cobol_identifiers_ReferenceModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_ReferenceModifier", type=ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
length303: BinaryAssociation = BinaryAssociation(
    name="length303",
    ends={
        Property(name="ArithmeticExpression305", type=cobol_identifiers_ReferenceModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_ReferenceModifier304", type=ArithmeticExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveOperator306: BinaryAssociation = BinaryAssociation(
    name="additiveOperator306",
    ends={
        Property(name="AdditiveOperator307", type=cobol_identifiers_RelativeSubscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_RelativeSubscript", type=AdditiveOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer308: BinaryAssociation = BinaryAssociation(
    name="integer308",
    ends={
        Property(name="IntegerLiteral310", type=cobol_identifiers_RelativeSubscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_RelativeSubscript309", type=IntegerLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileNames311: BinaryAssociation = BinaryAssociation(
    name="fileNames311",
    ends={
        Property(name="FileNameReference312", type=cobol_ios_FileDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_ios_FileDirective", type=FileNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label313: BinaryAssociation = BinaryAssociation(
    name="label313",
    ends={
        Property(name="Label", type=cobol_ios_ProcedureDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_ios_ProcedureDirective", type=Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
water314: BinaryAssociation = BinaryAssociation(
    name="water314",
    ends={
        Property(name="Water", type=cobol_water_IncompleteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_water_IncompleteElement", type=Water, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand315: BinaryAssociation = BinaryAssociation(
    name="operand315",
    ends={
        Property(name="PrimaryOperand316", type=cobol_registers_Register, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_registers_Register", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nameRange317: BinaryAssociation = BinaryAssociation(
    name="nameRange317",
    ends={
        Property(name="RangeExpression", type=cobol_dataitems_RenamingDataName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_RenamingDataName", type=RangeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values318: BinaryAssociation = BinaryAssociation(
    name="values318",
    ends={
        Property(name="Condition319", type=cobol_dataitems_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_Value", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attributes320: BinaryAssociation = BinaryAssociation(
    name="attributes320",
    ends={
        Property(name="DataItemAttribute", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_DataItem", type=DataItemAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subentries321: BinaryAssociation = BinaryAssociation(
    name="subentries321",
    ends={
        Property(name="DataItem322", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="superentry", type=DataItem, multiplicity=Multiplicity(0, 9999))
    }
)
superentry323: BinaryAssociation = BinaryAssociation(
    name="superentry323",
    ends={
        Property(name="DataItem324", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="subentries", type=DataItem, multiplicity=Multiplicity(0, 1))
    }
)
range331: BinaryAssociation = BinaryAssociation(
    name="range331",
    ends={
        Property(name="RangeExpression332", type=cobol_specialnames_ExplicitAlphabetType, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_ExplicitAlphabetType", type=RangeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elems325: BinaryAssociation = BinaryAssociation(
    name="elems325",
    ends={
        Property(name="DataItem326", type=cobol_dataitems_RecordName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_RecordName", type=DataItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataName327: BinaryAssociation = BinaryAssociation(
    name="dataName327",
    ends={
        Property(name="IdentifierReference328", type=cobol_dataitems_Redefines, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_Redefines", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type329: BinaryAssociation = BinaryAssociation(
    name="type329",
    ends={
        Property(name="AlphabetType", type=cobol_specialnames_AlphabetName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_AlphabetName", type=AlphabetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionNames330: BinaryAssociation = BinaryAssociation(
    name="conditionNames330",
    ends={
        Property(name="ConditionName", type=cobol_specialnames_UPSISwitchIs, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_UPSISwitchIs", type=ConditionName, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
keysAre346: BinaryAssociation = BinaryAssociation(
    name="keysAre346",
    ends={
        Property(name="KeyName", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table347", type=KeyName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxTableDimension348: BinaryAssociation = BinaryAssociation(
    name="maxTableDimension348",
    ends={
        Property(name="TableDimension350", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table349", type=TableDimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependsOn351: BinaryAssociation = BinaryAssociation(
    name="dependsOn351",
    ends={
        Property(name="IdentifierReference353", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table352", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
currency333: BinaryAssociation = BinaryAssociation(
    name="currency333",
    ends={
        Property(name="Literal", type=cobol_specialnames_CurrencySign, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_CurrencySign", type=Literal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range334: BinaryAssociation = BinaryAssociation(
    name="range334",
    ends={
        Property(name="RangeExpression335", type=cobol_specialnames_ClassName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_ClassName", type=RangeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
environment336: BinaryAssociation = BinaryAssociation(
    name="environment336",
    ends={
        Property(name="Environment337", type=cobol_specialnames_MnemonicName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_MnemonicName", type=Environment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integers338: BinaryAssociation = BinaryAssociation(
    name="integers338",
    ends={
        Property(name="IntegerLiteral339", type=cobol_specialnames_SymbolicCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacter", type=IntegerLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
symbolicCharacters340: BinaryAssociation = BinaryAssociation(
    name="symbolicCharacters340",
    ends={
        Property(name="SymbolicCharacter", type=cobol_specialnames_SymbolicCharacterStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacterStatement", type=SymbolicCharacter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
alphabetNameReference341: BinaryAssociation = BinaryAssociation(
    name="alphabetNameReference341",
    ends={
        Property(name="AlphabetNameReference", type=cobol_specialnames_SymbolicCharacterStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacterStatement342", type=AlphabetNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDimension343: BinaryAssociation = BinaryAssociation(
    name="tableDimension343",
    ends={
        Property(name="TableDimension", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table", type=TableDimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indexedBy344: BinaryAssociation = BinaryAssociation(
    name="indexedBy344",
    ends={
        Property(name="IndexName", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table345", type=IndexName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vsamFileStatus371: BinaryAssociation = BinaryAssociation(
    name="vsamFileStatus371",
    ends={
        Property(name="cobol_files_FileStatus372", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="IdentifierReference373", type=cobol_files_FileStatus, multiplicity=Multiplicity(1, 1))
    }
)
parameters374: BinaryAssociation = BinaryAssociation(
    name="parameters374",
    ends={
        Property(name="Parameter", type=cobol_parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_parameters_Parametrizable", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keys354: BinaryAssociation = BinaryAssociation(
    name="keys354",
    ends={
        Property(name="IdentifierReference355", type=cobol_tables_KeyName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_KeyName", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additionalIndexNames356: BinaryAssociation = BinaryAssociation(
    name="additionalIndexNames356",
    ends={
        Property(name="AdditionalIndexName", type=cobol_tables_IndexName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_IndexName", type=AdditionalIndexName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records357: BinaryAssociation = BinaryAssociation(
    name="records357",
    ends={
        Property(name="DataItem358", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName", type=DataItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes359: BinaryAssociation = BinaryAssociation(
    name="attributes359",
    ends={
        Property(name="DataItemAttribute361", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName360", type=DataItemAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sentences362: BinaryAssociation = BinaryAssociation(
    name="sentences362",
    ends={
        Property(name="StatementContainer364", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName363", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileStatus365: BinaryAssociation = BinaryAssociation(
    name="fileStatus365",
    ends={
        Property(name="FileStatus", type=cobol_files_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_SelectStatement", type=FileStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileNameReference366: BinaryAssociation = BinaryAssociation(
    name="fileNameReference366",
    ends={
        Property(name="FileNameReference368", type=cobol_files_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_SelectStatement367", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileStatus369: BinaryAssociation = BinaryAssociation(
    name="fileStatus369",
    ends={
        Property(name="IdentifierReference370", type=cobol_files_FileStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileStatus", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
section384: BinaryAssociation = BinaryAssociation(
    name="section384",
    ends={
        Property(name="Section385", type=cobol_labels_ProcedureLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureLabel", type=Section, multiplicity=Multiplicity(0, 1))
    }
)
returning375: BinaryAssociation = BinaryAssociation(
    name="returning375",
    ends={
        Property(name="Parameter377", type=cobol_parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_parameters_Parametrizable376", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarativeSections378: BinaryAssociation = BinaryAssociation(
    name="declarativeSections378",
    ends={
        Property(name="DeclarativeSection", type=cobol_declaratives_Declaratives, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_declaratives_Declaratives", type=DeclarativeSection, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children379: BinaryAssociation = BinaryAssociation(
    name="children379",
    ends={
        Property(name="ProcedureRangeChild", type=cobol_labels_ProcedureRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRange", type=ProcedureRangeChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
throughOperator380: BinaryAssociation = BinaryAssociation(
    name="throughOperator380",
    ends={
        Property(name="Through382", type=cobol_labels_ProcedureRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRange381", type=Through, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target383: BinaryAssociation = BinaryAssociation(
    name="target383",
    ends={
        Property(name="Procedure", type=cobol_labels_ProcedureRangeChild, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRangeChild", type=Procedure, multiplicity=Multiplicity(1, 1))
    }
)
operands386: BinaryAssociation = BinaryAssociation(
    name="operands386",
    ends={
        Property(name="PrimaryOperand387", type=cobol_functions_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argument", type=PrimaryOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments388: BinaryAssociation = BinaryAssociation(
    name="arguments388",
    ends={
        Property(name="Argument", type=cobol_functions_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argumentable", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returning389: BinaryAssociation = BinaryAssociation(
    name="returning389",
    ends={
        Property(name="Argument391", type=cobol_functions_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argumentable390", type=Argument, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
handlerStatement392: BinaryAssociation = BinaryAssociation(
    name="handlerStatement392",
    ends={
        Property(name="Handler393", type=cobol_handlers_NotErrorHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_handlers_NotErrorHandler", type=Handler, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
locations394: BinaryAssociation = BinaryAssociation(
    name="locations394",
    ends={
        Property(name="Location", type=cobol_strings_StringManipulation, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_StringManipulation", type=Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strings395: BinaryAssociation = BinaryAssociation(
    name="strings395",
    ends={
        Property(name="PrimaryOperand396", type=cobol_strings_ManipulatedStrings, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ManipulatedStrings", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
delimiter397: BinaryAssociation = BinaryAssociation(
    name="delimiter397",
    ends={
        Property(name="PrimaryOperand399", type=cobol_strings_ManipulatedStrings, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ManipulatedStrings398", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counter400: BinaryAssociation = BinaryAssociation(
    name="counter400",
    ends={
        Property(name="PrimaryOperand401", type=cobol_strings_SplittedString, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SplittedString", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base402: BinaryAssociation = BinaryAssociation(
    name="base402",
    ends={
        Property(name="PrimaryOperand403", type=cobol_strings_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_Location", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target404: BinaryAssociation = BinaryAssociation(
    name="target404",
    ends={
        Property(name="ReplacementOperand", type=cobol_strings_Replacement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_Replacement", type=ReplacementOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
occurrences405: BinaryAssociation = BinaryAssociation(
    name="occurrences405",
    ends={
        Property(name="Tallying406", type=cobol_strings_TallyingOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_TallyingOccurrence", type=Tallying, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
occurrences407: BinaryAssociation = BinaryAssociation(
    name="occurrences407",
    ends={
        Property(name="Replacement408", type=cobol_strings_ReplacementOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ReplacementOccurrence", type=Replacement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tallying409: BinaryAssociation = BinaryAssociation(
    name="tallying409",
    ends={
        Property(name="PrimaryOperand410", type=cobol_strings_SpecificCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SpecificCharacter", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source411: BinaryAssociation = BinaryAssociation(
    name="source411",
    ends={
        Property(name="ReplacementOperand412", type=cobol_strings_SpecificCharacterBySpecificCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SpecificCharacterBySpecificCharacter", type=ReplacementOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cobol_commons_NamedElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_NamedElement)
gen_cobol_commons_LabellableElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_LabellableElement)
gen_cobol_conditions_NegatedConditionalExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_NegatedConditionalExpressionChild)
gen_cobol_conditions_SimpleConditionChild_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_SimpleConditionChild)
gen_cobol_conditions_RelationalExpression_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_RelationalExpression)
gen_cobol_commons_URIableElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_URIableElement)
gen_cobol_conditions_ConditionalOrExpression_Condition = Generalization(general=Condition, specific=cobol_conditions_ConditionalOrExpression)
gen_cobol_conditions_ConditionalOrExpressionChild_Condition = Generalization(general=Condition, specific=cobol_conditions_ConditionalOrExpressionChild)
gen_cobol_conditions_NegatedConditionalExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_NegatedConditionalExpression)
gen_cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_AbbreviatedConditionalExpressionChild = Generalization(general=AbbreviatedConditionalExpressionChild, specific=cobol_conditions_NegatedAbbreviatedConditionalExpressionChild)
gen_cobol_conditions_AbbreviatedRelationalExpression_NegatedAbbreviatedConditionalExpressionChild = Generalization(general=NegatedAbbreviatedConditionalExpressionChild, specific=cobol_conditions_AbbreviatedRelationalExpression)
gen_cobol_conditions_NestedAbbreviatedConditionalExpression_AbbreviatedRelationalExpressionChild = Generalization(general=AbbreviatedRelationalExpressionChild, specific=cobol_conditions_NestedAbbreviatedConditionalExpression)
gen_cobol_conditions_SignCondition_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_SignCondition)
gen_cobol_conditions_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=cobol_conditions_ConditionalAndExpressionChild)
gen_cobol_conditions_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=cobol_conditions_ConditionalAndExpression)
gen_cobol_conditions_AbbreviatedConditionalExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_AbbreviatedConditionalExpression)
gen_cobol_conditions_AbbreviatedConditionalExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_AbbreviatedConditionalExpressionChild)
gen_cobol_conditions_NegatedAbbreviatedConditionalExpression_AbbreviatedConditionalExpressionChild = Generalization(general=AbbreviatedConditionalExpressionChild, specific=cobol_conditions_NegatedAbbreviatedConditionalExpression)
gen_cobol_conditions_NestedCondition_SimpleConditionChild = Generalization(general=SimpleConditionChild, specific=cobol_conditions_NestedCondition)
gen_cobol_arithmetics_AdditiveArithmeticExpression_RangeExpressionChild = Generalization(general=RangeExpressionChild, specific=cobol_arithmetics_AdditiveArithmeticExpression)
gen_cobol_arithmetics_AdditiveArithmeticExpressionChild_RangeExpressionChild = Generalization(general=RangeExpressionChild, specific=cobol_arithmetics_AdditiveArithmeticExpressionChild)
gen_cobol_arithmetics_MultiplicativeArithmeticExpression_AdditiveArithmeticExpressionChild = Generalization(general=AdditiveArithmeticExpressionChild, specific=cobol_arithmetics_MultiplicativeArithmeticExpression)
gen_cobol_arithmetics_MultiplicativeArithmeticExpressionChild_AdditiveArithmeticExpressionChild = Generalization(general=AdditiveArithmeticExpressionChild, specific=cobol_arithmetics_MultiplicativeArithmeticExpressionChild)
gen_cobol_arithmetics_PowerArithmeticExpression_MultiplicativeArithmeticExpressionChild = Generalization(general=MultiplicativeArithmeticExpressionChild, specific=cobol_arithmetics_PowerArithmeticExpression)
gen_cobol_conditions_ClassCondition_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_ClassCondition)
gen_cobol_conditions_AbbreviatedRelationalExpressionChild_NegatedAbbreviatedConditionalExpressionChild = Generalization(general=NegatedAbbreviatedConditionalExpressionChild, specific=cobol_conditions_AbbreviatedRelationalExpressionChild)
gen_cobol_arithmetics_RangeExpressionChild_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=cobol_arithmetics_RangeExpressionChild)
gen_cobol_arithmetics_NestedArithmeticExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cobol_arithmetics_NestedArithmeticExpression)
gen_cobol_arithmetics_ArithmeticExpression_conditions_AbbreviatedRelationalExpressionChild = Generalization(general=conditions_AbbreviatedRelationalExpressionChild, specific=cobol_arithmetics_ArithmeticExpression)
gen_cobol_arithmetics_ArithmeticExpression_conditions_SimpleConditionChild = Generalization(general=conditions_SimpleConditionChild, specific=cobol_arithmetics_ArithmeticExpression)
gen_cobol_containers_CompilationGroup_containers_CobolRoot = Generalization(general=containers_CobolRoot, specific=cobol_containers_CompilationGroup)
gen_cobol_containers_CompilationGroup_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_containers_CompilationGroup)
gen_cobol_containers_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=cobol_containers_CompilationUnit)
gen_cobol_arithmetics_PowerArithmeticExpressionChild_MultiplicativeArithmeticExpressionChild = Generalization(general=MultiplicativeArithmeticExpressionChild, specific=cobol_arithmetics_PowerArithmeticExpressionChild)
gen_cobol_arithmetics_UnaryArithmeticExpressionChild_PowerArithmeticExpressionChild = Generalization(general=PowerArithmeticExpressionChild, specific=cobol_arithmetics_UnaryArithmeticExpressionChild)
gen_cobol_arithmetics_UnaryArithmeticExpression_PowerArithmeticExpressionChild = Generalization(general=PowerArithmeticExpressionChild, specific=cobol_arithmetics_UnaryArithmeticExpression)
gen_cobol_arithmetics_PrimaryExpression_UnaryArithmeticExpressionChild = Generalization(general=UnaryArithmeticExpressionChild, specific=cobol_arithmetics_PrimaryExpression)
gen_cobol_arithmetics_RangeExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=cobol_arithmetics_RangeExpression)
gen_cobol_divisions_EnvironmentDivision_Division = Generalization(general=Division, specific=cobol_divisions_EnvironmentDivision)
gen_cobol_divisions_IdentificationDivision_divisions_Division = Generalization(general=divisions_Division, specific=cobol_divisions_IdentificationDivision)
gen_cobol_divisions_IdentificationDivision_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_divisions_IdentificationDivision)
gen_cobol_divisions_ProcedureDivision_divisions_Division = Generalization(general=divisions_Division, specific=cobol_divisions_ProcedureDivision)
gen_cobol_divisions_ProcedureDivision_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=cobol_divisions_ProcedureDivision)
gen_cobol_literals_Literal_water_SelectStatementWater = Generalization(general=water_SelectStatementWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_SpecialNamesParagraphWater = Generalization(general=water_SpecialNamesParagraphWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_CICSStatementWater = Generalization(general=water_CICSStatementWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_operands_PrimaryOperand = Generalization(general=operands_PrimaryOperand, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_InvokeStatementWater = Generalization(general=water_InvokeStatementWater, specific=cobol_literals_Literal)
gen_cobol_containers_EmptyModel_CobolRoot = Generalization(general=CobolRoot, specific=cobol_containers_EmptyModel)
gen_cobol_divisions_Division_NamedElement = Generalization(general=NamedElement, specific=cobol_divisions_Division)
gen_cobol_divisions_DataDivision_Division = Generalization(general=Division, specific=cobol_divisions_DataDivision)
gen_cobol_literals_AlphanumericLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_AlphanumericLiteral)
gen_cobol_literals_IntegerLiteral_literals_NumericLiteral = Generalization(general=literals_NumericLiteral, specific=cobol_literals_IntegerLiteral)
gen_cobol_literals_IntegerLiteral_water_ObjectComputerParagraphWater = Generalization(general=water_ObjectComputerParagraphWater, specific=cobol_literals_IntegerLiteral)
gen_cobol_literals_IntegerLiteral_water_FileDescriptorWater = Generalization(general=water_FileDescriptorWater, specific=cobol_literals_IntegerLiteral)
gen_cobol_literals_IntegerLiteral_water_IOControlParagraphWater = Generalization(general=water_IOControlParagraphWater, specific=cobol_literals_IntegerLiteral)
gen_cobol_literals_DecimalLiteral_NumericLiteral = Generalization(general=NumericLiteral, specific=cobol_literals_DecimalLiteral)
gen_cobol_literals_FigurativeConstantLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_FigurativeConstantLiteral)
gen_cobol_literals_BooleanLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_BooleanLiteral)
gen_cobol_literals_FloatingDecimalLiteral_DecimalLiteral = Generalization(general=DecimalLiteral, specific=cobol_literals_FloatingDecimalLiteral)
gen_cobol_literals_AllLiteral_FigurativeConstantLiteral = Generalization(general=FigurativeConstantLiteral, specific=cobol_literals_AllLiteral)
gen_cobol_literals_NumericLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_NumericLiteral)
gen_cobol_literals_ConstantLiteral_FigurativeConstantLiteral = Generalization(general=FigurativeConstantLiteral, specific=cobol_literals_ConstantLiteral)
gen_cobol_literals_Literal_labels_StopLabel = Generalization(general=labels_StopLabel, specific=cobol_literals_Literal)
gen_cobol_literals_Space_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_Space)
gen_cobol_literals_Any_Literal = Generalization(general=Literal, specific=cobol_literals_Any)
gen_cobol_literals_Characters_Literal = Generalization(general=Literal, specific=cobol_literals_Characters)
gen_cobol_literals_PseudoLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_PseudoLiteral)
gen_cobol_literals_DBCSLiteral_Literal = Generalization(general=Literal, specific=cobol_literals_DBCSLiteral)
gen_cobol_literals_NationalLiteral_DBCSLiteral = Generalization(general=DBCSLiteral, specific=cobol_literals_NationalLiteral)
gen_cobol_literals_FixedDecimalLiteral_DecimalLiteral = Generalization(general=DecimalLiteral, specific=cobol_literals_FixedDecimalLiteral)
gen_cobol_literals_NationalHexLiteral_DBCSLiteral = Generalization(general=DBCSLiteral, specific=cobol_literals_NationalHexLiteral)
gen_cobol_literals_Null_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_Null)
gen_cobol_literals_Zero_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_Zero)
gen_cobol_literals_Quote_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_Quote)
gen_cobol_literals_LowValue_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_LowValue)
gen_cobol_literals_HighValue_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_HighValue)
gen_cobol_operators_Subtraction_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=cobol_operators_Subtraction)
gen_cobol_operators_Subtraction_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=cobol_operators_Subtraction)
gen_cobol_operators_GreaterThanOrEqual_RelationalOperator = Generalization(general=RelationalOperator, specific=cobol_operators_GreaterThanOrEqual)
gen_cobol_operators_GreaterThan_RelationalOperator = Generalization(general=RelationalOperator, specific=cobol_operators_GreaterThan)
gen_cobol_operators_LessThan_RelationalOperator = Generalization(general=RelationalOperator, specific=cobol_operators_LessThan)
gen_cobol_operators_LessThanOrEqual_RelationalOperator = Generalization(general=RelationalOperator, specific=cobol_operators_LessThanOrEqual)
gen_cobol_operators_Equal_RelationalOperator = Generalization(general=RelationalOperator, specific=cobol_operators_Equal)
gen_cobol_operators_Power_Operator = Generalization(general=Operator, specific=cobol_operators_Power)
gen_cobol_operators_Negate_Operator = Generalization(general=Operator, specific=cobol_operators_Negate)
gen_cobol_operators_Through_Operator = Generalization(general=Operator, specific=cobol_operators_Through)
gen_cobol_operators_ClassOperator_Operator = Generalization(general=Operator, specific=cobol_operators_ClassOperator)
gen_cobol_literals_AlphanumericHexaDecimalLiteral_AlphanumericLiteral = Generalization(general=AlphanumericLiteral, specific=cobol_literals_AlphanumericHexaDecimalLiteral)
gen_cobol_operators_AdditiveOperator_Operator = Generalization(general=Operator, specific=cobol_operators_AdditiveOperator)
gen_cobol_operators_MultiplicativeOperator_Operator = Generalization(general=Operator, specific=cobol_operators_MultiplicativeOperator)
gen_cobol_operators_UnaryOperator_Operator = Generalization(general=Operator, specific=cobol_operators_UnaryOperator)
gen_cobol_operators_LogicalOperator_Operator = Generalization(general=Operator, specific=cobol_operators_LogicalOperator)
gen_cobol_operators_RelationalOperator_Operator = Generalization(general=Operator, specific=cobol_operators_RelationalOperator)
gen_cobol_operators_ConditionOr_LogicalOperator = Generalization(general=LogicalOperator, specific=cobol_operators_ConditionOr)
gen_cobol_operators_ConditionAnd_LogicalOperator = Generalization(general=LogicalOperator, specific=cobol_operators_ConditionAnd)
gen_cobol_operators_Multiplication_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=cobol_operators_Multiplication)
gen_cobol_operators_SignOperator_Operator = Generalization(general=Operator, specific=cobol_operators_SignOperator)
gen_cobol_operators_Positive_SignOperator = Generalization(general=SignOperator, specific=cobol_operators_Positive)
gen_cobol_operators_Negative_SignOperator = Generalization(general=SignOperator, specific=cobol_operators_Negative)
gen_cobol_operators_Division_MultiplicativeOperator = Generalization(general=MultiplicativeOperator, specific=cobol_operators_Division)
gen_cobol_operators_Addition_operators_AdditiveOperator = Generalization(general=operators_AdditiveOperator, specific=cobol_operators_Addition)
gen_cobol_operators_Addition_operators_UnaryOperator = Generalization(general=operators_UnaryOperator, specific=cobol_operators_Addition)
gen_cobol_operators_GTSign_GreaterThan = Generalization(general=GreaterThan, specific=cobol_operators_GTSign)
gen_cobol_operators_GTEQPhrase_GreaterThanOrEqual = Generalization(general=GreaterThanOrEqual, specific=cobol_operators_GTEQPhrase)
gen_cobol_operators_GTEQSign_GreaterThanOrEqual = Generalization(general=GreaterThanOrEqual, specific=cobol_operators_GTEQSign)
gen_cobol_paragraphs_Paragraph_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_paragraphs_Paragraph)
gen_cobol_paragraphs_Paragraph_labels_Procedure = Generalization(general=labels_Procedure, specific=cobol_paragraphs_Paragraph)
gen_cobol_paragraphs_SourceComputerParagraph_ConfigurationSectionParagraph = Generalization(general=ConfigurationSectionParagraph, specific=cobol_paragraphs_SourceComputerParagraph)
gen_cobol_paragraphs_ObjectComputerParagraph_paragraphs_ConfigurationSectionParagraph = Generalization(general=paragraphs_ConfigurationSectionParagraph, specific=cobol_paragraphs_ObjectComputerParagraph)
gen_cobol_paragraphs_ObjectComputerParagraph_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_paragraphs_ObjectComputerParagraph)
gen_cobol_paragraphs_FileControlParagraph_IOSectionParagraph = Generalization(general=IOSectionParagraph, specific=cobol_paragraphs_FileControlParagraph)
gen_cobol_paragraphs_IOControlParagraph_paragraphs_IOSectionParagraph = Generalization(general=paragraphs_IOSectionParagraph, specific=cobol_paragraphs_IOControlParagraph)
gen_cobol_paragraphs_IOControlParagraph_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_paragraphs_IOControlParagraph)
gen_cobol_operators_Zero_SignOperator = Generalization(general=SignOperator, specific=cobol_operators_Zero)
gen_cobol_operators_ClassName_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_ClassName)
gen_cobol_operators_Alphabetic_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_Alphabetic)
gen_cobol_operators_DBCS_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_DBCS)
gen_cobol_operators_Numeric_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_Numeric)
gen_cobol_operators_AlphabeticUpper_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_AlphabeticUpper)
gen_cobol_operators_AlphabeticLower_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_AlphabeticLower)
gen_cobol_operators_Kanji_ClassOperator = Generalization(general=ClassOperator, specific=cobol_operators_Kanji)
gen_cobol_operators_EqualPhrase_Equal = Generalization(general=Equal, specific=cobol_operators_EqualPhrase)
gen_cobol_operators_EqualSign_Equal = Generalization(general=Equal, specific=cobol_operators_EqualSign)
gen_cobol_operators_LTPhrase_LessThan = Generalization(general=LessThan, specific=cobol_operators_LTPhrase)
gen_cobol_operators_LTSign_LessThan = Generalization(general=LessThan, specific=cobol_operators_LTSign)
gen_cobol_operators_LTEQPhrase_LessThanOrEqual = Generalization(general=LessThanOrEqual, specific=cobol_operators_LTEQPhrase)
gen_cobol_operators_LTEQSign_LessThanOrEqual = Generalization(general=LessThanOrEqual, specific=cobol_operators_LTEQSign)
gen_cobol_operators_GTPhrase_GreaterThan = Generalization(general=GreaterThan, specific=cobol_operators_GTPhrase)
gen_cobol_references_SpecialNamesConditionNameReference_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_references_SpecialNamesConditionNameReference)
gen_cobol_references_SpecialNamesConditionNameReference_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_references_SpecialNamesConditionNameReference)
gen_cobol_references_SpecialNamesConditionNameReference_references_ConditionName = Generalization(general=references_ConditionName, specific=cobol_references_SpecialNamesConditionNameReference)
gen_cobol_references_FileNameReference_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_references_FileNameReference)
gen_cobol_references_FileNameReference_references_IdentifierReferenceQualifier = Generalization(general=references_IdentifierReferenceQualifier, specific=cobol_references_FileNameReference)
gen_cobol_references_IndexNameReference_IdentifierReference = Generalization(general=IdentifierReference, specific=cobol_references_IndexNameReference)
gen_cobol_references_MnemonicNameReference_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_references_MnemonicNameReference)
gen_cobol_references_MnemonicNameReference_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_references_MnemonicNameReference)
gen_cobol_references_AlphabetNameReference_ElementReference = Generalization(general=ElementReference, specific=cobol_references_AlphabetNameReference)
gen_cobol_references_ConditionNameReference_identifiers_IdentifierReference = Generalization(general=identifiers_IdentifierReference, specific=cobol_references_ConditionNameReference)
gen_cobol_references_ConditionNameReference_references_ConditionName = Generalization(general=references_ConditionName, specific=cobol_references_ConditionNameReference)
gen_cobol_references_DataNameReference_identifiers_IdentifierReference = Generalization(general=identifiers_IdentifierReference, specific=cobol_references_DataNameReference)
gen_cobol_references_DataNameReference_references_IdentifierReferenceQualifier = Generalization(general=references_IdentifierReferenceQualifier, specific=cobol_references_DataNameReference)
gen_cobol_references_IdentifierReferenceQualifier_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_references_IdentifierReferenceQualifier)
gen_cobol_references_IdentifierReferenceQualifier_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_references_IdentifierReferenceQualifier)
gen_cobol_sections_Section_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_sections_Section)
gen_cobol_sections_Section_labels_Procedure = Generalization(general=labels_Procedure, specific=cobol_sections_Section)
gen_cobol_paragraphs_ConfigurationSectionParagraph_Paragraph = Generalization(general=Paragraph, specific=cobol_paragraphs_ConfigurationSectionParagraph)
gen_cobol_paragraphs_IOSectionParagraph_Paragraph = Generalization(general=Paragraph, specific=cobol_paragraphs_IOSectionParagraph)
gen_cobol_paragraphs_SpecialNamesParagraph_ConfigurationSectionParagraph = Generalization(general=ConfigurationSectionParagraph, specific=cobol_paragraphs_SpecialNamesParagraph)
gen_cobol_paragraphs_RepositoryParagraph_paragraphs_ConfigurationSectionParagraph = Generalization(general=paragraphs_ConfigurationSectionParagraph, specific=cobol_paragraphs_RepositoryParagraph)
gen_cobol_paragraphs_RepositoryParagraph_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_paragraphs_RepositoryParagraph)
gen_cobol_references_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=cobol_references_ReferenceableElement)
gen_cobol_references_ElementReference_Reference = Generalization(general=Reference, specific=cobol_references_ElementReference)
gen_cobol_sections_DeclarativeSection_Section = Generalization(general=Section, specific=cobol_sections_DeclarativeSection)
gen_cobol_sentences_EmptySentence_Sentence = Generalization(general=Sentence, specific=cobol_sentences_EmptySentence)
gen_cobol_sentences_UseSentence_sentences_StatementContainer = Generalization(general=sentences_StatementContainer, specific=cobol_sentences_UseSentence)
gen_cobol_sentences_UseSentence_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_sentences_UseSentence)
gen_cobol_sentences_AlteredGoTo_Sentence = Generalization(general=Sentence, specific=cobol_sentences_AlteredGoTo)
gen_cobol_sentences_ExitProcedure_Sentence = Generalization(general=Sentence, specific=cobol_sentences_ExitProcedure)
gen_cobol_sentences_EntrySentence_Sentence = Generalization(general=Sentence, specific=cobol_sentences_EntrySentence)
gen_cobol_sentences_ExecuteSentence_StatementContainer = Generalization(general=StatementContainer, specific=cobol_sentences_ExecuteSentence)
gen_cobol_sentences_Sentence_StatementContainer = Generalization(general=StatementContainer, specific=cobol_sentences_Sentence)
gen_cobol_operands_PrimaryOperand_operands_ReplacementOperand = Generalization(general=operands_ReplacementOperand, specific=cobol_operands_PrimaryOperand)
gen_cobol_operands_PrimaryOperand_operands_Operand = Generalization(general=operands_Operand, specific=cobol_operands_PrimaryOperand)
gen_cobol_operands_PrimaryOperand_arithmetics_PrimaryExpression = Generalization(general=arithmetics_PrimaryExpression, specific=cobol_operands_PrimaryOperand)
gen_cobol_operands_PrimaryOperand_operands_ArithmeticOperand = Generalization(general=operands_ArithmeticOperand, specific=cobol_operands_PrimaryOperand)
gen_cobol_sections_WorkingStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_WorkingStorageSection)
gen_cobol_sections_LocalStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_LocalStorageSection)
gen_cobol_operands_RoundedIdentifier_ArithmeticOperand = Generalization(general=ArithmeticOperand, specific=cobol_operands_RoundedIdentifier)
gen_cobol_sections_LinkageStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_LinkageStorageSection)
gen_cobol_sections_IOSection_EnvironmentDivisionSection = Generalization(general=EnvironmentDivisionSection, specific=cobol_sections_IOSection)
gen_cobol_sections_ConfigurationSection_EnvironmentDivisionSection = Generalization(general=EnvironmentDivisionSection, specific=cobol_sections_ConfigurationSection)
gen_cobol_sections_EnvironmentDivisionSection_Section = Generalization(general=Section, specific=cobol_sections_EnvironmentDivisionSection)
gen_cobol_sections_DataDivisionSection_Section = Generalization(general=Section, specific=cobol_sections_DataDivisionSection)
gen_cobol_sections_FileSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_FileSection)
gen_cobol_statements_ArithmeticStatement_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_ArithmeticStatement)
gen_cobol_statements_ArithmeticStatement_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_ArithmeticStatement)
gen_cobol_statements_Add_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Add)
gen_cobol_statements_Subtract_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Subtract)
gen_cobol_statements_Multiply_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Multiply)
gen_cobol_statements_Divide_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Divide)
gen_cobol_statements_Perform_Statement = Generalization(general=Statement, specific=cobol_statements_Perform)
gen_cobol_statements_PerformNestedStatement_statements_Perform = Generalization(general=statements_Perform, specific=cobol_statements_PerformNestedStatement)
gen_cobol_statements_PerformNestedStatement_statements_NestedStatement = Generalization(general=statements_NestedStatement, specific=cobol_statements_PerformNestedStatement)
gen_cobol_operands_ReplacementOperand_Operand = Generalization(general=Operand, specific=cobol_operands_ReplacementOperand)
gen_cobol_operands_Encoding_ReplacementOperand = Generalization(general=ReplacementOperand, specific=cobol_operands_Encoding)
gen_cobol_operands_ArithmeticOperand_Operand = Generalization(general=Operand, specific=cobol_operands_ArithmeticOperand)
gen_cobol_statements_Exit_Statement = Generalization(general=Statement, specific=cobol_statements_Exit)
gen_cobol_statements_Condition_statements_NestedStatement = Generalization(general=statements_NestedStatement, specific=cobol_statements_Condition)
gen_cobol_statements_Condition_statements_Conditional = Generalization(general=statements_Conditional, specific=cobol_statements_Condition)
gen_cobol_statements_Condition_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Condition)
gen_cobol_statements_Stop_Statement = Generalization(general=Statement, specific=cobol_statements_Stop)
gen_cobol_statements_Display_Statement = Generalization(general=Statement, specific=cobol_statements_Display)
gen_cobol_statements_Compute_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Compute)
gen_cobol_statements_Compute_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Compute)
gen_cobol_statements_Accept_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Accept)
gen_cobol_statements_Accept_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Accept)
gen_cobol_statements_PerformProcedure_Perform = Generalization(general=Perform, specific=cobol_statements_PerformProcedure)
gen_cobol_statements_Jump_Statement = Generalization(general=Statement, specific=cobol_statements_Jump)
gen_cobol_statements_NextSentence_Jump = Generalization(general=Jump, specific=cobol_statements_NextSentence)
gen_cobol_statements_GoTo_Jump = Generalization(general=Jump, specific=cobol_statements_GoTo)
gen_cobol_statements_GoBack_Jump = Generalization(general=Jump, specific=cobol_statements_GoBack)
gen_cobol_statements_Move_Statement = Generalization(general=Statement, specific=cobol_statements_Move)
gen_cobol_statements_SetIndexName_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_SetIndexName)
gen_cobol_statements_String_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_String)
gen_cobol_statements_String_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_String)
gen_cobol_statements_Close_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Close)
gen_cobol_statements_Close_statements_IOStatement = Generalization(general=statements_IOStatement, specific=cobol_statements_Close)
gen_cobol_statements_Cancel_Statement = Generalization(general=Statement, specific=cobol_statements_Cancel)
gen_cobol_statements_Call_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Call)
gen_cobol_statements_Call_functions_Argumentable = Generalization(general=functions_Argumentable, specific=cobol_statements_Call)
gen_cobol_statements_Call_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Call)
gen_cobol_statements_Execute_Statement = Generalization(general=Statement, specific=cobol_statements_Execute)
gen_cobol_statements_Return_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Return)
gen_cobol_statements_Return_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Return)
gen_cobol_statements_SetStatement_Statement = Generalization(general=Statement, specific=cobol_statements_SetStatement)
gen_cobol_statements_SetSwitches_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_SetSwitches)
gen_cobol_statements_Evaluate_Statement = Generalization(general=Statement, specific=cobol_statements_Evaluate)
gen_cobol_statements_NormalEvaluateCase_EvaluateCase = Generalization(general=EvaluateCase, specific=cobol_statements_NormalEvaluateCase)
gen_cobol_statements_OtherEvaluateCase_EvaluateCase = Generalization(general=EvaluateCase, specific=cobol_statements_OtherEvaluateCase)
gen_cobol_statements_EvaluateCase_NestedStatement = Generalization(general=NestedStatement, specific=cobol_statements_EvaluateCase)
gen_cobol_statements_Replace_Statement = Generalization(general=Statement, specific=cobol_statements_Replace)
gen_cobol_statements_Entry_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=cobol_statements_Entry)
gen_cobol_statements_Entry_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Entry)
gen_cobol_statements_Inspect_Statement = Generalization(general=Statement, specific=cobol_statements_Inspect)
gen_cobol_statements_Initialize_Statement = Generalization(general=Statement, specific=cobol_statements_Initialize)
gen_cobol_statements_Open_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Open)
gen_cobol_statements_Open_statements_IOStatement = Generalization(general=statements_IOStatement, specific=cobol_statements_Open)
gen_cobol_statements_SearchStatement_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_SearchStatement)
gen_cobol_statements_SearchStatement_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_SearchStatement)
gen_cobol_statements_SerialSearch_SearchStatement = Generalization(general=SearchStatement, specific=cobol_statements_SerialSearch)
gen_cobol_statements_BinarySearch_SearchStatement = Generalization(general=SearchStatement, specific=cobol_statements_BinarySearch)
gen_cobol_statements_Unstring_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Unstring)
gen_cobol_statements_Unstring_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Unstring)
gen_cobol_statements_Write_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Write)
gen_cobol_statements_Write_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Write)
gen_cobol_statements_Rewrite_Write = Generalization(general=Write, specific=cobol_statements_Rewrite)
gen_cobol_statements_Set_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_Set)
gen_cobol_statements_Read_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Read)
gen_cobol_statements_Read_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Read)
gen_cobol_statements_PerformFixedTimes_Perform = Generalization(general=Perform, specific=cobol_statements_PerformFixedTimes)
gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformUntilCondition = Generalization(general=statements_PerformUntilCondition, specific=cobol_statements_PerformProcedureUntilCondition)
gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformProcedure = Generalization(general=statements_PerformProcedure, specific=cobol_statements_PerformProcedureUntilCondition)
gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformNestedStatement = Generalization(general=statements_PerformNestedStatement, specific=cobol_statements_PerformNestedStatementFixedTimes)
gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformFixedTimes = Generalization(general=statements_PerformFixedTimes, specific=cobol_statements_PerformNestedStatementFixedTimes)
gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformUntilCondition = Generalization(general=statements_PerformUntilCondition, specific=cobol_statements_PerformNestedStatementUntilCondition)
gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformNestedStatement = Generalization(general=statements_PerformNestedStatement, specific=cobol_statements_PerformNestedStatementUntilCondition)
gen_cobol_statements_Continue_Jump = Generalization(general=Jump, specific=cobol_statements_Continue)
gen_cobol_statements_FileIOStatement_Statement = Generalization(general=Statement, specific=cobol_statements_FileIOStatement)
gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformProcedure = Generalization(general=statements_PerformProcedure, specific=cobol_statements_PerformProcedureFixedTimes)
gen_cobol_statements_Sort_statements_FileIOStatement = Generalization(general=statements_FileIOStatement, specific=cobol_statements_Sort)
gen_cobol_statements_Sort_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Sort)
gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformFixedTimes = Generalization(general=statements_PerformFixedTimes, specific=cobol_statements_PerformProcedureFixedTimes)
gen_cobol_statements_Merge_statements_FileIOStatement = Generalization(general=statements_FileIOStatement, specific=cobol_statements_Merge)
gen_cobol_statements_Merge_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Merge)
gen_cobol_statements_Release_Statement = Generalization(general=Statement, specific=cobol_statements_Release)
gen_cobol_statements_PerformUntilCondition_statements_Perform = Generalization(general=statements_Perform, specific=cobol_statements_PerformUntilCondition)
gen_cobol_statements_PerformUntilCondition_statements_VaryingUntilCondition = Generalization(general=statements_VaryingUntilCondition, specific=cobol_statements_PerformUntilCondition)
gen_cobol_statements_IOStatement_Statement = Generalization(general=Statement, specific=cobol_statements_IOStatement)
gen_cobol_statements_IOFile_IncompleteElement = Generalization(general=IncompleteElement, specific=cobol_statements_IOFile)
gen_cobol_statements_VaryingUntilCondition_Conditional = Generalization(general=Conditional, specific=cobol_statements_VaryingUntilCondition)
gen_cobol_statements_AfterUntilCondition_VaryingUntilCondition = Generalization(general=VaryingUntilCondition, specific=cobol_statements_AfterUntilCondition)
gen_cobol_statements_Start_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Start)
gen_cobol_statements_Start_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Start)
gen_cobol_statements_Delete_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Delete)
gen_cobol_statements_Delete_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Delete)
gen_cobol_identifiers_Identifier_operands_PrimaryOperand = Generalization(general=operands_PrimaryOperand, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_AcceptStatementWater = Generalization(general=water_AcceptStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_CICSStatementWater = Generalization(general=water_CICSStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SpecialNamesParagraphWater = Generalization(general=water_SpecialNamesParagraphWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_ObjectComputerParagraphWater = Generalization(general=water_ObjectComputerParagraphWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_RepositoryParagraphWater = Generalization(general=water_RepositoryParagraphWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_IOControlParagraphWater = Generalization(general=water_IOControlParagraphWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_IdentificationDivisionWater = Generalization(general=water_IdentificationDivisionWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_InvokeStatementWater = Generalization(general=water_InvokeStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SQLStatementWater = Generalization(general=water_SQLStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_UseStatementWater = Generalization(general=water_UseStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_FileDescriptorWater = Generalization(general=water_FileDescriptorWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_DataDescriptorWater = Generalization(general=water_DataDescriptorWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SelectStatementWater = Generalization(general=water_SelectStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SortPhraseWater = Generalization(general=water_SortPhraseWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_IdentifierReference_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_identifiers_IdentifierReference)
gen_cobol_identifiers_IdentifierReference_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_identifiers_IdentifierReference)
gen_cobol_identifiers_IdentifierReference_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_identifiers_IdentifierReference)
gen_cobol_water_ProgramDescription_IdentificationDivisionWater = Generalization(general=IdentificationDivisionWater, specific=cobol_water_ProgramDescription)
gen_cobol_identifiers_All_DirectSubscript = Generalization(general=DirectSubscript, specific=cobol_identifiers_All)
gen_cobol_identifiers_LinageCounter_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_identifiers_LinageCounter)
gen_cobol_identifiers_LinageCounter_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_identifiers_LinageCounter)
gen_cobol_identifiers_Qualifier_ElementReference = Generalization(general=ElementReference, specific=cobol_identifiers_Qualifier)
gen_cobol_identifiers_RelativeSubscript_Subscript = Generalization(general=Subscript, specific=cobol_identifiers_RelativeSubscript)
gen_cobol_identifiers_DirectSubscript_Subscript = Generalization(general=Subscript, specific=cobol_identifiers_DirectSubscript)
gen_cobol_ios_InputProcedure_ios_InputDirective = Generalization(general=ios_InputDirective, specific=cobol_ios_InputProcedure)
gen_cobol_ios_InputProcedure_ios_ProcedureDirective = Generalization(general=ios_ProcedureDirective, specific=cobol_ios_InputProcedure)
gen_cobol_ios_InputDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_InputDirective)
gen_cobol_ios_InputFile_ios_InputDirective = Generalization(general=ios_InputDirective, specific=cobol_ios_InputFile)
gen_cobol_ios_InputFile_ios_FileDirective = Generalization(general=ios_FileDirective, specific=cobol_ios_InputFile)
gen_cobol_ios_OutputDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_OutputDirective)
gen_cobol_ios_OutputProcedure_ios_ProcedureDirective = Generalization(general=ios_ProcedureDirective, specific=cobol_ios_OutputProcedure)
gen_cobol_ios_OutputProcedure_ios_OutputDirective = Generalization(general=ios_OutputDirective, specific=cobol_ios_OutputProcedure)
gen_cobol_ios_OutputFile_ios_OutputDirective = Generalization(general=ios_OutputDirective, specific=cobol_ios_OutputFile)
gen_cobol_ios_OutputFile_ios_FileDirective = Generalization(general=ios_FileDirective, specific=cobol_ios_OutputFile)
gen_cobol_ios_FileDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_FileDirective)
gen_cobol_ios_ProcedureDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_ProcedureDirective)
gen_cobol_water_IdentificationDivisionWater_Water = Generalization(general=Water, specific=cobol_water_IdentificationDivisionWater)
gen_cobol_water_SpecialNamesParagraphWater_Water = Generalization(general=Water, specific=cobol_water_SpecialNamesParagraphWater)
gen_cobol_water_SpecialNamesClause_SpecialNamesParagraphWater = Generalization(general=SpecialNamesParagraphWater, specific=cobol_water_SpecialNamesClause)
gen_cobol_water_Dot_water_IdentificationDivisionWater = Generalization(general=water_IdentificationDivisionWater, specific=cobol_water_Dot)
gen_cobol_water_Dot_water_SQLStatementWater = Generalization(general=water_SQLStatementWater, specific=cobol_water_Dot)
gen_cobol_water_ObjectComputerParagraphWater_Water = Generalization(general=Water, specific=cobol_water_ObjectComputerParagraphWater)
gen_cobol_water_ObjectComputerDescription_ObjectComputerParagraphWater = Generalization(general=ObjectComputerParagraphWater, specific=cobol_water_ObjectComputerDescription)
gen_cobol_water_PriorityNumber_ObjectComputerParagraphWater = Generalization(general=ObjectComputerParagraphWater, specific=cobol_water_PriorityNumber)
gen_cobol_water_SelectStatementWater_Water = Generalization(general=Water, specific=cobol_water_SelectStatementWater)
gen_cobol_water_SelectStatementClause_SelectStatementWater = Generalization(general=SelectStatementWater, specific=cobol_water_SelectStatementClause)
gen_cobol_water_FileDescriptorWater_Water = Generalization(general=Water, specific=cobol_water_FileDescriptorWater)
gen_cobol_water_FileDescription_FileDescriptorWater = Generalization(general=FileDescriptorWater, specific=cobol_water_FileDescription)
gen_cobol_water_DataDescriptorWater_Water = Generalization(general=Water, specific=cobol_water_DataDescriptorWater)
gen_cobol_water_DataDescription_DataDescriptorWater = Generalization(general=DataDescriptorWater, specific=cobol_water_DataDescription)
gen_cobol_water_IOControlParagraphWater_Water = Generalization(general=Water, specific=cobol_water_IOControlParagraphWater)
gen_cobol_water_IOControlDescription_IOControlParagraphWater = Generalization(general=IOControlParagraphWater, specific=cobol_water_IOControlDescription)
gen_cobol_water_RepositoryParagraphWater_Water = Generalization(general=Water, specific=cobol_water_RepositoryParagraphWater)
gen_cobol_water_RepositoryDescription_RepositoryParagraphWater = Generalization(general=RepositoryParagraphWater, specific=cobol_water_RepositoryDescription)
gen_cobol_water_SQLStatementWater_Water = Generalization(general=Water, specific=cobol_water_SQLStatementWater)
gen_cobol_water_CICSStatementWater_Water = Generalization(general=Water, specific=cobol_water_CICSStatementWater)
gen_cobol_water_SQLStatementToken_SQLStatementWater = Generalization(general=SQLStatementWater, specific=cobol_water_SQLStatementToken)
gen_cobol_water_CICSStatementToken_CICSStatementWater = Generalization(general=CICSStatementWater, specific=cobol_water_CICSStatementToken)
gen_cobol_water_AcceptStatementWater_Water = Generalization(general=Water, specific=cobol_water_AcceptStatementWater)
gen_cobol_water_AcceptStatementToken_AcceptStatementWater = Generalization(general=AcceptStatementWater, specific=cobol_water_AcceptStatementToken)
gen_cobol_water_UseStatementWater_Water = Generalization(general=Water, specific=cobol_water_UseStatementWater)
gen_cobol_water_UseStatementToken_UseStatementWater = Generalization(general=UseStatementWater, specific=cobol_water_UseStatementToken)
gen_cobol_water_CloseStatementWater_Water = Generalization(general=Water, specific=cobol_water_CloseStatementWater)
gen_cobol_water_CloseStatementToken_CloseStatementWater = Generalization(general=CloseStatementWater, specific=cobol_water_CloseStatementToken)
gen_cobol_environments_UPSI_Environment = Generalization(general=Environment, specific=cobol_environments_UPSI)
gen_cobol_water_InvokeStatementWater_Water = Generalization(general=Water, specific=cobol_water_InvokeStatementWater)
gen_cobol_water_InvokeStatementToken_InvokeStatementWater = Generalization(general=InvokeStatementWater, specific=cobol_water_InvokeStatementToken)
gen_cobol_water_OpenStatementWater_Water = Generalization(general=Water, specific=cobol_water_OpenStatementWater)
gen_cobol_water_OpenStatementToken_OpenStatementWater = Generalization(general=OpenStatementWater, specific=cobol_water_OpenStatementToken)
gen_cobol_water_SortPhraseToken_SortPhraseWater = Generalization(general=SortPhraseWater, specific=cobol_water_SortPhraseToken)
gen_cobol_water_SortPhraseWater_Water = Generalization(general=Water, specific=cobol_water_SortPhraseWater)
gen_cobol_registers_Register_PrimaryOperand = Generalization(general=PrimaryOperand, specific=cobol_registers_Register)
gen_cobol_registers_ShiftIn_Register = Generalization(general=Register, specific=cobol_registers_ShiftIn)
gen_cobol_registers_ShiftOut_Register = Generalization(general=Register, specific=cobol_registers_ShiftOut)
gen_cobol_registers_AddressOf_Register = Generalization(general=Register, specific=cobol_registers_AddressOf)
gen_cobol_registers_LengthOf_Register = Generalization(general=Register, specific=cobol_registers_LengthOf)
gen_cobol_registers_ReturnCode_Register = Generalization(general=Register, specific=cobol_registers_ReturnCode)
gen_cobol_registers_WhenCompiled_Register = Generalization(general=Register, specific=cobol_registers_WhenCompiled)
gen_cobol_environments_SystemDevice_Environment = Generalization(general=Environment, specific=cobol_environments_SystemDevice)
gen_cobol_environments_SystemLogicalInput_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SystemLogicalInput)
gen_cobol_environments_SystemLogicalOutput_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SystemLogicalOutput)
gen_cobol_environments_SystemPunchDevice_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SystemPunchDevice)
gen_cobol_environments_Console_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Console)
gen_cobol_environments_Channel_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Channel)
gen_cobol_environments_AdvancedFunctionPrinting_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_AdvancedFunctionPrinting)
gen_cobol_environments_SuppressSpacing_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SuppressSpacing)
gen_cobol_environments_Pocket_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Pocket)
gen_cobol_environments_Environment_AcceptStatementWater = Generalization(general=AcceptStatementWater, specific=cobol_environments_Environment)
gen_cobol_dataitems_PictureString_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_PictureString)
gen_cobol_dataitems_RenamingDataName_DataName = Generalization(general=DataName, specific=cobol_dataitems_RenamingDataName)
gen_cobol_dataitems_ConditionName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_ConditionName)
gen_cobol_dataitems_Global_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Global)
gen_cobol_dataitems_External_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_External)
gen_cobol_dataitems_Value_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Value)
gen_cobol_dataitems_Usage_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Usage)
gen_cobol_dataitems_GroupUsage_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_GroupUsage)
gen_cobol_dataitems_DataItem_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_dataitems_DataItem)
gen_cobol_dataitems_DataItem_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_dataitems_DataItem)
gen_cobol_specialnames_ExplicitAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_ExplicitAlphabetType)
gen_cobol_dataitems_RecordName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_RecordName)
gen_cobol_dataitems_DataName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_DataName)
gen_cobol_dataitems_Redefines_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Redefines)
gen_cobol_specialnames_SpecialName_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_specialnames_SpecialName)
gen_cobol_specialnames_ConditionName_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_specialnames_ConditionName)
gen_cobol_specialnames_ConditionName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_ConditionName)
gen_cobol_specialnames_OnStatus_ConditionName = Generalization(general=ConditionName, specific=cobol_specialnames_OnStatus)
gen_cobol_specialnames_OffStatus_ConditionName = Generalization(general=ConditionName, specific=cobol_specialnames_OffStatus)
gen_cobol_specialnames_AlphabetName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_AlphabetName)
gen_cobol_specialnames_AlphabetName_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_AlphabetName)
gen_cobol_specialnames_UPSISwitchIs_specialnames_MnemonicName = Generalization(general=specialnames_MnemonicName, specific=cobol_specialnames_UPSISwitchIs)
gen_cobol_specialnames_UPSISwitchIs_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_UPSISwitchIs)
gen_cobol_specialnames_PredefinedAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_PredefinedAlphabetType)
gen_cobol_specialnames_CodeNameAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_CodeNameAlphabetType)
gen_cobol_specialnames_CurrencySign_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_CurrencySign)
gen_cobol_specialnames_CurrencySign_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_CurrencySign)
gen_cobol_specialnames_ClassName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_ClassName)
gen_cobol_specialnames_ClassName_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_ClassName)
gen_cobol_specialnames_MnemonicName_SpecialName = Generalization(general=SpecialName, specific=cobol_specialnames_MnemonicName)
gen_cobol_specialnames_SystemDeviceIs_specialnames_MnemonicName = Generalization(general=specialnames_MnemonicName, specific=cobol_specialnames_SystemDeviceIs)
gen_cobol_specialnames_SystemDeviceIs_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_SystemDeviceIs)
gen_cobol_specialnames_SymbolicCharacter_SpecialName = Generalization(general=SpecialName, specific=cobol_specialnames_SymbolicCharacter)
gen_cobol_specialnames_SymbolicCharacterStatement_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_SymbolicCharacterStatement)
gen_cobol_specialnames_SymbolicCharacterStatement_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_specialnames_SymbolicCharacterStatement)
gen_cobol_tables_Table_dataitems_DataItem = Generalization(general=dataitems_DataItem, specific=cobol_tables_Table)
gen_cobol_tables_Table_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_tables_Table)
gen_cobol_tables_IndexName_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_tables_IndexName)
gen_cobol_tables_IndexName_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_tables_IndexName)
gen_cobol_tables_AdditionalIndexName_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_tables_AdditionalIndexName)
gen_cobol_files_FileName_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_files_FileName)
gen_cobol_files_FileName_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_files_FileName)
gen_cobol_files_SelectStatement_IncompleteElement = Generalization(general=IncompleteElement, specific=cobol_files_SelectStatement)
gen_cobol_labels_ProcedureLabel_ProcedureRangeChild = Generalization(general=ProcedureRangeChild, specific=cobol_labels_ProcedureLabel)
gen_cobol_parameters_Parameter_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_parameters_Parameter)
gen_cobol_parameters_ByReferenceParameter_Parameter = Generalization(general=Parameter_, specific=cobol_parameters_ByReferenceParameter)
gen_cobol_parameters_ByValueParameter_Parameter = Generalization(general=Parameter_, specific=cobol_parameters_ByValueParameter)
gen_cobol_verbs_Is_Verb = Generalization(general=Verb, specific=cobol_verbs_Is)
gen_cobol_labels_ProcedureRange_ProcedureRangeLabel = Generalization(general=ProcedureRangeLabel, specific=cobol_labels_ProcedureRange)
gen_cobol_labels_ProcedureRangeLabel_Label = Generalization(general=Label, specific=cobol_labels_ProcedureRangeLabel)
gen_cobol_handlers_InvalidKey_Handler = Generalization(general=Handler, specific=cobol_handlers_InvalidKey)
gen_cobol_labels_ProcedureRangeChild_ProcedureRangeLabel = Generalization(general=ProcedureRangeLabel, specific=cobol_labels_ProcedureRangeChild)
gen_cobol_handlers_NotAtEndOfPage_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotAtEndOfPage)
gen_cobol_labels_StopLabel_Label = Generalization(general=Label, specific=cobol_labels_StopLabel)
gen_cobol_labels_Run_StopLabel = Generalization(general=StopLabel, specific=cobol_labels_Run)
gen_cobol_functions_FunctionCall_functions_Argumentable = Generalization(general=functions_Argumentable, specific=cobol_functions_FunctionCall)
gen_cobol_functions_FunctionCall_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_functions_FunctionCall)
gen_cobol_functions_FunctionCall_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_functions_FunctionCall)
gen_cobol_functions_ByReferenceArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByReferenceArgument)
gen_cobol_functions_ByValueArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByValueArgument)
gen_cobol_functions_ByContentArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByContentArgument)
gen_cobol_functions_OmittedArgument_Argument = Generalization(general=Argument, specific=cobol_functions_OmittedArgument)
gen_cobol_handlers_OnSizeError_Handler = Generalization(general=Handler, specific=cobol_handlers_OnSizeError)
gen_cobol_handlers_Handler_NestedStatement = Generalization(general=NestedStatement, specific=cobol_handlers_Handler)
gen_cobol_handlers_NotOnSizeError_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotOnSizeError)
gen_cobol_handlers_OnOverflow_Handler = Generalization(general=Handler, specific=cobol_handlers_OnOverflow)
gen_cobol_handlers_OnException_Handler = Generalization(general=Handler, specific=cobol_handlers_OnException)
gen_cobol_handlers_NotOnException_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotOnException)
gen_cobol_handlers_NotErrorHandler_Handler = Generalization(general=Handler, specific=cobol_handlers_NotErrorHandler)
gen_cobol_handlers_NotOnOverflow_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotOnOverflow)
gen_cobol_handlers_NotAtEnd_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotAtEnd)
gen_cobol_handlers_AtEnd_Handler = Generalization(general=Handler, specific=cobol_handlers_AtEnd)
gen_cobol_handlers_AtEndOfPage_Handler = Generalization(general=Handler, specific=cobol_handlers_AtEndOfPage)
gen_cobol_strings_ReplacementOccurrence_strings_Occurrence = Generalization(general=strings_Occurrence, specific=cobol_strings_ReplacementOccurrence)
gen_cobol_strings_ReplacementOccurrence_strings_Replacement = Generalization(general=strings_Replacement, specific=cobol_strings_ReplacementOccurrence)
gen_cobol_handlers_NotInvalidKey_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotInvalidKey)
gen_cobol_strings_Tallying_StringManipulation = Generalization(general=StringManipulation, specific=cobol_strings_Tallying)
gen_cobol_strings_StringManipulation_String = Generalization(general=String, specific=cobol_strings_StringManipulation)
gen_cobol_strings_ManipulatedStrings_String = Generalization(general=String, specific=cobol_strings_ManipulatedStrings)
gen_cobol_strings_ConcatenatingStrings_ManipulatedStrings = Generalization(general=ManipulatedStrings, specific=cobol_strings_ConcatenatingStrings)
gen_cobol_strings_SplittedString_ManipulatedStrings = Generalization(general=ManipulatedStrings, specific=cobol_strings_SplittedString)
gen_cobol_strings_Replacement_StringManipulation = Generalization(general=StringManipulation, specific=cobol_strings_Replacement)
gen_cobol_strings_TallyingOccurrence_strings_Tallying = Generalization(general=strings_Tallying, specific=cobol_strings_TallyingOccurrence)
gen_cobol_strings_TallyingOccurrence_strings_Occurrence = Generalization(general=strings_Occurrence, specific=cobol_strings_TallyingOccurrence)
gen_cobol_strings_AnyCharacter_Tallying = Generalization(general=Tallying, specific=cobol_strings_AnyCharacter)
gen_cobol_strings_SpecificCharacter_Tallying = Generalization(general=Tallying, specific=cobol_strings_SpecificCharacter)
gen_cobol_strings_AnyCharacterBySpecificCharacter_Replacement = Generalization(general=Replacement, specific=cobol_strings_AnyCharacterBySpecificCharacter)
gen_cobol_strings_SpecificCharacterBySpecificCharacter_Replacement = Generalization(general=Replacement, specific=cobol_strings_SpecificCharacterBySpecificCharacter)

# Domain Model
domain_model = DomainModel(
    name="cobol",
    types={cobol_commons_NamedElement, Commentable, cobol_commons_Commentable, cobol_commons_LabellableElement, Negate, cobol_conditions_NegatedConditionalExpressionChild, cobol_conditions_SimpleConditionChild, cobol_conditions_RelationalExpression, SimpleConditionChild, RelationalOperator, Is, cobol_commons_URIableElement, cobol_conditions_Condition, cobol_conditions_ConditionalOrExpression, Condition, ConditionalOrExpressionChild, LogicalOperator, cobol_conditions_ConditionalOrExpressionChild, cobol_conditions_NegatedConditionalExpression, ConditionalAndExpressionChild, NegatedConditionalExpressionChild, cobol_conditions_NegatedAbbreviatedConditionalExpressionChild, cobol_conditions_AbbreviatedRelationalExpression, AbbreviatedRelationalExpressionChild, cobol_conditions_NestedAbbreviatedConditionalExpression, cobol_conditions_SignCondition, cobol_conditions_ExpressionList, cobol_conditions_ConditionalAndExpressionChild, cobol_conditions_ConditionalAndExpression, cobol_conditions_AbbreviatedConditionalExpression, AbbreviatedConditionalExpressionChild, cobol_conditions_AbbreviatedConditionalExpressionChild, cobol_conditions_NegatedAbbreviatedConditionalExpression, NegatedAbbreviatedConditionalExpressionChild, cobol_conditions_NestedCondition, cobol_arithmetics_AdditiveArithmeticExpression, RangeExpressionChild, AdditiveArithmeticExpressionChild, AdditiveOperator, cobol_arithmetics_AdditiveArithmeticExpressionChild, cobol_arithmetics_MultiplicativeArithmeticExpression, MultiplicativeArithmeticExpressionChild, MultiplicativeOperator, cobol_arithmetics_MultiplicativeArithmeticExpressionChild, cobol_arithmetics_PowerArithmeticExpression, SignOperator, cobol_conditions_ClassCondition, ClassOperator, cobol_conditions_AbbreviatedRelationalExpressionChild, Through, cobol_arithmetics_RangeExpressionChild, cobol_arithmetics_NestedArithmeticExpression, PrimaryExpression, cobol_arithmetics_ArithmeticExpression, conditions_AbbreviatedRelationalExpressionChild, conditions_SimpleConditionChild, cobol_containers_CompilationGroup, containers_CobolRoot, commons_NamedElement, CompilationUnit, cobol_containers_CompilationUnit, NamedElement, IdentificationDivision, PowerArithmeticExpressionChild, cobol_arithmetics_PowerArithmeticExpressionChild, cobol_arithmetics_UnaryArithmeticExpressionChild, cobol_arithmetics_UnaryArithmeticExpression, UnaryArithmeticExpressionChild, UnaryOperator, cobol_arithmetics_PrimaryExpression, cobol_arithmetics_AssignmentExpression, Equal, ArithmeticExpression, cobol_arithmetics_RangeExpression, cobol_divisions_IdentificationDivision, divisions_Division, water_IncompleteElement, cobol_divisions_ProcedureDivision, parameters_Parametrizable, Declaratives, cobol_literals_Literal, water_SelectStatementWater, water_SpecialNamesParagraphWater, water_CICSStatementWater, operands_PrimaryOperand, water_InvokeStatementWater, EnvironmentDivision, DataDivision, ProcedureDivision, cobol_containers_CobolRoot, cobol_containers_EmptyModel, CobolRoot, cobol_divisions_Division, Section, Paragraph, StatementContainer, cobol_divisions_DataDivision, Division, cobol_divisions_EnvironmentDivision, cobol_literals_AlphanumericLiteral, Literal, cobol_literals_IntegerLiteral, literals_NumericLiteral, water_ObjectComputerParagraphWater, water_FileDescriptorWater, water_IOControlParagraphWater, cobol_literals_DecimalLiteral, NumericLiteral, cobol_literals_FigurativeConstantLiteral, cobol_literals_BooleanLiteral, cobol_literals_FloatingDecimalLiteral, DecimalLiteral, cobol_literals_AllLiteral, FigurativeConstantLiteral, ConstantLiteral, cobol_literals_NumericLiteral, cobol_literals_ConstantLiteral, labels_StopLabel, cobol_literals_Space, cobol_literals_Any, cobol_literals_Characters, cobol_literals_PseudoLiteral, cobol_literals_DBCSLiteral, cobol_literals_NationalLiteral, DBCSLiteral, cobol_literals_FixedDecimalLiteral, cobol_literals_NationalHexLiteral, cobol_literals_Null, cobol_literals_Zero, cobol_literals_Quote, cobol_literals_LowValue, cobol_literals_HighValue, cobol_operators_GreaterThanOrEqual, cobol_operators_GreaterThan, cobol_operators_LessThan, cobol_operators_LessThanOrEqual, cobol_operators_Equal, cobol_operators_Power, cobol_operators_Negate, cobol_operators_Through, cobol_operators_ClassOperator, cobol_literals_AlphanumericHexaDecimalLiteral, AlphanumericLiteral, cobol_operators_Operator, cobol_operators_AdditiveOperator, Operator, cobol_operators_MultiplicativeOperator, cobol_operators_UnaryOperator, cobol_operators_LogicalOperator, cobol_operators_RelationalOperator, cobol_operators_ConditionOr, cobol_operators_ConditionAnd, cobol_operators_Multiplication, cobol_operators_SignOperator, cobol_operators_Positive, cobol_operators_Negative, cobol_operators_Division, cobol_operators_Addition, operators_AdditiveOperator, operators_UnaryOperator, cobol_operators_Subtraction, cobol_operators_GTSign, cobol_operators_GTEQPhrase, GreaterThanOrEqual, cobol_operators_GTEQSign, cobol_paragraphs_Paragraph, labels_Procedure, cobol_paragraphs_SourceComputerParagraph, ConfigurationSectionParagraph, DebuggingMode, cobol_paragraphs_ObjectComputerParagraph, paragraphs_ConfigurationSectionParagraph, cobol_paragraphs_FileControlParagraph, IOSectionParagraph, SelectStatement, cobol_paragraphs_IOControlParagraph, paragraphs_IOSectionParagraph, cobol_operators_Zero, cobol_operators_ClassName, cobol_operators_Alphabetic, cobol_operators_DBCS, cobol_operators_Numeric, cobol_operators_AlphabeticUpper, cobol_operators_AlphabeticLower, cobol_operators_Kanji, cobol_operators_EqualPhrase, cobol_operators_EqualSign, cobol_operators_LTPhrase, LessThan, cobol_operators_LTSign, cobol_operators_LTEQPhrase, LessThanOrEqual, cobol_operators_LTEQSign, cobol_operators_GTPhrase, GreaterThan, cobol_references_SpecialNamesConditionNameReference, references_ElementReference, references_Qualifiable, references_ConditionName, cobol_references_FileNameReference, references_IdentifierReferenceQualifier, cobol_references_IndexNameReference, IdentifierReference, cobol_references_MnemonicNameReference, cobol_references_AlphabetNameReference, ElementReference, cobol_references_ConditionName, cobol_references_Qualifiable, cobol_references_ConditionNameReference, identifiers_IdentifierReference, cobol_references_DataNameReference, cobol_references_IdentifierReferenceQualifier, cobol_sections_Section, cobol_paragraphs_ConfigurationSectionParagraph, cobol_paragraphs_IOSectionParagraph, cobol_paragraphs_SpecialNamesParagraph, SpecialNameStatement, SpecialNamesParagraphWater, cobol_paragraphs_RepositoryParagraph, cobol_paragraphs_DebuggingMode, cobol_references_Reference, cobol_references_ReferenceableElement, ReferenceableElement, cobol_references_ElementReference, Reference, FileName, cobol_sections_DeclarativeSection, cobol_sentences_StatementContainer, cobol_sentences_EmptySentence, Sentence, cobol_sentences_UseSentence, sentences_StatementContainer, cobol_sentences_AlteredGoTo, cobol_sentences_ExitProcedure, cobol_sentences_EntrySentence, cobol_sentences_ExecuteSentence, cobol_sentences_Sentence, cobol_operands_PrimaryOperand, operands_ReplacementOperand, operands_Operand, arithmetics_PrimaryExpression, operands_ArithmeticOperand, cobol_sections_WorkingStorageSection, DataDivisionSection, cobol_operands_RoundedIdentifier, cobol_sections_LocalStorageSection, ArithmeticOperand, cobol_sections_LinkageStorageSection, cobol_sections_IOSection, EnvironmentDivisionSection, cobol_sections_ConfigurationSection, cobol_sections_EnvironmentDivisionSection, cobol_sections_DataDivisionSection, Statement, DataItem, cobol_sections_FileSection, cobol_statements_ArithmeticStatement, statements_Statement, statements_ErrorHandled, cobol_statements_Add, ArithmeticStatement, cobol_statements_Subtract, cobol_statements_Multiply, cobol_statements_Divide, cobol_statements_Perform, cobol_statements_PerformNestedStatement, statements_Perform, statements_NestedStatement, Identifier, cobol_operands_ReplacementOperand, Operand, cobol_operands_Encoding, ReplacementOperand, cobol_operands_Operand, cobol_operands_ArithmeticOperand, cobol_statements_Statement, cobol_statements_Exit, cobol_statements_Condition, statements_Conditional, cobol_statements_Conditional, cobol_statements_Stop, StopLabel, cobol_statements_Display, Environment, cobol_statements_Compute, AssignmentExpression, cobol_statements_Accept, cobol_statements_PerformProcedure, Perform, ProcedureRangeLabel, cobol_statements_Jump, cobol_statements_NextSentence, Jump, cobol_statements_GoTo, cobol_statements_GoBack, cobol_statements_NestedStatement, cobol_statements_Move, PrimaryOperand, SwitchStatus, cobol_statements_SetIndexName, IndexNameReference, cobol_statements_String, ConcatenatingStrings, cobol_statements_Close, statements_IOStatement, cobol_statements_Cancel, cobol_statements_Call, functions_Argumentable, cobol_statements_Execute, cobol_statements_ErrorHandled, Handler, cobol_statements_Return, FileNameReference, cobol_statements_SetStatement, cobol_statements_SetSwitches, SetStatement, SplittedString, cobol_statements_Evaluate, EvaluateCase, ExpressionList, cobol_statements_NormalEvaluateCase, cobol_statements_OtherEvaluateCase, cobol_statements_EvaluateCase, NestedStatement, cobol_statements_Replace, cobol_statements_Entry, cobol_statements_Inspect, cobol_statements_Initialize, Replacement, cobol_statements_Open, cobol_statements_SearchStatement, NormalEvaluateCase, cobol_statements_SerialSearch, SearchStatement, cobol_statements_BinarySearch, cobol_statements_Unstring, cobol_statements_Write, IntegerLiteral, MnemonicNameReference, cobol_statements_Rewrite, Write, cobol_statements_SwitchStatus, TallyingIn, cobol_statements_Set, cobol_statements_Read, cobol_statements_PerformFixedTimes, cobol_statements_PerformProcedureUntilCondition, statements_PerformUntilCondition, AfterUntilCondition, cobol_statements_PerformNestedStatementFixedTimes, statements_PerformNestedStatement, cobol_statements_PerformNestedStatementUntilCondition, cobol_statements_Continue, cobol_statements_FileIOStatement, cobol_statements_PerformProcedureFixedTimes, statements_PerformProcedure, InputDirective, OutputDirective, KeyDescriptor, cobol_statements_Sort, statements_FileIOStatement, statements_PerformFixedTimes, cobol_statements_Merge, cobol_statements_Release, cobol_statements_PerformUntilCondition, statements_VaryingUntilCondition, cobol_statements_KeyDescriptor, cobol_statements_IOStatement, IOFileDescriptor, cobol_statements_IOFileDescriptor, IOFile, cobol_statements_IOFile, IncompleteElement, cobol_statements_TallyingIn, Tallying, cobol_statements_VaryingUntilCondition, Conditional, Qualifier, cobol_statements_AfterUntilCondition, VaryingUntilCondition, cobol_statements_Start, cobol_statements_Delete, cobol_identifiers_Subscript, cobol_identifiers_Identifier, water_AcceptStatementWater, water_RepositoryParagraphWater, water_IdentificationDivisionWater, water_SQLStatementWater, water_UseStatementWater, water_DataDescriptorWater, water_SortPhraseWater, ReferenceModifier, cobol_identifiers_IdentifierReference, identifiers_Identifier, Subscript, cobol_water_ProgramDescription, IdentificationDivisionWater, cobol_identifiers_All, DirectSubscript, cobol_identifiers_ReferenceModifier, cobol_identifiers_LinageCounter, cobol_identifiers_Qualifier, cobol_identifiers_RelativeSubscript, cobol_identifiers_DirectSubscript, cobol_ios_InputProcedure, ios_InputDirective, ios_ProcedureDirective, cobol_ios_InputDirective, IODirectives, cobol_ios_InputFile, ios_FileDirective, cobol_ios_OutputDirective, cobol_ios_OutputProcedure, ios_OutputDirective, cobol_ios_OutputFile, cobol_ios_IODirectives, cobol_ios_FileDirective, cobol_ios_ProcedureDirective, Label, cobol_water_IncompleteElement, Water, cobol_water_IdentificationDivisionWater, cobol_water_Water, cobol_water_SpecialNamesParagraphWater, cobol_water_SpecialNamesClause, cobol_water_Dot, cobol_water_ObjectComputerParagraphWater, cobol_water_ObjectComputerDescription, ObjectComputerParagraphWater, cobol_water_PriorityNumber, cobol_water_SelectStatementWater, cobol_water_SelectStatementClause, SelectStatementWater, cobol_water_FileDescriptorWater, cobol_water_FileDescription, FileDescriptorWater, cobol_water_DataDescriptorWater, cobol_water_DataDescription, DataDescriptorWater, cobol_water_IOControlParagraphWater, cobol_water_IOControlDescription, IOControlParagraphWater, cobol_water_RepositoryParagraphWater, cobol_water_RepositoryDescription, RepositoryParagraphWater, cobol_water_SQLStatementWater, cobol_water_CICSStatementWater, cobol_water_SQLStatementToken, SQLStatementWater, cobol_water_CICSStatementToken, CICSStatementWater, cobol_water_AcceptStatementWater, cobol_water_AcceptStatementToken, AcceptStatementWater, cobol_water_UseStatementWater, cobol_water_UseStatementToken, UseStatementWater, cobol_water_CloseStatementWater, cobol_water_CloseStatementToken, CloseStatementWater, cobol_environments_UPSI, cobol_water_InvokeStatementWater, cobol_water_InvokeStatementToken, InvokeStatementWater, cobol_water_OpenStatementWater, cobol_water_OpenStatementToken, OpenStatementWater, cobol_water_SortPhraseToken, SortPhraseWater, cobol_water_SortPhraseWater, cobol_registers_Register, cobol_registers_ShiftIn, Register, cobol_registers_ShiftOut, cobol_registers_AddressOf, cobol_registers_LengthOf, cobol_registers_ReturnCode, cobol_registers_WhenCompiled, cobol_environments_SystemDevice, cobol_environments_SystemLogicalInput, SystemDevice, cobol_environments_SystemLogicalOutput, cobol_environments_SystemPunchDevice, cobol_environments_Console, cobol_environments_Channel, cobol_environments_AdvancedFunctionPrinting, cobol_environments_SuppressSpacing, cobol_environments_Pocket, cobol_environments_Environment, cobol_dataitems_PictureString, DataItemAttribute, cobol_dataitems_RenamingDataName, DataName, RangeExpression, cobol_dataitems_ConditionName, cobol_dataitems_Global, cobol_dataitems_External, cobol_dataitems_Value, cobol_dataitems_DataItemAttribute, cobol_dataitems_Usage, cobol_dataitems_GroupUsage, cobol_dataitems_DataItem, references_ReferenceableElement, cobol_specialnames_ExplicitAlphabetType, cobol_dataitems_RecordName, cobol_dataitems_DataName, cobol_dataitems_Redefines, cobol_specialnames_SpecialName, cobol_specialnames_ConditionName, specialnames_SpecialName, cobol_specialnames_OnStatus, ConditionName, cobol_specialnames_OffStatus, cobol_specialnames_AlphabetName, specialnames_SpecialNameStatement, AlphabetType, cobol_specialnames_UPSISwitchIs, specialnames_MnemonicName, cobol_specialnames_AlphabetType, cobol_specialnames_PredefinedAlphabetType, KeyName, cobol_tables_KeyName, cobol_specialnames_CodeNameAlphabetType, cobol_specialnames_CurrencySign, cobol_specialnames_ClassName, cobol_specialnames_MnemonicName, SpecialName, cobol_specialnames_SystemDeviceIs, cobol_specialnames_SymbolicCharacter, cobol_specialnames_SymbolicCharacterStatement, SymbolicCharacter, AlphabetNameReference, cobol_specialnames_SpecialNameStatement, cobol_tables_Table, dataitems_DataItem, TableDimension, IndexName, cobol_parameters_Parametrizable, Parameter_, cobol_tables_IndexName, AdditionalIndexName, cobol_tables_TableDimension, cobol_tables_AdditionalIndexName, cobol_files_FileName, cobol_files_SelectStatement, FileStatus, cobol_files_FileStatus, cobol_labels_ProcedureLabel, cobol_parameters_Parameter, cobol_parameters_ByReferenceParameter, cobol_parameters_ByValueParameter, cobol_declaratives_Declaratives, DeclarativeSection, cobol_verbs_Is, Verb, cobol_verbs_Verb, cobol_labels_ProcedureRange, ProcedureRangeChild, cobol_labels_ProcedureRangeLabel, cobol_handlers_InvalidKey, cobol_labels_ProcedureRangeChild, cobol_handlers_NotAtEndOfPage, Procedure, cobol_labels_Procedure, cobol_labels_Label, cobol_labels_StopLabel, cobol_labels_Run, cobol_functions_FunctionCall, cobol_functions_Argument, cobol_functions_ByReferenceArgument, Argument, cobol_functions_ByValueArgument, cobol_functions_ByContentArgument, cobol_functions_OmittedArgument, cobol_functions_Argumentable, cobol_handlers_OnSizeError, cobol_handlers_Handler, cobol_handlers_NotOnSizeError, NotErrorHandler, cobol_handlers_OnOverflow, cobol_handlers_OnException, cobol_handlers_NotOnException, cobol_handlers_NotErrorHandler, cobol_handlers_NotOnOverflow, cobol_handlers_NotAtEnd, cobol_handlers_AtEnd, cobol_handlers_AtEndOfPage, cobol_strings_ReplacementOccurrence, strings_Replacement, cobol_handlers_NotInvalidKey, cobol_strings_Tallying, StringManipulation, cobol_strings_StringManipulation, String, Location, cobol_strings_ManipulatedStrings, cobol_strings_String, cobol_strings_ConcatenatingStrings, ManipulatedStrings, cobol_strings_SplittedString, cobol_strings_Location, cobol_strings_Replacement, cobol_strings_Occurrence, cobol_strings_TallyingOccurrence, strings_Tallying, strings_Occurrence, cobol_strings_AnyCharacter, cobol_strings_SpecificCharacter, cobol_strings_AnyCharacterBySpecificCharacter, cobol_strings_SpecificCharacterBySpecificCharacter, Properties, Nulls, Zeroes, Quotes, LowValues, HighValues, Spaces, ThroughPhrase, EncodingTypes, Adjustings, Status, ExitLabels, EOP, IOTypes, Orders, Corresponding, ProgramDescriptionInfo, ObjectComputerDescriptionInfo, SelectStatementClauses, SpecialNamesClauses, FileDescriptionInfo, DataDescriptionInfo, IOControlDescriptionInfo, RepositoryDescriptionInfo, CICSStatementTokens, SQLStatementTokens, InvokeStatementTokens, AcceptStatementTokens, UseStatementTokens, CloseStatementTokens, OpenStatementTokens, SortPhraseTokens, Selects, UPSISwitches, Channels, SystemInputs, SystemOutputs, SystemPunchDevices, PictureStringCharacters, Usages, PredefinedAlphabetTypes, FileDescriptors, SortingOrder, Positions, Occurrences},
    associations={negateOperator4, children6, relationalOperator7, negateOperator9, is_12, children0, logicalOperators1, child3, negateOperator18, relationalOperator21, child23, negateOperator25, is_28, expression31, rest33, expressions14, children15, children16, child17, condition56, children58, additiveOperators59, children61, multiplicativeOperators62, child36, signOperator38, negateOperator40, is_43, child46, classOperator48, negateOperator50, is_53, children74, throughOperator75, expression77, compilationUnits79, identificationDivision80, children64, child65, unaryOperator66, assignmentOperator68, children69, value71, declaratives95, environmentDivision81, dataDivision83, procedureDivision85, nestedCompilationUnits87, sections90, paragraphs91, sentences93, constant96, sentences97, withDebuggingMode99, selectStatements100, qualifier109, sentences110, paragraphs112, specialNameStatements101, water102, aliasesTo104, aliasesFrom105, target107, fileDescriptors118, statements119, next121, statements115, records116, next123, operands125, givings126, tos129, froms131, bys133, intos135, remainders137, identifier122, sender147, elseStatements150, condition152, label154, operands155, output157, expression159, label140, labels141, dependsOn143, statements144, receivers146, switches169, receivers170, pointer171, receiver173, senders176, subprograms178, subprogram180, receiver160, handlers162, fileName163, output164, sender167, pointer192, tally194, sender197, receivers200, delimiter202, counter205, cases208, subject209, objects211, subprograms182, replacements184, cases186, table187, variable190, receiver225, keyName227, fileName230, recordName233, numLines235, integer238, mnemonicName240, sender242, mnemonicNames245, tallyingIns213, replacements214, conversions217, string220, receivers223, sender262, conditions247, iterations249, afters251, fileName252, input254, output256, keyDescriptors258, recordName260, variable275, keyNames265, ioFileDescriptors267, ioFiles268, fileName269, occurrences271, counter272, qualifiers299, init277, increment280, fileName283, operator285, dataName288, not_291, fileName294, subscript296, modifier297, subscripts298, start301, length303, additiveOperator306, integer308, fileNames311, label313, water314, operand315, nameRange317, values318, attributes320, subentries321, superentry323, range331, elems325, dataName327, type329, conditionNames330, keysAre346, maxTableDimension348, dependsOn351, currency333, range334, environment336, integers338, symbolicCharacters340, alphabetNameReference341, tableDimension343, indexedBy344, vsamFileStatus371, parameters374, keys354, additionalIndexNames356, records357, attributes359, sentences362, fileStatus365, fileNameReference366, fileStatus369, section384, returning375, declarativeSections378, children379, throughOperator380, target383, operands386, arguments388, returning389, handlerStatement392, locations394, strings395, delimiter397, counter400, base402, target404, occurrences405, occurrences407, tallying409, source411},
    generalizations={gen_cobol_commons_NamedElement_Commentable, gen_cobol_commons_LabellableElement_Commentable, gen_cobol_conditions_NegatedConditionalExpressionChild_ConditionalAndExpressionChild, gen_cobol_conditions_SimpleConditionChild_NegatedConditionalExpressionChild, gen_cobol_conditions_RelationalExpression_NegatedConditionalExpressionChild, gen_cobol_commons_URIableElement_Commentable, gen_cobol_conditions_ConditionalOrExpression_Condition, gen_cobol_conditions_ConditionalOrExpressionChild_Condition, gen_cobol_conditions_NegatedConditionalExpression_ConditionalAndExpressionChild, gen_cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_AbbreviatedConditionalExpressionChild, gen_cobol_conditions_AbbreviatedRelationalExpression_NegatedAbbreviatedConditionalExpressionChild, gen_cobol_conditions_NestedAbbreviatedConditionalExpression_AbbreviatedRelationalExpressionChild, gen_cobol_conditions_SignCondition_NegatedConditionalExpressionChild, gen_cobol_conditions_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_cobol_conditions_ConditionalAndExpression_ConditionalOrExpressionChild, gen_cobol_conditions_AbbreviatedConditionalExpression_ConditionalAndExpressionChild, gen_cobol_conditions_AbbreviatedConditionalExpressionChild_ConditionalAndExpressionChild, gen_cobol_conditions_NegatedAbbreviatedConditionalExpression_AbbreviatedConditionalExpressionChild, gen_cobol_conditions_NestedCondition_SimpleConditionChild, gen_cobol_arithmetics_AdditiveArithmeticExpression_RangeExpressionChild, gen_cobol_arithmetics_AdditiveArithmeticExpressionChild_RangeExpressionChild, gen_cobol_arithmetics_MultiplicativeArithmeticExpression_AdditiveArithmeticExpressionChild, gen_cobol_arithmetics_MultiplicativeArithmeticExpressionChild_AdditiveArithmeticExpressionChild, gen_cobol_arithmetics_PowerArithmeticExpression_MultiplicativeArithmeticExpressionChild, gen_cobol_conditions_ClassCondition_NegatedConditionalExpressionChild, gen_cobol_conditions_AbbreviatedRelationalExpressionChild_NegatedAbbreviatedConditionalExpressionChild, gen_cobol_arithmetics_RangeExpressionChild_ArithmeticExpression, gen_cobol_arithmetics_NestedArithmeticExpression_PrimaryExpression, gen_cobol_arithmetics_ArithmeticExpression_conditions_AbbreviatedRelationalExpressionChild, gen_cobol_arithmetics_ArithmeticExpression_conditions_SimpleConditionChild, gen_cobol_containers_CompilationGroup_containers_CobolRoot, gen_cobol_containers_CompilationGroup_commons_NamedElement, gen_cobol_containers_CompilationUnit_NamedElement, gen_cobol_arithmetics_PowerArithmeticExpressionChild_MultiplicativeArithmeticExpressionChild, gen_cobol_arithmetics_UnaryArithmeticExpressionChild_PowerArithmeticExpressionChild, gen_cobol_arithmetics_UnaryArithmeticExpression_PowerArithmeticExpressionChild, gen_cobol_arithmetics_PrimaryExpression_UnaryArithmeticExpressionChild, gen_cobol_arithmetics_RangeExpression_ArithmeticExpression, gen_cobol_divisions_EnvironmentDivision_Division, gen_cobol_divisions_IdentificationDivision_divisions_Division, gen_cobol_divisions_IdentificationDivision_water_IncompleteElement, gen_cobol_divisions_ProcedureDivision_divisions_Division, gen_cobol_divisions_ProcedureDivision_parameters_Parametrizable, gen_cobol_literals_Literal_water_SelectStatementWater, gen_cobol_literals_Literal_water_SpecialNamesParagraphWater, gen_cobol_literals_Literal_water_CICSStatementWater, gen_cobol_literals_Literal_operands_PrimaryOperand, gen_cobol_literals_Literal_water_InvokeStatementWater, gen_cobol_containers_EmptyModel_CobolRoot, gen_cobol_divisions_Division_NamedElement, gen_cobol_divisions_DataDivision_Division, gen_cobol_literals_AlphanumericLiteral_Literal, gen_cobol_literals_IntegerLiteral_literals_NumericLiteral, gen_cobol_literals_IntegerLiteral_water_ObjectComputerParagraphWater, gen_cobol_literals_IntegerLiteral_water_FileDescriptorWater, gen_cobol_literals_IntegerLiteral_water_IOControlParagraphWater, gen_cobol_literals_DecimalLiteral_NumericLiteral, gen_cobol_literals_FigurativeConstantLiteral_Literal, gen_cobol_literals_BooleanLiteral_Literal, gen_cobol_literals_FloatingDecimalLiteral_DecimalLiteral, gen_cobol_literals_AllLiteral_FigurativeConstantLiteral, gen_cobol_literals_NumericLiteral_Literal, gen_cobol_literals_ConstantLiteral_FigurativeConstantLiteral, gen_cobol_literals_Literal_labels_StopLabel, gen_cobol_literals_Space_ConstantLiteral, gen_cobol_literals_Any_Literal, gen_cobol_literals_Characters_Literal, gen_cobol_literals_PseudoLiteral_Literal, gen_cobol_literals_DBCSLiteral_Literal, gen_cobol_literals_NationalLiteral_DBCSLiteral, gen_cobol_literals_FixedDecimalLiteral_DecimalLiteral, gen_cobol_literals_NationalHexLiteral_DBCSLiteral, gen_cobol_literals_Null_ConstantLiteral, gen_cobol_literals_Zero_ConstantLiteral, gen_cobol_literals_Quote_ConstantLiteral, gen_cobol_literals_LowValue_ConstantLiteral, gen_cobol_literals_HighValue_ConstantLiteral, gen_cobol_operators_Subtraction_operators_AdditiveOperator, gen_cobol_operators_Subtraction_operators_UnaryOperator, gen_cobol_operators_GreaterThanOrEqual_RelationalOperator, gen_cobol_operators_GreaterThan_RelationalOperator, gen_cobol_operators_LessThan_RelationalOperator, gen_cobol_operators_LessThanOrEqual_RelationalOperator, gen_cobol_operators_Equal_RelationalOperator, gen_cobol_operators_Power_Operator, gen_cobol_operators_Negate_Operator, gen_cobol_operators_Through_Operator, gen_cobol_operators_ClassOperator_Operator, gen_cobol_literals_AlphanumericHexaDecimalLiteral_AlphanumericLiteral, gen_cobol_operators_AdditiveOperator_Operator, gen_cobol_operators_MultiplicativeOperator_Operator, gen_cobol_operators_UnaryOperator_Operator, gen_cobol_operators_LogicalOperator_Operator, gen_cobol_operators_RelationalOperator_Operator, gen_cobol_operators_ConditionOr_LogicalOperator, gen_cobol_operators_ConditionAnd_LogicalOperator, gen_cobol_operators_Multiplication_MultiplicativeOperator, gen_cobol_operators_SignOperator_Operator, gen_cobol_operators_Positive_SignOperator, gen_cobol_operators_Negative_SignOperator, gen_cobol_operators_Division_MultiplicativeOperator, gen_cobol_operators_Addition_operators_AdditiveOperator, gen_cobol_operators_Addition_operators_UnaryOperator, gen_cobol_operators_GTSign_GreaterThan, gen_cobol_operators_GTEQPhrase_GreaterThanOrEqual, gen_cobol_operators_GTEQSign_GreaterThanOrEqual, gen_cobol_paragraphs_Paragraph_commons_NamedElement, gen_cobol_paragraphs_Paragraph_labels_Procedure, gen_cobol_paragraphs_SourceComputerParagraph_ConfigurationSectionParagraph, gen_cobol_paragraphs_ObjectComputerParagraph_paragraphs_ConfigurationSectionParagraph, gen_cobol_paragraphs_ObjectComputerParagraph_water_IncompleteElement, gen_cobol_paragraphs_FileControlParagraph_IOSectionParagraph, gen_cobol_paragraphs_IOControlParagraph_paragraphs_IOSectionParagraph, gen_cobol_paragraphs_IOControlParagraph_water_IncompleteElement, gen_cobol_operators_Zero_SignOperator, gen_cobol_operators_ClassName_ClassOperator, gen_cobol_operators_Alphabetic_ClassOperator, gen_cobol_operators_DBCS_ClassOperator, gen_cobol_operators_Numeric_ClassOperator, gen_cobol_operators_AlphabeticUpper_ClassOperator, gen_cobol_operators_AlphabeticLower_ClassOperator, gen_cobol_operators_Kanji_ClassOperator, gen_cobol_operators_EqualPhrase_Equal, gen_cobol_operators_EqualSign_Equal, gen_cobol_operators_LTPhrase_LessThan, gen_cobol_operators_LTSign_LessThan, gen_cobol_operators_LTEQPhrase_LessThanOrEqual, gen_cobol_operators_LTEQSign_LessThanOrEqual, gen_cobol_operators_GTPhrase_GreaterThan, gen_cobol_references_SpecialNamesConditionNameReference_references_ElementReference, gen_cobol_references_SpecialNamesConditionNameReference_references_Qualifiable, gen_cobol_references_SpecialNamesConditionNameReference_references_ConditionName, gen_cobol_references_FileNameReference_references_ElementReference, gen_cobol_references_FileNameReference_references_IdentifierReferenceQualifier, gen_cobol_references_IndexNameReference_IdentifierReference, gen_cobol_references_MnemonicNameReference_references_ElementReference, gen_cobol_references_MnemonicNameReference_references_Qualifiable, gen_cobol_references_AlphabetNameReference_ElementReference, gen_cobol_references_ConditionNameReference_identifiers_IdentifierReference, gen_cobol_references_ConditionNameReference_references_ConditionName, gen_cobol_references_DataNameReference_identifiers_IdentifierReference, gen_cobol_references_DataNameReference_references_IdentifierReferenceQualifier, gen_cobol_references_IdentifierReferenceQualifier_references_Qualifiable, gen_cobol_references_IdentifierReferenceQualifier_references_ElementReference, gen_cobol_sections_Section_commons_NamedElement, gen_cobol_sections_Section_labels_Procedure, gen_cobol_paragraphs_ConfigurationSectionParagraph_Paragraph, gen_cobol_paragraphs_IOSectionParagraph_Paragraph, gen_cobol_paragraphs_SpecialNamesParagraph_ConfigurationSectionParagraph, gen_cobol_paragraphs_RepositoryParagraph_paragraphs_ConfigurationSectionParagraph, gen_cobol_paragraphs_RepositoryParagraph_water_IncompleteElement, gen_cobol_references_ReferenceableElement_NamedElement, gen_cobol_references_ElementReference_Reference, gen_cobol_sections_DeclarativeSection_Section, gen_cobol_sentences_EmptySentence_Sentence, gen_cobol_sentences_UseSentence_sentences_StatementContainer, gen_cobol_sentences_UseSentence_water_IncompleteElement, gen_cobol_sentences_AlteredGoTo_Sentence, gen_cobol_sentences_ExitProcedure_Sentence, gen_cobol_sentences_EntrySentence_Sentence, gen_cobol_sentences_ExecuteSentence_StatementContainer, gen_cobol_sentences_Sentence_StatementContainer, gen_cobol_operands_PrimaryOperand_operands_ReplacementOperand, gen_cobol_operands_PrimaryOperand_operands_Operand, gen_cobol_operands_PrimaryOperand_arithmetics_PrimaryExpression, gen_cobol_operands_PrimaryOperand_operands_ArithmeticOperand, gen_cobol_sections_WorkingStorageSection_DataDivisionSection, gen_cobol_sections_LocalStorageSection_DataDivisionSection, gen_cobol_operands_RoundedIdentifier_ArithmeticOperand, gen_cobol_sections_LinkageStorageSection_DataDivisionSection, gen_cobol_sections_IOSection_EnvironmentDivisionSection, gen_cobol_sections_ConfigurationSection_EnvironmentDivisionSection, gen_cobol_sections_EnvironmentDivisionSection_Section, gen_cobol_sections_DataDivisionSection_Section, gen_cobol_sections_FileSection_DataDivisionSection, gen_cobol_statements_ArithmeticStatement_statements_Statement, gen_cobol_statements_ArithmeticStatement_statements_ErrorHandled, gen_cobol_statements_Add_ArithmeticStatement, gen_cobol_statements_Subtract_ArithmeticStatement, gen_cobol_statements_Multiply_ArithmeticStatement, gen_cobol_statements_Divide_ArithmeticStatement, gen_cobol_statements_Perform_Statement, gen_cobol_statements_PerformNestedStatement_statements_Perform, gen_cobol_statements_PerformNestedStatement_statements_NestedStatement, gen_cobol_operands_ReplacementOperand_Operand, gen_cobol_operands_Encoding_ReplacementOperand, gen_cobol_operands_ArithmeticOperand_Operand, gen_cobol_statements_Exit_Statement, gen_cobol_statements_Condition_statements_NestedStatement, gen_cobol_statements_Condition_statements_Conditional, gen_cobol_statements_Condition_statements_Statement, gen_cobol_statements_Stop_Statement, gen_cobol_statements_Display_Statement, gen_cobol_statements_Compute_statements_Statement, gen_cobol_statements_Compute_statements_ErrorHandled, gen_cobol_statements_Accept_statements_Statement, gen_cobol_statements_Accept_water_IncompleteElement, gen_cobol_statements_PerformProcedure_Perform, gen_cobol_statements_Jump_Statement, gen_cobol_statements_NextSentence_Jump, gen_cobol_statements_GoTo_Jump, gen_cobol_statements_GoBack_Jump, gen_cobol_statements_Move_Statement, gen_cobol_statements_SetIndexName_SetStatement, gen_cobol_statements_String_statements_Statement, gen_cobol_statements_String_statements_ErrorHandled, gen_cobol_statements_Close_water_IncompleteElement, gen_cobol_statements_Close_statements_IOStatement, gen_cobol_statements_Cancel_Statement, gen_cobol_statements_Call_statements_Statement, gen_cobol_statements_Call_functions_Argumentable, gen_cobol_statements_Call_statements_ErrorHandled, gen_cobol_statements_Execute_Statement, gen_cobol_statements_Return_statements_Statement, gen_cobol_statements_Return_statements_ErrorHandled, gen_cobol_statements_SetStatement_Statement, gen_cobol_statements_SetSwitches_SetStatement, gen_cobol_statements_Evaluate_Statement, gen_cobol_statements_NormalEvaluateCase_EvaluateCase, gen_cobol_statements_OtherEvaluateCase_EvaluateCase, gen_cobol_statements_EvaluateCase_NestedStatement, gen_cobol_statements_Replace_Statement, gen_cobol_statements_Entry_parameters_Parametrizable, gen_cobol_statements_Entry_statements_Statement, gen_cobol_statements_Inspect_Statement, gen_cobol_statements_Initialize_Statement, gen_cobol_statements_Open_water_IncompleteElement, gen_cobol_statements_Open_statements_IOStatement, gen_cobol_statements_SearchStatement_statements_Statement, gen_cobol_statements_SearchStatement_statements_ErrorHandled, gen_cobol_statements_SerialSearch_SearchStatement, gen_cobol_statements_BinarySearch_SearchStatement, gen_cobol_statements_Unstring_statements_ErrorHandled, gen_cobol_statements_Unstring_statements_Statement, gen_cobol_statements_Write_statements_Statement, gen_cobol_statements_Write_statements_ErrorHandled, gen_cobol_statements_Rewrite_Write, gen_cobol_statements_Set_SetStatement, gen_cobol_statements_Read_statements_Statement, gen_cobol_statements_Read_statements_ErrorHandled, gen_cobol_statements_PerformFixedTimes_Perform, gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformUntilCondition, gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformProcedure, gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformNestedStatement, gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformFixedTimes, gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformUntilCondition, gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformNestedStatement, gen_cobol_statements_Continue_Jump, gen_cobol_statements_FileIOStatement_Statement, gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformProcedure, gen_cobol_statements_Sort_statements_FileIOStatement, gen_cobol_statements_Sort_water_IncompleteElement, gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformFixedTimes, gen_cobol_statements_Merge_statements_FileIOStatement, gen_cobol_statements_Merge_water_IncompleteElement, gen_cobol_statements_Release_Statement, gen_cobol_statements_PerformUntilCondition_statements_Perform, gen_cobol_statements_PerformUntilCondition_statements_VaryingUntilCondition, gen_cobol_statements_IOStatement_Statement, gen_cobol_statements_IOFile_IncompleteElement, gen_cobol_statements_VaryingUntilCondition_Conditional, gen_cobol_statements_AfterUntilCondition_VaryingUntilCondition, gen_cobol_statements_Start_statements_ErrorHandled, gen_cobol_statements_Start_statements_Statement, gen_cobol_statements_Delete_statements_Statement, gen_cobol_statements_Delete_statements_ErrorHandled, gen_cobol_identifiers_Identifier_operands_PrimaryOperand, gen_cobol_identifiers_Identifier_water_AcceptStatementWater, gen_cobol_identifiers_Identifier_water_CICSStatementWater, gen_cobol_identifiers_Identifier_water_SpecialNamesParagraphWater, gen_cobol_identifiers_Identifier_water_ObjectComputerParagraphWater, gen_cobol_identifiers_Identifier_water_RepositoryParagraphWater, gen_cobol_identifiers_Identifier_water_IOControlParagraphWater, gen_cobol_identifiers_Identifier_water_IdentificationDivisionWater, gen_cobol_identifiers_Identifier_water_InvokeStatementWater, gen_cobol_identifiers_Identifier_water_SQLStatementWater, gen_cobol_identifiers_Identifier_water_UseStatementWater, gen_cobol_identifiers_Identifier_water_FileDescriptorWater, gen_cobol_identifiers_Identifier_water_DataDescriptorWater, gen_cobol_identifiers_Identifier_water_SelectStatementWater, gen_cobol_identifiers_Identifier_water_SortPhraseWater, gen_cobol_identifiers_IdentifierReference_identifiers_Identifier, gen_cobol_identifiers_IdentifierReference_references_ElementReference, gen_cobol_identifiers_IdentifierReference_references_Qualifiable, gen_cobol_water_ProgramDescription_IdentificationDivisionWater, gen_cobol_identifiers_All_DirectSubscript, gen_cobol_identifiers_LinageCounter_identifiers_Identifier, gen_cobol_identifiers_LinageCounter_references_Qualifiable, gen_cobol_identifiers_Qualifier_ElementReference, gen_cobol_identifiers_RelativeSubscript_Subscript, gen_cobol_identifiers_DirectSubscript_Subscript, gen_cobol_ios_InputProcedure_ios_InputDirective, gen_cobol_ios_InputProcedure_ios_ProcedureDirective, gen_cobol_ios_InputDirective_IODirectives, gen_cobol_ios_InputFile_ios_InputDirective, gen_cobol_ios_InputFile_ios_FileDirective, gen_cobol_ios_OutputDirective_IODirectives, gen_cobol_ios_OutputProcedure_ios_ProcedureDirective, gen_cobol_ios_OutputProcedure_ios_OutputDirective, gen_cobol_ios_OutputFile_ios_OutputDirective, gen_cobol_ios_OutputFile_ios_FileDirective, gen_cobol_ios_FileDirective_IODirectives, gen_cobol_ios_ProcedureDirective_IODirectives, gen_cobol_water_IdentificationDivisionWater_Water, gen_cobol_water_SpecialNamesParagraphWater_Water, gen_cobol_water_SpecialNamesClause_SpecialNamesParagraphWater, gen_cobol_water_Dot_water_IdentificationDivisionWater, gen_cobol_water_Dot_water_SQLStatementWater, gen_cobol_water_ObjectComputerParagraphWater_Water, gen_cobol_water_ObjectComputerDescription_ObjectComputerParagraphWater, gen_cobol_water_PriorityNumber_ObjectComputerParagraphWater, gen_cobol_water_SelectStatementWater_Water, gen_cobol_water_SelectStatementClause_SelectStatementWater, gen_cobol_water_FileDescriptorWater_Water, gen_cobol_water_FileDescription_FileDescriptorWater, gen_cobol_water_DataDescriptorWater_Water, gen_cobol_water_DataDescription_DataDescriptorWater, gen_cobol_water_IOControlParagraphWater_Water, gen_cobol_water_IOControlDescription_IOControlParagraphWater, gen_cobol_water_RepositoryParagraphWater_Water, gen_cobol_water_RepositoryDescription_RepositoryParagraphWater, gen_cobol_water_SQLStatementWater_Water, gen_cobol_water_CICSStatementWater_Water, gen_cobol_water_SQLStatementToken_SQLStatementWater, gen_cobol_water_CICSStatementToken_CICSStatementWater, gen_cobol_water_AcceptStatementWater_Water, gen_cobol_water_AcceptStatementToken_AcceptStatementWater, gen_cobol_water_UseStatementWater_Water, gen_cobol_water_UseStatementToken_UseStatementWater, gen_cobol_water_CloseStatementWater_Water, gen_cobol_water_CloseStatementToken_CloseStatementWater, gen_cobol_environments_UPSI_Environment, gen_cobol_water_InvokeStatementWater_Water, gen_cobol_water_InvokeStatementToken_InvokeStatementWater, gen_cobol_water_OpenStatementWater_Water, gen_cobol_water_OpenStatementToken_OpenStatementWater, gen_cobol_water_SortPhraseToken_SortPhraseWater, gen_cobol_water_SortPhraseWater_Water, gen_cobol_registers_Register_PrimaryOperand, gen_cobol_registers_ShiftIn_Register, gen_cobol_registers_ShiftOut_Register, gen_cobol_registers_AddressOf_Register, gen_cobol_registers_LengthOf_Register, gen_cobol_registers_ReturnCode_Register, gen_cobol_registers_WhenCompiled_Register, gen_cobol_environments_SystemDevice_Environment, gen_cobol_environments_SystemLogicalInput_SystemDevice, gen_cobol_environments_SystemLogicalOutput_SystemDevice, gen_cobol_environments_SystemPunchDevice_SystemDevice, gen_cobol_environments_Console_SystemDevice, gen_cobol_environments_Channel_SystemDevice, gen_cobol_environments_AdvancedFunctionPrinting_SystemDevice, gen_cobol_environments_SuppressSpacing_SystemDevice, gen_cobol_environments_Pocket_SystemDevice, gen_cobol_environments_Environment_AcceptStatementWater, gen_cobol_dataitems_PictureString_DataItemAttribute, gen_cobol_dataitems_RenamingDataName_DataName, gen_cobol_dataitems_ConditionName_DataItem, gen_cobol_dataitems_Global_DataItemAttribute, gen_cobol_dataitems_External_DataItemAttribute, gen_cobol_dataitems_Value_DataItemAttribute, gen_cobol_dataitems_Usage_DataItemAttribute, gen_cobol_dataitems_GroupUsage_DataItemAttribute, gen_cobol_dataitems_DataItem_references_ReferenceableElement, gen_cobol_dataitems_DataItem_water_IncompleteElement, gen_cobol_specialnames_ExplicitAlphabetType_AlphabetType, gen_cobol_dataitems_RecordName_DataItem, gen_cobol_dataitems_DataName_DataItem, gen_cobol_dataitems_Redefines_DataItemAttribute, gen_cobol_specialnames_SpecialName_ReferenceableElement, gen_cobol_specialnames_ConditionName_commons_NamedElement, gen_cobol_specialnames_ConditionName_specialnames_SpecialName, gen_cobol_specialnames_OnStatus_ConditionName, gen_cobol_specialnames_OffStatus_ConditionName, gen_cobol_specialnames_AlphabetName_specialnames_SpecialName, gen_cobol_specialnames_AlphabetName_specialnames_SpecialNameStatement, gen_cobol_specialnames_UPSISwitchIs_specialnames_MnemonicName, gen_cobol_specialnames_UPSISwitchIs_specialnames_SpecialNameStatement, gen_cobol_specialnames_PredefinedAlphabetType_AlphabetType, gen_cobol_specialnames_CodeNameAlphabetType_AlphabetType, gen_cobol_specialnames_CurrencySign_specialnames_SpecialName, gen_cobol_specialnames_CurrencySign_specialnames_SpecialNameStatement, gen_cobol_specialnames_ClassName_specialnames_SpecialName, gen_cobol_specialnames_ClassName_specialnames_SpecialNameStatement, gen_cobol_specialnames_MnemonicName_SpecialName, gen_cobol_specialnames_SystemDeviceIs_specialnames_MnemonicName, gen_cobol_specialnames_SystemDeviceIs_specialnames_SpecialNameStatement, gen_cobol_specialnames_SymbolicCharacter_SpecialName, gen_cobol_specialnames_SymbolicCharacterStatement_specialnames_SpecialNameStatement, gen_cobol_specialnames_SymbolicCharacterStatement_references_ElementReference, gen_cobol_tables_Table_dataitems_DataItem, gen_cobol_tables_Table_water_IncompleteElement, gen_cobol_tables_IndexName_commons_NamedElement, gen_cobol_tables_IndexName_references_ReferenceableElement, gen_cobol_tables_AdditionalIndexName_ReferenceableElement, gen_cobol_files_FileName_water_IncompleteElement, gen_cobol_files_FileName_references_ReferenceableElement, gen_cobol_files_SelectStatement_IncompleteElement, gen_cobol_labels_ProcedureLabel_ProcedureRangeChild, gen_cobol_parameters_Parameter_ReferenceableElement, gen_cobol_parameters_ByReferenceParameter_Parameter, gen_cobol_parameters_ByValueParameter_Parameter, gen_cobol_verbs_Is_Verb, gen_cobol_labels_ProcedureRange_ProcedureRangeLabel, gen_cobol_labels_ProcedureRangeLabel_Label, gen_cobol_handlers_InvalidKey_Handler, gen_cobol_labels_ProcedureRangeChild_ProcedureRangeLabel, gen_cobol_handlers_NotAtEndOfPage_NotErrorHandler, gen_cobol_labels_StopLabel_Label, gen_cobol_labels_Run_StopLabel, gen_cobol_functions_FunctionCall_functions_Argumentable, gen_cobol_functions_FunctionCall_commons_NamedElement, gen_cobol_functions_FunctionCall_identifiers_Identifier, gen_cobol_functions_ByReferenceArgument_Argument, gen_cobol_functions_ByValueArgument_Argument, gen_cobol_functions_ByContentArgument_Argument, gen_cobol_functions_OmittedArgument_Argument, gen_cobol_handlers_OnSizeError_Handler, gen_cobol_handlers_Handler_NestedStatement, gen_cobol_handlers_NotOnSizeError_NotErrorHandler, gen_cobol_handlers_OnOverflow_Handler, gen_cobol_handlers_OnException_Handler, gen_cobol_handlers_NotOnException_NotErrorHandler, gen_cobol_handlers_NotErrorHandler_Handler, gen_cobol_handlers_NotOnOverflow_NotErrorHandler, gen_cobol_handlers_NotAtEnd_NotErrorHandler, gen_cobol_handlers_AtEnd_Handler, gen_cobol_handlers_AtEndOfPage_Handler, gen_cobol_strings_ReplacementOccurrence_strings_Occurrence, gen_cobol_strings_ReplacementOccurrence_strings_Replacement, gen_cobol_handlers_NotInvalidKey_NotErrorHandler, gen_cobol_strings_Tallying_StringManipulation, gen_cobol_strings_StringManipulation_String, gen_cobol_strings_ManipulatedStrings_String, gen_cobol_strings_ConcatenatingStrings_ManipulatedStrings, gen_cobol_strings_SplittedString_ManipulatedStrings, gen_cobol_strings_Replacement_StringManipulation, gen_cobol_strings_TallyingOccurrence_strings_Tallying, gen_cobol_strings_TallyingOccurrence_strings_Occurrence, gen_cobol_strings_AnyCharacter_Tallying, gen_cobol_strings_SpecificCharacter_Tallying, gen_cobol_strings_AnyCharacterBySpecificCharacter_Replacement, gen_cobol_strings_SpecificCharacterBySpecificCharacter_Replacement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)