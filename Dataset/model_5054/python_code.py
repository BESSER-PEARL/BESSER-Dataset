from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class amazoninformational_Package:

    pass
class amazoninformational_Invoice:

    pass
class amazoninformational_Payment:

    pass
class amazoninformational_Shipment:

    pass
class amazoninformational_Product:

    def __init__(self, onHand: int, amazoninformational_Product: "amazoninformational_Order" = None, amazoninformational_Product7: "amazoninformational_Package" = None):
        self.onHand = onHand
        self.amazoninformational_Product = amazoninformational_Product
        self.amazoninformational_Product7 = amazoninformational_Product7
        
    @property
    def onHand(self) -> int:
        return self.__onHand

    @onHand.setter
    def onHand(self, onHand: int):
        self.__onHand = onHand

    @property
    def amazoninformational_Product(self):
        return self.__amazoninformational_Product

    @amazoninformational_Product.setter
    def amazoninformational_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Product__amazoninformational_Product", None)
        self.__amazoninformational_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Order"):
                opp_val = getattr(old_value, "amazoninformational_Order", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Order"):
                opp_val = getattr(value, "amazoninformational_Order", None)
                if opp_val is None:
                    setattr(value, "amazoninformational_Order", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def amazoninformational_Product7(self):
        return self.__amazoninformational_Product7

    @amazoninformational_Product7.setter
    def amazoninformational_Product7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_amazoninformational_Product__amazoninformational_Product7", None)
        self.__amazoninformational_Product7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "amazoninformational_Package"):
                opp_val = getattr(old_value, "amazoninformational_Package", None)
                if opp_val == self:
                    setattr(old_value, "amazoninformational_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "amazoninformational_Package"):
                opp_val = getattr(value, "amazoninformational_Package", None)
                setattr(value, "amazoninformational_Package", self)

class amazoninformational_Order:

    pass