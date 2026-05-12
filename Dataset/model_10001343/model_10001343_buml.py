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
Pessoa = Class(name="Pessoa")
Funcionario = Class(name="Funcionario")
Actor_Actor = Class(name="Actor_Actor")
Component_Component = Class(name="Component_Component")
Actor2_Actor = Class(name="Actor2_Actor")
Actor3_Actor = Class(name="Actor3_Actor")
Actor4_Actor = Class(name="Actor4_Actor")
Component2_Component = Class(name="Component2_Component")
Component3_Component = Class(name="Component3_Component")
Actor5_Actor = Class(name="Actor5_Actor")
Actor6_Actor = Class(name="Actor6_Actor")
Actor7_Actor = Class(name="Actor7_Actor")

# Pessoa class attributes and methods
Pessoa_id: Property = Property(name="id", type=IntegerType)
Pessoa_Nome: Property = Property(name="Nome", type=StringType)
Pessoa_idade: Property = Property(name="idade", type=IntegerType)
Pessoa.attributes={Pessoa_Nome, Pessoa_id, Pessoa_idade}

# Funcionario class attributes and methods
Funcionario_cracha: Property = Property(name="cracha", type=IntegerType)
Funcionario.attributes={Funcionario_cracha}

# Actor_Actor class attributes and methods

# Component_Component class attributes and methods

# Actor2_Actor class attributes and methods

# Actor3_Actor class attributes and methods

# Actor4_Actor class attributes and methods

# Component2_Component class attributes and methods

# Component3_Component class attributes and methods

# Actor5_Actor class attributes and methods

# Actor6_Actor class attributes and methods

# Actor7_Actor class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_10zNQAm3EeihOuC11hdjgA",
    types={Pessoa, Funcionario, Actor_Actor, Component_Component, Actor2_Actor, Actor3_Actor, Actor4_Actor, Component2_Component, Component3_Component, Actor5_Actor, Actor6_Actor, Actor7_Actor},
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