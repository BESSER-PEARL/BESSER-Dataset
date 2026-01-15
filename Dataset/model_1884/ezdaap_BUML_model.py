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

# Enumerations
DAAP_CONNECTION_KIND: Enumeration = Enumeration(
    name="DAAP_CONNECTION_KIND",
    literals={
            EnumerationLiteral(name="USER"),
			EnumerationLiteral(name="DB")
    }
)

DAAP_COMM_CST: Enumeration = Enumeration(
    name="DAAP_COMM_CST",
    literals={
            EnumerationLiteral(name="MAX_USER_CONNECTIONS_PER_SESSION"),
			EnumerationLiteral(name="MAX_USER_SIMULTANEOUS_CONNECTION"),
			EnumerationLiteral(name="MAX_SIMULTATNEOUS_CONNECTIONS")
    }
)

# Classes
ezdaap_EZDaapAlbum = Class(name="ezdaap::EZDaapAlbum")
ezdaap_EZDaapArtist = Class(name="ezdaap::EZDaapArtist")
ezdaap_EZDaapITunesInstance = Class(name="ezdaap::EZDaapITunesInstance")
ezdaap_EZDaapLibrary = Class(name="ezdaap::EZDaapLibrary")
ezdaap_EZDaapPlayList = Class(name="ezdaap::EZDaapPlayList")
ezdaap_EZDaapSong = Class(name="ezdaap::EZDaapSong")
ezdaap_EZDaapDictionary = Class(name="ezdaap::EZDaapDictionary")
ezdaap_EZDaapManager = Class(name="ezdaap::EZDaapManager")
EZDaapElem = Class(name="EZDaapElem")
EZDaapIntelPropertyElem = Class(name="EZDaapIntelPropertyElem")
ezdaap_EZDaapLibraryUnit = Class(name="ezdaap::EZDaapLibraryUnit", is_abstract=True)
EZDaapLibraryUnit = Class(name="EZDaapLibraryUnit")
ezdaap_EZDaapElem = Class(name="ezdaap::EZDaapElem")
ezdaap_EZDaapIntelPropertyElem = Class(name="ezdaap::EZDaapIntelPropertyElem")

# ezdaap_EZDaapAlbum class attributes and methods

# ezdaap_EZDaapArtist class attributes and methods

# ezdaap_EZDaapITunesInstance class attributes and methods
ezdaap_EZDaapITunesInstance_revID: Property = Property(name="revID", type=IntegerType)
ezdaap_EZDaapITunesInstance_id: Property = Property(name="id", type=StringType)
ezdaap_EZDaapITunesInstance_sessionID: Property = Property(name="sessionID", type=IntegerType)
ezdaap_EZDaapITunesInstance_serverName: Property = Property(name="serverName", type=StringType)
ezdaap_EZDaapITunesInstance.attributes={ezdaap_EZDaapITunesInstance_revID, ezdaap_EZDaapITunesInstance_sessionID, ezdaap_EZDaapITunesInstance_id, ezdaap_EZDaapITunesInstance_serverName}

# ezdaap_EZDaapLibrary class attributes and methods

# ezdaap_EZDaapPlayList class attributes and methods

# ezdaap_EZDaapSong class attributes and methods

# ezdaap_EZDaapDictionary class attributes and methods

# ezdaap_EZDaapManager class attributes and methods

# EZDaapElem class attributes and methods

# EZDaapIntelPropertyElem class attributes and methods

# ezdaap_EZDaapLibraryUnit class attributes and methods
ezdaap_EZDaapLibraryUnit_name: Property = Property(name="name", type=StringType)
ezdaap_EZDaapLibraryUnit.attributes={ezdaap_EZDaapLibraryUnit_name}

# EZDaapLibraryUnit class attributes and methods

# ezdaap_EZDaapElem class attributes and methods

# ezdaap_EZDaapIntelPropertyElem class attributes and methods
ezdaap_EZDaapIntelPropertyElem_license: Property = Property(name="license", type=StringType)
ezdaap_EZDaapIntelPropertyElem.attributes={ezdaap_EZDaapIntelPropertyElem_license}

# Relationships
Albums5: BinaryAssociation = BinaryAssociation(
    name="Albums5",
    ends={
        Property(name="ezdaap_EZDaapAlbum", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapITunesInstance6", type=ezdaap_EZDaapAlbum, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists7: BinaryAssociation = BinaryAssociation(
    name="artists7",
    ends={
        Property(name="ezdaap_EZDaapArtist", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapITunesInstance8", type=ezdaap_EZDaapArtist, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraries0: BinaryAssociation = BinaryAssociation(
    name="libraries0",
    ends={
        Property(name="ezdaap_EZDaapLibrary", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapITunesInstance", type=ezdaap_EZDaapLibrary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
palylists1: BinaryAssociation = BinaryAssociation(
    name="palylists1",
    ends={
        Property(name="ezdaap_EZDaapPlayList", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapITunesInstance2", type=ezdaap_EZDaapPlayList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
songs3: BinaryAssociation = BinaryAssociation(
    name="songs3",
    ends={
        Property(name="ezdaap_EZDaapSong", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapITunesInstance4", type=ezdaap_EZDaapSong, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iTunes9: BinaryAssociation = BinaryAssociation(
    name="iTunes9",
    ends={
        Property(name="ezdaap_EZDaapITunesInstance10", type=ezdaap_EZDaapManager, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapManager", type=ezdaap_EZDaapITunesInstance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
songs11: BinaryAssociation = BinaryAssociation(
    name="songs11",
    ends={
        Property(name="ezdaap_EZDaapSong13", type=ezdaap_EZDaapAlbum, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapAlbum12", type=ezdaap_EZDaapSong, multiplicity=Multiplicity(0, 9999))
    }
)
songs14: BinaryAssociation = BinaryAssociation(
    name="songs14",
    ends={
        Property(name="ezdaap_EZDaapSong16", type=ezdaap_EZDaapPlayList, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapPlayList15", type=ezdaap_EZDaapSong, multiplicity=Multiplicity(0, 9999))
    }
)
elements17: BinaryAssociation = BinaryAssociation(
    name="elements17",
    ends={
        Property(name="ezdaap_EZDaapLibraryUnit", type=ezdaap_EZDaapLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapLibrary18", type=ezdaap_EZDaapLibraryUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists19: BinaryAssociation = BinaryAssociation(
    name="artists19",
    ends={
        Property(name="ezdaap_EZDaapArtist20", type=ezdaap_EZDaapIntelPropertyElem, multiplicity=Multiplicity(1, 1)),
        Property(name="ezdaap_EZDaapIntelPropertyElem", type=ezdaap_EZDaapArtist, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ezdaap_EZDaapPlayList_EZDaapElem = Generalization(general=EZDaapElem, specific=ezdaap_EZDaapPlayList)
gen_ezdaap_EZDaapSong_EZDaapElem = Generalization(general=EZDaapElem, specific=ezdaap_EZDaapSong)
gen_ezdaap_EZDaapSong_EZDaapIntelPropertyElem = Generalization(general=EZDaapIntelPropertyElem, specific=ezdaap_EZDaapSong)
gen_ezdaap_EZDaapAlbum_EZDaapIntelPropertyElem = Generalization(general=EZDaapIntelPropertyElem, specific=ezdaap_EZDaapAlbum)
gen_ezdaap_EZDaapAlbum_EZDaapElem = Generalization(general=EZDaapElem, specific=ezdaap_EZDaapAlbum)
gen_ezdaap_EZDaapLibrary_EZDaapLibraryUnit = Generalization(general=EZDaapLibraryUnit, specific=ezdaap_EZDaapLibrary)
gen_ezdaap_EZDaapElem_EZDaapLibraryUnit = Generalization(general=EZDaapLibraryUnit, specific=ezdaap_EZDaapElem)

# Domain Model
domain_model = DomainModel(
    name="ezdaap",
    types={ezdaap_EZDaapAlbum, ezdaap_EZDaapArtist, ezdaap_EZDaapITunesInstance, ezdaap_EZDaapLibrary, ezdaap_EZDaapPlayList, ezdaap_EZDaapSong, ezdaap_EZDaapDictionary, ezdaap_EZDaapManager, EZDaapElem, EZDaapIntelPropertyElem, ezdaap_EZDaapLibraryUnit, EZDaapLibraryUnit, ezdaap_EZDaapElem, ezdaap_EZDaapIntelPropertyElem, DAAP_CONNECTION_KIND, DAAP_COMM_CST},
    associations={Albums5, artists7, libraries0, palylists1, songs3, iTunes9, songs11, songs14, elements17, artists19},
    generalizations={gen_ezdaap_EZDaapPlayList_EZDaapElem, gen_ezdaap_EZDaapSong_EZDaapElem, gen_ezdaap_EZDaapSong_EZDaapIntelPropertyElem, gen_ezdaap_EZDaapAlbum_EZDaapIntelPropertyElem, gen_ezdaap_EZDaapAlbum_EZDaapElem, gen_ezdaap_EZDaapLibrary_EZDaapLibraryUnit, gen_ezdaap_EZDaapElem_EZDaapLibraryUnit},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)