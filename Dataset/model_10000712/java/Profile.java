




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String email;
    private String state;
    private int IDType;
    private String country;
    private String phoneNumber;
    private String firstname;
    private String address2;
    private String address1;
    private String userID;
    private String lastname;
    private String IDNum;
    private String zipcode;
    private LocalDate dateOfBirth;
    private String city;



    public Profile(
        String email,        String state,        int IDType,        String country,        String phoneNumber,        String firstname,        String address2,        String address1,        String userID,        String lastname,        String IDNum,        String zipcode,        LocalDate dateOfBirth,        String city    ) {
        this.email = email;
        this.state = state;
        this.IDType = IDType;
        this.country = country;
        this.phoneNumber = phoneNumber;
        this.firstname = firstname;
        this.address2 = address2;
        this.address1 = address1;
        this.userID = userID;
        this.lastname = lastname;
        this.IDNum = IDNum;
        this.zipcode = zipcode;
        this.dateOfBirth = dateOfBirth;
        this.city = city;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public int getIdtype() {
        return IDType;
    }

    public void setIdtype(int IDType) {
        this.IDType = IDType;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
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
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
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
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }


}