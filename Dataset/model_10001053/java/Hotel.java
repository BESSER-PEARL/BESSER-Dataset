





import java.util.List;
import java.util.ArrayList;

public class Hotel  {






    private List<Customer> customers;


    public Hotel(
    ) {
        this.customers = new ArrayList<>();
    }

    public Hotel(
        ArrayList<Customer> customers    ) {
        this.customers = customers;
    }


    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}