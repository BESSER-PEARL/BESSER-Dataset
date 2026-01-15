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
calculatrice_Calculatrice = Class(name="calculatrice::Calculatrice")
calculatrice_Calc = Class(name="calculatrice::Calc")
calculatrice_BoolExpr = Class(name="calculatrice::BoolExpr")
calculatrice_CalcExpr = Class(name="calculatrice::CalcExpr")
calculatrice_Condition = Class(name="calculatrice::Condition")
Calc = Class(name="Calc")
Condition = Class(name="Condition")
calculatrice_Number = Class(name="calculatrice::Number")
CalcExpr = Class(name="CalcExpr")
calculatrice_VarCall = Class(name="calculatrice::VarCall")
calculatrice_Boolean = Class(name="calculatrice::Boolean")
BoolExpr = Class(name="BoolExpr")

# calculatrice_Calculatrice class attributes and methods

# calculatrice_Calc class attributes and methods
calculatrice_Calc_boolName: Property = Property(name="boolName", type=StringType)
calculatrice_Calc_decl: Property = Property(name="decl", type=BooleanType)
calculatrice_Calc_varName: Property = Property(name="varName", type=StringType)
calculatrice_Calc.attributes={calculatrice_Calc_varName, calculatrice_Calc_decl, calculatrice_Calc_boolName}

# calculatrice_BoolExpr class attributes and methods
calculatrice_BoolExpr_op: Property = Property(name="op", type=StringType)
calculatrice_BoolExpr.attributes={calculatrice_BoolExpr_op}

# calculatrice_CalcExpr class attributes and methods
calculatrice_CalcExpr_op: Property = Property(name="op", type=StringType)
calculatrice_CalcExpr.attributes={calculatrice_CalcExpr_op}

# calculatrice_Condition class attributes and methods

# Calc class attributes and methods

# Condition class attributes and methods

# calculatrice_Number class attributes and methods
calculatrice_Number_neg: Property = Property(name="neg", type=BooleanType)
calculatrice_Number_value: Property = Property(name="value", type=IntegerType)
calculatrice_Number.attributes={calculatrice_Number_value, calculatrice_Number_neg}

# CalcExpr class attributes and methods

# calculatrice_VarCall class attributes and methods
calculatrice_VarCall_varCall: Property = Property(name="varCall", type=StringType)
calculatrice_VarCall.attributes={calculatrice_VarCall_varCall}

# calculatrice_Boolean class attributes and methods
calculatrice_Boolean_BoolValue: Property = Property(name="BoolValue", type=StringType)
calculatrice_Boolean.attributes={calculatrice_Boolean_BoolValue}

# BoolExpr class attributes and methods

# Relationships
calculs0: BinaryAssociation = BinaryAssociation(
    name="calculs0",
    ends={
        Property(name="calculatrice_Calc", type=calculatrice_Calculatrice, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_Calculatrice", type=calculatrice_Calc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="calculatrice_BoolExpr", type=calculatrice_Calc, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_Calc2", type=calculatrice_BoolExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e3: BinaryAssociation = BinaryAssociation(
    name="e3",
    ends={
        Property(name="calculatrice_CalcExpr", type=calculatrice_Calc, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_Calc4", type=calculatrice_CalcExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="calculatrice_CalcExpr7", type=calculatrice_CalcExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_CalcExpr5", type=calculatrice_CalcExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right9: BinaryAssociation = BinaryAssociation(
    name="right9",
    ends={
        Property(name="calculatrice_CalcExpr10", type=calculatrice_CalcExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_CalcExpr8", type=calculatrice_CalcExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right21: BinaryAssociation = BinaryAssociation(
    name="right21",
    ends={
        Property(name="calculatrice_BoolExpr22", type=calculatrice_BoolExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_BoolExpr20", type=calculatrice_BoolExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBlock11: BinaryAssociation = BinaryAssociation(
    name="thenBlock11",
    ends={
        Property(name="calculatrice_Calc13", type=calculatrice_BoolExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_BoolExpr12", type=calculatrice_Calc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseBlock14: BinaryAssociation = BinaryAssociation(
    name="elseBlock14",
    ends={
        Property(name="calculatrice_Calc16", type=calculatrice_BoolExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_BoolExpr15", type=calculatrice_Calc, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="calculatrice_BoolExpr19", type=calculatrice_BoolExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="calculatrice_BoolExpr17", type=calculatrice_BoolExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_calculatrice_Condition_Calc = Generalization(general=Calc, specific=calculatrice_Condition)
gen_calculatrice_BoolExpr_Condition = Generalization(general=Condition, specific=calculatrice_BoolExpr)
gen_calculatrice_Number_CalcExpr = Generalization(general=CalcExpr, specific=calculatrice_Number)
gen_calculatrice_VarCall_CalcExpr = Generalization(general=CalcExpr, specific=calculatrice_VarCall)
gen_calculatrice_Boolean_BoolExpr = Generalization(general=BoolExpr, specific=calculatrice_Boolean)

# Domain Model
domain_model = DomainModel(
    name="calculatrice",
    types={calculatrice_Calculatrice, calculatrice_Calc, calculatrice_BoolExpr, calculatrice_CalcExpr, calculatrice_Condition, Calc, Condition, calculatrice_Number, CalcExpr, calculatrice_VarCall, calculatrice_Boolean, BoolExpr},
    associations={calculs0, b1, e3, left6, right9, right21, thenBlock11, elseBlock14, left18},
    generalizations={gen_calculatrice_Condition_Calc, gen_calculatrice_BoolExpr_Condition, gen_calculatrice_Number_CalcExpr, gen_calculatrice_VarCall_CalcExpr, gen_calculatrice_Boolean_BoolExpr},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)