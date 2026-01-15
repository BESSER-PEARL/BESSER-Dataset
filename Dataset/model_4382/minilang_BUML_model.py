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
minilang_IntExpression = Class(name="minilang::IntExpression")
minilang_Integer = Class(name="minilang::Integer")
IntExpression = Class(name="IntExpression")
minilang_Boolean = Class(name="minilang::Boolean")
BooleanExpression = Class(name="BooleanExpression")
minilang_IntOperation = Class(name="minilang::IntOperation")
minilang_Equal = Class(name="minilang::Equal")
IntComparison = Class(name="IntComparison")
minilang_GreaterOrEqual = Class(name="minilang::GreaterOrEqual")
minilang_Less = Class(name="minilang::Less")
minilang_LessOrEqual = Class(name="minilang::LessOrEqual")
minilang_Not = Class(name="minilang::Not")
minilang_BooleanExpression = Class(name="minilang::BooleanExpression")
minilang_Or = Class(name="minilang::Or")
BooleanOperation = Class(name="BooleanOperation")
minilang_And = Class(name="minilang::And")
minilang_Plus = Class(name="minilang::Plus")
IntOperation = Class(name="IntOperation")
minilang_Minus = Class(name="minilang::Minus")
minilang_Multiply = Class(name="minilang::Multiply")
minilang_Divide = Class(name="minilang::Divide")
minilang_IntComparison = Class(name="minilang::IntComparison", is_abstract=True)
minilang_BooleanOperation = Class(name="minilang::BooleanOperation")
minilang_BooleanVariableRef = Class(name="minilang::BooleanVariableRef")
VariableRef = Class(name="VariableRef")
minilang_IntVariableRef = Class(name="minilang::IntVariableRef")
minilang_VariableRef = Class(name="minilang::VariableRef")
minilang_Statement = Class(name="minilang::Statement")
minilang_BooleanAssignment = Class(name="minilang::BooleanAssignment")
Statement = Class(name="Statement")
minilang_IntAssignment = Class(name="minilang::IntAssignment")
minilang_Greater = Class(name="minilang::Greater")
minilang_PrintVar = Class(name="minilang::PrintVar")
minilang_PrintStr = Class(name="minilang::PrintStr")
minilang_Block = Class(name="minilang::Block")
minilang_If = Class(name="minilang::If")
minilang_While = Class(name="minilang::While")

# minilang_IntExpression class attributes and methods

# minilang_Integer class attributes and methods
minilang_Integer_value: Property = Property(name="value", type=IntegerType)
minilang_Integer.attributes={minilang_Integer_value}

# IntExpression class attributes and methods

# minilang_Boolean class attributes and methods
minilang_Boolean_value: Property = Property(name="value", type=BooleanType)
minilang_Boolean.attributes={minilang_Boolean_value}

# BooleanExpression class attributes and methods

# minilang_IntOperation class attributes and methods

# minilang_Equal class attributes and methods

# IntComparison class attributes and methods

# minilang_GreaterOrEqual class attributes and methods

# minilang_Less class attributes and methods

# minilang_LessOrEqual class attributes and methods

# minilang_Not class attributes and methods

# minilang_BooleanExpression class attributes and methods

# minilang_Or class attributes and methods

# BooleanOperation class attributes and methods

# minilang_And class attributes and methods

# minilang_Plus class attributes and methods

# IntOperation class attributes and methods

# minilang_Minus class attributes and methods

# minilang_Multiply class attributes and methods

# minilang_Divide class attributes and methods

# minilang_IntComparison class attributes and methods

# minilang_BooleanOperation class attributes and methods

# minilang_BooleanVariableRef class attributes and methods

# VariableRef class attributes and methods

# minilang_IntVariableRef class attributes and methods

# minilang_VariableRef class attributes and methods
minilang_VariableRef_name: Property = Property(name="name", type=StringType)
minilang_VariableRef.attributes={minilang_VariableRef_name}

# minilang_Statement class attributes and methods

# minilang_BooleanAssignment class attributes and methods

# Statement class attributes and methods

# minilang_IntAssignment class attributes and methods

# minilang_Greater class attributes and methods

# minilang_PrintVar class attributes and methods
minilang_PrintVar_value: Property = Property(name="value", type=StringType)
minilang_PrintVar.attributes={minilang_PrintVar_value}

# minilang_PrintStr class attributes and methods
minilang_PrintStr_value: Property = Property(name="value", type=StringType)
minilang_PrintStr.attributes={minilang_PrintStr_value}

# minilang_Block class attributes and methods

# minilang_If class attributes and methods

# minilang_While class attributes and methods

# Relationships
right0: BinaryAssociation = BinaryAssociation(
    name="right0",
    ends={
        Property(name="minilang_IntExpression", type=minilang_IntOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntOperation", type=minilang_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="minilang_IntExpression3", type=minilang_IntOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntOperation2", type=minilang_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression4: BinaryAssociation = BinaryAssociation(
    name="expression4",
    ends={
        Property(name="minilang_BooleanExpression", type=minilang_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Not", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right5: BinaryAssociation = BinaryAssociation(
    name="right5",
    ends={
        Property(name="minilang_IntExpression6", type=minilang_IntComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntComparison", type=minilang_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left7: BinaryAssociation = BinaryAssociation(
    name="left7",
    ends={
        Property(name="minilang_IntExpression9", type=minilang_IntComparison, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntComparison8", type=minilang_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left10: BinaryAssociation = BinaryAssociation(
    name="left10",
    ends={
        Property(name="minilang_BooleanExpression11", type=minilang_BooleanOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BooleanOperation", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right12: BinaryAssociation = BinaryAssociation(
    name="right12",
    ends={
        Property(name="minilang_BooleanExpression14", type=minilang_BooleanOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BooleanOperation13", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable15: BinaryAssociation = BinaryAssociation(
    name="variable15",
    ends={
        Property(name="minilang_BooleanVariableRef", type=minilang_BooleanAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BooleanAssignment", type=minilang_BooleanVariableRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="minilang_BooleanExpression18", type=minilang_BooleanAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BooleanAssignment17", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value20: BinaryAssociation = BinaryAssociation(
    name="value20",
    ends={
        Property(name="minilang_IntExpression22", type=minilang_IntAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntAssignment21", type=minilang_IntExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement23: BinaryAssociation = BinaryAssociation(
    name="statement23",
    ends={
        Property(name="minilang_Statement", type=minilang_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Block", type=minilang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="minilang_BooleanExpression25", type=minilang_If, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_If", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then26: BinaryAssociation = BinaryAssociation(
    name="then26",
    ends={
        Property(name="minilang_Block28", type=minilang_If, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_If27", type=minilang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else29: BinaryAssociation = BinaryAssociation(
    name="else29",
    ends={
        Property(name="minilang_Block31", type=minilang_If, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_If30", type=minilang_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="minilang_BooleanExpression33", type=minilang_While, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_While", type=minilang_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body34: BinaryAssociation = BinaryAssociation(
    name="body34",
    ends={
        Property(name="minilang_Block36", type=minilang_While, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_While35", type=minilang_Block, multiplicity=Multiplicity(1, 1))
    }
)
variable19: BinaryAssociation = BinaryAssociation(
    name="variable19",
    ends={
        Property(name="minilang_IntVariableRef", type=minilang_IntAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IntAssignment", type=minilang_IntVariableRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_minilang_Integer_IntExpression = Generalization(general=IntExpression, specific=minilang_Integer)
gen_minilang_Boolean_BooleanExpression = Generalization(general=BooleanExpression, specific=minilang_Boolean)
gen_minilang_IntOperation_IntExpression = Generalization(general=IntExpression, specific=minilang_IntOperation)
gen_minilang_Equal_IntComparison = Generalization(general=IntComparison, specific=minilang_Equal)
gen_minilang_GreaterOrEqual_IntComparison = Generalization(general=IntComparison, specific=minilang_GreaterOrEqual)
gen_minilang_Less_IntComparison = Generalization(general=IntComparison, specific=minilang_Less)
gen_minilang_LessOrEqual_IntComparison = Generalization(general=IntComparison, specific=minilang_LessOrEqual)
gen_minilang_Not_BooleanExpression = Generalization(general=BooleanExpression, specific=minilang_Not)
gen_minilang_Or_BooleanOperation = Generalization(general=BooleanOperation, specific=minilang_Or)
gen_minilang_And_BooleanOperation = Generalization(general=BooleanOperation, specific=minilang_And)
gen_minilang_Plus_IntOperation = Generalization(general=IntOperation, specific=minilang_Plus)
gen_minilang_Minus_IntOperation = Generalization(general=IntOperation, specific=minilang_Minus)
gen_minilang_Multiply_IntOperation = Generalization(general=IntOperation, specific=minilang_Multiply)
gen_minilang_Divide_IntOperation = Generalization(general=IntOperation, specific=minilang_Divide)
gen_minilang_IntComparison_BooleanExpression = Generalization(general=BooleanExpression, specific=minilang_IntComparison)
gen_minilang_BooleanOperation_BooleanExpression = Generalization(general=BooleanExpression, specific=minilang_BooleanOperation)
gen_minilang_BooleanVariableRef_VariableRef = Generalization(general=VariableRef, specific=minilang_BooleanVariableRef)
gen_minilang_BooleanVariableRef_BooleanExpression = Generalization(general=BooleanExpression, specific=minilang_BooleanVariableRef)
gen_minilang_IntVariableRef_VariableRef = Generalization(general=VariableRef, specific=minilang_IntVariableRef)
gen_minilang_IntVariableRef_IntExpression = Generalization(general=IntExpression, specific=minilang_IntVariableRef)
gen_minilang_BooleanAssignment_Statement = Generalization(general=Statement, specific=minilang_BooleanAssignment)
gen_minilang_IntAssignment_Statement = Generalization(general=Statement, specific=minilang_IntAssignment)
gen_minilang_Greater_IntComparison = Generalization(general=IntComparison, specific=minilang_Greater)
gen_minilang_PrintVar_Statement = Generalization(general=Statement, specific=minilang_PrintVar)
gen_minilang_PrintStr_Statement = Generalization(general=Statement, specific=minilang_PrintStr)

# Domain Model
domain_model = DomainModel(
    name="minilang",
    types={minilang_IntExpression, minilang_Integer, IntExpression, minilang_Boolean, BooleanExpression, minilang_IntOperation, minilang_Equal, IntComparison, minilang_GreaterOrEqual, minilang_Less, minilang_LessOrEqual, minilang_Not, minilang_BooleanExpression, minilang_Or, BooleanOperation, minilang_And, minilang_Plus, IntOperation, minilang_Minus, minilang_Multiply, minilang_Divide, minilang_IntComparison, minilang_BooleanOperation, minilang_BooleanVariableRef, VariableRef, minilang_IntVariableRef, minilang_VariableRef, minilang_Statement, minilang_BooleanAssignment, Statement, minilang_IntAssignment, minilang_Greater, minilang_PrintVar, minilang_PrintStr, minilang_Block, minilang_If, minilang_While},
    associations={right0, left1, expression4, right5, left7, left10, right12, variable15, value16, value20, statement23, condition24, then26, else29, condition32, body34, variable19},
    generalizations={gen_minilang_Integer_IntExpression, gen_minilang_Boolean_BooleanExpression, gen_minilang_IntOperation_IntExpression, gen_minilang_Equal_IntComparison, gen_minilang_GreaterOrEqual_IntComparison, gen_minilang_Less_IntComparison, gen_minilang_LessOrEqual_IntComparison, gen_minilang_Not_BooleanExpression, gen_minilang_Or_BooleanOperation, gen_minilang_And_BooleanOperation, gen_minilang_Plus_IntOperation, gen_minilang_Minus_IntOperation, gen_minilang_Multiply_IntOperation, gen_minilang_Divide_IntOperation, gen_minilang_IntComparison_BooleanExpression, gen_minilang_BooleanOperation_BooleanExpression, gen_minilang_BooleanVariableRef_VariableRef, gen_minilang_BooleanVariableRef_BooleanExpression, gen_minilang_IntVariableRef_VariableRef, gen_minilang_IntVariableRef_IntExpression, gen_minilang_BooleanAssignment_Statement, gen_minilang_IntAssignment_Statement, gen_minilang_Greater_IntComparison, gen_minilang_PrintVar_Statement, gen_minilang_PrintStr_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)