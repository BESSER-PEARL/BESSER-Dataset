





import java.util.List;
import java.util.ArrayList;

public class System_order  {

    private int Date;
    private int Customer_ID;
    private String Customer_Name;
    private int Delivery_Charges;
    private int Order_ID;
    private int Total;
    private int Time;
    private String Payment_Option;





    private Customer customer;


    public System_order(
        int Date,        int Customer_ID,        String Customer_Name,        int Delivery_Charges,        int Order_ID,        int Total,        int Time,        String Payment_Option    ) {
        this.Date = Date;
        this.Customer_ID = Customer_ID;
        this.Customer_Name = Customer_Name;
        this.Delivery_Charges = Delivery_Charges;
        this.Order_ID = Order_ID;
        this.Total = Total;
        this.Time = Time;
        this.Payment_Option = Payment_Option;
    }


    public int getDate() {
        return Date;
    }

    public void setDate(int Date) {
        this.Date = Date;
    }
    public int getCustomer_id() {
        return Customer_ID;
    }

    public void setCustomer_id(int Customer_ID) {
        this.Customer_ID = Customer_ID;
    }
    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public int getDelivery_charges() {
        return Delivery_Charges;
    }

    public void setDelivery_charges(int Delivery_Charges) {
        this.Delivery_Charges = Delivery_Charges;
    }
    public int getOrder_id() {
        return Order_ID;
    }

    public void setOrder_id(int Order_ID) {
        this.Order_ID = Order_ID;
    }
    public int getTotal() {
        return Total;
    }

    public void setTotal(int Total) {
        this.Total = Total;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }
    public String getPayment_option() {
        return Payment_Option;
    }

    public void setPayment_option(String Payment_Option) {
        this.Payment_Option = Payment_Option;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}