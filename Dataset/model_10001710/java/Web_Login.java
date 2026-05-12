





import java.util.List;
import java.util.ArrayList;

public class Web_Login  {

    private String login_id;
    private None verification;
    private String password;





    private Customer customer;




    private Cart cart;


    public Web_Login(
        String login_id,        None verification,        String password    ) {
        this.login_id = login_id;
        this.verification = verification;
        this.password = password;
    }


    public String getLogin_id() {
        return login_id;
    }

    public void setLogin_id(String login_id) {
        this.login_id = login_id;
    }
    public None getVerification() {
        return verification;
    }

    public void setVerification(None verification) {
        this.verification = verification;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Cart getCart() {
        return cart;
    }

    public void setCart(Cart cart) {
        this.cart = cart;
    }

}