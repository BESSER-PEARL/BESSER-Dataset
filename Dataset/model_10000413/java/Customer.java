




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phoneNumber;
    private String emailAddress;
    private String name;
    private LocalDate dateOfBirth;
    private String address;



    public Customer(
        String phoneNumber,        String emailAddress,        String name,        LocalDate dateOfBirth,        String address    ) {
        this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.address = address;
    }


    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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


}