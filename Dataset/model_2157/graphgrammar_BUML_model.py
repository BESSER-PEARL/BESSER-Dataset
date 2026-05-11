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
graphgrammar_Grammar = Class(name="graphgrammar_Grammar")
graphgrammar_Symbol = Class(name="graphgrammar_Symbol")
graphgrammar_Graph = Class(name="graphgrammar_Graph")
graphgrammar_VertexToSymbolSymbolsPairMap = Class(name="graphgrammar_VertexToSymbolSymbolsPairMap")
graphgrammar_Vertex = Class(name="graphgrammar_Vertex")
graphgrammar_SymbolSymbolsPair = Class(name="graphgrammar_SymbolSymbolsPair")
graphgrammar_Rule = Class(name="graphgrammar_Rule")
graphgrammar_DerivationStep = Class(name="graphgrammar_DerivationStep")
graphgrammar_VertexToVertexMap = Class(name="graphgrammar_VertexToVertexMap")
graphgrammar_Derivation = Class(name="graphgrammar_Derivation")
graphgrammar_ParsingTree = Class(name="graphgrammar_ParsingTree")
graphgrammar_ZoneVertex = Class(name="graphgrammar_ZoneVertex")
graphgrammar_ResolutionStep = Class(name="graphgrammar_ResolutionStep")
graphgrammar_VertexToStringMap = Class(name="graphgrammar_VertexToStringMap")
graphgrammar_Resolution = Class(name="graphgrammar_Resolution")
graphgrammar_StringToVertexMap = Class(name="graphgrammar_StringToVertexMap")
Vertex = Class(name="Vertex")
graphgrammar_TripleGrammar = Class(name="graphgrammar_TripleGrammar")
graphgrammar_Edge = Class(name="graphgrammar_Edge")
graphgrammar_TripleRule = Class(name="graphgrammar_TripleRule")
graphgrammar_TripleGraph = Class(name="graphgrammar_TripleGraph")

# graphgrammar_Grammar class attributes and methods
graphgrammar_Grammar_name: Property = Property(name="name", type=StringType)
graphgrammar_Grammar_m_derives: Method = Method(name="derives", parameters={Parameter(name='graphgrammar_next', type=StringType), Parameter(name='graphgrammar_rhs', type=StringType), Parameter(name='graphgrammar_prev', type=StringType), Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Grammar.attributes={graphgrammar_Grammar_name}
graphgrammar_Grammar.methods={graphgrammar_Grammar_m_derives}

# graphgrammar_Symbol class attributes and methods
graphgrammar_Symbol_name: Property = Property(name="name", type=StringType)
graphgrammar_Symbol_subscript: Property = Property(name="subscript", type=StringType)
graphgrammar_Symbol_superscript: Property = Property(name="superscript", type=StringType)
graphgrammar_Symbol_m_equivalates: Method = Method(name="equivalates", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=BooleanType)
graphgrammar_Symbol_m_compareTo: Method = Method(name="compareTo", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=IntegerType)
graphgrammar_Symbol.attributes={graphgrammar_Symbol_superscript, graphgrammar_Symbol_subscript, graphgrammar_Symbol_name}
graphgrammar_Symbol.methods={graphgrammar_Symbol_m_equivalates, graphgrammar_Symbol_m_compareTo}

# graphgrammar_Graph class attributes and methods
graphgrammar_Graph_m_neighborhood: Method = Method(name="neighborhood", parameters={Parameter(name='graphgrammar_vertices', type=StringType)}, type=StringType)
graphgrammar_Graph_m_neighborhood: Method = Method(name="neighborhood", parameters={Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Graph_m_isomorphicTo: Method = Method(name="isomorphicTo", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=BooleanType)
graphgrammar_Graph_m_isomorphism: Method = Method(name="isomorphism", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=StringType)
graphgrammar_Graph_m_inEdges: Method = Method(name="inEdges", parameters={Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Graph_m_outEdges: Method = Method(name="outEdges", parameters={Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Graph_m_edges: Method = Method(name="edges", parameters={Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Graph.methods={graphgrammar_Graph_m_isomorphicTo, graphgrammar_Graph_m_isomorphism, graphgrammar_Graph_m_neighborhood, graphgrammar_Graph_m_inEdges, graphgrammar_Graph_m_neighborhood, graphgrammar_Graph_m_edges, graphgrammar_Graph_m_outEdges}

# graphgrammar_VertexToSymbolSymbolsPairMap class attributes and methods

# graphgrammar_Vertex class attributes and methods
graphgrammar_Vertex_id: Property = Property(name="id", type=StringType)
graphgrammar_Vertex_m_equivalates: Method = Method(name="equivalates", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=BooleanType)
graphgrammar_Vertex.attributes={graphgrammar_Vertex_id}
graphgrammar_Vertex.methods={graphgrammar_Vertex_m_equivalates}

# graphgrammar_SymbolSymbolsPair class attributes and methods

# graphgrammar_Rule class attributes and methods
graphgrammar_Rule_id: Property = Property(name="id", type=StringType)
graphgrammar_Rule_name: Property = Property(name="name", type=StringType)
graphgrammar_Rule_m_apply: Method = Method(name="apply", parameters={Parameter(name='graphgrammar_pacs', type=StringType), Parameter(name='graphgrammar_graph', type=StringType), Parameter(name='graphgrammar_vertex', type=StringType)}, type=StringType)
graphgrammar_Rule_m_derive: Method = Method(name="derive", parameters={Parameter(name='graphgrammar_vertex', type=StringType), Parameter(name='graphgrammar_graph', type=StringType)}, type=StringType)
graphgrammar_Rule_m_embed: Method = Method(name="embed", parameters={Parameter(name='graphgrammar_edges', type=StringType), Parameter(name='graphgrammar_unifier', type=StringType), Parameter(name='graphgrammar_graph', type=StringType), Parameter(name='graphgrammar_vertex', type=StringType), Parameter(name='graphgrammar_pacs', type=StringType)}, type=StringType)
graphgrammar_Rule.attributes={graphgrammar_Rule_name, graphgrammar_Rule_id}
graphgrammar_Rule.methods={graphgrammar_Rule_m_derive, graphgrammar_Rule_m_embed, graphgrammar_Rule_m_apply}

# graphgrammar_DerivationStep class attributes and methods

# graphgrammar_VertexToVertexMap class attributes and methods

# graphgrammar_Derivation class attributes and methods

# graphgrammar_ParsingTree class attributes and methods
graphgrammar_ParsingTree_m_derivation: Method = Method(name="derivation", parameters={}, type=StringType)
graphgrammar_ParsingTree.methods={graphgrammar_ParsingTree_m_derivation}

# graphgrammar_ZoneVertex class attributes and methods
graphgrammar_ZoneVertex_m_equivalates: Method = Method(name="equivalates", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=BooleanType)
graphgrammar_ZoneVertex.methods={graphgrammar_ZoneVertex_m_equivalates}

# graphgrammar_ResolutionStep class attributes and methods

# graphgrammar_VertexToStringMap class attributes and methods
graphgrammar_VertexToStringMap_value: Property = Property(name="value", type=StringType)
graphgrammar_VertexToStringMap.attributes={graphgrammar_VertexToStringMap_value}

# graphgrammar_Resolution class attributes and methods

# graphgrammar_StringToVertexMap class attributes and methods
graphgrammar_StringToVertexMap_key: Property = Property(name="key", type=StringType)
graphgrammar_StringToVertexMap.attributes={graphgrammar_StringToVertexMap_key}

# Vertex class attributes and methods

# graphgrammar_TripleGrammar class attributes and methods
graphgrammar_TripleGrammar_name: Property = Property(name="name", type=StringType)
graphgrammar_TripleGrammar_m_produce: Method = Method(name="produce", parameters={Parameter(name='graphgrammar_derivationStep', type=StringType), Parameter(name='graphgrammar_tripleGraph', type=StringType), Parameter(name='graphgrammar_resolution', type=StringType), Parameter(name='graphgrammar_forward', type=StringType)}, type=StringType)
graphgrammar_TripleGrammar_m_resolve: Method = Method(name="resolve", parameters={Parameter(name='graphgrammar_forward', type=StringType), Parameter(name='graphgrammar_resolution', type=StringType), Parameter(name='graphgrammar_resolutionStep', type=StringType), Parameter(name='graphgrammar_tripleGraph', type=StringType)})
graphgrammar_TripleGrammar.attributes={graphgrammar_TripleGrammar_name}
graphgrammar_TripleGrammar.methods={graphgrammar_TripleGrammar_m_resolve, graphgrammar_TripleGrammar_m_produce}

# graphgrammar_Edge class attributes and methods
graphgrammar_Edge_m_compareTo: Method = Method(name="compareTo", parameters={Parameter(name='graphgrammar_other', type=StringType)}, type=IntegerType)
graphgrammar_Edge.methods={graphgrammar_Edge_m_compareTo}

# graphgrammar_TripleRule class attributes and methods
graphgrammar_TripleRule_m_invMs: Method = Method(name="invMs", parameters={Parameter(name='graphgrammar_sourceVertex', type=StringType)}, type=Vertex)
graphgrammar_TripleRule_m_invMt: Method = Method(name="invMt", parameters={Parameter(name='graphgrammar_targetVertex', type=StringType)}, type=Vertex)
graphgrammar_TripleRule.methods={graphgrammar_TripleRule_m_invMt, graphgrammar_TripleRule_m_invMs}

# graphgrammar_TripleGraph class attributes and methods
graphgrammar_TripleGraph_m_invMt: Method = Method(name="invMt", parameters={Parameter(name='graphgrammar_targetVertex', type=StringType)}, type=Vertex)
graphgrammar_TripleGraph_m_invMs: Method = Method(name="invMs", parameters={Parameter(name='graphgrammar_sourceVertex', type=StringType)}, type=Vertex)
graphgrammar_TripleGraph.methods={graphgrammar_TripleGraph_m_invMs, graphgrammar_TripleGraph_m_invMt}

# Relationships
alphabet0: BinaryAssociation = BinaryAssociation(
    name="alphabet0",
    ends={
        Property(name="graphgrammar_Symbol", type=graphgrammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Grammar", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminals1: BinaryAssociation = BinaryAssociation(
    name="terminals1",
    ends={
        Property(name="graphgrammar_Symbol3", type=graphgrammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Grammar2", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999))
    }
)
lhs12: BinaryAssociation = BinaryAssociation(
    name="lhs12",
    ends={
        Property(name="graphgrammar_Symbol14", type=graphgrammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Rule13", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs15: BinaryAssociation = BinaryAssociation(
    name="rhs15",
    ends={
        Property(name="graphgrammar_Graph", type=graphgrammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Rule16", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
embedding17: BinaryAssociation = BinaryAssociation(
    name="embedding17",
    ends={
        Property(name="graphgrammar_VertexToSymbolSymbolsPairMap", type=graphgrammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Rule18", type=graphgrammar_VertexToSymbolSymbolsPairMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pac19: BinaryAssociation = BinaryAssociation(
    name="pac19",
    ends={
        Property(name="graphgrammar_Vertex", type=graphgrammar_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Rule20", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 9999))
    }
)
edgeLabel21: BinaryAssociation = BinaryAssociation(
    name="edgeLabel21",
    ends={
        Property(name="graphgrammar_Symbol22", type=graphgrammar_SymbolSymbolsPair, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_SymbolSymbolsPair", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nonterminals4: BinaryAssociation = BinaryAssociation(
    name="nonterminals4",
    ends={
        Property(name="graphgrammar_Symbol6", type=graphgrammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Grammar5", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999))
    }
)
rules7: BinaryAssociation = BinaryAssociation(
    name="rules7",
    ends={
        Property(name="graphgrammar_Rule", type=graphgrammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Grammar8", type=graphgrammar_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial9: BinaryAssociation = BinaryAssociation(
    name="initial9",
    ends={
        Property(name="graphgrammar_Symbol11", type=graphgrammar_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Grammar10", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
rule32: BinaryAssociation = BinaryAssociation(
    name="rule32",
    ends={
        Property(name="graphgrammar_Rule33", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_DerivationStep", type=graphgrammar_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vertex34: BinaryAssociation = BinaryAssociation(
    name="vertex34",
    ends={
        Property(name="graphgrammar_Vertex36", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_DerivationStep35", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
previous37: BinaryAssociation = BinaryAssociation(
    name="previous37",
    ends={
        Property(name="graphgrammar_Graph39", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_DerivationStep38", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
next40: BinaryAssociation = BinaryAssociation(
    name="next40",
    ends={
        Property(name="graphgrammar_Graph42", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_DerivationStep41", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
unifier43: BinaryAssociation = BinaryAssociation(
    name="unifier43",
    ends={
        Property(name="graphgrammar_VertexToVertexMap", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_DerivationStep44", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps45: BinaryAssociation = BinaryAssociation(
    name="steps45",
    ends={
        Property(name="graphgrammar_DerivationStep46", type=graphgrammar_Derivation, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Derivation", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertexLabels23: BinaryAssociation = BinaryAssociation(
    name="vertexLabels23",
    ends={
        Property(name="graphgrammar_Symbol25", type=graphgrammar_SymbolSymbolsPair, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_SymbolSymbolsPair24", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key26: BinaryAssociation = BinaryAssociation(
    name="key26",
    ends={
        Property(name="graphgrammar_Vertex28", type=graphgrammar_VertexToSymbolSymbolsPairMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_VertexToSymbolSymbolsPairMap27", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="graphgrammar_SymbolSymbolsPair31", type=graphgrammar_VertexToSymbolSymbolsPairMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_VertexToSymbolSymbolsPairMap30", type=graphgrammar_SymbolSymbolsPair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps56: BinaryAssociation = BinaryAssociation(
    name="steps56",
    ends={
        Property(name="graphgrammar_ResolutionStep58", type=graphgrammar_Resolution, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Resolution57", type=graphgrammar_ResolutionStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
zoneVertex47: BinaryAssociation = BinaryAssociation(
    name="zoneVertex47",
    ends={
        Property(name="graphgrammar_ZoneVertex", type=graphgrammar_ParsingTree, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ParsingTree", type=graphgrammar_ZoneVertex, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivationStep48: BinaryAssociation = BinaryAssociation(
    name="derivationStep48",
    ends={
        Property(name="graphgrammar_DerivationStep50", type=graphgrammar_ParsingTree, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ParsingTree49", type=graphgrammar_DerivationStep, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children52: BinaryAssociation = BinaryAssociation(
    name="children52",
    ends={
        Property(name="graphgrammar_ParsingTree53", type=graphgrammar_ParsingTree, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ParsingTree51", type=graphgrammar_ParsingTree, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pac54: BinaryAssociation = BinaryAssociation(
    name="pac54",
    ends={
        Property(name="graphgrammar_VertexToStringMap", type=graphgrammar_ResolutionStep, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ResolutionStep", type=graphgrammar_VertexToStringMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referenceIds55: BinaryAssociation = BinaryAssociation(
    name="referenceIds55",
    ends={
        Property(name="graphgrammar_StringToVertexMap", type=graphgrammar_Resolution, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Resolution", type=graphgrammar_StringToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vertices67: BinaryAssociation = BinaryAssociation(
    name="vertices67",
    ends={
        Property(name="graphgrammar_Vertex69", type=graphgrammar_ZoneVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ZoneVertex68", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pac70: BinaryAssociation = BinaryAssociation(
    name="pac70",
    ends={
        Property(name="graphgrammar_Vertex72", type=graphgrammar_ZoneVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_ZoneVertex71", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_73: BinaryAssociation = BinaryAssociation(
    name="from_73",
    ends={
        Property(name="graphgrammar_Vertex75", type=graphgrammar_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Edge74", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
to76: BinaryAssociation = BinaryAssociation(
    name="to76",
    ends={
        Property(name="graphgrammar_Vertex78", type=graphgrammar_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Edge77", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
label79: BinaryAssociation = BinaryAssociation(
    name="label79",
    ends={
        Property(name="graphgrammar_Symbol81", type=graphgrammar_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Edge80", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vertices59: BinaryAssociation = BinaryAssociation(
    name="vertices59",
    ends={
        Property(name="graphgrammar_Vertex61", type=graphgrammar_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Graph60", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges62: BinaryAssociation = BinaryAssociation(
    name="edges62",
    ends={
        Property(name="graphgrammar_Edge", type=graphgrammar_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Graph63", type=graphgrammar_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
label64: BinaryAssociation = BinaryAssociation(
    name="label64",
    ends={
        Property(name="graphgrammar_Symbol66", type=graphgrammar_Vertex, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_Vertex65", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alphabet82: BinaryAssociation = BinaryAssociation(
    name="alphabet82",
    ends={
        Property(name="graphgrammar_Symbol83", type=graphgrammar_TripleGrammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGrammar", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
terminals84: BinaryAssociation = BinaryAssociation(
    name="terminals84",
    ends={
        Property(name="graphgrammar_Symbol86", type=graphgrammar_TripleGrammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGrammar85", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999))
    }
)
nonterminals87: BinaryAssociation = BinaryAssociation(
    name="nonterminals87",
    ends={
        Property(name="graphgrammar_Symbol89", type=graphgrammar_TripleGrammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGrammar88", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 9999))
    }
)
tripleRules90: BinaryAssociation = BinaryAssociation(
    name="tripleRules90",
    ends={
        Property(name="graphgrammar_TripleRule", type=graphgrammar_TripleGrammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGrammar91", type=graphgrammar_TripleRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial92: BinaryAssociation = BinaryAssociation(
    name="initial92",
    ends={
        Property(name="graphgrammar_Symbol94", type=graphgrammar_TripleGrammar, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGrammar93", type=graphgrammar_Symbol, multiplicity=Multiplicity(0, 1))
    }
)
source95: BinaryAssociation = BinaryAssociation(
    name="source95",
    ends={
        Property(name="graphgrammar_Rule97", type=graphgrammar_TripleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleRule96", type=graphgrammar_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corr98: BinaryAssociation = BinaryAssociation(
    name="corr98",
    ends={
        Property(name="graphgrammar_Rule100", type=graphgrammar_TripleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleRule99", type=graphgrammar_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source110: BinaryAssociation = BinaryAssociation(
    name="source110",
    ends={
        Property(name="graphgrammar_Graph111", type=graphgrammar_TripleGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGraph", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corr112: BinaryAssociation = BinaryAssociation(
    name="corr112",
    ends={
        Property(name="graphgrammar_Graph114", type=graphgrammar_TripleGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGraph113", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target115: BinaryAssociation = BinaryAssociation(
    name="target115",
    ends={
        Property(name="graphgrammar_Graph117", type=graphgrammar_TripleGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGraph116", type=graphgrammar_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ms118: BinaryAssociation = BinaryAssociation(
    name="ms118",
    ends={
        Property(name="graphgrammar_VertexToVertexMap120", type=graphgrammar_TripleGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGraph119", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mt121: BinaryAssociation = BinaryAssociation(
    name="mt121",
    ends={
        Property(name="graphgrammar_VertexToVertexMap123", type=graphgrammar_TripleGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleGraph122", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key124: BinaryAssociation = BinaryAssociation(
    name="key124",
    ends={
        Property(name="graphgrammar_Vertex126", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_VertexToVertexMap125", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
value127: BinaryAssociation = BinaryAssociation(
    name="value127",
    ends={
        Property(name="graphgrammar_Vertex129", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_VertexToVertexMap128", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
key130: BinaryAssociation = BinaryAssociation(
    name="key130",
    ends={
        Property(name="graphgrammar_Vertex132", type=graphgrammar_VertexToStringMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_VertexToStringMap131", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
target101: BinaryAssociation = BinaryAssociation(
    name="target101",
    ends={
        Property(name="graphgrammar_Rule103", type=graphgrammar_TripleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleRule102", type=graphgrammar_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ms104: BinaryAssociation = BinaryAssociation(
    name="ms104",
    ends={
        Property(name="graphgrammar_VertexToVertexMap106", type=graphgrammar_TripleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleRule105", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mt107: BinaryAssociation = BinaryAssociation(
    name="mt107",
    ends={
        Property(name="graphgrammar_VertexToVertexMap109", type=graphgrammar_TripleRule, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_TripleRule108", type=graphgrammar_VertexToVertexMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value133: BinaryAssociation = BinaryAssociation(
    name="value133",
    ends={
        Property(name="graphgrammar_Vertex135", type=graphgrammar_StringToVertexMap, multiplicity=Multiplicity(1, 1)),
        Property(name="graphgrammar_StringToVertexMap134", type=graphgrammar_Vertex, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_graphgrammar_ZoneVertex_Vertex = Generalization(general=Vertex, specific=graphgrammar_ZoneVertex)

# Domain Model
domain_model = DomainModel(
    name="graphgrammar",
    types={graphgrammar_Grammar, graphgrammar_Symbol, graphgrammar_Graph, graphgrammar_VertexToSymbolSymbolsPairMap, graphgrammar_Vertex, graphgrammar_SymbolSymbolsPair, graphgrammar_Rule, graphgrammar_DerivationStep, graphgrammar_VertexToVertexMap, graphgrammar_Derivation, graphgrammar_ParsingTree, graphgrammar_ZoneVertex, graphgrammar_ResolutionStep, graphgrammar_VertexToStringMap, graphgrammar_Resolution, graphgrammar_StringToVertexMap, Vertex, graphgrammar_TripleGrammar, graphgrammar_Edge, graphgrammar_TripleRule, graphgrammar_TripleGraph},
    associations={alphabet0, terminals1, lhs12, rhs15, embedding17, pac19, edgeLabel21, nonterminals4, rules7, initial9, rule32, vertex34, previous37, next40, unifier43, steps45, vertexLabels23, key26, value29, steps56, zoneVertex47, derivationStep48, children52, pac54, referenceIds55, vertices67, pac70, from_73, to76, label79, vertices59, edges62, label64, alphabet82, terminals84, nonterminals87, tripleRules90, initial92, source95, corr98, source110, corr112, target115, ms118, mt121, key124, value127, key130, target101, ms104, mt107, value133},
    generalizations={gen_graphgrammar_ZoneVertex_Vertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)