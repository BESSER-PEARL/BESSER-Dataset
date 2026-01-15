from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class contacts_UoD:

    pass
class contacts_AddressBook:

    pass
class contacts_Contact:

    def __init__(self, company: str, jobTitle: str, email: str, webPage: str, firstName: str, middleName: str, lastName: str, title: str, note: str, image: str, contacts_Contact: "contacts_Address" = None, contacts_Contact2: "contacts_PhoneNumber" = None, contacts_Contact10: "contacts_AddressBook" = None, contacts_Contact4: "contacts_PhoneNumber" = None, contacts_Contact7: "contacts_Address" = None):
        self.company = company
        self.jobTitle = jobTitle
        self.email = email
        self.webPage = webPage
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.title = title
        self.note = note
        self.image = image
        self.contacts_Contact = contacts_Contact
        self.contacts_Contact2 = contacts_Contact2
        self.contacts_Contact10 = contacts_Contact10
        self.contacts_Contact4 = contacts_Contact4
        self.contacts_Contact7 = contacts_Contact7
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def company(self) -> str:
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def webPage(self) -> str:
        return self.__webPage

    @webPage.setter
    def webPage(self, webPage: str):
        self.__webPage = webPage

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def jobTitle(self) -> str:
        return self.__jobTitle

    @jobTitle.setter
    def jobTitle(self, jobTitle: str):
        self.__jobTitle = jobTitle

    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def middleName(self) -> str:
        return self.__middleName

    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def contacts_Contact7(self):
        return self.__contacts_Contact7

    @contacts_Contact7.setter
    def contacts_Contact7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Contact__contacts_Contact7", None)
        self.__contacts_Contact7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Address8"):
                opp_val = getattr(old_value, "contacts_Address8", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Address8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Address8"):
                opp_val = getattr(value, "contacts_Address8", None)
                setattr(value, "contacts_Address8", self)

    @property
    def contacts_Contact10(self):
        return self.__contacts_Contact10

    @contacts_Contact10.setter
    def contacts_Contact10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Contact__contacts_Contact10", None)
        self.__contacts_Contact10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_AddressBook"):
                opp_val = getattr(old_value, "contacts_AddressBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_AddressBook"):
                opp_val = getattr(value, "contacts_AddressBook", None)
                if opp_val is None:
                    setattr(value, "contacts_AddressBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contacts_Contact4(self):
        return self.__contacts_Contact4

    @contacts_Contact4.setter
    def contacts_Contact4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Contact__contacts_Contact4", None)
        self.__contacts_Contact4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_PhoneNumber5"):
                opp_val = getattr(old_value, "contacts_PhoneNumber5", None)
                if opp_val == self:
                    setattr(old_value, "contacts_PhoneNumber5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_PhoneNumber5"):
                opp_val = getattr(value, "contacts_PhoneNumber5", None)
                setattr(value, "contacts_PhoneNumber5", self)

    @property
    def contacts_Contact(self):
        return self.__contacts_Contact

    @contacts_Contact.setter
    def contacts_Contact(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Contact__contacts_Contact", None)
        self.__contacts_Contact = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Address"):
                opp_val = getattr(old_value, "contacts_Address", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Address"):
                opp_val = getattr(value, "contacts_Address", None)
                setattr(value, "contacts_Address", self)

    @property
    def contacts_Contact2(self):
        return self.__contacts_Contact2

    @contacts_Contact2.setter
    def contacts_Contact2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Contact__contacts_Contact2", None)
        self.__contacts_Contact2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_PhoneNumber"):
                opp_val = getattr(old_value, "contacts_PhoneNumber", None)
                if opp_val == self:
                    setattr(old_value, "contacts_PhoneNumber", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_PhoneNumber"):
                opp_val = getattr(value, "contacts_PhoneNumber", None)
                setattr(value, "contacts_PhoneNumber", self)

class contacts_PhoneNumber:

    def __init__(self, number: str, country: str, contacts_PhoneNumber: "contacts_Contact" = None, contacts_PhoneNumber5: "contacts_Contact" = None):
        self.number = number
        self.country = country
        self.contacts_PhoneNumber = contacts_PhoneNumber
        self.contacts_PhoneNumber5 = contacts_PhoneNumber5
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def contacts_PhoneNumber(self):
        return self.__contacts_PhoneNumber

    @contacts_PhoneNumber.setter
    def contacts_PhoneNumber(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_PhoneNumber__contacts_PhoneNumber", None)
        self.__contacts_PhoneNumber = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Contact2"):
                opp_val = getattr(old_value, "contacts_Contact2", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Contact2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Contact2"):
                opp_val = getattr(value, "contacts_Contact2", None)
                setattr(value, "contacts_Contact2", self)

    @property
    def contacts_PhoneNumber5(self):
        return self.__contacts_PhoneNumber5

    @contacts_PhoneNumber5.setter
    def contacts_PhoneNumber5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_PhoneNumber__contacts_PhoneNumber5", None)
        self.__contacts_PhoneNumber5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Contact4"):
                opp_val = getattr(old_value, "contacts_Contact4", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Contact4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Contact4"):
                opp_val = getattr(value, "contacts_Contact4", None)
                setattr(value, "contacts_Contact4", self)

class contacts_Address:

    def __init__(self, zipCode: str, street: str, city: str, state: str, country: str, contacts_Address: "contacts_Contact" = None, contacts_Address8: "contacts_Contact" = None):
        self.zipCode = zipCode
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.contacts_Address = contacts_Address
        self.contacts_Address8 = contacts_Address8
        
    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def zipCode(self) -> str:
        return self.__zipCode

    @zipCode.setter
    def zipCode(self, zipCode: str):
        self.__zipCode = zipCode

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def contacts_Address8(self):
        return self.__contacts_Address8

    @contacts_Address8.setter
    def contacts_Address8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Address__contacts_Address8", None)
        self.__contacts_Address8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Contact7"):
                opp_val = getattr(old_value, "contacts_Contact7", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Contact7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Contact7"):
                opp_val = getattr(value, "contacts_Contact7", None)
                setattr(value, "contacts_Contact7", self)

    @property
    def contacts_Address(self):
        return self.__contacts_Address

    @contacts_Address.setter
    def contacts_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_contacts_Address__contacts_Address", None)
        self.__contacts_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contacts_Contact"):
                opp_val = getattr(old_value, "contacts_Contact", None)
                if opp_val == self:
                    setattr(old_value, "contacts_Contact", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contacts_Contact"):
                opp_val = getattr(value, "contacts_Contact", None)
                setattr(value, "contacts_Contact", self)
