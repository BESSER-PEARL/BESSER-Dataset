





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None Orderlist;
    private None customer_address;
    private None customername;
    private None Amount;
    private None customerphone;
    private None customer_email;





    private Order_management_System order_management_system;


    public Order(
        None Orderlist,        None customer_address,        None customername,        None Amount,        None customerphone,        None customer_email    ) {
        this.Orderlist = Orderlist;
        this.customer_address = customer_address;
        this.customername = customername;
        this.Amount = Amount;
        this.customerphone = customerphone;
        this.customer_email = customer_email;
    }


    public None getOrderlist() {
        return Orderlist;
    }

    public void setOrderlist(None Orderlist) {
        this.Orderlist = Orderlist;
    }
    public None getCustomer_address() {
        return customer_address;
    }

    public void setCustomer_address(None customer_address) {
        this.customer_address = customer_address;
    }
    public None getCustomername() {
        return customername;
    }

    public void setCustomername(None customername) {
        this.customername = customername;
    }
    public None getAmount() {
        return Amount;
    }

    public void setAmount(None Amount) {
        this.Amount = Amount;
    }
    public None getCustomerphone() {
        return customerphone;
    }

    public void setCustomerphone(None customerphone) {
        this.customerphone = customerphone;
    }
    public None getCustomer_email() {
        return customer_email;
    }

    public void setCustomer_email(None customer_email) {
        this.customer_email = customer_email;
    }

    public Order_management_System getOrder_management_system() {
        return order_management_system;
    }

    public void setOrder_management_system(Order_management_System order_management_system) {
        this.order_management_system = order_management_system;
    }

}