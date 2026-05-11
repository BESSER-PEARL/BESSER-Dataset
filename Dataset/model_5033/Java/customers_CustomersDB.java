





import java.util.List;
import java.util.ArrayList;

public class customers_CustomersDB  {

    private String comment;





    private List<customers_Customer> customers_customers;


    public customers_CustomersDB(
        String comment    ) {
        this.comment = comment;
        this.customers_customers = new ArrayList<>();
    }

    public customers_CustomersDB(
        String comment        ArrayList<customers_Customer> customers_customers    ) {
        this.comment = comment;
        this.customers_customers = customers_customers;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<customers_Customer> getCustomers_customers() {
        return customers_customers;
    }

    public void addCustomers_customer(Customers_customer customers_customer) {
        this.customers_customers.add(customers_customer);
    }

}