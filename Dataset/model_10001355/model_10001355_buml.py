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
venda = Class(name="venda")
VendaAVista = Class(name="VendaAVista")
VendaParcelada = Class(name="VendaParcelada")

# venda class attributes and methods

# VendaAVista class attributes and methods

# VendaParcelada class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_1v4s0MHqEei9yqzfX9cFYA",
    types={venda, VendaAVista, VendaParcelada},
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