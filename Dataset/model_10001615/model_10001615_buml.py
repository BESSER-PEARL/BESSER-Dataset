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
Group = Class(name="Group")
Ver_ffentlich = Class(name="Ver_ffentlich")
Privat = Class(name="Privat")
_unnamed = Class(name="_unnamed")
Freund = Class(name="Freund")
Hashtag = Class(name="Hashtag")
Registrieren = Class(name="Registrieren")
Anmelden = Class(name="Anmelden")
Kommentare = Class(name="Kommentare")
Benutzer = Class(name="Benutzer")
Beitrag = Class(name="Beitrag")

# Group class attributes and methods
Group_name: Property = Property(name="name", type=StringType)
Group.attributes={Group_name}

# Ver_ffentlich class attributes and methods

# Privat class attributes and methods

# _unnamed class attributes and methods
_unnamed_maxChars: Property = Property(name="maxChars", type=StringType)
_unnamed.attributes={_unnamed_maxChars}

# Freund class attributes and methods

# Hashtag class attributes and methods
Hashtag_name: Property = Property(name="name", type=StringType)
Hashtag_numOfRepeat: Property = Property(name="numOfRepeat", type=IntegerType)
Hashtag.attributes={Hashtag_name, Hashtag_numOfRepeat}

# Registrieren class attributes and methods
Registrieren_vorname: Property = Property(name="vorname", type=StringType)
Registrieren_nachname: Property = Property(name="nachname", type=StringType)
Registrieren_email: Property = Property(name="email", type=StringType)
Registrieren_passwort: Property = Property(name="passwort", type=StringType)
Registrieren_email1: Property = Property(name="email1", type=StringType)
Registrieren_geburtsdatum: Property = Property(name="geburtsdatum", type=StringType)
Registrieren_geschlecht: Property = Property(name="geschlecht", type=StringType)
Registrieren.attributes={Registrieren_vorname, Registrieren_geburtsdatum, Registrieren_nachname, Registrieren_email, Registrieren_passwort, Registrieren_geschlecht, Registrieren_email1}

# Anmelden class attributes and methods
Anmelden_email: Property = Property(name="email", type=StringType)
Anmelden_passwort: Property = Property(name="passwort", type=StringType)
Anmelden.attributes={Anmelden_email, Anmelden_passwort}

# Kommentare class attributes and methods
Kommentare_text: Property = Property(name="text", type=StringType)
Kommentare.attributes={Kommentare_text}

# Benutzer class attributes and methods
Benutzer_Vorname: Property = Property(name="Vorname", type=StringType)
Benutzer_Nachname: Property = Property(name="Nachname", type=StringType)
Benutzer_Info: Property = Property(name="Info", type=StringType)
Benutzer_profilbild: Property = Property(name="profilbild", type=StringType)
Benutzer.attributes={Benutzer_Vorname, Benutzer_Nachname, Benutzer_Info, Benutzer_profilbild}

# Beitrag class attributes and methods
Beitrag_privatph_re: Property = Property(name="privatph_re", type=StringType)
Beitrag_text: Property = Property(name="text", type=StringType)
Beitrag_foto: Property = Property(name="foto", type=StringType)
Beitrag_video: Property = Property(name="video", type=StringType)
Beitrag_Audio: Property = Property(name="Audio", type=StringType)
Beitrag.attributes={Beitrag_Audio, Beitrag_text, Beitrag_video, Beitrag_privatph_re, Beitrag_foto}

# Relationships
User_Post: BinaryAssociation = BinaryAssociation(
    name="User_Post",
    ends={
        Property(name="post0", type=Beitrag, multiplicity=Multiplicity(0, 9999)),
        Property(name="user1", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Login: BinaryAssociation = BinaryAssociation(
    name="User_Login",
    ends={
        Property(name="login2", type=Anmelden, multiplicity=Multiplicity(1, 1)),
        Property(name="user3", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Group: BinaryAssociation = BinaryAssociation(
    name="User_Group",
    ends={
        Property(name="group4", type=Group, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Registeration: BinaryAssociation = BinaryAssociation(
    name="User_Registeration",
    ends={
        Property(name="registeration6", type=Registrieren, multiplicity=Multiplicity(1, 1)),
        Property(name="user7", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Message: BinaryAssociation = BinaryAssociation(
    name="User_Message",
    ends={
        Property(name="message8", type=_unnamed, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Friends: BinaryAssociation = BinaryAssociation(
    name="User_Friends",
    ends={
        Property(name="friends10", type=Freund, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
User_Hashtag: BinaryAssociation = BinaryAssociation(
    name="User_Hashtag",
    ends={
        Property(name="hashtag12", type=Hashtag, multiplicity=Multiplicity(0, 9999)),
        Property(name="user13", type=Benutzer, multiplicity=Multiplicity(1, 1))
    }
)
Post_public: BinaryAssociation = BinaryAssociation(
    name="Post_public",
    ends={
        Property(name="Post_public_014", type=Ver_ffentlich, multiplicity=Multiplicity(1, 1)),
        Property(name="Post_public_115", type=Beitrag, multiplicity=Multiplicity(1, 1))
    }
)
Post_secret: BinaryAssociation = BinaryAssociation(
    name="Post_secret",
    ends={
        Property(name="Post_secret_016", type=Privat, multiplicity=Multiplicity(1, 1)),
        Property(name="Post_secret_117", type=Beitrag, multiplicity=Multiplicity(1, 1))
    }
)
Kommentare_Post: BinaryAssociation = BinaryAssociation(
    name="Kommentare_Post",
    ends={
        Property(name="Kommentare_Post_018", type=Beitrag, multiplicity=Multiplicity(1, 1)),
        Property(name="Kommentare_Post_119", type=Kommentare, multiplicity=Multiplicity(0, 9999))
    }
)
Group_Beitrag: BinaryAssociation = BinaryAssociation(
    name="Group_Beitrag",
    ends={
        Property(name="Group_Beitrag_020", type=Beitrag, multiplicity=Multiplicity(0, 9999)),
        Property(name="Group_Beitrag_121", type=Group, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JVD6cDxHEeqTDpmqRhKD9Q",
    types={Group, Ver_ffentlich, Privat, _unnamed, Freund, Hashtag, Registrieren, Anmelden, Kommentare, Benutzer, Beitrag},
    associations={User_Post, User_Login, User_Group, User_Registeration, User_Message, User_Friends, User_Hashtag, Post_public, Post_secret, Kommentare_Post, Group_Beitrag},
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