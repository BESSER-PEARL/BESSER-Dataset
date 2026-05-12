





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String city;
    private String phone;
    private String email;
    private String name;
    private String address;



    public Customer(
        String city,        String phone,        String email,        String name,        String address    ) {
        this.city = city;
        this.phone = phone;
        this.email = email;
        this.name = name;
        this.address = address;
    }


    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}