





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String DOB;
    private int Phone;
    private String LastName;
    private String Address;
    private String Email;
    private String Name;





    private Registration registration;


    public Person(
        String DOB,        int Phone,        String LastName,        String Address,        String Email,        String Name    ) {
        this.DOB = DOB;
        this.Phone = Phone;
        this.LastName = LastName;
        this.Address = Address;
        this.Email = Email;
        this.Name = Name;
    }


    public String getDob() {
        return DOB;
    }

    public void setDob(String DOB) {
        this.DOB = DOB;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
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

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }

}