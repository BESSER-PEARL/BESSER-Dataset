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
expressions_Expression = Class(name="expressions::Expression", is_abstract=True)
expressions_BinaryOperator = Class(name="expressions::BinaryOperator", is_abstract=True)
Expression = Class(name="Expression")
expressions_UnaryOperator = Class(name="expressions::UnaryOperator", is_abstract=True)
expressions_All = Class(name="expressions::All")
QuantifyOperator = Class(name="QuantifyOperator")
expressions_Number = Class(name="expressions::Number")
expressions_Any = Class(name="expressions::Any")
expressions_ComparisonOperator = Class(name="expressions::ComparisonOperator")
expressions_ComparisonOperand = Class(name="expressions::ComparisonOperand")
expressions_GE = Class(name="expressions::GE")
ComparisonOperator = Class(name="ComparisonOperator")
expressions_G = Class(name="expressions::G")
expressions_LE = Class(name="expressions::LE")
expressions_L = Class(name="expressions::L")
expressions_E = Class(name="expressions::E")
expressions_D = Class(name="expressions::D")
expressions_Quantity = Class(name="expressions::Quantity")
ComparisonOperand = Class(name="ComparisonOperand")
expressions_Function = Class(name="expressions::Function")
expressions_Implies = Class(name="expressions::Implies")
BinaryOperator = Class(name="BinaryOperator")
expressions_Or = Class(name="expressions::Or")
expressions_And = Class(name="expressions::And")
expressions_Neg = Class(name="expressions::Neg")
UnaryOperator = Class(name="UnaryOperator")
expressions_Model = Class(name="expressions::Model")
expressions_Feature = Class(name="expressions::Feature")
expressions_Count = Class(name="expressions::Count")
Function = Class(name="Function")
expressions_QuantifyOperator = Class(name="expressions::QuantifyOperator")

# expressions_Expression class attributes and methods

# expressions_BinaryOperator class attributes and methods

# Expression class attributes and methods

# expressions_UnaryOperator class attributes and methods

# expressions_All class attributes and methods

# QuantifyOperator class attributes and methods

# expressions_Number class attributes and methods
expressions_Number_value: Property = Property(name="value", type=IntegerType)
expressions_Number.attributes={expressions_Number_value}

# expressions_Any class attributes and methods

# expressions_ComparisonOperator class attributes and methods

# expressions_ComparisonOperand class attributes and methods

# expressions_GE class attributes and methods

# ComparisonOperator class attributes and methods

# expressions_G class attributes and methods

# expressions_LE class attributes and methods

# expressions_L class attributes and methods

# expressions_E class attributes and methods

# expressions_D class attributes and methods

# expressions_Quantity class attributes and methods
expressions_Quantity_value: Property = Property(name="value", type=IntegerType)
expressions_Quantity.attributes={expressions_Quantity_value}

# ComparisonOperand class attributes and methods

# expressions_Function class attributes and methods

# expressions_Implies class attributes and methods

# BinaryOperator class attributes and methods

# expressions_Or class attributes and methods

# expressions_And class attributes and methods

# expressions_Neg class attributes and methods

# UnaryOperator class attributes and methods

# expressions_Model class attributes and methods

# expressions_Feature class attributes and methods
expressions_Feature_name: Property = Property(name="name", type=StringType)
expressions_Feature.attributes={expressions_Feature_name}

# expressions_Count class attributes and methods

# Function class attributes and methods

# expressions_QuantifyOperator class attributes and methods

# Relationships
op10: BinaryAssociation = BinaryAssociation(
    name="op10",
    ends={
        Property(name="expressions_Expression", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op21: BinaryAssociation = BinaryAssociation(
    name="op21",
    ends={
        Property(name="expressions_Expression3", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator2", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op18: BinaryAssociation = BinaryAssociation(
    name="op18",
    ends={
        Property(name="expressions_ComparisonOperand", type=expressions_ComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ComparisonOperator", type=expressions_ComparisonOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op29: BinaryAssociation = BinaryAssociation(
    name="op29",
    ends={
        Property(name="expressions_ComparisonOperand11", type=expressions_ComparisonOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ComparisonOperator10", type=expressions_ComparisonOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op12: BinaryAssociation = BinaryAssociation(
    name="op12",
    ends={
        Property(name="expressions_Feature", type=expressions_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Function", type=expressions_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op4: BinaryAssociation = BinaryAssociation(
    name="op4",
    ends={
        Property(name="expressions_Expression5", type=expressions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="expressions_Expression7", type=expressions_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Model", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
op13: BinaryAssociation = BinaryAssociation(
    name="op13",
    ends={
        Property(name="expressions_Feature14", type=expressions_QuantifyOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_QuantifyOperator", type=expressions_Feature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_expressions_BinaryOperator_Expression = Generalization(general=Expression, specific=expressions_BinaryOperator)
gen_expressions_UnaryOperator_Expression = Generalization(general=Expression, specific=expressions_UnaryOperator)
gen_expressions_All_QuantifyOperator = Generalization(general=QuantifyOperator, specific=expressions_All)
gen_expressions_Number_QuantifyOperator = Generalization(general=QuantifyOperator, specific=expressions_Number)
gen_expressions_Any_QuantifyOperator = Generalization(general=QuantifyOperator, specific=expressions_Any)
gen_expressions_ComparisonOperator_Expression = Generalization(general=Expression, specific=expressions_ComparisonOperator)
gen_expressions_GE_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_GE)
gen_expressions_G_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_G)
gen_expressions_LE_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_LE)
gen_expressions_L_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_L)
gen_expressions_E_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_E)
gen_expressions_D_ComparisonOperator = Generalization(general=ComparisonOperator, specific=expressions_D)
gen_expressions_ComparisonOperand_Expression = Generalization(general=Expression, specific=expressions_ComparisonOperand)
gen_expressions_Quantity_ComparisonOperand = Generalization(general=ComparisonOperand, specific=expressions_Quantity)
gen_expressions_Function_ComparisonOperand = Generalization(general=ComparisonOperand, specific=expressions_Function)
gen_expressions_Implies_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Implies)
gen_expressions_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Or)
gen_expressions_And_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_And)
gen_expressions_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_Neg)
gen_expressions_Feature_Expression = Generalization(general=Expression, specific=expressions_Feature)
gen_expressions_Count_Function = Generalization(general=Function, specific=expressions_Count)
gen_expressions_QuantifyOperator_Expression = Generalization(general=Expression, specific=expressions_QuantifyOperator)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_Expression, expressions_BinaryOperator, Expression, expressions_UnaryOperator, expressions_All, QuantifyOperator, expressions_Number, expressions_Any, expressions_ComparisonOperator, expressions_ComparisonOperand, expressions_GE, ComparisonOperator, expressions_G, expressions_LE, expressions_L, expressions_E, expressions_D, expressions_Quantity, ComparisonOperand, expressions_Function, expressions_Implies, BinaryOperator, expressions_Or, expressions_And, expressions_Neg, UnaryOperator, expressions_Model, expressions_Feature, expressions_Count, Function, expressions_QuantifyOperator},
    associations={op10, op21, op18, op29, op12, op4, constraints6, op13},
    generalizations={gen_expressions_BinaryOperator_Expression, gen_expressions_UnaryOperator_Expression, gen_expressions_All_QuantifyOperator, gen_expressions_Number_QuantifyOperator, gen_expressions_Any_QuantifyOperator, gen_expressions_ComparisonOperator_Expression, gen_expressions_GE_ComparisonOperator, gen_expressions_G_ComparisonOperator, gen_expressions_LE_ComparisonOperator, gen_expressions_L_ComparisonOperator, gen_expressions_E_ComparisonOperator, gen_expressions_D_ComparisonOperator, gen_expressions_ComparisonOperand_Expression, gen_expressions_Quantity_ComparisonOperand, gen_expressions_Function_ComparisonOperand, gen_expressions_Implies_BinaryOperator, gen_expressions_Or_BinaryOperator, gen_expressions_And_BinaryOperator, gen_expressions_Neg_UnaryOperator, gen_expressions_Feature_Expression, gen_expressions_Count_Function, gen_expressions_QuantifyOperator_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)