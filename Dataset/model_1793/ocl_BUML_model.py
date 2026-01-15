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
library_OclExpression = Class(name="library::OclExpression")
library_OclLibrary = Class(name="library::OclLibrary")

# library_OclExpression class attributes and methods
library_OclExpression_name: Property = Property(name="name", type=StringType)
library_OclExpression_description: Property = Property(name="description", type=StringType)
library_OclExpression_query: Property = Property(name="query", type=StringType)
library_OclExpression_context: Property = Property(name="context", type=StringType)
library_OclExpression.attributes={library_OclExpression_description, library_OclExpression_name, library_OclExpression_query, library_OclExpression_context}

# library_OclLibrary class attributes and methods
library_OclLibrary_name: Property = Property(name="name", type=StringType)
library_OclLibrary.attributes={library_OclLibrary_name}

# Relationships
oclExpressions0: BinaryAssociation = BinaryAssociation(
    name="oclExpressions0",
    ends={
        Property(name="library_OclExpression", type=library_OclLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="library_OclLibrary", type=library_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_OclExpression, library_OclLibrary},
    associations={oclExpressions0},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)