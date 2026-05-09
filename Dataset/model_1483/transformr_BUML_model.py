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
transformr_Edge = Class(name="transformr_Edge")
transformr_Attribute = Class(name="transformr_Attribute")
transformr_Graph = Class(name="transformr_Graph")
NamedElement = Class(name="NamedElement")
transformr_Node = Class(name="transformr_Node")
GraphElement = Class(name="GraphElement")
transformr_And = Class(name="transformr_And")
BinaryConstraint = Class(name="BinaryConstraint")
transformr_Or = Class(name="transformr_Or")
transformr_Not = Class(name="transformr_Not")
transformr_Pattern = Class(name="transformr_Pattern")
Graph = Class(name="Graph")
transformr_Constraint = Class(name="transformr_Constraint", is_abstract=True)
transformr_Variable = Class(name="transformr_Variable")
transformr_Rule = Class(name="transformr_Rule")
Pattern = Class(name="Pattern")
Executable = Class(name="Executable")
transformr_GraphElement = Class(name="transformr_GraphElement", is_abstract=True)
transformr_Assignment = Class(name="transformr_Assignment")
TypedElement = Class(name="TypedElement")
transformr_NamedElement = Class(name="transformr_NamedElement", is_abstract=True)
transformr_TypedElement = Class(name="transformr_TypedElement", is_abstract=True)
transformr_PatternConstraint = Class(name="transformr_PatternConstraint", is_abstract=True)
Constraint = Class(name="Constraint")
transformr_Exists = Class(name="transformr_Exists")
PatternConstraint = Class(name="PatternConstraint")
transformr_ForAll = Class(name="transformr_ForAll")
transformr_BinaryConstraint = Class(name="transformr_BinaryConstraint", is_abstract=True)
transformr_Expression = Class(name="transformr_Expression")
transformr_VariableConstraint = Class(name="transformr_VariableConstraint")
Expression = Class(name="Expression")
transformr_Executable = Class(name="transformr_Executable", is_abstract=True)
transformr_Branch = Class(name="transformr_Branch")
transformr_Block = Class(name="transformr_Block")

# transformr_Edge class attributes and methods
transformr_Edge_m_setEType: Method = Method(name="setEType", parameters={Parameter(name='transformr_ereference', type=StringType)})
transformr_Edge_m_getSource: Method = Method(name="getSource", parameters={}, type=StringType)
transformr_Edge_m_setSource: Method = Method(name="setSource", parameters={Parameter(name='transformr_source', type=StringType)})
transformr_Edge.methods={transformr_Edge_m_setSource, transformr_Edge_m_setEType, transformr_Edge_m_getSource}

# transformr_Attribute class attributes and methods
transformr_Attribute_m_setEType: Method = Method(name="setEType", parameters={Parameter(name='transformr_eattribute', type=StringType)})
transformr_Attribute.methods={transformr_Attribute_m_setEType}

# transformr_Graph class attributes and methods

# NamedElement class attributes and methods

# transformr_Node class attributes and methods
transformr_Node_m_setEType: Method = Method(name="setEType", parameters={Parameter(name='transformr_eclass', type=StringType)})
transformr_Node.methods={transformr_Node_m_setEType}

# GraphElement class attributes and methods

# transformr_And class attributes and methods

# BinaryConstraint class attributes and methods

# transformr_Or class attributes and methods

# transformr_Not class attributes and methods

# transformr_Pattern class attributes and methods

# Graph class attributes and methods

# transformr_Constraint class attributes and methods

# transformr_Variable class attributes and methods

# transformr_Rule class attributes and methods

# Pattern class attributes and methods

# Executable class attributes and methods

# transformr_GraphElement class attributes and methods

# transformr_Assignment class attributes and methods

# TypedElement class attributes and methods

# transformr_NamedElement class attributes and methods
transformr_NamedElement_name: Property = Property(name="name", type=StringType)
transformr_NamedElement.attributes={transformr_NamedElement_name}

# transformr_TypedElement class attributes and methods
transformr_TypedElement_type: Property = Property(name="type", type=StringType)
transformr_TypedElement.attributes={transformr_TypedElement_type}

# transformr_PatternConstraint class attributes and methods

# Constraint class attributes and methods

# transformr_Exists class attributes and methods

# PatternConstraint class attributes and methods

# transformr_ForAll class attributes and methods

# transformr_BinaryConstraint class attributes and methods

# transformr_Expression class attributes and methods
transformr_Expression_expression: Property = Property(name="expression", type=StringType)
transformr_Expression.attributes={transformr_Expression_expression}

# transformr_VariableConstraint class attributes and methods

# Expression class attributes and methods

# transformr_Executable class attributes and methods

# transformr_Branch class attributes and methods

# transformr_Block class attributes and methods

# Relationships
edges1: BinaryAssociation = BinaryAssociation(
    name="edges1",
    ends={
        Property(name="transformr_Edge", type=transformr_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Node2", type=transformr_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="transformr_Attribute", type=transformr_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Node4", type=transformr_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="transformr_Node", type=transformr_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Graph", type=transformr_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subpattern17: BinaryAssociation = BinaryAssociation(
    name="subpattern17",
    ends={
        Property(name="transformr_Pattern18", type=transformr_PatternConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_PatternConstraint", type=transformr_Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="transformr_Node7", type=transformr_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Edge6", type=transformr_Node, multiplicity=Multiplicity(1, 1))
    }
)
constraint8: BinaryAssociation = BinaryAssociation(
    name="constraint8",
    ends={
        Property(name="transformr_Constraint", type=transformr_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Pattern", type=transformr_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variables9: BinaryAssociation = BinaryAssociation(
    name="variables9",
    ends={
        Property(name="transformr_Variable", type=transformr_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Pattern10", type=transformr_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
creations11: BinaryAssociation = BinaryAssociation(
    name="creations11",
    ends={
        Property(name="transformr_GraphElement", type=transformr_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Rule", type=transformr_GraphElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
deletions12: BinaryAssociation = BinaryAssociation(
    name="deletions12",
    ends={
        Property(name="transformr_GraphElement14", type=transformr_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Rule13", type=transformr_GraphElement, multiplicity=Multiplicity(0, 9999))
    }
)
assignments15: BinaryAssociation = BinaryAssociation(
    name="assignments15",
    ends={
        Property(name="transformr_Assignment", type=transformr_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Rule16", type=transformr_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
child19: BinaryAssociation = BinaryAssociation(
    name="child19",
    ends={
        Property(name="transformr_Constraint20", type=transformr_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Not", type=transformr_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="transformr_Constraint22", type=transformr_BinaryConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_BinaryConstraint", type=transformr_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="transformr_Constraint25", type=transformr_BinaryConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_BinaryConstraint24", type=transformr_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetAttribute26: BinaryAssociation = BinaryAssociation(
    name="targetAttribute26",
    ends={
        Property(name="transformr_Attribute28", type=transformr_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Variable27", type=transformr_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
involvedVariables29: BinaryAssociation = BinaryAssociation(
    name="involvedVariables29",
    ends={
        Property(name="transformr_Variable30", type=transformr_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Expression", type=transformr_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
targetVariable31: BinaryAssociation = BinaryAssociation(
    name="targetVariable31",
    ends={
        Property(name="transformr_Variable33", type=transformr_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Assignment32", type=transformr_Variable, multiplicity=Multiplicity(1, 1))
    }
)
if_34: BinaryAssociation = BinaryAssociation(
    name="if_34",
    ends={
        Property(name="transformr_Pattern35", type=transformr_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Branch", type=transformr_Pattern, multiplicity=Multiplicity(0, 1))
    }
)
then36: BinaryAssociation = BinaryAssociation(
    name="then36",
    ends={
        Property(name="transformr_Executable", type=transformr_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Branch37", type=transformr_Executable, multiplicity=Multiplicity(1, 1))
    }
)
else_38: BinaryAssociation = BinaryAssociation(
    name="else_38",
    ends={
        Property(name="transformr_Executable40", type=transformr_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Branch39", type=transformr_Executable, multiplicity=Multiplicity(1, 1))
    }
)
children41: BinaryAssociation = BinaryAssociation(
    name="children41",
    ends={
        Property(name="transformr_Executable42", type=transformr_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="transformr_Block", type=transformr_Executable, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_transformr_Edge_GraphElement = Generalization(general=GraphElement, specific=transformr_Edge)
gen_transformr_Graph_NamedElement = Generalization(general=NamedElement, specific=transformr_Graph)
gen_transformr_Node_GraphElement = Generalization(general=GraphElement, specific=transformr_Node)
gen_transformr_And_BinaryConstraint = Generalization(general=BinaryConstraint, specific=transformr_And)
gen_transformr_Or_BinaryConstraint = Generalization(general=BinaryConstraint, specific=transformr_Or)
gen_transformr_Not_Constraint = Generalization(general=Constraint, specific=transformr_Not)
gen_transformr_Pattern_Graph = Generalization(general=Graph, specific=transformr_Pattern)
gen_transformr_Rule_Pattern = Generalization(general=Pattern, specific=transformr_Rule)
gen_transformr_Rule_Executable = Generalization(general=Executable, specific=transformr_Rule)
gen_transformr_GraphElement_TypedElement = Generalization(general=TypedElement, specific=transformr_GraphElement)
gen_transformr_GraphElement_NamedElement = Generalization(general=NamedElement, specific=transformr_GraphElement)
gen_transformr_Attribute_TypedElement = Generalization(general=TypedElement, specific=transformr_Attribute)
gen_transformr_Attribute_NamedElement = Generalization(general=NamedElement, specific=transformr_Attribute)
gen_transformr_PatternConstraint_Constraint = Generalization(general=Constraint, specific=transformr_PatternConstraint)
gen_transformr_Exists_PatternConstraint = Generalization(general=PatternConstraint, specific=transformr_Exists)
gen_transformr_ForAll_PatternConstraint = Generalization(general=PatternConstraint, specific=transformr_ForAll)
gen_transformr_BinaryConstraint_Constraint = Generalization(general=Constraint, specific=transformr_BinaryConstraint)
gen_transformr_Variable_NamedElement = Generalization(general=NamedElement, specific=transformr_Variable)
gen_transformr_VariableConstraint_Expression = Generalization(general=Expression, specific=transformr_VariableConstraint)
gen_transformr_VariableConstraint_Constraint = Generalization(general=Constraint, specific=transformr_VariableConstraint)
gen_transformr_Assignment_Expression = Generalization(general=Expression, specific=transformr_Assignment)
gen_transformr_Executable_NamedElement = Generalization(general=NamedElement, specific=transformr_Executable)
gen_transformr_Branch_Executable = Generalization(general=Executable, specific=transformr_Branch)
gen_transformr_Block_Executable = Generalization(general=Executable, specific=transformr_Block)

# Domain Model
domain_model = DomainModel(
    name="transformr",
    types={transformr_Edge, transformr_Attribute, transformr_Graph, NamedElement, transformr_Node, GraphElement, transformr_And, BinaryConstraint, transformr_Or, transformr_Not, transformr_Pattern, Graph, transformr_Constraint, transformr_Variable, transformr_Rule, Pattern, Executable, transformr_GraphElement, transformr_Assignment, TypedElement, transformr_NamedElement, transformr_TypedElement, transformr_PatternConstraint, Constraint, transformr_Exists, PatternConstraint, transformr_ForAll, transformr_BinaryConstraint, transformr_Expression, transformr_VariableConstraint, Expression, transformr_Executable, transformr_Branch, transformr_Block},
    associations={edges1, attributes3, nodes0, subpattern17, target5, constraint8, variables9, creations11, deletions12, assignments15, child19, left21, right23, targetAttribute26, involvedVariables29, targetVariable31, if_34, then36, else_38, children41},
    generalizations={gen_transformr_Edge_GraphElement, gen_transformr_Graph_NamedElement, gen_transformr_Node_GraphElement, gen_transformr_And_BinaryConstraint, gen_transformr_Or_BinaryConstraint, gen_transformr_Not_Constraint, gen_transformr_Pattern_Graph, gen_transformr_Rule_Pattern, gen_transformr_Rule_Executable, gen_transformr_GraphElement_TypedElement, gen_transformr_GraphElement_NamedElement, gen_transformr_Attribute_TypedElement, gen_transformr_Attribute_NamedElement, gen_transformr_PatternConstraint_Constraint, gen_transformr_Exists_PatternConstraint, gen_transformr_ForAll_PatternConstraint, gen_transformr_BinaryConstraint_Constraint, gen_transformr_Variable_NamedElement, gen_transformr_VariableConstraint_Expression, gen_transformr_VariableConstraint_Constraint, gen_transformr_Assignment_Expression, gen_transformr_Executable_NamedElement, gen_transformr_Branch_Executable, gen_transformr_Block_Executable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)