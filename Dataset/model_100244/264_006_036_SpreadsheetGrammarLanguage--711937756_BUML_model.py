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
Element = Class(name="Element")
spreadsheetGrammarLanguage_Column = Class(name="spreadsheetGrammarLanguage_Column")
spreadsheetGrammarLanguage_Grammar = Class(name="spreadsheetGrammarLanguage_Grammar")
spreadsheetGrammarLanguage_Block = Class(name="spreadsheetGrammarLanguage_Block")
spreadsheetGrammarLanguage_Element = Class(name="spreadsheetGrammarLanguage_Element")
spreadsheetGrammarLanguage_Rule = Class(name="spreadsheetGrammarLanguage_Rule")
spreadsheetGrammarLanguage_ColumnDefinition = Class(name="spreadsheetGrammarLanguage_ColumnDefinition")
spreadsheetGrammarLanguage_ColumnSpec = Class(name="spreadsheetGrammarLanguage_ColumnSpec")
spreadsheetGrammarLanguage_MandatoryColumn = Class(name="spreadsheetGrammarLanguage_MandatoryColumn")
ColumnDefinition = Class(name="ColumnDefinition")
spreadsheetGrammarLanguage_OptionalColumn = Class(name="spreadsheetGrammarLanguage_OptionalColumn")
spreadsheetGrammarLanguage_RowSpec = Class(name="spreadsheetGrammarLanguage_RowSpec")
ColumnSpec = Class(name="ColumnSpec")
spreadsheetGrammarLanguage_Syntax = Class(name="spreadsheetGrammarLanguage_Syntax")
spreadsheetGrammarLanguage_BlockSpec = Class(name="spreadsheetGrammarLanguage_BlockSpec")
spreadsheetGrammarLanguage_SyntaxSeq = Class(name="spreadsheetGrammarLanguage_SyntaxSeq")

# Element class attributes and methods

# spreadsheetGrammarLanguage_Column class attributes and methods
spreadsheetGrammarLanguage_Column_name: Property = Property(name="name", type=StringType)
spreadsheetGrammarLanguage_Column_multiple: Property = Property(name="multiple", type=BooleanType)
spreadsheetGrammarLanguage_Column.attributes={spreadsheetGrammarLanguage_Column_multiple, spreadsheetGrammarLanguage_Column_name}

# spreadsheetGrammarLanguage_Grammar class attributes and methods
spreadsheetGrammarLanguage_Grammar_name: Property = Property(name="name", type=StringType)
spreadsheetGrammarLanguage_Grammar.attributes={spreadsheetGrammarLanguage_Grammar_name}

# spreadsheetGrammarLanguage_Block class attributes and methods

# spreadsheetGrammarLanguage_Element class attributes and methods
spreadsheetGrammarLanguage_Element_name: Property = Property(name="name", type=StringType)
spreadsheetGrammarLanguage_Element.attributes={spreadsheetGrammarLanguage_Element_name}

# spreadsheetGrammarLanguage_Rule class attributes and methods

# spreadsheetGrammarLanguage_ColumnDefinition class attributes and methods

# spreadsheetGrammarLanguage_ColumnSpec class attributes and methods

# spreadsheetGrammarLanguage_MandatoryColumn class attributes and methods

# ColumnDefinition class attributes and methods

# spreadsheetGrammarLanguage_OptionalColumn class attributes and methods

# spreadsheetGrammarLanguage_RowSpec class attributes and methods
spreadsheetGrammarLanguage_RowSpec_header: Property = Property(name="header", type=StringType)
spreadsheetGrammarLanguage_RowSpec.attributes={spreadsheetGrammarLanguage_RowSpec_header}

# ColumnSpec class attributes and methods

# spreadsheetGrammarLanguage_Syntax class attributes and methods
spreadsheetGrammarLanguage_Syntax_is_id: Property = Property(name="is_id", type=BooleanType)
spreadsheetGrammarLanguage_Syntax_is_string: Property = Property(name="is_string", type=BooleanType)
spreadsheetGrammarLanguage_Syntax_is_int: Property = Property(name="is_int", type=BooleanType)
spreadsheetGrammarLanguage_Syntax_token: Property = Property(name="token", type=StringType)
spreadsheetGrammarLanguage_Syntax.attributes={spreadsheetGrammarLanguage_Syntax_is_id, spreadsheetGrammarLanguage_Syntax_is_int, spreadsheetGrammarLanguage_Syntax_token, spreadsheetGrammarLanguage_Syntax_is_string}

# spreadsheetGrammarLanguage_BlockSpec class attributes and methods

# spreadsheetGrammarLanguage_SyntaxSeq class attributes and methods

# Relationships
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="spreadsheetGrammarLanguage_Column", type=spreadsheetGrammarLanguage_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Block4", type=spreadsheetGrammarLanguage_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="spreadsheetGrammarLanguage_Block", type=spreadsheetGrammarLanguage_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Grammar", type=spreadsheetGrammarLanguage_Block, multiplicity=Multiplicity(0, 1))
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="spreadsheetGrammarLanguage_Element", type=spreadsheetGrammarLanguage_Grammar, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Grammar2", type=spreadsheetGrammarLanguage_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
kind10: BinaryAssociation = BinaryAssociation(
    name="kind10",
    ends={
        Property(name="spreadsheetGrammarLanguage_Block11", type=spreadsheetGrammarLanguage_BlockSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_BlockSpec", type=spreadsheetGrammarLanguage_Block, multiplicity=Multiplicity(0, 1))
    }
)
rule12: BinaryAssociation = BinaryAssociation(
    name="rule12",
    ends={
        Property(name="spreadsheetGrammarLanguage_Rule", type=spreadsheetGrammarLanguage_Syntax, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Syntax13", type=spreadsheetGrammarLanguage_Rule, multiplicity=Multiplicity(0, 1))
    }
)
def_5: BinaryAssociation = BinaryAssociation(
    name="def_5",
    ends={
        Property(name="spreadsheetGrammarLanguage_ColumnDefinition", type=spreadsheetGrammarLanguage_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Column6", type=spreadsheetGrammarLanguage_ColumnDefinition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
spec7: BinaryAssociation = BinaryAssociation(
    name="spec7",
    ends={
        Property(name="spreadsheetGrammarLanguage_ColumnSpec", type=spreadsheetGrammarLanguage_ColumnDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_ColumnDefinition8", type=spreadsheetGrammarLanguage_ColumnSpec, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
syntax9: BinaryAssociation = BinaryAssociation(
    name="syntax9",
    ends={
        Property(name="spreadsheetGrammarLanguage_Syntax", type=spreadsheetGrammarLanguage_RowSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_RowSpec", type=spreadsheetGrammarLanguage_Syntax, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternatives14: BinaryAssociation = BinaryAssociation(
    name="alternatives14",
    ends={
        Property(name="spreadsheetGrammarLanguage_SyntaxSeq", type=spreadsheetGrammarLanguage_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_Rule15", type=spreadsheetGrammarLanguage_SyntaxSeq, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parts16: BinaryAssociation = BinaryAssociation(
    name="parts16",
    ends={
        Property(name="spreadsheetGrammarLanguage_Syntax18", type=spreadsheetGrammarLanguage_SyntaxSeq, multiplicity=Multiplicity(1, 1)),
        Property(name="spreadsheetGrammarLanguage_SyntaxSeq17", type=spreadsheetGrammarLanguage_Syntax, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_spreadsheetGrammarLanguage_Block_Element = Generalization(general=Element, specific=spreadsheetGrammarLanguage_Block)
gen_spreadsheetGrammarLanguage_MandatoryColumn_ColumnDefinition = Generalization(general=ColumnDefinition, specific=spreadsheetGrammarLanguage_MandatoryColumn)
gen_spreadsheetGrammarLanguage_OptionalColumn_ColumnDefinition = Generalization(general=ColumnDefinition, specific=spreadsheetGrammarLanguage_OptionalColumn)
gen_spreadsheetGrammarLanguage_RowSpec_ColumnSpec = Generalization(general=ColumnSpec, specific=spreadsheetGrammarLanguage_RowSpec)
gen_spreadsheetGrammarLanguage_BlockSpec_ColumnSpec = Generalization(general=ColumnSpec, specific=spreadsheetGrammarLanguage_BlockSpec)
gen_spreadsheetGrammarLanguage_Rule_Element = Generalization(general=Element, specific=spreadsheetGrammarLanguage_Rule)

# Domain Model
domain_model = DomainModel(
    name="spreadsheetGrammarLanguage",
    types={Element, spreadsheetGrammarLanguage_Column, spreadsheetGrammarLanguage_Grammar, spreadsheetGrammarLanguage_Block, spreadsheetGrammarLanguage_Element, spreadsheetGrammarLanguage_Rule, spreadsheetGrammarLanguage_ColumnDefinition, spreadsheetGrammarLanguage_ColumnSpec, spreadsheetGrammarLanguage_MandatoryColumn, ColumnDefinition, spreadsheetGrammarLanguage_OptionalColumn, spreadsheetGrammarLanguage_RowSpec, ColumnSpec, spreadsheetGrammarLanguage_Syntax, spreadsheetGrammarLanguage_BlockSpec, spreadsheetGrammarLanguage_SyntaxSeq},
    associations={columns3, root0, elements1, kind10, rule12, def_5, spec7, syntax9, alternatives14, parts16},
    generalizations={gen_spreadsheetGrammarLanguage_Block_Element, gen_spreadsheetGrammarLanguage_MandatoryColumn_ColumnDefinition, gen_spreadsheetGrammarLanguage_OptionalColumn_ColumnDefinition, gen_spreadsheetGrammarLanguage_RowSpec_ColumnSpec, gen_spreadsheetGrammarLanguage_BlockSpec_ColumnSpec, gen_spreadsheetGrammarLanguage_Rule_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)