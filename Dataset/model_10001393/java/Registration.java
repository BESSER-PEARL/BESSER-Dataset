





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String LastName;
    private String Address;
    private String Password;
    private String DOB;
    private String Email;
    private String name;
    private String UserName;
    private int Phone;



    public Registration(
        String LastName,        String Address,        String Password,        String DOB,        String Email,        String name,        String UserName,        int Phone    ) {
        this.LastName = LastName;
        this.Address = Address;
        this.Password = Password;
        this.DOB = DOB;
        this.Email = Email;
        this.name = name;
        this.UserName = UserName;
        this.Phone = Phone;
    }


    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }


}