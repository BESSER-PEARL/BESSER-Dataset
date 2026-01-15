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
AccessModifier: Enumeration = Enumeration(
    name="AccessModifier",
    literals={
            EnumerationLiteral(name="Public"),
			EnumerationLiteral(name="Private")
    }
)

DateTimePrecision: Enumeration = Enumeration(
    name="DateTimePrecision",
    literals={
            EnumerationLiteral(name="Year"),
			EnumerationLiteral(name="Month"),
			EnumerationLiteral(name="Week"),
			EnumerationLiteral(name="Day"),
			EnumerationLiteral(name="Hour"),
			EnumerationLiteral(name="Minute"),
			EnumerationLiteral(name="Second"),
			EnumerationLiteral(name="Millisecond")
    }
)

SortDirection: Enumeration = Enumeration(
    name="SortDirection",
    literals={
            EnumerationLiteral(name="asc"),
			EnumerationLiteral(name="ascending"),
			EnumerationLiteral(name="desc"),
			EnumerationLiteral(name="descending")
    }
)

# Classes
r1_Abs = Class(name="r1::Abs")
UnaryExpression = Class(name="UnaryExpression")
r1_Add = Class(name="r1::Add")
BinaryExpression = Class(name="BinaryExpression")
r1_After = Class(name="r1::After")
r1_AggregateExpression = Class(name="r1::AggregateExpression", is_abstract=True)
Expression = Class(name="Expression")
r1_Expression = Class(name="r1::Expression", is_abstract=True)
r1_AliasedQuerySource = Class(name="r1::AliasedQuerySource")
Element = Class(name="Element")
r1_AliasRef = Class(name="r1::AliasRef")
r1_AllTrue = Class(name="r1::AllTrue")
AggregateExpression = Class(name="AggregateExpression")
r1_AnyTrue = Class(name="r1::AnyTrue")
r1_As = Class(name="r1::As")
r1_TypeSpecifier = Class(name="r1::TypeSpecifier", is_abstract=True)
r1_And = Class(name="r1::And")
r1_Before = Class(name="r1::Before")
r1_BinaryExpression = Class(name="r1::BinaryExpression")
r1_ByColumn = Class(name="r1::ByColumn")
SortByItem = Class(name="SortByItem")
r1_Avg = Class(name="r1::Avg")
r1_ByExpression = Class(name="r1::ByExpression")
r1_CalculateAge = Class(name="r1::CalculateAge")
r1_CalculateAgeAt = Class(name="r1::CalculateAgeAt")
r1_ByDirection = Class(name="r1::ByDirection")
r1_CaseItem = Class(name="r1::CaseItem")
r1_Case = Class(name="r1::Case")
r1_Ceiling = Class(name="r1::Ceiling")
r1_Coalesce = Class(name="r1::Coalesce")
NaryExpression = Class(name="NaryExpression")
r1_Code = Class(name="r1::Code")
r1_CodeSystemRef = Class(name="r1::CodeSystemRef")
r1_CodeSystemDef = Class(name="r1::CodeSystemDef")
r1_Combine = Class(name="r1::Combine")
r1_Collapse = Class(name="r1::Collapse")
r1_Contains = Class(name="r1::Contains")
r1_Concatenate = Class(name="r1::Concatenate")
r1_Concept = Class(name="r1::Concept")
r1_Count = Class(name="r1::Count")
r1_Current = Class(name="r1::Current")
r1_Convert = Class(name="r1::Convert")
r1_DateFrom = Class(name="r1::DateFrom")
r1_DateTime = Class(name="r1::DateTime")
r1_DateTimeComponentFrom = Class(name="r1::DateTimeComponentFrom")
r1_DifferenceBetween = Class(name="r1::DifferenceBetween")
r1_DefineClause = Class(name="r1::DefineClause")
r1_Element = Class(name="r1::Element", is_abstract=True)
r1_EObject = Class(name="r1::EObject")
r1_Distinct = Class(name="r1::Distinct")
r1_Divide = Class(name="r1::Divide")
r1_DurationBetween = Class(name="r1::DurationBetween")
r1_Equal = Class(name="r1::Equal")
r1_Except = Class(name="r1::Except")
r1_Exists = Class(name="r1::Exists")
r1_End = Class(name="r1::End")
r1_Ends = Class(name="r1::Ends")
r1_Expand = Class(name="r1::Expand")
r1_ExpressionDef = Class(name="r1::ExpressionDef")
r1_ExpressionRef = Class(name="r1::ExpressionRef")
r1_Filter = Class(name="r1::Filter")
r1_Floor = Class(name="r1::Floor")
r1_ForEach = Class(name="r1::ForEach")
r1_First = Class(name="r1::First")
r1_OperandDef = Class(name="r1::OperandDef")
r1_FunctionRef = Class(name="r1::FunctionRef")
ExpressionRef = Class(name="ExpressionRef")
r1_FunctionDef = Class(name="r1::FunctionDef")
ExpressionDef = Class(name="ExpressionDef")
r1_If = Class(name="r1::If")
r1_Greater = Class(name="r1::Greater")
r1_GreaterOrEqual = Class(name="r1::GreaterOrEqual")
r1_IdentifierRef = Class(name="r1::IdentifierRef")
r1_In = Class(name="r1::In")
r1_IncludedIn = Class(name="r1::IncludedIn")
r1_Includes = Class(name="r1::Includes")
r1_IndexOf = Class(name="r1::IndexOf")
r1_Instance = Class(name="r1::Instance")
r1_InstanceElement = Class(name="r1::InstanceElement")
r1_InCodeSystem = Class(name="r1::InCodeSystem")
r1_Indexer = Class(name="r1::Indexer")
r1_Intersect = Class(name="r1::Intersect")
r1_Interval = Class(name="r1::Interval")
r1_IntervalTypeSpecifier = Class(name="r1::IntervalTypeSpecifier")
TypeSpecifier = Class(name="TypeSpecifier")
r1_InValueSet = Class(name="r1::InValueSet")
r1_ValueSetRef = Class(name="r1::ValueSetRef")
r1_IsNull = Class(name="r1::IsNull")
r1_IsTrue = Class(name="r1::IsTrue")
r1_Last = Class(name="r1::Last")
r1_Is = Class(name="r1::Is")
r1_IsFalse = Class(name="r1::IsFalse")
r1_ListTypeSpecifier = Class(name="r1::ListTypeSpecifier")
r1_Length = Class(name="r1::Length")
r1_Literal = Class(name="r1::Literal")
r1_Less = Class(name="r1::Less")
r1_LessOrEqual = Class(name="r1::LessOrEqual")
r1_List = Class(name="r1::List")
r1_Log = Class(name="r1::Log")
r1_Lower = Class(name="r1::Lower")
r1_Matches = Class(name="r1::Matches")
r1_Max = Class(name="r1::Max")
r1_MaxValue = Class(name="r1::MaxValue")
r1_Ln = Class(name="r1::Ln")
r1_Median = Class(name="r1::Median")
r1_Meets = Class(name="r1::Meets")
r1_MeetsAfter = Class(name="r1::MeetsAfter")
r1_MeetsBefore = Class(name="r1::MeetsBefore")
r1_MinValue = Class(name="r1::MinValue")
r1_Mode = Class(name="r1::Mode")
r1_Modulo = Class(name="r1::Modulo")
r1_Multiply = Class(name="r1::Multiply")
r1_NamedTypeSpecifier = Class(name="r1::NamedTypeSpecifier")
r1_Min = Class(name="r1::Min")
r1_Now = Class(name="r1::Now")
r1_NaryExpression = Class(name="r1::NaryExpression", is_abstract=True)
r1_Null = Class(name="r1::Null")
r1_Negate = Class(name="r1::Negate")
r1_Not = Class(name="r1::Not")
r1_NotEqual = Class(name="r1::NotEqual")
r1_OperandRef = Class(name="r1::OperandRef")
r1_Or = Class(name="r1::Or")
r1_Overlaps = Class(name="r1::Overlaps")
r1_OverlapsBefore = Class(name="r1::OverlapsBefore")
r1_ParameterDef = Class(name="r1::ParameterDef")
r1_OverlapsAfter = Class(name="r1::OverlapsAfter")
r1_ParameterRef = Class(name="r1::ParameterRef")
r1_PopulationStdDev = Class(name="r1::PopulationStdDev")
r1_Power = Class(name="r1::Power")
r1_PopulationVariance = Class(name="r1::PopulationVariance")
r1_PositionOf = Class(name="r1::PositionOf")
r1_ProperIn = Class(name="r1::ProperIn")
r1_ProperIncludedIn = Class(name="r1::ProperIncludedIn")
r1_ProperIncludes = Class(name="r1::ProperIncludes")
r1_Predecessor = Class(name="r1::Predecessor")
r1_ProperContains = Class(name="r1::ProperContains")
r1_Quantity = Class(name="r1::Quantity")
r1_Property = Class(name="r1::Property")
r1_RelationshipClause = Class(name="r1::RelationshipClause", is_abstract=True)
r1_Query = Class(name="r1::Query")
r1_SortClause = Class(name="r1::SortClause")
r1_QueryDefineRef = Class(name="r1::QueryDefineRef")
AliasedQuerySource = Class(name="AliasedQuerySource")
r1_ReturnClause = Class(name="r1::ReturnClause")
r1_Retrieve = Class(name="r1::Retrieve")
r1_Round = Class(name="r1::Round")
r1_SameOrAfter = Class(name="r1::SameOrAfter")
r1_SameOrBefore = Class(name="r1::SameOrBefore")
r1_SameAs = Class(name="r1::SameAs")
r1_SortByItem = Class(name="r1::SortByItem", is_abstract=True)
r1_SingletonFrom = Class(name="r1::SingletonFrom")
r1_Sort = Class(name="r1::Sort")
r1_Split = Class(name="r1::Split")
r1_Start = Class(name="r1::Start")
r1_Substring = Class(name="r1::Substring")
r1_Starts = Class(name="r1::Starts")
r1_StdDev = Class(name="r1::StdDev")
r1_TernaryExpression = Class(name="r1::TernaryExpression")
r1_Time = Class(name="r1::Time")
r1_Subtract = Class(name="r1::Subtract")
r1_Successor = Class(name="r1::Successor")
r1_Sum = Class(name="r1::Sum")
r1_Times = Class(name="r1::Times")
r1_TimeFrom = Class(name="r1::TimeFrom")
r1_TimeOfDay = Class(name="r1::TimeOfDay")
r1_TimezoneFrom = Class(name="r1::TimezoneFrom")
r1_Today = Class(name="r1::Today")
r1_Truncate = Class(name="r1::Truncate")
r1_TruncatedDivide = Class(name="r1::TruncatedDivide")
r1_Tuple = Class(name="r1::Tuple")
r1_TupleElement = Class(name="r1::TupleElement")
r1_TupleTypeSpecifier = Class(name="r1::TupleTypeSpecifier")
r1_TupleElementDefinition = Class(name="r1::TupleElementDefinition")
r1_Upper = Class(name="r1::Upper")
r1_ValueSetDef = Class(name="r1::ValueSetDef")
r1_UnaryExpression = Class(name="r1::UnaryExpression", is_abstract=True)
r1_Union = Class(name="r1::Union")
r1_Variance = Class(name="r1::Variance")
r1_Width = Class(name="r1::Width")
r1_With = Class(name="r1::With")
RelationshipClause = Class(name="RelationshipClause")
r1_Without = Class(name="r1::Without")
r1_Xor = Class(name="r1::Xor")

# r1_Abs class attributes and methods

# UnaryExpression class attributes and methods

# r1_Add class attributes and methods

# BinaryExpression class attributes and methods

# r1_After class attributes and methods
r1_After_precision: Property = Property(name="precision", type=StringType)
r1_After.attributes={r1_After_precision}

# r1_AggregateExpression class attributes and methods
r1_AggregateExpression_path: Property = Property(name="path", type=StringType)
r1_AggregateExpression.attributes={r1_AggregateExpression_path}

# Expression class attributes and methods

# r1_Expression class attributes and methods

# r1_AliasedQuerySource class attributes and methods
r1_AliasedQuerySource_alias: Property = Property(name="alias", type=StringType)
r1_AliasedQuerySource.attributes={r1_AliasedQuerySource_alias}

# Element class attributes and methods

# r1_AliasRef class attributes and methods
r1_AliasRef_name: Property = Property(name="name", type=StringType)
r1_AliasRef.attributes={r1_AliasRef_name}

# r1_AllTrue class attributes and methods

# AggregateExpression class attributes and methods

# r1_AnyTrue class attributes and methods

# r1_As class attributes and methods
r1_As_asType: Property = Property(name="asType", type=StringType)
r1_As_strict: Property = Property(name="strict", type=StringType)
r1_As.attributes={r1_As_strict, r1_As_asType}

# r1_TypeSpecifier class attributes and methods

# r1_And class attributes and methods

# r1_Before class attributes and methods
r1_Before_precision: Property = Property(name="precision", type=StringType)
r1_Before.attributes={r1_Before_precision}

# r1_BinaryExpression class attributes and methods

# r1_ByColumn class attributes and methods
r1_ByColumn_path: Property = Property(name="path", type=StringType)
r1_ByColumn.attributes={r1_ByColumn_path}

# SortByItem class attributes and methods

# r1_Avg class attributes and methods

# r1_ByExpression class attributes and methods

# r1_CalculateAge class attributes and methods
r1_CalculateAge_precision: Property = Property(name="precision", type=StringType)
r1_CalculateAge.attributes={r1_CalculateAge_precision}

# r1_CalculateAgeAt class attributes and methods
r1_CalculateAgeAt_precision: Property = Property(name="precision", type=StringType)
r1_CalculateAgeAt.attributes={r1_CalculateAgeAt_precision}

# r1_ByDirection class attributes and methods

# r1_CaseItem class attributes and methods

# r1_Case class attributes and methods

# r1_Ceiling class attributes and methods

# r1_Coalesce class attributes and methods

# NaryExpression class attributes and methods

# r1_Code class attributes and methods
r1_Code_code: Property = Property(name="code", type=StringType)
r1_Code_display: Property = Property(name="display", type=StringType)
r1_Code.attributes={r1_Code_code, r1_Code_display}

# r1_CodeSystemRef class attributes and methods
r1_CodeSystemRef_libraryName: Property = Property(name="libraryName", type=StringType)
r1_CodeSystemRef_name: Property = Property(name="name", type=StringType)
r1_CodeSystemRef.attributes={r1_CodeSystemRef_name, r1_CodeSystemRef_libraryName}

# r1_CodeSystemDef class attributes and methods
r1_CodeSystemDef_id: Property = Property(name="id", type=StringType)
r1_CodeSystemDef_name: Property = Property(name="name", type=StringType)
r1_CodeSystemDef_version: Property = Property(name="version", type=StringType)
r1_CodeSystemDef_accessLevel: Property = Property(name="accessLevel", type=StringType)
r1_CodeSystemDef.attributes={r1_CodeSystemDef_name, r1_CodeSystemDef_id, r1_CodeSystemDef_version, r1_CodeSystemDef_accessLevel}

# r1_Combine class attributes and methods

# r1_Collapse class attributes and methods

# r1_Contains class attributes and methods
r1_Contains_precision: Property = Property(name="precision", type=StringType)
r1_Contains.attributes={r1_Contains_precision}

# r1_Concatenate class attributes and methods

# r1_Concept class attributes and methods
r1_Concept_display: Property = Property(name="display", type=StringType)
r1_Concept.attributes={r1_Concept_display}

# r1_Count class attributes and methods

# r1_Current class attributes and methods
r1_Current_scope: Property = Property(name="scope", type=StringType)
r1_Current.attributes={r1_Current_scope}

# r1_Convert class attributes and methods
r1_Convert_toType: Property = Property(name="toType", type=StringType)
r1_Convert.attributes={r1_Convert_toType}

# r1_DateFrom class attributes and methods

# r1_DateTime class attributes and methods

# r1_DateTimeComponentFrom class attributes and methods
r1_DateTimeComponentFrom_precision: Property = Property(name="precision", type=StringType)
r1_DateTimeComponentFrom.attributes={r1_DateTimeComponentFrom_precision}

# r1_DifferenceBetween class attributes and methods
r1_DifferenceBetween_precision: Property = Property(name="precision", type=StringType)
r1_DifferenceBetween.attributes={r1_DifferenceBetween_precision}

# r1_DefineClause class attributes and methods
r1_DefineClause_identifier: Property = Property(name="identifier", type=StringType)
r1_DefineClause.attributes={r1_DefineClause_identifier}

# r1_Element class attributes and methods
r1_Element_localId: Property = Property(name="localId", type=StringType)
r1_Element.attributes={r1_Element_localId}

# r1_EObject class attributes and methods

# r1_Distinct class attributes and methods

# r1_Divide class attributes and methods

# r1_DurationBetween class attributes and methods
r1_DurationBetween_precision: Property = Property(name="precision", type=StringType)
r1_DurationBetween.attributes={r1_DurationBetween_precision}

# r1_Equal class attributes and methods

# r1_Except class attributes and methods

# r1_Exists class attributes and methods

# r1_End class attributes and methods

# r1_Ends class attributes and methods
r1_Ends_precision: Property = Property(name="precision", type=StringType)
r1_Ends.attributes={r1_Ends_precision}

# r1_Expand class attributes and methods

# r1_ExpressionDef class attributes and methods
r1_ExpressionDef_accessLevel: Property = Property(name="accessLevel", type=StringType)
r1_ExpressionDef_context: Property = Property(name="context", type=StringType)
r1_ExpressionDef_name: Property = Property(name="name", type=StringType)
r1_ExpressionDef.attributes={r1_ExpressionDef_name, r1_ExpressionDef_accessLevel, r1_ExpressionDef_context}

# r1_ExpressionRef class attributes and methods
r1_ExpressionRef_libraryName: Property = Property(name="libraryName", type=StringType)
r1_ExpressionRef_name: Property = Property(name="name", type=StringType)
r1_ExpressionRef.attributes={r1_ExpressionRef_name, r1_ExpressionRef_libraryName}

# r1_Filter class attributes and methods
r1_Filter_scope: Property = Property(name="scope", type=StringType)
r1_Filter.attributes={r1_Filter_scope}

# r1_Floor class attributes and methods

# r1_ForEach class attributes and methods
r1_ForEach_scope: Property = Property(name="scope", type=StringType)
r1_ForEach.attributes={r1_ForEach_scope}

# r1_First class attributes and methods
r1_First_orderBy: Property = Property(name="orderBy", type=StringType)
r1_First.attributes={r1_First_orderBy}

# r1_OperandDef class attributes and methods
r1_OperandDef_name: Property = Property(name="name", type=StringType)
r1_OperandDef_operandType: Property = Property(name="operandType", type=StringType)
r1_OperandDef.attributes={r1_OperandDef_operandType, r1_OperandDef_name}

# r1_FunctionRef class attributes and methods

# ExpressionRef class attributes and methods

# r1_FunctionDef class attributes and methods

# ExpressionDef class attributes and methods

# r1_If class attributes and methods

# r1_Greater class attributes and methods

# r1_GreaterOrEqual class attributes and methods

# r1_IdentifierRef class attributes and methods
r1_IdentifierRef_libraryName: Property = Property(name="libraryName", type=StringType)
r1_IdentifierRef_name: Property = Property(name="name", type=StringType)
r1_IdentifierRef.attributes={r1_IdentifierRef_name, r1_IdentifierRef_libraryName}

# r1_In class attributes and methods
r1_In_precision: Property = Property(name="precision", type=StringType)
r1_In.attributes={r1_In_precision}

# r1_IncludedIn class attributes and methods
r1_IncludedIn_precision: Property = Property(name="precision", type=StringType)
r1_IncludedIn.attributes={r1_IncludedIn_precision}

# r1_Includes class attributes and methods
r1_Includes_precision: Property = Property(name="precision", type=StringType)
r1_Includes.attributes={r1_Includes_precision}

# r1_IndexOf class attributes and methods

# r1_Instance class attributes and methods
r1_Instance_classType: Property = Property(name="classType", type=StringType)
r1_Instance.attributes={r1_Instance_classType}

# r1_InstanceElement class attributes and methods
r1_InstanceElement_name: Property = Property(name="name", type=StringType)
r1_InstanceElement.attributes={r1_InstanceElement_name}

# r1_InCodeSystem class attributes and methods

# r1_Indexer class attributes and methods

# r1_Intersect class attributes and methods

# r1_Interval class attributes and methods
r1_Interval_lowClosed: Property = Property(name="lowClosed", type=StringType)
r1_Interval_highClosed: Property = Property(name="highClosed", type=StringType)
r1_Interval.attributes={r1_Interval_lowClosed, r1_Interval_highClosed}

# r1_IntervalTypeSpecifier class attributes and methods

# TypeSpecifier class attributes and methods

# r1_InValueSet class attributes and methods

# r1_ValueSetRef class attributes and methods
r1_ValueSetRef_libraryName: Property = Property(name="libraryName", type=StringType)
r1_ValueSetRef_name: Property = Property(name="name", type=StringType)
r1_ValueSetRef.attributes={r1_ValueSetRef_name, r1_ValueSetRef_libraryName}

# r1_IsNull class attributes and methods

# r1_IsTrue class attributes and methods

# r1_Last class attributes and methods
r1_Last_orderBy: Property = Property(name="orderBy", type=StringType)
r1_Last.attributes={r1_Last_orderBy}

# r1_Is class attributes and methods
r1_Is_isType: Property = Property(name="isType", type=StringType)
r1_Is.attributes={r1_Is_isType}

# r1_IsFalse class attributes and methods

# r1_ListTypeSpecifier class attributes and methods

# r1_Length class attributes and methods

# r1_Literal class attributes and methods
r1_Literal_value: Property = Property(name="value", type=StringType)
r1_Literal_valueType: Property = Property(name="valueType", type=StringType)
r1_Literal.attributes={r1_Literal_valueType, r1_Literal_value}

# r1_Less class attributes and methods

# r1_LessOrEqual class attributes and methods

# r1_List class attributes and methods

# r1_Log class attributes and methods

# r1_Lower class attributes and methods

# r1_Matches class attributes and methods

# r1_Max class attributes and methods

# r1_MaxValue class attributes and methods
r1_MaxValue_valueType: Property = Property(name="valueType", type=StringType)
r1_MaxValue.attributes={r1_MaxValue_valueType}

# r1_Ln class attributes and methods

# r1_Median class attributes and methods

# r1_Meets class attributes and methods
r1_Meets_precision: Property = Property(name="precision", type=StringType)
r1_Meets.attributes={r1_Meets_precision}

# r1_MeetsAfter class attributes and methods
r1_MeetsAfter_precision: Property = Property(name="precision", type=StringType)
r1_MeetsAfter.attributes={r1_MeetsAfter_precision}

# r1_MeetsBefore class attributes and methods
r1_MeetsBefore_precision: Property = Property(name="precision", type=StringType)
r1_MeetsBefore.attributes={r1_MeetsBefore_precision}

# r1_MinValue class attributes and methods
r1_MinValue_valueType: Property = Property(name="valueType", type=StringType)
r1_MinValue.attributes={r1_MinValue_valueType}

# r1_Mode class attributes and methods

# r1_Modulo class attributes and methods

# r1_Multiply class attributes and methods

# r1_NamedTypeSpecifier class attributes and methods
r1_NamedTypeSpecifier_name: Property = Property(name="name", type=StringType)
r1_NamedTypeSpecifier.attributes={r1_NamedTypeSpecifier_name}

# r1_Min class attributes and methods

# r1_Now class attributes and methods

# r1_NaryExpression class attributes and methods

# r1_Null class attributes and methods
r1_Null_valueType: Property = Property(name="valueType", type=StringType)
r1_Null.attributes={r1_Null_valueType}

# r1_Negate class attributes and methods

# r1_Not class attributes and methods

# r1_NotEqual class attributes and methods

# r1_OperandRef class attributes and methods
r1_OperandRef_name: Property = Property(name="name", type=StringType)
r1_OperandRef.attributes={r1_OperandRef_name}

# r1_Or class attributes and methods

# r1_Overlaps class attributes and methods
r1_Overlaps_precision: Property = Property(name="precision", type=StringType)
r1_Overlaps.attributes={r1_Overlaps_precision}

# r1_OverlapsBefore class attributes and methods
r1_OverlapsBefore_precision: Property = Property(name="precision", type=StringType)
r1_OverlapsBefore.attributes={r1_OverlapsBefore_precision}

# r1_ParameterDef class attributes and methods
r1_ParameterDef_parameterType: Property = Property(name="parameterType", type=StringType)
r1_ParameterDef_accessLevel: Property = Property(name="accessLevel", type=StringType)
r1_ParameterDef_name: Property = Property(name="name", type=StringType)
r1_ParameterDef.attributes={r1_ParameterDef_name, r1_ParameterDef_parameterType, r1_ParameterDef_accessLevel}

# r1_OverlapsAfter class attributes and methods
r1_OverlapsAfter_precision: Property = Property(name="precision", type=StringType)
r1_OverlapsAfter.attributes={r1_OverlapsAfter_precision}

# r1_ParameterRef class attributes and methods
r1_ParameterRef_libraryName: Property = Property(name="libraryName", type=StringType)
r1_ParameterRef_name: Property = Property(name="name", type=StringType)
r1_ParameterRef.attributes={r1_ParameterRef_name, r1_ParameterRef_libraryName}

# r1_PopulationStdDev class attributes and methods

# r1_Power class attributes and methods

# r1_PopulationVariance class attributes and methods

# r1_PositionOf class attributes and methods

# r1_ProperIn class attributes and methods
r1_ProperIn_precision: Property = Property(name="precision", type=StringType)
r1_ProperIn.attributes={r1_ProperIn_precision}

# r1_ProperIncludedIn class attributes and methods
r1_ProperIncludedIn_precision: Property = Property(name="precision", type=StringType)
r1_ProperIncludedIn.attributes={r1_ProperIncludedIn_precision}

# r1_ProperIncludes class attributes and methods
r1_ProperIncludes_precision: Property = Property(name="precision", type=StringType)
r1_ProperIncludes.attributes={r1_ProperIncludes_precision}

# r1_Predecessor class attributes and methods

# r1_ProperContains class attributes and methods
r1_ProperContains_precision: Property = Property(name="precision", type=StringType)
r1_ProperContains.attributes={r1_ProperContains_precision}

# r1_Quantity class attributes and methods
r1_Quantity_unit: Property = Property(name="unit", type=StringType)
r1_Quantity_value: Property = Property(name="value", type=StringType)
r1_Quantity.attributes={r1_Quantity_value, r1_Quantity_unit}

# r1_Property class attributes and methods
r1_Property_path: Property = Property(name="path", type=StringType)
r1_Property_scope: Property = Property(name="scope", type=StringType)
r1_Property.attributes={r1_Property_path, r1_Property_scope}

# r1_RelationshipClause class attributes and methods

# r1_Query class attributes and methods

# r1_SortClause class attributes and methods

# r1_QueryDefineRef class attributes and methods
r1_QueryDefineRef_name: Property = Property(name="name", type=StringType)
r1_QueryDefineRef.attributes={r1_QueryDefineRef_name}

# AliasedQuerySource class attributes and methods

# r1_ReturnClause class attributes and methods
r1_ReturnClause_distinct: Property = Property(name="distinct", type=StringType)
r1_ReturnClause.attributes={r1_ReturnClause_distinct}

# r1_Retrieve class attributes and methods
r1_Retrieve_dataType: Property = Property(name="dataType", type=StringType)
r1_Retrieve_dateHighProperty: Property = Property(name="dateHighProperty", type=StringType)
r1_Retrieve_dateLowProperty: Property = Property(name="dateLowProperty", type=StringType)
r1_Retrieve_dateProperty: Property = Property(name="dateProperty", type=StringType)
r1_Retrieve_idProperty: Property = Property(name="idProperty", type=StringType)
r1_Retrieve_codeProperty: Property = Property(name="codeProperty", type=StringType)
r1_Retrieve_templateId: Property = Property(name="templateId", type=StringType)
r1_Retrieve_scope: Property = Property(name="scope", type=StringType)
r1_Retrieve.attributes={r1_Retrieve_codeProperty, r1_Retrieve_templateId, r1_Retrieve_dateProperty, r1_Retrieve_dataType, r1_Retrieve_dateLowProperty, r1_Retrieve_scope, r1_Retrieve_idProperty, r1_Retrieve_dateHighProperty}

# r1_Round class attributes and methods

# r1_SameOrAfter class attributes and methods
r1_SameOrAfter_precision: Property = Property(name="precision", type=StringType)
r1_SameOrAfter.attributes={r1_SameOrAfter_precision}

# r1_SameOrBefore class attributes and methods
r1_SameOrBefore_precision: Property = Property(name="precision", type=StringType)
r1_SameOrBefore.attributes={r1_SameOrBefore_precision}

# r1_SameAs class attributes and methods
r1_SameAs_precision: Property = Property(name="precision", type=StringType)
r1_SameAs.attributes={r1_SameAs_precision}

# r1_SortByItem class attributes and methods
r1_SortByItem_direction: Property = Property(name="direction", type=StringType)
r1_SortByItem.attributes={r1_SortByItem_direction}

# r1_SingletonFrom class attributes and methods

# r1_Sort class attributes and methods

# r1_Split class attributes and methods

# r1_Start class attributes and methods

# r1_Substring class attributes and methods

# r1_Starts class attributes and methods
r1_Starts_precision: Property = Property(name="precision", type=StringType)
r1_Starts.attributes={r1_Starts_precision}

# r1_StdDev class attributes and methods

# r1_TernaryExpression class attributes and methods

# r1_Time class attributes and methods

# r1_Subtract class attributes and methods

# r1_Successor class attributes and methods

# r1_Sum class attributes and methods

# r1_Times class attributes and methods

# r1_TimeFrom class attributes and methods

# r1_TimeOfDay class attributes and methods

# r1_TimezoneFrom class attributes and methods

# r1_Today class attributes and methods

# r1_Truncate class attributes and methods

# r1_TruncatedDivide class attributes and methods

# r1_Tuple class attributes and methods

# r1_TupleElement class attributes and methods
r1_TupleElement_name: Property = Property(name="name", type=StringType)
r1_TupleElement.attributes={r1_TupleElement_name}

# r1_TupleTypeSpecifier class attributes and methods

# r1_TupleElementDefinition class attributes and methods
r1_TupleElementDefinition_name: Property = Property(name="name", type=StringType)
r1_TupleElementDefinition.attributes={r1_TupleElementDefinition_name}

# r1_Upper class attributes and methods

# r1_ValueSetDef class attributes and methods
r1_ValueSetDef_accessLevel: Property = Property(name="accessLevel", type=StringType)
r1_ValueSetDef_id: Property = Property(name="id", type=StringType)
r1_ValueSetDef_name: Property = Property(name="name", type=StringType)
r1_ValueSetDef_version: Property = Property(name="version", type=StringType)
r1_ValueSetDef.attributes={r1_ValueSetDef_version, r1_ValueSetDef_id, r1_ValueSetDef_name, r1_ValueSetDef_accessLevel}

# r1_UnaryExpression class attributes and methods

# r1_Union class attributes and methods

# r1_Variance class attributes and methods

# r1_Width class attributes and methods

# r1_With class attributes and methods

# RelationshipClause class attributes and methods

# r1_Without class attributes and methods

# r1_Xor class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="r1_Expression", type=r1_AggregateExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_AggregateExpression", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="r1_Expression2", type=r1_AliasedQuerySource, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_AliasedQuerySource", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
asTypeSpecifier3: BinaryAssociation = BinaryAssociation(
    name="asTypeSpecifier3",
    ends={
        Property(name="r1_TypeSpecifier", type=r1_As, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_As", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand4: BinaryAssociation = BinaryAssociation(
    name="operand4",
    ends={
        Property(name="r1_Expression5", type=r1_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_BinaryExpression", type=r1_Expression, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
expression6: BinaryAssociation = BinaryAssociation(
    name="expression6",
    ends={
        Property(name="r1_Expression7", type=r1_ByExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ByExpression", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comparand8: BinaryAssociation = BinaryAssociation(
    name="comparand8",
    ends={
        Property(name="r1_Expression9", type=r1_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Case", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
caseItem10: BinaryAssociation = BinaryAssociation(
    name="caseItem10",
    ends={
        Property(name="r1_CaseItem", type=r1_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Case11", type=r1_CaseItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
else12: BinaryAssociation = BinaryAssociation(
    name="else12",
    ends={
        Property(name="r1_Expression14", type=r1_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Case13", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
when15: BinaryAssociation = BinaryAssociation(
    name="when15",
    ends={
        Property(name="r1_Expression17", type=r1_CaseItem, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_CaseItem16", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then18: BinaryAssociation = BinaryAssociation(
    name="then18",
    ends={
        Property(name="r1_Expression20", type=r1_CaseItem, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_CaseItem19", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
system21: BinaryAssociation = BinaryAssociation(
    name="system21",
    ends={
        Property(name="r1_CodeSystemRef", type=r1_Code, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Code", type=r1_CodeSystemRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="r1_Expression23", type=r1_Combine, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Combine", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
code27: BinaryAssociation = BinaryAssociation(
    name="code27",
    ends={
        Property(name="r1_Code28", type=r1_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Concept", type=r1_Code, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
separator24: BinaryAssociation = BinaryAssociation(
    name="separator24",
    ends={
        Property(name="r1_Expression26", type=r1_Combine, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Combine25", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toTypeSpecifier29: BinaryAssociation = BinaryAssociation(
    name="toTypeSpecifier29",
    ends={
        Property(name="r1_TypeSpecifier30", type=r1_Convert, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Convert", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
month33: BinaryAssociation = BinaryAssociation(
    name="month33",
    ends={
        Property(name="r1_Expression35", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime34", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
day36: BinaryAssociation = BinaryAssociation(
    name="day36",
    ends={
        Property(name="r1_Expression38", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime37", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hour39: BinaryAssociation = BinaryAssociation(
    name="hour39",
    ends={
        Property(name="r1_Expression41", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime40", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
year31: BinaryAssociation = BinaryAssociation(
    name="year31",
    ends={
        Property(name="r1_Expression32", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
millisecond48: BinaryAssociation = BinaryAssociation(
    name="millisecond48",
    ends={
        Property(name="r1_Expression50", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime49", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timezoneOffset51: BinaryAssociation = BinaryAssociation(
    name="timezoneOffset51",
    ends={
        Property(name="r1_Expression53", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime52", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minute42: BinaryAssociation = BinaryAssociation(
    name="minute42",
    ends={
        Property(name="r1_Expression44", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime43", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
second45: BinaryAssociation = BinaryAssociation(
    name="second45",
    ends={
        Property(name="r1_Expression47", type=r1_DateTime, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DateTime46", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression54: BinaryAssociation = BinaryAssociation(
    name="expression54",
    ends={
        Property(name="r1_Expression55", type=r1_DefineClause, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_DefineClause", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotation56: BinaryAssociation = BinaryAssociation(
    name="annotation56",
    ends={
        Property(name="r1_EObject", type=r1_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Element", type=r1_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression57: BinaryAssociation = BinaryAssociation(
    name="expression57",
    ends={
        Property(name="r1_Expression58", type=r1_ExpressionDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ExpressionDef", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source59: BinaryAssociation = BinaryAssociation(
    name="source59",
    ends={
        Property(name="r1_Expression60", type=r1_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Filter", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition61: BinaryAssociation = BinaryAssociation(
    name="condition61",
    ends={
        Property(name="r1_Expression63", type=r1_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Filter62", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source66: BinaryAssociation = BinaryAssociation(
    name="source66",
    ends={
        Property(name="r1_Expression67", type=r1_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ForEach", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source64: BinaryAssociation = BinaryAssociation(
    name="source64",
    ends={
        Property(name="r1_Expression65", type=r1_First, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_First", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand71: BinaryAssociation = BinaryAssociation(
    name="operand71",
    ends={
        Property(name="r1_OperandDef", type=r1_FunctionDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_FunctionDef", type=r1_OperandDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand72: BinaryAssociation = BinaryAssociation(
    name="operand72",
    ends={
        Property(name="r1_Expression73", type=r1_FunctionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_FunctionRef", type=r1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element68: BinaryAssociation = BinaryAssociation(
    name="element68",
    ends={
        Property(name="r1_Expression70", type=r1_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ForEach69", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition74: BinaryAssociation = BinaryAssociation(
    name="condition74",
    ends={
        Property(name="r1_Expression75", type=r1_If, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_If", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then76: BinaryAssociation = BinaryAssociation(
    name="then76",
    ends={
        Property(name="r1_Expression78", type=r1_If, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_If77", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else79: BinaryAssociation = BinaryAssociation(
    name="else79",
    ends={
        Property(name="r1_Expression81", type=r1_If, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_If80", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source87: BinaryAssociation = BinaryAssociation(
    name="source87",
    ends={
        Property(name="r1_Expression88", type=r1_IndexOf, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_IndexOf", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element89: BinaryAssociation = BinaryAssociation(
    name="element89",
    ends={
        Property(name="r1_Expression91", type=r1_IndexOf, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_IndexOf90", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element92: BinaryAssociation = BinaryAssociation(
    name="element92",
    ends={
        Property(name="r1_InstanceElement", type=r1_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Instance", type=r1_InstanceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
code82: BinaryAssociation = BinaryAssociation(
    name="code82",
    ends={
        Property(name="r1_Expression83", type=r1_InCodeSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_InCodeSystem", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
codesystem84: BinaryAssociation = BinaryAssociation(
    name="codesystem84",
    ends={
        Property(name="r1_CodeSystemRef86", type=r1_InCodeSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_InCodeSystem85", type=r1_CodeSystemRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value93: BinaryAssociation = BinaryAssociation(
    name="value93",
    ends={
        Property(name="r1_Expression95", type=r1_InstanceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_InstanceElement94", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
low96: BinaryAssociation = BinaryAssociation(
    name="low96",
    ends={
        Property(name="r1_Expression97", type=r1_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Interval", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pointType107: BinaryAssociation = BinaryAssociation(
    name="pointType107",
    ends={
        Property(name="r1_TypeSpecifier108", type=r1_IntervalTypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_IntervalTypeSpecifier", type=r1_TypeSpecifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
code109: BinaryAssociation = BinaryAssociation(
    name="code109",
    ends={
        Property(name="r1_Expression110", type=r1_InValueSet, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_InValueSet", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lowClosedExpression98: BinaryAssociation = BinaryAssociation(
    name="lowClosedExpression98",
    ends={
        Property(name="r1_Expression100", type=r1_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Interval99", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
high101: BinaryAssociation = BinaryAssociation(
    name="high101",
    ends={
        Property(name="r1_Expression103", type=r1_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Interval102", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
highClosedExpression104: BinaryAssociation = BinaryAssociation(
    name="highClosedExpression104",
    ends={
        Property(name="r1_Expression106", type=r1_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Interval105", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source115: BinaryAssociation = BinaryAssociation(
    name="source115",
    ends={
        Property(name="r1_Expression116", type=r1_Last, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Last", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valueset111: BinaryAssociation = BinaryAssociation(
    name="valueset111",
    ends={
        Property(name="r1_ValueSetRef", type=r1_InValueSet, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_InValueSet112", type=r1_ValueSetRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
isTypeSpecifier113: BinaryAssociation = BinaryAssociation(
    name="isTypeSpecifier113",
    ends={
        Property(name="r1_TypeSpecifier114", type=r1_Is, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Is", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element119: BinaryAssociation = BinaryAssociation(
    name="element119",
    ends={
        Property(name="r1_Expression121", type=r1_List, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_List120", type=r1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType122: BinaryAssociation = BinaryAssociation(
    name="elementType122",
    ends={
        Property(name="r1_TypeSpecifier123", type=r1_ListTypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ListTypeSpecifier", type=r1_TypeSpecifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeSpecifier117: BinaryAssociation = BinaryAssociation(
    name="typeSpecifier117",
    ends={
        Property(name="r1_TypeSpecifier118", type=r1_List, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_List", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand124: BinaryAssociation = BinaryAssociation(
    name="operand124",
    ends={
        Property(name="r1_Expression125", type=r1_NaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_NaryExpression", type=r1_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operandTypeSpecifier126: BinaryAssociation = BinaryAssociation(
    name="operandTypeSpecifier126",
    ends={
        Property(name="r1_TypeSpecifier128", type=r1_OperandDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_OperandDef127", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
default129: BinaryAssociation = BinaryAssociation(
    name="default129",
    ends={
        Property(name="r1_Expression130", type=r1_ParameterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ParameterDef", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterTypeSpecifier131: BinaryAssociation = BinaryAssociation(
    name="parameterTypeSpecifier131",
    ends={
        Property(name="r1_TypeSpecifier133", type=r1_ParameterDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ParameterDef132", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern134: BinaryAssociation = BinaryAssociation(
    name="pattern134",
    ends={
        Property(name="r1_Expression135", type=r1_PositionOf, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_PositionOf", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
string136: BinaryAssociation = BinaryAssociation(
    name="string136",
    ends={
        Property(name="r1_Expression138", type=r1_PositionOf, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_PositionOf137", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source139: BinaryAssociation = BinaryAssociation(
    name="source139",
    ends={
        Property(name="r1_Expression140", type=r1_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Property", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source141: BinaryAssociation = BinaryAssociation(
    name="source141",
    ends={
        Property(name="r1_AliasedQuerySource142", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query", type=r1_AliasedQuerySource, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
define143: BinaryAssociation = BinaryAssociation(
    name="define143",
    ends={
        Property(name="r1_DefineClause145", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query144", type=r1_DefineClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship146: BinaryAssociation = BinaryAssociation(
    name="relationship146",
    ends={
        Property(name="r1_RelationshipClause", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query147", type=r1_RelationshipClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where148: BinaryAssociation = BinaryAssociation(
    name="where148",
    ends={
        Property(name="r1_Expression150", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query149", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sort153: BinaryAssociation = BinaryAssociation(
    name="sort153",
    ends={
        Property(name="r1_SortClause", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query154", type=r1_SortClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return151: BinaryAssociation = BinaryAssociation(
    name="return151",
    ends={
        Property(name="r1_ReturnClause", type=r1_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Query152", type=r1_ReturnClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codes158: BinaryAssociation = BinaryAssociation(
    name="codes158",
    ends={
        Property(name="r1_Expression159", type=r1_Retrieve, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Retrieve", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dateRange160: BinaryAssociation = BinaryAssociation(
    name="dateRange160",
    ends={
        Property(name="r1_Expression162", type=r1_Retrieve, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Retrieve161", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
suchThat155: BinaryAssociation = BinaryAssociation(
    name="suchThat155",
    ends={
        Property(name="r1_Expression157", type=r1_RelationshipClause, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_RelationshipClause156", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression163: BinaryAssociation = BinaryAssociation(
    name="expression163",
    ends={
        Property(name="r1_Expression165", type=r1_ReturnClause, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ReturnClause164", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand166: BinaryAssociation = BinaryAssociation(
    name="operand166",
    ends={
        Property(name="r1_Expression167", type=r1_Round, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Round", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
precision168: BinaryAssociation = BinaryAssociation(
    name="precision168",
    ends={
        Property(name="r1_Expression170", type=r1_Round, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Round169", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
by173: BinaryAssociation = BinaryAssociation(
    name="by173",
    ends={
        Property(name="r1_SortByItem", type=r1_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Sort174", type=r1_SortByItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source171: BinaryAssociation = BinaryAssociation(
    name="source171",
    ends={
        Property(name="r1_Expression172", type=r1_Sort, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Sort", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stringToSplit178: BinaryAssociation = BinaryAssociation(
    name="stringToSplit178",
    ends={
        Property(name="r1_Expression179", type=r1_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Split", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
separator180: BinaryAssociation = BinaryAssociation(
    name="separator180",
    ends={
        Property(name="r1_Expression182", type=r1_Split, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Split181", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
by175: BinaryAssociation = BinaryAssociation(
    name="by175",
    ends={
        Property(name="r1_SortByItem177", type=r1_SortClause, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_SortClause176", type=r1_SortByItem, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
stringToSub183: BinaryAssociation = BinaryAssociation(
    name="stringToSub183",
    ends={
        Property(name="r1_EObject184", type=r1_Substring, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Substring", type=r1_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
startIndex185: BinaryAssociation = BinaryAssociation(
    name="startIndex185",
    ends={
        Property(name="r1_EObject187", type=r1_Substring, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Substring186", type=r1_EObject, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
length188: BinaryAssociation = BinaryAssociation(
    name="length188",
    ends={
        Property(name="r1_EObject190", type=r1_Substring, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Substring189", type=r1_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operand191: BinaryAssociation = BinaryAssociation(
    name="operand191",
    ends={
        Property(name="r1_Expression192", type=r1_TernaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_TernaryExpression", type=r1_Expression, multiplicity=Multiplicity(3, 3), is_composite=True)
    }
)
hour193: BinaryAssociation = BinaryAssociation(
    name="hour193",
    ends={
        Property(name="r1_Expression194", type=r1_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Time", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
second198: BinaryAssociation = BinaryAssociation(
    name="second198",
    ends={
        Property(name="r1_Expression200", type=r1_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Time199", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
millisecond201: BinaryAssociation = BinaryAssociation(
    name="millisecond201",
    ends={
        Property(name="r1_Expression203", type=r1_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Time202", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
timezoneOffset204: BinaryAssociation = BinaryAssociation(
    name="timezoneOffset204",
    ends={
        Property(name="r1_Expression206", type=r1_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Time205", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
minute195: BinaryAssociation = BinaryAssociation(
    name="minute195",
    ends={
        Property(name="r1_Expression197", type=r1_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Time196", type=r1_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element207: BinaryAssociation = BinaryAssociation(
    name="element207",
    ends={
        Property(name="r1_TupleElement", type=r1_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_Tuple", type=r1_TupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element213: BinaryAssociation = BinaryAssociation(
    name="element213",
    ends={
        Property(name="r1_TupleElementDefinition214", type=r1_TupleTypeSpecifier, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_TupleTypeSpecifier", type=r1_TupleElementDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value208: BinaryAssociation = BinaryAssociation(
    name="value208",
    ends={
        Property(name="r1_Expression210", type=r1_TupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_TupleElement209", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type211: BinaryAssociation = BinaryAssociation(
    name="type211",
    ends={
        Property(name="r1_TypeSpecifier212", type=r1_TupleElementDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_TupleElementDefinition", type=r1_TypeSpecifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
codeSystem217: BinaryAssociation = BinaryAssociation(
    name="codeSystem217",
    ends={
        Property(name="r1_CodeSystemRef218", type=r1_ValueSetDef, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_ValueSetDef", type=r1_CodeSystemRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand215: BinaryAssociation = BinaryAssociation(
    name="operand215",
    ends={
        Property(name="r1_Expression216", type=r1_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="r1_UnaryExpression", type=r1_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_r1_Abs_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Abs)
gen_r1_Add_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Add)
gen_r1_After_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_After)
gen_r1_AggregateExpression_Expression = Generalization(general=Expression, specific=r1_AggregateExpression)
gen_r1_AliasedQuerySource_Element = Generalization(general=Element, specific=r1_AliasedQuerySource)
gen_r1_AliasRef_Expression = Generalization(general=Expression, specific=r1_AliasRef)
gen_r1_AllTrue_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_AllTrue)
gen_r1_AnyTrue_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_AnyTrue)
gen_r1_As_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_As)
gen_r1_And_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_And)
gen_r1_Before_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Before)
gen_r1_BinaryExpression_Expression = Generalization(general=Expression, specific=r1_BinaryExpression)
gen_r1_ByColumn_SortByItem = Generalization(general=SortByItem, specific=r1_ByColumn)
gen_r1_Avg_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Avg)
gen_r1_ByExpression_SortByItem = Generalization(general=SortByItem, specific=r1_ByExpression)
gen_r1_CalculateAge_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_CalculateAge)
gen_r1_CalculateAgeAt_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_CalculateAgeAt)
gen_r1_ByDirection_SortByItem = Generalization(general=SortByItem, specific=r1_ByDirection)
gen_r1_CaseItem_Element = Generalization(general=Element, specific=r1_CaseItem)
gen_r1_Case_Expression = Generalization(general=Expression, specific=r1_Case)
gen_r1_Ceiling_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Ceiling)
gen_r1_Coalesce_NaryExpression = Generalization(general=NaryExpression, specific=r1_Coalesce)
gen_r1_Code_Expression = Generalization(general=Expression, specific=r1_Code)
gen_r1_CodeSystemDef_Element = Generalization(general=Element, specific=r1_CodeSystemDef)
gen_r1_Combine_Expression = Generalization(general=Expression, specific=r1_Combine)
gen_r1_CodeSystemRef_Expression = Generalization(general=Expression, specific=r1_CodeSystemRef)
gen_r1_Collapse_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Collapse)
gen_r1_Contains_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Contains)
gen_r1_Concatenate_NaryExpression = Generalization(general=NaryExpression, specific=r1_Concatenate)
gen_r1_Concept_Expression = Generalization(general=Expression, specific=r1_Concept)
gen_r1_Count_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Count)
gen_r1_Current_Expression = Generalization(general=Expression, specific=r1_Current)
gen_r1_Convert_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Convert)
gen_r1_DateFrom_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_DateFrom)
gen_r1_DateTime_Expression = Generalization(general=Expression, specific=r1_DateTime)
gen_r1_DateTimeComponentFrom_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_DateTimeComponentFrom)
gen_r1_DifferenceBetween_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_DifferenceBetween)
gen_r1_DefineClause_Element = Generalization(general=Element, specific=r1_DefineClause)
gen_r1_Distinct_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Distinct)
gen_r1_Divide_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Divide)
gen_r1_DurationBetween_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_DurationBetween)
gen_r1_Equal_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Equal)
gen_r1_Except_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Except)
gen_r1_Exists_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Exists)
gen_r1_End_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_End)
gen_r1_Ends_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Ends)
gen_r1_Expand_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Expand)
gen_r1_Expression_Element = Generalization(general=Element, specific=r1_Expression)
gen_r1_ExpressionDef_Element = Generalization(general=Element, specific=r1_ExpressionDef)
gen_r1_ExpressionRef_Expression = Generalization(general=Expression, specific=r1_ExpressionRef)
gen_r1_Filter_Expression = Generalization(general=Expression, specific=r1_Filter)
gen_r1_Floor_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Floor)
gen_r1_ForEach_Expression = Generalization(general=Expression, specific=r1_ForEach)
gen_r1_First_Expression = Generalization(general=Expression, specific=r1_First)
gen_r1_FunctionRef_ExpressionRef = Generalization(general=ExpressionRef, specific=r1_FunctionRef)
gen_r1_FunctionDef_ExpressionDef = Generalization(general=ExpressionDef, specific=r1_FunctionDef)
gen_r1_If_Expression = Generalization(general=Expression, specific=r1_If)
gen_r1_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Greater)
gen_r1_GreaterOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_GreaterOrEqual)
gen_r1_IdentifierRef_Expression = Generalization(general=Expression, specific=r1_IdentifierRef)
gen_r1_In_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_In)
gen_r1_IncludedIn_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_IncludedIn)
gen_r1_Includes_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Includes)
gen_r1_IndexOf_Expression = Generalization(general=Expression, specific=r1_IndexOf)
gen_r1_Instance_Expression = Generalization(general=Expression, specific=r1_Instance)
gen_r1_InCodeSystem_Expression = Generalization(general=Expression, specific=r1_InCodeSystem)
gen_r1_Indexer_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Indexer)
gen_r1_Intersect_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Intersect)
gen_r1_Interval_Expression = Generalization(general=Expression, specific=r1_Interval)
gen_r1_IntervalTypeSpecifier_TypeSpecifier = Generalization(general=TypeSpecifier, specific=r1_IntervalTypeSpecifier)
gen_r1_InValueSet_Expression = Generalization(general=Expression, specific=r1_InValueSet)
gen_r1_IsNull_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_IsNull)
gen_r1_IsTrue_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_IsTrue)
gen_r1_Last_Expression = Generalization(general=Expression, specific=r1_Last)
gen_r1_Is_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Is)
gen_r1_IsFalse_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_IsFalse)
gen_r1_ListTypeSpecifier_TypeSpecifier = Generalization(general=TypeSpecifier, specific=r1_ListTypeSpecifier)
gen_r1_Length_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Length)
gen_r1_Literal_Expression = Generalization(general=Expression, specific=r1_Literal)
gen_r1_Less_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Less)
gen_r1_LessOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_LessOrEqual)
gen_r1_List_Expression = Generalization(general=Expression, specific=r1_List)
gen_r1_Log_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Log)
gen_r1_Lower_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Lower)
gen_r1_Matches_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Matches)
gen_r1_Max_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Max)
gen_r1_MaxValue_Expression = Generalization(general=Expression, specific=r1_MaxValue)
gen_r1_Ln_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Ln)
gen_r1_Median_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Median)
gen_r1_Meets_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Meets)
gen_r1_MeetsAfter_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_MeetsAfter)
gen_r1_MeetsBefore_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_MeetsBefore)
gen_r1_MinValue_Expression = Generalization(general=Expression, specific=r1_MinValue)
gen_r1_Mode_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Mode)
gen_r1_Modulo_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Modulo)
gen_r1_Multiply_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Multiply)
gen_r1_NamedTypeSpecifier_TypeSpecifier = Generalization(general=TypeSpecifier, specific=r1_NamedTypeSpecifier)
gen_r1_Min_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Min)
gen_r1_Now_Expression = Generalization(general=Expression, specific=r1_Now)
gen_r1_NaryExpression_Expression = Generalization(general=Expression, specific=r1_NaryExpression)
gen_r1_Null_Expression = Generalization(general=Expression, specific=r1_Null)
gen_r1_Negate_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Negate)
gen_r1_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Not)
gen_r1_NotEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_NotEqual)
gen_r1_OperandRef_Expression = Generalization(general=Expression, specific=r1_OperandRef)
gen_r1_Or_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Or)
gen_r1_Overlaps_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Overlaps)
gen_r1_OperandDef_Element = Generalization(general=Element, specific=r1_OperandDef)
gen_r1_OverlapsBefore_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_OverlapsBefore)
gen_r1_ParameterDef_Element = Generalization(general=Element, specific=r1_ParameterDef)
gen_r1_OverlapsAfter_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_OverlapsAfter)
gen_r1_ParameterRef_Expression = Generalization(general=Expression, specific=r1_ParameterRef)
gen_r1_PopulationStdDev_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_PopulationStdDev)
gen_r1_Power_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Power)
gen_r1_PopulationVariance_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_PopulationVariance)
gen_r1_PositionOf_Expression = Generalization(general=Expression, specific=r1_PositionOf)
gen_r1_ProperIn_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_ProperIn)
gen_r1_ProperIncludedIn_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_ProperIncludedIn)
gen_r1_ProperIncludes_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_ProperIncludes)
gen_r1_Predecessor_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Predecessor)
gen_r1_ProperContains_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_ProperContains)
gen_r1_Quantity_Expression = Generalization(general=Expression, specific=r1_Quantity)
gen_r1_Property_Expression = Generalization(general=Expression, specific=r1_Property)
gen_r1_Query_Expression = Generalization(general=Expression, specific=r1_Query)
gen_r1_QueryDefineRef_Expression = Generalization(general=Expression, specific=r1_QueryDefineRef)
gen_r1_RelationshipClause_AliasedQuerySource = Generalization(general=AliasedQuerySource, specific=r1_RelationshipClause)
gen_r1_Retrieve_Expression = Generalization(general=Expression, specific=r1_Retrieve)
gen_r1_ReturnClause_Element = Generalization(general=Element, specific=r1_ReturnClause)
gen_r1_Round_Expression = Generalization(general=Expression, specific=r1_Round)
gen_r1_SameOrAfter_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_SameOrAfter)
gen_r1_SameOrBefore_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_SameOrBefore)
gen_r1_SameAs_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_SameAs)
gen_r1_SortByItem_Element = Generalization(general=Element, specific=r1_SortByItem)
gen_r1_SortClause_Element = Generalization(general=Element, specific=r1_SortClause)
gen_r1_SingletonFrom_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_SingletonFrom)
gen_r1_Sort_Expression = Generalization(general=Expression, specific=r1_Sort)
gen_r1_Split_Expression = Generalization(general=Expression, specific=r1_Split)
gen_r1_Start_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Start)
gen_r1_Substring_Expression = Generalization(general=Expression, specific=r1_Substring)
gen_r1_Starts_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Starts)
gen_r1_StdDev_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_StdDev)
gen_r1_TernaryExpression_Expression = Generalization(general=Expression, specific=r1_TernaryExpression)
gen_r1_Time_Expression = Generalization(general=Expression, specific=r1_Time)
gen_r1_Subtract_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Subtract)
gen_r1_Successor_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Successor)
gen_r1_Sum_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Sum)
gen_r1_Times_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Times)
gen_r1_TimeFrom_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_TimeFrom)
gen_r1_TimeOfDay_Expression = Generalization(general=Expression, specific=r1_TimeOfDay)
gen_r1_TimezoneFrom_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_TimezoneFrom)
gen_r1_Today_Expression = Generalization(general=Expression, specific=r1_Today)
gen_r1_Truncate_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Truncate)
gen_r1_TruncatedDivide_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_TruncatedDivide)
gen_r1_Tuple_Expression = Generalization(general=Expression, specific=r1_Tuple)
gen_r1_TupleTypeSpecifier_TypeSpecifier = Generalization(general=TypeSpecifier, specific=r1_TupleTypeSpecifier)
gen_r1_TypeSpecifier_Element = Generalization(general=Element, specific=r1_TypeSpecifier)
gen_r1_TupleElementDefinition_Element = Generalization(general=Element, specific=r1_TupleElementDefinition)
gen_r1_Upper_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Upper)
gen_r1_ValueSetDef_Element = Generalization(general=Element, specific=r1_ValueSetDef)
gen_r1_UnaryExpression_Expression = Generalization(general=Expression, specific=r1_UnaryExpression)
gen_r1_Union_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Union)
gen_r1_ValueSetRef_Expression = Generalization(general=Expression, specific=r1_ValueSetRef)
gen_r1_Variance_AggregateExpression = Generalization(general=AggregateExpression, specific=r1_Variance)
gen_r1_Width_UnaryExpression = Generalization(general=UnaryExpression, specific=r1_Width)
gen_r1_Without_RelationshipClause = Generalization(general=RelationshipClause, specific=r1_Without)
gen_r1_Xor_BinaryExpression = Generalization(general=BinaryExpression, specific=r1_Xor)
gen_r1_With_RelationshipClause = Generalization(general=RelationshipClause, specific=r1_With)

# Domain Model
domain_model = DomainModel(
    name="r1",
    types={r1_Abs, UnaryExpression, r1_Add, BinaryExpression, r1_After, r1_AggregateExpression, Expression, r1_Expression, r1_AliasedQuerySource, Element, r1_AliasRef, r1_AllTrue, AggregateExpression, r1_AnyTrue, r1_As, r1_TypeSpecifier, r1_And, r1_Before, r1_BinaryExpression, r1_ByColumn, SortByItem, r1_Avg, r1_ByExpression, r1_CalculateAge, r1_CalculateAgeAt, r1_ByDirection, r1_CaseItem, r1_Case, r1_Ceiling, r1_Coalesce, NaryExpression, r1_Code, r1_CodeSystemRef, r1_CodeSystemDef, r1_Combine, r1_Collapse, r1_Contains, r1_Concatenate, r1_Concept, r1_Count, r1_Current, r1_Convert, r1_DateFrom, r1_DateTime, r1_DateTimeComponentFrom, r1_DifferenceBetween, r1_DefineClause, r1_Element, r1_EObject, r1_Distinct, r1_Divide, r1_DurationBetween, r1_Equal, r1_Except, r1_Exists, r1_End, r1_Ends, r1_Expand, r1_ExpressionDef, r1_ExpressionRef, r1_Filter, r1_Floor, r1_ForEach, r1_First, r1_OperandDef, r1_FunctionRef, ExpressionRef, r1_FunctionDef, ExpressionDef, r1_If, r1_Greater, r1_GreaterOrEqual, r1_IdentifierRef, r1_In, r1_IncludedIn, r1_Includes, r1_IndexOf, r1_Instance, r1_InstanceElement, r1_InCodeSystem, r1_Indexer, r1_Intersect, r1_Interval, r1_IntervalTypeSpecifier, TypeSpecifier, r1_InValueSet, r1_ValueSetRef, r1_IsNull, r1_IsTrue, r1_Last, r1_Is, r1_IsFalse, r1_ListTypeSpecifier, r1_Length, r1_Literal, r1_Less, r1_LessOrEqual, r1_List, r1_Log, r1_Lower, r1_Matches, r1_Max, r1_MaxValue, r1_Ln, r1_Median, r1_Meets, r1_MeetsAfter, r1_MeetsBefore, r1_MinValue, r1_Mode, r1_Modulo, r1_Multiply, r1_NamedTypeSpecifier, r1_Min, r1_Now, r1_NaryExpression, r1_Null, r1_Negate, r1_Not, r1_NotEqual, r1_OperandRef, r1_Or, r1_Overlaps, r1_OverlapsBefore, r1_ParameterDef, r1_OverlapsAfter, r1_ParameterRef, r1_PopulationStdDev, r1_Power, r1_PopulationVariance, r1_PositionOf, r1_ProperIn, r1_ProperIncludedIn, r1_ProperIncludes, r1_Predecessor, r1_ProperContains, r1_Quantity, r1_Property, r1_RelationshipClause, r1_Query, r1_SortClause, r1_QueryDefineRef, AliasedQuerySource, r1_ReturnClause, r1_Retrieve, r1_Round, r1_SameOrAfter, r1_SameOrBefore, r1_SameAs, r1_SortByItem, r1_SingletonFrom, r1_Sort, r1_Split, r1_Start, r1_Substring, r1_Starts, r1_StdDev, r1_TernaryExpression, r1_Time, r1_Subtract, r1_Successor, r1_Sum, r1_Times, r1_TimeFrom, r1_TimeOfDay, r1_TimezoneFrom, r1_Today, r1_Truncate, r1_TruncatedDivide, r1_Tuple, r1_TupleElement, r1_TupleTypeSpecifier, r1_TupleElementDefinition, r1_Upper, r1_ValueSetDef, r1_UnaryExpression, r1_Union, r1_Variance, r1_Width, r1_With, RelationshipClause, r1_Without, r1_Xor, AccessModifier, DateTimePrecision, SortDirection},
    associations={source0, expression1, asTypeSpecifier3, operand4, expression6, comparand8, caseItem10, else12, when15, then18, system21, source22, code27, separator24, toTypeSpecifier29, month33, day36, hour39, year31, millisecond48, timezoneOffset51, minute42, second45, expression54, annotation56, expression57, source59, condition61, source66, source64, operand71, operand72, element68, condition74, then76, else79, source87, element89, element92, code82, codesystem84, value93, low96, pointType107, code109, lowClosedExpression98, high101, highClosedExpression104, source115, valueset111, isTypeSpecifier113, element119, elementType122, typeSpecifier117, operand124, operandTypeSpecifier126, default129, parameterTypeSpecifier131, pattern134, string136, source139, source141, define143, relationship146, where148, sort153, return151, codes158, dateRange160, suchThat155, expression163, operand166, precision168, by173, source171, stringToSplit178, separator180, by175, stringToSub183, startIndex185, length188, operand191, hour193, second198, millisecond201, timezoneOffset204, minute195, element207, element213, value208, type211, codeSystem217, operand215},
    generalizations={gen_r1_Abs_UnaryExpression, gen_r1_Add_BinaryExpression, gen_r1_After_BinaryExpression, gen_r1_AggregateExpression_Expression, gen_r1_AliasedQuerySource_Element, gen_r1_AliasRef_Expression, gen_r1_AllTrue_AggregateExpression, gen_r1_AnyTrue_AggregateExpression, gen_r1_As_UnaryExpression, gen_r1_And_BinaryExpression, gen_r1_Before_BinaryExpression, gen_r1_BinaryExpression_Expression, gen_r1_ByColumn_SortByItem, gen_r1_Avg_AggregateExpression, gen_r1_ByExpression_SortByItem, gen_r1_CalculateAge_UnaryExpression, gen_r1_CalculateAgeAt_BinaryExpression, gen_r1_ByDirection_SortByItem, gen_r1_CaseItem_Element, gen_r1_Case_Expression, gen_r1_Ceiling_UnaryExpression, gen_r1_Coalesce_NaryExpression, gen_r1_Code_Expression, gen_r1_CodeSystemDef_Element, gen_r1_Combine_Expression, gen_r1_CodeSystemRef_Expression, gen_r1_Collapse_UnaryExpression, gen_r1_Contains_BinaryExpression, gen_r1_Concatenate_NaryExpression, gen_r1_Concept_Expression, gen_r1_Count_AggregateExpression, gen_r1_Current_Expression, gen_r1_Convert_UnaryExpression, gen_r1_DateFrom_UnaryExpression, gen_r1_DateTime_Expression, gen_r1_DateTimeComponentFrom_UnaryExpression, gen_r1_DifferenceBetween_BinaryExpression, gen_r1_DefineClause_Element, gen_r1_Distinct_UnaryExpression, gen_r1_Divide_BinaryExpression, gen_r1_DurationBetween_BinaryExpression, gen_r1_Equal_BinaryExpression, gen_r1_Except_BinaryExpression, gen_r1_Exists_UnaryExpression, gen_r1_End_UnaryExpression, gen_r1_Ends_BinaryExpression, gen_r1_Expand_UnaryExpression, gen_r1_Expression_Element, gen_r1_ExpressionDef_Element, gen_r1_ExpressionRef_Expression, gen_r1_Filter_Expression, gen_r1_Floor_UnaryExpression, gen_r1_ForEach_Expression, gen_r1_First_Expression, gen_r1_FunctionRef_ExpressionRef, gen_r1_FunctionDef_ExpressionDef, gen_r1_If_Expression, gen_r1_Greater_BinaryExpression, gen_r1_GreaterOrEqual_BinaryExpression, gen_r1_IdentifierRef_Expression, gen_r1_In_BinaryExpression, gen_r1_IncludedIn_BinaryExpression, gen_r1_Includes_BinaryExpression, gen_r1_IndexOf_Expression, gen_r1_Instance_Expression, gen_r1_InCodeSystem_Expression, gen_r1_Indexer_BinaryExpression, gen_r1_Intersect_BinaryExpression, gen_r1_Interval_Expression, gen_r1_IntervalTypeSpecifier_TypeSpecifier, gen_r1_InValueSet_Expression, gen_r1_IsNull_UnaryExpression, gen_r1_IsTrue_UnaryExpression, gen_r1_Last_Expression, gen_r1_Is_UnaryExpression, gen_r1_IsFalse_UnaryExpression, gen_r1_ListTypeSpecifier_TypeSpecifier, gen_r1_Length_UnaryExpression, gen_r1_Literal_Expression, gen_r1_Less_BinaryExpression, gen_r1_LessOrEqual_BinaryExpression, gen_r1_List_Expression, gen_r1_Log_BinaryExpression, gen_r1_Lower_UnaryExpression, gen_r1_Matches_BinaryExpression, gen_r1_Max_AggregateExpression, gen_r1_MaxValue_Expression, gen_r1_Ln_UnaryExpression, gen_r1_Median_AggregateExpression, gen_r1_Meets_BinaryExpression, gen_r1_MeetsAfter_BinaryExpression, gen_r1_MeetsBefore_BinaryExpression, gen_r1_MinValue_Expression, gen_r1_Mode_AggregateExpression, gen_r1_Modulo_BinaryExpression, gen_r1_Multiply_BinaryExpression, gen_r1_NamedTypeSpecifier_TypeSpecifier, gen_r1_Min_AggregateExpression, gen_r1_Now_Expression, gen_r1_NaryExpression_Expression, gen_r1_Null_Expression, gen_r1_Negate_UnaryExpression, gen_r1_Not_UnaryExpression, gen_r1_NotEqual_BinaryExpression, gen_r1_OperandRef_Expression, gen_r1_Or_BinaryExpression, gen_r1_Overlaps_BinaryExpression, gen_r1_OperandDef_Element, gen_r1_OverlapsBefore_BinaryExpression, gen_r1_ParameterDef_Element, gen_r1_OverlapsAfter_BinaryExpression, gen_r1_ParameterRef_Expression, gen_r1_PopulationStdDev_AggregateExpression, gen_r1_Power_BinaryExpression, gen_r1_PopulationVariance_AggregateExpression, gen_r1_PositionOf_Expression, gen_r1_ProperIn_BinaryExpression, gen_r1_ProperIncludedIn_BinaryExpression, gen_r1_ProperIncludes_BinaryExpression, gen_r1_Predecessor_UnaryExpression, gen_r1_ProperContains_BinaryExpression, gen_r1_Quantity_Expression, gen_r1_Property_Expression, gen_r1_Query_Expression, gen_r1_QueryDefineRef_Expression, gen_r1_RelationshipClause_AliasedQuerySource, gen_r1_Retrieve_Expression, gen_r1_ReturnClause_Element, gen_r1_Round_Expression, gen_r1_SameOrAfter_BinaryExpression, gen_r1_SameOrBefore_BinaryExpression, gen_r1_SameAs_BinaryExpression, gen_r1_SortByItem_Element, gen_r1_SortClause_Element, gen_r1_SingletonFrom_UnaryExpression, gen_r1_Sort_Expression, gen_r1_Split_Expression, gen_r1_Start_UnaryExpression, gen_r1_Substring_Expression, gen_r1_Starts_BinaryExpression, gen_r1_StdDev_AggregateExpression, gen_r1_TernaryExpression_Expression, gen_r1_Time_Expression, gen_r1_Subtract_BinaryExpression, gen_r1_Successor_UnaryExpression, gen_r1_Sum_AggregateExpression, gen_r1_Times_BinaryExpression, gen_r1_TimeFrom_UnaryExpression, gen_r1_TimeOfDay_Expression, gen_r1_TimezoneFrom_UnaryExpression, gen_r1_Today_Expression, gen_r1_Truncate_UnaryExpression, gen_r1_TruncatedDivide_BinaryExpression, gen_r1_Tuple_Expression, gen_r1_TupleTypeSpecifier_TypeSpecifier, gen_r1_TypeSpecifier_Element, gen_r1_TupleElementDefinition_Element, gen_r1_Upper_UnaryExpression, gen_r1_ValueSetDef_Element, gen_r1_UnaryExpression_Expression, gen_r1_Union_BinaryExpression, gen_r1_ValueSetRef_Expression, gen_r1_Variance_AggregateExpression, gen_r1_Width_UnaryExpression, gen_r1_Without_RelationshipClause, gen_r1_Xor_BinaryExpression, gen_r1_With_RelationshipClause},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)