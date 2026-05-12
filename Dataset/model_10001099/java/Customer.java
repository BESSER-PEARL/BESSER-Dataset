




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String emailAddress;
    private String address;
    private LocalDate dateOfBirth;
    private String name;
    private String phoneNumber;



    public Customer(
        String emailAddress,        String address,        LocalDate dateOfBirth,        String name,        String phoneNumber    ) {
        this.emailAddress = emailAddress;
        this.address = address;
        this.dateOfBirth = dateOfBirth;
        this.name = name;
        this.phoneNumber = phoneNumber;
    }


    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
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