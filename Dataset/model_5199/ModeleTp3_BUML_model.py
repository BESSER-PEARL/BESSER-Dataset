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
ModeleTp3_Int = Class(name="ModeleTp3::Int")
ModeleTp3_pack1_B = Class(name="ModeleTp3::pack1::B")
ModeleTp3_pack1_A = Class(name="ModeleTp3::pack1::A")
pack1_ModeleTp3_Int = Class(name="pack1::ModeleTp3::Int")
ModeleTp3_pack2_C = Class(name="ModeleTp3::pack2::C")
ModeleTp3_pack2_D = Class(name="ModeleTp3::pack2::D")
C = Class(name="C")
ModeleTp3_pack2_E = Class(name="ModeleTp3::pack2::E")
pack2_ModeleTp3_Int = Class(name="pack2::ModeleTp3::Int")

# ModeleTp3_Int class attributes and methods

# ModeleTp3_pack1_B class attributes and methods

# ModeleTp3_pack1_A class attributes and methods

# pack1_ModeleTp3_Int class attributes and methods

# ModeleTp3_pack2_C class attributes and methods

# ModeleTp3_pack2_D class attributes and methods
ModeleTp3_pack2_D_m_foo: Method = Method(name="foo", parameters={})
ModeleTp3_pack2_D.methods={ModeleTp3_pack2_D_m_foo}

# C class attributes and methods

# ModeleTp3_pack2_E class attributes and methods

# pack2_ModeleTp3_Int class attributes and methods

# Relationships
t0: BinaryAssociation = BinaryAssociation(
    name="t0",
    ends={
        Property(name="pack1_ModeleTp3_Int", type=ModeleTp3_pack1_A, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeleTp3_pack1_A", type=pack1_ModeleTp3_Int, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
x1: BinaryAssociation = BinaryAssociation(
    name="x1",
    ends={
        Property(name="pack2_ModeleTp3_Int", type=ModeleTp3_pack2_E, multiplicity=Multiplicity(1, 1)),
        Property(name="ModeleTp3_pack2_E", type=pack2_ModeleTp3_Int, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_ModeleTp3_pack2_D_C = Generalization(general=C, specific=ModeleTp3_pack2_D)

# Domain Model
domain_model = DomainModel(
    name="ModeleTp3",
    types={ModeleTp3_Int, ModeleTp3_pack1_B, ModeleTp3_pack1_A, pack1_ModeleTp3_Int, ModeleTp3_pack2_C, ModeleTp3_pack2_D, C, ModeleTp3_pack2_E, pack2_ModeleTp3_Int},
    associations={t0, x1},
    generalizations={gen_ModeleTp3_pack2_D_C},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)