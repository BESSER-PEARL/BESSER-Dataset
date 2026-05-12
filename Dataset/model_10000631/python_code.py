from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Class:

    pass


class PlanDAO:

    pass


class PatientDAO:

    pass


class PatientBO:

    pass


class StateDAO1:

    pass


class PatientTO:

    def __init__(self, patient_id: int, first_name: str, last_name: str, password: str, date_of_birth: date, email: str, contact_no: int, state_id: int, plan_id: int):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.date_of_birth = date_of_birth
        self.email = email
        self.contact_no = contact_no
        self.state_id = state_id
        self.plan_id = plan_id
        
        pass
    @property
    def plan_id(self):
        return self.__plan_id
    @plan_id.setter
    def plan_id(self, plan_id: int):
        self.__plan_id = plan_id

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def state_id(self):
        return self.__state_id
    @state_id.setter
    def state_id(self, state_id: int):
        self.__state_id = state_id

    @property
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def patient_id(self):
        return self.__patient_id
    @patient_id.setter
    def patient_id(self, patient_id: int):
        self.__patient_id = patient_id



class StateDAO:

    pass


class EnrollPatient_Controller:

    pass
