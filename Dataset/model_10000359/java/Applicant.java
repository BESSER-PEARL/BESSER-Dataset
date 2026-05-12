





import java.util.List;
import java.util.ArrayList;

public class Applicant  {

    private String Applied_Position;
    private String First_Name;
    private String Password;
    private String Date_of_Birth;
    private String Phone;
    private String Last_Name;
    private String Address;
    private String Email;



    public Applicant(
        String Applied_Position,        String First_Name,        String Password,        String Date_of_Birth,        String Phone,        String Last_Name,        String Address,        String Email    ) {
        this.Applied_Position = Applied_Position;
        this.First_Name = First_Name;
        this.Password = Password;
        this.Date_of_Birth = Date_of_Birth;
        this.Phone = Phone;
        this.Last_Name = Last_Name;
        this.Address = Address;
        this.Email = Email;
    }


    public String getApplied_position() {
        return Applied_Position;
    }

    public void setApplied_position(String Applied_Position) {
        this.Applied_Position = Applied_Position;
    }
    public String getFirst_name() {
        return First_Name;
    }

    public void setFirst_name(String First_Name) {
        this.First_Name = First_Name;
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
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }
    public String getLast_name() {
        return Last_Name;
    }

    public void setLast_name(String Last_Name) {
        this.Last_Name = Last_Name;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }


}