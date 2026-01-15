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
realop_Realop = Class(name="realop::Realop")
realop_Operator = Class(name="realop::Operator")
realop_Expression = Class(name="realop::Expression")
realop_OrExp = Class(name="realop::OrExp")
Expression = Class(name="Expression")
realop_AndExp = Class(name="realop::AndExp")
realop_XorExp = Class(name="realop::XorExp")
realop_NotExp = Class(name="realop::NotExp")
realop_IsRealised = Class(name="realop::IsRealised")
realop_IsPositive = Class(name="realop::IsPositive")
realop_IsNegative = Class(name="realop::IsNegative")

# realop_Realop class attributes and methods

# realop_Operator class attributes and methods
realop_Operator_name: Property = Property(name="name", type=StringType)
realop_Operator.attributes={realop_Operator_name}

# realop_Expression class attributes and methods

# realop_OrExp class attributes and methods

# Expression class attributes and methods

# realop_AndExp class attributes and methods

# realop_XorExp class attributes and methods

# realop_NotExp class attributes and methods

# realop_IsRealised class attributes and methods
realop_IsRealised_featureName: Property = Property(name="featureName", type=StringType)
realop_IsRealised.attributes={realop_IsRealised_featureName}

# realop_IsPositive class attributes and methods
realop_IsPositive_featureName: Property = Property(name="featureName", type=StringType)
realop_IsPositive.attributes={realop_IsPositive_featureName}

# realop_IsNegative class attributes and methods
realop_IsNegative_featureName: Property = Property(name="featureName", type=StringType)
realop_IsNegative.attributes={realop_IsNegative_featureName}

# Relationships
operators0: BinaryAssociation = BinaryAssociation(
    name="operators0",
    ends={
        Property(name="realop_Operator", type=realop_Realop, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_Realop", type=realop_Operator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expPre1: BinaryAssociation = BinaryAssociation(
    name="expPre1",
    ends={
        Property(name="realop_Expression", type=realop_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_Operator2", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expPost3: BinaryAssociation = BinaryAssociation(
    name="expPost3",
    ends={
        Property(name="realop_Expression5", type=realop_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_Operator4", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="realop_Expression7", type=realop_OrExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_OrExp", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="realop_Expression10", type=realop_OrExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_OrExp9", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="realop_Expression12", type=realop_AndExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_AndExp", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="realop_Expression15", type=realop_AndExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_AndExp14", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="realop_Expression17", type=realop_XorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_XorExp", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="realop_Expression20", type=realop_XorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_XorExp19", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp21: BinaryAssociation = BinaryAssociation(
    name="exp21",
    ends={
        Property(name="realop_Expression22", type=realop_NotExp, multiplicity=Multiplicity(1, 1)),
        Property(name="realop_NotExp", type=realop_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_realop_OrExp_Expression = Generalization(general=Expression, specific=realop_OrExp)
gen_realop_AndExp_Expression = Generalization(general=Expression, specific=realop_AndExp)
gen_realop_XorExp_Expression = Generalization(general=Expression, specific=realop_XorExp)
gen_realop_NotExp_Expression = Generalization(general=Expression, specific=realop_NotExp)
gen_realop_IsRealised_Expression = Generalization(general=Expression, specific=realop_IsRealised)
gen_realop_IsPositive_Expression = Generalization(general=Expression, specific=realop_IsPositive)
gen_realop_IsNegative_Expression = Generalization(general=Expression, specific=realop_IsNegative)

# Domain Model
domain_model = DomainModel(
    name="realop",
    types={realop_Realop, realop_Operator, realop_Expression, realop_OrExp, Expression, realop_AndExp, realop_XorExp, realop_NotExp, realop_IsRealised, realop_IsPositive, realop_IsNegative},
    associations={operators0, expPre1, expPost3, left6, right8, left11, right13, left16, right18, exp21},
    generalizations={gen_realop_OrExp_Expression, gen_realop_AndExp_Expression, gen_realop_XorExp_Expression, gen_realop_NotExp_Expression, gen_realop_IsRealised_Expression, gen_realop_IsPositive_Expression, gen_realop_IsNegative_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)