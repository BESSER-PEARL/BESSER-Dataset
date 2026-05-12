





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phone;
    private String email;



    public Customer(
        String phone,        String email    ) {
        this.phone = phone;
        this.email = email;
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