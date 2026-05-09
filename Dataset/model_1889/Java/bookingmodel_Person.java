





import java.util.List;
import java.util.ArrayList;

public class bookingmodel_Person  {

    private String lastName;
    private String telephoneNr;
    private String firstName;
    private String email;
    private String Address;
    private String age;



    public bookingmodel_Person(
        String lastName,        String telephoneNr,        String firstName,        String email,        String Address,        String age    ) {
        this.lastName = lastName;
        this.telephoneNr = telephoneNr;
        this.firstName = firstName;
        this.email = email;
        this.Address = Address;
        this.age = age;
    }


    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }
    public String getTelephonenr() {
        return telephoneNr;
    }

    public void setTelephonenr(String telephoneNr) {
        this.telephoneNr = telephoneNr;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }


}