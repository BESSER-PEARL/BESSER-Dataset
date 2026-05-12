





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private int id;
    private String userName;
    private String password;





    private Registration registration;




    private Product product;


    public Admin(
        int id,        String userName,        String password    ) {
        this.id = id;
        this.userName = userName;
        this.password = password;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}