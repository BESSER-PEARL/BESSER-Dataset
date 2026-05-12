





import java.util.List;
import java.util.ArrayList;

public class Registration  {

    private String LastName;
    private String Address;
    private int Phone;
    private String UserName;
    private String name;
    private String Email;
    private String DOB;
    private String Password;





    private Admin admin;


    public Registration(
        String LastName,        String Address,        int Phone,        String UserName,        String name,        String Email,        String DOB,        String Password    ) {
        this.LastName = LastName;
        this.Address = Address;
        this.Phone = Phone;
        this.UserName = UserName;
        this.name = name;
        this.Email = Email;
        this.DOB = DOB;
        this.Password = Password;
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
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}