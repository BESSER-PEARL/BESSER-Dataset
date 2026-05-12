





import java.util.List;
import java.util.ArrayList;

public class Applicant  {

    private String Last_Name;
    private String Email;
    private String Address;
    private String First_Name;
    private String Phone;
    private String Password;
    private String Date_of_Birth;
    private String Applied_Position;



    public Applicant(
        String Last_Name,        String Email,        String Address,        String First_Name,        String Phone,        String Password,        String Date_of_Birth,        String Applied_Position    ) {
        this.Last_Name = Last_Name;
        this.Email = Email;
        this.Address = Address;
        this.First_Name = First_Name;
        this.Phone = Phone;
        this.Password = Password;
        this.Date_of_Birth = Date_of_Birth;
        this.Applied_Position = Applied_Position;
    }


    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
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
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
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
    public String getDate_of_birth() {
        return Date_of_Birth;
    }

    public void setDate_of_birth(String Date_of_Birth) {
        this.Date_of_Birth = Date_of_Birth;
    }
    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
    }


}