####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, 
)

# Enumerations
Industry: Enumeration = Enumeration(
    name="Industry",
    literals={
            EnumerationLiteral(name="MANUFACTURING"),
			EnumerationLiteral(name="HEALTHCARE"),
			EnumerationLiteral(name="FINANCE"),
			EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="TECHNOLOGY"),
			EnumerationLiteral(name="SERVICES"),
			EnumerationLiteral(name="RETAIL")
    }
)

InteractionType: Enumeration = Enumeration(
    name="InteractionType",
    literals={
            EnumerationLiteral(name="MEETING"),
			EnumerationLiteral(name="EMAIL"),
			EnumerationLiteral(name="CALL"),
			EnumerationLiteral(name="NOTE")
    }
)

LeadScoreLevel: Enumeration = Enumeration(
    name="LeadScoreLevel",
    literals={
            EnumerationLiteral(name="COLD"),
			EnumerationLiteral(name="WARM"),
			EnumerationLiteral(name="HOT")
    }
)

CompanySize: Enumeration = Enumeration(
    name="CompanySize",
    literals={
            EnumerationLiteral(name="STARTUP"),
			EnumerationLiteral(name="ENTERPRISE"),
			EnumerationLiteral(name="LARGE"),
			EnumerationLiteral(name="MEDIUM"),
			EnumerationLiteral(name="SMALL")
    }
)

OpportunityStage: Enumeration = Enumeration(
    name="OpportunityStage",
    literals={
            EnumerationLiteral(name="PROPOSAL"),
			EnumerationLiteral(name="QUALIFICATION"),
			EnumerationLiteral(name="CLOSED_LOST"),
			EnumerationLiteral(name="PROSPECTING"),
			EnumerationLiteral(name="CLOSED_WON"),
			EnumerationLiteral(name="NEGOTIATION")
    }
)

UserRole: Enumeration = Enumeration(
    name="UserRole",
    literals={
            EnumerationLiteral(name="SALES_MANAGER"),
			EnumerationLiteral(name="ADMIN"),
			EnumerationLiteral(name="SALES_REP")
    }
)

InteractionDirection: Enumeration = Enumeration(
    name="InteractionDirection",
    literals={
            EnumerationLiteral(name="INBOUND"),
			EnumerationLiteral(name="OUTBOUND")
    }
)

# Classes
Opportunity = Class(name="Opportunity")
Contact = Class(name="Contact")
Company = Class(name="Company")
User = Class(name="User")
ScoreHistory = Class(name="ScoreHistory")
EnrichmentLog = Class(name="EnrichmentLog")
GeneratedEmail = Class(name="GeneratedEmail")
EmailTemplate = Class(name="EmailTemplate")
Task = Class(name="Task")
Tag = Class(name="Tag")
Interaction = Class(name="Interaction")

# Opportunity class attributes and methods
Opportunity_expected_close_date: Property = Property(name="expected_close_date", type=DateType)
Opportunity_id: Property = Property(name="id", type=IntegerType)
Opportunity_probability: Property = Property(name="probability", type=IntegerType)
Opportunity_value: Property = Property(name="value", type=FloatType)
Opportunity_closed_at: Property = Property(name="closed_at", type=DateTimeType)
Opportunity_stage: Property = Property(name="stage", type=OpportunityStage)
Opportunity_updated_at: Property = Property(name="updated_at", type=DateTimeType)
Opportunity_description: Property = Property(name="description", type=StringType)
Opportunity_created_at: Property = Property(name="created_at", type=DateTimeType)
Opportunity_title: Property = Property(name="title", type=StringType)
Opportunity.attributes={Opportunity_closed_at, Opportunity_created_at, Opportunity_description, Opportunity_expected_close_date, Opportunity_id, Opportunity_probability, Opportunity_stage, Opportunity_title, Opportunity_updated_at, Opportunity_value}

# Contact class attributes and methods
Contact_updated_at: Property = Property(name="updated_at", type=DateTimeType)
Contact_phone: Property = Property(name="phone", type=StringType)
Contact_lead_score_level: Property = Property(name="lead_score_level", type=LeadScoreLevel)
Contact_email: Property = Property(name="email", type=StringType)
Contact_lead_score: Property = Property(name="lead_score", type=IntegerType)
Contact_last_name: Property = Property(name="last_name", type=StringType)
Contact_profile_picture_url: Property = Property(name="profile_picture_url", type=StringType)
Contact_first_name: Property = Property(name="first_name", type=StringType)
Contact_created_at: Property = Property(name="created_at", type=DateTimeType)
Contact_linkedin_url: Property = Property(name="linkedin_url", type=StringType)
Contact_id: Property = Property(name="id", type=IntegerType)
Contact_notes: Property = Property(name="notes", type=StringType)
Contact_job_title: Property = Property(name="job_title", type=StringType)
Contact_is_enriched: Property = Property(name="is_enriched", type=BooleanType)
Contact.attributes={Contact_created_at, Contact_email, Contact_first_name, Contact_id, Contact_is_enriched, Contact_job_title, Contact_last_name, Contact_lead_score, Contact_lead_score_level, Contact_linkedin_url, Contact_notes, Contact_phone, Contact_profile_picture_url, Contact_updated_at}

# Company class attributes and methods
Company_website: Property = Property(name="website", type=StringType)
Company_phone: Property = Property(name="phone", type=StringType)
Company_name: Property = Property(name="name", type=StringType)
Company_created_at: Property = Property(name="created_at", type=DateTimeType)
Company_linkedin_url: Property = Property(name="linkedin_url", type=StringType)
Company_description: Property = Property(name="description", type=StringType)
Company_updated_at: Property = Property(name="updated_at", type=DateTimeType)
Company_id: Property = Property(name="id", type=IntegerType)
Company_country: Property = Property(name="country", type=StringType)
Company_size: Property = Property(name="size", type=CompanySize)
Company_city: Property = Property(name="city", type=StringType)
Company_industry: Property = Property(name="industry", type=Industry)
Company_address: Property = Property(name="address", type=StringType)
Company.attributes={Company_address, Company_city, Company_country, Company_created_at, Company_description, Company_id, Company_industry, Company_linkedin_url, Company_name, Company_phone, Company_size, Company_updated_at, Company_website}

# User class attributes and methods
User_last_name: Property = Property(name="last_name", type=StringType)
User_first_name: Property = Property(name="first_name", type=StringType)
User_password_hash: Property = Property(name="password_hash", type=StringType)
User_last_login: Property = Property(name="last_login", type=DateTimeType)
User_email: Property = Property(name="email", type=StringType)
User_is_active: Property = Property(name="is_active", type=BooleanType)
User_created_at: Property = Property(name="created_at", type=DateTimeType)
User_id: Property = Property(name="id", type=IntegerType)
User_role: Property = Property(name="role", type=UserRole)
User.attributes={User_created_at, User_email, User_first_name, User_id, User_is_active, User_last_login, User_last_name, User_password_hash, User_role}

# ScoreHistory class attributes and methods
ScoreHistory_id: Property = Property(name="id", type=IntegerType)
ScoreHistory_calculated_at: Property = Property(name="calculated_at", type=DateTimeType)
ScoreHistory_reason: Property = Property(name="reason", type=StringType)
ScoreHistory_new_score: Property = Property(name="new_score", type=IntegerType)
ScoreHistory_old_score: Property = Property(name="old_score", type=IntegerType)
ScoreHistory.attributes={ScoreHistory_calculated_at, ScoreHistory_id, ScoreHistory_new_score, ScoreHistory_old_score, ScoreHistory_reason}

# EnrichmentLog class attributes and methods
EnrichmentLog_id: Property = Property(name="id", type=IntegerType)
EnrichmentLog_error_message: Property = Property(name="error_message", type=StringType)
EnrichmentLog_is_successful: Property = Property(name="is_successful", type=BooleanType)
EnrichmentLog_linkedin_url: Property = Property(name="linkedin_url", type=StringType)
EnrichmentLog_enriched_at: Property = Property(name="enriched_at", type=DateTimeType)
EnrichmentLog.attributes={EnrichmentLog_enriched_at, EnrichmentLog_error_message, EnrichmentLog_id, EnrichmentLog_is_successful, EnrichmentLog_linkedin_url}

# GeneratedEmail class attributes and methods
GeneratedEmail_created_at: Property = Property(name="created_at", type=DateTimeType)
GeneratedEmail_sent_at: Property = Property(name="sent_at", type=DateTimeType)
GeneratedEmail_is_sent: Property = Property(name="is_sent", type=BooleanType)#=False)
GeneratedEmail_body: Property = Property(name="body", type=StringType)
GeneratedEmail_subject: Property = Property(name="subject", type=StringType)
GeneratedEmail_id: Property = Property(name="id", type=IntegerType)
GeneratedEmail.attributes={GeneratedEmail_body, GeneratedEmail_created_at, GeneratedEmail_id, GeneratedEmail_is_sent, GeneratedEmail_sent_at, GeneratedEmail_subject}

# EmailTemplate class attributes and methods
EmailTemplate_created_at: Property = Property(name="created_at", type=DateTimeType)
EmailTemplate_category: Property = Property(name="category", type=StringType)
EmailTemplate_body_template: Property = Property(name="body_template", type=StringType)
EmailTemplate_subject_template: Property = Property(name="subject_template", type=StringType)
EmailTemplate_id: Property = Property(name="id", type=IntegerType)
EmailTemplate_name: Property = Property(name="name", type=StringType)
EmailTemplate.attributes={EmailTemplate_body_template, EmailTemplate_category, EmailTemplate_created_at, EmailTemplate_id, EmailTemplate_name, EmailTemplate_subject_template}

# Task class attributes and methods
Task_description: Property = Property(name="description", type=StringType)
Task_due_date: Property = Property(name="due_date", type=DateTimeType)
Task_created_at: Property = Property(name="created_at", type=DateTimeType)
Task_title: Property = Property(name="title", type=StringType)
Task_id: Property = Property(name="id", type=IntegerType)
Task_completed_at: Property = Property(name="completed_at", type=DateTimeType)
Task_is_completed: Property = Property(name="is_completed", type=BooleanType)#=False)
Task.attributes={Task_completed_at, Task_created_at, Task_description, Task_due_date, Task_id, Task_is_completed, Task_title}

# Tag class attributes and methods
Tag_name: Property = Property(name="name", type=StringType)
Tag_color: Property = Property(name="color", type=StringType)#="#3B82F6")
Tag_id: Property = Property(name="id", type=IntegerType)
Tag.attributes={Tag_color, Tag_id, Tag_name}

# Interaction class attributes and methods
Interaction_created_at: Property = Property(name="created_at", type=DateTimeType)
Interaction_subject: Property = Property(name="subject", type=StringType)
Interaction_type: Property = Property(name="type", type=InteractionType)
Interaction_content: Property = Property(name="content", type=StringType)
Interaction_occurred_at: Property = Property(name="occurred_at", type=DateTimeType)
Interaction_id: Property = Property(name="id", type=IntegerType)
Interaction_direction: Property = Property(name="direction", type=InteractionDirection)
Interaction.attributes={Interaction_content, Interaction_created_at, Interaction_direction, Interaction_id, Interaction_occurred_at, Interaction_subject, Interaction_type}

# Relationships
template_user: BinaryAssociation = BinaryAssociation(
    name="template_user",
    ends={
        Property(name="email_templates", type=EmailTemplate, multiplicity=Multiplicity(0, 9999)),
        Property(name="created_by", type=User, multiplicity=Multiplicity(1, 1))
    }
)
contact_company: BinaryAssociation = BinaryAssociation(
    name="contact_company",
    ends={
        Property(name="contacts", type=Contact, multiplicity=Multiplicity(0, 9999)),
        Property(name="company", type=Company, multiplicity=Multiplicity(0, 1))
    }
)
task_opportunity: BinaryAssociation = BinaryAssociation(
    name="task_opportunity",
    ends={
        Property(name="tasks", type=Task, multiplicity=Multiplicity(0, 9999)),
        Property(name="opportunity", type=Opportunity, multiplicity=Multiplicity(0, 1))
    }
)
contact_created_by: BinaryAssociation = BinaryAssociation(
    name="contact_created_by",
    ends={
        Property(name="created_by", type=User, multiplicity=Multiplicity(1, 1)),
        Property(name="created_contacts", type=Contact, multiplicity=Multiplicity(0, 9999))
    }
)
opportunity_owner: BinaryAssociation = BinaryAssociation(
    name="opportunity_owner",
    ends={
        Property(name="owned_opportunities", type=Opportunity, multiplicity=Multiplicity(0, 9999)),
        Property(name="owner", type=User, multiplicity=Multiplicity(1, 1))
    }
)
contact_tag: BinaryAssociation = BinaryAssociation(
    name="contact_tag",
    ends={
        Property(name="tagged_contacts", type=Contact, multiplicity=Multiplicity(0, 9999)),
        Property(name="tags", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
opportunity_contact: BinaryAssociation = BinaryAssociation(
    name="opportunity_contact",
    ends={
        Property(name="contacts", type=Contact, multiplicity=Multiplicity(1, 9999)),
        Property(name="opportunities", type=Opportunity, multiplicity=Multiplicity(0, 9999))
    }
)
email_template_link: BinaryAssociation = BinaryAssociation(
    name="email_template_link",
    ends={
        Property(name="template", type=EmailTemplate, multiplicity=Multiplicity(0, 1)),
        Property(name="generated_emails", type=GeneratedEmail, multiplicity=Multiplicity(0, 9999))
    }
)
email_contact: BinaryAssociation = BinaryAssociation(
    name="email_contact",
    ends={
        Property(name="contact", type=Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="generated_emails", type=GeneratedEmail, multiplicity=Multiplicity(0, 9999))
    }
)
task_contact: BinaryAssociation = BinaryAssociation(
    name="task_contact",
    ends={
        Property(name="contact", type=Contact, multiplicity=Multiplicity(0, 1)),
        Property(name="tasks", type=Task, multiplicity=Multiplicity(0, 9999))
    }
)
company_created_by: BinaryAssociation = BinaryAssociation(
    name="company_created_by",
    ends={
        Property(name="created_companies", type=Company, multiplicity=Multiplicity(0, 9999)),
        Property(name="created_by", type=User, multiplicity=Multiplicity(1, 1))
    }
)
score_contact: BinaryAssociation = BinaryAssociation(
    name="score_contact",
    ends={
        Property(name="score_history", type=ScoreHistory, multiplicity=Multiplicity(0, 9999)),
        Property(name="contact", type=Contact, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interaction_contact: BinaryAssociation = BinaryAssociation(
    name="interaction_contact",
    ends={
        Property(name="interactions", type=Interaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="contact", type=Contact, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
opportunity_company: BinaryAssociation = BinaryAssociation(
    name="opportunity_company",
    ends={
        Property(name="company", type=Company, multiplicity=Multiplicity(0, 1)),
        Property(name="opportunities", type=Opportunity, multiplicity=Multiplicity(0, 9999))
    }
)
company_tag: BinaryAssociation = BinaryAssociation(
    name="company_tag",
    ends={
        Property(name="tagged_companies", type=Company, multiplicity=Multiplicity(0, 9999)),
        Property(name="tags", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
email_user: BinaryAssociation = BinaryAssociation(
    name="email_user",
    ends={
        Property(name="generated_emails", type=GeneratedEmail, multiplicity=Multiplicity(0, 9999)),
        Property(name="created_by", type=User, multiplicity=Multiplicity(1, 1))
    }
)
interaction_user: BinaryAssociation = BinaryAssociation(
    name="interaction_user",
    ends={
        Property(name="interactions", type=Interaction, multiplicity=Multiplicity(0, 9999)),
        Property(name="performed_by", type=User, multiplicity=Multiplicity(1, 1))
    }
)
task_user: BinaryAssociation = BinaryAssociation(
    name="task_user",
    ends={
        Property(name="tasks", type=Task, multiplicity=Multiplicity(0, 9999)),
        Property(name="assigned_to", type=User, multiplicity=Multiplicity(1, 1))
    }
)
enrichment_contact: BinaryAssociation = BinaryAssociation(
    name="enrichment_contact",
    ends={
        Property(name="contact", type=Contact, multiplicity=Multiplicity(1, 1)),
        Property(name="enrichment_logs", type=EnrichmentLog, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="NexaCRM",
    types={Opportunity, Contact, Company, User, ScoreHistory, EnrichmentLog, GeneratedEmail, EmailTemplate, Task, Tag, Interaction, Industry, InteractionType, LeadScoreLevel, CompanySize, OpportunityStage, UserRole, InteractionDirection},
    associations={template_user, contact_company, task_opportunity, contact_created_by, opportunity_owner, contact_tag, opportunity_contact, email_template_link, email_contact, task_contact, company_created_by, score_contact, interaction_contact, opportunity_company, company_tag, email_user, interaction_user, task_user, enrichment_contact},
    generalizations={},
    metadata=None
)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="New project")
project = Project(
    name="sampleModel",
    models=[domain_model],
    owner="User",
    metadata=metadata
)
