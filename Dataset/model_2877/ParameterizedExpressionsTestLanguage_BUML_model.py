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
parameterizedExpressionsTestLanguage_LabelledStatement = Class(name="parameterizedExpressionsTestLanguage::LabelledStatement")
parameterizedExpressionsTestLanguage_IdentifierRef = Class(name="parameterizedExpressionsTestLanguage::IdentifierRef")
Expression = Class(name="Expression")
parameterizedExpressionsTestLanguage_IndexedAccessExpression = Class(name="parameterizedExpressionsTestLanguage::IndexedAccessExpression")
parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression = Class(name="parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression")
parameterizedExpressionsTestLanguage_ShiftExpression = Class(name="parameterizedExpressionsTestLanguage::ShiftExpression")
parameterizedExpressionsTestLanguage_Statement = Class(name="parameterizedExpressionsTestLanguage::Statement")
parameterizedExpressionsTestLanguage_FunctionDeclaration = Class(name="parameterizedExpressionsTestLanguage::FunctionDeclaration")
Statement = Class(name="Statement")
parameterizedExpressionsTestLanguage_Block = Class(name="parameterizedExpressionsTestLanguage::Block")
parameterizedExpressionsTestLanguage_ExpressionStatement = Class(name="parameterizedExpressionsTestLanguage::ExpressionStatement")
parameterizedExpressionsTestLanguage_Expression = Class(name="parameterizedExpressionsTestLanguage::Expression")
parameterizedExpressionsTestLanguage_CommaExpression = Class(name="parameterizedExpressionsTestLanguage::CommaExpression")
parameterizedExpressionsTestLanguage_RelationalExpression = Class(name="parameterizedExpressionsTestLanguage::RelationalExpression")
parameterizedExpressionsTestLanguage_AssignmentExpression = Class(name="parameterizedExpressionsTestLanguage::AssignmentExpression")
parameterizedExpressionsTestLanguage_YieldExpression = Class(name="parameterizedExpressionsTestLanguage::YieldExpression")

# parameterizedExpressionsTestLanguage_LabelledStatement class attributes and methods
parameterizedExpressionsTestLanguage_LabelledStatement_name: Property = Property(name="name", type=StringType)
parameterizedExpressionsTestLanguage_LabelledStatement.attributes={parameterizedExpressionsTestLanguage_LabelledStatement_name}

# parameterizedExpressionsTestLanguage_IdentifierRef class attributes and methods
parameterizedExpressionsTestLanguage_IdentifierRef_id: Property = Property(name="id", type=StringType)
parameterizedExpressionsTestLanguage_IdentifierRef.attributes={parameterizedExpressionsTestLanguage_IdentifierRef_id}

# Expression class attributes and methods

# parameterizedExpressionsTestLanguage_IndexedAccessExpression class attributes and methods

# parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression class attributes and methods
parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_property: Property = Property(name="property", type=StringType)
parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression.attributes={parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_property}

# parameterizedExpressionsTestLanguage_ShiftExpression class attributes and methods
parameterizedExpressionsTestLanguage_ShiftExpression_op: Property = Property(name="op", type=StringType)
parameterizedExpressionsTestLanguage_ShiftExpression.attributes={parameterizedExpressionsTestLanguage_ShiftExpression_op}

# parameterizedExpressionsTestLanguage_Statement class attributes and methods

# parameterizedExpressionsTestLanguage_FunctionDeclaration class attributes and methods
parameterizedExpressionsTestLanguage_FunctionDeclaration_generator: Property = Property(name="generator", type=BooleanType)
parameterizedExpressionsTestLanguage_FunctionDeclaration_name: Property = Property(name="name", type=StringType)
parameterizedExpressionsTestLanguage_FunctionDeclaration.attributes={parameterizedExpressionsTestLanguage_FunctionDeclaration_generator, parameterizedExpressionsTestLanguage_FunctionDeclaration_name}

# Statement class attributes and methods

# parameterizedExpressionsTestLanguage_Block class attributes and methods

# parameterizedExpressionsTestLanguage_ExpressionStatement class attributes and methods

# parameterizedExpressionsTestLanguage_Expression class attributes and methods

# parameterizedExpressionsTestLanguage_CommaExpression class attributes and methods

# parameterizedExpressionsTestLanguage_RelationalExpression class attributes and methods
parameterizedExpressionsTestLanguage_RelationalExpression_op: Property = Property(name="op", type=StringType)
parameterizedExpressionsTestLanguage_RelationalExpression.attributes={parameterizedExpressionsTestLanguage_RelationalExpression_op}

# parameterizedExpressionsTestLanguage_AssignmentExpression class attributes and methods
parameterizedExpressionsTestLanguage_AssignmentExpression_op: Property = Property(name="op", type=StringType)
parameterizedExpressionsTestLanguage_AssignmentExpression.attributes={parameterizedExpressionsTestLanguage_AssignmentExpression_op}

# parameterizedExpressionsTestLanguage_YieldExpression class attributes and methods
parameterizedExpressionsTestLanguage_YieldExpression_many: Property = Property(name="many", type=BooleanType)
parameterizedExpressionsTestLanguage_YieldExpression.attributes={parameterizedExpressionsTestLanguage_YieldExpression_many}

# Relationships
expression3: BinaryAssociation = BinaryAssociation(
    name="expression3",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression", type=parameterizedExpressionsTestLanguage_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_ExpressionStatement", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement4: BinaryAssociation = BinaryAssociation(
    name="statement4",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Statement5", type=parameterizedExpressionsTestLanguage_LabelledStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_LabelledStatement", type=parameterizedExpressionsTestLanguage_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression7", type=parameterizedExpressionsTestLanguage_IndexedAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_IndexedAccessExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index8: BinaryAssociation = BinaryAssociation(
    name="index8",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression10", type=parameterizedExpressionsTestLanguage_IndexedAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_IndexedAccessExpression9", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression12", type=parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs13: BinaryAssociation = BinaryAssociation(
    name="lhs13",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression14", type=parameterizedExpressionsTestLanguage_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_ShiftExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs15: BinaryAssociation = BinaryAssociation(
    name="rhs15",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression17", type=parameterizedExpressionsTestLanguage_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_ShiftExpression16", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Block", type=parameterizedExpressionsTestLanguage_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_FunctionDeclaration", type=parameterizedExpressionsTestLanguage_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements1: BinaryAssociation = BinaryAssociation(
    name="statements1",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Statement", type=parameterizedExpressionsTestLanguage_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_Block2", type=parameterizedExpressionsTestLanguage_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression28: BinaryAssociation = BinaryAssociation(
    name="expression28",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression29", type=parameterizedExpressionsTestLanguage_YieldExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_YieldExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exprs30: BinaryAssociation = BinaryAssociation(
    name="exprs30",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression31", type=parameterizedExpressionsTestLanguage_CommaExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_CommaExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs18: BinaryAssociation = BinaryAssociation(
    name="lhs18",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression19", type=parameterizedExpressionsTestLanguage_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_RelationalExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs20: BinaryAssociation = BinaryAssociation(
    name="rhs20",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression22", type=parameterizedExpressionsTestLanguage_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_RelationalExpression21", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs23: BinaryAssociation = BinaryAssociation(
    name="lhs23",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression24", type=parameterizedExpressionsTestLanguage_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_AssignmentExpression", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs25: BinaryAssociation = BinaryAssociation(
    name="rhs25",
    ends={
        Property(name="parameterizedExpressionsTestLanguage_Expression27", type=parameterizedExpressionsTestLanguage_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="parameterizedExpressionsTestLanguage_AssignmentExpression26", type=parameterizedExpressionsTestLanguage_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_parameterizedExpressionsTestLanguage_LabelledStatement_Statement = Generalization(general=Statement, specific=parameterizedExpressionsTestLanguage_LabelledStatement)
gen_parameterizedExpressionsTestLanguage_IdentifierRef_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_IdentifierRef)
gen_parameterizedExpressionsTestLanguage_IndexedAccessExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_IndexedAccessExpression)
gen_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression)
gen_parameterizedExpressionsTestLanguage_ShiftExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_ShiftExpression)
gen_parameterizedExpressionsTestLanguage_FunctionDeclaration_Statement = Generalization(general=Statement, specific=parameterizedExpressionsTestLanguage_FunctionDeclaration)
gen_parameterizedExpressionsTestLanguage_Block_Statement = Generalization(general=Statement, specific=parameterizedExpressionsTestLanguage_Block)
gen_parameterizedExpressionsTestLanguage_ExpressionStatement_Statement = Generalization(general=Statement, specific=parameterizedExpressionsTestLanguage_ExpressionStatement)
gen_parameterizedExpressionsTestLanguage_CommaExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_CommaExpression)
gen_parameterizedExpressionsTestLanguage_RelationalExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_RelationalExpression)
gen_parameterizedExpressionsTestLanguage_AssignmentExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_AssignmentExpression)
gen_parameterizedExpressionsTestLanguage_YieldExpression_Expression = Generalization(general=Expression, specific=parameterizedExpressionsTestLanguage_YieldExpression)

# Domain Model
domain_model = DomainModel(
    name="parameterizedExpressionsTestLanguage",
    types={parameterizedExpressionsTestLanguage_LabelledStatement, parameterizedExpressionsTestLanguage_IdentifierRef, Expression, parameterizedExpressionsTestLanguage_IndexedAccessExpression, parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression, parameterizedExpressionsTestLanguage_ShiftExpression, parameterizedExpressionsTestLanguage_Statement, parameterizedExpressionsTestLanguage_FunctionDeclaration, Statement, parameterizedExpressionsTestLanguage_Block, parameterizedExpressionsTestLanguage_ExpressionStatement, parameterizedExpressionsTestLanguage_Expression, parameterizedExpressionsTestLanguage_CommaExpression, parameterizedExpressionsTestLanguage_RelationalExpression, parameterizedExpressionsTestLanguage_AssignmentExpression, parameterizedExpressionsTestLanguage_YieldExpression},
    associations={expression3, statement4, target6, index8, target11, lhs13, rhs15, body0, statements1, expression28, exprs30, lhs18, rhs20, lhs23, rhs25},
    generalizations={gen_parameterizedExpressionsTestLanguage_LabelledStatement_Statement, gen_parameterizedExpressionsTestLanguage_IdentifierRef_Expression, gen_parameterizedExpressionsTestLanguage_IndexedAccessExpression_Expression, gen_parameterizedExpressionsTestLanguage_ParameterizedPropertyAccessExpression_Expression, gen_parameterizedExpressionsTestLanguage_ShiftExpression_Expression, gen_parameterizedExpressionsTestLanguage_FunctionDeclaration_Statement, gen_parameterizedExpressionsTestLanguage_Block_Statement, gen_parameterizedExpressionsTestLanguage_ExpressionStatement_Statement, gen_parameterizedExpressionsTestLanguage_CommaExpression_Expression, gen_parameterizedExpressionsTestLanguage_RelationalExpression_Expression, gen_parameterizedExpressionsTestLanguage_AssignmentExpression_Expression, gen_parameterizedExpressionsTestLanguage_YieldExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)