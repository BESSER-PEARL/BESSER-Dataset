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
RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="lessThanOrEqualTo"),
			EnumerationLiteral(name="greaterThanOrEqualTo")
    }
)

ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="mult"),
			EnumerationLiteral(name="div")
    }
)

# Classes
flowchartpck_Node = Class(name="flowchartpck::Node", is_abstract=True)
flowchartpck_NamedElement = Class(name="flowchartpck::NamedElement")
flowchartpck_Flowchart = Class(name="flowchartpck::Flowchart")
NamedElement = Class(name="NamedElement")
flowchartpck_Arc = Class(name="flowchartpck::Arc")
flowchartpck_Constraint = Class(name="flowchartpck::Constraint")
flowchartpck_Action = Class(name="flowchartpck::Action")
Node = Class(name="Node")
flowchartpck_Program = Class(name="flowchartpck::Program")
flowchartpck_Decision = Class(name="flowchartpck::Decision")
flowchartpck_IntegerLit = Class(name="flowchartpck::IntegerLit")
Literal = Class(name="Literal")
flowchartpck_Start = Class(name="flowchartpck::Start")
flowchartpck_End = Class(name="flowchartpck::End")
flowchartpck_RelationalConstraint = Class(name="flowchartpck::RelationalConstraint")
Constraint = Class(name="Constraint")
flowchartpck_Expression = Class(name="flowchartpck::Expression")
flowchartpck_Literal = Class(name="flowchartpck::Literal")
Expression = Class(name="Expression")
flowchartpck_StringLit = Class(name="flowchartpck::StringLit")
flowchartpck_BoolLit = Class(name="flowchartpck::BoolLit")
flowchartpck_ArithmeticExpression = Class(name="flowchartpck::ArithmeticExpression")
flowchartpck_RelationalExpression = Class(name="flowchartpck::RelationalExpression")
flowchartpck_Println = Class(name="flowchartpck::Println")
ConsoleOutput = Class(name="ConsoleOutput")
flowchartpck_Print = Class(name="flowchartpck::Print")
flowchartpck_Assignation = Class(name="flowchartpck::Assignation")
flowchartpck_VarDecl = Class(name="flowchartpck::VarDecl")
flowchartpck_Wait = Class(name="flowchartpck::Wait")
flowchartpck_VarReference = Class(name="flowchartpck::VarReference")
flowchartpck_Statement = Class(name="flowchartpck::Statement", is_abstract=True)
Statement = Class(name="Statement")
flowchartpck_Conditional = Class(name="flowchartpck::Conditional")
flowchartpck_Loop = Class(name="flowchartpck::Loop")
flowchartpck_ConsoleOutput = Class(name="flowchartpck::ConsoleOutput")

# flowchartpck_Node class attributes and methods

# flowchartpck_NamedElement class attributes and methods
flowchartpck_NamedElement_name: Property = Property(name="name", type=StringType)
flowchartpck_NamedElement.attributes={flowchartpck_NamedElement_name}

# flowchartpck_Flowchart class attributes and methods

# NamedElement class attributes and methods

# flowchartpck_Arc class attributes and methods

# flowchartpck_Constraint class attributes and methods

# flowchartpck_Action class attributes and methods

# Node class attributes and methods

# flowchartpck_Program class attributes and methods

# flowchartpck_Decision class attributes and methods

# flowchartpck_IntegerLit class attributes and methods
flowchartpck_IntegerLit_value: Property = Property(name="value", type=IntegerType)
flowchartpck_IntegerLit.attributes={flowchartpck_IntegerLit_value}

# Literal class attributes and methods

# flowchartpck_Start class attributes and methods

# flowchartpck_End class attributes and methods

# flowchartpck_RelationalConstraint class attributes and methods

# Constraint class attributes and methods

# flowchartpck_Expression class attributes and methods

# flowchartpck_Literal class attributes and methods

# Expression class attributes and methods

# flowchartpck_StringLit class attributes and methods
flowchartpck_StringLit_value: Property = Property(name="value", type=StringType)
flowchartpck_StringLit.attributes={flowchartpck_StringLit_value}

# flowchartpck_BoolLit class attributes and methods
flowchartpck_BoolLit_value: Property = Property(name="value", type=BooleanType)
flowchartpck_BoolLit.attributes={flowchartpck_BoolLit_value}

# flowchartpck_ArithmeticExpression class attributes and methods
flowchartpck_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
flowchartpck_ArithmeticExpression.attributes={flowchartpck_ArithmeticExpression_operator}

# flowchartpck_RelationalExpression class attributes and methods
flowchartpck_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
flowchartpck_RelationalExpression.attributes={flowchartpck_RelationalExpression_operator}

# flowchartpck_Println class attributes and methods

# ConsoleOutput class attributes and methods

# flowchartpck_Print class attributes and methods

# flowchartpck_Assignation class attributes and methods

# flowchartpck_VarDecl class attributes and methods
flowchartpck_VarDecl_key: Property = Property(name="key", type=StringType)
flowchartpck_VarDecl.attributes={flowchartpck_VarDecl_key}

# flowchartpck_Wait class attributes and methods
flowchartpck_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
flowchartpck_Wait.attributes={flowchartpck_Wait_miliseconds}

# flowchartpck_VarReference class attributes and methods
flowchartpck_VarReference_key: Property = Property(name="key", type=StringType)
flowchartpck_VarReference.attributes={flowchartpck_VarReference_key}

# flowchartpck_Statement class attributes and methods

# Statement class attributes and methods

# flowchartpck_Conditional class attributes and methods

# flowchartpck_Loop class attributes and methods

# flowchartpck_ConsoleOutput class attributes and methods
flowchartpck_ConsoleOutput_input: Property = Property(name="input", type=StringType)
flowchartpck_ConsoleOutput.attributes={flowchartpck_ConsoleOutput_input}

# Relationships
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="flowchartpck_Node", type=flowchartpck_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Flowchart", type=flowchartpck_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="flowchartpck_Arc", type=flowchartpck_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Flowchart2", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="4", type=flowchartpck_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="7", type=flowchartpck_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
guard15: BinaryAssociation = BinaryAssociation(
    name="guard15",
    ends={
        Property(name="flowchartpck_Constraint", type=flowchartpck_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Decision", type=flowchartpck_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="10", type=flowchartpck_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=flowchartpck_Node, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="13", type=flowchartpck_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=flowchartpck_Node, multiplicity=Multiplicity(0, 1))
    }
)
doProgram14: BinaryAssociation = BinaryAssociation(
    name="doProgram14",
    ends={
        Property(name="flowchartpck_Program", type=flowchartpck_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Action", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="flowchartpck_Expression", type=flowchartpck_RelationalConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalConstraint", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left22: BinaryAssociation = BinaryAssociation(
    name="left22",
    ends={
        Property(name="flowchartpck_Expression23", type=flowchartpck_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalExpression", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right24: BinaryAssociation = BinaryAssociation(
    name="right24",
    ends={
        Property(name="flowchartpck_Expression26", type=flowchartpck_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalExpression25", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="flowchartpck_Expression18", type=flowchartpck_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_ArithmeticExpression", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="flowchartpck_Expression21", type=flowchartpck_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_ArithmeticExpression20", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varRef42: BinaryAssociation = BinaryAssociation(
    name="varRef42",
    ends={
        Property(name="flowchartpck_VarDecl", type=flowchartpck_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Assignation", type=flowchartpck_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="flowchartpck_Expression45", type=flowchartpck_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Assignation44", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements27: BinaryAssociation = BinaryAssociation(
    name="statements27",
    ends={
        Property(name="flowchartpck_Statement", type=flowchartpck_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Program28", type=flowchartpck_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenInstructions29: BinaryAssociation = BinaryAssociation(
    name="thenInstructions29",
    ends={
        Property(name="flowchartpck_Program30", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseInstructions31: BinaryAssociation = BinaryAssociation(
    name="elseInstructions31",
    ends={
        Property(name="flowchartpck_Program33", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional32", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition34: BinaryAssociation = BinaryAssociation(
    name="condition34",
    ends={
        Property(name="flowchartpck_Expression36", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional35", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="flowchartpck_Program38", type=flowchartpck_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Loop", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard39: BinaryAssociation = BinaryAssociation(
    name="guard39",
    ends={
        Property(name="flowchartpck_Expression41", type=flowchartpck_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Loop40", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression46: BinaryAssociation = BinaryAssociation(
    name="expression46",
    ends={
        Property(name="flowchartpck_Expression48", type=flowchartpck_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_VarDecl47", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_flowchartpck_Flowchart_NamedElement = Generalization(general=NamedElement, specific=flowchartpck_Flowchart)
gen_flowchartpck_Node_NamedElement = Generalization(general=NamedElement, specific=flowchartpck_Node)
gen_flowchartpck_Action_Node = Generalization(general=Node, specific=flowchartpck_Action)
gen_flowchartpck_Decision_Node = Generalization(general=Node, specific=flowchartpck_Decision)
gen_flowchartpck_IntegerLit_Literal = Generalization(general=Literal, specific=flowchartpck_IntegerLit)
gen_flowchartpck_Start_Node = Generalization(general=Node, specific=flowchartpck_Start)
gen_flowchartpck_End_Node = Generalization(general=Node, specific=flowchartpck_End)
gen_flowchartpck_RelationalConstraint_Constraint = Generalization(general=Constraint, specific=flowchartpck_RelationalConstraint)
gen_flowchartpck_Literal_Expression = Generalization(general=Expression, specific=flowchartpck_Literal)
gen_flowchartpck_StringLit_Literal = Generalization(general=Literal, specific=flowchartpck_StringLit)
gen_flowchartpck_BoolLit_Literal = Generalization(general=Literal, specific=flowchartpck_BoolLit)
gen_flowchartpck_ArithmeticExpression_Expression = Generalization(general=Expression, specific=flowchartpck_ArithmeticExpression)
gen_flowchartpck_RelationalExpression_Expression = Generalization(general=Expression, specific=flowchartpck_RelationalExpression)
gen_flowchartpck_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=flowchartpck_Println)
gen_flowchartpck_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=flowchartpck_Print)
gen_flowchartpck_Assignation_Statement = Generalization(general=Statement, specific=flowchartpck_Assignation)
gen_flowchartpck_VarReference_Expression = Generalization(general=Expression, specific=flowchartpck_VarReference)
gen_flowchartpck_Program_Statement = Generalization(general=Statement, specific=flowchartpck_Program)
gen_flowchartpck_Conditional_Statement = Generalization(general=Statement, specific=flowchartpck_Conditional)
gen_flowchartpck_Loop_Statement = Generalization(general=Statement, specific=flowchartpck_Loop)
gen_flowchartpck_ConsoleOutput_Statement = Generalization(general=Statement, specific=flowchartpck_ConsoleOutput)
gen_flowchartpck_Wait_Statement = Generalization(general=Statement, specific=flowchartpck_Wait)
gen_flowchartpck_VarDecl_Statement = Generalization(general=Statement, specific=flowchartpck_VarDecl)

# Domain Model
domain_model = DomainModel(
    name="flowchartpck",
    types={flowchartpck_Node, flowchartpck_NamedElement, flowchartpck_Flowchart, NamedElement, flowchartpck_Arc, flowchartpck_Constraint, flowchartpck_Action, Node, flowchartpck_Program, flowchartpck_Decision, flowchartpck_IntegerLit, Literal, flowchartpck_Start, flowchartpck_End, flowchartpck_RelationalConstraint, Constraint, flowchartpck_Expression, flowchartpck_Literal, Expression, flowchartpck_StringLit, flowchartpck_BoolLit, flowchartpck_ArithmeticExpression, flowchartpck_RelationalExpression, flowchartpck_Println, ConsoleOutput, flowchartpck_Print, flowchartpck_Assignation, flowchartpck_VarDecl, flowchartpck_Wait, flowchartpck_VarReference, flowchartpck_Statement, Statement, flowchartpck_Conditional, flowchartpck_Loop, flowchartpck_ConsoleOutput, RelationalOperator, ArithmeticOperator},
    associations={nodes0, arcs1, outgoing3, incoming5, guard15, source8, target11, doProgram14, expression16, left22, right24, left17, right19, varRef42, expression43, statements27, thenInstructions29, elseInstructions31, condition34, body37, guard39, expression46},
    generalizations={gen_flowchartpck_Flowchart_NamedElement, gen_flowchartpck_Node_NamedElement, gen_flowchartpck_Action_Node, gen_flowchartpck_Decision_Node, gen_flowchartpck_IntegerLit_Literal, gen_flowchartpck_Start_Node, gen_flowchartpck_End_Node, gen_flowchartpck_RelationalConstraint_Constraint, gen_flowchartpck_Literal_Expression, gen_flowchartpck_StringLit_Literal, gen_flowchartpck_BoolLit_Literal, gen_flowchartpck_ArithmeticExpression_Expression, gen_flowchartpck_RelationalExpression_Expression, gen_flowchartpck_Println_ConsoleOutput, gen_flowchartpck_Print_ConsoleOutput, gen_flowchartpck_Assignation_Statement, gen_flowchartpck_VarReference_Expression, gen_flowchartpck_Program_Statement, gen_flowchartpck_Conditional_Statement, gen_flowchartpck_Loop_Statement, gen_flowchartpck_ConsoleOutput_Statement, gen_flowchartpck_Wait_Statement, gen_flowchartpck_VarDecl_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)