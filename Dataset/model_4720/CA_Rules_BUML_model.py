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
ca_rule_PopulationRange = Class(name="ca::rule::PopulationRange")
ca_rule_Max = Class(name="ca::rule::Max")
NeighborsExpression = Class(name="NeighborsExpression")
ca_rule_Add = Class(name="ca::rule::Add")
BinaryExpression = Class(name="BinaryExpression")
ca_rule_UnaryExpression = Class(name="ca::rule::UnaryExpression")
IntegerExpression = Class(name="IntegerExpression")
ca_rule_And = Class(name="ca::rule::And")
ca_rule_Or = Class(name="ca::rule::Or")
ca_rule_Rule = Class(name="ca::rule::Rule")
ca_rule_IntegerExpression = Class(name="ca::rule::IntegerExpression")
ca_rule_Mult = Class(name="ca::rule::Mult")
ca_rule_Div = Class(name="ca::rule::Div")
ca_rule_Sum = Class(name="ca::rule::Sum")
ca_rule_CellularAutomata = Class(name="ca::rule::CellularAutomata")
ca_rule_Mod = Class(name="ca::rule::Mod")
ca_rule_UMinus = Class(name="ca::rule::UMinus")
ca_rule_Minus = Class(name="ca::rule::Minus")
ca_rule_Not = Class(name="ca::rule::Not")
UnaryExpression = Class(name="UnaryExpression")
ca_rule_Greater = Class(name="ca::rule::Greater")
ca_rule_Lower = Class(name="ca::rule::Lower")
ca_rule_IntegerLiteral = Class(name="ca::rule::IntegerLiteral")
ca_rule_Conditional = Class(name="ca::rule::Conditional")
ca_rule_CurrentCellPopulation = Class(name="ca::rule::CurrentCellPopulation")
ca_rule_Size = Class(name="ca::rule::Size")
ca_rule_NeighborsExpression = Class(name="ca::rule::NeighborsExpression")
ca_rule_Min = Class(name="ca::rule::Min")
ca_rule_BinaryExpression = Class(name="ca::rule::BinaryExpression")
ca_rule_Equal = Class(name="ca::rule::Equal")

# ca_rule_PopulationRange class attributes and methods
ca_rule_PopulationRange_lowerRange: Property = Property(name="lowerRange", type=IntegerType)
ca_rule_PopulationRange_upperRange: Property = Property(name="upperRange", type=IntegerType)
ca_rule_PopulationRange.attributes={ca_rule_PopulationRange_lowerRange, ca_rule_PopulationRange_upperRange}

# ca_rule_Max class attributes and methods

# NeighborsExpression class attributes and methods

# ca_rule_Add class attributes and methods

# BinaryExpression class attributes and methods

# ca_rule_UnaryExpression class attributes and methods

# IntegerExpression class attributes and methods

# ca_rule_And class attributes and methods

# ca_rule_Or class attributes and methods

# ca_rule_Rule class attributes and methods

# ca_rule_IntegerExpression class attributes and methods

# ca_rule_Mult class attributes and methods

# ca_rule_Div class attributes and methods

# ca_rule_Sum class attributes and methods

# ca_rule_CellularAutomata class attributes and methods

# ca_rule_Mod class attributes and methods

# ca_rule_UMinus class attributes and methods

# ca_rule_Minus class attributes and methods

# ca_rule_Not class attributes and methods

# UnaryExpression class attributes and methods

# ca_rule_Greater class attributes and methods

# ca_rule_Lower class attributes and methods

# ca_rule_IntegerLiteral class attributes and methods
ca_rule_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
ca_rule_IntegerLiteral.attributes={ca_rule_IntegerLiteral_value}

# ca_rule_Conditional class attributes and methods

# ca_rule_CurrentCellPopulation class attributes and methods

# ca_rule_Size class attributes and methods

# ca_rule_NeighborsExpression class attributes and methods

# ca_rule_Min class attributes and methods

# ca_rule_BinaryExpression class attributes and methods

# ca_rule_Equal class attributes and methods

# Relationships
nextValue0: BinaryAssociation = BinaryAssociation(
    name="nextValue0",
    ends={
        Property(name="ca_rule_Rule", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="ca_rule_IntegerExpression", type=ca_rule_Rule, multiplicity=Multiplicity(1, 1))
    }
)
filter1: BinaryAssociation = BinaryAssociation(
    name="filter1",
    ends={
        Property(name="ca_rule_PopulationRange", type=ca_rule_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_Rule2", type=ca_rule_PopulationRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="ca_rule_IntegerExpression4", type=ca_rule_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_UnaryExpression", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right17: BinaryAssociation = BinaryAssociation(
    name="right17",
    ends={
        Property(name="ca_rule_IntegerExpression19", type=ca_rule_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_BinaryExpression18", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rules20: BinaryAssociation = BinaryAssociation(
    name="rules20",
    ends={
        Property(name="ca_rule_Rule21", type=ca_rule_CellularAutomata, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_CellularAutomata", type=ca_rule_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ifTrueExpression5: BinaryAssociation = BinaryAssociation(
    name="ifTrueExpression5",
    ends={
        Property(name="ca_rule_IntegerExpression6", type=ca_rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_Conditional", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalseExpression7: BinaryAssociation = BinaryAssociation(
    name="ifFalseExpression7",
    ends={
        Property(name="ca_rule_IntegerExpression9", type=ca_rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_Conditional8", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="ca_rule_IntegerExpression12", type=ca_rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_Conditional11", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
neighborsFilter13: BinaryAssociation = BinaryAssociation(
    name="neighborsFilter13",
    ends={
        Property(name="ca_rule_PopulationRange14", type=ca_rule_NeighborsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_NeighborsExpression", type=ca_rule_PopulationRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left15: BinaryAssociation = BinaryAssociation(
    name="left15",
    ends={
        Property(name="ca_rule_IntegerExpression16", type=ca_rule_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="ca_rule_BinaryExpression", type=ca_rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ca_rule_Max_NeighborsExpression = Generalization(general=NeighborsExpression, specific=ca_rule_Max)
gen_ca_rule_Add_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Add)
gen_ca_rule_UnaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_UnaryExpression)
gen_ca_rule_And_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_And)
gen_ca_rule_Or_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Or)
gen_ca_rule_Mult_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Mult)
gen_ca_rule_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Div)
gen_ca_rule_Sum_NeighborsExpression = Generalization(general=NeighborsExpression, specific=ca_rule_Sum)
gen_ca_rule_Mod_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Mod)
gen_ca_rule_UMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=ca_rule_UMinus)
gen_ca_rule_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Minus)
gen_ca_rule_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=ca_rule_Not)
gen_ca_rule_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Greater)
gen_ca_rule_Lower_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Lower)
gen_ca_rule_IntegerLiteral_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_IntegerLiteral)
gen_ca_rule_Conditional_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_Conditional)
gen_ca_rule_CurrentCellPopulation_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_CurrentCellPopulation)
gen_ca_rule_Size_NeighborsExpression = Generalization(general=NeighborsExpression, specific=ca_rule_Size)
gen_ca_rule_NeighborsExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_NeighborsExpression)
gen_ca_rule_Min_NeighborsExpression = Generalization(general=NeighborsExpression, specific=ca_rule_Min)
gen_ca_rule_BinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=ca_rule_BinaryExpression)
gen_ca_rule_Equal_BinaryExpression = Generalization(general=BinaryExpression, specific=ca_rule_Equal)

# Domain Model
domain_model = DomainModel(
    name="ca_rule",
    types={ca_rule_PopulationRange, ca_rule_Max, NeighborsExpression, ca_rule_Add, BinaryExpression, ca_rule_UnaryExpression, IntegerExpression, ca_rule_And, ca_rule_Or, ca_rule_Rule, ca_rule_IntegerExpression, ca_rule_Mult, ca_rule_Div, ca_rule_Sum, ca_rule_CellularAutomata, ca_rule_Mod, ca_rule_UMinus, ca_rule_Minus, ca_rule_Not, UnaryExpression, ca_rule_Greater, ca_rule_Lower, ca_rule_IntegerLiteral, ca_rule_Conditional, ca_rule_CurrentCellPopulation, ca_rule_Size, ca_rule_NeighborsExpression, ca_rule_Min, ca_rule_BinaryExpression, ca_rule_Equal},
    associations={nextValue0, filter1, target3, right17, rules20, ifTrueExpression5, ifFalseExpression7, condition10, neighborsFilter13, left15},
    generalizations={gen_ca_rule_Max_NeighborsExpression, gen_ca_rule_Add_BinaryExpression, gen_ca_rule_UnaryExpression_IntegerExpression, gen_ca_rule_And_BinaryExpression, gen_ca_rule_Or_BinaryExpression, gen_ca_rule_Mult_BinaryExpression, gen_ca_rule_Div_BinaryExpression, gen_ca_rule_Sum_NeighborsExpression, gen_ca_rule_Mod_BinaryExpression, gen_ca_rule_UMinus_UnaryExpression, gen_ca_rule_Minus_BinaryExpression, gen_ca_rule_Not_UnaryExpression, gen_ca_rule_Greater_BinaryExpression, gen_ca_rule_Lower_BinaryExpression, gen_ca_rule_IntegerLiteral_IntegerExpression, gen_ca_rule_Conditional_IntegerExpression, gen_ca_rule_CurrentCellPopulation_IntegerExpression, gen_ca_rule_Size_NeighborsExpression, gen_ca_rule_NeighborsExpression_IntegerExpression, gen_ca_rule_Min_NeighborsExpression, gen_ca_rule_BinaryExpression_IntegerExpression, gen_ca_rule_Equal_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)