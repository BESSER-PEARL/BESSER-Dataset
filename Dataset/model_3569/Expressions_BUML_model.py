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
expressions_AbstractElement = Class(name="expressions::AbstractElement")
expressions_ExpressionsModel = Class(name="expressions::ExpressionsModel")
expressions_Variable = Class(name="expressions::Variable")
AbstractElement = Class(name="AbstractElement")
expressions_Plus = Class(name="expressions::Plus")
Expression = Class(name="Expression")
expressions_Expression = Class(name="expressions::Expression")
expressions_StringConstant = Class(name="expressions::StringConstant")
expressions_IntConstant = Class(name="expressions::IntConstant")
expressions_VariableRef = Class(name="expressions::VariableRef")
expressions_BoolConstant = Class(name="expressions::BoolConstant")

# expressions_AbstractElement class attributes and methods

# expressions_ExpressionsModel class attributes and methods

# expressions_Variable class attributes and methods
expressions_Variable_name: Property = Property(name="name", type=StringType)
expressions_Variable.attributes={expressions_Variable_name}

# AbstractElement class attributes and methods

# expressions_Plus class attributes and methods

# Expression class attributes and methods

# expressions_Expression class attributes and methods

# expressions_StringConstant class attributes and methods
expressions_StringConstant_value: Property = Property(name="value", type=StringType)
expressions_StringConstant.attributes={expressions_StringConstant_value}

# expressions_IntConstant class attributes and methods
expressions_IntConstant_value: Property = Property(name="value", type=IntegerType)
expressions_IntConstant.attributes={expressions_IntConstant_value}

# expressions_VariableRef class attributes and methods

# expressions_BoolConstant class attributes and methods
expressions_BoolConstant_value: Property = Property(name="value", type=StringType)
expressions_BoolConstant.attributes={expressions_BoolConstant_value}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="expressions_AbstractElement", type=expressions_ExpressionsModel, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_ExpressionsModel", type=expressions_AbstractElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="expressions_Expression", type=expressions_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Variable", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right4: BinaryAssociation = BinaryAssociation(
    name="right4",
    ends={
        Property(name="expressions_Expression6", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus5", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left2: BinaryAssociation = BinaryAssociation(
    name="left2",
    ends={
        Property(name="expressions_Expression3", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus", type=expressions_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable7: BinaryAssociation = BinaryAssociation(
    name="variable7",
    ends={
        Property(name="expressions_Variable8", type=expressions_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_VariableRef", type=expressions_Variable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_expressions_Variable_AbstractElement = Generalization(general=AbstractElement, specific=expressions_Variable)
gen_expressions_Plus_Expression = Generalization(general=Expression, specific=expressions_Plus)
gen_expressions_Expression_AbstractElement = Generalization(general=AbstractElement, specific=expressions_Expression)
gen_expressions_StringConstant_Expression = Generalization(general=Expression, specific=expressions_StringConstant)
gen_expressions_IntConstant_Expression = Generalization(general=Expression, specific=expressions_IntConstant)
gen_expressions_VariableRef_Expression = Generalization(general=Expression, specific=expressions_VariableRef)
gen_expressions_BoolConstant_Expression = Generalization(general=Expression, specific=expressions_BoolConstant)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_AbstractElement, expressions_ExpressionsModel, expressions_Variable, AbstractElement, expressions_Plus, Expression, expressions_Expression, expressions_StringConstant, expressions_IntConstant, expressions_VariableRef, expressions_BoolConstant},
    associations={elements0, expression1, right4, left2, variable7},
    generalizations={gen_expressions_Variable_AbstractElement, gen_expressions_Plus_Expression, gen_expressions_Expression_AbstractElement, gen_expressions_StringConstant_Expression, gen_expressions_IntConstant_Expression, gen_expressions_VariableRef_Expression, gen_expressions_BoolConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)