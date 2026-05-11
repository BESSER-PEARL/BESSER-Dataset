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
graph_AssignStmt = Class(name="graph_AssignStmt")
Statement = Class(name="Statement")
graph_Expr = Class(name="graph_Expr")
graph_PrintStmt = Class(name="graph_PrintStmt")
graph_IfStmt = Class(name="graph_IfStmt")
graph_WhileStmt = Class(name="graph_WhileStmt")
graph_MoveStmt = Class(name="graph_MoveStmt")
graph_Vertex = Class(name="graph_Vertex")
graph_Edge = Class(name="graph_Edge")
graph_Program = Class(name="graph_Program")
graph_Declaration = Class(name="graph_Declaration")
graph_Statement = Class(name="graph_Statement")
graph_PathExistence = Class(name="graph_PathExistence")
graph_Comparison = Class(name="graph_Comparison")
graph_PlusOrMin = Class(name="graph_PlusOrMin")
graph_MulOrDiv = Class(name="graph_MulOrDiv")
graph_Not = Class(name="graph_Not")
graph_IntConstant = Class(name="graph_IntConstant")
graph_Or = Class(name="graph_Or")
Expr = Class(name="Expr")
graph_And = Class(name="graph_And")
graph_ParticleConstant = Class(name="graph_ParticleConstant")
graph_StringConstant = Class(name="graph_StringConstant")
graph_BoolConstant = Class(name="graph_BoolConstant")
graph_VariableRef = Class(name="graph_VariableRef")
graph_GraphConstant = Class(name="graph_GraphConstant")

# graph_AssignStmt class attributes and methods

# Statement class attributes and methods

# graph_Expr class attributes and methods

# graph_PrintStmt class attributes and methods

# graph_IfStmt class attributes and methods

# graph_WhileStmt class attributes and methods

# graph_MoveStmt class attributes and methods

# graph_Vertex class attributes and methods
graph_Vertex_name: Property = Property(name="name", type=StringType)
graph_Vertex.attributes={graph_Vertex_name}

# graph_Edge class attributes and methods

# graph_Program class attributes and methods

# graph_Declaration class attributes and methods
graph_Declaration_name: Property = Property(name="name", type=StringType)
graph_Declaration_type: Property = Property(name="type", type=StringType)
graph_Declaration.attributes={graph_Declaration_type, graph_Declaration_name}

# graph_Statement class attributes and methods

# graph_PathExistence class attributes and methods

# graph_Comparison class attributes and methods
graph_Comparison_op: Property = Property(name="op", type=StringType)
graph_Comparison.attributes={graph_Comparison_op}

# graph_PlusOrMin class attributes and methods
graph_PlusOrMin_op: Property = Property(name="op", type=StringType)
graph_PlusOrMin.attributes={graph_PlusOrMin_op}

# graph_MulOrDiv class attributes and methods
graph_MulOrDiv_op: Property = Property(name="op", type=StringType)
graph_MulOrDiv.attributes={graph_MulOrDiv_op}

# graph_Not class attributes and methods

# graph_IntConstant class attributes and methods
graph_IntConstant_value: Property = Property(name="value", type=IntegerType)
graph_IntConstant.attributes={graph_IntConstant_value}

# graph_Or class attributes and methods

# Expr class attributes and methods

# graph_And class attributes and methods

# graph_ParticleConstant class attributes and methods

# graph_StringConstant class attributes and methods
graph_StringConstant_value: Property = Property(name="value", type=StringType)
graph_StringConstant.attributes={graph_StringConstant_value}

# graph_BoolConstant class attributes and methods
graph_BoolConstant_value: Property = Property(name="value", type=StringType)
graph_BoolConstant.attributes={graph_BoolConstant_value}

# graph_VariableRef class attributes and methods

# graph_GraphConstant class attributes and methods

# Relationships
var3: BinaryAssociation = BinaryAssociation(
    name="var3",
    ends={
        Property(name="graph_Declaration4", type=graph_AssignStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_AssignStmt", type=graph_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
expr5: BinaryAssociation = BinaryAssociation(
    name="expr5",
    ends={
        Property(name="graph_Expr", type=graph_AssignStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_AssignStmt6", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr7: BinaryAssociation = BinaryAssociation(
    name="expr7",
    ends={
        Property(name="graph_Expr8", type=graph_PrintStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_PrintStmt", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr9: BinaryAssociation = BinaryAssociation(
    name="expr9",
    ends={
        Property(name="graph_Expr10", type=graph_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_IfStmt", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts11: BinaryAssociation = BinaryAssociation(
    name="stmts11",
    ends={
        Property(name="graph_Statement13", type=graph_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_IfStmt12", type=graph_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseStmts14: BinaryAssociation = BinaryAssociation(
    name="elseStmts14",
    ends={
        Property(name="graph_Statement16", type=graph_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_IfStmt15", type=graph_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr17: BinaryAssociation = BinaryAssociation(
    name="expr17",
    ends={
        Property(name="graph_Expr18", type=graph_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_WhileStmt", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts19: BinaryAssociation = BinaryAssociation(
    name="stmts19",
    ends={
        Property(name="graph_Statement21", type=graph_WhileStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_WhileStmt20", type=graph_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
var22: BinaryAssociation = BinaryAssociation(
    name="var22",
    ends={
        Property(name="graph_Declaration23", type=graph_MoveStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_MoveStmt", type=graph_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
source24: BinaryAssociation = BinaryAssociation(
    name="source24",
    ends={
        Property(name="graph_Vertex", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
declarations0: BinaryAssociation = BinaryAssociation(
    name="declarations0",
    ends={
        Property(name="graph_Declaration", type=graph_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Program", type=graph_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts1: BinaryAssociation = BinaryAssociation(
    name="stmts1",
    ends={
        Property(name="graph_Statement", type=graph_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Program2", type=graph_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left38: BinaryAssociation = BinaryAssociation(
    name="left38",
    ends={
        Property(name="graph_Expr39", type=graph_PathExistence, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_PathExistence", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right40: BinaryAssociation = BinaryAssociation(
    name="right40",
    ends={
        Property(name="graph_Expr42", type=graph_PathExistence, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_PathExistence41", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left43: BinaryAssociation = BinaryAssociation(
    name="left43",
    ends={
        Property(name="graph_Expr44", type=graph_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Comparison", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right45: BinaryAssociation = BinaryAssociation(
    name="right45",
    ends={
        Property(name="graph_Expr47", type=graph_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Comparison46", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left48: BinaryAssociation = BinaryAssociation(
    name="left48",
    ends={
        Property(name="graph_Expr49", type=graph_PlusOrMin, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_PlusOrMin", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right50: BinaryAssociation = BinaryAssociation(
    name="right50",
    ends={
        Property(name="graph_Expr52", type=graph_PlusOrMin, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_PlusOrMin51", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left53: BinaryAssociation = BinaryAssociation(
    name="left53",
    ends={
        Property(name="graph_Expr54", type=graph_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_MulOrDiv", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right55: BinaryAssociation = BinaryAssociation(
    name="right55",
    ends={
        Property(name="graph_Expr57", type=graph_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_MulOrDiv56", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Expr58: BinaryAssociation = BinaryAssociation(
    name="Expr58",
    ends={
        Property(name="graph_Expr59", type=graph_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Not", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dest25: BinaryAssociation = BinaryAssociation(
    name="dest25",
    ends={
        Property(name="graph_Vertex27", type=graph_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Edge26", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
left28: BinaryAssociation = BinaryAssociation(
    name="left28",
    ends={
        Property(name="graph_Expr29", type=graph_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Or", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right30: BinaryAssociation = BinaryAssociation(
    name="right30",
    ends={
        Property(name="graph_Expr32", type=graph_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Or31", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left33: BinaryAssociation = BinaryAssociation(
    name="left33",
    ends={
        Property(name="graph_Expr34", type=graph_And, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_And", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right35: BinaryAssociation = BinaryAssociation(
    name="right35",
    ends={
        Property(name="graph_Expr37", type=graph_And, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_And36", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
edges64: BinaryAssociation = BinaryAssociation(
    name="edges64",
    ends={
        Property(name="graph_Edge66", type=graph_GraphConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphConstant65", type=graph_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph67: BinaryAssociation = BinaryAssociation(
    name="graph67",
    ends={
        Property(name="graph_Expr68", type=graph_ParticleConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ParticleConstant", type=graph_Expr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
vertex69: BinaryAssociation = BinaryAssociation(
    name="vertex69",
    ends={
        Property(name="graph_Vertex71", type=graph_ParticleConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_ParticleConstant70", type=graph_Vertex, multiplicity=Multiplicity(0, 1))
    }
)
variable60: BinaryAssociation = BinaryAssociation(
    name="variable60",
    ends={
        Property(name="graph_Declaration61", type=graph_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_VariableRef", type=graph_Declaration, multiplicity=Multiplicity(0, 1))
    }
)
vertices62: BinaryAssociation = BinaryAssociation(
    name="vertices62",
    ends={
        Property(name="graph_Vertex63", type=graph_GraphConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_GraphConstant", type=graph_Vertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_graph_AssignStmt_Statement = Generalization(general=Statement, specific=graph_AssignStmt)
gen_graph_PrintStmt_Statement = Generalization(general=Statement, specific=graph_PrintStmt)
gen_graph_IfStmt_Statement = Generalization(general=Statement, specific=graph_IfStmt)
gen_graph_WhileStmt_Statement = Generalization(general=Statement, specific=graph_WhileStmt)
gen_graph_MoveStmt_Statement = Generalization(general=Statement, specific=graph_MoveStmt)
gen_graph_PathExistence_Expr = Generalization(general=Expr, specific=graph_PathExistence)
gen_graph_Comparison_Expr = Generalization(general=Expr, specific=graph_Comparison)
gen_graph_PlusOrMin_Expr = Generalization(general=Expr, specific=graph_PlusOrMin)
gen_graph_MulOrDiv_Expr = Generalization(general=Expr, specific=graph_MulOrDiv)
gen_graph_Not_Expr = Generalization(general=Expr, specific=graph_Not)
gen_graph_Or_Expr = Generalization(general=Expr, specific=graph_Or)
gen_graph_And_Expr = Generalization(general=Expr, specific=graph_And)
gen_graph_ParticleConstant_Expr = Generalization(general=Expr, specific=graph_ParticleConstant)
gen_graph_IntConstant_Expr = Generalization(general=Expr, specific=graph_IntConstant)
gen_graph_StringConstant_Expr = Generalization(general=Expr, specific=graph_StringConstant)
gen_graph_BoolConstant_Expr = Generalization(general=Expr, specific=graph_BoolConstant)
gen_graph_VariableRef_Expr = Generalization(general=Expr, specific=graph_VariableRef)
gen_graph_GraphConstant_Expr = Generalization(general=Expr, specific=graph_GraphConstant)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_AssignStmt, Statement, graph_Expr, graph_PrintStmt, graph_IfStmt, graph_WhileStmt, graph_MoveStmt, graph_Vertex, graph_Edge, graph_Program, graph_Declaration, graph_Statement, graph_PathExistence, graph_Comparison, graph_PlusOrMin, graph_MulOrDiv, graph_Not, graph_IntConstant, graph_Or, Expr, graph_And, graph_ParticleConstant, graph_StringConstant, graph_BoolConstant, graph_VariableRef, graph_GraphConstant},
    associations={var3, expr5, expr7, expr9, stmts11, elseStmts14, expr17, stmts19, var22, source24, declarations0, stmts1, left38, right40, left43, right45, left48, right50, left53, right55, Expr58, dest25, left28, right30, left33, right35, edges64, graph67, vertex69, variable60, vertices62},
    generalizations={gen_graph_AssignStmt_Statement, gen_graph_PrintStmt_Statement, gen_graph_IfStmt_Statement, gen_graph_WhileStmt_Statement, gen_graph_MoveStmt_Statement, gen_graph_PathExistence_Expr, gen_graph_Comparison_Expr, gen_graph_PlusOrMin_Expr, gen_graph_MulOrDiv_Expr, gen_graph_Not_Expr, gen_graph_Or_Expr, gen_graph_And_Expr, gen_graph_ParticleConstant_Expr, gen_graph_IntConstant_Expr, gen_graph_StringConstant_Expr, gen_graph_BoolConstant_Expr, gen_graph_VariableRef_Expr, gen_graph_GraphConstant_Expr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)