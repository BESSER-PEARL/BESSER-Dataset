from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    lessThen = "lessThen"
    greaterThen = "greaterThen"
    lessEqual = "lessEqual"
    greaterEqual = "greaterEqual"
    equal = "equal"
    notEqual = "notEqual"
    sum = "sum"
    div = "div"
    sub = "sub"
    multiplicity = "multiplicity"


############################################
# Definition of Classes
############################################

class Aggregate:

    pass
class sparql_SumAggregate(Aggregate):

    pass
class sparql_SampleAggregate(Aggregate):

    pass
class sparql_AvgAggregate(Aggregate):

    pass
class sparql_MinAgregate(Aggregate):

    pass
class sparql_MaxAggregate(Aggregate):

    pass
class sparql_GroupAggregate(Aggregate):

    def __init__(self, isDistinct: bool, value: str, sparql_GroupAggregate: set["sparql_Expression"] = None):
        self.isDistinct = isDistinct
        self.value = value
        self.sparql_GroupAggregate = sparql_GroupAggregate if sparql_GroupAggregate is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def sparql_GroupAggregate(self):
        return self.__sparql_GroupAggregate

    @sparql_GroupAggregate.setter
    def sparql_GroupAggregate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_GroupAggregate__sparql_GroupAggregate", None)
        self.__sparql_GroupAggregate = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparql_Expression132"):
                    opp_val = getattr(item, "sparql_Expression132", None)
                    
                    if opp_val == self:
                        setattr(item, "sparql_Expression132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparql_Expression132"):
                    opp_val = getattr(item, "sparql_Expression132", None)
                    
                    setattr(item, "sparql_Expression132", self)
                    

class sparql_CountAggregate(Aggregate):

    def __init__(self, isDistinct: bool, isAll: bool, sparql_CountAggregate: "sparql_Expression" = None):
        self.isDistinct = isDistinct
        self.isAll = isAll
        self.sparql_CountAggregate = sparql_CountAggregate
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def isAll(self):
        return self.__isAll

    @isAll.setter
    def isAll(self, isAll: bool):
        self.__isAll = isAll


    @property
    def sparql_CountAggregate(self):
        return self.__sparql_CountAggregate

    @sparql_CountAggregate.setter
    def sparql_CountAggregate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_CountAggregate__sparql_CountAggregate", None)
        self.__sparql_CountAggregate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_Expression120"):
                opp_val = getattr(old_value, "sparql_Expression120", None)
                if opp_val == self:
                    setattr(old_value, "sparql_Expression120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_Expression120"):
                opp_val = getattr(value, "sparql_Expression120", None)
                setattr(value, "sparql_Expression120", self)

class RDFTag:

    pass
class sparql_LangTag(RDFTag):

    def __init__(self, lang: str):
        self.lang = lang
        
        pass
    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang


class sparql_TypeTag(RDFTag):

    pass
class Value:

    pass
class sparql_IntegerValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class sparql_StringValue(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class sparql_RDFTag:

    pass
class sparql_ExprAggArg:

    def __init__(self, isDistinct: bool, sparql_ExprAggArg122: "sparql_SumAggregate" = None, sparql_ExprAggArg124: "sparql_MinAgregate" = None, sparql_ExprAggArg126: "sparql_MaxAggregate" = None, sparql_ExprAggArg128: "sparql_AvgAggregate" = None, sparql_ExprAggArg130: "sparql_SampleAggregate" = None, sparql_ExprAggArg: "sparql_Expression" = None):
        self.isDistinct = isDistinct
        self.sparql_ExprAggArg122 = sparql_ExprAggArg122
        self.sparql_ExprAggArg124 = sparql_ExprAggArg124
        self.sparql_ExprAggArg126 = sparql_ExprAggArg126
        self.sparql_ExprAggArg128 = sparql_ExprAggArg128
        self.sparql_ExprAggArg130 = sparql_ExprAggArg130
        self.sparql_ExprAggArg = sparql_ExprAggArg
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def sparql_ExprAggArg124(self):
        return self.__sparql_ExprAggArg124

    @sparql_ExprAggArg124.setter
    def sparql_ExprAggArg124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg124", None)
        self.__sparql_ExprAggArg124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_MinAgregate"):
                opp_val = getattr(old_value, "sparql_MinAgregate", None)
                if opp_val == self:
                    setattr(old_value, "sparql_MinAgregate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_MinAgregate"):
                opp_val = getattr(value, "sparql_MinAgregate", None)
                setattr(value, "sparql_MinAgregate", self)

    @property
    def sparql_ExprAggArg130(self):
        return self.__sparql_ExprAggArg130

    @sparql_ExprAggArg130.setter
    def sparql_ExprAggArg130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg130", None)
        self.__sparql_ExprAggArg130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SampleAggregate"):
                opp_val = getattr(old_value, "sparql_SampleAggregate", None)
                if opp_val == self:
                    setattr(old_value, "sparql_SampleAggregate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SampleAggregate"):
                opp_val = getattr(value, "sparql_SampleAggregate", None)
                setattr(value, "sparql_SampleAggregate", self)

    @property
    def sparql_ExprAggArg(self):
        return self.__sparql_ExprAggArg

    @sparql_ExprAggArg.setter
    def sparql_ExprAggArg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg", None)
        self.__sparql_ExprAggArg = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_Expression109"):
                opp_val = getattr(old_value, "sparql_Expression109", None)
                if opp_val == self:
                    setattr(old_value, "sparql_Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_Expression109"):
                opp_val = getattr(value, "sparql_Expression109", None)
                setattr(value, "sparql_Expression109", self)

    @property
    def sparql_ExprAggArg128(self):
        return self.__sparql_ExprAggArg128

    @sparql_ExprAggArg128.setter
    def sparql_ExprAggArg128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg128", None)
        self.__sparql_ExprAggArg128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_AvgAggregate"):
                opp_val = getattr(old_value, "sparql_AvgAggregate", None)
                if opp_val == self:
                    setattr(old_value, "sparql_AvgAggregate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_AvgAggregate"):
                opp_val = getattr(value, "sparql_AvgAggregate", None)
                setattr(value, "sparql_AvgAggregate", self)

    @property
    def sparql_ExprAggArg122(self):
        return self.__sparql_ExprAggArg122

    @sparql_ExprAggArg122.setter
    def sparql_ExprAggArg122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg122", None)
        self.__sparql_ExprAggArg122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SumAggregate"):
                opp_val = getattr(old_value, "sparql_SumAggregate", None)
                if opp_val == self:
                    setattr(old_value, "sparql_SumAggregate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SumAggregate"):
                opp_val = getattr(value, "sparql_SumAggregate", None)
                setattr(value, "sparql_SumAggregate", self)

    @property
    def sparql_ExprAggArg126(self):
        return self.__sparql_ExprAggArg126

    @sparql_ExprAggArg126.setter
    def sparql_ExprAggArg126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExprAggArg__sparql_ExprAggArg126", None)
        self.__sparql_ExprAggArg126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_MaxAggregate"):
                opp_val = getattr(old_value, "sparql_MaxAggregate", None)
                if opp_val == self:
                    setattr(old_value, "sparql_MaxAggregate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_MaxAggregate"):
                opp_val = getattr(value, "sparql_MaxAggregate", None)
                setattr(value, "sparql_MaxAggregate", self)

class Variable:

    pass
class sparql_NamedVariable(Variable):

    pass
class sparql_UnNamedVariable(Variable):

    pass
class GraphNode:

    pass
class sparql_Value(GraphNode):

    pass
class sparql_Parameter(GraphNode):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class sparql_BlankNode(GraphNode):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class sparql_Aggregate:

    pass
class Function:

    pass
class sparql_SparqlFunction(Function):

    pass
class sparql_NamedFunction(Function):

    pass
class FilterNode:

    pass
class GroupCondition:

    pass
class sparql_FilterNode:

    pass
class Expression:

    pass
class sparql_AndFilterExpression(Expression):

    pass
class sparql_OrFilterExpression(Expression):

    pass
class sparql_ExpressionFilterExpression(Expression):

    def __init__(self, operator: str, sparql_ExpressionFilterExpression: "sparql_FilterNode" = None, sparql_ExpressionFilterExpression82: "sparql_FilterNode" = None):
        self.operator = operator
        self.sparql_ExpressionFilterExpression = sparql_ExpressionFilterExpression
        self.sparql_ExpressionFilterExpression82 = sparql_ExpressionFilterExpression82
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def sparql_ExpressionFilterExpression(self):
        return self.__sparql_ExpressionFilterExpression

    @sparql_ExpressionFilterExpression.setter
    def sparql_ExpressionFilterExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExpressionFilterExpression__sparql_ExpressionFilterExpression", None)
        self.__sparql_ExpressionFilterExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_FilterNode"):
                opp_val = getattr(old_value, "sparql_FilterNode", None)
                if opp_val == self:
                    setattr(old_value, "sparql_FilterNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_FilterNode"):
                opp_val = getattr(value, "sparql_FilterNode", None)
                setattr(value, "sparql_FilterNode", self)

    @property
    def sparql_ExpressionFilterExpression82(self):
        return self.__sparql_ExpressionFilterExpression82

    @sparql_ExpressionFilterExpression82.setter
    def sparql_ExpressionFilterExpression82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ExpressionFilterExpression__sparql_ExpressionFilterExpression82", None)
        self.__sparql_ExpressionFilterExpression82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_FilterNode83"):
                opp_val = getattr(old_value, "sparql_FilterNode83", None)
                if opp_val == self:
                    setattr(old_value, "sparql_FilterNode83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_FilterNode83"):
                opp_val = getattr(value, "sparql_FilterNode83", None)
                setattr(value, "sparql_FilterNode83", self)

class Constraint:

    pass
class sparql_BuiltInCall(Constraint, GroupCondition):

    pass
class sparql_Function(FilterNode, Constraint, GroupCondition):

    def __init__(self, name: str, sparql_Function: set["sparql_Variable"] = None):
        self.name = name
        self.sparql_Function = sparql_Function if sparql_Function is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sparql_Function(self):
        return self.__sparql_Function

    @sparql_Function.setter
    def sparql_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Function__sparql_Function", None)
        self.__sparql_Function = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparql_Variable85"):
                    opp_val = getattr(item, "sparql_Variable85", None)
                    
                    if opp_val == self:
                        setattr(item, "sparql_Variable85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparql_Variable85"):
                    opp_val = getattr(item, "sparql_Variable85", None)
                    
                    setattr(item, "sparql_Variable85", self)
                    

class sparql_Expression(Constraint):

    pass
class GraphPattern:

    pass
class sparql_FilterPattern(GraphPattern):

    pass
class sparql_ExistsPattern(GraphPattern):

    pass
class sparql_GraphGraphPattern(GraphPattern):

    pass
class sparql_NotExistsPattern(GraphPattern):

    pass
class sparql_MinusPattern(GraphPattern):

    pass
class sparql_ServiceGraphPattern(GraphPattern):

    pass
class sparql_TriplesSameSubject(GraphPattern):

    pass
class sparql_OptionalGraphPattern(GraphPattern):

    pass
class sparql_GroupOrUnionGraphPattern(GraphPattern):

    pass
class sparql_PropertyList:

    pass
class sparql_GraphPattern:

    pass
class GroupGraphPattern:

    pass
class sparql_GroupGraphPatternSub(GroupGraphPattern):

    pass
class sparql_SubSelectQuery(GroupGraphPattern):

    pass
class sparql_Constraint:

    pass
class sparql_GroupCondition:

    pass
class DatasetClause:

    pass
class sparql_ServiceDataSet(DatasetClause):

    pass
class sparql_NamedDataSet(DatasetClause):

    pass
class sparql_DefaultDataSet(DatasetClause):

    pass
class ModifyQuery:

    pass
class sparql_DeleteDataQuery(ModifyQuery):

    def __init__(self, graph: str):
        self.graph = graph
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


class sparql_DeleteWhereQuery(ModifyQuery):

    pass
class sparql_InsertDataQuery(ModifyQuery):

    def __init__(self, graph: str):
        self.graph = graph
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


class sparql_DeleteQuery(ModifyQuery):

    def __init__(self, graph: str, sparql_DeleteQuery25: "sparql_WhereClause" = None, sparql_DeleteQuery: "sparql_GroupGraphPattern" = None):
        self.graph = graph
        self.sparql_DeleteQuery25 = sparql_DeleteQuery25
        self.sparql_DeleteQuery = sparql_DeleteQuery
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


    @property
    def sparql_DeleteQuery(self):
        return self.__sparql_DeleteQuery

    @sparql_DeleteQuery.setter
    def sparql_DeleteQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_DeleteQuery__sparql_DeleteQuery", None)
        self.__sparql_DeleteQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_GroupGraphPattern23"):
                opp_val = getattr(old_value, "sparql_GroupGraphPattern23", None)
                if opp_val == self:
                    setattr(old_value, "sparql_GroupGraphPattern23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_GroupGraphPattern23"):
                opp_val = getattr(value, "sparql_GroupGraphPattern23", None)
                setattr(value, "sparql_GroupGraphPattern23", self)

    @property
    def sparql_DeleteQuery25(self):
        return self.__sparql_DeleteQuery25

    @sparql_DeleteQuery25.setter
    def sparql_DeleteQuery25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_DeleteQuery__sparql_DeleteQuery25", None)
        self.__sparql_DeleteQuery25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_WhereClause26"):
                opp_val = getattr(old_value, "sparql_WhereClause26", None)
                if opp_val == self:
                    setattr(old_value, "sparql_WhereClause26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_WhereClause26"):
                opp_val = getattr(value, "sparql_WhereClause26", None)
                setattr(value, "sparql_WhereClause26", self)

class sparql_InsertQuery(ModifyQuery):

    def __init__(self, graph: str, sparql_InsertQuery: "sparql_WhereClause" = None):
        self.graph = graph
        self.sparql_InsertQuery = sparql_InsertQuery
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


    @property
    def sparql_InsertQuery(self):
        return self.__sparql_InsertQuery

    @sparql_InsertQuery.setter
    def sparql_InsertQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_InsertQuery__sparql_InsertQuery", None)
        self.__sparql_InsertQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_WhereClause21"):
                opp_val = getattr(old_value, "sparql_WhereClause21", None)
                if opp_val == self:
                    setattr(old_value, "sparql_WhereClause21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_WhereClause21"):
                opp_val = getattr(value, "sparql_WhereClause21", None)
                setattr(value, "sparql_WhereClause21", self)

class sparql_UsingGraph:

    def __init__(self, named: bool, uri: str):
        self.named = named
        self.uri = uri
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def named(self):
        return self.__named

    @named.setter
    def named(self, named: bool):
        self.__named = named


class UpdateOperation:

    pass
class sparql_LoadGraphQuery(UpdateOperation):

    def __init__(self, intoGraph: str, graph: str):
        self.intoGraph = intoGraph
        self.graph = graph
        
        pass
    @property
    def intoGraph(self):
        return self.__intoGraph

    @intoGraph.setter
    def intoGraph(self, intoGraph: str):
        self.__intoGraph = intoGraph


    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


class sparql_DropGraphQuery(UpdateOperation):

    def __init__(self, isSilent: str, graph: str):
        self.isSilent = isSilent
        self.graph = graph
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


    @property
    def isSilent(self):
        return self.__isSilent

    @isSilent.setter
    def isSilent(self, isSilent: str):
        self.__isSilent = isSilent


class sparql_CreateGraphQuery(UpdateOperation):

    def __init__(self, isSilent: str, graph: str):
        self.isSilent = isSilent
        self.graph = graph
        
        pass
    @property
    def graph(self):
        return self.__graph

    @graph.setter
    def graph(self, graph: str):
        self.__graph = graph


    @property
    def isSilent(self):
        return self.__isSilent

    @isSilent.setter
    def isSilent(self, isSilent: str):
        self.__isSilent = isSilent


class sparql_ClearGraphQuery(UpdateOperation):

    def __init__(self, uri: str, isDefault: bool):
        self.uri = uri
        self.isDefault = isDefault
        
        pass
    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri


    @property
    def isDefault(self):
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: bool):
        self.__isDefault = isDefault


class sparql_ModifyQuery(UpdateOperation):

    def __init__(self, withGraph: str, sparql_ModifyQuery: "sparql_GroupGraphPattern" = None):
        self.withGraph = withGraph
        self.sparql_ModifyQuery = sparql_ModifyQuery
        
        pass
    @property
    def withGraph(self):
        return self.__withGraph

    @withGraph.setter
    def withGraph(self, withGraph: str):
        self.__withGraph = withGraph


    @property
    def sparql_ModifyQuery(self):
        return self.__sparql_ModifyQuery

    @sparql_ModifyQuery.setter
    def sparql_ModifyQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_ModifyQuery__sparql_ModifyQuery", None)
        self.__sparql_ModifyQuery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_GroupGraphPattern19"):
                opp_val = getattr(old_value, "sparql_GroupGraphPattern19", None)
                if opp_val == self:
                    setattr(old_value, "sparql_GroupGraphPattern19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_GroupGraphPattern19"):
                opp_val = getattr(value, "sparql_GroupGraphPattern19", None)
                setattr(value, "sparql_GroupGraphPattern19", self)

class sparql_UpdateOperation:

    pass
class sparql_GroupGraphPattern:

    pass
class sparql_GraphNode(FilterNode):

    pass
class sparql_Variable(GroupCondition, GraphNode):

    def __init__(self, name: str, sparql_Variable: "sparql_SelectQuery" = None, sparql_Variable38: "sparql_SubSelectQuery" = None, sparql_Variable85: "sparql_Function" = None, sparql_Variable98: "sparql_BuiltInCall" = None):
        self.name = name
        self.sparql_Variable = sparql_Variable
        self.sparql_Variable38 = sparql_Variable38
        self.sparql_Variable85 = sparql_Variable85
        self.sparql_Variable98 = sparql_Variable98
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sparql_Variable38(self):
        return self.__sparql_Variable38

    @sparql_Variable38.setter
    def sparql_Variable38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Variable__sparql_Variable38", None)
        self.__sparql_Variable38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SubSelectQuery"):
                opp_val = getattr(old_value, "sparql_SubSelectQuery", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SubSelectQuery"):
                opp_val = getattr(value, "sparql_SubSelectQuery", None)
                if opp_val is None:
                    setattr(value, "sparql_SubSelectQuery", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparql_Variable98(self):
        return self.__sparql_Variable98

    @sparql_Variable98.setter
    def sparql_Variable98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Variable__sparql_Variable98", None)
        self.__sparql_Variable98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_BuiltInCall97"):
                opp_val = getattr(old_value, "sparql_BuiltInCall97", None)
                if opp_val == self:
                    setattr(old_value, "sparql_BuiltInCall97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_BuiltInCall97"):
                opp_val = getattr(value, "sparql_BuiltInCall97", None)
                setattr(value, "sparql_BuiltInCall97", self)

    @property
    def sparql_Variable85(self):
        return self.__sparql_Variable85

    @sparql_Variable85.setter
    def sparql_Variable85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Variable__sparql_Variable85", None)
        self.__sparql_Variable85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_Function"):
                opp_val = getattr(old_value, "sparql_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_Function"):
                opp_val = getattr(value, "sparql_Function", None)
                if opp_val is None:
                    setattr(value, "sparql_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sparql_Variable(self):
        return self.__sparql_Variable

    @sparql_Variable.setter
    def sparql_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Variable__sparql_Variable", None)
        self.__sparql_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SelectQuery"):
                opp_val = getattr(old_value, "sparql_SelectQuery", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SelectQuery"):
                opp_val = getattr(value, "sparql_SelectQuery", None)
                if opp_val is None:
                    setattr(value, "sparql_SelectQuery", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SelectionQuery:

    pass
class sparql_AskQuery(SelectionQuery):

    pass
class sparql_ConstructQuery(SelectionQuery):

    pass
class sparql_DescribeQuery(SelectionQuery):

    pass
class sparql_SelectQuery(SelectionQuery):

    def __init__(self, isDistinct: bool, isReduced: bool, all: bool, sparql_SelectQuery: set["sparql_Variable"] = None):
        self.isDistinct = isDistinct
        self.isReduced = isReduced
        self.all = all
        self.sparql_SelectQuery = sparql_SelectQuery if sparql_SelectQuery is not None else set()
        
        pass
    @property
    def isDistinct(self):
        return self.__isDistinct

    @isDistinct.setter
    def isDistinct(self, isDistinct: bool):
        self.__isDistinct = isDistinct


    @property
    def isReduced(self):
        return self.__isReduced

    @isReduced.setter
    def isReduced(self, isReduced: bool):
        self.__isReduced = isReduced


    @property
    def all(self):
        return self.__all

    @all.setter
    def all(self, all: bool):
        self.__all = all


    @property
    def sparql_SelectQuery(self):
        return self.__sparql_SelectQuery

    @sparql_SelectQuery.setter
    def sparql_SelectQuery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_SelectQuery__sparql_SelectQuery", None)
        self.__sparql_SelectQuery = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sparql_Variable"):
                    opp_val = getattr(item, "sparql_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "sparql_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sparql_Variable"):
                    opp_val = getattr(item, "sparql_Variable", None)
                    
                    setattr(item, "sparql_Variable", self)
                    

class sparql_LimitClause:

    def __init__(self, limit: int, sparql_LimitClause: "sparql_SelectionQuery" = None):
        self.limit = limit
        self.sparql_LimitClause = sparql_LimitClause
        
        pass
    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit


    @property
    def sparql_LimitClause(self):
        return self.__sparql_LimitClause

    @sparql_LimitClause.setter
    def sparql_LimitClause(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_LimitClause__sparql_LimitClause", None)
        self.__sparql_LimitClause = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SelectionQuery13"):
                opp_val = getattr(old_value, "sparql_SelectionQuery13", None)
                if opp_val == self:
                    setattr(old_value, "sparql_SelectionQuery13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SelectionQuery13"):
                opp_val = getattr(value, "sparql_SelectionQuery13", None)
                setattr(value, "sparql_SelectionQuery13", self)

class sparql_HavingClause:

    pass
class sparql_GroupClause:

    pass
class sparql_WhereClause:

    pass
class sparql_DatasetClause:

    pass
class SPARQLQuery:

    pass
class sparql_UpdateQuery(SPARQLQuery):

    pass
class sparql_SelectionQuery(SPARQLQuery):

    pass
class sparql_IRI(GraphNode):

    def __init__(self, value: str, sparql_IRI29: "sparql_DatasetClause" = None, sparql_IRI: "sparql_Base" = None):
        self.value = value
        self.sparql_IRI29 = sparql_IRI29
        self.sparql_IRI = sparql_IRI
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def sparql_IRI29(self):
        return self.__sparql_IRI29

    @sparql_IRI29.setter
    def sparql_IRI29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_IRI__sparql_IRI29", None)
        self.__sparql_IRI29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_DatasetClause28"):
                opp_val = getattr(old_value, "sparql_DatasetClause28", None)
                if opp_val == self:
                    setattr(old_value, "sparql_DatasetClause28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_DatasetClause28"):
                opp_val = getattr(value, "sparql_DatasetClause28", None)
                setattr(value, "sparql_DatasetClause28", self)

    @property
    def sparql_IRI(self):
        return self.__sparql_IRI

    @sparql_IRI.setter
    def sparql_IRI(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_IRI__sparql_IRI", None)
        self.__sparql_IRI = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_Base"):
                opp_val = getattr(old_value, "sparql_Base", None)
                if opp_val == self:
                    setattr(old_value, "sparql_Base", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_Base"):
                opp_val = getattr(value, "sparql_Base", None)
                setattr(value, "sparql_Base", self)

class sparql_Base:

    pass
class sparql_Prefix:

    def __init__(self, iref: str, name: str, sparql_Prefix: "sparql_SPARQLQuery" = None, sparql_Prefix87: "sparql_NamedFunction" = None, sparql_Prefix111: "sparql_NamedVariable" = None):
        self.iref = iref
        self.name = name
        self.sparql_Prefix = sparql_Prefix
        self.sparql_Prefix87 = sparql_Prefix87
        self.sparql_Prefix111 = sparql_Prefix111
        
        pass
    @property
    def iref(self):
        return self.__iref

    @iref.setter
    def iref(self, iref: str):
        self.__iref = iref


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def sparql_Prefix111(self):
        return self.__sparql_Prefix111

    @sparql_Prefix111.setter
    def sparql_Prefix111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Prefix__sparql_Prefix111", None)
        self.__sparql_Prefix111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_NamedVariable"):
                opp_val = getattr(old_value, "sparql_NamedVariable", None)
                if opp_val == self:
                    setattr(old_value, "sparql_NamedVariable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_NamedVariable"):
                opp_val = getattr(value, "sparql_NamedVariable", None)
                setattr(value, "sparql_NamedVariable", self)

    @property
    def sparql_Prefix87(self):
        return self.__sparql_Prefix87

    @sparql_Prefix87.setter
    def sparql_Prefix87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Prefix__sparql_Prefix87", None)
        self.__sparql_Prefix87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_NamedFunction"):
                opp_val = getattr(old_value, "sparql_NamedFunction", None)
                if opp_val == self:
                    setattr(old_value, "sparql_NamedFunction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_NamedFunction"):
                opp_val = getattr(value, "sparql_NamedFunction", None)
                setattr(value, "sparql_NamedFunction", self)

    @property
    def sparql_Prefix(self):
        return self.__sparql_Prefix

    @sparql_Prefix.setter
    def sparql_Prefix(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sparql_Prefix__sparql_Prefix", None)
        self.__sparql_Prefix = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sparql_SPARQLQuery"):
                opp_val = getattr(old_value, "sparql_SPARQLQuery", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sparql_SPARQLQuery"):
                opp_val = getattr(value, "sparql_SPARQLQuery", None)
                if opp_val is None:
                    setattr(value, "sparql_SPARQLQuery", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sparql_SPARQLQuery:

    pass