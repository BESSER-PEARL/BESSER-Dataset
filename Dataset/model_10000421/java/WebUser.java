





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String password;
    private String email;
    private String status;
    private boolean fblogin;
    private int id;





    private ShoppingCart shoppingcart;




    private Customer customer;


    public WebUser(
        String password,        String email,        String status,        boolean fblogin,        int id    ) {
        this.password = password;
        this.email = email;
        this.status = status;
        this.fblogin = fblogin;
        this.id = id;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public boolean getFblogin() {
        return fblogin;
    }

    public void setFblogin(boolean fblogin) {
        this.fblogin = fblogin;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}