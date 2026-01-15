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
expressionDSL_SubFieldDef = Class(name="expressionDSL::SubFieldDef")
expressionDSL_FunctionDef = Class(name="expressionDSL::FunctionDef")
expressionDSL_VariableAssignment = Class(name="expressionDSL::VariableAssignment")
expressionDSL_Model = Class(name="expressionDSL::Model")
expressionDSL_Statement = Class(name="expressionDSL::Statement")
expressionDSL_VariableDef = Class(name="expressionDSL::VariableDef")
Statement = Class(name="Statement")
Named = Class(name="Named")
expressionDSL_Dim = Class(name="expressionDSL::Dim")
expressionDSL_ConstDef = Class(name="expressionDSL::ConstDef")
expressionDSL_StructDef = Class(name="expressionDSL::StructDef")
SubField = Class(name="SubField")
expressionDSL_SubField = Class(name="expressionDSL::SubField")
expressionDSL_Comparison = Class(name="expressionDSL::Comparison")
expressionDSL_BinaryPlus = Class(name="expressionDSL::BinaryPlus")
expressionDSL_Expression = Class(name="expressionDSL::Expression")
expressionDSL_FunctionCallStatement = Class(name="expressionDSL::FunctionCallStatement")
expressionDSL_FunctionCall = Class(name="expressionDSL::FunctionCall")
expressionDSL_Named = Class(name="expressionDSL::Named")
expressionDSL_VariableArrayOrFunctionRef = Class(name="expressionDSL::VariableArrayOrFunctionRef")
Expression = Class(name="Expression")
expressionDSL_Or = Class(name="expressionDSL::Or")
expressionDSL_And = Class(name="expressionDSL::And")
expressionDSL_Not = Class(name="expressionDSL::Not")
expressionDSL_QualifiedRef = Class(name="expressionDSL::QualifiedRef")
expressionDSL_BinaryMinus = Class(name="expressionDSL::BinaryMinus")
expressionDSL_MulOrDiv = Class(name="expressionDSL::MulOrDiv")
expressionDSL_Exponent = Class(name="expressionDSL::Exponent")
expressionDSL_UnaryPlus = Class(name="expressionDSL::UnaryPlus")
expressionDSL_UnaryMinus = Class(name="expressionDSL::UnaryMinus")
expressionDSL_IntConstant = Class(name="expressionDSL::IntConstant")
expressionDSL_StringConstant = Class(name="expressionDSL::StringConstant")
expressionDSL_BooleanConstant = Class(name="expressionDSL::BooleanConstant")

# expressionDSL_SubFieldDef class attributes and methods
expressionDSL_SubFieldDef_type: Property = Property(name="type", type=StringType)
expressionDSL_SubFieldDef.attributes={expressionDSL_SubFieldDef_type}

# expressionDSL_FunctionDef class attributes and methods
expressionDSL_FunctionDef_type: Property = Property(name="type", type=StringType)
expressionDSL_FunctionDef.attributes={expressionDSL_FunctionDef_type}

# expressionDSL_VariableAssignment class attributes and methods
expressionDSL_VariableAssignment_op: Property = Property(name="op", type=StringType)
expressionDSL_VariableAssignment.attributes={expressionDSL_VariableAssignment_op}

# expressionDSL_Model class attributes and methods

# expressionDSL_Statement class attributes and methods

# expressionDSL_VariableDef class attributes and methods
expressionDSL_VariableDef_type: Property = Property(name="type", type=StringType)
expressionDSL_VariableDef.attributes={expressionDSL_VariableDef_type}

# Statement class attributes and methods

# Named class attributes and methods

# expressionDSL_Dim class attributes and methods
expressionDSL_Dim_arrayDimensions: Property = Property(name="arrayDimensions", type=IntegerType)
expressionDSL_Dim.attributes={expressionDSL_Dim_arrayDimensions}

# expressionDSL_ConstDef class attributes and methods
expressionDSL_ConstDef_type: Property = Property(name="type", type=StringType)
expressionDSL_ConstDef.attributes={expressionDSL_ConstDef_type}

# expressionDSL_StructDef class attributes and methods

# SubField class attributes and methods

# expressionDSL_SubField class attributes and methods

# expressionDSL_Comparison class attributes and methods
expressionDSL_Comparison_op: Property = Property(name="op", type=StringType)
expressionDSL_Comparison.attributes={expressionDSL_Comparison_op}

# expressionDSL_BinaryPlus class attributes and methods

# expressionDSL_Expression class attributes and methods

# expressionDSL_FunctionCallStatement class attributes and methods

# expressionDSL_FunctionCall class attributes and methods

# expressionDSL_Named class attributes and methods
expressionDSL_Named_name: Property = Property(name="name", type=StringType)
expressionDSL_Named.attributes={expressionDSL_Named_name}

# expressionDSL_VariableArrayOrFunctionRef class attributes and methods

# Expression class attributes and methods

# expressionDSL_Or class attributes and methods

# expressionDSL_And class attributes and methods

# expressionDSL_Not class attributes and methods

# expressionDSL_QualifiedRef class attributes and methods

# expressionDSL_BinaryMinus class attributes and methods

# expressionDSL_MulOrDiv class attributes and methods
expressionDSL_MulOrDiv_op: Property = Property(name="op", type=StringType)
expressionDSL_MulOrDiv.attributes={expressionDSL_MulOrDiv_op}

# expressionDSL_Exponent class attributes and methods

# expressionDSL_UnaryPlus class attributes and methods

# expressionDSL_UnaryMinus class attributes and methods

# expressionDSL_IntConstant class attributes and methods
expressionDSL_IntConstant_value: Property = Property(name="value", type=IntegerType)
expressionDSL_IntConstant.attributes={expressionDSL_IntConstant_value}

# expressionDSL_StringConstant class attributes and methods
expressionDSL_StringConstant_value: Property = Property(name="value", type=StringType)
expressionDSL_StringConstant.attributes={expressionDSL_StringConstant_value}

# expressionDSL_BooleanConstant class attributes and methods
expressionDSL_BooleanConstant_value: Property = Property(name="value", type=StringType)
expressionDSL_BooleanConstant.attributes={expressionDSL_BooleanConstant_value}

# Relationships
options8: BinaryAssociation = BinaryAssociation(
    name="options8",
    ends={
        Property(name="expressionDSL_Dim9", type=expressionDSL_SubFieldDef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_SubFieldDef", type=expressionDSL_Dim, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="expressionDSL_Statement", type=expressionDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Model", type=expressionDSL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
options1: BinaryAssociation = BinaryAssociation(
    name="options1",
    ends={
        Property(name="expressionDSL_Dim", type=expressionDSL_VariableDef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_VariableDef", type=expressionDSL_Dim, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
options2: BinaryAssociation = BinaryAssociation(
    name="options2",
    ends={
        Property(name="expressionDSL_Dim3", type=expressionDSL_ConstDef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_ConstDef", type=expressionDSL_Dim, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
options4: BinaryAssociation = BinaryAssociation(
    name="options4",
    ends={
        Property(name="expressionDSL_Dim5", type=expressionDSL_StructDef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_StructDef", type=expressionDSL_Dim, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subFields6: BinaryAssociation = BinaryAssociation(
    name="subFields6",
    ends={
        Property(name="expressionDSL_SubField", type=expressionDSL_StructDef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_StructDef7", type=expressionDSL_SubField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right31: BinaryAssociation = BinaryAssociation(
    name="right31",
    ends={
        Property(name="expressionDSL_Expression33", type=expressionDSL_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_And32", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left34: BinaryAssociation = BinaryAssociation(
    name="left34",
    ends={
        Property(name="expressionDSL_Expression35", type=expressionDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Comparison", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right36: BinaryAssociation = BinaryAssociation(
    name="right36",
    ends={
        Property(name="expressionDSL_Expression38", type=expressionDSL_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Comparison37", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tgtvar10: BinaryAssociation = BinaryAssociation(
    name="tgtvar10",
    ends={
        Property(name="expressionDSL_VariableDef11", type=expressionDSL_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_VariableAssignment", type=expressionDSL_VariableDef, multiplicity=Multiplicity(0, 1))
    }
)
exp12: BinaryAssociation = BinaryAssociation(
    name="exp12",
    ends={
        Property(name="expressionDSL_Expression", type=expressionDSL_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_VariableAssignment13", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
call14: BinaryAssociation = BinaryAssociation(
    name="call14",
    ends={
        Property(name="expressionDSL_FunctionCall", type=expressionDSL_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_FunctionCallStatement", type=expressionDSL_FunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref15: BinaryAssociation = BinaryAssociation(
    name="ref15",
    ends={
        Property(name="expressionDSL_FunctionDef", type=expressionDSL_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_FunctionCall16", type=expressionDSL_FunctionDef, multiplicity=Multiplicity(0, 1))
    }
)
args17: BinaryAssociation = BinaryAssociation(
    name="args17",
    ends={
        Property(name="expressionDSL_Expression19", type=expressionDSL_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_FunctionCall18", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref20: BinaryAssociation = BinaryAssociation(
    name="ref20",
    ends={
        Property(name="expressionDSL_Named", type=expressionDSL_VariableArrayOrFunctionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_VariableArrayOrFunctionRef", type=expressionDSL_Named, multiplicity=Multiplicity(0, 1))
    }
)
args21: BinaryAssociation = BinaryAssociation(
    name="args21",
    ends={
        Property(name="expressionDSL_Expression23", type=expressionDSL_VariableArrayOrFunctionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_VariableArrayOrFunctionRef22", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left24: BinaryAssociation = BinaryAssociation(
    name="left24",
    ends={
        Property(name="expressionDSL_Expression25", type=expressionDSL_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Or", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right26: BinaryAssociation = BinaryAssociation(
    name="right26",
    ends={
        Property(name="expressionDSL_Expression28", type=expressionDSL_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Or27", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left29: BinaryAssociation = BinaryAssociation(
    name="left29",
    ends={
        Property(name="expressionDSL_Expression30", type=expressionDSL_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_And", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr63: BinaryAssociation = BinaryAssociation(
    name="expr63",
    ends={
        Property(name="expressionDSL_Expression64", type=expressionDSL_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Not", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
head65: BinaryAssociation = BinaryAssociation(
    name="head65",
    ends={
        Property(name="expressionDSL_Expression66", type=expressionDSL_QualifiedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_QualifiedRef", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tail67: BinaryAssociation = BinaryAssociation(
    name="tail67",
    ends={
        Property(name="expressionDSL_Expression69", type=expressionDSL_QualifiedRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_QualifiedRef68", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left39: BinaryAssociation = BinaryAssociation(
    name="left39",
    ends={
        Property(name="expressionDSL_Expression40", type=expressionDSL_BinaryPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_BinaryPlus", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right41: BinaryAssociation = BinaryAssociation(
    name="right41",
    ends={
        Property(name="expressionDSL_Expression43", type=expressionDSL_BinaryPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_BinaryPlus42", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left44: BinaryAssociation = BinaryAssociation(
    name="left44",
    ends={
        Property(name="expressionDSL_Expression45", type=expressionDSL_BinaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_BinaryMinus", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right46: BinaryAssociation = BinaryAssociation(
    name="right46",
    ends={
        Property(name="expressionDSL_Expression48", type=expressionDSL_BinaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_BinaryMinus47", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left49: BinaryAssociation = BinaryAssociation(
    name="left49",
    ends={
        Property(name="expressionDSL_Expression50", type=expressionDSL_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_MulOrDiv", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right51: BinaryAssociation = BinaryAssociation(
    name="right51",
    ends={
        Property(name="expressionDSL_Expression53", type=expressionDSL_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_MulOrDiv52", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left54: BinaryAssociation = BinaryAssociation(
    name="left54",
    ends={
        Property(name="expressionDSL_Expression55", type=expressionDSL_Exponent, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Exponent", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right56: BinaryAssociation = BinaryAssociation(
    name="right56",
    ends={
        Property(name="expressionDSL_Expression58", type=expressionDSL_Exponent, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_Exponent57", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr59: BinaryAssociation = BinaryAssociation(
    name="expr59",
    ends={
        Property(name="expressionDSL_Expression60", type=expressionDSL_UnaryPlus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_UnaryPlus", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr61: BinaryAssociation = BinaryAssociation(
    name="expr61",
    ends={
        Property(name="expressionDSL_Expression62", type=expressionDSL_UnaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressionDSL_UnaryMinus", type=expressionDSL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expressionDSL_SubFieldDef_SubField = Generalization(general=SubField, specific=expressionDSL_SubFieldDef)
gen_expressionDSL_SubFieldDef_Named = Generalization(general=Named, specific=expressionDSL_SubFieldDef)
gen_expressionDSL_FunctionDef_Statement = Generalization(general=Statement, specific=expressionDSL_FunctionDef)
gen_expressionDSL_FunctionDef_Named = Generalization(general=Named, specific=expressionDSL_FunctionDef)
gen_expressionDSL_VariableAssignment_Statement = Generalization(general=Statement, specific=expressionDSL_VariableAssignment)
gen_expressionDSL_VariableDef_Statement = Generalization(general=Statement, specific=expressionDSL_VariableDef)
gen_expressionDSL_VariableDef_Named = Generalization(general=Named, specific=expressionDSL_VariableDef)
gen_expressionDSL_ConstDef_Statement = Generalization(general=Statement, specific=expressionDSL_ConstDef)
gen_expressionDSL_ConstDef_Named = Generalization(general=Named, specific=expressionDSL_ConstDef)
gen_expressionDSL_StructDef_Statement = Generalization(general=Statement, specific=expressionDSL_StructDef)
gen_expressionDSL_StructDef_SubField = Generalization(general=SubField, specific=expressionDSL_StructDef)
gen_expressionDSL_StructDef_Named = Generalization(general=Named, specific=expressionDSL_StructDef)
gen_expressionDSL_Comparison_Expression = Generalization(general=Expression, specific=expressionDSL_Comparison)
gen_expressionDSL_BinaryPlus_Expression = Generalization(general=Expression, specific=expressionDSL_BinaryPlus)
gen_expressionDSL_FunctionCallStatement_Statement = Generalization(general=Statement, specific=expressionDSL_FunctionCallStatement)
gen_expressionDSL_VariableArrayOrFunctionRef_Expression = Generalization(general=Expression, specific=expressionDSL_VariableArrayOrFunctionRef)
gen_expressionDSL_Or_Expression = Generalization(general=Expression, specific=expressionDSL_Or)
gen_expressionDSL_And_Expression = Generalization(general=Expression, specific=expressionDSL_And)
gen_expressionDSL_Not_Expression = Generalization(general=Expression, specific=expressionDSL_Not)
gen_expressionDSL_QualifiedRef_Expression = Generalization(general=Expression, specific=expressionDSL_QualifiedRef)
gen_expressionDSL_BinaryMinus_Expression = Generalization(general=Expression, specific=expressionDSL_BinaryMinus)
gen_expressionDSL_MulOrDiv_Expression = Generalization(general=Expression, specific=expressionDSL_MulOrDiv)
gen_expressionDSL_Exponent_Expression = Generalization(general=Expression, specific=expressionDSL_Exponent)
gen_expressionDSL_UnaryPlus_Expression = Generalization(general=Expression, specific=expressionDSL_UnaryPlus)
gen_expressionDSL_UnaryMinus_Expression = Generalization(general=Expression, specific=expressionDSL_UnaryMinus)
gen_expressionDSL_IntConstant_Expression = Generalization(general=Expression, specific=expressionDSL_IntConstant)
gen_expressionDSL_StringConstant_Expression = Generalization(general=Expression, specific=expressionDSL_StringConstant)
gen_expressionDSL_BooleanConstant_Expression = Generalization(general=Expression, specific=expressionDSL_BooleanConstant)

# Domain Model
domain_model = DomainModel(
    name="expressionDSL",
    types={expressionDSL_SubFieldDef, expressionDSL_FunctionDef, expressionDSL_VariableAssignment, expressionDSL_Model, expressionDSL_Statement, expressionDSL_VariableDef, Statement, Named, expressionDSL_Dim, expressionDSL_ConstDef, expressionDSL_StructDef, SubField, expressionDSL_SubField, expressionDSL_Comparison, expressionDSL_BinaryPlus, expressionDSL_Expression, expressionDSL_FunctionCallStatement, expressionDSL_FunctionCall, expressionDSL_Named, expressionDSL_VariableArrayOrFunctionRef, Expression, expressionDSL_Or, expressionDSL_And, expressionDSL_Not, expressionDSL_QualifiedRef, expressionDSL_BinaryMinus, expressionDSL_MulOrDiv, expressionDSL_Exponent, expressionDSL_UnaryPlus, expressionDSL_UnaryMinus, expressionDSL_IntConstant, expressionDSL_StringConstant, expressionDSL_BooleanConstant},
    associations={options8, statements0, options1, options2, options4, subFields6, right31, left34, right36, tgtvar10, exp12, call14, ref15, args17, ref20, args21, left24, right26, left29, expr63, head65, tail67, left39, right41, left44, right46, left49, right51, left54, right56, expr59, expr61},
    generalizations={gen_expressionDSL_SubFieldDef_SubField, gen_expressionDSL_SubFieldDef_Named, gen_expressionDSL_FunctionDef_Statement, gen_expressionDSL_FunctionDef_Named, gen_expressionDSL_VariableAssignment_Statement, gen_expressionDSL_VariableDef_Statement, gen_expressionDSL_VariableDef_Named, gen_expressionDSL_ConstDef_Statement, gen_expressionDSL_ConstDef_Named, gen_expressionDSL_StructDef_Statement, gen_expressionDSL_StructDef_SubField, gen_expressionDSL_StructDef_Named, gen_expressionDSL_Comparison_Expression, gen_expressionDSL_BinaryPlus_Expression, gen_expressionDSL_FunctionCallStatement_Statement, gen_expressionDSL_VariableArrayOrFunctionRef_Expression, gen_expressionDSL_Or_Expression, gen_expressionDSL_And_Expression, gen_expressionDSL_Not_Expression, gen_expressionDSL_QualifiedRef_Expression, gen_expressionDSL_BinaryMinus_Expression, gen_expressionDSL_MulOrDiv_Expression, gen_expressionDSL_Exponent_Expression, gen_expressionDSL_UnaryPlus_Expression, gen_expressionDSL_UnaryMinus_Expression, gen_expressionDSL_IntConstant_Expression, gen_expressionDSL_StringConstant_Expression, gen_expressionDSL_BooleanConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)