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
expressions_Expression = Class(name="expressions_Expression", is_abstract=True)
expressions_BinaryOperator = Class(name="expressions_BinaryOperator", is_abstract=True)
Expression = Class(name="Expression")
expressions_UnaryOperator = Class(name="expressions_UnaryOperator", is_abstract=True)
expressions_Implies = Class(name="expressions_Implies")
BinaryOperator = Class(name="BinaryOperator")
expressions_Or = Class(name="expressions_Or")
expressions_And = Class(name="expressions_And")
expressions_Neg = Class(name="expressions_Neg")
UnaryOperator = Class(name="UnaryOperator")
expressions_Model = Class(name="expressions_Model")
expressions_Feature = Class(name="expressions_Feature")
expressions_All = Class(name="expressions_All")
expressions_Number = Class(name="expressions_Number")
expressions_Any = Class(name="expressions_Any")

# expressions_Expression class attributes and methods

# expressions_BinaryOperator class attributes and methods

# Expression class attributes and methods

# expressions_UnaryOperator class attributes and methods

# expressions_Implies class attributes and methods

# BinaryOperator class attributes and methods

# expressions_Or class attributes and methods

# expressions_And class attributes and methods

# expressions_Neg class attributes and methods

# UnaryOperator class attributes and methods

# expressions_Model class attributes and methods

# expressions_Feature class attributes and methods
expressions_Feature_name: Property = Property(name="name", type=StringType)
expressions_Feature.attributes={expressions_Feature_name}

# expressions_All class attributes and methods

# expressions_Number class attributes and methods

# expressions_Any class attributes and methods

# Relationships
op10: BinaryAssociation = BinaryAssociation(
    name="op10",
    ends={
        Property(name="expressions_Expression", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op21: BinaryAssociation = BinaryAssociation(
    name="op21",
    ends={
        Property(name="expressions_Expression3", type=expressions_BinaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_BinaryOperator2", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
op4: BinaryAssociation = BinaryAssociation(
    name="op4",
    ends={
        Property(name="expressions_Expression5", type=expressions_UnaryOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_UnaryOperator", type=expressions_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="expressions_Expression7", type=expressions_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Model", type=expressions_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_expressions_BinaryOperator_Expression = Generalization(general=Expression, specific=expressions_BinaryOperator)
gen_expressions_UnaryOperator_Expression = Generalization(general=Expression, specific=expressions_UnaryOperator)
gen_expressions_Implies_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Implies)
gen_expressions_Or_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_Or)
gen_expressions_And_BinaryOperator = Generalization(general=BinaryOperator, specific=expressions_And)
gen_expressions_Neg_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_Neg)
gen_expressions_Feature_Expression = Generalization(general=Expression, specific=expressions_Feature)
gen_expressions_All_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_All)
gen_expressions_Number_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_Number)
gen_expressions_Any_UnaryOperator = Generalization(general=UnaryOperator, specific=expressions_Any)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_Expression, expressions_BinaryOperator, Expression, expressions_UnaryOperator, expressions_Implies, BinaryOperator, expressions_Or, expressions_And, expressions_Neg, UnaryOperator, expressions_Model, expressions_Feature, expressions_All, expressions_Number, expressions_Any},
    associations={op10, op21, op4, constraints6},
    generalizations={gen_expressions_BinaryOperator_Expression, gen_expressions_UnaryOperator_Expression, gen_expressions_Implies_BinaryOperator, gen_expressions_Or_BinaryOperator, gen_expressions_And_BinaryOperator, gen_expressions_Neg_UnaryOperator, gen_expressions_Feature_Expression, gen_expressions_All_UnaryOperator, gen_expressions_Number_UnaryOperator, gen_expressions_Any_UnaryOperator},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)