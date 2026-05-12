





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private None Billing_address;
    private None Customer_name;
    private None Total_Price;





    private Order order;




    private Customer customer;


    public Bill(
        None Billing_address,        None Customer_name,        None Total_Price    ) {
        this.Billing_address = Billing_address;
        this.Customer_name = Customer_name;
        this.Total_Price = Total_Price;
    }


    public None getBilling_address() {
        return Billing_address;
    }

    public void setBilling_address(None Billing_address) {
        this.Billing_address = Billing_address;
    }
    public None getCustomer_name() {
        return Customer_name;
    }

    public void setCustomer_name(None Customer_name) {
        this.Customer_name = Customer_name;
    }
    public None getTotal_price() {
        return Total_Price;
    }

    public void setTotal_price(None Total_Price) {
        this.Total_Price = Total_Price;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}