





import java.util.List;
import java.util.ArrayList;

public class Contact  {

    private String phone;
    private String email;
    private String address;
    private String name;



    public Contact(
        String phone,        String email,        String address,        String name    ) {
        this.phone = phone;
        this.email = email;
        this.address = address;
        this.name = name;
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
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}