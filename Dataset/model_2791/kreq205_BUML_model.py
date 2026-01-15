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
kreq205_Bbbb = Class(name="kreq205::Bbbb")
kreq205_Rrrr = Class(name="kreq205::Rrrr")
kreq205_Tttt = Class(name="kreq205::Tttt")
kreq205_Ffff = Class(name="kreq205::Ffff")
kreq205_Rqs = Class(name="kreq205::Rqs")
SObject = Class(name="SObject")
kreq205_Cccc = Class(name="kreq205::Cccc")
kreq205_Llll = Class(name="kreq205::Llll")
kreq205_SObject = Class(name="kreq205::SObject", is_abstract=True)

# kreq205_Bbbb class attributes and methods

# kreq205_Rrrr class attributes and methods
kreq205_Rrrr_d3: Property = Property(name="d3", type=StringType)
kreq205_Rrrr.attributes={kreq205_Rrrr_d3}

# kreq205_Tttt class attributes and methods

# kreq205_Ffff class attributes and methods
kreq205_Ffff_d4: Property = Property(name="d4", type=StringType)
kreq205_Ffff.attributes={kreq205_Ffff_d4}

# kreq205_Rqs class attributes and methods
kreq205_Rqs_d2: Property = Property(name="d2", type=StringType)
kreq205_Rqs_a: Property = Property(name="a", type=BooleanType)
kreq205_Rqs.attributes={kreq205_Rqs_d2, kreq205_Rqs_a}

# SObject class attributes and methods

# kreq205_Cccc class attributes and methods
kreq205_Cccc_de1: Property = Property(name="de1", type=StringType)
kreq205_Cccc.attributes={kreq205_Cccc_de1}

# kreq205_Llll class attributes and methods
kreq205_Llll_d6: Property = Property(name="d6", type=StringType)
kreq205_Llll.attributes={kreq205_Llll_d6}

# kreq205_SObject class attributes and methods
kreq205_SObject_name: Property = Property(name="name", type=StringType)
kreq205_SObject_id: Property = Property(name="id", type=StringType)
kreq205_SObject.attributes={kreq205_SObject_id, kreq205_SObject_name}

# Relationships
rs0: BinaryAssociation = BinaryAssociation(
    name="rs0",
    ends={
        Property(name="kreq205_Rrrr", type=kreq205_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Bbbb", type=kreq205_Rrrr, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ts1: BinaryAssociation = BinaryAssociation(
    name="ts1",
    ends={
        Property(name="kreq205_Tttt", type=kreq205_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Bbbb2", type=kreq205_Tttt, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fs5: BinaryAssociation = BinaryAssociation(
    name="fs5",
    ends={
        Property(name="kreq205_Ffff", type=kreq205_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Bbbb6", type=kreq205_Ffff, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rqs7: BinaryAssociation = BinaryAssociation(
    name="rqs7",
    ends={
        Property(name="kreq205_Rqs", type=kreq205_Rrrr, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Rrrr8", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rqs9: BinaryAssociation = BinaryAssociation(
    name="rqs9",
    ends={
        Property(name="Rqs", type=kreq205_Tttt, multiplicity=Multiplicity(1, 1)),
        Property(name="rts", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999))
    }
)
rts10: BinaryAssociation = BinaryAssociation(
    name="rts10",
    ends={
        Property(name="Tttt", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="rqs", type=kreq205_Tttt, multiplicity=Multiplicity(0, 9999))
    }
)
dReqt12: BinaryAssociation = BinaryAssociation(
    name="dReqt12",
    ends={
        Property(name="kreq205_Rqs13", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Rqs11", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999))
    }
)
subRqs15: BinaryAssociation = BinaryAssociation(
    name="subRqs15",
    ends={
        Property(name="kreq205_Rqs16", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Rqs14", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ccs3: BinaryAssociation = BinaryAssociation(
    name="ccs3",
    ends={
        Property(name="kreq205_Cccc", type=kreq205_Bbbb, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Bbbb4", type=kreq205_Cccc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refine19: BinaryAssociation = BinaryAssociation(
    name="refine19",
    ends={
        Property(name="kreq205_Rqs20", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Rqs18", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999))
    }
)
spc21: BinaryAssociation = BinaryAssociation(
    name="spc21",
    ends={
        Property(name="Cccc", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="specifiedBy", type=kreq205_Cccc, multiplicity=Multiplicity(0, 9999))
    }
)
isBy22: BinaryAssociation = BinaryAssociation(
    name="isBy22",
    ends={
        Property(name="Rqs23", type=kreq205_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="specs", type=kreq205_Rqs, multiplicity=Multiplicity(0, 9999))
    }
)
dmof24: BinaryAssociation = BinaryAssociation(
    name="dmof24",
    ends={
        Property(name="Cccc25", type=kreq205_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="pfrmis", type=kreq205_Cccc, multiplicity=Multiplicity(0, 9999))
    }
)
subFs27: BinaryAssociation = BinaryAssociation(
    name="subFs27",
    ends={
        Property(name="kreq205_Ffff28", type=kreq205_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Ffff26", type=kreq205_Ffff, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alto29: BinaryAssociation = BinaryAssociation(
    name="alto29",
    ends={
        Property(name="Cccc30", type=kreq205_Ffff, multiplicity=Multiplicity(1, 1)),
        Property(name="impf", type=kreq205_Cccc, multiplicity=Multiplicity(0, 9999))
    }
)
specs17: BinaryAssociation = BinaryAssociation(
    name="specs17",
    ends={
        Property(name="Ffff", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1)),
        Property(name="isBy", type=kreq205_Ffff, multiplicity=Multiplicity(0, 9999))
    }
)
satisfy31: BinaryAssociation = BinaryAssociation(
    name="satisfy31",
    ends={
        Property(name="kreq205_Rqs33", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Cccc32", type=kreq205_Rqs, multiplicity=Multiplicity(1, 9999))
    }
)
specifiedBy34: BinaryAssociation = BinaryAssociation(
    name="specifiedBy34",
    ends={
        Property(name="Rqs35", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="spc", type=kreq205_Rqs, multiplicity=Multiplicity(1, 9999))
    }
)
pfrmis36: BinaryAssociation = BinaryAssociation(
    name="pfrmis36",
    ends={
        Property(name="Ffff37", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="dmof", type=kreq205_Ffff, multiplicity=Multiplicity(0, 9999))
    }
)
subCs39: BinaryAssociation = BinaryAssociation(
    name="subCs39",
    ends={
        Property(name="kreq205_Cccc40", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Cccc38", type=kreq205_Cccc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
impf41: BinaryAssociation = BinaryAssociation(
    name="impf41",
    ends={
        Property(name="Ffff42", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="alto", type=kreq205_Ffff, multiplicity=Multiplicity(0, 9999))
    }
)
ls43: BinaryAssociation = BinaryAssociation(
    name="ls43",
    ends={
        Property(name="kreq205_Llll", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Cccc44", type=kreq205_Llll, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source45: BinaryAssociation = BinaryAssociation(
    name="source45",
    ends={
        Property(name="kreq205_Cccc47", type=kreq205_Llll, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Llll46", type=kreq205_Cccc, multiplicity=Multiplicity(1, 1))
    }
)
target48: BinaryAssociation = BinaryAssociation(
    name="target48",
    ends={
        Property(name="kreq205_Rqs50", type=kreq205_Llll, multiplicity=Multiplicity(1, 1)),
        Property(name="kreq205_Llll49", type=kreq205_Rqs, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_kreq205_Tttt_SObject = Generalization(general=SObject, specific=kreq205_Tttt)
gen_kreq205_Rqs_SObject = Generalization(general=SObject, specific=kreq205_Rqs)

# Domain Model
domain_model = DomainModel(
    name="kreq205",
    types={kreq205_Bbbb, kreq205_Rrrr, kreq205_Tttt, kreq205_Ffff, kreq205_Rqs, SObject, kreq205_Cccc, kreq205_Llll, kreq205_SObject},
    associations={rs0, ts1, fs5, rqs7, rqs9, rts10, dReqt12, subRqs15, ccs3, refine19, spc21, isBy22, dmof24, subFs27, alto29, specs17, satisfy31, specifiedBy34, pfrmis36, subCs39, impf41, ls43, source45, target48},
    generalizations={gen_kreq205_Tttt_SObject, gen_kreq205_Rqs_SObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)