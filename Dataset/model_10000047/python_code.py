from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Daily_production:

    def __init__(self, date: str, pro_number: str, item_code: str, section: int, curr_qty: int, item_name: str, future_Qty: int):
        self.date = date
        self.pro_number = pro_number
        self.item_code = item_code
        self.section = section
        self.curr_qty = curr_qty
        self.item_name = item_name
        self.future_Qty = future_Qty
        
        pass
    @property
    def item_name(self):
        return self.__item_name
    @item_name.setter
    def item_name(self, item_name: str):
        self.__item_name = item_name

    @property
    def curr_qty(self):
        return self.__curr_qty
    @curr_qty.setter
    def curr_qty(self, curr_qty: int):
        self.__curr_qty = curr_qty

    @property
    def item_code(self):
        return self.__item_code
    @item_code.setter
    def item_code(self, item_code: str):
        self.__item_code = item_code

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def future_Qty(self):
        return self.__future_Qty
    @future_Qty.setter
    def future_Qty(self, future_Qty: int):
        self.__future_Qty = future_Qty

    @property
    def pro_number(self):
        return self.__pro_number
    @pro_number.setter
    def pro_number(self, pro_number: str):
        self.__pro_number = pro_number

    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: int):
        self.__section = section



class ETF_EPF:

    def __init__(self, no: int, rate: str, type: str, salary21: "Salary" = None):
        self.no = no
        self.rate = rate
        self.type = type
        self.salary21 = salary21
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rate(self):
        return self.__rate
    @rate.setter
    def rate(self, rate: str):
        self.__rate = rate

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def salary21(self):
        return self.__salary21
    @salary21.setter
    def salary21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ETF_EPF__salary21", None)
        self.__salary21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eTF_EPF20"):
                opp_val = getattr(old_value, "eTF_EPF20", None)
                if opp_val == self:
                    setattr(old_value, "eTF_EPF20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eTF_EPF20"):
                opp_val = getattr(value, "eTF_EPF20", None)
                setattr(value, "eTF_EPF20", self)



class Bonus:

    def __init__(self, id: int, type: str, amount: str, IDnum: int, salary19: "Salary" = None):
        self.id = id
        self.type = type
        self.amount = amount
        self.IDnum = IDnum
        self.salary19 = salary19
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def IDnum(self):
        return self.__IDnum
    @IDnum.setter
    def IDnum(self, IDnum: int):
        self.__IDnum = IDnum

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def salary19(self):
        return self.__salary19
    @salary19.setter
    def salary19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bonus__salary19", None)
        self.__salary19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bonus18"):
                opp_val = getattr(old_value, "bonus18", None)
                if opp_val == self:
                    setattr(old_value, "bonus18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bonus18"):
                opp_val = getattr(value, "bonus18", None)
                setattr(value, "bonus18", self)



class Salary:

    def __init__(self, id: int, position: str, Salary: str, employee17: "Employee" = None, bonus18: "Bonus" = None, eTF_EPF20: "ETF_EPF" = None):
        self.id = id
        self.position = position
        self.Salary = Salary
        self.employee17 = employee17
        self.bonus18 = bonus18
        self.eTF_EPF20 = eTF_EPF20
        
        pass
    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: str):
        self.__Salary = Salary

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def employee17(self):
        return self.__employee17
    @employee17.setter
    def employee17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__employee17", None)
        self.__employee17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary16"):
                opp_val = getattr(old_value, "salary16", None)
                if opp_val == self:
                    setattr(old_value, "salary16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary16"):
                opp_val = getattr(value, "salary16", None)
                setattr(value, "salary16", self)

    @property
    def bonus18(self):
        return self.__bonus18
    @bonus18.setter
    def bonus18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__bonus18", None)
        self.__bonus18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary19"):
                opp_val = getattr(old_value, "salary19", None)
                if opp_val == self:
                    setattr(old_value, "salary19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary19"):
                opp_val = getattr(value, "salary19", None)
                setattr(value, "salary19", self)

    @property
    def eTF_EPF20(self):
        return self.__eTF_EPF20
    @eTF_EPF20.setter
    def eTF_EPF20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Salary__eTF_EPF20", None)
        self.__eTF_EPF20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "salary21"):
                opp_val = getattr(old_value, "salary21", None)
                if opp_val == self:
                    setattr(old_value, "salary21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "salary21"):
                opp_val = getattr(value, "salary21", None)
                setattr(value, "salary21", self)



class Order_Sent:

    def __init__(self, sentOrder_id: str, Item_id: str, quantity: str, order_status: str, administrator14: set["Administrator"] = None):
        self.sentOrder_id = sentOrder_id
        self.Item_id = Item_id
        self.quantity = quantity
        self.order_status = order_status
        self.administrator14 = administrator14 if administrator14 is not None else set()
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def sentOrder_id(self):
        return self.__sentOrder_id
    @sentOrder_id.setter
    def sentOrder_id(self, sentOrder_id: str):
        self.__sentOrder_id = sentOrder_id

    @property
    def order_status(self):
        return self.__order_status
    @order_status.setter
    def order_status(self, order_status: str):
        self.__order_status = order_status

    @property
    def Item_id(self):
        return self.__Item_id
    @Item_id.setter
    def Item_id(self, Item_id: str):
        self.__Item_id = Item_id

    @property
    def administrator14(self):
        return self.__administrator14
    @administrator14.setter
    def administrator14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order_Sent__administrator14", None)
        self.__administrator14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "order_Sent15"):
                    opp_val = getattr(item, "order_Sent15", None)
                    
                    if opp_val == self:
                        setattr(item, "order_Sent15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "order_Sent15"):
                    opp_val = getattr(item, "order_Sent15", None)
                    
                    setattr(item, "order_Sent15", self)
                    



class Administrator:

    def __init__(self, username: str, password: str, orders12: set["Orders"] = None, order_Sent15: "Order_Sent" = None):
        self.username = username
        self.password = password
        self.orders12 = orders12 if orders12 is not None else set()
        self.order_Sent15 = order_Sent15
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def orders12(self):
        return self.__orders12
    @orders12.setter
    def orders12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__orders12", None)
        self.__orders12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administrator13"):
                    opp_val = getattr(item, "administrator13", None)
                    
                    if opp_val == self:
                        setattr(item, "administrator13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administrator13"):
                    opp_val = getattr(item, "administrator13", None)
                    
                    setattr(item, "administrator13", self)
                    

    @property
    def order_Sent15(self):
        return self.__order_Sent15
    @order_Sent15.setter
    def order_Sent15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__order_Sent15", None)
        self.__order_Sent15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator14"):
                opp_val = getattr(old_value, "administrator14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator14"):
                opp_val = getattr(value, "administrator14", None)
                if opp_val is None:
                    setattr(value, "administrator14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Worker:

    def __init__(self, section: str, team: int):
        self.section = section
        self.team = team
        
        pass
    @property
    def section(self):
        return self.__section
    @section.setter
    def section(self, section: str):
        self.__section = section

    @property
    def team(self):
        return self.__team
    @team.setter
    def team(self, team: int):
        self.__team = team



class Staff:

    def __init__(self, Position: str):
        self.Position = Position
        
        pass
    @property
    def Position(self):
        return self.__Position
    @Position.setter
    def Position(self, Position: str):
        self.__Position = Position



class Leave:

    def __init__(self, leave_id: str, date: str, from_: str, to: str, leave_type: str, employee10: "Employee" = None):
        self.leave_id = leave_id
        self.date = date
        self.from_ = from_
        self.to = to
        self.leave_type = leave_type
        self.employee10 = employee10
        
        pass
    @property
    def leave_type(self):
        return self.__leave_type
    @leave_type.setter
    def leave_type(self, leave_type: str):
        self.__leave_type = leave_type

    @property
    def from_(self):
        return self.__from_
    @from_.setter
    def from_(self, from_: str):
        self.__from_ = from_

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def to(self):
        return self.__to
    @to.setter
    def to(self, to: str):
        self.__to = to

    @property
    def leave_id(self):
        return self.__leave_id
    @leave_id.setter
    def leave_id(self, leave_id: str):
        self.__leave_id = leave_id

    @property
    def employee10(self):
        return self.__employee10
    @employee10.setter
    def employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Leave__employee10", None)
        self.__employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leave11"):
                opp_val = getattr(old_value, "leave11", None)
                if opp_val == self:
                    setattr(old_value, "leave11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leave11"):
                opp_val = getattr(value, "leave11", None)
                setattr(value, "leave11", self)



class Attendance:

    def __init__(self, att_id: str, in_time: str, out_time: str, work_hours: str, OT_hours: str, date: str, employee9: "Employee" = None):
        self.att_id = att_id
        self.in_time = in_time
        self.out_time = out_time
        self.work_hours = work_hours
        self.OT_hours = OT_hours
        self.date = date
        self.employee9 = employee9
        
        pass
    @property
    def out_time(self):
        return self.__out_time
    @out_time.setter
    def out_time(self, out_time: str):
        self.__out_time = out_time

    @property
    def work_hours(self):
        return self.__work_hours
    @work_hours.setter
    def work_hours(self, work_hours: str):
        self.__work_hours = work_hours

    @property
    def in_time(self):
        return self.__in_time
    @in_time.setter
    def in_time(self, in_time: str):
        self.__in_time = in_time

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def OT_hours(self):
        return self.__OT_hours
    @OT_hours.setter
    def OT_hours(self, OT_hours: str):
        self.__OT_hours = OT_hours

    @property
    def att_id(self):
        return self.__att_id
    @att_id.setter
    def att_id(self, att_id: str):
        self.__att_id = att_id

    @property
    def employee9(self):
        return self.__employee9
    @employee9.setter
    def employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Attendance__employee9", None)
        self.__employee9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance8"):
                opp_val = getattr(old_value, "attendance8", None)
                if opp_val == self:
                    setattr(old_value, "attendance8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance8"):
                opp_val = getattr(value, "attendance8", None)
                setattr(value, "attendance8", self)



class Employee:

    def __init__(self, emp_id: str, fname: str, lname: str, address: str, email: str, phone: int, DOB: str, attendance_count: int, attendance8: "Attendance" = None, leave11: "Leave" = None, salary16: "Salary" = None, section6: set["Section"] = None):
        self.emp_id = emp_id
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email
        self.phone = phone
        self.DOB = DOB
        self.attendance_count = attendance_count
        self.attendance8 = attendance8
        self.leave11 = leave11
        self.salary16 = salary16
        self.section6 = section6 if section6 is not None else set()
        
        pass
    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def attendance_count(self):
        return self.__attendance_count
    @attendance_count.setter
    def attendance_count(self, attendance_count: int):
        self.__attendance_count = attendance_count

    @property
    def emp_id(self):
        return self.__emp_id
    @emp_id.setter
    def emp_id(self, emp_id: str):
        self.__emp_id = emp_id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname: str):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname: str):
        self.__lname = lname

    @property
    def attendance8(self):
        return self.__attendance8
    @attendance8.setter
    def attendance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__attendance8", None)
        self.__attendance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee9"):
                opp_val = getattr(old_value, "employee9", None)
                if opp_val == self:
                    setattr(old_value, "employee9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee9"):
                opp_val = getattr(value, "employee9", None)
                setattr(value, "employee9", self)

    @property
    def leave11(self):
        return self.__leave11
    @leave11.setter
    def leave11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__leave11", None)
        self.__leave11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee10"):
                opp_val = getattr(old_value, "employee10", None)
                if opp_val == self:
                    setattr(old_value, "employee10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee10"):
                opp_val = getattr(value, "employee10", None)
                setattr(value, "employee10", self)

    @property
    def section6(self):
        return self.__section6
    @section6.setter
    def section6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__section6", None)
        self.__section6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee7"):
                    opp_val = getattr(item, "employee7", None)
                    
                    if opp_val == self:
                        setattr(item, "employee7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee7"):
                    opp_val = getattr(item, "employee7", None)
                    
                    setattr(item, "employee7", self)
                    

    @property
    def salary16(self):
        return self.__salary16
    @salary16.setter
    def salary16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__salary16", None)
        self.__salary16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee17"):
                opp_val = getattr(old_value, "employee17", None)
                if opp_val == self:
                    setattr(old_value, "employee17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee17"):
                opp_val = getattr(value, "employee17", None)
                setattr(value, "employee17", self)



class Section:

    def __init__(self, section_id: str, name: str, description: str, employee7: "Employee" = None):
        self.section_id = section_id
        self.name = name
        self.description = description
        self.employee7 = employee7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def section_id(self):
        return self.__section_id
    @section_id.setter
    def section_id(self, section_id: str):
        self.__section_id = section_id

    @property
    def employee7(self):
        return self.__employee7
    @employee7.setter
    def employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Section__employee7", None)
        self.__employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "section6"):
                opp_val = getattr(old_value, "section6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "section6"):
                opp_val = getattr(value, "section6", None)
                if opp_val is None:
                    setattr(value, "section6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Interface_Interface:

    pass


class Items:

    def __init__(self, re_order_qty: str, unit_of_measure: str, price_per_unit: str, item_id: str, item_code: str, description: str, stock3: set["Stock"] = None, orders5: set["Orders"] = None):
        self.re_order_qty = re_order_qty
        self.unit_of_measure = unit_of_measure
        self.price_per_unit = price_per_unit
        self.item_id = item_id
        self.item_code = item_code
        self.description = description
        self.stock3 = stock3 if stock3 is not None else set()
        self.orders5 = orders5 if orders5 is not None else set()
        
        pass
    @property
    def item_code(self):
        return self.__item_code
    @item_code.setter
    def item_code(self, item_code: str):
        self.__item_code = item_code

    @property
    def re_order_qty(self):
        return self.__re_order_qty
    @re_order_qty.setter
    def re_order_qty(self, re_order_qty: str):
        self.__re_order_qty = re_order_qty

    @property
    def unit_of_measure(self):
        return self.__unit_of_measure
    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure: str):
        self.__unit_of_measure = unit_of_measure

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def item_id(self):
        return self.__item_id
    @item_id.setter
    def item_id(self, item_id: str):
        self.__item_id = item_id

    @property
    def price_per_unit(self):
        return self.__price_per_unit
    @price_per_unit.setter
    def price_per_unit(self, price_per_unit: str):
        self.__price_per_unit = price_per_unit

    @property
    def orders5(self):
        return self.__orders5
    @orders5.setter
    def orders5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__orders5", None)
        self.__orders5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "items4"):
                    opp_val = getattr(item, "items4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "items4"):
                    opp_val = getattr(item, "items4", None)
                    
                    if opp_val is None:
                        setattr(item, "items4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def stock3(self):
        return self.__stock3
    @stock3.setter
    def stock3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Items__stock3", None)
        self.__stock3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "items2"):
                    opp_val = getattr(item, "items2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "items2"):
                    opp_val = getattr(item, "items2", None)
                    
                    if opp_val is None:
                        setattr(item, "items2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Stock:

    def __init__(self, stock_id: str, item_id: str, quantity: str, exp_date: str, items2: set["Items"] = None):
        self.stock_id = stock_id
        self.item_id = item_id
        self.quantity = quantity
        self.exp_date = exp_date
        self.items2 = items2 if items2 is not None else set()
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: str):
        self.__quantity = quantity

    @property
    def exp_date(self):
        return self.__exp_date
    @exp_date.setter
    def exp_date(self, exp_date: str):
        self.__exp_date = exp_date

    @property
    def item_id(self):
        return self.__item_id
    @item_id.setter
    def item_id(self, item_id: str):
        self.__item_id = item_id

    @property
    def stock_id(self):
        return self.__stock_id
    @stock_id.setter
    def stock_id(self, stock_id: str):
        self.__stock_id = stock_id

    @property
    def items2(self):
        return self.__items2
    @items2.setter
    def items2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock__items2", None)
        self.__items2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "stock3"):
                    opp_val = getattr(item, "stock3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "stock3"):
                    opp_val = getattr(item, "stock3", None)
                    
                    if opp_val is None:
                        setattr(item, "stock3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Orders:

    def __init__(self, order_id: str, item_id: str, Quantity: str, order_date: str, status: str, recieved_date: str, price_per_unit: str, total_amount: str, administrator13: "Administrator" = None, supplier1: set["Supplier"] = None, items4: set["Items"] = None):
        self.order_id = order_id
        self.item_id = item_id
        self.Quantity = Quantity
        self.order_date = order_date
        self.status = status
        self.recieved_date = recieved_date
        self.price_per_unit = price_per_unit
        self.total_amount = total_amount
        self.administrator13 = administrator13
        self.supplier1 = supplier1 if supplier1 is not None else set()
        self.items4 = items4 if items4 is not None else set()
        
        pass
    @property
    def total_amount(self):
        return self.__total_amount
    @total_amount.setter
    def total_amount(self, total_amount: str):
        self.__total_amount = total_amount

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def item_id(self):
        return self.__item_id
    @item_id.setter
    def item_id(self, item_id: str):
        self.__item_id = item_id

    @property
    def price_per_unit(self):
        return self.__price_per_unit
    @price_per_unit.setter
    def price_per_unit(self, price_per_unit: str):
        self.__price_per_unit = price_per_unit

    @property
    def order_date(self):
        return self.__order_date
    @order_date.setter
    def order_date(self, order_date: str):
        self.__order_date = order_date

    @property
    def order_id(self):
        return self.__order_id
    @order_id.setter
    def order_id(self, order_id: str):
        self.__order_id = order_id

    @property
    def recieved_date(self):
        return self.__recieved_date
    @recieved_date.setter
    def recieved_date(self, recieved_date: str):
        self.__recieved_date = recieved_date

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: str):
        self.__Quantity = Quantity

    @property
    def supplier1(self):
        return self.__supplier1
    @supplier1.setter
    def supplier1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__supplier1", None)
        self.__supplier1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orders0"):
                    opp_val = getattr(item, "orders0", None)
                    
                    if opp_val == self:
                        setattr(item, "orders0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orders0"):
                    opp_val = getattr(item, "orders0", None)
                    
                    setattr(item, "orders0", self)
                    

    @property
    def items4(self):
        return self.__items4
    @items4.setter
    def items4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__items4", None)
        self.__items4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "orders5"):
                    opp_val = getattr(item, "orders5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "orders5"):
                    opp_val = getattr(item, "orders5", None)
                    
                    if opp_val is None:
                        setattr(item, "orders5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def administrator13(self):
        return self.__administrator13
    @administrator13.setter
    def administrator13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Orders__administrator13", None)
        self.__administrator13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "orders12"):
                opp_val = getattr(old_value, "orders12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "orders12"):
                opp_val = getattr(value, "orders12", None)
                if opp_val is None:
                    setattr(value, "orders12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Supplier:

    def __init__(self, Supplier_id: str, name: str, address: str, contact_no: int, email: str, orders0: "Orders" = None):
        self.Supplier_id = Supplier_id
        self.name = name
        self.address = address
        self.contact_no = contact_no
        self.email = email
        self.orders0 = orders0
        
        pass
    @property
    def contact_no(self):
        return self.__contact_no
    @contact_no.setter
    def contact_no(self, contact_no: int):
        self.__contact_no = contact_no

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

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
    def Supplier_id(self):
        return self.__Supplier_id
    @Supplier_id.setter
    def Supplier_id(self, Supplier_id: str):
        self.__Supplier_id = Supplier_id

    @property
    def orders0(self):
        return self.__orders0
    @orders0.setter
    def orders0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supplier__orders0", None)
        self.__orders0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier1"):
                opp_val = getattr(old_value, "supplier1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier1"):
                opp_val = getattr(value, "supplier1", None)
                if opp_val is None:
                    setattr(value, "supplier1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

