





import java.util.List;
import java.util.ArrayList;

public class Login  {

    private String login_id_;
    private String password_;





    private Customer customer;


    public Login(
        String login_id_,        String password_    ) {
        this.login_id_ = login_id_;
        this.password_ = password_;
    }


    public String getLogin_id_() {
        return login_id_;
    }

    public void setLogin_id_(String login_id_) {
        this.login_id_ = login_id_;
    }
    public String getPassword_() {
        return password_;
    }

    public void setPassword_(String password_) {
        this.password_ = password_;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}