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
BinaryCalculator_Model = Class(name="BinaryCalculator::Model")
BinaryCalculator_BinaryCalculator = Class(name="BinaryCalculator::BinaryCalculator")
BinaryCalculator_BitSeq = Class(name="BinaryCalculator::BitSeq", is_abstract=True)
BinaryCalculator_Value = Class(name="BinaryCalculator::Value")
BinaryCalculator_L = Class(name="BinaryCalculator::L")
BitSeq = Class(name="BitSeq")
BinaryCalculator_Bit = Class(name="BinaryCalculator::Bit")

# BinaryCalculator_Model class attributes and methods

# BinaryCalculator_BinaryCalculator class attributes and methods
BinaryCalculator_BinaryCalculator_description: Property = Property(name="description", type=StringType)
BinaryCalculator_BinaryCalculator.attributes={BinaryCalculator_BinaryCalculator_description}

# BinaryCalculator_BitSeq class attributes and methods

# BinaryCalculator_Value class attributes and methods
BinaryCalculator_Value_value: Property = Property(name="value", type=StringType)
BinaryCalculator_Value.attributes={BinaryCalculator_Value_value}

# BinaryCalculator_L class attributes and methods

# BitSeq class attributes and methods

# BinaryCalculator_Bit class attributes and methods
BinaryCalculator_Bit_value: Property = Property(name="value", type=StringType)
BinaryCalculator_Bit.attributes={BinaryCalculator_Bit_value}

# Relationships
calculators0: BinaryAssociation = BinaryAssociation(
    name="calculators0",
    ends={
        Property(name="BinaryCalculator_BinaryCalculator", type=BinaryCalculator_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="BinaryCalculator_Model", type=BinaryCalculator_BinaryCalculator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
number1: BinaryAssociation = BinaryAssociation(
    name="number1",
    ends={
        Property(name="BinaryCalculator_BitSeq", type=BinaryCalculator_BinaryCalculator, multiplicity=Multiplicity(1, 1)),
        Property(name="BinaryCalculator_BinaryCalculator2", type=BinaryCalculator_BitSeq, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result3: BinaryAssociation = BinaryAssociation(
    name="result3",
    ends={
        Property(name="BinaryCalculator_Value", type=BinaryCalculator_BinaryCalculator, multiplicity=Multiplicity(1, 1)),
        Property(name="BinaryCalculator_BinaryCalculator4", type=BinaryCalculator_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="BinaryCalculator_BitSeq6", type=BinaryCalculator_L, multiplicity=Multiplicity(1, 1)),
        Property(name="BinaryCalculator_L", type=BinaryCalculator_BitSeq, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rigth7: BinaryAssociation = BinaryAssociation(
    name="rigth7",
    ends={
        Property(name="BinaryCalculator_Bit", type=BinaryCalculator_L, multiplicity=Multiplicity(1, 1)),
        Property(name="BinaryCalculator_L8", type=BinaryCalculator_Bit, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_BinaryCalculator_L_BitSeq = Generalization(general=BitSeq, specific=BinaryCalculator_L)
gen_BinaryCalculator_Bit_BitSeq = Generalization(general=BitSeq, specific=BinaryCalculator_Bit)

# Domain Model
domain_model = DomainModel(
    name="BinaryCalculator",
    types={BinaryCalculator_Model, BinaryCalculator_BinaryCalculator, BinaryCalculator_BitSeq, BinaryCalculator_Value, BinaryCalculator_L, BitSeq, BinaryCalculator_Bit},
    associations={calculators0, number1, result3, left5, rigth7},
    generalizations={gen_BinaryCalculator_L_BitSeq, gen_BinaryCalculator_Bit_BitSeq},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)