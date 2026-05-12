





import java.util.List;
import java.util.ArrayList;

public class compuer  {






    private List<customer> customers;


    public compuer(
    ) {
        this.customers = new ArrayList<>();
    }

    public compuer(
        ArrayList<customer> customers    ) {
        this.customers = customers;
    }


    public List<customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}