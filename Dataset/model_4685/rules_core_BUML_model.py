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
rules_core_Minus = Class(name="rules::core::Minus")
rules_core_Mult = Class(name="rules::core::Mult")
rules_core_Div = Class(name="rules::core::Div")
rules_core_Max = Class(name="rules::core::Max")
rules_core_Min = Class(name="rules::core::Min")
rules_core_Greater = Class(name="rules::core::Greater")
rules_core_Expression = Class(name="rules::core::Expression", is_abstract=True)
rules_core_Rule = Class(name="rules::core::Rule")
rules_core_Filter = Class(name="rules::core::Filter")
rules_core_BinaryExp = Class(name="rules::core::BinaryExp")
Expression = Class(name="Expression")
rules_core_Plus = Class(name="rules::core::Plus")
BinaryExp = Class(name="BinaryExp")
rules_core_Lower = Class(name="rules::core::Lower")
rules_core_Equals = Class(name="rules::core::Equals")
rules_core_Constant = Class(name="rules::core::Constant")
rules_core_If = Class(name="rules::core::If")

# rules_core_Minus class attributes and methods

# rules_core_Mult class attributes and methods

# rules_core_Div class attributes and methods

# rules_core_Max class attributes and methods

# rules_core_Min class attributes and methods

# rules_core_Greater class attributes and methods

# rules_core_Expression class attributes and methods

# rules_core_Rule class attributes and methods

# rules_core_Filter class attributes and methods

# rules_core_BinaryExp class attributes and methods

# Expression class attributes and methods

# rules_core_Plus class attributes and methods

# BinaryExp class attributes and methods

# rules_core_Lower class attributes and methods

# rules_core_Equals class attributes and methods

# rules_core_Constant class attributes and methods
rules_core_Constant_integerValue: Property = Property(name="integerValue", type=IntegerType)
rules_core_Constant.attributes={rules_core_Constant_integerValue}

# rules_core_If class attributes and methods

# Relationships
condition0: BinaryAssociation = BinaryAssociation(
    name="condition0",
    ends={
        Property(name="rules_core_Expression", type=rules_core_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_Rule", type=rules_core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs1: BinaryAssociation = BinaryAssociation(
    name="rhs1",
    ends={
        Property(name="rules_core_Expression2", type=rules_core_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_BinaryExp", type=rules_core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs3: BinaryAssociation = BinaryAssociation(
    name="lhs3",
    ends={
        Property(name="rules_core_Expression5", type=rules_core_BinaryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_BinaryExp4", type=rules_core_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition6: BinaryAssociation = BinaryAssociation(
    name="condition6",
    ends={
        Property(name="rules_core_Expression7", type=rules_core_If, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_If", type=rules_core_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenPart8: BinaryAssociation = BinaryAssociation(
    name="thenPart8",
    ends={
        Property(name="rules_core_Expression10", type=rules_core_If, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_If9", type=rules_core_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart11: BinaryAssociation = BinaryAssociation(
    name="elsePart11",
    ends={
        Property(name="rules_core_Expression13", type=rules_core_If, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_core_If12", type=rules_core_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_rules_core_Minus_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Minus)
gen_rules_core_Mult_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Mult)
gen_rules_core_Div_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Div)
gen_rules_core_Max_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Max)
gen_rules_core_Min_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Min)
gen_rules_core_Greater_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Greater)
gen_rules_core_BinaryExp_Expression = Generalization(general=Expression, specific=rules_core_BinaryExp)
gen_rules_core_Plus_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Plus)
gen_rules_core_Lower_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Lower)
gen_rules_core_Equals_BinaryExp = Generalization(general=BinaryExp, specific=rules_core_Equals)
gen_rules_core_Constant_Expression = Generalization(general=Expression, specific=rules_core_Constant)
gen_rules_core_If_Expression = Generalization(general=Expression, specific=rules_core_If)

# Domain Model
domain_model = DomainModel(
    name="rules_core",
    types={rules_core_Minus, rules_core_Mult, rules_core_Div, rules_core_Max, rules_core_Min, rules_core_Greater, rules_core_Expression, rules_core_Rule, rules_core_Filter, rules_core_BinaryExp, Expression, rules_core_Plus, BinaryExp, rules_core_Lower, rules_core_Equals, rules_core_Constant, rules_core_If},
    associations={condition0, rhs1, lhs3, condition6, thenPart8, elsePart11},
    generalizations={gen_rules_core_Minus_BinaryExp, gen_rules_core_Mult_BinaryExp, gen_rules_core_Div_BinaryExp, gen_rules_core_Max_BinaryExp, gen_rules_core_Min_BinaryExp, gen_rules_core_Greater_BinaryExp, gen_rules_core_BinaryExp_Expression, gen_rules_core_Plus_BinaryExp, gen_rules_core_Lower_BinaryExp, gen_rules_core_Equals_BinaryExp, gen_rules_core_Constant_Expression, gen_rules_core_If_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)