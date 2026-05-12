





import java.util.List;
import java.util.ArrayList;

public class Customer_Data  {

    private String Name;
    private String Contact;





    private Store store;




    private Online_Portal online_portal;




    private List<Terminal> terminals;




    private Order order;




    private List<Customer> customers;


    public Customer_Data(
        String Name,        String Contact    ) {
        this.Name = Name;
        this.Contact = Contact;
        this.terminals = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public Customer_Data(
        String Name,        String Contact        ArrayList<Terminal> terminals,        ArrayList<Customer> customers    ) {
        this.Name = Name;
        this.Contact = Contact;
        this.terminals = terminals;
        this.customers = customers;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getContact() {
        return Contact;
    }

    public void setContact(String Contact) {
        this.Contact = Contact;
    }

    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }
    public Online_Portal getOnline_portal() {
        return online_portal;
    }

    public void setOnline_portal(Online_Portal online_portal) {
        this.online_portal = online_portal;
    }
    public List<Terminal> getTerminals() {
        return terminals;
    }

    public void addTerminal(Terminal terminal) {
        this.terminals.add(terminal);
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}