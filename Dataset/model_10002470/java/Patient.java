




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String name;
    private LocalDate dateOfBirth;
    private String GP_Address;
    private String emailAddress;
    private String phoneNumber;
    private String address;



    public Patient(
        String name,        LocalDate dateOfBirth,        String GP_Address,        String emailAddress,        String phoneNumber,        String address    ) {
        this.name = name;
        this.dateOfBirth = dateOfBirth;
        this.GP_Address = GP_Address;
        this.emailAddress = emailAddress;
        this.phoneNumber = phoneNumber;
        this.address = address;
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
    public String getGp_address() {
        return GP_Address;
    }

    public void setGp_address(String GP_Address) {
        this.GP_Address = GP_Address;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}