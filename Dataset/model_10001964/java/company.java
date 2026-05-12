





import java.util.List;
import java.util.ArrayList;

public class company  {

    private String type;
    private String name;
    private int id;





    private List<Customer> customers;


    public company(
        String type,        String name,        int id    ) {
        this.type = type;
        this.name = name;
        this.id = id;
        this.customers = new ArrayList<>();
    }

    public company(
        String type,        String name,        int id        ArrayList<Customer> customers    ) {
        this.type = type;
        this.name = name;
        this.id = id;
        this.customers = customers;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}