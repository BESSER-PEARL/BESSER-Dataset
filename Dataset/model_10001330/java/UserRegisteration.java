





import java.util.List;
import java.util.ArrayList;

public class UserRegisteration  {

    private String Email;
    private String Address;
    private String UserName;
    private String FirstName;
    private String LastName;
    private String Password;
    private String Phone;



    public UserRegisteration(
        String Email,        String Address,        String UserName,        String FirstName,        String LastName,        String Password,        String Phone    ) {
        this.Email = Email;
        this.Address = Address;
        this.UserName = UserName;
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.Password = Password;
        this.Phone = Phone;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getUsername() {
        return UserName;
    }

    public void setUsername(String UserName) {
        this.UserName = UserName;
    }
    public String getFirstname() {
        return FirstName;
    }

    public void setFirstname(String FirstName) {
        this.FirstName = FirstName;
    }
    public String getLastname() {
        return LastName;
    }

    public void setLastname(String LastName) {
        this.LastName = LastName;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }


}