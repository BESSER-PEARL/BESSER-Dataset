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
NeighborsExpression = Class(name="NeighborsExpression")
rule_Add = Class(name="rule::Add")
BinaryExpression = Class(name="BinaryExpression")
rule_UnaryExpression = Class(name="rule::UnaryExpression")
IntegerExpression = Class(name="IntegerExpression")
rule_Rule = Class(name="rule::Rule")
rule_IntegerExpression = Class(name="rule::IntegerExpression")
rule_PopulationRange = Class(name="rule::PopulationRange")
rule_Max = Class(name="rule::Max")
rule_Sum = Class(name="rule::Sum")
rule_CellularAutomata = Class(name="rule::CellularAutomata")
rule_And = Class(name="rule::And")
rule_Or = Class(name="rule::Or")
rule_Not = Class(name="rule::Not")
UnaryExpression = Class(name="UnaryExpression")
rule_Greater = Class(name="rule::Greater")
rule_Lower = Class(name="rule::Lower")
rule_IntegerLiteral = Class(name="rule::IntegerLiteral")
rule_Conditional = Class(name="rule::Conditional")
rule_CurrentCellPopulation = Class(name="rule::CurrentCellPopulation")
rule_Size = Class(name="rule::Size")
rule_NeighborsExpression = Class(name="rule::NeighborsExpression")
rule_Min = Class(name="rule::Min")
rule_BinaryExpression = Class(name="rule::BinaryExpression")
rule_Mult = Class(name="rule::Mult")
rule_Div = Class(name="rule::Div")
rule_Mod = Class(name="rule::Mod")
rule_UMinus = Class(name="rule::UMinus")
rule_Minus = Class(name="rule::Minus")
rule_Equal = Class(name="rule::Equal")

# NeighborsExpression class attributes and methods

# rule_Add class attributes and methods

# BinaryExpression class attributes and methods

# rule_UnaryExpression class attributes and methods

# IntegerExpression class attributes and methods

# rule_Rule class attributes and methods

# rule_IntegerExpression class attributes and methods

# rule_PopulationRange class attributes and methods
rule_PopulationRange_lowerRange: Property = Property(name="lowerRange", type=IntegerType)
rule_PopulationRange_upperRange: Property = Property(name="upperRange", type=IntegerType)
rule_PopulationRange.attributes={rule_PopulationRange_upperRange, rule_PopulationRange_lowerRange}

# rule_Max class attributes and methods

# rule_Sum class attributes and methods

# rule_CellularAutomata class attributes and methods

# rule_And class attributes and methods

# rule_Or class attributes and methods

# rule_Not class attributes and methods

# UnaryExpression class attributes and methods

# rule_Greater class attributes and methods

# rule_Lower class attributes and methods

# rule_IntegerLiteral class attributes and methods
rule_IntegerLiteral_val: Property = Property(name="val", type=IntegerType)
rule_IntegerLiteral.attributes={rule_IntegerLiteral_val}

# rule_Conditional class attributes and methods

# rule_CurrentCellPopulation class attributes and methods

# rule_Size class attributes and methods

# rule_NeighborsExpression class attributes and methods

# rule_Min class attributes and methods

# rule_BinaryExpression class attributes and methods

# rule_Mult class attributes and methods

# rule_Div class attributes and methods

# rule_Mod class attributes and methods

# rule_UMinus class attributes and methods

# rule_Minus class attributes and methods

# rule_Equal class attributes and methods

# Relationships
target3: BinaryAssociation = BinaryAssociation(
    name="target3",
    ends={
        Property(name="rule_IntegerExpression4", type=rule_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_UnaryExpression", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nextVal0: BinaryAssociation = BinaryAssociation(
    name="nextVal0",
    ends={
        Property(name="rule_IntegerExpression", type=rule_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_Rule", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
filter1: BinaryAssociation = BinaryAssociation(
    name="filter1",
    ends={
        Property(name="rule_PopulationRange", type=rule_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_Rule2", type=rule_PopulationRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules20: BinaryAssociation = BinaryAssociation(
    name="rules20",
    ends={
        Property(name="rule_Rule21", type=rule_CellularAutomata, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_CellularAutomata", type=rule_Rule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ifTrueExpression5: BinaryAssociation = BinaryAssociation(
    name="ifTrueExpression5",
    ends={
        Property(name="rule_IntegerExpression6", type=rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_Conditional", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifFalseExpression7: BinaryAssociation = BinaryAssociation(
    name="ifFalseExpression7",
    ends={
        Property(name="rule_IntegerExpression9", type=rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_Conditional8", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="rule_IntegerExpression12", type=rule_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_Conditional11", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
neighborsFilter13: BinaryAssociation = BinaryAssociation(
    name="neighborsFilter13",
    ends={
        Property(name="rule_PopulationRange14", type=rule_NeighborsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_NeighborsExpression", type=rule_PopulationRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left15: BinaryAssociation = BinaryAssociation(
    name="left15",
    ends={
        Property(name="rule_IntegerExpression16", type=rule_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_BinaryExpression", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right17: BinaryAssociation = BinaryAssociation(
    name="right17",
    ends={
        Property(name="rule_IntegerExpression19", type=rule_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="rule_BinaryExpression18", type=rule_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_rule_Max_NeighborsExpression = Generalization(general=NeighborsExpression, specific=rule_Max)
gen_rule_Add_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Add)
gen_rule_UnaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_UnaryExpression)
gen_rule_Sum_NeighborsExpression = Generalization(general=NeighborsExpression, specific=rule_Sum)
gen_rule_And_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_And)
gen_rule_Or_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Or)
gen_rule_Not_UnaryExpression = Generalization(general=UnaryExpression, specific=rule_Not)
gen_rule_Greater_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Greater)
gen_rule_Lower_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Lower)
gen_rule_IntegerLiteral_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_IntegerLiteral)
gen_rule_Conditional_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_Conditional)
gen_rule_CurrentCellPopulation_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_CurrentCellPopulation)
gen_rule_Size_NeighborsExpression = Generalization(general=NeighborsExpression, specific=rule_Size)
gen_rule_NeighborsExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_NeighborsExpression)
gen_rule_Min_NeighborsExpression = Generalization(general=NeighborsExpression, specific=rule_Min)
gen_rule_BinaryExpression_IntegerExpression = Generalization(general=IntegerExpression, specific=rule_BinaryExpression)
gen_rule_Mult_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Mult)
gen_rule_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Div)
gen_rule_Mod_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Mod)
gen_rule_UMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=rule_UMinus)
gen_rule_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Minus)
gen_rule_Equal_BinaryExpression = Generalization(general=BinaryExpression, specific=rule_Equal)

# Domain Model
domain_model = DomainModel(
    name="rule",
    types={NeighborsExpression, rule_Add, BinaryExpression, rule_UnaryExpression, IntegerExpression, rule_Rule, rule_IntegerExpression, rule_PopulationRange, rule_Max, rule_Sum, rule_CellularAutomata, rule_And, rule_Or, rule_Not, UnaryExpression, rule_Greater, rule_Lower, rule_IntegerLiteral, rule_Conditional, rule_CurrentCellPopulation, rule_Size, rule_NeighborsExpression, rule_Min, rule_BinaryExpression, rule_Mult, rule_Div, rule_Mod, rule_UMinus, rule_Minus, rule_Equal},
    associations={target3, nextVal0, filter1, rules20, ifTrueExpression5, ifFalseExpression7, condition10, neighborsFilter13, left15, right17},
    generalizations={gen_rule_Max_NeighborsExpression, gen_rule_Add_BinaryExpression, gen_rule_UnaryExpression_IntegerExpression, gen_rule_Sum_NeighborsExpression, gen_rule_And_BinaryExpression, gen_rule_Or_BinaryExpression, gen_rule_Not_UnaryExpression, gen_rule_Greater_BinaryExpression, gen_rule_Lower_BinaryExpression, gen_rule_IntegerLiteral_IntegerExpression, gen_rule_Conditional_IntegerExpression, gen_rule_CurrentCellPopulation_IntegerExpression, gen_rule_Size_NeighborsExpression, gen_rule_NeighborsExpression_IntegerExpression, gen_rule_Min_NeighborsExpression, gen_rule_BinaryExpression_IntegerExpression, gen_rule_Mult_BinaryExpression, gen_rule_Div_BinaryExpression, gen_rule_Mod_BinaryExpression, gen_rule_UMinus_UnaryExpression, gen_rule_Minus_BinaryExpression, gen_rule_Equal_BinaryExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)