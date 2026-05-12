





import java.util.List;
import java.util.ArrayList;

public class Products  {

    private int Product_ID;





    private List<Customer> customers;


    public Products(
        int Product_ID    ) {
        this.Product_ID = Product_ID;
        this.customers = new ArrayList<>();
    }

    public Products(
        int Product_ID        ArrayList<Customer> customers    ) {
        this.Product_ID = Product_ID;
        this.customers = customers;
    }

    public int getProduct_id() {
        return Product_ID;
    }

    public void setProduct_id(int Product_ID) {
        this.Product_ID = Product_ID;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}