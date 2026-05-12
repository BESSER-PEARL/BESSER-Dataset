





import java.util.List;
import java.util.ArrayList;

public class WebUser  {

    private String password;
    private None state;
    private String login;





    private Customer customer;




    private ShoppinCart shoppincart;


    public WebUser(
        String password,        None state,        String login    ) {
        this.password = password;
        this.state = state;
        this.login = login;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public None getState() {
        return state;
    }

    public void setState(None state) {
        this.state = state;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public ShoppinCart getShoppincart() {
        return shoppincart;
    }

    public void setShoppincart(ShoppinCart shoppincart) {
        this.shoppincart = shoppincart;
    }

}