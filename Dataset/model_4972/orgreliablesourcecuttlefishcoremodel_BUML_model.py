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
orgreliablesourcecuttlefishcoremodel_IEntity = Class(name="orgreliablesourcecuttlefishcoremodel_IEntity", is_abstract=True)
orgreliablesourcecuttlefishcoremodel_IEntityFactory = Class(name="orgreliablesourcecuttlefishcoremodel_IEntityFactory", is_abstract=True)
orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity = Class(name="orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity", is_abstract=True)

# orgreliablesourcecuttlefishcoremodel_IEntity class attributes and methods

# orgreliablesourcecuttlefishcoremodel_IEntityFactory class attributes and methods

# orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="orgreliablesourcecuttlefishcoremodel",
    types={orgreliablesourcecuttlefishcoremodel_IEntity, orgreliablesourcecuttlefishcoremodel_IEntityFactory, orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity},
    associations={},
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