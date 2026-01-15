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
dml_D = Class(name="dml::D")
dml_F = Class(name="dml::F")
dml_E = Class(name="dml::E")
dml_S = Class(name="dml::S")
dml_ID = Class(name="dml::ID")
dml_PL = Class(name="dml::PL")
dml_SPKV = Class(name="dml::SPKV")
dml_DI = Class(name="dml::DI")
dml_FC = Class(name="dml::FC")
dml_BS = Class(name="dml::BS")
dml_FP = Class(name="dml::FP")
dml_PARFORPARAMS = Class(name="dml::PARFORPARAMS")
dml_IS = Class(name="dml::IS")
dml_PE = Class(name="dml::PE")
dml_EObject = Class(name="dml::EObject")
dml_TE = Class(name="dml::TE")
dml_TAN = Class(name="dml::TAN")

# dml_D class attributes and methods

# dml_F class attributes and methods

# dml_E class attributes and methods
dml_E_op: Property = Property(name="op", type=StringType)
dml_E.attributes={dml_E_op}

# dml_S class attributes and methods
dml_S_src: Property = Property(name="src", type=StringType)
dml_S_cwd: Property = Property(name="cwd", type=StringType)
dml_S.attributes={dml_S_src, dml_S_cwd}

# dml_ID class attributes and methods
dml_ID_name: Property = Property(name="name", type=StringType)
dml_ID.attributes={dml_ID_name}

# dml_PL class attributes and methods

# dml_SPKV class attributes and methods
dml_SPKV_v: Property = Property(name="v", type=StringType)
dml_SPKV.attributes={dml_SPKV_v}

# dml_DI class attributes and methods
dml_DI_clid: Property = Property(name="clid", type=StringType)
dml_DI_cln: Property = Property(name="cln", type=StringType)
dml_DI.attributes={dml_DI_cln, dml_DI_clid}

# dml_FC class attributes and methods
dml_FC_bif: Property = Property(name="bif", type=StringType)
dml_FC.attributes={dml_FC_bif}

# dml_BS class attributes and methods

# dml_FP class attributes and methods

# dml_PARFORPARAMS class attributes and methods
dml_PARFORPARAMS_params: Property = Property(name="params", type=StringType)
dml_PARFORPARAMS.attributes={dml_PARFORPARAMS_params}

# dml_IS class attributes and methods

# dml_PE class attributes and methods

# dml_EObject class attributes and methods

# dml_TE class attributes and methods
dml_TE_i: Property = Property(name="i", type=IntegerType)
dml_TE_d: Property = Property(name="d", type=FloatType)
dml_TE_s: Property = Property(name="s", type=StringType)
dml_TE_b: Property = Property(name="b", type=StringType)
dml_TE.attributes={dml_TE_d, dml_TE_b, dml_TE_i, dml_TE_s}

# dml_TAN class attributes and methods
dml_TAN_t: Property = Property(name="t", type=StringType)
dml_TAN.attributes={dml_TAN_t}

# Relationships
f0: BinaryAssociation = BinaryAssociation(
    name="f0",
    ends={
        Property(name="dml_F", type=dml_D, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_D", type=dml_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
srcid15: BinaryAssociation = BinaryAssociation(
    name="srcid15",
    ends={
        Property(name="dml_ID17", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S16", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ife18: BinaryAssociation = BinaryAssociation(
    name="ife18",
    ends={
        Property(name="dml_E", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S19", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
s1: BinaryAssociation = BinaryAssociation(
    name="s1",
    ends={
        Property(name="dml_S", type=dml_D, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_D2", type=dml_S, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name3: BinaryAssociation = BinaryAssociation(
    name="name3",
    ends={
        Property(name="dml_ID", type=dml_F, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_F4", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
i5: BinaryAssociation = BinaryAssociation(
    name="i5",
    ends={
        Property(name="dml_PL", type=dml_F, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_F6", type=dml_PL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
r7: BinaryAssociation = BinaryAssociation(
    name="r7",
    ends={
        Property(name="dml_PL9", type=dml_F, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_F8", type=dml_PL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
s10: BinaryAssociation = BinaryAssociation(
    name="s10",
    ends={
        Property(name="dml_S12", type=dml_F, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_F11", type=dml_S, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
spkv13: BinaryAssociation = BinaryAssociation(
    name="spkv13",
    ends={
        Property(name="dml_SPKV", type=dml_F, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_F14", type=dml_SPKV, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
di38: BinaryAssociation = BinaryAssociation(
    name="di38",
    ends={
        Property(name="dml_DI", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S39", type=dml_DI, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fc40: BinaryAssociation = BinaryAssociation(
    name="fc40",
    ends={
        Property(name="dml_FC", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S41", type=dml_FC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhsdi42: BinaryAssociation = BinaryAssociation(
    name="lhsdi42",
    ends={
        Property(name="dml_DI44", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S43", type=dml_DI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is20: BinaryAssociation = BinaryAssociation(
    name="is20",
    ends={
        Property(name="dml_BS", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S21", type=dml_BS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
es22: BinaryAssociation = BinaryAssociation(
    name="es22",
    ends={
        Property(name="dml_BS24", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S23", type=dml_BS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fp25: BinaryAssociation = BinaryAssociation(
    name="fp25",
    ends={
        Property(name="dml_FP", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S26", type=dml_FP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
p27: BinaryAssociation = BinaryAssociation(
    name="p27",
    ends={
        Property(name="dml_PARFORPARAMS", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S28", type=dml_PARFORPARAMS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
s29: BinaryAssociation = BinaryAssociation(
    name="s29",
    ends={
        Property(name="dml_BS31", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S30", type=dml_BS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pf32: BinaryAssociation = BinaryAssociation(
    name="pf32",
    ends={
        Property(name="dml_FP34", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S33", type=dml_FP, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
we35: BinaryAssociation = BinaryAssociation(
    name="we35",
    ends={
        Property(name="dml_E37", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S36", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
is62: BinaryAssociation = BinaryAssociation(
    name="is62",
    ends={
        Property(name="dml_IS", type=dml_FP, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_FP63", type=dml_IS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id64: BinaryAssociation = BinaryAssociation(
    name="id64",
    ends={
        Property(name="dml_ID66", type=dml_DI, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_DI65", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b67: BinaryAssociation = BinaryAssociation(
    name="b67",
    ends={
        Property(name="dml_IS69", type=dml_DI, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_DI68", type=dml_IS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e45: BinaryAssociation = BinaryAssociation(
    name="e45",
    ends={
        Property(name="dml_E47", type=dml_S, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_S46", type=dml_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
e70: BinaryAssociation = BinaryAssociation(
    name="e70",
    ends={
        Property(name="dml_IS72", type=dml_DI, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_DI71", type=dml_IS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id48: BinaryAssociation = BinaryAssociation(
    name="id48",
    ends={
        Property(name="dml_ID50", type=dml_FC, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_FC49", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e173: BinaryAssociation = BinaryAssociation(
    name="e173",
    ends={
        Property(name="dml_E75", type=dml_IS, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_IS74", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pe51: BinaryAssociation = BinaryAssociation(
    name="pe51",
    ends={
        Property(name="dml_PE", type=dml_FC, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_FC52", type=dml_PE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleS53: BinaryAssociation = BinaryAssociation(
    name="singleS53",
    ends={
        Property(name="dml_S55", type=dml_BS, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_BS54", type=dml_S, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
s56: BinaryAssociation = BinaryAssociation(
    name="s56",
    ends={
        Property(name="dml_S58", type=dml_BS, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_BS57", type=dml_S, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id59: BinaryAssociation = BinaryAssociation(
    name="id59",
    ends={
        Property(name="dml_ID61", type=dml_FP, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_FP60", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t181: BinaryAssociation = BinaryAssociation(
    name="t181",
    ends={
        Property(name="dml_EObject", type=dml_E, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_E82", type=dml_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t284: BinaryAssociation = BinaryAssociation(
    name="t284",
    ends={
        Property(name="dml_E85", type=dml_E, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_E83", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e86: BinaryAssociation = BinaryAssociation(
    name="e86",
    ends={
        Property(name="dml_E87", type=dml_TE, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_TE", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
f88: BinaryAssociation = BinaryAssociation(
    name="f88",
    ends={
        Property(name="dml_FC90", type=dml_TE, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_TE89", type=dml_FC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
di91: BinaryAssociation = BinaryAssociation(
    name="di91",
    ends={
        Property(name="dml_DI93", type=dml_TE, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_TE92", type=dml_DI, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e276: BinaryAssociation = BinaryAssociation(
    name="e276",
    ends={
        Property(name="dml_E78", type=dml_IS, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_IS77", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
k94: BinaryAssociation = BinaryAssociation(
    name="k94",
    ends={
        Property(name="dml_ID96", type=dml_SPKV, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_SPKV95", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
t79: BinaryAssociation = BinaryAssociation(
    name="t79",
    ends={
        Property(name="dml_TAN", type=dml_PL, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_PL80", type=dml_TAN, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name103: BinaryAssociation = BinaryAssociation(
    name="name103",
    ends={
        Property(name="dml_ID105", type=dml_TAN, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_TAN104", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
id97: BinaryAssociation = BinaryAssociation(
    name="id97",
    ends={
        Property(name="dml_ID99", type=dml_PE, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_PE98", type=dml_ID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
e100: BinaryAssociation = BinaryAssociation(
    name="e100",
    ends={
        Property(name="dml_E102", type=dml_PE, multiplicity=Multiplicity(1, 1)),
        Property(name="dml_PE101", type=dml_E, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="dml",
    types={dml_D, dml_F, dml_E, dml_S, dml_ID, dml_PL, dml_SPKV, dml_DI, dml_FC, dml_BS, dml_FP, dml_PARFORPARAMS, dml_IS, dml_PE, dml_EObject, dml_TE, dml_TAN},
    associations={f0, srcid15, ife18, s1, name3, i5, r7, s10, spkv13, di38, fc40, lhsdi42, is20, es22, fp25, p27, s29, pf32, we35, is62, id64, b67, e45, e70, id48, e173, pe51, singleS53, s56, id59, t181, t284, e86, f88, di91, e276, k94, t79, name103, id97, e100},
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