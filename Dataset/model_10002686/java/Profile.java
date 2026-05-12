




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String firstname;
    private String phoneNumber;
    private String IDNum;
    private String country;
    private String state;
    private String zipcode;
    private String lastname;
    private String userID;
    private String email;
    private String city;
    private LocalDate dateOfBirth;
    private int IDType;
    private String address2;
    private String address1;



    public Profile(
        String firstname,        String phoneNumber,        String IDNum,        String country,        String state,        String zipcode,        String lastname,        String userID,        String email,        String city,        LocalDate dateOfBirth,        int IDType,        String address2,        String address1    ) {
        this.firstname = firstname;
        this.phoneNumber = phoneNumber;
        this.IDNum = IDNum;
        this.country = country;
        this.state = state;
        this.zipcode = zipcode;
        this.lastname = lastname;
        this.userID = userID;
        this.email = email;
        this.city = city;
        this.dateOfBirth = dateOfBirth;
        this.IDType = IDType;
        this.address2 = address2;
        this.address1 = address1;
    }


    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getIdnum() {
        return IDNum;
    }

    public void setIdnum(String IDNum) {
        this.IDNum = IDNum;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public int getIdtype() {
        return IDType;
    }

    public void setIdtype(int IDType) {
        this.IDType = IDType;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }


}