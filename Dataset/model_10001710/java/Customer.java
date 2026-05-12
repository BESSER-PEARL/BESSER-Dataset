





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String id_;
    private String email;
    private String address;
    private int phone;



    public Customer(
        String id_,        String email,        String address,        int phone    ) {
        this.id_ = id_;
        this.email = email;
        this.address = address;
        this.phone = phone;
    }


    public String getId_() {
        return id_;
    }

    public void setId_(String id_) {
        this.id_ = id_;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }


}