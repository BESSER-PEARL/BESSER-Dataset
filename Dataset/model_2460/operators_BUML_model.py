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
operators_OclExpression = Class(name="operators::OclExpression", is_abstract=True)
operators_OperatorCallExp = Class(name="operators::OperatorCallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
operators_BinaryOperatorCallExp = Class(name="operators::BinaryOperatorCallExp")
OperatorCallExp = Class(name="OperatorCallExp")
operators_UnaryOperatorCallExp = Class(name="operators::UnaryOperatorCallExp")
operators_IntegerExp = Class(name="operators::IntegerExp")
operators_PrimitiveExp = Class(name="operators::PrimitiveExp", is_abstract=True)
operators_StringExp = Class(name="operators::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
operators_BooleanExp = Class(name="operators::BooleanExp")
operators_NumericExp = Class(name="operators::NumericExp", is_abstract=True)
operators_RealExp = Class(name="operators::RealExp")
NumericExp = Class(name="NumericExp")

# operators_OclExpression class attributes and methods

# operators_OperatorCallExp class attributes and methods
operators_OperatorCallExp_name: Property = Property(name="name", type=StringType)
operators_OperatorCallExp.attributes={operators_OperatorCallExp_name}

# OclExpression class attributes and methods

# operators_BinaryOperatorCallExp class attributes and methods

# OperatorCallExp class attributes and methods

# operators_UnaryOperatorCallExp class attributes and methods

# operators_IntegerExp class attributes and methods
operators_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
operators_IntegerExp.attributes={operators_IntegerExp_integerSymbol}

# operators_PrimitiveExp class attributes and methods

# operators_StringExp class attributes and methods
operators_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
operators_StringExp.attributes={operators_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# operators_BooleanExp class attributes and methods
operators_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
operators_BooleanExp.attributes={operators_BooleanExp_booleanSymbol}

# operators_NumericExp class attributes and methods

# operators_RealExp class attributes and methods
operators_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
operators_RealExp.attributes={operators_RealExp_realSymbol}

# NumericExp class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="operators_OclExpression", type=operators_BinaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_BinaryOperatorCallExp", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument1: BinaryAssociation = BinaryAssociation(
    name="argument1",
    ends={
        Property(name="operators_OclExpression3", type=operators_BinaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_BinaryOperatorCallExp2", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="operators_OclExpression5", type=operators_UnaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_UnaryOperatorCallExp", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_operators_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=operators_OperatorCallExp)
gen_operators_BinaryOperatorCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=operators_BinaryOperatorCallExp)
gen_operators_UnaryOperatorCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=operators_UnaryOperatorCallExp)
gen_operators_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=operators_PrimitiveExp)
gen_operators_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=operators_StringExp)
gen_operators_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=operators_BooleanExp)
gen_operators_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=operators_NumericExp)
gen_operators_RealExp_NumericExp = Generalization(general=NumericExp, specific=operators_RealExp)
gen_operators_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=operators_IntegerExp)

# Domain Model
domain_model = DomainModel(
    name="operators",
    types={operators_OclExpression, operators_OperatorCallExp, OclExpression, operators_BinaryOperatorCallExp, OperatorCallExp, operators_UnaryOperatorCallExp, operators_IntegerExp, operators_PrimitiveExp, operators_StringExp, PrimitiveExp, operators_BooleanExp, operators_NumericExp, operators_RealExp, NumericExp},
    associations={source0, argument1, source4},
    generalizations={gen_operators_OperatorCallExp_OclExpression, gen_operators_BinaryOperatorCallExp_OperatorCallExp, gen_operators_UnaryOperatorCallExp_OperatorCallExp, gen_operators_PrimitiveExp_OclExpression, gen_operators_StringExp_PrimitiveExp, gen_operators_BooleanExp_PrimitiveExp, gen_operators_NumericExp_PrimitiveExp, gen_operators_RealExp_NumericExp, gen_operators_IntegerExp_NumericExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)