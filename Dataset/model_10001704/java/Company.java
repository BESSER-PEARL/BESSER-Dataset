





import java.util.List;
import java.util.ArrayList;

public class Company  {






    private Service service;




    private List<Customer> customers;


    public Company(
    ) {
        this.customers = new ArrayList<>();
    }

    public Company(
        ArrayList<Customer> customers    ) {
        this.customers = customers;
    }


    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}