





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String LastName;
    private String Address;
    private String Name;
    private int Phone;
    private String DOB;
    private String Email;





    private Registration registration;


    public Person(
        String LastName,        String Address,        String Name,        int Phone,        String DOB,        String Email    ) {
        this.LastName = LastName;
        this.Address = Address;
        this.Name = Name;
        this.Phone = Phone;
        this.DOB = DOB;
        this.Email = Email;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
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

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }

}