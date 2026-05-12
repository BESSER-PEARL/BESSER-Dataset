





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String address;
    private String phone;
    private String email;



    public Customer(
        String address,        String phone,        String email    ) {
        this.address = address;
        this.phone = phone;
        this.email = email;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}