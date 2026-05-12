





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int Date;





    private List<Customer> customers;


    public Shopping_Cart(
        int Date    ) {
        this.Date = Date;
        this.customers = new ArrayList<>();
    }

    public Shopping_Cart(
        int Date        ArrayList<Customer> customers    ) {
        this.Date = Date;
        this.customers = customers;
    }

    public int getDate() {
        return Date;
    }

    public void setDate(int Date) {
        this.Date = Date;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}