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
simpleal_ArithOp = Class(name="simpleal::ArithOp", is_abstract=True)
simpleal_ArithPlus = Class(name="simpleal::ArithPlus")
ArithOp = Class(name="ArithOp")
simpleal_Block = Class(name="simpleal::Block")
simpleal_Stmt = Class(name="simpleal::Stmt", is_abstract=True)
simpleal_Arith = Class(name="simpleal::Arith", is_abstract=True)
simpleal_VarRef = Class(name="simpleal::VarRef")
Arith = Class(name="Arith")
simpleal_ArithLit = Class(name="simpleal::ArithLit")
simpleal_ArithMinus = Class(name="simpleal::ArithMinus")
simpleal_Print = Class(name="simpleal::Print")
Stmt = Class(name="Stmt")
simpleal_Assign = Class(name="simpleal::Assign")

# simpleal_ArithOp class attributes and methods

# simpleal_ArithPlus class attributes and methods

# ArithOp class attributes and methods

# simpleal_Block class attributes and methods

# simpleal_Stmt class attributes and methods

# simpleal_Arith class attributes and methods

# simpleal_VarRef class attributes and methods
simpleal_VarRef_name: Property = Property(name="name", type=StringType)
simpleal_VarRef.attributes={simpleal_VarRef_name}

# Arith class attributes and methods

# simpleal_ArithLit class attributes and methods
simpleal_ArithLit_val: Property = Property(name="val", type=IntegerType)
simpleal_ArithLit.attributes={simpleal_ArithLit_val}

# simpleal_ArithMinus class attributes and methods

# simpleal_Print class attributes and methods
simpleal_Print_name: Property = Property(name="name", type=StringType)
simpleal_Print.attributes={simpleal_Print_name}

# Stmt class attributes and methods

# simpleal_Assign class attributes and methods
simpleal_Assign_name: Property = Property(name="name", type=StringType)
simpleal_Assign.attributes={simpleal_Assign_name}

# Relationships
lhs1: BinaryAssociation = BinaryAssociation(
    name="lhs1",
    ends={
        Property(name="simpleal_Arith", type=simpleal_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleal_ArithOp", type=simpleal_Arith, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs2: BinaryAssociation = BinaryAssociation(
    name="rhs2",
    ends={
        Property(name="simpleal_Arith4", type=simpleal_ArithOp, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleal_ArithOp3", type=simpleal_Arith, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmts0: BinaryAssociation = BinaryAssociation(
    name="stmts0",
    ends={
        Property(name="simpleal_Stmt", type=simpleal_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleal_Block", type=simpleal_Stmt, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
val5: BinaryAssociation = BinaryAssociation(
    name="val5",
    ends={
        Property(name="simpleal_Arith6", type=simpleal_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleal_Assign", type=simpleal_Arith, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simpleal_ArithOp_Arith = Generalization(general=Arith, specific=simpleal_ArithOp)
gen_simpleal_ArithPlus_ArithOp = Generalization(general=ArithOp, specific=simpleal_ArithPlus)
gen_simpleal_VarRef_Arith = Generalization(general=Arith, specific=simpleal_VarRef)
gen_simpleal_ArithLit_Arith = Generalization(general=Arith, specific=simpleal_ArithLit)
gen_simpleal_ArithMinus_ArithOp = Generalization(general=ArithOp, specific=simpleal_ArithMinus)
gen_simpleal_Print_Stmt = Generalization(general=Stmt, specific=simpleal_Print)
gen_simpleal_Assign_Stmt = Generalization(general=Stmt, specific=simpleal_Assign)

# Domain Model
domain_model = DomainModel(
    name="simpleal",
    types={simpleal_ArithOp, simpleal_ArithPlus, ArithOp, simpleal_Block, simpleal_Stmt, simpleal_Arith, simpleal_VarRef, Arith, simpleal_ArithLit, simpleal_ArithMinus, simpleal_Print, Stmt, simpleal_Assign},
    associations={lhs1, rhs2, stmts0, val5},
    generalizations={gen_simpleal_ArithOp_Arith, gen_simpleal_ArithPlus_ArithOp, gen_simpleal_VarRef_Arith, gen_simpleal_ArithLit_Arith, gen_simpleal_ArithMinus_ArithOp, gen_simpleal_Print_Stmt, gen_simpleal_Assign_Stmt},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)