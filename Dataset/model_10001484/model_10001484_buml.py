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
cgv_Classqwe = Class(name="cgv_Classqwe")
vvvv = Class(name="vvvv")
aaa = Class(name="aaa")
ccc = Class(name="ccc")
Class_ = Class(name="Class")
vcx = Class(name="vcx")
Class4 = Class(name="Class4")

# cgv_Classqwe class attributes and methods
cgv_Classqwe_qw: Property = Property(name="qw", type=aaa)
cgv_Classqwe.attributes={cgv_Classqwe_qw}

# vvvv class attributes and methods
vvvv_zsxc: Property = Property(name="zsxc", type=IntegerType)
vvvv.attributes={vvvv_zsxc}

# aaa class attributes and methods
aaa_attribute: Property = Property(name="attribute", type=BooleanType)
aaa_qwe: Property = Property(name="qwe", type=aaa)
aaa.attributes={aaa_qwe, aaa_attribute}

# ccc class attributes and methods
ccc_qwe: Property = Property(name="qwe", type=StringType)
ccc.attributes={ccc_qwe}

# Class class attributes and methods

# vcx class attributes and methods
vcx_attribute: Property = Property(name="attribute", type=BooleanType)
vcx_attribute2: Property = Property(name="attribute2", type=StringType)
vcx.attributes={vcx_attribute, vcx_attribute2}

# Class4 class attributes and methods
Class4_attribute: Property = Property(name="attribute", type=StringType)
Class4.attributes={Class4_attribute}

# Relationships
c3_c2: BinaryAssociation = BinaryAssociation(
    name="c3_c2",
    ends={
        Property(name="c20", type=aaa, multiplicity=Multiplicity(1, 1)),
        Property(name="c31", type=ccc, multiplicity=Multiplicity(0, 9999))
    }
)
Class2_Class4: BinaryAssociation = BinaryAssociation(
    name="Class2_Class4",
    ends={
        Property(name="class42", type=Class4, multiplicity=Multiplicity(0, 1)),
        Property(name="class23", type=vcx, multiplicity=Multiplicity(0, 1))
    }
)
Class2_vvvv: BinaryAssociation = BinaryAssociation(
    name="Class2_vvvv",
    ends={
        Property(name="vvvv4", type=vvvv, multiplicity=Multiplicity(1, 1)),
        Property(name="class25", type=vcx, multiplicity=Multiplicity(0, 9999))
    }
)
Class2_Classqwe: BinaryAssociation = BinaryAssociation(
    name="Class2_Classqwe",
    ends={
        Property(name="classqwe6", type=cgv_Classqwe, multiplicity=Multiplicity(0, 1)),
        Property(name="class27", type=vcx, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_A7QHYOheEeiV94kHgjpOMg",
    types={cgv_Classqwe, vvvv, aaa, ccc, Class_, vcx, Class4},
    associations={c3_c2, Class2_Class4, Class2_vvvv, Class2_Classqwe},
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