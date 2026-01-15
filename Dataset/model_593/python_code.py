from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ExamItemView:

    pass
class AssistantMVC_MultipleChoiceView(ExamItemView):

    pass
class ExamView:

    pass
class AssistantMVC_OpenView(ExamView):

    pass
class View:

    pass
class AssistantMVC_ExamItemView(View):

    pass
class AssistantMVC_ExamView(View):

    pass
class ExamItemController:

    pass
class AssistantMVC_OpenController(ExamItemController):

    pass
class AssistantMVC_MultipleChoiceController(ExamItemController):

    pass
class Observable:

    pass
class AssistantMVC_ExamItem(Observable):

    def __init__(self, value: str, optional: bool, question: str, AssistantMVC_ExamItem: "AssistantMVC_Exam" = None):
        self.value = value
        self.optional = optional
        self.question = question
        self.AssistantMVC_ExamItem = AssistantMVC_ExamItem
        
    @property
    def question(self) -> str:
        return self.__question

    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def AssistantMVC_ExamItem(self):
        return self.__AssistantMVC_ExamItem

    @AssistantMVC_ExamItem.setter
    def AssistantMVC_ExamItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_ExamItem__AssistantMVC_ExamItem", None)
        self.__AssistantMVC_ExamItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssistantMVC_Exam"):
                opp_val = getattr(old_value, "AssistantMVC_Exam", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssistantMVC_Exam"):
                opp_val = getattr(value, "AssistantMVC_Exam", None)
                if opp_val is None:
                    setattr(value, "AssistantMVC_Exam", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AssistantMVC_Exam(Observable):

    def __init__(self, question: str, AssistantMVC_Exam: set["AssistantMVC_ExamItem"] = None, AssistantMVC_Exam2: set["AssistantMVC_Controller"] = None, AssistantMVC_Exam4: set["AssistantMVC_View"] = None):
        self.question = question
        self.AssistantMVC_Exam = AssistantMVC_Exam if AssistantMVC_Exam is not None else set()
        self.AssistantMVC_Exam2 = AssistantMVC_Exam2 if AssistantMVC_Exam2 is not None else set()
        self.AssistantMVC_Exam4 = AssistantMVC_Exam4 if AssistantMVC_Exam4 is not None else set()
        
    @property
    def question(self) -> str:
        return self.__question

    @question.setter
    def question(self, question: str):
        self.__question = question

    @property
    def AssistantMVC_Exam(self):
        return self.__AssistantMVC_Exam

    @AssistantMVC_Exam.setter
    def AssistantMVC_Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_Exam__AssistantMVC_Exam", None)
        self.__AssistantMVC_Exam = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssistantMVC_ExamItem"):
                    opp_val = getattr(item, "AssistantMVC_ExamItem", None)
                    
                    if opp_val == self:
                        setattr(item, "AssistantMVC_ExamItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssistantMVC_ExamItem"):
                    opp_val = getattr(item, "AssistantMVC_ExamItem", None)
                    
                    setattr(item, "AssistantMVC_ExamItem", self)
                    

    @property
    def AssistantMVC_Exam2(self):
        return self.__AssistantMVC_Exam2

    @AssistantMVC_Exam2.setter
    def AssistantMVC_Exam2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_Exam__AssistantMVC_Exam2", None)
        self.__AssistantMVC_Exam2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssistantMVC_Controller"):
                    opp_val = getattr(item, "AssistantMVC_Controller", None)
                    
                    if opp_val == self:
                        setattr(item, "AssistantMVC_Controller", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssistantMVC_Controller"):
                    opp_val = getattr(item, "AssistantMVC_Controller", None)
                    
                    setattr(item, "AssistantMVC_Controller", self)
                    

    @property
    def AssistantMVC_Exam4(self):
        return self.__AssistantMVC_Exam4

    @AssistantMVC_Exam4.setter
    def AssistantMVC_Exam4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_Exam__AssistantMVC_Exam4", None)
        self.__AssistantMVC_Exam4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssistantMVC_View"):
                    opp_val = getattr(item, "AssistantMVC_View", None)
                    
                    if opp_val == self:
                        setattr(item, "AssistantMVC_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssistantMVC_View"):
                    opp_val = getattr(item, "AssistantMVC_View", None)
                    
                    setattr(item, "AssistantMVC_View", self)
                    

class Controller:

    pass
class AssistantMVC_ExamItemController(Controller):

    pass
class AssistantMVC_ExamController(Controller):

    pass
class Observer:

    pass
class AssistantMVC_View(Observer):

    def __init__(self, fontName: str, fontColor: str, AssistantMVC_View7: "AssistantMVC_Controller" = None, AssistantMVC_View: "AssistantMVC_Exam" = None):
        self.fontName = fontName
        self.fontColor = fontColor
        self.AssistantMVC_View7 = AssistantMVC_View7
        self.AssistantMVC_View = AssistantMVC_View
        
    @property
    def fontColor(self) -> str:
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def AssistantMVC_View7(self):
        return self.__AssistantMVC_View7

    @AssistantMVC_View7.setter
    def AssistantMVC_View7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_View__AssistantMVC_View7", None)
        self.__AssistantMVC_View7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssistantMVC_Controller8"):
                opp_val = getattr(old_value, "AssistantMVC_Controller8", None)
                if opp_val == self:
                    setattr(old_value, "AssistantMVC_Controller8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssistantMVC_Controller8"):
                opp_val = getattr(value, "AssistantMVC_Controller8", None)
                setattr(value, "AssistantMVC_Controller8", self)

    @property
    def AssistantMVC_View(self):
        return self.__AssistantMVC_View

    @AssistantMVC_View.setter
    def AssistantMVC_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AssistantMVC_View__AssistantMVC_View", None)
        self.__AssistantMVC_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssistantMVC_Exam4"):
                opp_val = getattr(old_value, "AssistantMVC_Exam4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssistantMVC_Exam4"):
                opp_val = getattr(value, "AssistantMVC_Exam4", None)
                if opp_val is None:
                    setattr(value, "AssistantMVC_Exam4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AssistantMVC_Controller(Observer):

    pass
class AssistantMVC_Observer:

    pass
class AssistantMVC_Observable:

    pass
class ExamItem:

    pass
class AssistantMVC_MultipleChoice(ExamItem):

    pass
class AssistantMVC_Open(ExamItem):

    pass