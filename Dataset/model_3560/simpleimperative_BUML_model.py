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
simpleimperative_Program = Class(name="simpleimperative_Program")
simpleimperative_Statement = Class(name="simpleimperative_Statement", is_abstract=True)
simpleimperative_Conditional = Class(name="simpleimperative_Conditional")
Statement = Class(name="Statement")
simpleimperative_Expression = Class(name="simpleimperative_Expression", is_abstract=True)
simpleimperative_Loop = Class(name="simpleimperative_Loop")
simpleimperative_VarDecl = Class(name="simpleimperative_VarDecl")
simpleimperative_Assignation = Class(name="simpleimperative_Assignation")
simpleimperative_ConsoleOutput = Class(name="simpleimperative_ConsoleOutput")
simpleimperative_Println = Class(name="simpleimperative_Println")
ConsoleOutput = Class(name="ConsoleOutput")
simpleimperative_Print = Class(name="simpleimperative_Print")
simpleimperative_Wait = Class(name="simpleimperative_Wait")
simpleimperative_VarRef = Class(name="simpleimperative_VarRef")
Expression = Class(name="Expression")

# simpleimperative_Program class attributes and methods

# simpleimperative_Statement class attributes and methods

# simpleimperative_Conditional class attributes and methods

# Statement class attributes and methods

# simpleimperative_Expression class attributes and methods
simpleimperative_Expression_m_eval: Method = Method(name="eval", parameters={Parameter(name='simpleimperative_context', type=StringType)})
simpleimperative_Expression.methods={simpleimperative_Expression_m_eval}

# simpleimperative_Loop class attributes and methods

# simpleimperative_VarDecl class attributes and methods
simpleimperative_VarDecl_name: Property = Property(name="name", type=StringType)
simpleimperative_VarDecl.attributes={simpleimperative_VarDecl_name}

# simpleimperative_Assignation class attributes and methods

# simpleimperative_ConsoleOutput class attributes and methods
simpleimperative_ConsoleOutput_input: Property = Property(name="input", type=StringType)
simpleimperative_ConsoleOutput.attributes={simpleimperative_ConsoleOutput_input}

# simpleimperative_Println class attributes and methods

# ConsoleOutput class attributes and methods

# simpleimperative_Print class attributes and methods

# simpleimperative_Wait class attributes and methods
simpleimperative_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
simpleimperative_Wait.attributes={simpleimperative_Wait_miliseconds}

# simpleimperative_VarRef class attributes and methods
simpleimperative_VarRef_varRef: Property = Property(name="varRef", type=StringType)
simpleimperative_VarRef.attributes={simpleimperative_VarRef_varRef}

# Expression class attributes and methods

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="simpleimperative_Statement", type=simpleimperative_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Program", type=simpleimperative_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition1: BinaryAssociation = BinaryAssociation(
    name="condition1",
    ends={
        Property(name="simpleimperative_Expression", type=simpleimperative_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Conditional", type=simpleimperative_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body2: BinaryAssociation = BinaryAssociation(
    name="body2",
    ends={
        Property(name="simpleimperative_Statement4", type=simpleimperative_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Conditional3", type=simpleimperative_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard5: BinaryAssociation = BinaryAssociation(
    name="guard5",
    ends={
        Property(name="simpleimperative_Expression6", type=simpleimperative_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Loop", type=simpleimperative_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body7: BinaryAssociation = BinaryAssociation(
    name="body7",
    ends={
        Property(name="simpleimperative_Statement9", type=simpleimperative_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Loop8", type=simpleimperative_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr10: BinaryAssociation = BinaryAssociation(
    name="expr10",
    ends={
        Property(name="simpleimperative_Expression11", type=simpleimperative_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_VarDecl", type=simpleimperative_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varRef12: BinaryAssociation = BinaryAssociation(
    name="varRef12",
    ends={
        Property(name="simpleimperative_VarDecl13", type=simpleimperative_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Assignation", type=simpleimperative_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression14: BinaryAssociation = BinaryAssociation(
    name="expression14",
    ends={
        Property(name="simpleimperative_Expression16", type=simpleimperative_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleimperative_Assignation15", type=simpleimperative_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_simpleimperative_Conditional_Statement = Generalization(general=Statement, specific=simpleimperative_Conditional)
gen_simpleimperative_Loop_Statement = Generalization(general=Statement, specific=simpleimperative_Loop)
gen_simpleimperative_VarDecl_Statement = Generalization(general=Statement, specific=simpleimperative_VarDecl)
gen_simpleimperative_Assignation_Statement = Generalization(general=Statement, specific=simpleimperative_Assignation)
gen_simpleimperative_ConsoleOutput_Statement = Generalization(general=Statement, specific=simpleimperative_ConsoleOutput)
gen_simpleimperative_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=simpleimperative_Println)
gen_simpleimperative_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=simpleimperative_Print)
gen_simpleimperative_Wait_Statement = Generalization(general=Statement, specific=simpleimperative_Wait)
gen_simpleimperative_VarRef_Expression = Generalization(general=Expression, specific=simpleimperative_VarRef)

# Domain Model
domain_model = DomainModel(
    name="simpleimperative",
    types={simpleimperative_Program, simpleimperative_Statement, simpleimperative_Conditional, Statement, simpleimperative_Expression, simpleimperative_Loop, simpleimperative_VarDecl, simpleimperative_Assignation, simpleimperative_ConsoleOutput, simpleimperative_Println, ConsoleOutput, simpleimperative_Print, simpleimperative_Wait, simpleimperative_VarRef, Expression},
    associations={statements0, condition1, body2, guard5, body7, expr10, varRef12, expression14},
    generalizations={gen_simpleimperative_Conditional_Statement, gen_simpleimperative_Loop_Statement, gen_simpleimperative_VarDecl_Statement, gen_simpleimperative_Assignation_Statement, gen_simpleimperative_ConsoleOutput_Statement, gen_simpleimperative_Println_ConsoleOutput, gen_simpleimperative_Print_ConsoleOutput, gen_simpleimperative_Wait_Statement, gen_simpleimperative_VarRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)