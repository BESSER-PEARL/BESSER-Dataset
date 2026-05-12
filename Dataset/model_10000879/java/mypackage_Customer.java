




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class mypackage_Customer  {

    private String address;
    private String lastname;
    private String name;
    private String phoneNumber;
    private String emailAddress;
    private LocalDate dateOfBirth;





    private mypackage_Login mypackage_login;


    public mypackage_Customer(
        String address,        String lastname,        String name,        String phoneNumber,        String emailAddress,        LocalDate dateOfBirth    ) {
        this.address = address;
        this.lastname = lastname;
        this.name = name;
        this.phoneNumber = phoneNumber;
        this.emailAddress = emailAddress;
        this.dateOfBirth = dateOfBirth;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
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

    public mypackage_Login getMypackage_login() {
        return mypackage_login;
    }

    public void setMypackage_login(mypackage_Login mypackage_login) {
        this.mypackage_login = mypackage_login;
    }

}