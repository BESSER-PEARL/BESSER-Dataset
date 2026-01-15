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
message_Message = Class(name="message::Message")
message_Translation = Class(name="message::Translation")
message_MessageLibrary = Class(name="message::MessageLibrary")
Categorized = Class(name="Categorized")
message_Language = Class(name="message::Language")

# message_Message class attributes and methods
message_Message_uid: Property = Property(name="uid", type=StringType)
message_Message_name: Property = Property(name="name", type=StringType)
message_Message.attributes={message_Message_name, message_Message_uid}

# message_Translation class attributes and methods
message_Translation_uid: Property = Property(name="uid", type=StringType)
message_Translation_translation: Property = Property(name="translation", type=StringType)
message_Translation.attributes={message_Translation_uid, message_Translation_translation}

# message_MessageLibrary class attributes and methods
message_MessageLibrary_name: Property = Property(name="name", type=StringType)
message_MessageLibrary_uid: Property = Property(name="uid", type=StringType)
message_MessageLibrary.attributes={message_MessageLibrary_uid, message_MessageLibrary_name}

# Categorized class attributes and methods

# message_Language class attributes and methods
message_Language_defaultLang: Property = Property(name="defaultLang", type=BooleanType)
message_Language_uid: Property = Property(name="uid", type=StringType)
message_Language_lang: Property = Property(name="lang", type=StringType)
message_Language_code: Property = Property(name="code", type=StringType)
message_Language.attributes={message_Language_uid, message_Language_defaultLang, message_Language_code, message_Language_lang}

# Relationships
messages0: BinaryAssociation = BinaryAssociation(
    name="messages0",
    ends={
        Property(name="message_Message", type=message_MessageLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="message_MessageLibrary", type=message_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
translatioins1: BinaryAssociation = BinaryAssociation(
    name="translatioins1",
    ends={
        Property(name="message_Translation", type=message_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="message_Message2", type=message_Translation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lang3: BinaryAssociation = BinaryAssociation(
    name="lang3",
    ends={
        Property(name="message_Language", type=message_Translation, multiplicity=Multiplicity(1, 1)),
        Property(name="message_Translation4", type=message_Language, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_message_MessageLibrary_Categorized = Generalization(general=Categorized, specific=message_MessageLibrary)

# Domain Model
domain_model = DomainModel(
    name="message",
    types={message_Message, message_Translation, message_MessageLibrary, Categorized, message_Language},
    associations={messages0, translatioins1, lang3},
    generalizations={gen_message_MessageLibrary_Categorized},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)