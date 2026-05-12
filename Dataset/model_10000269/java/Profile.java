




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String city;
    private String country;
    private LocalDate dateOfBirth;
    private String email;
    private String userID;
    private int IDType;
    private String address1;
    private String IDNum;
    private String zipcode;
    private String address2;
    private String lastname;
    private String firstname;
    private String state;
    private String phoneNumber;





    private List<account_Account> account_accounts;




    private List<loan_LoanApplication> loan_loanapplications;


    public Profile(
        String city,        String country,        LocalDate dateOfBirth,        String email,        String userID,        int IDType,        String address1,        String IDNum,        String zipcode,        String address2,        String lastname,        String firstname,        String state,        String phoneNumber    ) {
        this.city = city;
        this.country = country;
        this.dateOfBirth = dateOfBirth;
        this.email = email;
        this.userID = userID;
        this.IDType = IDType;
        this.address1 = address1;
        this.IDNum = IDNum;
        this.zipcode = zipcode;
        this.address2 = address2;
        this.lastname = lastname;
        this.firstname = firstname;
        this.state = state;
        this.phoneNumber = phoneNumber;
        this.account_accounts = new ArrayList<>();
        this.loan_loanapplications = new ArrayList<>();
    }

    public Profile(
        String city,        String country,        LocalDate dateOfBirth,        String email,        String userID,        int IDType,        String address1,        String IDNum,        String zipcode,        String address2,        String lastname,        String firstname,        String state,        String phoneNumber        ArrayList<account_Account> account_accounts,        ArrayList<loan_LoanApplication> loan_loanapplications    ) {
        this.city = city;
        this.country = country;
        this.dateOfBirth = dateOfBirth;
        this.email = email;
        this.userID = userID;
        this.IDType = IDType;
        this.address1 = address1;
        this.IDNum = IDNum;
        this.zipcode = zipcode;
        this.address2 = address2;
        this.lastname = lastname;
        this.firstname = firstname;
        this.state = state;
        this.phoneNumber = phoneNumber;
        this.account_accounts = account_accounts;
        this.loan_loanapplications = loan_loanapplications;
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
    public LocalDate getDateofbirth() {
        return dateOfBirth;
    }

    public void setDateofbirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public int getIdtype() {
        return IDType;
    }

    public void setIdtype(int IDType) {
        this.IDType = IDType;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
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
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public List<account_Account> getAccount_accounts() {
        return account_accounts;
    }

    public void addAccount_account(Account_account account_account) {
        this.account_accounts.add(account_account);
    }
    public List<loan_LoanApplication> getLoan_loanapplications() {
        return loan_loanapplications;
    }

    public void addLoan_loanapplication(Loan_loanapplication loan_loanapplication) {
        this.loan_loanapplications.add(loan_loanapplication);
    }

}