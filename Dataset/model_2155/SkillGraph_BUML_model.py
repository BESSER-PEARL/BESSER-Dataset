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
Category: Enumeration = Enumeration(
    name="Category",
    literals={
            EnumerationLiteral(name="main"),
			EnumerationLiteral(name="observable_external_behavior"),
			EnumerationLiteral(name="perception"),
			EnumerationLiteral(name="planning"),
			EnumerationLiteral(name="action"),
			EnumerationLiteral(name="sensor"),
			EnumerationLiteral(name="actuator")
    }
)

Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="Functional_Safety_Requirement"),
			EnumerationLiteral(name="Technical_Safety_Requirement"),
			EnumerationLiteral(name="Technical_Requirement")
    }
)

# Classes
SkillGraph_Parameter = Class(name="SkillGraph::Parameter")
SkillGraph_Graph = Class(name="SkillGraph::Graph")
SkillGraph_Node = Class(name="SkillGraph::Node")
SkillGraph_Equation = Class(name="SkillGraph::Equation")
SkillGraph_Edge = Class(name="SkillGraph::Edge")
SkillGraph_Requirement = Class(name="SkillGraph::Requirement")

# SkillGraph_Parameter class attributes and methods
SkillGraph_Parameter_name: Property = Property(name="name", type=StringType)
SkillGraph_Parameter_unit: Property = Property(name="unit", type=StringType)
SkillGraph_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
SkillGraph_Parameter_abbreviation: Property = Property(name="abbreviation", type=StringType)
SkillGraph_Parameter_variable: Property = Property(name="variable", type=BooleanType)
SkillGraph_Parameter.attributes={SkillGraph_Parameter_variable, SkillGraph_Parameter_defaultValue, SkillGraph_Parameter_abbreviation, SkillGraph_Parameter_unit, SkillGraph_Parameter_name}

# SkillGraph_Graph class attributes and methods

# SkillGraph_Node class attributes and methods
SkillGraph_Node_category: Property = Property(name="category", type=StringType)
SkillGraph_Node_name: Property = Property(name="name", type=StringType)
SkillGraph_Node_programPath: Property = Property(name="programPath", type=StringType)
SkillGraph_Node.attributes={SkillGraph_Node_programPath, SkillGraph_Node_name, SkillGraph_Node_category}

# SkillGraph_Equation class attributes and methods
SkillGraph_Equation_equation: Property = Property(name="equation", type=StringType)
SkillGraph_Equation.attributes={SkillGraph_Equation_equation}

# SkillGraph_Edge class attributes and methods

# SkillGraph_Requirement class attributes and methods
SkillGraph_Requirement_comment: Property = Property(name="comment", type=StringType)
SkillGraph_Requirement_term: Property = Property(name="term", type=StringType)
SkillGraph_Requirement_type: Property = Property(name="type", type=StringType)
SkillGraph_Requirement.attributes={SkillGraph_Requirement_type, SkillGraph_Requirement_term, SkillGraph_Requirement_comment}

# Relationships
parentNode17: BinaryAssociation = BinaryAssociation(
    name="parentNode17",
    ends={
        Property(name="SkillGraph_Node19", type=SkillGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Edge18", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)
childNode20: BinaryAssociation = BinaryAssociation(
    name="childNode20",
    ends={
        Property(name="SkillGraph_Node22", type=SkillGraph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Edge21", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)
graph0: BinaryAssociation = BinaryAssociation(
    name="graph0",
    ends={
        Property(name="Graph", type=SkillGraph_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterList", type=SkillGraph_Graph, multiplicity=Multiplicity(1, 1))
    }
)
nodes1: BinaryAssociation = BinaryAssociation(
    name="nodes1",
    ends={
        Property(name="SkillGraph_Node", type=SkillGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Graph", type=SkillGraph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootNode2: BinaryAssociation = BinaryAssociation(
    name="rootNode2",
    ends={
        Property(name="SkillGraph_Node4", type=SkillGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Graph3", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterList5: BinaryAssociation = BinaryAssociation(
    name="parameterList5",
    ends={
        Property(name="Parameter", type=SkillGraph_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=SkillGraph_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equations6: BinaryAssociation = BinaryAssociation(
    name="equations6",
    ends={
        Property(name="Equation", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=SkillGraph_Equation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childEdges7: BinaryAssociation = BinaryAssociation(
    name="childEdges7",
    ends={
        Property(name="SkillGraph_Edge", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Node8", type=SkillGraph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNodes10: BinaryAssociation = BinaryAssociation(
    name="parentNodes10",
    ends={
        Property(name="SkillGraph_Node11", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="SkillGraph_Node9", type=SkillGraph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
requirements12: BinaryAssociation = BinaryAssociation(
    name="requirements12",
    ends={
        Property(name="Requirement", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node13", type=SkillGraph_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node14: BinaryAssociation = BinaryAssociation(
    name="node14",
    ends={
        Property(name="Node", type=SkillGraph_Requirement, multiplicity=Multiplicity(1, 1)),
        Property(name="requirements", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)
node15: BinaryAssociation = BinaryAssociation(
    name="node15",
    ends={
        Property(name="Node16", type=SkillGraph_Equation, multiplicity=Multiplicity(1, 1)),
        Property(name="equations", type=SkillGraph_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="SkillGraph",
    types={SkillGraph_Parameter, SkillGraph_Graph, SkillGraph_Node, SkillGraph_Equation, SkillGraph_Edge, SkillGraph_Requirement, Category, Type},
    associations={parentNode17, childNode20, graph0, nodes1, rootNode2, parameterList5, equations6, childEdges7, parentNodes10, requirements12, node14, node15},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)