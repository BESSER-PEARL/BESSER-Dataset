from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MealDeal:

    def __init__(self, name: str, description: str, price: float, isVegetarian: bool, sides14: set["Sides"] = None, pizza16: set["Pizza"] = None, order19: set["Order"] = None):
        self.name = name
        self.description = description
        self.price = price
        self.isVegetarian = isVegetarian
        self.sides14 = sides14 if sides14 is not None else set()
        self.pizza16 = pizza16 if pizza16 is not None else set()
        self.order19 = order19 if order19 is not None else set()
        
        pass
    @property
    def isVegetarian(self):
        return self.__isVegetarian
    @isVegetarian.setter
    def isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sides14(self):
        return self.__sides14
    @sides14.setter
    def sides14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MealDeal__sides14", None)
        self.__sides14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mealDeal15"):
                    opp_val = getattr(item, "mealDeal15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mealDeal15"):
                    opp_val = getattr(item, "mealDeal15", None)
                    
                    if opp_val is None:
                        setattr(item, "mealDeal15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def order19(self):
        return self.__order19
    @order19.setter
    def order19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MealDeal__order19", None)
        self.__order19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mealDeal18"):
                    opp_val = getattr(item, "mealDeal18", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mealDeal18"):
                    opp_val = getattr(item, "mealDeal18", None)
                    
                    if opp_val is None:
                        setattr(item, "mealDeal18", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def pizza16(self):
        return self.__pizza16
    @pizza16.setter
    def pizza16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MealDeal__pizza16", None)
        self.__pizza16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mealDeal17"):
                    opp_val = getattr(item, "mealDeal17", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mealDeal17"):
                    opp_val = getattr(item, "mealDeal17", None)
                    
                    if opp_val is None:
                        setattr(item, "mealDeal17", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Base:

    def __init__(self, name: str, isVegetarian: bool, pizza1: set["Pizza"] = None):
        self.name = name
        self.isVegetarian = isVegetarian
        self.pizza1 = pizza1 if pizza1 is not None else set()
        
        pass
    @property
    def isVegetarian(self):
        return self.__isVegetarian
    @isVegetarian.setter
    def isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pizza1(self):
        return self.__pizza1
    @pizza1.setter
    def pizza1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Base__pizza1", None)
        self.__pizza1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "base0"):
                    opp_val = getattr(item, "base0", None)
                    
                    if opp_val == self:
                        setattr(item, "base0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "base0"):
                    opp_val = getattr(item, "base0", None)
                    
                    setattr(item, "base0", self)
                    



class Address:

    def __init__(self, Line1: str, Line_2: str, City: str, County: str, customer13: "Customer" = None, order21: set["Order"] = None):
        self.Line1 = Line1
        self.Line_2 = Line_2
        self.City = City
        self.County = County
        self.customer13 = customer13
        self.order21 = order21 if order21 is not None else set()
        
        pass
    @property
    def County(self):
        return self.__County
    @County.setter
    def County(self, County: str):
        self.__County = County

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def Line1(self):
        return self.__Line1
    @Line1.setter
    def Line1(self, Line1: str):
        self.__Line1 = Line1

    @property
    def Line_2(self):
        return self.__Line_2
    @Line_2.setter
    def Line_2(self, Line_2: str):
        self.__Line_2 = Line_2

    @property
    def customer13(self):
        return self.__customer13
    @customer13.setter
    def customer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__customer13", None)
        self.__customer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "address12"):
                opp_val = getattr(old_value, "address12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "address12"):
                opp_val = getattr(value, "address12", None)
                if opp_val is None:
                    setattr(value, "address12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order21(self):
        return self.__order21
    @order21.setter
    def order21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Address__order21", None)
        self.__order21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "address20"):
                    opp_val = getattr(item, "address20", None)
                    
                    if opp_val == self:
                        setattr(item, "address20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "address20"):
                    opp_val = getattr(item, "address20", None)
                    
                    setattr(item, "address20", self)
                    



class Sides:

    def __init__(self, isVegetarian: bool, name: str, price: float, mealDeal15: set["MealDeal"] = None, order11: "Order" = None):
        self.isVegetarian = isVegetarian
        self.name = name
        self.price = price
        self.mealDeal15 = mealDeal15 if mealDeal15 is not None else set()
        self.order11 = order11
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def isVegetarian(self):
        return self.__isVegetarian
    @isVegetarian.setter
    def isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mealDeal15(self):
        return self.__mealDeal15
    @mealDeal15.setter
    def mealDeal15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sides__mealDeal15", None)
        self.__mealDeal15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sides14"):
                    opp_val = getattr(item, "sides14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sides14"):
                    opp_val = getattr(item, "sides14", None)
                    
                    if opp_val is None:
                        setattr(item, "sides14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def order11(self):
        return self.__order11
    @order11.setter
    def order11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sides__order11", None)
        self.__order11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sides10"):
                opp_val = getattr(old_value, "sides10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sides10"):
                opp_val = getattr(value, "sides10", None)
                if opp_val is None:
                    setattr(value, "sides10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Toppings:

    def __init__(self, isVegetarian: bool, name: str, pizza7: set["Pizza"] = None):
        self.isVegetarian = isVegetarian
        self.name = name
        self.pizza7 = pizza7 if pizza7 is not None else set()
        
        pass
    @property
    def isVegetarian(self):
        return self.__isVegetarian
    @isVegetarian.setter
    def isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pizza7(self):
        return self.__pizza7
    @pizza7.setter
    def pizza7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Toppings__pizza7", None)
        self.__pizza7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "toppings6"):
                    opp_val = getattr(item, "toppings6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "toppings6"):
                    opp_val = getattr(item, "toppings6", None)
                    
                    if opp_val is None:
                        setattr(item, "toppings6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Pizza:

    def __init__(self, price: float, isVegetarian: bool, mealDeal17: set["MealDeal"] = None, base0: "Base" = None, order3: "Order" = None, toppings6: set["Toppings"] = None):
        self.price = price
        self.isVegetarian = isVegetarian
        self.mealDeal17 = mealDeal17 if mealDeal17 is not None else set()
        self.base0 = base0
        self.order3 = order3
        self.toppings6 = toppings6 if toppings6 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def isVegetarian(self):
        return self.__isVegetarian
    @isVegetarian.setter
    def isVegetarian(self, isVegetarian: bool):
        self.__isVegetarian = isVegetarian

    @property
    def base0(self):
        return self.__base0
    @base0.setter
    def base0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizza__base0", None)
        self.__base0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pizza1"):
                opp_val = getattr(old_value, "pizza1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pizza1"):
                opp_val = getattr(value, "pizza1", None)
                if opp_val is None:
                    setattr(value, "pizza1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def order3(self):
        return self.__order3
    @order3.setter
    def order3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizza__order3", None)
        self.__order3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pizza2"):
                opp_val = getattr(old_value, "pizza2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pizza2"):
                opp_val = getattr(value, "pizza2", None)
                if opp_val is None:
                    setattr(value, "pizza2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def toppings6(self):
        return self.__toppings6
    @toppings6.setter
    def toppings6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizza__toppings6", None)
        self.__toppings6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pizza7"):
                    opp_val = getattr(item, "pizza7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pizza7"):
                    opp_val = getattr(item, "pizza7", None)
                    
                    if opp_val is None:
                        setattr(item, "pizza7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def mealDeal17(self):
        return self.__mealDeal17
    @mealDeal17.setter
    def mealDeal17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizza__mealDeal17", None)
        self.__mealDeal17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pizza16"):
                    opp_val = getattr(item, "pizza16", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pizza16"):
                    opp_val = getattr(item, "pizza16", None)
                    
                    if opp_val is None:
                        setattr(item, "pizza16", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class GPSLocation:

    def __init__(self, GPS: str, order5: "Order" = None):
        self.GPS = GPS
        self.order5 = order5
        
        pass
    @property
    def GPS(self):
        return self.__GPS
    @GPS.setter
    def GPS(self, GPS: str):
        self.__GPS = GPS

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_GPSLocation__order5", None)
        self.__order5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GPS_Location4"):
                opp_val = getattr(old_value, "GPS_Location4", None)
                if opp_val == self:
                    setattr(old_value, "GPS_Location4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GPS_Location4"):
                opp_val = getattr(value, "GPS_Location4", None)
                setattr(value, "GPS_Location4", self)



class Order:

    def __init__(self, orderID: int, date: str, time: int, orderNotes: str, creditCardDetails: str, mealDeal18: set["MealDeal"] = None, address20: "Address" = None, pizza2: set["Pizza"] = None, GPS_Location4: "GPSLocation" = None, customer8: "Customer" = None, sides10: set["Sides"] = None):
        self.orderID = orderID
        self.date = date
        self.time = time
        self.orderNotes = orderNotes
        self.creditCardDetails = creditCardDetails
        self.mealDeal18 = mealDeal18 if mealDeal18 is not None else set()
        self.address20 = address20
        self.pizza2 = pizza2 if pizza2 is not None else set()
        self.GPS_Location4 = GPS_Location4
        self.customer8 = customer8
        self.sides10 = sides10 if sides10 is not None else set()
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def orderID(self):
        return self.__orderID
    @orderID.setter
    def orderID(self, orderID: int):
        self.__orderID = orderID

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def creditCardDetails(self):
        return self.__creditCardDetails
    @creditCardDetails.setter
    def creditCardDetails(self, creditCardDetails: str):
        self.__creditCardDetails = creditCardDetails

    @property
    def orderNotes(self):
        return self.__orderNotes
    @orderNotes.setter
    def orderNotes(self, orderNotes: str):
        self.__orderNotes = orderNotes

    @property
    def sides10(self):
        return self.__sides10
    @sides10.setter
    def sides10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__sides10", None)
        self.__sides10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order11"):
                    opp_val = getattr(item, "order11", None)
                    
                    if opp_val == self:
                        setattr(item, "order11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order11"):
                    opp_val = getattr(item, "order11", None)
                    
                    setattr(item, "order11", self)
                    

    @property
    def mealDeal18(self):
        return self.__mealDeal18
    @mealDeal18.setter
    def mealDeal18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__mealDeal18", None)
        self.__mealDeal18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order19"):
                    opp_val = getattr(item, "order19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order19"):
                    opp_val = getattr(item, "order19", None)
                    
                    if opp_val is None:
                        setattr(item, "order19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def address20(self):
        return self.__address20
    @address20.setter
    def address20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__address20", None)
        self.__address20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order21"):
                opp_val = getattr(old_value, "order21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order21"):
                opp_val = getattr(value, "order21", None)
                if opp_val is None:
                    setattr(value, "order21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def GPS_Location4(self):
        return self.__GPS_Location4
    @GPS_Location4.setter
    def GPS_Location4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__GPS_Location4", None)
        self.__GPS_Location4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if opp_val == self:
                    setattr(old_value, "order5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                setattr(value, "order5", self)

    @property
    def customer8(self):
        return self.__customer8
    @customer8.setter
    def customer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__customer8", None)
        self.__customer8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order9"):
                opp_val = getattr(old_value, "order9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order9"):
                opp_val = getattr(value, "order9", None)
                if opp_val is None:
                    setattr(value, "order9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pizza2(self):
        return self.__pizza2
    @pizza2.setter
    def pizza2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__pizza2", None)
        self.__pizza2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    if opp_val == self:
                        setattr(item, "order3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order3"):
                    opp_val = getattr(item, "order3", None)
                    
                    setattr(item, "order3", self)
                    



class Customer:

    def __init__(self, customerID: int, customerName: str, phoneNumber: int, order9: set["Order"] = None, address12: set["Address"] = None):
        self.customerID = customerID
        self.customerName = customerName
        self.phoneNumber = phoneNumber
        self.order9 = order9 if order9 is not None else set()
        self.address12 = address12 if address12 is not None else set()
        
        pass
    @property
    def customerID(self):
        return self.__customerID
    @customerID.setter
    def customerID(self, customerID: int):
        self.__customerID = customerID

    @property
    def customerName(self):
        return self.__customerName
    @customerName.setter
    def customerName(self, customerName: str):
        self.__customerName = customerName

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

    @property
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__order9", None)
        self.__order9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer8"):
                    opp_val = getattr(item, "customer8", None)
                    
                    if opp_val == self:
                        setattr(item, "customer8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer8"):
                    opp_val = getattr(item, "customer8", None)
                    
                    setattr(item, "customer8", self)
                    

    @property
    def address12(self):
        return self.__address12
    @address12.setter
    def address12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__address12", None)
        self.__address12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer13"):
                    opp_val = getattr(item, "customer13", None)
                    
                    if opp_val == self:
                        setattr(item, "customer13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer13"):
                    opp_val = getattr(item, "customer13", None)
                    
                    setattr(item, "customer13", self)
                    

