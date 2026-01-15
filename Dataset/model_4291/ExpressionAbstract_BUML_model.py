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
expression_IncludingExpression = Class(name="expression::IncludingExpression")
SubExpression = Class(name="SubExpression")
expression_Expression = Class(name="expression::Expression", is_abstract=True)
expression_BooleanExpression = Class(name="expression::BooleanExpression")
expression_NegativeIntExpression = Class(name="expression::NegativeIntExpression")
expression_SubExpression = Class(name="expression::SubExpression", is_abstract=True)
Expression = Class(name="Expression")
expression_SubExpression2 = Class(name="expression::SubExpression2")
expression_ExpressionList = Class(name="expression::ExpressionList")
expression_StringExpression = Class(name="expression::StringExpression")
SubExpression2 = Class(name="SubExpression2")

# expression_IncludingExpression class attributes and methods

# SubExpression class attributes and methods

# expression_Expression class attributes and methods

# expression_BooleanExpression class attributes and methods
expression_BooleanExpression_value: Property = Property(name="value", type=StringType)
expression_BooleanExpression.attributes={expression_BooleanExpression_value}

# expression_NegativeIntExpression class attributes and methods
expression_NegativeIntExpression_value: Property = Property(name="value", type=StringType)
expression_NegativeIntExpression_isNegative: Property = Property(name="isNegative", type=StringType)
expression_NegativeIntExpression.attributes={expression_NegativeIntExpression_isNegative, expression_NegativeIntExpression_value}

# expression_SubExpression class attributes and methods

# Expression class attributes and methods

# expression_SubExpression2 class attributes and methods

# expression_ExpressionList class attributes and methods

# expression_StringExpression class attributes and methods
expression_StringExpression_value: Property = Property(name="value", type=StringType)
expression_StringExpression.attributes={expression_StringExpression_value}

# SubExpression2 class attributes and methods

# Relationships
argument0: BinaryAssociation = BinaryAssociation(
    name="argument0",
    ends={
        Property(name="expression_Expression", type=expression_IncludingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_IncludingExpression", type=expression_Expression, multiplicity=Multiplicity(1, 1))
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="expression_Expression3", type=expression_IncludingExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_IncludingExpression2", type=expression_Expression, multiplicity=Multiplicity(1, 1))
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="expression_Expression5", type=expression_ExpressionList, multiplicity=Multiplicity(1, 1)),
        Property(name="expression_ExpressionList", type=expression_Expression, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_expression_IncludingExpression_SubExpression = Generalization(general=SubExpression, specific=expression_IncludingExpression)
gen_expression_BooleanExpression_SubExpression = Generalization(general=SubExpression, specific=expression_BooleanExpression)
gen_expression_NegativeIntExpression_SubExpression2 = Generalization(general=SubExpression2, specific=expression_NegativeIntExpression)
gen_expression_SubExpression_Expression = Generalization(general=Expression, specific=expression_SubExpression)
gen_expression_SubExpression2_Expression = Generalization(general=Expression, specific=expression_SubExpression2)
gen_expression_StringExpression_SubExpression2 = Generalization(general=SubExpression2, specific=expression_StringExpression)

# Domain Model
domain_model = DomainModel(
    name="expression",
    types={expression_IncludingExpression, SubExpression, expression_Expression, expression_BooleanExpression, expression_NegativeIntExpression, expression_SubExpression, Expression, expression_SubExpression2, expression_ExpressionList, expression_StringExpression, SubExpression2},
    associations={argument0, source1, elements4},
    generalizations={gen_expression_IncludingExpression_SubExpression, gen_expression_BooleanExpression_SubExpression, gen_expression_NegativeIntExpression_SubExpression2, gen_expression_SubExpression_Expression, gen_expression_SubExpression2_Expression, gen_expression_StringExpression_SubExpression2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)