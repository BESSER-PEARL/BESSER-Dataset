from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BugStatusType(Enum):
    bst_open = "bst_open"
    bst_closed = "bst_closed"
    bst_skipped = "bst_skipped"


############################################
# Definition of Classes
############################################

class BugTracking:

    pass
class SoftwareQualityControl_Bug:

    def __init__(self, number: str, componentVersion: str, description: str, status: str, originator: str, responsible: str, commentsAnswers: str, openDate: str, closeDate: str, bugs: "BugTracking" = None):
        self.number = number
        self.componentVersion = componentVersion
        self.description = description
        self.status = status
        self.originator = originator
        self.responsible = responsible
        self.commentsAnswers = commentsAnswers
        self.openDate = openDate
        self.closeDate = closeDate
        self.bugs = bugs
        
        pass
    @property
    def componentVersion(self):
        return self.__componentVersion

    @componentVersion.setter
    def componentVersion(self, componentVersion: str):
        self.__componentVersion = componentVersion


    @property
    def commentsAnswers(self):
        return self.__commentsAnswers

    @commentsAnswers.setter
    def commentsAnswers(self, commentsAnswers: str):
        self.__commentsAnswers = commentsAnswers


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def openDate(self):
        return self.__openDate

    @openDate.setter
    def openDate(self, openDate: str):
        self.__openDate = openDate


    @property
    def responsible(self):
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: str):
        self.__responsible = responsible


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number


    @property
    def closeDate(self):
        return self.__closeDate

    @closeDate.setter
    def closeDate(self, closeDate: str):
        self.__closeDate = closeDate


    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status


    @property
    def originator(self):
        return self.__originator

    @originator.setter
    def originator(self, originator: str):
        self.__originator = originator


    @property
    def bugs(self):
        return self.__bugs

    @bugs.setter
    def bugs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SoftwareQualityControl_Bug__bugs", None)
        self.__bugs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BugTracking"):
                opp_val = getattr(old_value, "BugTracking", None)
                if opp_val == self:
                    setattr(old_value, "BugTracking", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BugTracking"):
                opp_val = getattr(value, "BugTracking", None)
                setattr(value, "BugTracking", self)

class ControlType:

    pass
class DateType:

    pass
class ControlsSequence:

    pass
class SoftwareQualityControl_Control:

    def __init__(self, responsible: str, component: str, developmentPhase: str, scope: str, controlledElt: str, eltRef: str, eltAuthor: str, formRef: str, ct_control: "ControlType" = None, controls: "ControlsSequence" = None, SoftwareQualityControl_Control: "DateType" = None):
        self.responsible = responsible
        self.component = component
        self.developmentPhase = developmentPhase
        self.scope = scope
        self.controlledElt = controlledElt
        self.eltRef = eltRef
        self.eltAuthor = eltAuthor
        self.formRef = formRef
        self.ct_control = ct_control
        self.controls = controls
        self.SoftwareQualityControl_Control = SoftwareQualityControl_Control
        
        pass
    @property
    def eltRef(self):
        return self.__eltRef

    @eltRef.setter
    def eltRef(self, eltRef: str):
        self.__eltRef = eltRef


    @property
    def controlledElt(self):
        return self.__controlledElt

    @controlledElt.setter
    def controlledElt(self, controlledElt: str):
        self.__controlledElt = controlledElt


    @property
    def formRef(self):
        return self.__formRef

    @formRef.setter
    def formRef(self, formRef: str):
        self.__formRef = formRef


    @property
    def developmentPhase(self):
        return self.__developmentPhase

    @developmentPhase.setter
    def developmentPhase(self, developmentPhase: str):
        self.__developmentPhase = developmentPhase


    @property
    def responsible(self):
        return self.__responsible

    @responsible.setter
    def responsible(self, responsible: str):
        self.__responsible = responsible


    @property
    def eltAuthor(self):
        return self.__eltAuthor

    @eltAuthor.setter
    def eltAuthor(self, eltAuthor: str):
        self.__eltAuthor = eltAuthor


    @property
    def component(self):
        return self.__component

    @component.setter
    def component(self, component: str):
        self.__component = component


    @property
    def scope(self):
        return self.__scope

    @scope.setter
    def scope(self, scope: str):
        self.__scope = scope


    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SoftwareQualityControl_Control__controls", None)
        self.__controls = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlsSequence"):
                opp_val = getattr(old_value, "ControlsSequence", None)
                if opp_val == self:
                    setattr(old_value, "ControlsSequence", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlsSequence"):
                opp_val = getattr(value, "ControlsSequence", None)
                setattr(value, "ControlsSequence", self)

    @property
    def SoftwareQualityControl_Control(self):
        return self.__SoftwareQualityControl_Control

    @SoftwareQualityControl_Control.setter
    def SoftwareQualityControl_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SoftwareQualityControl_Control__SoftwareQualityControl_Control", None)
        self.__SoftwareQualityControl_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DateType"):
                opp_val = getattr(old_value, "DateType", None)
                if opp_val == self:
                    setattr(old_value, "DateType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DateType"):
                opp_val = getattr(value, "DateType", None)
                setattr(value, "DateType", self)

    @property
    def ct_control(self):
        return self.__ct_control

    @ct_control.setter
    def ct_control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SoftwareQualityControl_Control__ct_control", None)
        self.__ct_control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ControlType"):
                opp_val = getattr(old_value, "ControlType", None)
                if opp_val == self:
                    setattr(old_value, "ControlType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ControlType"):
                opp_val = getattr(value, "ControlType", None)
                setattr(value, "ControlType", self)

class Control:

    pass
class SoftwareQualityControl_ControlsSequence:

    pass
class SoftwareQualityControl_DateType:

    def __init__(self, day: str, month: str, year: str):
        self.day = day
        self.month = month
        self.year = year
        
        pass
    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year


class Bug:

    pass
class SoftwareQualityControl_BugTracking(ControlType):

    pass
class SoftwareQualityControl_ControlType(ABC):

    pass