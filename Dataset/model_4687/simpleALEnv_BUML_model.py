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
simpleALEnv_Block = Class(name="simpleALEnv::Block")
simpleALEnv_Stmt = Class(name="simpleALEnv::Stmt", is_abstract=True)
simpleALEnv_Arith = Class(name="simpleALEnv::Arith", is_abstract=True)
simpleALEnv_ALVarRef = Class(name="simpleALEnv::ALVarRef")
Arith = Class(name="Arith")
simpleALEnv_ArithLit = Class(name="simpleALEnv::ArithLit")
simpleALEnv_ArithOp = Class(name="simpleALEnv::ArithOp", is_abstract=True)
simpleALEnv_ArithPlus = Class(name="simpleALEnv::ArithPlus")
ArithOp = Class(name="ArithOp")
simpleALEnv_ArithMinus = Class(name="simpleALEnv::ArithMinus")
simpleALEnv_Print = Class(name="simpleALEnv::Print")
Stmt = Class(name="Stmt")
simpleALEnv_Assign = Class(name="simpleALEnv::Assign")
simpleALEnv_IfStmt = Class(name="simpleALEnv::IfStmt")
simpleALEnv_EqualityTest = Class(name="simpleALEnv::EqualityTest")
simpleALEnv_RandRange = Class(name="simpleALEnv::RandRange")

# simpleALEnv_Block class attributes and methods

# simpleALEnv_Stmt class attributes and methods

# simpleALEnv_Arith class attributes and methods

# simpleALEnv_ALVarRef class attributes and methods
simpleALEnv_ALVarRef_name: Property = Property(name="name", type=StringType)
simpleALEnv_ALVarRef.attributes={simpleALEnv_ALVarRef_name}

# Arith class attributes and methods

# simpleALEnv_ArithLit class attributes and methods
simpleALEnv_ArithLit_val: Property = Property(name="val", type=IntegerType)
simpleALEnv_ArithLit.attributes={simpleALEnv_ArithLit_val}

# simpleALEnv_ArithOp class attributes and methods

# simpleALEnv_ArithPlus class attributes and methods

# ArithOp class attributes and methods

# simpleALEnv_ArithMinus class attributes and methods

# simpleALEnv_Print class attributes and methods
simpleALEnv_Print_name: Property = Property(name="name", type=StringType)
simpleALEnv_Print.attributes={simpleALEnv_Print_name}

# Stmt class attributes and methods

# simpleALEnv_Assign class attributes and methods
simpleALEnv_Assign_name: Property = Property(name="name", type=StringType)
simpleALEnv_Assign.attributes={simpleALEnv_Assign_name}

# simpleALEnv_IfStmt class attributes and methods

# simpleALEnv_EqualityTest class attributes and methods

# simpleALEnv_RandRange class attributes and methods
simpleALEnv_RandRange_min: Property = Property(name="min", type=IntegerType)
simpleALEnv_RandRange_max: Property = Property(name="max", type=IntegerType)
simpleALEnv_RandRange.attributes={simpleALEnv_RandRange_max, simpleALEnv_RandRange_min}

# Relationships
stmts0: BinaryAssociation = BinaryAssociation(
    name="stmts0",
    ends={
        Property(name="simpleALEnv_Stmt", type=simpleALEnv_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_Block", type=simpleALEnv_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs1: BinaryAssociation = BinaryAssociation(
    name="lhs1",
    ends={
        Property(name="simpleALEnv_Arith", type=simpleALEnv_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_ArithOp", type=simpleALEnv_Arith, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs2: BinaryAssociation = BinaryAssociation(
    name="rhs2",
    ends={
        Property(name="simpleALEnv_Arith4", type=simpleALEnv_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_ArithOp3", type=simpleALEnv_Arith, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
val5: BinaryAssociation = BinaryAssociation(
    name="val5",
    ends={
        Property(name="simpleALEnv_Arith6", type=simpleALEnv_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_Assign", type=simpleALEnv_Arith, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifBranch7: BinaryAssociation = BinaryAssociation(
    name="ifBranch7",
    ends={
        Property(name="simpleALEnv_Assign8", type=simpleALEnv_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_IfStmt", type=simpleALEnv_Assign, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBranch9: BinaryAssociation = BinaryAssociation(
    name="elseBranch9",
    ends={
        Property(name="simpleALEnv_Assign11", type=simpleALEnv_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_IfStmt10", type=simpleALEnv_Assign, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
test12: BinaryAssociation = BinaryAssociation(
    name="test12",
    ends={
        Property(name="simpleALEnv_EqualityTest", type=simpleALEnv_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_IfStmt13", type=simpleALEnv_EqualityTest, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs14: BinaryAssociation = BinaryAssociation(
    name="lhs14",
    ends={
        Property(name="simpleALEnv_Arith16", type=simpleALEnv_EqualityTest, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_EqualityTest15", type=simpleALEnv_Arith, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs17: BinaryAssociation = BinaryAssociation(
    name="rhs17",
    ends={
        Property(name="simpleALEnv_Arith19", type=simpleALEnv_EqualityTest, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleALEnv_EqualityTest18", type=simpleALEnv_Arith, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_simpleALEnv_ALVarRef_Arith = Generalization(general=Arith, specific=simpleALEnv_ALVarRef)
gen_simpleALEnv_ArithLit_Arith = Generalization(general=Arith, specific=simpleALEnv_ArithLit)
gen_simpleALEnv_ArithOp_Arith = Generalization(general=Arith, specific=simpleALEnv_ArithOp)
gen_simpleALEnv_ArithPlus_ArithOp = Generalization(general=ArithOp, specific=simpleALEnv_ArithPlus)
gen_simpleALEnv_ArithMinus_ArithOp = Generalization(general=ArithOp, specific=simpleALEnv_ArithMinus)
gen_simpleALEnv_Print_Stmt = Generalization(general=Stmt, specific=simpleALEnv_Print)
gen_simpleALEnv_Assign_Stmt = Generalization(general=Stmt, specific=simpleALEnv_Assign)
gen_simpleALEnv_IfStmt_Stmt = Generalization(general=Stmt, specific=simpleALEnv_IfStmt)
gen_simpleALEnv_RandRange_Arith = Generalization(general=Arith, specific=simpleALEnv_RandRange)

# Domain Model
domain_model = DomainModel(
    name="simpleALEnv",
    types={simpleALEnv_Block, simpleALEnv_Stmt, simpleALEnv_Arith, simpleALEnv_ALVarRef, Arith, simpleALEnv_ArithLit, simpleALEnv_ArithOp, simpleALEnv_ArithPlus, ArithOp, simpleALEnv_ArithMinus, simpleALEnv_Print, Stmt, simpleALEnv_Assign, simpleALEnv_IfStmt, simpleALEnv_EqualityTest, simpleALEnv_RandRange},
    associations={stmts0, lhs1, rhs2, val5, ifBranch7, elseBranch9, test12, lhs14, rhs17},
    generalizations={gen_simpleALEnv_ALVarRef_Arith, gen_simpleALEnv_ArithLit_Arith, gen_simpleALEnv_ArithOp_Arith, gen_simpleALEnv_ArithPlus_ArithOp, gen_simpleALEnv_ArithMinus_ArithOp, gen_simpleALEnv_Print_Stmt, gen_simpleALEnv_Assign_Stmt, gen_simpleALEnv_IfStmt_Stmt, gen_simpleALEnv_RandRange_Arith},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)