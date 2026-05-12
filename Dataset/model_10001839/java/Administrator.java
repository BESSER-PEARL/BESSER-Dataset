





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int IDAdm;
    private String Email;
    private String Last_name;
    private String Password;
    private String Name;





    private List<Product> products;




    private List<Customer> customers;


    public Administrator(
        int IDAdm,        String Email,        String Last_name,        String Password,        String Name    ) {
        this.IDAdm = IDAdm;
        this.Email = Email;
        this.Last_name = Last_name;
        this.Password = Password;
        this.Name = Name;
        this.products = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public Administrator(
        int IDAdm,        String Email,        String Last_name,        String Password,        String Name        ArrayList<Product> products,        ArrayList<Customer> customers    ) {
        this.IDAdm = IDAdm;
        this.Email = Email;
        this.Last_name = Last_name;
        this.Password = Password;
        this.Name = Name;
        this.products = products;
        this.customers = customers;
    }

    public int getIdadm() {
        return IDAdm;
    }

    public void setIdadm(int IDAdm) {
        this.IDAdm = IDAdm;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getLast_name() {
        return Last_name;
    }

    public void setLast_name(String Last_name) {
        this.Last_name = Last_name;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}