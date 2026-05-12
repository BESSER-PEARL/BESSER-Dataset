





import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int customerID;
    private String price;
    private int orderID;





    private List<Customer> customers;




    private List<BooksOrder> booksorders;


    public ShoppingCart(
        int customerID,        String price,        int orderID    ) {
        this.customerID = customerID;
        this.price = price;
        this.orderID = orderID;
        this.customers = new ArrayList<>();
        this.booksorders = new ArrayList<>();
    }

    public ShoppingCart(
        int customerID,        String price,        int orderID        ArrayList<Customer> customers,        ArrayList<BooksOrder> booksorders    ) {
        this.customerID = customerID;
        this.price = price;
        this.orderID = orderID;
        this.customers = customers;
        this.booksorders = booksorders;
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
    public int getOrderid() {
        return orderID;
    }

    public void setOrderid(int orderID) {
        this.orderID = orderID;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public List<BooksOrder> getBooksorders() {
        return booksorders;
    }

    public void addBooksorder(Booksorder booksorder) {
        this.booksorders.add(booksorder);
    }

}