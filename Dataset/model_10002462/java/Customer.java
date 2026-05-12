




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private LocalDate dateOfBirth;
    private String address;
    private String name;
    private String phoneNumber;



    public Customer(
        String emailAddress,        LocalDate dateOfBirth,        String address,        String name,        String phoneNumber    ) {
        this.emailAddress = emailAddress;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
        this.name = name;
        this.phoneNumber = phoneNumber;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }


}