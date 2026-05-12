





import java.util.List;
import java.util.ArrayList;

public class CompanyAddRider  {

    private String Email;
    private String Name;
    private String Address;
    private String UserName;
    private String Phone;
    private String Password;
    private int CNIC;



    public CompanyAddRider(
        String Email,        String Name,        String Address,        String UserName,        String Phone,        String Password,        int CNIC    ) {
        this.Email = Email;
        this.Name = Name;
        this.Address = Address;
        this.UserName = UserName;
        this.Phone = Phone;
        this.Password = Password;
        this.CNIC = CNIC;
    }


    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getPassword() {
        return Password;
    }

    public void setPassword(String Password) {
        this.Password = Password;
    }
    public int getCnic() {
        return CNIC;
    }

    public void setCnic(int CNIC) {
        this.CNIC = CNIC;
    }


}