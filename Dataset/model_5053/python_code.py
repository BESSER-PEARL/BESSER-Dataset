from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person:

    pass
class hairDressersRegSys_ServiceEmployee(Person):

    def __init__(self, Role: str, EmployeeId: int, hairDressersRegSys_ServiceEmployee: set["hairDressersRegSys_Appointment"] = None):
        self.Role = Role
        self.EmployeeId = EmployeeId
        self.hairDressersRegSys_ServiceEmployee = hairDressersRegSys_ServiceEmployee if hairDressersRegSys_ServiceEmployee is not None else set()
        
    @property
    def Role(self) -> str:
        return self.__Role

    @Role.setter
    def Role(self, Role: str):
        self.__Role = Role

    @property
    def EmployeeId(self) -> int:
        return self.__EmployeeId

    @EmployeeId.setter
    def EmployeeId(self, EmployeeId: int):
        self.__EmployeeId = EmployeeId

    @property
    def hairDressersRegSys_ServiceEmployee(self):
        return self.__hairDressersRegSys_ServiceEmployee

    @hairDressersRegSys_ServiceEmployee.setter
    def hairDressersRegSys_ServiceEmployee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_ServiceEmployee__hairDressersRegSys_ServiceEmployee", None)
        self.__hairDressersRegSys_ServiceEmployee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hairDressersRegSys_Appointment18"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment18", None)
                    
                    if opp_val == self:
                        setattr(item, "hairDressersRegSys_Appointment18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hairDressersRegSys_Appointment18"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment18", None)
                    
                    setattr(item, "hairDressersRegSys_Appointment18", self)
                    

    def ViewAppointments(self):
        # TODO: Implement ViewAppointments method
        pass

    def MakeAppointment(self):
        # TODO: Implement MakeAppointment method
        pass

    def RemoveAppointment(self):
        # TODO: Implement RemoveAppointment method
        pass

    def ViewAllAvailableEmployees(self):
        # TODO: Implement ViewAllAvailableEmployees method
        pass

    def AddNewEmployee(self):
        # TODO: Implement AddNewEmployee method
        pass

class Service:

    pass
class hairDressersRegSys_Haircuts(Service):

    def __init__(self, IsWash: bool, IsShave: bool, IsCut: bool):
        self.IsWash = IsWash
        self.IsShave = IsShave
        self.IsCut = IsCut
        
    @property
    def IsCut(self) -> bool:
        return self.__IsCut

    @IsCut.setter
    def IsCut(self, IsCut: bool):
        self.__IsCut = IsCut

    @property
    def IsShave(self) -> bool:
        return self.__IsShave

    @IsShave.setter
    def IsShave(self, IsShave: bool):
        self.__IsShave = IsShave

    @property
    def IsWash(self) -> bool:
        return self.__IsWash

    @IsWash.setter
    def IsWash(self, IsWash: bool):
        self.__IsWash = IsWash

class hairDressersRegSys_Other(Service):

    def __init__(self, AdditionalInformation: str):
        self.AdditionalInformation = AdditionalInformation
        
    @property
    def AdditionalInformation(self) -> str:
        return self.__AdditionalInformation

    @AdditionalInformation.setter
    def AdditionalInformation(self, AdditionalInformation: str):
        self.__AdditionalInformation = AdditionalInformation

class hairDressersRegSys_Styling(Service):

    def __init__(self, IsWash: bool):
        self.IsWash = IsWash
        
    @property
    def IsWash(self) -> bool:
        return self.__IsWash

    @IsWash.setter
    def IsWash(self, IsWash: bool):
        self.__IsWash = IsWash

class hairDressersRegSys_Person:

    def __init__(self, FirstName: str, LastName: str, Address: str, DateOfBirth: date):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address
        self.DateOfBirth = DateOfBirth
        
    @property
    def FirstName(self) -> str:
        return self.__FirstName

    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def LastName(self) -> str:
        return self.__LastName

    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def DateOfBirth(self) -> date:
        return self.__DateOfBirth

    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: date):
        self.__DateOfBirth = DateOfBirth

    @property
    def Address(self) -> str:
        return self.__Address

    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    def GetAge(self) -> int:
        # TODO: Implement GetAge method
        pass

class hairDressersRegSys_Products:

    def __init__(self, Name: str, Description: str, Price: str, Products: "hairDressersRegSys_Invoice" = None, products: "hairDressersRegSys_Invoice" = None):
        self.Name = Name
        self.Description = Description
        self.Price = Price
        self.Products = Products
        self.products = products
        
    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Price(self) -> str:
        return self.__Price

    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Products(self):
        return self.__Products

    @Products.setter
    def Products(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Products__Products", None)
        self.__Products = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoice"):
                opp_val = getattr(old_value, "invoice", None)
                if opp_val == self:
                    setattr(old_value, "invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoice"):
                opp_val = getattr(value, "invoice", None)
                setattr(value, "invoice", self)

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Products__products", None)
        self.__products = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Invoice"):
                opp_val = getattr(old_value, "Invoice", None)
                if opp_val == self:
                    setattr(old_value, "Invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Invoice"):
                opp_val = getattr(value, "Invoice", None)
                setattr(value, "Invoice", self)

    def ViewTotalStock(self):
        # TODO: Implement ViewTotalStock method
        pass

    def AddProduct(self):
        # TODO: Implement AddProduct method
        pass

class hairDressersRegSys_Invoice:

    def __init__(self, Date: str, InvoiceNumber: int, Total: str, invoice: "hairDressersRegSys_Products" = None, invoice6: "hairDressersRegSys_Discounts" = None, invoice8: "hairDressersRegSys_Payment" = None, Invoice12: "hairDressersRegSys_Discounts" = None, hairDressersRegSys_Invoice: "hairDressersRegSys_Appointment" = None, Invoice: "hairDressersRegSys_Products" = None, Invoice20: "hairDressersRegSys_Payment" = None):
        self.Date = Date
        self.InvoiceNumber = InvoiceNumber
        self.Total = Total
        self.invoice = invoice
        self.invoice6 = invoice6
        self.invoice8 = invoice8
        self.Invoice12 = Invoice12
        self.hairDressersRegSys_Invoice = hairDressersRegSys_Invoice
        self.Invoice = Invoice
        self.Invoice20 = Invoice20
        
    @property
    def InvoiceNumber(self) -> int:
        return self.__InvoiceNumber

    @InvoiceNumber.setter
    def InvoiceNumber(self, InvoiceNumber: int):
        self.__InvoiceNumber = InvoiceNumber

    @property
    def Total(self) -> str:
        return self.__Total

    @Total.setter
    def Total(self, Total: str):
        self.__Total = Total

    @property
    def Date(self) -> str:
        return self.__Date

    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Invoice12(self):
        return self.__Invoice12

    @Invoice12.setter
    def Invoice12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__Invoice12", None)
        self.__Invoice12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discounts11"):
                opp_val = getattr(old_value, "discounts11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discounts11"):
                opp_val = getattr(value, "discounts11", None)
                if opp_val is None:
                    setattr(value, "discounts11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invoice8(self):
        return self.__invoice8

    @invoice8.setter
    def invoice8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__invoice8", None)
        self.__invoice8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Payment"):
                opp_val = getattr(old_value, "Payment", None)
                if opp_val == self:
                    setattr(old_value, "Payment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Payment"):
                opp_val = getattr(value, "Payment", None)
                setattr(value, "Payment", self)

    @property
    def Invoice20(self):
        return self.__Invoice20

    @Invoice20.setter
    def Invoice20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__Invoice20", None)
        self.__Invoice20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment"):
                opp_val = getattr(old_value, "payment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment"):
                opp_val = getattr(value, "payment", None)
                if opp_val is None:
                    setattr(value, "payment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__invoice", None)
        self.__invoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Products"):
                opp_val = getattr(old_value, "Products", None)
                if opp_val == self:
                    setattr(old_value, "Products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Products"):
                opp_val = getattr(value, "Products", None)
                setattr(value, "Products", self)

    @property
    def invoice6(self):
        return self.__invoice6

    @invoice6.setter
    def invoice6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__invoice6", None)
        self.__invoice6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Discounts"):
                opp_val = getattr(old_value, "Discounts", None)
                if opp_val == self:
                    setattr(old_value, "Discounts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Discounts"):
                opp_val = getattr(value, "Discounts", None)
                setattr(value, "Discounts", self)

    @property
    def Invoice(self):
        return self.__Invoice

    @Invoice.setter
    def Invoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__Invoice", None)
        self.__Invoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "products"):
                opp_val = getattr(old_value, "products", None)
                if opp_val == self:
                    setattr(old_value, "products", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "products"):
                opp_val = getattr(value, "products", None)
                setattr(value, "products", self)

    @property
    def hairDressersRegSys_Invoice(self):
        return self.__hairDressersRegSys_Invoice

    @hairDressersRegSys_Invoice.setter
    def hairDressersRegSys_Invoice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Invoice__hairDressersRegSys_Invoice", None)
        self.__hairDressersRegSys_Invoice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hairDressersRegSys_Appointment2"):
                opp_val = getattr(old_value, "hairDressersRegSys_Appointment2", None)
                if opp_val == self:
                    setattr(old_value, "hairDressersRegSys_Appointment2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hairDressersRegSys_Appointment2"):
                opp_val = getattr(value, "hairDressersRegSys_Appointment2", None)
                setattr(value, "hairDressersRegSys_Appointment2", self)

    def CalculateTotal(self):
        # TODO: Implement CalculateTotal method
        pass

    def GetDiscount(self):
        # TODO: Implement GetDiscount method
        pass

class hairDressersRegSys_Appointment:

    def __init__(self, Date: date, StartTime: date, EndTime: date, hairDressersRegSys_Appointment: "hairDressersRegSys_Service" = None, hairDressersRegSys_Appointment2: "hairDressersRegSys_Invoice" = None, hairDressersRegSys_Appointment18: "hairDressersRegSys_ServiceEmployee" = None, hairDressersRegSys_Appointment14: "hairDressersRegSys_Customer" = None):
        self.Date = Date
        self.StartTime = StartTime
        self.EndTime = EndTime
        self.hairDressersRegSys_Appointment = hairDressersRegSys_Appointment
        self.hairDressersRegSys_Appointment2 = hairDressersRegSys_Appointment2
        self.hairDressersRegSys_Appointment18 = hairDressersRegSys_Appointment18
        self.hairDressersRegSys_Appointment14 = hairDressersRegSys_Appointment14
        
    @property
    def EndTime(self) -> date:
        return self.__EndTime

    @EndTime.setter
    def EndTime(self, EndTime: date):
        self.__EndTime = EndTime

    @property
    def Date(self) -> date:
        return self.__Date

    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def StartTime(self) -> date:
        return self.__StartTime

    @StartTime.setter
    def StartTime(self, StartTime: date):
        self.__StartTime = StartTime

    @property
    def hairDressersRegSys_Appointment2(self):
        return self.__hairDressersRegSys_Appointment2

    @hairDressersRegSys_Appointment2.setter
    def hairDressersRegSys_Appointment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Appointment__hairDressersRegSys_Appointment2", None)
        self.__hairDressersRegSys_Appointment2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hairDressersRegSys_Invoice"):
                opp_val = getattr(old_value, "hairDressersRegSys_Invoice", None)
                if opp_val == self:
                    setattr(old_value, "hairDressersRegSys_Invoice", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hairDressersRegSys_Invoice"):
                opp_val = getattr(value, "hairDressersRegSys_Invoice", None)
                setattr(value, "hairDressersRegSys_Invoice", self)

    @property
    def hairDressersRegSys_Appointment18(self):
        return self.__hairDressersRegSys_Appointment18

    @hairDressersRegSys_Appointment18.setter
    def hairDressersRegSys_Appointment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Appointment__hairDressersRegSys_Appointment18", None)
        self.__hairDressersRegSys_Appointment18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hairDressersRegSys_ServiceEmployee"):
                opp_val = getattr(old_value, "hairDressersRegSys_ServiceEmployee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hairDressersRegSys_ServiceEmployee"):
                opp_val = getattr(value, "hairDressersRegSys_ServiceEmployee", None)
                if opp_val is None:
                    setattr(value, "hairDressersRegSys_ServiceEmployee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hairDressersRegSys_Appointment14(self):
        return self.__hairDressersRegSys_Appointment14

    @hairDressersRegSys_Appointment14.setter
    def hairDressersRegSys_Appointment14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Appointment__hairDressersRegSys_Appointment14", None)
        self.__hairDressersRegSys_Appointment14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hairDressersRegSys_Customer"):
                opp_val = getattr(old_value, "hairDressersRegSys_Customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hairDressersRegSys_Customer"):
                opp_val = getattr(value, "hairDressersRegSys_Customer", None)
                if opp_val is None:
                    setattr(value, "hairDressersRegSys_Customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hairDressersRegSys_Appointment(self):
        return self.__hairDressersRegSys_Appointment

    @hairDressersRegSys_Appointment.setter
    def hairDressersRegSys_Appointment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Appointment__hairDressersRegSys_Appointment", None)
        self.__hairDressersRegSys_Appointment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hairDressersRegSys_Service"):
                opp_val = getattr(old_value, "hairDressersRegSys_Service", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hairDressersRegSys_Service"):
                opp_val = getattr(value, "hairDressersRegSys_Service", None)
                if opp_val is None:
                    setattr(value, "hairDressersRegSys_Service", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def AddAppointment(self):
        # TODO: Implement AddAppointment method
        pass

    def ViewSchedule(self):
        # TODO: Implement ViewSchedule method
        pass

class hairDressersRegSys_Customer(Person):

    def __init__(self, CustomerId: int, Customer: "hairDressersRegSys_Discounts" = None, hairDressersRegSys_Customer: set["hairDressersRegSys_Appointment"] = None, customer: "hairDressersRegSys_Discounts" = None):
        self.CustomerId = CustomerId
        self.Customer = Customer
        self.hairDressersRegSys_Customer = hairDressersRegSys_Customer if hairDressersRegSys_Customer is not None else set()
        self.customer = customer
        
    @property
    def CustomerId(self) -> int:
        return self.__CustomerId

    @CustomerId.setter
    def CustomerId(self, CustomerId: int):
        self.__CustomerId = CustomerId

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Customer__customer", None)
        self.__customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Discounts16"):
                opp_val = getattr(old_value, "Discounts16", None)
                if opp_val == self:
                    setattr(old_value, "Discounts16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Discounts16"):
                opp_val = getattr(value, "Discounts16", None)
                setattr(value, "Discounts16", self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discounts"):
                opp_val = getattr(old_value, "discounts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discounts"):
                opp_val = getattr(value, "discounts", None)
                if opp_val is None:
                    setattr(value, "discounts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hairDressersRegSys_Customer(self):
        return self.__hairDressersRegSys_Customer

    @hairDressersRegSys_Customer.setter
    def hairDressersRegSys_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Customer__hairDressersRegSys_Customer", None)
        self.__hairDressersRegSys_Customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hairDressersRegSys_Appointment14"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment14", None)
                    
                    if opp_val == self:
                        setattr(item, "hairDressersRegSys_Appointment14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hairDressersRegSys_Appointment14"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment14", None)
                    
                    setattr(item, "hairDressersRegSys_Appointment14", self)
                    

    def PlaceAppointment(self):
        # TODO: Implement PlaceAppointment method
        pass

    def AddNewCustomer(self):
        # TODO: Implement AddNewCustomer method
        pass

class hairDressersRegSys_Payment:

    def __init__(self, PaymentMethod: str, Date: date, AmountPaid: str, Payment: "hairDressersRegSys_Invoice" = None, payment: set["hairDressersRegSys_Invoice"] = None):
        self.PaymentMethod = PaymentMethod
        self.Date = Date
        self.AmountPaid = AmountPaid
        self.Payment = Payment
        self.payment = payment if payment is not None else set()
        
    @property
    def Date(self) -> date:
        return self.__Date

    @Date.setter
    def Date(self, Date: date):
        self.__Date = Date

    @property
    def AmountPaid(self) -> str:
        return self.__AmountPaid

    @AmountPaid.setter
    def AmountPaid(self, AmountPaid: str):
        self.__AmountPaid = AmountPaid

    @property
    def PaymentMethod(self) -> str:
        return self.__PaymentMethod

    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod: str):
        self.__PaymentMethod = PaymentMethod

    @property
    def Payment(self):
        return self.__Payment

    @Payment.setter
    def Payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Payment__Payment", None)
        self.__Payment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoice8"):
                opp_val = getattr(old_value, "invoice8", None)
                if opp_val == self:
                    setattr(old_value, "invoice8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoice8"):
                opp_val = getattr(value, "invoice8", None)
                setattr(value, "invoice8", self)

    @property
    def payment(self):
        return self.__payment

    @payment.setter
    def payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Payment__payment", None)
        self.__payment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invoice20"):
                    opp_val = getattr(item, "Invoice20", None)
                    
                    if opp_val == self:
                        setattr(item, "Invoice20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invoice20"):
                    opp_val = getattr(item, "Invoice20", None)
                    
                    setattr(item, "Invoice20", self)
                    

    def MakePayment(self):
        # TODO: Implement MakePayment method
        pass

class hairDressersRegSys_Discounts:

    def __init__(self, Name: str, Description: str, Percentage: int, Discounts: "hairDressersRegSys_Invoice" = None, discounts: set["hairDressersRegSys_Customer"] = None, discounts11: set["hairDressersRegSys_Invoice"] = None, Discounts16: "hairDressersRegSys_Customer" = None):
        self.Name = Name
        self.Description = Description
        self.Percentage = Percentage
        self.Discounts = Discounts
        self.discounts = discounts if discounts is not None else set()
        self.discounts11 = discounts11 if discounts11 is not None else set()
        self.Discounts16 = Discounts16
        
    @property
    def Percentage(self) -> int:
        return self.__Percentage

    @Percentage.setter
    def Percentage(self, Percentage: int):
        self.__Percentage = Percentage

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def discounts(self):
        return self.__discounts

    @discounts.setter
    def discounts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Discounts__discounts", None)
        self.__discounts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    setattr(item, "Customer", self)
                    

    @property
    def Discounts16(self):
        return self.__Discounts16

    @Discounts16.setter
    def Discounts16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Discounts__Discounts16", None)
        self.__Discounts16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if opp_val == self:
                    setattr(old_value, "customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                setattr(value, "customer", self)

    @property
    def Discounts(self):
        return self.__Discounts

    @Discounts.setter
    def Discounts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Discounts__Discounts", None)
        self.__Discounts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "invoice6"):
                opp_val = getattr(old_value, "invoice6", None)
                if opp_val == self:
                    setattr(old_value, "invoice6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "invoice6"):
                opp_val = getattr(value, "invoice6", None)
                setattr(value, "invoice6", self)

    @property
    def discounts11(self):
        return self.__discounts11

    @discounts11.setter
    def discounts11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Discounts__discounts11", None)
        self.__discounts11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Invoice12"):
                    opp_val = getattr(item, "Invoice12", None)
                    
                    if opp_val == self:
                        setattr(item, "Invoice12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Invoice12"):
                    opp_val = getattr(item, "Invoice12", None)
                    
                    setattr(item, "Invoice12", self)
                    

class hairDressersRegSys_Service:

    def __init__(self, Name: str, Description: str, CostPerHour: str, Time: date, hairDressersRegSys_Service: set["hairDressersRegSys_Appointment"] = None):
        self.Name = Name
        self.Description = Description
        self.CostPerHour = CostPerHour
        self.Time = Time
        self.hairDressersRegSys_Service = hairDressersRegSys_Service if hairDressersRegSys_Service is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Time(self) -> date:
        return self.__Time

    @Time.setter
    def Time(self, Time: date):
        self.__Time = Time

    @property
    def Description(self) -> str:
        return self.__Description

    @Description.setter
    def Description(self, Description: str):
        self.__Description = Description

    @property
    def CostPerHour(self) -> str:
        return self.__CostPerHour

    @CostPerHour.setter
    def CostPerHour(self, CostPerHour: str):
        self.__CostPerHour = CostPerHour

    @property
    def hairDressersRegSys_Service(self):
        return self.__hairDressersRegSys_Service

    @hairDressersRegSys_Service.setter
    def hairDressersRegSys_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hairDressersRegSys_Service__hairDressersRegSys_Service", None)
        self.__hairDressersRegSys_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hairDressersRegSys_Appointment"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment", None)
                    
                    if opp_val == self:
                        setattr(item, "hairDressersRegSys_Appointment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hairDressersRegSys_Appointment"):
                    opp_val = getattr(item, "hairDressersRegSys_Appointment", None)
                    
                    setattr(item, "hairDressersRegSys_Appointment", self)
                    

    def RemoveService(self):
        # TODO: Implement RemoveService method
        pass

    def AddService(self):
        # TODO: Implement AddService method
        pass

    def ViewAllServices(self):
        # TODO: Implement ViewAllServices method
        pass
