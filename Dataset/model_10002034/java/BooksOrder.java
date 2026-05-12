





import java.util.List;
import java.util.ArrayList;

public class BooksOrder  {

    private int orderID;
    private int customerID;
    private String price;
    private int quantity;





    private List<Customer> customers;


    public BooksOrder(
        int orderID,        int customerID,        String price,        int quantity    ) {
        this.orderID = orderID;
        this.customerID = customerID;
        this.price = price;
        this.quantity = quantity;
        this.customers = new ArrayList<>();
    }

    public BooksOrder(
        int orderID,        int customerID,        String price,        int quantity        ArrayList<Customer> customers    ) {
        this.orderID = orderID;
        this.customerID = customerID;
        this.price = price;
        this.quantity = quantity;
        this.customers = customers;
    }

    public int getOrderid() {
        return orderID;
    }

    public void setOrderid(int orderID) {
        this.orderID = orderID;
    }
    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}