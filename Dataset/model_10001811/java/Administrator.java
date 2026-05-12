





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private String Password;
    private String Last_name;
    private int IDAdm;
    private String Name;
    private String Email;





    private List<Product> products;




    private List<Customer> customers;


    public Administrator(
        String Password,        String Last_name,        int IDAdm,        String Name,        String Email    ) {
        this.Password = Password;
        this.Last_name = Last_name;
        this.IDAdm = IDAdm;
        this.Name = Name;
        this.Email = Email;
        this.products = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public Administrator(
        String Password,        String Last_name,        int IDAdm,        String Name,        String Email        ArrayList<Product> products,        ArrayList<Customer> customers    ) {
        this.Password = Password;
        this.Last_name = Last_name;
        this.IDAdm = IDAdm;
        this.Name = Name;
        this.Email = Email;
        this.products = products;
        this.customers = customers;
    }

    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getLast_name() {
        return Last_name;
    }

    public void setLast_name(String Last_name) {
        this.Last_name = Last_name;
    }
    public int getIdadm() {
        return IDAdm;
    }

    public void setIdadm(int IDAdm) {
        this.IDAdm = IDAdm;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
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