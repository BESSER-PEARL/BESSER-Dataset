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
kreq108c_Bbbb = Class(name="kreq108c::Bbbb")
kreq108c_Cccc = Class(name="kreq108c::Cccc")
kreq108c_Eeee = Class(name="kreq108c::Eeee")
kreq108c_Ffff = Class(name="kreq108c::Ffff")
kreq108c_Gggg = Class(name="kreq108c::Gggg", is_abstract=True)
Gggg = Class(name="Gggg")

# kreq108c_Bbbb class attributes and methods

# kreq108c_Cccc class attributes and methods
kreq108c_Cccc_id: Property = Property(name="id", type=StringType)
kreq108c_Cccc.attributes={kreq108c_Cccc_id}

# kreq108c_Eeee class attributes and methods
kreq108c_Eeee_id: Property = Property(name="id", type=StringType)
kreq108c_Eeee.attributes={kreq108c_Eeee_id}

# kreq108c_Ffff class attributes and methods
kreq108c_Ffff_id: Property = Property(name="id", type=StringType)
kreq108c_Ffff.attributes={kreq108c_Ffff_id}

# kreq108c_Gggg class attributes and methods
kreq108c_Gggg_name: Property = Property(name="name", type=StringType)
kreq108c_Gggg.attributes={kreq108c_Gggg_name}

# Gggg class attributes and methods

# Relationships
cs0: BinaryAssociation = BinaryAssociation(
    name="cs0",
    ends={
        Property(name="kreq108c_Cccc", type=kreq108c_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq108c_Bbbb", type=kreq108c_Cccc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
es1: BinaryAssociation = BinaryAssociation(
    name="es1",
    ends={
        Property(name="kreq108c_Eeee", type=kreq108c_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq108c_Bbbb2", type=kreq108c_Eeee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fs3: BinaryAssociation = BinaryAssociation(
    name="fs3",
    ends={
        Property(name="kreq108c_Ffff", type=kreq108c_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq108c_Cccc4", type=kreq108c_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
varifedBy5: BinaryAssociation = BinaryAssociation(
    name="varifedBy5",
    ends={
        Property(name="kreq108c_Eeee7", type=kreq108c_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq108c_Ffff6", type=kreq108c_Eeee, multiplicity=Multiplicity(0, 9999))
    }
)
subFs9: BinaryAssociation = BinaryAssociation(
    name="subFs9",
    ends={
        Property(name="kreq108c_Ffff10", type=kreq108c_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq108c_Ffff8", type=kreq108c_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_kreq108c_Ffff_Gggg = Generalization(general=Gggg, specific=kreq108c_Ffff)
gen_kreq108c_Eeee_Gggg = Generalization(general=Gggg, specific=kreq108c_Eeee)

# Domain Model
domain_model = DomainModel(
    name="kreq108c",
    types={kreq108c_Bbbb, kreq108c_Cccc, kreq108c_Eeee, kreq108c_Ffff, kreq108c_Gggg, Gggg},
    associations={cs0, es1, fs3, varifedBy5, subFs9},
    generalizations={gen_kreq108c_Ffff_Gggg, gen_kreq108c_Eeee_Gggg},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)