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
xDstmdata_vVariable = Class(name="xDstmdata::vVariable")
xDstmdata_tTypes = Class(name="xDstmdata::tTypes")
xDstmdata_tEnum = Class(name="xDstmdata::tEnum")
xDstmdata_tCompound = Class(name="xDstmdata::tCompound")
xDstmdata_tMultitype = Class(name="xDstmdata::tMultitype")
xDstmdata_cIntchannel = Class(name="xDstmdata::cIntchannel")
xDstmdata_cExtchannel = Class(name="xDstmdata::cExtchannel")
xDstmdata_subtype = Class(name="xDstmdata::subtype")
xDstmdata_channel_specifier = Class(name="xDstmdata::channel::specifier")
xDstmdata_composingtype = Class(name="xDstmdata::composingtype")

# xDstmdata_vVariable class attributes and methods
xDstmdata_vVariable_tString: Property = Property(name="tString", type=StringType)
xDstmdata_vVariable_tID: Property = Property(name="tID", type=StringType)
xDstmdata_vVariable_name: Property = Property(name="name", type=StringType)
xDstmdata_vVariable.attributes={xDstmdata_vVariable_tID, xDstmdata_vVariable_tString, xDstmdata_vVariable_name}

# xDstmdata_tTypes class attributes and methods

# xDstmdata_tEnum class attributes and methods
xDstmdata_tEnum_name: Property = Property(name="name", type=StringType)
xDstmdata_tEnum_literals: Property = Property(name="literals", type=StringType)
xDstmdata_tEnum.attributes={xDstmdata_tEnum_literals, xDstmdata_tEnum_name}

# xDstmdata_tCompound class attributes and methods
xDstmdata_tCompound_name: Property = Property(name="name", type=StringType)
xDstmdata_tCompound.attributes={xDstmdata_tCompound_name}

# xDstmdata_tMultitype class attributes and methods
xDstmdata_tMultitype_name: Property = Property(name="name", type=StringType)
xDstmdata_tMultitype.attributes={xDstmdata_tMultitype_name}

# xDstmdata_cIntchannel class attributes and methods
xDstmdata_cIntchannel_name: Property = Property(name="name", type=StringType)
xDstmdata_cIntchannel_bound: Property = Property(name="bound", type=IntegerType)
xDstmdata_cIntchannel_tString: Property = Property(name="tString", type=StringType)
xDstmdata_cIntchannel_tID: Property = Property(name="tID", type=StringType)
xDstmdata_cIntchannel.attributes={xDstmdata_cIntchannel_bound, xDstmdata_cIntchannel_tID, xDstmdata_cIntchannel_name, xDstmdata_cIntchannel_tString}

# xDstmdata_cExtchannel class attributes and methods
xDstmdata_cExtchannel_name: Property = Property(name="name", type=StringType)
xDstmdata_cExtchannel_tString: Property = Property(name="tString", type=StringType)
xDstmdata_cExtchannel_tID: Property = Property(name="tID", type=StringType)
xDstmdata_cExtchannel.attributes={xDstmdata_cExtchannel_tString, xDstmdata_cExtchannel_name, xDstmdata_cExtchannel_tID}

# xDstmdata_subtype class attributes and methods
xDstmdata_subtype_tString: Property = Property(name="tString", type=StringType)
xDstmdata_subtype_tID: Property = Property(name="tID", type=StringType)
xDstmdata_subtype.attributes={xDstmdata_subtype_tString, xDstmdata_subtype_tID}

# xDstmdata_channel_specifier class attributes and methods
xDstmdata_channel_specifier_type: Property = Property(name="type", type=StringType)
xDstmdata_channel_specifier.attributes={xDstmdata_channel_specifier_type}

# xDstmdata_composingtype class attributes and methods
xDstmdata_composingtype_tID: Property = Property(name="tID", type=StringType)
xDstmdata_composingtype_tString: Property = Property(name="tString", type=StringType)
xDstmdata_composingtype.attributes={xDstmdata_composingtype_tString, xDstmdata_composingtype_tID}

# Relationships
cExtchannel7: BinaryAssociation = BinaryAssociation(
    name="cExtchannel7",
    ends={
        Property(name="xDstmdata_cExtchannel", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes8", type=xDstmdata_cExtchannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vVariable9: BinaryAssociation = BinaryAssociation(
    name="vVariable9",
    ends={
        Property(name="xDstmdata_vVariable", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes10", type=xDstmdata_vVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tEnum0: BinaryAssociation = BinaryAssociation(
    name="tEnum0",
    ends={
        Property(name="xDstmdata_tEnum", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes", type=xDstmdata_tEnum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tCompound1: BinaryAssociation = BinaryAssociation(
    name="tCompound1",
    ends={
        Property(name="xDstmdata_tCompound", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes2", type=xDstmdata_tCompound, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tMultitype3: BinaryAssociation = BinaryAssociation(
    name="tMultitype3",
    ends={
        Property(name="xDstmdata_tMultitype", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes4", type=xDstmdata_tMultitype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cIntchannel5: BinaryAssociation = BinaryAssociation(
    name="cIntchannel5",
    ends={
        Property(name="xDstmdata_cIntchannel", type=xDstmdata_tTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tTypes6", type=xDstmdata_cIntchannel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tChn20: BinaryAssociation = BinaryAssociation(
    name="tChn20",
    ends={
        Property(name="xDstmdata_channel_specifier22", type=xDstmdata_cIntchannel, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_cIntchannel21", type=xDstmdata_channel_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subtypes11: BinaryAssociation = BinaryAssociation(
    name="subtypes11",
    ends={
        Property(name="xDstmdata_subtype", type=xDstmdata_tCompound, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tCompound12", type=xDstmdata_subtype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tChn13: BinaryAssociation = BinaryAssociation(
    name="tChn13",
    ends={
        Property(name="xDstmdata_channel_specifier", type=xDstmdata_subtype, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_subtype14", type=xDstmdata_channel_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
composingtypes15: BinaryAssociation = BinaryAssociation(
    name="composingtypes15",
    ends={
        Property(name="xDstmdata_composingtype", type=xDstmdata_tMultitype, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_tMultitype16", type=xDstmdata_composingtype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tChn17: BinaryAssociation = BinaryAssociation(
    name="tChn17",
    ends={
        Property(name="xDstmdata_channel_specifier19", type=xDstmdata_composingtype, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_composingtype18", type=xDstmdata_channel_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tChn23: BinaryAssociation = BinaryAssociation(
    name="tChn23",
    ends={
        Property(name="xDstmdata_channel_specifier25", type=xDstmdata_cExtchannel, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_cExtchannel24", type=xDstmdata_channel_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tChn26: BinaryAssociation = BinaryAssociation(
    name="tChn26",
    ends={
        Property(name="xDstmdata_channel_specifier28", type=xDstmdata_vVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="xDstmdata_vVariable27", type=xDstmdata_channel_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="xDstmdata",
    types={xDstmdata_vVariable, xDstmdata_tTypes, xDstmdata_tEnum, xDstmdata_tCompound, xDstmdata_tMultitype, xDstmdata_cIntchannel, xDstmdata_cExtchannel, xDstmdata_subtype, xDstmdata_channel_specifier, xDstmdata_composingtype},
    associations={cExtchannel7, vVariable9, tEnum0, tCompound1, tMultitype3, cIntchannel5, tChn20, subtypes11, tChn13, composingtypes15, tChn17, tChn23, tChn26},
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