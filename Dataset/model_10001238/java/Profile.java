




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String city;
    private String phoneNumber;
    private String userID;
    private LocalDate dateOfBirth;
    private String zipcode;
    private String address2;
    private String lastname;
    private int IDType;
    private String state;
    private String country;
    private String address1;
    private String email;
    private String IDNum;
    private String firstname;





    private List<account_Account> account_accounts;


    public Profile(
        String city,        String phoneNumber,        String userID,        LocalDate dateOfBirth,        String zipcode,        String address2,        String lastname,        int IDType,        String state,        String country,        String address1,        String email,        String IDNum,        String firstname    ) {
        this.city = city;
        this.phoneNumber = phoneNumber;
        this.userID = userID;
        this.dateOfBirth = dateOfBirth;
        this.zipcode = zipcode;
        this.address2 = address2;
        this.lastname = lastname;
        this.IDType = IDType;
        this.state = state;
        this.country = country;
        this.address1 = address1;
        this.email = email;
        this.IDNum = IDNum;
        this.firstname = firstname;
        this.account_accounts = new ArrayList<>();
    }

    public Profile(
        String city,        String phoneNumber,        String userID,        LocalDate dateOfBirth,        String zipcode,        String address2,        String lastname,        int IDType,        String state,        String country,        String address1,        String email,        String IDNum,        String firstname        ArrayList<account_Account> account_accounts    ) {
        this.city = city;
        this.phoneNumber = phoneNumber;
        this.userID = userID;
        this.dateOfBirth = dateOfBirth;
        this.zipcode = zipcode;
        this.address2 = address2;
        this.lastname = lastname;
        this.IDType = IDType;
        this.state = state;
        this.country = country;
        this.address1 = address1;
        this.email = email;
        this.IDNum = IDNum;
        this.firstname = firstname;
        this.account_accounts = account_accounts;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public int getIdtype() {
        return IDType;
    }

    public void setIdtype(int IDType) {
        this.IDType = IDType;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getIdnum() {
        return IDNum;
    }

    public void setIdnum(String IDNum) {
        this.IDNum = IDNum;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }

}