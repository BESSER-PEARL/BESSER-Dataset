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
Triangles_Container = Class(name="Triangles::Container")
Triangles_A_Class = Class(name="Triangles::A::Class")
Triangles_E_Class = Class(name="Triangles::E::Class")
AbstractClass = Class(name="AbstractClass")
Triangles_AbstractClass = Class(name="Triangles::AbstractClass", is_abstract=True)
Triangles_B_Class = Class(name="Triangles::B::Class")
Triangles_C_Class = Class(name="Triangles::C::Class")
Triangles_D_Class = Class(name="Triangles::D::Class")

# Triangles_Container class attributes and methods

# Triangles_A_Class class attributes and methods

# Triangles_E_Class class attributes and methods

# AbstractClass class attributes and methods

# Triangles_AbstractClass class attributes and methods
Triangles_AbstractClass_id: Property = Property(name="id", type=IntegerType)
Triangles_AbstractClass_name: Property = Property(name="name", type=StringType)
Triangles_AbstractClass_flag: Property = Property(name="flag", type=BooleanType)
Triangles_AbstractClass.attributes={Triangles_AbstractClass_flag, Triangles_AbstractClass_name, Triangles_AbstractClass_id}

# Triangles_B_Class class attributes and methods

# Triangles_C_Class class attributes and methods

# Triangles_D_Class class attributes and methods

# Relationships
e7: BinaryAssociation = BinaryAssociation(
    name="e7",
    ends={
        Property(name="Triangles_E_Class", type=Triangles_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_Container8", type=Triangles_E_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b9: BinaryAssociation = BinaryAssociation(
    name="b9",
    ends={
        Property(name="B_Class", type=Triangles_A_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=Triangles_B_Class, multiplicity=Multiplicity(0, 9999))
    }
)
c10: BinaryAssociation = BinaryAssociation(
    name="c10",
    ends={
        Property(name="C_Class", type=Triangles_A_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="a11", type=Triangles_C_Class, multiplicity=Multiplicity(0, 9999))
    }
)
a12: BinaryAssociation = BinaryAssociation(
    name="a12",
    ends={
        Property(name="A_Class", type=Triangles_B_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=Triangles_A_Class, multiplicity=Multiplicity(0, 9999))
    }
)
c13: BinaryAssociation = BinaryAssociation(
    name="c13",
    ends={
        Property(name="C_Class15", type=Triangles_B_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="b14", type=Triangles_C_Class, multiplicity=Multiplicity(0, 9999))
    }
)
a16: BinaryAssociation = BinaryAssociation(
    name="a16",
    ends={
        Property(name="A_Class17", type=Triangles_C_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c", type=Triangles_A_Class, multiplicity=Multiplicity(0, 9999))
    }
)
b18: BinaryAssociation = BinaryAssociation(
    name="b18",
    ends={
        Property(name="B_Class20", type=Triangles_C_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="c19", type=Triangles_B_Class, multiplicity=Multiplicity(0, 9999))
    }
)
b21: BinaryAssociation = BinaryAssociation(
    name="b21",
    ends={
        Property(name="Triangles_B_Class23", type=Triangles_E_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_E_Class22", type=Triangles_B_Class, multiplicity=Multiplicity(0, 9999))
    }
)
a24: BinaryAssociation = BinaryAssociation(
    name="a24",
    ends={
        Property(name="Triangles_A_Class26", type=Triangles_D_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_D_Class25", type=Triangles_A_Class, multiplicity=Multiplicity(0, 9999))
    }
)
a0: BinaryAssociation = BinaryAssociation(
    name="a0",
    ends={
        Property(name="Triangles_A_Class", type=Triangles_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_Container", type=Triangles_A_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="Triangles_B_Class", type=Triangles_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_Container2", type=Triangles_B_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="Triangles_C_Class", type=Triangles_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_Container4", type=Triangles_C_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="Triangles_D_Class", type=Triangles_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="Triangles_Container6", type=Triangles_D_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Triangles_A_Class_AbstractClass = Generalization(general=AbstractClass, specific=Triangles_A_Class)
gen_Triangles_B_Class_AbstractClass = Generalization(general=AbstractClass, specific=Triangles_B_Class)
gen_Triangles_C_Class_AbstractClass = Generalization(general=AbstractClass, specific=Triangles_C_Class)
gen_Triangles_E_Class_AbstractClass = Generalization(general=AbstractClass, specific=Triangles_E_Class)
gen_Triangles_D_Class_AbstractClass = Generalization(general=AbstractClass, specific=Triangles_D_Class)

# Domain Model
domain_model = DomainModel(
    name="Triangles",
    types={Triangles_Container, Triangles_A_Class, Triangles_E_Class, AbstractClass, Triangles_AbstractClass, Triangles_B_Class, Triangles_C_Class, Triangles_D_Class},
    associations={e7, b9, c10, a12, c13, a16, b18, b21, a24, a0, b1, c3, d5},
    generalizations={gen_Triangles_A_Class_AbstractClass, gen_Triangles_B_Class_AbstractClass, gen_Triangles_C_Class_AbstractClass, gen_Triangles_E_Class_AbstractClass, gen_Triangles_D_Class_AbstractClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)