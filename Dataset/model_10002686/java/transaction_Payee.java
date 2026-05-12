





import java.util.List;
import java.util.ArrayList;

public class transaction_Payee  {

    private String name;
    private String accountNum;
    private String address1;
    private String address2;
    private String phoneNum;
    private String state;
    private String city;
    private String email;
    private String zipcode;
    private String country;



    public transaction_Payee(
        String name,        String accountNum,        String address1,        String address2,        String phoneNum,        String state,        String city,        String email,        String zipcode,        String country    ) {
        this.name = name;
        this.accountNum = accountNum;
        this.address1 = address1;
        this.address2 = address2;
        this.phoneNum = phoneNum;
        this.state = state;
        this.city = city;
        this.email = email;
        this.zipcode = zipcode;
        this.country = country;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccountnum() {
        return accountNum;
    }

    public void setAccountnum(String accountNum) {
        this.accountNum = accountNum;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }
    public String getAddress2() {
        return address2;
    }

    public void setAddress2(String address2) {
        this.address2 = address2;
    }
    public String getPhonenum() {
        return phoneNum;
    }

    public void setPhonenum(String phoneNum) {
        this.phoneNum = phoneNum;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getZipcode() {
        return zipcode;
    }

    public void setZipcode(String zipcode) {
        this.zipcode = zipcode;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }


}