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
Quantifier: Enumeration = Enumeration(
    name="Quantifier",
    literals={
            EnumerationLiteral(name="EXISTS"),
			EnumerationLiteral(name="FORALL")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="NOT"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR"),
			EnumerationLiteral(name="IMPLIES")
    }
)

# Classes
GraphConstraint_NestedGraphCondition = Class(name="GraphConstraint::NestedGraphCondition", is_abstract=True)
GraphConstraint_Graph = Class(name="GraphConstraint::Graph")
GraphConstraint_Edge = Class(name="GraphConstraint::Edge")
GraphConstraint_Node = Class(name="GraphConstraint::Node")
GraphConstraint_GraphElement = Class(name="GraphConstraint::GraphElement", is_abstract=True)
GraphConstraint_NestedGraphConstraint = Class(name="GraphConstraint::NestedGraphConstraint")
GraphConstraint_EPackage = Class(name="GraphConstraint::EPackage")
GraphConstraint_EAttribute = Class(name="GraphConstraint::EAttribute")
GraphConstraint_Mapping = Class(name="GraphConstraint::Mapping")
GraphElement = Class(name="GraphElement")
GraphConstraint_Attribute = Class(name="GraphConstraint::Attribute")
GraphConstraint_EClass = Class(name="GraphConstraint::EClass")
GraphConstraint_EReference = Class(name="GraphConstraint::EReference")
GraphConstraint_ElementMapping = Class(name="GraphConstraint::ElementMapping")
GraphConstraint_QuantifiedGraphCondition = Class(name="GraphConstraint::QuantifiedGraphCondition")
NestedGraphCondition = Class(name="NestedGraphCondition")
GraphConstraint_True = Class(name="GraphConstraint::True")
GraphConstraint_Formula = Class(name="GraphConstraint::Formula")
GraphConstraint_Variable = Class(name="GraphConstraint::Variable")
GraphConstraint_EDataType = Class(name="GraphConstraint::EDataType")

# GraphConstraint_NestedGraphCondition class attributes and methods

# GraphConstraint_Graph class attributes and methods

# GraphConstraint_Edge class attributes and methods

# GraphConstraint_Node class attributes and methods

# GraphConstraint_GraphElement class attributes and methods
GraphConstraint_GraphElement_name: Property = Property(name="name", type=StringType)
GraphConstraint_GraphElement.attributes={GraphConstraint_GraphElement_name}

# GraphConstraint_NestedGraphConstraint class attributes and methods
GraphConstraint_NestedGraphConstraint_name: Property = Property(name="name", type=StringType)
GraphConstraint_NestedGraphConstraint.attributes={GraphConstraint_NestedGraphConstraint_name}

# GraphConstraint_EPackage class attributes and methods

# GraphConstraint_EAttribute class attributes and methods

# GraphConstraint_Mapping class attributes and methods

# GraphElement class attributes and methods

# GraphConstraint_Attribute class attributes and methods
GraphConstraint_Attribute_op: Property = Property(name="op", type=StringType)
GraphConstraint_Attribute_value: Property = Property(name="value", type=StringType)
GraphConstraint_Attribute.attributes={GraphConstraint_Attribute_op, GraphConstraint_Attribute_value}

# GraphConstraint_EClass class attributes and methods

# GraphConstraint_EReference class attributes and methods

# GraphConstraint_ElementMapping class attributes and methods

# GraphConstraint_QuantifiedGraphCondition class attributes and methods
GraphConstraint_QuantifiedGraphCondition_quantifier: Property = Property(name="quantifier", type=StringType)
GraphConstraint_QuantifiedGraphCondition.attributes={GraphConstraint_QuantifiedGraphCondition_quantifier}

# NestedGraphCondition class attributes and methods

# GraphConstraint_True class attributes and methods

# GraphConstraint_Formula class attributes and methods
GraphConstraint_Formula_op: Property = Property(name="op", type=StringType)
GraphConstraint_Formula.attributes={GraphConstraint_Formula_op}

# GraphConstraint_Variable class attributes and methods
GraphConstraint_Variable_name: Property = Property(name="name", type=StringType)
GraphConstraint_Variable.attributes={GraphConstraint_Variable_name}

# GraphConstraint_EDataType class attributes and methods

# Relationships
condition4: BinaryAssociation = BinaryAssociation(
    name="condition4",
    ends={
        Property(name="NestedGraphCondition", type=GraphConstraint_NestedGraphConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="gc", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
emptyDomain5: BinaryAssociation = BinaryAssociation(
    name="emptyDomain5",
    ends={
        Property(name="GraphConstraint_Graph7", type=GraphConstraint_NestedGraphConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_NestedGraphConstraint6", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
edges0: BinaryAssociation = BinaryAssociation(
    name="edges0",
    ends={
        Property(name="GraphConstraint_Edge", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Graph", type=GraphConstraint_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="GraphConstraint_Node", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Graph2", type=GraphConstraint_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
import3: BinaryAssociation = BinaryAssociation(
    name="import3",
    ends={
        Property(name="GraphConstraint_EPackage", type=GraphConstraint_NestedGraphConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_NestedGraphConstraint", type=GraphConstraint_EPackage, multiplicity=Multiplicity(1, 1))
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="GraphConstraint_EAttribute", type=GraphConstraint_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Attribute21", type=GraphConstraint_EAttribute, multiplicity=Multiplicity(1, 1))
    }
)
from22: BinaryAssociation = BinaryAssociation(
    name="from22",
    ends={
        Property(name="GraphConstraint_Graph23", type=GraphConstraint_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Mapping", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1))
    }
)
attributes8: BinaryAssociation = BinaryAssociation(
    name="attributes8",
    ends={
        Property(name="GraphConstraint_Attribute", type=GraphConstraint_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Node9", type=GraphConstraint_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="GraphConstraint_EClass", type=GraphConstraint_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Node11", type=GraphConstraint_EClass, multiplicity=Multiplicity(1, 1))
    }
)
src12: BinaryAssociation = BinaryAssociation(
    name="src12",
    ends={
        Property(name="GraphConstraint_Node14", type=GraphConstraint_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Edge13", type=GraphConstraint_Node, multiplicity=Multiplicity(1, 1))
    }
)
tgt15: BinaryAssociation = BinaryAssociation(
    name="tgt15",
    ends={
        Property(name="GraphConstraint_Node17", type=GraphConstraint_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Edge16", type=GraphConstraint_Node, multiplicity=Multiplicity(1, 1))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="GraphConstraint_EReference", type=GraphConstraint_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Edge19", type=GraphConstraint_EReference, multiplicity=Multiplicity(1, 1))
    }
)
codomain34: BinaryAssociation = BinaryAssociation(
    name="codomain34",
    ends={
        Property(name="GraphConstraint_QuantifiedGraphCondition", type=GraphConstraint_Graph, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="GraphConstraint_Graph35", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(1, 1))
    }
)
restriction36: BinaryAssociation = BinaryAssociation(
    name="restriction36",
    ends={
        Property(name="GraphConstraint_Graph38", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_QuantifiedGraphCondition37", type=GraphConstraint_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
restrictionMapping39: BinaryAssociation = BinaryAssociation(
    name="restrictionMapping39",
    ends={
        Property(name="GraphConstraint_Mapping41", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_QuantifiedGraphCondition40", type=GraphConstraint_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to24: BinaryAssociation = BinaryAssociation(
    name="to24",
    ends={
        Property(name="GraphConstraint_Graph26", type=GraphConstraint_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Mapping25", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1))
    }
)
mappings27: BinaryAssociation = BinaryAssociation(
    name="mappings27",
    ends={
        Property(name="GraphConstraint_ElementMapping", type=GraphConstraint_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Mapping28", type=GraphConstraint_ElementMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
origin29: BinaryAssociation = BinaryAssociation(
    name="origin29",
    ends={
        Property(name="GraphConstraint_GraphElement", type=GraphConstraint_ElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_ElementMapping30", type=GraphConstraint_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
image31: BinaryAssociation = BinaryAssociation(
    name="image31",
    ends={
        Property(name="GraphConstraint_GraphElement33", type=GraphConstraint_ElementMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_ElementMapping32", type=GraphConstraint_GraphElement, multiplicity=Multiplicity(1, 1))
    }
)
formula50: BinaryAssociation = BinaryAssociation(
    name="formula50",
    ends={
        Property(name="Formula", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="args", type=GraphConstraint_Formula, multiplicity=Multiplicity(0, 1))
    }
)
codomainMapping42: BinaryAssociation = BinaryAssociation(
    name="codomainMapping42",
    ends={
        Property(name="GraphConstraint_Mapping44", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_QuantifiedGraphCondition43", type=GraphConstraint_Mapping, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nested45: BinaryAssociation = BinaryAssociation(
    name="nested45",
    ends={
        Property(name="NestedGraphCondition46", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="qgc", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
args47: BinaryAssociation = BinaryAssociation(
    name="args47",
    ends={
        Property(name="NestedGraphCondition48", type=GraphConstraint_Formula, multiplicity=Multiplicity(1, 1)),
        Property(name="formula", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="GraphConstraint_EDataType", type=GraphConstraint_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_Variable", type=GraphConstraint_EDataType, multiplicity=Multiplicity(1, 1))
    }
)
qgc51: BinaryAssociation = BinaryAssociation(
    name="qgc51",
    ends={
        Property(name="QuantifiedGraphCondition", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="nested", type=GraphConstraint_QuantifiedGraphCondition, multiplicity=Multiplicity(0, 1))
    }
)
gc52: BinaryAssociation = BinaryAssociation(
    name="gc52",
    ends={
        Property(name="NestedGraphConstraint", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="condition", type=GraphConstraint_NestedGraphConstraint, multiplicity=Multiplicity(0, 1))
    }
)
domain53: BinaryAssociation = BinaryAssociation(
    name="domain53",
    ends={
        Property(name="GraphConstraint_Graph54", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_NestedGraphCondition", type=GraphConstraint_Graph, multiplicity=Multiplicity(1, 1))
    }
)
vars55: BinaryAssociation = BinaryAssociation(
    name="vars55",
    ends={
        Property(name="GraphConstraint_Variable57", type=GraphConstraint_NestedGraphCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConstraint_NestedGraphCondition56", type=GraphConstraint_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_GraphConstraint_Node_GraphElement = Generalization(general=GraphElement, specific=GraphConstraint_Node)
gen_GraphConstraint_Edge_GraphElement = Generalization(general=GraphElement, specific=GraphConstraint_Edge)
gen_GraphConstraint_Attribute_GraphElement = Generalization(general=GraphElement, specific=GraphConstraint_Attribute)
gen_GraphConstraint_QuantifiedGraphCondition_NestedGraphCondition = Generalization(general=NestedGraphCondition, specific=GraphConstraint_QuantifiedGraphCondition)
gen_GraphConstraint_True_NestedGraphCondition = Generalization(general=NestedGraphCondition, specific=GraphConstraint_True)
gen_GraphConstraint_Formula_NestedGraphCondition = Generalization(general=NestedGraphCondition, specific=GraphConstraint_Formula)

# Domain Model
domain_model = DomainModel(
    name="GraphConstraint",
    types={GraphConstraint_NestedGraphCondition, GraphConstraint_Graph, GraphConstraint_Edge, GraphConstraint_Node, GraphConstraint_GraphElement, GraphConstraint_NestedGraphConstraint, GraphConstraint_EPackage, GraphConstraint_EAttribute, GraphConstraint_Mapping, GraphElement, GraphConstraint_Attribute, GraphConstraint_EClass, GraphConstraint_EReference, GraphConstraint_ElementMapping, GraphConstraint_QuantifiedGraphCondition, NestedGraphCondition, GraphConstraint_True, GraphConstraint_Formula, GraphConstraint_Variable, GraphConstraint_EDataType, Quantifier, Operator},
    associations={condition4, emptyDomain5, edges0, nodes1, import3, type20, from22, attributes8, type10, src12, tgt15, type18, codomain34, restriction36, restrictionMapping39, to24, mappings27, origin29, image31, formula50, codomainMapping42, nested45, args47, type49, qgc51, gc52, domain53, vars55},
    generalizations={gen_GraphConstraint_Node_GraphElement, gen_GraphConstraint_Edge_GraphElement, gen_GraphConstraint_Attribute_GraphElement, gen_GraphConstraint_QuantifiedGraphCondition_NestedGraphCondition, gen_GraphConstraint_True_NestedGraphCondition, gen_GraphConstraint_Formula_NestedGraphCondition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)