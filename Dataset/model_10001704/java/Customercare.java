





import java.util.List;
import java.util.ArrayList;

public class Customercare  {






    private List<Customer> customers;


    public Customercare(
    ) {
        this.customers = new ArrayList<>();
    }

    public Customercare(
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