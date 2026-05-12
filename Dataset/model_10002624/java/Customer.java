





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private int postal_code;
    private String address;
    private String UserName;
    private String country;
    private String password;



    public Customer(
        int postal_code,        String address,        String UserName,        String country,        String password    ) {
        this.postal_code = postal_code;
        this.address = address;
        this.UserName = UserName;
        this.country = country;
        this.password = password;
    }


    public int getPostal_code() {
        return postal_code;
    }

    public void setPostal_code(int postal_code) {
        this.postal_code = postal_code;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}