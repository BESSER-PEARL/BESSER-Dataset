





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String password;
    private String login;
    private None state;





    private ShoppinCart shoppincart;




    private Customer customer;


    public WebUser(
        String password,        String login,        None state    ) {
        this.password = password;
        this.login = login;
        this.state = state;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }

    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}