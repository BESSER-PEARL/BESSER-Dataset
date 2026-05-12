





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int id;
    private None billing_address;





    private Bill bill;




    private Order order;




    private Shopping_cart shopping_cart;




    private Customer customer;


    public Account(
        int id,        None billing_address    ) {
        this.id = id;
        this.billing_address = billing_address;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getBilling_address() {
        return billing_address;
    }

    public void setBilling_address(None billing_address) {
        this.billing_address = billing_address;
    }

    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Shopping_cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}