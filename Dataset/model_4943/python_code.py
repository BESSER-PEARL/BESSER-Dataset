from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Alignment(Enum):
    left = "left"
    right = "right"


############################################
# Definition of Classes
############################################

class webshop_builder_3k_model_Border:

    def __init__(self, thickness: int, color: str, webshop_builder_3k_model_Border: "webshop_builder_3k_model_Style" = None):
        self.thickness = thickness
        self.color = color
        self.webshop_builder_3k_model_Border = webshop_builder_3k_model_Border
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def thickness(self) -> int:
        return self.__thickness

    @thickness.setter
    def thickness(self, thickness: int):
        self.__thickness = thickness

    @property
    def webshop_builder_3k_model_Border(self):
        return self.__webshop_builder_3k_model_Border

    @webshop_builder_3k_model_Border.setter
    def webshop_builder_3k_model_Border(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Border__webshop_builder_3k_model_Border", None)
        self.__webshop_builder_3k_model_Border = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Style50"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Style50", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Style50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Style50"):
                opp_val = getattr(value, "webshop_builder_3k_model_Style50", None)
                setattr(value, "webshop_builder_3k_model_Style50", self)

class webshop_builder_3k_model_Navigation_to_Page_link:

    pass
class webshop_builder_3k_model_Source_code:

    pass
class webshop_builder_3k_model_Component_group:

    pass
class webshop_builder_3k_model_Menu:

    pass
class webshop_builder_3k_model_Search_widget:

    pass
class webshop_builder_3k_model_Shopping_cart_button:

    pass
class webshop_builder_3k_model_Newsletter_subscription_widget:

    pass
class webshop_builder_3k_model_Social_button:

    pass
class webshop_builder_3k_model_Slideshow:

    pass
class webshop_builder_3k_model_Login_widget:

    pass
class webshop_builder_3k_model_Webshop_builder_3k:

    def __init__(self, company_name: str, webshop_builder_3k_model_Webshop_builder_3k: set["webshop_builder_3k_model_Page"] = None, webshop_builder_3k_model_Webshop_builder_3k20: set["webshop_builder_3k_model_Component"] = None, webshop_builder_3k_model_Webshop_builder_3k23: set["webshop_builder_3k_model_Knowledge_base"] = None, webshop_builder_3k_model_Webshop_builder_3k26: "webshop_builder_3k_model_Page" = None, webshop_builder_3k_model_Webshop_builder_3k29: "webshop_builder_3k_model_Page" = None):
        self.company_name = company_name
        self.webshop_builder_3k_model_Webshop_builder_3k = webshop_builder_3k_model_Webshop_builder_3k if webshop_builder_3k_model_Webshop_builder_3k is not None else set()
        self.webshop_builder_3k_model_Webshop_builder_3k20 = webshop_builder_3k_model_Webshop_builder_3k20 if webshop_builder_3k_model_Webshop_builder_3k20 is not None else set()
        self.webshop_builder_3k_model_Webshop_builder_3k23 = webshop_builder_3k_model_Webshop_builder_3k23 if webshop_builder_3k_model_Webshop_builder_3k23 is not None else set()
        self.webshop_builder_3k_model_Webshop_builder_3k26 = webshop_builder_3k_model_Webshop_builder_3k26
        self.webshop_builder_3k_model_Webshop_builder_3k29 = webshop_builder_3k_model_Webshop_builder_3k29
        
    @property
    def company_name(self) -> str:
        return self.__company_name

    @company_name.setter
    def company_name(self, company_name: str):
        self.__company_name = company_name

    @property
    def webshop_builder_3k_model_Webshop_builder_3k26(self):
        return self.__webshop_builder_3k_model_Webshop_builder_3k26

    @webshop_builder_3k_model_Webshop_builder_3k26.setter
    def webshop_builder_3k_model_Webshop_builder_3k26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Webshop_builder_3k__webshop_builder_3k_model_Webshop_builder_3k26", None)
        self.__webshop_builder_3k_model_Webshop_builder_3k26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Page27"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Page27", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Page27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Page27"):
                opp_val = getattr(value, "webshop_builder_3k_model_Page27", None)
                setattr(value, "webshop_builder_3k_model_Page27", self)

    @property
    def webshop_builder_3k_model_Webshop_builder_3k23(self):
        return self.__webshop_builder_3k_model_Webshop_builder_3k23

    @webshop_builder_3k_model_Webshop_builder_3k23.setter
    def webshop_builder_3k_model_Webshop_builder_3k23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Webshop_builder_3k__webshop_builder_3k_model_Webshop_builder_3k23", None)
        self.__webshop_builder_3k_model_Webshop_builder_3k23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webshop_builder_3k_model_Knowledge_base24"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Knowledge_base24", None)
                    
                    if opp_val == self:
                        setattr(item, "webshop_builder_3k_model_Knowledge_base24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webshop_builder_3k_model_Knowledge_base24"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Knowledge_base24", None)
                    
                    setattr(item, "webshop_builder_3k_model_Knowledge_base24", self)
                    

    @property
    def webshop_builder_3k_model_Webshop_builder_3k20(self):
        return self.__webshop_builder_3k_model_Webshop_builder_3k20

    @webshop_builder_3k_model_Webshop_builder_3k20.setter
    def webshop_builder_3k_model_Webshop_builder_3k20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Webshop_builder_3k__webshop_builder_3k_model_Webshop_builder_3k20", None)
        self.__webshop_builder_3k_model_Webshop_builder_3k20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webshop_builder_3k_model_Component21"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Component21", None)
                    
                    if opp_val == self:
                        setattr(item, "webshop_builder_3k_model_Component21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webshop_builder_3k_model_Component21"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Component21", None)
                    
                    setattr(item, "webshop_builder_3k_model_Component21", self)
                    

    @property
    def webshop_builder_3k_model_Webshop_builder_3k29(self):
        return self.__webshop_builder_3k_model_Webshop_builder_3k29

    @webshop_builder_3k_model_Webshop_builder_3k29.setter
    def webshop_builder_3k_model_Webshop_builder_3k29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Webshop_builder_3k__webshop_builder_3k_model_Webshop_builder_3k29", None)
        self.__webshop_builder_3k_model_Webshop_builder_3k29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Page30"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Page30", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Page30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Page30"):
                opp_val = getattr(value, "webshop_builder_3k_model_Page30", None)
                setattr(value, "webshop_builder_3k_model_Page30", self)

    @property
    def webshop_builder_3k_model_Webshop_builder_3k(self):
        return self.__webshop_builder_3k_model_Webshop_builder_3k

    @webshop_builder_3k_model_Webshop_builder_3k.setter
    def webshop_builder_3k_model_Webshop_builder_3k(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Webshop_builder_3k__webshop_builder_3k_model_Webshop_builder_3k", None)
        self.__webshop_builder_3k_model_Webshop_builder_3k = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webshop_builder_3k_model_Page18"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Page18", None)
                    
                    if opp_val == self:
                        setattr(item, "webshop_builder_3k_model_Page18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webshop_builder_3k_model_Page18"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Page18", None)
                    
                    setattr(item, "webshop_builder_3k_model_Page18", self)
                    

class User_input_field:

    pass
class webshop_builder_3k_model_Radio_button(User_input_field):

    pass
class webshop_builder_3k_model_Text_input_field(User_input_field):

    pass
class webshop_builder_3k_model_Checkbox(User_input_field):

    pass
class webshop_builder_3k_model_Item_to_KB_link:

    pass
class webshop_builder_3k_model_User_input_field:

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class Component:

    pass
class webshop_builder_3k_model_Item(Component):

    pass
class webshop_builder_3k_model_Text_field(Component):

    def __init__(self, header_level: int, text: str, webshop_builder_3k_model_Text_field: "webshop_builder_3k_model_Branding" = None, webshop_builder_3k_model_Text_field35: "webshop_builder_3k_model_Item" = None, webshop_builder_3k_model_Text_field44: "webshop_builder_3k_model_Navigation_button" = None):
        self.header_level = header_level
        self.text = text
        self.webshop_builder_3k_model_Text_field = webshop_builder_3k_model_Text_field
        self.webshop_builder_3k_model_Text_field35 = webshop_builder_3k_model_Text_field35
        self.webshop_builder_3k_model_Text_field44 = webshop_builder_3k_model_Text_field44
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def header_level(self) -> int:
        return self.__header_level

    @header_level.setter
    def header_level(self, header_level: int):
        self.__header_level = header_level

    @property
    def webshop_builder_3k_model_Text_field(self):
        return self.__webshop_builder_3k_model_Text_field

    @webshop_builder_3k_model_Text_field.setter
    def webshop_builder_3k_model_Text_field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Text_field__webshop_builder_3k_model_Text_field", None)
        self.__webshop_builder_3k_model_Text_field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Branding"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Branding", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Branding", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Branding"):
                opp_val = getattr(value, "webshop_builder_3k_model_Branding", None)
                setattr(value, "webshop_builder_3k_model_Branding", self)

    @property
    def webshop_builder_3k_model_Text_field44(self):
        return self.__webshop_builder_3k_model_Text_field44

    @webshop_builder_3k_model_Text_field44.setter
    def webshop_builder_3k_model_Text_field44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Text_field__webshop_builder_3k_model_Text_field44", None)
        self.__webshop_builder_3k_model_Text_field44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Navigation_button43"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Navigation_button43", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Navigation_button43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Navigation_button43"):
                opp_val = getattr(value, "webshop_builder_3k_model_Navigation_button43", None)
                setattr(value, "webshop_builder_3k_model_Navigation_button43", self)

    @property
    def webshop_builder_3k_model_Text_field35(self):
        return self.__webshop_builder_3k_model_Text_field35

    @webshop_builder_3k_model_Text_field35.setter
    def webshop_builder_3k_model_Text_field35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Text_field__webshop_builder_3k_model_Text_field35", None)
        self.__webshop_builder_3k_model_Text_field35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Item34"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Item34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Item34"):
                opp_val = getattr(value, "webshop_builder_3k_model_Item34", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Item34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webshop_builder_3k_model_Navigation_button(Component):

    pass
class webshop_builder_3k_model_Result_list(Component):

    def __init__(self, number_of_items_per_page: int, distance_between_items: int, webshop_builder_3k_model_Result_list: "webshop_builder_3k_model_Item" = None):
        self.number_of_items_per_page = number_of_items_per_page
        self.distance_between_items = distance_between_items
        self.webshop_builder_3k_model_Result_list = webshop_builder_3k_model_Result_list
        
    @property
    def distance_between_items(self) -> int:
        return self.__distance_between_items

    @distance_between_items.setter
    def distance_between_items(self, distance_between_items: int):
        self.__distance_between_items = distance_between_items

    @property
    def number_of_items_per_page(self) -> int:
        return self.__number_of_items_per_page

    @number_of_items_per_page.setter
    def number_of_items_per_page(self, number_of_items_per_page: int):
        self.__number_of_items_per_page = number_of_items_per_page

    @property
    def webshop_builder_3k_model_Result_list(self):
        return self.__webshop_builder_3k_model_Result_list

    @webshop_builder_3k_model_Result_list.setter
    def webshop_builder_3k_model_Result_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Result_list__webshop_builder_3k_model_Result_list", None)
        self.__webshop_builder_3k_model_Result_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Item38"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Item38", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Item38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Item38"):
                opp_val = getattr(value, "webshop_builder_3k_model_Item38", None)
                setattr(value, "webshop_builder_3k_model_Item38", self)

class webshop_builder_3k_model_Branding(Component):

    pass
class webshop_builder_3k_model_Picture(Component):

    def __init__(self, source: str, title: str, alternative_text: str, webshop_builder_3k_model_Picture: "webshop_builder_3k_model_Branding" = None, webshop_builder_3k_model_Picture32: "webshop_builder_3k_model_Item" = None, webshop_builder_3k_model_Picture41: "webshop_builder_3k_model_Navigation_button" = None):
        self.source = source
        self.title = title
        self.alternative_text = alternative_text
        self.webshop_builder_3k_model_Picture = webshop_builder_3k_model_Picture
        self.webshop_builder_3k_model_Picture32 = webshop_builder_3k_model_Picture32
        self.webshop_builder_3k_model_Picture41 = webshop_builder_3k_model_Picture41
        
    @property
    def alternative_text(self) -> str:
        return self.__alternative_text

    @alternative_text.setter
    def alternative_text(self, alternative_text: str):
        self.__alternative_text = alternative_text

    @property
    def source(self) -> str:
        return self.__source

    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def webshop_builder_3k_model_Picture(self):
        return self.__webshop_builder_3k_model_Picture

    @webshop_builder_3k_model_Picture.setter
    def webshop_builder_3k_model_Picture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Picture__webshop_builder_3k_model_Picture", None)
        self.__webshop_builder_3k_model_Picture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Branding13"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Branding13", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Branding13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Branding13"):
                opp_val = getattr(value, "webshop_builder_3k_model_Branding13", None)
                setattr(value, "webshop_builder_3k_model_Branding13", self)

    @property
    def webshop_builder_3k_model_Picture41(self):
        return self.__webshop_builder_3k_model_Picture41

    @webshop_builder_3k_model_Picture41.setter
    def webshop_builder_3k_model_Picture41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Picture__webshop_builder_3k_model_Picture41", None)
        self.__webshop_builder_3k_model_Picture41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Navigation_button"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Navigation_button", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Navigation_button", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Navigation_button"):
                opp_val = getattr(value, "webshop_builder_3k_model_Navigation_button", None)
                setattr(value, "webshop_builder_3k_model_Navigation_button", self)

    @property
    def webshop_builder_3k_model_Picture32(self):
        return self.__webshop_builder_3k_model_Picture32

    @webshop_builder_3k_model_Picture32.setter
    def webshop_builder_3k_model_Picture32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Picture__webshop_builder_3k_model_Picture32", None)
        self.__webshop_builder_3k_model_Picture32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Item"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Item", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Item", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Item"):
                opp_val = getattr(value, "webshop_builder_3k_model_Item", None)
                setattr(value, "webshop_builder_3k_model_Item", self)

class webshop_builder_3k_model_Reuses_component_link:

    pass
class webshop_builder_3k_model_Style:

    def __init__(self, background_color: str, webshop_builder_3k_model_Style: "webshop_builder_3k_model_Page" = None, webshop_builder_3k_model_Style8: "webshop_builder_3k_model_Component" = None, webshop_builder_3k_model_Style50: "webshop_builder_3k_model_Border" = None):
        self.background_color = background_color
        self.webshop_builder_3k_model_Style = webshop_builder_3k_model_Style
        self.webshop_builder_3k_model_Style8 = webshop_builder_3k_model_Style8
        self.webshop_builder_3k_model_Style50 = webshop_builder_3k_model_Style50
        
    @property
    def background_color(self) -> str:
        return self.__background_color

    @background_color.setter
    def background_color(self, background_color: str):
        self.__background_color = background_color

    @property
    def webshop_builder_3k_model_Style50(self):
        return self.__webshop_builder_3k_model_Style50

    @webshop_builder_3k_model_Style50.setter
    def webshop_builder_3k_model_Style50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Style__webshop_builder_3k_model_Style50", None)
        self.__webshop_builder_3k_model_Style50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Border"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Border", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Border", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Border"):
                opp_val = getattr(value, "webshop_builder_3k_model_Border", None)
                setattr(value, "webshop_builder_3k_model_Border", self)

    @property
    def webshop_builder_3k_model_Style8(self):
        return self.__webshop_builder_3k_model_Style8

    @webshop_builder_3k_model_Style8.setter
    def webshop_builder_3k_model_Style8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Style__webshop_builder_3k_model_Style8", None)
        self.__webshop_builder_3k_model_Style8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Component7"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Component7", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Component7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Component7"):
                opp_val = getattr(value, "webshop_builder_3k_model_Component7", None)
                setattr(value, "webshop_builder_3k_model_Component7", self)

    @property
    def webshop_builder_3k_model_Style(self):
        return self.__webshop_builder_3k_model_Style

    @webshop_builder_3k_model_Style.setter
    def webshop_builder_3k_model_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Style__webshop_builder_3k_model_Style", None)
        self.__webshop_builder_3k_model_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Page4"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Page4", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Page4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Page4"):
                opp_val = getattr(value, "webshop_builder_3k_model_Page4", None)
                setattr(value, "webshop_builder_3k_model_Page4", self)

class webshop_builder_3k_model_Reuse_component:

    def __init__(self, xposition: int, yposition: int, webshop_builder_3k_model_Reuse_component: "webshop_builder_3k_model_Page" = None, source: "webshop_builder_3k_model_Reuses_component_link" = None, Reuse_component: "webshop_builder_3k_model_Reuses_component_link" = None):
        self.xposition = xposition
        self.yposition = yposition
        self.webshop_builder_3k_model_Reuse_component = webshop_builder_3k_model_Reuse_component
        self.source = source
        self.Reuse_component = Reuse_component
        
    @property
    def yposition(self) -> int:
        return self.__yposition

    @yposition.setter
    def yposition(self, yposition: int):
        self.__yposition = yposition

    @property
    def xposition(self) -> int:
        return self.__xposition

    @xposition.setter
    def xposition(self, xposition: int):
        self.__xposition = xposition

    @property
    def Reuse_component(self):
        return self.__Reuse_component

    @Reuse_component.setter
    def Reuse_component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Reuse_component__Reuse_component", None)
        self.__Reuse_component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "link"):
                opp_val = getattr(old_value, "link", None)
                if opp_val == self:
                    setattr(old_value, "link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "link"):
                opp_val = getattr(value, "link", None)
                setattr(value, "link", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Reuse_component__source", None)
        self.__source = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Reuses_component_link"):
                opp_val = getattr(old_value, "Reuses_component_link", None)
                if opp_val == self:
                    setattr(old_value, "Reuses_component_link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Reuses_component_link"):
                opp_val = getattr(value, "Reuses_component_link", None)
                setattr(value, "Reuses_component_link", self)

    @property
    def webshop_builder_3k_model_Reuse_component(self):
        return self.__webshop_builder_3k_model_Reuse_component

    @webshop_builder_3k_model_Reuse_component.setter
    def webshop_builder_3k_model_Reuse_component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Reuse_component__webshop_builder_3k_model_Reuse_component", None)
        self.__webshop_builder_3k_model_Reuse_component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Page2"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Page2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Page2"):
                opp_val = getattr(value, "webshop_builder_3k_model_Page2", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Page2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webshop_builder_3k_model_Knowledge_base:

    def __init__(self, xml_file_uri: str, webshop_builder_3k_model_Knowledge_base: "webshop_builder_3k_model_Item_to_KB_link" = None, webshop_builder_3k_model_Knowledge_base24: "webshop_builder_3k_model_Webshop_builder_3k" = None):
        self.xml_file_uri = xml_file_uri
        self.webshop_builder_3k_model_Knowledge_base = webshop_builder_3k_model_Knowledge_base
        self.webshop_builder_3k_model_Knowledge_base24 = webshop_builder_3k_model_Knowledge_base24
        
    @property
    def xml_file_uri(self) -> str:
        return self.__xml_file_uri

    @xml_file_uri.setter
    def xml_file_uri(self, xml_file_uri: str):
        self.__xml_file_uri = xml_file_uri

    @property
    def webshop_builder_3k_model_Knowledge_base(self):
        return self.__webshop_builder_3k_model_Knowledge_base

    @webshop_builder_3k_model_Knowledge_base.setter
    def webshop_builder_3k_model_Knowledge_base(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Knowledge_base__webshop_builder_3k_model_Knowledge_base", None)
        self.__webshop_builder_3k_model_Knowledge_base = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Item_to_KB_link"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Item_to_KB_link", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Item_to_KB_link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Item_to_KB_link"):
                opp_val = getattr(value, "webshop_builder_3k_model_Item_to_KB_link", None)
                setattr(value, "webshop_builder_3k_model_Item_to_KB_link", self)

    @property
    def webshop_builder_3k_model_Knowledge_base24(self):
        return self.__webshop_builder_3k_model_Knowledge_base24

    @webshop_builder_3k_model_Knowledge_base24.setter
    def webshop_builder_3k_model_Knowledge_base24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Knowledge_base__webshop_builder_3k_model_Knowledge_base24", None)
        self.__webshop_builder_3k_model_Knowledge_base24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k23"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Webshop_builder_3k23"):
                opp_val = getattr(value, "webshop_builder_3k_model_Webshop_builder_3k23", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Webshop_builder_3k23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webshop_builder_3k_model_Component(ABC):

    def __init__(self, xposition: int, yposition: int, width: int, height: int, name: str, alignment: str, webshop_builder_3k_model_Component: "webshop_builder_3k_model_Page" = None, webshop_builder_3k_model_Component7: "webshop_builder_3k_model_Style" = None, webshop_builder_3k_model_Component16: "webshop_builder_3k_model_Reuses_component_link" = None, webshop_builder_3k_model_Component21: "webshop_builder_3k_model_Webshop_builder_3k" = None):
        self.xposition = xposition
        self.yposition = yposition
        self.width = width
        self.height = height
        self.name = name
        self.alignment = alignment
        self.webshop_builder_3k_model_Component = webshop_builder_3k_model_Component
        self.webshop_builder_3k_model_Component7 = webshop_builder_3k_model_Component7
        self.webshop_builder_3k_model_Component16 = webshop_builder_3k_model_Component16
        self.webshop_builder_3k_model_Component21 = webshop_builder_3k_model_Component21
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def yposition(self) -> int:
        return self.__yposition

    @yposition.setter
    def yposition(self, yposition: int):
        self.__yposition = yposition

    @property
    def xposition(self) -> int:
        return self.__xposition

    @xposition.setter
    def xposition(self, xposition: int):
        self.__xposition = xposition

    @property
    def webshop_builder_3k_model_Component16(self):
        return self.__webshop_builder_3k_model_Component16

    @webshop_builder_3k_model_Component16.setter
    def webshop_builder_3k_model_Component16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Component__webshop_builder_3k_model_Component16", None)
        self.__webshop_builder_3k_model_Component16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Reuses_component_link"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Reuses_component_link", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Reuses_component_link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Reuses_component_link"):
                opp_val = getattr(value, "webshop_builder_3k_model_Reuses_component_link", None)
                setattr(value, "webshop_builder_3k_model_Reuses_component_link", self)

    @property
    def webshop_builder_3k_model_Component21(self):
        return self.__webshop_builder_3k_model_Component21

    @webshop_builder_3k_model_Component21.setter
    def webshop_builder_3k_model_Component21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Component__webshop_builder_3k_model_Component21", None)
        self.__webshop_builder_3k_model_Component21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k20"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Webshop_builder_3k20"):
                opp_val = getattr(value, "webshop_builder_3k_model_Webshop_builder_3k20", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Webshop_builder_3k20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webshop_builder_3k_model_Component7(self):
        return self.__webshop_builder_3k_model_Component7

    @webshop_builder_3k_model_Component7.setter
    def webshop_builder_3k_model_Component7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Component__webshop_builder_3k_model_Component7", None)
        self.__webshop_builder_3k_model_Component7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Style8"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Style8", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Style8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Style8"):
                opp_val = getattr(value, "webshop_builder_3k_model_Style8", None)
                setattr(value, "webshop_builder_3k_model_Style8", self)

    @property
    def webshop_builder_3k_model_Component(self):
        return self.__webshop_builder_3k_model_Component

    @webshop_builder_3k_model_Component.setter
    def webshop_builder_3k_model_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Component__webshop_builder_3k_model_Component", None)
        self.__webshop_builder_3k_model_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Page"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Page"):
                opp_val = getattr(value, "webshop_builder_3k_model_Page", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webshop_builder_3k_model_Page:

    def __init__(self, width: int, title: str, height: int, canvas_color: str, webshop_builder_3k_model_Page: set["webshop_builder_3k_model_Component"] = None, webshop_builder_3k_model_Page2: set["webshop_builder_3k_model_Reuse_component"] = None, webshop_builder_3k_model_Page4: "webshop_builder_3k_model_Style" = None, webshop_builder_3k_model_Page18: "webshop_builder_3k_model_Webshop_builder_3k" = None, webshop_builder_3k_model_Page27: "webshop_builder_3k_model_Webshop_builder_3k" = None, webshop_builder_3k_model_Page30: "webshop_builder_3k_model_Webshop_builder_3k" = None, webshop_builder_3k_model_Page48: "webshop_builder_3k_model_Navigation_to_Page_link" = None):
        self.width = width
        self.title = title
        self.height = height
        self.canvas_color = canvas_color
        self.webshop_builder_3k_model_Page = webshop_builder_3k_model_Page if webshop_builder_3k_model_Page is not None else set()
        self.webshop_builder_3k_model_Page2 = webshop_builder_3k_model_Page2 if webshop_builder_3k_model_Page2 is not None else set()
        self.webshop_builder_3k_model_Page4 = webshop_builder_3k_model_Page4
        self.webshop_builder_3k_model_Page18 = webshop_builder_3k_model_Page18
        self.webshop_builder_3k_model_Page27 = webshop_builder_3k_model_Page27
        self.webshop_builder_3k_model_Page30 = webshop_builder_3k_model_Page30
        self.webshop_builder_3k_model_Page48 = webshop_builder_3k_model_Page48
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def canvas_color(self) -> str:
        return self.__canvas_color

    @canvas_color.setter
    def canvas_color(self, canvas_color: str):
        self.__canvas_color = canvas_color

    @property
    def webshop_builder_3k_model_Page(self):
        return self.__webshop_builder_3k_model_Page

    @webshop_builder_3k_model_Page.setter
    def webshop_builder_3k_model_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page", None)
        self.__webshop_builder_3k_model_Page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webshop_builder_3k_model_Component"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "webshop_builder_3k_model_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webshop_builder_3k_model_Component"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Component", None)
                    
                    setattr(item, "webshop_builder_3k_model_Component", self)
                    

    @property
    def webshop_builder_3k_model_Page4(self):
        return self.__webshop_builder_3k_model_Page4

    @webshop_builder_3k_model_Page4.setter
    def webshop_builder_3k_model_Page4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page4", None)
        self.__webshop_builder_3k_model_Page4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Style"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Style", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Style"):
                opp_val = getattr(value, "webshop_builder_3k_model_Style", None)
                setattr(value, "webshop_builder_3k_model_Style", self)

    @property
    def webshop_builder_3k_model_Page18(self):
        return self.__webshop_builder_3k_model_Page18

    @webshop_builder_3k_model_Page18.setter
    def webshop_builder_3k_model_Page18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page18", None)
        self.__webshop_builder_3k_model_Page18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Webshop_builder_3k"):
                opp_val = getattr(value, "webshop_builder_3k_model_Webshop_builder_3k", None)
                if opp_val is None:
                    setattr(value, "webshop_builder_3k_model_Webshop_builder_3k", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webshop_builder_3k_model_Page48(self):
        return self.__webshop_builder_3k_model_Page48

    @webshop_builder_3k_model_Page48.setter
    def webshop_builder_3k_model_Page48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page48", None)
        self.__webshop_builder_3k_model_Page48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Navigation_to_Page_link"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Navigation_to_Page_link", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Navigation_to_Page_link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Navigation_to_Page_link"):
                opp_val = getattr(value, "webshop_builder_3k_model_Navigation_to_Page_link", None)
                setattr(value, "webshop_builder_3k_model_Navigation_to_Page_link", self)

    @property
    def webshop_builder_3k_model_Page2(self):
        return self.__webshop_builder_3k_model_Page2

    @webshop_builder_3k_model_Page2.setter
    def webshop_builder_3k_model_Page2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page2", None)
        self.__webshop_builder_3k_model_Page2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webshop_builder_3k_model_Reuse_component"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Reuse_component", None)
                    
                    if opp_val == self:
                        setattr(item, "webshop_builder_3k_model_Reuse_component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webshop_builder_3k_model_Reuse_component"):
                    opp_val = getattr(item, "webshop_builder_3k_model_Reuse_component", None)
                    
                    setattr(item, "webshop_builder_3k_model_Reuse_component", self)
                    

    @property
    def webshop_builder_3k_model_Page30(self):
        return self.__webshop_builder_3k_model_Page30

    @webshop_builder_3k_model_Page30.setter
    def webshop_builder_3k_model_Page30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page30", None)
        self.__webshop_builder_3k_model_Page30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k29"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k29", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Webshop_builder_3k29"):
                opp_val = getattr(value, "webshop_builder_3k_model_Webshop_builder_3k29", None)
                setattr(value, "webshop_builder_3k_model_Webshop_builder_3k29", self)

    @property
    def webshop_builder_3k_model_Page27(self):
        return self.__webshop_builder_3k_model_Page27

    @webshop_builder_3k_model_Page27.setter
    def webshop_builder_3k_model_Page27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webshop_builder_3k_model_Page__webshop_builder_3k_model_Page27", None)
        self.__webshop_builder_3k_model_Page27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k26"):
                opp_val = getattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k26", None)
                if opp_val == self:
                    setattr(old_value, "webshop_builder_3k_model_Webshop_builder_3k26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webshop_builder_3k_model_Webshop_builder_3k26"):
                opp_val = getattr(value, "webshop_builder_3k_model_Webshop_builder_3k26", None)
                setattr(value, "webshop_builder_3k_model_Webshop_builder_3k26", self)
