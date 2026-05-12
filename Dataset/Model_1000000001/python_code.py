from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class InteractionDirection(Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"
class CompanySize(Enum):
    STARTUP = "STARTUP"
    ENTERPRISE = "ENTERPRISE"
    LARGE = "LARGE"
    MEDIUM = "MEDIUM"
    SMALL = "SMALL"
class InteractionType(Enum):
    MEETING = "MEETING"
    EMAIL = "EMAIL"
    CALL = "CALL"
    NOTE = "NOTE"
class UserRole(Enum):
    SALES_MANAGER = "SALES_MANAGER"
    ADMIN = "ADMIN"
    SALES_REP = "SALES_REP"
class OpportunityStage(Enum):
    PROPOSAL = "PROPOSAL"
    QUALIFICATION = "QUALIFICATION"
    CLOSED_LOST = "CLOSED_LOST"
    PROSPECTING = "PROSPECTING"
    CLOSED_WON = "CLOSED_WON"
    NEGOTIATION = "NEGOTIATION"
class Industry(Enum):
    MANUFACTURING = "MANUFACTURING"
    HEALTHCARE = "HEALTHCARE"
    FINANCE = "FINANCE"
    OTHER = "OTHER"
    TECHNOLOGY = "TECHNOLOGY"
    SERVICES = "SERVICES"
    RETAIL = "RETAIL"
class LeadScoreLevel(Enum):
    COLD = "COLD"
    WARM = "WARM"
    HOT = "HOT"

############################################
# Definition of Classes
############################################










class Interaction:

    def __init__(self, created_at: datetime, subject: str, type: InteractionType, content: str, occurred_at: datetime, id: int, direction: InteractionDirection, contact: "Contact" = None, performed_by: "User" = None):
        self.created_at = created_at
        self.subject = subject
        self.type = type
        self.content = content
        self.occurred_at = occurred_at
        self.id = id
        self.direction = direction
        self.contact = contact
        self.performed_by = performed_by
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: InteractionType):
        self.__type = type

    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def occurred_at(self):
        return self.__occurred_at
    @occurred_at.setter
    def occurred_at(self, occurred_at: datetime):
        self.__occurred_at = occurred_at

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: InteractionDirection):
        self.__direction = direction

    @property
    def performed_by(self):
        return self.__performed_by
    @performed_by.setter
    def performed_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Interaction__performed_by", None)
        self.__performed_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interactions"):
                opp_val = getattr(old_value, "interactions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interactions"):
                opp_val = getattr(value, "interactions", None)
                if opp_val is None:
                    setattr(value, "interactions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Interaction__contact", None)
        self.__contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interactions"):
                opp_val = getattr(old_value, "interactions", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interactions"):
                opp_val = getattr(value, "interactions", None)
                if opp_val is None:
                    setattr(value, "interactions", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Tag:

    def __init__(self, name: str, color: str, id: int, tagged_contacts: set["Contact"] = None, tagged_companies: set["Company"] = None):
        self.name = name
        self.color = color
        self.id = id
        self.tagged_contacts = tagged_contacts if tagged_contacts is not None else set()
        self.tagged_companies = tagged_companies if tagged_companies is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tagged_companies(self):
        return self.__tagged_companies
    @tagged_companies.setter
    def tagged_companies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tag__tagged_companies", None)
        self.__tagged_companies = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tags"):
                    opp_val = getattr(item, "tags", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tags"):
                    opp_val = getattr(item, "tags", None)
                    
                    if opp_val is None:
                        setattr(item, "tags", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def tagged_contacts(self):
        return self.__tagged_contacts
    @tagged_contacts.setter
    def tagged_contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Tag__tagged_contacts", None)
        self.__tagged_contacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tags"):
                    opp_val = getattr(item, "tags", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tags"):
                    opp_val = getattr(item, "tags", None)
                    
                    if opp_val is None:
                        setattr(item, "tags", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Task:

    def __init__(self, description: str, due_date: datetime, created_at: datetime, title: str, id: int, completed_at: datetime, is_completed: bool, opportunity: "Opportunity" = None, contact: "Contact" = None, assigned_to: "User" = None):
        self.description = description
        self.due_date = due_date
        self.created_at = created_at
        self.title = title
        self.id = id
        self.completed_at = completed_at
        self.is_completed = is_completed
        self.opportunity = opportunity
        self.contact = contact
        self.assigned_to = assigned_to
        
        pass
    @property
    def due_date(self):
        return self.__due_date
    @due_date.setter
    def due_date(self, due_date: datetime):
        self.__due_date = due_date

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def completed_at(self):
        return self.__completed_at
    @completed_at.setter
    def completed_at(self, completed_at: datetime):
        self.__completed_at = completed_at

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def is_completed(self):
        return self.__is_completed
    @is_completed.setter
    def is_completed(self, is_completed: bool):
        self.__is_completed = is_completed

    @property
    def assigned_to(self):
        return self.__assigned_to
    @assigned_to.setter
    def assigned_to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task__assigned_to", None)
        self.__assigned_to = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks"):
                opp_val = getattr(old_value, "tasks", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks"):
                opp_val = getattr(value, "tasks", None)
                if opp_val is None:
                    setattr(value, "tasks", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def opportunity(self):
        return self.__opportunity
    @opportunity.setter
    def opportunity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task__opportunity", None)
        self.__opportunity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks"):
                opp_val = getattr(old_value, "tasks", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks"):
                opp_val = getattr(value, "tasks", None)
                if opp_val is None:
                    setattr(value, "tasks", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Task__contact", None)
        self.__contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tasks"):
                opp_val = getattr(old_value, "tasks", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tasks"):
                opp_val = getattr(value, "tasks", None)
                if opp_val is None:
                    setattr(value, "tasks", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class EmailTemplate:

    def __init__(self, created_at: datetime, category: str, body_template: str, subject_template: str, id: int, name: str, created_by: "User" = None, generated_emails: set["GeneratedEmail"] = None):
        self.created_at = created_at
        self.category = category
        self.body_template = body_template
        self.subject_template = subject_template
        self.id = id
        self.name = name
        self.created_by = created_by
        self.generated_emails = generated_emails if generated_emails is not None else set()
        
        pass
    @property
    def body_template(self):
        return self.__body_template
    @body_template.setter
    def body_template(self, body_template: str):
        self.__body_template = body_template

    @property
    def subject_template(self):
        return self.__subject_template
    @subject_template.setter
    def subject_template(self, subject_template: str):
        self.__subject_template = subject_template

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def created_by(self):
        return self.__created_by
    @created_by.setter
    def created_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmailTemplate__created_by", None)
        self.__created_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "email_templates"):
                opp_val = getattr(old_value, "email_templates", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "email_templates"):
                opp_val = getattr(value, "email_templates", None)
                if opp_val is None:
                    setattr(value, "email_templates", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generated_emails(self):
        return self.__generated_emails
    @generated_emails.setter
    def generated_emails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EmailTemplate__generated_emails", None)
        self.__generated_emails = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "template"):
                    opp_val = getattr(item, "template", None)
                    
                    if opp_val == self:
                        setattr(item, "template", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "template"):
                    opp_val = getattr(item, "template", None)
                    
                    setattr(item, "template", self)
                    



class GeneratedEmail:

    def __init__(self, created_at: datetime, sent_at: datetime, is_sent: bool, body: str, subject: str, id: int, template: "EmailTemplate" = None, contact: "Contact" = None, created_by: "User" = None):
        self.created_at = created_at
        self.sent_at = sent_at
        self.is_sent = is_sent
        self.body = body
        self.subject = subject
        self.id = id
        self.template = template
        self.contact = contact
        self.created_by = created_by
        
        pass
    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def subject(self):
        return self.__subject
    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def sent_at(self):
        return self.__sent_at
    @sent_at.setter
    def sent_at(self, sent_at: datetime):
        self.__sent_at = sent_at

    @property
    def is_sent(self):
        return self.__is_sent
    @is_sent.setter
    def is_sent(self, is_sent: bool):
        self.__is_sent = is_sent

    @property
    def created_by(self):
        return self.__created_by
    @created_by.setter
    def created_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GeneratedEmail__created_by", None)
        self.__created_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generated_emails"):
                opp_val = getattr(old_value, "generated_emails", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generated_emails"):
                opp_val = getattr(value, "generated_emails", None)
                if opp_val is None:
                    setattr(value, "generated_emails", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def template(self):
        return self.__template
    @template.setter
    def template(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GeneratedEmail__template", None)
        self.__template = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generated_emails"):
                opp_val = getattr(old_value, "generated_emails", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generated_emails"):
                opp_val = getattr(value, "generated_emails", None)
                if opp_val is None:
                    setattr(value, "generated_emails", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GeneratedEmail__contact", None)
        self.__contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generated_emails"):
                opp_val = getattr(old_value, "generated_emails", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generated_emails"):
                opp_val = getattr(value, "generated_emails", None)
                if opp_val is None:
                    setattr(value, "generated_emails", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class EnrichmentLog:

    def __init__(self, id: int, error_message: str, is_successful: bool, linkedin_url: str, enriched_at: datetime, contact: "Contact" = None):
        self.id = id
        self.error_message = error_message
        self.is_successful = is_successful
        self.linkedin_url = linkedin_url
        self.enriched_at = enriched_at
        self.contact = contact
        
        pass
    @property
    def linkedin_url(self):
        return self.__linkedin_url
    @linkedin_url.setter
    def linkedin_url(self, linkedin_url: str):
        self.__linkedin_url = linkedin_url

    @property
    def enriched_at(self):
        return self.__enriched_at
    @enriched_at.setter
    def enriched_at(self, enriched_at: datetime):
        self.__enriched_at = enriched_at

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def error_message(self):
        return self.__error_message
    @error_message.setter
    def error_message(self, error_message: str):
        self.__error_message = error_message

    @property
    def is_successful(self):
        return self.__is_successful
    @is_successful.setter
    def is_successful(self, is_successful: bool):
        self.__is_successful = is_successful

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EnrichmentLog__contact", None)
        self.__contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enrichment_logs"):
                opp_val = getattr(old_value, "enrichment_logs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enrichment_logs"):
                opp_val = getattr(value, "enrichment_logs", None)
                if opp_val is None:
                    setattr(value, "enrichment_logs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ScoreHistory:

    def __init__(self, id: int, calculated_at: datetime, reason: str, new_score: int, old_score: int, contact: "Contact" = None):
        self.id = id
        self.calculated_at = calculated_at
        self.reason = reason
        self.new_score = new_score
        self.old_score = old_score
        self.contact = contact
        
        pass
    @property
    def new_score(self):
        return self.__new_score
    @new_score.setter
    def new_score(self, new_score: int):
        self.__new_score = new_score

    @property
    def old_score(self):
        return self.__old_score
    @old_score.setter
    def old_score(self, old_score: int):
        self.__old_score = old_score

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def calculated_at(self):
        return self.__calculated_at
    @calculated_at.setter
    def calculated_at(self, calculated_at: datetime):
        self.__calculated_at = calculated_at

    @property
    def reason(self):
        return self.__reason
    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ScoreHistory__contact", None)
        self.__contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "score_history"):
                opp_val = getattr(old_value, "score_history", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "score_history"):
                opp_val = getattr(value, "score_history", None)
                if opp_val is None:
                    setattr(value, "score_history", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, last_name: str, first_name: str, password_hash: str, last_login: datetime, email: str, is_active: bool, created_at: datetime, id: int, role: UserRole, email_templates: set["EmailTemplate"] = None, created_contacts: set["Contact"] = None, owned_opportunities: set["Opportunity"] = None, created_companies: set["Company"] = None, generated_emails: set["GeneratedEmail"] = None, interactions: set["Interaction"] = None, tasks: set["Task"] = None):
        self.last_name = last_name
        self.first_name = first_name
        self.password_hash = password_hash
        self.last_login = last_login
        self.email = email
        self.is_active = is_active
        self.created_at = created_at
        self.id = id
        self.role = role
        self.email_templates = email_templates if email_templates is not None else set()
        self.created_contacts = created_contacts if created_contacts is not None else set()
        self.owned_opportunities = owned_opportunities if owned_opportunities is not None else set()
        self.created_companies = created_companies if created_companies is not None else set()
        self.generated_emails = generated_emails if generated_emails is not None else set()
        self.interactions = interactions if interactions is not None else set()
        self.tasks = tasks if tasks is not None else set()
        
        pass
    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def password_hash(self):
        return self.__password_hash
    @password_hash.setter
    def password_hash(self, password_hash: str):
        self.__password_hash = password_hash

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: UserRole):
        self.__role = role

    @property
    def last_login(self):
        return self.__last_login
    @last_login.setter
    def last_login(self, last_login: datetime):
        self.__last_login = last_login

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def is_active(self):
        return self.__is_active
    @is_active.setter
    def is_active(self, is_active: bool):
        self.__is_active = is_active

    @property
    def created_contacts(self):
        return self.__created_contacts
    @created_contacts.setter
    def created_contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__created_contacts", None)
        self.__created_contacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    if opp_val == self:
                        setattr(item, "created_by", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    setattr(item, "created_by", self)
                    

    @property
    def tasks(self):
        return self.__tasks
    @tasks.setter
    def tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__tasks", None)
        self.__tasks = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assigned_to"):
                    opp_val = getattr(item, "assigned_to", None)
                    
                    if opp_val == self:
                        setattr(item, "assigned_to", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assigned_to"):
                    opp_val = getattr(item, "assigned_to", None)
                    
                    setattr(item, "assigned_to", self)
                    

    @property
    def interactions(self):
        return self.__interactions
    @interactions.setter
    def interactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__interactions", None)
        self.__interactions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "performed_by"):
                    opp_val = getattr(item, "performed_by", None)
                    
                    if opp_val == self:
                        setattr(item, "performed_by", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "performed_by"):
                    opp_val = getattr(item, "performed_by", None)
                    
                    setattr(item, "performed_by", self)
                    

    @property
    def generated_emails(self):
        return self.__generated_emails
    @generated_emails.setter
    def generated_emails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__generated_emails", None)
        self.__generated_emails = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    if opp_val == self:
                        setattr(item, "created_by", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    setattr(item, "created_by", self)
                    

    @property
    def email_templates(self):
        return self.__email_templates
    @email_templates.setter
    def email_templates(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__email_templates", None)
        self.__email_templates = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    if opp_val == self:
                        setattr(item, "created_by", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    setattr(item, "created_by", self)
                    

    @property
    def created_companies(self):
        return self.__created_companies
    @created_companies.setter
    def created_companies(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__created_companies", None)
        self.__created_companies = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    if opp_val == self:
                        setattr(item, "created_by", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "created_by"):
                    opp_val = getattr(item, "created_by", None)
                    
                    setattr(item, "created_by", self)
                    

    @property
    def owned_opportunities(self):
        return self.__owned_opportunities
    @owned_opportunities.setter
    def owned_opportunities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__owned_opportunities", None)
        self.__owned_opportunities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "owner"):
                    opp_val = getattr(item, "owner", None)
                    
                    if opp_val == self:
                        setattr(item, "owner", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "owner"):
                    opp_val = getattr(item, "owner", None)
                    
                    setattr(item, "owner", self)
                    



class Company:

    def __init__(self, website: str, phone: str, name: str, created_at: datetime, linkedin_url: str, description: str, updated_at: datetime, id: int, country: str, size: CompanySize, city: str, industry: Industry, address: str, contacts: set["Contact"] = None, created_by: "User" = None, opportunities: set["Opportunity"] = None, tags: set["Tag"] = None):
        self.website = website
        self.phone = phone
        self.name = name
        self.created_at = created_at
        self.linkedin_url = linkedin_url
        self.description = description
        self.updated_at = updated_at
        self.id = id
        self.country = country
        self.size = size
        self.city = city
        self.industry = industry
        self.address = address
        self.contacts = contacts if contacts is not None else set()
        self.created_by = created_by
        self.opportunities = opportunities if opportunities is not None else set()
        self.tags = tags if tags is not None else set()
        
        pass
    @property
    def linkedin_url(self):
        return self.__linkedin_url
    @linkedin_url.setter
    def linkedin_url(self, linkedin_url: str):
        self.__linkedin_url = linkedin_url

    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def industry(self):
        return self.__industry
    @industry.setter
    def industry(self, industry: Industry):
        self.__industry = industry

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def updated_at(self):
        return self.__updated_at
    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        self.__updated_at = updated_at

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: CompanySize):
        self.__size = size

    @property
    def opportunities(self):
        return self.__opportunities
    @opportunities.setter
    def opportunities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company__opportunities", None)
        self.__opportunities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company"):
                    opp_val = getattr(item, "company", None)
                    
                    if opp_val == self:
                        setattr(item, "company", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company"):
                    opp_val = getattr(item, "company", None)
                    
                    setattr(item, "company", self)
                    

    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company__tags", None)
        self.__tags = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tagged_companies"):
                    opp_val = getattr(item, "tagged_companies", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tagged_companies"):
                    opp_val = getattr(item, "tagged_companies", None)
                    
                    if opp_val is None:
                        setattr(item, "tagged_companies", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def contacts(self):
        return self.__contacts
    @contacts.setter
    def contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company__contacts", None)
        self.__contacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company"):
                    opp_val = getattr(item, "company", None)
                    
                    if opp_val == self:
                        setattr(item, "company", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company"):
                    opp_val = getattr(item, "company", None)
                    
                    setattr(item, "company", self)
                    

    @property
    def created_by(self):
        return self.__created_by
    @created_by.setter
    def created_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company__created_by", None)
        self.__created_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "created_companies"):
                opp_val = getattr(old_value, "created_companies", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "created_companies"):
                opp_val = getattr(value, "created_companies", None)
                if opp_val is None:
                    setattr(value, "created_companies", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Contact:

    def __init__(self, updated_at: datetime, phone: str, lead_score_level: LeadScoreLevel, email: str, lead_score: int, last_name: str, profile_picture_url: str, first_name: str, created_at: datetime, linkedin_url: str, id: int, notes: str, job_title: str, is_enriched: bool, company: "Company" = None, created_by: "User" = None, tags: set["Tag"] = None, opportunities: set["Opportunity"] = None, generated_emails: set["GeneratedEmail"] = None, tasks: set["Task"] = None, score_history: set["ScoreHistory"] = None, interactions: set["Interaction"] = None, enrichment_logs: set["EnrichmentLog"] = None):
        self.updated_at = updated_at
        self.phone = phone
        self.lead_score_level = lead_score_level
        self.email = email
        self.lead_score = lead_score
        self.last_name = last_name
        self.profile_picture_url = profile_picture_url
        self.first_name = first_name
        self.created_at = created_at
        self.linkedin_url = linkedin_url
        self.id = id
        self.notes = notes
        self.job_title = job_title
        self.is_enriched = is_enriched
        self.company = company
        self.created_by = created_by
        self.tags = tags if tags is not None else set()
        self.opportunities = opportunities if opportunities is not None else set()
        self.generated_emails = generated_emails if generated_emails is not None else set()
        self.tasks = tasks if tasks is not None else set()
        self.score_history = score_history if score_history is not None else set()
        self.interactions = interactions if interactions is not None else set()
        self.enrichment_logs = enrichment_logs if enrichment_logs is not None else set()
        
        pass
    @property
    def is_enriched(self):
        return self.__is_enriched
    @is_enriched.setter
    def is_enriched(self, is_enriched: bool):
        self.__is_enriched = is_enriched

    @property
    def updated_at(self):
        return self.__updated_at
    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        self.__updated_at = updated_at

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def profile_picture_url(self):
        return self.__profile_picture_url
    @profile_picture_url.setter
    def profile_picture_url(self, profile_picture_url: str):
        self.__profile_picture_url = profile_picture_url

    @property
    def lead_score_level(self):
        return self.__lead_score_level
    @lead_score_level.setter
    def lead_score_level(self, lead_score_level: LeadScoreLevel):
        self.__lead_score_level = lead_score_level

    @property
    def notes(self):
        return self.__notes
    @notes.setter
    def notes(self, notes: str):
        self.__notes = notes

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def job_title(self):
        return self.__job_title
    @job_title.setter
    def job_title(self, job_title: str):
        self.__job_title = job_title

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def lead_score(self):
        return self.__lead_score
    @lead_score.setter
    def lead_score(self, lead_score: int):
        self.__lead_score = lead_score

    @property
    def linkedin_url(self):
        return self.__linkedin_url
    @linkedin_url.setter
    def linkedin_url(self, linkedin_url: str):
        self.__linkedin_url = linkedin_url

    @property
    def opportunities(self):
        return self.__opportunities
    @opportunities.setter
    def opportunities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__opportunities", None)
        self.__opportunities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contacts"):
                    opp_val = getattr(item, "contacts", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contacts"):
                    opp_val = getattr(item, "contacts", None)
                    
                    if opp_val is None:
                        setattr(item, "contacts", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def created_by(self):
        return self.__created_by
    @created_by.setter
    def created_by(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__created_by", None)
        self.__created_by = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "created_contacts"):
                opp_val = getattr(old_value, "created_contacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "created_contacts"):
                opp_val = getattr(value, "created_contacts", None)
                if opp_val is None:
                    setattr(value, "created_contacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__company", None)
        self.__company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts"):
                opp_val = getattr(old_value, "contacts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts"):
                opp_val = getattr(value, "contacts", None)
                if opp_val is None:
                    setattr(value, "contacts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tags(self):
        return self.__tags
    @tags.setter
    def tags(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__tags", None)
        self.__tags = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tagged_contacts"):
                    opp_val = getattr(item, "tagged_contacts", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tagged_contacts"):
                    opp_val = getattr(item, "tagged_contacts", None)
                    
                    if opp_val is None:
                        setattr(item, "tagged_contacts", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def enrichment_logs(self):
        return self.__enrichment_logs
    @enrichment_logs.setter
    def enrichment_logs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__enrichment_logs", None)
        self.__enrichment_logs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    if opp_val == self:
                        setattr(item, "contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    setattr(item, "contact", self)
                    

    @property
    def interactions(self):
        return self.__interactions
    @interactions.setter
    def interactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__interactions", None)
        self.__interactions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    if opp_val == self:
                        setattr(item, "contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    setattr(item, "contact", self)
                    

    @property
    def score_history(self):
        return self.__score_history
    @score_history.setter
    def score_history(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__score_history", None)
        self.__score_history = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    if opp_val == self:
                        setattr(item, "contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    setattr(item, "contact", self)
                    

    @property
    def tasks(self):
        return self.__tasks
    @tasks.setter
    def tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__tasks", None)
        self.__tasks = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    if opp_val == self:
                        setattr(item, "contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    setattr(item, "contact", self)
                    

    @property
    def generated_emails(self):
        return self.__generated_emails
    @generated_emails.setter
    def generated_emails(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__generated_emails", None)
        self.__generated_emails = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    if opp_val == self:
                        setattr(item, "contact", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "contact"):
                    opp_val = getattr(item, "contact", None)
                    
                    setattr(item, "contact", self)
                    



class Opportunity:

    def __init__(self, expected_close_date: date, id: int, probability: int, value: float, closed_at: datetime, stage: OpportunityStage, updated_at: datetime, description: str, created_at: datetime, title: str, tasks: set["Task"] = None, owner: "User" = None, contacts: set["Contact"] = None, company: "Company" = None):
        self.expected_close_date = expected_close_date
        self.id = id
        self.probability = probability
        self.value = value
        self.closed_at = closed_at
        self.stage = stage
        self.updated_at = updated_at
        self.description = description
        self.created_at = created_at
        self.title = title
        self.tasks = tasks if tasks is not None else set()
        self.owner = owner
        self.contacts = contacts if contacts is not None else set()
        self.company = company
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def stage(self):
        return self.__stage
    @stage.setter
    def stage(self, stage: OpportunityStage):
        self.__stage = stage

    @property
    def probability(self):
        return self.__probability
    @probability.setter
    def probability(self, probability: int):
        self.__probability = probability

    @property
    def updated_at(self):
        return self.__updated_at
    @updated_at.setter
    def updated_at(self, updated_at: datetime):
        self.__updated_at = updated_at

    @property
    def expected_close_date(self):
        return self.__expected_close_date
    @expected_close_date.setter
    def expected_close_date(self, expected_close_date: date):
        self.__expected_close_date = expected_close_date

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def created_at(self):
        return self.__created_at
    @created_at.setter
    def created_at(self, created_at: datetime):
        self.__created_at = created_at

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def closed_at(self):
        return self.__closed_at
    @closed_at.setter
    def closed_at(self, closed_at: datetime):
        self.__closed_at = closed_at

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Opportunity__owner", None)
        self.__owner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owned_opportunities"):
                opp_val = getattr(old_value, "owned_opportunities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owned_opportunities"):
                opp_val = getattr(value, "owned_opportunities", None)
                if opp_val is None:
                    setattr(value, "owned_opportunities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contacts(self):
        return self.__contacts
    @contacts.setter
    def contacts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Opportunity__contacts", None)
        self.__contacts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "opportunities"):
                    opp_val = getattr(item, "opportunities", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "opportunities"):
                    opp_val = getattr(item, "opportunities", None)
                    
                    if opp_val is None:
                        setattr(item, "opportunities", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def tasks(self):
        return self.__tasks
    @tasks.setter
    def tasks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Opportunity__tasks", None)
        self.__tasks = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "opportunity"):
                    opp_val = getattr(item, "opportunity", None)
                    
                    if opp_val == self:
                        setattr(item, "opportunity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "opportunity"):
                    opp_val = getattr(item, "opportunity", None)
                    
                    setattr(item, "opportunity", self)
                    

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Opportunity__company", None)
        self.__company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opportunities"):
                opp_val = getattr(old_value, "opportunities", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opportunities"):
                opp_val = getattr(value, "opportunities", None)
                if opp_val is None:
                    setattr(value, "opportunities", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

