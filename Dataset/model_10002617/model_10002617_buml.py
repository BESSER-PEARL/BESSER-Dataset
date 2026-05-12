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
Pet = Class(name="Pet")
User = Class(name="User")
Organization = Class(name="Organization")
User_Actor = Class(name="User_Actor")
Administrator_Actor = Class(name="Administrator_Actor")
Medeina = Class(name="Medeina")
Registering_into_program_UseCase = Class(name="Registering_into_program_UseCase")
Logging_into_program_UseCase = Class(name="Logging_into_program_UseCase")
Report_a_pet_situation_UseCase = Class(name="Report_a_pet_situation_UseCase")
Search_UseCase = Class(name="Search_UseCase")
Registering_UseCase = Class(name="Registering_UseCase")
Register_as_an_adopter_UseCase = Class(name="Register_as_an_adopter_UseCase")
Qualify_an_pet_owner_UseCase = Class(name="Qualify_an_pet_owner_UseCase")
Donate_UseCase = Class(name="Donate_UseCase")
Report_a_person_to_the_blacklist_UseCase = Class(name="Report_a_person_to_the_blacklist_UseCase")
Report_a_lost_pet_UseCase = Class(name="Report_a_lost_pet_UseCase")
Report_a_found_pet_UseCase = Class(name="Report_a_found_pet_UseCase")
Register_a_pet_UseCase = Class(name="Register_a_pet_UseCase")
Edit_information_UseCase = Class(name="Edit_information_UseCase")
Edit_user_information_UseCase = Class(name="Edit_user_information_UseCase")
Edit_pet_information_UseCase = Class(name="Edit_pet_information_UseCase")
Report_an_adopted_pet_UseCase = Class(name="Report_an_adopted_pet_UseCase")
Register_as_a_pro_care_association_UseCase = Class(name="Register_as_a_pro_care_association_UseCase")
Search_for_lost_pets_UseCase = Class(name="Search_for_lost_pets_UseCase")
Search_for_donations_per_user_UseCase = Class(name="Search_for_donations_per_user_UseCase")
Search_for_total_cash_donated_per_association_UseCase = Class(name="Search_for_total_cash_donated_per_association_UseCase")
Register_as_a_cradle_home_UseCase = Class(name="Register_as_a_cradle_home_UseCase")
Register_pet_races_UseCase = Class(name="Register_pet_races_UseCase")
Check_black_list_requests_UseCase = Class(name="Check_black_list_requests_UseCase")
System_Actor = Class(name="System_Actor")
Publish_on_social_networks_UseCase = Class(name="Publish_on_social_networks_UseCase")
Create_reports_UseCase = Class(name="Create_reports_UseCase")
Match_lost_pet_cases_UseCase = Class(name="Match_lost_pet_cases_UseCase")
Send_mail_to_lost_pet_owners_UseCase = Class(name="Send_mail_to_lost_pet_owners_UseCase")
Register_pet_types_UseCase = Class(name="Register_pet_types_UseCase")
Make_requests_to_administrator_UseCase = Class(name="Make_requests_to_administrator_UseCase")
Register_pets__physical_characteristics_UseCase = Class(name="Register_pets__physical_characteristics_UseCase")
Logging_into_program_UseCase1 = Class(name="Logging_into_program_UseCase1")
Create_new_administrators_UseCase = Class(name="Create_new_administrators_UseCase")
Search_for_registered_associations_UseCase = Class(name="Search_for_registered_associations_UseCase")
Search_for_registered_cradle_homes_UseCase = Class(name="Search_for_registered_cradle_homes_UseCase")
Donate_to_an_user_UseCase = Class(name="Donate_to_an_user_UseCase")
Donate_to_an_association_UseCase = Class(name="Donate_to_an_association_UseCase")
Donate_to_a_cradle_home_UseCase = Class(name="Donate_to_a_cradle_home_UseCase")

# Pet class attributes and methods
Pet_type: Property = Property(name="type", type=StringType)
Pet_breed: Property = Property(name="breed", type=StringType)
Pet_name: Property = Property(name="name", type=StringType)
Pet_chipID: Property = Property(name="chipID", type=StringType)
Pet_color: Property = Property(name="color", type=StringType)
Pet_picture: Property = Property(name="picture", type=StringType)
Pet_phone: Property = Property(name="phone", type=StringType)
Pet_email: Property = Property(name="email", type=StringType)
Pet_stray: Property = Property(name="stray", type=BooleanType)
Pet_place: Property = Property(name="place", type=StringType)
Pet_date: Property = Property(name="date", type=DateType)
Pet_reward: Property = Property(name="reward", type=IntegerType)
Pet_notes: Property = Property(name="notes", type=StringType)
Pet_state: Property = Property(name="state", type=StringType)
Pet.attributes={Pet_reward, Pet_name, Pet_stray, Pet_phone, Pet_color, Pet_date, Pet_state, Pet_notes, Pet_picture, Pet_type, Pet_email, Pet_place, Pet_breed, Pet_chipID}

# User class attributes and methods
User_name: Property = Property(name="name", type=StringType)
User_lastName: Property = Property(name="lastName", type=StringType)
User.attributes={User_lastName, User_name}

# Organization class attributes and methods
Organization_name: Property = Property(name="name", type=StringType)
Organization.attributes={Organization_name}

# User_Actor class attributes and methods

# Administrator_Actor class attributes and methods

# Medeina class attributes and methods
Medeina_attribute: Property = Property(name="attribute", type=StringType)
Medeina_blackList_User_: Property = Property(name="blackList_User_", type=User)
Medeina.attributes={Medeina_attribute, Medeina_blackList_User_}

# Registering_into_program_UseCase class attributes and methods

# Logging_into_program_UseCase class attributes and methods

# Report_a_pet_situation_UseCase class attributes and methods

# Search_UseCase class attributes and methods

# Registering_UseCase class attributes and methods

# Register_as_an_adopter_UseCase class attributes and methods

# Qualify_an_pet_owner_UseCase class attributes and methods

# Donate_UseCase class attributes and methods

# Report_a_person_to_the_blacklist_UseCase class attributes and methods

# Report_a_lost_pet_UseCase class attributes and methods

# Report_a_found_pet_UseCase class attributes and methods

# Register_a_pet_UseCase class attributes and methods

# Edit_information_UseCase class attributes and methods

# Edit_user_information_UseCase class attributes and methods

# Edit_pet_information_UseCase class attributes and methods

# Report_an_adopted_pet_UseCase class attributes and methods

# Register_as_a_pro_care_association_UseCase class attributes and methods

# Search_for_lost_pets_UseCase class attributes and methods

# Search_for_donations_per_user_UseCase class attributes and methods

# Search_for_total_cash_donated_per_association_UseCase class attributes and methods

# Register_as_a_cradle_home_UseCase class attributes and methods

# Register_pet_races_UseCase class attributes and methods

# Check_black_list_requests_UseCase class attributes and methods

# System_Actor class attributes and methods

# Publish_on_social_networks_UseCase class attributes and methods

# Create_reports_UseCase class attributes and methods

# Match_lost_pet_cases_UseCase class attributes and methods

# Send_mail_to_lost_pet_owners_UseCase class attributes and methods

# Register_pet_types_UseCase class attributes and methods

# Make_requests_to_administrator_UseCase class attributes and methods

# Register_pets__physical_characteristics_UseCase class attributes and methods

# Logging_into_program_UseCase1 class attributes and methods

# Create_new_administrators_UseCase class attributes and methods

# Search_for_registered_associations_UseCase class attributes and methods

# Search_for_registered_cradle_homes_UseCase class attributes and methods

# Donate_to_an_user_UseCase class attributes and methods

# Donate_to_an_association_UseCase class attributes and methods

# Donate_to_a_cradle_home_UseCase class attributes and methods

# Relationships
Medeina_Create_reports: BinaryAssociation = BinaryAssociation(
    name="Medeina_Create_reports",
    ends={
        Property(name="medeina7", type=System_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_reports6", type=Create_reports_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Medeina_Match_lost_pet_cases: BinaryAssociation = BinaryAssociation(
    name="Medeina_Match_lost_pet_cases",
    ends={
        Property(name="match_lost_pet_cases8", type=Match_lost_pet_cases_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medeina9", type=System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medeina_Send_mail_to_lost_pet_owners: BinaryAssociation = BinaryAssociation(
    name="Medeina_Send_mail_to_lost_pet_owners",
    ends={
        Property(name="send_mail_to_lost_pet_owners10", type=Send_mail_to_lost_pet_owners_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medeina11", type=System_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Make_requests_to_administrator_Administrator: BinaryAssociation = BinaryAssociation(
    name="Make_requests_to_administrator_Administrator",
    ends={
        Property(name="administrator12", type=Administrator_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="make_requests_to_administrator13", type=Make_requests_to_administrator_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
User_Send_mail_to_lost_pet_owners: BinaryAssociation = BinaryAssociation(
    name="User_Send_mail_to_lost_pet_owners",
    ends={
        Property(name="send_mail_to_lost_pet_owners14", type=Send_mail_to_lost_pet_owners_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user15", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Logging_into_program: BinaryAssociation = BinaryAssociation(
    name="Administrator_Logging_into_program",
    ends={
        Property(name="logging_into_program16", type=Logging_into_program_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Logging_into_program_Register_pets__physical_characteristics: BinaryAssociation = BinaryAssociation(
    name="Logging_into_program_Register_pets__physical_characteristics",
    ends={
        Property(name="register_pets__physical_characteristics18", type=Register_pets__physical_characteristics_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="logging_into_program19", type=Logging_into_program_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Logging_into_program_Check_black_list_requests: BinaryAssociation = BinaryAssociation(
    name="Logging_into_program_Check_black_list_requests",
    ends={
        Property(name="check_black_list_requests20", type=Check_black_list_requests_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="logging_into_program21", type=Logging_into_program_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
Logging_into_program_Create_new_administrators: BinaryAssociation = BinaryAssociation(
    name="Logging_into_program_Create_new_administrators",
    ends={
        Property(name="create_new_administrators22", type=Create_new_administrators_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="logging_into_program23", type=Logging_into_program_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
User_Registering_into_program: BinaryAssociation = BinaryAssociation(
    name="User_Registering_into_program",
    ends={
        Property(name="registering_into_program0", type=Registering_into_program_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Logging_into_program: BinaryAssociation = BinaryAssociation(
    name="User_Logging_into_program",
    ends={
        Property(name="logging_into_program2", type=Logging_into_program_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Medeina_Publish_on_social_networks: BinaryAssociation = BinaryAssociation(
    name="Medeina_Publish_on_social_networks",
    ends={
        Property(name="publish_on_social_networks4", type=Publish_on_social_networks_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="medeina5", type=System_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c7635f0a_1a15_40fa_9a9b_60117bc1924f",
    types={Pet, User, Organization, User_Actor, Administrator_Actor, Medeina, Registering_into_program_UseCase, Logging_into_program_UseCase, Report_a_pet_situation_UseCase, Search_UseCase, Registering_UseCase, Register_as_an_adopter_UseCase, Qualify_an_pet_owner_UseCase, Donate_UseCase, Report_a_person_to_the_blacklist_UseCase, Report_a_lost_pet_UseCase, Report_a_found_pet_UseCase, Register_a_pet_UseCase, Edit_information_UseCase, Edit_user_information_UseCase, Edit_pet_information_UseCase, Report_an_adopted_pet_UseCase, Register_as_a_pro_care_association_UseCase, Search_for_lost_pets_UseCase, Search_for_donations_per_user_UseCase, Search_for_total_cash_donated_per_association_UseCase, Register_as_a_cradle_home_UseCase, Register_pet_races_UseCase, Check_black_list_requests_UseCase, System_Actor, Publish_on_social_networks_UseCase, Create_reports_UseCase, Match_lost_pet_cases_UseCase, Send_mail_to_lost_pet_owners_UseCase, Register_pet_types_UseCase, Make_requests_to_administrator_UseCase, Register_pets__physical_characteristics_UseCase, Logging_into_program_UseCase1, Create_new_administrators_UseCase, Search_for_registered_associations_UseCase, Search_for_registered_cradle_homes_UseCase, Donate_to_an_user_UseCase, Donate_to_an_association_UseCase, Donate_to_a_cradle_home_UseCase},
    associations={Medeina_Create_reports, Medeina_Match_lost_pet_cases, Medeina_Send_mail_to_lost_pet_owners, Make_requests_to_administrator_Administrator, User_Send_mail_to_lost_pet_owners, Administrator_Logging_into_program, Logging_into_program_Register_pets__physical_characteristics, Logging_into_program_Check_black_list_requests, Logging_into_program_Create_new_administrators, User_Registering_into_program, User_Logging_into_program, Medeina_Publish_on_social_networks},
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