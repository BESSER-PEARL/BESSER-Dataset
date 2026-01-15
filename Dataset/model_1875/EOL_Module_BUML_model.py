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
eol_module_EOLLibraryModule = Class(name="eol::module::EOLLibraryModule")
eol_module_ModelDeclarationStatement = Class(name="eol::module::ModelDeclarationStatement")
eol_module_OperationDefinition = Class(name="eol::module::OperationDefinition")
eol_module_EOLModule = Class(name="eol::module::EOLModule")
EOLLibraryModule = Class(name="EOLLibraryModule")
eol_module_Block = Class(name="eol::module::Block")
eol_module_Statement = Class(name="eol::module::Statement", is_abstract=True)
eol_module_AnnotationBlock = Class(name="eol::module::AnnotationBlock")
Block = Class(name="Block")
eol_module_Import = Class(name="eol::module::Import")
eol_module_Expression = Class(name="eol::module::Expression", is_abstract=True)
eol_module_Type = Class(name="eol::module::Type")
eol_module_NameExpression = Class(name="eol::module::NameExpression")
eol_module_FormalParameterExpression = Class(name="eol::module::FormalParameterExpression")
eol_module_ExpressionOrStatementBlock = Class(name="eol::module::ExpressionOrStatementBlock")
Expression = Class(name="Expression")

# eol_module_EOLLibraryModule class attributes and methods
eol_module_EOLLibraryModule_name: Property = Property(name="name", type=StringType)
eol_module_EOLLibraryModule.attributes={eol_module_EOLLibraryModule_name}

# eol_module_ModelDeclarationStatement class attributes and methods

# eol_module_OperationDefinition class attributes and methods

# eol_module_EOLModule class attributes and methods

# EOLLibraryModule class attributes and methods

# eol_module_Block class attributes and methods

# eol_module_Statement class attributes and methods

# eol_module_AnnotationBlock class attributes and methods

# Block class attributes and methods

# eol_module_Import class attributes and methods
eol_module_Import_imported: Property = Property(name="imported", type=StringType)
eol_module_Import.attributes={eol_module_Import_imported}

# eol_module_Expression class attributes and methods

# eol_module_Type class attributes and methods

# eol_module_NameExpression class attributes and methods
eol_module_NameExpression_name: Property = Property(name="name", type=StringType)
eol_module_NameExpression_isType: Property = Property(name="isType", type=BooleanType)
eol_module_NameExpression.attributes={eol_module_NameExpression_isType, eol_module_NameExpression_name}

# eol_module_FormalParameterExpression class attributes and methods

# eol_module_ExpressionOrStatementBlock class attributes and methods

# Expression class attributes and methods

# Relationships
modelDeclarations1: BinaryAssociation = BinaryAssociation(
    name="modelDeclarations1",
    ends={
        Property(name="eol_module_ModelDeclarationStatement", type=eol_module_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_EOLLibraryModule2", type=eol_module_ModelDeclarationStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations3: BinaryAssociation = BinaryAssociation(
    name="operations3",
    ends={
        Property(name="eol_module_OperationDefinition", type=eol_module_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_EOLLibraryModule4", type=eol_module_OperationDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block5: BinaryAssociation = BinaryAssociation(
    name="block5",
    ends={
        Property(name="eol_module_Block", type=eol_module_EOLModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_EOLModule", type=eol_module_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importedModule6: BinaryAssociation = BinaryAssociation(
    name="importedModule6",
    ends={
        Property(name="eol_module_EOLLibraryModule8", type=eol_module_Import, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_Import7", type=eol_module_EOLLibraryModule, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements9: BinaryAssociation = BinaryAssociation(
    name="statements9",
    ends={
        Property(name="eol_module_Statement", type=eol_module_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_Block10", type=eol_module_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="eol_module_Import", type=eol_module_EOLLibraryModule, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_EOLLibraryModule", type=eol_module_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block11: BinaryAssociation = BinaryAssociation(
    name="block11",
    ends={
        Property(name="eol_module_ExpressionOrStatementBlock", type=eol_module_Block, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="eol_module_Block12", type=eol_module_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1))
    }
)
expression13: BinaryAssociation = BinaryAssociation(
    name="expression13",
    ends={
        Property(name="eol_module_Expression", type=eol_module_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_ExpressionOrStatementBlock14", type=eol_module_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition15: BinaryAssociation = BinaryAssociation(
    name="condition15",
    ends={
        Property(name="eol_module_Expression17", type=eol_module_ExpressionOrStatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_ExpressionOrStatementBlock16", type=eol_module_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextType18: BinaryAssociation = BinaryAssociation(
    name="contextType18",
    ends={
        Property(name="eol_module_Type", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition19", type=eol_module_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnType20: BinaryAssociation = BinaryAssociation(
    name="returnType20",
    ends={
        Property(name="eol_module_Type22", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition21", type=eol_module_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotationBlock23: BinaryAssociation = BinaryAssociation(
    name="annotationBlock23",
    ends={
        Property(name="eol_module_AnnotationBlock", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition24", type=eol_module_AnnotationBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body25: BinaryAssociation = BinaryAssociation(
    name="body25",
    ends={
        Property(name="eol_module_Block27", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition26", type=eol_module_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name28: BinaryAssociation = BinaryAssociation(
    name="name28",
    ends={
        Property(name="eol_module_NameExpression", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition29", type=eol_module_NameExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="eol_module_FormalParameterExpression", type=eol_module_OperationDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="eol_module_OperationDefinition31", type=eol_module_FormalParameterExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_eol_module_EOLModule_EOLLibraryModule = Generalization(general=EOLLibraryModule, specific=eol_module_EOLModule)
gen_eol_module_AnnotationBlock_Block = Generalization(general=Block, specific=eol_module_AnnotationBlock)
gen_eol_module_NameExpression_Expression = Generalization(general=Expression, specific=eol_module_NameExpression)

# Domain Model
domain_model = DomainModel(
    name="eol_module",
    types={eol_module_EOLLibraryModule, eol_module_ModelDeclarationStatement, eol_module_OperationDefinition, eol_module_EOLModule, EOLLibraryModule, eol_module_Block, eol_module_Statement, eol_module_AnnotationBlock, Block, eol_module_Import, eol_module_Expression, eol_module_Type, eol_module_NameExpression, eol_module_FormalParameterExpression, eol_module_ExpressionOrStatementBlock, Expression},
    associations={modelDeclarations1, operations3, block5, importedModule6, statements9, imports0, block11, expression13, condition15, contextType18, returnType20, annotationBlock23, body25, name28, parameters30},
    generalizations={gen_eol_module_EOLModule_EOLLibraryModule, gen_eol_module_AnnotationBlock_Block, gen_eol_module_NameExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)