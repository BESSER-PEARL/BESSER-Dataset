from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BlankNode:

    pass
class sparql_ANON(BlankNode):

    pass
class sparql_BLANK_NODE_LABEL(BlankNode):

    def __init__(self, pn_local: str):
        self.pn_local = pn_local
        
        pass
    @property
    def pn_local(self):
        return self.__pn_local

    @pn_local.setter
    def pn_local(self, pn_local: str):
        self.__pn_local = pn_local


class AscOrDecs:

    pass
class sparql_DescendingLiteral(AscOrDecs):

    pass
class sparql_AscendingLiteral(AscOrDecs):

    pass
class StringLiteral:

    pass
class sparql_STRING_LITERAL_LONG1(StringLiteral):

    def __init__(self, string: str):
        self.string = string
        
        pass
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


class sparql_STRING_LITERAL2(StringLiteral):

    def __init__(self, string: str):
        self.string = string
        
        pass
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


class sparql_STRING_LITERAL_LONG2(StringLiteral):

    def __init__(self, string: str):
        self.string = string
        
        pass
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


class sparql_STRING_LITERAL1(StringLiteral):

    def __init__(self, string: str):
        self.string = string
        
        pass
    @property
    def string(self):
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string


class sparql_VAR2:

    pass
class sparql_VAR1:

    pass
class BooleanLiteral:

    pass
class sparql_FalseBooleanLiteralNE(BooleanLiteral):

    pass
class sparql_TrueBooleanLiteralNE(BooleanLiteral):

    pass
class PrefixedName:

    pass
class sparql_StringLiteral(ABC):

    pass
class LANGTAGOrIRIrefNE:

    pass
class sparql_LANGTAG(LANGTAGOrIRIrefNE):

    def __init__(self, langtag: str):
        self.langtag = langtag
        
        pass
    @property
    def langtag(self):
        return self.__langtag

    @langtag.setter
    def langtag(self, langtag: str):
        self.__langtag = langtag


class sparql_UpIRIrefNE(LANGTAGOrIRIrefNE):

    pass
class AdditionalUnaryExpressionNE:

    pass
class sparql_TimesAdditionalUnaryExpressionNE(AdditionalUnaryExpressionNE):

    pass
class NumericLiteral:

    pass
class sparql_NumericLiteralUnsigned(NumericLiteral):

    pass
class sparql_DECIMAL(NumericLiteral):

    def __init__(self, decimal: str):
        self.decimal = decimal
        
        pass
    @property
    def decimal(self):
        return self.__decimal

    @decimal.setter
    def decimal(self, decimal: str):
        self.__decimal = decimal


class sparql_DOUBLE(NumericLiteral):

    def __init__(self, double: str):
        self.double = double
        
        pass
    @property
    def double(self):
        return self.__double

    @double.setter
    def double(self, double: str):
        self.__double = double


class AdditionalMultiplicativeExpressionNE:

    pass
class sparql_MinusMultiplicativeExpressionNE(AdditionalMultiplicativeExpressionNE):

    pass
class sparql_NumericLiteralPositive(AdditionalMultiplicativeExpressionNE, NumericLiteral):

    pass
class sparql_NumericLiteralNegative(AdditionalMultiplicativeExpressionNE, NumericLiteral):

    pass
class sparql_PlusMultiplicativeExpressionNE(AdditionalMultiplicativeExpressionNE):

    pass
class UnaryExpression:

    pass
class sparql_PlusPrimaryExpressionNE(UnaryExpression):

    pass
class sparql_PrimaryExpression(UnaryExpression):

    pass
class sparql_MinusPrimaryExpressionNE(UnaryExpression):

    pass
class sparql_NotPrimaryExpressionNE(UnaryExpression):

    pass
class sparql_DividedByAdditionalUnaryExpressionNE(AdditionalUnaryExpressionNE):

    pass
class AdditionalNumericExpressionNE:

    pass
class sparql_BiggerNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class sparql_NotEqualNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class sparql_SmallerNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class sparql_SmallerOrEqualNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class sparql_BiggerOrEqualNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class sparql_EqualsNumericExpressionNE(AdditionalNumericExpressionNE):

    pass
class ArgList:

    pass
class sparql_ArgListExpressionNE(ArgList):

    pass
class sparql_ArgListNILNE(ArgList):

    pass
class BuiltInCall:

    pass
class sparql_IsLiteralBuiltInCallNE(BuiltInCall):

    pass
class sparql_LangmatchesBuiltInCallNE(BuiltInCall):

    pass
class sparql_IsBlankBuiltInCallNE(BuiltInCall):

    pass
class sparql_IsURIBuiltInCallNE(BuiltInCall):

    pass
class sparql_LangBuiltInCallNE(BuiltInCall):

    pass
class sparql_DatatypeBuiltInCallNE(BuiltInCall):

    pass
class sparql_RegexExpression(BuiltInCall):

    pass
class sparql_IsIRIBuiltInCallNE(BuiltInCall):

    pass
class sparql_StrBuiltInCallNE(BuiltInCall):

    pass
class Constraint:

    pass
class sparql_FunctionCall(Constraint):

    pass
class sparql_SameTermBuiltInCallNE(BuiltInCall):

    pass
class sparql_BoundBuiltInCallNE(BuiltInCall):

    pass
class TriplesNode:

    pass
class sparql_BlankNodePropertyList(TriplesNode):

    pass
class sparql_Collection(TriplesNode):

    pass
class GraphNode:

    pass
class sparql_PatternOrFilterNE(ABC):

    pass
class sparql_VarOrTerm(GraphNode):

    pass
class TriplesSameSubject:

    pass
class sparql_TriplesSameSubjectLeftNE(TriplesSameSubject):

    pass
class sparql_TriplesBlock:

    pass
class GraphPatternNotTriples:

    pass
class sparql_GraphGraphPattern(GraphPatternNotTriples):

    pass
class sparql_GroupOrUnionGraphPattern(GraphPatternNotTriples):

    pass
class sparql_OptionalGraphPattern(GraphPatternNotTriples):

    pass
class PatternOrFilterNE:

    pass
class sparql_Filter(PatternOrFilterNE):

    pass
class sparql_GraphPatternNotTriples(PatternOrFilterNE):

    pass
class sparql_TriplesNode(GraphNode):

    pass
class sparql_TriplesSameSubjectRightNE(TriplesSameSubject):

    pass
class IRIreference:

    pass
class sparql_PrefixedName(IRIreference):

    pass
class SourceSelector:

    pass
class GraphTerm:

    pass
class sparql_NotInList(GraphTerm):

    pass
class sparql_BlankNode(GraphTerm):

    pass
class sparql_WhereLiteral:

    pass
class GraphClauseNE:

    pass
class sparql_NamedGraphClause(GraphClauseNE):

    pass
class sparql_DefaultGraphClause(GraphClauseNE):

    pass
class OrderConditionRightNE:

    pass
class sparql_Constraint(OrderConditionRightNE):

    pass
class VarOrTerm:

    pass
class sparql_GraphTerm(VarOrTerm):

    pass
class PrimaryExpression:

    pass
class sparql_BuiltInCall(PrimaryExpression, Constraint):

    pass
class sparql_NumericLiteral(AdditionalMultiplicativeExpressionNE, GraphTerm, PrimaryExpression):

    pass
class sparql_BooleanLiteral(GraphTerm, PrimaryExpression):

    pass
class sparql_IRIrefOrFunction(PrimaryExpression):

    pass
class sparql_RDFLiteral(GraphTerm, PrimaryExpression):

    pass
class VarOrIRIref:

    pass
class sparql_IRIreference(GraphTerm, SourceSelector, VarOrIRIref):

    pass
class sparql_PNAME_LN(PrefixedName, VarOrIRIref):

    pass
class Verb:

    pass
class sparql_VerbANE(Verb):

    def __init__(self, theA: str):
        self.theA = theA
        
        pass
    @property
    def theA(self):
        return self.__theA

    @theA.setter
    def theA(self, theA: str):
        self.__theA = theA


class VariablesNE:

    pass
class sparql_SomeVariablesNE(VariablesNE):

    pass
class sparql_AllVariablesNE(VariablesNE):

    pass
class SolutionsDisplayNE:

    pass
class sparql_ReducedNE(SolutionsDisplayNE):

    pass
class sparql_DistinctNE(SolutionsDisplayNE):

    pass
class sparql_INTEGER(NumericLiteral):

    def __init__(self, integer: str, sparql_INTEGER: "sparql_LimitClause" = None, sparql_INTEGER71: "sparql_OffsetClause" = None):
        self.integer = integer
        self.sparql_INTEGER = sparql_INTEGER
        self.sparql_INTEGER71 = sparql_INTEGER71
        
        pass
    @property
    def integer(self):
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer


    @property
    def sparql_INTEGER71(self):
        return self.__sparql_INTEGER71

    @sparql_INTEGER71.setter
    def sparql_INTEGER71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_INTEGER__sparql_INTEGER71", None)
        self.__sparql_INTEGER71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_OffsetClause70"):
                opp_val = getattr(old_value, "sparql_OffsetClause70", None)
                if opp_val == self:
                    setattr(old_value, "sparql_OffsetClause70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_OffsetClause70"):
                opp_val = getattr(value, "sparql_OffsetClause70", None)
                setattr(value, "sparql_OffsetClause70", self)

    @property
    def sparql_INTEGER(self):
        return self.__sparql_INTEGER

    @sparql_INTEGER.setter
    def sparql_INTEGER(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_INTEGER__sparql_INTEGER", None)
        self.__sparql_INTEGER = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_LimitClause68"):
                opp_val = getattr(old_value, "sparql_LimitClause68", None)
                if opp_val == self:
                    setattr(old_value, "sparql_LimitClause68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_LimitClause68"):
                opp_val = getattr(value, "sparql_LimitClause68", None)
                setattr(value, "sparql_LimitClause68", self)

class LimitOffsetClauses:

    pass
class sparql_LimitOffsetClausesRightNE(LimitOffsetClauses):

    pass
class sparql_LimitOffsetClausesLeftNE(LimitOffsetClauses):

    pass
class sparql_BrackettedExpression(PrimaryExpression, Constraint):

    pass
class sparql_AscOrDecs(ABC):

    pass
class OrderCondition:

    pass
class sparql_OrderConditionRightNE(OrderCondition):

    pass
class sparql_OrderConditionLeftNE(OrderCondition):

    pass
class sparql_VarOrIRIref(Verb):

    pass
class Query:

    pass
class sparql_DescribeQuery(Query):

    pass
class sparql_AskQuery(Query):

    pass
class sparql_ConstructQuery(Query):

    pass
class sparql_SelectQuery(Query):

    pass
class sparql_PNAME_NS(PrefixedName, VarOrIRIref):

    def __init__(self, pn_prefix: str, sparql_PNAME_NS: "sparql_PrefixDecl" = None):
        self.pn_prefix = pn_prefix
        self.sparql_PNAME_NS = sparql_PNAME_NS
        
        pass
    @property
    def pn_prefix(self):
        return self.__pn_prefix

    @pn_prefix.setter
    def pn_prefix(self, pn_prefix: str):
        self.__pn_prefix = pn_prefix


    @property
    def sparql_PNAME_NS(self):
        return self.__sparql_PNAME_NS

    @sparql_PNAME_NS.setter
    def sparql_PNAME_NS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_PNAME_NS__sparql_PNAME_NS", None)
        self.__sparql_PNAME_NS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_PrefixDecl10"):
                opp_val = getattr(old_value, "sparql_PrefixDecl10", None)
                if opp_val == self:
                    setattr(old_value, "sparql_PrefixDecl10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_PrefixDecl10"):
                opp_val = getattr(value, "sparql_PrefixDecl10", None)
                setattr(value, "sparql_PrefixDecl10", self)

class sparql_Var(OrderConditionRightNE, VarOrTerm, PrimaryExpression, VarOrIRIref):

    def __init__(self, varname: str, sparql_Var: "sparql_SelectQuery" = None, sparql_Var73: "sparql_SomeVariablesNE" = None, sparql_Var137: "sparql_BoundBuiltInCallNE" = None):
        self.varname = varname
        self.sparql_Var = sparql_Var
        self.sparql_Var73 = sparql_Var73
        self.sparql_Var137 = sparql_Var137
        
        pass
    @property
    def varname(self):
        return self.__varname

    @varname.setter
    def varname(self, varname: str):
        self.__varname = varname


    @property
    def sparql_Var(self):
        return self.__sparql_Var

    @sparql_Var.setter
    def sparql_Var(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Var__sparql_Var", None)
        self.__sparql_Var = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SelectQuery16"):
                opp_val = getattr(old_value, "sparql_SelectQuery16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SelectQuery16"):
                opp_val = getattr(value, "sparql_SelectQuery16", None)
                if opp_val is None:
                    setattr(value, "sparql_SelectQuery16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparql_Var137(self):
        return self.__sparql_Var137

    @sparql_Var137.setter
    def sparql_Var137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Var__sparql_Var137", None)
        self.__sparql_Var137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_BoundBuiltInCallNE"):
                opp_val = getattr(old_value, "sparql_BoundBuiltInCallNE", None)
                if opp_val == self:
                    setattr(old_value, "sparql_BoundBuiltInCallNE", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_BoundBuiltInCallNE"):
                opp_val = getattr(value, "sparql_BoundBuiltInCallNE", None)
                setattr(value, "sparql_BoundBuiltInCallNE", self)

    @property
    def sparql_Var73(self):
        return self.__sparql_Var73

    @sparql_Var73.setter
    def sparql_Var73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Var__sparql_Var73", None)
        self.__sparql_Var73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SomeVariablesNE"):
                opp_val = getattr(old_value, "sparql_SomeVariablesNE", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SomeVariablesNE"):
                opp_val = getattr(value, "sparql_SomeVariablesNE", None)
                if opp_val is None:
                    setattr(value, "sparql_SomeVariablesNE", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparql_LocatedElement(ABC):

    def __init__(self, commentsBefore: str, commentsAfter: str, location: str):
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def commentsAfter(self):
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter


    @property
    def commentsBefore(self):
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore


class sparql_IRI_REF(IRIreference, VarOrIRIref):

    def __init__(self, iri_ref: str, sparql_IRI_REF: "sparql_BaseDecl" = None, sparql_IRI_REF13: "sparql_PrefixDecl" = None):
        self.iri_ref = iri_ref
        self.sparql_IRI_REF = sparql_IRI_REF
        self.sparql_IRI_REF13 = sparql_IRI_REF13
        
        pass
    @property
    def iri_ref(self):
        return self.__iri_ref

    @iri_ref.setter
    def iri_ref(self, iri_ref: str):
        self.__iri_ref = iri_ref


    @property
    def sparql_IRI_REF13(self):
        return self.__sparql_IRI_REF13

    @sparql_IRI_REF13.setter
    def sparql_IRI_REF13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_IRI_REF__sparql_IRI_REF13", None)
        self.__sparql_IRI_REF13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_PrefixDecl12"):
                opp_val = getattr(old_value, "sparql_PrefixDecl12", None)
                if opp_val == self:
                    setattr(old_value, "sparql_PrefixDecl12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_PrefixDecl12"):
                opp_val = getattr(value, "sparql_PrefixDecl12", None)
                setattr(value, "sparql_PrefixDecl12", self)

    @property
    def sparql_IRI_REF(self):
        return self.__sparql_IRI_REF

    @sparql_IRI_REF.setter
    def sparql_IRI_REF(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_IRI_REF__sparql_IRI_REF", None)
        self.__sparql_IRI_REF = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_BaseDecl8"):
                opp_val = getattr(old_value, "sparql_BaseDecl8", None)
                if opp_val == self:
                    setattr(old_value, "sparql_BaseDecl8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_BaseDecl8"):
                opp_val = getattr(value, "sparql_BaseDecl8", None)
                setattr(value, "sparql_BaseDecl8", self)

class LocatedElement:

    pass
class sparql_LimitOffsetClauses(LocatedElement):

    pass
class sparql_Query(LocatedElement):

    pass
class sparql_AdditionalValueLogicalNE(LocatedElement):

    pass
class sparql_VariablesNE(LocatedElement):

    pass
class sparql_PrefixDecl(LocatedElement):

    pass
class sparql_ArgList(LocatedElement):

    pass
class sparql_ConstructTemplate(LocatedElement):

    pass
class sparql_GroupGraphPattern(LocatedElement):

    pass
class sparql_GraphNode(LocatedElement):

    pass
class sparql_VARNAME(LocatedElement):

    def __init__(self, varname: str, sparql_VARNAME: "sparql_VAR1" = None, sparql_VARNAME237: "sparql_VAR2" = None):
        self.varname = varname
        self.sparql_VARNAME = sparql_VARNAME
        self.sparql_VARNAME237 = sparql_VARNAME237
        
        pass
    @property
    def varname(self):
        return self.__varname

    @varname.setter
    def varname(self, varname: str):
        self.__varname = varname


    @property
    def sparql_VARNAME237(self):
        return self.__sparql_VARNAME237

    @sparql_VARNAME237.setter
    def sparql_VARNAME237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_VARNAME__sparql_VARNAME237", None)
        self.__sparql_VARNAME237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_VAR2"):
                opp_val = getattr(old_value, "sparql_VAR2", None)
                if opp_val == self:
                    setattr(old_value, "sparql_VAR2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_VAR2"):
                opp_val = getattr(value, "sparql_VAR2", None)
                setattr(value, "sparql_VAR2", self)

    @property
    def sparql_VARNAME(self):
        return self.__sparql_VARNAME

    @sparql_VARNAME.setter
    def sparql_VARNAME(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_VARNAME__sparql_VARNAME", None)
        self.__sparql_VARNAME = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_VAR1"):
                opp_val = getattr(old_value, "sparql_VAR1", None)
                if opp_val == self:
                    setattr(old_value, "sparql_VAR1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_VAR1"):
                opp_val = getattr(value, "sparql_VAR1", None)
                setattr(value, "sparql_VAR1", self)

class sparql_OffsetClause(LocatedElement):

    pass
class sparql_NumericExpression(LocatedElement):

    pass
class sparql_SolutionsDisplayNE(LocatedElement):

    pass
class sparql_WS(LocatedElement):

    def __init__(self, ws: str, sparql_WS: "sparql_NotInList" = None, sparql_WS242: "sparql_ANON" = None):
        self.ws = ws
        self.sparql_WS = sparql_WS
        self.sparql_WS242 = sparql_WS242
        
        pass
    @property
    def ws(self):
        return self.__ws

    @ws.setter
    def ws(self, ws: str):
        self.__ws = ws


    @property
    def sparql_WS242(self):
        return self.__sparql_WS242

    @sparql_WS242.setter
    def sparql_WS242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_WS__sparql_WS242", None)
        self.__sparql_WS242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_ANON"):
                opp_val = getattr(old_value, "sparql_ANON", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_ANON"):
                opp_val = getattr(value, "sparql_ANON", None)
                if opp_val is None:
                    setattr(value, "sparql_ANON", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparql_WS(self):
        return self.__sparql_WS

    @sparql_WS.setter
    def sparql_WS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_WS__sparql_WS", None)
        self.__sparql_WS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_NotInList240"):
                opp_val = getattr(old_value, "sparql_NotInList240", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_NotInList240"):
                opp_val = getattr(value, "sparql_NotInList240", None)
                if opp_val is None:
                    setattr(value, "sparql_NotInList240", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparql_PN_LOCAL(LocatedElement):

    def __init__(self, pn_local: str, sparql_PN_LOCAL: "sparql_PNAME_LN" = None):
        self.pn_local = pn_local
        self.sparql_PN_LOCAL = sparql_PN_LOCAL
        
        pass
    @property
    def pn_local(self):
        return self.__pn_local

    @pn_local.setter
    def pn_local(self, pn_local: str):
        self.__pn_local = pn_local


    @property
    def sparql_PN_LOCAL(self):
        return self.__sparql_PN_LOCAL

    @sparql_PN_LOCAL.setter
    def sparql_PN_LOCAL(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_PN_LOCAL__sparql_PN_LOCAL", None)
        self.__sparql_PN_LOCAL = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_PNAME_LN"):
                opp_val = getattr(old_value, "sparql_PNAME_LN", None)
                if opp_val == self:
                    setattr(old_value, "sparql_PNAME_LN", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_PNAME_LN"):
                opp_val = getattr(value, "sparql_PNAME_LN", None)
                setattr(value, "sparql_PNAME_LN", self)

class sparql_ConditionalAndExpression(LocatedElement):

    pass
class sparql_WhereClause(LocatedElement):

    pass
class sparql_RelationalExpression(LocatedElement):

    pass
class sparql_PropertyListNotEmpty(LocatedElement):

    pass
class sparql_DatasetClause(LocatedElement):

    pass
class sparql_OrderClause(LocatedElement):

    pass
class sparql_GraphClauseNE(LocatedElement):

    pass
class sparql_Object(LocatedElement):

    pass
class sparql_AdditionalGGPElement(LocatedElement):

    pass
class sparql_SolutionModifier(LocatedElement):

    pass
class sparql_LimitClause(LocatedElement):

    pass
class sparql_PN_PREFIX(LocatedElement):

    def __init__(self, pn_prefix: str):
        self.pn_prefix = pn_prefix
        
        pass
    @property
    def pn_prefix(self):
        return self.__pn_prefix

    @pn_prefix.setter
    def pn_prefix(self, pn_prefix: str):
        self.__pn_prefix = pn_prefix


class sparql_ConditionalOrExpression(LocatedElement):

    pass
class sparql_BaseDecl(LocatedElement):

    pass
class sparql_AdditionalExpressionNE(LocatedElement):

    pass
class sparql_Expression(LocatedElement):

    pass
class sparql_AdditionalMultiplicativeExpressionNE(LocatedElement):

    pass
class sparql_AdditionalUnaryExpressionNE(LocatedElement):

    pass
class sparql_ObjectList(LocatedElement):

    pass
class sparql_AdditionalNumericExpressionNE(LocatedElement):

    pass
class sparql_ValueLogical(LocatedElement):

    pass
class sparql_Verb(LocatedElement):

    pass
class sparql_Prologue(LocatedElement):

    pass
class sparql_LANGTAGOrIRIrefNE(LocatedElement):

    pass
class sparql_OrderCondition(LocatedElement):

    pass
class sparql_AdditionalConditionalAndExpressionNE(LocatedElement):

    pass
class sparql_SourceSelector(LocatedElement):

    pass
class sparql_TriplesSameSubject(LocatedElement):

    pass
class sparql_AdditiveExpression(LocatedElement):

    pass
class sparql_UnaryExpression(LocatedElement):

    pass
class sparql_MultiplicativeExpression(LocatedElement):

    pass
class sparql_SparqlQueries(LocatedElement):

    pass