





import java.util.List;
import java.util.ArrayList;

public class New_Customer  {

    private String address;
    private String Name;
    private String password;
    private String email;
    private String phone;



    public New_Customer(
        String address,        String Name,        String password,        String email,        String phone    ) {
        this.address = address;
        this.Name = Name;
        this.password = password;
        this.email = email;
        this.phone = phone;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }


}