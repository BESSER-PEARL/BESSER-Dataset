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
mpl_Program = Class(name="mpl::Program")
mpl_VariableDeclaration = Class(name="mpl::VariableDeclaration")
mpl_Statement = Class(name="mpl::Statement", is_abstract=True)
mpl_ArithmeticExpression = Class(name="mpl::ArithmeticExpression")
Expression = Class(name="Expression")
mpl_AtomicExpression = Class(name="mpl::AtomicExpression", is_abstract=True)
mpl_Variable = Class(name="mpl::Variable")
mpl_Assignment = Class(name="mpl::Assignment")
Statement = Class(name="Statement")
mpl_Expression = Class(name="mpl::Expression", is_abstract=True)
mpl_VariableRefrence = Class(name="mpl::VariableRefrence")
mpl_ExpressionStatement = Class(name="mpl::ExpressionStatement")
mpl_LiteralValue = Class(name="mpl::LiteralValue")
AtomicExpression = Class(name="AtomicExpression")
mpl_AddExpression = Class(name="mpl::AddExpression")
ArithmeticExpression = Class(name="ArithmeticExpression")

# mpl_Program class attributes and methods
mpl_Program_name: Property = Property(name="name", type=StringType)
mpl_Program.attributes={mpl_Program_name}

# mpl_VariableDeclaration class attributes and methods

# mpl_Statement class attributes and methods

# mpl_ArithmeticExpression class attributes and methods

# Expression class attributes and methods

# mpl_AtomicExpression class attributes and methods

# mpl_Variable class attributes and methods
mpl_Variable_name: Property = Property(name="name", type=StringType)
mpl_Variable.attributes={mpl_Variable_name}

# mpl_Assignment class attributes and methods

# Statement class attributes and methods

# mpl_Expression class attributes and methods

# mpl_VariableRefrence class attributes and methods

# mpl_ExpressionStatement class attributes and methods

# mpl_LiteralValue class attributes and methods
mpl_LiteralValue_rawValue: Property = Property(name="rawValue", type=IntegerType)
mpl_LiteralValue.attributes={mpl_LiteralValue_rawValue}

# AtomicExpression class attributes and methods

# mpl_AddExpression class attributes and methods

# ArithmeticExpression class attributes and methods

# Relationships
variabledeclarations0: BinaryAssociation = BinaryAssociation(
    name="variabledeclarations0",
    ends={
        Property(name="mpl_VariableDeclaration", type=mpl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Program", type=mpl_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand210: BinaryAssociation = BinaryAssociation(
    name="operand210",
    ends={
        Property(name="mpl_Expression11", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operand112: BinaryAssociation = BinaryAssociation(
    name="operand112",
    ends={
        Property(name="mpl_Expression14", type=mpl_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ArithmeticExpression13", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement1: BinaryAssociation = BinaryAssociation(
    name="statement1",
    ends={
        Property(name="mpl_Statement", type=mpl_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Program2", type=mpl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="mpl_Variable", type=mpl_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableDeclaration4", type=mpl_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightHandSide5: BinaryAssociation = BinaryAssociation(
    name="rightHandSide5",
    ends={
        Property(name="mpl_Expression", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftHandSide6: BinaryAssociation = BinaryAssociation(
    name="leftHandSide6",
    ends={
        Property(name="mpl_VariableRefrence", type=mpl_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_Assignment7", type=mpl_VariableRefrence, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression8: BinaryAssociation = BinaryAssociation(
    name="expression8",
    ends={
        Property(name="mpl_Expression9", type=mpl_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_ExpressionStatement", type=mpl_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable15: BinaryAssociation = BinaryAssociation(
    name="variable15",
    ends={
        Property(name="mpl_Variable17", type=mpl_VariableRefrence, multiplicity=Multiplicity(1, 1)),
        Property(name="mpl_VariableRefrence16", type=mpl_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mpl_ArithmeticExpression_Expression = Generalization(general=Expression, specific=mpl_ArithmeticExpression)
gen_mpl_AtomicExpression_Expression = Generalization(general=Expression, specific=mpl_AtomicExpression)
gen_mpl_Assignment_Statement = Generalization(general=Statement, specific=mpl_Assignment)
gen_mpl_ExpressionStatement_Statement = Generalization(general=Statement, specific=mpl_ExpressionStatement)
gen_mpl_LiteralValue_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_LiteralValue)
gen_mpl_VariableRefrence_AtomicExpression = Generalization(general=AtomicExpression, specific=mpl_VariableRefrence)
gen_mpl_AddExpression_ArithmeticExpression = Generalization(general=ArithmeticExpression, specific=mpl_AddExpression)

# Domain Model
domain_model = DomainModel(
    name="mpl",
    types={mpl_Program, mpl_VariableDeclaration, mpl_Statement, mpl_ArithmeticExpression, Expression, mpl_AtomicExpression, mpl_Variable, mpl_Assignment, Statement, mpl_Expression, mpl_VariableRefrence, mpl_ExpressionStatement, mpl_LiteralValue, AtomicExpression, mpl_AddExpression, ArithmeticExpression},
    associations={variabledeclarations0, operand210, operand112, statement1, variable3, rightHandSide5, leftHandSide6, expression8, variable15},
    generalizations={gen_mpl_ArithmeticExpression_Expression, gen_mpl_AtomicExpression_Expression, gen_mpl_Assignment_Statement, gen_mpl_ExpressionStatement_Statement, gen_mpl_LiteralValue_AtomicExpression, gen_mpl_VariableRefrence_AtomicExpression, gen_mpl_AddExpression_ArithmeticExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)