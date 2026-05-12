





import java.util.List;
import java.util.ArrayList;

public class Vendedor  {

    private String email;
    private String address;
    private String phone;



    public Vendedor(
        String email,        String address,        String phone    ) {
        this.email = email;
        this.address = address;
        this.phone = phone;
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
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}