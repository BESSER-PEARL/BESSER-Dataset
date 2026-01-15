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

ExitLabels: Enumeration = Enumeration(
    name="ExitLabels",
    literals={
            EnumerationLiteral(name="program"),
			EnumerationLiteral(name="paragraph"),
			EnumerationLiteral(name="method")
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

SpecialNamesClauses: Enumeration = Enumeration(
    name="SpecialNamesClauses",
    literals={
            EnumerationLiteral(name="decimalPoint"),
			EnumerationLiteral(name="is"),
			EnumerationLiteral(name="comma"),
			EnumerationLiteral(name="xmlSchema")
    }
)

FileDescriptionInfo: Enumeration = Enumeration(
    name="FileDescriptionInfo",
    literals={
            EnumerationLiteral(name="block"),
			EnumerationLiteral(name="contains"),
			EnumerationLiteral(name="lines"),
			EnumerationLiteral(name="with"),
			EnumerationLiteral(name="footing"),
			EnumerationLiteral(name="at"),
			EnumerationLiteral(name="top"),
			EnumerationLiteral(name="bottom"),
			EnumerationLiteral(name="varying"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="size"),
			EnumerationLiteral(name="from"),
			EnumerationLiteral(name="depending"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="mode"),
			EnumerationLiteral(name="recording"),
			EnumerationLiteral(name="f"),
			EnumerationLiteral(name="v"),
			EnumerationLiteral(name="to"),
			EnumerationLiteral(name="u"),
			EnumerationLiteral(name="characters"),
			EnumerationLiteral(name="s"),
			EnumerationLiteral(name="value"),
			EnumerationLiteral(name="records"),
			EnumerationLiteral(name="of"),
			EnumerationLiteral(name="codeSet"),
			EnumerationLiteral(name="identification"),
			EnumerationLiteral(name="is"),
			EnumerationLiteral(name="id"),
			EnumerationLiteral(name="data"),
			EnumerationLiteral(name="report"),
			EnumerationLiteral(name="reports"),
			EnumerationLiteral(name="record"),
			EnumerationLiteral(name="are"),
			EnumerationLiteral(name="label"),
			EnumerationLiteral(name="omitted"),
			EnumerationLiteral(name="standard"),
			EnumerationLiteral(name="linage")
    }
)

SelectStatementClauses: Enumeration = Enumeration(
    name="SelectStatementClauses",
    literals={
            EnumerationLiteral(name="with"),
			EnumerationLiteral(name="dynamic"),
			EnumerationLiteral(name="organization"),
			EnumerationLiteral(name="duplicates"),
			EnumerationLiteral(name="indexed"),
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
			EnumerationLiteral(name="is"),
			EnumerationLiteral(name="sequential"),
			EnumerationLiteral(name="random")
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
			EnumerationLiteral(name="for"),
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

DataDescriptionInfo: Enumeration = Enumeration(
    name="DataDescriptionInfo",
    literals={
            EnumerationLiteral(name="just"),
			EnumerationLiteral(name="right"),
			EnumerationLiteral(name="sign"),
			EnumerationLiteral(name="is"),
			EnumerationLiteral(name="leading"),
			EnumerationLiteral(name="trailing"),
			EnumerationLiteral(name="separate"),
			EnumerationLiteral(name="character"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="format"),
			EnumerationLiteral(name="synchronized"),
			EnumerationLiteral(name="sync"),
			EnumerationLiteral(name="left"),
			EnumerationLiteral(name="blank"),
			EnumerationLiteral(name="when"),
			EnumerationLiteral(name="zero"),
			EnumerationLiteral(name="zeros"),
			EnumerationLiteral(name="zeroes"),
			EnumerationLiteral(name="justified")
    }
)

CICSStatementTokens: Enumeration = Enumeration(
    name="CICSStatementTokens",
    literals={
            EnumerationLiteral(name="ts"),
			EnumerationLiteral(name="queue"),
			EnumerationLiteral(name="qname"),
			EnumerationLiteral(name="openpar"),
			EnumerationLiteral(name="closepar"),
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
			EnumerationLiteral(name="from"),
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
			EnumerationLiteral(name="xctl"),
			EnumerationLiteral(name="load"),
			EnumerationLiteral(name="start"),
			EnumerationLiteral(name="tr"),
			EnumerationLiteral(name="massinsert"),
			EnumerationLiteral(name="program"),
			EnumerationLiteral(name="commarea"),
			EnumerationLiteral(name="datalength"),
			EnumerationLiteral(name="synconreturn"),
			EnumerationLiteral(name="transid"),
			EnumerationLiteral(name="inputmsg"),
			EnumerationLiteral(name="inputmsglen"),
			EnumerationLiteral(name="channel")
    }
)

RepositoryDescriptionInfo: Enumeration = Enumeration(
    name="RepositoryDescriptionInfo",
    literals={
            EnumerationLiteral(name="class"),
			EnumerationLiteral(name="is")
    }
)

SQLStatementTokens: Enumeration = Enumeration(
    name="SQLStatementTokens",
    literals={
            EnumerationLiteral(name="include"),
			EnumerationLiteral(name="select"),
			EnumerationLiteral(name="declare"),
			EnumerationLiteral(name="from"),
			EnumerationLiteral(name="insert"),
			EnumerationLiteral(name="into"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete")
    }
)

AcceptStatementTokens: Enumeration = Enumeration(
    name="AcceptStatementTokens",
    literals={
            EnumerationLiteral(name="from"),
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
            EnumerationLiteral(name="global"),
			EnumerationLiteral(name="after"),
			EnumerationLiteral(name="standard"),
			EnumerationLiteral(name="error"),
			EnumerationLiteral(name="exception"),
			EnumerationLiteral(name="procedure"),
			EnumerationLiteral(name="on"),
			EnumerationLiteral(name="input"),
			EnumerationLiteral(name="output"),
			EnumerationLiteral(name="extend"),
			EnumerationLiteral(name="for"),
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
            EnumerationLiteral(name="with"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="rewind"),
			EnumerationLiteral(name="lock"),
			EnumerationLiteral(name="reel"),
			EnumerationLiteral(name="unit"),
			EnumerationLiteral(name="for"),
			EnumerationLiteral(name="removal")
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

SortPhraseTokens: Enumeration = Enumeration(
    name="SortPhraseTokens",
    literals={
            EnumerationLiteral(name="with"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="order"),
			EnumerationLiteral(name="sequence"),
			EnumerationLiteral(name="duplicates"),
			EnumerationLiteral(name="collating"),
			EnumerationLiteral(name="is")
    }
)

OpenStatementTokens: Enumeration = Enumeration(
    name="OpenStatementTokens",
    literals={
            EnumerationLiteral(name="reversed"),
			EnumerationLiteral(name="with"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="rewind")
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

Usages: Enumeration = Enumeration(
    name="Usages",
    literals={
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
			EnumerationLiteral(name="computational3"),
			EnumerationLiteral(name="comp3"),
			EnumerationLiteral(name="computational4"),
			EnumerationLiteral(name="comp4"),
			EnumerationLiteral(name="computational5"),
			EnumerationLiteral(name="comp5"),
			EnumerationLiteral(name="pointer"),
			EnumerationLiteral(name="procedurePointer"),
			EnumerationLiteral(name="functionPointer"),
			EnumerationLiteral(name="national")
    }
)

PictureStringCharacters: Enumeration = Enumeration(
    name="PictureStringCharacters",
    literals={
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
			EnumerationLiteral(name="escape"),
			EnumerationLiteral(name="any"),
			EnumerationLiteral(name="blank"),
			EnumerationLiteral(name="sign"),
			EnumerationLiteral(name="leadingZero"),
			EnumerationLiteral(name="decimalPoint")
    }
)

PredefinedAlphabetTypes: Enumeration = Enumeration(
    name="PredefinedAlphabetTypes",
    literals={
            EnumerationLiteral(name="native"),
			EnumerationLiteral(name="standard1"),
			EnumerationLiteral(name="standard2"),
			EnumerationLiteral(name="ebcdic")
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
            EnumerationLiteral(name="dsc"),
			EnumerationLiteral(name="asc")
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
cobol_commons_NamedElement = Class(name="cobol::commons::NamedElement", is_abstract=True)
Commentable = Class(name="Commentable")
cobol_commons_Commentable = Class(name="cobol::commons::Commentable", is_abstract=True)
cobol_commons_LabellableElement = Class(name="cobol::commons::LabellableElement", is_abstract=True)
cobol_commons_URIableElement = Class(name="cobol::commons::URIableElement", is_abstract=True)
cobol_conditions_Condition = Class(name="cobol::conditions::Condition", is_abstract=True)
cobol_conditions_ConditionalOrExpression = Class(name="cobol::conditions::ConditionalOrExpression")
Condition = Class(name="Condition")
ConditionalOrExpressionChild = Class(name="ConditionalOrExpressionChild")
LogicalOperator = Class(name="LogicalOperator")
cobol_conditions_ConditionalOrExpressionChild = Class(name="cobol::conditions::ConditionalOrExpressionChild", is_abstract=True)
cobol_conditions_NegatedConditionalExpression = Class(name="cobol::conditions::NegatedConditionalExpression")
ConditionalAndExpressionChild = Class(name="ConditionalAndExpressionChild")
NegatedConditionalExpressionChild = Class(name="NegatedConditionalExpressionChild")
Negate = Class(name="Negate")
cobol_conditions_NegatedConditionalExpressionChild = Class(name="cobol::conditions::NegatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_SimpleConditionChild = Class(name="cobol::conditions::SimpleConditionChild", is_abstract=True)
cobol_conditions_RelationalExpression = Class(name="cobol::conditions::RelationalExpression")
SimpleConditionChild = Class(name="SimpleConditionChild")
RelationalOperator = Class(name="RelationalOperator")
Is = Class(name="Is")
cobol_conditions_ExpressionList = Class(name="cobol::conditions::ExpressionList")
cobol_conditions_ConditionalAndExpressionChild = Class(name="cobol::conditions::ConditionalAndExpressionChild", is_abstract=True)
cobol_conditions_ConditionalAndExpression = Class(name="cobol::conditions::ConditionalAndExpression")
cobol_conditions_AbbreviatedConditionalExpression = Class(name="cobol::conditions::AbbreviatedConditionalExpression")
AbbreviatedConditionalExpressionChild = Class(name="AbbreviatedConditionalExpressionChild")
cobol_conditions_AbbreviatedConditionalExpressionChild = Class(name="cobol::conditions::AbbreviatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_NegatedAbbreviatedConditionalExpression = Class(name="cobol::conditions::NegatedAbbreviatedConditionalExpression")
cobol_conditions_NegatedAbbreviatedConditionalExpressionChild = Class(name="cobol::conditions::NegatedAbbreviatedConditionalExpressionChild", is_abstract=True)
cobol_conditions_AbbreviatedRelationalExpression = Class(name="cobol::conditions::AbbreviatedRelationalExpression")
AbbreviatedRelationalExpressionChild = Class(name="AbbreviatedRelationalExpressionChild")
cobol_conditions_NestedAbbreviatedConditionalExpression = Class(name="cobol::conditions::NestedAbbreviatedConditionalExpression")
cobol_conditions_SignCondition = Class(name="cobol::conditions::SignCondition")
SignOperator = Class(name="SignOperator")
cobol_conditions_ClassCondition = Class(name="cobol::conditions::ClassCondition")
ClassOperator = Class(name="ClassOperator")
cobol_conditions_AbbreviatedRelationalExpressionChild = Class(name="cobol::conditions::AbbreviatedRelationalExpressionChild", is_abstract=True)
cobol_conditions_NestedCondition = Class(name="cobol::conditions::NestedCondition")
NegatedAbbreviatedConditionalExpressionChild = Class(name="NegatedAbbreviatedConditionalExpressionChild")
AdditiveArithmeticExpressionChild = Class(name="AdditiveArithmeticExpressionChild")
AdditiveOperator = Class(name="AdditiveOperator")
cobol_arithmetics_AdditiveArithmeticExpressionChild = Class(name="cobol::arithmetics::AdditiveArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_MultiplicativeArithmeticExpression = Class(name="cobol::arithmetics::MultiplicativeArithmeticExpression")
MultiplicativeArithmeticExpressionChild = Class(name="MultiplicativeArithmeticExpressionChild")
MultiplicativeOperator = Class(name="MultiplicativeOperator")
cobol_arithmetics_MultiplicativeArithmeticExpressionChild = Class(name="cobol::arithmetics::MultiplicativeArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_PowerArithmeticExpression = Class(name="cobol::arithmetics::PowerArithmeticExpression")
PowerArithmeticExpressionChild = Class(name="PowerArithmeticExpressionChild")
cobol_arithmetics_PowerArithmeticExpressionChild = Class(name="cobol::arithmetics::PowerArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_UnaryArithmeticExpressionChild = Class(name="cobol::arithmetics::UnaryArithmeticExpressionChild", is_abstract=True)
cobol_arithmetics_UnaryArithmeticExpression = Class(name="cobol::arithmetics::UnaryArithmeticExpression")
UnaryArithmeticExpressionChild = Class(name="UnaryArithmeticExpressionChild")
UnaryOperator = Class(name="UnaryOperator")
cobol_arithmetics_PrimaryExpression = Class(name="cobol::arithmetics::PrimaryExpression", is_abstract=True)
cobol_arithmetics_AssignmentExpression = Class(name="cobol::arithmetics::AssignmentExpression")
Equal = Class(name="Equal")
ArithmeticExpression = Class(name="ArithmeticExpression")
cobol_arithmetics_RangeExpression = Class(name="cobol::arithmetics::RangeExpression")
Through = Class(name="Through")
cobol_arithmetics_AdditiveArithmeticExpression = Class(name="cobol::arithmetics::AdditiveArithmeticExpression")
RangeExpressionChild = Class(name="RangeExpressionChild")
cobol_arithmetics_NestedArithmeticExpression = Class(name="cobol::arithmetics::NestedArithmeticExpression")
PrimaryExpression = Class(name="PrimaryExpression")
cobol_arithmetics_ArithmeticExpression = Class(name="cobol::arithmetics::ArithmeticExpression", is_abstract=True)
conditions_AbbreviatedRelationalExpressionChild = Class(name="conditions::AbbreviatedRelationalExpressionChild")
conditions_SimpleConditionChild = Class(name="conditions::SimpleConditionChild")
cobol_containers_CompilationGroup = Class(name="cobol::containers::CompilationGroup")
containers_CobolRoot = Class(name="containers::CobolRoot")
commons_NamedElement = Class(name="commons::NamedElement")
CompilationUnit = Class(name="CompilationUnit")
cobol_containers_CompilationUnit = Class(name="cobol::containers::CompilationUnit")
NamedElement = Class(name="NamedElement")
IdentificationDivision = Class(name="IdentificationDivision")
EnvironmentDivision = Class(name="EnvironmentDivision")
DataDivision = Class(name="DataDivision")
ProcedureDivision = Class(name="ProcedureDivision")
cobol_containers_CobolRoot = Class(name="cobol::containers::CobolRoot", is_abstract=True)
cobol_containers_EmptyModel = Class(name="cobol::containers::EmptyModel")
CobolRoot = Class(name="CobolRoot")
cobol_divisions_Division = Class(name="cobol::divisions::Division", is_abstract=True)
Section = Class(name="Section")
Paragraph = Class(name="Paragraph")
StatementContainer = Class(name="StatementContainer")
cobol_divisions_DataDivision = Class(name="cobol::divisions::DataDivision")
Division = Class(name="Division")
cobol_divisions_EnvironmentDivision = Class(name="cobol::divisions::EnvironmentDivision")
cobol_divisions_IdentificationDivision = Class(name="cobol::divisions::IdentificationDivision")
divisions_Division = Class(name="divisions::Division")
water_IncompleteElement = Class(name="water::IncompleteElement")
cobol_divisions_ProcedureDivision = Class(name="cobol::divisions::ProcedureDivision")
parameters_Parametrizable = Class(name="parameters::Parametrizable")
cobol_arithmetics_RangeExpressionChild = Class(name="cobol::arithmetics::RangeExpressionChild", is_abstract=True)
Declaratives = Class(name="Declaratives")
cobol_literals_Literal = Class(name="cobol::literals::Literal", is_abstract=True)
water_SelectStatementWater = Class(name="water::SelectStatementWater")
water_SpecialNamesParagraphWater = Class(name="water::SpecialNamesParagraphWater")
water_CICSStatementWater = Class(name="water::CICSStatementWater")
operands_PrimaryOperand = Class(name="operands::PrimaryOperand")
water_InvokeStatementWater = Class(name="water::InvokeStatementWater")
labels_StopLabel = Class(name="labels::StopLabel")
cobol_literals_AlphanumericLiteral = Class(name="cobol::literals::AlphanumericLiteral")
Literal = Class(name="Literal")
cobol_literals_IntegerLiteral = Class(name="cobol::literals::IntegerLiteral")
literals_NumericLiteral = Class(name="literals::NumericLiteral")
water_ObjectComputerParagraphWater = Class(name="water::ObjectComputerParagraphWater")
water_FileDescriptorWater = Class(name="water::FileDescriptorWater")
water_IOControlParagraphWater = Class(name="water::IOControlParagraphWater")
cobol_literals_DecimalLiteral = Class(name="cobol::literals::DecimalLiteral", is_abstract=True)
NumericLiteral = Class(name="NumericLiteral")
cobol_literals_FigurativeConstantLiteral = Class(name="cobol::literals::FigurativeConstantLiteral", is_abstract=True)
cobol_literals_BooleanLiteral = Class(name="cobol::literals::BooleanLiteral")
cobol_literals_FloatingDecimalLiteral = Class(name="cobol::literals::FloatingDecimalLiteral")
DecimalLiteral = Class(name="DecimalLiteral")
cobol_literals_AllLiteral = Class(name="cobol::literals::AllLiteral")
FigurativeConstantLiteral = Class(name="FigurativeConstantLiteral")
ConstantLiteral = Class(name="ConstantLiteral")
cobol_literals_NumericLiteral = Class(name="cobol::literals::NumericLiteral", is_abstract=True)
cobol_literals_ConstantLiteral = Class(name="cobol::literals::ConstantLiteral", is_abstract=True)
cobol_literals_PseudoLiteral = Class(name="cobol::literals::PseudoLiteral")
cobol_literals_DBCSLiteral = Class(name="cobol::literals::DBCSLiteral", is_abstract=True)
cobol_literals_NationalLiteral = Class(name="cobol::literals::NationalLiteral")
DBCSLiteral = Class(name="DBCSLiteral")
cobol_literals_FixedDecimalLiteral = Class(name="cobol::literals::FixedDecimalLiteral")
cobol_literals_NationalHexLiteral = Class(name="cobol::literals::NationalHexLiteral")
cobol_literals_Null = Class(name="cobol::literals::Null")
cobol_literals_Zero = Class(name="cobol::literals::Zero")
cobol_literals_Quote = Class(name="cobol::literals::Quote")
cobol_literals_LowValue = Class(name="cobol::literals::LowValue")
cobol_literals_HighValue = Class(name="cobol::literals::HighValue")
cobol_literals_Space = Class(name="cobol::literals::Space")
cobol_literals_Any = Class(name="cobol::literals::Any")
cobol_literals_Characters = Class(name="cobol::literals::Characters")
cobol_literals_AlphanumericHexaDecimalLiteral = Class(name="cobol::literals::AlphanumericHexaDecimalLiteral")
AlphanumericLiteral = Class(name="AlphanumericLiteral")
cobol_operators_Operator = Class(name="cobol::operators::Operator", is_abstract=True)
cobol_operators_AdditiveOperator = Class(name="cobol::operators::AdditiveOperator", is_abstract=True)
Operator = Class(name="Operator")
cobol_operators_MultiplicativeOperator = Class(name="cobol::operators::MultiplicativeOperator", is_abstract=True)
cobol_operators_UnaryOperator = Class(name="cobol::operators::UnaryOperator", is_abstract=True)
cobol_operators_RelationalOperator = Class(name="cobol::operators::RelationalOperator", is_abstract=True)
cobol_operators_ConditionOr = Class(name="cobol::operators::ConditionOr")
cobol_operators_ConditionAnd = Class(name="cobol::operators::ConditionAnd")
cobol_operators_Multiplication = Class(name="cobol::operators::Multiplication")
cobol_operators_SignOperator = Class(name="cobol::operators::SignOperator", is_abstract=True)
cobol_operators_Positive = Class(name="cobol::operators::Positive")
cobol_operators_Negative = Class(name="cobol::operators::Negative")
cobol_operators_Division = Class(name="cobol::operators::Division")
cobol_operators_Addition = Class(name="cobol::operators::Addition")
operators_AdditiveOperator = Class(name="operators::AdditiveOperator")
operators_UnaryOperator = Class(name="operators::UnaryOperator")
cobol_operators_Subtraction = Class(name="cobol::operators::Subtraction")
cobol_operators_GreaterThanOrEqual = Class(name="cobol::operators::GreaterThanOrEqual", is_abstract=True)
cobol_operators_GreaterThan = Class(name="cobol::operators::GreaterThan", is_abstract=True)
cobol_operators_LessThan = Class(name="cobol::operators::LessThan", is_abstract=True)
cobol_operators_LessThanOrEqual = Class(name="cobol::operators::LessThanOrEqual", is_abstract=True)
cobol_operators_Equal = Class(name="cobol::operators::Equal", is_abstract=True)
cobol_operators_Power = Class(name="cobol::operators::Power")
cobol_operators_Negate = Class(name="cobol::operators::Negate")
cobol_operators_Through = Class(name="cobol::operators::Through")
cobol_operators_ClassOperator = Class(name="cobol::operators::ClassOperator", is_abstract=True)
cobol_operators_Zero = Class(name="cobol::operators::Zero")
cobol_operators_ClassName = Class(name="cobol::operators::ClassName")
cobol_operators_Alphabetic = Class(name="cobol::operators::Alphabetic")
cobol_operators_DBCS = Class(name="cobol::operators::DBCS")
cobol_operators_Numeric = Class(name="cobol::operators::Numeric")
cobol_operators_AlphabeticUpper = Class(name="cobol::operators::AlphabeticUpper")
cobol_operators_AlphabeticLower = Class(name="cobol::operators::AlphabeticLower")
cobol_operators_LogicalOperator = Class(name="cobol::operators::LogicalOperator", is_abstract=True)
cobol_operators_Kanji = Class(name="cobol::operators::Kanji")
cobol_operators_EqualPhrase = Class(name="cobol::operators::EqualPhrase")
cobol_operators_EqualSign = Class(name="cobol::operators::EqualSign")
cobol_operators_LTPhrase = Class(name="cobol::operators::LTPhrase")
LessThan = Class(name="LessThan")
cobol_operators_LTSign = Class(name="cobol::operators::LTSign")
cobol_operators_LTEQPhrase = Class(name="cobol::operators::LTEQPhrase")
LessThanOrEqual = Class(name="LessThanOrEqual")
cobol_operators_LTEQSign = Class(name="cobol::operators::LTEQSign")
cobol_operators_GTPhrase = Class(name="cobol::operators::GTPhrase")
GreaterThan = Class(name="GreaterThan")
cobol_operators_GTSign = Class(name="cobol::operators::GTSign")
cobol_operators_GTEQPhrase = Class(name="cobol::operators::GTEQPhrase")
GreaterThanOrEqual = Class(name="GreaterThanOrEqual")
cobol_operators_GTEQSign = Class(name="cobol::operators::GTEQSign")
cobol_paragraphs_Paragraph = Class(name="cobol::paragraphs::Paragraph")
labels_Procedure = Class(name="labels::Procedure")
cobol_paragraphs_SourceComputerParagraph = Class(name="cobol::paragraphs::SourceComputerParagraph")
ConfigurationSectionParagraph = Class(name="ConfigurationSectionParagraph")
DebuggingMode = Class(name="DebuggingMode")
cobol_paragraphs_ObjectComputerParagraph = Class(name="cobol::paragraphs::ObjectComputerParagraph")
paragraphs_ConfigurationSectionParagraph = Class(name="paragraphs::ConfigurationSectionParagraph")
cobol_paragraphs_FileControlParagraph = Class(name="cobol::paragraphs::FileControlParagraph")
IOSectionParagraph = Class(name="IOSectionParagraph")
SelectStatement = Class(name="SelectStatement")
cobol_paragraphs_IOControlParagraph = Class(name="cobol::paragraphs::IOControlParagraph")
paragraphs_IOSectionParagraph = Class(name="paragraphs::IOSectionParagraph")
cobol_paragraphs_ConfigurationSectionParagraph = Class(name="cobol::paragraphs::ConfigurationSectionParagraph", is_abstract=True)
cobol_paragraphs_IOSectionParagraph = Class(name="cobol::paragraphs::IOSectionParagraph", is_abstract=True)
cobol_paragraphs_SpecialNamesParagraph = Class(name="cobol::paragraphs::SpecialNamesParagraph")
SpecialNameStatement = Class(name="SpecialNameStatement")
cobol_paragraphs_DebuggingMode = Class(name="cobol::paragraphs::DebuggingMode")
cobol_references_Reference = Class(name="cobol::references::Reference", is_abstract=True)
cobol_references_ReferenceableElement = Class(name="cobol::references::ReferenceableElement", is_abstract=True)
ReferenceableElement = Class(name="ReferenceableElement")
cobol_references_ElementReference = Class(name="cobol::references::ElementReference", is_abstract=True)
Reference = Class(name="Reference")
cobol_references_SpecialNamesConditionNameReference = Class(name="cobol::references::SpecialNamesConditionNameReference")
references_ElementReference = Class(name="references::ElementReference")
references_Qualifiable = Class(name="references::Qualifiable")
references_ConditionName = Class(name="references::ConditionName")
cobol_references_FileNameReference = Class(name="cobol::references::FileNameReference")
references_IdentifierReferenceQualifier = Class(name="references::IdentifierReferenceQualifier")
cobol_references_IndexNameReference = Class(name="cobol::references::IndexNameReference")
IdentifierReference = Class(name="IdentifierReference")
cobol_references_MnemonicNameReference = Class(name="cobol::references::MnemonicNameReference")
cobol_references_AlphabetNameReference = Class(name="cobol::references::AlphabetNameReference")
ElementReference = Class(name="ElementReference")
cobol_references_ConditionName = Class(name="cobol::references::ConditionName", is_abstract=True)
cobol_references_Qualifiable = Class(name="cobol::references::Qualifiable", is_abstract=True)
cobol_references_ConditionNameReference = Class(name="cobol::references::ConditionNameReference")
identifiers_IdentifierReference = Class(name="identifiers::IdentifierReference")
cobol_references_DataNameReference = Class(name="cobol::references::DataNameReference")
cobol_references_IdentifierReferenceQualifier = Class(name="cobol::references::IdentifierReferenceQualifier")
cobol_sections_Section = Class(name="cobol::sections::Section")
cobol_sections_WorkingStorageSection = Class(name="cobol::sections::WorkingStorageSection")
DataDivisionSection = Class(name="DataDivisionSection")
cobol_sections_LocalStorageSection = Class(name="cobol::sections::LocalStorageSection")
SpecialNamesParagraphWater = Class(name="SpecialNamesParagraphWater")
cobol_sections_LinkageStorageSection = Class(name="cobol::sections::LinkageStorageSection")
cobol_sections_IOSection = Class(name="cobol::sections::IOSection")
EnvironmentDivisionSection = Class(name="EnvironmentDivisionSection")
cobol_paragraphs_RepositoryParagraph = Class(name="cobol::paragraphs::RepositoryParagraph")
cobol_sections_EnvironmentDivisionSection = Class(name="cobol::sections::EnvironmentDivisionSection", is_abstract=True)
cobol_sections_DataDivisionSection = Class(name="cobol::sections::DataDivisionSection", is_abstract=True)
Statement = Class(name="Statement")
DataItem = Class(name="DataItem")
cobol_sections_FileSection = Class(name="cobol::sections::FileSection")
FileName = Class(name="FileName")
cobol_sections_DeclarativeSection = Class(name="cobol::sections::DeclarativeSection")
cobol_sentences_StatementContainer = Class(name="cobol::sentences::StatementContainer", is_abstract=True)
cobol_sentences_EmptySentence = Class(name="cobol::sentences::EmptySentence")
Sentence = Class(name="Sentence")
cobol_sentences_UseSentence = Class(name="cobol::sentences::UseSentence")
sentences_StatementContainer = Class(name="sentences::StatementContainer")
cobol_sentences_AlteredGoTo = Class(name="cobol::sentences::AlteredGoTo")
cobol_sentences_ExitProcedure = Class(name="cobol::sentences::ExitProcedure")
cobol_sentences_EntrySentence = Class(name="cobol::sentences::EntrySentence")
cobol_sentences_ExecuteSentence = Class(name="cobol::sentences::ExecuteSentence")
cobol_sentences_Sentence = Class(name="cobol::sentences::Sentence")
cobol_operands_PrimaryOperand = Class(name="cobol::operands::PrimaryOperand", is_abstract=True)
operands_ReplacementOperand = Class(name="operands::ReplacementOperand")
operands_Operand = Class(name="operands::Operand")
arithmetics_PrimaryExpression = Class(name="arithmetics::PrimaryExpression")
operands_ArithmeticOperand = Class(name="operands::ArithmeticOperand")
cobol_sections_ConfigurationSection = Class(name="cobol::sections::ConfigurationSection")
cobol_operands_ReplacementOperand = Class(name="cobol::operands::ReplacementOperand", is_abstract=True)
Operand = Class(name="Operand")
cobol_operands_Encoding = Class(name="cobol::operands::Encoding")
ReplacementOperand = Class(name="ReplacementOperand")
cobol_operands_Operand = Class(name="cobol::operands::Operand", is_abstract=True)
cobol_operands_ArithmeticOperand = Class(name="cobol::operands::ArithmeticOperand", is_abstract=True)
cobol_statements_Statement = Class(name="cobol::statements::Statement", is_abstract=True)
cobol_statements_ArithmeticStatement = Class(name="cobol::statements::ArithmeticStatement", is_abstract=True)
statements_Statement = Class(name="statements::Statement")
statements_ErrorHandled = Class(name="statements::ErrorHandled")
cobol_statements_Add = Class(name="cobol::statements::Add")
ArithmeticStatement = Class(name="ArithmeticStatement")
cobol_statements_Subtract = Class(name="cobol::statements::Subtract")
cobol_statements_Multiply = Class(name="cobol::statements::Multiply")
cobol_operands_RoundedIdentifier = Class(name="cobol::operands::RoundedIdentifier")
ArithmeticOperand = Class(name="ArithmeticOperand")
Identifier = Class(name="Identifier")
cobol_statements_Perform = Class(name="cobol::statements::Perform", is_abstract=True)
cobol_statements_PerformNestedStatement = Class(name="cobol::statements::PerformNestedStatement")
statements_Perform = Class(name="statements::Perform")
statements_NestedStatement = Class(name="statements::NestedStatement")
cobol_statements_PerformProcedure = Class(name="cobol::statements::PerformProcedure")
Perform = Class(name="Perform")
ProcedureRangeLabel = Class(name="ProcedureRangeLabel")
cobol_statements_Jump = Class(name="cobol::statements::Jump", is_abstract=True)
cobol_statements_NextSentence = Class(name="cobol::statements::NextSentence")
Jump = Class(name="Jump")
cobol_statements_GoTo = Class(name="cobol::statements::GoTo")
cobol_statements_GoBack = Class(name="cobol::statements::GoBack")
cobol_statements_NestedStatement = Class(name="cobol::statements::NestedStatement", is_abstract=True)
cobol_statements_Move = Class(name="cobol::statements::Move")
PrimaryOperand = Class(name="PrimaryOperand")
cobol_statements_Exit = Class(name="cobol::statements::Exit")
cobol_statements_Condition = Class(name="cobol::statements::Condition")
cobol_statements_Divide = Class(name="cobol::statements::Divide")
statements_Conditional = Class(name="statements::Conditional")
cobol_statements_Conditional = Class(name="cobol::statements::Conditional", is_abstract=True)
cobol_statements_Stop = Class(name="cobol::statements::Stop")
StopLabel = Class(name="StopLabel")
cobol_statements_Display = Class(name="cobol::statements::Display")
Environment = Class(name="Environment")
cobol_statements_Compute = Class(name="cobol::statements::Compute")
AssignmentExpression = Class(name="AssignmentExpression")
cobol_statements_Accept = Class(name="cobol::statements::Accept")
cobol_statements_Execute = Class(name="cobol::statements::Execute")
cobol_statements_ErrorHandled = Class(name="cobol::statements::ErrorHandled", is_abstract=True)
Handler = Class(name="Handler")
cobol_statements_Return = Class(name="cobol::statements::Return")
FileNameReference = Class(name="FileNameReference")
cobol_statements_SetStatement = Class(name="cobol::statements::SetStatement", is_abstract=True)
cobol_statements_SetSwitches = Class(name="cobol::statements::SetSwitches")
SetStatement = Class(name="SetStatement")
SwitchStatus = Class(name="SwitchStatus")
cobol_statements_SetIndexName = Class(name="cobol::statements::SetIndexName")
IndexNameReference = Class(name="IndexNameReference")
cobol_statements_String = Class(name="cobol::statements::String")
ConcatenatingStrings = Class(name="ConcatenatingStrings")
cobol_statements_Close = Class(name="cobol::statements::Close")
statements_IOStatement = Class(name="statements::IOStatement")
cobol_statements_Cancel = Class(name="cobol::statements::Cancel")
cobol_statements_Initialize = Class(name="cobol::statements::Initialize")
Replacement = Class(name="Replacement")
cobol_statements_Open = Class(name="cobol::statements::Open")
cobol_statements_SearchStatement = Class(name="cobol::statements::SearchStatement", is_abstract=True)
NormalEvaluateCase = Class(name="NormalEvaluateCase")
cobol_statements_SerialSearch = Class(name="cobol::statements::SerialSearch")
SearchStatement = Class(name="SearchStatement")
cobol_statements_BinarySearch = Class(name="cobol::statements::BinarySearch")
cobol_statements_Unstring = Class(name="cobol::statements::Unstring")
cobol_statements_Call = Class(name="cobol::statements::Call")
functions_Argumentable = Class(name="functions::Argumentable")
cobol_statements_Evaluate = Class(name="cobol::statements::Evaluate")
EvaluateCase = Class(name="EvaluateCase")
ExpressionList = Class(name="ExpressionList")
cobol_statements_NormalEvaluateCase = Class(name="cobol::statements::NormalEvaluateCase")
cobol_statements_OtherEvaluateCase = Class(name="cobol::statements::OtherEvaluateCase")
cobol_statements_EvaluateCase = Class(name="cobol::statements::EvaluateCase", is_abstract=True)
NestedStatement = Class(name="NestedStatement")
cobol_statements_Replace = Class(name="cobol::statements::Replace")
cobol_statements_Entry = Class(name="cobol::statements::Entry")
cobol_statements_Inspect = Class(name="cobol::statements::Inspect")
TallyingIn = Class(name="TallyingIn")
cobol_statements_Set = Class(name="cobol::statements::Set")
cobol_statements_Read = Class(name="cobol::statements::Read")
SplittedString = Class(name="SplittedString")
cobol_statements_Write = Class(name="cobol::statements::Write")
IntegerLiteral = Class(name="IntegerLiteral")
MnemonicNameReference = Class(name="MnemonicNameReference")
cobol_statements_Rewrite = Class(name="cobol::statements::Rewrite")
Write = Class(name="Write")
cobol_statements_SwitchStatus = Class(name="cobol::statements::SwitchStatus")
cobol_statements_PerformProcedureFixedTimes = Class(name="cobol::statements::PerformProcedureFixedTimes")
statements_PerformProcedure = Class(name="statements::PerformProcedure")
statements_PerformFixedTimes = Class(name="statements::PerformFixedTimes")
cobol_statements_PerformUntilCondition = Class(name="cobol::statements::PerformUntilCondition", is_abstract=True)
statements_VaryingUntilCondition = Class(name="statements::VaryingUntilCondition")
cobol_statements_PerformFixedTimes = Class(name="cobol::statements::PerformFixedTimes", is_abstract=True)
AfterUntilCondition = Class(name="AfterUntilCondition")
cobol_statements_PerformNestedStatementFixedTimes = Class(name="cobol::statements::PerformNestedStatementFixedTimes")
statements_PerformNestedStatement = Class(name="statements::PerformNestedStatement")
cobol_statements_PerformNestedStatementUntilCondition = Class(name="cobol::statements::PerformNestedStatementUntilCondition")
cobol_statements_Continue = Class(name="cobol::statements::Continue")
cobol_statements_FileIOStatement = Class(name="cobol::statements::FileIOStatement", is_abstract=True)
InputDirective = Class(name="InputDirective")
OutputDirective = Class(name="OutputDirective")
KeyDescriptor = Class(name="KeyDescriptor")
cobol_statements_Sort = Class(name="cobol::statements::Sort")
statements_FileIOStatement = Class(name="statements::FileIOStatement")
cobol_statements_Merge = Class(name="cobol::statements::Merge")
cobol_statements_Release = Class(name="cobol::statements::Release")
cobol_statements_KeyDescriptor = Class(name="cobol::statements::KeyDescriptor")
cobol_statements_IOStatement = Class(name="cobol::statements::IOStatement", is_abstract=True)
IOFileDescriptor = Class(name="IOFileDescriptor")
cobol_statements_PerformProcedureUntilCondition = Class(name="cobol::statements::PerformProcedureUntilCondition")
statements_PerformUntilCondition = Class(name="statements::PerformUntilCondition")
cobol_statements_IOFile = Class(name="cobol::statements::IOFile")
IncompleteElement = Class(name="IncompleteElement")
cobol_statements_TallyingIn = Class(name="cobol::statements::TallyingIn")
Tallying = Class(name="Tallying")
cobol_statements_Delete = Class(name="cobol::statements::Delete")
cobol_identifiers_Subscript = Class(name="cobol::identifiers::Subscript", is_abstract=True)
cobol_identifiers_Identifier = Class(name="cobol::identifiers::Identifier", is_abstract=True)
water_AcceptStatementWater = Class(name="water::AcceptStatementWater")
water_RepositoryParagraphWater = Class(name="water::RepositoryParagraphWater")
water_IdentificationDivisionWater = Class(name="water::IdentificationDivisionWater")
water_SQLStatementWater = Class(name="water::SQLStatementWater")
cobol_statements_IOFileDescriptor = Class(name="cobol::statements::IOFileDescriptor")
IOFile = Class(name="IOFile")
cobol_statements_VaryingUntilCondition = Class(name="cobol::statements::VaryingUntilCondition", is_abstract=True)
Conditional = Class(name="Conditional")
cobol_statements_AfterUntilCondition = Class(name="cobol::statements::AfterUntilCondition")
VaryingUntilCondition = Class(name="VaryingUntilCondition")
cobol_statements_Start = Class(name="cobol::statements::Start")
cobol_identifiers_Qualifier = Class(name="cobol::identifiers::Qualifier")
cobol_identifiers_RelativeSubscript = Class(name="cobol::identifiers::RelativeSubscript")
cobol_identifiers_DirectSubscript = Class(name="cobol::identifiers::DirectSubscript")
cobol_ios_InputProcedure = Class(name="cobol::ios::InputProcedure")
ios_InputDirective = Class(name="ios::InputDirective")
ios_ProcedureDirective = Class(name="ios::ProcedureDirective")
cobol_ios_InputDirective = Class(name="cobol::ios::InputDirective", is_abstract=True)
IODirectives = Class(name="IODirectives")
cobol_ios_InputFile = Class(name="cobol::ios::InputFile")
ios_FileDirective = Class(name="ios::FileDirective")
water_UseStatementWater = Class(name="water::UseStatementWater")
water_DataDescriptorWater = Class(name="water::DataDescriptorWater")
water_SortPhraseWater = Class(name="water::SortPhraseWater")
ReferenceModifier = Class(name="ReferenceModifier")
cobol_identifiers_IdentifierReference = Class(name="cobol::identifiers::IdentifierReference")
identifiers_Identifier = Class(name="identifiers::Identifier")
Subscript = Class(name="Subscript")
Qualifier = Class(name="Qualifier")
cobol_identifiers_All = Class(name="cobol::identifiers::All")
DirectSubscript = Class(name="DirectSubscript")
cobol_identifiers_ReferenceModifier = Class(name="cobol::identifiers::ReferenceModifier")
cobol_identifiers_LinageCounter = Class(name="cobol::identifiers::LinageCounter")
cobol_water_Dot = Class(name="cobol::water::Dot")
cobol_ios_OutputDirective = Class(name="cobol::ios::OutputDirective", is_abstract=True)
cobol_ios_OutputProcedure = Class(name="cobol::ios::OutputProcedure")
ios_OutputDirective = Class(name="ios::OutputDirective")
cobol_ios_OutputFile = Class(name="cobol::ios::OutputFile")
cobol_ios_IODirectives = Class(name="cobol::ios::IODirectives", is_abstract=True)
cobol_ios_FileDirective = Class(name="cobol::ios::FileDirective", is_abstract=True)
cobol_ios_ProcedureDirective = Class(name="cobol::ios::ProcedureDirective", is_abstract=True)
Label = Class(name="Label")
cobol_water_IncompleteElement = Class(name="cobol::water::IncompleteElement", is_abstract=True)
Water = Class(name="Water")
cobol_water_IdentificationDivisionWater = Class(name="cobol::water::IdentificationDivisionWater", is_abstract=True)
cobol_water_Water = Class(name="cobol::water::Water", is_abstract=True)
cobol_water_ProgramDescription = Class(name="cobol::water::ProgramDescription")
IdentificationDivisionWater = Class(name="IdentificationDivisionWater")
cobol_water_SpecialNamesParagraphWater = Class(name="cobol::water::SpecialNamesParagraphWater", is_abstract=True)
cobol_water_SpecialNamesClause = Class(name="cobol::water::SpecialNamesClause")
cobol_water_FileDescriptorWater = Class(name="cobol::water::FileDescriptorWater", is_abstract=True)
cobol_water_ObjectComputerParagraphWater = Class(name="cobol::water::ObjectComputerParagraphWater", is_abstract=True)
cobol_water_ObjectComputerDescription = Class(name="cobol::water::ObjectComputerDescription")
ObjectComputerParagraphWater = Class(name="ObjectComputerParagraphWater")
cobol_water_PriorityNumber = Class(name="cobol::water::PriorityNumber")
cobol_water_SelectStatementWater = Class(name="cobol::water::SelectStatementWater", is_abstract=True)
cobol_water_SelectStatementClause = Class(name="cobol::water::SelectStatementClause")
SelectStatementWater = Class(name="SelectStatementWater")
cobol_water_FileDescription = Class(name="cobol::water::FileDescription")
FileDescriptorWater = Class(name="FileDescriptorWater")
cobol_water_DataDescriptorWater = Class(name="cobol::water::DataDescriptorWater", is_abstract=True)
cobol_water_DataDescription = Class(name="cobol::water::DataDescription")
DataDescriptorWater = Class(name="DataDescriptorWater")
cobol_water_IOControlParagraphWater = Class(name="cobol::water::IOControlParagraphWater", is_abstract=True)
cobol_water_IOControlDescription = Class(name="cobol::water::IOControlDescription")
IOControlParagraphWater = Class(name="IOControlParagraphWater")
cobol_water_RepositoryParagraphWater = Class(name="cobol::water::RepositoryParagraphWater", is_abstract=True)
cobol_water_RepositoryDescription = Class(name="cobol::water::RepositoryDescription")
RepositoryParagraphWater = Class(name="RepositoryParagraphWater")
cobol_water_SQLStatementWater = Class(name="cobol::water::SQLStatementWater", is_abstract=True)
cobol_water_CICSStatementWater = Class(name="cobol::water::CICSStatementWater", is_abstract=True)
cobol_water_SQLStatementToken = Class(name="cobol::water::SQLStatementToken")
SQLStatementWater = Class(name="SQLStatementWater")
cobol_water_CICSStatementToken = Class(name="cobol::water::CICSStatementToken")
CICSStatementWater = Class(name="CICSStatementWater")
cobol_water_AcceptStatementWater = Class(name="cobol::water::AcceptStatementWater", is_abstract=True)
cobol_water_AcceptStatementToken = Class(name="cobol::water::AcceptStatementToken")
AcceptStatementWater = Class(name="AcceptStatementWater")
cobol_water_UseStatementWater = Class(name="cobol::water::UseStatementWater", is_abstract=True)
cobol_water_UseStatementToken = Class(name="cobol::water::UseStatementToken")
UseStatementWater = Class(name="UseStatementWater")
cobol_water_InvokeStatementWater = Class(name="cobol::water::InvokeStatementWater", is_abstract=True)
cobol_water_InvokeStatementToken = Class(name="cobol::water::InvokeStatementToken")
InvokeStatementWater = Class(name="InvokeStatementWater")
cobol_water_CloseStatementWater = Class(name="cobol::water::CloseStatementWater", is_abstract=True)
cobol_water_CloseStatementToken = Class(name="cobol::water::CloseStatementToken")
CloseStatementWater = Class(name="CloseStatementWater")
cobol_water_OpenStatementWater = Class(name="cobol::water::OpenStatementWater", is_abstract=True)
cobol_water_OpenStatementToken = Class(name="cobol::water::OpenStatementToken")
OpenStatementWater = Class(name="OpenStatementWater")
cobol_water_SortPhraseToken = Class(name="cobol::water::SortPhraseToken")
SortPhraseWater = Class(name="SortPhraseWater")
cobol_water_SortPhraseWater = Class(name="cobol::water::SortPhraseWater", is_abstract=True)
cobol_registers_ShiftIn = Class(name="cobol::registers::ShiftIn")
Register = Class(name="Register")
cobol_registers_ShiftOut = Class(name="cobol::registers::ShiftOut")
cobol_registers_AddressOf = Class(name="cobol::registers::AddressOf")
cobol_registers_LengthOf = Class(name="cobol::registers::LengthOf")
cobol_registers_ReturnCode = Class(name="cobol::registers::ReturnCode")
cobol_registers_WhenCompiled = Class(name="cobol::registers::WhenCompiled")
cobol_environments_SystemDevice = Class(name="cobol::environments::SystemDevice", is_abstract=True)
cobol_environments_SystemLogicalInput = Class(name="cobol::environments::SystemLogicalInput")
SystemDevice = Class(name="SystemDevice")
cobol_environments_UPSI = Class(name="cobol::environments::UPSI")
cobol_environments_SystemPunchDevice = Class(name="cobol::environments::SystemPunchDevice")
cobol_registers_Register = Class(name="cobol::registers::Register", is_abstract=True)
cobol_environments_Console = Class(name="cobol::environments::Console")
cobol_environments_Channel = Class(name="cobol::environments::Channel")
cobol_environments_AdvancedFunctionPrinting = Class(name="cobol::environments::AdvancedFunctionPrinting")
cobol_environments_SuppressSpacing = Class(name="cobol::environments::SuppressSpacing")
cobol_environments_Pocket = Class(name="cobol::environments::Pocket")
cobol_environments_SystemLogicalOutput = Class(name="cobol::environments::SystemLogicalOutput")
cobol_environments_Environment = Class(name="cobol::environments::Environment", is_abstract=True)
RangeExpression = Class(name="RangeExpression")
cobol_dataitems_ConditionName = Class(name="cobol::dataitems::ConditionName")
cobol_dataitems_Global = Class(name="cobol::dataitems::Global")
cobol_dataitems_External = Class(name="cobol::dataitems::External")
cobol_dataitems_Value = Class(name="cobol::dataitems::Value")
cobol_dataitems_DataItemAttribute = Class(name="cobol::dataitems::DataItemAttribute", is_abstract=True)
cobol_dataitems_Usage = Class(name="cobol::dataitems::Usage")
cobol_dataitems_GroupUsage = Class(name="cobol::dataitems::GroupUsage")
cobol_dataitems_DataItem = Class(name="cobol::dataitems::DataItem")
references_ReferenceableElement = Class(name="references::ReferenceableElement")
cobol_dataitems_PictureString = Class(name="cobol::dataitems::PictureString")
DataItemAttribute = Class(name="DataItemAttribute")
cobol_dataitems_RenamingDataName = Class(name="cobol::dataitems::RenamingDataName")
DataName = Class(name="DataName")
cobol_dataitems_RecordName = Class(name="cobol::dataitems::RecordName")
cobol_dataitems_DataName = Class(name="cobol::dataitems::DataName")
cobol_dataitems_Redefines = Class(name="cobol::dataitems::Redefines")
specialnames_SpecialName = Class(name="specialnames::SpecialName")
cobol_specialnames_OnStatus = Class(name="cobol::specialnames::OnStatus")
ConditionName = Class(name="ConditionName")
cobol_specialnames_OffStatus = Class(name="cobol::specialnames::OffStatus")
cobol_specialnames_AlphabetName = Class(name="cobol::specialnames::AlphabetName")
specialnames_SpecialNameStatement = Class(name="specialnames::SpecialNameStatement")
AlphabetType = Class(name="AlphabetType")
cobol_specialnames_UPSISwitchIs = Class(name="cobol::specialnames::UPSISwitchIs")
specialnames_MnemonicName = Class(name="specialnames::MnemonicName")
cobol_specialnames_AlphabetType = Class(name="cobol::specialnames::AlphabetType", is_abstract=True)
cobol_specialnames_PredefinedAlphabetType = Class(name="cobol::specialnames::PredefinedAlphabetType")
cobol_specialnames_ExplicitAlphabetType = Class(name="cobol::specialnames::ExplicitAlphabetType")
cobol_specialnames_SpecialName = Class(name="cobol::specialnames::SpecialName", is_abstract=True)
cobol_specialnames_ConditionName = Class(name="cobol::specialnames::ConditionName", is_abstract=True)
cobol_specialnames_CodeNameAlphabetType = Class(name="cobol::specialnames::CodeNameAlphabetType")
cobol_specialnames_CurrencySign = Class(name="cobol::specialnames::CurrencySign")
cobol_specialnames_ClassName = Class(name="cobol::specialnames::ClassName")
cobol_specialnames_MnemonicName = Class(name="cobol::specialnames::MnemonicName", is_abstract=True)
SpecialName = Class(name="SpecialName")
cobol_specialnames_SystemDeviceIs = Class(name="cobol::specialnames::SystemDeviceIs")
cobol_specialnames_SymbolicCharacter = Class(name="cobol::specialnames::SymbolicCharacter")
SymbolicCharacter = Class(name="SymbolicCharacter")
AlphabetNameReference = Class(name="AlphabetNameReference")
cobol_specialnames_SpecialNameStatement = Class(name="cobol::specialnames::SpecialNameStatement", is_abstract=True)
cobol_tables_Table = Class(name="cobol::tables::Table")
dataitems_DataItem = Class(name="dataitems::DataItem")
TableDimension = Class(name="TableDimension")
IndexName = Class(name="IndexName")
KeyName = Class(name="KeyName")
cobol_tables_KeyName = Class(name="cobol::tables::KeyName")
cobol_tables_IndexName = Class(name="cobol::tables::IndexName")
AdditionalIndexName = Class(name="AdditionalIndexName")
cobol_tables_TableDimension = Class(name="cobol::tables::TableDimension")
cobol_specialnames_SymbolicCharacterStatement = Class(name="cobol::specialnames::SymbolicCharacterStatement")
cobol_tables_AdditionalIndexName = Class(name="cobol::tables::AdditionalIndexName")
cobol_files_FileName = Class(name="cobol::files::FileName")
cobol_files_SelectStatement = Class(name="cobol::files::SelectStatement")
FileStatus = Class(name="FileStatus")
cobol_files_FileStatus = Class(name="cobol::files::FileStatus")
cobol_parameters_Parametrizable = Class(name="cobol::parameters::Parametrizable", is_abstract=True)
Parameter_ = Class(name="Parameter")
cobol_parameters_Parameter = Class(name="cobol::parameters::Parameter", is_abstract=True)
cobol_declaratives_Declaratives = Class(name="cobol::declaratives::Declaratives")
DeclarativeSection = Class(name="DeclarativeSection")
cobol_verbs_Is = Class(name="cobol::verbs::Is")
Verb = Class(name="Verb")
cobol_verbs_Verb = Class(name="cobol::verbs::Verb", is_abstract=True)
cobol_labels_ProcedureRange = Class(name="cobol::labels::ProcedureRange")
ProcedureRangeChild = Class(name="ProcedureRangeChild")
cobol_labels_ProcedureRangeLabel = Class(name="cobol::labels::ProcedureRangeLabel", is_abstract=True)
cobol_labels_ProcedureRangeChild = Class(name="cobol::labels::ProcedureRangeChild", is_abstract=True)
Procedure = Class(name="Procedure")
cobol_labels_ProcedureLabel = Class(name="cobol::labels::ProcedureLabel")
cobol_labels_Procedure = Class(name="cobol::labels::Procedure", is_abstract=True)
cobol_labels_Label = Class(name="cobol::labels::Label", is_abstract=True)
cobol_labels_StopLabel = Class(name="cobol::labels::StopLabel", is_abstract=True)
cobol_labels_Run = Class(name="cobol::labels::Run")
cobol_functions_FunctionCall = Class(name="cobol::functions::FunctionCall")
cobol_functions_Argument = Class(name="cobol::functions::Argument", is_abstract=True)
cobol_functions_ByReferenceArgument = Class(name="cobol::functions::ByReferenceArgument")
Argument = Class(name="Argument")
cobol_functions_ByValueArgument = Class(name="cobol::functions::ByValueArgument")
cobol_functions_ByContentArgument = Class(name="cobol::functions::ByContentArgument")
cobol_functions_OmittedArgument = Class(name="cobol::functions::OmittedArgument")
cobol_functions_Argumentable = Class(name="cobol::functions::Argumentable", is_abstract=True)
cobol_parameters_ByReferenceParameter = Class(name="cobol::parameters::ByReferenceParameter")
cobol_parameters_ByValueParameter = Class(name="cobol::parameters::ByValueParameter")
cobol_handlers_OnSizeError = Class(name="cobol::handlers::OnSizeError")
cobol_handlers_Handler = Class(name="cobol::handlers::Handler", is_abstract=True)
cobol_handlers_NotOnSizeError = Class(name="cobol::handlers::NotOnSizeError")
NotErrorHandler = Class(name="NotErrorHandler")
cobol_handlers_OnOverflow = Class(name="cobol::handlers::OnOverflow")
cobol_handlers_OnException = Class(name="cobol::handlers::OnException")
cobol_handlers_NotOnException = Class(name="cobol::handlers::NotOnException")
cobol_handlers_NotErrorHandler = Class(name="cobol::handlers::NotErrorHandler", is_abstract=True)
cobol_handlers_NotOnOverflow = Class(name="cobol::handlers::NotOnOverflow")
cobol_handlers_NotAtEnd = Class(name="cobol::handlers::NotAtEnd")
cobol_handlers_AtEnd = Class(name="cobol::handlers::AtEnd")
cobol_handlers_AtEndOfPage = Class(name="cobol::handlers::AtEndOfPage")
cobol_handlers_InvalidKey = Class(name="cobol::handlers::InvalidKey")
cobol_handlers_NotAtEndOfPage = Class(name="cobol::handlers::NotAtEndOfPage")
cobol_handlers_NotInvalidKey = Class(name="cobol::handlers::NotInvalidKey")
cobol_strings_Tallying = Class(name="cobol::strings::Tallying", is_abstract=True)
StringManipulation = Class(name="StringManipulation")
cobol_strings_StringManipulation = Class(name="cobol::strings::StringManipulation", is_abstract=True)
String = Class(name="String")
Location = Class(name="Location")
cobol_strings_ManipulatedStrings = Class(name="cobol::strings::ManipulatedStrings", is_abstract=True)
cobol_strings_String = Class(name="cobol::strings::String", is_abstract=True)
cobol_strings_ConcatenatingStrings = Class(name="cobol::strings::ConcatenatingStrings")
ManipulatedStrings = Class(name="ManipulatedStrings")
cobol_strings_SplittedString = Class(name="cobol::strings::SplittedString")
cobol_strings_Replacement = Class(name="cobol::strings::Replacement", is_abstract=True)
cobol_strings_Occurrence = Class(name="cobol::strings::Occurrence", is_abstract=True)
cobol_strings_TallyingOccurrence = Class(name="cobol::strings::TallyingOccurrence")
strings_Tallying = Class(name="strings::Tallying")
strings_Occurrence = Class(name="strings::Occurrence")
cobol_strings_ReplacementOccurrence = Class(name="cobol::strings::ReplacementOccurrence")
strings_Replacement = Class(name="strings::Replacement")
cobol_strings_AnyCharacter = Class(name="cobol::strings::AnyCharacter")
cobol_strings_SpecificCharacter = Class(name="cobol::strings::SpecificCharacter")
cobol_strings_AnyCharacterBySpecificCharacter = Class(name="cobol::strings::AnyCharacterBySpecificCharacter")
cobol_strings_SpecificCharacterBySpecificCharacter = Class(name="cobol::strings::SpecificCharacterBySpecificCharacter")
cobol_strings_Location = Class(name="cobol::strings::Location")

# cobol_commons_NamedElement class attributes and methods
cobol_commons_NamedElement_name: Property = Property(name="name", type=StringType)
cobol_commons_NamedElement.attributes={cobol_commons_NamedElement_name}

# Commentable class attributes and methods

# cobol_commons_Commentable class attributes and methods

# cobol_commons_LabellableElement class attributes and methods
cobol_commons_LabellableElement_label: Property = Property(name="label", type=StringType)
cobol_commons_LabellableElement.attributes={cobol_commons_LabellableElement_label}

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

# Negate class attributes and methods

# cobol_conditions_NegatedConditionalExpressionChild class attributes and methods

# cobol_conditions_SimpleConditionChild class attributes and methods

# cobol_conditions_RelationalExpression class attributes and methods

# SimpleConditionChild class attributes and methods

# RelationalOperator class attributes and methods

# Is class attributes and methods

# cobol_conditions_ExpressionList class attributes and methods

# cobol_conditions_ConditionalAndExpressionChild class attributes and methods

# cobol_conditions_ConditionalAndExpression class attributes and methods

# cobol_conditions_AbbreviatedConditionalExpression class attributes and methods

# AbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_AbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_NegatedAbbreviatedConditionalExpression class attributes and methods

# cobol_conditions_NegatedAbbreviatedConditionalExpressionChild class attributes and methods

# cobol_conditions_AbbreviatedRelationalExpression class attributes and methods

# AbbreviatedRelationalExpressionChild class attributes and methods

# cobol_conditions_NestedAbbreviatedConditionalExpression class attributes and methods

# cobol_conditions_SignCondition class attributes and methods

# SignOperator class attributes and methods

# cobol_conditions_ClassCondition class attributes and methods

# ClassOperator class attributes and methods

# cobol_conditions_AbbreviatedRelationalExpressionChild class attributes and methods

# cobol_conditions_NestedCondition class attributes and methods

# NegatedAbbreviatedConditionalExpressionChild class attributes and methods

# AdditiveArithmeticExpressionChild class attributes and methods

# AdditiveOperator class attributes and methods

# cobol_arithmetics_AdditiveArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_MultiplicativeArithmeticExpression class attributes and methods

# MultiplicativeArithmeticExpressionChild class attributes and methods

# MultiplicativeOperator class attributes and methods

# cobol_arithmetics_MultiplicativeArithmeticExpressionChild class attributes and methods

# cobol_arithmetics_PowerArithmeticExpression class attributes and methods

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

# Through class attributes and methods

# cobol_arithmetics_AdditiveArithmeticExpression class attributes and methods

# RangeExpressionChild class attributes and methods

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

# cobol_divisions_IdentificationDivision class attributes and methods
cobol_divisions_IdentificationDivision_properties: Property = Property(name="properties", type=StringType)
cobol_divisions_IdentificationDivision.attributes={cobol_divisions_IdentificationDivision_properties}

# divisions_Division class attributes and methods

# water_IncompleteElement class attributes and methods

# cobol_divisions_ProcedureDivision class attributes and methods

# parameters_Parametrizable class attributes and methods

# cobol_arithmetics_RangeExpressionChild class attributes and methods

# Declaratives class attributes and methods

# cobol_literals_Literal class attributes and methods

# water_SelectStatementWater class attributes and methods

# water_SpecialNamesParagraphWater class attributes and methods

# water_CICSStatementWater class attributes and methods

# operands_PrimaryOperand class attributes and methods

# water_InvokeStatementWater class attributes and methods

# labels_StopLabel class attributes and methods

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

# cobol_literals_Space class attributes and methods
cobol_literals_Space_value: Property = Property(name="value", type=StringType)
cobol_literals_Space.attributes={cobol_literals_Space_value}

# cobol_literals_Any class attributes and methods

# cobol_literals_Characters class attributes and methods

# cobol_literals_AlphanumericHexaDecimalLiteral class attributes and methods

# AlphanumericLiteral class attributes and methods

# cobol_operators_Operator class attributes and methods

# cobol_operators_AdditiveOperator class attributes and methods

# Operator class attributes and methods

# cobol_operators_MultiplicativeOperator class attributes and methods

# cobol_operators_UnaryOperator class attributes and methods

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

# cobol_operators_GreaterThanOrEqual class attributes and methods
cobol_operators_GreaterThanOrEqual_than: Property = Property(name="than", type=BooleanType)
cobol_operators_GreaterThanOrEqual_to: Property = Property(name="to", type=BooleanType)
cobol_operators_GreaterThanOrEqual.attributes={cobol_operators_GreaterThanOrEqual_than, cobol_operators_GreaterThanOrEqual_to}

# cobol_operators_GreaterThan class attributes and methods
cobol_operators_GreaterThan_than: Property = Property(name="than", type=BooleanType)
cobol_operators_GreaterThan.attributes={cobol_operators_GreaterThan_than}

# cobol_operators_LessThan class attributes and methods
cobol_operators_LessThan_than: Property = Property(name="than", type=BooleanType)
cobol_operators_LessThan.attributes={cobol_operators_LessThan_than}

# cobol_operators_LessThanOrEqual class attributes and methods
cobol_operators_LessThanOrEqual_than: Property = Property(name="than", type=BooleanType)
cobol_operators_LessThanOrEqual_to: Property = Property(name="to", type=BooleanType)
cobol_operators_LessThanOrEqual.attributes={cobol_operators_LessThanOrEqual_than, cobol_operators_LessThanOrEqual_to}

# cobol_operators_Equal class attributes and methods
cobol_operators_Equal_to: Property = Property(name="to", type=BooleanType)
cobol_operators_Equal.attributes={cobol_operators_Equal_to}

# cobol_operators_Power class attributes and methods

# cobol_operators_Negate class attributes and methods

# cobol_operators_Through class attributes and methods
cobol_operators_Through_value: Property = Property(name="value", type=StringType)
cobol_operators_Through.attributes={cobol_operators_Through_value}

# cobol_operators_ClassOperator class attributes and methods

# cobol_operators_Zero class attributes and methods

# cobol_operators_ClassName class attributes and methods

# cobol_operators_Alphabetic class attributes and methods

# cobol_operators_DBCS class attributes and methods

# cobol_operators_Numeric class attributes and methods

# cobol_operators_AlphabeticUpper class attributes and methods

# cobol_operators_AlphabeticLower class attributes and methods

# cobol_operators_LogicalOperator class attributes and methods

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

# cobol_paragraphs_ConfigurationSectionParagraph class attributes and methods

# cobol_paragraphs_IOSectionParagraph class attributes and methods

# cobol_paragraphs_SpecialNamesParagraph class attributes and methods

# SpecialNameStatement class attributes and methods

# cobol_paragraphs_DebuggingMode class attributes and methods

# cobol_references_Reference class attributes and methods

# cobol_references_ReferenceableElement class attributes and methods

# ReferenceableElement class attributes and methods

# cobol_references_ElementReference class attributes and methods

# Reference class attributes and methods

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

# cobol_sections_WorkingStorageSection class attributes and methods

# DataDivisionSection class attributes and methods

# cobol_sections_LocalStorageSection class attributes and methods

# SpecialNamesParagraphWater class attributes and methods

# cobol_sections_LinkageStorageSection class attributes and methods

# cobol_sections_IOSection class attributes and methods

# EnvironmentDivisionSection class attributes and methods

# cobol_paragraphs_RepositoryParagraph class attributes and methods

# cobol_sections_EnvironmentDivisionSection class attributes and methods

# cobol_sections_DataDivisionSection class attributes and methods

# Statement class attributes and methods

# DataItem class attributes and methods

# cobol_sections_FileSection class attributes and methods

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

# cobol_sections_ConfigurationSection class attributes and methods

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

# cobol_statements_ArithmeticStatement class attributes and methods
cobol_statements_ArithmeticStatement_corresponding: Property = Property(name="corresponding", type=StringType)
cobol_statements_ArithmeticStatement.attributes={cobol_statements_ArithmeticStatement_corresponding}

# statements_Statement class attributes and methods

# statements_ErrorHandled class attributes and methods

# cobol_statements_Add class attributes and methods

# ArithmeticStatement class attributes and methods

# cobol_statements_Subtract class attributes and methods

# cobol_statements_Multiply class attributes and methods

# cobol_operands_RoundedIdentifier class attributes and methods

# ArithmeticOperand class attributes and methods

# Identifier class attributes and methods

# cobol_statements_Perform class attributes and methods

# cobol_statements_PerformNestedStatement class attributes and methods

# statements_Perform class attributes and methods

# statements_NestedStatement class attributes and methods

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

# cobol_statements_Exit class attributes and methods
cobol_statements_Exit_exitLabel: Property = Property(name="exitLabel", type=StringType)
cobol_statements_Exit.attributes={cobol_statements_Exit_exitLabel}

# cobol_statements_Condition class attributes and methods

# cobol_statements_Divide class attributes and methods

# statements_Conditional class attributes and methods

# cobol_statements_Conditional class attributes and methods

# cobol_statements_Stop class attributes and methods

# StopLabel class attributes and methods

# cobol_statements_Display class attributes and methods

# Environment class attributes and methods

# cobol_statements_Compute class attributes and methods

# AssignmentExpression class attributes and methods

# cobol_statements_Accept class attributes and methods

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

# cobol_statements_Initialize class attributes and methods

# Replacement class attributes and methods

# cobol_statements_Open class attributes and methods

# cobol_statements_SearchStatement class attributes and methods

# NormalEvaluateCase class attributes and methods

# cobol_statements_SerialSearch class attributes and methods

# SearchStatement class attributes and methods

# cobol_statements_BinarySearch class attributes and methods

# cobol_statements_Unstring class attributes and methods

# cobol_statements_Call class attributes and methods

# functions_Argumentable class attributes and methods

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

# TallyingIn class attributes and methods

# cobol_statements_Set class attributes and methods

# cobol_statements_Read class attributes and methods

# SplittedString class attributes and methods

# cobol_statements_Write class attributes and methods

# IntegerLiteral class attributes and methods

# MnemonicNameReference class attributes and methods

# cobol_statements_Rewrite class attributes and methods

# Write class attributes and methods

# cobol_statements_SwitchStatus class attributes and methods
cobol_statements_SwitchStatus_status: Property = Property(name="status", type=StringType)
cobol_statements_SwitchStatus.attributes={cobol_statements_SwitchStatus_status}

# cobol_statements_PerformProcedureFixedTimes class attributes and methods

# statements_PerformProcedure class attributes and methods

# statements_PerformFixedTimes class attributes and methods

# cobol_statements_PerformUntilCondition class attributes and methods
cobol_statements_PerformUntilCondition_position: Property = Property(name="position", type=StringType)
cobol_statements_PerformUntilCondition.attributes={cobol_statements_PerformUntilCondition_position}

# statements_VaryingUntilCondition class attributes and methods

# cobol_statements_PerformFixedTimes class attributes and methods

# AfterUntilCondition class attributes and methods

# cobol_statements_PerformNestedStatementFixedTimes class attributes and methods

# statements_PerformNestedStatement class attributes and methods

# cobol_statements_PerformNestedStatementUntilCondition class attributes and methods

# cobol_statements_Continue class attributes and methods

# cobol_statements_FileIOStatement class attributes and methods

# InputDirective class attributes and methods

# OutputDirective class attributes and methods

# KeyDescriptor class attributes and methods

# cobol_statements_Sort class attributes and methods

# statements_FileIOStatement class attributes and methods

# cobol_statements_Merge class attributes and methods

# cobol_statements_Release class attributes and methods

# cobol_statements_KeyDescriptor class attributes and methods
cobol_statements_KeyDescriptor_order: Property = Property(name="order", type=StringType)
cobol_statements_KeyDescriptor.attributes={cobol_statements_KeyDescriptor_order}

# cobol_statements_IOStatement class attributes and methods

# IOFileDescriptor class attributes and methods

# cobol_statements_PerformProcedureUntilCondition class attributes and methods

# statements_PerformUntilCondition class attributes and methods

# cobol_statements_IOFile class attributes and methods

# IncompleteElement class attributes and methods

# cobol_statements_TallyingIn class attributes and methods

# Tallying class attributes and methods

# cobol_statements_Delete class attributes and methods

# cobol_identifiers_Subscript class attributes and methods

# cobol_identifiers_Identifier class attributes and methods

# water_AcceptStatementWater class attributes and methods

# water_RepositoryParagraphWater class attributes and methods

# water_IdentificationDivisionWater class attributes and methods

# water_SQLStatementWater class attributes and methods

# cobol_statements_IOFileDescriptor class attributes and methods
cobol_statements_IOFileDescriptor_type: Property = Property(name="type", type=StringType)
cobol_statements_IOFileDescriptor.attributes={cobol_statements_IOFileDescriptor_type}

# IOFile class attributes and methods

# cobol_statements_VaryingUntilCondition class attributes and methods

# Conditional class attributes and methods

# cobol_statements_AfterUntilCondition class attributes and methods

# VaryingUntilCondition class attributes and methods

# cobol_statements_Start class attributes and methods

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

# water_UseStatementWater class attributes and methods

# water_DataDescriptorWater class attributes and methods

# water_SortPhraseWater class attributes and methods

# ReferenceModifier class attributes and methods

# cobol_identifiers_IdentifierReference class attributes and methods

# identifiers_Identifier class attributes and methods

# Subscript class attributes and methods

# Qualifier class attributes and methods

# cobol_identifiers_All class attributes and methods

# DirectSubscript class attributes and methods

# cobol_identifiers_ReferenceModifier class attributes and methods

# cobol_identifiers_LinageCounter class attributes and methods

# cobol_water_Dot class attributes and methods

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

# cobol_water_ProgramDescription class attributes and methods
cobol_water_ProgramDescription_value: Property = Property(name="value", type=StringType)
cobol_water_ProgramDescription.attributes={cobol_water_ProgramDescription_value}

# IdentificationDivisionWater class attributes and methods

# cobol_water_SpecialNamesParagraphWater class attributes and methods

# cobol_water_SpecialNamesClause class attributes and methods
cobol_water_SpecialNamesClause_value: Property = Property(name="value", type=StringType)
cobol_water_SpecialNamesClause.attributes={cobol_water_SpecialNamesClause_value}

# cobol_water_FileDescriptorWater class attributes and methods

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

# cobol_water_InvokeStatementWater class attributes and methods

# cobol_water_InvokeStatementToken class attributes and methods
cobol_water_InvokeStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_InvokeStatementToken.attributes={cobol_water_InvokeStatementToken_value}

# InvokeStatementWater class attributes and methods

# cobol_water_CloseStatementWater class attributes and methods

# cobol_water_CloseStatementToken class attributes and methods
cobol_water_CloseStatementToken_value: Property = Property(name="value", type=StringType)
cobol_water_CloseStatementToken.attributes={cobol_water_CloseStatementToken_value}

# CloseStatementWater class attributes and methods

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

# cobol_environments_UPSI class attributes and methods
cobol_environments_UPSI_value: Property = Property(name="value", type=StringType)
cobol_environments_UPSI.attributes={cobol_environments_UPSI_value}

# cobol_environments_SystemPunchDevice class attributes and methods
cobol_environments_SystemPunchDevice_value: Property = Property(name="value", type=StringType)
cobol_environments_SystemPunchDevice.attributes={cobol_environments_SystemPunchDevice_value}

# cobol_registers_Register class attributes and methods

# cobol_environments_Console class attributes and methods

# cobol_environments_Channel class attributes and methods
cobol_environments_Channel_value: Property = Property(name="value", type=StringType)
cobol_environments_Channel.attributes={cobol_environments_Channel_value}

# cobol_environments_AdvancedFunctionPrinting class attributes and methods

# cobol_environments_SuppressSpacing class attributes and methods

# cobol_environments_Pocket class attributes and methods
cobol_environments_Pocket_value: Property = Property(name="value", type=StringType)
cobol_environments_Pocket.attributes={cobol_environments_Pocket_value}

# cobol_environments_SystemLogicalOutput class attributes and methods
cobol_environments_SystemLogicalOutput_value: Property = Property(name="value", type=StringType)
cobol_environments_SystemLogicalOutput.attributes={cobol_environments_SystemLogicalOutput_value}

# cobol_environments_Environment class attributes and methods

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

# cobol_dataitems_PictureString class attributes and methods
cobol_dataitems_PictureString_picture: Property = Property(name="picture", type=StringType)
cobol_dataitems_PictureString.attributes={cobol_dataitems_PictureString_picture}

# DataItemAttribute class attributes and methods

# cobol_dataitems_RenamingDataName class attributes and methods

# DataName class attributes and methods

# cobol_dataitems_RecordName class attributes and methods

# cobol_dataitems_DataName class attributes and methods

# cobol_dataitems_Redefines class attributes and methods

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

# cobol_specialnames_ExplicitAlphabetType class attributes and methods

# cobol_specialnames_SpecialName class attributes and methods

# cobol_specialnames_ConditionName class attributes and methods

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

# SymbolicCharacter class attributes and methods

# AlphabetNameReference class attributes and methods

# cobol_specialnames_SpecialNameStatement class attributes and methods

# cobol_tables_Table class attributes and methods

# dataitems_DataItem class attributes and methods

# TableDimension class attributes and methods

# IndexName class attributes and methods

# KeyName class attributes and methods

# cobol_tables_KeyName class attributes and methods
cobol_tables_KeyName_keyOrder: Property = Property(name="keyOrder", type=StringType)
cobol_tables_KeyName.attributes={cobol_tables_KeyName_keyOrder}

# cobol_tables_IndexName class attributes and methods

# AdditionalIndexName class attributes and methods

# cobol_tables_TableDimension class attributes and methods
cobol_tables_TableDimension_value: Property = Property(name="value", type=IntegerType)
cobol_tables_TableDimension.attributes={cobol_tables_TableDimension_value}

# cobol_specialnames_SymbolicCharacterStatement class attributes and methods

# cobol_tables_AdditionalIndexName class attributes and methods

# cobol_files_FileName class attributes and methods
cobol_files_FileName_fileDescriptor: Property = Property(name="fileDescriptor", type=StringType)
cobol_files_FileName.attributes={cobol_files_FileName_fileDescriptor}

# cobol_files_SelectStatement class attributes and methods
cobol_files_SelectStatement_isOptional: Property = Property(name="isOptional", type=BooleanType)
cobol_files_SelectStatement_externalFileNames: Property = Property(name="externalFileNames", type=StringType)
cobol_files_SelectStatement.attributes={cobol_files_SelectStatement_externalFileNames, cobol_files_SelectStatement_isOptional}

# FileStatus class attributes and methods

# cobol_files_FileStatus class attributes and methods

# cobol_parameters_Parametrizable class attributes and methods

# Parameter class attributes and methods

# cobol_parameters_Parameter class attributes and methods

# cobol_declaratives_Declaratives class attributes and methods

# DeclarativeSection class attributes and methods

# cobol_verbs_Is class attributes and methods

# Verb class attributes and methods

# cobol_verbs_Verb class attributes and methods

# cobol_labels_ProcedureRange class attributes and methods

# ProcedureRangeChild class attributes and methods

# cobol_labels_ProcedureRangeLabel class attributes and methods

# cobol_labels_ProcedureRangeChild class attributes and methods

# Procedure class attributes and methods

# cobol_labels_ProcedureLabel class attributes and methods

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

# cobol_parameters_ByReferenceParameter class attributes and methods

# cobol_parameters_ByValueParameter class attributes and methods

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

# cobol_handlers_InvalidKey class attributes and methods

# cobol_handlers_NotAtEndOfPage class attributes and methods

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

# cobol_strings_Replacement class attributes and methods

# cobol_strings_Occurrence class attributes and methods
cobol_strings_Occurrence_type: Property = Property(name="type", type=StringType)
cobol_strings_Occurrence.attributes={cobol_strings_Occurrence_type}

# cobol_strings_TallyingOccurrence class attributes and methods

# strings_Tallying class attributes and methods

# strings_Occurrence class attributes and methods

# cobol_strings_ReplacementOccurrence class attributes and methods

# strings_Replacement class attributes and methods

# cobol_strings_AnyCharacter class attributes and methods

# cobol_strings_SpecificCharacter class attributes and methods

# cobol_strings_AnyCharacterBySpecificCharacter class attributes and methods

# cobol_strings_SpecificCharacterBySpecificCharacter class attributes and methods

# cobol_strings_Location class attributes and methods
cobol_strings_Location_position: Property = Property(name="position", type=StringType)
cobol_strings_Location_initial: Property = Property(name="initial", type=BooleanType)
cobol_strings_Location.attributes={cobol_strings_Location_position, cobol_strings_Location_initial}

# Relationships
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
is12: BinaryAssociation = BinaryAssociation(
    name="is12",
    ends={
        Property(name="Is", type=cobol_conditions_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_RelationalExpression13", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
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
is28: BinaryAssociation = BinaryAssociation(
    name="is28",
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
is43: BinaryAssociation = BinaryAssociation(
    name="is43",
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
is53: BinaryAssociation = BinaryAssociation(
    name="is53",
    ends={
        Property(name="Is55", type=cobol_conditions_ClassCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_ClassCondition54", type=Is, multiplicity=Multiplicity(1, 1), is_composite=True)
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
negateOperator18: BinaryAssociation = BinaryAssociation(
    name="negateOperator18",
    ends={
        Property(name="Negate20", type=cobol_conditions_NegatedAbbreviatedConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_conditions_NegatedAbbreviatedConditionalExpression19", type=Negate, multiplicity=Multiplicity(1, 1), is_composite=True)
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
declaratives95: BinaryAssociation = BinaryAssociation(
    name="declaratives95",
    ends={
        Property(name="Declaratives", type=cobol_divisions_ProcedureDivision, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_divisions_ProcedureDivision", type=Declaratives, multiplicity=Multiplicity(0, 1), is_composite=True)
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
aliasesTo104: BinaryAssociation = BinaryAssociation(
    name="aliasesTo104",
    ends={
        Property(name="references", type=cobol_references_ReferenceableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ReferenceableElement", type=ReferenceableElement, multiplicity=Multiplicity(0, 9999))
    }
)
aliasesFrom105: BinaryAssociation = BinaryAssociation(
    name="aliasesFrom105",
    ends={
        Property(name="references107", type=cobol_references_ReferenceableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="ReferenceableElement106", type=ReferenceableElement, multiplicity=Multiplicity(0, 9999))
    }
)
target108: BinaryAssociation = BinaryAssociation(
    name="target108",
    ends={
        Property(name="ReferenceableElement109", type=cobol_references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(1, 1))
    }
)
qualifier110: BinaryAssociation = BinaryAssociation(
    name="qualifier110",
    ends={
        Property(name="ElementReference", type=cobol_references_Qualifiable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_references_Qualifiable", type=ElementReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sentences111: BinaryAssociation = BinaryAssociation(
    name="sentences111",
    ends={
        Property(name="StatementContainer112", type=cobol_sections_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_Section", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraphs113: BinaryAssociation = BinaryAssociation(
    name="paragraphs113",
    ends={
        Property(name="Paragraph115", type=cobol_sections_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_Section114", type=Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
statements116: BinaryAssociation = BinaryAssociation(
    name="statements116",
    ends={
        Property(name="Statement", type=cobol_sections_DataDivisionSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_DataDivisionSection", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records117: BinaryAssociation = BinaryAssociation(
    name="records117",
    ends={
        Property(name="DataItem", type=cobol_sections_DataDivisionSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_DataDivisionSection118", type=DataItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileDescriptors119: BinaryAssociation = BinaryAssociation(
    name="fileDescriptors119",
    ends={
        Property(name="FileName", type=cobol_sections_FileSection, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sections_FileSection", type=FileName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements120: BinaryAssociation = BinaryAssociation(
    name="statements120",
    ends={
        Property(name="Statement121", type=cobol_sentences_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sentences_StatementContainer", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
next122: BinaryAssociation = BinaryAssociation(
    name="next122",
    ends={
        Property(name="Sentence", type=cobol_sentences_Sentence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_sentences_Sentence", type=Sentence, multiplicity=Multiplicity(0, 1))
    }
)
next124: BinaryAssociation = BinaryAssociation(
    name="next124",
    ends={
        Property(name="Statement125", type=cobol_statements_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Statement", type=Statement, multiplicity=Multiplicity(0, 1))
    }
)
operands126: BinaryAssociation = BinaryAssociation(
    name="operands126",
    ends={
        Property(name="ArithmeticOperand", type=cobol_statements_ArithmeticStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ArithmeticStatement", type=ArithmeticOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
givings127: BinaryAssociation = BinaryAssociation(
    name="givings127",
    ends={
        Property(name="ArithmeticOperand129", type=cobol_statements_ArithmeticStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ArithmeticStatement128", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tos130: BinaryAssociation = BinaryAssociation(
    name="tos130",
    ends={
        Property(name="ArithmeticOperand131", type=cobol_statements_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Add", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
froms132: BinaryAssociation = BinaryAssociation(
    name="froms132",
    ends={
        Property(name="ArithmeticOperand133", type=cobol_statements_Subtract, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Subtract", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifier123: BinaryAssociation = BinaryAssociation(
    name="identifier123",
    ends={
        Property(name="Identifier", type=cobol_operands_RoundedIdentifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_operands_RoundedIdentifier", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
intos136: BinaryAssociation = BinaryAssociation(
    name="intos136",
    ends={
        Property(name="cobol_statements_Divide", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="ArithmeticOperand137", type=cobol_statements_Divide, multiplicity=Multiplicity(1, 1))
    }
)
remainders138: BinaryAssociation = BinaryAssociation(
    name="remainders138",
    ends={
        Property(name="Identifier140", type=cobol_statements_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Divide139", type=Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label141: BinaryAssociation = BinaryAssociation(
    name="label141",
    ends={
        Property(name="ProcedureRangeLabel", type=cobol_statements_PerformProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformProcedure", type=ProcedureRangeLabel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
labels142: BinaryAssociation = BinaryAssociation(
    name="labels142",
    ends={
        Property(name="ProcedureRangeLabel143", type=cobol_statements_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Jump", type=ProcedureRangeLabel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependsOn144: BinaryAssociation = BinaryAssociation(
    name="dependsOn144",
    ends={
        Property(name="IdentifierReference", type=cobol_statements_GoTo, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_GoTo", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements145: BinaryAssociation = BinaryAssociation(
    name="statements145",
    ends={
        Property(name="Statement146", type=cobol_statements_NestedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_NestedStatement", type=Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
receivers147: BinaryAssociation = BinaryAssociation(
    name="receivers147",
    ends={
        Property(name="PrimaryOperand", type=cobol_statements_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Move", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sender148: BinaryAssociation = BinaryAssociation(
    name="sender148",
    ends={
        Property(name="PrimaryOperand150", type=cobol_statements_Move, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Move149", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bys134: BinaryAssociation = BinaryAssociation(
    name="bys134",
    ends={
        Property(name="ArithmeticOperand135", type=cobol_statements_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Multiply", type=ArithmeticOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStatements151: BinaryAssociation = BinaryAssociation(
    name="elseStatements151",
    ends={
        Property(name="Statement152", type=cobol_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Condition", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition153: BinaryAssociation = BinaryAssociation(
    name="condition153",
    ends={
        Property(name="Condition154", type=cobol_statements_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Conditional", type=Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label155: BinaryAssociation = BinaryAssociation(
    name="label155",
    ends={
        Property(name="StopLabel", type=cobol_statements_Stop, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Stop", type=StopLabel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands156: BinaryAssociation = BinaryAssociation(
    name="operands156",
    ends={
        Property(name="PrimaryOperand157", type=cobol_statements_Display, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Display", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
output158: BinaryAssociation = BinaryAssociation(
    name="output158",
    ends={
        Property(name="Environment", type=cobol_statements_Display, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Display159", type=Environment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="AssignmentExpression", type=cobol_statements_Compute, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Compute", type=AssignmentExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiver161: BinaryAssociation = BinaryAssociation(
    name="receiver161",
    ends={
        Property(name="PrimaryOperand162", type=cobol_statements_Accept, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Accept", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
handlers163: BinaryAssociation = BinaryAssociation(
    name="handlers163",
    ends={
        Property(name="Handler", type=cobol_statements_ErrorHandled, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_ErrorHandled", type=Handler, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileName164: BinaryAssociation = BinaryAssociation(
    name="fileName164",
    ends={
        Property(name="FileNameReference", type=cobol_statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Return", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
output165: BinaryAssociation = BinaryAssociation(
    name="output165",
    ends={
        Property(name="IdentifierReference167", type=cobol_statements_Return, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Return166", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender168: BinaryAssociation = BinaryAssociation(
    name="sender168",
    ends={
        Property(name="PrimaryOperand169", type=cobol_statements_SetStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetStatement", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
switches170: BinaryAssociation = BinaryAssociation(
    name="switches170",
    ends={
        Property(name="SwitchStatus", type=cobol_statements_SetSwitches, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetSwitches", type=SwitchStatus, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
receivers171: BinaryAssociation = BinaryAssociation(
    name="receivers171",
    ends={
        Property(name="IndexNameReference", type=cobol_statements_SetIndexName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SetIndexName", type=IndexNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
pointer172: BinaryAssociation = BinaryAssociation(
    name="pointer172",
    ends={
        Property(name="Identifier173", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receiver174: BinaryAssociation = BinaryAssociation(
    name="receiver174",
    ends={
        Property(name="Identifier176", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String175", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
senders177: BinaryAssociation = BinaryAssociation(
    name="senders177",
    ends={
        Property(name="ConcatenatingStrings", type=cobol_statements_String, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_String178", type=ConcatenatingStrings, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subprograms179: BinaryAssociation = BinaryAssociation(
    name="subprograms179",
    ends={
        Property(name="PrimaryOperand180", type=cobol_statements_Cancel, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Cancel", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subprogram181: BinaryAssociation = BinaryAssociation(
    name="subprogram181",
    ends={
        Property(name="PrimaryOperand182", type=cobol_statements_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Call", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subprograms183: BinaryAssociation = BinaryAssociation(
    name="subprograms183",
    ends={
        Property(name="Identifier184", type=cobol_statements_Initialize, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Initialize", type=Identifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacements185: BinaryAssociation = BinaryAssociation(
    name="replacements185",
    ends={
        Property(name="Replacement", type=cobol_statements_Initialize, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Initialize186", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases187: BinaryAssociation = BinaryAssociation(
    name="cases187",
    ends={
        Property(name="NormalEvaluateCase", type=cobol_statements_SearchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SearchStatement", type=NormalEvaluateCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
table188: BinaryAssociation = BinaryAssociation(
    name="table188",
    ends={
        Property(name="PrimaryOperand190", type=cobol_statements_SearchStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SearchStatement189", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable191: BinaryAssociation = BinaryAssociation(
    name="variable191",
    ends={
        Property(name="Identifier192", type=cobol_statements_SerialSearch, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SerialSearch", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointer193: BinaryAssociation = BinaryAssociation(
    name="pointer193",
    ends={
        Property(name="Identifier194", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tally195: BinaryAssociation = BinaryAssociation(
    name="tally195",
    ends={
        Property(name="IdentifierReference197", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring196", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delimiter203: BinaryAssociation = BinaryAssociation(
    name="delimiter203",
    ends={
        Property(name="Condition205", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring204", type=Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counter206: BinaryAssociation = BinaryAssociation(
    name="counter206",
    ends={
        Property(name="Identifier208", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring207", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cases209: BinaryAssociation = BinaryAssociation(
    name="cases209",
    ends={
        Property(name="EvaluateCase", type=cobol_statements_Evaluate, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Evaluate", type=EvaluateCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subject210: BinaryAssociation = BinaryAssociation(
    name="subject210",
    ends={
        Property(name="ExpressionList", type=cobol_statements_Evaluate, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Evaluate211", type=ExpressionList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
objects212: BinaryAssociation = BinaryAssociation(
    name="objects212",
    ends={
        Property(name="ExpressionList213", type=cobol_statements_EvaluateCase, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_EvaluateCase", type=ExpressionList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tallyingIns214: BinaryAssociation = BinaryAssociation(
    name="tallyingIns214",
    ends={
        Property(name="TallyingIn", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect", type=TallyingIn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
replacements215: BinaryAssociation = BinaryAssociation(
    name="replacements215",
    ends={
        Property(name="Replacement217", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect216", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conversions218: BinaryAssociation = BinaryAssociation(
    name="conversions218",
    ends={
        Property(name="Replacement220", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect219", type=Replacement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
string221: BinaryAssociation = BinaryAssociation(
    name="string221",
    ends={
        Property(name="PrimaryOperand223", type=cobol_statements_Inspect, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Inspect222", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receivers224: BinaryAssociation = BinaryAssociation(
    name="receivers224",
    ends={
        Property(name="IdentifierReference225", type=cobol_statements_Set, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Set", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sender198: BinaryAssociation = BinaryAssociation(
    name="sender198",
    ends={
        Property(name="Identifier200", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring199", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiver226: BinaryAssociation = BinaryAssociation(
    name="receiver226",
    ends={
        Property(name="Identifier227", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
receivers201: BinaryAssociation = BinaryAssociation(
    name="receivers201",
    ends={
        Property(name="SplittedString", type=cobol_statements_Unstring, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Unstring202", type=SplittedString, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
keyName228: BinaryAssociation = BinaryAssociation(
    name="keyName228",
    ends={
        Property(name="Identifier230", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read229", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileName231: BinaryAssociation = BinaryAssociation(
    name="fileName231",
    ends={
        Property(name="FileNameReference233", type=cobol_statements_Read, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Read232", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
recordName234: BinaryAssociation = BinaryAssociation(
    name="recordName234",
    ends={
        Property(name="Identifier235", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numLines236: BinaryAssociation = BinaryAssociation(
    name="numLines236",
    ends={
        Property(name="Identifier238", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write237", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer239: BinaryAssociation = BinaryAssociation(
    name="integer239",
    ends={
        Property(name="IntegerLiteral", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write240", type=IntegerLiteral, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mnemonicName241: BinaryAssociation = BinaryAssociation(
    name="mnemonicName241",
    ends={
        Property(name="MnemonicNameReference", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write242", type=MnemonicNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sender243: BinaryAssociation = BinaryAssociation(
    name="sender243",
    ends={
        Property(name="Identifier245", type=cobol_statements_Write, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Write244", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mnemonicNames246: BinaryAssociation = BinaryAssociation(
    name="mnemonicNames246",
    ends={
        Property(name="MnemonicNameReference247", type=cobol_statements_SwitchStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_SwitchStatus", type=MnemonicNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
conditions248: BinaryAssociation = BinaryAssociation(
    name="conditions248",
    ends={
        Property(name="Condition249", type=cobol_statements_PerformUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformUntilCondition", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
afters252: BinaryAssociation = BinaryAssociation(
    name="afters252",
    ends={
        Property(name="AfterUntilCondition", type=cobol_statements_PerformProcedureUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformProcedureUntilCondition", type=AfterUntilCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileName253: BinaryAssociation = BinaryAssociation(
    name="fileName253",
    ends={
        Property(name="FileNameReference254", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
input255: BinaryAssociation = BinaryAssociation(
    name="input255",
    ends={
        Property(name="InputDirective", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement256", type=InputDirective, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
output257: BinaryAssociation = BinaryAssociation(
    name="output257",
    ends={
        Property(name="OutputDirective", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement258", type=OutputDirective, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyDescriptors259: BinaryAssociation = BinaryAssociation(
    name="keyDescriptors259",
    ends={
        Property(name="KeyDescriptor", type=cobol_statements_FileIOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_FileIOStatement260", type=KeyDescriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
recordName261: BinaryAssociation = BinaryAssociation(
    name="recordName261",
    ends={
        Property(name="IdentifierReference262", type=cobol_statements_Release, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Release", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sender263: BinaryAssociation = BinaryAssociation(
    name="sender263",
    ends={
        Property(name="IdentifierReference265", type=cobol_statements_Release, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Release264", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyNames266: BinaryAssociation = BinaryAssociation(
    name="keyNames266",
    ends={
        Property(name="IdentifierReference267", type=cobol_statements_KeyDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_KeyDescriptor", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ioFileDescriptors268: BinaryAssociation = BinaryAssociation(
    name="ioFileDescriptors268",
    ends={
        Property(name="IOFileDescriptor", type=cobol_statements_IOStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOStatement", type=IOFileDescriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
iterations250: BinaryAssociation = BinaryAssociation(
    name="iterations250",
    ends={
        Property(name="PrimaryOperand251", type=cobol_statements_PerformFixedTimes, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_PerformFixedTimes", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileName270: BinaryAssociation = BinaryAssociation(
    name="fileName270",
    ends={
        Property(name="FileNameReference271", type=cobol_statements_IOFile, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOFile", type=FileNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
occurrences272: BinaryAssociation = BinaryAssociation(
    name="occurrences272",
    ends={
        Property(name="Tallying", type=cobol_statements_TallyingIn, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_TallyingIn", type=Tallying, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fileName295: BinaryAssociation = BinaryAssociation(
    name="fileName295",
    ends={
        Property(name="FileNameReference296", type=cobol_statements_Delete, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Delete", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subscript297: BinaryAssociation = BinaryAssociation(
    name="subscript297",
    ends={
        Property(name="Operand", type=cobol_identifiers_Subscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_Subscript", type=Operand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
counter273: BinaryAssociation = BinaryAssociation(
    name="counter273",
    ends={
        Property(name="Identifier275", type=cobol_statements_TallyingIn, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_TallyingIn274", type=Identifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ioFiles269: BinaryAssociation = BinaryAssociation(
    name="ioFiles269",
    ends={
        Property(name="IOFile", type=cobol_statements_IOFileDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_IOFileDescriptor", type=IOFile, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable276: BinaryAssociation = BinaryAssociation(
    name="variable276",
    ends={
        Property(name="IdentifierReference277", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init278: BinaryAssociation = BinaryAssociation(
    name="init278",
    ends={
        Property(name="PrimaryOperand280", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition279", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
increment281: BinaryAssociation = BinaryAssociation(
    name="increment281",
    ends={
        Property(name="PrimaryOperand283", type=cobol_statements_VaryingUntilCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_VaryingUntilCondition282", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileName284: BinaryAssociation = BinaryAssociation(
    name="fileName284",
    ends={
        Property(name="FileNameReference285", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operator286: BinaryAssociation = BinaryAssociation(
    name="operator286",
    ends={
        Property(name="RelationalOperator288", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start287", type=RelationalOperator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataName289: BinaryAssociation = BinaryAssociation(
    name="dataName289",
    ends={
        Property(name="Identifier291", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start290", type=Identifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not292: BinaryAssociation = BinaryAssociation(
    name="not292",
    ends={
        Property(name="Negate294", type=cobol_statements_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_statements_Start293", type=Negate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveOperator307: BinaryAssociation = BinaryAssociation(
    name="additiveOperator307",
    ends={
        Property(name="AdditiveOperator308", type=cobol_identifiers_RelativeSubscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_RelativeSubscript", type=AdditiveOperator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer309: BinaryAssociation = BinaryAssociation(
    name="integer309",
    ends={
        Property(name="IntegerLiteral311", type=cobol_identifiers_RelativeSubscript, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_RelativeSubscript310", type=IntegerLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modifier298: BinaryAssociation = BinaryAssociation(
    name="modifier298",
    ends={
        Property(name="ReferenceModifier", type=cobol_identifiers_Identifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_Identifier", type=ReferenceModifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subscripts299: BinaryAssociation = BinaryAssociation(
    name="subscripts299",
    ends={
        Property(name="Subscript", type=cobol_identifiers_IdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_IdentifierReference", type=Subscript, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
qualifiers300: BinaryAssociation = BinaryAssociation(
    name="qualifiers300",
    ends={
        Property(name="Qualifier", type=cobol_identifiers_IdentifierReference, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_IdentifierReference301", type=Qualifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start302: BinaryAssociation = BinaryAssociation(
    name="start302",
    ends={
        Property(name="ArithmeticExpression303", type=cobol_identifiers_ReferenceModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_ReferenceModifier", type=ArithmeticExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
length304: BinaryAssociation = BinaryAssociation(
    name="length304",
    ends={
        Property(name="ArithmeticExpression306", type=cobol_identifiers_ReferenceModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_identifiers_ReferenceModifier305", type=ArithmeticExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileNames312: BinaryAssociation = BinaryAssociation(
    name="fileNames312",
    ends={
        Property(name="FileNameReference313", type=cobol_ios_FileDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_ios_FileDirective", type=FileNameReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label314: BinaryAssociation = BinaryAssociation(
    name="label314",
    ends={
        Property(name="Label", type=cobol_ios_ProcedureDirective, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_ios_ProcedureDirective", type=Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
water315: BinaryAssociation = BinaryAssociation(
    name="water315",
    ends={
        Property(name="Water", type=cobol_water_IncompleteElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_water_IncompleteElement", type=Water, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand316: BinaryAssociation = BinaryAssociation(
    name="operand316",
    ends={
        Property(name="PrimaryOperand317", type=cobol_registers_Register, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_registers_Register", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nameRange318: BinaryAssociation = BinaryAssociation(
    name="nameRange318",
    ends={
        Property(name="RangeExpression", type=cobol_dataitems_RenamingDataName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_RenamingDataName", type=RangeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values319: BinaryAssociation = BinaryAssociation(
    name="values319",
    ends={
        Property(name="Condition320", type=cobol_dataitems_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_Value", type=Condition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subentries322: BinaryAssociation = BinaryAssociation(
    name="subentries322",
    ends={
        Property(name="dataitems", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="DataItem323", type=DataItem, multiplicity=Multiplicity(0, 9999))
    }
)
superentry324: BinaryAssociation = BinaryAssociation(
    name="superentry324",
    ends={
        Property(name="dataitems326", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="DataItem325", type=DataItem, multiplicity=Multiplicity(0, 1))
    }
)
attributes321: BinaryAssociation = BinaryAssociation(
    name="attributes321",
    ends={
        Property(name="DataItemAttribute", type=cobol_dataitems_DataItem, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_DataItem", type=DataItemAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elems327: BinaryAssociation = BinaryAssociation(
    name="elems327",
    ends={
        Property(name="DataItem328", type=cobol_dataitems_RecordName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_RecordName", type=DataItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dataName329: BinaryAssociation = BinaryAssociation(
    name="dataName329",
    ends={
        Property(name="IdentifierReference330", type=cobol_dataitems_Redefines, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_dataitems_Redefines", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type331: BinaryAssociation = BinaryAssociation(
    name="type331",
    ends={
        Property(name="AlphabetType", type=cobol_specialnames_AlphabetName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_AlphabetName", type=AlphabetType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionNames332: BinaryAssociation = BinaryAssociation(
    name="conditionNames332",
    ends={
        Property(name="ConditionName", type=cobol_specialnames_UPSISwitchIs, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_UPSISwitchIs", type=ConditionName, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
currency335: BinaryAssociation = BinaryAssociation(
    name="currency335",
    ends={
        Property(name="Literal", type=cobol_specialnames_CurrencySign, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_CurrencySign", type=Literal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range336: BinaryAssociation = BinaryAssociation(
    name="range336",
    ends={
        Property(name="RangeExpression337", type=cobol_specialnames_ClassName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_ClassName", type=RangeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
environment338: BinaryAssociation = BinaryAssociation(
    name="environment338",
    ends={
        Property(name="Environment339", type=cobol_specialnames_MnemonicName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_MnemonicName", type=Environment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range333: BinaryAssociation = BinaryAssociation(
    name="range333",
    ends={
        Property(name="RangeExpression334", type=cobol_specialnames_ExplicitAlphabetType, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_ExplicitAlphabetType", type=RangeExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
integers340: BinaryAssociation = BinaryAssociation(
    name="integers340",
    ends={
        Property(name="IntegerLiteral341", type=cobol_specialnames_SymbolicCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacter", type=IntegerLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
symbolicCharacters342: BinaryAssociation = BinaryAssociation(
    name="symbolicCharacters342",
    ends={
        Property(name="SymbolicCharacter", type=cobol_specialnames_SymbolicCharacterStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacterStatement", type=SymbolicCharacter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
alphabetNameReference343: BinaryAssociation = BinaryAssociation(
    name="alphabetNameReference343",
    ends={
        Property(name="AlphabetNameReference", type=cobol_specialnames_SymbolicCharacterStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_specialnames_SymbolicCharacterStatement344", type=AlphabetNameReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableDimension345: BinaryAssociation = BinaryAssociation(
    name="tableDimension345",
    ends={
        Property(name="TableDimension", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table", type=TableDimension, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indexedBy346: BinaryAssociation = BinaryAssociation(
    name="indexedBy346",
    ends={
        Property(name="IndexName", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table347", type=IndexName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keysAre348: BinaryAssociation = BinaryAssociation(
    name="keysAre348",
    ends={
        Property(name="KeyName", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table349", type=KeyName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxTableDimension350: BinaryAssociation = BinaryAssociation(
    name="maxTableDimension350",
    ends={
        Property(name="TableDimension352", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table351", type=TableDimension, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependsOn353: BinaryAssociation = BinaryAssociation(
    name="dependsOn353",
    ends={
        Property(name="IdentifierReference355", type=cobol_tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_Table354", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keys356: BinaryAssociation = BinaryAssociation(
    name="keys356",
    ends={
        Property(name="IdentifierReference357", type=cobol_tables_KeyName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_KeyName", type=IdentifierReference, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
additionalIndexNames358: BinaryAssociation = BinaryAssociation(
    name="additionalIndexNames358",
    ends={
        Property(name="AdditionalIndexName", type=cobol_tables_IndexName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_tables_IndexName", type=AdditionalIndexName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
records359: BinaryAssociation = BinaryAssociation(
    name="records359",
    ends={
        Property(name="DataItem360", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName", type=DataItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes361: BinaryAssociation = BinaryAssociation(
    name="attributes361",
    ends={
        Property(name="DataItemAttribute363", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName362", type=DataItemAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sentences364: BinaryAssociation = BinaryAssociation(
    name="sentences364",
    ends={
        Property(name="StatementContainer366", type=cobol_files_FileName, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileName365", type=StatementContainer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fileStatus367: BinaryAssociation = BinaryAssociation(
    name="fileStatus367",
    ends={
        Property(name="FileStatus", type=cobol_files_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_SelectStatement", type=FileStatus, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fileNameReference368: BinaryAssociation = BinaryAssociation(
    name="fileNameReference368",
    ends={
        Property(name="FileNameReference370", type=cobol_files_SelectStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_SelectStatement369", type=FileNameReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fileStatus371: BinaryAssociation = BinaryAssociation(
    name="fileStatus371",
    ends={
        Property(name="IdentifierReference372", type=cobol_files_FileStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileStatus", type=IdentifierReference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vsamFileStatus373: BinaryAssociation = BinaryAssociation(
    name="vsamFileStatus373",
    ends={
        Property(name="IdentifierReference375", type=cobol_files_FileStatus, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_files_FileStatus374", type=IdentifierReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters376: BinaryAssociation = BinaryAssociation(
    name="parameters376",
    ends={
        Property(name="Parameter", type=cobol_parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_parameters_Parametrizable", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returning377: BinaryAssociation = BinaryAssociation(
    name="returning377",
    ends={
        Property(name="Parameter379", type=cobol_parameters_Parametrizable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_parameters_Parametrizable378", type=Parameter_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declarativeSections380: BinaryAssociation = BinaryAssociation(
    name="declarativeSections380",
    ends={
        Property(name="DeclarativeSection", type=cobol_declaratives_Declaratives, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_declaratives_Declaratives", type=DeclarativeSection, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
children381: BinaryAssociation = BinaryAssociation(
    name="children381",
    ends={
        Property(name="ProcedureRangeChild", type=cobol_labels_ProcedureRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRange", type=ProcedureRangeChild, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
throughOperator382: BinaryAssociation = BinaryAssociation(
    name="throughOperator382",
    ends={
        Property(name="Through384", type=cobol_labels_ProcedureRange, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRange383", type=Through, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target385: BinaryAssociation = BinaryAssociation(
    name="target385",
    ends={
        Property(name="Procedure", type=cobol_labels_ProcedureRangeChild, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureRangeChild", type=Procedure, multiplicity=Multiplicity(1, 1))
    }
)
section386: BinaryAssociation = BinaryAssociation(
    name="section386",
    ends={
        Property(name="Section387", type=cobol_labels_ProcedureLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_labels_ProcedureLabel", type=Section, multiplicity=Multiplicity(0, 1))
    }
)
operands388: BinaryAssociation = BinaryAssociation(
    name="operands388",
    ends={
        Property(name="PrimaryOperand389", type=cobol_functions_Argument, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argument", type=PrimaryOperand, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arguments390: BinaryAssociation = BinaryAssociation(
    name="arguments390",
    ends={
        Property(name="Argument", type=cobol_functions_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argumentable", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
handlerStatement394: BinaryAssociation = BinaryAssociation(
    name="handlerStatement394",
    ends={
        Property(name="Handler395", type=cobol_handlers_NotErrorHandler, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_handlers_NotErrorHandler", type=Handler, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
locations396: BinaryAssociation = BinaryAssociation(
    name="locations396",
    ends={
        Property(name="Location", type=cobol_strings_StringManipulation, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_StringManipulation", type=Location, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
strings397: BinaryAssociation = BinaryAssociation(
    name="strings397",
    ends={
        Property(name="PrimaryOperand398", type=cobol_strings_ManipulatedStrings, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ManipulatedStrings", type=PrimaryOperand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
delimiter399: BinaryAssociation = BinaryAssociation(
    name="delimiter399",
    ends={
        Property(name="PrimaryOperand401", type=cobol_strings_ManipulatedStrings, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ManipulatedStrings400", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
counter402: BinaryAssociation = BinaryAssociation(
    name="counter402",
    ends={
        Property(name="PrimaryOperand403", type=cobol_strings_SplittedString, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SplittedString", type=PrimaryOperand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returning391: BinaryAssociation = BinaryAssociation(
    name="returning391",
    ends={
        Property(name="Argument393", type=cobol_functions_Argumentable, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_functions_Argumentable392", type=Argument, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base404: BinaryAssociation = BinaryAssociation(
    name="base404",
    ends={
        Property(name="PrimaryOperand405", type=cobol_strings_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_Location", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target406: BinaryAssociation = BinaryAssociation(
    name="target406",
    ends={
        Property(name="ReplacementOperand", type=cobol_strings_Replacement, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_Replacement", type=ReplacementOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
occurrences407: BinaryAssociation = BinaryAssociation(
    name="occurrences407",
    ends={
        Property(name="Tallying408", type=cobol_strings_TallyingOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_TallyingOccurrence", type=Tallying, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
occurrences409: BinaryAssociation = BinaryAssociation(
    name="occurrences409",
    ends={
        Property(name="Replacement410", type=cobol_strings_ReplacementOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_ReplacementOccurrence", type=Replacement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tallying411: BinaryAssociation = BinaryAssociation(
    name="tallying411",
    ends={
        Property(name="PrimaryOperand412", type=cobol_strings_SpecificCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SpecificCharacter", type=PrimaryOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source413: BinaryAssociation = BinaryAssociation(
    name="source413",
    ends={
        Property(name="ReplacementOperand414", type=cobol_strings_SpecificCharacterBySpecificCharacter, multiplicity=Multiplicity(1, 1)),
        Property(name="cobol_strings_SpecificCharacterBySpecificCharacter", type=ReplacementOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cobol_commons_NamedElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_NamedElement)
gen_cobol_commons_LabellableElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_LabellableElement)
gen_cobol_commons_URIableElement_Commentable = Generalization(general=Commentable, specific=cobol_commons_URIableElement)
gen_cobol_conditions_ConditionalOrExpression_Condition = Generalization(general=Condition, specific=cobol_conditions_ConditionalOrExpression)
gen_cobol_conditions_ConditionalOrExpressionChild_Condition = Generalization(general=Condition, specific=cobol_conditions_ConditionalOrExpressionChild)
gen_cobol_conditions_NegatedConditionalExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_NegatedConditionalExpression)
gen_cobol_conditions_NegatedConditionalExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_NegatedConditionalExpressionChild)
gen_cobol_conditions_SimpleConditionChild_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_SimpleConditionChild)
gen_cobol_conditions_RelationalExpression_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_RelationalExpression)
gen_cobol_conditions_ConditionalAndExpressionChild_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=cobol_conditions_ConditionalAndExpressionChild)
gen_cobol_conditions_ConditionalAndExpression_ConditionalOrExpressionChild = Generalization(general=ConditionalOrExpressionChild, specific=cobol_conditions_ConditionalAndExpression)
gen_cobol_conditions_AbbreviatedConditionalExpression_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_AbbreviatedConditionalExpression)
gen_cobol_conditions_AbbreviatedConditionalExpressionChild_ConditionalAndExpressionChild = Generalization(general=ConditionalAndExpressionChild, specific=cobol_conditions_AbbreviatedConditionalExpressionChild)
gen_cobol_conditions_NegatedAbbreviatedConditionalExpression_AbbreviatedConditionalExpressionChild = Generalization(general=AbbreviatedConditionalExpressionChild, specific=cobol_conditions_NegatedAbbreviatedConditionalExpression)
gen_cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_AbbreviatedConditionalExpressionChild = Generalization(general=AbbreviatedConditionalExpressionChild, specific=cobol_conditions_NegatedAbbreviatedConditionalExpressionChild)
gen_cobol_conditions_AbbreviatedRelationalExpression_NegatedAbbreviatedConditionalExpressionChild = Generalization(general=NegatedAbbreviatedConditionalExpressionChild, specific=cobol_conditions_AbbreviatedRelationalExpression)
gen_cobol_conditions_NestedAbbreviatedConditionalExpression_AbbreviatedRelationalExpressionChild = Generalization(general=AbbreviatedRelationalExpressionChild, specific=cobol_conditions_NestedAbbreviatedConditionalExpression)
gen_cobol_conditions_SignCondition_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_SignCondition)
gen_cobol_conditions_ClassCondition_NegatedConditionalExpressionChild = Generalization(general=NegatedConditionalExpressionChild, specific=cobol_conditions_ClassCondition)
gen_cobol_conditions_AbbreviatedRelationalExpressionChild_NegatedAbbreviatedConditionalExpressionChild = Generalization(general=NegatedAbbreviatedConditionalExpressionChild, specific=cobol_conditions_AbbreviatedRelationalExpressionChild)
gen_cobol_conditions_NestedCondition_SimpleConditionChild = Generalization(general=SimpleConditionChild, specific=cobol_conditions_NestedCondition)
gen_cobol_arithmetics_AdditiveArithmeticExpression_RangeExpressionChild = Generalization(general=RangeExpressionChild, specific=cobol_arithmetics_AdditiveArithmeticExpression)
gen_cobol_arithmetics_AdditiveArithmeticExpressionChild_RangeExpressionChild = Generalization(general=RangeExpressionChild, specific=cobol_arithmetics_AdditiveArithmeticExpressionChild)
gen_cobol_arithmetics_MultiplicativeArithmeticExpression_AdditiveArithmeticExpressionChild = Generalization(general=AdditiveArithmeticExpressionChild, specific=cobol_arithmetics_MultiplicativeArithmeticExpression)
gen_cobol_arithmetics_MultiplicativeArithmeticExpressionChild_AdditiveArithmeticExpressionChild = Generalization(general=AdditiveArithmeticExpressionChild, specific=cobol_arithmetics_MultiplicativeArithmeticExpressionChild)
gen_cobol_arithmetics_PowerArithmeticExpression_MultiplicativeArithmeticExpressionChild = Generalization(general=MultiplicativeArithmeticExpressionChild, specific=cobol_arithmetics_PowerArithmeticExpression)
gen_cobol_arithmetics_PowerArithmeticExpressionChild_MultiplicativeArithmeticExpressionChild = Generalization(general=MultiplicativeArithmeticExpressionChild, specific=cobol_arithmetics_PowerArithmeticExpressionChild)
gen_cobol_arithmetics_UnaryArithmeticExpressionChild_PowerArithmeticExpressionChild = Generalization(general=PowerArithmeticExpressionChild, specific=cobol_arithmetics_UnaryArithmeticExpressionChild)
gen_cobol_arithmetics_UnaryArithmeticExpression_PowerArithmeticExpressionChild = Generalization(general=PowerArithmeticExpressionChild, specific=cobol_arithmetics_UnaryArithmeticExpression)
gen_cobol_arithmetics_PrimaryExpression_UnaryArithmeticExpressionChild = Generalization(general=UnaryArithmeticExpressionChild, specific=cobol_arithmetics_PrimaryExpression)
gen_cobol_arithmetics_RangeExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=cobol_arithmetics_RangeExpression)
gen_cobol_arithmetics_NestedArithmeticExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cobol_arithmetics_NestedArithmeticExpression)
gen_cobol_arithmetics_ArithmeticExpression_conditions_AbbreviatedRelationalExpressionChild = Generalization(general=conditions_AbbreviatedRelationalExpressionChild, specific=cobol_arithmetics_ArithmeticExpression)
gen_cobol_arithmetics_ArithmeticExpression_conditions_SimpleConditionChild = Generalization(general=conditions_SimpleConditionChild, specific=cobol_arithmetics_ArithmeticExpression)
gen_cobol_containers_CompilationGroup_containers_CobolRoot = Generalization(general=containers_CobolRoot, specific=cobol_containers_CompilationGroup)
gen_cobol_containers_CompilationGroup_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_containers_CompilationGroup)
gen_cobol_containers_CompilationUnit_NamedElement = Generalization(general=NamedElement, specific=cobol_containers_CompilationUnit)
gen_cobol_containers_EmptyModel_CobolRoot = Generalization(general=CobolRoot, specific=cobol_containers_EmptyModel)
gen_cobol_divisions_Division_NamedElement = Generalization(general=NamedElement, specific=cobol_divisions_Division)
gen_cobol_divisions_DataDivision_Division = Generalization(general=Division, specific=cobol_divisions_DataDivision)
gen_cobol_divisions_EnvironmentDivision_Division = Generalization(general=Division, specific=cobol_divisions_EnvironmentDivision)
gen_cobol_divisions_IdentificationDivision_divisions_Division = Generalization(general=divisions_Division, specific=cobol_divisions_IdentificationDivision)
gen_cobol_divisions_IdentificationDivision_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_divisions_IdentificationDivision)
gen_cobol_divisions_ProcedureDivision_divisions_Division = Generalization(general=divisions_Division, specific=cobol_divisions_ProcedureDivision)
gen_cobol_divisions_ProcedureDivision_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=cobol_divisions_ProcedureDivision)
gen_cobol_arithmetics_RangeExpressionChild_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=cobol_arithmetics_RangeExpressionChild)
gen_cobol_literals_Literal_water_SelectStatementWater = Generalization(general=water_SelectStatementWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_SpecialNamesParagraphWater = Generalization(general=water_SpecialNamesParagraphWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_CICSStatementWater = Generalization(general=water_CICSStatementWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_operands_PrimaryOperand = Generalization(general=operands_PrimaryOperand, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_water_InvokeStatementWater = Generalization(general=water_InvokeStatementWater, specific=cobol_literals_Literal)
gen_cobol_literals_Literal_labels_StopLabel = Generalization(general=labels_StopLabel, specific=cobol_literals_Literal)
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
gen_cobol_literals_Space_ConstantLiteral = Generalization(general=ConstantLiteral, specific=cobol_literals_Space)
gen_cobol_literals_Any_Literal = Generalization(general=Literal, specific=cobol_literals_Any)
gen_cobol_literals_Characters_Literal = Generalization(general=Literal, specific=cobol_literals_Characters)
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
gen_cobol_paragraphs_ConfigurationSectionParagraph_Paragraph = Generalization(general=Paragraph, specific=cobol_paragraphs_ConfigurationSectionParagraph)
gen_cobol_paragraphs_IOSectionParagraph_Paragraph = Generalization(general=Paragraph, specific=cobol_paragraphs_IOSectionParagraph)
gen_cobol_paragraphs_SpecialNamesParagraph_ConfigurationSectionParagraph = Generalization(general=ConfigurationSectionParagraph, specific=cobol_paragraphs_SpecialNamesParagraph)
gen_cobol_paragraphs_RepositoryParagraph_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_paragraphs_RepositoryParagraph)
gen_cobol_references_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=cobol_references_ReferenceableElement)
gen_cobol_references_ElementReference_Reference = Generalization(general=Reference, specific=cobol_references_ElementReference)
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
gen_cobol_sections_WorkingStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_WorkingStorageSection)
gen_cobol_sections_LocalStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_LocalStorageSection)
gen_cobol_sections_LinkageStorageSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_LinkageStorageSection)
gen_cobol_sections_IOSection_EnvironmentDivisionSection = Generalization(general=EnvironmentDivisionSection, specific=cobol_sections_IOSection)
gen_cobol_paragraphs_RepositoryParagraph_paragraphs_ConfigurationSectionParagraph = Generalization(general=paragraphs_ConfigurationSectionParagraph, specific=cobol_paragraphs_RepositoryParagraph)
gen_cobol_sections_ConfigurationSection_EnvironmentDivisionSection = Generalization(general=EnvironmentDivisionSection, specific=cobol_sections_ConfigurationSection)
gen_cobol_sections_EnvironmentDivisionSection_Section = Generalization(general=Section, specific=cobol_sections_EnvironmentDivisionSection)
gen_cobol_sections_DataDivisionSection_Section = Generalization(general=Section, specific=cobol_sections_DataDivisionSection)
gen_cobol_sections_FileSection_DataDivisionSection = Generalization(general=DataDivisionSection, specific=cobol_sections_FileSection)
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
gen_cobol_operands_ReplacementOperand_Operand = Generalization(general=Operand, specific=cobol_operands_ReplacementOperand)
gen_cobol_operands_Encoding_ReplacementOperand = Generalization(general=ReplacementOperand, specific=cobol_operands_Encoding)
gen_cobol_operands_ArithmeticOperand_Operand = Generalization(general=Operand, specific=cobol_operands_ArithmeticOperand)
gen_cobol_statements_ArithmeticStatement_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_ArithmeticStatement)
gen_cobol_statements_ArithmeticStatement_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_ArithmeticStatement)
gen_cobol_statements_Add_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Add)
gen_cobol_statements_Subtract_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Subtract)
gen_cobol_statements_Multiply_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Multiply)
gen_cobol_operands_RoundedIdentifier_ArithmeticOperand = Generalization(general=ArithmeticOperand, specific=cobol_operands_RoundedIdentifier)
gen_cobol_statements_Condition_statements_NestedStatement = Generalization(general=statements_NestedStatement, specific=cobol_statements_Condition)
gen_cobol_statements_Perform_Statement = Generalization(general=Statement, specific=cobol_statements_Perform)
gen_cobol_statements_PerformNestedStatement_statements_Perform = Generalization(general=statements_Perform, specific=cobol_statements_PerformNestedStatement)
gen_cobol_statements_PerformNestedStatement_statements_NestedStatement = Generalization(general=statements_NestedStatement, specific=cobol_statements_PerformNestedStatement)
gen_cobol_statements_PerformProcedure_Perform = Generalization(general=Perform, specific=cobol_statements_PerformProcedure)
gen_cobol_statements_Jump_Statement = Generalization(general=Statement, specific=cobol_statements_Jump)
gen_cobol_statements_NextSentence_Jump = Generalization(general=Jump, specific=cobol_statements_NextSentence)
gen_cobol_statements_GoTo_Jump = Generalization(general=Jump, specific=cobol_statements_GoTo)
gen_cobol_statements_GoBack_Jump = Generalization(general=Jump, specific=cobol_statements_GoBack)
gen_cobol_statements_Move_Statement = Generalization(general=Statement, specific=cobol_statements_Move)
gen_cobol_statements_Exit_Statement = Generalization(general=Statement, specific=cobol_statements_Exit)
gen_cobol_statements_Divide_ArithmeticStatement = Generalization(general=ArithmeticStatement, specific=cobol_statements_Divide)
gen_cobol_statements_Condition_statements_Conditional = Generalization(general=statements_Conditional, specific=cobol_statements_Condition)
gen_cobol_statements_Condition_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Condition)
gen_cobol_statements_Stop_Statement = Generalization(general=Statement, specific=cobol_statements_Stop)
gen_cobol_statements_Display_Statement = Generalization(general=Statement, specific=cobol_statements_Display)
gen_cobol_statements_Compute_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Compute)
gen_cobol_statements_Compute_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Compute)
gen_cobol_statements_Accept_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Accept)
gen_cobol_statements_Accept_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Accept)
gen_cobol_statements_Execute_Statement = Generalization(general=Statement, specific=cobol_statements_Execute)
gen_cobol_statements_Return_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Return)
gen_cobol_statements_Return_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Return)
gen_cobol_statements_SetStatement_Statement = Generalization(general=Statement, specific=cobol_statements_SetStatement)
gen_cobol_statements_SetSwitches_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_SetSwitches)
gen_cobol_statements_SetIndexName_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_SetIndexName)
gen_cobol_statements_String_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_String)
gen_cobol_statements_String_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_String)
gen_cobol_statements_Close_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Close)
gen_cobol_statements_Close_statements_IOStatement = Generalization(general=statements_IOStatement, specific=cobol_statements_Close)
gen_cobol_statements_Cancel_Statement = Generalization(general=Statement, specific=cobol_statements_Cancel)
gen_cobol_statements_Initialize_Statement = Generalization(general=Statement, specific=cobol_statements_Initialize)
gen_cobol_statements_Open_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Open)
gen_cobol_statements_Open_statements_IOStatement = Generalization(general=statements_IOStatement, specific=cobol_statements_Open)
gen_cobol_statements_SearchStatement_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_SearchStatement)
gen_cobol_statements_SearchStatement_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_SearchStatement)
gen_cobol_statements_SerialSearch_SearchStatement = Generalization(general=SearchStatement, specific=cobol_statements_SerialSearch)
gen_cobol_statements_BinarySearch_SearchStatement = Generalization(general=SearchStatement, specific=cobol_statements_BinarySearch)
gen_cobol_statements_Unstring_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Unstring)
gen_cobol_statements_Unstring_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Unstring)
gen_cobol_statements_Call_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Call)
gen_cobol_statements_Call_functions_Argumentable = Generalization(general=functions_Argumentable, specific=cobol_statements_Call)
gen_cobol_statements_Call_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Call)
gen_cobol_statements_Evaluate_Statement = Generalization(general=Statement, specific=cobol_statements_Evaluate)
gen_cobol_statements_NormalEvaluateCase_EvaluateCase = Generalization(general=EvaluateCase, specific=cobol_statements_NormalEvaluateCase)
gen_cobol_statements_OtherEvaluateCase_EvaluateCase = Generalization(general=EvaluateCase, specific=cobol_statements_OtherEvaluateCase)
gen_cobol_statements_EvaluateCase_NestedStatement = Generalization(general=NestedStatement, specific=cobol_statements_EvaluateCase)
gen_cobol_statements_Replace_Statement = Generalization(general=Statement, specific=cobol_statements_Replace)
gen_cobol_statements_Entry_parameters_Parametrizable = Generalization(general=parameters_Parametrizable, specific=cobol_statements_Entry)
gen_cobol_statements_Entry_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Entry)
gen_cobol_statements_Inspect_Statement = Generalization(general=Statement, specific=cobol_statements_Inspect)
gen_cobol_statements_Set_SetStatement = Generalization(general=SetStatement, specific=cobol_statements_Set)
gen_cobol_statements_Read_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Read)
gen_cobol_statements_Read_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Read)
gen_cobol_statements_Write_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Write)
gen_cobol_statements_Write_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Write)
gen_cobol_statements_Rewrite_Write = Generalization(general=Write, specific=cobol_statements_Rewrite)
gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformProcedure = Generalization(general=statements_PerformProcedure, specific=cobol_statements_PerformProcedureFixedTimes)
gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformFixedTimes = Generalization(general=statements_PerformFixedTimes, specific=cobol_statements_PerformProcedureFixedTimes)
gen_cobol_statements_PerformUntilCondition_statements_Perform = Generalization(general=statements_Perform, specific=cobol_statements_PerformUntilCondition)
gen_cobol_statements_PerformUntilCondition_statements_VaryingUntilCondition = Generalization(general=statements_VaryingUntilCondition, specific=cobol_statements_PerformUntilCondition)
gen_cobol_statements_PerformFixedTimes_Perform = Generalization(general=Perform, specific=cobol_statements_PerformFixedTimes)
gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformNestedStatement = Generalization(general=statements_PerformNestedStatement, specific=cobol_statements_PerformNestedStatementFixedTimes)
gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformFixedTimes = Generalization(general=statements_PerformFixedTimes, specific=cobol_statements_PerformNestedStatementFixedTimes)
gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformUntilCondition = Generalization(general=statements_PerformUntilCondition, specific=cobol_statements_PerformNestedStatementUntilCondition)
gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformNestedStatement = Generalization(general=statements_PerformNestedStatement, specific=cobol_statements_PerformNestedStatementUntilCondition)
gen_cobol_statements_Continue_Jump = Generalization(general=Jump, specific=cobol_statements_Continue)
gen_cobol_statements_FileIOStatement_Statement = Generalization(general=Statement, specific=cobol_statements_FileIOStatement)
gen_cobol_statements_Sort_statements_FileIOStatement = Generalization(general=statements_FileIOStatement, specific=cobol_statements_Sort)
gen_cobol_statements_Sort_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Sort)
gen_cobol_statements_Merge_statements_FileIOStatement = Generalization(general=statements_FileIOStatement, specific=cobol_statements_Merge)
gen_cobol_statements_Merge_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_statements_Merge)
gen_cobol_statements_Release_Statement = Generalization(general=Statement, specific=cobol_statements_Release)
gen_cobol_statements_IOStatement_Statement = Generalization(general=Statement, specific=cobol_statements_IOStatement)
gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformUntilCondition = Generalization(general=statements_PerformUntilCondition, specific=cobol_statements_PerformProcedureUntilCondition)
gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformProcedure = Generalization(general=statements_PerformProcedure, specific=cobol_statements_PerformProcedureUntilCondition)
gen_cobol_statements_IOFile_IncompleteElement = Generalization(general=IncompleteElement, specific=cobol_statements_IOFile)
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
gen_cobol_statements_VaryingUntilCondition_Conditional = Generalization(general=Conditional, specific=cobol_statements_VaryingUntilCondition)
gen_cobol_statements_AfterUntilCondition_VaryingUntilCondition = Generalization(general=VaryingUntilCondition, specific=cobol_statements_AfterUntilCondition)
gen_cobol_statements_Start_statements_ErrorHandled = Generalization(general=statements_ErrorHandled, specific=cobol_statements_Start)
gen_cobol_statements_Start_statements_Statement = Generalization(general=statements_Statement, specific=cobol_statements_Start)
gen_cobol_identifiers_Qualifier_ElementReference = Generalization(general=ElementReference, specific=cobol_identifiers_Qualifier)
gen_cobol_identifiers_RelativeSubscript_Subscript = Generalization(general=Subscript, specific=cobol_identifiers_RelativeSubscript)
gen_cobol_identifiers_DirectSubscript_Subscript = Generalization(general=Subscript, specific=cobol_identifiers_DirectSubscript)
gen_cobol_ios_InputProcedure_ios_InputDirective = Generalization(general=ios_InputDirective, specific=cobol_ios_InputProcedure)
gen_cobol_ios_InputProcedure_ios_ProcedureDirective = Generalization(general=ios_ProcedureDirective, specific=cobol_ios_InputProcedure)
gen_cobol_ios_InputDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_InputDirective)
gen_cobol_ios_InputFile_ios_InputDirective = Generalization(general=ios_InputDirective, specific=cobol_ios_InputFile)
gen_cobol_ios_InputFile_ios_FileDirective = Generalization(general=ios_FileDirective, specific=cobol_ios_InputFile)
gen_cobol_identifiers_Identifier_water_UseStatementWater = Generalization(general=water_UseStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_FileDescriptorWater = Generalization(general=water_FileDescriptorWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_DataDescriptorWater = Generalization(general=water_DataDescriptorWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SelectStatementWater = Generalization(general=water_SelectStatementWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_Identifier_water_SortPhraseWater = Generalization(general=water_SortPhraseWater, specific=cobol_identifiers_Identifier)
gen_cobol_identifiers_IdentifierReference_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_identifiers_IdentifierReference)
gen_cobol_identifiers_IdentifierReference_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_identifiers_IdentifierReference)
gen_cobol_identifiers_IdentifierReference_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_identifiers_IdentifierReference)
gen_cobol_identifiers_All_DirectSubscript = Generalization(general=DirectSubscript, specific=cobol_identifiers_All)
gen_cobol_identifiers_LinageCounter_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_identifiers_LinageCounter)
gen_cobol_identifiers_LinageCounter_references_Qualifiable = Generalization(general=references_Qualifiable, specific=cobol_identifiers_LinageCounter)
gen_cobol_water_Dot_water_IdentificationDivisionWater = Generalization(general=water_IdentificationDivisionWater, specific=cobol_water_Dot)
gen_cobol_water_Dot_water_SQLStatementWater = Generalization(general=water_SQLStatementWater, specific=cobol_water_Dot)
gen_cobol_ios_OutputDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_OutputDirective)
gen_cobol_ios_OutputProcedure_ios_ProcedureDirective = Generalization(general=ios_ProcedureDirective, specific=cobol_ios_OutputProcedure)
gen_cobol_ios_OutputProcedure_ios_OutputDirective = Generalization(general=ios_OutputDirective, specific=cobol_ios_OutputProcedure)
gen_cobol_ios_OutputFile_ios_OutputDirective = Generalization(general=ios_OutputDirective, specific=cobol_ios_OutputFile)
gen_cobol_ios_OutputFile_ios_FileDirective = Generalization(general=ios_FileDirective, specific=cobol_ios_OutputFile)
gen_cobol_ios_FileDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_FileDirective)
gen_cobol_ios_ProcedureDirective_IODirectives = Generalization(general=IODirectives, specific=cobol_ios_ProcedureDirective)
gen_cobol_water_IdentificationDivisionWater_Water = Generalization(general=Water, specific=cobol_water_IdentificationDivisionWater)
gen_cobol_water_ProgramDescription_IdentificationDivisionWater = Generalization(general=IdentificationDivisionWater, specific=cobol_water_ProgramDescription)
gen_cobol_water_SpecialNamesParagraphWater_Water = Generalization(general=Water, specific=cobol_water_SpecialNamesParagraphWater)
gen_cobol_water_SpecialNamesClause_SpecialNamesParagraphWater = Generalization(general=SpecialNamesParagraphWater, specific=cobol_water_SpecialNamesClause)
gen_cobol_water_FileDescriptorWater_Water = Generalization(general=Water, specific=cobol_water_FileDescriptorWater)
gen_cobol_water_ObjectComputerParagraphWater_Water = Generalization(general=Water, specific=cobol_water_ObjectComputerParagraphWater)
gen_cobol_water_ObjectComputerDescription_ObjectComputerParagraphWater = Generalization(general=ObjectComputerParagraphWater, specific=cobol_water_ObjectComputerDescription)
gen_cobol_water_PriorityNumber_ObjectComputerParagraphWater = Generalization(general=ObjectComputerParagraphWater, specific=cobol_water_PriorityNumber)
gen_cobol_water_SelectStatementWater_Water = Generalization(general=Water, specific=cobol_water_SelectStatementWater)
gen_cobol_water_SelectStatementClause_SelectStatementWater = Generalization(general=SelectStatementWater, specific=cobol_water_SelectStatementClause)
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
gen_cobol_water_InvokeStatementWater_Water = Generalization(general=Water, specific=cobol_water_InvokeStatementWater)
gen_cobol_water_InvokeStatementToken_InvokeStatementWater = Generalization(general=InvokeStatementWater, specific=cobol_water_InvokeStatementToken)
gen_cobol_water_CloseStatementWater_Water = Generalization(general=Water, specific=cobol_water_CloseStatementWater)
gen_cobol_water_CloseStatementToken_CloseStatementWater = Generalization(general=CloseStatementWater, specific=cobol_water_CloseStatementToken)
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
gen_cobol_environments_UPSI_Environment = Generalization(general=Environment, specific=cobol_environments_UPSI)
gen_cobol_environments_SystemPunchDevice_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SystemPunchDevice)
gen_cobol_environments_Console_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Console)
gen_cobol_environments_Channel_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Channel)
gen_cobol_environments_AdvancedFunctionPrinting_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_AdvancedFunctionPrinting)
gen_cobol_environments_SuppressSpacing_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SuppressSpacing)
gen_cobol_environments_Pocket_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_Pocket)
gen_cobol_environments_SystemLogicalOutput_SystemDevice = Generalization(general=SystemDevice, specific=cobol_environments_SystemLogicalOutput)
gen_cobol_environments_Environment_AcceptStatementWater = Generalization(general=AcceptStatementWater, specific=cobol_environments_Environment)
gen_cobol_dataitems_RenamingDataName_DataName = Generalization(general=DataName, specific=cobol_dataitems_RenamingDataName)
gen_cobol_dataitems_ConditionName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_ConditionName)
gen_cobol_dataitems_Global_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Global)
gen_cobol_dataitems_External_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_External)
gen_cobol_dataitems_Value_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Value)
gen_cobol_dataitems_Usage_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Usage)
gen_cobol_dataitems_GroupUsage_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_GroupUsage)
gen_cobol_dataitems_DataItem_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_dataitems_DataItem)
gen_cobol_dataitems_DataItem_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_dataitems_DataItem)
gen_cobol_dataitems_PictureString_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_PictureString)
gen_cobol_dataitems_RecordName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_RecordName)
gen_cobol_dataitems_DataName_DataItem = Generalization(general=DataItem, specific=cobol_dataitems_DataName)
gen_cobol_dataitems_Redefines_DataItemAttribute = Generalization(general=DataItemAttribute, specific=cobol_dataitems_Redefines)
gen_cobol_specialnames_ConditionName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_ConditionName)
gen_cobol_specialnames_OnStatus_ConditionName = Generalization(general=ConditionName, specific=cobol_specialnames_OnStatus)
gen_cobol_specialnames_OffStatus_ConditionName = Generalization(general=ConditionName, specific=cobol_specialnames_OffStatus)
gen_cobol_specialnames_AlphabetName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_AlphabetName)
gen_cobol_specialnames_AlphabetName_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_AlphabetName)
gen_cobol_specialnames_UPSISwitchIs_specialnames_MnemonicName = Generalization(general=specialnames_MnemonicName, specific=cobol_specialnames_UPSISwitchIs)
gen_cobol_specialnames_UPSISwitchIs_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_UPSISwitchIs)
gen_cobol_specialnames_PredefinedAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_PredefinedAlphabetType)
gen_cobol_specialnames_ExplicitAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_ExplicitAlphabetType)
gen_cobol_specialnames_SpecialName_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_specialnames_SpecialName)
gen_cobol_specialnames_ConditionName_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_specialnames_ConditionName)
gen_cobol_specialnames_CodeNameAlphabetType_AlphabetType = Generalization(general=AlphabetType, specific=cobol_specialnames_CodeNameAlphabetType)
gen_cobol_specialnames_CurrencySign_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_CurrencySign)
gen_cobol_specialnames_CurrencySign_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_CurrencySign)
gen_cobol_specialnames_ClassName_specialnames_SpecialName = Generalization(general=specialnames_SpecialName, specific=cobol_specialnames_ClassName)
gen_cobol_specialnames_ClassName_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_ClassName)
gen_cobol_specialnames_MnemonicName_SpecialName = Generalization(general=SpecialName, specific=cobol_specialnames_MnemonicName)
gen_cobol_specialnames_SystemDeviceIs_specialnames_MnemonicName = Generalization(general=specialnames_MnemonicName, specific=cobol_specialnames_SystemDeviceIs)
gen_cobol_specialnames_SystemDeviceIs_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_SystemDeviceIs)
gen_cobol_specialnames_SymbolicCharacter_SpecialName = Generalization(general=SpecialName, specific=cobol_specialnames_SymbolicCharacter)
gen_cobol_tables_Table_dataitems_DataItem = Generalization(general=dataitems_DataItem, specific=cobol_tables_Table)
gen_cobol_tables_Table_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_tables_Table)
gen_cobol_tables_IndexName_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_tables_IndexName)
gen_cobol_tables_IndexName_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_tables_IndexName)
gen_cobol_specialnames_SymbolicCharacterStatement_specialnames_SpecialNameStatement = Generalization(general=specialnames_SpecialNameStatement, specific=cobol_specialnames_SymbolicCharacterStatement)
gen_cobol_specialnames_SymbolicCharacterStatement_references_ElementReference = Generalization(general=references_ElementReference, specific=cobol_specialnames_SymbolicCharacterStatement)
gen_cobol_tables_AdditionalIndexName_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_tables_AdditionalIndexName)
gen_cobol_files_FileName_water_IncompleteElement = Generalization(general=water_IncompleteElement, specific=cobol_files_FileName)
gen_cobol_files_FileName_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=cobol_files_FileName)
gen_cobol_files_SelectStatement_IncompleteElement = Generalization(general=IncompleteElement, specific=cobol_files_SelectStatement)
gen_cobol_parameters_Parameter_ReferenceableElement = Generalization(general=ReferenceableElement, specific=cobol_parameters_Parameter)
gen_cobol_verbs_Is_Verb = Generalization(general=Verb, specific=cobol_verbs_Is)
gen_cobol_labels_ProcedureRange_ProcedureRangeLabel = Generalization(general=ProcedureRangeLabel, specific=cobol_labels_ProcedureRange)
gen_cobol_labels_ProcedureRangeLabel_Label = Generalization(general=Label, specific=cobol_labels_ProcedureRangeLabel)
gen_cobol_labels_ProcedureRangeChild_ProcedureRangeLabel = Generalization(general=ProcedureRangeLabel, specific=cobol_labels_ProcedureRangeChild)
gen_cobol_labels_ProcedureLabel_ProcedureRangeChild = Generalization(general=ProcedureRangeChild, specific=cobol_labels_ProcedureLabel)
gen_cobol_labels_StopLabel_Label = Generalization(general=Label, specific=cobol_labels_StopLabel)
gen_cobol_labels_Run_StopLabel = Generalization(general=StopLabel, specific=cobol_labels_Run)
gen_cobol_functions_FunctionCall_functions_Argumentable = Generalization(general=functions_Argumentable, specific=cobol_functions_FunctionCall)
gen_cobol_functions_FunctionCall_commons_NamedElement = Generalization(general=commons_NamedElement, specific=cobol_functions_FunctionCall)
gen_cobol_functions_FunctionCall_identifiers_Identifier = Generalization(general=identifiers_Identifier, specific=cobol_functions_FunctionCall)
gen_cobol_functions_ByReferenceArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByReferenceArgument)
gen_cobol_functions_ByValueArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByValueArgument)
gen_cobol_functions_ByContentArgument_Argument = Generalization(general=Argument, specific=cobol_functions_ByContentArgument)
gen_cobol_functions_OmittedArgument_Argument = Generalization(general=Argument, specific=cobol_functions_OmittedArgument)
gen_cobol_parameters_ByReferenceParameter_Parameter = Generalization(general=Parameter_, specific=cobol_parameters_ByReferenceParameter)
gen_cobol_parameters_ByValueParameter_Parameter = Generalization(general=Parameter_, specific=cobol_parameters_ByValueParameter)
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
gen_cobol_handlers_InvalidKey_Handler = Generalization(general=Handler, specific=cobol_handlers_InvalidKey)
gen_cobol_handlers_NotAtEndOfPage_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotAtEndOfPage)
gen_cobol_handlers_NotInvalidKey_NotErrorHandler = Generalization(general=NotErrorHandler, specific=cobol_handlers_NotInvalidKey)
gen_cobol_strings_Tallying_StringManipulation = Generalization(general=StringManipulation, specific=cobol_strings_Tallying)
gen_cobol_strings_StringManipulation_String = Generalization(general=String, specific=cobol_strings_StringManipulation)
gen_cobol_strings_ManipulatedStrings_String = Generalization(general=String, specific=cobol_strings_ManipulatedStrings)
gen_cobol_strings_ConcatenatingStrings_ManipulatedStrings = Generalization(general=ManipulatedStrings, specific=cobol_strings_ConcatenatingStrings)
gen_cobol_strings_SplittedString_ManipulatedStrings = Generalization(general=ManipulatedStrings, specific=cobol_strings_SplittedString)
gen_cobol_strings_Replacement_StringManipulation = Generalization(general=StringManipulation, specific=cobol_strings_Replacement)
gen_cobol_strings_TallyingOccurrence_strings_Tallying = Generalization(general=strings_Tallying, specific=cobol_strings_TallyingOccurrence)
gen_cobol_strings_TallyingOccurrence_strings_Occurrence = Generalization(general=strings_Occurrence, specific=cobol_strings_TallyingOccurrence)
gen_cobol_strings_ReplacementOccurrence_strings_Occurrence = Generalization(general=strings_Occurrence, specific=cobol_strings_ReplacementOccurrence)
gen_cobol_strings_ReplacementOccurrence_strings_Replacement = Generalization(general=strings_Replacement, specific=cobol_strings_ReplacementOccurrence)
gen_cobol_strings_AnyCharacter_Tallying = Generalization(general=Tallying, specific=cobol_strings_AnyCharacter)
gen_cobol_strings_SpecificCharacter_Tallying = Generalization(general=Tallying, specific=cobol_strings_SpecificCharacter)
gen_cobol_strings_AnyCharacterBySpecificCharacter_Replacement = Generalization(general=Replacement, specific=cobol_strings_AnyCharacterBySpecificCharacter)
gen_cobol_strings_SpecificCharacterBySpecificCharacter_Replacement = Generalization(general=Replacement, specific=cobol_strings_SpecificCharacterBySpecificCharacter)

# Domain Model
domain_model = DomainModel(
    name="cobol",
    types={cobol_commons_NamedElement, Commentable, cobol_commons_Commentable, cobol_commons_LabellableElement, cobol_commons_URIableElement, cobol_conditions_Condition, cobol_conditions_ConditionalOrExpression, Condition, ConditionalOrExpressionChild, LogicalOperator, cobol_conditions_ConditionalOrExpressionChild, cobol_conditions_NegatedConditionalExpression, ConditionalAndExpressionChild, NegatedConditionalExpressionChild, Negate, cobol_conditions_NegatedConditionalExpressionChild, cobol_conditions_SimpleConditionChild, cobol_conditions_RelationalExpression, SimpleConditionChild, RelationalOperator, Is, cobol_conditions_ExpressionList, cobol_conditions_ConditionalAndExpressionChild, cobol_conditions_ConditionalAndExpression, cobol_conditions_AbbreviatedConditionalExpression, AbbreviatedConditionalExpressionChild, cobol_conditions_AbbreviatedConditionalExpressionChild, cobol_conditions_NegatedAbbreviatedConditionalExpression, cobol_conditions_NegatedAbbreviatedConditionalExpressionChild, cobol_conditions_AbbreviatedRelationalExpression, AbbreviatedRelationalExpressionChild, cobol_conditions_NestedAbbreviatedConditionalExpression, cobol_conditions_SignCondition, SignOperator, cobol_conditions_ClassCondition, ClassOperator, cobol_conditions_AbbreviatedRelationalExpressionChild, cobol_conditions_NestedCondition, NegatedAbbreviatedConditionalExpressionChild, AdditiveArithmeticExpressionChild, AdditiveOperator, cobol_arithmetics_AdditiveArithmeticExpressionChild, cobol_arithmetics_MultiplicativeArithmeticExpression, MultiplicativeArithmeticExpressionChild, MultiplicativeOperator, cobol_arithmetics_MultiplicativeArithmeticExpressionChild, cobol_arithmetics_PowerArithmeticExpression, PowerArithmeticExpressionChild, cobol_arithmetics_PowerArithmeticExpressionChild, cobol_arithmetics_UnaryArithmeticExpressionChild, cobol_arithmetics_UnaryArithmeticExpression, UnaryArithmeticExpressionChild, UnaryOperator, cobol_arithmetics_PrimaryExpression, cobol_arithmetics_AssignmentExpression, Equal, ArithmeticExpression, cobol_arithmetics_RangeExpression, Through, cobol_arithmetics_AdditiveArithmeticExpression, RangeExpressionChild, cobol_arithmetics_NestedArithmeticExpression, PrimaryExpression, cobol_arithmetics_ArithmeticExpression, conditions_AbbreviatedRelationalExpressionChild, conditions_SimpleConditionChild, cobol_containers_CompilationGroup, containers_CobolRoot, commons_NamedElement, CompilationUnit, cobol_containers_CompilationUnit, NamedElement, IdentificationDivision, EnvironmentDivision, DataDivision, ProcedureDivision, cobol_containers_CobolRoot, cobol_containers_EmptyModel, CobolRoot, cobol_divisions_Division, Section, Paragraph, StatementContainer, cobol_divisions_DataDivision, Division, cobol_divisions_EnvironmentDivision, cobol_divisions_IdentificationDivision, divisions_Division, water_IncompleteElement, cobol_divisions_ProcedureDivision, parameters_Parametrizable, cobol_arithmetics_RangeExpressionChild, Declaratives, cobol_literals_Literal, water_SelectStatementWater, water_SpecialNamesParagraphWater, water_CICSStatementWater, operands_PrimaryOperand, water_InvokeStatementWater, labels_StopLabel, cobol_literals_AlphanumericLiteral, Literal, cobol_literals_IntegerLiteral, literals_NumericLiteral, water_ObjectComputerParagraphWater, water_FileDescriptorWater, water_IOControlParagraphWater, cobol_literals_DecimalLiteral, NumericLiteral, cobol_literals_FigurativeConstantLiteral, cobol_literals_BooleanLiteral, cobol_literals_FloatingDecimalLiteral, DecimalLiteral, cobol_literals_AllLiteral, FigurativeConstantLiteral, ConstantLiteral, cobol_literals_NumericLiteral, cobol_literals_ConstantLiteral, cobol_literals_PseudoLiteral, cobol_literals_DBCSLiteral, cobol_literals_NationalLiteral, DBCSLiteral, cobol_literals_FixedDecimalLiteral, cobol_literals_NationalHexLiteral, cobol_literals_Null, cobol_literals_Zero, cobol_literals_Quote, cobol_literals_LowValue, cobol_literals_HighValue, cobol_literals_Space, cobol_literals_Any, cobol_literals_Characters, cobol_literals_AlphanumericHexaDecimalLiteral, AlphanumericLiteral, cobol_operators_Operator, cobol_operators_AdditiveOperator, Operator, cobol_operators_MultiplicativeOperator, cobol_operators_UnaryOperator, cobol_operators_RelationalOperator, cobol_operators_ConditionOr, cobol_operators_ConditionAnd, cobol_operators_Multiplication, cobol_operators_SignOperator, cobol_operators_Positive, cobol_operators_Negative, cobol_operators_Division, cobol_operators_Addition, operators_AdditiveOperator, operators_UnaryOperator, cobol_operators_Subtraction, cobol_operators_GreaterThanOrEqual, cobol_operators_GreaterThan, cobol_operators_LessThan, cobol_operators_LessThanOrEqual, cobol_operators_Equal, cobol_operators_Power, cobol_operators_Negate, cobol_operators_Through, cobol_operators_ClassOperator, cobol_operators_Zero, cobol_operators_ClassName, cobol_operators_Alphabetic, cobol_operators_DBCS, cobol_operators_Numeric, cobol_operators_AlphabeticUpper, cobol_operators_AlphabeticLower, cobol_operators_LogicalOperator, cobol_operators_Kanji, cobol_operators_EqualPhrase, cobol_operators_EqualSign, cobol_operators_LTPhrase, LessThan, cobol_operators_LTSign, cobol_operators_LTEQPhrase, LessThanOrEqual, cobol_operators_LTEQSign, cobol_operators_GTPhrase, GreaterThan, cobol_operators_GTSign, cobol_operators_GTEQPhrase, GreaterThanOrEqual, cobol_operators_GTEQSign, cobol_paragraphs_Paragraph, labels_Procedure, cobol_paragraphs_SourceComputerParagraph, ConfigurationSectionParagraph, DebuggingMode, cobol_paragraphs_ObjectComputerParagraph, paragraphs_ConfigurationSectionParagraph, cobol_paragraphs_FileControlParagraph, IOSectionParagraph, SelectStatement, cobol_paragraphs_IOControlParagraph, paragraphs_IOSectionParagraph, cobol_paragraphs_ConfigurationSectionParagraph, cobol_paragraphs_IOSectionParagraph, cobol_paragraphs_SpecialNamesParagraph, SpecialNameStatement, cobol_paragraphs_DebuggingMode, cobol_references_Reference, cobol_references_ReferenceableElement, ReferenceableElement, cobol_references_ElementReference, Reference, cobol_references_SpecialNamesConditionNameReference, references_ElementReference, references_Qualifiable, references_ConditionName, cobol_references_FileNameReference, references_IdentifierReferenceQualifier, cobol_references_IndexNameReference, IdentifierReference, cobol_references_MnemonicNameReference, cobol_references_AlphabetNameReference, ElementReference, cobol_references_ConditionName, cobol_references_Qualifiable, cobol_references_ConditionNameReference, identifiers_IdentifierReference, cobol_references_DataNameReference, cobol_references_IdentifierReferenceQualifier, cobol_sections_Section, cobol_sections_WorkingStorageSection, DataDivisionSection, cobol_sections_LocalStorageSection, SpecialNamesParagraphWater, cobol_sections_LinkageStorageSection, cobol_sections_IOSection, EnvironmentDivisionSection, cobol_paragraphs_RepositoryParagraph, cobol_sections_EnvironmentDivisionSection, cobol_sections_DataDivisionSection, Statement, DataItem, cobol_sections_FileSection, FileName, cobol_sections_DeclarativeSection, cobol_sentences_StatementContainer, cobol_sentences_EmptySentence, Sentence, cobol_sentences_UseSentence, sentences_StatementContainer, cobol_sentences_AlteredGoTo, cobol_sentences_ExitProcedure, cobol_sentences_EntrySentence, cobol_sentences_ExecuteSentence, cobol_sentences_Sentence, cobol_operands_PrimaryOperand, operands_ReplacementOperand, operands_Operand, arithmetics_PrimaryExpression, operands_ArithmeticOperand, cobol_sections_ConfigurationSection, cobol_operands_ReplacementOperand, Operand, cobol_operands_Encoding, ReplacementOperand, cobol_operands_Operand, cobol_operands_ArithmeticOperand, cobol_statements_Statement, cobol_statements_ArithmeticStatement, statements_Statement, statements_ErrorHandled, cobol_statements_Add, ArithmeticStatement, cobol_statements_Subtract, cobol_statements_Multiply, cobol_operands_RoundedIdentifier, ArithmeticOperand, Identifier, cobol_statements_Perform, cobol_statements_PerformNestedStatement, statements_Perform, statements_NestedStatement, cobol_statements_PerformProcedure, Perform, ProcedureRangeLabel, cobol_statements_Jump, cobol_statements_NextSentence, Jump, cobol_statements_GoTo, cobol_statements_GoBack, cobol_statements_NestedStatement, cobol_statements_Move, PrimaryOperand, cobol_statements_Exit, cobol_statements_Condition, cobol_statements_Divide, statements_Conditional, cobol_statements_Conditional, cobol_statements_Stop, StopLabel, cobol_statements_Display, Environment, cobol_statements_Compute, AssignmentExpression, cobol_statements_Accept, cobol_statements_Execute, cobol_statements_ErrorHandled, Handler, cobol_statements_Return, FileNameReference, cobol_statements_SetStatement, cobol_statements_SetSwitches, SetStatement, SwitchStatus, cobol_statements_SetIndexName, IndexNameReference, cobol_statements_String, ConcatenatingStrings, cobol_statements_Close, statements_IOStatement, cobol_statements_Cancel, cobol_statements_Initialize, Replacement, cobol_statements_Open, cobol_statements_SearchStatement, NormalEvaluateCase, cobol_statements_SerialSearch, SearchStatement, cobol_statements_BinarySearch, cobol_statements_Unstring, cobol_statements_Call, functions_Argumentable, cobol_statements_Evaluate, EvaluateCase, ExpressionList, cobol_statements_NormalEvaluateCase, cobol_statements_OtherEvaluateCase, cobol_statements_EvaluateCase, NestedStatement, cobol_statements_Replace, cobol_statements_Entry, cobol_statements_Inspect, TallyingIn, cobol_statements_Set, cobol_statements_Read, SplittedString, cobol_statements_Write, IntegerLiteral, MnemonicNameReference, cobol_statements_Rewrite, Write, cobol_statements_SwitchStatus, cobol_statements_PerformProcedureFixedTimes, statements_PerformProcedure, statements_PerformFixedTimes, cobol_statements_PerformUntilCondition, statements_VaryingUntilCondition, cobol_statements_PerformFixedTimes, AfterUntilCondition, cobol_statements_PerformNestedStatementFixedTimes, statements_PerformNestedStatement, cobol_statements_PerformNestedStatementUntilCondition, cobol_statements_Continue, cobol_statements_FileIOStatement, InputDirective, OutputDirective, KeyDescriptor, cobol_statements_Sort, statements_FileIOStatement, cobol_statements_Merge, cobol_statements_Release, cobol_statements_KeyDescriptor, cobol_statements_IOStatement, IOFileDescriptor, cobol_statements_PerformProcedureUntilCondition, statements_PerformUntilCondition, cobol_statements_IOFile, IncompleteElement, cobol_statements_TallyingIn, Tallying, cobol_statements_Delete, cobol_identifiers_Subscript, cobol_identifiers_Identifier, water_AcceptStatementWater, water_RepositoryParagraphWater, water_IdentificationDivisionWater, water_SQLStatementWater, cobol_statements_IOFileDescriptor, IOFile, cobol_statements_VaryingUntilCondition, Conditional, cobol_statements_AfterUntilCondition, VaryingUntilCondition, cobol_statements_Start, cobol_identifiers_Qualifier, cobol_identifiers_RelativeSubscript, cobol_identifiers_DirectSubscript, cobol_ios_InputProcedure, ios_InputDirective, ios_ProcedureDirective, cobol_ios_InputDirective, IODirectives, cobol_ios_InputFile, ios_FileDirective, water_UseStatementWater, water_DataDescriptorWater, water_SortPhraseWater, ReferenceModifier, cobol_identifiers_IdentifierReference, identifiers_Identifier, Subscript, Qualifier, cobol_identifiers_All, DirectSubscript, cobol_identifiers_ReferenceModifier, cobol_identifiers_LinageCounter, cobol_water_Dot, cobol_ios_OutputDirective, cobol_ios_OutputProcedure, ios_OutputDirective, cobol_ios_OutputFile, cobol_ios_IODirectives, cobol_ios_FileDirective, cobol_ios_ProcedureDirective, Label, cobol_water_IncompleteElement, Water, cobol_water_IdentificationDivisionWater, cobol_water_Water, cobol_water_ProgramDescription, IdentificationDivisionWater, cobol_water_SpecialNamesParagraphWater, cobol_water_SpecialNamesClause, cobol_water_FileDescriptorWater, cobol_water_ObjectComputerParagraphWater, cobol_water_ObjectComputerDescription, ObjectComputerParagraphWater, cobol_water_PriorityNumber, cobol_water_SelectStatementWater, cobol_water_SelectStatementClause, SelectStatementWater, cobol_water_FileDescription, FileDescriptorWater, cobol_water_DataDescriptorWater, cobol_water_DataDescription, DataDescriptorWater, cobol_water_IOControlParagraphWater, cobol_water_IOControlDescription, IOControlParagraphWater, cobol_water_RepositoryParagraphWater, cobol_water_RepositoryDescription, RepositoryParagraphWater, cobol_water_SQLStatementWater, cobol_water_CICSStatementWater, cobol_water_SQLStatementToken, SQLStatementWater, cobol_water_CICSStatementToken, CICSStatementWater, cobol_water_AcceptStatementWater, cobol_water_AcceptStatementToken, AcceptStatementWater, cobol_water_UseStatementWater, cobol_water_UseStatementToken, UseStatementWater, cobol_water_InvokeStatementWater, cobol_water_InvokeStatementToken, InvokeStatementWater, cobol_water_CloseStatementWater, cobol_water_CloseStatementToken, CloseStatementWater, cobol_water_OpenStatementWater, cobol_water_OpenStatementToken, OpenStatementWater, cobol_water_SortPhraseToken, SortPhraseWater, cobol_water_SortPhraseWater, cobol_registers_ShiftIn, Register, cobol_registers_ShiftOut, cobol_registers_AddressOf, cobol_registers_LengthOf, cobol_registers_ReturnCode, cobol_registers_WhenCompiled, cobol_environments_SystemDevice, cobol_environments_SystemLogicalInput, SystemDevice, cobol_environments_UPSI, cobol_environments_SystemPunchDevice, cobol_registers_Register, cobol_environments_Console, cobol_environments_Channel, cobol_environments_AdvancedFunctionPrinting, cobol_environments_SuppressSpacing, cobol_environments_Pocket, cobol_environments_SystemLogicalOutput, cobol_environments_Environment, RangeExpression, cobol_dataitems_ConditionName, cobol_dataitems_Global, cobol_dataitems_External, cobol_dataitems_Value, cobol_dataitems_DataItemAttribute, cobol_dataitems_Usage, cobol_dataitems_GroupUsage, cobol_dataitems_DataItem, references_ReferenceableElement, cobol_dataitems_PictureString, DataItemAttribute, cobol_dataitems_RenamingDataName, DataName, cobol_dataitems_RecordName, cobol_dataitems_DataName, cobol_dataitems_Redefines, specialnames_SpecialName, cobol_specialnames_OnStatus, ConditionName, cobol_specialnames_OffStatus, cobol_specialnames_AlphabetName, specialnames_SpecialNameStatement, AlphabetType, cobol_specialnames_UPSISwitchIs, specialnames_MnemonicName, cobol_specialnames_AlphabetType, cobol_specialnames_PredefinedAlphabetType, cobol_specialnames_ExplicitAlphabetType, cobol_specialnames_SpecialName, cobol_specialnames_ConditionName, cobol_specialnames_CodeNameAlphabetType, cobol_specialnames_CurrencySign, cobol_specialnames_ClassName, cobol_specialnames_MnemonicName, SpecialName, cobol_specialnames_SystemDeviceIs, cobol_specialnames_SymbolicCharacter, SymbolicCharacter, AlphabetNameReference, cobol_specialnames_SpecialNameStatement, cobol_tables_Table, dataitems_DataItem, TableDimension, IndexName, KeyName, cobol_tables_KeyName, cobol_tables_IndexName, AdditionalIndexName, cobol_tables_TableDimension, cobol_specialnames_SymbolicCharacterStatement, cobol_tables_AdditionalIndexName, cobol_files_FileName, cobol_files_SelectStatement, FileStatus, cobol_files_FileStatus, cobol_parameters_Parametrizable, Parameter_, cobol_parameters_Parameter, cobol_declaratives_Declaratives, DeclarativeSection, cobol_verbs_Is, Verb, cobol_verbs_Verb, cobol_labels_ProcedureRange, ProcedureRangeChild, cobol_labels_ProcedureRangeLabel, cobol_labels_ProcedureRangeChild, Procedure, cobol_labels_ProcedureLabel, cobol_labels_Procedure, cobol_labels_Label, cobol_labels_StopLabel, cobol_labels_Run, cobol_functions_FunctionCall, cobol_functions_Argument, cobol_functions_ByReferenceArgument, Argument, cobol_functions_ByValueArgument, cobol_functions_ByContentArgument, cobol_functions_OmittedArgument, cobol_functions_Argumentable, cobol_parameters_ByReferenceParameter, cobol_parameters_ByValueParameter, cobol_handlers_OnSizeError, cobol_handlers_Handler, cobol_handlers_NotOnSizeError, NotErrorHandler, cobol_handlers_OnOverflow, cobol_handlers_OnException, cobol_handlers_NotOnException, cobol_handlers_NotErrorHandler, cobol_handlers_NotOnOverflow, cobol_handlers_NotAtEnd, cobol_handlers_AtEnd, cobol_handlers_AtEndOfPage, cobol_handlers_InvalidKey, cobol_handlers_NotAtEndOfPage, cobol_handlers_NotInvalidKey, cobol_strings_Tallying, StringManipulation, cobol_strings_StringManipulation, String, Location, cobol_strings_ManipulatedStrings, cobol_strings_String, cobol_strings_ConcatenatingStrings, ManipulatedStrings, cobol_strings_SplittedString, cobol_strings_Replacement, cobol_strings_Occurrence, cobol_strings_TallyingOccurrence, strings_Tallying, strings_Occurrence, cobol_strings_ReplacementOccurrence, strings_Replacement, cobol_strings_AnyCharacter, cobol_strings_SpecificCharacter, cobol_strings_AnyCharacterBySpecificCharacter, cobol_strings_SpecificCharacterBySpecificCharacter, cobol_strings_Location, Properties, Nulls, Zeroes, Quotes, LowValues, HighValues, Spaces, ThroughPhrase, EncodingTypes, ExitLabels, Adjustings, Status, EOP, IOTypes, Orders, Corresponding, ProgramDescriptionInfo, ObjectComputerDescriptionInfo, SpecialNamesClauses, FileDescriptionInfo, SelectStatementClauses, IOControlDescriptionInfo, DataDescriptionInfo, CICSStatementTokens, RepositoryDescriptionInfo, SQLStatementTokens, AcceptStatementTokens, UseStatementTokens, CloseStatementTokens, InvokeStatementTokens, SortPhraseTokens, OpenStatementTokens, UPSISwitches, SystemInputs, SystemOutputs, SystemPunchDevices, Selects, Channels, Usages, PictureStringCharacters, PredefinedAlphabetTypes, FileDescriptors, SortingOrder, Positions, Occurrences},
    associations={children0, logicalOperators1, child3, negateOperator4, children6, relationalOperator7, negateOperator9, is12, expressions14, children15, children16, relationalOperator21, child23, negateOperator25, is28, expression31, rest33, child36, signOperator38, negateOperator40, is43, child46, classOperator48, negateOperator50, is53, child17, condition56, negateOperator18, children58, additiveOperators59, children61, multiplicativeOperators62, children64, child65, unaryOperator66, assignmentOperator68, children69, value71, children74, throughOperator75, expression77, compilationUnits79, identificationDivision80, environmentDivision81, dataDivision83, procedureDivision85, nestedCompilationUnits87, sections90, paragraphs91, sentences93, declaratives95, constant96, sentences97, withDebuggingMode99, selectStatements100, aliasesTo104, aliasesFrom105, target108, qualifier110, sentences111, paragraphs113, specialNameStatements101, water102, statements116, records117, fileDescriptors119, statements120, next122, next124, operands126, givings127, tos130, froms132, identifier123, intos136, remainders138, label141, labels142, dependsOn144, statements145, receivers147, sender148, bys134, elseStatements151, condition153, label155, operands156, output158, expression160, receiver161, handlers163, fileName164, output165, sender168, switches170, receivers171, pointer172, receiver174, senders177, subprograms179, subprogram181, subprograms183, replacements185, cases187, table188, variable191, pointer193, tally195, delimiter203, counter206, cases209, subject210, objects212, tallyingIns214, replacements215, conversions218, string221, receivers224, sender198, receiver226, receivers201, keyName228, fileName231, recordName234, numLines236, integer239, mnemonicName241, sender243, mnemonicNames246, conditions248, afters252, fileName253, input255, output257, keyDescriptors259, recordName261, sender263, keyNames266, ioFileDescriptors268, iterations250, fileName270, occurrences272, fileName295, subscript297, counter273, ioFiles269, variable276, init278, increment281, fileName284, operator286, dataName289, not292, additiveOperator307, integer309, modifier298, subscripts299, qualifiers300, start302, length304, fileNames312, label314, water315, operand316, nameRange318, values319, subentries322, superentry324, attributes321, elems327, dataName329, type331, conditionNames332, currency335, range336, environment338, range333, integers340, symbolicCharacters342, alphabetNameReference343, tableDimension345, indexedBy346, keysAre348, maxTableDimension350, dependsOn353, keys356, additionalIndexNames358, records359, attributes361, sentences364, fileStatus367, fileNameReference368, fileStatus371, vsamFileStatus373, parameters376, returning377, declarativeSections380, children381, throughOperator382, target385, section386, operands388, arguments390, handlerStatement394, locations396, strings397, delimiter399, counter402, returning391, base404, target406, occurrences407, occurrences409, tallying411, source413},
    generalizations={gen_cobol_commons_NamedElement_Commentable, gen_cobol_commons_LabellableElement_Commentable, gen_cobol_commons_URIableElement_Commentable, gen_cobol_conditions_ConditionalOrExpression_Condition, gen_cobol_conditions_ConditionalOrExpressionChild_Condition, gen_cobol_conditions_NegatedConditionalExpression_ConditionalAndExpressionChild, gen_cobol_conditions_NegatedConditionalExpressionChild_ConditionalAndExpressionChild, gen_cobol_conditions_SimpleConditionChild_NegatedConditionalExpressionChild, gen_cobol_conditions_RelationalExpression_NegatedConditionalExpressionChild, gen_cobol_conditions_ConditionalAndExpressionChild_ConditionalOrExpressionChild, gen_cobol_conditions_ConditionalAndExpression_ConditionalOrExpressionChild, gen_cobol_conditions_AbbreviatedConditionalExpression_ConditionalAndExpressionChild, gen_cobol_conditions_AbbreviatedConditionalExpressionChild_ConditionalAndExpressionChild, gen_cobol_conditions_NegatedAbbreviatedConditionalExpression_AbbreviatedConditionalExpressionChild, gen_cobol_conditions_NegatedAbbreviatedConditionalExpressionChild_AbbreviatedConditionalExpressionChild, gen_cobol_conditions_AbbreviatedRelationalExpression_NegatedAbbreviatedConditionalExpressionChild, gen_cobol_conditions_NestedAbbreviatedConditionalExpression_AbbreviatedRelationalExpressionChild, gen_cobol_conditions_SignCondition_NegatedConditionalExpressionChild, gen_cobol_conditions_ClassCondition_NegatedConditionalExpressionChild, gen_cobol_conditions_AbbreviatedRelationalExpressionChild_NegatedAbbreviatedConditionalExpressionChild, gen_cobol_conditions_NestedCondition_SimpleConditionChild, gen_cobol_arithmetics_AdditiveArithmeticExpression_RangeExpressionChild, gen_cobol_arithmetics_AdditiveArithmeticExpressionChild_RangeExpressionChild, gen_cobol_arithmetics_MultiplicativeArithmeticExpression_AdditiveArithmeticExpressionChild, gen_cobol_arithmetics_MultiplicativeArithmeticExpressionChild_AdditiveArithmeticExpressionChild, gen_cobol_arithmetics_PowerArithmeticExpression_MultiplicativeArithmeticExpressionChild, gen_cobol_arithmetics_PowerArithmeticExpressionChild_MultiplicativeArithmeticExpressionChild, gen_cobol_arithmetics_UnaryArithmeticExpressionChild_PowerArithmeticExpressionChild, gen_cobol_arithmetics_UnaryArithmeticExpression_PowerArithmeticExpressionChild, gen_cobol_arithmetics_PrimaryExpression_UnaryArithmeticExpressionChild, gen_cobol_arithmetics_RangeExpression_ArithmeticExpression, gen_cobol_arithmetics_NestedArithmeticExpression_PrimaryExpression, gen_cobol_arithmetics_ArithmeticExpression_conditions_AbbreviatedRelationalExpressionChild, gen_cobol_arithmetics_ArithmeticExpression_conditions_SimpleConditionChild, gen_cobol_containers_CompilationGroup_containers_CobolRoot, gen_cobol_containers_CompilationGroup_commons_NamedElement, gen_cobol_containers_CompilationUnit_NamedElement, gen_cobol_containers_EmptyModel_CobolRoot, gen_cobol_divisions_Division_NamedElement, gen_cobol_divisions_DataDivision_Division, gen_cobol_divisions_EnvironmentDivision_Division, gen_cobol_divisions_IdentificationDivision_divisions_Division, gen_cobol_divisions_IdentificationDivision_water_IncompleteElement, gen_cobol_divisions_ProcedureDivision_divisions_Division, gen_cobol_divisions_ProcedureDivision_parameters_Parametrizable, gen_cobol_arithmetics_RangeExpressionChild_ArithmeticExpression, gen_cobol_literals_Literal_water_SelectStatementWater, gen_cobol_literals_Literal_water_SpecialNamesParagraphWater, gen_cobol_literals_Literal_water_CICSStatementWater, gen_cobol_literals_Literal_operands_PrimaryOperand, gen_cobol_literals_Literal_water_InvokeStatementWater, gen_cobol_literals_Literal_labels_StopLabel, gen_cobol_literals_AlphanumericLiteral_Literal, gen_cobol_literals_IntegerLiteral_literals_NumericLiteral, gen_cobol_literals_IntegerLiteral_water_ObjectComputerParagraphWater, gen_cobol_literals_IntegerLiteral_water_FileDescriptorWater, gen_cobol_literals_IntegerLiteral_water_IOControlParagraphWater, gen_cobol_literals_DecimalLiteral_NumericLiteral, gen_cobol_literals_FigurativeConstantLiteral_Literal, gen_cobol_literals_BooleanLiteral_Literal, gen_cobol_literals_FloatingDecimalLiteral_DecimalLiteral, gen_cobol_literals_AllLiteral_FigurativeConstantLiteral, gen_cobol_literals_NumericLiteral_Literal, gen_cobol_literals_ConstantLiteral_FigurativeConstantLiteral, gen_cobol_literals_PseudoLiteral_Literal, gen_cobol_literals_DBCSLiteral_Literal, gen_cobol_literals_NationalLiteral_DBCSLiteral, gen_cobol_literals_FixedDecimalLiteral_DecimalLiteral, gen_cobol_literals_NationalHexLiteral_DBCSLiteral, gen_cobol_literals_Null_ConstantLiteral, gen_cobol_literals_Zero_ConstantLiteral, gen_cobol_literals_Quote_ConstantLiteral, gen_cobol_literals_LowValue_ConstantLiteral, gen_cobol_literals_HighValue_ConstantLiteral, gen_cobol_literals_Space_ConstantLiteral, gen_cobol_literals_Any_Literal, gen_cobol_literals_Characters_Literal, gen_cobol_literals_AlphanumericHexaDecimalLiteral_AlphanumericLiteral, gen_cobol_operators_AdditiveOperator_Operator, gen_cobol_operators_MultiplicativeOperator_Operator, gen_cobol_operators_UnaryOperator_Operator, gen_cobol_operators_LogicalOperator_Operator, gen_cobol_operators_RelationalOperator_Operator, gen_cobol_operators_ConditionOr_LogicalOperator, gen_cobol_operators_ConditionAnd_LogicalOperator, gen_cobol_operators_Multiplication_MultiplicativeOperator, gen_cobol_operators_SignOperator_Operator, gen_cobol_operators_Positive_SignOperator, gen_cobol_operators_Negative_SignOperator, gen_cobol_operators_Division_MultiplicativeOperator, gen_cobol_operators_Addition_operators_AdditiveOperator, gen_cobol_operators_Addition_operators_UnaryOperator, gen_cobol_operators_Subtraction_operators_AdditiveOperator, gen_cobol_operators_Subtraction_operators_UnaryOperator, gen_cobol_operators_GreaterThanOrEqual_RelationalOperator, gen_cobol_operators_GreaterThan_RelationalOperator, gen_cobol_operators_LessThan_RelationalOperator, gen_cobol_operators_LessThanOrEqual_RelationalOperator, gen_cobol_operators_Equal_RelationalOperator, gen_cobol_operators_Power_Operator, gen_cobol_operators_Negate_Operator, gen_cobol_operators_Through_Operator, gen_cobol_operators_ClassOperator_Operator, gen_cobol_operators_Zero_SignOperator, gen_cobol_operators_ClassName_ClassOperator, gen_cobol_operators_Alphabetic_ClassOperator, gen_cobol_operators_DBCS_ClassOperator, gen_cobol_operators_Numeric_ClassOperator, gen_cobol_operators_AlphabeticUpper_ClassOperator, gen_cobol_operators_AlphabeticLower_ClassOperator, gen_cobol_operators_Kanji_ClassOperator, gen_cobol_operators_EqualPhrase_Equal, gen_cobol_operators_EqualSign_Equal, gen_cobol_operators_LTPhrase_LessThan, gen_cobol_operators_LTSign_LessThan, gen_cobol_operators_LTEQPhrase_LessThanOrEqual, gen_cobol_operators_LTEQSign_LessThanOrEqual, gen_cobol_operators_GTPhrase_GreaterThan, gen_cobol_operators_GTSign_GreaterThan, gen_cobol_operators_GTEQPhrase_GreaterThanOrEqual, gen_cobol_operators_GTEQSign_GreaterThanOrEqual, gen_cobol_paragraphs_Paragraph_commons_NamedElement, gen_cobol_paragraphs_Paragraph_labels_Procedure, gen_cobol_paragraphs_SourceComputerParagraph_ConfigurationSectionParagraph, gen_cobol_paragraphs_ObjectComputerParagraph_paragraphs_ConfigurationSectionParagraph, gen_cobol_paragraphs_ObjectComputerParagraph_water_IncompleteElement, gen_cobol_paragraphs_FileControlParagraph_IOSectionParagraph, gen_cobol_paragraphs_IOControlParagraph_paragraphs_IOSectionParagraph, gen_cobol_paragraphs_IOControlParagraph_water_IncompleteElement, gen_cobol_paragraphs_ConfigurationSectionParagraph_Paragraph, gen_cobol_paragraphs_IOSectionParagraph_Paragraph, gen_cobol_paragraphs_SpecialNamesParagraph_ConfigurationSectionParagraph, gen_cobol_paragraphs_RepositoryParagraph_water_IncompleteElement, gen_cobol_references_ReferenceableElement_NamedElement, gen_cobol_references_ElementReference_Reference, gen_cobol_references_SpecialNamesConditionNameReference_references_ElementReference, gen_cobol_references_SpecialNamesConditionNameReference_references_Qualifiable, gen_cobol_references_SpecialNamesConditionNameReference_references_ConditionName, gen_cobol_references_FileNameReference_references_ElementReference, gen_cobol_references_FileNameReference_references_IdentifierReferenceQualifier, gen_cobol_references_IndexNameReference_IdentifierReference, gen_cobol_references_MnemonicNameReference_references_ElementReference, gen_cobol_references_MnemonicNameReference_references_Qualifiable, gen_cobol_references_AlphabetNameReference_ElementReference, gen_cobol_references_ConditionNameReference_identifiers_IdentifierReference, gen_cobol_references_ConditionNameReference_references_ConditionName, gen_cobol_references_DataNameReference_identifiers_IdentifierReference, gen_cobol_references_DataNameReference_references_IdentifierReferenceQualifier, gen_cobol_references_IdentifierReferenceQualifier_references_Qualifiable, gen_cobol_references_IdentifierReferenceQualifier_references_ElementReference, gen_cobol_sections_Section_commons_NamedElement, gen_cobol_sections_Section_labels_Procedure, gen_cobol_sections_WorkingStorageSection_DataDivisionSection, gen_cobol_sections_LocalStorageSection_DataDivisionSection, gen_cobol_sections_LinkageStorageSection_DataDivisionSection, gen_cobol_sections_IOSection_EnvironmentDivisionSection, gen_cobol_paragraphs_RepositoryParagraph_paragraphs_ConfigurationSectionParagraph, gen_cobol_sections_ConfigurationSection_EnvironmentDivisionSection, gen_cobol_sections_EnvironmentDivisionSection_Section, gen_cobol_sections_DataDivisionSection_Section, gen_cobol_sections_FileSection_DataDivisionSection, gen_cobol_sections_DeclarativeSection_Section, gen_cobol_sentences_EmptySentence_Sentence, gen_cobol_sentences_UseSentence_sentences_StatementContainer, gen_cobol_sentences_UseSentence_water_IncompleteElement, gen_cobol_sentences_AlteredGoTo_Sentence, gen_cobol_sentences_ExitProcedure_Sentence, gen_cobol_sentences_EntrySentence_Sentence, gen_cobol_sentences_ExecuteSentence_StatementContainer, gen_cobol_sentences_Sentence_StatementContainer, gen_cobol_operands_PrimaryOperand_operands_ReplacementOperand, gen_cobol_operands_PrimaryOperand_operands_Operand, gen_cobol_operands_PrimaryOperand_arithmetics_PrimaryExpression, gen_cobol_operands_PrimaryOperand_operands_ArithmeticOperand, gen_cobol_operands_ReplacementOperand_Operand, gen_cobol_operands_Encoding_ReplacementOperand, gen_cobol_operands_ArithmeticOperand_Operand, gen_cobol_statements_ArithmeticStatement_statements_Statement, gen_cobol_statements_ArithmeticStatement_statements_ErrorHandled, gen_cobol_statements_Add_ArithmeticStatement, gen_cobol_statements_Subtract_ArithmeticStatement, gen_cobol_statements_Multiply_ArithmeticStatement, gen_cobol_operands_RoundedIdentifier_ArithmeticOperand, gen_cobol_statements_Condition_statements_NestedStatement, gen_cobol_statements_Perform_Statement, gen_cobol_statements_PerformNestedStatement_statements_Perform, gen_cobol_statements_PerformNestedStatement_statements_NestedStatement, gen_cobol_statements_PerformProcedure_Perform, gen_cobol_statements_Jump_Statement, gen_cobol_statements_NextSentence_Jump, gen_cobol_statements_GoTo_Jump, gen_cobol_statements_GoBack_Jump, gen_cobol_statements_Move_Statement, gen_cobol_statements_Exit_Statement, gen_cobol_statements_Divide_ArithmeticStatement, gen_cobol_statements_Condition_statements_Conditional, gen_cobol_statements_Condition_statements_Statement, gen_cobol_statements_Stop_Statement, gen_cobol_statements_Display_Statement, gen_cobol_statements_Compute_statements_Statement, gen_cobol_statements_Compute_statements_ErrorHandled, gen_cobol_statements_Accept_statements_Statement, gen_cobol_statements_Accept_water_IncompleteElement, gen_cobol_statements_Execute_Statement, gen_cobol_statements_Return_statements_Statement, gen_cobol_statements_Return_statements_ErrorHandled, gen_cobol_statements_SetStatement_Statement, gen_cobol_statements_SetSwitches_SetStatement, gen_cobol_statements_SetIndexName_SetStatement, gen_cobol_statements_String_statements_Statement, gen_cobol_statements_String_statements_ErrorHandled, gen_cobol_statements_Close_water_IncompleteElement, gen_cobol_statements_Close_statements_IOStatement, gen_cobol_statements_Cancel_Statement, gen_cobol_statements_Initialize_Statement, gen_cobol_statements_Open_water_IncompleteElement, gen_cobol_statements_Open_statements_IOStatement, gen_cobol_statements_SearchStatement_statements_Statement, gen_cobol_statements_SearchStatement_statements_ErrorHandled, gen_cobol_statements_SerialSearch_SearchStatement, gen_cobol_statements_BinarySearch_SearchStatement, gen_cobol_statements_Unstring_statements_ErrorHandled, gen_cobol_statements_Unstring_statements_Statement, gen_cobol_statements_Call_statements_Statement, gen_cobol_statements_Call_functions_Argumentable, gen_cobol_statements_Call_statements_ErrorHandled, gen_cobol_statements_Evaluate_Statement, gen_cobol_statements_NormalEvaluateCase_EvaluateCase, gen_cobol_statements_OtherEvaluateCase_EvaluateCase, gen_cobol_statements_EvaluateCase_NestedStatement, gen_cobol_statements_Replace_Statement, gen_cobol_statements_Entry_parameters_Parametrizable, gen_cobol_statements_Entry_statements_Statement, gen_cobol_statements_Inspect_Statement, gen_cobol_statements_Set_SetStatement, gen_cobol_statements_Read_statements_Statement, gen_cobol_statements_Read_statements_ErrorHandled, gen_cobol_statements_Write_statements_Statement, gen_cobol_statements_Write_statements_ErrorHandled, gen_cobol_statements_Rewrite_Write, gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformProcedure, gen_cobol_statements_PerformProcedureFixedTimes_statements_PerformFixedTimes, gen_cobol_statements_PerformUntilCondition_statements_Perform, gen_cobol_statements_PerformUntilCondition_statements_VaryingUntilCondition, gen_cobol_statements_PerformFixedTimes_Perform, gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformNestedStatement, gen_cobol_statements_PerformNestedStatementFixedTimes_statements_PerformFixedTimes, gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformUntilCondition, gen_cobol_statements_PerformNestedStatementUntilCondition_statements_PerformNestedStatement, gen_cobol_statements_Continue_Jump, gen_cobol_statements_FileIOStatement_Statement, gen_cobol_statements_Sort_statements_FileIOStatement, gen_cobol_statements_Sort_water_IncompleteElement, gen_cobol_statements_Merge_statements_FileIOStatement, gen_cobol_statements_Merge_water_IncompleteElement, gen_cobol_statements_Release_Statement, gen_cobol_statements_IOStatement_Statement, gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformUntilCondition, gen_cobol_statements_PerformProcedureUntilCondition_statements_PerformProcedure, gen_cobol_statements_IOFile_IncompleteElement, gen_cobol_statements_Delete_statements_Statement, gen_cobol_statements_Delete_statements_ErrorHandled, gen_cobol_identifiers_Identifier_operands_PrimaryOperand, gen_cobol_identifiers_Identifier_water_AcceptStatementWater, gen_cobol_identifiers_Identifier_water_CICSStatementWater, gen_cobol_identifiers_Identifier_water_SpecialNamesParagraphWater, gen_cobol_identifiers_Identifier_water_ObjectComputerParagraphWater, gen_cobol_identifiers_Identifier_water_RepositoryParagraphWater, gen_cobol_identifiers_Identifier_water_IOControlParagraphWater, gen_cobol_identifiers_Identifier_water_IdentificationDivisionWater, gen_cobol_identifiers_Identifier_water_InvokeStatementWater, gen_cobol_identifiers_Identifier_water_SQLStatementWater, gen_cobol_statements_VaryingUntilCondition_Conditional, gen_cobol_statements_AfterUntilCondition_VaryingUntilCondition, gen_cobol_statements_Start_statements_ErrorHandled, gen_cobol_statements_Start_statements_Statement, gen_cobol_identifiers_Qualifier_ElementReference, gen_cobol_identifiers_RelativeSubscript_Subscript, gen_cobol_identifiers_DirectSubscript_Subscript, gen_cobol_ios_InputProcedure_ios_InputDirective, gen_cobol_ios_InputProcedure_ios_ProcedureDirective, gen_cobol_ios_InputDirective_IODirectives, gen_cobol_ios_InputFile_ios_InputDirective, gen_cobol_ios_InputFile_ios_FileDirective, gen_cobol_identifiers_Identifier_water_UseStatementWater, gen_cobol_identifiers_Identifier_water_FileDescriptorWater, gen_cobol_identifiers_Identifier_water_DataDescriptorWater, gen_cobol_identifiers_Identifier_water_SelectStatementWater, gen_cobol_identifiers_Identifier_water_SortPhraseWater, gen_cobol_identifiers_IdentifierReference_identifiers_Identifier, gen_cobol_identifiers_IdentifierReference_references_ElementReference, gen_cobol_identifiers_IdentifierReference_references_Qualifiable, gen_cobol_identifiers_All_DirectSubscript, gen_cobol_identifiers_LinageCounter_identifiers_Identifier, gen_cobol_identifiers_LinageCounter_references_Qualifiable, gen_cobol_water_Dot_water_IdentificationDivisionWater, gen_cobol_water_Dot_water_SQLStatementWater, gen_cobol_ios_OutputDirective_IODirectives, gen_cobol_ios_OutputProcedure_ios_ProcedureDirective, gen_cobol_ios_OutputProcedure_ios_OutputDirective, gen_cobol_ios_OutputFile_ios_OutputDirective, gen_cobol_ios_OutputFile_ios_FileDirective, gen_cobol_ios_FileDirective_IODirectives, gen_cobol_ios_ProcedureDirective_IODirectives, gen_cobol_water_IdentificationDivisionWater_Water, gen_cobol_water_ProgramDescription_IdentificationDivisionWater, gen_cobol_water_SpecialNamesParagraphWater_Water, gen_cobol_water_SpecialNamesClause_SpecialNamesParagraphWater, gen_cobol_water_FileDescriptorWater_Water, gen_cobol_water_ObjectComputerParagraphWater_Water, gen_cobol_water_ObjectComputerDescription_ObjectComputerParagraphWater, gen_cobol_water_PriorityNumber_ObjectComputerParagraphWater, gen_cobol_water_SelectStatementWater_Water, gen_cobol_water_SelectStatementClause_SelectStatementWater, gen_cobol_water_FileDescription_FileDescriptorWater, gen_cobol_water_DataDescriptorWater_Water, gen_cobol_water_DataDescription_DataDescriptorWater, gen_cobol_water_IOControlParagraphWater_Water, gen_cobol_water_IOControlDescription_IOControlParagraphWater, gen_cobol_water_RepositoryParagraphWater_Water, gen_cobol_water_RepositoryDescription_RepositoryParagraphWater, gen_cobol_water_SQLStatementWater_Water, gen_cobol_water_CICSStatementWater_Water, gen_cobol_water_SQLStatementToken_SQLStatementWater, gen_cobol_water_CICSStatementToken_CICSStatementWater, gen_cobol_water_AcceptStatementWater_Water, gen_cobol_water_AcceptStatementToken_AcceptStatementWater, gen_cobol_water_UseStatementWater_Water, gen_cobol_water_UseStatementToken_UseStatementWater, gen_cobol_water_InvokeStatementWater_Water, gen_cobol_water_InvokeStatementToken_InvokeStatementWater, gen_cobol_water_CloseStatementWater_Water, gen_cobol_water_CloseStatementToken_CloseStatementWater, gen_cobol_water_OpenStatementWater_Water, gen_cobol_water_OpenStatementToken_OpenStatementWater, gen_cobol_water_SortPhraseToken_SortPhraseWater, gen_cobol_water_SortPhraseWater_Water, gen_cobol_registers_Register_PrimaryOperand, gen_cobol_registers_ShiftIn_Register, gen_cobol_registers_ShiftOut_Register, gen_cobol_registers_AddressOf_Register, gen_cobol_registers_LengthOf_Register, gen_cobol_registers_ReturnCode_Register, gen_cobol_registers_WhenCompiled_Register, gen_cobol_environments_SystemDevice_Environment, gen_cobol_environments_SystemLogicalInput_SystemDevice, gen_cobol_environments_UPSI_Environment, gen_cobol_environments_SystemPunchDevice_SystemDevice, gen_cobol_environments_Console_SystemDevice, gen_cobol_environments_Channel_SystemDevice, gen_cobol_environments_AdvancedFunctionPrinting_SystemDevice, gen_cobol_environments_SuppressSpacing_SystemDevice, gen_cobol_environments_Pocket_SystemDevice, gen_cobol_environments_SystemLogicalOutput_SystemDevice, gen_cobol_environments_Environment_AcceptStatementWater, gen_cobol_dataitems_RenamingDataName_DataName, gen_cobol_dataitems_ConditionName_DataItem, gen_cobol_dataitems_Global_DataItemAttribute, gen_cobol_dataitems_External_DataItemAttribute, gen_cobol_dataitems_Value_DataItemAttribute, gen_cobol_dataitems_Usage_DataItemAttribute, gen_cobol_dataitems_GroupUsage_DataItemAttribute, gen_cobol_dataitems_DataItem_references_ReferenceableElement, gen_cobol_dataitems_DataItem_water_IncompleteElement, gen_cobol_dataitems_PictureString_DataItemAttribute, gen_cobol_dataitems_RecordName_DataItem, gen_cobol_dataitems_DataName_DataItem, gen_cobol_dataitems_Redefines_DataItemAttribute, gen_cobol_specialnames_ConditionName_specialnames_SpecialName, gen_cobol_specialnames_OnStatus_ConditionName, gen_cobol_specialnames_OffStatus_ConditionName, gen_cobol_specialnames_AlphabetName_specialnames_SpecialName, gen_cobol_specialnames_AlphabetName_specialnames_SpecialNameStatement, gen_cobol_specialnames_UPSISwitchIs_specialnames_MnemonicName, gen_cobol_specialnames_UPSISwitchIs_specialnames_SpecialNameStatement, gen_cobol_specialnames_PredefinedAlphabetType_AlphabetType, gen_cobol_specialnames_ExplicitAlphabetType_AlphabetType, gen_cobol_specialnames_SpecialName_ReferenceableElement, gen_cobol_specialnames_ConditionName_commons_NamedElement, gen_cobol_specialnames_CodeNameAlphabetType_AlphabetType, gen_cobol_specialnames_CurrencySign_specialnames_SpecialName, gen_cobol_specialnames_CurrencySign_specialnames_SpecialNameStatement, gen_cobol_specialnames_ClassName_specialnames_SpecialName, gen_cobol_specialnames_ClassName_specialnames_SpecialNameStatement, gen_cobol_specialnames_MnemonicName_SpecialName, gen_cobol_specialnames_SystemDeviceIs_specialnames_MnemonicName, gen_cobol_specialnames_SystemDeviceIs_specialnames_SpecialNameStatement, gen_cobol_specialnames_SymbolicCharacter_SpecialName, gen_cobol_tables_Table_dataitems_DataItem, gen_cobol_tables_Table_water_IncompleteElement, gen_cobol_tables_IndexName_commons_NamedElement, gen_cobol_tables_IndexName_references_ReferenceableElement, gen_cobol_specialnames_SymbolicCharacterStatement_specialnames_SpecialNameStatement, gen_cobol_specialnames_SymbolicCharacterStatement_references_ElementReference, gen_cobol_tables_AdditionalIndexName_ReferenceableElement, gen_cobol_files_FileName_water_IncompleteElement, gen_cobol_files_FileName_references_ReferenceableElement, gen_cobol_files_SelectStatement_IncompleteElement, gen_cobol_parameters_Parameter_ReferenceableElement, gen_cobol_verbs_Is_Verb, gen_cobol_labels_ProcedureRange_ProcedureRangeLabel, gen_cobol_labels_ProcedureRangeLabel_Label, gen_cobol_labels_ProcedureRangeChild_ProcedureRangeLabel, gen_cobol_labels_ProcedureLabel_ProcedureRangeChild, gen_cobol_labels_StopLabel_Label, gen_cobol_labels_Run_StopLabel, gen_cobol_functions_FunctionCall_functions_Argumentable, gen_cobol_functions_FunctionCall_commons_NamedElement, gen_cobol_functions_FunctionCall_identifiers_Identifier, gen_cobol_functions_ByReferenceArgument_Argument, gen_cobol_functions_ByValueArgument_Argument, gen_cobol_functions_ByContentArgument_Argument, gen_cobol_functions_OmittedArgument_Argument, gen_cobol_parameters_ByReferenceParameter_Parameter, gen_cobol_parameters_ByValueParameter_Parameter, gen_cobol_handlers_OnSizeError_Handler, gen_cobol_handlers_Handler_NestedStatement, gen_cobol_handlers_NotOnSizeError_NotErrorHandler, gen_cobol_handlers_OnOverflow_Handler, gen_cobol_handlers_OnException_Handler, gen_cobol_handlers_NotOnException_NotErrorHandler, gen_cobol_handlers_NotErrorHandler_Handler, gen_cobol_handlers_NotOnOverflow_NotErrorHandler, gen_cobol_handlers_NotAtEnd_NotErrorHandler, gen_cobol_handlers_AtEnd_Handler, gen_cobol_handlers_AtEndOfPage_Handler, gen_cobol_handlers_InvalidKey_Handler, gen_cobol_handlers_NotAtEndOfPage_NotErrorHandler, gen_cobol_handlers_NotInvalidKey_NotErrorHandler, gen_cobol_strings_Tallying_StringManipulation, gen_cobol_strings_StringManipulation_String, gen_cobol_strings_ManipulatedStrings_String, gen_cobol_strings_ConcatenatingStrings_ManipulatedStrings, gen_cobol_strings_SplittedString_ManipulatedStrings, gen_cobol_strings_Replacement_StringManipulation, gen_cobol_strings_TallyingOccurrence_strings_Tallying, gen_cobol_strings_TallyingOccurrence_strings_Occurrence, gen_cobol_strings_ReplacementOccurrence_strings_Occurrence, gen_cobol_strings_ReplacementOccurrence_strings_Replacement, gen_cobol_strings_AnyCharacter_Tallying, gen_cobol_strings_SpecificCharacter_Tallying, gen_cobol_strings_AnyCharacterBySpecificCharacter_Replacement, gen_cobol_strings_SpecificCharacterBySpecificCharacter_Replacement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)