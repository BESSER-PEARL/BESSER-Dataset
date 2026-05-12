





import java.util.List;
import java.util.ArrayList;

public class SinhVien  {

    private None state;
    private String password;
    private String login;





    private Customer customer;


    public SinhVien(
        None state,        String password,        String login    ) {
        this.state = state;
        this.password = password;
        this.login = login;
    }


    public None getState() {
        return state;
    }

    public void setState(None state) {
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

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}