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
graphpattern_GraphPattern = Class(name="graphpattern::GraphPattern")
PatternElement = Class(name="PatternElement")
graphpattern_NodePattern = Class(name="graphpattern::NodePattern")
graphpattern_Pattern = Class(name="graphpattern::Pattern")
graphpattern_DependencyGraph = Class(name="graphpattern::DependencyGraph")
graphpattern_SubGraph = Class(name="graphpattern::SubGraph")
GraphElement = Class(name="GraphElement")
graphpattern_EdgePattern = Class(name="graphpattern::EdgePattern")
graphpattern_EClass = Class(name="graphpattern::EClass")
graphpattern_AttributePattern = Class(name="graphpattern::AttributePattern")
graphpattern_Matching = Class(name="graphpattern::Matching", is_abstract=True)
graphpattern_Association = Class(name="graphpattern::Association")
graphpattern_EReference = Class(name="graphpattern::EReference")
graphpattern_EAttribute = Class(name="graphpattern::EAttribute")
graphpattern_Bundle = Class(name="graphpattern::Bundle")
Pattern = Class(name="Pattern")
graphpattern_Profile = Class(name="graphpattern::Profile")
graphpattern_EObject = Class(name="graphpattern::EObject")
graphpattern_EPackage = Class(name="graphpattern::EPackage")
graphpattern_Parameter = Class(name="graphpattern::Parameter")
graphpattern_Assignment = Class(name="graphpattern::Assignment")
graphpattern_DependencyNode = Class(name="graphpattern::DependencyNode")
graphpattern_PatternElement = Class(name="graphpattern::PatternElement", is_abstract=True)
Extendable = Class(name="Extendable")
graphpattern_EObjectList = Class(name="graphpattern::EObjectList")
graphpattern_GraphElement = Class(name="graphpattern::GraphElement", is_abstract=True)
graphpattern_DependencyEdge = Class(name="graphpattern::DependencyEdge")
graphpattern_ValueBinding = Class(name="graphpattern::ValueBinding")
graphpattern_Stereotype = Class(name="graphpattern::Stereotype")
graphpattern_ParameterBinding = Class(name="graphpattern::ParameterBinding", is_abstract=True)
graphpattern_ObjectBinding = Class(name="graphpattern::ObjectBinding")
ParameterBinding = Class(name="ParameterBinding")
graphpattern_Resource = Class(name="graphpattern::Resource", is_abstract=True)
graphpattern_Extendable = Class(name="graphpattern::Extendable", is_abstract=True)

# graphpattern_GraphPattern class attributes and methods

# PatternElement class attributes and methods

# graphpattern_NodePattern class attributes and methods
graphpattern_NodePattern_m_getAttribute: Method = Method(name="getAttribute", parameters={Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getOutgoings: Method = Method(name="getOutgoings", parameters={Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getAdjacent: Method = Method(name="getAdjacent", parameters={}, type=StringType)
graphpattern_NodePattern_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='target'), Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getOutgoing: Method = Method(name="getOutgoing", parameters={Parameter(name='target'), Parameter(name='type'), Parameter(name='stereotype')}, type=StringType)
graphpattern_NodePattern_m_getIncoming: Method = Method(name="getIncoming", parameters={Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getIncomings: Method = Method(name="getIncomings", parameters={Parameter(name='type')}, type=StringType)
graphpattern_NodePattern_m_getIncident: Method = Method(name="getIncident", parameters={}, type=StringType)
graphpattern_NodePattern_m_getIncident: Method = Method(name="getIncident", parameters={Parameter(name='adjacent')}, type=StringType)
graphpattern_NodePattern_m_removeIncident: Method = Method(name="removeIncident", parameters={}, type=StringType)
graphpattern_NodePattern_m_removeIncident: Method = Method(name="removeIncident", parameters={Parameter(name='node')}, type=StringType)
graphpattern_NodePattern.methods={graphpattern_NodePattern_m_getAdjacent, graphpattern_NodePattern_m_getOutgoing, graphpattern_NodePattern_m_getIncomings, graphpattern_NodePattern_m_removeIncident, graphpattern_NodePattern_m_getAttribute, graphpattern_NodePattern_m_getIncoming, graphpattern_NodePattern_m_getOutgoing, graphpattern_NodePattern_m_removeIncident, graphpattern_NodePattern_m_getOutgoings, graphpattern_NodePattern_m_getIncident, graphpattern_NodePattern_m_getIncident, graphpattern_NodePattern_m_getOutgoing}

# graphpattern_Pattern class attributes and methods
graphpattern_Pattern_m_getPattern: Method = Method(name="getPattern", parameters={Parameter(name='name')}, type=Pattern)
graphpattern_Pattern_m_getParameter: Method = Method(name="getParameter", parameters={Parameter(name='name')}, type=StringType)
graphpattern_Pattern_m_getGraph: Method = Method(name="getGraph", parameters={Parameter(name='name')}, type=StringType)
graphpattern_Pattern_m_getAllGraphPatterns: Method = Method(name="getAllGraphPatterns", parameters={}, type=StringType)
graphpattern_Pattern.methods={graphpattern_Pattern_m_getGraph, graphpattern_Pattern_m_getParameter, graphpattern_Pattern_m_getPattern, graphpattern_Pattern_m_getAllGraphPatterns}

# graphpattern_DependencyGraph class attributes and methods

# graphpattern_SubGraph class attributes and methods

# GraphElement class attributes and methods

# graphpattern_EdgePattern class attributes and methods

# graphpattern_EClass class attributes and methods

# graphpattern_AttributePattern class attributes and methods
graphpattern_AttributePattern_constant: Property = Property(name="constant", type=StringType)
graphpattern_AttributePattern_value: Property = Property(name="value", type=StringType)
graphpattern_AttributePattern_variables: Property = Property(name="variables", type=StringType)
graphpattern_AttributePattern_m_isConstant: Method = Method(name="isConstant", parameters={}, type=BooleanType)
graphpattern_AttributePattern_m_isVariable: Method = Method(name="isVariable", parameters={}, type=BooleanType)
graphpattern_AttributePattern_m_isExpression: Method = Method(name="isExpression", parameters={}, type=BooleanType)
graphpattern_AttributePattern.attributes={graphpattern_AttributePattern_variables, graphpattern_AttributePattern_value, graphpattern_AttributePattern_constant}
graphpattern_AttributePattern.methods={graphpattern_AttributePattern_m_isConstant, graphpattern_AttributePattern_m_isExpression, graphpattern_AttributePattern_m_isVariable}

# graphpattern_Matching class attributes and methods
graphpattern_Matching_m_iterator: Method = Method(name="iterator", parameters={}, type=StringType)
graphpattern_Matching_m_size: Method = Method(name="size", parameters={}, type=IntegerType)
graphpattern_Matching_m_isEmpty: Method = Method(name="isEmpty", parameters={}, type=BooleanType)
graphpattern_Matching_m_add: Method = Method(name="add", parameters={Parameter(name='match')})
graphpattern_Matching_m_remove: Method = Method(name="remove", parameters={Parameter(name='match')}, type=BooleanType)
graphpattern_Matching_m_contains: Method = Method(name="contains", parameters={Parameter(name='match')}, type=BooleanType)
graphpattern_Matching_m_clear: Method = Method(name="clear", parameters={})
graphpattern_Matching.methods={graphpattern_Matching_m_add, graphpattern_Matching_m_contains, graphpattern_Matching_m_clear, graphpattern_Matching_m_remove, graphpattern_Matching_m_size, graphpattern_Matching_m_iterator, graphpattern_Matching_m_isEmpty}

# graphpattern_Association class attributes and methods

# graphpattern_EReference class attributes and methods

# graphpattern_EAttribute class attributes and methods

# graphpattern_Bundle class attributes and methods

# Pattern class attributes and methods

# graphpattern_Profile class attributes and methods
graphpattern_Profile_name: Property = Property(name="name", type=StringType)
graphpattern_Profile_description: Property = Property(name="description", type=StringType)
graphpattern_Profile_id: Property = Property(name="id", type=StringType)
graphpattern_Profile_m_getStereotype: Method = Method(name="getStereotype", parameters={Parameter(name='name')}, type=StringType)
graphpattern_Profile.attributes={graphpattern_Profile_name, graphpattern_Profile_description, graphpattern_Profile_id}
graphpattern_Profile.methods={graphpattern_Profile_m_getStereotype}

# graphpattern_EObject class attributes and methods

# graphpattern_EPackage class attributes and methods

# graphpattern_Parameter class attributes and methods

# graphpattern_Assignment class attributes and methods

# graphpattern_DependencyNode class attributes and methods

# graphpattern_PatternElement class attributes and methods
graphpattern_PatternElement_name: Property = Property(name="name", type=StringType)
graphpattern_PatternElement_description: Property = Property(name="description", type=StringType)
graphpattern_PatternElement.attributes={graphpattern_PatternElement_description, graphpattern_PatternElement_name}

# Extendable class attributes and methods

# graphpattern_EObjectList class attributes and methods
graphpattern_EObjectList_label: Property = Property(name="label", type=StringType)
graphpattern_EObjectList.attributes={graphpattern_EObjectList_label}

# graphpattern_GraphElement class attributes and methods

# graphpattern_DependencyEdge class attributes and methods

# graphpattern_ValueBinding class attributes and methods
graphpattern_ValueBinding_value: Property = Property(name="value", type=StringType)
graphpattern_ValueBinding.attributes={graphpattern_ValueBinding_value}

# graphpattern_Stereotype class attributes and methods
graphpattern_Stereotype_name: Property = Property(name="name", type=StringType)
graphpattern_Stereotype.attributes={graphpattern_Stereotype_name}

# graphpattern_ParameterBinding class attributes and methods

# graphpattern_ObjectBinding class attributes and methods

# ParameterBinding class attributes and methods

# graphpattern_Resource class attributes and methods

# graphpattern_Extendable class attributes and methods

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="graphpattern_NodePattern", type=graphpattern_GraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_GraphPattern", type=graphpattern_NodePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern1: BinaryAssociation = BinaryAssociation(
    name="pattern1",
    ends={
        Property(name="Pattern", type=graphpattern_GraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
dependencyGraph2: BinaryAssociation = BinaryAssociation(
    name="dependencyGraph2",
    ends={
        Property(name="DependencyGraph", type=graphpattern_GraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=graphpattern_DependencyGraph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subgraphs3: BinaryAssociation = BinaryAssociation(
    name="subgraphs3",
    ends={
        Property(name="graphpattern_SubGraph", type=graphpattern_GraphPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_GraphPattern4", type=graphpattern_SubGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings5: BinaryAssociation = BinaryAssociation(
    name="outgoings5",
    ends={
        Property(name="EdgePattern", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=graphpattern_EdgePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="NodePattern", type=graphpattern_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="graphpattern_EClass", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_NodePattern7", type=graphpattern_EClass, multiplicity=Multiplicity(1, 1))
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="AttributePattern", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=graphpattern_AttributePattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
matching9: BinaryAssociation = BinaryAssociation(
    name="matching9",
    ends={
        Property(name="Matching", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="node10", type=graphpattern_Matching, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
incomings11: BinaryAssociation = BinaryAssociation(
    name="incomings11",
    ends={
        Property(name="EdgePattern12", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=graphpattern_EdgePattern, multiplicity=Multiplicity(0, 9999))
    }
)
associations13: BinaryAssociation = BinaryAssociation(
    name="associations13",
    ends={
        Property(name="Association", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="source14", type=graphpattern_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="graphpattern_AttributePattern", type=graphpattern_EAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_EAttribute", type=graphpattern_AttributePattern, multiplicity=Multiplicity(1, 1))
    }
)
node23: BinaryAssociation = BinaryAssociation(
    name="node23",
    ends={
        Property(name="NodePattern24", type=graphpattern_AttributePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=graphpattern_NodePattern, multiplicity=Multiplicity(0, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="NodePattern17", type=graphpattern_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
opposite19: BinaryAssociation = BinaryAssociation(
    name="opposite19",
    ends={
        Property(name="graphpattern_EdgePattern", type=graphpattern_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_EdgePattern18", type=graphpattern_EdgePattern, multiplicity=Multiplicity(0, 1))
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="graphpattern_EReference", type=graphpattern_EdgePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_EdgePattern21", type=graphpattern_EReference, multiplicity=Multiplicity(1, 1))
    }
)
profiles28: BinaryAssociation = BinaryAssociation(
    name="profiles28",
    ends={
        Property(name="graphpattern_Profile", type=graphpattern_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Bundle", type=graphpattern_Profile, multiplicity=Multiplicity(0, 9999))
    }
)
matches25: BinaryAssociation = BinaryAssociation(
    name="matches25",
    ends={
        Property(name="graphpattern_EObject", type=graphpattern_Matching, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Matching", type=graphpattern_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
node26: BinaryAssociation = BinaryAssociation(
    name="node26",
    ends={
        Property(name="NodePattern27", type=graphpattern_Matching, multiplicity=Multiplicity(1, 1)),
        Property(name="matching", type=graphpattern_NodePattern, multiplicity=Multiplicity(0, 1))
    }
)
assignments34: BinaryAssociation = BinaryAssociation(
    name="assignments34",
    ends={
        Property(name="pattern35", type=graphpattern_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Assignment", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
bundle36: BinaryAssociation = BinaryAssociation(
    name="bundle36",
    ends={
        Property(name="graphpattern_Bundle37", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Pattern", type=graphpattern_Bundle, multiplicity=Multiplicity(0, 1))
    }
)
domains29: BinaryAssociation = BinaryAssociation(
    name="domains29",
    ends={
        Property(name="graphpattern_EPackage", type=graphpattern_Bundle, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Bundle30", type=graphpattern_EPackage, multiplicity=Multiplicity(0, 9999))
    }
)
graphs31: BinaryAssociation = BinaryAssociation(
    name="graphs31",
    ends={
        Property(name="GraphPattern", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=graphpattern_GraphPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters32: BinaryAssociation = BinaryAssociation(
    name="parameters32",
    ends={
        Property(name="Parameter", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern33", type=graphpattern_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
independent45: BinaryAssociation = BinaryAssociation(
    name="independent45",
    ends={
        Property(name="graphpattern_DependencyNode", type=graphpattern_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_DependencyGraph", type=graphpattern_DependencyNode, multiplicity=Multiplicity(0, 9999))
    }
)
graph46: BinaryAssociation = BinaryAssociation(
    name="graph46",
    ends={
        Property(name="GraphPattern47", type=graphpattern_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="dependencyGraph", type=graphpattern_GraphPattern, multiplicity=Multiplicity(0, 1))
    }
)
patterns39: BinaryAssociation = BinaryAssociation(
    name="patterns39",
    ends={
        Property(name="graphpattern_Pattern40", type=graphpattern_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Pattern38", type=graphpattern_Pattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern41: BinaryAssociation = BinaryAssociation(
    name="pattern41",
    ends={
        Property(name="Pattern42", type=graphpattern_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=graphpattern_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
content43: BinaryAssociation = BinaryAssociation(
    name="content43",
    ends={
        Property(name="graphpattern_EObject44", type=graphpattern_EObjectList, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_EObjectList", type=graphpattern_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
source66: BinaryAssociation = BinaryAssociation(
    name="source66",
    ends={
        Property(name="NodePattern67", type=graphpattern_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associations", type=graphpattern_NodePattern, multiplicity=Multiplicity(1, 1))
    }
)
nodes48: BinaryAssociation = BinaryAssociation(
    name="nodes48",
    ends={
        Property(name="graphpattern_DependencyNode50", type=graphpattern_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_DependencyGraph49", type=graphpattern_DependencyNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges51: BinaryAssociation = BinaryAssociation(
    name="edges51",
    ends={
        Property(name="graphpattern_DependencyEdge", type=graphpattern_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_DependencyGraph52", type=graphpattern_DependencyEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoings53: BinaryAssociation = BinaryAssociation(
    name="outgoings53",
    ends={
        Property(name="DependencyEdge", type=graphpattern_DependencyNode, multiplicity=Multiplicity(1, 1)),
        Property(name="source54", type=graphpattern_DependencyEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incomings55: BinaryAssociation = BinaryAssociation(
    name="incomings55",
    ends={
        Property(name="DependencyEdge57", type=graphpattern_DependencyNode, multiplicity=Multiplicity(1, 1)),
        Property(name="target56", type=graphpattern_DependencyEdge, multiplicity=Multiplicity(0, 9999))
    }
)
nodes58: BinaryAssociation = BinaryAssociation(
    name="nodes58",
    ends={
        Property(name="graphpattern_NodePattern60", type=graphpattern_DependencyNode, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_DependencyNode59", type=graphpattern_NodePattern, multiplicity=Multiplicity(0, 9999))
    }
)
source61: BinaryAssociation = BinaryAssociation(
    name="source61",
    ends={
        Property(name="DependencyNode", type=graphpattern_DependencyEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoings62", type=graphpattern_DependencyNode, multiplicity=Multiplicity(0, 1))
    }
)
target63: BinaryAssociation = BinaryAssociation(
    name="target63",
    ends={
        Property(name="DependencyNode65", type=graphpattern_DependencyEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomings64", type=graphpattern_DependencyNode, multiplicity=Multiplicity(0, 1))
    }
)
target68: BinaryAssociation = BinaryAssociation(
    name="target68",
    ends={
        Property(name="graphpattern_GraphElement", type=graphpattern_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Association", type=graphpattern_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
profile69: BinaryAssociation = BinaryAssociation(
    name="profile69",
    ends={
        Property(name="Profile", type=graphpattern_Stereotype, multiplicity=Multiplicity(1, 1)),
        Property(name="stereotypes", type=graphpattern_Profile, multiplicity=Multiplicity(1, 1))
    }
)
parameter70: BinaryAssociation = BinaryAssociation(
    name="parameter70",
    ends={
        Property(name="graphpattern_Parameter", type=graphpattern_ParameterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_ParameterBinding", type=graphpattern_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
assignment71: BinaryAssociation = BinaryAssociation(
    name="assignment71",
    ends={
        Property(name="graphpattern_ParameterBinding72", type=graphpattern_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Assignment", type=graphpattern_ParameterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern73: BinaryAssociation = BinaryAssociation(
    name="pattern73",
    ends={
        Property(name="Pattern74", type=graphpattern_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignments", type=graphpattern_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
value75: BinaryAssociation = BinaryAssociation(
    name="value75",
    ends={
        Property(name="graphpattern_EObject76", type=graphpattern_ObjectBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_ObjectBinding", type=graphpattern_EObject, multiplicity=Multiplicity(0, 1))
    }
)
elements77: BinaryAssociation = BinaryAssociation(
    name="elements77",
    ends={
        Property(name="GraphElement", type=graphpattern_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="subgraphs", type=graphpattern_GraphElement, multiplicity=Multiplicity(0, 9999))
    }
)
subgraphs79: BinaryAssociation = BinaryAssociation(
    name="subgraphs79",
    ends={
        Property(name="graphpattern_SubGraph80", type=graphpattern_SubGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_SubGraph78", type=graphpattern_SubGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subgraphs81: BinaryAssociation = BinaryAssociation(
    name="subgraphs81",
    ends={
        Property(name="SubGraph", type=graphpattern_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=graphpattern_SubGraph, multiplicity=Multiplicity(0, 9999))
    }
)
graph82: BinaryAssociation = BinaryAssociation(
    name="graph82",
    ends={
        Property(name="graphpattern_GraphPattern84", type=graphpattern_GraphElement, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_GraphElement83", type=graphpattern_GraphPattern, multiplicity=Multiplicity(1, 1))
    }
)
stereotypes85: BinaryAssociation = BinaryAssociation(
    name="stereotypes85",
    ends={
        Property(name="Stereotype", type=graphpattern_Profile, multiplicity=Multiplicity(1, 1)),
        Property(name="profile", type=graphpattern_Stereotype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents86: BinaryAssociation = BinaryAssociation(
    name="contents86",
    ends={
        Property(name="graphpattern_EObject87", type=graphpattern_Resource, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Resource", type=graphpattern_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stereotypes88: BinaryAssociation = BinaryAssociation(
    name="stereotypes88",
    ends={
        Property(name="graphpattern_Stereotype", type=graphpattern_Extendable, multiplicity=Multiplicity(1, 1)),
        Property(name="graphpattern_Extendable", type=graphpattern_Stereotype, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_graphpattern_GraphPattern_PatternElement = Generalization(general=PatternElement, specific=graphpattern_GraphPattern)
gen_graphpattern_NodePattern_GraphElement = Generalization(general=GraphElement, specific=graphpattern_NodePattern)
gen_graphpattern_EdgePattern_GraphElement = Generalization(general=GraphElement, specific=graphpattern_EdgePattern)
gen_graphpattern_AttributePattern_GraphElement = Generalization(general=GraphElement, specific=graphpattern_AttributePattern)
gen_graphpattern_Bundle_Pattern = Generalization(general=Pattern, specific=graphpattern_Bundle)
gen_graphpattern_Pattern_PatternElement = Generalization(general=PatternElement, specific=graphpattern_Pattern)
gen_graphpattern_PatternElement_Extendable = Generalization(general=Extendable, specific=graphpattern_PatternElement)
gen_graphpattern_Parameter_PatternElement = Generalization(general=PatternElement, specific=graphpattern_Parameter)
gen_graphpattern_Association_PatternElement = Generalization(general=PatternElement, specific=graphpattern_Association)
gen_graphpattern_ValueBinding_ParameterBinding = Generalization(general=ParameterBinding, specific=graphpattern_ValueBinding)
gen_graphpattern_SubGraph_PatternElement = Generalization(general=PatternElement, specific=graphpattern_SubGraph)
gen_graphpattern_ObjectBinding_ParameterBinding = Generalization(general=ParameterBinding, specific=graphpattern_ObjectBinding)
gen_graphpattern_GraphElement_PatternElement = Generalization(general=PatternElement, specific=graphpattern_GraphElement)

# Domain Model
domain_model = DomainModel(
    name="graphpattern",
    types={graphpattern_GraphPattern, PatternElement, graphpattern_NodePattern, graphpattern_Pattern, graphpattern_DependencyGraph, graphpattern_SubGraph, GraphElement, graphpattern_EdgePattern, graphpattern_EClass, graphpattern_AttributePattern, graphpattern_Matching, graphpattern_Association, graphpattern_EReference, graphpattern_EAttribute, graphpattern_Bundle, Pattern, graphpattern_Profile, graphpattern_EObject, graphpattern_EPackage, graphpattern_Parameter, graphpattern_Assignment, graphpattern_DependencyNode, graphpattern_PatternElement, Extendable, graphpattern_EObjectList, graphpattern_GraphElement, graphpattern_DependencyEdge, graphpattern_ValueBinding, graphpattern_Stereotype, graphpattern_ParameterBinding, graphpattern_ObjectBinding, ParameterBinding, graphpattern_Resource, graphpattern_Extendable},
    associations={nodes0, pattern1, dependencyGraph2, subgraphs3, outgoings5, target15, type6, attributes8, matching9, incomings11, associations13, type22, node23, source16, opposite19, type20, profiles28, matches25, node26, assignments34, bundle36, domains29, graphs31, parameters32, independent45, graph46, patterns39, pattern41, content43, source66, nodes48, edges51, outgoings53, incomings55, nodes58, source61, target63, target68, profile69, parameter70, assignment71, pattern73, value75, elements77, subgraphs79, subgraphs81, graph82, stereotypes85, contents86, stereotypes88},
    generalizations={gen_graphpattern_GraphPattern_PatternElement, gen_graphpattern_NodePattern_GraphElement, gen_graphpattern_EdgePattern_GraphElement, gen_graphpattern_AttributePattern_GraphElement, gen_graphpattern_Bundle_Pattern, gen_graphpattern_Pattern_PatternElement, gen_graphpattern_PatternElement_Extendable, gen_graphpattern_Parameter_PatternElement, gen_graphpattern_Association_PatternElement, gen_graphpattern_ValueBinding_ParameterBinding, gen_graphpattern_SubGraph_PatternElement, gen_graphpattern_ObjectBinding_ParameterBinding, gen_graphpattern_GraphElement_PatternElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)