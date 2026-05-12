





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String Address;
    private String password;
    private int Id;
    private String email;
    private int phone;



    public User(
        String Address,        String password,        int Id,        String email,        int phone    ) {
        this.Address = Address;
        this.password = password;
        this.Id = Id;
        this.email = email;
        this.phone = phone;
    }


    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }


}