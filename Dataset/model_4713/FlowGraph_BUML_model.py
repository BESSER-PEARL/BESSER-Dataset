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
flowgraph_Conditional = Class(name="flowgraph::Conditional", is_abstract=True)
flowgraph_JumpStmt = Class(name="flowgraph::JumpStmt", is_abstract=True)
flowgraph_Label = Class(name="flowgraph::Label")
flowgraph_Break = Class(name="flowgraph::Break")
JumpStmt = Class(name="JumpStmt")
flowgraph_Stmt = Class(name="flowgraph::Stmt", is_abstract=True)
Item = Class(name="Item")
flowgraph_SimpleStmt = Class(name="flowgraph::SimpleStmt")
Stmt = Class(name="Stmt")
FlowInstr = Class(name="FlowInstr")
flowgraph_Block = Class(name="flowgraph::Block")
flowgraph_If = Class(name="flowgraph::If")
Conditional = Class(name="Conditional")
flowgraph_Expr = Class(name="flowgraph::Expr")
flowgraph_Item = Class(name="flowgraph::Item", is_abstract=True)
flowgraph_Return = Class(name="flowgraph::Return")
flowgraph_Method = Class(name="flowgraph::Method")
Block = Class(name="Block")
flowgraph_Exit = Class(name="flowgraph::Exit")
flowgraph_Var = Class(name="flowgraph::Var")
flowgraph_Loop = Class(name="flowgraph::Loop")
flowgraph_Continue = Class(name="flowgraph::Continue")
flowgraph_FlowInstr = Class(name="flowgraph::FlowInstr", is_abstract=True)
flowgraph_Param = Class(name="flowgraph::Param")
Var = Class(name="Var")

# flowgraph_Conditional class attributes and methods

# flowgraph_JumpStmt class attributes and methods

# flowgraph_Label class attributes and methods

# flowgraph_Break class attributes and methods

# JumpStmt class attributes and methods

# flowgraph_Stmt class attributes and methods

# Item class attributes and methods

# flowgraph_SimpleStmt class attributes and methods
flowgraph_SimpleStmt_type: Property = Property(name="type", type=StringType)
flowgraph_SimpleStmt_valiableAccess: Property = Property(name="valiableAccess", type=StringType)
flowgraph_SimpleStmt_functionAccess: Property = Property(name="functionAccess", type=StringType)
flowgraph_SimpleStmt.attributes={flowgraph_SimpleStmt_valiableAccess, flowgraph_SimpleStmt_type, flowgraph_SimpleStmt_functionAccess}

# Stmt class attributes and methods

# FlowInstr class attributes and methods

# flowgraph_Block class attributes and methods

# flowgraph_If class attributes and methods

# Conditional class attributes and methods

# flowgraph_Expr class attributes and methods

# flowgraph_Item class attributes and methods
flowgraph_Item_txt: Property = Property(name="txt", type=StringType)
flowgraph_Item_line: Property = Property(name="line", type=IntegerType)
flowgraph_Item.attributes={flowgraph_Item_txt, flowgraph_Item_line}

# flowgraph_Return class attributes and methods

# flowgraph_Method class attributes and methods

# Block class attributes and methods

# flowgraph_Exit class attributes and methods

# flowgraph_Var class attributes and methods

# flowgraph_Loop class attributes and methods

# flowgraph_Continue class attributes and methods

# flowgraph_FlowInstr class attributes and methods

# flowgraph_Param class attributes and methods

# Var class attributes and methods

# Relationships
expr10: BinaryAssociation = BinaryAssociation(
    name="expr10",
    ends={
        Property(name="flowgraph_Expr", type=flowgraph_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_Conditional", type=flowgraph_Expr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
label11: BinaryAssociation = BinaryAssociation(
    name="label11",
    ends={
        Property(name="Label", type=flowgraph_JumpStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="jumps", type=flowgraph_Label, multiplicity=Multiplicity(0, 1))
    }
)
stmts0: BinaryAssociation = BinaryAssociation(
    name="stmts0",
    ends={
        Property(name="flowgraph_Stmt", type=flowgraph_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_Block", type=flowgraph_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then1: BinaryAssociation = BinaryAssociation(
    name="then1",
    ends={
        Property(name="flowgraph_Stmt2", type=flowgraph_If, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_If", type=flowgraph_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else3: BinaryAssociation = BinaryAssociation(
    name="else3",
    ends={
        Property(name="flowgraph_Stmt5", type=flowgraph_If, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_If4", type=flowgraph_Stmt, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit6: BinaryAssociation = BinaryAssociation(
    name="exit6",
    ends={
        Property(name="flowgraph_Exit", type=flowgraph_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_Method", type=flowgraph_Exit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vars7: BinaryAssociation = BinaryAssociation(
    name="vars7",
    ends={
        Property(name="Var", type=flowgraph_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=flowgraph_Var, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body8: BinaryAssociation = BinaryAssociation(
    name="body8",
    ends={
        Property(name="flowgraph_Stmt9", type=flowgraph_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_Loop", type=flowgraph_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cfNext13: BinaryAssociation = BinaryAssociation(
    name="cfNext13",
    ends={
        Property(name="FlowInstr", type=flowgraph_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="cfPrev", type=flowgraph_FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
cfPrev15: BinaryAssociation = BinaryAssociation(
    name="cfPrev15",
    ends={
        Property(name="FlowInstr16", type=flowgraph_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="cfNext", type=flowgraph_FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
def17: BinaryAssociation = BinaryAssociation(
    name="def17",
    ends={
        Property(name="Var18", type=flowgraph_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="definers", type=flowgraph_Var, multiplicity=Multiplicity(0, 9999))
    }
)
use19: BinaryAssociation = BinaryAssociation(
    name="use19",
    ends={
        Property(name="Var20", type=flowgraph_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="users", type=flowgraph_Var, multiplicity=Multiplicity(0, 9999))
    }
)
dfNext22: BinaryAssociation = BinaryAssociation(
    name="dfNext22",
    ends={
        Property(name="flowgraph_FlowInstr", type=flowgraph_FlowInstr, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_FlowInstr21", type=flowgraph_FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
definers23: BinaryAssociation = BinaryAssociation(
    name="definers23",
    ends={
        Property(name="FlowInstr24", type=flowgraph_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="def", type=flowgraph_FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
users25: BinaryAssociation = BinaryAssociation(
    name="users25",
    ends={
        Property(name="FlowInstr26", type=flowgraph_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="use", type=flowgraph_FlowInstr, multiplicity=Multiplicity(0, 9999))
    }
)
method27: BinaryAssociation = BinaryAssociation(
    name="method27",
    ends={
        Property(name="Method", type=flowgraph_Var, multiplicity=Multiplicity(1, 1)),
        Property(name="vars", type=flowgraph_Method, multiplicity=Multiplicity(0, 1))
    }
)
stmt28: BinaryAssociation = BinaryAssociation(
    name="stmt28",
    ends={
        Property(name="flowgraph_Stmt29", type=flowgraph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="flowgraph_Label", type=flowgraph_Stmt, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
jumps30: BinaryAssociation = BinaryAssociation(
    name="jumps30",
    ends={
        Property(name="JumpStmt", type=flowgraph_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="label", type=flowgraph_JumpStmt, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_flowgraph_Conditional_Stmt = Generalization(general=Stmt, specific=flowgraph_Conditional)
gen_flowgraph_JumpStmt_Stmt = Generalization(general=Stmt, specific=flowgraph_JumpStmt)
gen_flowgraph_JumpStmt_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_JumpStmt)
gen_flowgraph_Break_JumpStmt = Generalization(general=JumpStmt, specific=flowgraph_Break)
gen_flowgraph_Stmt_Item = Generalization(general=Item, specific=flowgraph_Stmt)
gen_flowgraph_SimpleStmt_Stmt = Generalization(general=Stmt, specific=flowgraph_SimpleStmt)
gen_flowgraph_SimpleStmt_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_SimpleStmt)
gen_flowgraph_Block_Stmt = Generalization(general=Stmt, specific=flowgraph_Block)
gen_flowgraph_If_Conditional = Generalization(general=Conditional, specific=flowgraph_If)
gen_flowgraph_Expr_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_Expr)
gen_flowgraph_Return_Stmt = Generalization(general=Stmt, specific=flowgraph_Return)
gen_flowgraph_Return_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_Return)
gen_flowgraph_Method_Block = Generalization(general=Block, specific=flowgraph_Method)
gen_flowgraph_Method_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_Method)
gen_flowgraph_Exit_FlowInstr = Generalization(general=FlowInstr, specific=flowgraph_Exit)
gen_flowgraph_Loop_Conditional = Generalization(general=Conditional, specific=flowgraph_Loop)
gen_flowgraph_Continue_JumpStmt = Generalization(general=JumpStmt, specific=flowgraph_Continue)
gen_flowgraph_FlowInstr_Item = Generalization(general=Item, specific=flowgraph_FlowInstr)
gen_flowgraph_Var_Item = Generalization(general=Item, specific=flowgraph_Var)
gen_flowgraph_Param_Var = Generalization(general=Var, specific=flowgraph_Param)
gen_flowgraph_Label_Stmt = Generalization(general=Stmt, specific=flowgraph_Label)

# Domain Model
domain_model = DomainModel(
    name="flowgraph",
    types={flowgraph_Conditional, flowgraph_JumpStmt, flowgraph_Label, flowgraph_Break, JumpStmt, flowgraph_Stmt, Item, flowgraph_SimpleStmt, Stmt, FlowInstr, flowgraph_Block, flowgraph_If, Conditional, flowgraph_Expr, flowgraph_Item, flowgraph_Return, flowgraph_Method, Block, flowgraph_Exit, flowgraph_Var, flowgraph_Loop, flowgraph_Continue, flowgraph_FlowInstr, flowgraph_Param, Var},
    associations={expr10, label11, stmts0, then1, else3, exit6, vars7, body8, cfNext13, cfPrev15, def17, use19, dfNext22, definers23, users25, method27, stmt28, jumps30},
    generalizations={gen_flowgraph_Conditional_Stmt, gen_flowgraph_JumpStmt_Stmt, gen_flowgraph_JumpStmt_FlowInstr, gen_flowgraph_Break_JumpStmt, gen_flowgraph_Stmt_Item, gen_flowgraph_SimpleStmt_Stmt, gen_flowgraph_SimpleStmt_FlowInstr, gen_flowgraph_Block_Stmt, gen_flowgraph_If_Conditional, gen_flowgraph_Expr_FlowInstr, gen_flowgraph_Return_Stmt, gen_flowgraph_Return_FlowInstr, gen_flowgraph_Method_Block, gen_flowgraph_Method_FlowInstr, gen_flowgraph_Exit_FlowInstr, gen_flowgraph_Loop_Conditional, gen_flowgraph_Continue_JumpStmt, gen_flowgraph_FlowInstr_Item, gen_flowgraph_Var_Item, gen_flowgraph_Param_Var, gen_flowgraph_Label_Stmt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)