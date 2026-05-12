





import java.util.List;
import java.util.ArrayList;

public class New_Customer  {

    private String password;
    private String Name;
    private String email;
    private String address;
    private String phone;



    public New_Customer(
        String password,        String Name,        String email,        String address,        String phone    ) {
        this.password = password;
        this.Name = Name;
        this.email = email;
        this.address = address;
        this.phone = phone;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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