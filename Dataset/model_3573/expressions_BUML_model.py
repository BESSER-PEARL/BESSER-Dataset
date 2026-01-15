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

# Enumerations
AddType: Enumeration = Enumeration(
    name="AddType",
    literals={
            EnumerationLiteral(name="ADDITION"),
			EnumerationLiteral(name="SUBTRACTION")
    }
)

ShiftType: Enumeration = Enumeration(
    name="ShiftType",
    literals={
            EnumerationLiteral(name="LEFT"),
			EnumerationLiteral(name="RIGHT")
    }
)

UnaryType: Enumeration = Enumeration(
    name="UnaryType",
    literals={
            EnumerationLiteral(name="NEGATIVE"),
			EnumerationLiteral(name="POSITIVE"),
			EnumerationLiteral(name="TILDE")
    }
)

MultiType: Enumeration = Enumeration(
    name="MultiType",
    literals={
            EnumerationLiteral(name="MULTIPLICATION"),
			EnumerationLiteral(name="DIVISION"),
			EnumerationLiteral(name="MODULATION")
    }
)

# Classes
expressions_Expression = Class(name="expressions::Expression", is_abstract=True)
FileRegion = Class(name="FileRegion")
expressions_ConstExpression = Class(name="expressions::ConstExpression")
Expression = Class(name="Expression")
expressions_AndExpression = Class(name="expressions::AndExpression")
expressions_ShiftExpression = Class(name="expressions::ShiftExpression")
expressions_OrExpression = Class(name="expressions::OrExpression")
expressions_XOrExpression = Class(name="expressions::XOrExpression")
expressions_MultExpression = Class(name="expressions::MultExpression")
expressions_AddExpression = Class(name="expressions::AddExpression")
expressions_ScopeLiteral = Class(name="expressions::ScopeLiteral")
expressions_IdlTypeDcl = Class(name="expressions::IdlTypeDcl")
expressions_UnaryExpression = Class(name="expressions::UnaryExpression")
expressions_BooleanLiteral = Class(name="expressions::BooleanLiteral")
expressions_FixedPtLiteral = Class(name="expressions::FixedPtLiteral")
expressions_WideStringLiteral = Class(name="expressions::WideStringLiteral")
expressions_IntegerLiteral = Class(name="expressions::IntegerLiteral")
expressions_StringLiteral = Class(name="expressions::StringLiteral")
expressions_CharacterLiteral = Class(name="expressions::CharacterLiteral")
expressions_FloatingPointLiteral = Class(name="expressions::FloatingPointLiteral")
expressions_DoubleLiteral = Class(name="expressions::DoubleLiteral")
expressions_WideCharacterLiteral = Class(name="expressions::WideCharacterLiteral")

# expressions_Expression class attributes and methods

# FileRegion class attributes and methods

# expressions_ConstExpression class attributes and methods

# Expression class attributes and methods

# expressions_AndExpression class attributes and methods

# expressions_ShiftExpression class attributes and methods
expressions_ShiftExpression_type: Property = Property(name="type", type=StringType)
expressions_ShiftExpression.attributes={expressions_ShiftExpression_type}

# expressions_OrExpression class attributes and methods

# expressions_XOrExpression class attributes and methods

# expressions_MultExpression class attributes and methods
expressions_MultExpression_type: Property = Property(name="type", type=StringType)
expressions_MultExpression.attributes={expressions_MultExpression_type}

# expressions_AddExpression class attributes and methods
expressions_AddExpression_type: Property = Property(name="type", type=StringType)
expressions_AddExpression.attributes={expressions_AddExpression_type}

# expressions_ScopeLiteral class attributes and methods

# expressions_IdlTypeDcl class attributes and methods

# expressions_UnaryExpression class attributes and methods
expressions_UnaryExpression_type: Property = Property(name="type", type=StringType)
expressions_UnaryExpression.attributes={expressions_UnaryExpression_type}

# expressions_BooleanLiteral class attributes and methods
expressions_BooleanLiteral_value: Property = Property(name="value", type=BooleanType)
expressions_BooleanLiteral.attributes={expressions_BooleanLiteral_value}

# expressions_FixedPtLiteral class attributes and methods
expressions_FixedPtLiteral_integerPart: Property = Property(name="integerPart", type=IntegerType)
expressions_FixedPtLiteral_decimalPart: Property = Property(name="decimalPart", type=IntegerType)
expressions_FixedPtLiteral_value: Property = Property(name="value", type=StringType)
expressions_FixedPtLiteral.attributes={expressions_FixedPtLiteral_value, expressions_FixedPtLiteral_integerPart, expressions_FixedPtLiteral_decimalPart}

# expressions_WideStringLiteral class attributes and methods
expressions_WideStringLiteral_value: Property = Property(name="value", type=StringType)
expressions_WideStringLiteral.attributes={expressions_WideStringLiteral_value}

# expressions_IntegerLiteral class attributes and methods
expressions_IntegerLiteral_value: Property = Property(name="value", type=IntegerType)
expressions_IntegerLiteral.attributes={expressions_IntegerLiteral_value}

# expressions_StringLiteral class attributes and methods
expressions_StringLiteral_value: Property = Property(name="value", type=StringType)
expressions_StringLiteral.attributes={expressions_StringLiteral_value}

# expressions_CharacterLiteral class attributes and methods
expressions_CharacterLiteral_value: Property = Property(name="value", type=StringType)
expressions_CharacterLiteral.attributes={expressions_CharacterLiteral_value}

# expressions_FloatingPointLiteral class attributes and methods
expressions_FloatingPointLiteral_value: Property = Property(name="value", type=FloatType)
expressions_FloatingPointLiteral.attributes={expressions_FloatingPointLiteral_value}

# expressions_DoubleLiteral class attributes and methods
expressions_DoubleLiteral_value: Property = Property(name="value", type=FloatType)
expressions_DoubleLiteral.attributes={expressions_DoubleLiteral_value}

# expressions_WideCharacterLiteral class attributes and methods
expressions_WideCharacterLiteral_value: Property = Property(name="value", type=StringType)
expressions_WideCharacterLiteral.attributes={expressions_WideCharacterLiteral_value}

# Relationships
right8: BinaryAssociation = BinaryAssociation(
    name="right8",
    ends={
        Property(name="expressions_Expression10", type=expressions_XOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_XOrExpression9", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left11: BinaryAssociation = BinaryAssociation(
    name="left11",
    ends={
        Property(name="expressions_Expression12", type=expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AndExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right13: BinaryAssociation = BinaryAssociation(
    name="right13",
    ends={
        Property(name="expressions_Expression15", type=expressions_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AndExpression14", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression0: BinaryAssociation = BinaryAssociation(
    name="expression0",
    ends={
        Property(name="expressions_Expression", type=expressions_ConstExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ConstExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="expressions_Expression2", type=expressions_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_OrExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="expressions_Expression5", type=expressions_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_OrExpression4", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left6: BinaryAssociation = BinaryAssociation(
    name="left6",
    ends={
        Property(name="expressions_Expression7", type=expressions_XOrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_XOrExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="expressions_Expression25", type=expressions_AddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AddExpression24", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="expressions_Expression27", type=expressions_MultExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MultExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left16: BinaryAssociation = BinaryAssociation(
    name="left16",
    ends={
        Property(name="expressions_Expression17", type=expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ShiftExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right18: BinaryAssociation = BinaryAssociation(
    name="right18",
    ends={
        Property(name="expressions_Expression20", type=expressions_ShiftExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ShiftExpression19", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="expressions_Expression22", type=expressions_AddExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_AddExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr31: BinaryAssociation = BinaryAssociation(
    name="expr31",
    ends={
        Property(name="expressions_Expression32", type=expressions_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryExpression", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="expressions_Expression30", type=expressions_MultExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_MultExpression29", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="expressions_IdlTypeDcl", type=expressions_ScopeLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ScopeLiteral", type=expressions_IdlTypeDcl, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_expressions_Expression_FileRegion = Generalization(general=FileRegion, specific=expressions_Expression)
gen_expressions_ConstExpression_Expression = Generalization(general=Expression, specific=expressions_ConstExpression)
gen_expressions_AndExpression_Expression = Generalization(general=Expression, specific=expressions_AndExpression)
gen_expressions_ShiftExpression_Expression = Generalization(general=Expression, specific=expressions_ShiftExpression)
gen_expressions_OrExpression_Expression = Generalization(general=Expression, specific=expressions_OrExpression)
gen_expressions_XOrExpression_Expression = Generalization(general=Expression, specific=expressions_XOrExpression)
gen_expressions_MultExpression_Expression = Generalization(general=Expression, specific=expressions_MultExpression)
gen_expressions_AddExpression_Expression = Generalization(general=Expression, specific=expressions_AddExpression)
gen_expressions_ScopeLiteral_Expression = Generalization(general=Expression, specific=expressions_ScopeLiteral)
gen_expressions_UnaryExpression_Expression = Generalization(general=Expression, specific=expressions_UnaryExpression)
gen_expressions_BooleanLiteral_Expression = Generalization(general=Expression, specific=expressions_BooleanLiteral)
gen_expressions_FixedPtLiteral_Expression = Generalization(general=Expression, specific=expressions_FixedPtLiteral)
gen_expressions_WideStringLiteral_Expression = Generalization(general=Expression, specific=expressions_WideStringLiteral)
gen_expressions_IntegerLiteral_Expression = Generalization(general=Expression, specific=expressions_IntegerLiteral)
gen_expressions_StringLiteral_Expression = Generalization(general=Expression, specific=expressions_StringLiteral)
gen_expressions_CharacterLiteral_Expression = Generalization(general=Expression, specific=expressions_CharacterLiteral)
gen_expressions_FloatingPointLiteral_Expression = Generalization(general=Expression, specific=expressions_FloatingPointLiteral)
gen_expressions_DoubleLiteral_Expression = Generalization(general=Expression, specific=expressions_DoubleLiteral)
gen_expressions_WideCharacterLiteral_Expression = Generalization(general=Expression, specific=expressions_WideCharacterLiteral)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_Expression, FileRegion, expressions_ConstExpression, Expression, expressions_AndExpression, expressions_ShiftExpression, expressions_OrExpression, expressions_XOrExpression, expressions_MultExpression, expressions_AddExpression, expressions_ScopeLiteral, expressions_IdlTypeDcl, expressions_UnaryExpression, expressions_BooleanLiteral, expressions_FixedPtLiteral, expressions_WideStringLiteral, expressions_IntegerLiteral, expressions_StringLiteral, expressions_CharacterLiteral, expressions_FloatingPointLiteral, expressions_DoubleLiteral, expressions_WideCharacterLiteral, AddType, ShiftType, UnaryType, MultiType},
    associations={right8, left11, right13, expression0, left1, right3, left6, right23, left26, left16, right18, left21, expr31, right28, value33},
    generalizations={gen_expressions_Expression_FileRegion, gen_expressions_ConstExpression_Expression, gen_expressions_AndExpression_Expression, gen_expressions_ShiftExpression_Expression, gen_expressions_OrExpression_Expression, gen_expressions_XOrExpression_Expression, gen_expressions_MultExpression_Expression, gen_expressions_AddExpression_Expression, gen_expressions_ScopeLiteral_Expression, gen_expressions_UnaryExpression_Expression, gen_expressions_BooleanLiteral_Expression, gen_expressions_FixedPtLiteral_Expression, gen_expressions_WideStringLiteral_Expression, gen_expressions_IntegerLiteral_Expression, gen_expressions_StringLiteral_Expression, gen_expressions_CharacterLiteral_Expression, gen_expressions_FloatingPointLiteral_Expression, gen_expressions_DoubleLiteral_Expression, gen_expressions_WideCharacterLiteral_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)