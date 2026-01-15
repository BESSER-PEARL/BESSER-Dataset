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
codemodel_CMElement = Class(name="codemodel::CMElement", is_abstract=True)
codemodel_E = Class(name="codemodel::E")
codemodel_expressions_Expression = Class(name="codemodel::expressions::Expression", is_abstract=True)
codemodel_expressions_VarExp = Class(name="codemodel::expressions::VarExp")
Expression = Class(name="Expression")
expressions_codemodel_Variable = Class(name="expressions::codemodel::Variable")
codemodel_expressions_BinExp = Class(name="codemodel::expressions::BinExp")
codemodel_CodeModel = Class(name="codemodel::CodeModel")
CMElement = Class(name="CMElement")
codemodel_Variable = Class(name="codemodel::Variable")
Statement = Class(name="Statement")
codemodel_D = Class(name="codemodel::D")
codemodel_statements_CompStmt = Class(name="codemodel::statements::CompStmt")
codemodel_statements_Statement = Class(name="codemodel::statements::Statement", is_abstract=True)
codemodel_statements_AsgnStmt = Class(name="codemodel::statements::AsgnStmt")

# codemodel_CMElement class attributes and methods
codemodel_CMElement_name: Property = Property(name="name", type=StringType)
codemodel_CMElement.attributes={codemodel_CMElement_name}

# codemodel_E class attributes and methods

# codemodel_expressions_Expression class attributes and methods

# codemodel_expressions_VarExp class attributes and methods

# Expression class attributes and methods

# expressions_codemodel_Variable class attributes and methods

# codemodel_expressions_BinExp class attributes and methods
codemodel_expressions_BinExp_operator: Property = Property(name="operator", type=StringType)
codemodel_expressions_BinExp.attributes={codemodel_expressions_BinExp_operator}

# codemodel_CodeModel class attributes and methods

# CMElement class attributes and methods

# codemodel_Variable class attributes and methods

# Statement class attributes and methods

# codemodel_D class attributes and methods

# codemodel_statements_CompStmt class attributes and methods

# codemodel_statements_Statement class attributes and methods

# codemodel_statements_AsgnStmt class attributes and methods

# Relationships
refE3: BinaryAssociation = BinaryAssociation(
    name="refE3",
    ends={
        Property(name="codemodel_E", type=codemodel_D, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_D", type=codemodel_E, multiplicity=Multiplicity(0, 9999))
    }
)
variable4: BinaryAssociation = BinaryAssociation(
    name="variable4",
    ends={
        Property(name="expressions_codemodel_Variable", type=codemodel_expressions_VarExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_VarExp", type=expressions_codemodel_Variable, multiplicity=Multiplicity(1, 1))
    }
)
left5: BinaryAssociation = BinaryAssociation(
    name="left5",
    ends={
        Property(name="Expression", type=codemodel_expressions_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_BinExp", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right6: BinaryAssociation = BinaryAssociation(
    name="right6",
    ends={
        Property(name="Expression8", type=codemodel_expressions_BinExp, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_expressions_BinExp7", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vars0: BinaryAssociation = BinaryAssociation(
    name="vars0",
    ends={
        Property(name="codemodel_Variable", type=codemodel_CodeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_CodeModel", type=codemodel_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stmts1: BinaryAssociation = BinaryAssociation(
    name="stmts1",
    ends={
        Property(name="Statement", type=codemodel_CodeModel, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_CodeModel2", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements14: BinaryAssociation = BinaryAssociation(
    name="statements14",
    ends={
        Property(name="Statement15", type=codemodel_statements_CompStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_CompStmt", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leftExp9: BinaryAssociation = BinaryAssociation(
    name="leftExp9",
    ends={
        Property(name="Expression10", type=codemodel_statements_AsgnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_AsgnStmt", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp11: BinaryAssociation = BinaryAssociation(
    name="rightExp11",
    ends={
        Property(name="Expression13", type=codemodel_statements_AsgnStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="codemodel_statements_AsgnStmt12", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_codemodel_E_CMElement = Generalization(general=CMElement, specific=codemodel_E)
gen_codemodel_expressions_Expression_CMElement = Generalization(general=CMElement, specific=codemodel_expressions_Expression)
gen_codemodel_expressions_VarExp_Expression = Generalization(general=Expression, specific=codemodel_expressions_VarExp)
gen_codemodel_expressions_BinExp_Expression = Generalization(general=Expression, specific=codemodel_expressions_BinExp)
gen_codemodel_CodeModel_CMElement = Generalization(general=CMElement, specific=codemodel_CodeModel)
gen_codemodel_Variable_CMElement = Generalization(general=CMElement, specific=codemodel_Variable)
gen_codemodel_D_CMElement = Generalization(general=CMElement, specific=codemodel_D)
gen_codemodel_statements_CompStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_CompStmt)
gen_codemodel_statements_Statement_CMElement = Generalization(general=CMElement, specific=codemodel_statements_Statement)
gen_codemodel_statements_AsgnStmt_Statement = Generalization(general=Statement, specific=codemodel_statements_AsgnStmt)

# Domain Model
domain_model = DomainModel(
    name="codemodel",
    types={codemodel_CMElement, codemodel_E, codemodel_expressions_Expression, codemodel_expressions_VarExp, Expression, expressions_codemodel_Variable, codemodel_expressions_BinExp, codemodel_CodeModel, CMElement, codemodel_Variable, Statement, codemodel_D, codemodel_statements_CompStmt, codemodel_statements_Statement, codemodel_statements_AsgnStmt},
    associations={refE3, variable4, left5, right6, vars0, stmts1, statements14, leftExp9, rightExp11},
    generalizations={gen_codemodel_E_CMElement, gen_codemodel_expressions_Expression_CMElement, gen_codemodel_expressions_VarExp_Expression, gen_codemodel_expressions_BinExp_Expression, gen_codemodel_CodeModel_CMElement, gen_codemodel_Variable_CMElement, gen_codemodel_D_CMElement, gen_codemodel_statements_CompStmt_Statement, gen_codemodel_statements_Statement_CMElement, gen_codemodel_statements_AsgnStmt_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)