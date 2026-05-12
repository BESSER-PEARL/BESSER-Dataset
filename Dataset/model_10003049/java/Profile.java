




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String lastname;
    private String IDNum;
    private String state;
    private String email;
    private int IDType;
    private String firstname;
    private String userID;
    private String city;
    private String country;
    private String address2;
    private LocalDate dateOfBirth;
    private String phoneNumber;
    private String address1;
    private String zipcode;



    public Profile(
        String lastname,        String IDNum,        String state,        String email,        int IDType,        String firstname,        String userID,        String city,        String country,        String address2,        LocalDate dateOfBirth,        String phoneNumber,        String address1,        String zipcode    ) {
        this.lastname = lastname;
        this.IDNum = IDNum;
        this.state = state;
        this.email = email;
        this.IDType = IDType;
        this.firstname = firstname;
        this.userID = userID;
        this.city = city;
        this.country = country;
        this.address2 = address2;
        this.dateOfBirth = dateOfBirth;
        this.phoneNumber = phoneNumber;
        this.address1 = address1;
        this.zipcode = zipcode;
    }


    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getIdnum() {
        return IDNum;
    }

    public void setIdnum(String IDNum) {
        this.IDNum = IDNum;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getIdtype() {
        return IDType;
    }

    public void setIdtype(int IDType) {
        this.IDType = IDType;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }


}