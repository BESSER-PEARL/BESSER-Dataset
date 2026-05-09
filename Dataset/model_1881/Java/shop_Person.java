




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class shop_Person  {

    private String address;
    private String emails;
    private LocalDate birthDate;
    private String phoneNumbers;
    private String firstName;
    private String lastName;



    public shop_Person(
        String address,        String emails,        LocalDate birthDate,        String phoneNumbers,        String firstName,        String lastName    ) {
        this.address = address;
        this.emails = emails;
        this.birthDate = birthDate;
        this.phoneNumbers = phoneNumbers;
        this.firstName = firstName;
        this.lastName = lastName;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmails() {
        return emails;
    }

    public void setEmails(String emails) {
        this.emails = emails;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public String getPhonenumbers() {
        return phoneNumbers;
    }

    public void setPhonenumbers(String phoneNumbers) {
        this.phoneNumbers = phoneNumbers;
    }
    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getLastname() {
        return lastName;
    }

    public void setLastname(String lastName) {
        this.lastName = lastName;
    }


}