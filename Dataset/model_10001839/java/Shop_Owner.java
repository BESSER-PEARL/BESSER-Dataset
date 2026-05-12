





import java.util.List;
import java.util.ArrayList;

public class Shop_Owner  {

    private String Name;
    private String Last_name;
    private String Email;
    private int IDSowner;
    private String Password;





    private Administrator administrator;




    private List<Product> products;




    private List<Product> products;


    public Shop_Owner(
        String Name,        String Last_name,        String Email,        int IDSowner,        String Password    ) {
        this.Name = Name;
        this.Last_name = Last_name;
        this.Email = Email;
        this.IDSowner = IDSowner;
        this.Password = Password;
        this.products = new ArrayList<>();
        this.products = new ArrayList<>();
    }

    public Shop_Owner(
        String Name,        String Last_name,        String Email,        int IDSowner,        String Password        ArrayList<Product> products,        ArrayList<Product> products    ) {
        this.Name = Name;
        this.Last_name = Last_name;
        this.Email = Email;
        this.IDSowner = IDSowner;
        this.Password = Password;
        this.products = products;
        this.products = products;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getLast_name() {
        return Last_name;
    }

    public void setLast_name(String Last_name) {
        this.Last_name = Last_name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public int getIdsowner() {
        return IDSowner;
    }

    public void setIdsowner(int IDSowner) {
        this.IDSowner = IDSowner;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
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
    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}