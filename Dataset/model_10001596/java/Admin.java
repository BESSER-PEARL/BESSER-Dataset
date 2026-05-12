





import java.util.List;
import java.util.ArrayList;

public class Admin  {

    private String userName;
    private int id;
    private String password;





    private Registration registration;




    private Product product;


    public Admin(
        String userName,        int id,        String password    ) {
        this.userName = userName;
        this.id = id;
        this.password = password;
    }


    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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