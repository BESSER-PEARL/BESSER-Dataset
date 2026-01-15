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
orgreliablesourcecuttlefishcoremodel_IEntityFactory = Class(name="orgreliablesourcecuttlefishcoremodel::IEntityFactory", is_abstract=True)
orgreliablesourcecuttlefishcoremodel_IEntity = Class(name="orgreliablesourcecuttlefishcoremodel::IEntity", is_abstract=True)
orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity = Class(name="orgreliablesourcecuttlefishcoremodel::internal::CuttleFishEntity", is_abstract=True)

# orgreliablesourcecuttlefishcoremodel_IEntityFactory class attributes and methods

# orgreliablesourcecuttlefishcoremodel_IEntity class attributes and methods

# orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="orgreliablesourcecuttlefishcoremodel",
    types={orgreliablesourcecuttlefishcoremodel_IEntityFactory, orgreliablesourcecuttlefishcoremodel_IEntity, orgreliablesourcecuttlefishcoremodel_internal_CuttleFishEntity},
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