





import java.util.List;
import java.util.ArrayList;

public class System_order  {

    private String Customer_Name;
    private int Order_ID;
    private int Date;
    private int Delivery_Charges;
    private int Customer_ID;
    private int Total;
    private String Payment_Option;
    private int Time;





    private Customer customer;


    public System_order(
        String Customer_Name,        int Order_ID,        int Date,        int Delivery_Charges,        int Customer_ID,        int Total,        String Payment_Option,        int Time    ) {
        this.Customer_Name = Customer_Name;
        this.Order_ID = Order_ID;
        this.Date = Date;
        this.Delivery_Charges = Delivery_Charges;
        this.Customer_ID = Customer_ID;
        this.Total = Total;
        this.Payment_Option = Payment_Option;
        this.Time = Time;
    }


    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public int getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(int Order_ID) {
        this.Order_ID = Order_ID;
    }
    public int getDate() {
        return Date;
    }

    public void setDate(int Date) {
        this.Date = Date;
    }
    public int getDelivery_charges() {
        return Delivery_Charges;
    }

    public void setDelivery_charges(int Delivery_Charges) {
        this.Delivery_Charges = Delivery_Charges;
    }
    public int getCustomer_id() {
        return Customer_ID;
    }

    public void setCustomer_id(int Customer_ID) {
        this.Customer_ID = Customer_ID;
    }
    public int getTotal() {
        return Total;
    }

    public void setTotal(int Total) {
        this.Total = Total;
    }
    public String getPayment_option() {
        return Payment_Option;
    }

    public void setPayment_option(String Payment_Option) {
        this.Payment_Option = Payment_Option;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}