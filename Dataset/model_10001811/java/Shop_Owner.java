





import java.util.List;
import java.util.ArrayList;

public class Shop_Owner  {

    private String Last_name;
    private String Password;
    private int IDSowner;
    private String Name;
    private String Email;





    private List<Product> products;




    private Administrator administrator;




    private List<Product> products;


    public Shop_Owner(
        String Last_name,        String Password,        int IDSowner,        String Name,        String Email    ) {
        this.Last_name = Last_name;
        this.Password = Password;
        this.IDSowner = IDSowner;
        this.Name = Name;
        this.Email = Email;
        this.products = new ArrayList<>();
        this.products = new ArrayList<>();
    }

    public Shop_Owner(
        String Last_name,        String Password,        int IDSowner,        String Name,        String Email        ArrayList<Product> products,        ArrayList<Product> products    ) {
        this.Last_name = Last_name;
        this.Password = Password;
        this.IDSowner = IDSowner;
        this.Name = Name;
        this.Email = Email;
        this.products = products;
        this.products = products;
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
    public int getIdsowner() {
        return IDSowner;
    }

    public void setIdsowner(int IDSowner) {
        this.IDSowner = IDSowner;
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
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}