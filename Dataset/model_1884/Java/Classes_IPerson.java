





import java.util.List;
import java.util.ArrayList;

public class Classes_IPerson  {

    private String email;
    private String address;
    private String lastName;
    private String phoneNumber;
    private String firstName;



    public Classes_IPerson(
        String email,        String address,        String lastName,        String phoneNumber,        String firstName    ) {
        this.email = email;
        this.address = address;
        this.lastName = lastName;
        this.phoneNumber = phoneNumber;
        this.firstName = firstName;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }


}