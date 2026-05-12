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
sparql_SparqlQueries = Class(name="sparql_SparqlQueries")
LocatedElement = Class(name="LocatedElement")
sparql_Prologue = Class(name="sparql_Prologue")
sparql_Query = Class(name="sparql_Query", is_abstract=True)
sparql_BaseDecl = Class(name="sparql_BaseDecl")
sparql_PrefixDecl = Class(name="sparql_PrefixDecl")
sparql_IRI_REF = Class(name="sparql_IRI_REF")
sparql_LocatedElement = Class(name="sparql_LocatedElement", is_abstract=True)
sparql_Var = Class(name="sparql_Var")
sparql_DatasetClause = Class(name="sparql_DatasetClause")
sparql_WhereClause = Class(name="sparql_WhereClause")
sparql_PNAME_NS = Class(name="sparql_PNAME_NS")
sparql_SelectQuery = Class(name="sparql_SelectQuery")
Query = Class(name="Query")
sparql_SolutionsDisplayNE = Class(name="sparql_SolutionsDisplayNE", is_abstract=True)
sparql_DescribeQuery = Class(name="sparql_DescribeQuery")
sparql_VarOrIRIref = Class(name="sparql_VarOrIRIref", is_abstract=True)
sparql_AskQuery = Class(name="sparql_AskQuery")
sparql_SolutionModifier = Class(name="sparql_SolutionModifier")
sparql_ConstructQuery = Class(name="sparql_ConstructQuery")
sparql_ConstructTemplate = Class(name="sparql_ConstructTemplate")
sparql_LimitOffsetClauses = Class(name="sparql_LimitOffsetClauses", is_abstract=True)
sparql_OrderCondition = Class(name="sparql_OrderCondition", is_abstract=True)
sparql_OrderConditionLeftNE = Class(name="sparql_OrderConditionLeftNE")
OrderCondition = Class(name="OrderCondition")
sparql_AscOrDecs = Class(name="sparql_AscOrDecs", is_abstract=True)
sparql_BrackettedExpression = Class(name="sparql_BrackettedExpression")
sparql_OrderConditionRightNE = Class(name="sparql_OrderConditionRightNE", is_abstract=True)
sparql_LimitOffsetClausesLeftNE = Class(name="sparql_LimitOffsetClausesLeftNE")
LimitOffsetClauses = Class(name="LimitOffsetClauses")
sparql_LimitClause = Class(name="sparql_LimitClause")
sparql_OffsetClause = Class(name="sparql_OffsetClause")
sparql_TriplesSameSubject = Class(name="sparql_TriplesSameSubject", is_abstract=True)
sparql_OrderClause = Class(name="sparql_OrderClause")
sparql_INTEGER = Class(name="sparql_INTEGER")
sparql_DistinctNE = Class(name="sparql_DistinctNE")
SolutionsDisplayNE = Class(name="SolutionsDisplayNE")
sparql_ReducedNE = Class(name="sparql_ReducedNE")
sparql_VariablesNE = Class(name="sparql_VariablesNE", is_abstract=True)
sparql_AllVariablesNE = Class(name="sparql_AllVariablesNE")
VariablesNE = Class(name="VariablesNE")
sparql_SomeVariablesNE = Class(name="sparql_SomeVariablesNE")
Verb = Class(name="Verb")
VarOrIRIref = Class(name="VarOrIRIref")
PrimaryExpression = Class(name="PrimaryExpression")
VarOrTerm = Class(name="VarOrTerm")
OrderConditionRightNE = Class(name="OrderConditionRightNE")
sparql_LimitOffsetClausesRightNE = Class(name="sparql_LimitOffsetClausesRightNE")
sparql_GraphClauseNE = Class(name="sparql_GraphClauseNE", is_abstract=True)
sparql_DefaultGraphClause = Class(name="sparql_DefaultGraphClause")
GraphClauseNE = Class(name="GraphClauseNE")
sparql_SourceSelector = Class(name="sparql_SourceSelector", is_abstract=True)
sparql_NamedGraphClause = Class(name="sparql_NamedGraphClause")
sparql_WhereLiteral = Class(name="sparql_WhereLiteral")
sparql_GroupGraphPattern = Class(name="sparql_GroupGraphPattern")
sparql_IRIreference = Class(name="sparql_IRIreference", is_abstract=True)
GraphTerm = Class(name="GraphTerm")
SourceSelector = Class(name="SourceSelector")
sparql_PrefixedName = Class(name="sparql_PrefixedName", is_abstract=True)
IRIreference = Class(name="IRIreference")
sparql_TriplesSameSubjectRightNE = Class(name="sparql_TriplesSameSubjectRightNE")
sparql_TriplesNode = Class(name="sparql_TriplesNode", is_abstract=True)
sparql_GraphPatternNotTriples = Class(name="sparql_GraphPatternNotTriples", is_abstract=True)
PatternOrFilterNE = Class(name="PatternOrFilterNE")
sparql_OptionalGraphPattern = Class(name="sparql_OptionalGraphPattern")
GraphPatternNotTriples = Class(name="GraphPatternNotTriples")
sparql_GroupOrUnionGraphPattern = Class(name="sparql_GroupOrUnionGraphPattern")
sparql_GraphGraphPattern = Class(name="sparql_GraphGraphPattern")
sparql_Filter = Class(name="sparql_Filter")
sparql_Constraint = Class(name="sparql_Constraint", is_abstract=True)
sparql_TriplesBlock = Class(name="sparql_TriplesBlock")
sparql_AdditionalGGPElement = Class(name="sparql_AdditionalGGPElement")
sparql_TriplesSameSubjectLeftNE = Class(name="sparql_TriplesSameSubjectLeftNE")
TriplesSameSubject = Class(name="TriplesSameSubject")
sparql_VarOrTerm = Class(name="sparql_VarOrTerm", is_abstract=True)
sparql_PatternOrFilterNE = Class(name="sparql_PatternOrFilterNE", is_abstract=True)
sparql_PropertyListNotEmpty = Class(name="sparql_PropertyListNotEmpty")
GraphNode = Class(name="GraphNode")
sparql_Verb = Class(name="sparql_Verb", is_abstract=True)
sparql_ObjectList = Class(name="sparql_ObjectList")
sparql_VerbANE = Class(name="sparql_VerbANE")
sparql_Object = Class(name="sparql_Object")
sparql_GraphNode = Class(name="sparql_GraphNode", is_abstract=True)
sparql_Collection = Class(name="sparql_Collection")
TriplesNode = Class(name="TriplesNode")
sparql_BlankNodePropertyList = Class(name="sparql_BlankNodePropertyList")
sparql_BoundBuiltInCallNE = Class(name="sparql_BoundBuiltInCallNE")
sparql_SameTermBuiltInCallNE = Class(name="sparql_SameTermBuiltInCallNE")
sparql_GraphTerm = Class(name="sparql_GraphTerm", is_abstract=True)
sparql_BlankNode = Class(name="sparql_BlankNode", is_abstract=True)
Constraint = Class(name="Constraint")
sparql_Expression = Class(name="sparql_Expression")
sparql_BuiltInCall = Class(name="sparql_BuiltInCall", is_abstract=True)
sparql_StrBuiltInCallNE = Class(name="sparql_StrBuiltInCallNE")
BuiltInCall = Class(name="BuiltInCall")
sparql_LangBuiltInCallNE = Class(name="sparql_LangBuiltInCallNE")
sparql_LangmatchesBuiltInCallNE = Class(name="sparql_LangmatchesBuiltInCallNE")
sparql_AdditionalExpressionNE = Class(name="sparql_AdditionalExpressionNE")
sparql_DatatypeBuiltInCallNE = Class(name="sparql_DatatypeBuiltInCallNE")
sparql_FunctionCall = Class(name="sparql_FunctionCall")
sparql_ArgList = Class(name="sparql_ArgList", is_abstract=True)
sparql_IsIRIBuiltInCallNE = Class(name="sparql_IsIRIBuiltInCallNE")
sparql_IsURIBuiltInCallNE = Class(name="sparql_IsURIBuiltInCallNE")
sparql_IsBlankBuiltInCallNE = Class(name="sparql_IsBlankBuiltInCallNE")
sparql_IsLiteralBuiltInCallNE = Class(name="sparql_IsLiteralBuiltInCallNE")
sparql_RegexExpression = Class(name="sparql_RegexExpression")
sparql_ConditionalOrExpression = Class(name="sparql_ConditionalOrExpression")
sparql_ArgListNILNE = Class(name="sparql_ArgListNILNE")
ArgList = Class(name="ArgList")
sparql_NotInList = Class(name="sparql_NotInList")
sparql_ArgListExpressionNE = Class(name="sparql_ArgListExpressionNE")
sparql_ValueLogical = Class(name="sparql_ValueLogical")
sparql_ConditionalAndExpression = Class(name="sparql_ConditionalAndExpression")
sparql_AdditionalConditionalAndExpressionNE = Class(name="sparql_AdditionalConditionalAndExpressionNE")
sparql_AdditionalNumericExpressionNE = Class(name="sparql_AdditionalNumericExpressionNE", is_abstract=True)
sparql_AdditiveExpression = Class(name="sparql_AdditiveExpression")
sparql_EqualsNumericExpressionNE = Class(name="sparql_EqualsNumericExpressionNE")
AdditionalNumericExpressionNE = Class(name="AdditionalNumericExpressionNE")
sparql_AdditionalValueLogicalNE = Class(name="sparql_AdditionalValueLogicalNE")
sparql_RelationalExpression = Class(name="sparql_RelationalExpression")
sparql_NumericExpression = Class(name="sparql_NumericExpression")
sparql_MultiplicativeExpression = Class(name="sparql_MultiplicativeExpression")
sparql_AdditionalMultiplicativeExpressionNE = Class(name="sparql_AdditionalMultiplicativeExpressionNE", is_abstract=True)
sparql_UnaryExpression = Class(name="sparql_UnaryExpression", is_abstract=True)
sparql_AdditionalUnaryExpressionNE = Class(name="sparql_AdditionalUnaryExpressionNE", is_abstract=True)
sparql_NotEqualNumericExpressionNE = Class(name="sparql_NotEqualNumericExpressionNE")
sparql_SmallerNumericExpressionNE = Class(name="sparql_SmallerNumericExpressionNE")
sparql_BiggerNumericExpressionNE = Class(name="sparql_BiggerNumericExpressionNE")
sparql_SmallerOrEqualNumericExpressionNE = Class(name="sparql_SmallerOrEqualNumericExpressionNE")
sparql_BiggerOrEqualNumericExpressionNE = Class(name="sparql_BiggerOrEqualNumericExpressionNE")
sparql_DividedByAdditionalUnaryExpressionNE = Class(name="sparql_DividedByAdditionalUnaryExpressionNE")
sparql_NotPrimaryExpressionNE = Class(name="sparql_NotPrimaryExpressionNE")
UnaryExpression = Class(name="UnaryExpression")
sparql_PrimaryExpression = Class(name="sparql_PrimaryExpression", is_abstract=True)
sparql_PlusPrimaryExpressionNE = Class(name="sparql_PlusPrimaryExpressionNE")
sparql_PlusMultiplicativeExpressionNE = Class(name="sparql_PlusMultiplicativeExpressionNE")
AdditionalMultiplicativeExpressionNE = Class(name="AdditionalMultiplicativeExpressionNE")
sparql_MinusMultiplicativeExpressionNE = Class(name="sparql_MinusMultiplicativeExpressionNE")
sparql_NumericLiteralPositive = Class(name="sparql_NumericLiteralPositive", is_abstract=True)
NumericLiteral = Class(name="NumericLiteral")
sparql_NumericLiteralNegative = Class(name="sparql_NumericLiteralNegative", is_abstract=True)
sparql_TimesAdditionalUnaryExpressionNE = Class(name="sparql_TimesAdditionalUnaryExpressionNE")
AdditionalUnaryExpressionNE = Class(name="AdditionalUnaryExpressionNE")
sparql_UpIRIrefNE = Class(name="sparql_UpIRIrefNE")
LANGTAGOrIRIrefNE = Class(name="LANGTAGOrIRIrefNE")
sparql_NumericLiteral = Class(name="sparql_NumericLiteral", is_abstract=True)
sparql_NumericLiteralUnsigned = Class(name="sparql_NumericLiteralUnsigned", is_abstract=True)
sparql_MinusPrimaryExpressionNE = Class(name="sparql_MinusPrimaryExpressionNE")
sparql_IRIrefOrFunction = Class(name="sparql_IRIrefOrFunction")
sparql_RDFLiteral = Class(name="sparql_RDFLiteral")
sparql_StringLiteral = Class(name="sparql_StringLiteral", is_abstract=True)
sparql_LANGTAGOrIRIrefNE = Class(name="sparql_LANGTAGOrIRIrefNE", is_abstract=True)
PrefixedName = Class(name="PrefixedName")
sparql_PNAME_LN = Class(name="sparql_PNAME_LN")
sparql_PN_LOCAL = Class(name="sparql_PN_LOCAL")
sparql_WS = Class(name="sparql_WS")
sparql_BooleanLiteral = Class(name="sparql_BooleanLiteral", is_abstract=True)
sparql_TrueBooleanLiteralNE = Class(name="sparql_TrueBooleanLiteralNE")
BooleanLiteral = Class(name="BooleanLiteral")
sparql_FalseBooleanLiteralNE = Class(name="sparql_FalseBooleanLiteralNE")
sparql_VAR1 = Class(name="sparql_VAR1")
sparql_VARNAME = Class(name="sparql_VARNAME")
sparql_VAR2 = Class(name="sparql_VAR2")
sparql_STRING_LITERAL1 = Class(name="sparql_STRING_LITERAL1")
StringLiteral = Class(name="StringLiteral")
sparql_STRING_LITERAL2 = Class(name="sparql_STRING_LITERAL2")
sparql_DECIMAL = Class(name="sparql_DECIMAL")
sparql_DOUBLE = Class(name="sparql_DOUBLE")
sparql_AscendingLiteral = Class(name="sparql_AscendingLiteral")
AscOrDecs = Class(name="AscOrDecs")
sparql_DescendingLiteral = Class(name="sparql_DescendingLiteral")
sparql_STRING_LITERAL_LONG1 = Class(name="sparql_STRING_LITERAL_LONG1")
sparql_STRING_LITERAL_LONG2 = Class(name="sparql_STRING_LITERAL_LONG2")
sparql_BLANK_NODE_LABEL = Class(name="sparql_BLANK_NODE_LABEL")
BlankNode = Class(name="BlankNode")
sparql_ANON = Class(name="sparql_ANON")
sparql_LANGTAG = Class(name="sparql_LANGTAG")
sparql_PN_PREFIX = Class(name="sparql_PN_PREFIX")

# sparql_SparqlQueries class attributes and methods

# LocatedElement class attributes and methods

# sparql_Prologue class attributes and methods

# sparql_Query class attributes and methods

# sparql_BaseDecl class attributes and methods

# sparql_PrefixDecl class attributes and methods

# sparql_IRI_REF class attributes and methods
sparql_IRI_REF_iri_ref: Property = Property(name="iri_ref", type=StringType)
sparql_IRI_REF.attributes={sparql_IRI_REF_iri_ref}

# sparql_LocatedElement class attributes and methods
sparql_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
sparql_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
sparql_LocatedElement_location: Property = Property(name="location", type=StringType)
sparql_LocatedElement.attributes={sparql_LocatedElement_commentsAfter, sparql_LocatedElement_commentsBefore, sparql_LocatedElement_location}

# sparql_Var class attributes and methods
sparql_Var_varname: Property = Property(name="varname", type=StringType)
sparql_Var.attributes={sparql_Var_varname}

# sparql_DatasetClause class attributes and methods

# sparql_WhereClause class attributes and methods

# sparql_PNAME_NS class attributes and methods
sparql_PNAME_NS_pn_prefix: Property = Property(name="pn_prefix", type=StringType)
sparql_PNAME_NS.attributes={sparql_PNAME_NS_pn_prefix}

# sparql_SelectQuery class attributes and methods

# Query class attributes and methods

# sparql_SolutionsDisplayNE class attributes and methods

# sparql_DescribeQuery class attributes and methods

# sparql_VarOrIRIref class attributes and methods

# sparql_AskQuery class attributes and methods

# sparql_SolutionModifier class attributes and methods

# sparql_ConstructQuery class attributes and methods

# sparql_ConstructTemplate class attributes and methods

# sparql_LimitOffsetClauses class attributes and methods

# sparql_OrderCondition class attributes and methods

# sparql_OrderConditionLeftNE class attributes and methods

# OrderCondition class attributes and methods

# sparql_AscOrDecs class attributes and methods

# sparql_BrackettedExpression class attributes and methods

# sparql_OrderConditionRightNE class attributes and methods

# sparql_LimitOffsetClausesLeftNE class attributes and methods

# LimitOffsetClauses class attributes and methods

# sparql_LimitClause class attributes and methods

# sparql_OffsetClause class attributes and methods

# sparql_TriplesSameSubject class attributes and methods

# sparql_OrderClause class attributes and methods

# sparql_INTEGER class attributes and methods
sparql_INTEGER_integer: Property = Property(name="integer", type=StringType)
sparql_INTEGER.attributes={sparql_INTEGER_integer}

# sparql_DistinctNE class attributes and methods

# SolutionsDisplayNE class attributes and methods

# sparql_ReducedNE class attributes and methods

# sparql_VariablesNE class attributes and methods

# sparql_AllVariablesNE class attributes and methods

# VariablesNE class attributes and methods

# sparql_SomeVariablesNE class attributes and methods

# Verb class attributes and methods

# VarOrIRIref class attributes and methods

# PrimaryExpression class attributes and methods

# VarOrTerm class attributes and methods

# OrderConditionRightNE class attributes and methods

# sparql_LimitOffsetClausesRightNE class attributes and methods

# sparql_GraphClauseNE class attributes and methods

# sparql_DefaultGraphClause class attributes and methods

# GraphClauseNE class attributes and methods

# sparql_SourceSelector class attributes and methods

# sparql_NamedGraphClause class attributes and methods

# sparql_WhereLiteral class attributes and methods

# sparql_GroupGraphPattern class attributes and methods

# sparql_IRIreference class attributes and methods

# GraphTerm class attributes and methods

# SourceSelector class attributes and methods

# sparql_PrefixedName class attributes and methods

# IRIreference class attributes and methods

# sparql_TriplesSameSubjectRightNE class attributes and methods

# sparql_TriplesNode class attributes and methods

# sparql_GraphPatternNotTriples class attributes and methods

# PatternOrFilterNE class attributes and methods

# sparql_OptionalGraphPattern class attributes and methods

# GraphPatternNotTriples class attributes and methods

# sparql_GroupOrUnionGraphPattern class attributes and methods

# sparql_GraphGraphPattern class attributes and methods

# sparql_Filter class attributes and methods

# sparql_Constraint class attributes and methods

# sparql_TriplesBlock class attributes and methods

# sparql_AdditionalGGPElement class attributes and methods

# sparql_TriplesSameSubjectLeftNE class attributes and methods

# TriplesSameSubject class attributes and methods

# sparql_VarOrTerm class attributes and methods

# sparql_PatternOrFilterNE class attributes and methods

# sparql_PropertyListNotEmpty class attributes and methods

# GraphNode class attributes and methods

# sparql_Verb class attributes and methods

# sparql_ObjectList class attributes and methods

# sparql_VerbANE class attributes and methods
sparql_VerbANE_theA: Property = Property(name="theA", type=StringType)
sparql_VerbANE.attributes={sparql_VerbANE_theA}

# sparql_Object class attributes and methods

# sparql_GraphNode class attributes and methods

# sparql_Collection class attributes and methods

# TriplesNode class attributes and methods

# sparql_BlankNodePropertyList class attributes and methods

# sparql_BoundBuiltInCallNE class attributes and methods

# sparql_SameTermBuiltInCallNE class attributes and methods

# sparql_GraphTerm class attributes and methods

# sparql_BlankNode class attributes and methods

# Constraint class attributes and methods

# sparql_Expression class attributes and methods

# sparql_BuiltInCall class attributes and methods

# sparql_StrBuiltInCallNE class attributes and methods

# BuiltInCall class attributes and methods

# sparql_LangBuiltInCallNE class attributes and methods

# sparql_LangmatchesBuiltInCallNE class attributes and methods

# sparql_AdditionalExpressionNE class attributes and methods

# sparql_DatatypeBuiltInCallNE class attributes and methods

# sparql_FunctionCall class attributes and methods

# sparql_ArgList class attributes and methods

# sparql_IsIRIBuiltInCallNE class attributes and methods

# sparql_IsURIBuiltInCallNE class attributes and methods

# sparql_IsBlankBuiltInCallNE class attributes and methods

# sparql_IsLiteralBuiltInCallNE class attributes and methods

# sparql_RegexExpression class attributes and methods

# sparql_ConditionalOrExpression class attributes and methods

# sparql_ArgListNILNE class attributes and methods

# ArgList class attributes and methods

# sparql_NotInList class attributes and methods

# sparql_ArgListExpressionNE class attributes and methods

# sparql_ValueLogical class attributes and methods

# sparql_ConditionalAndExpression class attributes and methods

# sparql_AdditionalConditionalAndExpressionNE class attributes and methods

# sparql_AdditionalNumericExpressionNE class attributes and methods

# sparql_AdditiveExpression class attributes and methods

# sparql_EqualsNumericExpressionNE class attributes and methods

# AdditionalNumericExpressionNE class attributes and methods

# sparql_AdditionalValueLogicalNE class attributes and methods

# sparql_RelationalExpression class attributes and methods

# sparql_NumericExpression class attributes and methods

# sparql_MultiplicativeExpression class attributes and methods

# sparql_AdditionalMultiplicativeExpressionNE class attributes and methods

# sparql_UnaryExpression class attributes and methods

# sparql_AdditionalUnaryExpressionNE class attributes and methods

# sparql_NotEqualNumericExpressionNE class attributes and methods

# sparql_SmallerNumericExpressionNE class attributes and methods

# sparql_BiggerNumericExpressionNE class attributes and methods

# sparql_SmallerOrEqualNumericExpressionNE class attributes and methods

# sparql_BiggerOrEqualNumericExpressionNE class attributes and methods

# sparql_DividedByAdditionalUnaryExpressionNE class attributes and methods

# sparql_NotPrimaryExpressionNE class attributes and methods

# UnaryExpression class attributes and methods

# sparql_PrimaryExpression class attributes and methods

# sparql_PlusPrimaryExpressionNE class attributes and methods

# sparql_PlusMultiplicativeExpressionNE class attributes and methods

# AdditionalMultiplicativeExpressionNE class attributes and methods

# sparql_MinusMultiplicativeExpressionNE class attributes and methods

# sparql_NumericLiteralPositive class attributes and methods

# NumericLiteral class attributes and methods

# sparql_NumericLiteralNegative class attributes and methods

# sparql_TimesAdditionalUnaryExpressionNE class attributes and methods

# AdditionalUnaryExpressionNE class attributes and methods

# sparql_UpIRIrefNE class attributes and methods

# LANGTAGOrIRIrefNE class attributes and methods

# sparql_NumericLiteral class attributes and methods

# sparql_NumericLiteralUnsigned class attributes and methods

# sparql_MinusPrimaryExpressionNE class attributes and methods

# sparql_IRIrefOrFunction class attributes and methods

# sparql_RDFLiteral class attributes and methods

# sparql_StringLiteral class attributes and methods

# sparql_LANGTAGOrIRIrefNE class attributes and methods

# PrefixedName class attributes and methods

# sparql_PNAME_LN class attributes and methods

# sparql_PN_LOCAL class attributes and methods
sparql_PN_LOCAL_pn_local: Property = Property(name="pn_local", type=StringType)
sparql_PN_LOCAL.attributes={sparql_PN_LOCAL_pn_local}

# sparql_WS class attributes and methods
sparql_WS_ws: Property = Property(name="ws", type=StringType)
sparql_WS.attributes={sparql_WS_ws}

# sparql_BooleanLiteral class attributes and methods

# sparql_TrueBooleanLiteralNE class attributes and methods

# BooleanLiteral class attributes and methods

# sparql_FalseBooleanLiteralNE class attributes and methods

# sparql_VAR1 class attributes and methods

# sparql_VARNAME class attributes and methods
sparql_VARNAME_varname: Property = Property(name="varname", type=StringType)
sparql_VARNAME.attributes={sparql_VARNAME_varname}

# sparql_VAR2 class attributes and methods

# sparql_STRING_LITERAL1 class attributes and methods
sparql_STRING_LITERAL1_string: Property = Property(name="string", type=StringType)
sparql_STRING_LITERAL1.attributes={sparql_STRING_LITERAL1_string}

# StringLiteral class attributes and methods

# sparql_STRING_LITERAL2 class attributes and methods
sparql_STRING_LITERAL2_string: Property = Property(name="string", type=StringType)
sparql_STRING_LITERAL2.attributes={sparql_STRING_LITERAL2_string}

# sparql_DECIMAL class attributes and methods
sparql_DECIMAL_decimal: Property = Property(name="decimal", type=StringType)
sparql_DECIMAL.attributes={sparql_DECIMAL_decimal}

# sparql_DOUBLE class attributes and methods
sparql_DOUBLE_double: Property = Property(name="double", type=StringType)
sparql_DOUBLE.attributes={sparql_DOUBLE_double}

# sparql_AscendingLiteral class attributes and methods

# AscOrDecs class attributes and methods

# sparql_DescendingLiteral class attributes and methods

# sparql_STRING_LITERAL_LONG1 class attributes and methods
sparql_STRING_LITERAL_LONG1_string: Property = Property(name="string", type=StringType)
sparql_STRING_LITERAL_LONG1.attributes={sparql_STRING_LITERAL_LONG1_string}

# sparql_STRING_LITERAL_LONG2 class attributes and methods
sparql_STRING_LITERAL_LONG2_string: Property = Property(name="string", type=StringType)
sparql_STRING_LITERAL_LONG2.attributes={sparql_STRING_LITERAL_LONG2_string}

# sparql_BLANK_NODE_LABEL class attributes and methods
sparql_BLANK_NODE_LABEL_pn_local: Property = Property(name="pn_local", type=StringType)
sparql_BLANK_NODE_LABEL.attributes={sparql_BLANK_NODE_LABEL_pn_local}

# BlankNode class attributes and methods

# sparql_ANON class attributes and methods

# sparql_LANGTAG class attributes and methods
sparql_LANGTAG_langtag: Property = Property(name="langtag", type=StringType)
sparql_LANGTAG.attributes={sparql_LANGTAG_langtag}

# sparql_PN_PREFIX class attributes and methods
sparql_PN_PREFIX_pn_prefix: Property = Property(name="pn_prefix", type=StringType)
sparql_PN_PREFIX.attributes={sparql_PN_PREFIX_pn_prefix}

# Relationships
prologue0: BinaryAssociation = BinaryAssociation(
    name="prologue0",
    ends={
        Property(name="sparql_Prologue", type=sparql_SparqlQueries, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SparqlQueries", type=sparql_Prologue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
query1: BinaryAssociation = BinaryAssociation(
    name="query1",
    ends={
        Property(name="sparql_Query", type=sparql_SparqlQueries, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SparqlQueries2", type=sparql_Query, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
basedeclaration3: BinaryAssociation = BinaryAssociation(
    name="basedeclaration3",
    ends={
        Property(name="sparql_BaseDecl", type=sparql_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Prologue4", type=sparql_BaseDecl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
prefixdeclaration5: BinaryAssociation = BinaryAssociation(
    name="prefixdeclaration5",
    ends={
        Property(name="sparql_PrefixDecl", type=sparql_Prologue, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Prologue6", type=sparql_PrefixDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iriref7: BinaryAssociation = BinaryAssociation(
    name="iriref7",
    ends={
        Property(name="sparql_IRI_REF", type=sparql_BaseDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BaseDecl8", type=sparql_IRI_REF, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
solutionsdisplay14: BinaryAssociation = BinaryAssociation(
    name="solutionsdisplay14",
    ends={
        Property(name="sparql_SelectQuery", type=sparql_SolutionsDisplayNE, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="sparql_SolutionsDisplayNE", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1))
    }
)
var15: BinaryAssociation = BinaryAssociation(
    name="var15",
    ends={
        Property(name="sparql_Var", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectQuery16", type=sparql_Var, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
datasetclause17: BinaryAssociation = BinaryAssociation(
    name="datasetclause17",
    ends={
        Property(name="sparql_DatasetClause", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectQuery18", type=sparql_DatasetClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereclause19: BinaryAssociation = BinaryAssociation(
    name="whereclause19",
    ends={
        Property(name="sparql_WhereClause", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectQuery20", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pnamens9: BinaryAssociation = BinaryAssociation(
    name="pnamens9",
    ends={
        Property(name="sparql_PNAME_NS", type=sparql_PrefixDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PrefixDecl10", type=sparql_PNAME_NS, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iriref11: BinaryAssociation = BinaryAssociation(
    name="iriref11",
    ends={
        Property(name="sparql_IRI_REF13", type=sparql_PrefixDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PrefixDecl12", type=sparql_IRI_REF, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whereclause27: BinaryAssociation = BinaryAssociation(
    name="whereclause27",
    ends={
        Property(name="sparql_WhereClause29", type=sparql_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructQuery28", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
solutionmodifier30: BinaryAssociation = BinaryAssociation(
    name="solutionmodifier30",
    ends={
        Property(name="sparql_SolutionModifier32", type=sparql_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructQuery31", type=sparql_SolutionModifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varoririref33: BinaryAssociation = BinaryAssociation(
    name="varoririref33",
    ends={
        Property(name="sparql_VarOrIRIref", type=sparql_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DescribeQuery", type=sparql_VarOrIRIref, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
datasetclause34: BinaryAssociation = BinaryAssociation(
    name="datasetclause34",
    ends={
        Property(name="sparql_DatasetClause36", type=sparql_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DescribeQuery35", type=sparql_DatasetClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereclause37: BinaryAssociation = BinaryAssociation(
    name="whereclause37",
    ends={
        Property(name="sparql_WhereClause39", type=sparql_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DescribeQuery38", type=sparql_WhereClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
solutionmodifier40: BinaryAssociation = BinaryAssociation(
    name="solutionmodifier40",
    ends={
        Property(name="sparql_SolutionModifier42", type=sparql_DescribeQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DescribeQuery41", type=sparql_SolutionModifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
datasetclause43: BinaryAssociation = BinaryAssociation(
    name="datasetclause43",
    ends={
        Property(name="sparql_DatasetClause44", type=sparql_AskQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AskQuery", type=sparql_DatasetClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
solutionmodifier21: BinaryAssociation = BinaryAssociation(
    name="solutionmodifier21",
    ends={
        Property(name="sparql_SolutionModifier", type=sparql_SelectQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SelectQuery22", type=sparql_SolutionModifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constructtemplate23: BinaryAssociation = BinaryAssociation(
    name="constructtemplate23",
    ends={
        Property(name="sparql_ConstructTemplate", type=sparql_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructQuery", type=sparql_ConstructTemplate, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
datasetclause24: BinaryAssociation = BinaryAssociation(
    name="datasetclause24",
    ends={
        Property(name="sparql_DatasetClause26", type=sparql_ConstructQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructQuery25", type=sparql_DatasetClause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
limitoffsetclauses52: BinaryAssociation = BinaryAssociation(
    name="limitoffsetclauses52",
    ends={
        Property(name="sparql_LimitOffsetClauses", type=sparql_SolutionModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SolutionModifier53", type=sparql_LimitOffsetClauses, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ordercondition54: BinaryAssociation = BinaryAssociation(
    name="ordercondition54",
    ends={
        Property(name="sparql_OrderCondition", type=sparql_OrderClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OrderClause55", type=sparql_OrderCondition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ascOrDecs56: BinaryAssociation = BinaryAssociation(
    name="ascOrDecs56",
    ends={
        Property(name="sparql_AscOrDecs", type=sparql_OrderConditionLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OrderConditionLeftNE", type=sparql_AscOrDecs, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
brackettedexpression57: BinaryAssociation = BinaryAssociation(
    name="brackettedexpression57",
    ends={
        Property(name="sparql_BrackettedExpression", type=sparql_OrderConditionLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OrderConditionLeftNE58", type=sparql_BrackettedExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
limitclause59: BinaryAssociation = BinaryAssociation(
    name="limitclause59",
    ends={
        Property(name="sparql_LimitClause", type=sparql_LimitOffsetClausesLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LimitOffsetClausesLeftNE", type=sparql_LimitClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whereclause45: BinaryAssociation = BinaryAssociation(
    name="whereclause45",
    ends={
        Property(name="sparql_WhereClause47", type=sparql_AskQuery, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AskQuery46", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constructtriples48: BinaryAssociation = BinaryAssociation(
    name="constructtriples48",
    ends={
        Property(name="sparql_TriplesSameSubject", type=sparql_ConstructTemplate, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConstructTemplate49", type=sparql_TriplesSameSubject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
orderclause50: BinaryAssociation = BinaryAssociation(
    name="orderclause50",
    ends={
        Property(name="sparql_OrderClause", type=sparql_SolutionModifier, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SolutionModifier51", type=sparql_OrderClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer67: BinaryAssociation = BinaryAssociation(
    name="integer67",
    ends={
        Property(name="sparql_INTEGER", type=sparql_LimitClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LimitClause68", type=sparql_INTEGER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer69: BinaryAssociation = BinaryAssociation(
    name="integer69",
    ends={
        Property(name="sparql_INTEGER71", type=sparql_OffsetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OffsetClause70", type=sparql_INTEGER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables72: BinaryAssociation = BinaryAssociation(
    name="variables72",
    ends={
        Property(name="sparql_Var73", type=sparql_SomeVariablesNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SomeVariablesNE", type=sparql_Var, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
offsetclause60: BinaryAssociation = BinaryAssociation(
    name="offsetclause60",
    ends={
        Property(name="sparql_OffsetClause", type=sparql_LimitOffsetClausesLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LimitOffsetClausesLeftNE61", type=sparql_OffsetClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
offsetclause62: BinaryAssociation = BinaryAssociation(
    name="offsetclause62",
    ends={
        Property(name="sparql_OffsetClause63", type=sparql_LimitOffsetClausesRightNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LimitOffsetClausesRightNE", type=sparql_OffsetClause, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
limitclause64: BinaryAssociation = BinaryAssociation(
    name="limitclause64",
    ends={
        Property(name="sparql_LimitClause66", type=sparql_LimitOffsetClausesRightNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LimitOffsetClausesRightNE65", type=sparql_LimitClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
graphclause74: BinaryAssociation = BinaryAssociation(
    name="graphclause74",
    ends={
        Property(name="sparql_GraphClauseNE", type=sparql_DatasetClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DatasetClause75", type=sparql_GraphClauseNE, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceselector76: BinaryAssociation = BinaryAssociation(
    name="sourceselector76",
    ends={
        Property(name="sparql_SourceSelector", type=sparql_DefaultGraphClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DefaultGraphClause", type=sparql_SourceSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sourceselector77: BinaryAssociation = BinaryAssociation(
    name="sourceselector77",
    ends={
        Property(name="sparql_SourceSelector78", type=sparql_NamedGraphClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NamedGraphClause", type=sparql_SourceSelector, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
where79: BinaryAssociation = BinaryAssociation(
    name="where79",
    ends={
        Property(name="sparql_WhereLiteral", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_WhereClause80", type=sparql_WhereLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groupgraphpattern81: BinaryAssociation = BinaryAssociation(
    name="groupgraphpattern81",
    ends={
        Property(name="sparql_GroupGraphPattern", type=sparql_WhereClause, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_WhereClause82", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
triplesnode108: BinaryAssociation = BinaryAssociation(
    name="triplesnode108",
    ends={
        Property(name="sparql_TriplesNode", type=sparql_TriplesSameSubjectRightNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubjectRightNE", type=sparql_TriplesNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
triplessamesubject92: BinaryAssociation = BinaryAssociation(
    name="triplessamesubject92",
    ends={
        Property(name="sparql_TriplesSameSubject94", type=sparql_TriplesBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesBlock93", type=sparql_TriplesSameSubject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
propertylistnotempty109: BinaryAssociation = BinaryAssociation(
    name="propertylistnotempty109",
    ends={
        Property(name="sparql_PropertyListNotEmpty111", type=sparql_TriplesSameSubjectRightNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubjectRightNE110", type=sparql_PropertyListNotEmpty, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
groupgraphpattern95: BinaryAssociation = BinaryAssociation(
    name="groupgraphpattern95",
    ends={
        Property(name="sparql_GroupGraphPattern96", type=sparql_OptionalGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_OptionalGraphPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groupgraphpattern97: BinaryAssociation = BinaryAssociation(
    name="groupgraphpattern97",
    ends={
        Property(name="sparql_GroupGraphPattern98", type=sparql_GroupOrUnionGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupOrUnionGraphPattern", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
varoririref99: BinaryAssociation = BinaryAssociation(
    name="varoririref99",
    ends={
        Property(name="sparql_VarOrIRIref100", type=sparql_GraphGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GraphGraphPattern", type=sparql_VarOrIRIref, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
groupgraphpattern101: BinaryAssociation = BinaryAssociation(
    name="groupgraphpattern101",
    ends={
        Property(name="sparql_GroupGraphPattern103", type=sparql_GraphGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GraphGraphPattern102", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraint104: BinaryAssociation = BinaryAssociation(
    name="constraint104",
    ends={
        Property(name="sparql_Constraint", type=sparql_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Filter", type=sparql_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
triplesblock83: BinaryAssociation = BinaryAssociation(
    name="triplesblock83",
    ends={
        Property(name="sparql_TriplesBlock", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupGraphPattern84", type=sparql_TriplesBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additionalGGPelements85: BinaryAssociation = BinaryAssociation(
    name="additionalGGPelements85",
    ends={
        Property(name="sparql_AdditionalGGPElement", type=sparql_GroupGraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_GroupGraphPattern86", type=sparql_AdditionalGGPElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varorterm105: BinaryAssociation = BinaryAssociation(
    name="varorterm105",
    ends={
        Property(name="sparql_VarOrTerm", type=sparql_TriplesSameSubjectLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubjectLeftNE", type=sparql_VarOrTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
patternOrFilterNE87: BinaryAssociation = BinaryAssociation(
    name="patternOrFilterNE87",
    ends={
        Property(name="sparql_PatternOrFilterNE", type=sparql_AdditionalGGPElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditionalGGPElement88", type=sparql_PatternOrFilterNE, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
propertylistnotempty106: BinaryAssociation = BinaryAssociation(
    name="propertylistnotempty106",
    ends={
        Property(name="sparql_PropertyListNotEmpty", type=sparql_TriplesSameSubjectLeftNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TriplesSameSubjectLeftNE107", type=sparql_PropertyListNotEmpty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
triplesblock89: BinaryAssociation = BinaryAssociation(
    name="triplesblock89",
    ends={
        Property(name="sparql_TriplesBlock91", type=sparql_AdditionalGGPElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditionalGGPElement90", type=sparql_TriplesBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
propertylistnotempty122: BinaryAssociation = BinaryAssociation(
    name="propertylistnotempty122",
    ends={
        Property(name="sparql_PropertyListNotEmpty123", type=sparql_BlankNodePropertyList, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BlankNodePropertyList", type=sparql_PropertyListNotEmpty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
verb112: BinaryAssociation = BinaryAssociation(
    name="verb112",
    ends={
        Property(name="sparql_Verb", type=sparql_PropertyListNotEmpty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PropertyListNotEmpty113", type=sparql_Verb, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
objectlist114: BinaryAssociation = BinaryAssociation(
    name="objectlist114",
    ends={
        Property(name="sparql_ObjectList", type=sparql_PropertyListNotEmpty, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PropertyListNotEmpty115", type=sparql_ObjectList, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
object116: BinaryAssociation = BinaryAssociation(
    name="object116",
    ends={
        Property(name="sparql_Object", type=sparql_ObjectList, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ObjectList117", type=sparql_Object, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
graphnode118: BinaryAssociation = BinaryAssociation(
    name="graphnode118",
    ends={
        Property(name="sparql_GraphNode", type=sparql_Object, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Object119", type=sparql_GraphNode, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
graphnode120: BinaryAssociation = BinaryAssociation(
    name="graphnode120",
    ends={
        Property(name="sparql_GraphNode121", type=sparql_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Collection", type=sparql_GraphNode, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression134: BinaryAssociation = BinaryAssociation(
    name="expression134",
    ends={
        Property(name="sparql_Expression135", type=sparql_DatatypeBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DatatypeBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var136: BinaryAssociation = BinaryAssociation(
    name="var136",
    ends={
        Property(name="sparql_Var137", type=sparql_BoundBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BoundBuiltInCallNE", type=sparql_Var, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression124: BinaryAssociation = BinaryAssociation(
    name="expression124",
    ends={
        Property(name="sparql_Expression", type=sparql_BrackettedExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BrackettedExpression125", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression126: BinaryAssociation = BinaryAssociation(
    name="expression126",
    ends={
        Property(name="sparql_Expression127", type=sparql_StrBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_StrBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression128: BinaryAssociation = BinaryAssociation(
    name="expression128",
    ends={
        Property(name="sparql_Expression129", type=sparql_LangBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LangBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression130: BinaryAssociation = BinaryAssociation(
    name="expression130",
    ends={
        Property(name="sparql_Expression131", type=sparql_LangmatchesBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LangmatchesBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addexpression132: BinaryAssociation = BinaryAssociation(
    name="addexpression132",
    ends={
        Property(name="sparql_AdditionalExpressionNE", type=sparql_LangmatchesBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_LangmatchesBuiltInCallNE133", type=sparql_AdditionalExpressionNE, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iriref156: BinaryAssociation = BinaryAssociation(
    name="iriref156",
    ends={
        Property(name="sparql_IRIreference", type=sparql_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_FunctionCall", type=sparql_IRIreference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression138: BinaryAssociation = BinaryAssociation(
    name="expression138",
    ends={
        Property(name="sparql_Expression139", type=sparql_SameTermBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SameTermBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addexpression140: BinaryAssociation = BinaryAssociation(
    name="addexpression140",
    ends={
        Property(name="sparql_AdditionalExpressionNE142", type=sparql_SameTermBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SameTermBuiltInCallNE141", type=sparql_AdditionalExpressionNE, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression143: BinaryAssociation = BinaryAssociation(
    name="expression143",
    ends={
        Property(name="sparql_Expression144", type=sparql_IsIRIBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IsIRIBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression145: BinaryAssociation = BinaryAssociation(
    name="expression145",
    ends={
        Property(name="sparql_Expression146", type=sparql_IsURIBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IsURIBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression147: BinaryAssociation = BinaryAssociation(
    name="expression147",
    ends={
        Property(name="sparql_Expression148", type=sparql_IsBlankBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IsBlankBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression149: BinaryAssociation = BinaryAssociation(
    name="expression149",
    ends={
        Property(name="sparql_Expression150", type=sparql_IsLiteralBuiltInCallNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IsLiteralBuiltInCallNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression151: BinaryAssociation = BinaryAssociation(
    name="expression151",
    ends={
        Property(name="sparql_Expression152", type=sparql_RegexExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RegexExpression", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addexpression153: BinaryAssociation = BinaryAssociation(
    name="addexpression153",
    ends={
        Property(name="sparql_AdditionalExpressionNE155", type=sparql_RegexExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RegexExpression154", type=sparql_AdditionalExpressionNE, multiplicity=Multiplicity(1, 2), is_composite=True)
    }
)
addexpression162: BinaryAssociation = BinaryAssociation(
    name="addexpression162",
    ends={
        Property(name="sparql_AdditionalExpressionNE164", type=sparql_ArgListExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ArgListExpressionNE163", type=sparql_AdditionalExpressionNE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arglist157: BinaryAssociation = BinaryAssociation(
    name="arglist157",
    ends={
        Property(name="sparql_ArgList", type=sparql_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_FunctionCall158", type=sparql_ArgList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalorexpression165: BinaryAssociation = BinaryAssociation(
    name="conditionalorexpression165",
    ends={
        Property(name="sparql_ConditionalOrExpression", type=sparql_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_Expression166", type=sparql_ConditionalOrExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nil159: BinaryAssociation = BinaryAssociation(
    name="nil159",
    ends={
        Property(name="sparql_NotInList", type=sparql_ArgListNILNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ArgListNILNE", type=sparql_NotInList, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="sparql_Expression161", type=sparql_ArgListExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ArgListExpressionNE", type=sparql_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalandexpression174: BinaryAssociation = BinaryAssociation(
    name="conditionalandexpression174",
    ends={
        Property(name="sparql_ConditionalAndExpression176", type=sparql_AdditionalConditionalAndExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditionalConditionalAndExpressionNE175", type=sparql_ConditionalAndExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalorexpression167: BinaryAssociation = BinaryAssociation(
    name="conditionalorexpression167",
    ends={
        Property(name="sparql_ConditionalOrExpression169", type=sparql_AdditionalExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditionalExpressionNE168", type=sparql_ConditionalOrExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionalandexpression170: BinaryAssociation = BinaryAssociation(
    name="conditionalandexpression170",
    ends={
        Property(name="sparql_ConditionalAndExpression", type=sparql_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConditionalOrExpression171", type=sparql_ConditionalAndExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addconditionalandexpression172: BinaryAssociation = BinaryAssociation(
    name="addconditionalandexpression172",
    ends={
        Property(name="sparql_AdditionalConditionalAndExpressionNE", type=sparql_ConditionalOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConditionalOrExpression173", type=sparql_AdditionalConditionalAndExpressionNE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addnumericexpression188: BinaryAssociation = BinaryAssociation(
    name="addnumericexpression188",
    ends={
        Property(name="sparql_AdditionalNumericExpressionNE", type=sparql_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RelationalExpression189", type=sparql_AdditionalNumericExpressionNE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
additiveexpression190: BinaryAssociation = BinaryAssociation(
    name="additiveexpression190",
    ends={
        Property(name="sparql_AdditiveExpression", type=sparql_NumericExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NumericExpression191", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additiveexpression192: BinaryAssociation = BinaryAssociation(
    name="additiveexpression192",
    ends={
        Property(name="sparql_AdditiveExpression193", type=sparql_EqualsNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_EqualsNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
valuelogical177: BinaryAssociation = BinaryAssociation(
    name="valuelogical177",
    ends={
        Property(name="sparql_ValueLogical", type=sparql_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConditionalAndExpression178", type=sparql_ValueLogical, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addvaluelogical179: BinaryAssociation = BinaryAssociation(
    name="addvaluelogical179",
    ends={
        Property(name="sparql_AdditionalValueLogicalNE", type=sparql_ConditionalAndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ConditionalAndExpression180", type=sparql_AdditionalValueLogicalNE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationalexpression181: BinaryAssociation = BinaryAssociation(
    name="relationalexpression181",
    ends={
        Property(name="sparql_RelationalExpression", type=sparql_ValueLogical, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ValueLogical182", type=sparql_RelationalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relationalexpression183: BinaryAssociation = BinaryAssociation(
    name="relationalexpression183",
    ends={
        Property(name="sparql_RelationalExpression185", type=sparql_AdditionalValueLogicalNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditionalValueLogicalNE184", type=sparql_RelationalExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numericexpression186: BinaryAssociation = BinaryAssociation(
    name="numericexpression186",
    ends={
        Property(name="sparql_NumericExpression", type=sparql_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RelationalExpression187", type=sparql_NumericExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiplicativeexpression204: BinaryAssociation = BinaryAssociation(
    name="multiplicativeexpression204",
    ends={
        Property(name="sparql_MultiplicativeExpression", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditiveExpression205", type=sparql_MultiplicativeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addmultiplicativeexpression206: BinaryAssociation = BinaryAssociation(
    name="addmultiplicativeexpression206",
    ends={
        Property(name="sparql_AdditionalMultiplicativeExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_AdditiveExpression207", type=sparql_AdditionalMultiplicativeExpressionNE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unaryexpression208: BinaryAssociation = BinaryAssociation(
    name="unaryexpression208",
    ends={
        Property(name="sparql_UnaryExpression", type=sparql_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MultiplicativeExpression209", type=sparql_UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
addunaryexpression210: BinaryAssociation = BinaryAssociation(
    name="addunaryexpression210",
    ends={
        Property(name="sparql_AdditionalUnaryExpressionNE", type=sparql_MultiplicativeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MultiplicativeExpression211", type=sparql_AdditionalUnaryExpressionNE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additiveexpression194: BinaryAssociation = BinaryAssociation(
    name="additiveexpression194",
    ends={
        Property(name="sparql_AdditiveExpression195", type=sparql_NotEqualNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NotEqualNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additiveexpression196: BinaryAssociation = BinaryAssociation(
    name="additiveexpression196",
    ends={
        Property(name="sparql_AdditiveExpression197", type=sparql_SmallerNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SmallerNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additiveexpression198: BinaryAssociation = BinaryAssociation(
    name="additiveexpression198",
    ends={
        Property(name="sparql_AdditiveExpression199", type=sparql_BiggerNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BiggerNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additiveexpression200: BinaryAssociation = BinaryAssociation(
    name="additiveexpression200",
    ends={
        Property(name="sparql_AdditiveExpression201", type=sparql_SmallerOrEqualNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_SmallerOrEqualNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
additiveexpression202: BinaryAssociation = BinaryAssociation(
    name="additiveexpression202",
    ends={
        Property(name="sparql_AdditiveExpression203", type=sparql_BiggerOrEqualNumericExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_BiggerOrEqualNumericExpressionNE", type=sparql_AdditiveExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryexpression218: BinaryAssociation = BinaryAssociation(
    name="unaryexpression218",
    ends={
        Property(name="sparql_UnaryExpression219", type=sparql_DividedByAdditionalUnaryExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_DividedByAdditionalUnaryExpressionNE", type=sparql_UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
primaryexpression220: BinaryAssociation = BinaryAssociation(
    name="primaryexpression220",
    ends={
        Property(name="sparql_PrimaryExpression", type=sparql_NotPrimaryExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NotPrimaryExpressionNE", type=sparql_PrimaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
primaryexpression221: BinaryAssociation = BinaryAssociation(
    name="primaryexpression221",
    ends={
        Property(name="sparql_PrimaryExpression222", type=sparql_PlusPrimaryExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PlusPrimaryExpressionNE", type=sparql_PrimaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiplicativeexpression212: BinaryAssociation = BinaryAssociation(
    name="multiplicativeexpression212",
    ends={
        Property(name="sparql_MultiplicativeExpression213", type=sparql_PlusMultiplicativeExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PlusMultiplicativeExpressionNE", type=sparql_MultiplicativeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiplicativeexpression214: BinaryAssociation = BinaryAssociation(
    name="multiplicativeexpression214",
    ends={
        Property(name="sparql_MultiplicativeExpression215", type=sparql_MinusMultiplicativeExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MinusMultiplicativeExpressionNE", type=sparql_MultiplicativeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryexpression216: BinaryAssociation = BinaryAssociation(
    name="unaryexpression216",
    ends={
        Property(name="sparql_UnaryExpression217", type=sparql_TimesAdditionalUnaryExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_TimesAdditionalUnaryExpressionNE", type=sparql_UnaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iriref233: BinaryAssociation = BinaryAssociation(
    name="iriref233",
    ends={
        Property(name="sparql_IRIreference234", type=sparql_UpIRIrefNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_UpIRIrefNE", type=sparql_IRIreference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
primaryexpression223: BinaryAssociation = BinaryAssociation(
    name="primaryexpression223",
    ends={
        Property(name="sparql_PrimaryExpression224", type=sparql_MinusPrimaryExpressionNE, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_MinusPrimaryExpressionNE", type=sparql_PrimaryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iriref225: BinaryAssociation = BinaryAssociation(
    name="iriref225",
    ends={
        Property(name="sparql_IRIreference226", type=sparql_IRIrefOrFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IRIrefOrFunction", type=sparql_IRIreference, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arglist227: BinaryAssociation = BinaryAssociation(
    name="arglist227",
    ends={
        Property(name="sparql_ArgList229", type=sparql_IRIrefOrFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_IRIrefOrFunction228", type=sparql_ArgList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
string230: BinaryAssociation = BinaryAssociation(
    name="string230",
    ends={
        Property(name="sparql_StringLiteral", type=sparql_RDFLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RDFLiteral", type=sparql_StringLiteral, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
langtagoririrefNE231: BinaryAssociation = BinaryAssociation(
    name="langtagoririrefNE231",
    ends={
        Property(name="sparql_LANGTAGOrIRIrefNE", type=sparql_RDFLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_RDFLiteral232", type=sparql_LANGTAGOrIRIrefNE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pn_local238: BinaryAssociation = BinaryAssociation(
    name="pn_local238",
    ends={
        Property(name="sparql_PN_LOCAL", type=sparql_PNAME_LN, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_PNAME_LN", type=sparql_PN_LOCAL, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ws239: BinaryAssociation = BinaryAssociation(
    name="ws239",
    ends={
        Property(name="sparql_WS", type=sparql_NotInList, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_NotInList240", type=sparql_WS, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name235: BinaryAssociation = BinaryAssociation(
    name="name235",
    ends={
        Property(name="sparql_VARNAME", type=sparql_VAR1, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_VAR1", type=sparql_VARNAME, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
name236: BinaryAssociation = BinaryAssociation(
    name="name236",
    ends={
        Property(name="sparql_VARNAME237", type=sparql_VAR2, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_VAR2", type=sparql_VARNAME, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ws241: BinaryAssociation = BinaryAssociation(
    name="ws241",
    ends={
        Property(name="sparql_WS242", type=sparql_ANON, multiplicity=Multiplicity(1, 1)),
        Property(name="sparql_ANON", type=sparql_WS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_sparql_SparqlQueries_LocatedElement = Generalization(general=LocatedElement, specific=sparql_SparqlQueries)
gen_sparql_Prologue_LocatedElement = Generalization(general=LocatedElement, specific=sparql_Prologue)
gen_sparql_BaseDecl_LocatedElement = Generalization(general=LocatedElement, specific=sparql_BaseDecl)
gen_sparql_PrefixDecl_LocatedElement = Generalization(general=LocatedElement, specific=sparql_PrefixDecl)
gen_sparql_Query_LocatedElement = Generalization(general=LocatedElement, specific=sparql_Query)
gen_sparql_SelectQuery_Query = Generalization(general=Query, specific=sparql_SelectQuery)
gen_sparql_DescribeQuery_Query = Generalization(general=Query, specific=sparql_DescribeQuery)
gen_sparql_AskQuery_Query = Generalization(general=Query, specific=sparql_AskQuery)
gen_sparql_ConstructQuery_Query = Generalization(general=Query, specific=sparql_ConstructQuery)
gen_sparql_OrderClause_LocatedElement = Generalization(general=LocatedElement, specific=sparql_OrderClause)
gen_sparql_OrderCondition_LocatedElement = Generalization(general=LocatedElement, specific=sparql_OrderCondition)
gen_sparql_OrderConditionLeftNE_OrderCondition = Generalization(general=OrderCondition, specific=sparql_OrderConditionLeftNE)
gen_sparql_OrderConditionRightNE_OrderCondition = Generalization(general=OrderCondition, specific=sparql_OrderConditionRightNE)
gen_sparql_LimitOffsetClauses_LocatedElement = Generalization(general=LocatedElement, specific=sparql_LimitOffsetClauses)
gen_sparql_LimitOffsetClausesLeftNE_LimitOffsetClauses = Generalization(general=LimitOffsetClauses, specific=sparql_LimitOffsetClausesLeftNE)
gen_sparql_ConstructTemplate_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ConstructTemplate)
gen_sparql_SolutionModifier_LocatedElement = Generalization(general=LocatedElement, specific=sparql_SolutionModifier)
gen_sparql_OffsetClause_LocatedElement = Generalization(general=LocatedElement, specific=sparql_OffsetClause)
gen_sparql_SolutionsDisplayNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_SolutionsDisplayNE)
gen_sparql_DistinctNE_SolutionsDisplayNE = Generalization(general=SolutionsDisplayNE, specific=sparql_DistinctNE)
gen_sparql_ReducedNE_SolutionsDisplayNE = Generalization(general=SolutionsDisplayNE, specific=sparql_ReducedNE)
gen_sparql_VariablesNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_VariablesNE)
gen_sparql_AllVariablesNE_VariablesNE = Generalization(general=VariablesNE, specific=sparql_AllVariablesNE)
gen_sparql_SomeVariablesNE_VariablesNE = Generalization(general=VariablesNE, specific=sparql_SomeVariablesNE)
gen_sparql_VarOrIRIref_Verb = Generalization(general=Verb, specific=sparql_VarOrIRIref)
gen_sparql_Var_VarOrIRIref = Generalization(general=VarOrIRIref, specific=sparql_Var)
gen_sparql_Var_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_Var)
gen_sparql_Var_VarOrTerm = Generalization(general=VarOrTerm, specific=sparql_Var)
gen_sparql_Var_OrderConditionRightNE = Generalization(general=OrderConditionRightNE, specific=sparql_Var)
gen_sparql_LimitOffsetClausesRightNE_LimitOffsetClauses = Generalization(general=LimitOffsetClauses, specific=sparql_LimitOffsetClausesRightNE)
gen_sparql_LimitClause_LocatedElement = Generalization(general=LocatedElement, specific=sparql_LimitClause)
gen_sparql_GraphClauseNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_GraphClauseNE)
gen_sparql_DefaultGraphClause_GraphClauseNE = Generalization(general=GraphClauseNE, specific=sparql_DefaultGraphClause)
gen_sparql_NamedGraphClause_GraphClauseNE = Generalization(general=GraphClauseNE, specific=sparql_NamedGraphClause)
gen_sparql_SourceSelector_LocatedElement = Generalization(general=LocatedElement, specific=sparql_SourceSelector)
gen_sparql_WhereClause_LocatedElement = Generalization(general=LocatedElement, specific=sparql_WhereClause)
gen_sparql_GroupGraphPattern_LocatedElement = Generalization(general=LocatedElement, specific=sparql_GroupGraphPattern)
gen_sparql_IRIreference_VarOrIRIref = Generalization(general=VarOrIRIref, specific=sparql_IRIreference)
gen_sparql_IRIreference_GraphTerm = Generalization(general=GraphTerm, specific=sparql_IRIreference)
gen_sparql_IRIreference_SourceSelector = Generalization(general=SourceSelector, specific=sparql_IRIreference)
gen_sparql_PrefixedName_IRIreference = Generalization(general=IRIreference, specific=sparql_PrefixedName)
gen_sparql_DatasetClause_LocatedElement = Generalization(general=LocatedElement, specific=sparql_DatasetClause)
gen_sparql_TriplesSameSubjectRightNE_TriplesSameSubject = Generalization(general=TriplesSameSubject, specific=sparql_TriplesSameSubjectRightNE)
gen_sparql_GraphPatternNotTriples_PatternOrFilterNE = Generalization(general=PatternOrFilterNE, specific=sparql_GraphPatternNotTriples)
gen_sparql_OptionalGraphPattern_GraphPatternNotTriples = Generalization(general=GraphPatternNotTriples, specific=sparql_OptionalGraphPattern)
gen_sparql_GroupOrUnionGraphPattern_GraphPatternNotTriples = Generalization(general=GraphPatternNotTriples, specific=sparql_GroupOrUnionGraphPattern)
gen_sparql_GraphGraphPattern_GraphPatternNotTriples = Generalization(general=GraphPatternNotTriples, specific=sparql_GraphGraphPattern)
gen_sparql_Filter_PatternOrFilterNE = Generalization(general=PatternOrFilterNE, specific=sparql_Filter)
gen_sparql_TriplesSameSubject_LocatedElement = Generalization(general=LocatedElement, specific=sparql_TriplesSameSubject)
gen_sparql_TriplesSameSubjectLeftNE_TriplesSameSubject = Generalization(general=TriplesSameSubject, specific=sparql_TriplesSameSubjectLeftNE)
gen_sparql_AdditionalGGPElement_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalGGPElement)
gen_sparql_BlankNodePropertyList_TriplesNode = Generalization(general=TriplesNode, specific=sparql_BlankNodePropertyList)
gen_sparql_VarOrTerm_GraphNode = Generalization(general=GraphNode, specific=sparql_VarOrTerm)
gen_sparql_PropertyListNotEmpty_LocatedElement = Generalization(general=LocatedElement, specific=sparql_PropertyListNotEmpty)
gen_sparql_Verb_LocatedElement = Generalization(general=LocatedElement, specific=sparql_Verb)
gen_sparql_VerbANE_Verb = Generalization(general=Verb, specific=sparql_VerbANE)
gen_sparql_ObjectList_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ObjectList)
gen_sparql_Object_LocatedElement = Generalization(general=LocatedElement, specific=sparql_Object)
gen_sparql_GraphNode_LocatedElement = Generalization(general=LocatedElement, specific=sparql_GraphNode)
gen_sparql_TriplesNode_GraphNode = Generalization(general=GraphNode, specific=sparql_TriplesNode)
gen_sparql_Collection_TriplesNode = Generalization(general=TriplesNode, specific=sparql_Collection)
gen_sparql_BoundBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_BoundBuiltInCallNE)
gen_sparql_SameTermBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_SameTermBuiltInCallNE)
gen_sparql_GraphTerm_VarOrTerm = Generalization(general=VarOrTerm, specific=sparql_GraphTerm)
gen_sparql_BlankNode_GraphTerm = Generalization(general=GraphTerm, specific=sparql_BlankNode)
gen_sparql_Constraint_OrderConditionRightNE = Generalization(general=OrderConditionRightNE, specific=sparql_Constraint)
gen_sparql_BrackettedExpression_Constraint = Generalization(general=Constraint, specific=sparql_BrackettedExpression)
gen_sparql_BrackettedExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_BrackettedExpression)
gen_sparql_BuiltInCall_Constraint = Generalization(general=Constraint, specific=sparql_BuiltInCall)
gen_sparql_BuiltInCall_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_BuiltInCall)
gen_sparql_StrBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_StrBuiltInCallNE)
gen_sparql_LangBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_LangBuiltInCallNE)
gen_sparql_LangmatchesBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_LangmatchesBuiltInCallNE)
gen_sparql_DatatypeBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_DatatypeBuiltInCallNE)
gen_sparql_FunctionCall_Constraint = Generalization(general=Constraint, specific=sparql_FunctionCall)
gen_sparql_IsIRIBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_IsIRIBuiltInCallNE)
gen_sparql_IsURIBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_IsURIBuiltInCallNE)
gen_sparql_IsBlankBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_IsBlankBuiltInCallNE)
gen_sparql_IsLiteralBuiltInCallNE_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_IsLiteralBuiltInCallNE)
gen_sparql_RegexExpression_BuiltInCall = Generalization(general=BuiltInCall, specific=sparql_RegexExpression)
gen_sparql_Expression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_Expression)
gen_sparql_ArgList_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ArgList)
gen_sparql_ArgListNILNE_ArgList = Generalization(general=ArgList, specific=sparql_ArgListNILNE)
gen_sparql_ArgListExpressionNE_ArgList = Generalization(general=ArgList, specific=sparql_ArgListExpressionNE)
gen_sparql_ConditionalAndExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ConditionalAndExpression)
gen_sparql_AdditionalExpressionNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalExpressionNE)
gen_sparql_ConditionalOrExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ConditionalOrExpression)
gen_sparql_AdditionalConditionalAndExpressionNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalConditionalAndExpressionNE)
gen_sparql_NumericExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_NumericExpression)
gen_sparql_AdditionalNumericExpressionNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalNumericExpressionNE)
gen_sparql_EqualsNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_EqualsNumericExpressionNE)
gen_sparql_ValueLogical_LocatedElement = Generalization(general=LocatedElement, specific=sparql_ValueLogical)
gen_sparql_AdditionalValueLogicalNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalValueLogicalNE)
gen_sparql_RelationalExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_RelationalExpression)
gen_sparql_MultiplicativeExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_MultiplicativeExpression)
gen_sparql_NotEqualNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_NotEqualNumericExpressionNE)
gen_sparql_SmallerNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_SmallerNumericExpressionNE)
gen_sparql_BiggerNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_BiggerNumericExpressionNE)
gen_sparql_SmallerOrEqualNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_SmallerOrEqualNumericExpressionNE)
gen_sparql_BiggerOrEqualNumericExpressionNE_AdditionalNumericExpressionNE = Generalization(general=AdditionalNumericExpressionNE, specific=sparql_BiggerOrEqualNumericExpressionNE)
gen_sparql_AdditiveExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditiveExpression)
gen_sparql_DividedByAdditionalUnaryExpressionNE_AdditionalUnaryExpressionNE = Generalization(general=AdditionalUnaryExpressionNE, specific=sparql_DividedByAdditionalUnaryExpressionNE)
gen_sparql_NotPrimaryExpressionNE_UnaryExpression = Generalization(general=UnaryExpression, specific=sparql_NotPrimaryExpressionNE)
gen_sparql_PlusPrimaryExpressionNE_UnaryExpression = Generalization(general=UnaryExpression, specific=sparql_PlusPrimaryExpressionNE)
gen_sparql_AdditionalMultiplicativeExpressionNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalMultiplicativeExpressionNE)
gen_sparql_PlusMultiplicativeExpressionNE_AdditionalMultiplicativeExpressionNE = Generalization(general=AdditionalMultiplicativeExpressionNE, specific=sparql_PlusMultiplicativeExpressionNE)
gen_sparql_MinusMultiplicativeExpressionNE_AdditionalMultiplicativeExpressionNE = Generalization(general=AdditionalMultiplicativeExpressionNE, specific=sparql_MinusMultiplicativeExpressionNE)
gen_sparql_NumericLiteralPositive_AdditionalMultiplicativeExpressionNE = Generalization(general=AdditionalMultiplicativeExpressionNE, specific=sparql_NumericLiteralPositive)
gen_sparql_NumericLiteralPositive_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_NumericLiteralPositive)
gen_sparql_NumericLiteralNegative_AdditionalMultiplicativeExpressionNE = Generalization(general=AdditionalMultiplicativeExpressionNE, specific=sparql_NumericLiteralNegative)
gen_sparql_NumericLiteralNegative_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_NumericLiteralNegative)
gen_sparql_UnaryExpression_LocatedElement = Generalization(general=LocatedElement, specific=sparql_UnaryExpression)
gen_sparql_AdditionalUnaryExpressionNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_AdditionalUnaryExpressionNE)
gen_sparql_TimesAdditionalUnaryExpressionNE_AdditionalUnaryExpressionNE = Generalization(general=AdditionalUnaryExpressionNE, specific=sparql_TimesAdditionalUnaryExpressionNE)
gen_sparql_LANGTAGOrIRIrefNE_LocatedElement = Generalization(general=LocatedElement, specific=sparql_LANGTAGOrIRIrefNE)
gen_sparql_UpIRIrefNE_LANGTAGOrIRIrefNE = Generalization(general=LANGTAGOrIRIrefNE, specific=sparql_UpIRIrefNE)
gen_sparql_NumericLiteral_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_NumericLiteral)
gen_sparql_NumericLiteral_GraphTerm = Generalization(general=GraphTerm, specific=sparql_NumericLiteral)
gen_sparql_NumericLiteral_AdditionalMultiplicativeExpressionNE = Generalization(general=AdditionalMultiplicativeExpressionNE, specific=sparql_NumericLiteral)
gen_sparql_NumericLiteralUnsigned_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_NumericLiteralUnsigned)
gen_sparql_MinusPrimaryExpressionNE_UnaryExpression = Generalization(general=UnaryExpression, specific=sparql_MinusPrimaryExpressionNE)
gen_sparql_PrimaryExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=sparql_PrimaryExpression)
gen_sparql_IRIrefOrFunction_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_IRIrefOrFunction)
gen_sparql_RDFLiteral_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_RDFLiteral)
gen_sparql_RDFLiteral_GraphTerm = Generalization(general=GraphTerm, specific=sparql_RDFLiteral)
gen_sparql_PNAME_NS_PrefixedName = Generalization(general=PrefixedName, specific=sparql_PNAME_NS)
gen_sparql_PNAME_NS_VarOrIRIref = Generalization(general=VarOrIRIref, specific=sparql_PNAME_NS)
gen_sparql_PNAME_LN_PrefixedName = Generalization(general=PrefixedName, specific=sparql_PNAME_LN)
gen_sparql_PNAME_LN_VarOrIRIref = Generalization(general=VarOrIRIref, specific=sparql_PNAME_LN)
gen_sparql_NotInList_GraphTerm = Generalization(general=GraphTerm, specific=sparql_NotInList)
gen_sparql_BooleanLiteral_PrimaryExpression = Generalization(general=PrimaryExpression, specific=sparql_BooleanLiteral)
gen_sparql_BooleanLiteral_GraphTerm = Generalization(general=GraphTerm, specific=sparql_BooleanLiteral)
gen_sparql_TrueBooleanLiteralNE_BooleanLiteral = Generalization(general=BooleanLiteral, specific=sparql_TrueBooleanLiteralNE)
gen_sparql_FalseBooleanLiteralNE_BooleanLiteral = Generalization(general=BooleanLiteral, specific=sparql_FalseBooleanLiteralNE)
gen_sparql_VARNAME_LocatedElement = Generalization(general=LocatedElement, specific=sparql_VARNAME)
gen_sparql_IRI_REF_IRIreference = Generalization(general=IRIreference, specific=sparql_IRI_REF)
gen_sparql_IRI_REF_VarOrIRIref = Generalization(general=VarOrIRIref, specific=sparql_IRI_REF)
gen_sparql_STRING_LITERAL1_StringLiteral = Generalization(general=StringLiteral, specific=sparql_STRING_LITERAL1)
gen_sparql_STRING_LITERAL2_StringLiteral = Generalization(general=StringLiteral, specific=sparql_STRING_LITERAL2)
gen_sparql_INTEGER_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_INTEGER)
gen_sparql_DECIMAL_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_DECIMAL)
gen_sparql_DOUBLE_NumericLiteral = Generalization(general=NumericLiteral, specific=sparql_DOUBLE)
gen_sparql_WS_LocatedElement = Generalization(general=LocatedElement, specific=sparql_WS)
gen_sparql_AscendingLiteral_AscOrDecs = Generalization(general=AscOrDecs, specific=sparql_AscendingLiteral)
gen_sparql_DescendingLiteral_AscOrDecs = Generalization(general=AscOrDecs, specific=sparql_DescendingLiteral)
gen_sparql_STRING_LITERAL_LONG1_StringLiteral = Generalization(general=StringLiteral, specific=sparql_STRING_LITERAL_LONG1)
gen_sparql_STRING_LITERAL_LONG2_StringLiteral = Generalization(general=StringLiteral, specific=sparql_STRING_LITERAL_LONG2)
gen_sparql_BLANK_NODE_LABEL_BlankNode = Generalization(general=BlankNode, specific=sparql_BLANK_NODE_LABEL)
gen_sparql_ANON_BlankNode = Generalization(general=BlankNode, specific=sparql_ANON)
gen_sparql_LANGTAG_LANGTAGOrIRIrefNE = Generalization(general=LANGTAGOrIRIrefNE, specific=sparql_LANGTAG)
gen_sparql_PN_PREFIX_LocatedElement = Generalization(general=LocatedElement, specific=sparql_PN_PREFIX)
gen_sparql_PN_LOCAL_LocatedElement = Generalization(general=LocatedElement, specific=sparql_PN_LOCAL)

# Domain Model
domain_model = DomainModel(
    name="sparql",
    types={sparql_SparqlQueries, LocatedElement, sparql_Prologue, sparql_Query, sparql_BaseDecl, sparql_PrefixDecl, sparql_IRI_REF, sparql_LocatedElement, sparql_Var, sparql_DatasetClause, sparql_WhereClause, sparql_PNAME_NS, sparql_SelectQuery, Query, sparql_SolutionsDisplayNE, sparql_DescribeQuery, sparql_VarOrIRIref, sparql_AskQuery, sparql_SolutionModifier, sparql_ConstructQuery, sparql_ConstructTemplate, sparql_LimitOffsetClauses, sparql_OrderCondition, sparql_OrderConditionLeftNE, OrderCondition, sparql_AscOrDecs, sparql_BrackettedExpression, sparql_OrderConditionRightNE, sparql_LimitOffsetClausesLeftNE, LimitOffsetClauses, sparql_LimitClause, sparql_OffsetClause, sparql_TriplesSameSubject, sparql_OrderClause, sparql_INTEGER, sparql_DistinctNE, SolutionsDisplayNE, sparql_ReducedNE, sparql_VariablesNE, sparql_AllVariablesNE, VariablesNE, sparql_SomeVariablesNE, Verb, VarOrIRIref, PrimaryExpression, VarOrTerm, OrderConditionRightNE, sparql_LimitOffsetClausesRightNE, sparql_GraphClauseNE, sparql_DefaultGraphClause, GraphClauseNE, sparql_SourceSelector, sparql_NamedGraphClause, sparql_WhereLiteral, sparql_GroupGraphPattern, sparql_IRIreference, GraphTerm, SourceSelector, sparql_PrefixedName, IRIreference, sparql_TriplesSameSubjectRightNE, sparql_TriplesNode, sparql_GraphPatternNotTriples, PatternOrFilterNE, sparql_OptionalGraphPattern, GraphPatternNotTriples, sparql_GroupOrUnionGraphPattern, sparql_GraphGraphPattern, sparql_Filter, sparql_Constraint, sparql_TriplesBlock, sparql_AdditionalGGPElement, sparql_TriplesSameSubjectLeftNE, TriplesSameSubject, sparql_VarOrTerm, sparql_PatternOrFilterNE, sparql_PropertyListNotEmpty, GraphNode, sparql_Verb, sparql_ObjectList, sparql_VerbANE, sparql_Object, sparql_GraphNode, sparql_Collection, TriplesNode, sparql_BlankNodePropertyList, sparql_BoundBuiltInCallNE, sparql_SameTermBuiltInCallNE, sparql_GraphTerm, sparql_BlankNode, Constraint, sparql_Expression, sparql_BuiltInCall, sparql_StrBuiltInCallNE, BuiltInCall, sparql_LangBuiltInCallNE, sparql_LangmatchesBuiltInCallNE, sparql_AdditionalExpressionNE, sparql_DatatypeBuiltInCallNE, sparql_FunctionCall, sparql_ArgList, sparql_IsIRIBuiltInCallNE, sparql_IsURIBuiltInCallNE, sparql_IsBlankBuiltInCallNE, sparql_IsLiteralBuiltInCallNE, sparql_RegexExpression, sparql_ConditionalOrExpression, sparql_ArgListNILNE, ArgList, sparql_NotInList, sparql_ArgListExpressionNE, sparql_ValueLogical, sparql_ConditionalAndExpression, sparql_AdditionalConditionalAndExpressionNE, sparql_AdditionalNumericExpressionNE, sparql_AdditiveExpression, sparql_EqualsNumericExpressionNE, AdditionalNumericExpressionNE, sparql_AdditionalValueLogicalNE, sparql_RelationalExpression, sparql_NumericExpression, sparql_MultiplicativeExpression, sparql_AdditionalMultiplicativeExpressionNE, sparql_UnaryExpression, sparql_AdditionalUnaryExpressionNE, sparql_NotEqualNumericExpressionNE, sparql_SmallerNumericExpressionNE, sparql_BiggerNumericExpressionNE, sparql_SmallerOrEqualNumericExpressionNE, sparql_BiggerOrEqualNumericExpressionNE, sparql_DividedByAdditionalUnaryExpressionNE, sparql_NotPrimaryExpressionNE, UnaryExpression, sparql_PrimaryExpression, sparql_PlusPrimaryExpressionNE, sparql_PlusMultiplicativeExpressionNE, AdditionalMultiplicativeExpressionNE, sparql_MinusMultiplicativeExpressionNE, sparql_NumericLiteralPositive, NumericLiteral, sparql_NumericLiteralNegative, sparql_TimesAdditionalUnaryExpressionNE, AdditionalUnaryExpressionNE, sparql_UpIRIrefNE, LANGTAGOrIRIrefNE, sparql_NumericLiteral, sparql_NumericLiteralUnsigned, sparql_MinusPrimaryExpressionNE, sparql_IRIrefOrFunction, sparql_RDFLiteral, sparql_StringLiteral, sparql_LANGTAGOrIRIrefNE, PrefixedName, sparql_PNAME_LN, sparql_PN_LOCAL, sparql_WS, sparql_BooleanLiteral, sparql_TrueBooleanLiteralNE, BooleanLiteral, sparql_FalseBooleanLiteralNE, sparql_VAR1, sparql_VARNAME, sparql_VAR2, sparql_STRING_LITERAL1, StringLiteral, sparql_STRING_LITERAL2, sparql_DECIMAL, sparql_DOUBLE, sparql_AscendingLiteral, AscOrDecs, sparql_DescendingLiteral, sparql_STRING_LITERAL_LONG1, sparql_STRING_LITERAL_LONG2, sparql_BLANK_NODE_LABEL, BlankNode, sparql_ANON, sparql_LANGTAG, sparql_PN_PREFIX},
    associations={prologue0, query1, basedeclaration3, prefixdeclaration5, iriref7, solutionsdisplay14, var15, datasetclause17, whereclause19, pnamens9, iriref11, whereclause27, solutionmodifier30, varoririref33, datasetclause34, whereclause37, solutionmodifier40, datasetclause43, solutionmodifier21, constructtemplate23, datasetclause24, limitoffsetclauses52, ordercondition54, ascOrDecs56, brackettedexpression57, limitclause59, whereclause45, constructtriples48, orderclause50, integer67, integer69, variables72, offsetclause60, offsetclause62, limitclause64, graphclause74, sourceselector76, sourceselector77, where79, groupgraphpattern81, triplesnode108, triplessamesubject92, propertylistnotempty109, groupgraphpattern95, groupgraphpattern97, varoririref99, groupgraphpattern101, constraint104, triplesblock83, additionalGGPelements85, varorterm105, patternOrFilterNE87, propertylistnotempty106, triplesblock89, propertylistnotempty122, verb112, objectlist114, object116, graphnode118, graphnode120, expression134, var136, expression124, expression126, expression128, expression130, addexpression132, iriref156, expression138, addexpression140, expression143, expression145, expression147, expression149, expression151, addexpression153, addexpression162, arglist157, conditionalorexpression165, nil159, expression160, conditionalandexpression174, conditionalorexpression167, conditionalandexpression170, addconditionalandexpression172, addnumericexpression188, additiveexpression190, additiveexpression192, valuelogical177, addvaluelogical179, relationalexpression181, relationalexpression183, numericexpression186, multiplicativeexpression204, addmultiplicativeexpression206, unaryexpression208, addunaryexpression210, additiveexpression194, additiveexpression196, additiveexpression198, additiveexpression200, additiveexpression202, unaryexpression218, primaryexpression220, primaryexpression221, multiplicativeexpression212, multiplicativeexpression214, unaryexpression216, iriref233, primaryexpression223, iriref225, arglist227, string230, langtagoririrefNE231, pn_local238, ws239, name235, name236, ws241},
    generalizations={gen_sparql_SparqlQueries_LocatedElement, gen_sparql_Prologue_LocatedElement, gen_sparql_BaseDecl_LocatedElement, gen_sparql_PrefixDecl_LocatedElement, gen_sparql_Query_LocatedElement, gen_sparql_SelectQuery_Query, gen_sparql_DescribeQuery_Query, gen_sparql_AskQuery_Query, gen_sparql_ConstructQuery_Query, gen_sparql_OrderClause_LocatedElement, gen_sparql_OrderCondition_LocatedElement, gen_sparql_OrderConditionLeftNE_OrderCondition, gen_sparql_OrderConditionRightNE_OrderCondition, gen_sparql_LimitOffsetClauses_LocatedElement, gen_sparql_LimitOffsetClausesLeftNE_LimitOffsetClauses, gen_sparql_ConstructTemplate_LocatedElement, gen_sparql_SolutionModifier_LocatedElement, gen_sparql_OffsetClause_LocatedElement, gen_sparql_SolutionsDisplayNE_LocatedElement, gen_sparql_DistinctNE_SolutionsDisplayNE, gen_sparql_ReducedNE_SolutionsDisplayNE, gen_sparql_VariablesNE_LocatedElement, gen_sparql_AllVariablesNE_VariablesNE, gen_sparql_SomeVariablesNE_VariablesNE, gen_sparql_VarOrIRIref_Verb, gen_sparql_Var_VarOrIRIref, gen_sparql_Var_PrimaryExpression, gen_sparql_Var_VarOrTerm, gen_sparql_Var_OrderConditionRightNE, gen_sparql_LimitOffsetClausesRightNE_LimitOffsetClauses, gen_sparql_LimitClause_LocatedElement, gen_sparql_GraphClauseNE_LocatedElement, gen_sparql_DefaultGraphClause_GraphClauseNE, gen_sparql_NamedGraphClause_GraphClauseNE, gen_sparql_SourceSelector_LocatedElement, gen_sparql_WhereClause_LocatedElement, gen_sparql_GroupGraphPattern_LocatedElement, gen_sparql_IRIreference_VarOrIRIref, gen_sparql_IRIreference_GraphTerm, gen_sparql_IRIreference_SourceSelector, gen_sparql_PrefixedName_IRIreference, gen_sparql_DatasetClause_LocatedElement, gen_sparql_TriplesSameSubjectRightNE_TriplesSameSubject, gen_sparql_GraphPatternNotTriples_PatternOrFilterNE, gen_sparql_OptionalGraphPattern_GraphPatternNotTriples, gen_sparql_GroupOrUnionGraphPattern_GraphPatternNotTriples, gen_sparql_GraphGraphPattern_GraphPatternNotTriples, gen_sparql_Filter_PatternOrFilterNE, gen_sparql_TriplesSameSubject_LocatedElement, gen_sparql_TriplesSameSubjectLeftNE_TriplesSameSubject, gen_sparql_AdditionalGGPElement_LocatedElement, gen_sparql_BlankNodePropertyList_TriplesNode, gen_sparql_VarOrTerm_GraphNode, gen_sparql_PropertyListNotEmpty_LocatedElement, gen_sparql_Verb_LocatedElement, gen_sparql_VerbANE_Verb, gen_sparql_ObjectList_LocatedElement, gen_sparql_Object_LocatedElement, gen_sparql_GraphNode_LocatedElement, gen_sparql_TriplesNode_GraphNode, gen_sparql_Collection_TriplesNode, gen_sparql_BoundBuiltInCallNE_BuiltInCall, gen_sparql_SameTermBuiltInCallNE_BuiltInCall, gen_sparql_GraphTerm_VarOrTerm, gen_sparql_BlankNode_GraphTerm, gen_sparql_Constraint_OrderConditionRightNE, gen_sparql_BrackettedExpression_Constraint, gen_sparql_BrackettedExpression_PrimaryExpression, gen_sparql_BuiltInCall_Constraint, gen_sparql_BuiltInCall_PrimaryExpression, gen_sparql_StrBuiltInCallNE_BuiltInCall, gen_sparql_LangBuiltInCallNE_BuiltInCall, gen_sparql_LangmatchesBuiltInCallNE_BuiltInCall, gen_sparql_DatatypeBuiltInCallNE_BuiltInCall, gen_sparql_FunctionCall_Constraint, gen_sparql_IsIRIBuiltInCallNE_BuiltInCall, gen_sparql_IsURIBuiltInCallNE_BuiltInCall, gen_sparql_IsBlankBuiltInCallNE_BuiltInCall, gen_sparql_IsLiteralBuiltInCallNE_BuiltInCall, gen_sparql_RegexExpression_BuiltInCall, gen_sparql_Expression_LocatedElement, gen_sparql_ArgList_LocatedElement, gen_sparql_ArgListNILNE_ArgList, gen_sparql_ArgListExpressionNE_ArgList, gen_sparql_ConditionalAndExpression_LocatedElement, gen_sparql_AdditionalExpressionNE_LocatedElement, gen_sparql_ConditionalOrExpression_LocatedElement, gen_sparql_AdditionalConditionalAndExpressionNE_LocatedElement, gen_sparql_NumericExpression_LocatedElement, gen_sparql_AdditionalNumericExpressionNE_LocatedElement, gen_sparql_EqualsNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_ValueLogical_LocatedElement, gen_sparql_AdditionalValueLogicalNE_LocatedElement, gen_sparql_RelationalExpression_LocatedElement, gen_sparql_MultiplicativeExpression_LocatedElement, gen_sparql_NotEqualNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_SmallerNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_BiggerNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_SmallerOrEqualNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_BiggerOrEqualNumericExpressionNE_AdditionalNumericExpressionNE, gen_sparql_AdditiveExpression_LocatedElement, gen_sparql_DividedByAdditionalUnaryExpressionNE_AdditionalUnaryExpressionNE, gen_sparql_NotPrimaryExpressionNE_UnaryExpression, gen_sparql_PlusPrimaryExpressionNE_UnaryExpression, gen_sparql_AdditionalMultiplicativeExpressionNE_LocatedElement, gen_sparql_PlusMultiplicativeExpressionNE_AdditionalMultiplicativeExpressionNE, gen_sparql_MinusMultiplicativeExpressionNE_AdditionalMultiplicativeExpressionNE, gen_sparql_NumericLiteralPositive_AdditionalMultiplicativeExpressionNE, gen_sparql_NumericLiteralPositive_NumericLiteral, gen_sparql_NumericLiteralNegative_AdditionalMultiplicativeExpressionNE, gen_sparql_NumericLiteralNegative_NumericLiteral, gen_sparql_UnaryExpression_LocatedElement, gen_sparql_AdditionalUnaryExpressionNE_LocatedElement, gen_sparql_TimesAdditionalUnaryExpressionNE_AdditionalUnaryExpressionNE, gen_sparql_LANGTAGOrIRIrefNE_LocatedElement, gen_sparql_UpIRIrefNE_LANGTAGOrIRIrefNE, gen_sparql_NumericLiteral_PrimaryExpression, gen_sparql_NumericLiteral_GraphTerm, gen_sparql_NumericLiteral_AdditionalMultiplicativeExpressionNE, gen_sparql_NumericLiteralUnsigned_NumericLiteral, gen_sparql_MinusPrimaryExpressionNE_UnaryExpression, gen_sparql_PrimaryExpression_UnaryExpression, gen_sparql_IRIrefOrFunction_PrimaryExpression, gen_sparql_RDFLiteral_PrimaryExpression, gen_sparql_RDFLiteral_GraphTerm, gen_sparql_PNAME_NS_PrefixedName, gen_sparql_PNAME_NS_VarOrIRIref, gen_sparql_PNAME_LN_PrefixedName, gen_sparql_PNAME_LN_VarOrIRIref, gen_sparql_NotInList_GraphTerm, gen_sparql_BooleanLiteral_PrimaryExpression, gen_sparql_BooleanLiteral_GraphTerm, gen_sparql_TrueBooleanLiteralNE_BooleanLiteral, gen_sparql_FalseBooleanLiteralNE_BooleanLiteral, gen_sparql_VARNAME_LocatedElement, gen_sparql_IRI_REF_IRIreference, gen_sparql_IRI_REF_VarOrIRIref, gen_sparql_STRING_LITERAL1_StringLiteral, gen_sparql_STRING_LITERAL2_StringLiteral, gen_sparql_INTEGER_NumericLiteral, gen_sparql_DECIMAL_NumericLiteral, gen_sparql_DOUBLE_NumericLiteral, gen_sparql_WS_LocatedElement, gen_sparql_AscendingLiteral_AscOrDecs, gen_sparql_DescendingLiteral_AscOrDecs, gen_sparql_STRING_LITERAL_LONG1_StringLiteral, gen_sparql_STRING_LITERAL_LONG2_StringLiteral, gen_sparql_BLANK_NODE_LABEL_BlankNode, gen_sparql_ANON_BlankNode, gen_sparql_LANGTAG_LANGTAGOrIRIrefNE, gen_sparql_PN_PREFIX_LocatedElement, gen_sparql_PN_LOCAL_LocatedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)