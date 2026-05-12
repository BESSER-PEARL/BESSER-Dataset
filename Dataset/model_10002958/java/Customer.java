





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String login_id_;
    private int Phone_;
    private String Address_;



    public Customer(
        String login_id_,        int Phone_,        String Address_    ) {
        this.login_id_ = login_id_;
        this.Phone_ = Phone_;
        this.Address_ = Address_;
    }


    public String getLogin_id_() {
        return login_id_;
    }

    public void setLogin_id_(String login_id_) {
        this.login_id_ = login_id_;
    }
    public int getPhone_() {
        return Phone_;
    }

    public void setPhone_(int Phone_) {
        this.Phone_ = Phone_;
    }
    public String getAddress_() {
        return Address_;
    }

    public void setAddress_(String Address_) {
        this.Address_ = Address_;
    }


}